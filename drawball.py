import matplotlib.pyplot as plt
import matplotlib as mpl
from math import pi
import numpy as np

def drawball(ax=plt.gca(), r=1, x=0, y=0, s=90, ballcolor = '#f0f0f0', ball_edgecolor = '#737373',
    ball_alpha = 1, patchcolor = '#737373', zorder = 1):
    angles = np.array([s, s+72, s+144, s+216, s+288]) * pi / 180
    polygon = np.array([[x+np.cos(a)*r*0.35 , y+np.sin(a)*r*0.35] for a in angles])

    c = mpl.patches.Circle(radius=r, xy = (x, y),
    facecolor = ballcolor, edgecolor = ball_edgecolor,
    alpha = ball_alpha, zorder = zorder, linewidth=0.25)
    f = mpl.patches.Polygon(polygon, color = patchcolor, alpha = ball_alpha, zorder = zorder)
    ax.add_patch(c), ax.add_patch(f)

    offset = 15 * pi / 180

    angles = np.array([-s, -s+72, -s+144, -s+216, -s+288]) * pi / 180

    for i in range(len(angles)):
        w = mpl.patches.Wedge(center = (x,y), r = r,
                              theta1=(angles[i]-offset)*180/pi,
                              theta2=(angles[i]+offset)*180/pi,
                              width=r/4,
                              color = patchcolor,
                              alpha = ball_alpha,
                              zorder = zorder)
        ax.add_patch(w)
