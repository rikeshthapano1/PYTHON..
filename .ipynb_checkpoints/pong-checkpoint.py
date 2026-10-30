import turtle
import time

# ===================== STATE MACHINE =====================
STATE = "MENU"

# ===================== WINDOW SETUP =====================
win = turtle.Screen()
win.title("Neon Arcade Pong")
win.bgcolor("#0f172a")
win.setup(width=800, height=600)
win.tracer(0)
win.getcanvas().config(cursor="")

# ===================== COURT TURTLES (bottom layer) =====================
divider = turtle.Turtle()
divider.speed(0)
divider.color("#1e293b")
divider.penup()
divider.hideturtle()
divider.goto(0, 300)
divider.setheading(270)
divider.pensize(4)
for _ in range(15):
    divider.pendown()
    divider.forward(20)
    divider.penup()
    divider.forward(20)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#00f2fe")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#ff007f")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#ffee00")
ball.penup()
ball.goto(0, 0)
ball.dx = 8
ball.dy = 8

score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("0   |   0", align="center", font=("Consolas", 36, "bold"))

# ===================== BLUR OVERLAY (middle layer) =====================
blur = turtle.Turtle()
blur.speed(0)
blur.hideturtle()
blur.penup()

def draw_blur():
    blur.clear()
    blur.goto(-400, -300)
    blur.setheading(0)
    blur.pensize(0)
    blur.color("#0f172a")
    blur.begin_fill()
    for _ in range(2):
        blur.forward(800)
        blur.left(90)
        blur.forward(600)
        blur.left(90)
    blur.end_fill()

def hide_blur():
    blur.clear()

# ===================== UI TURTLES (top layer) =====================
ui = turtle.Turtle()
ui.speed(0)
ui.color("white")
ui.penup()
ui.hideturtle()

MENU_BUTTONS = [
    ("PLAY",         -140, -30, 240, 60, "start"),
    ("HOW TO PLAY",   140, -30, 240, 60, "instructions"),
]
INSTR_BUTTONS = [
    ("BACK",          200, -220, 160, 50, "back"),
]
GAMEOVER_BUTTONS = [
    ("PLAY AGAIN",  -260, -220, 220, 60, "reset"),
    ("EXIT",           60, -220, 160, 60, "menu"),
]

def draw_button(t, label, x, y, w, h):
    t.penup()
    t.goto(x - w/2, y - h/2)
    t.setheading(0)
    t.pensize(3)
    t.color("#00f2fe")
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.penup()
    t.goto(x, y - 10)
    t.color("white")
    t.write(label, align="center", font=("Consolas", 22, "bold"))

def draw_all_buttons(t, buttons):
    for label, x, y, w, h, action in buttons:
        draw_button(t, label, x, y, w, h)

# ===================== ELEMENT VISIBILITY =====================
def hide_game_elements():
    ball.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    divider.clear()
    pen.clear()

def show_game_elements():
    ball.showturtle()
    paddle_a.showturtle()
    paddle_b.showturtle()
    divider.clear()
    divider.goto(0, 300)
    divider.setheading(270)
    divider.pensize(4)
    for _ in range(15):
        divider.pendown()
        divider.forward(20)
        divider.penup()
        divider.forward(20)

# ===================== RENDER FUNCTIONS =====================
def render_menu():
    global STATE
    STATE = "MENU"
    win.getcanvas().config(cursor="")
    hide_game_elements()
    draw_blur()
    ui.clear()
    ui.goto(0, 120)
    ui.color("#00f2fe")
    ui.write("NEON ARCADE PONG", align="center", font=("Consolas", 44, "bold"))
    ui.goto(0, 60)
    ui.color("#ff007f")
    ui.write("Choose your game mode", align="center", font=("Consolas", 20, "italic"))
    draw_all_buttons(ui, MENU_BUTTONS)

