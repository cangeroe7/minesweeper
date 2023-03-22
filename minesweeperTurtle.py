import turtle
import random
from turtle import *
import time
from threading import Timer

NUM_ROWS, NUM_COLS, NUM_MINES = 16, 30, 99
CELL_SIZE = 40



pen = Turtle()
pen.speed(0)
delay(0)
pen.penup()
title("Minesweeper")
setup(width=1., height=1.)
# pen.hideturtle()
def make_borders(size, color):
    pen.setpos(-600 - size, (-350 -size))
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.setheading(90)
    for num in [640+2*size, 1200+2*size, 640+2*size, 1200+2*size]:
        pen.forward(num)
        pen.right(90)
    pen.end_fill()
    pen.penup()

make_borders(10, "black")
make_borders(0, "lightgray")

# pen.color("black")
# for i in range(NUM_ROWS):
#     for j in range(NUM_COLS):
#         pen.setpos(j * CELL_SIZE - 600, i * CELL_SIZE - 350)
#         pen.pendown()
#         pen.setheading(90)
#         for _ in range(4):
#             pen.forward(CELL_SIZE)
#             pen.right(90)
#         pen.penup()
window = Screen()
window.tracer(0)
timer_text = turtle.Turtle()
timer_text.hideturtle()
start = 0

def update_timer():
    timer_text.clear()
    print("second", time.time(), start)
    timer_text.write(int(time.time() - start)+1, font=("Courier", 30))
    window.update()

timer = Timer(3, update_timer)

def start_timer():
    global start
    timer.start()
    start = time.time()
    print("hello first", start)
start_timer()





    

pen.dot(200, "purple")

# mainloop()
board = [[0 for col in range(NUM_COLS)] for row in range(NUM_ROWS)]
mines = random.sample(range(NUM_ROWS * NUM_COLS), NUM_MINES)
for mine in mines:
    row = mine // NUM_COLS
    col = mine % NUM_COLS
    board[row][col] = "X"

def count_adjacent_mines(row, col):
    if board[row][col] == "X":
        return "X"

    count = 0
    for i in range(max(row - 1, 0), min(row + 2, NUM_ROWS)):
        for j in range(max(col - 1, 0), min(col + 2, NUM_COLS)):
            if board[i][j] == "X":
                count += 1
    return count

for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        board[row][col] = count_adjacent_mines(row, col) 




mainloop()