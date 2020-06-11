# CONSTANTS
    # Window size
WIDTH = 900
HEIGHT = 600
    # Bat and Ball
BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
SPEED = 350 # px/s
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
    # draw ball 
    create_rectangle(
        ball_position[0] - BALL_SIZE // 2, 
        ball_position[1] - BALL_SIZE // 2,  
        ball_position[0] + BALL_SIZE // 2,
        ball_position[1] + BALL_SIZE // 2,
    )
    # draw bats
    for x, y in [(0, bat_position[0]), (WIDTH, bat_position[1])]:
        create_rectangle(
            x - BAT_THICKNESS,
            y - BAT_LENGTH // 2,
            x + BAT_THICKNESS,
            y + BAT_LENGTH // 2,
        )
    # draw centre division line
    for y in range (LINE_LENGTH // 2, HEIGHT, LINE_LENGTH * 2):
        create_rectangle(
            WIDTH // 2 - 0.5,
            y,
            WIDTH // 2 + 0.5,
            y + LINE_LENGTH,
        )
    # draw score
    draw_text(
        str(score[0]),
        TEXT_INDENT,
        HEIGHT - TEXT_INDENT - FONT_SIZE,
        'left',
    )
    draw_text(
        str(score[1]),
        WIDTH - TEXT_INDENT,
        HEIGHT - TEXT_INDENT - FONT_SIZE,
        'right',
    )
    
def draw_text(text, x, y, position_x):
    '''Draw given text on given position
    position_x argument can be 'left' or 'right'
    '''    
    score_label = pyglet.text.Label(
        text,
        font_size = FONT_SIZE,
        x=x, y=y, anchor_x=position_x
    )
    score_label.draw()

from pyglet.window import key

def press_key(symbol, modificator):
    "adds key to pressed_keys set"
    if symbol == key.W:
        pressed_keys.add(('up', 0))
    if symbol == key.S:
        pressed_keys.add(('down', 0))
    if symbol == key.UP:
        pressed_keys.add(('up', 1))
    if symbol == key.DOWN:
        pressed_keys.add(('down', 1))

def release_key(symbol, modificator):
    "removes key from pressed_keys set"
    if symbol == key.W:
        pressed_keys.discard(('up', 0))
    if symbol == key.S:
        pressed_keys.discard(('down', 0))
    if symbol == key.UP:
        pressed_keys.discard(('up', 1))
    if symbol == key.DOWN:
        pressed_keys.discard(('down', 1))

def restore(dt):
    "moving bats, ball, not escaping the field"
    for bat_number in (0, 1):
        # move according keys
        if ('up', bat_number) in pressed_keys:
            bat_position[bat_number] += BAT_SPEED * dt
        if ('down', bat_number) in pressed_keys:
            bat_position[bat_number] -= BAT_SPEED * dt                
        # bottom limit
        if bat_position[bat_number] < BAT_LENGTH / 2:
            bat_position[bat_number] = BAT_LENGTH /2
        # top limit
        if bat_position[bat_number] > HEIGHT - BAT_LENGTH /2:
            bat_position[bat_number] = HEIGHT - BAT_LENGTH / 2
    # move the ball
    ball_position[0] += ball_speed[0] * dt
    ball_position[1] += ball_speed[1] * dt
    # bounce the ball from wall
    if ball_position[1] < BALL_SIZE // 2:
        ball_speed[1] = abs(ball_speed[1])
    if ball_position[1] > HEIGHT - BALL_SIZE // 2:
        ball_speed[1] = -abs(ball_speed[1])

    bat_min = ball_position[1] - BALL_SIZE / 2 - BAT_LENGTH / 2
    bat_max = ball_position[1] + BALL_SIZE / 2 + BAT_LENGTH / 2
    # hit ball left
    if ball_position[0] < BAT_THICKNESS + BALL_SIZE / 2:
        if bat_min < bat_position[0] < bat_max:
            ball_speed[0] = abs(ball_speed[0])
        else:
            score[1] += 1
            reset()
    # hit ball right
    if ball_position[0] > WIDTH - (BAT_THICKNESS + BALL_SIZE / 2):
        if bat_min < bat_position[1] < bat_max:
            ball_speed[0] = -abs(ball_speed[0])
        else:
            score[0] += 1
            reset()



import random
def reset():
    "ball at the beggining starting in the middle in random direction"
    ball_position[0] = WIDTH // 2
    ball_position[1] = HEIGHT // 2
    # x speed: right / left
    if random.randint(0, 1):
        ball_speed[0] = SPEED
    else:
        ball_speed[0] = -SPEED
    # y speed is random
    ball_speed[1] = random.uniform(-1, 1) * SPEED
    

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.push_handlers(
    on_draw=draw,  # to draw the window use the function 'draw'
    on_key_press=press_key,
    on_key_release=release_key,
)
pyglet.clock.schedule(restore)
reset()
pyglet.app.run()  # everything set to start the game