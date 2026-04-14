import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

categories = ['SprintSpeed','Agility','Stamina','Aggression','Positioning','Vision']
data1 = np.random.randn(6)
data2 = np.random.randn(6)
avg1 = np.mean(data1)
avg2 = np.mean(data2)
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
  r=data1,
  theta=categories,
  fill='toself',
  name=f'Contender Overall {avg1:.2f}',
  showlegend=True))
fig.add_trace(go.Scatterpolar(
  r=data2,
  theta=categories,
  fill='toself',
  name=f'Contender Overall {avg2:.2f}',
  showlegend=True))
fig.update_layout(
  template='plotly_dark'
)
fig.show()