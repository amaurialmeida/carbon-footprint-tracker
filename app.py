import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from fpdf import FPDF
import base64

# --- Configurações da Página --- #
st.set_page_config(
    page_title="Calculadora de Impacto Ambiental",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Estilo Futurístico e Cores (Baseado no Portfólio) --- #
# Cores do portfólio: Dark Navy, Verde Neon, Vermelho/Laranja, Amarelo
# Cores do globo: gradiente azul -> verde -> amarelo -> vermelho

custom_css = """
<style>
    @import url(\'https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap\');

    /* Fundo principal */
    body {
        background-color: #0a0e27; /* Dark Navy */
        color: #FFFFFF; /* Texto principal branco */
        font-family: \'Space Mono\', monospace; /* Fonte futurística */
    }
    .stApp {
        background-color: #0a0e27;
        color: #FFFFFF;
    }
    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #00FF00; /* Verde Neon */
        font-family: \'Space Mono\', monospace;
    }
    /* Botões */
    .stButton>button {
        background-color: #00FF00; /* Verde Neon */
        color: #0a0e27; /* Texto Dark Navy */
        border-radius: 8px;
        border: 1px solid #00FF00;
        transition: all 0.3s ease;
        font-family: \'Space Mono\', monospace;
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
    /* Texto de opções */
    .stRadio > label > div {
        color: #FFFFFF;
    }
    /* Cores das opções do questionário */
    .option-style {
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        border: 1px solid transparent;
    }
    .option-style:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 255, 0, 0.2);
        border-color: #00FF00;
    }
    .option-blue { background-color: #2196F3; color: white; }
    .option-green { background-color: #4CAF50; color: white; }
    .option-yellow { background-color: #FFEB3B; color: black; }
    .option-orange { background-color: #FF9800; color: white; }
    .option-red { background-color: #F44336; color: white; }
    .option-purple { background-color: #9C27B0; color: white; }

    /* Estilo para o globo 3D (se for incorporado via HTML/JS) */
    #globe-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
        background-color: #1a1f3a;
    }
    .stPlotlyChart {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
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
    # Simulações de métricas de impacto (ajustar conforme dados reais)
    co2 = total_score * 0.8  # toneladas/ano
    trees = co2 * 45  # árvores
    ice = co2 * 3  # m² de gelo derretido
    water = co2 * 2000 # litros
    warming = total_score * 0.01 # °C
    return {"total_score": total_score, "co2": co2, "trees": trees, "ice": ice, "water": water, "warming": warming}

def get_profile(total_score):
    for p in PROFILES:
        if p["range"][0] <= total_score <= p["range"][1]:
            return p
    return PROFILES[0] # Default

def generate_ai_recommendations(answers, profile_name):
    # Esta é uma simulação. Em um cenário real, você chamaria uma API de LLM aqui.
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
    # impact_level de 0 (verde) a 1 (vermelho)
    # Cores do seu globo interativo: gradiente azul -> verde -> amarelo -> vermelho
    color_scale = [
        [0.0, "#00FF00"],  # Verde Neon (baixo impacto)
        [0.3, "#FFFF00"],  # Amarelo (médio impacto)
        [0.7, "#FF9800"],  # Laranja (alto impacto)
        [1.0, "#FF0000"],  # Vermelho (muito alto impacto)
    ]
    
    # Usando um mapa-múndi real com Plotly
    fig = px.choropleth(
        pd.DataFrame({"country": ["World"], "impact": [impact_level]}),
        locations=["World"],
        locationmode="country names",
        color="impact",
        color_continuous_scale=color_scale,
        range_color=[0, 1],
        projection="orthographic",
        title="Visualização de Impacto Global",
    )
    fig.update_geos(
        showland=True, landcolor="#1a1f3a",
        showocean=True, oceancolor="#0a0e27",
        showcountries=True, countrycolor="#00FF00",
        showframe=False, showcoastlines=False
    )
    fig.update_layout(
        height=400,
        margin={"r":0,"t":50,"l":0,"b":0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        title_font_color="#00FF00",
        coloraxis_showscale=False,
        geo=dict(
            bgcolor=\'rgba(0,0,0,0)\'
            lakecolor=\'#0a0e27\'
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de Pizza no Mapa --- #
def render_pizza_map(answers_data, total_score):
    df_answers = pd.DataFrame(answers_data)
    
    # Cores para o gráfico de pizza (baseado nas cores das opções)
    pie_colors = {
        "Mobilidade": "#2196F3",
        "Alimentação": "#4CAF50",
        "Consumo de Moda": "#FFEB3B",
        "Tecnologia": "#FF9800",
        "Energia": "#F44336",
    }
    # Mapear as cores para as categorias respondidas
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
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#FFFFFF",
        showlegend=True,
        legend=dict(font=dict(color="#FFFFFF"))
    )
    
    st.subheader("Distribuição de Impacto por Categoria")
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown("<p style=\'text-align: center; color: #999999;\'><i>Este gráfico representa a distribuição do seu impacto, como fatias sobre um mapa-múndi.</i></p>", unsafe_allow_html=True)

# --- Geração de PDF --- #
def generate_pdf_report(profile, impact_data, answers, recommendations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 255, 0) # Verde Neon
    pdf.cell(0, 10, "Relatório de Impacto Ambiental", 0, 1, "C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255) # Branco
    pdf.set_fill_color(26, 31, 58) # Dark Navy mais claro
    pdf.multi_cell(0, 10, f"Seu Perfil: {profile['name']}\n{profile['desc']}", 0, "L", 1)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 255, 0)
    pdf.cell(0, 10, "Métricas de Impacto Anual", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 7, f"💨 CO2 / ano: {impact_data['co2']:.1f} toneladas", 0, 1, "L")
    pdf.cell(0, 7, f"🌳 Árvores / ano: {int(impact_data['trees'])}", 0, 1, "L")
    pdf.cell(0, 7, f"🧊 Gelo Derretido: {impact_data['ice']:.1f} m²", 0, 1, "L")
    pdf.cell(0, 7, f"💧 Água Consumida: {int(impact_data['water']):,} litros", 0, 1, "L")
    pdf.cell(0, 7, f"🌡️ Aquecimento: +{impact_data['warming']:.2f}°C", 0, 1, "L")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 255, 0)
    pdf.cell(0, 10, "Distribuição por Categoria", 0, 1, "L")
    pdf.ln(2)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(255, 255, 255)
    for ans in answers:
        pdf.cell(0, 7, f"{ans['category']}: {ans['points']} pontos", 0, 1, "L")
    pdf.ln(5)

    if recommendations:
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(0, 255, 0)
        pdf.cell(0, 10, "Recomendações Personalizadas", 0, 1, "L")
        pdf.ln(2)

        pdf.set_font("Arial", "", 12)
        pdf.set_text_color(255, 255, 255)
        for rec in recommendations:
            pdf.multi_cell(0, 7, f"- {rec['title']}: {rec['desc']}", 0, "L", 0)
        pdf.ln(5)

    pdf_output = pdf.output(dest='S').encode('latin-1')
    return base64.b64encode(pdf_output).decode('latin-1')


# --- UI do Questionário --- #
if not st.session_state.is_complete:
    current_question = QUESTIONS[st.session_state.current_step]
    progress_percent = (st.session_state.current_step / len(QUESTIONS)) * 100

    st.markdown("<h1 style=\'text-align: center;\'>🌍 Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)
    st.markdown("<p style=\'text-align: center; color: #999999;\'>Descubra como suas escolhas diárias afetam o planeta</p>", unsafe_allow_html=True)

    st.progress(progress_percent, text=f"Pergunta {st.session_state.current_step + 1} de {len(QUESTIONS)}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"<div class=\'stCard\'>", unsafe_allow_html=True)
        st.subheader(current_question["title"])
        st.write(current_question["question"])

        selected_option_text = st.radio(
            "Escolha uma opção:",
            [option["text"] for option in current_question["options"]],
            key=f"radio_{current_question["id"]}",
            index=None, # Permite que nenhuma opção seja selecionada inicialmente
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
        # Simulação do impacto no globo
        current_impact_score = sum(a["points"] for a in st.session_state.answers) if st.session_state.answers else 0
        impact_level = min(current_impact_score / 26, 1) # Max score 26
        render_globe_3d(impact_level)
        st.markdown("<p style=\'text-align: center; color: #999999;\'><i>À medida que você responde, o globo reflete o nível de pressão sobre os ecossistemas</i></p>", unsafe_allow_html=True)

else: # --- Tela de Resultados --- #
    impact_data = calculate_impact(st.session_state.answers)
    profile = get_profile(impact_data["total_score"])
    recommendations = generate_ai_recommendations(st.session_state.answers, profile["name"])

    st.markdown("<h1 style=\'text-align: center;\'>🌍 Seus Resultados</h1>", unsafe_allow_html=True)
    st.markdown("<p style=\'text-align: center; color: #999999;\'>Análise completa do seu impacto ambiental</p>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class=\'stCard\' style=\'text-align: center; border-color: #00FF00; box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);\'>
        <h2 style=\'color: #00FF00;\'>{profile['name']}</h2>
        <p style=\'color: #FFFFFF;\'>{profile['desc']}</p>
        <div style=\'display: flex; justify-content: center; gap: 50px; margin-top: 20px;\'>
            <div>
                <p style=\'font-size: 2.5em; font-weight: bold; color: #00FF00;\'>{impact_data['total_score']}</p>
                <p style=\'color: #999999;\'>Pontuação Total</p>
            </div>
            <div>
                <p style=\'font-size: 2.5em; font-weight: bold; color: #FF9800;\'>{impact_data['co2']:.1f}t</p>
                <p style=\'color: #999999;\'>CO2/ano</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("--- ")

    col_viz1, col_viz2 = st.columns(2)
    with col_viz1:
        render_pizza_map(st.session_state.answers, impact_data["total_score"])
    with col_viz2:
        render_globe_3d(min(impact_data["total_score"] / 26, 1))

    st.markdown("--- ")

    st.subheader("Métricas de Impacto Anual")
    metrics_col = st.columns(5)
    metrics = [
        {"label": "CO2 / ano", "value": f"{impact_data['co2']:.1f}t", "icon": "💨"},
        {"label": "Árvores / ano", "value": f"{int(impact_data['trees'])}", "icon": "🌳"},
        {"label": "Gelo Derretido", "value": f"{impact_data['ice']:.1f}m²", "icon": "🧊"},
        {"label": "Água Consumida", "value": f"{int(impact_data['water']):,}L", "icon": "💧"},
        {"label": "Aquecimento", "value": f"\+{impact_data['warming']:.2f}°C", "icon": "🌡️"},
    ]
    for i, metric in enumerate(metrics):
        with metrics_col[i]:
            st.markdown(f"""
            <div class=\'stCard\' style=\'text-align: center; border-color: #1a1f3a; box-shadow: none;\'>
                <p style=\'font-size: 2em;\'>{metric['icon']}</p>
                <p style=\'font-size: 1.5em; font-weight: bold; color: #00FF00;\'>{metric['value']}</p>
                <p style=\'color: #999999;\'> {metric['label']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("--- ")

    st.subheader("Análise Comparativa Global")
    global_average_co2 = 4.8 # Exemplo
    global_average_score = 13 # Exemplo
    percentile = int((1 - (impact_data["total_score"] / 26)) * 100) # Simulação

    st.markdown(f"""
    <div class=\'stCard\'>
        <div style=\'display: flex; justify-content: space-around; text-align: center;\'>
            <div>
                <h3 style=\'color: #00FF00;\'>Seu CO2</h3>
                <p style=\'font-size: 1.8em; font-weight: bold; color: #FFFFFF;\'>{impact_data['co2']:.1f}t</p>
            </div>
            <div>
                <h3 style=\'color: #00FF00;\'>Média Global</h3>
                <p style=\'font-size: 1.8em; font-weight: bold; color: #FFFFFF;\'>{global_average_co2:.1f}t</p>
            </div>
            <div>
                <h3 style=\'color: #00FF00;\'>Seu Percentil</h3>
                <p style=\'font-size: 1.8em; font-weight: bold; color: #FFFFFF;\'>{percentile}%</p>
            </div>
        </div>
        <p style=\'text-align: center; color: #999999; margin-top: 20px;\'>
            Você está no top {100 - percentile}% de menor impacto ambiental. { 'Parabéns!' if percentile > 50 else 'Há espaço para melhorias.' }
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("--- ")

    st.subheader("Recomendações Personalizadas com IA")
    for rec in recommendations:
        st.markdown(f"""
        <div class=\'stCard\' style=\'border-color: {'#00FF00' if rec['impact'] == 'low' else '#FF9800' if rec['impact'] == 'medium' else '#FF0000'};\'>
            <h4 style=\'color: #00FF00;\'>{rec['title']}</h4>
            <p style=\'color: #FFFFFF;\'>{rec['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    if not recommendations:
        st.info("Parabéns! Você já está seguindo as melhores práticas. Continue assim! 🌱")

    st.markdown("--- ")

    st.subheader("Exportar e Compartilhar")
    pdf_base64 = generate_pdf_report(profile, impact_data, st.session_state.answers, recommendations)
    st.download_button(
        label="Baixar Relatório PDF",
        data=base64.b64decode(pdf_base64),
        file_name="relatorio_impacto_ambiental.pdf",
        mime="application/pdf",
        help="Baixe um relatório detalhado do seu impacto ambiental."
    )

    share_text = f"Descobri meu impacto ambiental! Sou um \"{profile['name']}\" com {impact_data['total_score']} pontos. Estou no top {percentile}% de menor impacto. Teste também! 🌍"
    share_url = "https://share.streamlit.io/YOUR_APP_URL" # Substituir pela URL real do seu app

    st.markdown(f"""
    <div style=\'display: flex; justify-content: center; gap: 15px; margin-top: 20px;\'>
        <a href=\'https://twitter.com/intent/tweet?text={share_text}&url={share_url}\' target=\'_blank\'>
            <img src=\'https://img.icons8.com/color/48/000000/twitterx.png\' alt=\'Twitter\' width=\'40\'>
        </a>
        <a href=\'https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title={share_text}\' target=\'_blank\'>
            <img src=\'https://img.icons8.com/color/48/000000/linkedin.png\' alt=\'LinkedIn\' width=\'40\'>
        </a>
        <a href=\'https://api.whatsapp.com/send?text={share_text} {share_url}\' target=\'_blank\'>
            <img src=\'https://img.icons8.com/color/48/000000/whatsapp.png\' alt=\'WhatsApp\' width=\'40\'>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("--- ")

    st.button("Refazer Cálculo", on_click=reset_quiz)
