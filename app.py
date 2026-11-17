import base64

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF

from globe_component import render_globe_3d
from translations import TRANSLATIONS

# ============================================================== #
# CONFIGURAÇÃO DA PÁGINA
# ============================================================== #
st.set_page_config(
    page_title="Pegada · Carbon Footprint Calculator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================== #
# IDIOMAS (mesmos 10 do portfólio)
# ============================================================== #
LANGS = [
    ("pt", "🇧🇷", "PT"), ("en", "🇺🇸", "EN"), ("es", "🇪🇸", "ES"),
    ("it", "🇮🇹", "IT"), ("fr", "🇫🇷", "FR"), ("de", "🇩🇪", "DE"),
    ("zh", "🇨🇳", "ZH"), ("ar", "🇸🇦", "AR"), ("el", "🇬🇷", "EL"),
    ("af", "🇿🇦", "AF"),
]
CODES = [c for c, _, _ in LANGS]
FLAGS = {c: f"{flag} {label}" for c, flag, label in LANGS}

DECIMAL = {"pt": ",", "en": ".", "es": ",", "it": ",", "fr": ",", "de": ",",
           "zh": ".", "ar": ".", "el": ",", "af": ","}
THOUSANDS = {"pt": ".", "en": ",", "es": ".", "it": ".", "fr": "\u202f", "de": ".",
             "zh": ",", "ar": ",", "el": ".", "af": "\u00a0"}
PLOTLY_SEP = {"pt": ",.", "en": ".,", "es": ",.", "it": ",.", "fr": ",\u202f",
              "de": ",.", "zh": ".,", "ar": ".,", "el": ",.", "af": ",\u00a0"}
# PDF com a fonte padrão só aceita Latin-1; zh/ar/el usam o PDF em inglês.
PDF_LANGS = {"pt", "en", "es", "it", "fr", "de", "af"}


def _initial_lang():
    q = st.query_params.get("lang")
    if isinstance(q, list):
        q = q[0] if q else None
    return q if q in CODES else "pt"


if "lang" not in st.session_state:
    st.session_state.lang = _initial_lang()


def render_lang_selector():
    """Seletor com os 10 idiomas; guarda a escolha também na URL (?lang=xx)."""
    try:
        escolha = st.pills(
            "Language", CODES, selection_mode="single",
            default=st.session_state.lang, format_func=lambda c: FLAGS[c],
            key="lang_pick", label_visibility="collapsed",
        )
    except AttributeError:  # versões antigas do Streamlit sem st.pills
        escolha = st.radio(
            "Language", CODES, index=CODES.index(st.session_state.lang),
            format_func=lambda c: FLAGS[c], horizontal=True,
            key="lang_pick", label_visibility="collapsed",
        )
    if escolha and escolha != st.session_state.lang:
        st.session_state.lang = escolha
        st.query_params["lang"] = escolha
        st.rerun()


render_lang_selector()
LANG = st.session_state.lang
T = TRANSLATIONS[LANG]
RTL = LANG == "ar"


def num(x, nd=1):
    """Número com os separadores do idioma."""
    s = f"{x:,.{nd}f}"
    return s.replace(",", "\x00").replace(".", DECIMAL[LANG]).replace("\x00", THOUSANDS[LANG])


def stretch(fn, *args, **kwargs):
    """Chama o widget com width='stretch' (Streamlit novo) ou use_container_width (antigo)."""
    try:
        return fn(*args, width="stretch", **kwargs)
    except TypeError:
        return fn(*args, use_container_width=True, **kwargs)


def plot(fig):
    fig.update_layout(separators=PLOTLY_SEP[LANG])
    stretch(st.plotly_chart, fig, config={"displayModeBar": False})


CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
    --bg: #050810;
    --surface: #0d1424;
    --surface-2: #111a2e;
    --border: rgba(255,255,255,0.08);
    --text: #f4f6fb;
    --text-dim: #8b93a7;
    --mint: #00e5a0;
    --amber: #ffb347;
    --coral: #ff5470;
    --blue: #5b7fff;
}

