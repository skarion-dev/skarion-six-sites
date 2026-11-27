"""Deterministic drafting-business stress tests. No customer outcomes are simulated as facts.

Run with Python 3. Outputs assumptions and aggregated results to stress_test_results.json.
All USD cost/conversion inputs are hypothetical until replaced with Skarion observations.
Grid outcome shares are sensitivity coverage, never empirical success probabilities.
"""
from itertools import product
from collections import defaultdict
from math import comb, ceil, isclose, log
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def job(price, hours, labor, rework, review_fraction, reviewer, pm_hours, fee, acquisition):
    delivery = hours * (1 + rework) * labor + hours * review_fraction * reviewer + pm_hours * 20
    return {'delivery_cost': delivery, 'contribution': price * (1 - fee) - delivery,
            'after_acquisition': price * (1 - fee) - delivery - acquisition}

def month(rate, capacity, sold, labor, rework, review_fraction, reviewer, fee, overhead):
    production = sold * (1 + rework)
    review_hours = sold * review_fraction
    pm_hours = sold * .1
    costs = capacity * labor + review_hours * reviewer + pm_hours * 20 + 150 + overhead
    return {'profit': sold * rate * (1-fee) - costs,
            'cost_before_fees': costs,
            'technical_feasible': production <= capacity + 1e-9 and review_hours <= 40 and pm_hours <= 20,
            'safe_feasible': production <= capacity * .8 + 1e-9 and review_hours <= 40 and pm_hours <= 20}

def binom_tail(n, k, p):
    if k <= 0: return 1.0
    if k > n: return 0.0
    return sum(comb(n, x) * p**x * (1-p)**(n-x) for x in range(k, n+1))

def cohort(price, labor, trial_hours, acquisition_per_trial, conversion, repeat_rate, blocks):
    # 10 completed trials. 25% trial rework, 0.5 reviewer hours and 0.25 PM hours each.
    trial_delivery = trial_hours * 1.25 * labor + .5 * 20 + .25 * 20
    trial_loss = 10 * (trial_delivery + acquisition_per_trial - price*.97) + 100
    # Each repeat block: 20 sold hours, 10% drafting rework, 4 review and 2 PM hours.
    # $25/block overhead allocation. No idle reserved capacity charged in this model.
    block_contribution = 20 * repeat_rate * .97 - (22*labor + 4*20 + 2*20 + 25)
    if trial_loss <= 0:
        needed_clients, threshold = 0, 0.0
    elif block_contribution <= 0:
        needed_clients, threshold = None, None
    else:
        needed_clients = ceil(trial_loss / (blocks * block_contribution) - 1e-12)
        threshold = trial_loss / (10 * blocks * block_contribution)
    # Direct enumeration also handles profitable entry offers followed by loss-making work.
    probability = sum(comb(10,k)*conversion**k*(1-conversion)**(10-k)
                      for k in range(11) if k*blocks*block_contribution >= trial_loss-1e-9)
    return {'trial_delivery_each':trial_delivery, 'trial_loss':trial_loss,
            'repeat_block_contribution':block_contribution,
            'needed_repeat_clients':needed_clients,
            'expected_conversion_break_even':threshold,
            'expected_result':10*conversion*blocks*block_contribution-trial_loss,
            'payback_probability_conditional_on_inputs':probability}

def funnel(n, response, accept, repeat, research_minutes, price, repeat_rate, blocks, labor=10):
    trials = n * response * accept
    clients = trials * repeat
    prospect_cost = n * research_minutes / 60 * 15
    discovery_cost = n * response * .25 * 15
    delivery_cost = trials * (1.875*labor+15)
    block_contribution = repeat_rate * 20 * .97 - (22*labor+145)
    result = trials*price*.97 + clients*blocks*block_contribution - prospect_cost - discovery_cost - delivery_cost - 100
    p = response * accept * repeat
    return {'expected_trials':trials,'expected_repeat_clients':clients,
            'sales_labor_cost':prospect_cost+discovery_cost,
            'expected_result':result,
            'probability_at_least_one_repeat':1-(1-p)**n,
            'probability_at_least_two_repeat':1-(1-p)**n-n*p*(1-p)**(n-1)}

