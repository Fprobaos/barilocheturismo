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

/* ── CONTACT FORM ─────────────────────────────────────────────── */
const contactForm = document.getElementById('contactForm');
const formMsg     = document.getElementById('formMsg');

contactForm.addEventListener('submit', e => {
  e.preventDefault();

  const nombre      = contactForm.nombre.value.trim();
  const email       = contactForm.email.value.trim();
  const experiencia = contactForm.experiencia.value;
  const mensaje     = contactForm.mensaje.value.trim();

  if (!nombre || !email) {
    formMsg.className = 'form-msg error';
    formMsg.textContent = currentLang === 'es'
      ? 'Por favor completá nombre y email.'
      : 'Please fill in name and email.';
    return;
  }

  const btn = contactForm.querySelector('.btn-submit');
  btn.disabled = true;
  btn.textContent = currentLang === 'es' ? 'Enviando...' : 'Sending...';

  const waText = encodeURIComponent(
    `Hola! Soy ${nombre} (${email}).\n` +
    (experiencia ? `Experiencia: ${experiencia}\n` : '') +
    (mensaje ? `\n${mensaje}` : '')
  );

  setTimeout(() => {
    formMsg.className = 'form-msg success';
    formMsg.textContent = currentLang === 'es'
      ? '¡Mensaje enviado! Te contactamos pronto.'
      : 'Message sent! We\'ll contact you soon.';

    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${waText}`, '_blank');

    contactForm.reset();
    btn.disabled = false;
    btn.textContent = currentLang === 'es' ? 'Enviar consulta' : 'Send inquiry';

    setTimeout(() => { formMsg.textContent = ''; }, 5000);
  }, 600);
});

/* ── APPLY INSTAGRAM LINKS ────────────────────────────────────── */
document.querySelectorAll('.canal-instagram, .footer-social a[aria-label="Instagram"]').forEach(a => {
  a.href = INSTAGRAM_URL;
});

/* ── APPLY WHATSAPP LINKS ─────────────────────────────────────── */
const waLink = encodeURIComponent(WHATSAPP_MSG);
document.querySelectorAll('.whatsapp-fab, .canal-whatsapp, .footer-social a[aria-label="WhatsApp"]').forEach(a => {
  a.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${waLink}`;
});
