import numpy as np
from math import pi
from bokeh.models.glyphs import Circle, Patches, Wedge
from bokeh.plotting import figure
from bokeh.models import Range1d

def draw_pitch(width = 700, height = 500,
                measure = 'metres',
                fill_color = '#B3DE69', fill_alpha = 0.5,
                line_color = 'grey', line_alpha = 1,
                hspan = [-52.5, 52.5], vspan = [-34, 34],
                arcs = True):
    '''
    -----
    Draws and returns a pitch on a Bokeh figure object with width 105m and height 68m
    p = drawpitch()
    -----
    If you are using StatsBomb Data with a 120x80yard pitch, use:
    measure = 'SB'
    -----
    If you are using Opta Data, use:
    measure = 'Opta'
    -----
    If you are using any other pitch size, set measure to yards or metres
    for correct pitch markings and
    hspan = [left, right] // eg. for SBData this is: hspan = [0, 120]
    vspan = [bottom, top] //
    to adjust the plot to your needs.
    -----
    set arcs = False to not draw the penaltybox arcs
    '''

    # measures:
    # goalcenter to post, fiveyard-box-length, fiveyard-width,
    # box-width, penalty-spot x-distance, circle-radius


    if measure == 'yards':
        measures = [4, 6, 10, 18, 42, 12, 10]
    elif (measure == 'SBData')|(measure == 'StatsBomb')|(measure == 'statsbomb')|(measure == 'SB'):
        measures = [4, 6, 10, 18, 44, 12, 10]
        hspan = [0, 120]
        vspan = [0, 80]
    elif measure == 'Opta':
        measures = [4.8, 5.8, 13.2, 17, 57.8, 11.5, 8.71]
        hspan = [0, 100]
        vspan = [0, 100]
    else: #if measure = metres or whatever else
        measures = [3.66, 5.5, 9.16, 16.5, 40.32, 11, 9.15]

    hmid = (hspan[1]+hspan[0])/2
    vmid = (vspan[1]+vspan[0])/2

    p = figure(width = width,
        height = height,
        x_range = Range1d(hspan[0], hspan[1]),
        y_range = Range1d(vspan[0], vspan[1]),
        tools = [])

    boxes = p.quad(top = [vspan[1], vmid+measures[2], vmid+measures[4]/2, vmid+measures[4]/2, vmid+measures[2]],
           bottom = [vspan[0], vmid-measures[2], vmid-measures[4]/2, vmid-measures[4]/2, vmid-measures[2]],
           left = [hspan[0], hspan[1]-measures[1], hspan[1]-measures[3], hspan[0]+measures[3], hspan[0]+measures[1]],
           right = [hspan[1], hspan[1], hspan[1], hspan[0], hspan[0]],
           color = fill_color,
           alpha = [fill_alpha,0,0,0,0], line_width = 2,
           line_alpha = line_alpha,
           line_color = line_color)
    boxes.selection_glyph = boxes.glyph
    boxes.nonselection_glyph = boxes.glyph

    #middle circle
    p.circle(x=[hmid], y=[vmid], radius = measures[6],
            color = line_color,
            line_width = 2,
            fill_alpha = 0,
            fill_color = 'grey',
            line_color= line_color)

    if arcs == True:
        p.arc(x=[hspan[0]+measures[5], hspan[1]-measures[5]], y=[vmid, vmid],
            radius = measures[6],
            start_angle = [(2*pi-np.arccos((measures[3]-measures[5])/measures[6])), pi - np.arccos((measures[3]-measures[5])/measures[6])],
            end_angle = [np.arccos((measures[3]-measures[5])/measures[6]), pi + np.arccos((measures[3]-measures[5])/measures[6])],
            color = line_color,
            line_width = 2)

    p.circle([hmid, hspan[1]-measures[5], hspan[0]+measures[5]], [vmid, vmid, vmid], size=5, color=line_color, alpha=1)
    #midfield line
    p.line([hmid, hmid], [vspan[0], vspan[1]], line_width = 2, color = line_color)
    #goal lines
    p.line((hspan[1],hspan[1]),(vmid+measures[0],vmid-measures[0]), line_width = 6, color = 'white')
    p.line((hspan[0],hspan[0]),(vmid+measures[0],vmid-measures[0]), line_width = 6, color = 'white')
    p.grid.visible = False
    p.xaxis.visible = False
    p.yaxis.visible = False

    return p
