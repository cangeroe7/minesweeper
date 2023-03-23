import random
from turtle import *
import time
from threading import Thread

colors = {
    "X": "black",
    1: "#0000FF",
    2: "#008200",
    3: "#FE0000",
    4: "#000084",
    5: "#840000",
    6: "#008284",
    7: "#840084",
    8: "#757575",
}

NUM_ROWS, NUM_COLS, NUM_MINES = 16, 30, 99
CELL_SIZE = 40
revealed_cells = 0
running = False
board = None
bomb_locations = None
timer_text = Turtle()
cell_opened_text = Turtle()
window = Screen()
pen = Turtle()




def count_adjacent_mines(row, col):
    if board[row][col][0] == "X":
        return "X"
    count = 0
    for i in range(max(row - 1, 0), min(row + 2, NUM_ROWS)):
        for j in range(max(col - 1, 0), min(col + 2, NUM_COLS)):
            if board[i][j][0] == "X":
                count += 1
    return count

def create_bomb_board():
    global board, bomb_locations
    bomb_locations = []
    board = [[[0, False] for col in range(NUM_COLS)] for row in range(NUM_ROWS)]
    mines = random.sample(range(NUM_ROWS * NUM_COLS), NUM_MINES)
    for mine in mines:
        row = mine // NUM_COLS
        col = mine % NUM_COLS
        board[row][col][0] = "X"
        bomb_locations.append([row,col])
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            board[row][col][0] = count_adjacent_mines(row, col) 
    return board, bomb_locations



def make_rectangle(min_x, min_y, width, height, color):
    pen.setpos(min_x, min_y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.setheading(90)
    for num in [height, width, height, width]:
        pen.forward(num)
        pen.right(90)
    pen.end_fill()
    pen.penup()

def create_visual_board():
    pen.speed(0)
    delay(0)
    pen.penup()
    title("Minesweeper")
    setup(width=1., height=1.)
    window.tracer(0)

    make_rectangle(-610, -360, 1220, 660, "black")
    make_rectangle(-600, -350, 1200, 640, "lightgray")
    make_rectangle(-610, 310, 1220, 120, "black")
    make_rectangle(-605, 315, 1210, 110, "#C0C0C0")
    make_rectangle(-103, 328, 200, 70)
    make_rectangle(-97, 322, 200, 70)
    make_rectangle()



    pen.color("black")
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            pen.setpos(j * CELL_SIZE - 600, i * CELL_SIZE - 350)
            pen.pendown()
            pen.setheading(90)
            for _ in range(4):
                pen.forward(CELL_SIZE)
                pen.right(90)
            pen.penup()

    cell_opened_text.hideturtle()
    timer_text.hideturtle()
    timer_text.goto(0, 310)
    timer_text.write(0, font=("Courier", 70), align="center")


def start_clock():
    start = time.time()
    while running and int(time.time() - start) < 999:
        timer_text.clear()
        timer_text.write(int(time.time() - start)+1, font=("Courier", 70), align="center")
        time.sleep(1)

def update_revealed_cells():
    pass


def color_cell(value, row, col, color):
    x_coor, y_coor = col * CELL_SIZE - 600, -row * CELL_SIZE + 250
    pen.goto(x_coor + 0.5, y_coor+ 0.5)
    pen.color(color)
    pen.begin_fill()
    pen.setheading(90)
    for _ in range(2):
        for _ in range(4):
            pen.forward(CELL_SIZE-1)
            pen.right(90)
    pen.end_fill()
    if value:
        pen.color(colors[value])
        pen.goto(x_coor+0.5 + CELL_SIZE/2, y_coor -5)
        pen.write(value, font=("Courier", 30, "bold"), align="center")

def game_lost(r, c):
    global running
    running = False
    for row, col in bomb_locations:
        color_cell("X", row, col, "#C0C0C0")
    color_cell("X", r, c, "red")

def game_won():
    global running
    window.onclick(restart_game)
    running = False

    for row, col in bomb_locations:
        color_cell(0, row, col, "#3EBD4B")

   
    

def reveal_cell(x, y, coords=True):
    # check if a the board is clicked
    if coords:
        if abs(x) < 50 and y > 400 and y < 500:
            start_new_game()
            return
    if abs(x) > 600 or  y < -350 or y > 290:
        return
    
    # checks if the timer is started
    global running, revealed_cells
    if not running:
        running = True
        thread = Thread(target=start_clock)
        thread.start()
    
    # if x and y are coordinates they are converted to the corresponding tiles indexes
    if coords:
        row, col = int(-(y-290) // 40), int((x+600) // 40)
        # if abs(x) < 50 and y > 400 and y < 500:
        #     start_new_game()
        #     return
    else:
        row, col = x, y

    # checks if the tile is already opened. 
    tile_value = board[row][col][0]
    if board[row][col][1]:
        return
    board[row][col][1] = True

    # checks if a bomb was clicked otherwise opens the visually reveals the cell
    if tile_value == "X":
        game_lost(row, col)
    else:
        color_cell(tile_value, row, col, "#C0C0C0")

    # checks if the clicked cell is a zero.
    # it will open all surrounding values if it was a zero
    if tile_value == 0:
        for i in range(max(row - 1, 0), min(row + 2, NUM_ROWS)):
                for j in range(max(col - 1, 0), min(col + 2, NUM_COLS)):
                    if not board[i][j][1]:
                        reveal_cell(i, j, False)

    revealed_cells += 1
    update_revealed_cells()
    if revealed_cells == 381:
        game_won()

def restart_game(x,y):
    pass

def start_new_game():
    global running, revealed_cells, board, bomb_locations, window, timer_text, cell_opened_text, pen
    running = False
    revealed_cells = 0
    clearscreen()
    board, bomb_locations = create_bomb_board()
    pen = Turtle()
    window = Screen()
    timer_text = Turtle()
    cell_opened_text = Turtle()
    create_visual_board()
    window.onclick(reveal_cell)

start_new_game()

mainloop()
running = False
