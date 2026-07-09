import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
from fpdf import FPDF
from globe_component import render_globe_3d

# ============================================================== #
# CONFIGURAÇÃO DA PÁGINA
# ============================================================== #
st.set_page_config(
    page_title="Pegada — Calculadora de Impacto Ambiental",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================== #
# DESIGN TOKENS
# ============================================================== #
# Fundo:      #050810 (quase-preto azulado)
# Superfície: #0d1424 / #111a2e
# Acento 1:   #00e5a0 (verde-menta neon — sustentável)
# Acento 2:   #ffb347 (âmbar — moderado)
# Acento 3:   #ff5470 (coral — crítico)
# Acento dado:#5b7fff (azul, usado em gráficos/dados)
# Display:    Space Grotesk | Corpo: Inter | Dados: JetBrains Mono

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
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1180px; }

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

hr { border-color: var(--border) !important; }

footer, #MainMenu { visibility: hidden; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================== #
# DADOS DO QUESTIONÁRIO
# ============================================================== #
QUESTIONS = [
    {
        "id": 1, "title": "Mobilidade",
        "question": "Quantos km você se locomove por dia (ida e volta)?",
        "options": [
            {"text": "0 a 5 km", "points": 1},
            {"text": "6 a 15 km", "points": 2},
            {"text": "16 a 40 km", "points": 3},
            {"text": "41 a 100 km", "points": 4},
            {"text": "101 a 200 km", "points": 5},
            {"text": "Mais de 200 km", "points": 6},
        ],
    },
    {
        "id": 2, "title": "Alimentação",
        "question": "Quantas refeições com carne você faz por semana?",
        "options": [
            {"text": "Nenhuma, sou vegetariano(a)", "points": 1},
            {"text": "1 a 3 refeições", "points": 2},
            {"text": "4 a 7 refeições", "points": 3},
            {"text": "8 a 14 refeições", "points": 4},
            {"text": "Mais de 14 refeições", "points": 5},
        ],
    },
    {
        "id": 3, "title": "Consumo de Moda",
        "question": "Quantas peças de roupa nova você compra por mês?",
        "options": [
            {"text": "0 - só quando necessário", "points": 1},
            {"text": "1 a 2 peças", "points": 2},
            {"text": "3 a 5 peças", "points": 3},
            {"text": "6 a 10 peças", "points": 4},
            {"text": "Mais de 10 peças", "points": 5},
        ],
    },
    {
        "id": 4, "title": "Tecnologia",
        "question": "Com que frequência você compra um celular novo?",
        "options": [
            {"text": "A cada 5 anos ou mais", "points": 1},
            {"text": "A cada 3 a 4 anos", "points": 2},
            {"text": "A cada 2 anos", "points": 3},
            {"text": "Todo ano", "points": 4},
            {"text": "Menos de 1 ano", "points": 5},
        ],
    },
    {
        "id": 5, "title": "Energia",
        "question": "Qual o consumo médio de energia elétrica na sua casa?",
        "options": [
            {"text": "Até 150 kWh/mês", "points": 1},
            {"text": "151 a 300 kWh/mês", "points": 2},
            {"text": "301 a 500 kWh/mês", "points": 3},
            {"text": "501 a 800 kWh/mês", "points": 4},
            {"text": "Mais de 800 kWh/mês", "points": 5},
        ],
    },
]

PROFILES = [
    {"range": [5, 8], "name": "Guardião da Terra", "emoji": "🟢", "color": "#00e5a0",
     "desc": "Seu estilo de vida é altamente sustentável. Você é um exemplo de regeneração!"},
    {"range": [9, 12], "name": "Consciente em Evolução", "emoji": "🟡", "color": "#ffe066",
     "desc": "Você está no caminho certo, mas pequenas mudanças podem reduzir ainda mais sua pegada."},
    {"range": [13, 17], "name": "Impacto Moderado", "emoji": "🟠", "color": "#ffb347",
     "desc": "Seu impacto é perceptível. Considere revisar hábitos de consumo e transporte."},
    {"range": [18, 22], "name": "Alerta Ambiental", "emoji": "🔴", "color": "#ff5470",
     "desc": "Seu padrão de vida exige recursos que o planeta não consegue repor rapidamente."},
    {"range": [23, 26], "name": "Crise Planetária", "emoji": "🟣", "color": "#b388ff",
     "desc": "Se todos vivessem como você, precisaríamos de vários planetas Terra."},
]

