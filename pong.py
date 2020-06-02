# CONSTANTS
    # Window size
WIDTH = 900
HEIGHT = 600
    # Bat and Ball
BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
SPEED = 200 # px/s
BAT_SPEED = SPEED * 1.5
    # Playing field
LINE_LENGTH = 20
FONT_SIZE = 42
TEXT_INDENT = 30

# VARIABLES
bat_position = [HEIGHT // 2, HEIGHT // 2]   # vertical position of two bats
ball_position = [0, 0]  # ball position in reset()
ball_speed = [0, 0] # ball speed in reset()
pressed_keys = set()    # set of pressed keys
score = [0, 0]

import pyglet

def draw_rectangle(x1, y1, x2, y2):
    "Draw a rectangle in given coordinates"
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # draw connected triangles
    gl.glVertex2f(int(x1), int(y1))  # vertex A
    gl.glVertex2f(int(x1), int(y2))  # vertex B
    gl.glVertex2f(int(x2), int(y2))  # vertex C, draw ABC triangle
    gl.glVertex2f(int(x2), int(y1))  # vertex D, draw BCD triangle
    # next coordinate E would draw CDE triangle and so on
    gl.glEnd()  # end drawing rectangles

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
pyglet.app.run()

