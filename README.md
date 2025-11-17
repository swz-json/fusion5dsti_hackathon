# Alpes-Maritimes Data Assistant 🗺️🤖  
*Hackathon “Top Tech 2025” - CCI Nice Côte d’Azur*

An interactive web app that lets users ask natural-language questions about the Alpes-Maritimes (06) and instantly get **indicators, charts and explanations**.

Example:  
> « Donne le nombre d'habitants de Nice »  
> « Top 5 communes du 06 par population »  
> « Évolution de la population à Cannes entre 1968 et 2020 »

---

## 🚀 Project Overview

This project was built in **24 hours** during the CCI Nice Côte d’Azur hackathon.

Goal: create a prototype that:

- Understands a question in French (commune, indicator, period…)
- Translates it into a query on **local datasets (Alpes-Maritimes / INSEE)**
- Returns:
  - numerical indicators
  - bar/line charts
  - short explanations in French
- Handles missing data with a **clear message + alternative suggestions**

The app is delivered as a **Dash web application** that anyone can run locally.

---

## 🎯 Main Features

- 🧠 **Chatbot-style interface**: ask questions in natural French  
- 📊 **Automatic visualizations**: line / bar charts generated from local CSV data  
- 🏙️ **Commune-level indicators** (INSEE code, name, department 06)  
- 🗂️ **Centralized data catalog**: population, land use, health/social (etc.)  
- ⚠️ **“Unavailable data” handling**: clear message + alternative suggestions  
- 🇫🇷 **French-only user interface** (labels, messages, explanations)  

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Frontend / Backend:** [Plotly Dash](https://dash.plotly.com/)  
- **Data / Analytics:** `pandas`, `numpy`, `pandasai` (or LLM wrapper)  
- **Visualization:** `plotly.express`  
- **LLM Integration:** PandasAI / LiteLLM / Mistral via Hugging Face  
- **Data Format:** CSV (INSEE, open data Alpes-Maritimes, etc.)

---

## 📊 Datasets

All datasets are stored in the `data/` or `code/fusion5dsti/data/` folder.

Examples (adapt to your real filenames):

- `department_06_population.csv` – Population by commune and year (INSEE code, commune name, year, population)  
- `department_06_land_use.csv` – Land use categories by commune (urban, agricultural, natural…)  
- `department_06_health_social.csv` – Health & social indicators (if available)  
- `metadata_dataset_catalog.csv` – Internal catalog describing each dataset (columns, definitions, source URLs)  

> Each file is documented in a **data catalog** so the chatbot can explain indicators to the user.

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt
