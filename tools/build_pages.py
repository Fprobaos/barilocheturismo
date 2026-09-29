# Genera experiencias.html (índice) + una página por experiencia a partir de index.html
import io, json

BASE = 'https://lagosur.site'
idx = io.open('index.html', encoding='utf-8').read()

def block(start, end, inclusive_end=True):
    i = idx.index(start); j = idx.index(end, i)
    return idx[i: j + (len(end) if inclusive_end else 0)]

nav      = block('  <!-- ── NAVBAR', '</nav>\n')
footer   = block('  <!-- ── FOOTER', '</footer>\n')
fab      = block('  <!-- ── WHATSAPP FAB', '  </a>\n')
lightbox = block('  <!-- ── LIGHTBOX', '  <script src="script.js"', False)
WA_SVG   = fab[fab.index('<svg'):fab.index('</svg>') + 6]

def nav_for(active_slug=None):
    n = (nav.replace('href="#inicio"', 'href="/"')
            .replace('href="#sobre"', 'href="/#sobre"')
            .replace('href="#experiencias" class="nav-drop-trigger"', 'href="/experiencias" class="nav-drop-trigger active"')
            .replace('href="#guias"', 'href="/#guias"')
            .replace('href="#galeria"', 'href="/#galeria"')
            .replace('href="#faq"', 'href="/#faq"'))
    if active_slug:
        n = n.replace(f'<a href="/{active_slug}"', f'<a href="/{active_slug}" class="active"')
    return n

foot2 = (footer.replace('href="#sobre"', 'href="/#sobre"')
               .replace('href="#galeria"', 'href="/#galeria"'))

DRON = ('Fotos y videos con dron de tu jornada', 'Drone photos and videos of your day')

