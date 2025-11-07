from dash import Dash, html, dcc, Input, Output, State
import micro

app_layout = html.Div([
    # 🔹 Navbar
    html.Nav(
        className="navbar",
        children=[
            html.Div("CCI NICE CÔTE D’AZUR", className="brand"),
            html.Div(
                className="navbar-links",
                children=[
                    html.A("Études et Data", href="/data", className="nav-link"),
                    html.A("Analyses", href="#", className="nav-link"),
                    html.Button("Connexion", className="btn-connexion")
                ]
            )
        ]
    ),
    # 🔹 Bloc principal
    html.Div(
        className="main-card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    html.H5("Posez votre question", className="section-title"),
                    dcc.Input(
                        id='user-input',
                        type='text',
                        placeholder="Ex: Quelle est la croissance démographique à Cannes ?",
                        className="input-question"
                    ),
                    micro.Micro(id='audioInput'),
                    html.Div(
                        className="audio-upload",
                        children=[
                            dcc.Upload(
                                id='audioInput',
                                children=html.Button("Upload Audio", className="upload-btn")
                            ),
                            html.Div(id='output')
                        ]
                    ),
                    html.Div(
                        className="suggestions-box",
                        children=[
                            html.Button("Quelle est l’évolution de la population à Nice ?", id="btn1", className="suggestion-btn"),
                            html.Button("Quels sont les secteurs d’emploi les plus dynamiques ?", id="btn2", className="suggestion-btn"),
                            html.Button("Montrez-moi la répartition par âge de la population", id="btn3", className="suggestion-btn"),
                            html.Button("Comparez les revenus médians des différentes villes", id="btn4", className="suggestion-btn")
                        ]
                    ),
                    html.Div(
                        className="analyze-btn-container",
                        children=[
                            html.Button("Analyser", id="analyze-btn", className="analyze-btn")
                        ]
                    )
                ]
            )
        ]
    ),

  # 🔹 Section conversation
    html.Div(
        className="conversation-section",
        id="conversation-section",
        children=[
            html.Div(
                className="conversation-block",
                children=[
                    html.Div(
                        className="user-block",
                        children=[
                            html.P("", className="user-message", id="dup-user-input")
                        ]
                    ),

                    html.Div(
                        className="assistant-block",
                        children=[
                            html.Div(
                                className="assistant-message",
                                children=[
                                    html.Div("Assistant AI CCI", className="assistant-name"),
                                    html.Div(
                                        className="assistant-message-box",
                                        id="assistant-response"
                                    ),
                                    html.Img(id="plot-image")
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    ),

# Storing conversation data (if needed for future use)
 dcc.Store(id="conversation-store", data=[])
])