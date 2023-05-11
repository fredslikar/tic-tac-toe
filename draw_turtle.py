import turtle
from time import sleep
from random import randint


pen = 0
count_drawer = turtle.Turtle()
count_drawer.hideturtle()
cross_count = 0
null_count = 0
window = turtle.Screen()
window.bgpic("page.gif")
count_click = 1
cell = 0
nf = -1  # номер нового игрового поля от 1 до 9
fields = []
x_cf = 0
y_cf = 0


def make_cfield():
    global count_click
    global nf
    global fields
    field = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    fields.append(field)
    nf = nf + 1
    count_click = 1


def draw_field(x, y):
    global cell
    global pen
    global x_cf
    global y_cf
    cell = randint(30, 40)
    x_cf = x
    y_cf = y
    pen = turtle.Turtle()
    pen.pensize(randint(2, 4))
    pen.color(randint(0, 10) / 10, randint(0, 10) / 10, randint(0, 10) / 10)
    pen.hideturtle()
    #pen.speed(100)
    pen.penup()
    pen.right(90)
    pen.setposition(-0.5 * cell + x, 1.5 * cell + y)
    pen.pendown()
    pen.forward(3 * cell)
    pen.penup()
    pen.setposition(0.5 * cell + x, 1.5 * cell + y)
    pen.pendown()
    pen.forward(3 * cell)
    pen.left(90)
    pen.penup()
    pen.setposition(-1.5 * cell + x, 0.5 * cell + y)
    pen.pendown()
    pen.forward(3 * cell)
    pen.penup()
    pen.setposition(-1.5 * cell + x, -0.5 * cell + y)
    pen.pendown()
    pen.forward(3 * cell)
    make_cfield()


def draw_x(x, y):
    global pen
    pen.penup()
    pen.goto(x + cell * 0.4, y + cell * 0.4)
    pen.pendown()
    pen.goto(x - cell * 0.4, y - cell * 0.4)
    pen.penup()
    pen.goto(x - cell * 0.4, y + cell * 0.4)
    pen.pendown()
    pen.goto(x + cell * 0.4, y - cell * 0.4)


def draw_o(x, y):
    global pen
    pen.penup()
    pen.goto(x, y - 0.5 * cell)
    pen.pendown()
    pen.circle(cell * 0.4)


def check(x, y):
    """Проверка, что кликнули на игровом поле и поочередная проверка на какой из девяти клеток кликнули"""
    if (x > (x_cf - 1.5 * cell)) & (x < (x_cf + 1.5 * cell)) & (y > (y_cf - 1.5 * cell)) & (y < (y_cf + 1.5 * cell)):
        if (x < (x_cf - 0.5 * cell)) & (x > (x_cf - 1.5 * cell)) & (y > (y_cf + 0.5 * cell)) & (
                y < (y_cf + 1.5 * cell)):
            return 1
        elif (x > (x_cf - 0.5 * cell)) & (x < (x_cf + 0.5 * cell)) & (y > (y_cf + 0.5 * cell)) & (
                y < (y_cf + 1.5 * cell)):
            return 2
        elif (x > (x_cf + 0.5 * cell)) & (x < (x_cf + 1.5 * cell)) & (y > (y_cf + 0.5 * cell)) & (
                y < (y_cf + 1.5 * cell)):
            return 3
        elif (x < (x_cf - 0.5 * cell)) & (x > (x_cf - 1.5 * cell)) & (y < (y_cf + 0.5 * cell)) & (
                y > (y_cf - 0.5 * cell)):
            return 4
        elif (x > (x_cf - 0.5 * cell)) & (x < (x_cf + 0.5 * cell)) & (y < (y_cf + 0.5 * cell)) & (
                y > (y_cf - 0.5 * cell)):
            return 5
        elif (x > (x_cf + 0.5 * cell)) & (x < (x_cf + 1.5 * cell)) & (y < (y_cf + 0.5 * cell)) & (
                y > (y_cf - 0.5 * cell)):
            return 6
        elif (x < (x_cf - 0.5 * cell)) & (x > (x_cf - 1.5 * cell)) & (y < (y_cf - 0.5 * cell)) & (
                y > (y_cf - 1.5 * cell)):
            return 7
        elif (x > (x_cf - 0.5 * cell)) & (x < (x_cf + 0.5 * cell)) & (y < (y_cf - 0.5 * cell)) & (
                y > (y_cf - 1.5 * cell)):
            return 8
        elif (x > (x_cf + 0.5 * cell)) & (x < (x_cf + 1.5 * cell)) & (y < (y_cf - 0.5 * cell)) & (
                y > (y_cf - 1.5 * cell)):
            return 9
    else:
        return 0


def title_draw():
    title_drawer = turtle.Turtle()
    title_drawer.hideturtle()
    title_drawer.penup()
    title_drawer.goto(-30, 250)
    title_drawer.write("Cross vs Null!!!", True, align='center', font=('Arial', 25, 'normal'))
    title_drawer.goto(200, 250)
    title_drawer.write("Cross!", True, align='center', font=('Arial', 20, 'normal'))
    title_drawer.goto(280, 250)
    title_drawer.write("Null!", True, align='center', font=('Arial', 20, 'normal'))