XPS = [
  dict(slug='paseo-en-lancha', id='lancha', num='01', kicker=('Lago','Lake'), title=('Paseo en Lancha','Boat Tour'),
    tag=('El Nahuel Huapi desde el agua: bahías, islas y calas turquesa a las que no llega ningún camino.',
         'Nahuel Huapi from the water: bays, islands and turquoise coves no road can reach.'),
    p1=('Salimos en nuestra lancha privada, con capacidad para hasta seis personas, y dejamos atrás el ruido del centro. En pocos minutos el lago se abre en brazos y bahías que solo se conocen navegando.',
        'We set out on our private boat, with room for up to six people, and leave the noise of downtown behind. Within minutes the lake opens into arms and bays you only get to know by sailing.'),
    p2=('El recorrido se arma según el día y el grupo: una cala de agua turquesa para nadar, una playa escondida para un picnic, o simplemente apagar el motor y escuchar el silencio de la cordillera. Mientras tanto, el dron registra la salida desde el aire para que te lleves las fotos y los videos.',
        'The route is shaped by the day and the group: a turquoise cove for a swim, a hidden beach for a picnic, or simply cutting the engine to listen to the silence of the Andes. Meanwhile, the drone captures the outing from above so you take the photos and videos home.'),
    p3=('No hay dos salidas iguales. Si el viento acompaña cruzamos a las islas; si el lago está planchado buscamos las calas del brazo norte, donde el agua se pone transparente y las montañas se reflejan enteras. Cerramos siempre con el atardecer sobre la cordillera. Y si te gusta pescar, sumá la pesca con mosca como adicional por persona.',
        'No two outings are alike. If the wind allows we cross to the islands; if the lake is glassy we head for the coves of the northern arm, where the water turns transparent and the mountains reflect in full. We always close with sunset over the Andes. And if you like fishing, add fly fishing as a per-person extra.'),
    facts=[('Duración','Duration','Medio día','Half day'),('Grupo','Group','Hasta 6 personas','Up to 6 people'),('Temporada','Season','Dic — Mar','Dec — Mar'),('Adicional','Add-on','Pesca con mosca','Fly fishing')],
    inc=[('Lancha privada para hasta 6 personas','Private boat for up to 6 people'),
         ('Recorrido por bahías, islas y rincones del Nahuel Huapi','Route through bays, islands and hidden corners of Nahuel Huapi'),
         ('Chalecos y equipo de seguridad a bordo','Life jackets and safety gear on board'),
         ('Parada para nadar o hacer picnic en una playa escondida','Stop to swim or picnic on a hidden beach'),
         DRON],
    hero=dict(video='assets/video/lanchas-navegando-hero-v2.mp4', poster='assets/video/lanchas-navegando-hero.jpg',
              alt=('Lanchas navegando a toda velocidad por el lago Nahuel Huapi','Boats speeding across Lake Nahuel Huapi')),
    card_img='assets/img/playa-turquesa-aerea.jpg',
    strip=[('assets/img/lancha-estela.jpg', None, 'Lancha navegando el lago Nahuel Huapi entre islas','Boat cruising Lake Nahuel Huapi between islands'),
           ('assets/img/playa-turquesa-aerea.jpg', None, 'Vista aérea con dron de una playa escondida con la lancha fondeada','Drone aerial view of a hidden beach with the boat anchored'),
           ('assets/img/gomones-agua-turquesa.jpg', None, 'El grupo en los gomones sobre aguas turquesas','The group on the rafts over turquoise waters'),
           ('assets/video/costa-turquesa.jpg', 'assets/video/costa-turquesa.mp4', 'Nadando en aguas transparentes junto a una roca, con la cordillera de fondo','Swimming in crystal-clear water by a rock, with the Andes behind'),
           ('assets/img/cala-turquesa.jpg', None, 'Cala de aguas turquesas entre acantilados y bosque','Turquoise cove between cliffs and forest'),
           ('assets/img/lago-orilla-aerea.jpg', None, 'Vista aérea con dron de la orilla y los bajos turquesa del lago','Drone aerial view of the shore and the turquoise shallows'),
           ('assets/img/grupo-lancha-cerro-nevado.jpg', None, 'El grupo a bordo de la lancha, con el lago turquesa y un cerro nevado de fondo','The group aboard the boat, with the turquoise lake and a snowy peak behind'),
           ('assets/img/gomones-cordillera-contraluz.jpg', None, 'El grupo en los gomones frente a la cordillera, a contraluz','The group on the rafts facing the Andes, backlit by the sun'),
           ('assets/img/lancha-costa-bosque.jpg', None, 'La lancha navegando junto a la costa de bosque','The boat cruising along the forested shore'),
           ('assets/video/lancha-estela-bosque.jpg', 'assets/video/lancha-estela-bosque.mp4', 'La lancha abriendo estela en el lago, con bosque y cerros nevados de fondo','The boat carving a wake across the lake, with forest and snowy peaks behind'),
           ('assets/video/lancha-agua-turquesa.jpg', 'assets/video/lancha-agua-turquesa.mp4', 'Vista con dron de la lancha sobre agua turquesa, subiendo hacia los cerros','Drone view of the boat on turquoise water, rising toward the peaks')],
    meta_title='Paseo en lancha privado por el Nahuel Huapi, Bariloche | Lago Sur',
    meta_desc='Navegación privada por bahías, islas y calas turquesa del Nahuel Huapi desde Arelauquen, Bariloche. Hasta 6 personas, pesca con mosca opcional y fotos con dron.',
    keywords='paseo en lancha Bariloche, navegación Nahuel Huapi, excursión lancha privada Bariloche, pesca con mosca Bariloche, Arelauquen',
    ld_type='TouristTrip', tourist=['Familias','Parejas','Grupos privados']),

  dict(slug='rutas-secretas', id='rutas', num='02', kicker=('Cordillera','Andes'), title=('Rutas Secretas','Secret Trails'),
    tag=('Cascadas, miradores y bosques de lengas que no figuran en ningún mapa.',
         'Waterfalls, viewpoints and beech forests that appear on no map.'),
    p1=('Lejos de los circuitos turísticos, la cordillera guarda senderos que solo conocen quienes la recorren hace años. Te llevamos en vehículo hasta el inicio de cada ruta y caminamos a un ritmo pensado para disfrutar, no para llegar.',
        'Far from the tourist circuits, the Andes hide trails known only to those who have walked them for years. We drive you to each trailhead and walk at a pace meant for enjoying, not arriving.'),
    p2=('Cada salida termina en un lugar especial: una cascada oculta, un mirador sobre el lago o una playa desierta, con un picnic patagónico para cerrar el día y el dron sobrevolando el paisaje para tus fotos y videos.',
        'Every outing ends somewhere special: a hidden waterfall, a lookout over the lake or a deserted beach, with a Patagonian picnic to close the day and the drone flying over the landscape for your photos and videos.'),
    p3=('Elegimos la ruta según el grupo y el clima: lagunas escondidas al pie de los cerros nevados, playas de piedra a las que solo se llega caminando, bosques de lengas centenarias. Sin multitudes, sin horarios ajenos, con la Patagonia entera para ustedes.',
        'We choose the route by group and weather: hidden lagoons at the foot of snowy peaks, stone beaches you only reach on foot, forests of century-old beech trees. No crowds, no one else’s schedule, the whole of Patagonia for you.'),
    facts=[('Duración','Duration','Medio día o día completo','Half or full day'),('Dificultad','Difficulty','Baja a media','Low to moderate'),('Grupo','Group','Grupos reducidos','Small groups'),('Temporada','Season','Dic — Mar','Dec — Mar')],
    inc=[('Caminatas a cascadas ocultas y miradores','Hikes to hidden waterfalls and viewpoints'),
         ('Traslado en vehículo hasta el inicio de cada ruta','Vehicle transfer to each trailhead'),
         ('Bosques de lengas y coihues fuera de los circuitos turísticos','Beech and coihue forests off the tourist circuits'),
         ('Picnic patagónico en el camino','Patagonian picnic along the way'),
         DRON],
    hero=dict(img='assets/img/lago-cordillera-nubes.jpg', alt=('Laguna escondida al pie de la cordillera con un cerro nevado de fondo','Hidden lagoon at the foot of the Andes with a snow-capped peak behind'), pos='center 60%'),
    card_img='assets/img/lago-cordillera-nubes.jpg',
    strip=[('assets/img/cala-turquesa.jpg', None, 'Cala de aguas turquesas entre acantilados y bosque','Turquoise cove between cliffs and forest'),
           ('assets/img/picos-lago.jpg', None, 'Paredones de granito sobre el lago turquesa, con la lancha en el centro','Granite walls over the turquoise lake, with the boat in the middle'),
           ('assets/video/lago-nevado.jpg', 'assets/video/lago-nevado.mp4', 'Laguna escondida con un cerro nevado de fondo, filmada desde el dron','Hidden lagoon with a snow-capped peak behind, filmed from the drone'),
           ('assets/img/brazo-lago-turquesa.jpg', None, 'Brazo del lago de aguas turquesas entre montañas de bosque, visto desde el dron','Turquoise arm of the lake between forested mountains, seen from the drone')],
    meta_title='Rutas Secretas: trekking privado en Bariloche | Lago Sur',
    meta_desc='Caminatas privadas a cascadas ocultas, miradores y bosques de lengas fuera de los circuitos turísticos de Bariloche. Con traslado, picnic y fotos con dron.',
    keywords='trekking Bariloche, caminatas privadas Bariloche, senderos secretos Patagonia, excursiones Arelauquen',
    ld_type='TouristTrip', tourist=['Familias','Parejas','Amantes del trekking']),

  dict(slug='casa-arelauquen', id='casa', num='03', kicker=('Alojamiento','Stay'), title=('Casa Acogedora','Cozy House'), soon=True,
    tag=('Un refugio de madera y hogar a leña dentro del barrio más exclusivo de Bariloche.',
         'A wood-and-fireplace refuge inside the most exclusive estate in Bariloche.'),
    p1=('La casa está pensada para hasta 6 personas que buscan tranquilidad y calidez. Madera noble, hogar a leña encendido al atardecer y ventanales que enmarcan el bosque y la cordillera.',
        'The house is designed for up to 6 guests looking for calm and warmth. Noble wood, a fireplace lit at sunset and windows that frame the forest and the Andes.'),
    p2=('Quedarse en Arelauquen significa acceder a la cancha de golf, a las áreas comunes del club y a la seguridad de un barrio privado con barrera las 24 horas, a 25 minutos del aeropuerto.',
        'Staying in Arelauquen means access to the golf course, the club common areas and the security of a gated estate with 24-hour access, 25 minutes from the airport.'),
    p3=('Estamos terminando de prepararla. Si querés que te avisemos cuando esté disponible, escribinos por WhatsApp y te reservamos prioridad para la temporada.',
        'We are finishing getting it ready. If you would like to be notified when it is available, message us on WhatsApp and we will hold priority for you this season.'),
    facts=[('Capacidad','Capacity','Hasta 6 personas','Up to 6 people'),('Ubicación','Location','Arelauquen','Arelauquen'),('Temporada','Season','Dic — Mar','Dec — Mar'),('Estado','Status','Próximamente','Coming soon')],
    inc=[('Alojamiento dentro del barrio privado Arelauquen','Accommodation inside the Arelauquen private estate'),
         ('Acceso a la cancha de golf y áreas comunes del club','Access to the golf course and club common areas'),
         ('WiFi de fibra y hogar a leña','Fiber WiFi and wood fireplace'),
         ('Welcome drink a la llegada','Welcome drink on arrival')],
    hero=dict(img='assets/img/arelauquen-golf.jpg', alt=('Cancha de golf de Arelauquen con el lago Nahuel Huapi y la cordillera','Arelauquen golf course with Lake Nahuel Huapi and the Andes'), pos='center 45%'),
    card_img='assets/img/arelauquen-golf.jpg',
    strip=[],
    meta_title='Casa en Arelauquen, Bariloche (próximamente) | Lago Sur',
    meta_desc='Casa para hasta 6 personas con hogar a leña dentro del barrio privado Arelauquen, Bariloche, con acceso al golf y al club. Próximamente.',
    keywords='alojamiento Arelauquen, casa Bariloche barrio privado, hospedaje golf Bariloche',
    ld_type='LodgingBusiness', tourist=[]),
]