def validate():
    # Independent hand-calculated reference cases and economic invariants.
    assert isclose(job(175,4,10,.25,.25,20,.5,.1,0)['contribution'],77.5)
    assert isclose(month(25,80,56,6,.1,.2,20,.1,100)['profit'],194)
    assert isclose(month(25,80,56,10,.1,.2,20,.1,100)['profit'],-126)
    assert month(40,80,80,4,.1,.1,15,.03,100)['safe_feasible'] is False
    assert isclose(cohort(0,10,1.5,15,.2,25,1)['trial_loss'],587.5)
    assert isclose(cohort(0,10,1.5,15,.2,25,1)['repeat_block_contribution'],120)
    assert cohort(0,10,1.5,15,.2,25,1)['needed_repeat_clients']==5
    assert cohort(0,10,1.5,15,.2,25,3)['needed_repeat_clients']==2
    assert isclose(binom_tail(10,1,.2),1-.8**10)
    assert binom_tail(10,11,.5)==0
    assert cohort(0,20,1.5,15,.5,10,3)['needed_repeat_clients'] is None
    assert cohort(99,10,1.5,15,0,25,1)['needed_repeat_clients']==0
    assert isclose(funnel(100,.1,.5,.2,10,0,25,1)['expected_repeat_clients'],1)
    for rate in [10,20,30]:
        a=month(rate,80,40,8,.1,.2,20,.1,100)
        b=month(rate+1,80,40,8,.1,.2,20,.1,100)
        assert isclose(b['profit']-a['profit'],36)
    assert cohort(99,10,1.5,15,1,10,6)['payback_probability_conditional_on_inputs']==0
    return 'Reference cases and economic invariants passed'

