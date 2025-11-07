from plotly import express as px
import pandasai as pai
import plotly

@pai.skill
def generate_plot(dataf, plot_type='bar', x_col=None, y_col=None)-> 'plotly.graph_objs._figure.Figure':
    """
    Generate a Plotly figure based on the type requested.
    
    Parameters:
    - dataf: pandas DataFrame
    - plot_type: str, one of 'bar', 'line', 'scatter', 'histogram', 'box'
    - x_col: column name for x-axis
    - y_col: column name for y-axis (not needed for histogram)
    
    Returns:
    - Plotly Figure
    """
    if plot_type == 'bar':
        fig = px.bar(dataf, x=x_col, y=y_col)
    elif plot_type == 'line':
        fig = px.line(dataf, x=x_col, y=y_col)
    elif plot_type == 'scatter':
        fig = px.scatter(dataf, x=x_col, y=y_col)
    elif plot_type == 'histogram':
        fig = px.histogram(dataf, x=x_col)
    elif plot_type == 'box':
        fig = px.box(dataf, x=x_col, y=y_col)
    else:
        raise ValueError(f"Unknown plot_type: {plot_type}")
    
    fig.update_layout(title=f"{plot_type.capitalize()} plot of {y_col} vs {x_col}")
    return fig



@pai.skill
def generate_cross_filter(df, x_col, y_col, selectedpoints, selectedpoints_local) -> 'plotly.graph_objs._figure.Figure':
    """
    Generate a scatter plot with cross-filtering capabilities.
    Parameters:
    - df: pandas DataFrame
    - x_col: column name for x-axis
    - y_col: column name for y-axis
    - selectedpoints: list of indices of selected points
    - selectedpoints_local: dict with 'range' key for local selection bounds
    Returns: - Plotly Figure
    """
    if selectedpoints_local and selectedpoints_local["range"]:
        ranges = selectedpoints_local["range"]
        selection_bounds = {
            "x0": ranges["x"][0],
            "x1": ranges["x"][1],
            "y0": ranges["y"][0],
            "y1": ranges["y"][1],
        }
    else:
        selection_bounds = {
            "x0": np.min(df[x_col]),
            "x1": np.max(df[x_col]),
            "y0": np.min(df[y_col]),
            "y1": np.max(df[y_col]),
        }

    # set which points are selected with the `selectedpoints` property
    # and style those points with the `selected` and `unselected`
    # attribute. see
    # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43e21
    # for an explanation
    fig = px.scatter(df, x=df[x_col], y=df[y_col], text=df.index)

    fig.update_traces(
        selectedpoints=selectedpoints,
        customdata=df.index,
        mode="markers+text",
        marker={"color": "rgba(0, 116, 217, 0.7)", "size": 20},
        unselected={
            "marker": {"opacity": 0.3},
            "textfont": {"color": "rgba(0, 0, 0, 0)"},
        },
    )

    fig.update_layout(
        margin={"l": 20, "r": 0, "b": 15, "t": 5},
        dragmode="select",
        hovermode=False,
        newselection_mode="gradual",
    )

    fig.add_shape(
        dict(
            {"type": "rect", "line": {"width": 1, "dash": "dot", "color": "darkgrey"}},
            **selection_bounds
        )
    )
    return fig