# ───────────────────────────── helpers ─────────────────────────────
def li(items):
    return '\n'.join(f'            <li data-es="{es}" data-en="{en}">{es}</li>' for es, en in items)

def facts(items):
    return '\n'.join(f'''          <div class="xp-fact">
            <span class="xp-fact-label" data-es="{les}" data-en="{len_}">{les}</span>
            <strong data-es="{ves}" data-en="{ven}">{ves}</strong>
          </div>''' for les, len_, ves, ven in items)

def gitem(n, src, video, alt_es, alt_en):
    base = src.rsplit('.', 1)[0]
    if video:
        return f'''        <div class="gallery-item gallery-item--video fade-in" data-index="{n}"
             data-video="{video}" data-poster="{src}" onclick="openLightbox({n})">
          <img src="{src.replace('.jpg', '-thumb.jpg')}" loading="lazy" alt="{alt_es}" data-alt-es="{alt_es}" data-alt-en="{alt_en}">
          <span class="gallery-play" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M8 5.5v13l11-6.5z" fill="white"/></svg><em>Video</em></span>
          <div class="gallery-overlay"><svg viewBox="0 0 24 24" fill="none"><path d="M8 5.5v13l11-6.5z" fill="white"/></svg></div>
        </div>'''
    return f'''        <div class="gallery-item fade-in" data-index="{n}" onclick="openLightbox({n})">
          <img src="{base}-800.jpg" srcset="{base}-800.jpg 800w, {src} 1600w"
               sizes="(max-width: 600px) 100vw, 33vw" data-full="{src}" loading="lazy"
               alt="{alt_es}" data-alt-es="{alt_es}" data-alt-en="{alt_en}">
          <div class="gallery-overlay"><svg viewBox="0 0 24 24" fill="none"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        </div>'''

