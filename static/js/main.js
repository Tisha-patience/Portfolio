/* ── Typed hero text ── */
(function () {
  const phrases = [
    'building with Python & Django.',
    'learning something new every day.',
    'turning ideas into working software.',
    'open to junior roles & opportunities.',
  ];

  const el = document.getElementById('typed-text');
  if (!el) return;

  let phraseIndex = 0;
  let charIndex = 0;
  let deleting = false;

  function type() {
    const current = phrases[phraseIndex];

    if (!deleting) {
      el.textContent = current.slice(0, charIndex + 1);
      charIndex++;
      if (charIndex === current.length) {
        deleting = true;
        setTimeout(type, 2200);
        return;
      }
    } else {
      el.textContent = current.slice(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        deleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
      }
    }
    setTimeout(type, deleting ? 45 : 70);
  }

  setTimeout(type, 900);
})();


/* ── Scroll reveal ── */
(function () {
  const targets = document.querySelectorAll('.reveal');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    { threshold: 0.12 }
  );

  targets.forEach((el) => observer.observe(el));
})();


/* ── Skill bar animations (triggered when in view) ── */
(function () {
  const bars = document.querySelectorAll('.skill-bar');
  if (!bars.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const width = target.getAttribute('data-width');
          setTimeout(() => {
            target.style.width = width + '%';
          }, 150);
          observer.unobserve(target);
        }
      });
    },
    { threshold: 0.3 }
  );

  bars.forEach((bar) => observer.observe(bar));
})();


/* ── Active nav link highlight on scroll ── */
(function () {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('nav a[href^="#"]');

  function onScroll() {
    let current = '';
    sections.forEach((section) => {
      const top = section.offsetTop - 80;
      if (window.scrollY >= top) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove('text-brand');
      link.classList.add('text-text-secondary');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('text-brand');
        link.classList.remove('text-text-secondary');
      }
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
})();


/* ── Smooth scroll for anchor links ── */
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (href === '#') return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