html, body, .stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}

/* remove o padding excessivo do topo padrão do Streamlit */
.block-container { padding-top: 4.5rem; padding-bottom: 3rem; max-width: 1180px; }
[data-testid="stHeader"] { background: transparent !important; }

* { font-family: 'Inter', sans-serif; }

h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
    letter-spacing: -0.01em;
}

.mono { font-family: 'JetBrains Mono', monospace !important; }

/* ---------- Hero ---------- */
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--mint);
    margin-bottom: 0.5rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    line-height: 1.05;
    margin: 0 0 0.6rem 0;
    background: linear-gradient(135deg, #ffffff 30%, #8fd8ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    color: var(--text-dim);
    font-size: 1.02rem;
    max-width: 480px;
    line-height: 1.5;
}

/* ---------- Cards ---------- */
.card {
    background: linear-gradient(180deg, var(--surface) 0%, var(--surface-2) 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
}
.card-quiet {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
}
.card-accent {
    border-color: rgba(0,229,160,0.35);
    box-shadow: 0 0 0 1px rgba(0,229,160,0.08), 0 20px 60px -30px rgba(0,229,160,0.35);
}

/* ---------- Progress ---------- */
.stProgress > div > div > div > div { background: linear-gradient(90deg, var(--mint), var(--blue)) !important; }
.stProgress > div > div > div { background: rgba(255,255,255,0.06) !important; border-radius: 8px; }

/* ---------- Question label ---------- */
.q-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: var(--text-dim); margin-bottom: 0.3rem;
}
.q-title { font-size: 1.5rem; font-weight: 600; margin-bottom: 0.4rem; }
.q-text { color: var(--text-dim); margin-bottom: 1rem; font-size: 0.95rem; }

/* ---------- Radio options styled as cards ---------- */
div[role="radiogroup"] > label {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.7rem 1rem !important;
    margin-bottom: 0.5rem;
    transition: all 0.15s ease;
    width: 100%;
}
div[role="radiogroup"] > label:hover {
    border-color: rgba(0,229,160,0.4);
    background: rgba(0,229,160,0.05);
}

/* ---------- Buttons ---------- */
.stButton > button {
    background: var(--mint) !important;
    color: #04140f !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.3rem !important;
    transition: all 0.15s ease !important;
}
.stButton > button:hover {
    background: #33ecb5 !important;
    transform: translateY(-1px);
    box-shadow: 0 8px 24px -8px rgba(0,229,160,0.5);
}
.stDownloadButton > button {
    background: var(--surface-2) !important;
    color: var(--text) !important;
    border: 1px solid var(--mint) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 1px solid var(--border); }
.stTabs [data-baseweb="tab"] {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--text-dim);
    font-weight: 500;
    padding: 0.6rem 1rem;
}
.stTabs [aria-selected="true"] {
    color: var(--mint) !important;
    border-bottom: 2px solid var(--mint) !important;
}

/* ---------- Metric tiles ---------- */
.metric-tile {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.1rem;
    text-align: center;
}
.metric-icon { font-size: 1.6rem; margin-bottom: 0.3rem; }
.metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem; font-weight: 700; color: var(--mint);
}
.metric-label { color: var(--text-dim); font-size: 0.82rem; margin-top: 0.2rem; }

/* ---------- Profile result banner ---------- */
.result-banner {
    text-align: center;
    padding: 2.4rem 1.5rem;
}
.result-badge {
    font-size: 2rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 0.4rem;
}
.result-desc { color: var(--text-dim); max-width: 560px; margin: 0 auto; }
.result-stats { display: flex; justify-content: center; gap: 3.5rem; margin-top: 1.8rem; }
.result-stat-value { font-family: 'JetBrains Mono', monospace; font-size: 2.2rem; font-weight: 700; }
.result-stat-label { color: var(--text-dim); font-size: 0.82rem; margin-top: 0.2rem; }

