/* ═══════════════════════════════════════
   HELIOS GYM — PRESENTATION JAVASCRIPT
   ═══════════════════════════════════════ */

let currentSlide = 1;
const totalSlides = 18;

const slideData = [
  { n: '01', t: 'Cover' },
  { n: '02', t: 'About Me' },
  { n: '03', t: 'Background' },
  { n: '04', t: 'Objectives' },
  { n: '05', t: 'IG Performance' },
  { n: '06', t: 'Customer Journey' },
  { n: '07', t: 'Lead Analysis' },
  { n: '08', t: 'Pain Points' },
  { n: '09', t: 'Behavior Analysis' },
  { n: '10', t: 'Case Study' },
  { n: '11', t: 'Current Funnel' },
  { n: '12', t: 'Business Opportunity' },
  { n: '13', t: 'Strategy Roadmap' },
  { n: '14', t: 'Content Calendar' },
  { n: '15', t: 'Workflow' },
  { n: '16', t: 'Expected KPI' },
  { n: '17', t: 'Long-Term Vision' },
  { n: '18', t: 'Closing' },
];

/* ──────────────── INIT ──────────────── */
function init() {
  buildDots();
  buildOverview();
  goToSlide(1);

  document.addEventListener('keydown', onKey);
  setupSwipe();
}

/* ──────────────── DOTS ──────────────── */
function buildDots() {
  const container = document.getElementById('slideDots');
  for (let i = 1; i <= totalSlides; i++) {
    const d = document.createElement('div');
    d.className = 'dot';
    d.id = `dot-${i}`;
    d.title = slideData[i - 1].t;
    d.onclick = () => goToSlide(i);
    container.appendChild(d);
  }
}

/* ──────────────── OVERVIEW ──────────────── */
function buildOverview() {
  const grid = document.getElementById('overviewGrid');
  slideData.forEach((s, i) => {
    const el = document.createElement('div');
    el.className = 'ov-thumb';
    el.innerHTML = `<div class="ov-n">${s.n}</div><div class="ov-t">${s.t}</div>`;
    el.onclick = () => { goToSlide(i + 1); closeOverview(); };
    grid.appendChild(el);
  });
}

/* ──────────────── NAVIGATION ──────────────── */
function goToSlide(n, skipAnim = false) {
  if (n < 1 || n > totalSlides) return;

  const prev = document.getElementById(`slide-${currentSlide}`);
  const next = document.getElementById(`slide-${n}`);

  if (prev && prev !== next) {
    prev.classList.remove('active');
    if (!skipAnim) {
      prev.classList.add('exit');
      setTimeout(() => prev.classList.remove('exit'), 500);
    }
  }

  currentSlide = n;

  if (next) {
    next.classList.add('active');
  }

  updateUI();
  runSlideEntrance(n);
}

function changeSlide(dir) {
  goToSlide(currentSlide + dir);
}

function updateUI() {
  // Nav number
  document.getElementById('navCurrent').textContent =
    String(currentSlide).padStart(2, '0');

  // Progress bar
  const pct = ((currentSlide - 1) / (totalSlides - 1)) * 100;
  document.getElementById('progressFill').style.width = pct + '%';

  // Dots
  document.querySelectorAll('.dot').forEach((d, i) => {
    d.classList.toggle('active', i + 1 === currentSlide);
  });

  // Prev/next buttons
  document.getElementById('prevBtn').style.opacity = currentSlide === 1 ? '0.3' : '1';
  document.getElementById('nextBtn').style.opacity = currentSlide === totalSlides ? '0.3' : '1';
}

/* ──────────────── SLIDE ENTRANCE EFFECTS ──────────────── */
function runSlideEntrance(n) {
  switch (n) {
    case 5: setTimeout(runCounters, 300); setTimeout(animateLeaderboard, 500); break;
    case 7: setTimeout(animateLeadBars, 400); break;
    case 16: setTimeout(animateKPIBars, 400); break;
  }
}

