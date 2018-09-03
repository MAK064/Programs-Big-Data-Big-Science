from JMSSGraphics import *
import random

jmss = Graphics(660, 700, fps = 60)

max_columns = 30
max_rows = 30

column_width = 22
row_height = 22

column_margin = 0
row_margin = 0
left_margin = 0
bottom_margin = 0

frames_until_move = 15
moves_until_grow = 5

move_counter = frames_until_move

# using a "list" of coordinates for the snake
snake = []
# adding the first coordinate
snake.append([0, 0])
snake_dir = 0
snake_state = 0

score = 0
high_score = 0

x = max_columns / 2
y = max_rows / 2
collectable = []

# using functions to make our code a little cleaner
def ScoreCheck():
    global score, high_score
    if score > high_score:
        high_score = score
def DrawScore():
    global score, display_score, high_score
    jmss.drawText("Score: " + str(int(score)), 80, 660, fontSize = 20)
    # TODO: implement your HIGH SCORE LOGIC!
    jmss.drawText("High Score:" + str(int(high_score)), 330, 660, fontSize = 20)

def DrawCollectable():
    global collectable
    x_pos = collectable[0] * (column_width + column_margin) + left_margin
    y_pos = collectable[1] * (row_height + row_margin) + bottom_margin
    jmss.drawRect(color = (0, 1, 0, 1), \
                  x1 = x_pos,
                  y1 = y_pos,
                  x2 = x_pos + column_width,
                  y2 = y_pos + row_height)


def DrawSnake():
    global snake_state
    segment = len(snake) - 1
    # drawing the snake backwards so that the head is drawn last in a different colour
    # using a while loop to go through the list
    while segment >= 0:
        x_pos = snake[segment][0] * (column_width + column_margin) + left_margin
        y_pos = snake[segment][1] * (row_height + row_margin) + bottom_margin
        if segment == 0:
            snake_color = (1, 0, 0, 1)
        else:
            snake_color = (1, 0, 1, 1)
        jmss.drawRect(color = snake_color, \
                      x1 = x_pos,
                      y1 = y_pos,
                      x2 = x_pos + column_width,
                      y2 = y_pos + row_height)
        # updating the control variable in the loop
        segment -= 1

def ResetSnake():
    global snake_state, snake, frames_until_move, moves_until_grow, score
    snake = [snake[0]]
    snake_state = 0
    frames_until_move = 15
    moves_until_grow = 5
    score = 0

def SpawnCollectable():
    global max_columns, max_rows, snake, collectable
    collectable = [random.randint(0, max_columns - 1), \
                   random.randint(0, max_rows - 1)]
    while collectable == snake[0]:
        collectable = [random.randint(0, max_columns - 1), \
                       random.randint(0, max_rows - 1)]

def UpdateSnake():
    global x, y, grow_frame_counter, move_frame_counter, frames_until_grow, \
           frames_until_move, snake, row_height, column_width, column_margin, \
           row_margin, left_margin, bottom_margin, moves_until_grow, \
           frames_until_move, move_counter, max_columns, \
           max_rows, snake_state, collectable, score, high_score

    move_counter -= 1

    if move_counter < 0:

        # round off the frames until move
        # we are using a decimal value so that we can reduce this rate by a fractional amount each frame
        move_counter = int(math.ceil(frames_until_move))

        segment = len(snake) - 1
        tail = snake[segment].copy()

        #shift all segments up by one
        while segment != 0:
            snake[segment] = snake[segment - 1].copy()
            segment -= 1

        #move the head
        head = snake[0]
        if snake_dir == 0:
            head[0] += 1
        if snake_dir == 1:
            head[0] -= 1
        if snake_dir == 2:
            head[1] += 1
        if snake_dir == 3:
            head[1] -= 1

        head[0] = head[0] % max_columns
        head[1] = head[1] % max_rows

        # check if dead
        segment = 1
        while segment < len(snake):
            if snake[0] == snake[segment]:
                # snake has eaten itself
                snake_state = 1
                return
            segment += 1

        # check if gotten the collectable
        if snake[0] == collectable:
            score += 50
            snake.append(tail)
            snake.append(tail)
            snake.append(tail)
            frames_until_move -= 3
            SpawnCollectable()

def ProcessInput():
    global snake_dir
    if jmss.isKeyDown(KEY_W):
        snake_dir = 2
    if jmss.isKeyDown(KEY_S):
        snake_dir = 3
    if jmss.isKeyDown(KEY_A):
        snake_dir = 1
    if jmss.isKeyDown(KEY_D):
        snake_dir = 0

    if jmss.isKeyDown(KEY_SPACE):
        ResetSnake()

def UpdateGame():
    global snake_state, frames_until_move, score, display_score
    ProcessInput()
    if frames_until_move < 2:
        # limit the fastest move rate
        frames_until_move = 2
    if snake_state == 0:
        UpdateSnake()
    ScoreCheck()

def DrawGame():
    jmss.clear()
    DrawSnake()
    DrawCollectable()
    DrawScore()

@jmss.mainloop
def Game():
    UpdateGame()
    DrawGame()

SpawnCollectable()

jmss.run()
