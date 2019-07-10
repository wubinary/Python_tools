import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import time
import math

zhfont1 = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")
def draw3D():
    fig = plt.figure(1)
    ax = plt.axes(projection='3d')
    array=[[],[],[]]
    for i in range(2004,2019):
        array[0].append(i)
        array[1].append(pow(1.12,(2018-i))*5700)
        array[2].append(0)
    ax.plot3D(array[0],array[1],array[2], color='green')
    #ax.plot3D(disReshape['asks'][0], disReshape['asks'][1], disReshape['asks'][2], color='blue')
    ax.set_title("2018茶葉幣回歸分析 [指數型回歸]",fontproperties=zhfont1)
    ax.set_xlabel('year年',fontproperties=zhfont1)
    ax.set_ylabel('price價格[RMB/KG]',fontproperties=zhfont1)
    ax.set_zlabel('',fontproperties=zhfont1)
    plt.grid(True)
    plt.show()

draw3D()
