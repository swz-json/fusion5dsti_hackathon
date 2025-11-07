# Alpes-Maritimes Data Explorer (Top Tech Hackathon 2025)
 
**Prototype developed in 24h during the Top Tech Hackathon 2025**  
Theme: **Data for Sustainable Territories (Alpes-Maritimes, France)** 
Team: Data ScienceTech Institue, Sophia Antipollis
 
---
 
## Project Overview
 
This project is an **interactive AI-powered dashboard** that answers natural language questions such as:  
> “Top 5 communes of Alpes-Maritimes by population”  
> “What is the population growth between 1947 and 2025?”  
> “Air quality in Nice today”  
 
The app allows users to **query, visualize, and understand socio-economic, environmental, and mobility data** of the Alpes-Maritimes region.
 
---
 
## Main Features
 
- **AI Chat Interface** — Ask questions in natural language (French or English).  
- **Dynamic Visualizations** — Auto-generated graphs (bar, line, map).  
- **Multi-dataset Integration** — Population, Transport, Air Quality, Employment, and more.  
- **Fallback Mode** — Suggests alternative indicators when a dataset is missing.  
- **Local Context Focus** — Works at the commune level using INSEE codes.
 
---
 
## Tech Stack
 
| Component | Tool / Library |
|------------|----------------|
| **Frontend** | Dash (Plotly) |
| **Backend / Logic** | Python (Pandas, PandasAI) |
| **AI Model** | Grok |
| **Data Handling** | Pandas, SmartDataframe |
| **Visualization** | Plotly Express |
| **Version Control** | GitHub |
| **Data Source** | INSEE, CRIGE PACA, AtmoSud, Data.gouv.fr |
 
---
 
## Datasets Used
 
| Dataset | Description | Source |
|----------|--------------|--------|
| `department_06_population.csv` | Population by commune (1947–2025) | INSEE |
| `air_quality.csv` | Daily air quality index (Nice, Cannes, Antibes) | AtmoSud |
| `transport_access.csv` | Transport accessibility and station data | CRIGE PACA |
| `land_use_ocs.csv` | Land use classification (OCSOL 2019) | BD OCSOL / IGN |
| `company_siren.csv` | Company registry and activity sectors | INSEE SIRENE |
| `employment_characteristics.csv` | Employment rate, activity, and unemployment | INSEE |
| `health_social.csv` | Social and medical infrastructures per commune | Data.gouv.fr |
 
*(All datasets used in this project can found in this [Share Point Link](https://ccinice-my.sharepoint.com/personal/luca_uggeri_cote-azur_cci_fr/_layouts/15/guestaccess.aspx?e=pUbUay&share=Eil_D0eQBCRGg9aOrsk_3gsBa3F7ScyEzvSdDMuRK9oWoA&xsdata=MDV8MDJ8fGU2Y2NhMDYwZWM1YzQxYjk2NDBmMDhkZTFkMzM0YTNkfGU1ZDE1MDY5NDFhMjQ4YmVhM2YzZDdmNTJkYjE2NDI1fDB8MHw2Mzg5ODAzMDMyNTkyNjQwMTV8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKRFFTSTZJbFJsWVcxelgwRlVVRk5sY25acFkyVmZVMUJQVEU5R0lpd2lWaUk2SWpBdU1DNHdNREF3SWl3aVVDSTZJbGRwYmpNeUlpd2lRVTRpT2lKUGRHaGxjaUlzSWxkVUlqb3hNWDA9fDF8TDJOb1lYUnpMekU1T21KbVlUWTRPRFkwTXpCak9EUmhNakE0WkdGalpHRTRPV05oTVdJeE5XTTFRSFJvY21WaFpDNTJNaTl0WlhOellXZGxjeTh4TnpZeU5ETXpOVEkwTWpRNXw4ODBjZTM0MmMzOGY0YTA1NjQwZjA4ZGUxZDMzNGEzZHw2ZjhmOGJkMWRmMTQ0ZGRmYWIxNTYwMjNlNzhhZDc2NQ%3D%3D&sdata=NDc0U1VIL0ZYa3I3Zit1LzZFTVdsQzFQaXZkOFR0VThSbS83Q3BMZlpDOD0%3D&ovuser=e5d15069-41a2-48be-a3f3-d7f52db16425%2Csai-aditya.lakkum%40edu.dsti.institute))*
