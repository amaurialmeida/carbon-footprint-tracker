"""Textos da Calculadora de Impacto em 10 idiomas (mesmos do portfólio).

Edite aqui para corrigir qualquer tradução. Estrutura idêntica em todos os idiomas.
"""

TRANSLATIONS = {
 "pt": {
  "page_title": "Pegada — Calculadora de Impacto Ambiental",
  "lang_label": "Idioma",
  "eyebrow": "Calculadora de impacto · 5 perguntas",
  "hero_title": "Qual é a sua<br>pegada no planeta?",
  "hero_sub": "Responda com honestidade. A cada resposta, o globo ao lado reage em tempo real ao seu nível de impacto.",
  "progress": "Pergunta {n} de {total}",
  "cat_eyebrow": "Categoria {n} · {title}",
  "choose": "Escolha uma opção",
  "globe_caption": "O globo reflete, em tempo real, a pressão do seu estilo de vida sobre os ecossistemas",
  "result_eyebrow": "Resultado",
  "score_label": "Pontuação total",
  "co2_year": "CO₂ por ano",
  "tabs": [
   "Distribuição",
   "Globo 3D",
   "Comparação",
   "Recomendações",
   "Tecnologia & Exportar"
  ],
  "dist_title": "Distribuição por categoria",
  "metrics_title": "Métricas de impacto anual",
  "metric_labels": [
   "CO₂ / ano",
   "Árvores / ano",
   "Gelo derretido",
   "Água consumida",
   "Aquecimento"
  ],
  "globe_tab_title": "O planeta segundo suas escolhas",
  "globe_tab_caption": "Cada ponto pulsante representa uma categoria respondida — quanto mais intenso, maior a pressão daquele hábito.",
  "compare_title": "Como você se compara",
  "scenarios": [
   "Seu perfil",
   "Média global",
   "Cenário sustentável",
   "Cenário crítico"
  ],
  "co2_unit": "CO₂/ano",
  "co2_axis": "CO₂ (t/ano)",
  "rec_title": "Recomendações personalizadas",
  "tech_title": "Sobre a tecnologia deste projeto",
  "tech_intro": "Este calculador combina um back-end declarativo em Python com uma camada de visualização WebGL renderizada sob demanda. A ideia central — fazer uma cena 3D reagir a dados em tempo real conforme o usuário interage — foi inspirada na abordagem generativa usada em <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, um projeto de visualização de jogadas de futebol que reconstrói lances em cena 3D a partir de dados de rastreamento (tracking data).",
  "making_title": "Making-of: duas abordagens de visualização generativa",
  "making_intro": "Embora sirvam a propósitos completamente diferentes, os dois projetos compartilham o mesmo problema central de engenharia: <i>como transformar dados brutos em uma cena viva, sem pré-renderizar cada quadro?</i> A tabela abaixo resume as escolhas técnicas de cada um.",
  "th_aspect": "Aspecto",
  "th_this": "Este projeto (Pegada)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Fonte de dados",
    "Respostas do questionário, calculadas no servidor a cada interação",
    "Tracking data posicional de partidas reais (coordenadas de jogadores/bola por frame)"
   ],
   [
    "Motor de renderização",
    "Three.js / WebGL, embutido via componente HTML no Streamlit",
    "Canvas/WebGL customizado, motor próprio de física e câmera"
   ],
   [
    "O que reage aos dados",
    "Cor do globo, hotspots por categoria, intensidade do \"índice de pressão\"",
    "Trajetórias de jogadores, câmera dinâmica, eventos (passes, chutes, duelos)"
   ],
   [
    "Interatividade",
    "Rotação manual do globo, atualização a cada resposta do quiz",
    "Parâmetros configuráveis via URL (JSON codificado), replay de lances"
   ],
   [
    "Stack de back-end",
    "Python + Streamlit (server-side rendering do estado)",
    "Estático / client-side, config embutida na própria URL"
   ],
   [
    "Objetivo da cena 3D",
    "Traduzir um score abstrato em uma metáfora visual imediata",
    "Reconstruir e analisar eventos esportivos reais com fidelidade tática"
   ]
  ],
  "lesson": "A principal lição incorporada aqui: pequenas cenas 3D reativas comunicam ordens de grandeza muito mais rápido do que tabelas — o cérebro humano lê cor e movimento antes de ler números.",
  "export_title": "Exportar & compartilhar",
  "pdf_button": "📥 Baixar relatório em PDF",
  "share_text": "Descobri meu impacto ambiental! Sou {profile} com {score} pontos.",
  "retry": "🔄 Refazer cálculo",
  "methodology_note": "Estimativa educativa: a pontuação converte respostas em faixas e multiplica por 0,8 t de CO₂ por ponto. Não substitui um inventário de emissões.",
  "questions": [
   {
    "title": "Mobilidade",
    "question": "Quantos km você se locomove por dia (ida e volta)?",
    "options": [
     "0 a 5 km",
     "6 a 15 km",
     "16 a 40 km",
     "41 a 100 km",
     "101 a 200 km",
     "Mais de 200 km"
    ]
   },
   {
    "title": "Alimentação",
    "question": "Quantas refeições com carne você faz por semana?",
    "options": [
     "Nenhuma, sou vegetariano(a)",
     "1 a 3 refeições",
     "4 a 7 refeições",
     "8 a 14 refeições",
     "Mais de 14 refeições"
    ]
   },
   {
    "title": "Consumo de Moda",
    "question": "Quantas peças de roupa nova você compra por mês?",
    "options": [
     "0 - só quando necessário",
     "1 a 2 peças",
     "3 a 5 peças",
     "6 a 10 peças",
     "Mais de 10 peças"
    ]
   },
   {
    "title": "Tecnologia",
    "question": "Com que frequência você compra um celular novo?",
    "options": [
     "A cada 5 anos ou mais",
     "A cada 3 a 4 anos",
     "A cada 2 anos",
     "Todo ano",
     "Menos de 1 ano"
    ]
   },
   {
    "title": "Energia",
    "question": "Qual o consumo médio de energia elétrica na sua casa?",
    "options": [
     "Até 150 kWh/mês",
     "151 a 300 kWh/mês",
     "301 a 500 kWh/mês",
     "501 a 800 kWh/mês",
     "Mais de 800 kWh/mês"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Guardião da Terra",
    "desc": "Seu estilo de vida é altamente sustentável. Você é um exemplo de regeneração!"
   },
   {
    "name": "Consciente em Evolução",
    "desc": "Você está no caminho certo, mas pequenas mudanças podem reduzir ainda mais sua pegada."
   },
   {
    "name": "Impacto Moderado",
    "desc": "Seu impacto é perceptível. Considere revisar hábitos de consumo e transporte."
   },
   {
    "name": "Alerta Ambiental",
    "desc": "Seu padrão de vida exige recursos que o planeta não consegue repor rapidamente."
   },
   {
    "name": "Crise Planetária",
    "desc": "Se todos vivessem como você, precisaríamos de vários planetas Terra."
   }
  ],
  "recs": {
   "transport": {
    "title": "Considere transporte público",
    "desc": "Usar transporte público reduz sua pegada de carbono em até 75% comparado a dirigir sozinho."
   },
   "meat": {
    "title": "Reduza o consumo de carne",
    "desc": "Adotar uma dieta com menos carne pode reduzir sua pegada de carbono em até 50%."
   },
   "fashion": {
    "title": "Compre roupas com mais critério",
    "desc": "Escolher marcas sustentáveis e comprar menos reduz o impacto têxtil significativamente."
   },
   "phone": {
    "title": "Estenda a vida do seu celular",
    "desc": "Manter o aparelho por mais tempo reduz resíduos eletrônicos e emissões de manufatura."
   },
   "solar": {
    "title": "Considere energia solar",
    "desc": "Painéis solares podem reduzir sua pegada de energia em até 80%."
   },
   "renewable": {
    "title": "Avalie energia renovável",
    "desc": "Contratar energia renovável de sua concessionária costuma ser uma opção acessível."
   },
   "great": {
    "title": "Parabéns!",
    "desc": "Você já segue as melhores práticas. Continue assim."
   }
  },
  "globe_hud": "Índice de Pressão",
  "globe_legend": "arraste para girar · scroll para zoom",
  "globe_intensity": "Intensidade",
  "pdf": {
   "file": "relatorio_impacto_ambiental.pdf",
   "title": "Relatório de Impacto Ambiental",
   "profile": "Seu Perfil",
   "metrics": "Métricas de Impacto Anual",
   "co2": "CO2 / ano: {v} toneladas",
   "trees": "Árvores / ano: {v}",
   "ice": "Gelo derretido: {v} m2",
   "water": "Água consumida: {v} litros",
   "warming": "Aquecimento: +{v} °C",
   "dist": "Distribuição por Categoria",
   "points": "{cat}: {n} pontos",
   "recs": "Recomendações Personalizadas"
  }
 },
 "en": {
  "page_title": "Footprint — Environmental Impact Calculator",
  "lang_label": "Language",
  "eyebrow": "Impact calculator · 5 questions",
  "hero_title": "What is your<br>footprint on the planet?",
  "hero_sub": "Answer honestly. With each answer, the globe beside you reacts in real time to your level of impact.",
  "progress": "Question {n} of {total}",
  "cat_eyebrow": "Category {n} · {title}",
  "choose": "Choose an option",
  "globe_caption": "The globe reflects, in real time, the pressure your lifestyle puts on ecosystems",
  "result_eyebrow": "Result",
  "score_label": "Total score",
  "co2_year": "CO₂ per year",
  "tabs": [
   "Breakdown",
   "3D Globe",
   "Comparison",
   "Recommendations",
   "Technology & Export"
  ],
  "dist_title": "Breakdown by category",
  "metrics_title": "Annual impact metrics",
  "metric_labels": [
   "CO₂ / year",
   "Trees / year",
   "Ice melted",
   "Water used",
   "Warming"
  ],
  "globe_tab_title": "The planet according to your choices",
  "globe_tab_caption": "Each pulsing dot represents an answered category — the more intense it is, the greater the pressure from that habit.",
  "compare_title": "How you compare",
  "scenarios": [
   "Your profile",
   "Global average",
   "Sustainable scenario",
   "Critical scenario"
  ],
  "co2_unit": "CO₂/year",
  "co2_axis": "CO₂ (t/year)",
  "rec_title": "Personalized recommendations",
  "tech_title": "About this project's technology",
  "tech_intro": "This calculator combines a declarative Python back end with an on-demand WebGL visualization layer. The core idea — making a 3D scene react to real-time data as the user interacts — was inspired by the generative approach used in <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, a soccer play visualization project that rebuilds plays as 3D scenes from tracking data.",
  "making_title": "Making-of: two approaches to generative visualization",
  "making_intro": "Although they serve completely different purposes, the two projects share the same core engineering problem: <i>how do you turn raw data into a living scene without pre-rendering every frame?</i> The table below summarizes each one's technical choices.",
  "th_aspect": "Aspect",
  "th_this": "This project (Footprint)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Data source",
    "Quiz answers, computed on the server at every interaction",
    "Positional tracking data from real matches (player/ball coordinates per frame)"
   ],
   [
    "Rendering engine",
    "Three.js / WebGL, embedded via an HTML component in Streamlit",
    "Custom Canvas/WebGL, with its own physics and camera engine"
   ],
   [
    "What reacts to the data",
    "Globe color, hotspots per category, intensity of the \"pressure index\"",
    "Player trajectories, dynamic camera, events (passes, shots, duels)"
   ],
   [
    "Interactivity",
    "Manual globe rotation, updated with each quiz answer",
    "Parameters configurable via URL (encoded JSON), play replays"
   ],
   [
    "Back-end stack",
    "Python + Streamlit (server-side rendering of state)",
    "Static / client-side, config embedded in the URL itself"
   ],
   [
    "Purpose of the 3D scene",
    "Turn an abstract score into an immediate visual metaphor",
    "Reconstruct and analyze real sports events with tactical fidelity"
   ]
  ],
  "lesson": "The main lesson built into this project: small reactive 3D scenes communicate orders of magnitude much faster than tables — the human brain reads color and motion before it reads numbers.",
  "export_title": "Export & share",
  "pdf_button": "📥 Download PDF report",
  "share_text": "I found out my environmental impact! I'm {profile} with {score} points.",
  "retry": "🔄 Recalculate",
  "methodology_note": "Educational estimate: the score converts answers into ranges and multiplies by 0.8 t of CO₂ per point. It does not replace an emissions inventory.",
  "questions": [
   {
    "title": "Mobility",
    "question": "How many miles do you travel per day (round trip)?",
    "options": [
     "0 to 5 km",
     "6 to 15 km",
     "16 to 40 km",
     "41 to 100 km",
     "101 to 200 km",
     "More than 200 km"
    ]
   },
   {
    "title": "Food",
    "question": "How many meals with meat do you eat per week?",
    "options": [
     "None, I'm vegetarian",
     "1 to 3 meals",
     "4 to 7 meals",
     "8 to 14 meals",
     "More than 14 meals"
    ]
   },
   {
    "title": "Fashion Consumption",
    "question": "How many new items of clothing do you buy per month?",
    "options": [
     "0 - only when necessary",
     "1 to 2 items",
     "3 to 5 items",
     "6 to 10 items",
     "More than 10 items"
    ]
   },
   {
    "title": "Technology",
    "question": "How often do you buy a new phone?",
    "options": [
     "Every 5 years or more",
     "Every 3 to 4 years",
     "Every 2 years",
     "Every year",
     "Less than 1 year"
    ]
   },
   {
    "title": "Energy",
    "question": "What is the average electricity consumption in your home?",
    "options": [
     "Up to 150 kWh/month",
     "151 to 300 kWh/month",
     "301 to 500 kWh/month",
     "501 to 800 kWh/month",
     "More than 800 kWh/month"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Earth Guardian",
    "desc": "Your lifestyle is highly sustainable. You are an example of regeneration!"
   },
   {
    "name": "Conscious in Progress",
    "desc": "You're on the right track, but small changes can reduce your footprint even further."
   },
   {
    "name": "Moderate Impact",
    "desc": "Your impact is noticeable. Consider reviewing your consumption and transportation habits."
   },
   {
    "name": "Environmental Alert",
    "desc": "Your way of life demands resources that the planet can't replenish quickly."
   },
   {
    "name": "Planetary Crisis",
    "desc": "If everyone lived like you, we would need several Planet Earths."
   }
  ],
  "recs": {
   "transport": {
    "title": "Consider public transportation",
    "desc": "Using public transportation reduces your carbon footprint by up to 75% compared to driving alone."
   },
   "meat": {
    "title": "Reduce your meat consumption",
    "desc": "Adopting a diet with less meat can reduce your carbon footprint by up to 50%."
   },
   "fashion": {
    "title": "Be more selective when buying clothes",
    "desc": "Choosing sustainable brands and buying less significantly reduces textile impact."
   },
   "phone": {
    "title": "Extend your phone's life",
    "desc": "Keeping your device longer reduces electronic waste and manufacturing emissions."
   },
   "solar": {
    "title": "Consider solar power",
    "desc": "Solar panels can reduce your energy footprint by up to 80%."
   },
   "renewable": {
    "title": "Look into renewable energy",
    "desc": "Signing up for renewable energy from your utility is often an affordable option."
   },
   "great": {
    "title": "Congratulations!",
    "desc": "You already follow best practices. Keep it up."
   }
  },
  "globe_hud": "Pressure Index",
  "globe_legend": "drag to rotate · scroll to zoom",
  "globe_intensity": "Intensity",
  "pdf": {
   "file": "environmental_impact_report.pdf",
   "title": "Environmental Impact Report",
   "profile": "Your Profile",
   "metrics": "Annual Impact Metrics",
   "co2": "CO2 / year: {v} tons",
   "trees": "Trees / year: {v}",
   "ice": "Ice melted: {v} m2",
   "water": "Water used: {v} liters",
   "warming": "Warming: +{v} °C",
   "dist": "Breakdown by Category",
   "points": "{cat}: {n} points",
   "recs": "Personalized Recommendations"
  }
 },
 "es": {
  "page_title": "Huella — Calculadora de Impacto Ambiental",
  "lang_label": "Idioma",
  "eyebrow": "Calculadora de impacto · 5 preguntas",
  "hero_title": "¿Cuál es tu<br>huella en el planeta?",
  "hero_sub": "Responde con honestidad. Con cada respuesta, el globo de al lado reacciona en tiempo real a tu nivel de impacto.",
  "progress": "Pregunta {n} de {total}",
  "cat_eyebrow": "Categoría {n} · {title}",
  "choose": "Elige una opción",
  "globe_caption": "El globo refleja, en tiempo real, la presión de tu estilo de vida sobre los ecosistemas",
  "result_eyebrow": "Resultado",
  "score_label": "Puntuación total",
  "co2_year": "CO₂ por año",
  "tabs": [
   "Distribución",
   "Globo 3D",
   "Comparación",
   "Recomendaciones",
   "Tecnología y Exportar"
  ],
  "dist_title": "Distribución por categoría",
  "metrics_title": "Métricas de impacto anual",
  "metric_labels": [
   "CO₂ / año",
   "Árboles / año",
   "Hielo derretido",
   "Agua consumida",
   "Calentamiento"
  ],
  "globe_tab_title": "El planeta según tus decisiones",
  "globe_tab_caption": "Cada punto pulsante representa una categoría respondida: cuanto más intenso, mayor es la presión de ese hábito.",
  "compare_title": "Cómo te comparas",
  "scenarios": [
   "Tu perfil",
   "Promedio mundial",
   "Escenario sostenible",
   "Escenario crítico"
  ],
  "co2_unit": "CO₂/año",
  "co2_axis": "CO₂ (t/año)",
  "rec_title": "Recomendaciones personalizadas",
  "tech_title": "Sobre la tecnología de este proyecto",
  "tech_intro": "Esta calculadora combina un back-end declarativo en Python con una capa de visualización WebGL renderizada bajo demanda. La idea central —hacer que una escena 3D reaccione a datos en tiempo real según interactúa el usuario— se inspiró en el enfoque generativo de <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, un proyecto de visualización de jugadas de fútbol que reconstruye jugadas en escenas 3D a partir de datos de seguimiento (tracking data).",
  "making_title": "Making-of: dos enfoques de visualización generativa",
  "making_intro": "Aunque sirven a propósitos completamente distintos, los dos proyectos comparten el mismo problema central de ingeniería: <i>¿cómo convertir datos en bruto en una escena viva, sin prerrenderizar cada fotograma?</i> La tabla siguiente resume las decisiones técnicas de cada uno.",
  "th_aspect": "Aspecto",
  "th_this": "Este proyecto (Huella)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Fuente de datos",
    "Respuestas del cuestionario, calculadas en el servidor en cada interacción",
    "Tracking data posicional de partidos reales (coordenadas de jugadores/balón por fotograma)"
   ],
   [
    "Motor de renderizado",
    "Three.js / WebGL, integrado mediante un componente HTML en Streamlit",
    "Canvas/WebGL personalizado, con motor propio de física y cámara"
   ],
   [
    "Qué reacciona a los datos",
    "Color del globo, puntos calientes por categoría, intensidad del \"índice de presión\"",
    "Trayectorias de jugadores, cámara dinámica, eventos (pases, tiros, duelos)"
   ],
   [
    "Interactividad",
    "Rotación manual del globo, actualización con cada respuesta del quiz",
    "Parámetros configurables mediante URL (JSON codificado), repetición de jugadas"
   ],
   [
    "Stack de back-end",
    "Python + Streamlit (renderizado del estado en el servidor)",
    "Estático / en el cliente, configuración integrada en la propia URL"
   ],
   [
    "Objetivo de la escena 3D",
    "Traducir una puntuación abstracta en una metáfora visual inmediata",
    "Reconstruir y analizar eventos deportivos reales con fidelidad táctica"
   ]
  ],
  "lesson": "La principal lección incorporada aquí: las pequeñas escenas 3D reactivas comunican órdenes de magnitud mucho más rápido que las tablas; el cerebro humano lee color y movimiento antes que números.",
  "export_title": "Exportar y compartir",
  "pdf_button": "📥 Descargar informe en PDF",
  "share_text": "¡Descubrí mi impacto ambiental! Soy {profile} con {score} puntos.",
  "retry": "🔄 Volver a calcular",
  "methodology_note": "Estimación educativa: la puntuación convierte las respuestas en rangos y multiplica por 0,8 t de CO₂ por punto. No sustituye un inventario de emisiones.",
  "questions": [
   {
    "title": "Movilidad",
    "question": "¿Cuántos km te desplazas por día (ida y vuelta)?",
    "options": [
     "0 a 5 km",
     "6 a 15 km",
     "16 a 40 km",
     "41 a 100 km",
     "101 a 200 km",
     "Más de 200 km"
    ]
   },
   {
    "title": "Alimentación",
    "question": "¿Cuántas comidas con carne haces por semana?",
    "options": [
     "Ninguna, soy vegetariano/a",
     "1 a 3 comidas",
     "4 a 7 comidas",
     "8 a 14 comidas",
     "Más de 14 comidas"
    ]
   },
   {
    "title": "Consumo de Moda",
    "question": "¿Cuántas prendas de ropa nuevas compras por mes?",
    "options": [
     "0 - solo cuando es necesario",
     "1 a 2 prendas",
     "3 a 5 prendas",
     "6 a 10 prendas",
     "Más de 10 prendas"
    ]
   },
   {
    "title": "Tecnología",
    "question": "¿Con qué frecuencia compras un celular nuevo?",
    "options": [
     "Cada 5 años o más",
     "Cada 3 a 4 años",
     "Cada 2 años",
     "Todos los años",
     "Menos de 1 año"
    ]
   },
   {
    "title": "Energía",
    "question": "¿Cuál es el consumo medio de electricidad en tu casa?",
    "options": [
     "Hasta 150 kWh/mes",
     "151 a 300 kWh/mes",
     "301 a 500 kWh/mes",
     "501 a 800 kWh/mes",
     "Más de 800 kWh/mes"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Guardián de la Tierra",
    "desc": "Tu estilo de vida es altamente sostenible. ¡Eres un ejemplo de regeneración!"
   },
   {
    "name": "Consciente en Evolución",
    "desc": "Vas por buen camino, pero pequeños cambios pueden reducir aún más tu huella."
   },
   {
    "name": "Impacto Moderado",
    "desc": "Tu impacto es perceptible. Considera revisar tus hábitos de consumo y transporte."
   },
   {
    "name": "Alerta Ambiental",
    "desc": "Tu forma de vida exige recursos que el planeta no puede reponer con rapidez."
   },
   {
    "name": "Crisis Planetaria",
    "desc": "Si todos vivieran como tú, necesitaríamos varios planetas Tierra."
   }
  ],
  "recs": {
   "transport": {
    "title": "Considera el transporte público",
    "desc": "Usar el transporte público reduce tu huella de carbono hasta un 75% en comparación con conducir solo."
   },
   "meat": {
    "title": "Reduce el consumo de carne",
    "desc": "Adoptar una dieta con menos carne puede reducir tu huella de carbono hasta un 50%."
   },
   "fashion": {
    "title": "Compra ropa con más criterio",
    "desc": "Elegir marcas sostenibles y comprar menos reduce significativamente el impacto textil."
   },
   "phone": {
    "title": "Alarga la vida de tu celular",
    "desc": "Conservar el dispositivo por más tiempo reduce los residuos electrónicos y las emisiones de fabricación."
   },
   "solar": {
    "title": "Considera la energía solar",
    "desc": "Los paneles solares pueden reducir tu huella energética hasta un 80%."
   },
   "renewable": {
    "title": "Evalúa la energía renovable",
    "desc": "Contratar energía renovable con tu compañía eléctrica suele ser una opción accesible."
   },
   "great": {
    "title": "¡Felicidades!",
    "desc": "Ya sigues las mejores prácticas. Sigue así."
   }
  },
  "globe_hud": "Índice de Presión",
  "globe_legend": "arrastra para girar · scroll para hacer zoom",
  "globe_intensity": "Intensidad",
  "pdf": {
   "file": "informe_impacto_ambiental.pdf",
   "title": "Informe de Impacto Ambiental",
   "profile": "Tu Perfil",
   "metrics": "Métricas de Impacto Anual",
   "co2": "CO2 / año: {v} toneladas",
   "trees": "Árboles / año: {v}",
   "ice": "Hielo derretido: {v} m2",
   "water": "Agua consumida: {v} litros",
   "warming": "Calentamiento: +{v} °C",
   "dist": "Distribución por Categoría",
   "points": "{cat}: {n} puntos",
   "recs": "Recomendaciones Personalizadas"
  }
 },
 "it": {
  "page_title": "Impronta — Calcolatore di Impatto Ambientale",
  "lang_label": "Lingua",
  "eyebrow": "Calcolatore di impatto · 5 domande",
  "hero_title": "Qual è la tua<br>impronta sul pianeta?",
  "hero_sub": "Rispondi con onestà. Ad ogni risposta, il globo accanto reagisce in tempo reale al tuo livello di impatto.",
  "progress": "Domanda {n} di {total}",
  "cat_eyebrow": "Categoria {n} · {title}",
  "choose": "Scegli un'opzione",
  "globe_caption": "Il globo riflette, in tempo reale, la pressione del tuo stile di vita sugli ecosistemi",
  "result_eyebrow": "Risultato",
  "score_label": "Punteggio totale",
  "co2_year": "CO₂ all'anno",
  "tabs": [
   "Distribuzione",
   "Globo 3D",
   "Confronto",
   "Raccomandazioni",
   "Tecnologia ed Esportazione"
  ],
  "dist_title": "Distribuzione per categoria",
  "metrics_title": "Metriche di impatto annuale",
  "metric_labels": [
   "CO₂ / anno",
   "Alberi / anno",
   "Ghiaccio sciolto",
   "Acqua consumata",
   "Riscaldamento"
  ],
  "globe_tab_title": "Il pianeta secondo le tue scelte",
  "globe_tab_caption": "Ogni punto pulsante rappresenta una categoria a cui hai risposto: più è intenso, maggiore è la pressione di quell'abitudine.",
  "compare_title": "Come ti confronti",
  "scenarios": [
   "Il tuo profilo",
   "Media globale",
   "Scenario sostenibile",
   "Scenario critico"
  ],
  "co2_unit": "CO₂/anno",
  "co2_axis": "CO₂ (t/anno)",
  "rec_title": "Raccomandazioni personalizzate",
  "tech_title": "Sulla tecnologia di questo progetto",
  "tech_intro": "Questo calcolatore combina un back-end dichiarativo in Python con un livello di visualizzazione WebGL renderizzato su richiesta. L'idea centrale — far reagire una scena 3D a dati in tempo reale mentre l'utente interagisce — è stata ispirata dall'approccio generativo usato in <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, un progetto di visualizzazione di azioni di calcio che ricostruisce le azioni in scene 3D a partire da dati di tracciamento (tracking data).",
  "making_title": "Making-of: due approcci alla visualizzazione generativa",
  "making_intro": "Pur servendo scopi completamente diversi, i due progetti condividono lo stesso problema centrale di ingegneria: <i>come trasformare dati grezzi in una scena viva, senza pre-renderizzare ogni fotogramma?</i> La tabella seguente riassume le scelte tecniche di ciascuno.",
  "th_aspect": "Aspetto",
  "th_this": "Questo progetto (Impronta)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Fonte dei dati",
    "Risposte del questionario, calcolate sul server a ogni interazione",
    "Tracking data posizionali di partite reali (coordinate di giocatori/pallone per fotogramma)"
   ],
   [
    "Motore di rendering",
    "Three.js / WebGL, incorporato tramite componente HTML in Streamlit",
    "Canvas/WebGL personalizzato, con motore proprio di fisica e telecamera"
   ],
   [
    "Cosa reagisce ai dati",
    "Colore del globo, hotspot per categoria, intensità dell'\"indice di pressione\"",
    "Traiettorie dei giocatori, telecamera dinamica, eventi (passaggi, tiri, duelli)"
   ],
   [
    "Interattività",
    "Rotazione manuale del globo, aggiornamento a ogni risposta del quiz",
    "Parametri configurabili tramite URL (JSON codificato), replay delle azioni"
   ],
   [
    "Stack di back-end",
    "Python + Streamlit (rendering dello stato lato server)",
    "Statico / lato client, configurazione incorporata nell'URL stesso"
   ],
   [
    "Obiettivo della scena 3D",
    "Tradurre un punteggio astratto in una metafora visiva immediata",
    "Ricostruire e analizzare eventi sportivi reali con fedeltà tattica"
   ]
  ],
  "lesson": "La lezione principale incorporata qui: piccole scene 3D reattive comunicano gli ordini di grandezza molto più in fretta delle tabelle — il cervello umano legge colore e movimento prima dei numeri.",
  "export_title": "Esporta e condividi",
  "pdf_button": "📥 Scarica il report in PDF",
  "share_text": "Ho scoperto il mio impatto ambientale! Sono {profile} con {score} punti.",
  "retry": "🔄 Ricalcola",
  "methodology_note": "Stima a scopo educativo: il punteggio converte le risposte in fasce e moltiplica per 0,8 t di CO₂ per punto. Non sostituisce un inventario delle emissioni.",
  "questions": [
   {
    "title": "Mobilità",
    "question": "Quanti km percorri al giorno (andata e ritorno)?",
    "options": [
     "Da 0 a 5 km",
     "Da 6 a 15 km",
     "Da 16 a 40 km",
     "Da 41 a 100 km",
     "Da 101 a 200 km",
     "Più di 200 km"
    ]
   },
   {
    "title": "Alimentazione",
    "question": "Quanti pasti a base di carne consumi a settimana?",
    "options": [
     "Nessuno, sono vegetariano/a",
     "Da 1 a 3 pasti",
     "Da 4 a 7 pasti",
     "Da 8 a 14 pasti",
     "Più di 14 pasti"
    ]
   },
   {
    "title": "Consumo di Moda",
    "question": "Quanti capi di abbigliamento nuovi compri al mese?",
    "options": [
     "0 - solo quando serve",
     "Da 1 a 2 capi",
     "Da 3 a 5 capi",
     "Da 6 a 10 capi",
     "Più di 10 capi"
    ]
   },
   {
    "title": "Tecnologia",
    "question": "Ogni quanto compri un nuovo cellulare?",
    "options": [
     "Ogni 5 anni o più",
     "Ogni 3 o 4 anni",
     "Ogni 2 anni",
     "Ogni anno",
     "Meno di 1 anno"
    ]
   },
   {
    "title": "Energia",
    "question": "Qual è il consumo medio di energia elettrica in casa tua?",
    "options": [
     "Fino a 150 kWh/mese",
     "Da 151 a 300 kWh/mese",
     "Da 301 a 500 kWh/mese",
     "Da 501 a 800 kWh/mese",
     "Più di 800 kWh/mese"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Guardiano della Terra",
    "desc": "Il tuo stile di vita è altamente sostenibile. Sei un esempio di rigenerazione!"
   },
   {
    "name": "Consapevole in Crescita",
    "desc": "Sei sulla strada giusta, ma piccoli cambiamenti possono ridurre ancora di più la tua impronta."
   },
   {
    "name": "Impatto Moderato",
    "desc": "Il tuo impatto è percepibile. Valuta di rivedere le tue abitudini di consumo e di trasporto."
   },
   {
    "name": "Allerta Ambientale",
    "desc": "Il tuo stile di vita richiede risorse che il pianeta non riesce a rigenerare in fretta."
   },
   {
    "name": "Crisi Planetaria",
    "desc": "Se tutti vivessero come te, ci vorrebbero diversi pianeti Terra."
   }
  ],
  "recs": {
   "transport": {
    "title": "Valuta il trasporto pubblico",
    "desc": "Usare il trasporto pubblico riduce la tua impronta di carbonio fino al 75% rispetto a guidare da solo."
   },
   "meat": {
    "title": "Riduci il consumo di carne",
    "desc": "Adottare una dieta con meno carne può ridurre la tua impronta di carbonio fino al 50%."
   },
   "fashion": {
    "title": "Acquista i vestiti con più criterio",
    "desc": "Scegliere marchi sostenibili e comprare meno riduce in modo significativo l'impatto tessile."
   },
   "phone": {
    "title": "Prolunga la vita del tuo cellulare",
    "desc": "Tenere il dispositivo più a lungo riduce i rifiuti elettronici e le emissioni di produzione."
   },
   "solar": {
    "title": "Valuta l'energia solare",
    "desc": "I pannelli solari possono ridurre la tua impronta energetica fino all'80%."
   },
   "renewable": {
    "title": "Valuta l'energia rinnovabile",
    "desc": "Attivare un'offerta di energia rinnovabile con il tuo fornitore è spesso un'opzione accessibile."
   },
   "great": {
    "title": "Complimenti!",
    "desc": "Segui già le migliori pratiche. Continua così."
   }
  },
  "globe_hud": "Indice di Pressione",
  "globe_legend": "trascina per ruotare · scroll per zoomare",
  "globe_intensity": "Intensità",
  "pdf": {
   "file": "report_impatto_ambientale.pdf",
   "title": "Report di Impatto Ambientale",
   "profile": "Il Tuo Profilo",
   "metrics": "Metriche di Impatto Annuale",
   "co2": "CO2 / anno: {v} tonnellate",
   "trees": "Alberi / anno: {v}",
   "ice": "Ghiaccio sciolto: {v} m2",
   "water": "Acqua consumata: {v} litri",
   "warming": "Riscaldamento: +{v} °C",
   "dist": "Distribuzione per Categoria",
   "points": "{cat}: {n} punti",
   "recs": "Raccomandazioni Personalizzate"
  }
 },
 "fr": {
  "page_title": "Empreinte — Calculateur d'impact environnemental",
  "lang_label": "Langue",
  "eyebrow": "Calculateur d'impact · 5 questions",
  "hero_title": "Quelle est votre<br>empreinte sur la planète ?",
  "hero_sub": "Répondez en toute honnêteté. À chaque réponse, le globe à côté réagit en temps réel à votre niveau d'impact.",
  "progress": "Question {n} sur {total}",
  "cat_eyebrow": "Catégorie {n} · {title}",
  "choose": "Choisissez une option",
  "globe_caption": "Le globe reflète, en temps réel, la pression de votre mode de vie sur les écosystèmes",
  "result_eyebrow": "Résultat",
  "score_label": "Score total",
  "co2_year": "CO₂ par an",
  "tabs": [
   "Répartition",
   "Globe 3D",
   "Comparaison",
   "Recommandations",
   "Technologie & Export"
  ],
  "dist_title": "Répartition par catégorie",
  "metrics_title": "Indicateurs d'impact annuel",
  "metric_labels": [
   "CO₂ / an",
   "Arbres / an",
   "Glace fondue",
   "Eau consommée",
   "Réchauffement"
  ],
  "globe_tab_title": "La planète selon vos choix",
  "globe_tab_caption": "Chaque point pulsant représente une catégorie renseignée — plus il est intense, plus la pression de cette habitude est forte.",
  "compare_title": "Comment vous vous situez",
  "scenarios": [
   "Votre profil",
   "Moyenne mondiale",
   "Scénario durable",
   "Scénario critique"
  ],
  "co2_unit": "CO₂/an",
  "co2_axis": "CO₂ (t/an)",
  "rec_title": "Recommandations personnalisées",
  "tech_title": "À propos de la technologie de ce projet",
  "tech_intro": "Ce calculateur associe un back-end déclaratif en Python à une couche de visualisation WebGL rendue à la demande. L'idée centrale — faire réagir une scène 3D à des données en temps réel selon l'interaction de l'utilisateur — s'inspire de l'approche générative utilisée sur <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, un projet de visualisation d'actions de football qui reconstitue les phases de jeu en scène 3D à partir de données de suivi (tracking data).",
  "making_title": "Making-of : deux approches de la visualisation générative",
  "making_intro": "Bien qu'ils servent des objectifs complètement différents, les deux projets partagent le même problème d'ingénierie central : <i>comment transformer des données brutes en une scène vivante, sans pré-calculer chaque image ?</i> Le tableau ci-dessous résume les choix techniques de chacun.",
  "th_aspect": "Aspect",
  "th_this": "Ce projet (Empreinte)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Source de données",
    "Réponses au questionnaire, calculées côté serveur à chaque interaction",
    "Tracking data positionnel de vrais matchs (coordonnées des joueurs/du ballon par image)"
   ],
   [
    "Moteur de rendu",
    "Three.js / WebGL, intégré via un composant HTML dans Streamlit",
    "Canvas/WebGL sur mesure, moteur de physique et de caméra maison"
   ],
   [
    "Ce qui réagit aux données",
    "Couleur du globe, points chauds par catégorie, intensité de l'« indice de pression »",
    "Trajectoires des joueurs, caméra dynamique, événements (passes, tirs, duels)"
   ],
   [
    "Interactivité",
    "Rotation manuelle du globe, mise à jour à chaque réponse du quiz",
    "Paramètres configurables via l'URL (JSON encodé), replay des actions"
   ],
   [
    "Stack back-end",
    "Python + Streamlit (rendu côté serveur de l'état)",
    "Statique / côté client, configuration intégrée à l'URL elle-même"
   ],
   [
    "Objectif de la scène 3D",
    "Traduire un score abstrait en métaphore visuelle immédiate",
    "Reconstituer et analyser de vrais événements sportifs avec une fidélité tactique"
   ]
  ],
  "lesson": "La principale leçon à retenir : de petites scènes 3D réactives communiquent les ordres de grandeur bien plus vite que des tableaux — le cerveau humain lit la couleur et le mouvement avant de lire les chiffres.",
  "export_title": "Exporter & partager",
  "pdf_button": "📥 Télécharger le rapport en PDF",
  "share_text": "J'ai découvert mon impact environnemental ! Je suis {profile} avec {score} points.",
  "retry": "🔄 Refaire le calcul",
  "methodology_note": "Estimation pédagogique : le score convertit les réponses en tranches et multiplie par 0,8 t de CO₂ par point. Ne remplace pas un bilan d'émissions.",
  "questions": [
   {
    "title": "Mobilité",
    "question": "Combien de km parcourez-vous par jour (aller-retour) ?",
    "options": [
     "0 à 5 km",
     "6 à 15 km",
     "16 à 40 km",
     "41 à 100 km",
     "101 à 200 km",
     "Plus de 200 km"
    ]
   },
   {
    "title": "Alimentation",
    "question": "Combien de repas avec de la viande faites-vous par semaine ?",
    "options": [
     "Aucun, je suis végétarien(ne)",
     "1 à 3 repas",
     "4 à 7 repas",
     "8 à 14 repas",
     "Plus de 14 repas"
    ]
   },
   {
    "title": "Consommation de mode",
    "question": "Combien de vêtements neufs achetez-vous par mois ?",
    "options": [
     "0 - seulement si nécessaire",
     "1 à 2 pièces",
     "3 à 5 pièces",
     "6 à 10 pièces",
     "Plus de 10 pièces"
    ]
   },
   {
    "title": "Technologie",
    "question": "À quelle fréquence achetez-vous un nouveau téléphone portable ?",
    "options": [
     "Tous les 5 ans ou plus",
     "Tous les 3 à 4 ans",
     "Tous les 2 ans",
     "Chaque année",
     "Moins d'un an"
    ]
   },
   {
    "title": "Énergie",
    "question": "Quelle est la consommation moyenne d'électricité de votre logement ?",
    "options": [
     "Jusqu'à 150 kWh/mois",
     "151 à 300 kWh/mois",
     "301 à 500 kWh/mois",
     "501 à 800 kWh/mois",
     "Plus de 800 kWh/mois"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Gardien de la Terre",
    "desc": "Votre mode de vie est très durable. Vous êtes un exemple de régénération !"
   },
   {
    "name": "Conscient en Évolution",
    "desc": "Vous êtes sur la bonne voie, mais de petits changements peuvent réduire encore votre empreinte."
   },
   {
    "name": "Impact Modéré",
    "desc": "Votre impact est perceptible. Pensez à revoir vos habitudes de consommation et de transport."
   },
   {
    "name": "Alerte Environnementale",
    "desc": "Votre mode de vie exige des ressources que la planète ne peut pas reconstituer rapidement."
   },
   {
    "name": "Crise Planétaire",
    "desc": "Si tout le monde vivait comme vous, il nous faudrait plusieurs planètes Terre."
   }
  ],
  "recs": {
   "transport": {
    "title": "Pensez aux transports en commun",
    "desc": "Utiliser les transports en commun réduit votre empreinte carbone jusqu'à 75 % par rapport à la conduite en solo."
   },
   "meat": {
    "title": "Réduisez votre consommation de viande",
    "desc": "Adopter une alimentation avec moins de viande peut réduire votre empreinte carbone jusqu'à 50 %."
   },
   "fashion": {
    "title": "Achetez vos vêtements avec plus de discernement",
    "desc": "Choisir des marques durables et acheter moins réduit nettement l'impact textile."
   },
   "phone": {
    "title": "Prolongez la vie de votre téléphone",
    "desc": "Garder l'appareil plus longtemps réduit les déchets électroniques et les émissions de fabrication."
   },
   "solar": {
    "title": "Pensez à l'énergie solaire",
    "desc": "Les panneaux solaires peuvent réduire votre empreinte énergétique jusqu'à 80 %."
   },
   "renewable": {
    "title": "Étudiez l'énergie renouvelable",
    "desc": "Souscrire une offre d'énergie renouvelable auprès de votre fournisseur est souvent une option accessible."
   },
   "great": {
    "title": "Félicitations !",
    "desc": "Vous suivez déjà les meilleures pratiques. Continuez ainsi."
   }
  },
  "globe_hud": "Indice de Pression",
  "globe_legend": "faites glisser pour tourner · molette pour zoomer",
  "globe_intensity": "Intensité",
  "pdf": {
   "file": "rapport_impact_environnemental.pdf",
   "title": "Rapport d'Impact Environnemental",
   "profile": "Votre Profil",
   "metrics": "Indicateurs d'Impact Annuel",
   "co2": "CO2 / an : {v} tonnes",
   "trees": "Arbres / an : {v}",
   "ice": "Glace fondue : {v} m2",
   "water": "Eau consommée : {v} litres",
   "warming": "Réchauffement : +{v} °C",
   "dist": "Répartition par Catégorie",
   "points": "{cat} : {n} points",
   "recs": "Recommandations Personnalisées"
  }
 },
 "de": {
  "page_title": "Fußabdruck — Rechner für die Umweltbilanz",
  "lang_label": "Sprache",
  "eyebrow": "Impact-Rechner · 5 Fragen",
  "hero_title": "Wie groß ist dein<br>Fußabdruck auf dem Planeten?",
  "hero_sub": "Antworte ehrlich. Mit jeder Antwort reagiert der Globus nebenan in Echtzeit auf dein Belastungsniveau.",
  "progress": "Frage {n} von {total}",
  "cat_eyebrow": "Kategorie {n} · {title}",
  "choose": "Wähle eine Option",
  "globe_caption": "Der Globus zeigt in Echtzeit, wie stark dein Lebensstil die Ökosysteme belastet",
  "result_eyebrow": "Ergebnis",
  "score_label": "Gesamtpunktzahl",
  "co2_year": "CO₂ pro Jahr",
  "tabs": [
   "Verteilung",
   "3D-Globus",
   "Vergleich",
   "Empfehlungen",
   "Technik & Export"
  ],
  "dist_title": "Verteilung nach Kategorie",
  "metrics_title": "Jährliche Umweltkennzahlen",
  "metric_labels": [
   "CO₂ / Jahr",
   "Bäume / Jahr",
   "Geschmolzenes Eis",
   "Wasserverbrauch",
   "Erwärmung"
  ],
  "globe_tab_title": "Der Planet nach deinen Entscheidungen",
  "globe_tab_caption": "Jeder pulsierende Punkt steht für eine beantwortete Kategorie — je intensiver, desto größer die Belastung durch diese Gewohnheit.",
  "compare_title": "So schneidest du im Vergleich ab",
  "scenarios": [
   "Dein Profil",
   "Globaler Durchschnitt",
   "Nachhaltiges Szenario",
   "Kritisches Szenario"
  ],
  "co2_unit": "CO₂/Jahr",
  "co2_axis": "CO₂ (t/Jahr)",
  "rec_title": "Persönliche Empfehlungen",
  "tech_title": "Zur Technik hinter diesem Projekt",
  "tech_intro": "Dieser Rechner kombiniert ein deklaratives Python-Backend mit einer bei Bedarf gerenderten WebGL-Visualisierungsschicht. Die zentrale Idee — eine 3D-Szene in Echtzeit auf Daten reagieren zu lassen, während der Nutzer interagiert — wurde vom generativen Ansatz von <b style='color:#8fd8ff;'>wc26.bogachev.fr</b> inspiriert, einem Projekt zur Visualisierung von Fußballaktionen, das Spielzüge anhand von Tracking-Daten (tracking data) als 3D-Szene rekonstruiert.",
  "making_title": "Making-of: zwei Ansätze generativer Visualisierung",
  "making_intro": "Obwohl sie völlig unterschiedlichen Zwecken dienen, teilen beide Projekte dasselbe zentrale Engineering-Problem: <i>Wie verwandelt man Rohdaten in eine lebendige Szene, ohne jedes Bild vorab zu rendern?</i> Die folgende Tabelle fasst die technischen Entscheidungen beider Projekte zusammen.",
  "th_aspect": "Aspekt",
  "th_this": "Dieses Projekt (Fußabdruck)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Datenquelle",
    "Antworten des Fragebogens, bei jeder Interaktion auf dem Server berechnet",
    "Positionelle Tracking-Daten echter Spiele (Spieler-/Ballkoordinaten pro Frame)"
   ],
   [
    "Rendering-Engine",
    "Three.js / WebGL, per HTML-Komponente in Streamlit eingebettet",
    "Eigener Canvas/WebGL-Code, eigene Physik- und Kamera-Engine"
   ],
   [
    "Was auf die Daten reagiert",
    "Farbe des Globus, Hotspots je Kategorie, Intensität des „Belastungsindex“",
    "Spielerbahnen, dynamische Kamera, Ereignisse (Pässe, Schüsse, Zweikämpfe)"
   ],
   [
    "Interaktivität",
    "Manuelles Drehen des Globus, Aktualisierung bei jeder Quiz-Antwort",
    "Per URL konfigurierbare Parameter (kodiertes JSON), Wiederholung von Spielzügen"
   ],
   [
    "Back-end-Stack",
    "Python + Streamlit (serverseitiges Rendering des Zustands)",
    "Statisch / clientseitig, Konfiguration in der URL selbst eingebettet"
   ],
   [
    "Ziel der 3D-Szene",
    "Eine abstrakte Punktzahl in eine unmittelbare visuelle Metapher übersetzen",
    "Echte Sportereignisse mit taktischer Genauigkeit rekonstruieren und analysieren"
   ]
  ],
  "lesson": "Die wichtigste Lehre daraus: Kleine reaktive 3D-Szenen vermitteln Größenordnungen viel schneller als Tabellen — das menschliche Gehirn liest Farbe und Bewegung, bevor es Zahlen liest.",
  "export_title": "Exportieren & teilen",
  "pdf_button": "📥 Bericht als PDF herunterladen",
  "share_text": "Ich habe meine Umweltbilanz herausgefunden! Ich bin {profile} mit {score} Punkten.",
  "retry": "🔄 Neu berechnen",
  "methodology_note": "Schätzung zu Bildungszwecken: Die Punktzahl wandelt Antworten in Stufen um und multipliziert mit 0,8 t CO₂ pro Punkt. Sie ersetzt keine Emissionsbilanz.",
  "questions": [
   {
    "title": "Mobilität",
    "question": "Wie viele km legst du pro Tag zurück (Hin- und Rückweg)?",
    "options": [
     "0 bis 5 km",
     "6 bis 15 km",
     "16 bis 40 km",
     "41 bis 100 km",
     "101 bis 200 km",
     "Mehr als 200 km"
    ]
   },
   {
    "title": "Ernährung",
    "question": "Wie viele Mahlzeiten mit Fleisch isst du pro Woche?",
    "options": [
     "Keine, ich bin Vegetarier(in)",
     "1 bis 3 Mahlzeiten",
     "4 bis 7 Mahlzeiten",
     "8 bis 14 Mahlzeiten",
     "Mehr als 14 Mahlzeiten"
    ]
   },
   {
    "title": "Modekonsum",
    "question": "Wie viele neue Kleidungsstücke kaufst du pro Monat?",
    "options": [
     "0 - nur wenn nötig",
     "1 bis 2 Teile",
     "3 bis 5 Teile",
     "6 bis 10 Teile",
     "Mehr als 10 Teile"
    ]
   },
   {
    "title": "Technik",
    "question": "Wie oft kaufst du ein neues Handy?",
    "options": [
     "Alle 5 Jahre oder seltener",
     "Alle 3 bis 4 Jahre",
     "Alle 2 Jahre",
     "Jedes Jahr",
     "Öfter als einmal im Jahr"
    ]
   },
   {
    "title": "Energie",
    "question": "Wie hoch ist der durchschnittliche Stromverbrauch in deinem Haushalt?",
    "options": [
     "Bis zu 150 kWh/Monat",
     "151 bis 300 kWh/Monat",
     "301 bis 500 kWh/Monat",
     "501 bis 800 kWh/Monat",
     "Mehr als 800 kWh/Monat"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Hüter der Erde",
    "desc": "Dein Lebensstil ist äußerst nachhaltig. Du bist ein Vorbild für Regeneration!"
   },
   {
    "name": "Bewusst auf dem Weg",
    "desc": "Du bist auf dem richtigen Weg, aber kleine Veränderungen können deinen Fußabdruck noch weiter verringern."
   },
   {
    "name": "Mäßige Belastung",
    "desc": "Deine Belastung ist spürbar. Überdenke deine Konsum- und Mobilitätsgewohnheiten."
   },
   {
    "name": "Umweltalarm",
    "desc": "Dein Lebensstandard verbraucht Ressourcen, die der Planet nicht schnell genug ersetzen kann."
   },
   {
    "name": "Planetare Krise",
    "desc": "Wenn alle so lebten wie du, bräuchten wir mehrere Planeten Erde."
   }
  ],
  "recs": {
   "transport": {
    "title": "Nutze öffentliche Verkehrsmittel",
    "desc": "Öffentliche Verkehrsmittel senken deinen CO₂-Fußabdruck um bis zu 75 % im Vergleich zum Alleinfahren im Auto."
   },
   "meat": {
    "title": "Reduziere deinen Fleischkonsum",
    "desc": "Eine Ernährung mit weniger Fleisch kann deinen CO₂-Fußabdruck um bis zu 50 % senken."
   },
   "fashion": {
    "title": "Kaufe Kleidung bewusster",
    "desc": "Nachhaltige Marken zu wählen und weniger zu kaufen verringert die Textilbelastung erheblich."
   },
   "phone": {
    "title": "Verlängere die Lebensdauer deines Handys",
    "desc": "Ein Gerät länger zu nutzen verringert Elektroschrott und Emissionen aus der Herstellung."
   },
   "solar": {
    "title": "Erwäge Solarenergie",
    "desc": "Solarmodule können deinen Energie-Fußabdruck um bis zu 80 % senken."
   },
   "renewable": {
    "title": "Prüfe erneuerbare Energie",
    "desc": "Ökostrom von deinem Versorger zu beziehen ist oft eine erschwingliche Option."
   },
   "great": {
    "title": "Glückwunsch!",
    "desc": "Du befolgst bereits die besten Praktiken. Weiter so."
   }
  },
  "globe_hud": "Belastungsindex",
  "globe_legend": "ziehen zum Drehen · Scrollen zum Zoomen",
  "globe_intensity": "Intensität",
  "pdf": {
   "file": "umweltbilanz_bericht.pdf",
   "title": "Bericht zur Umweltbilanz",
   "profile": "Dein Profil",
   "metrics": "Jährliche Umweltkennzahlen",
   "co2": "CO2 / Jahr: {v} Tonnen",
   "trees": "Bäume / Jahr: {v}",
   "ice": "Geschmolzenes Eis: {v} m2",
   "water": "Wasserverbrauch: {v} Liter",
   "warming": "Erwärmung: +{v} °C",
   "dist": "Verteilung nach Kategorie",
   "points": "{cat}: {n} Punkte",
   "recs": "Persönliche Empfehlungen"
  }
 },
 "zh": {
  "page_title": "足迹 — 环境影响计算器",
  "lang_label": "语言",
  "eyebrow": "影响计算器 · 5个问题",
  "hero_title": "你在地球上<br>留下了怎样的足迹?",
  "hero_sub": "请如实回答。每回答一题,旁边的地球都会实时反映你的影响程度。",
  "progress": "第 {n} 题,共 {total} 题",
  "cat_eyebrow": "类别 {n} · {title}",
  "choose": "请选择一项",
  "globe_caption": "地球实时反映你的生活方式对生态系统施加的压力",
  "result_eyebrow": "结果",
  "score_label": "总分",
  "co2_year": "每年 CO₂",
  "tabs": [
   "分布",
   "3D 地球",
   "对比",
   "建议",
   "技术与导出"
  ],
  "dist_title": "各类别分布",
  "metrics_title": "年度影响指标",
  "metric_labels": [
   "CO₂ / 年",
   "树木 / 年",
   "融化的冰",
   "耗水量",
   "升温"
  ],
  "globe_tab_title": "你的选择所塑造的地球",
  "globe_tab_caption": "每个闪动的点代表一个已回答的类别——越强烈,表示该习惯带来的压力越大。",
  "compare_title": "你与他人相比如何",
  "scenarios": [
   "你的画像",
   "全球平均",
   "可持续情景",
   "危机情景"
  ],
  "co2_unit": "CO₂/年",
  "co2_axis": "CO₂(吨/年)",
  "rec_title": "个性化建议",
  "tech_title": "关于本项目的技术",
  "tech_intro": "本计算器将基于 Python 的声明式后端与按需渲染的 WebGL 可视化层相结合。其核心理念——让 3D 场景随用户交互实时响应数据——灵感来自 <b style='color:#8fd8ff;'>wc26.bogachev.fr</b> 所采用的生成式方法。那是一个足球战术可视化项目,根据追踪数据(tracking data)在 3D 场景中还原比赛片段。",
  "making_title": "幕后制作:两种生成式可视化方法",
  "making_intro": "虽然两个项目的用途截然不同,但它们面临同一个核心工程问题:<i>如何在不预先渲染每一帧的情况下,把原始数据变成一个鲜活的场景?</i> 下表概述了双方各自的技术选择。",
  "th_aspect": "方面",
  "th_this": "本项目(足迹)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "数据来源",
    "问卷答案,每次交互时在服务器端计算",
    "真实比赛的位置追踪数据(每帧的球员/足球坐标)"
   ],
   [
    "渲染引擎",
    "Three.js / WebGL,通过 HTML 组件嵌入 Streamlit",
    "自定义 Canvas/WebGL,自研物理与相机引擎"
   ],
   [
    "随数据变化的内容",
    "地球颜色、各类别热点、“压力指数”的强度",
    "球员轨迹、动态相机、事件(传球、射门、对抗)"
   ],
   [
    "交互性",
    "手动旋转地球,每回答一题即更新",
    "可通过 URL(编码的 JSON)配置参数,支持回放片段"
   ],
   [
    "后端技术栈",
    "Python + Streamlit(状态的服务器端渲染)",
    "静态 / 客户端,配置直接嵌入 URL 本身"
   ],
   [
    "3D 场景的目标",
    "将抽象分数转化为直观的视觉隐喻",
    "以战术层面的真实度还原并分析真实体育赛事"
   ]
  ],
  "lesson": "这里体现的主要经验:小巧而会响应的 3D 场景比表格更快传达数量级——人脑先读到颜色和动态,然后才读到数字。",
  "export_title": "导出与分享",
  "pdf_button": "📥 下载 PDF 报告",
  "share_text": "我发现了自己的环境影响!我是{profile},得分 {score} 分。",
  "retry": "🔄 重新计算",
  "methodology_note": "教育性估算:得分将答案换算为区间,并按每分 0.8 吨 CO₂ 计算。不能替代温室气体排放清单。",
  "questions": [
   {
    "title": "出行",
    "question": "你每天出行多少公里(往返)?",
    "options": [
     "0 至 5 km",
     "6 至 15 km",
     "16 至 40 km",
     "41 至 100 km",
     "101 至 200 km",
     "超过 200 km"
    ]
   },
   {
    "title": "饮食",
    "question": "你每周吃多少顿含肉的餐?",
    "options": [
     "没有,我是素食者",
     "1 至 3 顿",
     "4 至 7 顿",
     "8 至 14 顿",
     "超过 14 顿"
    ]
   },
   {
    "title": "时尚消费",
    "question": "你每月购买多少件新衣服?",
    "options": [
     "0 件——仅在必要时购买",
     "1 至 2 件",
     "3 至 5 件",
     "6 至 10 件",
     "超过 10 件"
    ]
   },
   {
    "title": "科技",
    "question": "你多久换一次新手机?",
    "options": [
     "每 5 年或更久",
     "每 3 至 4 年",
     "每 2 年",
     "每年",
     "不到 1 年"
    ]
   },
   {
    "title": "能源",
    "question": "你家的平均用电量是多少?",
    "options": [
     "最高 150 kWh/月",
     "151 至 300 kWh/月",
     "301 至 500 kWh/月",
     "501 至 800 kWh/月",
     "超过 800 kWh/月"
    ]
   }
  ],
  "profiles": [
   {
    "name": "地球守护者",
    "desc": "你的生活方式高度可持续。你是再生的榜样!"
   },
   {
    "name": "觉醒进行时",
    "desc": "你走在正确的道路上,但一些小改变还能进一步减少你的足迹。"
   },
   {
    "name": "中等影响",
    "desc": "你的影响已经可见。请考虑审视自己的消费和出行习惯。"
   },
   {
    "name": "环境警报",
    "desc": "你的生活方式所需的资源,地球无法迅速补充。"
   },
   {
    "name": "地球危机",
    "desc": "如果所有人都像你这样生活,我们将需要好几个地球。"
   }
  ],
  "recs": {
   "transport": {
    "title": "考虑公共交通",
    "desc": "与独自驾车相比,乘坐公共交通最多可将你的碳足迹减少 75%。"
   },
   "meat": {
    "title": "减少肉类消费",
    "desc": "采用少肉饮食最多可将你的碳足迹减少 50%。"
   },
   "fashion": {
    "title": "更理性地购买衣物",
    "desc": "选择可持续品牌并减少购买,可显著降低纺织品带来的影响。"
   },
   "phone": {
    "title": "延长手机的使用寿命",
    "desc": "更长时间使用设备,可减少电子垃圾和制造过程中的排放。"
   },
   "solar": {
    "title": "考虑太阳能",
    "desc": "太阳能电池板最多可将你的能源足迹减少 80%。"
   },
   "renewable": {
    "title": "评估可再生能源",
    "desc": "向电力公司订购可再生能源通常是一个经济实惠的选择。"
   },
   "great": {
    "title": "恭喜!",
    "desc": "你已经遵循了最佳实践。请继续保持。"
   }
  },
  "globe_hud": "压力指数",
  "globe_legend": "拖动旋转 · 滚轮缩放",
  "globe_intensity": "强度",
  "pdf": {
   "file": "relatorio_impacto_ambiental.pdf",
   "title": "环境影响报告",
   "profile": "你的画像",
   "metrics": "年度影响指标",
   "co2": "CO2 / 年:{v} 吨",
   "trees": "树木 / 年:{v}",
   "ice": "融化的冰:{v} m2",
   "water": "耗水量:{v} 升",
   "warming": "升温:+{v} °C",
   "dist": "各类别分布",
   "points": "{cat}:{n} 分",
   "recs": "个性化建议"
  }
 },
 "ar": {
  "page_title": "البصمة — حاسبة الأثر البيئي",
  "lang_label": "اللغة",
  "eyebrow": "حاسبة الأثر · 5 أسئلة",
  "hero_title": "ما هي بصمتك<br>على الكوكب؟",
  "hero_sub": "أجب بصدق. مع كل إجابة، يتفاعل الكوكب بجانبك في الوقت الفعلي مع مستوى أثرك.",
  "progress": "السؤال {n} من {total}",
  "cat_eyebrow": "الفئة {n} · {title}",
  "choose": "اختر خيارًا",
  "globe_caption": "يعكس الكوكب، في الوقت الفعلي، الضغط الذي يمارسه أسلوب حياتك على النظم البيئية",
  "result_eyebrow": "النتيجة",
  "score_label": "مجموع النقاط",
  "co2_year": "CO₂ سنويًا",
  "tabs": [
   "التوزيع",
   "الكرة الأرضية ثلاثية الأبعاد",
   "المقارنة",
   "التوصيات",
   "التقنية والتصدير"
  ],
  "dist_title": "التوزيع حسب الفئة",
  "metrics_title": "مؤشرات الأثر السنوي",
  "metric_labels": [
   "CO₂ / سنة",
   "أشجار / سنة",
   "الجليد الذائب",
   "المياه المستهلكة",
   "الاحترار"
  ],
  "globe_tab_title": "الكوكب كما تشكّله اختياراتك",
  "globe_tab_caption": "كل نقطة نابضة تمثل فئة تمت الإجابة عنها — وكلما زادت شدتها، زاد الضغط الناتج عن تلك العادة.",
  "compare_title": "كيف تقارن بغيرك",
  "scenarios": [
   "ملفك الشخصي",
   "المتوسط العالمي",
   "السيناريو المستدام",
   "السيناريو الحرج"
  ],
  "co2_unit": "CO₂/سنة",
  "co2_axis": "CO₂ (طن/سنة)",
  "rec_title": "توصيات مخصصة",
  "tech_title": "عن تقنية هذا المشروع",
  "tech_intro": "تجمع هذه الحاسبة بين واجهة خلفية تصريحية بلغة Python وطبقة عرض WebGL تُرسَم عند الطلب. الفكرة المحورية — جعل مشهد ثلاثي الأبعاد يتفاعل مع البيانات في الوقت الفعلي بحسب تفاعل المستخدم — استُلهمت من النهج التوليدي المستخدم في <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>، وهو مشروع لتصور حركات كرة القدم يعيد بناء اللقطات في مشهد ثلاثي الأبعاد انطلاقًا من بيانات التتبع (tracking data).",
  "making_title": "كواليس العمل: نهجان في التصور التوليدي",
  "making_intro": "رغم أن المشروعين يخدمان غرضين مختلفين تمامًا، فإنهما يتشاركان المشكلة الهندسية الجوهرية نفسها: <i>كيف نحوّل البيانات الخام إلى مشهد حي دون إعداد كل إطار مسبقًا؟</i> يلخص الجدول أدناه الخيارات التقنية لكل منهما.",
  "th_aspect": "الجانب",
  "th_this": "هذا المشروع (البصمة)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "مصدر البيانات",
    "إجابات الاستبيان، تُحسب على الخادم عند كل تفاعل",
    "بيانات تتبع المواضع لمباريات حقيقية (إحداثيات اللاعبين/الكرة في كل إطار)"
   ],
   [
    "محرك العرض",
    "Three.js / WebGL، مضمَّن عبر مكوّن HTML في Streamlit",
    "Canvas/WebGL مخصص، مع محرك فيزياء وكاميرا خاص"
   ],
   [
    "ما يتفاعل مع البيانات",
    "لون الكرة الأرضية، ونقاط التركز لكل فئة، وشدة «مؤشر الضغط»",
    "مسارات اللاعبين، والكاميرا الديناميكية، والأحداث (تمريرات، تسديدات، التحامات)"
   ],
   [
    "التفاعلية",
    "تدوير الكرة الأرضية يدويًا، والتحديث مع كل إجابة في الاختبار",
    "معاملات قابلة للضبط عبر URL (JSON مشفّر)، وإعادة عرض اللقطات"
   ],
   [
    "بنية الواجهة الخلفية",
    "Python + Streamlit (عرض الحالة على جانب الخادم)",
    "ثابت / على جانب العميل، والإعدادات مضمَّنة في الـ URL نفسه"
   ],
   [
    "هدف المشهد ثلاثي الأبعاد",
    "تحويل نتيجة مجردة إلى استعارة بصرية فورية",
    "إعادة بناء الأحداث الرياضية الحقيقية وتحليلها بدقة تكتيكية"
   ]
  ],
  "lesson": "الدرس الرئيسي المتضمَّن هنا: المشاهد ثلاثية الأبعاد الصغيرة المتفاعلة تنقل أوامر المقادير أسرع بكثير من الجداول — فالدماغ البشري يقرأ اللون والحركة قبل أن يقرأ الأرقام.",
  "export_title": "التصدير والمشاركة",
  "pdf_button": "📥 تنزيل التقرير بصيغة PDF",
  "share_text": "اكتشفت أثري البيئي! أنا {profile} بـ {score} نقطة.",
  "retry": "🔄 إعادة الحساب",
  "methodology_note": "تقدير تعليمي: تحوّل النتيجة الإجابات إلى شرائح وتضربها في 0.8 طن من CO₂ لكل نقطة. ولا يغني عن جرد الانبعاثات.",
  "questions": [
   {
    "title": "التنقل",
    "question": "كم كيلومترًا تقطعها يوميًا (ذهابًا وإيابًا)؟",
    "options": [
     "من 0 إلى 5 km",
     "من 6 إلى 15 km",
     "من 16 إلى 40 km",
     "من 41 إلى 100 km",
     "من 101 إلى 200 km",
     "أكثر من 200 km"
    ]
   },
   {
    "title": "الغذاء",
    "question": "كم وجبة تحتوي على اللحم تتناولها في الأسبوع؟",
    "options": [
     "لا شيء، أنا نباتي/نباتية",
     "من 1 إلى 3 وجبات",
     "من 4 إلى 7 وجبات",
     "من 8 إلى 14 وجبة",
     "أكثر من 14 وجبة"
    ]
   },
   {
    "title": "استهلاك الأزياء",
    "question": "كم قطعة ملابس جديدة تشتري في الشهر؟",
    "options": [
     "0 - فقط عند الضرورة",
     "من 1 إلى 2 قطعة",
     "من 3 إلى 5 قطع",
     "من 6 إلى 10 قطع",
     "أكثر من 10 قطع"
    ]
   },
   {
    "title": "التكنولوجيا",
    "question": "كم مرة تشتري هاتفًا جديدًا؟",
    "options": [
     "كل 5 سنوات أو أكثر",
     "كل 3 إلى 4 سنوات",
     "كل سنتين",
     "كل سنة",
     "أقل من سنة"
    ]
   },
   {
    "title": "الطاقة",
    "question": "ما متوسط استهلاك الكهرباء في منزلك؟",
    "options": [
     "حتى 150 kWh/شهر",
     "من 151 إلى 300 kWh/شهر",
     "من 301 إلى 500 kWh/شهر",
     "من 501 إلى 800 kWh/شهر",
     "أكثر من 800 kWh/شهر"
    ]
   }
  ],
  "profiles": [
   {
    "name": "حارس الأرض",
    "desc": "أسلوب حياتك مستدام للغاية. أنت مثال على التجدد!"
   },
   {
    "name": "وعي في تطور",
    "desc": "أنت على الطريق الصحيح، لكن تغييرات صغيرة قد تقلل بصمتك أكثر."
   },
   {
    "name": "أثر متوسط",
    "desc": "أثرك ملحوظ. فكّر في مراجعة عاداتك في الاستهلاك والنقل."
   },
   {
    "name": "إنذار بيئي",
    "desc": "نمط حياتك يتطلب موارد لا يستطيع الكوكب تعويضها بسرعة."
   },
   {
    "name": "أزمة كوكبية",
    "desc": "لو عاش الجميع مثلك، لاحتجنا إلى عدة كواكب أرضية."
   }
  ],
  "recs": {
   "transport": {
    "title": "فكّر في استخدام النقل العام",
    "desc": "يقلل استخدام النقل العام بصمتك الكربونية بما يصل إلى 75% مقارنةً بالقيادة بمفردك."
   },
   "meat": {
    "title": "قلّل استهلاك اللحوم",
    "desc": "يمكن لاتباع نظام غذائي أقل لحمًا أن يقلل بصمتك الكربونية بما يصل إلى 50%."
   },
   "fashion": {
    "title": "اشترِ الملابس بمزيد من التمحيص",
    "desc": "اختيار علامات مستدامة وشراء كميات أقل يقلل أثر النسيج بدرجة كبيرة."
   },
   "phone": {
    "title": "أطِل عمر هاتفك",
    "desc": "الاحتفاظ بالجهاز لفترة أطول يقلل النفايات الإلكترونية وانبعاثات التصنيع."
   },
   "solar": {
    "title": "فكّر في الطاقة الشمسية",
    "desc": "يمكن للألواح الشمسية أن تقلل بصمتك من الطاقة بما يصل إلى 80%."
   },
   "renewable": {
    "title": "قيّم الطاقة المتجددة",
    "desc": "التعاقد على طاقة متجددة من شركة الكهرباء التي تخدمك غالبًا خيار متاح."
   },
   "great": {
    "title": "تهانينا!",
    "desc": "أنت تتبع بالفعل أفضل الممارسات. واصل هكذا."
   }
  },
  "globe_hud": "مؤشر الضغط",
  "globe_legend": "اسحب للتدوير · مرّر للتكبير",
  "globe_intensity": "الشدة",
  "pdf": {
   "file": "relatorio_impacto_ambiental.pdf",
   "title": "تقرير الأثر البيئي",
   "profile": "ملفك الشخصي",
   "metrics": "مؤشرات الأثر السنوي",
   "co2": "CO2 / سنة: {v} طن",
   "trees": "أشجار / سنة: {v}",
   "ice": "الجليد الذائب: {v} m2",
   "water": "المياه المستهلكة: {v} لتر",
   "warming": "الاحترار: +{v} °C",
   "dist": "التوزيع حسب الفئة",
   "points": "{cat}: {n} نقطة",
   "recs": "توصيات مخصصة"
  }
 },
 "el": {
  "page_title": "Αποτύπωμα — Υπολογιστής Περιβαλλοντικού Αντίκτυπου",
  "lang_label": "Γλώσσα",
  "eyebrow": "Υπολογιστής αντίκτυπου · 5 ερωτήσεις",
  "hero_title": "Ποιο είναι το αποτύπωμά σου<br>στον πλανήτη;",
  "hero_sub": "Απάντησε με ειλικρίνεια. Με κάθε απάντηση, η υδρόγειος δίπλα αντιδρά σε πραγματικό χρόνο στο επίπεδο του αντίκτυπού σου.",
  "progress": "Ερώτηση {n} από {total}",
  "cat_eyebrow": "Κατηγορία {n} · {title}",
  "choose": "Διάλεξε μια επιλογή",
  "globe_caption": "Η υδρόγειος αντικατοπτρίζει, σε πραγματικό χρόνο, την πίεση που ασκεί ο τρόπος ζωής σου στα οικοσυστήματα",
  "result_eyebrow": "Αποτέλεσμα",
  "score_label": "Συνολική βαθμολογία",
  "co2_year": "CO₂ ανά έτος",
  "tabs": [
   "Κατανομή",
   "Υδρόγειος 3D",
   "Σύγκριση",
   "Συστάσεις",
   "Τεχνολογία & Εξαγωγή"
  ],
  "dist_title": "Κατανομή ανά κατηγορία",
  "metrics_title": "Μετρικές ετήσιου αντίκτυπου",
  "metric_labels": [
   "CO₂ / έτος",
   "Δέντρα / έτος",
   "Λιωμένος πάγος",
   "Νερό που καταναλώθηκε",
   "Υπερθέρμανση"
  ],
  "globe_tab_title": "Ο πλανήτης σύμφωνα με τις επιλογές σου",
  "globe_tab_caption": "Κάθε παλλόμενο σημείο αντιπροσωπεύει μια κατηγορία που απαντήθηκε — όσο πιο έντονο, τόσο μεγαλύτερη η πίεση αυτής της συνήθειας.",
  "compare_title": "Πώς συγκρίνεσαι",
  "scenarios": [
   "Το προφίλ σου",
   "Παγκόσμιος μέσος όρος",
   "Βιώσιμο σενάριο",
   "Κρίσιμο σενάριο"
  ],
  "co2_unit": "CO₂/έτος",
  "co2_axis": "CO₂ (t/έτος)",
  "rec_title": "Εξατομικευμένες συστάσεις",
  "tech_title": "Σχετικά με την τεχνολογία αυτού του έργου",
  "tech_intro": "Αυτός ο υπολογιστής συνδυάζει ένα δηλωτικό back-end σε Python με ένα επίπεδο οπτικοποίησης WebGL που αποδίδεται κατά παραγγελία. Η κεντρική ιδέα — μια τρισδιάστατη σκηνή που αντιδρά σε δεδομένα πραγματικού χρόνου καθώς ο χρήστης αλληλεπιδρά — εμπνεύστηκε από τη γενετική προσέγγιση που χρησιμοποιεί το <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, ένα έργο οπτικοποίησης φάσεων ποδοσφαίρου που ανασυνθέτει ενέργειες σε τρισδιάστατη σκηνή από δεδομένα παρακολούθησης (tracking data).",
  "making_title": "Making-of: δύο προσεγγίσεις γενετικής οπτικοποίησης",
  "making_intro": "Αν και εξυπηρετούν εντελώς διαφορετικούς σκοπούς, τα δύο έργα μοιράζονται το ίδιο βασικό πρόβλημα μηχανικής: <i>πώς μετατρέπουμε ακατέργαστα δεδομένα σε μια ζωντανή σκηνή, χωρίς να αποδίδουμε εκ των προτέρων κάθε καρέ;</i> Ο παρακάτω πίνακας συνοψίζει τις τεχνικές επιλογές του καθενός.",
  "th_aspect": "Πτυχή",
  "th_this": "Αυτό το έργο (Αποτύπωμα)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Πηγή δεδομένων",
    "Απαντήσεις του ερωτηματολογίου, υπολογισμένες στον διακομιστή σε κάθε αλληλεπίδραση",
    "Δεδομένα θέσης (tracking data) από πραγματικούς αγώνες (συντεταγμένες παικτών/μπάλας ανά καρέ)"
   ],
   [
    "Μηχανή απόδοσης",
    "Three.js / WebGL, ενσωματωμένο μέσω στοιχείου HTML στο Streamlit",
    "Προσαρμοσμένο Canvas/WebGL, με δική του μηχανή φυσικής και κάμερας"
   ],
   [
    "Τι αντιδρά στα δεδομένα",
    "Το χρώμα της υδρογείου, τα hotspots ανά κατηγορία, η ένταση του «δείκτη πίεσης»",
    "Οι τροχιές των παικτών, η δυναμική κάμερα, τα γεγονότα (πάσες, σουτ, μονομαχίες)"
   ],
   [
    "Διαδραστικότητα",
    "Χειροκίνητη περιστροφή της υδρογείου, ενημέρωση σε κάθε απάντηση του κουίζ",
    "Παράμετροι ρυθμιζόμενες μέσω URL (κωδικοποιημένο JSON), επανάληψη φάσεων"
   ],
   [
    "Στοίβα back-end",
    "Python + Streamlit (απόδοση της κατάστασης από την πλευρά του διακομιστή)",
    "Στατικό / client-side, με τις ρυθμίσεις ενσωματωμένες στο ίδιο το URL"
   ],
   [
    "Στόχος της τρισδιάστατης σκηνής",
    "Να μεταφράσει μια αφηρημένη βαθμολογία σε μια άμεση οπτική μεταφορά",
    "Να ανασυνθέσει και να αναλύσει πραγματικά αθλητικά γεγονότα με τακτική πιστότητα"
   ]
  ],
  "lesson": "Το βασικό δίδαγμα εδώ: μικρές αντιδραστικές τρισδιάστατες σκηνές μεταδίδουν τάξεις μεγέθους πολύ πιο γρήγορα από τους πίνακες — ο ανθρώπινος εγκέφαλος διαβάζει χρώμα και κίνηση πριν διαβάσει αριθμούς.",
  "export_title": "Εξαγωγή & κοινοποίηση",
  "pdf_button": "📥 Λήψη αναφοράς σε PDF",
  "share_text": "Ανακάλυψα τον περιβαλλοντικό μου αντίκτυπο! Είμαι {profile} με {score} πόντους.",
  "retry": "🔄 Νέος υπολογισμός",
  "methodology_note": "Εκπαιδευτική εκτίμηση: η βαθμολογία μετατρέπει τις απαντήσεις σε εύρη και πολλαπλασιάζει επί 0,8 t CO₂ ανά πόντο. Δεν αντικαθιστά απογραφή εκπομπών.",
  "questions": [
   {
    "title": "Μετακινήσεις",
    "question": "Πόσα km διανύεις καθημερινά (πηγαινοερχόμενος/η);",
    "options": [
     "0 έως 5 km",
     "6 έως 15 km",
     "16 έως 40 km",
     "41 έως 100 km",
     "101 έως 200 km",
     "Πάνω από 200 km"
    ]
   },
   {
    "title": "Διατροφή",
    "question": "Πόσα γεύματα με κρέας τρως την εβδομάδα;",
    "options": [
     "Κανένα, είμαι χορτοφάγος",
     "1 έως 3 γεύματα",
     "4 έως 7 γεύματα",
     "8 έως 14 γεύματα",
     "Πάνω από 14 γεύματα"
    ]
   },
   {
    "title": "Κατανάλωση μόδας",
    "question": "Πόσα καινούργια ρούχα αγοράζεις τον μήνα;",
    "options": [
     "0 - μόνο όταν χρειάζεται",
     "1 έως 2 ρούχα",
     "3 έως 5 ρούχα",
     "6 έως 10 ρούχα",
     "Πάνω από 10 ρούχα"
    ]
   },
   {
    "title": "Τεχνολογία",
    "question": "Πόσο συχνά αγοράζεις καινούργιο κινητό;",
    "options": [
     "Κάθε 5 χρόνια ή περισσότερο",
     "Κάθε 3 έως 4 χρόνια",
     "Κάθε 2 χρόνια",
     "Κάθε χρόνο",
     "Σε λιγότερο από 1 χρόνο"
    ]
   },
   {
    "title": "Ενέργεια",
    "question": "Ποια είναι η μέση κατανάλωση ηλεκτρικής ενέργειας στο σπίτι σου;",
    "options": [
     "Έως 150 kWh/μήνα",
     "151 έως 300 kWh/μήνα",
     "301 έως 500 kWh/μήνα",
     "501 έως 800 kWh/μήνα",
     "Πάνω από 800 kWh/μήνα"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Φύλακας της Γης",
    "desc": "Ο τρόπος ζωής σου είναι εξαιρετικά βιώσιμος. Είσαι παράδειγμα αναγέννησης!"
   },
   {
    "name": "Συνειδητός σε εξέλιξη",
    "desc": "Είσαι στον σωστό δρόμο, αλλά μικρές αλλαγές μπορούν να μειώσουν ακόμη περισσότερο το αποτύπωμά σου."
   },
   {
    "name": "Μέτριος αντίκτυπος",
    "desc": "Ο αντίκτυπός σου είναι αισθητός. Σκέψου να επανεξετάσεις τις συνήθειες κατανάλωσης και μεταφοράς."
   },
   {
    "name": "Περιβαλλοντικός συναγερμός",
    "desc": "Ο τρόπος ζωής σου απαιτεί πόρους που ο πλανήτης δεν μπορεί να αναπληρώσει γρήγορα."
   },
   {
    "name": "Πλανητική κρίση",
    "desc": "Αν όλοι ζούσαν όπως εσύ, θα χρειαζόμασταν αρκετούς πλανήτες Γη."
   }
  ],
  "recs": {
   "transport": {
    "title": "Σκέψου τις δημόσιες συγκοινωνίες",
    "desc": "Η χρήση δημόσιων συγκοινωνιών μειώνει το αποτύπωμα άνθρακά σου έως και 75% σε σύγκριση με την οδήγηση μόνος/η."
   },
   "meat": {
    "title": "Μείωσε την κατανάλωση κρέατος",
    "desc": "Μια διατροφή με λιγότερο κρέας μπορεί να μειώσει το αποτύπωμα άνθρακά σου έως και 50%."
   },
   "fashion": {
    "title": "Αγόραζε ρούχα με περισσότερη σκέψη",
    "desc": "Η επιλογή βιώσιμων μαρκών και οι λιγότερες αγορές μειώνουν σημαντικά τον αντίκτυπο της κλωστοϋφαντουργίας."
   },
   "phone": {
    "title": "Παράτεινε τη ζωή του κινητού σου",
    "desc": "Η διατήρηση της συσκευής για περισσότερο χρόνο μειώνει τα ηλεκτρονικά απόβλητα και τις εκπομπές της κατασκευής."
   },
   "solar": {
    "title": "Σκέψου την ηλιακή ενέργεια",
    "desc": "Τα ηλιακά πάνελ μπορούν να μειώσουν το ενεργειακό σου αποτύπωμα έως και 80%."
   },
   "renewable": {
    "title": "Αξιολόγησε την ανανεώσιμη ενέργεια",
    "desc": "Η σύναψη συμβολαίου ανανεώσιμης ενέργειας με τον πάροχό σου είναι συνήθως μια προσιτή επιλογή."
   },
   "great": {
    "title": "Συγχαρητήρια!",
    "desc": "Ακολουθείς ήδη τις βέλτιστες πρακτικές. Συνέχισε έτσι."
   }
  },
  "globe_hud": "Δείκτης Πίεσης",
  "globe_legend": "σύρε για περιστροφή · scroll για zoom",
  "globe_intensity": "Ένταση",
  "pdf": {
   "file": "relatorio_impacto_ambiental.pdf",
   "title": "Αναφορά Περιβαλλοντικού Αντίκτυπου",
   "profile": "Το Προφίλ σου",
   "metrics": "Μετρικές Ετήσιου Αντίκτυπου",
   "co2": "CO2 / έτος: {v} τόνοι",
   "trees": "Δέντρα / έτος: {v}",
   "ice": "Λιωμένος πάγος: {v} m2",
   "water": "Νερό που καταναλώθηκε: {v} λίτρα",
   "warming": "Υπερθέρμανση: +{v} °C",
   "dist": "Κατανομή ανά Κατηγορία",
   "points": "{cat}: {n} πόντοι",
   "recs": "Εξατομικευμένες Συστάσεις"
  }
 },
 "af": {
  "page_title": "Voetspoor — Omgewingsimpaksakrekenaar",
  "lang_label": "Taal",
  "eyebrow": "Impakrekenaar · 5 vrae",
  "hero_title": "Wat is jou<br>voetspoor op die planeet?",
  "hero_sub": "Antwoord eerlik. Met elke antwoord reageer die aardbol langsaan intyds op jou impakvlak.",
  "progress": "Vraag {n} van {total}",
  "cat_eyebrow": "Kategorie {n} · {title}",
  "choose": "Kies 'n opsie",
  "globe_caption": "Die aardbol weerspieël intyds die druk wat jou leefstyl op ekosisteme plaas",
  "result_eyebrow": "Resultaat",
  "score_label": "Totale telling",
  "co2_year": "CO₂ per jaar",
  "tabs": [
   "Verdeling",
   "3D-aardbol",
   "Vergelyking",
   "Aanbevelings",
   "Tegnologie & Uitvoer"
  ],
  "dist_title": "Verdeling volgens kategorie",
  "metrics_title": "Jaarlikse impakmaatstawwe",
  "metric_labels": [
   "CO₂ / jaar",
   "Bome / jaar",
   "Gesmelte ys",
   "Water verbruik",
   "Verwarming"
  ],
  "globe_tab_title": "Die planeet volgens jou keuses",
  "globe_tab_caption": "Elke polsende punt verteenwoordig 'n beantwoorde kategorie — hoe intenser, hoe groter die druk van daardie gewoonte.",
  "compare_title": "Hoe jy vergelyk",
  "scenarios": [
   "Jou profiel",
   "Wêreldgemiddeld",
   "Volhoubare scenario",
   "Kritieke scenario"
  ],
  "co2_unit": "CO₂/jaar",
  "co2_axis": "CO₂ (t/jaar)",
  "rec_title": "Persoonlike aanbevelings",
  "tech_title": "Oor die tegnologie van hierdie projek",
  "tech_intro": "Hierdie sakrekenaar kombineer 'n deklaratiewe Python-agterkant met 'n WebGL-visualiseringslaag wat op aanvraag geteken word. Die kernidee — om 'n 3D-toneel intyds op data te laat reageer terwyl die gebruiker interaksie het — is geïnspireer deur die generatiewe benadering van <b style='color:#8fd8ff;'>wc26.bogachev.fr</b>, 'n projek wat sokkerspeletjies visualiseer en spelfases as 'n 3D-toneel herbou uit spoordata (tracking data).",
  "making_title": "Making-of: twee benaderings tot generatiewe visualisering",
  "making_intro": "Hoewel hulle heeltemal verskillende doeleindes dien, deel die twee projekte dieselfde kern-ingenieursprobleem: <i>hoe verander jy rou data in 'n lewendige toneel sonder om elke raampie vooraf te teken?</i> Die tabel hieronder som die tegniese keuses van elkeen op.",
  "th_aspect": "Aspek",
  "th_this": "Hierdie projek (Voetspoor)",
  "th_ref": "wc26.bogachev.fr",
  "rows": [
   [
    "Databron",
    "Antwoorde op die vraelys, by elke interaksie op die bediener bereken",
    "Posisionele tracking data van werklike wedstryde (speler-/bal-koördinate per raampie)"
   ],
   [
    "Weergee-enjin",
    "Three.js / WebGL, via 'n HTML-komponent in Streamlit ingebed",
    "Eie Canvas/WebGL, eie fisika- en kameraenjin"
   ],
   [
    "Wat op die data reageer",
    "Kleur van die aardbol, hotspots per kategorie, intensiteit van die \"drukindeks\"",
    "Spelerbane, dinamiese kamera, gebeure (aangee, skote, tweestryde)"
   ],
   [
    "Interaktiwiteit",
    "Handmatige draai van die aardbol, opdatering by elke vasvraag-antwoord",
    "Parameters instelbaar via URL (gekodeerde JSON), herhaling van spelfases"
   ],
   [
    "Agterkant-stapel",
    "Python + Streamlit (bedienerkant-weergawe van die toestand)",
    "Staties / kliëntkant, konfigurasie in die URL self ingebed"
   ],
   [
    "Doel van die 3D-toneel",
    "'n Abstrakte telling in 'n onmiddellike visuele metafoor omskep",
    "Werklike sportgebeure met taktiese getrouheid herbou en ontleed"
   ]
  ],
  "lesson": "Die belangrikste les hier: klein reaktiewe 3D-tonele kommunikeer groottes baie vinniger as tabelle — die menslike brein lees kleur en beweging voordat dit syfers lees.",
  "export_title": "Voer uit & deel",
  "pdf_button": "📥 Laai verslag as PDF af",
  "share_text": "Ek het my omgewingsimpak ontdek! Ek is {profile} met {score} punte.",
  "retry": "🔄 Bereken weer",
  "methodology_note": "Opvoedkundige skatting: die telling skakel antwoorde om na bande en vermenigvuldig met 0,8 t CO₂ per punt. Dit vervang nie 'n emissie-inventaris nie.",
  "questions": [
   {
    "title": "Mobiliteit",
    "question": "Hoeveel km beweeg jy per dag (heen en terug)?",
    "options": [
     "0 tot 5 km",
     "6 tot 15 km",
     "16 tot 40 km",
     "41 tot 100 km",
     "101 tot 200 km",
     "Meer as 200 km"
    ]
   },
   {
    "title": "Voeding",
    "question": "Hoeveel maaltye met vleis eet jy per week?",
    "options": [
     "Geen, ek is vegetariër",
     "1 tot 3 maaltye",
     "4 tot 7 maaltye",
     "8 tot 14 maaltye",
     "Meer as 14 maaltye"
    ]
   },
   {
    "title": "Modeverbruik",
    "question": "Hoeveel nuwe klere koop jy per maand?",
    "options": [
     "0 - net wanneer nodig",
     "1 tot 2 stukke",
     "3 tot 5 stukke",
     "6 tot 10 stukke",
     "Meer as 10 stukke"
    ]
   },
   {
    "title": "Tegnologie",
    "question": "Hoe gereeld koop jy 'n nuwe selfoon?",
    "options": [
     "Elke 5 jaar of langer",
     "Elke 3 tot 4 jaar",
     "Elke 2 jaar",
     "Elke jaar",
     "Minder as 1 jaar"
    ]
   },
   {
    "title": "Energie",
    "question": "Wat is die gemiddelde elektrisiteitsverbruik in jou huis?",
    "options": [
     "Tot 150 kWh/maand",
     "151 tot 300 kWh/maand",
     "301 tot 500 kWh/maand",
     "501 tot 800 kWh/maand",
     "Meer as 800 kWh/maand"
    ]
   }
  ],
  "profiles": [
   {
    "name": "Bewaarder van die Aarde",
    "desc": "Jou leefstyl is hoogs volhoubaar. Jy is 'n voorbeeld van hernuwing!"
   },
   {
    "name": "Bewus en Groeiend",
    "desc": "Jy is op die regte pad, maar klein veranderinge kan jou voetspoor nog verder verklein."
   },
   {
    "name": "Matige Impak",
    "desc": "Jou impak is merkbaar. Oorweeg dit om jou verbruiks- en vervoergewoontes te hersien."
   },
   {
    "name": "Omgewingsalarm",
    "desc": "Jou lewenspatroon vereis hulpbronne wat die planeet nie vinnig kan aanvul nie."
   },
   {
    "name": "Planetêre Krisis",
    "desc": "As almal soos jy gelewe het, sou ons verskeie planete soos Aarde nodig hê."
   }
  ],
  "recs": {
   "transport": {
    "title": "Oorweeg openbare vervoer",
    "desc": "Openbare vervoer verklein jou koolstofvoetspoor tot 75% in vergelyking met alleen bestuur."
   },
   "meat": {
    "title": "Verminder jou vleisverbruik",
    "desc": "'n Dieet met minder vleis kan jou koolstofvoetspoor tot 50% verklein."
   },
   "fashion": {
    "title": "Koop klere met meer oorleg",
    "desc": "Om volhoubare handelsmerke te kies en minder te koop verminder die tekstielimpak aansienlik."
   },
   "phone": {
    "title": "Verleng die lewe van jou selfoon",
    "desc": "Om die toestel langer te hou verminder elektroniese afval en vervaardigingsemissies."
   },
   "solar": {
    "title": "Oorweeg sonenergie",
    "desc": "Sonpanele kan jou energievoetspoor tot 80% verklein."
   },
   "renewable": {
    "title": "Evalueer hernubare energie",
    "desc": "Om hernubare energie by jou kragverskaffer te koop is dikwels 'n bekostigbare opsie."
   },
   "great": {
    "title": "Geluk!",
    "desc": "Jy volg reeds die beste praktyke. Gaan so voort."
   }
  },
  "globe_hud": "Drukindeks",
  "globe_legend": "sleep om te draai · rol om te zoem",
  "globe_intensity": "Intensiteit",
  "pdf": {
   "file": "omgewingsimpak_verslag.pdf",
   "title": "Omgewingsimpakverslag",
   "profile": "Jou Profiel",
   "metrics": "Jaarlikse Impakmaatstawwe",
   "co2": "CO2 / jaar: {v} ton",
   "trees": "Bome / jaar: {v}",
   "ice": "Gesmelte ys: {v} m2",
   "water": "Water verbruik: {v} liter",
   "warming": "Verwarming: +{v} °C",
   "dist": "Verdeling volgens Kategorie",
   "points": "{cat}: {n} punte",
   "recs": "Persoonlike Aanbevelings"
  }
 }
}
