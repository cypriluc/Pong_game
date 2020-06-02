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
from pyglet import gl

def create_rectangle(x1, y1, x2, y2):
    "Draw a rectangle in given coordinates"
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # draw connected triangles
    gl.glVertex2f(int(x1), int(y1))  # vertex A
    gl.glVertex2f(int(x1), int(y2))  # vertex B
    gl.glVertex2f(int(x2), int(y2))  # vertex C, draw ABC triangle
    gl.glVertex2f(int(x2), int(y1))  # vertex D, draw BCD triangle
    # next coordinate E would draw CDE triangle and so on
    gl.glEnd()  # end drawing rectangles

def draw():
    "Draw game status"
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # delete window content, black background
    gl.glColor3f(1, 1, 1)  # set drawing color to white
    create_rectangle(
        ball_position[0] - BALL_SIZE // 2, 
        ball_position[1] - BALL_SIZE // 2,  
        ball_position[0] + BALL_SIZE // 2,
        ball_position[1] + BALL_SIZE // 2,
    )
    for x, y in [(0, bat_position[0]), (WIDTH, bat_position[1])]:
        create_rectangle(
            x - BAT_THICKNESS,
            y - BAT_LENGTH // 2,
            x + BAT_THICKNESS,
            y + BAT_LENGTH // 2,
        )

    for y in range (LINE_LENGTH // 2, HEIGHT, LINE_LENGTH * 2):
        create_rectangle(
            WIDTH // 2 - 0.5,
            y,
            WIDTH // 2 + 0.5,
            y + LINE_LENGTH,
        )

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.push_handlers(
    on_draw=draw,  # to draw the window use the function 'draw'
)
pyglet.app.run()  # everything set to start the game