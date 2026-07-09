"""
Globo 3D interativo com mapa-múndi REAL (Globe.gl / Three.js) para o
Calculadora de Impacto Ambiental. Usa a mesma base de globo do projeto
earth-max-min-temp-history (textura de terra real + fronteiras de países
via GeoJSON), mantendo o layout e paleta verde/âmbar/vermelho.
Renderizado via st.components.v1.html — reage em tempo real ao nível de
impacto e às categorias já respondidas, com hotspots pulsantes por país.
"""

import streamlit.components.v1 as components
import json


def render_globe_3d(impact_level: float, category_breakdown: dict, height: int = 460, key: str = "globe"):
    """
    impact_level: float 0..1 — nível geral de impacto (0 = sustentável, 1 = crítico)
    category_breakdown: dict {category_title: points_normalized_0_1} usado para os hotspots
    """
    hotspots = json.dumps(category_breakdown)

    html = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://unpkg.com/globe.gl"></script>
<style>
  html, body {{ margin:0; padding:0; background: transparent; overflow: hidden; }}
  #wrap {{ position: relative; width: 100%; height: {height}px; }}
  #globeViz {{ width: 100%; height: 100%; }}
  #hud {{
    position: absolute; top: 12px; left: 16px;
    font-family: 'JetBrains Mono', monospace;
    color: #7fffd4; font-size: 11px; letter-spacing: 0.08em;
    text-transform: uppercase; opacity: 0.85; pointer-events: none; z-index: 10;
  }}
  #hud .val {{ color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: 0; display:block; margin-top:2px; }}
  #legend {{
    position: absolute; bottom: 10px; right: 14px;
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: rgba(255,255,255,0.5); text-align: right; pointer-events: none; z-index: 10;
  }}
</style>
</head>
<body>
<div id="wrap">
  <div id="globeViz"></div>
  <div id="hud">Índice de Pressão<span class="val" id="hud-val">--</span></div>
  <div id="legend">arraste para girar · scroll para zoom</div>
</div>

<script>
(function() {{
  const IMPACT = {impact_level};
  const HOTSPOTS = {hotspots};

  document.getElementById('hud-val').textContent = Math.round(IMPACT * 100) + '%';

  function lerpColor(a, b, t) {{
    const ah = parseInt(a.slice(1), 16), bh = parseInt(b.slice(1), 16);
    const ar = (ah >> 16) & 0xff, ag = (ah >> 8) & 0xff, ab = ah & 0xff;
    const br = (bh >> 16) & 0xff, bg = (bh >> 8) & 0xff, bb = bh & 0xff;
    const r = Math.round(ar + (br - ar) * t);
    const g = Math.round(ag + (bg - ag) * t);
    const b_ = Math.round(ab + (bb - ab) * t);
    return '#' + [r, g, b_].map(x => x.toString(16).padStart(2, '0')).join('');
  }}

  let ringColor;
  if (IMPACT < 0.5) {{
    ringColor = lerpColor('#00e5a0', '#ffb347', IMPACT / 0.5);
  }} else {{
    ringColor = lerpColor('#ffb347', '#ff5470', (IMPACT - 0.5) / 0.5);
  }}

  const CATEGORY_COORDS = {{
    "Mobilidade": {{ lat: -15, lng: -47 }},
    "Alimentação": {{ lat: 40, lng: -100 }},
    "Consumo de Moda": {{ lat: 22, lng: 114 }},
    "Tecnologia": {{ lat: 37, lng: -122 }},
    "Energia": {{ lat: 51, lng: 9 }}
  }};

  const ringsData = Object.keys(HOTSPOTS).map(cat => {{
    const coord = CATEGORY_COORDS[cat];
    if (!coord) return null;
    const intensity = HOTSPOTS[cat];
    return {{
      lat: coord.lat,
      lng: coord.lng,
      cat: cat,
      intensity: intensity,
      color: lerpColor('#00e5a0', '#ff5470', intensity),
      maxR: 4 + intensity * 5,
      propagationSpeed: 1.2 + intensity,
      repeatPeriod: 1600 - intensity * 700
    }};
  }}).filter(Boolean);

  const pointsData = ringsData.map(r => ({{ ...r, size: 0.6 + r.intensity * 0.9 }}));

  const wrap = document.getElementById('wrap');
  const world = Globe()
    (document.getElementById('globeViz'))
    .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-dark.jpg')
    .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png')
    .backgroundColor('rgba(0,0,0,0)')
    .showAtmosphere(true)
    .atmosphereColor(ringColor)
    .atmosphereAltitude(0.22)
    .polygonAltitude(0.006)
    .polygonCapColor(() => 'rgba(20, 30, 50, 0.25)')
    .polygonSideColor(() => 'rgba(0, 0, 0, 0.08)')
    .polygonStrokeColor(() => 'rgba(127, 255, 212, 0.35)')
    .ringsData(ringsData)
    .ringColor(d => t => {{
      const ah = parseInt(d.color.slice(1), 16);
      const r = (ah >> 16) & 0xff, g = (ah >> 8) & 0xff, b = ah & 0xff;
      const alpha = Math.max(0, (1 - t) * 0.9);
      return `rgba(${{r}},${{g}},${{b}},${{alpha.toFixed(2)}})`;
    }})
    .ringMaxRadius('maxR')
    .ringPropagationSpeed('propagationSpeed')
    .ringRepeatPeriod('repeatPeriod')
    .pointsData(pointsData)
    .pointLat('lat')
    .pointLng('lng')
    .pointColor('color')
    .pointAltitude(0.01)
    .pointRadius('size')
    .pointLabel(d => `<div style="background:rgba(5,8,16,0.9); color:#f4f6fb; padding:6px 10px; border-radius:6px; border:1px solid ${{d.color}}; font-family:Inter,sans-serif; font-size:12px;"><b>${{d.cat}}</b><br>Intensidade: ${{Math.round(d.intensity*100)}}%</div>`)
    .width(wrap.clientWidth)
    .height(wrap.clientHeight);

  fetch('https://raw.githubusercontent.com/vasturiano/globe.gl/master/example/datasets/ne_110m_admin_0_countries.geojson')
    .then(res => res.json())
    .then(countries => {{
      world.polygonsData(countries.features.filter(d => d.properties.ISO_A3 !== 'ATA'));
    }})
    .catch(() => {{ /* fronteiras são decorativas; globo funciona sem elas */ }});

  world.controls().autoRotate = true;
  world.controls().autoRotateSpeed = 0.55;
  world.controls().enableZoom = true;
  world.pointOfView({{ lat: 10, lng: -30, altitude: 2.3 }});

  window.addEventListener('resize', () => {{
    world.width(wrap.clientWidth);
    world.height(wrap.clientHeight);
  }});
}})();
</script>
</body>
</html>
    """
    components.html(html, height=height, scrolling=False)
