from dash import Dash, html, dcc, dash_table


# Each entry lists the dataset file and a clear English description for judges and code comments.

dataset_files = [
    # 🌦️ Climate & Environment
    {
        "file_name": "Climate_Change_Data_AlpesMaritimes_2022_2025.csv",
        "description": "Monthly climate indicators (2022–2025) for Alpes-Maritimes: precipitation, temperature, evaporation, SPI/SSWI drought indices, and water flow levels.",
        "reference": "https://www.insee.fr/fr/statistiques/8568899"
    },
    {
        "file_name": "Land_Use_Database_PACA_Region_2019.csv",
        "description": "Land use dataset for the PACA region (2019), classifying urban, forest, agricultural, and coastal land types.",
        "reference": "https://www.data.gouv.fr/en/datasets/occupation-du-sol-paca/"
    },
    {
        "file_name": "DÉVELOPPEMENT DURABLE - OBJECTIFS 1 À 5.xlsx",
        "description": "Local Sustainable Development Goal (SDG) indicators 1–5: poverty, education, gender equality, health, and economic growth.",
        "reference": "https://www.insee.fr/fr/statistiques/2011101?geo=DEP-06"
    },
    {
        "file_name": "Sustainable Development.xlsx",
        "description": "Regional sustainability indicators combining environmental, social, and economic metrics for Alpes-Maritimes.",
        "reference": "https://www.data.gouv.fr/en/datasets/indicateurs-de-developpement-durable/"
    },
 
    # 👥 Demographics & Population
    {
        "file_name": "evolution_population_alpes_maritimes_1947_2025.xlsx",
        "description": "Population evolution in Alpes-Maritimes from 1947 to 2025, including start and end values with growth rates.",
        "reference": "https://www.insee.fr/fr/statistiques/3698339"
    },
    {
        "file_name": "Résidences principales par type de logement, nombre de pièces et âge de la personne de référence en 2022.csv",
        "description": "Primary housing distribution by dwelling type, number of rooms, and age of household reference (2022).",
        "reference": "https://www.insee.fr/fr/statistiques/5654064"
    },
    {
        "file_name": "Diplômes - Formation en 2022.csv",
        "description": "Education and training level by commune in 2022.",
        "reference": "https://www.insee.fr/fr/statistiques/5654068"
    },
    {
        "file_name": "Country of Birth of Immigrants Living in France in 2024 (2).xlsx",
        "description": "Country of birth distribution for immigrants living in France (2024).",
        "reference": "https://www.data.gouv.fr/en/datasets/population-etrangere-et-immigree-en-france/"
    },
    {
        "file_name": "Educational Attainment of Immigrants by Geographic Origin in 2024.xlsx",
        "description": "Immigrant education level by geographic origin for 2024 (primary, secondary, higher education).",
        "reference": "https://www.insee.fr/fr/statistiques/6433434"
    },
 
    # 💼 Employment & Economy
    {
        "file_name": "Employment_Density_Grid_PACA_AlpesMaritimes.csv",
        "description": "Employment density grid (1 km²) for Alpes-Maritimes and PACA, showing workforce distribution.",
        "reference": "https://www.insee.fr/fr/statistiques/2520034"
    },
    {
        "file_name": "Workforce_Transport_and_PartTime_Trends_2021.csv",
        "description": "Trends in workforce transport habits and part-time employment for 2021.",
        "reference": "https://www.data.gouv.fr/en/datasets/mobilite-professionnelle-et-temps-de-travail/"
    },
 
    # 🏥 Health & Social
    {
        "file_name": "Health.xlsx",
        "description": "Health infrastructure (hospitals, clinics, pharmacies) with coordinates and OpenStreetMap metadata.",
        "reference": "https://www.data.gouv.fr/en/datasets/openstreetmap-sante-france/"
    },
    {
        "file_name": "Health & Social.csv",
        "description": "Healthcare and social facilities (EHPAD, hospitals, clinics) with postal address, contact, and geographic data.",
        "reference": "https://www.data.gouv.fr/en/datasets/etablissements-sanitaires-et-sociaux/"
    },
    {
        "file_name": "Hospitals Houses.xlsx",
        "description": "List of hospital centers and healthcare houses by location and service type.",
        "reference": "https://www.data.gouv.fr/en/datasets/liste-des-etablissements-de-sante/"
    },
 
    # 🏫 Education
    {
        "file_name": "lycée ( highschool).xlsx",
        "description": "High school dataset (public/private) with school names, addresses, and education levels.",
        "reference": "https://www.data.gouv.fr/en/datasets/annuaire-des-etablissements-du-second-degre/"
    },
    {
        "file_name": "Private School.xlsx",
        "description": "Private school data with type, academic level, and location.",
        "reference": "https://www.data.gouv.fr/en/datasets/annuaire-des-ecoles-privees/"
    },
 
    # 🌳 Nature & Recreation
    {
        "file_name": "Regional Natural Parks – Trails and Routes.xlsx",
        "description": "Dataset of natural parks and hiking routes in Alpes-Maritimes with trail names and geolocation.",
        "reference": "https://www.data.gouv.fr/en/datasets/parcs-naturels-regionaux-et-sentiers/"
    },
 
    # 🚗 Mobility & Infrastructure
    {
        "file_name": "Réseau routier du département du Var.csv",
        "description": "Road network of the Var department (adjacent to Alpes-Maritimes): road names, types, and coordinates.",
        "reference": "https://www.data.gouv.fr/en/datasets/reseau-routier-departemental/"
    },
    {
        "file_name": "Bicycle Database … – Parking Locations (with geolocation data).csv",
        "description": "Bicycle parking locations and capacities, with postal codes and providers for Alpes-Maritimes.",
        "reference": "https://www.data.gouv.fr/en/datasets/parkings-a-velos-et-amenagements-cyclables/"
    },
 
    # 🍴 Lifestyle & Services
    {
        "file_name": "restaurants.xlsx",
        "description": "Restaurant listing with name, type, address, and coordinates (for tourism and lifestyle analytics).",
        "reference": "https://www.data.gouv.fr/en/datasets/openstreetmap-restaurants-france/"
    }
]

