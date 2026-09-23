# Genera experiencias.html (índice) + una página por experiencia a partir de index.html
import io, json

BASE = 'https://lago-sur-experiences.vercel.app'
idx = io.open('index.html', encoding='utf-8').read()

def block(start, end, inclusive_end=True):
    i = idx.index(start); j = idx.index(end, i)
    return idx[i: j + (len(end) if inclusive_end else 0)]

nav      = block('  <!-- ── NAVBAR', '</nav>\n')
footer   = block('  <!-- ── FOOTER', '</footer>\n')
fab      = block('  <!-- ── WHATSAPP FAB', '  </a>\n')
lightbox = block('  <!-- ── LIGHTBOX', '  <script src="https://unpkg.com/leaflet', False)
WA_SVG   = fab[fab.index('<svg'):fab.index('</svg>') + 6]

def nav_for(active_slug=None):
    n = (nav.replace('href="#inicio"', 'href="index.html"')
            .replace('href="#sobre"', 'href="index.html#sobre"')
            .replace('href="#experiencias" class="nav-drop-trigger"', 'href="experiencias.html" class="nav-drop-trigger active"')
            .replace('href="#guias"', 'href="index.html#guias"')
            .replace('href="#galeria"', 'href="index.html#galeria"')
            .replace('href="#faq"', 'href="index.html#faq"'))
    if active_slug:
        n = n.replace(f'<a href="{active_slug}.html"', f'<a href="{active_slug}.html" class="active"')
    return n

foot2 = (footer.replace('href="#sobre"', 'href="index.html#sobre"')
               .replace('href="#galeria"', 'href="index.html#galeria"'))

DRON = ('Fotos y videos con dron de tu jornada', 'Drone photos and videos of your day')