def win_draw():
    global cross_count
    global null_count
    global count_drawer
    count_drawer.penup()
    if check_win(fields) == 1:
        cross_count = cross_count + 1
    if check_win(fields) == 2:
        null_count = null_count + 1
    count_drawer.clear()
    count_drawer.goto(195, 220)
    count_drawer.write(cross_count, True, align='left', font=('Arial', 20, 'normal'))
    count_drawer.goto(275, 220)
    count_drawer.write(null_count, True, align='left', font=('Arial', 20, 'normal'))


def play(x, y):
    global fields
    global count_click
    checker = check(x, y)
    if checker == 1:
        if fields[nf][0][0] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][0][0] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][0][0] = 2
                count_click = count_click + 1
    elif checker == 2:
        if fields[nf][0][1] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][0][1] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][0][1] = 2
                count_click = count_click + 1
    elif checker == 3:
        if fields[nf][0][2] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][0][2] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][0][2] = 2
                count_click = count_click + 1
    elif checker == 4:
        if fields[nf][1][0] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][1][0] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][1][0] = 2
                count_click = count_click + 1
    elif checker == 5:
        if fields[nf][1][1] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][1][1] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][1][1] = 2
                count_click = count_click + 1
    elif checker == 6:
        if fields[nf][1][2] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][1][2] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][1][2] = 2
                count_click = count_click + 1
    elif checker == 7:
        if fields[nf][2][0] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][2][0] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][2][0] = 2
                count_click = count_click + 1
    elif checker == 8:
        if fields[nf][2][1] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][2][1] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][2][1] = 2
                count_click = count_click + 1
    elif checker == 9:
        if fields[nf][2][2] == 0:
            if count_click % 2 == 1:
                draw_x(x, y)
                fields[nf][2][2] = 1
                count_click = count_click + 1
            else:
                draw_o(x, y)
                fields[nf][2][2] = 2
                count_click = count_click + 1
    else:
        None
    if check_win(fields) == 1:
        win_draw()
        for i in range(len(fields[nf])):
            for j in range(len(fields[nf][i])):
                fields[nf][i][j] = 3
    elif check_win(fields) == 2:
        win_draw()
        for i in range(len(fields[nf])):
            for j in range(len(fields[nf][i])):
                fields[nf][i][j] = 3

    sleep(1)


def check_win(filds):
    if (filds[nf][0][0] == 1) & (filds[nf][0][1] == 1) & (filds[nf][0][2] == 1):
        return 1
    elif (filds[nf][0][0] == 2) & (filds[nf][0][1] == 2) & (filds[nf][0][2] == 2):
        return 2
    elif (filds[nf][1][0] == 1) & (filds[nf][1][1] == 1) & (filds[nf][1][2] == 1):
        return 1
    elif (filds[nf][1][0] == 2) & (filds[nf][1][1] == 2) & (filds[nf][1][2] == 2):
        return 2
    elif (filds[nf][2][0] == 1) & (filds[nf][2][1] == 1) & (filds[nf][2][2] == 1):
        return 1
    elif (filds[nf][2][0] == 2) & (filds[nf][2][1] == 2) & (filds[nf][2][2] == 2):
        return 2

    elif (filds[nf][0][0] == 1) & (filds[nf][1][0] == 1) & (filds[nf][2][0] == 1):
        return 1
    elif (filds[nf][0][0] == 2) & (filds[nf][1][0] == 2) & (filds[nf][2][0] == 2):
        return 2
    elif (filds[nf][0][1] == 1) & (filds[nf][1][1] == 1) & (filds[nf][2][1] == 1):
        return 1
    elif (filds[nf][0][1] == 2) & (filds[nf][1][1] == 2) & (filds[nf][2][1] == 2):
        return 2
    elif (filds[nf][0][2] == 1) & (filds[nf][1][2] == 1) & (filds[nf][2][2] == 1):
        return 1
    elif (filds[nf][0][2] == 2) & (filds[nf][1][2] == 2) & (filds[nf][2][2] == 2):
        return 2

    elif (filds[nf][0][0] == 1) & (filds[nf][1][1] == 1) & (filds[nf][2][2] == 1):
        return 1
    elif (filds[nf][0][0] == 2) & (filds[nf][1][1] == 2) & (filds[nf][2][2] == 2):
        return 2

    elif (filds[nf][0][2] == 1) & (filds[nf][1][1] == 1) & (filds[nf][2][0] == 1):
        return 1
    elif (filds[nf][0][2] == 2) & (filds[nf][1][1] == 2) & (filds[nf][2][0] == 2):
        return 2


title_draw()
window.onclick(play, 1)
window.onclick(draw_field, 3)

turtle.mainloop()
