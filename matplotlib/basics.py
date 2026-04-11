import matplotlib.pyplot as plt

plt.title("This is the figure Title")
plt.xlabel("X Axis title")
plt.ylabel("Y Axis title")
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

import matplotlib
print(matplotlib.__version__)