/* ---------- Recommendation cards ---------- */
.rec-card {
    border-radius: 14px; padding: 1.2rem 1.4rem; margin-bottom: 0.8rem;
    border-left: 3px solid var(--mint);
    background: var(--surface);
}
.rec-title { font-weight: 600; margin-bottom: 0.3rem; font-family: 'Space Grotesk', sans-serif; }
.rec-desc { color: var(--text-dim); font-size: 0.9rem; line-height: 1.4; }

/* ---------- Tech tab ---------- */
.tech-pill {
    display: inline-block; padding: 0.3rem 0.8rem; border-radius: 999px;
    background: rgba(91,127,255,0.12); border: 1px solid rgba(91,127,255,0.3);
    color: #a9baff; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;
    margin: 0.2rem 0.3rem 0.2rem 0;
}
.compare-table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
.compare-table th, .compare-table td {
    padding: 0.7rem 0.9rem; text-align: left; border-bottom: 1px solid var(--border); font-size: 0.9rem;
}
.compare-table th { color: var(--text-dim); font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; }
.compare-table td.this-proj { color: var(--mint); }
.compare-table td.ref-proj { color: #8fd8ff; }


/* ---------- Ajustes de contraste e layout (v2) ---------- */
[data-testid="stVerticalBlockBorderWrapper"]:has(div[role="radiogroup"]) {
    background: linear-gradient(180deg, var(--surface) 0%, var(--surface-2) 100%);
    border: 1px solid var(--border) !important; border-radius: 16px; padding: 0.6rem 0.8rem;
}
div[role="radiogroup"] label, div[role="radiogroup"] label p, div[role="radiogroup"] label span { color: var(--text) !important; }
div[role="radiogroup"] > label { cursor: pointer; }
[data-testid="stProgress"] div[role="progressbar"] { background: rgba(255,255,255,0.08) !important; }
[data-testid="stProgress"] div[role="progressbar"] > div { background: linear-gradient(90deg, var(--mint), var(--blue)) !important; }
[data-testid="stProgress"] p { color: var(--text-dim) !important; }
[data-testid="stPills"] button, [data-testid="stButtonGroup"] button {
    background: var(--surface-2) !important; color: var(--text) !important; border: 1px solid var(--border) !important;
}
[data-testid="stPills"] button[aria-checked="true"], [data-testid="stButtonGroup"] button[aria-checked="true"],
[data-testid="stPills"] button[kind="pillsActive"], [data-testid="stButtonGroup"] button[kind="pillsActive"] {
    border-color: var(--mint) !important; color: var(--mint) !important; background: rgba(0,229,160,0.08) !important;
}

hr { border-color: var(--border) !important; }

footer, #MainMenu { visibility: hidden; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if RTL:
    st.markdown("""
<style>
[data-testid="stMain"] { direction: rtl; text-align: right; }
.result-banner, .metric-tile, .card-quiet { text-align: center; }
.result-stats { direction: ltr; }
.rec-card { border-left: none !important; border-right: 3px solid var(--mint); }
[data-testid="stMarkdownContainer"] { direction: rtl; text-align: right; }
.hero-sub { margin-left: auto; }
.hero-title { display: block; text-align: right; }
.result-banner, .result-banner p { text-align: center !important; }
iframe, .js-plotly-plot { direction: ltr; }
</style>
""", unsafe_allow_html=True)
if LANG in ("zh", "ar", "el"):
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;600;700&family=Noto+Naskh+Arabic:wght@400;700&family=Noto+Sans:wght@400;600;700&display=swap');
* { font-family: 'Inter', 'Noto Sans', 'Noto Sans SC', 'Noto Naskh Arabic', sans-serif; }
h1, h2, h3, h4, h5, h6, .hero-title { font-family: 'Space Grotesk', 'Noto Sans', 'Noto Sans SC', 'Noto Naskh Arabic', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================== #
# DADOS DO QUESTIONÁRIO (pontos fixos; textos vêm das traduções)
# ============================================================== #
QUESTION_POINTS = [
    [1, 2, 3, 4, 5, 6],   # 1 Mobilidade
    [1, 2, 3, 4, 5],      # 2 Alimentação
    [1, 2, 3, 4, 5],      # 3 Moda
    [1, 2, 3, 4, 5],      # 4 Tecnologia
    [1, 2, 3, 4, 5],      # 5 Energia
]
PROFILE_META = [  # (faixa de pontos, emoji, cor)
    ((5, 8), "🟢", "#00e5a0"),
    ((9, 12), "🟡", "#ffe066"),
    ((13, 17), "🟠", "#ffb347"),
    ((18, 22), "🔴", "#ff5470"),
    ((23, 26), "🟣", "#b388ff"),
]
CATEGORY_COLORS = ["#5b7fff", "#00e5a0", "#ffe066", "#ffb347", "#ff5470"]
MAX_SCORE = 26
N_Q = len(QUESTION_POINTS)

# ============================================================== #
# ESTADO — as respostas guardam só (categoria, pontos); o texto é montado
# no idioma atual, então trocar de idioma no meio do quiz não perde nada.
# ============================================================== #
def init_session_state():
    st.session_state.setdefault("current_step", 0)
    st.session_state.setdefault("answers", [])
    st.session_state.setdefault("is_complete", False)


def reset_quiz():
    st.session_state.current_step = 0
    st.session_state.answers = []
    st.session_state.is_complete = False


init_session_state()

# ============================================================== #
# LÓGICA DE CÁLCULO
# ============================================================== #
def calculate_impact(answers):
    total_score = sum(a["points"] for a in answers)
    co2 = total_score * 0.8
    return {"total_score": total_score, "co2": co2, "trees": co2 * 45, "ice": co2 * 3,
            "water": co2 * 2000, "warming": total_score * 0.01}


def get_profile(total_score):
    idx = 0
    for i, (rng, _, _) in enumerate(PROFILE_META):
        if rng[0] <= total_score <= rng[1]:
            idx = i
    _, emoji, color = PROFILE_META[idx]
    return {"name": T["profiles"][idx]["name"], "desc": T["profiles"][idx]["desc"],
            "emoji": emoji, "color": color}


def recommendations_for(answers, tr):
    """Regras de recomendação (impacto, chave do texto) usando o dicionário `tr`."""
    pts = {a["categoryId"]: a["points"] for a in answers}
    keys = []
    if pts.get(1, 0) >= 4: keys.append(("transport", "high"))
    if pts.get(2, 0) >= 4: keys.append(("meat", "high"))
    if pts.get(3, 0) >= 3: keys.append(("fashion", "medium"))
    if pts.get(4, 0) >= 3: keys.append(("phone", "medium"))
    if pts.get(5, 0) >= 4: keys.append(("solar", "high"))
    elif pts.get(5, 0) >= 2: keys.append(("renewable", "medium"))
    if not keys:
        keys.append(("great", "low"))
    return [{"title": tr["recs"][k]["title"], "desc": tr["recs"][k]["desc"], "impact": lvl} for k, lvl in keys]


def category_title(cat_id):
    return T["questions"][cat_id - 1]["title"]


def get_category_breakdown(answers):
    """{id: intensidade 0..1} para os hotspots do globo."""
    return {a["categoryId"]: a["points"] / max(QUESTION_POINTS[a["categoryId"] - 1]) for a in answers}


PLOTLY_LAYOUT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="#f4f6fb", font_family="Inter, Noto Sans, Noto Sans SC, Noto Naskh Arabic",
    margin=dict(r=20, t=40, l=20, b=20),
)


def render_globe(impact_level, answers, height):
    render_globe_3d(
        impact_level, get_category_breakdown(answers),
        labels={str(i + 1): q["title"] for i, q in enumerate(T["questions"])},
        texts={"hud": T["globe_hud"], "legend": T["globe_legend"], "intensity": T["globe_intensity"]},
        height=height, rtl=RTL,
    )


def render_pizza_map(answers):
    df = pd.DataFrame({
        "category": [category_title(a["categoryId"]) for a in answers],
        "points": [a["points"] for a in answers],
    })
    colors = [CATEGORY_COLORS[a["categoryId"] - 1] for a in answers]
    fig = go.Figure(data=[go.Pie(
        labels=df["category"], values=df["points"], hole=0.62,
        marker=dict(colors=colors, line=dict(color="#050810", width=2)),
        textinfo="percent", textfont=dict(color="#050810", size=13, family="JetBrains Mono"),
        hoverinfo="label+percent+value",
    )])
    fig.update_layout(**PLOTLY_LAYOUT_BASE, height=380, showlegend=True,
                      legend=dict(font=dict(color="#8b93a7", size=11), orientation="h", y=-0.1))
    plot(fig)


def render_interactive_comparison(impact_data):
    names = T["scenarios"]
    values = [impact_data["co2"], 4.8, 2.0, 8.5]
    colors_scenario = ["#00e5a0", "#8b93a7", "#00e5a0", "#ff5470"]

    cols = st.columns(4)
    max_co2 = max(values)
    for i, (name, val) in enumerate(zip(names, values)):
        pct = (val / max_co2) * 100
        with cols[i]:
            st.markdown(f"""
            <div class='card-quiet' style='text-align:center;'>
                <p style='color:var(--text-dim); font-size:0.8rem; margin-bottom:0.6rem;'>{name}</p>
                <div style='width:100%; height:8px; background:rgba(255,255,255,0.06); border-radius:6px; overflow:hidden; margin-bottom:0.7rem;'>
                    <div style='width:{pct}%; height:100%; background:{colors_scenario[i]}; border-radius:6px;'></div>
                </div>
                <p class='mono' style='font-size:1.4rem; font-weight:700; color:{colors_scenario[i]}; margin:0;'>{num(val)}t</p>
                <p style='color:var(--text-dim); font-size:0.75rem; margin-top:0.2rem;'>{T['co2_unit']}</p>
            </div>
            """, unsafe_allow_html=True)

    fig = go.Figure(go.Bar(
        x=names, y=values, marker=dict(color=colors_scenario, line=dict(width=0)),
        text=[f"{num(v)}t" for v in values], textposition="outside",
        textfont=dict(family="JetBrains Mono", color="#f4f6fb"),
    ))
    fig.update_layout(**PLOTLY_LAYOUT_BASE, height=340, showlegend=False,
                      yaxis=dict(gridcolor="rgba(255,255,255,0.06)", title=T["co2_axis"]),
                      xaxis=dict(gridcolor="rgba(255,255,255,0)"))
    plot(fig)


# ============================================================== #
# PDF (fonte padrão = Latin-1; zh/ar/el recebem o PDF em inglês)
# ============================================================== #
def _l1(text):
    return str(text).encode("latin-1", "replace").decode("latin-1")


def generate_pdf_report(impact_data, answers):
    pl = LANG if LANG in PDF_LANGS else "en"
    tr = TRANSLATIONS[pl]
    P = tr["pdf"]
    profile_idx = next((i for i, (r, _, _) in enumerate(PROFILE_META)
                        if r[0] <= impact_data["total_score"] <= r[1]), 0)
    prof = tr["profiles"][profile_idx]
    recs = recommendations_for(answers, tr)

    def fmt(x, nd=1):
        s = f"{x:,.{nd}f}"
        return s.replace(",", "\x00").replace(".", DECIMAL[pl]).replace("\x00", " " if THOUSANDS[pl] in ("\u202f", "\u00a0") else THOUSANDS[pl])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(True, 15)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 180, 140)
    pdf.cell(0, 10, _l1(P["title"]), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)

    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(0, 8, _l1(f"{P['profile']}: {prof['name']}\n{prof['desc']}"), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    def heading(text):
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(0, 140, 110)
        pdf.cell(0, 10, _l1(text), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 12)
        pdf.set_text_color(20, 20, 20)

    heading(P["metrics"])
    for line in (P["co2"].format(v=fmt(impact_data["co2"])),
                 P["trees"].format(v=fmt(impact_data["trees"], 0)),
                 P["ice"].format(v=fmt(impact_data["ice"])),
                 P["water"].format(v=fmt(impact_data["water"], 0)),
                 P["warming"].format(v=fmt(impact_data["warming"], 2))):
        pdf.cell(0, 7, _l1(line), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    heading(P["dist"])
    for a in answers:
        pdf.cell(0, 7, _l1(P["points"].format(cat=tr["questions"][a["categoryId"] - 1]["title"], n=a["points"])),
                 new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    heading(P["recs"])
    for rec in recs:
        pdf.multi_cell(0, 7, _l1(f"- {rec['title']}: {rec['desc']}"), new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output()), tr["pdf"]["file"]


# ============================================================== #
# UI — QUESTIONÁRIO
# ============================================================== #
if not st.session_state.is_complete:
    step = st.session_state.current_step
    q = T["questions"][step]
    progress = step / N_Q

    st.markdown(f"<p class='hero-eyebrow'>{T['eyebrow']}</p>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='hero-title'>{T['hero_title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='hero-sub'>{T['hero_sub']}</p>", unsafe_allow_html=True)
    st.write("")

    st.progress(progress, text=T["progress"].format(n=step + 1, total=N_Q))
    st.write("")

    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        card = st.container(border=True)
        with card:
          st.markdown(f"<p class='q-eyebrow'>{T['cat_eyebrow'].format(n=f'{step + 1:02d}', title=q['title'])}</p>", unsafe_allow_html=True)
          st.markdown(f"<p class='q-title'>{q['question']}</p>", unsafe_allow_html=True)

          # as opções são índices; o texto vem do idioma atual
          chosen = st.radio(
              T["choose"], list(range(len(q["options"]))),
              format_func=lambda i: q["options"][i],
              key=f"radio_{step + 1}", index=None, label_visibility="collapsed",
          )
          if chosen is not None:
              st.session_state.answers.append({
                  "categoryId": step + 1,
                  "points": QUESTION_POINTS[step][chosen],
              })
              if step < N_Q - 1:
                  st.session_state.current_step += 1
              else:
                  st.session_state.is_complete = True
              st.rerun()

    with col2:
        current_score = sum(a["points"] for a in st.session_state.answers)
        render_globe(min(current_score / MAX_SCORE, 1.0), st.session_state.answers, 420)
        st.markdown(
            f"<p style='text-align:center; color:var(--text-dim); font-size:0.85rem; margin-top:-0.5rem;'>{T['globe_caption']}</p>",
            unsafe_allow_html=True,
        )

# ============================================================== #
# UI — RESULTADOS
# ============================================================== #
else:
    impact_data = calculate_impact(st.session_state.answers)
    profile = get_profile(impact_data["total_score"])
    recommendations = recommendations_for(st.session_state.answers, T)

    st.markdown(f"<p class='hero-eyebrow'>{T['result_eyebrow']}</p>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card card-accent result-banner'>
        <p class='result-badge' style='color:{profile["color"]};'>{profile['emoji']} {profile['name']}</p>
        <p class='result-desc'>{profile['desc']}</p>
        <div class='result-stats'>
            <div>
                <p class='result-stat-value' style='color:{profile["color"]};'>{impact_data['total_score']}</p>
                <p class='result-stat-label'>{T['score_label']}</p>
            </div>
            <div>
                <p class='result-stat-value' style='color:var(--amber);'>{num(impact_data['co2'])}t</p>
                <p class='result-stat-label'>{T['co2_year']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption(T["methodology_note"])

    tab1, tab2, tab3, tab4, tab5 = st.tabs(T["tabs"])

    with tab1:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(f"#### {T['dist_title']}")
            render_pizza_map(st.session_state.answers)
        with c2:
            st.markdown(f"#### {T['metrics_title']}")
            L = T["metric_labels"]
            metrics = [
                {"label": L[0], "value": f"{num(impact_data['co2'])}t", "icon": "💨"},
                {"label": L[1], "value": num(impact_data['trees'], 0), "icon": "🌳"},
                {"label": L[2], "value": f"{num(impact_data['ice'])} m²", "icon": "🧊"},
                {"label": L[3], "value": f"{num(impact_data['water'], 0)} L", "icon": "💧"},
                {"label": L[4], "value": f"+{num(impact_data['warming'], 2)}°C", "icon": "🌡️"},
            ]
            m1, m2 = st.columns(2)
            for i, metric in enumerate(metrics):
                target = m1 if i % 2 == 0 else m2
                with target:
                    st.markdown(f"""
                    <div class='metric-tile'>
                        <div class='metric-icon'>{metric['icon']}</div>
                        <div class='metric-value'>{metric['value']}</div>
                        <div class='metric-label'>{metric['label']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")

    with tab2:
        st.markdown(f"#### {T['globe_tab_title']}")
        render_globe(min(impact_data["total_score"] / MAX_SCORE, 1.0), st.session_state.answers, 480)
        st.markdown(f"<p style='text-align:center; color:var(--text-dim); font-size:0.85rem;'>{T['globe_tab_caption']}</p>",
                    unsafe_allow_html=True)

    with tab3:
        st.markdown(f"#### {T['compare_title']}")
        render_interactive_comparison(impact_data)

    with tab4:
        st.markdown(f"#### {T['rec_title']}")
        impact_colors = {"high": "var(--coral)", "medium": "var(--amber)", "low": "var(--mint)"}
        for rec in recommendations:
            st.markdown(f"""
            <div class='rec-card' style='border-left-color:{impact_colors.get(rec["impact"], "var(--mint)")};'>
                <p class='rec-title'>{rec['title']}</p>
                <p class='rec-desc'>{rec['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.markdown(f"#### {T['tech_title']}")
        st.markdown(f"<p style='color:var(--text-dim); max-width:680px;'>{T['tech_intro']}</p>", unsafe_allow_html=True)

        pills = "".join(f"<span class='tech-pill'>{t}</span>" for t in
                        ["Streamlit", "Python", "Three.js (WebGL)", "Plotly", "Pandas", "FPDF", "CSS design system"])
        st.markdown(f"<div style='margin: 1rem 0;'>{pills}</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"#### {T['making_title']}")
        st.markdown(f"<p style='color:var(--text-dim); max-width:680px; margin-bottom:1rem;'>{T['making_intro']}</p>",
                    unsafe_allow_html=True)

        rows_html = "".join(
            f"<tr><td>{r[0]}</td><td class='this-proj'>{r[1]}</td><td class='ref-proj'>{r[2]}</td></tr>"
            for r in T["rows"]
        )
        st.markdown(f"""
        <table class='compare-table'>
            <tr><th>{T['th_aspect']}</th><th>{T['th_this']}</th><th>{T['th_ref']}</th></tr>
            {rows_html}
        </table>
        """, unsafe_allow_html=True)

        st.markdown(f"<p style='color:var(--text-dim); max-width:680px; margin-top:1.2rem; font-size:0.88rem;'>{T['lesson']}</p>",
                    unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"#### {T['export_title']}")

        exp1, exp2 = st.columns(2, gap="large")
        with exp1:
            pdf_bytes, pdf_name = generate_pdf_report(impact_data, st.session_state.answers)
            stretch(st.download_button, label=T["pdf_button"], data=pdf_bytes,
                    file_name=pdf_name, mime="application/pdf")
        with exp2:
            from urllib.parse import quote
            share_text = quote(T["share_text"].format(profile=profile["name"], score=impact_data["total_score"]))
            share_url = "https://carbon-footprint-tracker-tkfv5pthky3rk2gd8m9mm8.streamlit.app/"
            st.markdown(f"""
            <div style='display:flex; gap:14px; align-items:center; height:100%;'>
                <a href='https://twitter.com/intent/tweet?text={share_text}&url={share_url}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/twitterx.png' width='34'>
                </a>
                <a href='https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title={share_text}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='34'>
                </a>
                <a href='https://api.whatsapp.com/send?text={share_text}%20{share_url}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/whatsapp.png' width='34'>
                </a>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.button(T["retry"], on_click=reset_quiz)