XPS = [
  dict(slug='paseo-en-lancha', id='lancha', num='01', kicker=('Lago','Lake'), title=('Paseo en Lancha','Boat Tour'),
    tag=('El Nahuel Huapi desde el agua: bahías, islas y calas turquesa a las que no llega ningún camino.',
         'Nahuel Huapi from the water: bays, islands and turquoise coves no road can reach.'),
    p1=('Salimos en nuestra lancha privada, con capacidad para hasta seis personas, y dejamos atrás el ruido del centro. En pocos minutos el lago se abre en brazos y bahías que solo se conocen navegando.',
        'We set out on our private boat, with room for up to six people, and leave the noise of downtown behind. Within minutes the lake opens into arms and bays you only get to know by sailing.'),
    p2=('El recorrido se arma según el día y el grupo: una cala de agua turquesa para nadar, una playa escondida para un picnic, o simplemente apagar el motor y escuchar el silencio de la cordillera. Mientras tanto, el dron registra la salida desde el aire para que te lleves las fotos y los videos.',
        'The route is shaped by the day and the group: a turquoise cove for a swim, a hidden beach for a picnic, or simply cutting the engine to listen to the silence of the Andes. Meanwhile, the drone captures the outing from above so you take the photos and videos home.'),
    p3=('No hay dos salidas iguales. Si el viento acompaña cruzamos a las islas; si el lago está planchado buscamos las calas del brazo norte, donde el agua se pone transparente y las montañas se reflejan enteras. Cerramos siempre con el atardecer sobre la cordillera.',
        'No two outings are alike. If the wind allows we cross to the islands; if the lake is glassy we head for the coves of the northern arm, where the water turns transparent and the mountains reflect in full. We always close with sunset over the Andes.'),
    facts=[('Duración','Duration','Medio día','Half day'),('Grupo','Group','Hasta 6 personas','Up to 6 people'),('Temporada','Season','Dic — Mar','Dec — Mar'),('Idiomas','Languages','ES · EN','ES · EN')],
    inc=[('Lancha privada para hasta 6 personas','Private boat for up to 6 people'),
         ('Recorrido por bahías, islas y rincones del Nahuel Huapi','Route through bays, islands and hidden corners of Nahuel Huapi'),
         ('Chalecos y equipo de seguridad a bordo','Life jackets and safety gear on board'),
         ('Parada para nadar o hacer picnic en una playa escondida','Stop to swim or picnic on a hidden beach'),
         DRON],
    hero=dict(video='assets/video/lanchas-navegando.mp4', poster='assets/video/lanchas-navegando.jpg',
              alt=('Lanchas navegando a toda velocidad por el lago Nahuel Huapi','Boats speeding across Lake Nahuel Huapi')),
    card_img='assets/img/playa-turquesa-aerea.jpg',
    strip=[('assets/img/lancha-estela.jpg', None, 'Lancha navegando el lago Nahuel Huapi entre islas','Boat cruising Lake Nahuel Huapi between islands'),
           ('assets/img/playa-turquesa-aerea.jpg', None, 'Vista aérea con dron de una playa escondida con la lancha fondeada','Drone aerial view of a hidden beach with the boat anchored'),
           ('assets/img/gomones-agua-turquesa.jpg', None, 'El grupo en los gomones sobre aguas turquesas','The group on the rafts over turquoise waters'),
           ('assets/video/costa-turquesa.jpg', 'assets/video/costa-turquesa.mp4', 'Nadando en aguas transparentes junto a una roca, con la cordillera de fondo','Swimming in crystal-clear water by a rock, with the Andes behind'),
           ('assets/img/cala-turquesa.jpg', None, 'Cala de aguas turquesas entre acantilados y bosque','Turquoise cove between cliffs and forest'),
           ('assets/img/lago-orilla-aerea.jpg', None, 'Vista aérea con dron de la orilla y los bajos turquesa del lago','Drone aerial view of the shore and the turquoise shallows')],
    meta_title='Paseo en Lancha por el Nahuel Huapi | Lago Sur Experiences · Bariloche',
    meta_desc='Navegación privada por bahías, islas y calas turquesa del lago Nahuel Huapi desde Arelauquen, Bariloche. Lancha para hasta 6 personas, medio día, fotos y videos con dron incluidos.',
    keywords='paseo en lancha Bariloche, navegación Nahuel Huapi, excursión lancha privada Bariloche, Arelauquen',
    ld_type='TouristTrip', tourist=['Familias','Parejas','Grupos privados']),

  dict(slug='pesca-con-mosca', id='pesca', num='02', kicker=('Pesca','Fishing'), title=('Pesca con Mosca','Fly Fishing'),
    tag=('Truchas marrón y arco iris en aguas donde casi nadie lanza una línea.',
         'Brown and rainbow trout in waters where almost no one casts a line.'),
    p1=('La Patagonia norte es uno de los grandes destinos de pesca con mosca del mundo. Nosotros la vivimos desde adentro: bocas de río, orillas del lago y pozones que Francisco conoce desde los siete años.',
        'Northern Patagonia is one of the great fly-fishing destinations in the world. We live it from the inside: river mouths, lake shores and pools Francisco has known since he was seven.'),
    p2=('Proveemos todo el equipo técnico y adaptamos la jornada a tu nivel, desde el primer lanzamiento hasta la búsqueda de una trucha grande. La salida se hace en lancha o con vadeo, según el spot del día, y el dron registra las mejores capturas.',
        'We provide all the technical gear and adapt the day to your level, from your first cast to chasing a trophy trout. Outings are by boat or wading, depending on the spot of the day, and the drone captures the best catches.'),
    p3=('Pescamos con devolución, con moscas atadas para las aguas de la zona y respetando los reglamentos de temporada. Si es tu primera vez, la mañana arranca con una clase corta en la orilla; si ya pescás, vamos directo a los lugares que pocos conocen.',
        'We fish catch-and-release, with flies tied for local waters and in line with seasonal regulations. If it is your first time, the morning starts with a short lesson on the shore; if you already fish, we go straight to the spots few people know.'),
    facts=[('Duración','Duration','Día completo','Full day'),('Grupo','Group','Grupos reducidos','Small groups'),('Temporada','Season','Dic — Mar','Dec — Mar'),('Nivel','Level','Todos los niveles','All levels')],
    inc=[('Equipo técnico completo: cañas, moscas y waders','Full technical gear: rods, flies and waders'),
         ('Salida en lancha o vadeo según el spot del día','Boat or wading outing depending on the spot of the day'),
         ('Truchas marrón y arco iris en aguas de lago y río','Brown and rainbow trout in lake and river waters'),
         ('Modalidad pesca con devolución','Catch and release'),
         DRON],
    hero=dict(img='assets/img/lago-montanas.jpg', alt=('Lago y cordillera al atardecer con una lancha','Lake and Andes at sunset with a boat'), pos='center 55%'),
    card_img='assets/img/lago-montanas.jpg',
    strip=[('assets/img/atardecer-bote.jpg', None, 'El grupo a bordo del bote al atardecer','The group aboard the boat at sunset'),
           ('assets/img/lago-orilla-aerea.jpg', None, 'Vista aérea con dron de la orilla y los bajos turquesa del lago','Drone aerial view of the shore and the turquoise shallows'),
           ('assets/video/playa-grupo.jpg', 'assets/video/playa-grupo.mp4', 'El grupo en una playa escondida del lago','The group on a hidden lake beach'),
           ('assets/video/orilla-piedras.jpg', 'assets/video/orilla-piedras.mp4', 'Orilla de piedras y troncos con agua transparente, vista desde el dron','Stony shore with driftwood and crystal-clear water, seen from the drone')],
    meta_title='Pesca con Mosca en Bariloche | Lago Sur Experiences · Arelauquen',
    meta_desc='Jornada privada de pesca con mosca de truchas marrón y arco iris en lagos y ríos de la Patagonia norte. Equipo completo incluido, todos los niveles, pesca con devolución, fotos y videos con dron.',
    keywords='pesca con mosca Bariloche, fly fishing Bariloche, pesca de truchas Patagonia, guía de pesca Nahuel Huapi',
    ld_type='TouristTrip', tourist=['Pescadores','Principiantes','Expertos']),

  dict(slug='rutas-secretas', id='rutas', num='03', kicker=('Cordillera','Andes'), title=('Rutas Secretas','Secret Trails'),
    tag=('Cascadas, miradores y bosques de lengas que no figuran en ningún mapa.',
         'Waterfalls, viewpoints and beech forests that appear on no map.'),
    p1=('Lejos de los circuitos turísticos, la cordillera guarda senderos que solo conocen quienes crecieron acá. Te llevamos en vehículo hasta el inicio de cada ruta y caminamos a un ritmo pensado para disfrutar, no para llegar.',
        'Far from the tourist circuits, the Andes hide trails known only to those who grew up here. We drive you to each trailhead and walk at a pace meant for enjoying, not arriving.'),
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
           ('assets/video/playa-rocas.jpg', 'assets/video/playa-rocas.mp4', 'Pareja saludando al dron en una playa de piedras del lago','Couple waving at the drone on a stony lake beach'),
           ('assets/video/lago-nevado.jpg', 'assets/video/lago-nevado.mp4', 'Laguna escondida con un cerro nevado de fondo, filmada desde el dron','Hidden lagoon with a snow-capped peak behind, filmed from the drone')],
    meta_title='Rutas Secretas en la cordillera de Bariloche | Lago Sur Experiences',
    meta_desc='Caminatas privadas a cascadas ocultas, miradores y bosques de lengas fuera de los circuitos turísticos de Bariloche. Traslado, picnic patagónico y fotos y videos con dron incluidos.',
    keywords='trekking Bariloche, caminatas privadas Bariloche, senderos secretos Patagonia, excursiones Arelauquen',
    ld_type='TouristTrip', tourist=['Familias','Parejas','Amantes del trekking']),

  dict(slug='casa-arelauquen', id='casa', num='04', kicker=('Alojamiento','Stay'), title=('Casa Acogedora','Cozy House'), soon=True,
    tag=('Un refugio de madera y hogar a leña dentro del barrio más exclusivo de Bariloche.',
         'A wood-and-fireplace refuge inside the most exclusive estate in Bariloche.'),
    p1=('La casa está pensada para grupos chicos que buscan tranquilidad antes que ostentación. Madera noble, hogar a leña encendido al atardecer y ventanales que enmarcan el bosque y la cordillera.',
        'The house is designed for small groups who value calm over ostentation. Noble wood, a fireplace lit at sunset and windows that frame the forest and the Andes.'),
    p2=('Quedarse en Arelauquen significa acceder a la cancha de golf, a las áreas comunes del club y a la seguridad de un barrio privado con barrera las 24 horas, a 25 minutos del aeropuerto.',
        'Staying in Arelauquen means access to the golf course, the club common areas and the security of a gated estate with 24-hour access, 25 minutes from the airport.'),
    p3=('Estamos terminando de prepararla. Si querés que te avisemos cuando esté disponible, escribinos por WhatsApp y te reservamos prioridad para la temporada.',
        'We are finishing getting it ready. If you would like to be notified when it is available, message us on WhatsApp and we will hold priority for you this season.'),
    facts=[('Capacidad','Capacity','Grupos chicos','Small groups'),('Ubicación','Location','Arelauquen','Arelauquen'),('Temporada','Season','Dic — Mar','Dec — Mar'),('Estado','Status','Próximamente','Coming soon')],
    inc=[('Alojamiento dentro del barrio privado Arelauquen','Accommodation inside the Arelauquen private estate'),
         ('Acceso a la cancha de golf y áreas comunes del club','Access to the golf course and club common areas'),
         ('WiFi de fibra y hogar a leña','Fiber WiFi and wood fireplace'),
         ('Traslado desde el aeropuerto y welcome drink','Airport transfer and welcome drink')],
    hero=dict(img='assets/img/arelauquen-golf.jpg', alt=('Cancha de golf de Arelauquen con el lago Nahuel Huapi y la cordillera','Arelauquen golf course with Lake Nahuel Huapi and the Andes'), pos='center 45%'),
    card_img='assets/img/arelauquen-golf.jpg',
    strip=[],
    meta_title='Casa en Arelauquen, Bariloche (próximamente) | Lago Sur Experiences',
    meta_desc='Casa íntima con hogar a leña dentro del barrio privado Arelauquen, Bariloche, con acceso a la cancha de golf y al club. Próximamente. Consultá por WhatsApp.',
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
          <img src="{src}" loading="lazy" alt="{alt_es}" data-alt-es="{alt_es}" data-alt-en="{alt_en}">
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
        return f'''    <video class="{cls}" autoplay muted loop playsinline preload="metadata" poster="{h['poster']}" aria-label="{h['alt'][0]}">
      <source src="{h['video']}" type="video/mp4">
    </video>'''
    base = h['img'].rsplit('.', 1)[0]
    return f'''    <img class="{cls}" src="{h['img']}" srcset="{base}-800.jpg 800w, {h['img']} 1600w" sizes="100vw" fetchpriority="high"
         style="object-position:{h.get('pos','center')}" alt="{h['alt'][0]}" data-alt-es="{h['alt'][0]}" data-alt-en="{h['alt'][1]}">'''

def head(title, desc, keywords, canonical_path, og_img, jsonld):
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
  <meta property="og:locale" content="es_AR">
  <meta property="og:locale:alternate" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/{og_img}">
  <meta name="theme-color" content="#0a1a2e">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <script type="application/ld+json">
  {json.dumps(jsonld, ensure_ascii=False, indent=2).replace(chr(10), chr(10) + '  ')}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
'''

def contact_section(h2, lead):
    return f'''  <!-- ── CONTACTO ───────────────────────────────────────────────── -->
  <section id="contacto" class="contacto">
    <div class="container">
      <div class="contacto-simple fade-in">
        <p class="section-label" data-es="Hablemos" data-en="Let's talk">Hablemos</p>
        <h2 data-es="{h2[0]}" data-en="{h2[1]}">{h2[0]}</h2>
        <p class="contacto-lead" data-es="{lead[0]}" data-en="{lead[1]}">{lead[0]}</p>
        <div class="contacto-canales">
          <a href="https://wa.me/+54XXXXXXXXXX" class="canal-item canal-whatsapp" target="_blank" rel="noopener">
            {WA_SVG}
            WhatsApp
          </a>
          <a href="index.html#reservar" class="canal-item" data-es="Ver calendario" data-en="See calendar">Ver calendario</a>
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
        cards.append(f'''        <a href="{x['slug']}.html" class="xp-other fade-in">
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
    d = {"@type": x['ld_type'], "name": x['title'][0], "url": f"{BASE}/{x['slug']}.html",
         "image": f"{BASE}/{x['card_img']}", "description": x['meta_desc']}
    if x['ld_type'] == 'TouristTrip':
        d["touristType"] = x['tourist']
        d["provider"] = {"@type": "Organization", "name": "Lago Sur Experiences", "url": BASE + "/"}
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
            {"@type": "ListItem", "position": 2, "name": "Experiencias", "item": BASE + "/experiencias.html"},
            {"@type": "ListItem", "position": 3, "name": x['title'][0], "item": f"{BASE}/{x['slug']}.html"}]},
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
        cta = '            <span class="exp-cta exp-cta--soon" data-es="Disponible próximamente" data-en="Available soon">Disponible próximamente</span>\n            <a href="#contacto" class="btn-hero xp-cta" data-es="Avisame cuando esté lista" data-en="Notify me when it is ready">Avisame cuando esté lista</a>'
    else:
        cta = '            <a href="#contacto" class="btn-hero xp-cta" data-es="Consultar esta experiencia" data-en="Inquire about this experience">Consultar esta experiencia</a>'
    badge = '    <span class="exp-badge xp-hero-badge" data-es="Próximamente" data-en="Coming soon">Próximamente</span>\n' if soon else ''
    page = head(x['meta_title'], x['meta_desc'], x['keywords'], f"{x['slug']}.html", x['card_img'], jsonld) + f'''<body class="page-experiencias page-xp">

{nav_for(x['slug'])}
  <!-- ── HERO ──────────────────────────────────────────────────── -->
  <header class="xp-hero xp-hero--page">
{hero_media(x['hero'], 'xp-hero-img')}
    <div class="hero-overlay"></div>
{badge}    <div class="hero-content fade-in">
      <p class="hero-location"><span class="xp-num">{x['num']}</span> · <span data-es="{x['kicker'][0]}" data-en="{x['kicker'][1]}">{x['kicker'][0]}</span> · Arelauquen · Bariloche</p>
      <h1 class="hero-title" data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</h1>
      <p class="xp-hero-tag" data-es="{x['tag'][0]}" data-en="{x['tag'][1]}">{x['tag'][0]}</p>
    </div>
  </header>

  <!-- ── DETALLE ───────────────────────────────────────────────── -->
  <section class="xp-detail">
    <div class="container">
      <nav class="xp-crumbs fade-in" aria-label="Breadcrumb">
        <a href="index.html" data-es="Inicio" data-en="Home">Inicio</a><span>/</span><a href="experiencias.html" data-es="Experiencias" data-en="Experiences">Experiencias</a><span>/</span><span data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</span>
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
        <a href="{x['slug']}.html" class="xp-media fade-in">
{badge}          <img class="xp-img" src="{x['card_img']}" srcset="{base}-800.jpg 800w, {x['card_img']} 1600w" sizes="(max-width: 1024px) 100vw, 50vw" loading="lazy"
               alt="{x['hero']['alt'][0]}" data-alt-es="{x['hero']['alt'][0]}" data-alt-en="{x['hero']['alt'][1]}">
        </a>
        <div class="xp-body fade-in">
          <p class="section-label"><span class="xp-num">{x['num']}</span> · <span data-es="{x['kicker'][0]}" data-en="{x['kicker'][1]}">{x['kicker'][0]}</span></p>
          <h2><a href="{x['slug']}.html" data-es="{x['title'][0]}" data-en="{x['title'][1]}">{x['title'][0]}</a></h2>
          <p class="xp-tagline" data-es="{x['tag'][0]}" data-en="{x['tag'][1]}">{x['tag'][0]}</p>
          <p data-es="{x['p1'][0]}" data-en="{x['p1'][1]}">{x['p1'][0]}</p>
          <div class="xp-facts">
{facts(x['facts'])}
          </div>
          <a href="{x['slug']}.html" class="btn-hero xp-cta" data-es="{btn_es}" data-en="{btn_en}">{btn_es}</a>
        </div>
      </div>
    </div>
  </article>
''')

hub_ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Experiencias", "item": BASE + "/experiencias.html"}]},
    {"@type": "ItemList", "name": "Experiencias Lago Sur en Arelauquen, Bariloche",
     "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/{x['slug']}.html", "name": x['title'][0]} for i, x in enumerate(XPS)]}]}

hub = head('Experiencias en Bariloche: lancha, pesca con mosca y rutas secretas | Lago Sur Experiences',
           'Paseos privados en lancha por el Nahuel Huapi, pesca con mosca y rutas secretas en la cordillera, desde Arelauquen, Bariloche. Grupos reducidos, español e inglés, fotos y videos con dron incluidos. Reserva por WhatsApp.',
           'experiencias Bariloche, paseo en lancha Nahuel Huapi, pesca con mosca Bariloche, trekking Bariloche, Arelauquen, turismo de lujo Patagonia, fotos con dron',
           'experiencias.html', 'og-image.jpg', hub_ld) + f'''<body class="page-experiencias">

{nav_for()}
  <!-- ── HERO ──────────────────────────────────────────────────── -->
  <header class="xp-hero">
    <img class="xp-hero-img" src="assets/img/lago-orilla-aerea.jpg" srcset="assets/img/lago-orilla-aerea-800.jpg 800w, assets/img/lago-orilla-aerea.jpg 1600w" sizes="100vw"
         alt="Vista aérea con dron de la orilla y los bajos turquesa del lago Nahuel Huapi" data-alt-es="Vista aérea con dron de la orilla y los bajos turquesa del lago Nahuel Huapi" data-alt-en="Drone aerial view of the shore and turquoise shallows of Lake Nahuel Huapi" fetchpriority="high">
    <div class="hero-overlay"></div>
    <div class="hero-content fade-in">
      <p class="hero-location">Arelauquen · Bariloche · Patagonia</p>
      <h1 class="hero-title" data-es="Las experiencias" data-en="The experiences">Las experiencias</h1>
      <p class="hero-sub" data-es="Cuatro maneras de vivir la Patagonia que pocos conocen" data-en="Four ways to live the Patagonia only few discover">Cuatro maneras de vivir la Patagonia que pocos conocen</p>
    </div>
  </header>

  <!-- ── INTRO ─────────────────────────────────────────────────── -->
  <section class="xp-intro">
    <div class="container">
      <div class="section-header fade-in">
        <p class="section-label" data-es="A medida, en grupos reducidos" data-en="Tailor-made, in small groups">A medida, en grupos reducidos</p>
        <p class="xp-intro-text"
           data-es="Lago Sur Experiences ofrece experiencias privadas en Arelauquen, Bariloche: paseos en lancha por el Nahuel Huapi, pesca con mosca, rutas secretas por la cordillera y, próximamente, alojamiento dentro del barrio privado. Todo se organiza a medida, en español o inglés, incluye fotos y videos con dron de tu jornada y se reserva por WhatsApp."
           data-en="Lago Sur Experiences offers private experiences in Arelauquen, Bariloche: boat tours on Lake Nahuel Huapi, fly fishing, secret trails across the Andes and, coming soon, a house inside the private estate. Everything is tailor-made, in Spanish or English, includes drone photos and videos of your day and is booked via WhatsApp.">
          Lago Sur Experiences ofrece experiencias privadas en Arelauquen, Bariloche: paseos en lancha por el Nahuel Huapi, pesca con mosca, rutas secretas por la cordillera y, próximamente, alojamiento dentro del barrio privado. Todo se organiza a medida, en español o inglés, incluye fotos y videos con dron de tu jornada y se reserva por WhatsApp.
        </p>
        <nav class="xp-jump" aria-label="Experiencias">
          <a href="paseo-en-lancha.html" data-es="Lancha" data-en="Boat">Lancha</a>
          <a href="pesca-con-mosca.html"  data-es="Pesca"  data-en="Fishing">Pesca</a>
          <a href="rutas-secretas.html"  data-es="Rutas"  data-en="Trails">Rutas</a>
          <a href="casa-arelauquen.html"   data-es="Casa"   data-en="House">Casa</a>
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
