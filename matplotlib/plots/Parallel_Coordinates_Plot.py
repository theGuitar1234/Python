import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,1,5,3]

fig,(ax1,ax2) = plt.subplots(1, 2, sharey=False)

ax1.plot(x, y)
ax2.plot(x, y)
ax1.set_xlim([ x[0],x[2]])
ax2.set_xlim([ x[2],x[4]])

plt.subplots_adjust(wspace=0)
plt.savefig("img/prlll_crdnts_plt.png")
plt.show()