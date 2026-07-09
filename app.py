import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from fpdf import FPDF
import base64
from datetime import datetime

# --- Configurações da Página --- #
st.set_page_config(
    page_title="Calculadora de Impacto Ambiental",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Estilo Futurístico e Cores (Baseado no Portfólio) --- #
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

    /* Fundo principal */
    body {
        background-color: #0a0e27; /* Dark Navy */
        color: #FFFFFF; /* Texto principal branco */
        font-family: 'Space Mono', monospace; /* Fonte futurística */
    }
    .stApp {
        background-color: #0a0e27;
        color: #FFFFFF;
    }
    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #00FF00; /* Verde Neon */
        font-family: 'Space Mono', monospace;
    }
    /* Botões */
    .stButton>button {
        background-color: #00FF00; /* Verde Neon */
        color: #0a0e27; /* Texto Dark Navy */
        border-radius: 8px;
        border: 1px solid #00FF00;
        transition: all 0.3s ease;
        font-family: 'Space Mono', monospace;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00CC00; /* Verde mais escuro no hover */
        border-color: #00CC00;
        color: #FFFFFF;
    }
    /* Cards/Containers */
    .stCard, .stAlert {
        background-color: #1a1f3a; /* Um pouco mais claro que o fundo */
        border: 1px solid #00FF00; /* Borda Verde Neon */
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3); /* Sombra neon */
        padding: 20px;
        margin-bottom: 20px;
    }
    /* Barra de Progresso */
    .stProgress > div > div > div > div {
        background-color: #00FF00; /* Verde Neon */
    }
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] button {
        color: #FFFFFF;
        font-family: 'Space Mono', monospace;
    }
    .stTabs [aria-selected="true"] {
        color: #00FF00;
        border-bottom: 2px solid #00FF00;
    }
    /* Comparação animada */
    .comparison-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        margin: 20px 0;
    }
    .comparison-item {
        flex: 1;
        text-align: center;
        padding: 20px;
        background-color: #1a1f3a;
        border: 1px solid #00FF00;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
    }
    .comparison-bar {
        width: 100%;
        height: 40px;
        background-color: #0a0e27;
        border-radius: 8px;
        overflow: hidden;
        margin: 10px 0;
        position: relative;
        border: 1px solid #00FF00;
    }
    .comparison-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #00FF00, #FF0000);
        animation: fillAnimation 1.5s ease-out;
    }
    @keyframes fillAnimation {
        from {
            width: 0%;
        }
        to {
            width: var(--fill-width);
        }
    }
    .comparison-label {
        font-weight: bold;
        color: #00FF00;
        font-size: 1.2em;
        margin-top: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Dados do Questionário --- #
QUESTIONS = [
    {
        "id": 1,
        "title": "Mobilidade",
        "question": "Quantos km você se locomove por dia (ida e volta)?",
        "options": [
            {"text": "0 a 5 km", "points": 1, "color_class": "option-blue"},
            {"text": "6 a 15 km", "points": 2, "color_class": "option-green"},
            {"text": "16 a 40 km", "points": 3, "color_class": "option-yellow"},
            {"text": "41 a 100 km", "points": 4, "color_class": "option-orange"},
            {"text": "101 a 200 km", "points": 5, "color_class": "option-red"},
            {"text": "Mais de 200 km", "points": 6, "color_class": "option-purple"},
        ],
    },
    {
        "id": 2,
        "title": "Alimentação",
        "question": "Quantas refeições com carne você faz por semana?",
        "options": [
            {"text": "Nenhuma, sou vegetariano(a)", "points": 1, "color_class": "option-blue"},
            {"text": "1 a 3 refeições", "points": 2, "color_class": "option-green"},
            {"text": "4 a 7 refeições", "points": 3, "color_class": "option-yellow"},
            {"text": "8 a 14 refeições", "points": 4, "color_class": "option-orange"},
            {"text": "Mais de 14 refeições", "points": 5, "color_class": "option-red"},
        ],
    },
    {
        "id": 3,
        "title": "Consumo de Moda",
        "question": "Quantas peças de roupa nova você compra por mês?",
        "options": [
            {"text": "0 - só quando necessário", "points": 1, "color_class": "option-blue"},
            {"text": "1 a 2 peças", "points": 2, "color_class": "option-green"},
            {"text": "3 a 5 peças", "points": 3, "color_class": "option-yellow"},
            {"text": "6 a 10 peças", "points": 4, "color_class": "option-orange"},
            {"text": "Mais de 10 peças", "points": 5, "color_class": "option-red"},
        ],
    },
    {
        "id": 4,
        "title": "Tecnologia",
        "question": "Com que frequência você compra um celular novo?",
        "options": [
            {"text": "A cada 5 anos ou mais", "points": 1, "color_class": "option-blue"},
            {"text": "A cada 3 a 4 anos", "points": 2, "color_class": "option-green"},
            {"text": "A cada 2 anos", "points": 3, "color_class": "option-yellow"},
            {"text": "Todo ano", "points": 4, "color_class": "option-orange"},
            {"text": "Menos de 1 ano", "points": 5, "color_class": "option-red"},
        ],
    },
    {
        "id": 5,
        "title": "Energia",
        "question": "Qual o consumo médio de energia elétrica na sua casa?",
        "options": [
            {"text": "Até 150 kWh/mês", "points": 1, "color_class": "option-blue"},
            {"text": "151 a 300 kWh/mês", "points": 2, "color_class": "option-green"},
            {"text": "301 a 500 kWh/mês", "points": 3, "color_class": "option-yellow"},
            {"text": "501 a 800 kWh/mês", "points": 4, "color_class": "option-orange"},
            {"text": "Mais de 800 kWh/mês", "points": 5, "color_class": "option-red"},
        ],
    },
]

PROFILES = [
    {"range": [5, 8], "name": "🟢 Guardião da Terra", "desc": "Seu estilo de vida é altamente sustentável. Você é um exemplo de regeneração!"},
    {"range": [9, 12], "name": "🟡 Consciente em Evolução", "desc": "Você está no caminho certo, mas pequenas mudanças podem reduzir ainda mais sua pegada."},
    {"range": [13, 17], "name": "🟠 Impacto Moderado", "desc": "Seu impacto é perceptível. Considere revisar hábitos de consumo e transporte."},
    {"range": [18, 22], "name": "🔴 Alerta Ambiental", "desc": "Seu padrão de vida exige recursos que o planeta não consegue repor rapidamente."},
    {"range": [23, 26], "name": "🟣 Crise Planetária", "desc": "Se todos vivessem como você, precisaríamos de vários planetas Terra."},
]

# --- Funções de Estado --- #
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

# --- Lógica de Cálculo de Impacto --- #
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
    mobility_points = next((a["points"] for a in answers if a["categoryId"] == 1), 0)
    food_points = next((a["points"] for a in answers if a["categoryId"] == 2), 0)
    fashion_points = next((a["points"] for a in answers if a["categoryId"] == 3), 0)
    tech_points = next((a["points"] for a in answers if a["categoryId"] == 4), 0)
    energy_points = next((a["points"] for a in answers if a["categoryId"] == 5), 0)

    if mobility_points >= 4:
        recommendations.append({"title": "Considere Transporte Público", "desc": "Usar transporte público reduz sua pegada de carbono em até 75% comparado a dirigir sozinho.", "impact": "high"})
    if food_points >= 4:
        recommendations.append({"title": "Reduza Consumo de Carne", "desc": "Adotar uma dieta com menos carne pode reduzir sua pegada de carbono em até 50%.", "impact": "high"})
    if fashion_points >= 3:
        recommendations.append({"title": "Compre Roupas Sustentáveis", "desc": "Escolher marcas sustentáveis e comprar menos reduz impacto têxtil significativamente.", "impact": "medium"})
    if tech_points >= 3:
        recommendations.append({"title": "Estenda Vida do Celular", "desc": "Manter seu celular por mais tempo reduz resíduos eletrônicos e emissões de manufatura.", "impact": "medium"})
    if energy_points >= 4:
        recommendations.append({"title": "Instale Energia Solar", "desc": "Painéis solares podem reduzir sua pegada de energia em até 80%.", "impact": "high"})
    if energy_points >= 2:
        recommendations.append({"title": "Use Energia Renovável", "desc": "Contratar energia renovável de sua concessionária é uma opção acessível.", "impact": "medium"})
    
    if not recommendations:
        recommendations.append({"title": "Parabéns!", "desc": "Você já está seguindo as melhores práticas. Continue assim! 🌱", "impact": "low"})

    return recommendations

# --- Visualização do Globo 3D --- #
def render_globe_3d(impact_level):
    color_scale = [
        [0.0, "#00FF00"],
        [0.3, "#FFFF00"],
        [0.7, "#FF9800"],
        [1.0, "#FF0000"],
    ]
    
    fig = go.Figure(data=go.Scattergeo(
        lon = [0],
        lat = [0],
        mode = 'markers',
        marker = dict(
            size = 50,
            color = impact_level,
            colorscale = color_scale,
            showscale = False,
            line = dict(width=0)
        ),
        hoverinfo = 'text',
        text = f'Nível de Impacto: {impact_level:.1%}'
    ))
    
    fig.update_geos(
        showland=True, 
        landcolor="#1a1f3a",
        showocean=True, 
        oceancolor="#0a0e27",
        showcountries=True, 
        countrycolor="#00FF00",
        showframe=False, 
        showcoastlines=False,
        projection_type="orthographic"
    )
    
    fig.update_layout(
        height=400,
        margin=dict(r=0, t=50, l=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        title_text="Visualização de Impacto Global",
        title_font_color="#00FF00",
        coloraxis_showscale=False,
        geo=dict(
            bgcolor="rgba(0,0,0,0)",
            lakecolor="#0a0e27"
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de Pizza no Mapa --- #
def render_pizza_map(answers_data, total_score):
    df_answers = pd.DataFrame(answers_data)
    
    pie_colors = {
        "Mobilidade": "#2196F3",
        "Alimentação": "#4CAF50",
        "Consumo de Moda": "#FFEB3B",
        "Tecnologia": "#FF9800",
        "Energia": "#F44336",
    }
    colors = [pie_colors.get(cat, "#FFFFFF") for cat in df_answers["category"]]

    fig_pie = go.Figure(data=[go.Pie(
        labels=df_answers["category"],
        values=df_answers["points"],
        hole=0.5,
        marker_colors=colors,
        name="Distribuição de Impacto",
        hoverinfo="label+percent+value",
        textinfo="percent",
        textfont_color="#FFFFFF",
    )])
    fig_pie.update_layout(
        height=400,
        margin=dict(r=0, t=0, l=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        showlegend=True,
        legend=dict(font=dict(color="#FFFFFF"))
    )
    
    st.subheader("Distribuição de Impacto por Categoria")
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Comparação Interativa Animada (Estilo Data Portraits) --- #
def render_interactive_comparison(impact_data, profile):
    st.markdown("<h2 style='text-align: center; color: #00FF00;'>Análise Comparativa Interativa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #999999;'>Compare seu impacto com cenários alternativos</p>", unsafe_allow_html=True)
    
    # Cenários simulados
    scenarios = {
        "Seu Perfil": impact_data["co2"],
        "Média Global": 4.8,
        "Cenário Sustentável": 2.0,
        "Cenário Crítico": 8.5,
    }
    
    max_co2 = max(scenarios.values())
    
    # Criar visualização de comparação animada
    col1, col2, col3, col4 = st.columns(4)
    
    cols = [col1, col2, col3, col4]
    colors_scenario = ["#00FF00", "#FFFF00", "#00FF00", "#FF0000"]
    
    for i, (scenario_name, co2_value) in enumerate(scenarios.items()):
        with cols[i]:
            percentage = (co2_value / max_co2) * 100
            st.markdown(f"""
            <div class='stCard' style='text-align: center; border-color: {colors_scenario[i]}; box-shadow: 0 0 20px rgba({255 if i == 3 else 0}, 255, 0, 0.5);'>
                <h3 style='color: {colors_scenario[i]};'>{scenario_name}</h3>
                <div style='width: 100%; height: 60px; background-color: #0a0e27; border-radius: 8px; overflow: hidden; margin: 15px 0; border: 1px solid {colors_scenario[i]};'>
                    <div style='width: {percentage}%; height: 100%; background: linear-gradient(90deg, #00FF00, #FF0000); animation: fillAnimation 1.5s ease-out;'></div>
                </div>
                <p style='font-size: 1.8em; font-weight: bold; color: {colors_scenario[i]};'>{co2_value:.1f}t</p>
                <p style='color: #999999; font-size: 0.9em;'>CO2/ano</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Gráfico de barras comparativo
    st.markdown("<hr style='border-color: #00FF00;'>", unsafe_allow_html=True)
    
    comparison_df = pd.DataFrame({
        "Cenário": list(scenarios.keys()),
        "CO2 (toneladas/ano)": list(scenarios.values()),
    })
    
    fig_comparison = px.bar(
        comparison_df,
        x="Cenário",
        y="CO2 (toneladas/ano)",
        color="Cenário",
        color_discrete_sequence=colors_scenario,
        title="Comparação de Emissões de CO2",
        labels={"CO2 (toneladas/ano)": "CO2 (t/ano)"},
    )
    
    fig_comparison.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        title_font_color="#00FF00",
        xaxis_title_font_color="#00FF00",
        yaxis_title_font_color="#00FF00",
        showlegend=False,
        hovermode="x unified",
    )
    
    fig_comparison.update_traces(
        marker_line_color="#00FF00",
        marker_line_width=2,
    )
    
    st.plotly_chart(fig_comparison, use_container_width=True)

# --- Geração de PDF --- #
def generate_pdf_report(profile, impact_data, answers, recommendations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 255, 0)
    pdf.cell(0, 10, "Relatorio de Impacto Ambiental", 0, 1, "C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255)
    pdf.set_fill_color(26, 31, 58)
    pdf.multi_cell(0, 10, f"Seu Perfil: {profile['name']}\n{profile['desc']}", 0, "L", 1)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 255, 0)
    pdf.cell(0, 10, "Metricas de Impacto Anual", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 7, f"CO2 / ano: {impact_data['co2']:.1f} toneladas", 0, 1, "L")
    pdf.cell(0, 7, f"Arvores / ano: {int(impact_data['trees'])}", 0, 1, "L")
    pdf.cell(0, 7, f"Gelo Derretido: {impact_data['ice']:.1f} m2", 0, 1, "L")
    pdf.cell(0, 7, f"Agua Consumida: {int(impact_data['water']):,} litros", 0, 1, "L")
    pdf.cell(0, 7, f"Aquecimento: +{impact_data['warming']:.2f}C", 0, 1, "L")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 255, 0)
    pdf.cell(0, 10, "Distribuicao por Categoria", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255)
    for ans in answers:
        pdf.cell(0, 7, f"{ans['category']}: {ans['points']} pontos", 0, 1, "L")
    pdf.ln(5)

    if recommendations:
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(0, 255, 0)
        pdf.cell(0, 10, "Recomendacoes Personalizadas", 0, 1, "L")
        pdf.ln(2)

        pdf.set_font("Arial", "", 12)
        pdf.set_text_color(255, 255, 255)
        for rec in recommendations:
            pdf.multi_cell(0, 7, f"- {rec['title']}: {rec['desc']}", 0, "L", 0)
        pdf.ln(5)

    pdf_output = pdf.output(dest='S').encode('latin-1')
    return base64.b64encode(pdf_output).decode('latin-1')


# --- UI PRINCIPAL --- #
st.markdown("<h1 style='text-align: center;'>🌍 Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #999999;'>Descubra como suas escolhas diárias afetam o planeta</p>", unsafe_allow_html=True)

if not st.session_state.is_complete:
    # --- QUESTIONÁRIO --- #
    current_question = QUESTIONS[st.session_state.current_step]
    progress_percent = (st.session_state.current_step / len(QUESTIONS)) * 100

    st.progress(progress_percent / 100, text=f"Pergunta {st.session_state.current_step + 1} de {len(QUESTIONS)}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='stCard'>", unsafe_allow_html=True)
        st.subheader(current_question["title"])
        st.write(current_question["question"])

        selected_option_text = st.radio(
            "Escolha uma opção:",
            [option["text"] for option in current_question["options"]],
            key=f"radio_{current_question['id']}",
            index=None,
        )

        if selected_option_text:
            selected_option = next(option for option in current_question["options"] if option["text"] == selected_option_text)
            st.session_state.answers.append({
                "categoryId": current_question["id"],
                "category": current_question["title"],
                "points": selected_option["points"],
            })
            if st.session_state.current_step < len(QUESTIONS) - 1:
                st.session_state.current_step += 1
            else:
                st.session_state.is_complete = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        current_impact_score = sum(a["points"] for a in st.session_state.answers) if st.session_state.answers else 0
        impact_level = min(current_impact_score / 26, 1)
        render_globe_3d(impact_level)
        st.markdown("<p style='text-align: center; color: #999999;'><i>À medida que você responde, o globo reflete o nível de pressão sobre os ecossistemas</i></p>", unsafe_allow_html=True)

else:
    # --- RESULTADOS --- #
    impact_data = calculate_impact(st.session_state.answers)
    profile = get_profile(impact_data["total_score"])
    recommendations = generate_ai_recommendations(st.session_state.answers, profile["name"])

    st.markdown(f"""
    <div class='stCard' style='text-align: center; border-color: #00FF00; box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);'>
        <h2 style='color: #00FF00;'>{profile['name']}</h2>
        <p style='color: #FFFFFF;'>{profile['desc']}</p>
        <div style='display: flex; justify-content: center; gap: 50px; margin-top: 20px;'>
            <div>
                <p style='font-size: 2.5em; font-weight: bold; color: #00FF00;'>{impact_data['total_score']}</p>
                <p style='color: #999999;'>Pontuação Total</p>
            </div>
            <div>
                <p style='font-size: 2.5em; font-weight: bold; color: #FF9800;'>{impact_data['co2']:.1f}t</p>
                <p style='color: #999999;'>CO2/ano</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("--- ")

    # --- ABAS DE RESULTADOS --- #
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Distribuição", 
        "🌐 Globo 3D", 
        "⚡ Comparação Animada",
        "💡 Recomendações",
        "📥 Exportar"
    ])

    with tab1:
        col_viz1, col_viz2 = st.columns(2)
        with col_viz1:
            render_pizza_map(st.session_state.answers, impact_data["total_score"])
        with col_viz2:
            st.subheader("Métricas de Impacto Anual")
            metrics_col = st.columns(1)
            metrics = [
                {"label": "CO2 / ano", "value": f"{impact_data['co2']:.1f}t", "icon": "💨"},
                {"label": "Árvores / ano", "value": f"{int(impact_data['trees'])}", "icon": "🌳"},
                {"label": "Gelo Derretido", "value": f"{impact_data['ice']:.1f}m²", "icon": "🧊"},
                {"label": "Água Consumida", "value": f"{int(impact_data['water']):,}L", "icon": "💧"},
                {"label": "Aquecimento", "value": f"+{impact_data['warming']:.2f}°C", "icon": "🌡️"},
            ]
            for metric in metrics:
                st.markdown(f"""
                <div class='stCard' style='text-align: center; border-color: #1a1f3a; box-shadow: none;'>
                    <p style='font-size: 2em;'>{metric['icon']}</p>
                    <p style='font-size: 1.5em; font-weight: bold; color: #00FF00;'>{metric['value']}</p>
                    <p style='color: #999999;'>{metric['label']}</p>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        render_globe_3d(min(impact_data["total_score"] / 26, 1))

    with tab3:
        render_interactive_comparison(impact_data, profile)

    with tab4:
        st.subheader("Recomendações Personalizadas com IA")
        for rec in recommendations:
            st.markdown(f"""
            <div class='stCard' style='border-color: {"#00FF00" if rec["impact"] == "low" else "#FF9800" if rec["impact"] == "medium" else "#FF0000"};'>
                <h4 style='color: #00FF00;'>{rec['title']}</h4>
                <p style='color: #FFFFFF;'>{rec['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.subheader("Exportar Relatório")
        pdf_base64 = generate_pdf_report(profile, impact_data, st.session_state.answers, recommendations)
        st.download_button(
            label="📥 Baixar Relatório PDF",
            data=base64.b64decode(pdf_base64),
            file_name="relatorio_impacto_ambiental.pdf",
            mime="application/pdf",
            help="Baixe um relatório detalhado do seu impacto ambiental."
        )

        st.markdown("---")
        st.subheader("Compartilhar Resultados")
        share_text = f"Descobri meu impacto ambiental! Sou um {profile['name']} com {impact_data['total_score']} pontos. Teste também! 🌍"
        share_url = "https://carbon-footprint-tracker-tkfv5pthky3rk2gd8m9mm8.streamlit.app/"

        st.markdown(f"""
        <div style='display: flex; justify-content: center; gap: 15px; margin-top: 20px;'>
            <a href='https://twitter.com/intent/tweet?text={share_text}&url={share_url}' target='_blank'>
                <img src='https://img.icons8.com/color/48/000000/twitterx.png' alt='Twitter' width='40'>
            </a>
            <a href='https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title={share_text}' target='_blank'>
                <img src='https://img.icons8.com/color/48/000000/linkedin.png' alt='LinkedIn' width='40'>
            </a>
            <a href='https://api.whatsapp.com/send?text={share_text} {share_url}' target='_blank'>
                <img src='https://img.icons8.com/color/48/000000/whatsapp.png' alt='WhatsApp' width='40'>
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("--- ")
    st.button("🔄 Refazer Cálculo", on_click=reset_quiz)
