(() => {
  const toggle = document.querySelector('[data-nav-toggle]');
  const menu = document.querySelector('[data-nav-menu]');

  if (toggle && menu) {
    function setMenu(open) {
      toggle.setAttribute('aria-expanded', String(open));
      menu.dataset.open = String(open);
    }

    setMenu(false);
    toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', (event) => {
      if (event.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        toggle.focus();
      }
    });
  }

  const fields = {
    name: 'Name',
    email: 'Work email',
    company: 'Company',
    service: 'Service',
    timeline: 'Target deadline',
    scope: 'Project summary',
  };

  document.querySelectorAll('form[data-intake]').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const data = new FormData(form);
      const details = Object.entries(fields)
        .filter(([field]) => String(data.get(field) ?? '').trim())
        .map(([field, label]) => `${label}: ${String(data.get(field)).trim()}`)
        .join('\r\n');
      const recipient = form.dataset.recipient;
      const subject = encodeURIComponent(form.dataset.subject);
      const draft = `mailto:${recipient}?subject=${subject}&body=${encodeURIComponent(details)}`;
      const status = form.querySelector('[data-intake-status]') ?? document.querySelector('[data-intake-status]');

      if (status) {
        status.hidden = false;
        status.textContent = 'Your email draft is ready. If it does not open, ';
        const fallback = document.createElement('a');
        fallback.href = draft;
        fallback.textContent = 'open it here';
        status.append(fallback, `. You can also email ${recipient} directly.`);
      }

      window.location.href = draft;
    });
  });
})();
