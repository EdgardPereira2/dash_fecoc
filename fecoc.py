import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

df_agrupado = pd.read_parquet('df_agrupado.parquet')
# df_general = pd.read_parquet('df_general.parquet')

def custom_hovertemplate_sunburst(trace):
    labels = {
        'Categoría': 'Categoría',
        'Altitud [m.s.n.m]': 'Altitud [m.s.n.m]',
        'Cilindrada': 'Cilindrada [cc]',
        'Modelo': 'Modelo'
    }
    custom_data = []
    for i in range(len(trace.ids)):
        level = trace.ids[i].count('/')
        label_key = list(labels.keys())[level]
        tooltip_text = f"{labels[label_key]}: {trace.labels[i]}<br>#Vehículos: {trace.values[i]}"
        custom_data.append(tooltip_text)
    trace.customdata = custom_data
    trace.hovertemplate = '%{customdata}<extra></extra>'

def sunburst(df_agrupado, path):
    fig = px.sunburst(df_agrupado, path=path,
                      values=None,
                      color_discrete_sequence = ['#0000FF'])
    fig.for_each_trace(lambda trace: custom_hovertemplate_sunburst(trace))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(maxdepth=3)
    # fig.update_traces(textinfo='label+value')
    return fig


def custom_hovertemplate_sunburst2(trace):
    labels = {
        'Altitud [m.s.n.m]':'Altitud [m.s.n.m]',
        'Tipo de alimentación': 'Tipo de alimentación',
        'Transmisión': 'Transmisión',
        'Cilindrada': 'Cilindrada [cc]',
        'Modelo':'Modelo',
        'Kilometraje': 'Kilometraje'
    }
    custom_data = []
    for i in range(len(trace.ids)):
        level = trace.ids[i].count('/')
        label_key = list(labels.keys())[level]
        tooltip_text = f"{labels[label_key]}: {trace.labels[i]}<br>#Vehículos: {trace.values[i]}"
        custom_data.append(tooltip_text)
    trace.customdata = custom_data
    trace.hovertemplate = '%{customdata}<extra></extra>'
    
def sunburst2(df_agrupado, path):
    #Filtrar df
    df_agrupado = df_agrupado.replace('Semiautomática','Automática')
    df_agrupado = df_agrupado.replace('--',np.nan)
    df_agrupado = df_agrupado.fillna(0)
    fig = px.sunburst(df_agrupado, path=path,
                      values=None,
                      color_discrete_sequence = ['#0000FF'])
    fig.for_each_trace(lambda trace: custom_hovertemplate_sunburst2(trace))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(maxdepth=4)
    # fig.update_traces(textinfo='label+value')
    return fig

def custom_hovertemplate_sunburst3(trace):
    labels = {
        'Altitud [m.s.n.m]': 'Altitud [m.s.n.m]',
        'Norma de Emisión': 'Norma de Emisión',
        'Cilindrada':'Cilindrada [cc]',
        'Modelo':'Modelo',
        'Capacidad':'Capacidad [kg]'
    }
    custom_data = []
    for i in range(len(trace.ids)):
        level = trace.ids[i].count('/')
        label_key = list(labels.keys())[level]
        tooltip_text = f"{labels[label_key]}: {trace.labels[i]}<br>#Vehículos: {trace.values[i]}"
        custom_data.append(tooltip_text)
    trace.customdata = custom_data
    trace.hovertemplate = '%{customdata}<extra></extra>'
    
def sunburst3(df_agrupado, path):
    #Filtrar df
    # Cambiar los valores en la columna 'Norma de Emisión'
    df_agrupado['Norma de emisión'] = df_agrupado['Norma de emisión'].replace({
        'Epa_98': 'EPA 98',
        'Euro_III': 'Euro III',
        'Euro_IV': 'Euro IV',
        'Euro_V': 'Euro V',
        'Euro_VI': 'Euro VI',
        'pre_Euro': 'pre Euro',
        'Euro_II': 'Euro II'
    })
    df_agrupado = df_agrupado.replace('--',np.nan)
    df_agrupado = df_agrupado.fillna(0)
    fig = px.sunburst(df_agrupado, path=path,
                      values=None,
                      color_discrete_sequence = ['#0000FF'])
    fig.for_each_trace(lambda trace: custom_hovertemplate_sunburst3(trace))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(maxdepth=4)
    # fig.update_traces(textinfo='label+value')
    return fig

