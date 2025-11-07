from pydoc import text
from urllib import response
import io
import base64
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
# from langchain_groq import ChatGroq
import os
import pandasai as pai
from pandasai import  Agent
import pandas as pd
from pandasai_litellm import LiteLLM
from dash import Dash, html, dcc, Input, Output, State, ctx
from layout import app_layout

from data_page_layout import data_layout 
from dash_extensions import EventListener
import base64
import flask
from flask import request
from pathlib import Path
import os
from werkzeug.datastructures import FileStorage
from vosk import Model, KaldiRecognizer
import wave
import json
from plot_generation import generate_plot, generate_cross_filter

df = pd.read_csv(".\data\department_06_population.csv")

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    html.Div(id='page-content')
])


server = app.server


@server.route('/upload_audio', methods=['POST'])
def handle_upload():
    # print("file upload triggered!")
    if 'audioFile' not in request.files:
        return flask.jsonify({'error': 'No file part'}), 400
    
    file = request.files['audioFile']

    if file.filename == '':
        return flask.jsonify({'error': 'No selected file'}), 400
    if file:

        # Assume 'file' is your FileStorage object from the POST-ed file
        directory = '\\tmpfiles'
        os.listdir(directory)
        filename = file.filename
        file_path = os.path.join(directory, filename)

        # Check if the directory exists and create it if not
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Check if file exists and remove it to ensure overwrite -- app was originally not overwriting the existing file
        if os.path.exists(file_path):
            os.remove(file_path)

        file.save(file_path)
        # print("returning saved file_path")

        return flask.jsonify({'message': 'File uploaded successfully', "fileLoc": file_path}), 200

MODEL_PATH = "./vosk_models/vosk-model-small-fr-0.22"
model = Model(MODEL_PATH)

# @callback(
#     Output('output', 'children'),
#     Input('audioInput', 'fileUrl') 
# )
# def display_output(file_path):
#     from pydub import AudioSegment
#     if file_path is None:
#         return html.Div(
#     html.P("Ask me a question or upload an audio file!"),
#     style={'fontSize': '14px', 'color': '#555'}
# )

#     try:
#         # Convert MP3 to WAV if needed
#         if file_path.endswith(".mp3"):
#             audio = AudioSegment.from_mp3(file_path)
#             wav_path = file_path.replace(".mp3", ".wav")
#             audio.export(wav_path, format="wav")
#         else:
#             wav_path = file_path  # already WAV

#         # Transcribe with Vosk
#         wf = wave.open(wav_path, "rb")
#         rec = KaldiRecognizer(model, wf.getframerate())

#         while True:
#             data = wf.readframes(4000)
#             if len(data) == 0:
#                 break
#             rec.AcceptWaveform(data)

#         result = json.loads(rec.FinalResult())
#         text = result.get("text", "")

#         return html.Div([
#             html.P(f"Audio file: {file_path}"),
#             html.P(f"Transcription: {text}")
#         ])

#     except Exception as e:
#         return html.Div([
#             html.P(f"Error processing audio file: {file_path}"),
#             html.P(str(e))
#         ])
    



def get_data_frames():
    filenames =['bicycle_parking_locations.csv', 'department_06_population.csv',
                'enterprises_details.csv','high_school_data.csv','hospitals_locations_data.csv',
                'housing_tourism_employment_by_department.csv','maternal_child_services.csv',
                'population_by_nationality_gender.csv','private_school_data.csv','sncf_train_details.csv',
                'weather_and_climate_by_lat_long.csv']
    
    dataframes = []
    for file in filenames:
        try:
            dataframe = pd.read_csv("./processed_data/"+file, low_memory=False)
            dataframes.append(dataframe)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return dataframes



dataframes = get_data_frames()

# def test():
#     llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct',
#                     api_key='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')
    
#     llm_response = llm.invoke("What is this data about: "+ df.head().to_string())
#     print("LLM Response:", llm_response)


def run_pandasai():
    os.environ["GROQ_API_KEY"] = "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"
    os.environ["GEMINI_API_KEY"] = "AIzaSyBSFUa9mw0_rVidWyOnTkv16McZazi4rXA"
    # llm = LiteLLM(model="gemini/gemini-2.5-flash")
    llm = LiteLLM(model="groq/llama3-70b-8192")
    pai.config.set({"llm": llm})

    # Create SmartDataframe
    sdf = SmartDataframe(df)
    response = sdf.chat('what is the largest city by population ?')
    print(response)
    # response1 = sdf.ex('What is the percentage of young people in that city ?')
    print(response1)