/* ──────────────── COUNTERS ──────────────── */
function runCounters() {
  document.querySelectorAll('.counter').forEach(el => {
    const target = parseInt(el.dataset.target);
    const duration = 1200;
    const startTime = performance.now();
    const startVal = 0;

    function update(ts) {
      const elapsed = ts - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(startVal + (target - startVal) * eased).toLocaleString();
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  });
}

/* ──────────────── LEADERBOARD BARS ──────────────── */
function animateLeaderboard() {
  const rows = document.querySelectorAll('#slide-5 .lb-bar');
  rows.forEach((bar, i) => {
    const target = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 1s cubic-bezier(0.4,0,0.2,1)';
      bar.style.width = target;
    }, i * 120);
  });
}

/* ──────────────── BAR ANIMATIONS ──────────────── */
function animateBars() {
  document.querySelectorAll('.bar-fill').forEach((bar, i) => {
    const target = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 0.8s cubic-bezier(0.4,0,0.2,1)';
      bar.style.width = target;
    }, i * 80);
  });
}

function animateLeadBars() {
  document.querySelectorAll('.lb-fill').forEach((bar, i) => {
    const target = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 1s cubic-bezier(0.4,0,0.2,1)';
      bar.style.width = target;
    }, i * 100);
  });
}

function animateKPIBars() {
  document.querySelectorAll('.km-fill').forEach((bar, i) => {
    const targetPct = parseInt(bar.dataset.target) || 50;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 1.2s cubic-bezier(0.4,0,0.2,1)';
      bar.style.width = targetPct + '%';
    }, i * 150);
  });
}

/* ──────────────── KEYBOARD ──────────────── */
function onKey(e) {
  switch (e.key) {
    case 'ArrowRight':
    case 'ArrowDown':
    case ' ':
      e.preventDefault();
      changeSlide(1);
      break;
    case 'ArrowLeft':
    case 'ArrowUp':
      e.preventDefault();
      changeSlide(-1);
      break;
    case 'Escape':
      toggleOverview();
      break;
    case 'Home':
      goToSlide(1);
      break;
    case 'End':
      goToSlide(totalSlides);
      break;
  }
}

/* ──────────────── OVERVIEW ──────────────── */
function toggleOverview() {
  const modal = document.getElementById('overviewModal');
  modal.classList.toggle('open');
}

function closeOverview() {
  document.getElementById('overviewModal').classList.remove('open');
}

/* ──────────────── TOUCH / SWIPE ──────────────── */
function setupSwipe() {
  let startX = 0;
  let startY = 0;

  document.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
  }, { passive: true });

  document.addEventListener('touchend', e => {
    const dx = startX - e.changedTouches[0].clientX;
    const dy = startY - e.changedTouches[0].clientY;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
      dx > 0 ? changeSlide(1) : changeSlide(-1);
    }
  }, { passive: true });
}

/* ──────────────── MOUSE WHEEL ──────────────── */
let wheelLock = false;
document.addEventListener('wheel', e => {
  if (wheelLock) return;
  wheelLock = true;
  e.deltaY > 0 ? changeSlide(1) : changeSlide(-1);
  setTimeout(() => { wheelLock = false; }, 800);
}, { passive: true });

/* ──────────────── INTERSECTION OBSERVER for pain bars ──────────────── */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.pain-fill').forEach((bar, i) => {
        const w = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
          bar.style.transition = 'width 0.8s cubic-bezier(0.4,0,0.2,1)';
          bar.style.width = w;
        }, i * 60 + 200);
      });
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('#slide-8').forEach(el => observer.observe(el));

/* ──────────────── CT BARS animation on slide 5 ──────────────── */
function animateCTBars() {
  document.querySelectorAll('.ct-bar').forEach(bar => {
    const w = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 1s cubic-bezier(0.4,0,0.2,1)';
      bar.style.width = w;
    }, 300);
  });
}

/* ──────────────── START ──────────────── */
document.addEventListener('DOMContentLoaded', init);