def custom_hovertemplate_sunburst4(trace):
    labels = {
        'Altitud [m.s.n.m]':'Altitud [m.s.n.m]',
        'Tipo de inyección': 'Tipo de inyección',
        'Transmisión': 'Transmisión',
        'Cilindrada': 'Cilindrada [cc]',
        'Modelo':'Modelo',
        'Kilometraje': 'Kilometraje'
    }
    custom_data = []
    for i in range(len(trace.ids)):
        level = trace.ids[i].count('/')
        label_key = list(labels.keys())[level]
        tooltip_text = f"{labels[label_key]}: {trace.labels[i]}<br>#Vehículos: {trace.values[i]}"
        custom_data.append(tooltip_text)
    trace.customdata = custom_data
    trace.hovertemplate = '%{customdata}<extra></extra>'
    
def sunburst4(df_agrupado, path):
    #Filtrar df
    df_agrupado = df_agrupado.replace('--',np.nan)
    df_agrupado = df_agrupado.fillna(0)
    fig = px.sunburst(df_agrupado, path=path,
                      values=None,
                      color_discrete_sequence = ['#0000FF'])
    fig.for_each_trace(lambda trace: custom_hovertemplate_sunburst4(trace))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(maxdepth=4)
    # fig.update_traces(textinfo='label+value')
    return fig


def treemap(df_agrupado, contaminante, profundidad):
    fig = px.treemap(df_agrupado, path=[px.Constant(f'FECOC {contaminante}'),'Categoría','Altitud [m.s.n.m]','Cilindrada',contaminante],
                    color=contaminante, color_continuous_scale='aggrnyl')
    #Actualizar el color de la raíz y el número máximo de niveles que se muestran
    fig.update_traces(root_color="black", maxdepth=profundidad)
    #Actualizar la plantilla de la figura
    fig.for_each_trace(lambda trace: custom_hovertemplate(trace, contaminante))
    #Actualizar el diseño de la figura
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return fig

def custom_hovertemplate(trace, cont):
    #Diccionario para nombre de contaminante
    dict_cont = {'Rend. comb [km/gal]':'Rendimiento de combustible',
                    'FE CO2 [g/km]':'CO2 [g/km]',
                    'FE CO [g/km]':'CO [g/km]',
                    'FE NOx [g/km]':'NOx [g/km]',
                    'FE NO [g/km]':'NO [g/km]',
                    'FE NO2 [g/km]':'NO2 [g/km]',
                    'FE HC [g/km]':'HC [g/km]',
                    'FE PM [mg/km]':'PM [mg/km]',
                    'FE PN [# x 10^12/km]':'PN [# x 10^12/km]',
                    'Consumo [L/100km]':'Consumo [L/100km]',
                    'Consumo [L/100km-Ton]':'Consumo [L/100km-Ton]',
                    'CO2 [g/km-Ton]':'CO2 [g/km-Ton]'
                    }
    #Labels que se cambiaran cuando se acceda a cada nivel
    labels = {
        'FECOC': 'Categoría',
        'Categoría': 'Categoría',
        'Altitud [m.s.n.m]': 'Altitud [msnm]',
        'Cilindrada': 'Cilindrada [cc]',
        cont : dict_cont[cont]
    }
    custom_data = []
    for i in range(len(trace.ids)):
        #Determinar el nivel del noto actual contando el número de / que indica el nivel
        level = trace.ids[i].count('/')
        #Obtener el nombre de la etiqueta para el nivel actual
        label_key = list(labels.keys())[level-1]
        #Agregar el texto personalizado
        custom_data.append(f"{labels[label_key]}: {trace.labels[i]}<br>#Vehículos: {trace.values[i]}")
    trace.customdata = custom_data
    trace.hovertemplate = '%{customdata}<extra></extra>'
    
lis = ['Rend. comb [km/gal]','FE CO2 [g/km]','FE CO [g/km]','FE NOx [g/km]'
       ,'FE NO [g/km]','FE NO2 [g/km]','FE HC [g/km]','FE PM [mg/km]'
       ,'FE PN [# x 10^12/km]','CO2 [g/km-Ton]','Consumo [L/100km]','Consumo [L/100km-Ton]']


