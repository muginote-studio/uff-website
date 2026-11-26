(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#nav');
  function closeMenu() {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'メニューを開く');
    nav.classList.remove('is-open');
  }
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
      nav.classList.toggle('is-open', open);
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu(); toggle.focus();
      }
    });
    window.matchMedia('(min-width: 761px)').addEventListener('change', e => {
      if (e.matches) closeMenu();
    });
  }
  const modeButtons = [...document.querySelectorAll('[data-mode]')];
  modeButtons.forEach(button => button.addEventListener('click', () => {
    const mode = button.dataset.mode;
    document.body.classList.toggle('mode-day', mode === 'day');
    modeButtons.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    const img = document.querySelector('img[data-day]');
    if (img) img.src = img.dataset[mode];
  }));
  const filters = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('.gallery-card')];
  filters.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    filters.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    let visible = 0;
    cards.forEach(card => {
      card.hidden = category !== 'all' && card.dataset.category !== category;
      if (!card.hidden) visible++;
    });
    document.querySelector('#filter-status').textContent = visible + '件のデザイン';
  }));
})();

