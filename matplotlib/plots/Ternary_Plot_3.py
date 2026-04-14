import plotly.figure_factory as ff
import numpy as np

test_data = np.array([[0, 0, 1, 0],
                      [0.25, 0.25, 0.5, 0],
                      [0.25, 0.25, 0.5, 0],
                      [0.25, 0.25, 0.5, 1],
                      [0.25, 0.5, 0.25, 1],
                      [0, 1, 0, 1]])

a = test_data[:, 0]
b = test_data[:, 1]
c = test_data[:, 2]

v = test_data[:, -1]

# fig = ff.create_ternary_contour(
#     np.array([a, b, c]), v,
#     pole_labels=['A', 'B', 'C'],
# )

# fig = ff.create_ternary_contour(
#     np.array([a, b, c]), v,
#     pole_labels=['A', 'B', 'C'],
#     ncontours=20,
#     colorscale='Greens',
#     showscale=True,
#     title='Ternary Contour Plot'
# )

fig = ff.create_ternary_contour(
    np.array([a, b, c]), v,
    pole_labels=['A', 'B', 'C'],
    ncontours=20,
    colorscale='Greens',
    showscale=True,
    title='Ternary Contour Plot',
    coloring='lines',
    showmarkers=True
)

fig.show()