def hero_media(h, cls):
    if 'video' in h:
        return f'''    <video class="{cls}" muted loop playsinline preload="none" poster="{h['poster']}" aria-label="{h['alt'][0]}"
           data-src="{h['video']}" data-src-mobile="{h['video'].replace('.mp4', '-mobile.mp4')}"></video>'''
    base = h['img'].rsplit('.', 1)[0]
    return f'''    <img class="{cls}" src="{h['img']}" srcset="{base}-800.jpg 800w, {h['img']} 1600w" sizes="100vw" fetchpriority="high"
         style="object-position:{h.get('pos','center')}" alt="{h['alt'][0]}" data-alt-es="{h['alt'][0]}" data-alt-en="{h['alt'][1]}">'''

def head(title, desc, keywords, canonical_path, og_img, jsonld, preload_img=None):
    pre = f'  <link rel="preload" href="/{preload_img}" as="image" fetchpriority="high">\n' if preload_img else ''
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{BASE}/{canonical_path}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Lago Sur Experiences">
  <meta property="og:url" content="{BASE}/{canonical_path}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{BASE}/{og_img}">
  <meta property="og:image:alt" content="{title}">
  <meta property="og:locale" content="es_AR">
  <meta property="og:locale:alternate" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/{og_img}">
  <meta name="theme-color" content="#0a1a2e">

  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <script type="application/ld+json">
  {json.dumps(jsonld, ensure_ascii=False, indent=2).replace(chr(10), chr(10) + '  ')}
  </script>
  <link rel="preload" href="/assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/cormorant-garamond.woff2" as="font" type="font/woff2" crossorigin>
{pre}  <link rel="stylesheet" href="styles.css">
</head>
'''

def wa_msg(x):
    if x['slug'] == 'casa-arelauquen':
        return ('Hola, quiero que me avisen cuando la casa en Arelauquen esté disponible',
                'Hi, please let me know when the house in Arelauquen is available')
    return (f"Hola, quiero consultar por {x['title'][0]} con Lago Sur Experiences",
            f"Hi, I would like to ask about {x['title'][1]} with Lago Sur Experiences")

def contact_section(h2, lead):
    return f'''  <!-- ── CONTACTO ───────────────────────────────────────────────── -->
  <section id="contacto" class="contacto">
    <div class="container">
      <div class="contacto-simple fade-in">
        <p class="section-label" data-es="Hablemos" data-en="Let's talk">Hablemos</p>
        <h2 data-es="{h2[0]}" data-en="{h2[1]}">{h2[0]}</h2>
        <p class="contacto-lead" data-es="{lead[0]}" data-en="{lead[1]}">{lead[0]}</p>
        <div class="contacto-canales">
          <a href="#contacto" class="canal-item canal-whatsapp" target="_blank" rel="noopener">
            {WA_SVG}
            WhatsApp
          </a>
          <a href="/#reservar" class="canal-item" data-es="Ver calendario" data-en="See calendar">Ver calendario</a>
        </div>
      </div>
    </div>
  </section>

'''

def others_section(current):
    cards = []
    for x in XPS:
        if x['slug'] == current: continue
        base = x['card_img'].rsplit('.', 1)[0]
        soon = '<span class="exp-badge" data-es="Próximamente" data-en="Coming soon">Próximamente</span>' if x.get('soon') else ''
        cards.append(f'''        <a href="/{x['slug']}" class="xp-other fade-in">
          {soon}
          <img src="{base}-800.jpg" loading="lazy" alt="{x['title'][0]}" data-alt-es="{x['title'][0]}" data-alt-en="{x['title'][1]}">
          <div class="xp-other-body">
            <p class="section-label"><span class="xp-num">{x['num']}</span> · <span data-es="{x['kicker'][0]}" data-en="{x['kicker'][1]}">{x['kicker'][0]}</span></p>
            <h3 data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</h3>
            <span class="exp-cta" data-es="Ver experiencia" data-en="See experience">Ver experiencia</span>
          </div>
        </a>''')
    return f'''  <!-- ── OTRAS EXPERIENCIAS ─────────────────────────────────────── -->
  <section class="xp-others">
    <div class="container">
      <div class="section-header fade-in">
        <p class="section-label" data-es="Seguí explorando" data-en="Keep exploring">Seguí explorando</p>
        <h2 data-es="Otras experiencias" data-en="Other experiences">Otras experiencias</h2>
      </div>
      <div class="xp-others-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

