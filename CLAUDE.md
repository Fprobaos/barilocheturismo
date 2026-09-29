# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static marketing site for **Lago Sur Experiences** — luxury tourism experiences in Arelauquen, Bariloche (boat tours with optional fly fishing, secret trails, and a house coming soon). No build step, no dependencies, no framework.

- `index.html` — home (navbar, hero, sobre, experiencias, anfitrión, galería, mapa, reservar, llegar, faq, contacto, footer)
- `experiencias.html` — index of experiences (one big card per experience linking to its page)
- `paseo-en-lancha.html`, `rutas-secretas.html`, `casa-arelauquen.html` — one page per experience (hero, detail + sticky "Incluye" card, gallery strip, other experiences, contact)
- `tools/build_pages.py` — **generates the four pages above** from the `XPS` data list, copying navbar/footer/FAB/lightbox from `index.html`. Edit the data or templates there and run `python tools/build_pages.py` from the repo root; never hand-edit the generated pages. `.vercelignore` keeps `tools/` out of the deploy. Fly fishing is no longer its own experience (it is an add-on to the boat tour); `vercel.json` redirects the old `pesca-con-mosca.html` to `paseo-en-lancha.html`.
- `styles.css` — all styling (Cormorant Garamond + Montserrat from Google Fonts)
- `script.js` — all behavior

## Running

Open `index.html` directly in a browser, or serve the directory with any static server (e.g. `python -m http.server`). There is no build, no lint, and no test setup.

## Deploy

Production is https://lago-sur-experiences.vercel.app, deployed with `vercel --prod --yes` (no git integration). The owner wants every change deployed as soon as it is made.

## SEO / GEO / Ads

- `robots.txt`, `sitemap.xml`, `llms.txt` live at the root and use the canonical URL `https://lago-sur-experiences.vercel.app` (same as the `<link rel="canonical">` tags and the JSON-LD). There is no custom domain yet; when one is bought, replace that base URL in `index.html`, `experiencias.html`, `robots.txt`, `sitemap.xml` and `llms.txt` together, and add the domain in Vercel.
- JSON-LD: `TravelAgency` + `FAQPage` on the home, `BreadcrumbList` + `ItemList` of `TouristTrip` on the experiences page. The FAQ schema mirrors the `<details>` content — keep them in sync.
- Google Ads / GA4: `GA4_ID` and `ADS_CONVERSION` (`AW-…/label`) at the top of `script.js` are empty placeholders; the Google tag loads and configures whichever is set. `trackContact()` fires a GA4 `whatsapp_click` event (with `experience` from `<body data-xp>`) plus the Ads conversion on every WhatsApp click and on calendar confirm.
- Experience pages carry `data-wa-es` / `data-wa-en` on `<body>`: every WhatsApp link on that page (FAB, contact, the hero `.xp-cta-wa`) sends a message naming the experience. `?lang=en` in any URL opens the site in English (for English-language ads); the choice is kept in `sessionStorage` while browsing.

## Architecture notes

`script.js` is shared by both pages. Blocks that depend on home-only elements (calendar, map) are guarded with existence checks — keep that pattern when adding features.


**Bilingual content (ES/EN)** is driven by data attributes, not separate templates. Every translatable element carries `data-es="..."` and `data-en="..."`; `setLang(lang)` in `script.js` swaps `textContent` for all `[data-es]` nodes and `placeholder` for all `[data-placeholder-es]` inputs. To add translatable copy, add both attributes — don't introduce a new mechanism.

**Configurable contact endpoints** live at the top of `script.js`:
- `WHATSAPP_NUMBER`, `WHATSAPP_MSG` — applied to every `.whatsapp-fab`, `.canal-whatsapp`, and the WhatsApp footer link, plus the contact-form submission which opens `wa.me/...` in a new tab.
- `INSTAGRAM_URL` — applied to every `.canal-instagram` and the Instagram footer link.

`WHATSAPP_NUMBER` is empty until the owner's WhatsApp Business number exists (set it in wa.me format, e.g. `549…`, and add it as `telephone` in the home `TravelAgency` JSON-LD and in `llms.txt`). While empty, every WhatsApp link and the calendar confirm fall back to `#contacto` and no conversion is tracked. `INSTAGRAM_URL` is empty until the account exists — while empty, `script.js` removes every Instagram button, so the static `href="#"` never shows. When it exists, set it there and add it as `sameAs` in the home `TravelAgency` JSON-LD.

**Contact form** does not POST anywhere — it builds a prefilled WhatsApp message and opens `wa.me`. Any "backend" change means changing that flow.

**Scroll/visibility behaviors**: `IntersectionObserver` adds `.visible` to `.fade-in` elements (one-shot, unobserved after firing); navbar gets `.scrolled` after 40px; smooth-scroll handler offsets by `navbar.offsetHeight` so anchors don't hide under the fixed nav.

**Lakes map** (home only): Leaflet with Esri World Imagery tiles (CARTO now requires an API key). Pins come from the `lagos` array in `script.js`; giving an entry `pano` (equirectangular 2:1 JPG, 4096×2048, in `assets/pano/`), `thumb` (160px square crop) and optional start `yaw` turns its dot into a round thumbnail that opens a fullscreen Pannellum 360° viewer, lazy-loaded from jsdelivr on first open.

**Lightbox** iterates `.gallery-item` nodes, supports keyboard nav (Esc / ←/→), and clones `.img-placeholder` when an item has no `<img>`.
