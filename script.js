/* ── CONFIG — Editá estos valores ─────────────────────────────── */
const WHATSAPP_NUMBER = '+54XXXXXXXXXX'; // Reemplazá con tu número real
const WHATSAPP_MSG    = 'Hola, me gustaría consultar sobre Lago Sur Experiences';
const INSTAGRAM_URL   = 'https://instagram.com/TU_USUARIO_AQUI'; // Reemplazá con tu @

/* ── LANGUAGE ─────────────────────────────────────────────────── */
let currentLang = 'es';

function setLang(lang) {
  currentLang = lang;

  document.querySelectorAll('[data-es]').forEach(el => {
    const text = el.dataset[lang];
    if (text !== undefined) el.textContent = text;
  });

  document.querySelectorAll('[data-placeholder-es]').forEach(el => {
    const ph = lang === 'es' ? el.dataset.placeholderEs : el.dataset.placeholderEn;
    if (ph) el.placeholder = ph;
  });

  document.getElementById('btnEs').classList.toggle('active', lang === 'es');
  document.getElementById('btnEn').classList.toggle('active', lang === 'en');
  document.documentElement.lang = lang;

  if (typeof renderCalendar === 'function') {
    updateCalSummary();
    renderCalendar();
  }
}

/* ── NAVBAR SCROLL ────────────────────────────────────────────── */
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

/* ── MOBILE MENU ──────────────────────────────────────────────── */
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => navLinks.classList.remove('open'));
});

/* ── SMOOTH SCROLL ────────────────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = navbar.offsetHeight;
    window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
  });
});

/* ── FADE-IN ON SCROLL ────────────────────────────────────────── */
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.fade-in').forEach((el, i) => {
  el.style.transitionDelay = `${(i % 4) * 0.1}s`;
  observer.observe(el);
});

/* ── GALLERY LIGHTBOX ─────────────────────────────────────────── */
const galleryItems   = document.querySelectorAll('.gallery-item');
const lightbox       = document.getElementById('lightbox');
const lightboxContent = document.getElementById('lightboxContent');
let   currentIndex   = 0;

function openLightbox(index) {
  currentIndex = index;
  renderLightboxItem();
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  lightbox.classList.remove('open');
  document.body.style.overflow = '';
}

function lightboxNav(dir) {
  currentIndex = (currentIndex + dir + galleryItems.length) % galleryItems.length;
  renderLightboxItem();
}

function renderLightboxItem() {
  const src = galleryItems[currentIndex].querySelector('img');
  lightboxContent.innerHTML = '';

  if (src) {
    const img = document.createElement('img');
    img.src = src.src;
    img.alt = src.alt || '';
    img.style.cssText = 'max-width:85vw;max-height:80vh;border-radius:4px;display:block;';
    lightboxContent.appendChild(img);
  } else {
    const ph = galleryItems[currentIndex].querySelector('.img-placeholder');
    if (ph) {
      const clone = ph.cloneNode(true);
      clone.classList.add('img-placeholder');
      clone.style.cssText = 'width:800px;height:500px;max-width:85vw;max-height:75vh;border-radius:4px;';
      lightboxContent.appendChild(clone);
    }
  }
}

document.addEventListener('keydown', e => {
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape')      closeLightbox();
  if (e.key === 'ArrowRight')  lightboxNav(1);
  if (e.key === 'ArrowLeft')   lightboxNav(-1);
});

/* ── CALENDARIO RESERVAS ──────────────────────────────────────── */
/* Temporada: 1 Dic 2026 → 31 Mar 2027. Selección de rango consecutivo. */
const CAL_RANGE = {
  // months as [year, monthIndex] — monthIndex is 0-based
  months: [[2026, 11], [2027, 0], [2027, 1], [2027, 2]],
  min: new Date(2026, 11, 1),
  max: new Date(2027, 2, 31),
};

