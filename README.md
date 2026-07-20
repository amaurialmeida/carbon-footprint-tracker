# 🌍 Carbon Footprint Tracker — Interactive Environmental Impact Calculator

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://carbon-footprint-tracker-tkfv5pthky3rk2gd8m9mm8.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

🌐 **Languages:** English | [Português](README.pt-BR.md) | [Español](README.es.md)

**Applied Data Science — Personal Environmental Impact Modeling**
**Author:** Amauri Almeida de Souza Junior

---

## ❓ Project Question

> "Can a short, 5-question lifestyle quiz produce a meaningful, personalized estimate of someone's environmental footprint — and communicate it in a way that's more intuitive than a spreadsheet of numbers?"

**Answer:** Yes. By scoring five everyday behavior categories (mobility, diet, fashion consumption, tech consumption, and energy use) on a points scale, the tool converts a short questionnaire into a full impact profile — estimated annual CO₂, trees needed to offset it, water footprint, and ice-melt equivalent — then renders that score as a live, reactive 3D globe instead of a static chart, making the abstraction of "carbon footprint" visually immediate.

---

## 📊 How It Works

| Component | Detail |
|---|---|
| Quiz categories | 5 (Mobility, Diet, Fashion, Technology, Energy) |
| Scoring range | 5–26 points total |
| Impact profiles | 5 tiers, from "Earth Guardian" 🟢 to "Planetary Crisis" 🟣 |
| Derived metrics | CO₂/year, trees to offset, ice melted, water consumed, warming contribution |
| Output | Interactive dashboard + downloadable PDF report |

---

## 🔵 Key Features

- **Personalized impact score** — 5-question quiz converts real lifestyle habits (commute distance, meat consumption, clothing purchases, device upgrade frequency, household energy use) into a weighted impact score.
- **Reactive 3D globe visualization** — a WebGL globe (Globe.gl / Three.js) changes color and pulses per-category "hotspots" in real time based on the user's answers, translating an abstract score into an immediate visual metaphor.
- **Multi-metric breakdown** — beyond CO₂, the tool estimates trees required for offset, water footprint, ice-melt equivalent, and marginal warming contribution.
- **Personalized recommendations engine** — rule-based logic flags the highest-impact categories in each user's answers and surfaces targeted, actionable suggestions (e.g., public transit, renewable energy, reduced meat consumption).
- **Peer comparison** — visual comparison of the user's footprint against reference benchmarks.
- **Exportable PDF report** — one-click download of a full personal impact report, plus native social sharing (X, LinkedIn, WhatsApp).
- **Trilingual interface** — PT / EN / ES support throughout.

---

## 🔬 Methodology

```
Quiz design      →  5 categories, each with 4–6 graded answer options (1–6 points each),
                     covering mobility, diet, fashion, technology, and energy use

Scoring          →  total_score = sum of points across all 5 answers (range: 5–26)

Impact modeling  →  CO₂ (t/year)   = total_score × 0.8
                     Trees/year     = CO₂ × 45
                     Ice melted     = CO₂ × 3
                     Water (L)      = CO₂ × 2,000
                     Warming (°C)   = total_score × 0.01
                     (Illustrative linear model for relative comparison between
                     users, not a peer-reviewed LCA emissions calculation.)

Profiling        →  score mapped to one of 5 tiers (Earth Guardian → Planetary Crisis),
                     each with a distinct color, emoji, and descriptive message

Recommendations  →  rule-based: any category scoring at/above a threshold triggers
                     a targeted, pre-written suggestion

3D visualization →  Globe.gl (Three.js/WebGL) component embedded via
                     st.components.v1.html; globe color and per-category hotspot
                     intensity update live from the computed impact level
```

---

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| Python 3.11 | Core language |
| Streamlit | Interactive dashboard & multi-tab UI |
| Three.js / WebGL (via Globe.gl) | Real-time reactive 3D globe |
| Plotly | Category distribution & comparison charts |
| Pandas | Data handling |
| FPDF | PDF report generation |
| Custom CSS design system | Space Grotesk / Inter / JetBrains Mono, dark theme with mint/amber/coral accent system |

---

## 📁 Repository Structure

```
carbon-footprint-tracker/
├── app.py                   # Main Streamlit application (quiz, scoring, dashboard)
├── globe_component.py       # Reactive 3D globe (Globe.gl/Three.js) HTML component
├── requirements.txt         # Python dependencies
├── README.md                  # This file (English)
├── README.pt-BR.md            # Portuguese version
└── README.es.md               # Spanish version
```

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/amaurialmeida/carbon-footprint-tracker.git
cd carbon-footprint-tracker

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 🌐 Live App

🔗 **[carbon-footprint-tracker.streamlit.app](https://carbon-footprint-tracker-tkfv5pthky3rk2gd8m9mm8.streamlit.app/)**

Available in 🇧🇷 Portuguese, 🇺🇸 English, and 🇪🇸 Spanish.

---

## 🔗 Academic / Professional Links

| Platform | Link |
|---|---|
| Lattes | http://lattes.cnpq.br/9545242042800090 |
| Escavador | https://www.escavador.com/sobre/8577779/amauri-almeida-de-souza-junior |

---

## 🌿 Environmental Portfolio

This project is part of the author's environmental research and data science portfolio.
🔗 [amaurialmeida.github.io/environmental-portfolio](https://amaurialmeida.github.io/environmental-portfolio)

---

© 2025–2026 · Amauri Almeida de Souza Junior · Portfolio Project