lista2 = ['Motocicletas','Vehículos livianos','AB','C2G','TC','C2P']
app = dash.Dash(__name__)
server = app.server


app.layout = html.Div([
    html.Div('FECOC+', style={'textAlign': 'center', 'fontSize': 34, 'padding': '10px',
                              'font-family': 'Arial', 'border': '2px solid black',
                              'fontWeight': 'bold','backgroundColor': 'lightgreen'}),
    html.Div([
        html.Img(src='/assets/logo_upme.png', style={'height':'80px', 'padding-left':'10px', 'display': 'inline-block'}),
        html.Img(src='/assets/facultad-ingenieria.png', style={'height':'80px', 'padding-left':'10px', 'display': 'inline-block'}),
        html.Img(src='/assets/logo_gimell.png', style={'height':'80px', 'padding-left':'10px', 'display': 'inline-block'}),
    ], style={'textAlign': 'center'}),
    html.Div('Vehículos medidos', style={'textAlign': 'center', 'fontSize': 30, 'padding': '10px',
                                           'font-family': 'Arial','border': '2px solid black',
                                           'backgroundColor': 'lightgreen'}),
    html.H3('Seleccione categoría vehícular', style={'padding': '10px', 'textAlign': 'center'}),
    html.Div([
        # dcc.Graph(figure=sunburst(df_agrupado, ['Categoría', 'Altitud [m.s.n.m]','Cilindrada','Modelo']), style={'display': 'inline-block', 'width': '50%'}),
            dcc.Dropdown(
                id='my-dropdown2',
                options=[{'label': i, 'value': i} for i in lista2],
                value=lista2[0],
                className='Select--single',
                style={'width': '100%'}
            ),
            dcc.Graph(id='other-sunburst-graph', style={'width': '100%'})
    ], style={'border': '2px solid black'}),
    html.Div('Factores de emisión', style={'textAlign': 'center', 'fontSize': 30, 'padding': '10px',
                                           'font-family': 'Arial','border': '2px solid black',
                                           'backgroundColor': 'lightgreen'}),
    html.H3('Seleccione parámetro de intéres', style={'padding': '10px'}),
    dcc.Dropdown(
        id='my-dropdown',
        options=[{'label': i, 'value': i} for i in lis],
        value=lis[0],
        className='Select--single'
    ),
    dcc.Graph(className='my-graph', id='my-graph', style={'border': '2px solid black'}),
    html.H3('Seleccione categoría vehícular', style={'padding': '10px'}),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in df_agrupado['Categoría'].unique()],
        value=df_agrupado['Categoría'].unique()[0],
        className='Select--single'
    ),
    dcc.Graph(className='my-graph', id='my-second-graph', style={'border': '2px solid black'}),
    # html.H3('Diagrama de boxplot por altitud', style={'padding': '10px'}),
    html.Div('Comparativo', style={'textAlign': 'center', 'fontSize': 30, 'padding': '10px',
                                        'font-family': 'Arial','border': '2px solid black',
                                        'backgroundColor': 'lightgreen'}),
    html.Div([
        html.Div([
            html.H3('Seleccione contaminante', style={'padding': '10px'}),
            dcc.Dropdown(
                id='my-dropdown4',
                options=[{'label': i, 'value': i} for i in lis],
                value=lis[0],
                className='Select--single'
            )
        ], style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
            html.H3('Seleccione categoría vehícular', style={'padding': '10px'}),
            dcc.Dropdown(
                id='category-dropdown4',
                options=[{'label': i, 'value': i} for i in df_agrupado['Categoría'].unique()],
                value=df_agrupado['Categoría'].unique()[0],
                className='Select--single'
            )
        ], style={'width': '50%', 'display': 'inline-block'}),
    ]),
    html.Div([
        html.Div([
            html.H3('Cajas y bigotes por altitud', style={'padding': '10px'}),
            dcc.Graph(className='my-graph', id='my-boxplot'),
        ], style={'width': '50%'}),
        html.Div([
            html.H3('Cajas y bigotes por norma de emisión', style={'padding': '10px'}),
            dcc.Graph(className='my-graph', id='my-boxplot2'),
        ], style={'width': '50%'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'border': '2px solid black'})
])

