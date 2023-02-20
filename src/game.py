import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time
import sys
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    pullData1 = open("team1_data.txt","r").read()
    dataArray1 = pullData1.split('\n')
    xar1 = []
    yar1 = []

    pullData2 = open("team2_data.txt","r").read()
    dataArray2 = pullData2.split('\n')
    xar2 = []
    yar2 = []

    for eachLine in dataArray1:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar1.append(int(x))
            yar1.append(int(y))
    
    for eachLine in dataArray2:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar2.append(int(x))
            yar2.append(int(y))
    ax1.clear()
    ax1.plot(xar1,yar1)
    ax2.clear()
    ax2.plot(xar2,yar2)
ani = animation.FuncAnimation(fig, animate, interval=10)

plt.show()