def render_instructions():
    global STATE
    STATE = "INSTRUCTIONS"
    win.getcanvas().config(cursor="")
    hide_game_elements()
    draw_blur()
    ui.clear()
    ui.goto(0, 180)
    ui.color("#00f2fe")
    ui.write("HOW TO PLAY", align="center", font=("Consolas", 36, "bold"))
    lines = [
        "",
        "Move your paddle with the MOUSE.",
        "Hover over the left (cyan) paddle to control it.",
        "",
        "Bounce the ball off your paddle to keep it in play.",
        "Score by making the ball pass the AI's paddle (right side).",
        "First to 5 points wins!",
        "",
        "Use the BACK button to return to the menu.",
    ]
    y = 120
    for line in lines:
        ui.goto(0, y)
        ui.color("white")
        ui.write(line, align="center", font=("Consolas", 18, "normal"))
        y -= 32
    draw_all_buttons(ui, INSTR_BUTTONS)

def render_game_over(winner):
    global STATE
    STATE = "GAME_OVER"
    win.getcanvas().config(cursor="")
    hide_game_elements()
    draw_blur()
    ui.clear()
    ui.goto(0, 150)
    ui.color("#ffee00")
    ui.write(f"{winner} WINS!", align="center", font=("Consolas", 40, "bold"))
    ui.goto(0, 80)
    ui.color("white")
    ui.write(f"Final Score: {score_a} - {score_b}", align="center", font=("Consolas", 24, "bold"))
    draw_all_buttons(ui, GAMEOVER_BUTTONS)

def start_game():
    global STATE, score_a, score_b
    STATE = "PLAYING"
    win.getcanvas().config(cursor="none")
    hide_blur()
    ui.clear()
    show_game_elements()
    score_a = 0
    score_b = 0
    pen.goto(0, 220)
    pen.clear()
    pen.write(f"{score_a}   |   {score_b}", align="center", font=("Consolas", 36, "bold"))
    ball.goto(0, 0)
    ball.dx = 8
    ball.dy = 8
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)

def reset_game():
    start_game()

def return_to_menu():
    render_menu()

# ===================== PADDLE MOTION (mouse) =====================
def move_paddle_a(event):
    if STATE != "PLAYING":
        return
    y = 300 - event.y
    if y > 250:
        y = 250
    elif y < -240:
        y = -240
    paddle_a.sety(y)

win.getcanvas().bind("<Motion>", move_paddle_a)

# ===================== CLICK HANDLERS =====================
def on_click(x, y):
    if STATE == "MENU":
        for label, bx, by, bw, bh, action in MENU_BUTTONS:
            if bx - bw/2 <= x <= bx + bw/2 and by - bh/2 <= y <= by + bh/2:
                if action == "start":
                    start_game()
                elif action == "instructions":
                    render_instructions()
                return
    elif STATE == "INSTRUCTIONS":
        for label, bx, by, bw, bh, action in INSTR_BUTTONS:
            if bx - bw/2 <= x <= bx + bw/2 and by - bh/2 <= y <= by + bh/2:
                if action == "back":
                    render_menu()
                return
    elif STATE == "GAME_OVER":
        for label, bx, by, bw, bh, action in GAMEOVER_BUTTONS:
            if bx - bw/2 <= x <= bx + bw/2 and by - bh/2 <= y <= by + bh/2:
                if action == "reset":
                    reset_game()
                elif action == "menu":
                    return_to_menu()
                return

win.listen()
win.onclick(on_click)

# ===================== INITIAL RENDER =====================
render_menu()

# ===================== MAIN LOOP =====================
while True:
    if STATE == "PLAYING":
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if paddle_b.ycor() < ball.ycor() and paddle_b.ycor() < 250:
            paddle_b.sety(paddle_b.ycor() + 7)
        elif paddle_b.ycor() > ball.ycor() and paddle_b.ycor() > -240:
            paddle_b.sety(paddle_b.ycor() - 7)

        if ball.xcor() >= 340 and ball.xcor() <= 360 and ball.dx > 0 and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1
            ball.color("#ff007f")

        if ball.xcor() <= -340 and ball.xcor() >= -360 and ball.dx < 0 and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1
            ball.color("#00f2fe")

        if -300 < ball.xcor() < 300:
            ball.color("#ffee00")

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write(f"{score_a}   |   {score_b}", align="center", font=("Consolas", 36, "bold"))
            if score_a >= 5:
                render_game_over("HUMAN")

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(f"{score_a}   |   {score_b}", align="center", font=("Consolas", 36, "bold"))
            if score_b >= 5:
                render_game_over("AI")

    win.update()
    time.sleep(1 / 60)