const MONTH_NAMES = {
  es: ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
  en: ['January','February','March','April','May','June','July','August','September','October','November','December'],
};
const DOW = {
  es: ['Lu','Ma','Mi','Ju','Vi','Sá','Do'],
  en: ['Mo','Tu','We','Th','Fr','Sa','Su'],
};

let calStartDate = null;
let calEndDate   = null;

const calMonthsEl = document.getElementById('calMonths');
const calStartEl  = document.getElementById('calStart');
const calEndEl    = document.getElementById('calEnd');
const calNightsEl = document.getElementById('calNights');
const calConfirm  = document.getElementById('calConfirm');
const calClear    = document.getElementById('calClear');
const calHint     = document.getElementById('calHint');

const sameDay = (a, b) => a && b && a.getTime() === b.getTime();
const inRange = (d, a, b) => a && b && d > a && d < b;

function fmtDate(d, lang) {
  if (!d) return '—';
  return `${d.getDate()} ${MONTH_NAMES[lang][d.getMonth()]} ${d.getFullYear()}`;
}

function renderCalendar() {
  calMonthsEl.innerHTML = '';

  CAL_RANGE.months.forEach(([y, m]) => {
    const monthBox = document.createElement('div');
    monthBox.className = 'cal-month';

    const title = document.createElement('h4');
    title.className = 'cal-month-title';
    title.dataset.es = `${MONTH_NAMES.es[m]} ${y}`;
    title.dataset.en = `${MONTH_NAMES.en[m]} ${y}`;
    title.textContent = `${MONTH_NAMES[currentLang][m]} ${y}`;
    monthBox.appendChild(title);

    const grid = document.createElement('div');
    grid.className = 'cal-grid';

    DOW[currentLang].forEach((d, i) => {
      const dow = document.createElement('div');
      dow.className = 'cal-dow';
      dow.dataset.es = DOW.es[i];
      dow.dataset.en = DOW.en[i];
      dow.textContent = d;
      grid.appendChild(dow);
    });

    // Monday-first offset
    const firstDow = (new Date(y, m, 1).getDay() + 6) % 7;
    for (let i = 0; i < firstDow; i++) {
      const empty = document.createElement('div');
      empty.className = 'cal-day cal-day--empty';
      grid.appendChild(empty);
    }

    const daysInMonth = new Date(y, m + 1, 0).getDate();
    for (let d = 1; d <= daysInMonth; d++) {
      const date = new Date(y, m, d);
      const day = document.createElement('button');
      day.type = 'button';
      day.className = 'cal-day';
      day.textContent = d;

      if (date < CAL_RANGE.min || date > CAL_RANGE.max) {
        day.classList.add('cal-day--disabled');
        day.disabled = true;
      } else {
        day.addEventListener('click', () => onDayClick(date));
      }

      if (sameDay(date, calStartDate)) day.classList.add('cal-day--start');
      if (sameDay(date, calEndDate))   day.classList.add('cal-day--end');
      if (inRange(date, calStartDate, calEndDate)) day.classList.add('cal-day--in-range');

      grid.appendChild(day);
    }

    monthBox.appendChild(grid);
    calMonthsEl.appendChild(monthBox);
  });
}

function onDayClick(date) {
  if (!calStartDate || (calStartDate && calEndDate)) {
    // start fresh
    calStartDate = date;
    calEndDate = null;
  } else if (date.getTime() === calStartDate.getTime()) {
    // clicked same day — clear
    calStartDate = null;
    calEndDate = null;
  } else if (date < calStartDate) {
    // earlier date → restart from there
    calStartDate = date;
    calEndDate = null;
  } else {
    calEndDate = date;
  }
  updateCalSummary();
  renderCalendar();
}

