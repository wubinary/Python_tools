import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time,random

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.set_xlim(0,1000)
ax1.set_ylim(0,100)

def animate(i):
    xar=[]
    yar=[]
    for i in range(0,100):
        xar.append(int(i))
        yar.append(int(random.randint(0,1000)))
    plt.cla()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig,animate,interval=100)
plt.show()