#CALLBACK PARA SUNBURST QUE SE ACTUALIZA CON CATEGORIAS
@app.callback(
    Output('other-sunburst-graph', 'figure'),
    [Input('my-dropdown2', 'value')]
)
def update_other_sunburst(selected_value):
    # Genera el segundo gráfico sunburst
    if selected_value == 'Motocicletas':
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_value]
        path = ['Altitud [m.s.n.m]','Tipo de alimentación', 'Transmisión','Cilindrada','Modelo','Kilometraje']
        updated_figure = sunburst2(df_filtered, path)
    elif selected_value == 'AB' or selected_value == 'C2G' or selected_value == 'TC' or selected_value == 'C2P':
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_value]
        path = ['Altitud [m.s.n.m]','Norma de emisión','Cilindrada','Modelo','Capacidad']
        updated_figure = sunburst3(df_filtered, path)
    else:
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_value]
        path = ['Altitud [m.s.n.m]','Tipo de inyección','Transmisión','Cilindrada','Modelo','Kilometraje']
        updated_figure = sunburst4(df_filtered, path)
    return updated_figure


@app.callback(
    Output('my-graph', 'figure'),
    Input('my-dropdown', 'value')
)
def update_graph(selected_value):
    df_agrupado2 = df_agrupado.copy()
    df_agrupado2 = df_agrupado2.dropna(subset=[selected_value])
    if selected_value in ['CO2 [g/km-Ton]','Consumo [L/100km-Ton]']:
        df_agrupado3 = df_agrupado2.copy()
        df_agrupado3 = df_agrupado3.loc[df_agrupado2['Categoría'] != 'AB']
        fig = treemap(df_agrupado3, selected_value, 4)
    else:
        fig = treemap(df_agrupado2, selected_value, 4)
    return fig

@app.callback(
    Output('my-second-graph', 'figure'),
    Input('my-dropdown', 'value'),
    Input('category-dropdown', 'value')
)
def update_second_graph(selected_value, selected_category):
    df_agrupado2 = df_agrupado.copy()
    df_agrupado2 = df_agrupado2.dropna(subset=[selected_value])
    df_filtered = df_agrupado2[df_agrupado2['Categoría'] == selected_category]
    second_fig = treemap(df_filtered, selected_value, 4)
    return second_fig

import plotly.graph_objects as go

@app.callback(
    Output('my-boxplot', 'figure'),
    [Input('category-dropdown4', 'value'),
    Input('my-dropdown4', 'value')]
)
def update_boxplot(selected_category, selected_contaminant):
    df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_category]
    boxplot_fig = go.Figure()

    for altitud in df_filtered['Altitud [m.s.n.m]'].unique():
        y_data = df_filtered[df_filtered['Altitud [m.s.n.m]'] == altitud][selected_contaminant]
        boxplot_fig.add_trace(go.Box(
            y=y_data,
            name=f"{altitud}",
            whiskerwidth=0.4,
            line_width=2
        ))

    boxplot_fig.update_layout(
        title=f'{selected_contaminant} por altitud para {selected_category}',
        xaxis_title='Altitud [m.s.n.m]',
        yaxis_title=selected_contaminant,
        xaxis=dict(gridcolor='lightgray', linecolor='black', mirror=True, ticks='outside'),
        yaxis=dict(
            autorange=True,
            showgrid=True,
            zeroline=True,
            gridcolor='lightgray',
            gridwidth=1,
            zerolinecolor='rgb(255, 255, 255)',
            zerolinewidth=2,
            linecolor='black',
            mirror=True,
            ticks='outside'
        ),
        font=dict(family='Arial', size=12, color='black'),
        legend=dict(
            orientation="v",
            font=dict(family='Arial', size=12, color='black'),
            bgcolor="white",
            bordercolor="Black",
            borderwidth=1
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=50, r=50, t=50, b=50),
        autosize=False,
        showlegend=True
    )

    return boxplot_fig