function updateCalSummary() {
  calStartEl.textContent = calStartDate ? fmtDate(calStartDate, currentLang) : '—';
  calEndEl.textContent   = calEndDate   ? fmtDate(calEndDate, currentLang)   : '—';

  let nights = '—';
  if (calStartDate && calEndDate) {
    nights = Math.round((calEndDate - calStartDate) / 86400000);
  }
  calNightsEl.textContent = nights;

  calConfirm.disabled = !(calStartDate && calEndDate);

  if (!calStartDate) {
    calHint.dataset.es = 'Hacé clic en una fecha para empezar.';
    calHint.dataset.en = 'Click a date to start.';
  } else if (!calEndDate) {
    calHint.dataset.es = 'Ahora elegí la fecha de salida.';
    calHint.dataset.en = 'Now choose your check-out date.';
  } else {
    calHint.dataset.es = 'Confirmá para enviar tu consulta por WhatsApp.';
    calHint.dataset.en = 'Confirm to send your inquiry via WhatsApp.';
  }
  calHint.textContent = calHint.dataset[currentLang];
}

calClear.addEventListener('click', () => {
  calStartDate = null;
  calEndDate = null;
  updateCalSummary();
  renderCalendar();
});

calConfirm.addEventListener('click', () => {
  if (!calStartDate || !calEndDate) return;

  const rango = `${fmtDate(calStartDate, currentLang)} → ${fmtDate(calEndDate, currentLang)}`;
  const nights = Math.round((calEndDate - calStartDate) / 86400000);
  const text = currentLang === 'es'
    ? `Hola! Quisiera consultar disponibilidad para Lago Sur Experiences.\nFechas: ${rango} (${nights} noches).`
    : `Hi! I'd like to check availability for Lago Sur Experiences.\nDates: ${rango} (${nights} nights).`;
  window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(text)}`, '_blank');
});

renderCalendar();
updateCalSummary();

/* ── APPLY INSTAGRAM LINKS ────────────────────────────────────── */
document.querySelectorAll('.canal-instagram, .footer-social a[aria-label="Instagram"]').forEach(a => {
  a.href = INSTAGRAM_URL;
});

/* ── APPLY WHATSAPP LINKS ─────────────────────────────────────── */
const waLink = encodeURIComponent(WHATSAPP_MSG);
document.querySelectorAll('.whatsapp-fab, .canal-whatsapp, .footer-social a[aria-label="WhatsApp"]').forEach(a => {
  a.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${waLink}`;
});

/* ── MAPA LAGOS (Leaflet + CartoDB Dark Matter) ──────────────── */
if (typeof L !== 'undefined' && document.getElementById('lagosMap')) {
  const map = L.map('lagosMap', {
    center: [-41.20, -71.48],
    zoom: 10,
    scrollWheelZoom: false,
    zoomControl: true,
  });

  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; OpenStreetMap &copy; CARTO',
    subdomains: 'abcd',
    maxZoom: 19,
  }).addTo(map);

  const lagos = [
    { name: 'Nahuel Huapi', coords: [-41.02, -71.55] },
    { name: 'Lago Gutiérrez', coords: [-41.22, -71.43] },
    { name: 'Lago Mascardi', coords: [-41.34, -71.55] },
  ];

  const lakeIcon = L.divIcon({
    className: 'lago-pin',
    html: '<span class="lago-pin-dot"></span>',
    iconSize: [14, 14],
    iconAnchor: [7, 7],
  });

  lagos.forEach(l => {
    L.marker(l.coords, { icon: lakeIcon })
      .addTo(map)
      .bindTooltip(l.name, {
        permanent: true,
        direction: 'right',
        offset: [10, 0],
        className: 'lago-tooltip',
      });
  });

  // Arelauquen marker
  const homeIcon = L.divIcon({
    className: 'lago-pin lago-pin--home',
    html: '<span class="lago-pin-dot"></span>',
    iconSize: [16, 16],
    iconAnchor: [8, 8],
  });
  L.marker([-41.183, -71.465], { icon: homeIcon })
    .addTo(map)
    .bindTooltip('Arelauquen', {
      permanent: true,
      direction: 'right',
      offset: [10, 0],
      className: 'lago-tooltip lago-tooltip--home',
    });
}
