import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

plotly.tools.set_credentials_file(username='aruncsk', api_key='JgzgyNEmwBI5XIFZCfwF')

def scatterplot():
    N = 1000
    random_x = np.random.randn(N)
    random_y = np.random.randn(N)

    trace = go.Scatter(x=random_x, y=random_y, mode='markers')
    data = [trace]
    py.plot(data, filename='basic-scatter')

def random():
    N = 100
    random_x = np.random.randn(N)
    random_y = np.random.randn(N)

    trace = go.Scatter(x=random_x, y=random_y, mode='markers')
    data = [trace]
    py.plot(data, filename='basic-scatter')

def random500():
    N = 500
    random_x = np.random.randn(N)
    random_y = np.random.randn(N)+2

    trace = go.Scatter(
        x=random_x,
        y=random_y,
        mode='markers',
        marker = dict(
        size = 10,
        color = 'rgba(152, 0, 0, .8)',
        line = dict(
        width = 2,
        color = 'rgb(0, 0, 0)',
        )
     )
    )
    data = [trace]
    layout = dict(title='Styled Scatter',
                  yaxis=dict(zeroline=False),
                  xaxis=dict(zeroline=False)
                  )
    fig = dict(data=data, layout=layout)
    py.plot(data, filename='basic-scatter')

def csv():
    l = []
    y = []
    df = pd.read_csv("2014_usa_states.csv")
    N = 53
    c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 100, N)]

    for i in range(int(N)):
        y.append((2000 + i))
        trace0 = go.Scatter(
            x=df['Rank'],
            y=df['Population'] + (i * 1000000),
            mode='markers',
            marker=dict(size=14,
                        line=dict(width=1),
                        color=c[i],
                        opacity=0.3
                        ), name=y[i],
            text=df['State'])  # The hover text goes here...
        l.append(trace0);

    layout = go.Layout(
        title='Stats of USA States',
        hovermode='closest',
        xaxis=dict(
            title='Population',
            ticklen=5,
            zeroline=False,
            gridwidth=2,
        ),
        yaxis=dict(
            title='Rank',
            ticklen=5,
            gridwidth=2,
        ),
        showlegend=False
    )

    fig = go.Figure(data=l, layout=layout)
    py.plot(fig)

#accept user input options
io = input("1.1000: 2.100 3.500 4.csv  Enter values:")

if io == "1000":
    scatterplot()
elif io == "100":
    random()
elif io == "500":
    random500()
elif io == "csv":
    csv()
else:
    print('Execute Succes!!!')