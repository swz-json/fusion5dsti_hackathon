from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import json
import base64
import time

# --- 1. DATA SETUP (Mocking the CSV Load) ---
# Replace this synthetic data with your actual CSV loading path if running locally.
# df = pd.read_csv('/home/admin1/fusion5dsti/data/housing_and_employment_by_department(in).csv')
data = {
    'Department': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Housing_Units': [12000, 8000, 15000, 10000, 9000, 14000, 11000, 7000, 16000, 13000],
    'Employment_Rate': [0.65, 0.72, 0.58, 0.69, 0.60, 0.75, 0.62, 0.78, 0.55, 0.70],
    'Average_Income': [35000, 42000, 31000, 45000, 38000, 48000, 33000, 50000, 30000, 44000]
}
df = pd.DataFrame(data)

# Convert DataFrame to a string representation for the LLM to understand the schema
DF_SCHEMA = df.head(3).to_markdown(index=False)
ALL_COLUMNS = ", ".join(df.columns)

# --- 2. DASH APPLICATION SETUP ---
app = Dash(__name__)

# LLM API configuration (Placeholders for Canvas environment variables)
API_KEY = ""
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key="

# --- 3. JAVASCRIPT FOR API CALL (Integrated into the App) ---
# This script handles the asynchronous LLM call from the client side.
app.clientside_callback(
    """
    function generatePlotConfig(prompt, schema, n_clicks, apiKey, apiUrl) {
        if (n_clicks === 0 || !prompt) {
            return [{}, "Awaiting query..."];
        }
        
        // Set status to loading
        let initialConfig = {};
        
        // Use exponential backoff for retries
        const MAX_RETRIES = 5;
        const INITIAL_DELAY = 1000;
        
        // UPDATED SYSTEM INSTRUCTION to mimic SmartDataFrame's output extraction
        // We instruct the LLM to ONLY return the raw JSON object, without using
        // the API's structured generation schema.
        const systemInstruction = `You are a data visualization expert. Your task is to analyze the user's request and the provided Pandas DataFrame schema and generate a RAW JSON object with arguments suitable for a standard Plotly Express function (like px.bar, px.scatter, px.histogram).
The columns available in the DataFrame are: ${schema}.
The JSON object MUST contain the following fields: 'plot_type', 'x_column', 'y_column', 'title', and 'color_column'.
'color_column' should be null if not explicitly requested by the user.
'y_column' must be a numeric column from the DataFrame.
The 'plot_type' must be a valid plotly.express function name like 'bar', 'scatter', 'box', or 'histogram'.
DO NOT include any text, headers, or markdown formatting (like \`\`\`json) outside of the raw JSON object.`;

        const userQuery = `Generate the RAW JSON configuration object for a Plotly Express visualization based on this user request: "${prompt}".`;

        const payload = {
            contents: [{ parts: [{ text: userQuery }] }],
            systemInstruction: { parts: [{ text: systemInstruction }] },
            // Removed responseSchema to align with user request
        };

        const executeFetch = async (attempt) => {
            const delay = INITIAL_DELAY * Math.pow(2, attempt);

            try {
                const response = await fetch(apiUrl + apiKey, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.status === 429 && attempt < MAX_RETRIES - 1) {
                    await new Promise(resolve => setTimeout(resolve, delay));
                    return executeFetch(attempt + 1); // Retry
                } else if (!response.ok) {
                    throw new Error(`API request failed with status: ${response.status}`);
                }

                const result = await response.json();
                const jsonText = result?.candidates?.[0]?.content?.parts?.[0]?.text;

                if (!jsonText) {
                    throw new Error("LLM response was empty or malformed.");
                }

                // The LLM returns a JSON string, which must be parsed
                const config = JSON.parse(jsonText);
                
                // Return the config and a success message
                return [config, "Plot configuration generated successfully. Generating chart..."];

            } catch (error) {
                console.error("Error in LLM call or processing:", error);
                if (attempt < MAX_RETRIES - 1) {
                    await new Promise(resolve => setTimeout(resolve, delay));
                    return executeFetch(attempt + 1); // Retry on generic error
                }
                // Final failure: return an error message
                return [{}, `Error: Could not generate plot configuration. ${error.message}`];
            }
        };

        return executeFetch(0);
    }
    """,
    # The output is the plot config (hidden div) and the status message (visible div)
    Output('llm-config-store', 'data'),
    Output('status-message', 'children'),
    # The inputs are the user prompt and the button click
    Input('prompt-input', 'value'),
    Input('submit-button', 'n_clicks'),
    State('api-key-store', 'data'), # State holds the API Key and URL (empty string for Canvas)
    State('api-url-store', 'data'),
    prevent_initial_call=True
)

