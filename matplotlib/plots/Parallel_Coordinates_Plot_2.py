import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
data = [x,x*2,x*x,np.sqrt(x),-x*x,np.sin(x),np.cos(x)]
print(data)

fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4, sharey=False)
ax = (ax1,ax2,ax3,ax4)

for i in range(4):
    for j in range(len(data)):
        ax[i].plot(data[0],data[j])
    ax[i].set_xlim([x[i],x[i+1]])

plt.subplots_adjust(wspace=0)
plt.savefig("img/prlll_crdnts_plt.png")
plt.show()