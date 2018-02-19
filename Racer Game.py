import turtle
import random
import time
import math

game_over = False

player_pos = [0, 0]
player_stamp = -1
tracks = []
track_stamps = []
score = 100
difficulty = 0

difficulty = input("Choose a difficulty (1-3 reccomended) (>5 will be buggy):")
int(difficulty)

turtle.pu()
turtle.tracer(0,0)
turtle.bgcolor('black')

font = turtle.Turtle()

def reset():
    global tracks, track_stamps, player_pos, player_stamp, score, game_over

    turtle.clearstamp(player_stamp)
    clear_track()

    game_over = False
    score = 100
    player_pos = [0, 0]
    player_stamp = -1
    tracks = []
    track_stamps = []
    for i in range(21):
        tracks.append({'position': [0, 200 - i * 20], 'width': 150})

def clear_track():
    global track_stamps
    for track in track_stamps:
        turtle.clearstamp(track)
    track_stamps = []

def draw_track():
    global tracks
    for track in tracks:
        x_pos = track['position'][0] - track['width']/2
        y_pos = track['position'][1]
        turtle.color('blue')
        turtle.setpos(x_pos, y_pos)
        turtle.shape('square')
        track_stamps.append(turtle.stamp())

        x_pos = track['position'][0] + track['width']/2
        y_pos = track['position'][1]
        turtle.color('blue')
        turtle.setpos(x_pos, y_pos)
        turtle.shape('square')
        track_stamps.append(turtle.stamp())

def scroll_track():
    global tracks, score

    score += score//100
    tracks.pop(0)
    for track in tracks:
        track['position'][1] += 70
    x_pos = tracks[len(tracks)-1]['position'][0]
    width = tracks[len(tracks)-1]['width']

    step = random.randint(-2, 2)
    x_pos += step * (math.log10(score)*int(difficulty))


    width_step = random.randint(-1, 1)
    width += width_step * 10
    if (width <= 100):
        width = 100
    if (width >=200):
        width = 200

    if x_pos - width/2 < -200:
        x_pos = -200 + width/2
    if x_pos + width/2 > 200:
        x_pos = 200 - width/2
    tracks.append({'position': [x_pos, -200], 'width': width})

def draw_player():
    global player_stamp, score

    font.clear()
    font.ht()
    font.setpos(-70, -300)
    font.color("Red")
    font.write("Score: " + str(score), font=("Terminal", 16, "normal"))

    turtle.clearstamp(player_stamp)
    turtle.setpos(player_pos)
    turtle.shape('square')
    turtle.color('yellow')
    player_stamp = turtle.stamp()

def check_collision():
    global game_over, player_pos, tracks
    row = int((200 - player_pos[1]) / 20)
    if player_pos[0] <= (tracks[row]['position'][0] - tracks[row]['width']/2):
        game_over = True
    elif player_pos[0] >= (tracks[row]['position'][0] + tracks[row]['width']/2):
        game_over = True

def run_game():
    global game_over

    check_collision()
    if not game_over:
        scroll_track()
        clear_track()
        draw_track()

        draw_player()
    turtle.update()

    turtle.ontimer(run_game, 16)

def left():
    global player_pos
    player_pos[0] -= 10

def right():
    global player_pos
    player_pos[0] += 10

def up():
    global player_pos, score
    player_pos[1] += 20
    if player_pos[1] > 200:
        player_pos[1] = 200

def down():
    global player_pos, score
    player_pos[1] -= 20
    if player_pos[1] < -200:
        player_pos[1] = -200

def start():
    global game_over
    if game_over:
        reset()

turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(start, 'space')
turtle.listen()

reset()
run_game()