'''

def ld_item(x):
    d = {"@type": x['ld_type'], "name": x['title'][0], "url": f"{BASE}/{x['slug']}",
         "image": f"{BASE}/{x['card_img']}", "description": x['meta_desc']}
    if x['ld_type'] == 'TouristTrip':
        d["touristType"] = x['tourist']
        d["provider"] = {"@type": "TravelAgency", "@id": BASE + "/#org", "name": "Lago Sur Experiences", "url": BASE + "/"}
        d["itinerary"] = {"@type": "Place", "name": "Arelauquen, Bariloche", "address": {"@type": "PostalAddress", "addressLocality": "Bariloche", "addressRegion": "Río Negro", "addressCountry": "AR"}}
    else:
        d["address"] = {"@type": "PostalAddress", "addressLocality": "Bariloche", "addressRegion": "Río Negro", "addressCountry": "AR"}
    return d

# ───────────────────────────── páginas individuales ─────────────────────────────
for x in XPS:
    soon = x.get('soon', False)
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Experiencias", "item": BASE + "/experiencias"},
            {"@type": "ListItem", "position": 3, "name": x['title'][0], "item": f"{BASE}/{x['slug']}"}]},
        ld_item(x)]}
    strip = '\n'.join(gitem(i, s, v, a, b) for i, (s, v, a, b) in enumerate(x['strip']))
    strip_section = f'''  <!-- ── GALERÍA ───────────────────────────────────────────────── -->
  <section class="xp-gallery">
    <div class="container">
      <div class="section-header fade-in">
        <p class="section-label" data-es="Desde el aire y desde el agua" data-en="From the air and from the water">Desde el aire y desde el agua</p>
        <h2 data-es="Galería" data-en="Gallery">Galería</h2>
      </div>
      <div class="xp-strip">
{strip}
      </div>
    </div>
  </section>

''' if x['strip'] else ''
    if soon:
        cta = '            <span class="exp-cta exp-cta--soon" data-es="Disponible próximamente" data-en="Available soon">Disponible próximamente</span>\n            <a href="#contacto" class="btn-hero xp-cta xp-cta-wa" target="_blank" rel="noopener" data-es="Avisame cuando esté lista" data-en="Notify me when it is ready">Avisame cuando esté lista</a>'
    else:
        cta = '            <a href="#contacto" class="btn-hero xp-cta xp-cta-wa" target="_blank" rel="noopener" data-es="Consultar por WhatsApp" data-en="Ask on WhatsApp">Consultar por WhatsApp</a>'
    badge = '    <span class="exp-badge xp-hero-badge" data-es="Próximamente" data-en="Coming soon">Próximamente</span>\n' if soon else ''
    page = head(x['meta_title'], x['meta_desc'], x['keywords'], x['slug'], x['card_img'], jsonld, x['hero'].get('poster')) + f'''<body class="page-experiencias page-xp" data-xp="{x['slug']}" data-wa-es="{wa_msg(x)[0]}" data-wa-en="{wa_msg(x)[1]}">

{nav_for(x['slug'])}
  <!-- ── HERO ──────────────────────────────────────────────────── -->
  <header class="xp-hero xp-hero--page">
{hero_media(x['hero'], 'xp-hero-img')}
    <div class="hero-overlay"></div>
{badge}    <div class="hero-content hero-in">
      <p class="hero-location"><span class="xp-num">{x['num']}</span> · <span data-es="{x['kicker'][0]}" data-en="{x['kicker'][1]}">{x['kicker'][0]}</span> · Arelauquen · Bariloche</p>
      <h1 class="hero-title" data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</h1>
      <p class="xp-hero-tag" data-es="{x['tag'][0]}" data-en="{x['tag'][1]}">{x['tag'][0]}</p>
    </div>
  </header>

  <!-- ── DETALLE ───────────────────────────────────────────────── -->
  <section class="xp-detail">
    <div class="container">
      <nav class="xp-crumbs fade-in" aria-label="Breadcrumb">
        <a href="/" data-es="Inicio" data-en="Home">Inicio</a><span>/</span><a href="/experiencias" data-es="Experiencias" data-en="Experiences">Experiencias</a><span>/</span><span data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</span>
      </nav>
      <div class="xp-detail-grid">
        <div class="xp-body fade-in">
          <p class="section-label" data-es="La experiencia" data-en="The experience">La experiencia</p>
          <p data-es="{x['p1'][0]}" data-en="{x['p1'][1]}">{x['p1'][0]}</p>
          <p data-es="{x['p2'][0]}" data-en="{x['p2'][1]}">{x['p2'][0]}</p>
          <p data-es="{x['p3'][0]}" data-en="{x['p3'][1]}">{x['p3'][0]}</p>
          <div class="xp-facts">
{facts(x['facts'])}
          </div>
        </div>
        <aside class="xp-aside fade-in">
          <div class="xp-aside-card">
            <p class="exp-incluye-label" data-es="Incluye" data-en="Includes">Incluye</p>
            <ul class="exp-incluye">
{li(x['inc'])}
            </ul>
{cta}
            <p class="xp-aside-note" data-es="Respondemos en el día por WhatsApp, en español o inglés." data-en="We reply same-day via WhatsApp, in Spanish or English.">Respondemos en el día por WhatsApp, en español o inglés.</p>
          </div>
        </aside>
      </div>
    </div>
  </section>