@app.callback(
    Output('my-boxplot2', 'figure'),
    [Input('category-dropdown4', 'value'),
    Input('my-dropdown4', 'value')]
)
def update_boxplot2(selected_category, selected_contaminant):
    if selected_category == 'Motocicletas':
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_category]
        boxplot_fig = go.Figure()

        nombres = {'Carburada':'Carburada',
                'Inyección':'Inyección',      
                }
        
        for altitud in nombres.keys():
            y_data = df_filtered[df_filtered['Tipo de alimentación'] == altitud][selected_contaminant]
            boxplot_fig.add_trace(go.Box(
                y=y_data,
                name=f"{nombres[altitud]}",
                whiskerwidth=0.4,
                line_width=2
            ))

        boxplot_fig.update_layout(
            title=f'{selected_contaminant} por Tipo de Alimentación para {selected_category}',
            xaxis_title='Tipo de alimentación',
            yaxis_title=selected_contaminant,
            xaxis=dict(gridcolor='lightgray', linecolor='black', mirror=True, ticks='outside'),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                gridcolor='lightgray',
                gridwidth=1,
                zerolinecolor='rgb(255, 255, 255)',
                zerolinewidth=2,
                linecolor='black',
                mirror=True,
                ticks='outside'
            ),
            font=dict(family='Arial', size=12, color='black'),
            legend=dict(
                orientation="v",
                font=dict(family='Arial', size=12, color='black'),
                bgcolor="white",
                bordercolor="Black",
                borderwidth=1
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=50, t=50, b=50),
            autosize=False,
            showlegend=True
        )
    elif selected_category == 'AB' or selected_category == 'C2G' or selected_category == 'TC' or selected_category == 'C2P':
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_category]
        boxplot_fig = go.Figure()

        nombres = {'Epa_98':'EPA 98',
                'pre_Euro':'pre Euro',
                'Euro_II':'Euro II',
                'Euro_III':'Euro III',
                'Euro_IV':'Euro IV',
                'Euro_V':'Euro V',
                'Euro_VI':'Euro VI',}
        
        for altitud in nombres.keys():
            y_data = df_filtered[df_filtered['Norma de emisión'] == altitud][selected_contaminant]
            boxplot_fig.add_trace(go.Box(
                y=y_data,
                name=f"{nombres[altitud]}",
                whiskerwidth=0.4,
                line_width=2
            ))

        boxplot_fig.update_layout(
            title=f'{selected_contaminant} por Norma de Emisión para {selected_category}',
            xaxis_title='Norma de Emisión',
            yaxis_title=selected_contaminant,
            xaxis=dict(gridcolor='lightgray', linecolor='black', mirror=True, ticks='outside'),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                gridcolor='lightgray',
                gridwidth=1,
                zerolinecolor='rgb(255, 255, 255)',
                zerolinewidth=2,
                linecolor='black',
                mirror=True,
                ticks='outside'
            ),
            font=dict(family='Arial', size=12, color='black'),
            legend=dict(
                orientation="v",
                font=dict(family='Arial', size=12, color='black'),
                bgcolor="white",
                bordercolor="Black",
                borderwidth=1
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=50, t=50, b=50),
            autosize=False,
            showlegend=True
        )
    else:
        df_filtered = df_agrupado[df_agrupado['Categoría'] == selected_category]
        boxplot_fig = go.Figure()

        nombres = {'Multipunto':'Multipunto',
                'Directa':'Directa'}
        
        for altitud in nombres.keys():
            y_data = df_filtered[df_filtered['Tipo de inyección'] == altitud][selected_contaminant]
            boxplot_fig.add_trace(go.Box(
                y=y_data,
                name=f"{nombres[altitud]}",
                whiskerwidth=0.4,
                line_width=2
            ))

        boxplot_fig.update_layout(
            title=f'{selected_contaminant} por Tipo de inyección para {selected_category}',
            xaxis_title='Tipo de inyección',
            yaxis_title=selected_contaminant,
            xaxis=dict(gridcolor='lightgray', linecolor='black', mirror=True, ticks='outside'),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                gridcolor='lightgray',
                gridwidth=1,
                zerolinecolor='rgb(255, 255, 255)',
                zerolinewidth=2,
                linecolor='black',
                mirror=True,
                ticks='outside'
            ),
            font=dict(family='Arial', size=12, color='black'),
            legend=dict(
                orientation="v",
                font=dict(family='Arial', size=12, color='black'),
                bgcolor="white",
                bordercolor="Black",
                borderwidth=1
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=50, t=50, b=50),
            autosize=False,
            showlegend=True
        )
    
    return boxplot_fig

# @app.callback(
#     Output("download-dataframe-excel", "data"),
#     Input("btn_excel", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     return dcc.send_data_frame(df.to_excel, "CONSOLIDADO.xlsx")

if __name__ == '__main__':
    app.run_server(debug=True)