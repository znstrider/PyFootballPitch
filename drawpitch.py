import matplotlib.pyplot as plt
from matplotlib import patches
from math import pi
import numpy as np

def drawpitch(ax, hspan = [-52.5, 52.5], vspan = [-34, 34], measure = 'metres',\
                linecolor = '#525252', facecolor = '#f0f0f0', arcs = True, \
                lw = 1.5, x_offset = [4,4], y_offset = [4,4], style_id = None,
                grass_cutting = False):
    '''
    -----
    Draws a horizontal pitch on an axes object with width 105m and height 68m
    -----
    If you are using StatsBomb Data with a 120x80yard pitch, use:
    measure == 'SBData'
    -----
    If you are using any other pitch size, set measure to yards or metres
    for correct pitch markings and
    hspan = [left, right] // eg. for SBData this is: hspan = [0, 120]
    vspan = [bottom, top] //
    to adjust the plot to your needs.
    -----
    Choose a Style with
    style_id = 1...8
    you can also set linecolor, lw (linewidth), and facecolor individually.
    -----
    default arcs = True; False to not draw the penalty box arcs.
    -----
    use x_offset and y_offset to extend the plot further past the pitch
    or also to just draw half the pitch
    -----
    grass_cutting = n to divide the pitch into n-1 vertical stripes from box to box
    (works best for even n)
    grass_cutting = True sets n to 14
    '''


    if measure == 'metres':
        measures = [3.66, 5.5, 9.12, 16.5, 40.24]
    elif measure == 'yards':
        measures = [4, 6, 10, 18, 42]
    elif (measure == 'SBData')|(measure == 'StatsBomb'):
        measures = [4, 6, 10, 18, 42]
        hspan = [0, 120]
        vspan = [0, 80]

    hmid = (hspan[1]+hspan[0])/2
    vmid = (vspan[1]+vspan[0])/2
    ax.axis([hspan[0]-x_offset[0],hspan[1]+x_offset[1],vspan[0]-y_offset[0],vspan[1]+y_offset[1]])

    if style_id:
        style = {1: ["#525252", "#f0f0f0"],
                 2: ["#f0f0f0", "#252525"],
                 3: ["#000000", '#ffffff'],
                 4: ["#d9d9d9", "#525252"],
                 5: ["#525252", "#d9f0d3"],
                 6: ["#525252", "#f7fcf5"],
                 7: ["#525252", "#fff5eb"],
                 8: ["#525252", "#deebf7"]}
        if (style_id <= len(style))&(style_id>0):
            linecolor = style[style_id][0]
            facecolor = style[style_id][1]
        else:
            raise ValueError('style_id needs to be in range(1, '+str(len(style)+1)+')')
    ax.set_facecolor(facecolor)

    mid_circle = plt.Circle((hmid, vmid), radius=measures[2], fc='None', color = linecolor, lw = lw )
    ax.add_patch(mid_circle)

    mid_point = plt.Circle((hmid, vmid), radius=0.4, fc='white', color = linecolor, lw = lw)
    ax.add_patch(mid_point)

    fiveyard1 = plt.Rectangle((hspan[0], vmid-measures[2]), measures[1], measures[2]*2, fc='None', color = linecolor, lw = lw)
    ax.add_patch(fiveyard1)

    fiveyard2 = plt.Rectangle((hspan[1]-measures[1], vmid-measures[2]), measures[1], measures[2]*2, fc='None', color = linecolor, lw = lw)
    ax.add_patch(fiveyard2)

    box1 = plt.Rectangle((hspan[0], vmid-measures[4]/2), measures[3], measures[4], fc='None', color = linecolor, lw = lw)
    ax.add_patch(box1)

    box2 = plt.Rectangle((hspan[1]-measures[3], vmid-measures[4]/2), measures[3], measures[4], fc='None', color = linecolor, lw = lw)
    ax.add_patch(box2)

    midline = plt.Line2D((hmid, hmid), (vspan[0], vspan[1]), c = linecolor, lw = lw)
    ax.add_line(midline)

    leftgoalline = plt.Line2D((hspan[0],hspan[0]),(vspan[1], vspan[0]), c = linecolor, lw = lw)
    ax.add_line(leftgoalline)

    rightgoalline = plt.Line2D((hspan[1],hspan[1]),(vspan[1], vspan[0]), c = linecolor, lw = lw)
    ax.add_line(rightgoalline)

    topfieldline = plt.Line2D((hspan[0],hspan[1]),(vspan[1], vspan[1]), c = linecolor, lw = lw)
    ax.add_line(topfieldline)

    bottomfieldline = plt.Line2D((hspan[0],hspan[1]),(vspan[0],vspan[0]), c = linecolor, lw = lw)
    ax.add_line(bottomfieldline)

    goal1 = plt.Line2D((hspan[0],hspan[0]),(vmid+measures[0],vmid-measures[0]), c=linecolor, lw = 3*lw)
    ax.add_line(goal1)

    goal2 = plt.Line2D((hspan[1],hspan[1]),(vmid+measures[0],vmid-measures[0]), c = linecolor, lw = 3*lw)
    ax.add_line(goal2)

    penalty1 = plt.Circle((hspan[0]+2*measures[1], vmid), radius = 0.4, fc = linecolor, color=linecolor)
    ax.add_patch(penalty1)

    penalty2 = plt.Circle((hspan[1]-2*measures[1], vmid), radius = 0.4, fc = linecolor, color=linecolor)
    ax.add_patch(penalty2)

    if arcs:
        a = np.arccos((measures[3]-11)/measures[2])
        arc1 = patches.Arc(xy = (hspan[0]+11, vmid), width = 2*measures[2], height = 2*measures[2],\
                                theta1 = (2*pi - a)*180/pi, theta2 = a*180/pi, color = linecolor, lw = lw)
        ax.add_patch(arc1)
        arc2 = patches.Arc(xy = (hspan[1]-11, vmid), width = 2*measures[2], height = 2*measures[2],\
                                theta1 = (pi - a)*180/pi, theta2 = (pi + a)*180/pi, color = linecolor, lw = lw)
        ax.add_patch(arc2)

    if grass_cutting:
        if grass_cutting == True:
            grass_cutting = 14
        xmid = [hspan[0] + measures[3], hspan[1] - measures[3]]
        hbins = np.linspace(xmid[0], xmid[1], grass_cutting)

        for i in range(len(hbins)):
            if i in range(len(hbins))[:-1:2]:
                rect = plt.Rectangle((hbins[i], vspan[1]),
                                     hbins[i+1] - hbins[i],
                                     vspan[0] - vspan[1],
                                     color = linecolor, lw = 0, alpha = 0.04)
                ax.add_patch(rect)
        rect = plt.Rectangle((hspan[0]+measures[1], vspan[1]),
                                     measures[1],
                                     vspan[0] - vspan[1],
                                     color = linecolor, lw = 0, alpha = 0.04)
        ax.add_patch(rect)
        rect = plt.Rectangle((hspan[1]-measures[1], vspan[1]),
                                     -measures[1],
                                     vspan[0] - vspan[1],
                                     color = linecolor, lw = 0, alpha = 0.04)
        ax.add_patch(rect)

    ax.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        left='off',
        labelleft='off',
        labelbottom='off')

    return ax