{strip_section}{others_section(x['slug'])}{contact_section(('Reservá esta experiencia','Book this experience'), ('Contanos en qué fechas venís y cuántos son. Te respondemos en el día por WhatsApp con disponibilidad y precios.','Tell us your dates and how many you are. We reply same-day via WhatsApp with availability and prices.'))}{foot2}
{fab}
{lightbox}  <script src="script.js"></script>
</body>
</html>
'''
    io.open(f"{x['slug']}.html", 'w', encoding='utf-8', newline='').write(page)
    print(f"{x['slug']}.html OK")

# ───────────────────────────── índice experiencias.html ─────────────────────────────
hub_cards = []
for i, x in enumerate(XPS):
    base = x['card_img'].rsplit('.', 1)[0]
    flip = ' xp-grid--flip' if i % 2 else ''
    soon = x.get('soon', False)
    badge = '          <span class="exp-badge" data-es="Próximamente" data-en="Coming soon">Próximamente</span>\n' if soon else ''
    btn_es, btn_en = ('Ver la casa', 'See the house') if soon else ('Ver experiencia', 'See experience')
    hub_cards.append(f'''  <article class="xp{' xp--soon' if soon else ''}" id="{x['id']}">
    <div class="container">
      <div class="xp-grid{flip}">
        <a href="/{x['slug']}" class="xp-media fade-in">
{badge}          <img class="xp-img" src="{x['card_img']}" srcset="{base}-800.jpg 800w, {x['card_img']} 1600w" sizes="(max-width: 1024px) 100vw, 50vw" loading="lazy"
               alt="{x['hero']['alt'][0]}" data-alt-es="{x['hero']['alt'][0]}" data-alt-en="{x['hero']['alt'][1]}">
        </a>
        <div class="xp-body fade-in">
          <p class="section-label"><span class="xp-num">{x['num']}</span> · <span data-es="{x['kicker'][0]}" data-en="{x['kicker'][1]}">{x['kicker'][0]}</span></p>
          <h2><a href="/{x['slug']}" data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</a></h2>
          <p class="xp-tagline" data-es="{x['tag'][0]}" data-en="{x['tag'][1]}">{x['tag'][0]}</p>
          <p data-es="{x['p1'][0]}" data-en="{x['p1'][1]}">{x['p1'][0]}</p>
          <div class="xp-facts">
{facts(x['facts'])}
          </div>
          <a href="/{x['slug']}" class="btn-hero xp-cta" data-es="{btn_es}" data-en="{btn_en}">{btn_es}</a>
        </div>
      </div>
    </div>
  </article>
''')

hub_ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Experiencias", "item": BASE + "/experiencias"}]},
    {"@type": "ItemList", "name": "Experiencias Lago Sur en Arelauquen, Bariloche",
     "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/{x['slug']}", "name": x['title'][0]} for i, x in enumerate(XPS)]}]}

hub = head('Experiencias privadas en Bariloche: lancha y trekking | Lago Sur',
           'Paseos privados en lancha por el Nahuel Huapi, pesca con mosca opcional y rutas secretas en la cordillera, desde Arelauquen, Bariloche. En español o inglés.',
           'experiencias Bariloche, paseo en lancha Nahuel Huapi, pesca con mosca Bariloche, trekking Bariloche, Arelauquen, turismo de lujo Patagonia, fotos con dron',
           'experiencias', 'og-image.jpg', hub_ld) + f'''<body class="page-experiencias">

