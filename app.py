# import
# essential imports
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

import plotly.express as px
import math
from dash import no_update

import pandas as pd
import numpy as np
import json

# this css creates columns and row layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


## Uncomment the following line for runnning in Google Colab
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

## Uncomment the following line for running in a webbrowser
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
  "Amount": [4, 1, 2, 2, 4, 5],
  "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


# layout
app.layout = html.Div(children=[
  html.H1(children='Hello Dash'),#'<h1> this is a header </h1>'
  #
  # html.Div(children='''
  #     Dash: A web application framework for Python.
  # '''),

  dcc.Graph(
    id='example-graph',
    figure=fig
  )
])


  
# run the code
# uncomment the following line to run in Google Colab
app.run_server(mode='inline', port=8030)

# uncomment the following lines to run in Browser via command line/terminal
#if __name__ == '__main__':
#  app.run_server(debug=True, host='127.0.0.1', port=8000)
