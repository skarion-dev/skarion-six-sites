const form = document.querySelector('.research-filter');
const query = form.querySelector('input');
const result = form.querySelector('[data-result-count]');
const items = [...form.closest('.research-block').querySelectorAll('[data-filter-item]')];
const searchable = items.map((item) => item.textContent.toLowerCase().replaceAll(/[_-]/g, ' '));

function updateResults() {
  const terms = query.value.trim().toLowerCase().replaceAll(/[_-]/g, ' ').split(/\s+/).filter(Boolean);
  let visible = 0;
  items.forEach((item, index) => {
    const matches = terms.every((term) => searchable[index].includes(term));
    item.hidden = !matches;
    if (matches) visible++;
  });
  result.textContent = visible ? `${visible} of ${items.length} results` : 'No results found';
}

form.hidden = false;
form.addEventListener('submit', (event) => event.preventDefault());
query.addEventListener('input', updateResults);
updateResults();