# --- 4. PYTHON CALLBACK FOR PLOT GENERATION ---
@callback(
    Output('controls-and-graph', 'figure'),
    Input('llm-config-store', 'data'),
    prevent_initial_call=True
)
def update_graph(plot_config):
    """
    Takes the structured plot configuration generated by the LLM and creates the Plotly figure.
    """
    if not plot_config or not plot_config.get('plot_type'):
        # Return an empty figure if no valid config is present
        return {}

    plot_type = plot_config['plot_type']
    x_col = plot_config['x_column']
    y_col = plot_config['y_column']
    color_col = plot_config['color_column']
    title = plot_config['title']

    # Default function arguments
    plot_args = {
        'data_frame': df,
        'x': x_col,
        'y': y_col,
        'title': title
    }
    
    # Add color/grouping if provided
    if color_col:
        plot_args['color'] = color_col
        plot_args['barmode'] = 'group' # Default to group mode for bar charts

    try:
        # Dynamically call the correct plotly.express function
        if hasattr(px, plot_type):
            plot_func = getattr(px, plot_type)
            fig = plot_func(**plot_args)
            
            # Update layout for aesthetics
            fig.update_layout(
                margin={"r":10,"t":50,"l":10,"b":10}, 
                plot_bgcolor='white',
                paper_bgcolor='#f7f7f7',
                font=dict(family="Inter", size=12, color="#333"),
                title_font_size=20
            )
            return fig
        else:
            print(f"Plotly Express function '{plot_type}' not found.")
            return {}
            
    except Exception as e:
        print(f"Error generating plot with Plotly Express: {e}")
        return {}

# --- 5. APPLICATION LAYOUT ---

app.layout = html.Div(className="min-h-screen bg-gray-100 p-4 sm:p-8 font-['Inter']", children=[
    # Hidden components for state and API config
    dcc.Store(id='llm-config-store', data={}),
    dcc.Store(id='api-key-store', data=API_KEY),
    dcc.Store(id='api-url-store', data=API_URL),

    # Main Card Container
    html.Div(className="max-w-6xl mx-auto bg-white rounded-xl shadow-2xl p-6 md:p-10", children=[
        
        # Header
        html.H1("LLM-Powered Data Visualization", className="text-3xl font-extrabold text-blue-800 mb-2 border-b-2 border-blue-100 pb-2"),
        html.P(f"Current DataFrame Columns: {ALL_COLUMNS}", className="text-sm text-gray-500 mb-6"),

        # User Input Section
        html.Div(className="flex flex-col sm:flex-row gap-3 mb-6", children=[
            dcc.Input(
                id='prompt-input',
                type='text',
                placeholder='E.g., "Show a bar chart of the average income by region"',
                className="flex-grow p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-150"
            ),
            html.Button(
                'Generate Plot',
                id='submit-button',
                n_clicks=0,
                className="w-full sm:w-auto px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition duration-150"
            )
        ]),

        # Status Message
        html.Div(
            id='status-message',
            children="Enter a prompt above to generate a chart.",
            className="text-center p-3 mb-6 rounded-lg bg-yellow-50 text-yellow-800 font-medium"
        ),

        # Data Table Preview (for reference)
        html.H2("Data Preview", className="text-xl font-bold text-gray-700 mb-3"),
        html.Div(
            className="overflow-x-auto mb-8",
            children=[
                html.Table(
                    className="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg",
                    children=[
                        html.Thead(
                            className="bg-gray-50",
                            children=[html.Tr([html.Th(col, className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider") for col in df.columns])]
                        ),
                        html.Tbody(
                            className="bg-white divide-y divide-gray-200",
                            children=[
                                html.Tr([html.Td(row[col], className="px-6 py-4 whitespace-nowrap text-sm text-gray-900") for col in df.columns])
                                for index, row in df.head(5).iterrows()
                            ]
                        )
                    ]
                )
            ]
        ),


        # Graph Output
        html.H2("Generated Visualization", className="text-xl font-bold text-gray-700 mb-3"),
        html.Div(
            className="bg-white border border-gray-200 rounded-lg shadow-inner p-4",
            children=[
                dcc.Graph(
                    id='controls-and-graph',
                    figure={},
                    config={'displayModeBar': False}
                )
            ]
        ),
    ]),
])

if __name__ == '__main__':
    # NOTE: In the actual canvas environment, the app runs via a startup script.
    # This block is for local testing.
    app.run(debug=True)