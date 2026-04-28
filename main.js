/* ================================================
   PORTFOLIO MAIN JS — Agief Vemas Afrivanzah
   Handles: Nav scroll, hamburger, reveal animations,
            portfolio filter, form submit, skill bars
================================================ */

// ─── ENTRANCE SCREEN ─────────────────────────────
const entrance = document.getElementById('entrance-screen');
const enterBtn = document.getElementById('enter-btn');
const mainWrapper = document.getElementById('main-wrapper');

if (entrance && enterBtn) {
  // Check if user has already entered in this session
  if (sessionStorage.getItem('hasEntered')) {
    entrance.style.display = 'none';
    document.body.style.overflow = '';
    if (mainWrapper) {
      mainWrapper.style.opacity = '1';
      mainWrapper.style.visibility = 'visible';
      mainWrapper.style.transition = 'none';
    }
    // Observe animations immediately
    setTimeout(() => {
      document.querySelectorAll('.reveal').forEach(el => {
        if (typeof revealObserver !== 'undefined') revealObserver.observe(el);
      });
    }, 100);
  } else {
    // Lock scroll initially
    document.body.style.overflow = 'hidden';

    enterBtn.addEventListener('click', () => {
      entrance.classList.add('hidden');
      document.body.style.overflow = '';
      sessionStorage.setItem('hasEntered', 'true');
      
      // Reveal the main web content after a slight delay
      if (mainWrapper) {
        setTimeout(() => {
          mainWrapper.style.opacity = '1';
          mainWrapper.style.visibility = 'visible';
        }, 300);
      }
      
      // Completely disable entrance after it fades to free up browser resources
      setTimeout(() => {
        entrance.style.display = 'none';
        document.querySelectorAll('.reveal').forEach(el => {
          if (typeof revealObserver !== 'undefined') revealObserver.observe(el);
        });
      }, 1000);
    });
  }
}

// ─── NAV SCROLL EFFECT ──────────────────────────
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 30);
  });
}

// ─── HAMBURGER MENU ─────────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('nav-links');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('active');
    document.body.style.overflow =
      navLinks.classList.contains('active') ? 'hidden' : '';
  });

  // Close on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

// ─── SCROLL REVEAL ──────────────────────────────
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Stagger child items inside the revealed element
        setTimeout(() => {
          entry.target.classList.add('active');
        }, i * 60);
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ─── PORTFOLIO FILTER ───────────────────────────
const filterBtns = document.querySelectorAll('.filter-btn');
const portCards  = document.querySelectorAll('.port-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;

    portCards.forEach(card => {
      const cat = card.dataset.cat || '';
      const show = filter === 'all' || cat.includes(filter);
      card.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
      if (show) {
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
        card.style.pointerEvents = 'auto';
        card.style.display = '';
      } else {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.92)';
        card.style.pointerEvents = 'none';
        setTimeout(() => {
          if (!card.dataset.cat.includes(filter) && filter !== 'all') {
            card.style.display = 'none';
          }
        }, 360);
      }
    });
  });
});

// ─── ANIMATED COUNT-UP ──────────────────────────
function animateCounter(el) {
  const target = parseInt(el.dataset.count, 10);
  if (isNaN(target)) return;
  let current = 0;
  const step = Math.ceil(target / 40);
  const timer = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = current + (el.dataset.suffix || '+');
    if (current >= target) clearInterval(timer);
  }, 40);
}

const counterObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-count]').forEach(el => counterObserver.observe(el));

// ─── SKILL BAR ANIMATION ────────────────────────
const skillObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.skill-bar > div').forEach(bar => {
        const w = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => { bar.style.width = w; }, 100);
      });
      skillObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.skill-category, #skills-bars').forEach(el =>
  skillObserver.observe(el)
);

// ─── CONTACT FORM ───────────────────────────────
const form    = document.getElementById('contact-form');
const success = document.getElementById('form-success');
const btnText = document.getElementById('btn-text');

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (btnText) {
      btnText.textContent = 'Mengirim...';
    }
    // Simulate send
    setTimeout(() => {
      form.hidden = true;
      if (success) success.hidden = false;
    }, 1200);
  });
}

function resetForm() {
  if (form)    { form.reset(); form.hidden = false; }
  if (success) { success.hidden = true; }
  if (btnText) { btnText.textContent = 'Kirim Pesan ✉'; }
}

// ─── SMOOTH ACTIVE NAV HIGHLIGHT ────────────────
(function highlightCurrentPage() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === path) {
      link.classList.add('active');
    }
  });
})();

// ─── CURSOR GLOW (subtle) ───────────────────────
(function cursorGlow() {
  const glow = document.createElement('div');
  glow.style.cssText = `
    position: fixed; pointer-events: none; z-index: 9999;
    width: 400px; height: 400px; border-radius: 50%;
    background: radial-gradient(circle, rgba(124,106,255,0.06) 0%, transparent 70%);
    transform: translate(-50%, -50%);
    transition: left 0.15s ease, top 0.15s ease;
    top: 0; left: 0;
  `;
  document.body.appendChild(glow);
  window.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top  = e.clientY + 'px';
  });
})();

// ─── CARD TILT EFFECT (subtle 3-D) ──────────────
document.querySelectorAll('.project-card, .port-card, .skill-category').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width  - 0.5) * 10;
    const y = ((e.clientY - rect.top)  / rect.height - 0.5) * 10;
    card.style.transform = `perspective(600px) rotateY(${x}deg) rotateX(${-y}deg) translateY(-6px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

// ─── REVEAL PAGE TITLE LETTERS ──────────────────
document.querySelectorAll('.page-title').forEach(el => {
  // Already handled by CSS animation via .reveal
  el.style.opacity = '0';
  el.style.transform = 'translateY(30px)';
  setTimeout(() => {
    el.style.transition = 'opacity 0.9s ease, transform 0.9s ease';
    el.style.opacity = '1';
    el.style.transform = 'translateY(0)';
  }, 200);
});

// ─── TYPING EFFECT ON HERO TAGLINE ──────────────
(function typeEffect() {
  const tagline = document.querySelector('.hero-tagline');
  if (!tagline) return;
  const text = tagline.textContent.trim();
  tagline.textContent = '';
  tagline.style.opacity = '1';
  tagline.style.webkitTextFillColor = 'transparent';
  let i = 0;
  const type = () => {
    if (i <= text.length) {
      tagline.textContent = text.slice(0, i);
      i++;
      setTimeout(type, 80);
    }
  };
  setTimeout(type, 1200);
})();