MAX_SCORE = 26

# ============================================================== #
# ESTADO
# ============================================================== #
def init_session_state():
    if "current_step" not in st.session_state:
        st.session_state.current_step = 0
    if "answers" not in st.session_state:
        st.session_state.answers = []
    if "is_complete" not in st.session_state:
        st.session_state.is_complete = False

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
    trees = co2 * 45
    ice = co2 * 3
    water = co2 * 2000
    warming = total_score * 0.01
    return {"total_score": total_score, "co2": co2, "trees": trees, "ice": ice, "water": water, "warming": warming}

def get_profile(total_score):
    for p in PROFILES:
        if p["range"][0] <= total_score <= p["range"][1]:
            return p
    return PROFILES[0]

def generate_ai_recommendations(answers, profile_name):
    recommendations = []
    pts = {a["categoryId"]: a["points"] for a in answers}

    if pts.get(1, 0) >= 4:
        recommendations.append({"title": "Considere transporte público", "desc": "Usar transporte público reduz sua pegada de carbono em até 75% comparado a dirigir sozinho.", "impact": "high"})
    if pts.get(2, 0) >= 4:
        recommendations.append({"title": "Reduza o consumo de carne", "desc": "Adotar uma dieta com menos carne pode reduzir sua pegada de carbono em até 50%.", "impact": "high"})
    if pts.get(3, 0) >= 3:
        recommendations.append({"title": "Compre roupas com mais critério", "desc": "Escolher marcas sustentáveis e comprar menos reduz o impacto têxtil significativamente.", "impact": "medium"})
    if pts.get(4, 0) >= 3:
        recommendations.append({"title": "Estenda a vida do seu celular", "desc": "Manter o aparelho por mais tempo reduz resíduos eletrônicos e emissões de manufatura.", "impact": "medium"})
    if pts.get(5, 0) >= 4:
        recommendations.append({"title": "Considere energia solar", "desc": "Painéis solares podem reduzir sua pegada de energia em até 80%.", "impact": "high"})
    elif pts.get(5, 0) >= 2:
        recommendations.append({"title": "Avalie energia renovável", "desc": "Contratar energia renovável de sua concessionária costuma ser uma opção acessível.", "impact": "medium"})

    if not recommendations:
        recommendations.append({"title": "Parabéns!", "desc": "Você já segue as melhores práticas. Continue assim.", "impact": "low"})

    return recommendations

def impact_color(level):
    if level < 0.5:
        return "#00e5a0"
    elif level < 0.75:
        return "#ffb347"
    return "#ff5470"

def get_category_breakdown(answers, questions=QUESTIONS):
    """Retorna dict {título_categoria: intensidade 0..1} para os hotspots do globo."""
    breakdown = {}
    for a in answers:
        q = next((q for q in questions if q["id"] == a["categoryId"]), None)
        if q:
            max_pts = max(o["points"] for o in q["options"])
            breakdown[q["title"]] = a["points"] / max_pts
    return breakdown

PLOTLY_LAYOUT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#f4f6fb",
    font_family="Inter",
    margin=dict(r=20, t=40, l=20, b=20),
)

