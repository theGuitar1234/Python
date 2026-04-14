import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y1=[2,4,1,5,3,4,2,5,2]
y2=[3,4,3,5,2,6,4,2,3]

fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8) = plt.subplots(1, 8, sharey=False)
ax = (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8)

for i in range(8):
    ax[i].plot(x,y1,'g-.',x,y2,'r--')
    ax[i].set_xlim([ x[i],x[i+1]])

plt.subplots_adjust(wspace=0)
plt.savefig("img/prlll_crdnts_plt.png")
plt.show()