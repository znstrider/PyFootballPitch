import numpy as np
from math import pi
from bokeh.models.glyphs import Circle, Patches, Wedge
from bokeh.plotting import figure
from bokeh.models import Range1d

def draw_pitch(width = 700, height = 500, fill_color = '#B3DE69', fill_alpha = 0.5,
               line_color = 'grey', line_alpha = 1,
               arcs = True,
               pitch_marks = None,
               pitch_mark_alphas = np.array([0.25, 0.4])):
    '''

    draws a customizable horizontal 105m x 68m Pitch

    use pitch_marks = 'Grass Cutting' for differentiation of the pitch
    into 5m segments along the x-axis.
    pitch_marks = 'Positional Play' adds horizontal differentiations into
    sides, channels (half-spaces) and the middle (at the inside of 6yard box edges).

    set arcs = False to not draw the penaltybox arcs
    '''
    pitch_mark_alphas = np.array(pitch_mark_alphas)
    p = figure(width = width, height = height, tools = 'save')

    if (pitch_marks == 'Grass Cutting')|(pitch_marks =='Positional Play'):
      v_marks = p.quad(top = 20*[34],
           bottom = 20*[-34],
           left=     [52.5, 52.5-5.5, 52.5-11, 52.5-16.5, 52.5-21.5, 52.5-26.5, 52.5-31.5, 52.5-36.5,
                      52.5-41.5, 52.5-46.5, 0,
                      -52.5+46.5, -52.5+41.5, -52.5+36.5, -52.5+31.5, -52.5+26.5,
                      -52.5+21.5, -52.5+16.5, -52.5+11,-52.5+5.5],
           right = [52.5-5.5, 52.5-11, 52.5-16.5, 52.5-21.5, 52.5-26.5, 52.5-31.5, 52.5-36.5,
                      52.5-41.5, 52.5-46.5, 0,
                      -52.5+46.5, -52.5+41.5, -52.5+36.5, -52.5+31.5, -52.5+26.5,
                      -52.5+21.5, -52.5+16.5, -52.5+11,-52.5+5.5, -52.5],
           color = fill_color,
               alpha = pitch_mark_alphas[[0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0]],
               line_width = 2,
           line_alpha = 0,
           line_color = line_color)

    if (pitch_marks =='Positional Play'):
        h_marks = p.quad( top = [34, 20.12, 9.12, -20.12, -34],
           bottom = [20.12, 9.12, -9.12, -9.12, -20.12],
           left = [-52.5, -36, -36, -36, -52.5],
           right = [52.5, 36, 36, 36, 52.5],
           color = [fill_color,'white',fill_color,'white',fill_color],
           alpha = [0.2,0.25,0.2,0.25,0.2],
           line_width = 2,
           line_alpha = 0.,
           line_color = fill_color
          )

    boxes = p.quad(top = [34, 9.12, 20.12, 20.12, 9.12],
           bottom = [-34, -9.12, -20.12, -20.12, -9.12],
           left = [-52.5, 52.5-5.5, 52.5-16.5, -52.5+16.5, -52.5+5.5],
           right = [52.5, 52.5, 52.5, -52.5, -52.5],
           color = fill_color,
           alpha = [fill_alpha,0,0,0,0], line_width = 2,
           line_alpha = line_alpha,
           line_color = line_color)
    boxes.selection_glyph = boxes.glyph
    boxes.nonselection_glyph = boxes.glyph

    #middle circle
    p.circle(x=[0], y=[0], radius = 9.12,
            color = line_color,
            line_width = 2,
            fill_alpha = 0,
            fill_color = 'grey',
            line_color= line_color)

    if arcs == True:
        p.arc(x=[-41.5, 41.5], y=[0, 0],
            radius = 9.12,
            start_angle = [(2*pi-np.arccos((16.5-11)/9.12)), pi - np.arccos((16.5-11)/9.12)],
            end_angle = [np.arccos((16.5-11)/9.12), pi + np.arccos((16.5-11)/9.12)],
            color = line_color,
            line_width = 2)
    p.circle([0, 52.5-11, -52.5+11], [0, 0, 0], size=5, color=line_color, alpha=1)
    #midfield line
    p.line([0,0], [-34, 34], line_width = 2, color = line_color)
    #goal lines
    p.line((52.5,52.5),(3.66,-3.66), line_width = 6, color = 'white')
    p.line((-52.5,-52.5),(3.66,-3.66), line_width = 6, color = 'white')
    p.x_range=Range1d(-52.5, 52.5)
    p.y_range=Range1d(-34, 34)
    p.grid.visible = False
    p.xaxis.visible = False
    p.yaxis.visible = False

    return p
