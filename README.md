<div align="center">
  <br />
  <img width="150" height="150" alt="CCI-FRANCE-logo-removebg-preview" src="https://github.com/user-attachments/assets/06211337-cc0c-4635-adb9-a6cc128dc4e7" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img width="150" height="150" alt="logo-dsti" src="https://github.com/user-attachments/assets/1939ca52-665c-4b0a-a65b-0aee9aa15563" />
  <br /><br />



  # 🥈 Alpes-Maritimes Data Assistant (AMDA)
  ### Team Fusion5

  ![Hackathon Rank](https://img.shields.io/badge/Hackathon_Rank-2nd_Place-silver?style=for-the-badge&logo=trophy)
  ![Event](https://img.shields.io/badge/Event-Top_Tech_2025-blue?style=for-the-badge)
  ![Time Limit](https://img.shields.io/badge/Time_Limit-24h_Chrono-critical?style=for-the-badge)
  
  <br />

  **Un assistant conversationnel intelligent qui transforme vos questions en langage naturel en analyses visuelles sur le territoire des Alpes-Maritimes.**
  
  *Développé en 24h chrono lors du Hackathon CCI Nice Côte d'Azur "Top Tech 2025".*

  <br />
</div>

---

## 📸 L'Équipe en Action!


https://github.com/user-attachments/assets/208ea7aa-207d-4beb-b377-b16c2aab3ba6



<div align="center">
  [<img src="https://github.com/user-attachments/assets/5448e799-2985-4f43-81c9-80de7e8cc128" alt="Team Fusion5 Hackathon" width="300" height="300" style="border-radius: 10px;"/>](https://github.com/user-attachments/assets/208ea7aa-207d-4beb-b377-b16c2aab3ba6)
  <p><i>Team Fusion5 en plein rush pendant les 24h du hackathon à l'Azur Arena Antibes.</i></p>
</div>

---

## 💡 Le Défi & La Solution

**Le Contexte :** Nous avions **24 heures** pour concevoir une solution innovante exploitant les données ouvertes (Open Data) locales.

**Le Problème :** Les données publiques (INSEE, départements) sont riches mais difficiles d'accès pour les citoyens. Trouver une info simple comme *"L'évolution de la population à Cannes"* demande de fouiller dans des fichiers CSV complexes.

**Notre Solution - AMDA :** Nous avons créé **AMDA**, une interface IA générative connectée aux datasets locaux. Elle permet à n'importe qui de poser des questions en français et d'obtenir instantanément des graphiques et des résumés, sans écrire une seule ligne de code.

> **Exemples de questions supportées :**
> * 🗣️ *« Donne le nombre d'habitants de Nice »*
> * 🗣️ *« Top 5 des communes du 06 par densité de population »*
> * 🗣️ *« Affiche l'évolution démographique d'Antibes entre 2000 et 2020 »*

---

## ✨ Fonctionnalités Clés

- **🤖 Interface Chatbot Naturelle :** Utilisation de LLMs pour comprendre l'intention de l'utilisateur en français.
- **📊 Auto-Visualisation :** Génération dynamique du graphique le plus adapté (courbe, histogramme, camembert) selon la réponse.
- **🗺️ Focus Local (06) :** Spécialisé sur les données des Alpes-Maritimes à l'échelle communale.
- **🛡️ Gestion d'Erreur Intelligente :** Si la donnée manque, l'IA suggère des questions alternatives pertinentes au lieu de planter.
- **📚 Catalogue de Données :** L'IA "lit" les métadonnées pour comprendre le sens des colonnes (ex: Code INSEE, Population, Superficie).

---

## 🏗️ Stack Technique

Une architecture moderne combinant Python et IA Générative.

| Catégorie | Outils |
| :--- | :--- |
| **Frontend / Backend** | ![Dash](https://img.shields.io/badge/Plotly_Dash-000000?style=flat-square&logo=plotly&logoColor=white) (Framework Python pour data apps) |
| **Langage** | ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white) |
| **Data & Analyse** | `pandas`, `numpy` |
| **IA & LLM** | **PandasAI** (Text-to-Pandas), LLM via Hugging Face |
| **Visualisation** | `plotly.express` |
| **Sources** | CSV Locaux (INSEE, Open Data 06) |

---

## 🚀 Installation & Test

Suivez ces étapes pour lancer le prototype localement.

```bash
# 1. Cloner le dépôt
git clone [https://github.com/swz-json/fusion5dsti_hackathon.git](https://github.com/swz-json/fusion5dsti_hackathon.git)
cd fusion5dsti_hackathon

# 2. Créer un environnement virtuel (recommandé)
python -m venv .venv
# Sur Windows :
.venv\Scripts\activate
# Sur Mac/Linux :
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python app.py
```


## 👥 La Team Fusion5

Étudiants du **DSTI (Data ScienceTech Institute)** et de l'**Université Côte d'Azur**.

<div align="center">

| **Wassim Elmoufakkir** | **Abdellahi** | **Tuan Nam Pham** | **Sai Aditya Lakkum** |
| :---: | :---: | :---: | :---: |
| [GitHub Profile](https://github.com/swz-json) | [GitHub Profile](#) | [GitHub Profile](#) | [GitHub Profile](#) |

</div>

---
<div align="center">
  <sub>Projet réalisé avec beaucoup de ☕ et d'IA en 24h pour le Hackathon Top Tech 2025.</sub>
</div>
