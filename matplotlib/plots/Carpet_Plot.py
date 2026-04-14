import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a=[1, 2, 3, 4, 5, 6],
    b=[6, 5, 4, 3, 2, 1],
    y=[1, 2, 3, 4, 5, 6],

    aaxis=dict(
        tickprefix='F = ',
        ticksuffix='N',
        smoothing=0.2,
        minorgridcount=10,
    ),
    baxis=dict(
        tickprefix='P = ',
        ticksuffix='pa',
        smoothing=0.4,
        minorgridcount=9,
    )
))

fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(
        showgrid=False,
        showticklabels=False
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False
    )
)

fig.show()