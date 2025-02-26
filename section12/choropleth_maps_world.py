import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

df = pd.read_csv('2014_World_GDP')

data = dict(type='choropleth',
            colorscale='greens',
            locations=df['CODE'],
            locationmode='ISO-3',
            z=df['GDP (BILLIONS)'],
            text=df['COUNTRY'],
            marker=dict(line=dict(color='rgb(0,0,0)', width=2)),
            colorbar={'title': 'BILLIONS GDP'})

layout = dict(title='2014 World GDP by Country',
              geo=dict(scope='world', showframe=False, projection={'type': 'mercator'}))  # 'type': 'natural earth'

choromap = go.Figure(data=[data], layout=layout)

plot(choromap, filename='choropleth_world.html', auto_open=True)