data_layout = html.Div([
    # 🔹 Navbar
    html.Nav(
        className="navbar",
        children=[
            html.Div("CCI NICE CÔTE D’AZUR", className="brand"),
            html.Div(
                className="navbar-links",
                children=[
                    html.A("Études et Data", href="#", className="nav-link"),
                    html.A("Analyses", href="/", className="nav-link"),
                    html.Button("Connexion", className="btn-connexion")
                ]
            )
        ]
    ),

    # 🔹 Bloc principal: Data files overview
    html.Div(
        className="main-card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    html.H5("Fichiers de données utilisés", className="section-title"),
                    
                    html.P(
                        "Voici un aperçu des fichiers de données utilisés par l'outil, avec une description rapide de leur contenu.",
                        className="data-description"
                    ),
                    
                    # 🔹 Dash DataTable
                    dash_table.DataTable(
    id="dataset-table",
    columns=[
        {"name": "Nom du fichier", "id": "file_name"},
        {"name": "Description", "id": "description"},
        {"name": "Référence", "id": "reference"}
    ],
    data=dataset_files,  # comme avant, référence en markdown
    style_table={
        "width": "100%",
        "overflowX": "auto"   # permet le scroll horizontal si nécessaire
    },
    style_header={
        "backgroundColor": "#f0f0f0",
        "fontWeight": "bold",
        "whiteSpace": "normal"
    },
    style_cell={
        "textAlign": "left",
        "padding": "8px",
        "whiteSpace": "normal",  # autorise le retour à la ligne
        "height": "auto",        # ajuste la hauteur automatiquement
        "maxWidth": "400px",     # largeur max pour éviter que la cellule soit trop large
        "overflow": "hidden",    # masque l'excédent si nécessaire
        "textOverflow": "ellipsis"  # ajoute "..." si le texte déborde
    },
    style_cell_conditional=[
        {"if": {"column_id": "description"}, "maxWidth": "600px"}  # plus de place pour description
    ],
    page_size=10
)
  
                ]
            )
        ]
    ),

    # Optional: store page state
    dcc.Store(id="data-page-store", data={})
])