{nav_for()}
  <!-- ── HERO ──────────────────────────────────────────────────── -->
  <header class="xp-hero">
    <img class="xp-hero-img" src="assets/img/cala-turquesa.jpg" srcset="assets/img/cala-turquesa-800.jpg 800w, assets/img/cala-turquesa.jpg 1600w" sizes="100vw"
         style="object-position:center 60%" alt="Cala de aguas turquesas entre acantilados y bosque en el lago Nahuel Huapi" data-alt-es="Cala de aguas turquesas entre acantilados y bosque en el lago Nahuel Huapi" data-alt-en="Turquoise cove between cliffs and forest on Lake Nahuel Huapi" fetchpriority="high">
    <div class="hero-overlay"></div>
    <div class="hero-content hero-in">
      <p class="hero-location">Arelauquen · Bariloche · Patagonia</p>
      <h1 class="hero-title" data-es="Las experiencias" data-en="The experiences">Las experiencias</h1>
      <p class="hero-sub" data-es="Tres maneras de vivir la Patagonia que pocos conocen" data-en="Three ways to live the Patagonia only few discover">Tres maneras de vivir la Patagonia que pocos conocen</p>
    </div>
  </header>

  <!-- ── INTRO ─────────────────────────────────────────────────── -->
  <section class="xp-intro">
    <div class="container">
      <div class="section-header fade-in">
        <p class="section-label" data-es="A medida, en grupos reducidos" data-en="Tailor-made, in small groups">A medida, en grupos reducidos</p>
        <p class="xp-intro-text"
           data-es="Lago Sur Experiences ofrece experiencias privadas en Arelauquen, Bariloche: paseos en lancha por el Nahuel Huapi (con pesca con mosca opcional), rutas secretas por la cordillera y, próximamente, alojamiento dentro del barrio privado. Todo se organiza a medida, en español o inglés, incluye fotos y videos con dron de tu jornada y se reserva por WhatsApp."
           data-en="Lago Sur Experiences offers private experiences in Arelauquen, Bariloche: boat tours on Lake Nahuel Huapi (with optional fly fishing), secret trails across the Andes and, coming soon, a house inside the private estate. Everything is tailor-made, in Spanish or English, includes drone photos and videos of your day and is booked via WhatsApp.">
          Lago Sur Experiences ofrece experiencias privadas en Arelauquen, Bariloche: paseos en lancha por el Nahuel Huapi (con pesca con mosca opcional), rutas secretas por la cordillera y, próximamente, alojamiento dentro del barrio privado. Todo se organiza a medida, en español o inglés, incluye fotos y videos con dron de tu jornada y se reserva por WhatsApp.
        </p>
        <nav class="xp-jump" aria-label="Experiencias">
          <a href="/paseo-en-lancha" data-es="Lancha" data-en="Boat">Lancha</a>
          <a href="/rutas-secretas"  data-es="Rutas"  data-en="Trails">Rutas</a>
          <a href="/casa-arelauquen"   data-es="Casa"   data-en="House">Casa</a>
        </nav>
      </div>
    </div>
  </section>

