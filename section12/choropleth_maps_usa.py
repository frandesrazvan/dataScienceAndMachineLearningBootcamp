import chart_studio.plotly as cspy
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

'''
data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Jet',  # Portland, Greens
            text=['Arizona', 'text 2', 'text 3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})

layout = dict(geo={'scope': 'usa'})

choromap = go.Figure(data=[data], layout=layout)

plot(choromap, filename='choropleth.html', auto_open=True)
'''

df = pd.read_csv('2011_US_AGRI_Exports')
data = dict(type='choropleth',
            colorscale='ylorrd',
            locations=df['code'],
            locationmode = 'USA-states',
            z= df['total exports'],
            text=df['text'],
            marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
            colorbar={'title': 'Millions USD'})

layout = dict(title='2011 USD Agriculture Exports by State',
              geo=dict(scope='usa', showlakes=True, lakecolor='rgb(85,173,240)'))

choromap = go.Figure(data=[data], layout=layout)

plot(choromap, filename='choropleth_usa.html', auto_open=True)
