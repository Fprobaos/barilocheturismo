# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static marketing site for **Lago Sur Experiences** — luxury tourism experiences in Arelauquen, Bariloche (golf, lake, fishing, secret trails). No build step, no dependencies, no framework.

- `index.html` — home (navbar, hero, sobre, experiencias, anfitrión, galería, mapa, reservar, llegar, faq, contacto, footer)
- `experiencias.html` — detail page, one `<article class="xp">` per experience (lancha, pesca, rutas, casa). Navbar/footer/FAB/lightbox are copied from `index.html`, so keep them in sync (a mid-session generator script did this; edit both files by hand otherwise)
- `styles.css` — all styling (Cormorant Garamond + Montserrat from Google Fonts)
- `script.js` — all behavior

## Running

Open `index.html` directly in a browser, or serve the directory with any static server (e.g. `python -m http.server`). There is no build, no lint, and no test setup.

## Deploy

Production is https://lago-sur-experiences.vercel.app, deployed with `vercel --prod --yes` (no git integration). The owner wants every change deployed as soon as it is made.

## SEO / GEO / Ads

- `robots.txt`, `sitemap.xml`, `llms.txt` live at the root and use the canonical domain `lagosurexperiences.com` (same as the `<link rel="canonical">` tags). Update all of them together if the domain changes.
- JSON-LD: `TravelAgency` + `FAQPage` on the home, `BreadcrumbList` + `ItemList` of `TouristTrip` on the experiences page. The FAQ schema mirrors the `<details>` content — keep them in sync.
- Google Ads / GA4: `GTAG_ID` and `ADS_CONVERSION` at the top of `script.js` are empty placeholders; nothing loads until they are set. `trackContact()` fires on every WhatsApp click and on calendar confirm.

## Architecture notes

`script.js` is shared by both pages. Blocks that depend on home-only elements (calendar, map) are guarded with existence checks — keep that pattern when adding features.


**Bilingual content (ES/EN)** is driven by data attributes, not separate templates. Every translatable element carries `data-es="..."` and `data-en="..."`; `setLang(lang)` in `script.js` swaps `textContent` for all `[data-es]` nodes and `placeholder` for all `[data-placeholder-es]` inputs. To add translatable copy, add both attributes — don't introduce a new mechanism.

**Configurable contact endpoints** live at the top of `script.js`:
- `WHATSAPP_NUMBER`, `WHATSAPP_MSG` — applied to every `.whatsapp-fab`, `.canal-whatsapp`, and the WhatsApp footer link, plus the contact-form submission which opens `wa.me/...` in a new tab.
- `INSTAGRAM_URL` — applied to every `.canal-instagram` and the Instagram footer link.

These are placeholder values (`+54XXXXXXXXXX`, `TU_USUARIO_AQUI`) intended to be replaced before deploy.

**Contact form** does not POST anywhere — it builds a prefilled WhatsApp message and opens `wa.me`. Any "backend" change means changing that flow.

**Scroll/visibility behaviors**: `IntersectionObserver` adds `.visible` to `.fade-in` elements (one-shot, unobserved after firing); navbar gets `.scrolled` after 40px; smooth-scroll handler offsets by `navbar.offsetHeight` so anchors don't hide under the fixed nav.

**Lightbox** iterates `.gallery-item` nodes, supports keyboard nav (Esc / ←/→), and clones `.img-placeholder` when an item has no `<img>`.