def run():
    results={'date':'2026-11-12','validation':validate(),
      'caveat':'Exhaustive enumeration over specified discrete assumptions, not real sales or CAD delivery tests. Grid pass rates are not success probabilities.',
      'common':{'currency':'USD','pm_hourly_cost':20,'sales_hourly_cost':15,
        'actual_costs_confirmed':False,'taxes_included':False,
        'one_time_launch_costs_included_in_monthly_grid':False,
        'new_external_messages_sent':False}}
    grid={'price':[0,10,25,49,75,99,149,175,250,350],
          'production_hours':[.5,1,1.5,2,3,4,6,8,12],
          'drafter_cost':[2,2.5,3,4,6,8,10,12,15,20],
          'rework':[0,.1,.25,.5,1], 'review_fraction':[.1,.25,.5],
          'reviewer_cost':[10,15,20,30], 'pm_hours':[.25,.5,1],
          'fee':[0,.03,.1,.15], 'acquisition_cost_per_job':[0,10,25,50]}
    stats=defaultdict(lambda:{'tested':0,'positive_delivery_contribution':0,'positive_after_acquisition':0,'worst_after_acquisition':float('inf'),'best_after_acquisition':-float('inf')})
    count=0
    for params in product(*grid.values()):
        price=params[0]; v=job(*params); s=stats[str(price)]; count+=1
        s['tested']+=1; s['positive_delivery_contribution']+=v['contribution']>0
        s['positive_after_acquisition']+=v['after_acquisition']>0
        s['worst_after_acquisition']=min(s['worst_after_acquisition'],v['after_acquisition'])
        s['best_after_acquisition']=max(s['best_after_acquisition'],v['after_acquisition'])
    results['fixed_jobs']={'grid':grid,'count':count,'by_price':dict(stats)}

    grid={'hourly_rate':[5,8,10,12,15,18,20,22,25,28,30,32,35,40],
          'paid_capacity':[80,160],'sold_hours':[10,20,30,40,60,80,100,120,140,160],
          'drafter_cost':[2,2.5,3,4,6,8,10,12,15,20],'rework':[0,.1,.25,.5],
          'review_fraction':[.1,.2,.3],'reviewer_cost':[15,25],
          'fee':[.03,.1,.15],'overhead':[100,300,600]}
    count=technical=safe=positive=0
    by_rate=defaultdict(lambda:{'tested':0,'safe_feasible':0,'safe_and_profitable':0})
    for params in product(*grid.values()):
        v=month(*params);count+=1;technical+=v['technical_feasible'];safe+=v['safe_feasible']
        good=v['safe_feasible'] and v['profit']>0; positive+=good
        s=by_rate[str(params[0])];s['tested']+=1;s['safe_feasible']+=v['safe_feasible'];s['safe_and_profitable']+=good
    results['monthly']={'grid':grid,'count':count,'technical_feasible':technical,
      'safe_feasible':safe,'safe_and_profitable':positive,'by_rate':dict(by_rate),
      'other_assumptions':{'reviewer_capacity_hours':40,'pm_capacity_hours':20,
      'pm_hours_per_sold_hour':.1,'monthly_sales_labor':150,'drafter_capacity_reserve':.2}}

    grid={'entry_price':[0,10,25,49,75,99,175],'drafter_cost':[2,2.5,3,4,6,8,10,15,20],
          'trial_production_hours':[.5,1.5,3,6], 'acquisition_per_completed_trial':[0,15,50,150],
          'trial_to_repeat_conversion':[.05,.1,.2,.3,.5,.75],
          'repeat_hourly_rate':[10,15,20,25,30], 'repeat_blocks_per_converted_client':[1,2,3,6]}
    count=positive=unrecoverable=0
    for params in product(*grid.values()):
        v=cohort(*params);count+=1;positive+=v['expected_result']>0
        unrecoverable+=v['needed_repeat_clients'] is None or (v['needed_repeat_clients'] or 0)>10
    results['trial_cohorts']={'grid':grid,'count':count,'positive_expected_result':positive,
       'cannot_recover_within_ten_clients_and_selected_blocks':unrecoverable,
       'other_assumptions':{'cohort_size':10,'trial_rework':.25,'review_hours_per_trial':.5,
       'pm_hours_per_trial':.25,'reviewer_cost':20,'fee':.03,'cohort_overhead':100,
       'block_hours':20,'repeat_rework':.1,'review_hours_per_block':4,
       'pm_hours_per_block':2,'overhead_per_repeat_block':25,
       'idle_reserved_labor_included':False,
       'price_response_relationship':'not assumed; acceptance and retention must be measured'}}

    grid={'qualified_contacts':[30,60,100,200,500], 'response_rate':[.01,.02,.05,.1,.2],
          'trial_acceptance_among_responses':[.1,.25,.5,.75],
          'repeat_conversion_among_trials':[.05,.1,.2,.3,.5],
          'research_minutes_per_contact':[5,10,20], 'entry_price':[0,25,49,99],
          'repeat_rate':[20,25,30],'repeat_blocks':[1,3]}
    count=positive=0
    for params in product(*grid.values()):
        v=funnel(*params);count+=1;positive+=v['expected_result']>0
    results['funnel']={'grid':grid,'count':count,'positive_expected_result':positive,
      'other_assumptions':{'sales_hourly_cost':15,'discovery_hours_per_response':.25,
      'delivery_cost_per_trial':33.75,'cohort_overhead':100,'fee':.03,
      'cost_per_repeat_block_including_overhead':365,'capacity_limits':'not enforced; this module isolates sales economics'}}

    # Recalibration after the user supplied actual approximate monthly drafter cost.
    # Charge the entire monthly cost even when only some hours are available/sold.
    grid={'bdt_per_usd':[115,124.75,135],'cost_uplift':[0,.25,.5],
          'available_drafter_hours':[40,80,160],'sold_hours':[10,20,40,56,80,100,112,120,140,160],
          'selling_rate':[5,8,10,12,15,18,20,25,30,32],'reviewer_cost':[3,6,10,20],
          'review_fraction':[.1,.2,.3],'fee':[.03,.1,.15],
          'overhead':[100,300,600],'rework':[.1,.25,.5]}
    count=safe=positive=0
    for fx,uplift,capacity,hours,rate,qc,qfrac,fee,overhead,rework in product(*grid.values()):
        cost=40000/fx*(1+uplift)+hours*qfrac*qc+hours*.1*20+150+overhead
        feasible=hours*(1+rework)<=capacity*.8+1e-9 and hours*qfrac<=40 and hours*.1<=20
        count+=1;safe+=feasible;positive+=feasible and hours*rate*(1-fee)>cost
    usd=40000/124.75; labor=usd/160
    actual_months=[]
    for hours,rate,qc,uplift in product([56,112],[10,15,20,25],[6,20],[0,.25]):
        cost=usd*(1+uplift)+hours*.2*qc+hours*.1*20+150+100
        actual_months.append({'sold_hours':hours,'rate':rate,'reviewer_cost':qc,'uplift':uplift,
          'full_monthly_drafter_cost':usd*(1+uplift),'total_cost_before_fees':cost,
          'profit':hours*rate*.9-cost})
    sample_cost=1.875*labor+15; full_cost=5*labor+30
    results['user_calibrated']={'grid':grid,'count':count,'safe_feasible':safe,
      'safe_and_profitable':positive,'reported_drafter_monthly_bdt':40000,
      'reference_fx':124.75,'fx_source':'https://www.bb.org.bd/en/index.php/econdata/exchangerate',
      'monthly_usd':usd,'assumed_paid_hours_for_hourly_conversion':160,
      'hourly_usd':labor,'all_in_cost_and_availability_confirmed':False,
      'monthly_scenarios':actual_months,
      'sample_delivery_cost':sample_cost,'full_pilot_delivery_cost':full_cost,
      'entry_contributions':[{'price':p,'sample_contribution':p*.97-sample_cost,
          'full_pilot_contribution':p*.97-full_cost} for p in [0,25,49,99]],
      'trial_payback':[dict(price=p,blocks=b,**cohort(p,labor,1.5,15,.2,20,b)) for p in [0,25,49,99] for b in [1,3]],
      'free_repeat_rates':[dict(rate=r,**cohort(0,labor,1.5,15,.2,r,3)) for r in [10,15,20,25]],
      'cold_funnel':[dict(price=p,**funnel(200,.1,.5,.2,10,p,20,3,labor)) for p in [0,25,49]],
      'sensitivity_boundary':'Reviewer/PM/sales costs remain assumptions; monthly grid charges full drafter cost. Trials allocate only used labor, with idle capacity examined separately.'}
    assert isclose(usd*124.75,40000)
    assert isclose(sample_cost,18.75751503006012)
    assert isclose(next(x['profit'] for x in actual_months if x['sold_hours']==112 and x['rate']==20 and x['reviewer_cost']==20 and x['uplift']==0),773.3587174348697)
    results['total_grid_cases']=sum(results[k]['count'] for k in ['fixed_jobs','monthly','trial_cohorts','funnel','user_calibrated'])
    results['illustrations']={
      'simple_trial_contribution':[dict(price=p,delivery_cost=33.75,after_fees_and_delivery=p*.97-33.75) for p in [0,25,49,99]],
      'full_pilot_contribution':[dict(price=p,delivery_cost=80,after_fees_and_delivery=p*.97-80) for p in [0,25,49,99,175]],
      'monthly_sensitivity':[dict(rate=r,labor=c,**month(r,80,56,c,.1,.2,20,.1,100)) for c in [4,6,8,10] for r in [15,20,25,30]],
      'cohort_payback':[dict(price=p,blocks=b,**cohort(p,10,1.5,15,.2,25,b)) for p in [0,25,49,99] for b in [1,3]],
      'free_repeat_rate_sensitivity':[dict(rate=r,**cohort(0,10,1.5,15,.2,r,3)) for r in [15,20,25,30]],
      'free_acquisition_sensitivity':[dict(acquisition_per_trial=c,**cohort(0,10,1.5,c,.2,25,3)) for c in [0,15,50,150]],
      'direct_funnel_examples':[dict(n=n,**funnel(n,.1,.5,.2,10,0,25,3)) for n in [30,60,100,200,300]],
      'zero_repeats_upper_95_one_sided':[{'completed_trials':n,'upper_conversion':1-.05**(1/n)} for n in [10,20,30]],
    }
    outfile=ROOT/'stress_test_results.json'
    outfile.write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(json.dumps({'validation':results['validation'],'counts':{k:results[k]['count'] for k in ['fixed_jobs','monthly','trial_cohorts','funnel','user_calibrated']},'total':results['total_grid_cases'],'user_calibrated':results['user_calibrated']},indent=2))

if __name__=='__main__': run()
