import numpy as np
import matplotlib.pyplot as plt

#Define the whole window and the plotting area
fig, ax = plt.subplots(figsize=(7, 4)) #width = 7 height = 4

ax.set(title="Title", xlabel="X", ylabel="Y") #Set the title, x and y labels for the plotting area
# ax.set_title("Title")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")

ax.grid(True, alpha=0.3) #Add a grid with transparency over the plotting area
plt.show()
