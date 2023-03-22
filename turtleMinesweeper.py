import turtle
import random

# Define board parameters
CELL_SIZE = 40
NUM_ROWS = 16
NUM_COLS = 30
NUM_MINES = 99

# Define colors for the board
COLORS = {
    "background": "gray",
    "grid": "black",
    "mine": "red",
    "flag": "blue",
    "unrevealed": "gray",
    "revealed": "white"
}

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Minesweeper")
screen.bgcolor(COLORS["background"])

# Set up the turtle pen
pen = turtle.Turtle()
pen.speed(0)
turtle.delay(0)
pen.penup()
pen.hideturtle()
# Create the board
board = []
for i in range(NUM_ROWS):
    row = []
    for j in range(NUM_COLS):
        row.append({
            "x": j * CELL_SIZE,
            "y": i * CELL_SIZE,
            "mine": False,
            "revealed": False,
            "flagged": False,
            "num_adjacent_mines": 0
        })
        pen.goto(j * CELL_SIZE - 600, i * CELL_SIZE - 350)
        pen.pendown()
        pen.setheading(90)
        for _ in range(4):
            pen.forward(CELL_SIZE)
            pen.right(90)
        pen.penup()
    board.append(row)

# Add mines to the board
mines = random.sample(range(NUM_ROWS * NUM_COLS), NUM_MINES)
for mine in mines:
    row = mine // NUM_COLS
    col = mine % NUM_COLS
    board[row][col]["mine"] = True

# Function to count the number of adjacent mines
def count_adjacent_mines(row, col):
    count = 0
    for i in range(max(row - 1, 0), min(row + 2, NUM_ROWS)):
        for j in range(max(col - 1, 0), min(col + 2, NUM_COLS)):
            if board[i][j]["mine"]:
                count += 1
    return count

# Function to reveal a cell
def reveal_cell(row, col):
    cell = board[row][col]
    if not cell["revealed"] and not cell["flagged"]:
        cell["revealed"] = True
        pen.goto(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2)
        pen.write(count_adjacent_mines(row, col))
        pen.goto(col * CELL_SIZE, row * CELL_SIZE)
        pen.pendown()
        pen.setheading(90)
        pen.fillcolor(COLORS["revealed"])
        pen.begin_fill()
        for _ in range(4):
            pen.forward(CELL_SIZE)
            pen.right(90)
        pen.end_fill()
        pen.penup()
        if cell["mine"]:
            pen.goto(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2)
            pen.write("X", align="center", font=("Arial", 16, "bold"))
            screen.exitonclick()
        elif count_adjacent_mines(row, col) == 0:
            for i in range(max(row - 1, 0), min(row + 2, NUM_ROWS)):
                for j in range(max(col - 1, 0), min(col + 2, NUM_COLS)):
                    reveal_cell(i, j)

turtle.mainloop()