{''.join(hub_cards)}
{contact_section(('Armamos tu programa a medida','We tailor your program'), ('Contanos qué experiencias te interesan y en qué fechas. Te respondemos en el día por WhatsApp con disponibilidad y precios.','Tell us which experiences you are interested in and on which dates. We reply same-day via WhatsApp with availability and prices.'))}{foot2}
{fab}
{lightbox}  <script src="script.js"></script>
</body>
</html>
'''
io.open('experiencias.html', 'w', encoding='utf-8', newline='').write(hub)
print("experiencias.html OK")

# ───────────────────────────── privacidad.html ─────────────────────────────
from html import escape as esc

def t(tag, es, en, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} data-es="{esc(es)}" data-en="{esc(en)}">{esc(es)}</{tag}>'

PRIV = [
    ('h2', 'Quiénes somos', 'Who we are'),
    ('p', 'Lago Sur Experiences organiza experiencias privadas en Arelauquen, San Carlos de Bariloche, Río Negro, Argentina. Por cualquier consulta sobre tus datos, escribinos por WhatsApp al +54 9 11 7812-2900.',
          'Lago Sur Experiences runs private experiences in Arelauquen, San Carlos de Bariloche, Río Negro, Argentina. For any question about your data, message us on WhatsApp at +54 9 11 7812-2900.'),
    ('h2', 'Qué datos usamos', 'What data we use'),
    ('p', 'El sitio no tiene cuentas de usuario ni guarda formularios. El formulario de contacto y el calendario solo arman un mensaje que se envía desde tu propio WhatsApp.',
          'The site has no user accounts and does not store forms. The contact form and the calendar only compose a message that is sent from your own WhatsApp.'),
    ('p', 'Los datos que nos mandás por WhatsApp (nombre, fechas, cantidad de personas y lo que quieras contarnos) los usamos solo para responder tu consulta y organizar la experiencia. No los vendemos ni los compartimos con fines publicitarios.',
          'The details you send us on WhatsApp (name, dates, group size and anything else you tell us) are used only to answer your enquiry and organise the experience. We do not sell them or share them for advertising.'),
    ('h2', 'Cookies y medición', 'Cookies and measurement', 'cookies'),
    ('p', 'Usamos Google Analytics 4 para saber cuántas personas visitan el sitio y qué páginas miran, y Google Ads para saber si una consulta por WhatsApp llegó desde un anuncio. Estas herramientas pueden guardar cookies como _ga y _gcl_au.',
          'We use Google Analytics 4 to know how many people visit the site and which pages they view, and Google Ads to know whether a WhatsApp enquiry came from an ad. These tools may set cookies such as _ga and _gcl_au.'),
    ('p', 'Si estás en la Unión Europea, el Espacio Económico Europeo, el Reino Unido o Suiza, esas cookies solo se activan si las aceptás en el aviso. Si las rechazás, Google no guarda cookies y solo recibe señales sin identificadores (modo de consentimiento de Google).',
          'If you are in the European Union, the European Economic Area, the United Kingdom or Switzerland, these cookies are only set if you accept them in the notice. If you reject them, Google stores no cookies and only receives signals without identifiers (Google Consent Mode).'),
    ('p', 'El sitio también guarda en tu navegador el idioma elegido y tu decisión sobre las cookies. Eso queda en tu dispositivo y no se envía a nadie.',
          'The site also stores your chosen language and your cookie choice in your browser. That stays on your device and is not sent to anyone.'),
    ('h2', 'Servicios de terceros', 'Third-party services'),
    ('li', 'Vercel: aloja el sitio.', 'Vercel: hosts the site.'),
    ('li', 'Google: Analytics y Ads, según lo que elijas sobre las cookies.', 'Google: Analytics and Ads, according to your cookie choice.'),
    ('li', 'WhatsApp (Meta): recibe los mensajes que nos mandás.', 'WhatsApp (Meta): carries the messages you send us.'),
    ('li', 'Esri: imágenes satelitales del mapa de lagos.', 'Esri: satellite imagery for the lakes map.'),
    ('li', 'jsDelivr: carga el visor de fotos 360°.', 'jsDelivr: loads the 360° photo viewer.'),
    ('h2', 'Tus derechos', 'Your rights'),
    ('p', 'Podés pedirnos por WhatsApp acceder a tus datos, corregirlos o borrarlos. En Argentina rige la Ley 25.326 de Protección de Datos Personales y la autoridad de control es la Agencia de Acceso a la Información Pública. Si estás en la Unión Europea o el Reino Unido también tenés los derechos del RGPD y podés reclamar ante la autoridad de protección de datos de tu país.',
          'You can ask us on WhatsApp to access, correct or delete your data. Argentine Personal Data Protection Law 25.326 applies, and the supervisory authority is the Agencia de Acceso a la Información Pública. If you are in the European Union or the United Kingdom you also have your GDPR rights and may complain to your country’s data protection authority.'),
    ('h2', 'Cambiar tu elección de cookies', 'Change your cookie choice'),
    ('p', 'Podés cambiar tu decisión cuando quieras con este botón o con el link “Cookies” al pie de cada página.',
          'You can change your choice at any time with this button or with the “Cookies” link at the bottom of every page.'),
]

body_parts, in_list = [], False
for item in PRIV:
    tag, es, en = item[:3]
    if tag == 'li' and not in_list:
        body_parts.append('      <ul>'); in_list = True
    if tag != 'li' and in_list:
        body_parts.append('      </ul>'); in_list = False
    html = t(tag, es, en)
    if len(item) > 3:
        html = html.replace(f'<{tag} ', f'<{tag} id="{item[3]}" ', 1)
    body_parts.append(('        ' if tag == 'li' else '      ') + html)
if in_list:
    body_parts.append('      </ul>')

priv_ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Privacidad y cookies",
           "url": BASE + "/privacidad", "isPartOf": {"@id": BASE + "/#org"}}

priv = head('Privacidad y cookies | Lago Sur Experiences',
            'Qué datos usa Lago Sur Experiences, cómo funcionan las cookies de Google Analytics y Google Ads y cómo cambiar tu elección.',
            'privacidad, cookies, Lago Sur Experiences',
            'privacidad', 'og-image.jpg', priv_ld) + f'''<body class="page-privacidad">

{nav_for()}
  <!-- ── HERO ──────────────────────────────────────────────────── -->
  <header class="xp-hero" style="min-height:44vh">
    <img class="xp-hero-img" src="assets/img/lago-montanas.jpg" srcset="assets/img/lago-montanas-800.jpg 800w, assets/img/lago-montanas.jpg 1600w" sizes="100vw"
         alt="" fetchpriority="high">
    <div class="hero-overlay"></div>
    <div class="hero-content hero-in">
      <h1 class="hero-title" data-es="Privacidad y cookies" data-en="Privacy and cookies">Privacidad y cookies</h1>
    </div>
  </header>

  <!-- ── CONTENIDO ─────────────────────────────────────────────── -->
  <section class="legal">
    <div class="container">
{chr(10).join(body_parts)}
      <button type="button" class="btn-hero" data-cookie-settings data-es="Configurar cookies" data-en="Cookie settings">Configurar cookies</button>
      {t('p', 'Última actualización: 29 de septiembre de 2026', 'Last updated: September 29, 2026', 'legal-updated')}
    </div>
  </section>

{foot2}
{fab}
{lightbox}  <script src="script.js"></script>
</body>
</html>
'''
io.open('privacidad.html', 'w', encoding='utf-8', newline='').write(priv)
print("privacidad.html OK")