def render_pizza_map(answers_data):
    df = pd.DataFrame(answers_data)
    palette = {
        "Mobilidade": "#5b7fff",
        "Alimentação": "#00e5a0",
        "Consumo de Moda": "#ffe066",
        "Tecnologia": "#ffb347",
        "Energia": "#ff5470",
    }
    colors = [palette.get(c, "#8fd8ff") for c in df["category"]]

    fig = go.Figure(data=[go.Pie(
        labels=df["category"], values=df["points"], hole=0.62,
        marker=dict(colors=colors, line=dict(color="#050810", width=2)),
        textinfo="percent", textfont=dict(color="#050810", size=13, family="JetBrains Mono"),
        hoverinfo="label+percent+value",
    )])
    fig.update_layout(
        **PLOTLY_LAYOUT_BASE,
        height=380,
        showlegend=True,
        legend=dict(font=dict(color="#8b93a7", size=11), orientation="h", y=-0.1),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

def render_interactive_comparison(impact_data):
    scenarios = {
        "Seu perfil": impact_data["co2"],
        "Média global": 4.8,
        "Cenário sustentável": 2.0,
        "Cenário crítico": 8.5,
    }
    colors_scenario = ["#00e5a0", "#8b93a7", "#00e5a0", "#ff5470"]

    cols = st.columns(4)
    max_co2 = max(scenarios.values())
    for i, (name, val) in enumerate(scenarios.items()):
        pct = (val / max_co2) * 100
        with cols[i]:
            st.markdown(f"""
            <div class='card-quiet' style='text-align:center;'>
                <p style='color:var(--text-dim); font-size:0.8rem; margin-bottom:0.6rem;'>{name}</p>
                <div style='width:100%; height:8px; background:rgba(255,255,255,0.06); border-radius:6px; overflow:hidden; margin-bottom:0.7rem;'>
                    <div style='width:{pct}%; height:100%; background:{colors_scenario[i]}; border-radius:6px;'></div>
                </div>
                <p class='mono' style='font-size:1.4rem; font-weight:700; color:{colors_scenario[i]}; margin:0;'>{val:.1f}t</p>
                <p style='color:var(--text-dim); font-size:0.75rem; margin-top:0.2rem;'>CO₂/ano</p>
            </div>
            """, unsafe_allow_html=True)

    df = pd.DataFrame({"Cenário": list(scenarios.keys()), "CO2": list(scenarios.values())})
    fig = go.Figure(go.Bar(
        x=df["Cenário"], y=df["CO2"],
        marker=dict(color=colors_scenario, line=dict(width=0)),
        text=[f"{v:.1f}t" for v in df["CO2"]], textposition="outside",
        textfont=dict(family="JetBrains Mono", color="#f4f6fb"),
    ))
    fig.update_layout(
        **PLOTLY_LAYOUT_BASE,
        height=340,
        yaxis=dict(gridcolor="rgba(255,255,255,0.06)", title="CO₂ (t/ano)"),
        xaxis=dict(gridcolor="rgba(255,255,255,0)"),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ============================================================== #
# PDF
# ============================================================== #
def generate_pdf_report(profile, impact_data, answers, recommendations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 180, 140)
    pdf.cell(0, 10, "Relatorio de Impacto Ambiental", 0, 1, "C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(0, 10, f"Seu Perfil: {profile['name']}\n{profile['desc']}", 0, "L", 0)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 140, 110)
    pdf.cell(0, 10, "Metricas de Impacto Anual", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 7, f"CO2 / ano: {impact_data['co2']:.1f} toneladas", 0, 1, "L")
    pdf.cell(0, 7, f"Arvores / ano: {int(impact_data['trees'])}", 0, 1, "L")
    pdf.cell(0, 7, f"Gelo Derretido: {impact_data['ice']:.1f} m2", 0, 1, "L")
    pdf.cell(0, 7, f"Agua Consumida: {int(impact_data['water']):,} litros", 0, 1, "L")
    pdf.cell(0, 7, f"Aquecimento: +{impact_data['warming']:.2f}C", 0, 1, "L")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 140, 110)
    pdf.cell(0, 10, "Distribuicao por Categoria", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(20, 20, 20)
    for ans in answers:
        pdf.cell(0, 7, f"{ans['category']}: {ans['points']} pontos", 0, 1, "L")
    pdf.ln(5)

    if recommendations:
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(0, 140, 110)
        pdf.cell(0, 10, "Recomendacoes Personalizadas", 0, 1, "L")
        pdf.ln(2)

        pdf.set_font("Arial", "", 12)
        pdf.set_text_color(20, 20, 20)
        for rec in recommendations:
            pdf.multi_cell(0, 7, f"- {rec['title']}: {rec['desc']}", 0, "L", 0)
        pdf.ln(5)

    pdf_output = pdf.output(dest='S').encode('latin-1')
    return base64.b64encode(pdf_output).decode('latin-1')

# ============================================================== #
# UI — QUESTIONÁRIO
# ============================================================== #
if not st.session_state.is_complete:
    current_q = QUESTIONS[st.session_state.current_step]
    progress = st.session_state.current_step / len(QUESTIONS)

    st.markdown("<p class='hero-eyebrow'>Calculadora de impacto · 5 perguntas</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Qual é a sua<br>pegada no planeta?</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-sub'>Responda com honestidade. A cada resposta, o globo ao lado reage em tempo real ao seu nível de impacto.</p>", unsafe_allow_html=True)
    st.write("")

    st.progress(progress, text=f"Pergunta {st.session_state.current_step + 1} de {len(QUESTIONS)}")
    st.write("")

    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='q-eyebrow'>Categoria {st.session_state.current_step + 1:02d} · {current_q['title']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='q-title'>{current_q['question']}</p>", unsafe_allow_html=True)

        selected_text = st.radio(
            "Escolha uma opção",
            [o["text"] for o in current_q["options"]],
            key=f"radio_{current_q['id']}",
            index=None,
            label_visibility="collapsed",
        )

        if selected_text:
            selected = next(o for o in current_q["options"] if o["text"] == selected_text)
            st.session_state.answers.append({
                "categoryId": current_q["id"],
                "category": current_q["title"],
                "points": selected["points"],
            })
            if st.session_state.current_step < len(QUESTIONS) - 1:
                st.session_state.current_step += 1
            else:
                st.session_state.is_complete = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        current_score = sum(a["points"] for a in st.session_state.answers)
        impact_level = min(current_score / MAX_SCORE, 1.0)
        breakdown = get_category_breakdown(st.session_state.answers)
        render_globe_3d(impact_level, breakdown, height=420)
        st.markdown(
            "<p style='text-align:center; color:var(--text-dim); font-size:0.85rem; margin-top:-0.5rem;'>"
            "O globo reflete, em tempo real, a pressão do seu estilo de vida sobre os ecossistemas</p>",
            unsafe_allow_html=True,
        )

# ============================================================== #
# UI — RESULTADOS
# ============================================================== #
else:
    impact_data = calculate_impact(st.session_state.answers)
    profile = get_profile(impact_data["total_score"])
    recommendations = generate_ai_recommendations(st.session_state.answers, profile["name"])

    st.markdown("<p class='hero-eyebrow'>Resultado</p>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card card-accent result-banner'>
        <p class='result-badge' style='color:{profile["color"]};'>{profile['emoji']} {profile['name']}</p>
        <p class='result-desc'>{profile['desc']}</p>
        <div class='result-stats'>
            <div>
                <p class='result-stat-value' style='color:{profile["color"]};'>{impact_data['total_score']}</p>
                <p class='result-stat-label'>Pontuação total</p>
            </div>
            <div>
                <p class='result-stat-value' style='color:var(--amber);'>{impact_data['co2']:.1f}t</p>
                <p class='result-stat-label'>CO₂ por ano</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Distribuição", "Globo 3D", "Comparação", "Recomendações", "Tecnologia & Exportar"
    ])

    with tab1:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown("#### Distribuição por categoria")
            render_pizza_map(st.session_state.answers)
        with c2:
            st.markdown("#### Métricas de impacto anual")
            metrics = [
                {"label": "CO₂ / ano", "value": f"{impact_data['co2']:.1f}t", "icon": "💨"},
                {"label": "Árvores / ano", "value": f"{int(impact_data['trees'])}", "icon": "🌳"},
                {"label": "Gelo derretido", "value": f"{impact_data['ice']:.1f} m²", "icon": "🧊"},
                {"label": "Água consumida", "value": f"{int(impact_data['water']):,} L", "icon": "💧"},
                {"label": "Aquecimento", "value": f"+{impact_data['warming']:.2f}°C", "icon": "🌡️"},
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
        st.markdown("#### O planeta segundo suas escolhas")
        breakdown = get_category_breakdown(st.session_state.answers)
        render_globe_3d(min(impact_data["total_score"] / MAX_SCORE, 1.0), breakdown, height=480)
        st.markdown(
            "<p style='text-align:center; color:var(--text-dim); font-size:0.85rem;'>"
            "Cada ponto pulsante representa uma categoria respondida — quanto mais intenso, maior a pressão daquele hábito.</p>",
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown("#### Como você se compara")
        render_interactive_comparison(impact_data)

    with tab4:
        st.markdown("#### Recomendações personalizadas")
        impact_colors = {"high": "var(--coral)", "medium": "var(--amber)", "low": "var(--mint)"}
        for rec in recommendations:
            st.markdown(f"""
            <div class='rec-card' style='border-left-color:{impact_colors.get(rec["impact"], "var(--mint)")};'>
                <p class='rec-title'>{rec['title']}</p>
                <p class='rec-desc'>{rec['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.markdown("#### Sobre a tecnologia deste projeto")
        st.markdown("""
        <p style='color:var(--text-dim); max-width:680px;'>
        Este calculador combina um back-end declarativo em Python com uma camada de visualização
        WebGL renderizada sob demanda. A ideia central — fazer uma cena 3D reagir a dados em tempo real
        conforme o usuário interage — foi inspirada na abordagem generativa usada em
        <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, um projeto de visualização de jogadas de futebol
        que reconstrói lances em cena 3D a partir de dados de rastreamento (tracking data).
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin: 1rem 0;'>", unsafe_allow_html=True)
        for tech in ["Streamlit", "Python", "Three.js (WebGL)", "Plotly", "Pandas", "FPDF", "CSS custom design system"]:
            st.markdown(f"<span class='tech-pill'>{tech}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("#### Making-of: duas abordagens de visualização generativa")
        st.markdown("""
        <p style='color:var(--text-dim); max-width:680px; margin-bottom:1rem;'>
        Embora sirvam a propósitos completamente diferentes, os dois projetos compartilham o mesmo problema
        central de engenharia: <i>como transformar dados brutos em uma cena viva, sem pré-renderizar cada quadro?</i>
        A tabela abaixo resume as escolhas técnicas de cada um.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <table class='compare-table'>
            <tr>
                <th>Aspecto</th>
                <th>Este projeto (Pegada)</th>
                <th>wc26.bogachev.fr</th>
            </tr>
            <tr>
                <td>Fonte de dados</td>
                <td class='this-proj'>Respostas do questionário, calculadas no servidor a cada interação</td>
                <td class='ref-proj'>Tracking data posicional de partidas reais (coordenadas de jogadores/bola por frame)</td>
            </tr>
            <tr>
                <td>Motor de renderização</td>
                <td class='this-proj'>Three.js / WebGL, embutido via componente HTML no Streamlit</td>
                <td class='ref-proj'>Canvas/WebGL customizado, motor próprio de física e câmera</td>
            </tr>
            <tr>
                <td>O que reage aos dados</td>
                <td class='this-proj'>Cor do globo, hotspots por categoria, intensidade do "índice de pressão"</td>
                <td class='ref-proj'>Trajetórias de jogadores, câmera dinâmica, eventos (passes, chutes, duelos)</td>
            </tr>
            <tr>
                <td>Interatividade</td>
                <td class='this-proj'>Rotação manual do globo, atualização a cada resposta do quiz</td>
                <td class='ref-proj'>Parâmetros configuráveis via URL (JSON codificado), replay de lances</td>
            </tr>
            <tr>
                <td>Stack de back-end</td>
                <td class='this-proj'>Python + Streamlit (server-side rendering do estado)</td>
                <td class='ref-proj'>Estático / client-side, config embutida na própria URL</td>
            </tr>
            <tr>
                <td>Objetivo da cena 3D</td>
                <td class='this-proj'>Traduzir um score abstrato em uma metáfora visual imediata</td>
                <td class='ref-proj'>Reconstruir e analisar eventos esportivos reais com fidelidade tática</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style='color:var(--text-dim); max-width:680px; margin-top:1.2rem; font-size:0.88rem;'>
        A principal lição incorporada aqui: pequenas cenas 3D reativas comunicam ordens de grandeza
        muito mais rápido do que tabelas — o cérebro humano lê cor e movimento antes de ler números.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("#### Exportar & compartilhar")

        exp1, exp2 = st.columns(2, gap="large")
        with exp1:
            pdf_base64 = generate_pdf_report(profile, impact_data, st.session_state.answers, recommendations)
            st.download_button(
                label="📥 Baixar relatório em PDF",
                data=base64.b64decode(pdf_base64),
                file_name="relatorio_impacto_ambiental.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        with exp2:
            share_text = f"Descobri meu impacto ambiental! Sou {profile['name']} com {impact_data['total_score']} pontos."
            share_url = "https://carbon-footprint-tracker-tkfv5pthky3rk2gd8m9mm8.streamlit.app/"
            st.markdown(f"""
            <div style='display:flex; gap:14px; align-items:center; height:100%;'>
                <a href='https://twitter.com/intent/tweet?text={share_text}&url={share_url}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/twitterx.png' width='34'>
                </a>
                <a href='https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title={share_text}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='34'>
                </a>
                <a href='https://api.whatsapp.com/send?text={share_text} {share_url}' target='_blank'>
                    <img src='https://img.icons8.com/color/48/000000/whatsapp.png' width='34'>
                </a>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.button("🔄 Refazer cálculo", on_click=reset_quiz)
