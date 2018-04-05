# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:56:15 2018

@author: pbrogan
"""



import matplotlib.pyplot as plt
import numpy as np
import IEEEformat
import sys

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

eyeSize = 10
eyeSeparation = 30
eyeHight = 20

smileSize = 30
smileHeight = -30
happiness = 5

faceHeight = 90
faceWidth = 70


try:
    
    xEye = np.array([eyeSize * np.sin(phi) for phi in np.arange(-np.pi, np.pi, np.pi/36)])
    yEye = np.array([eyeSize * np.cos(phi) for phi in np.arange(-np.pi, np.pi, np.pi/36)])
    
    smileSize /= 2
    xSmile = np.array([ x for x in np.arange(-smileSize, smileSize, smileSize/36) ])
    ySmile = np.array([ smileHeight + x**2 for x in np.arange(-happiness, happiness, happiness/36) ])
    
    faceHeight /= 2
    faceWidth /= 2
    ax1.fill(xEye*faceWidth/eyeSize, yEye*faceHeight/eyeSize, color = 'y', zorder = 1)
    
    ax1.plot(xEye - eyeSeparation/2, yEye + eyeHight, color = 'k', linestyle ='--', zorder = 10)
    ax1.scatter(xEye + eyeSeparation/2, yEye + eyeHight, color = 'b', zorder = 10)
    
    ax2.fill(xSmile, ySmile, edgecolor = 'r', facecolor='k', linewidth = 5)
    
    ax1.set_xlabel('formula for happiness [$e^{ix} = cos(x) + i \\times sin(x)$]')
    ax1.set_ylabel(r"Y's Up [$\sum_{n=1}^{\infty} You_{s-uns}$]")
    ax2.set_ylabel(r"Y's Up U2 [$ \frac{Bloody Bono}{Bleeding Edge} $]")
    
    ax1.annotate("RCparam can be a bit `sticky' when doing \n multiple plots, so you might need to do a \nplt.close(), or even close the interpreter :-o", color = 'k', xy = (0.,0.), fontsize = 10)
    
    
    ax1.set_xlim([-50,50])
    ax1.set_ylim([-50,50])
    
    ax2.set_xlim([-50,50])
    ax2.set_ylim([-50,50])
    
    
except:
    ax1.annotate('Get numpy ;-)', color = 'k', xy = (0.5,0.5), fontsize = 10)
    ax1.annotate(str(sys.exc_info()[:2]), xy= (0.1,0.1))
    
plt.savefig('notIEEEformat.jpg')
IEEEformat.apply()

IEEEformat.apply(col = 2, axis = 2)

plt.savefig('IEEEformat-2col-2axis.jpg')
plt.close()