def ask_llm(question) -> tuple[str, str]:
    # os.environ["GEMINI_API_KEY"] = "AIzaSyBSFUa9mw0_rVidWyOnTkv16McZazi4rXA"
    # llm = LiteLLM(model="gemini/gemini-2.5-flash")

    os.environ["GROQ_API_KEY"] = "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"
    llm = LiteLLM(model="groq/llama-3.3-70b-versatile")

    pai.config.set({"llm": llm,"save_charts": True, "save_charts_path": "./assets/images/","enable_cache":False})

    agent = Agent(
    dfs=dataframes,
    memory_size=10,
    description="""
    Tu es un agent d’analyse de données démographiques.
    Tu utilises Pandas pour explorer, filtrer et visualiser les données.
    Ton objectif est d’aider l’utilisateur à comprendre les tendances de population, 
    les variations régionales et les corrélations entre les indicateurs démographiques.
    
    * Tu dois toujours renvoyer tes résultats sous la forme d’un dictionnaire Python contenant
    jusqu’à trois clés possibles selon le contexte :
      - 'text' : une explication claire et concise des résultats ou des observations.
      - 'table' : un DataFrame Pandas affichant un extrait ou un résumé des données.
      - 'plot' : une image (graphe, carte, histogramme, etc.) générée avec Matplotlib ou Plotly.

    * Exemple de format de sortie :
    {
        "text": "La population a augmenté de 12% entre 2010 et 2020.",
        "table": df_resultat,
        "plot": fig
    }

    Si certaines sorties ne sont pas pertinentes pour la question, tu peux les omettre.
    Tu renvoies toujours du code Python clair et bien commenté, 
    suivi d'une explication des résultats en langage naturel.
    """
)
    
   
    print("Question:", question)
    
    # Ask the question
    response = agent.chat(question)
    print("PandasAI Response:", response)
    
    figure = px.scatter() 
    plot_path= str(response)


    return str(response), plot_path, figure



@app.callback(
    Output("user-input", "value"),
    [Input("btn1", "n_clicks"),
    Input("btn2", "n_clicks"),
    Input("btn3", "n_clicks"),
    Input("btn4", "n_clicks")],
    prevent_initial_call=True
    )
def update_input(btn1_clicks, btn2_clicks, btn3_clicks, btn4_clicks):
    triggered = ctx.triggered_id
    suggestions = {
        "btn1": "Quelle est l’évolution de la population à Nice ?",
        "btn2": "Quels sont les secteurs d’emploi les plus dynamiques ?",
        "btn3": "Montrez-moi la répartition par âge de la population",
        "btn4": "Comparez les revenus médians des différentes villes"
    }
    return suggestions.get(triggered, "")


# (Optionnel) Callback futur pour rendre la conversation interactive
@app.callback(
    [Output('conversation-section', 'style'),
    Output('conversation-section','children'),
    Output('conversation-store', 'data')],
    [Input('analyze-btn', 'n_clicks')],
    State('user-input', 'value'),
    State('conversation-store', 'data'),
    prevent_initial_call=True
)
def handle_submit(n, text, conversation_data):
    question = text
    if conversation_data is None:
        conversation_data = []
    
    if not question:
        return {'display': 'none'}, [], conversation_data
    

    assistant_reply, plot_image_path, figure = "ask_llm(question)", "./assets/images/temp_char.png", px.scatter()

    if plot_image_path:
        plot_image_path = plot_image_path.replace("\\", "/")


    print("Assistant reply:", assistant_reply)

    conversation_data.append({
    'user': question,
    'assistant': assistant_reply,
    'plot': plot_image_path,
    'plot_fig': figure
})

    conversation = []
    for message in reversed(conversation_data):
        userMessage = html.Div(
            className="user-block",
            children=[
                html.P(message['user'], className="user-message"),
                 html.Img(src="./assets/images/Sample_User_Icon.png", className="actor-icon")
            ]
        )
        assistantMessage = html.Div(
            className="assistant-block",
            children=[
                html.Div(
                    className="assistant-message",
                    children=[
                        html.Div(
                    className="assistant-message-box",
                    children=[
                        html.Img(src="./assets/images/chatbot.png", className="actor-icon"),
                        html.Span("Assistant AI CCI", className="assistant-name"),
                        html.P(message['assistant'], className="assistant-message-text"),
                        # Ajouter le plot si disponible
                        html.Img(src="./" + message['plot'], className="assistant-plot") if 'plot' in message else None,
                        dcc.Graph(figure=message['plot_fig'], style={'height':'400px'})  if 'plot_fig' in message else None
                    ]
                )
            ]
        )
    ]
)
        conversation.extend([userMessage, assistantMessage])    

    return {'display': 'block'}, conversation, conversation_data




@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == "/data":
        return data_layout
    else:
        return app_layout


@app.callback(
    Output('plot-graph', 'figure'),
    Input('conversation-store', 'data')
)
def update_graph(conversation_data):
    if conversation_data and 'plot_fig' in conversation_data[-1]:
        return conversation_data[-1]['plot_fig']
    return px.scatter() 



if __name__ == "__main__":
    app.run(debug=True)
