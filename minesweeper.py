import random

class Minesweeper:

  def __init__(self, dim_size = 10, bomb_amount = 10):
    self.dim_size = dim_size
    self.bomb_amount = bomb_amount
    self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    self.bomb_board = []
    self.display_board = []
    Minesweeper.start_menu(self)


  def start_menu(self):
    print("""

000    000   00   000   00   0000000    000000   00        00   0000000   0000000   000000    0000000   000000 
0000  0000   00   0000  00   00        00        00   00   00   00        00        00   00   00        00   00
00 0000 00   00   00 00 00   00000      00000     00 0000 00    00000     00000     000000    00000     000000 
00  00  00   00   00  0000   00             00    0000  0000    00        00        00        00        00   00
00      00   00   00   000   0000000   000000      00    00     0000000   0000000   00        0000000   00   00

""")
    start_input = input("                                              PRESS ENTER TO START\n\n                                                       ").lower()
    if start_input == "remythechef":
      print("\n                                    Don't tell anyone: Ratatouille is goated")
      print("\n---------------------------------------------------------------------------------------------------------------\n")
      Minesweeper.get_difficulty_input(self)
    elif start_input == "exit":
      exit()
    else:
      print("---------------------------------------------------------------------------------------------------------------\n")
      Minesweeper.get_difficulty_input(self)
  
  def get_difficulty_input(self):
    self.revealed_count = 0
    print("Difficulties - Beginner: 6 x 6 | Intermediate: 9 x 9 | Expert: 12 x 12\n")
    difficulty_input = input("Choose difficulty - Beginner: 1 | Intermediate: 2 | Expert: 3 \n\nYour Choice: ")
    if difficulty_input == "1":
      self.dim_size = 6
      self.bomb_amount = 6
      print("\nGood Luck!\n\n----------------------------------------------------------------------")
      Minesweeper.play_game(self)
    elif difficulty_input == "2":
      self.dim_size = 9
      self.bomb_amount = 15
      print("\nGood Luck!\n\n----------------------------------------------------------------------")
      Minesweeper.play_game(self)
    elif difficulty_input == "3":
      self.dim_size = 12
      self.bomb_amount = 30
      print("\nGood Luck!\n\n----------------------------------------------------------------------------")
      Minesweeper.play_game(self)
    elif difficulty_input == "exit":
      exit()
    else: 
      print("\nERROR: That is not an option, try again\n")
      Minesweeper.get_difficulty_input(self)

  def play_game(self):
    self.display_board = [['-' for row in range(self.dim_size)] for column in range(self.dim_size)]
    Minesweeper.make_bomb_board(self)
    Minesweeper.make_display_board(self, self.display_board)
    Minesweeper.get_user_input(self)

  def make_bomb_board(self):
    add_numbers = 0
    self.bomb_board = [[0 for row in range(self.dim_size)] for column in range(self.dim_size)]
    if self.bomb_amount >= self.dim_size ** 2:
      return print('ERROR: Too many bombs for this map!')
    bombs_placed = 0
    while bombs_placed < self.bomb_amount:
      x = random.randint(0, self.dim_size - 1)
      y = random.randint(0, self.dim_size - 1)
      if self.bomb_board[y][x] == "X":
        continue
      self.bomb_board[y][x] = "X"
      bombs_placed += 1
      if (x >= 1):
        if self.bomb_board[y][x - 1] != "X":
          self.bomb_board[y][x - 1] += 1
      if (x <= self.dim_size - 2):
        if self.bomb_board[y][x + 1] != "X":
          self.bomb_board[y][x + 1] += 1
      if (y >= 1):
        if self.bomb_board[y -1][x] != "X":
          self.bomb_board[y - 1][x] += 1
      if (y <= self.dim_size-2):
        if self.bomb_board[y + 1][x] != "X":
          self.bomb_board[y + 1][x] += 1
      if (x >= 1) and (y >= 1):
        if self.bomb_board[y - 1][x - 1] != "X":
          self.bomb_board[y - 1][x - 1] += 1
      if (x <= self.dim_size-2) and (y >= 1):
        if self.bomb_board[y - 1][x + 1] != "X":
          self.bomb_board[y - 1][x + 1] += 1
      if (x >= 1) and (y <= self.dim_size-2):
        if self.bomb_board[y + 1][x - 1] != "X":
          self.bomb_board[y + 1][x - 1] += 1
      if (x <= self.dim_size-2) and (y <= self.dim_size-2):
        if self.bomb_board[y + 1][x + 1] != "X":
          self.bomb_board[y + 1][x + 1] += 1
        
  def make_display_board(self, display_board):
    count = 0
    row_top_numbers = ["      "]
    row_between = ["   |"]
    print(" ")
    for row in display_board:
      count += 1
      if count < 10:
        row_between.append("-----|")
        row_top_numbers.append(str(count) + "     ")
      else:
        row_between.append("-----|")
        row_top_numbers.append(str(count) + "    ")
    print("". join(row_top_numbers))
    print("".join(row_between))
    for row in display_board:
      row.insert(0, self.alphabet[display_board.index(row)])
      row.append(' ')
      print("  |  ".join(str(cell) for cell in row))
      print("".join(row_between))
      row.pop(self.dim_size + 1)
    for row in display_board:
      row.pop(0)
    print(" ")

  def get_user_input(self):
    while True:
      try:
        user_input_col = int(input("What is your X input? It should be a number! "))
      except ValueError:
        print("ERROR: Enter a valid number! ")
        continue
      else:
        if user_input_col in range(1, self.dim_size + 1):
          user_input_col -= 1
          break
        else: 
          print("ERROR: Choose an available number! ")
          continue

    while True:
      try: 
        user_input_row = input("What is your Y input? It should be a letter! ").upper()
      except ValueError:
        print("ERROR: Enter a valid letter!")
        continue
      else:
        if user_input_row in self.alphabet[0:self.dim_size]:
          break
        elif user_input_row == "EXIT":
          exit()
        else:
          print("ERROR: Choose an available letter! ")
          continue
    user_input_row = self.alphabet.index(user_input_row)
    if self.display_board[user_input_row][user_input_col] == '-':
      if self.dim_size == 6:
        print("\n----------------------------------------------")
      elif self.dim_size == 9:
        print("\n----------------------------------------------------------")
      else:
        print("\n----------------------------------------------------------------------------")
      Minesweeper.check_coordinates(self, user_input_row, user_input_col)
    else:
      print("\nThis square has already been revealed. Try another one!\n")
      Minesweeper.get_user_input(self)

  def check_coordinates(self, user_input_row, user_input_col):
    if self.bomb_board[user_input_row][user_input_col] in range(1, 9):
      Minesweeper.reveal_coordinates(self, user_input_row, user_input_col)
    if self.bomb_board[user_input_row][user_input_col] == 0:
      Minesweeper.reveal_zero_spots(self, user_input_row, user_input_col)
    if self.bomb_board[user_input_row][user_input_col] == 'X':
      Minesweeper.game_over_sequence(self)
    if self.revealed_count == self.dim_size ** 2 - self.bomb_amount:
      Minesweeper.game_win_sequence(self)
    elif self.bomb_board[user_input_row][user_input_col] != 'X':
      Minesweeper.make_display_board(self, self.display_board)
      Minesweeper.get_user_input(self)
    
  def reveal_coordinates(self, user_input_row, user_input_col):
    self.display_board[user_input_row][user_input_col] = self.bomb_board[user_input_row][user_input_col]
    self.revealed_count += 1

  def is_open(self, user_input_row, user_input_col):
    return self.display_board[user_input_row][user_input_col] in range(0, 9) 

  def reveal_zero_spots(self, user_input_row, user_input_col):
    # self.display_board[user_input_row][user_input_col] = self.bomb_board[user_input_row][user_input_col]
    queue = [[user_input_row, user_input_col]]

    while queue:
      curr = queue.pop(0)
      curr_0 = curr[0]
      curr_1 = curr[1]
      if Minesweeper.is_open(self, curr_0, curr_1):
        continue
      
      Minesweeper.reveal_coordinates(self, curr_0, curr_1)

      if self.bomb_board[curr_0][curr_1] != 0:
        continue
      if (curr_0 >= 1):
        queue.append([curr_0 - 1, curr_1])
      if (curr_0 <= self.dim_size - 2):
        queue.append([curr_0 + 1, curr_1])
      if (curr_1 >= 1):
        queue.append([curr_0, curr_1 - 1])
      if (curr_1 <= self.dim_size - 2):
        queue.append([curr_0, curr_1 + 1])
      if (curr_0 >= 1) and (curr_1 >= 1):
        queue.append([curr_0 - 1, curr_1 - 1])
      if (curr_0 <= self.dim_size - 2) and (curr_1 <= self.dim_size - 2):
        queue.append([curr_0 + 1, curr_1 + 1])
      if (curr_0 >= 1) and (curr_1 <= self.dim_size - 2):
        queue.append([curr_0 - 1, curr_1 + 1])
      if (curr_0 <= self.dim_size - 2) and (curr_1 >= 1):
        queue.append([curr_0 + 1, curr_1 - 1])
      
  def game_over_sequence(self):
    Minesweeper.make_display_board(self, self.bomb_board)
    print("You Lost...\n")
    Minesweeper.ask_stop_play(self)

  def game_win_sequence(self):
    Minesweeper.make_display_board(self, self.bomb_board)
    print("You Won!\n")
    Minesweeper.ask_stop_play(self)



  def ask_stop_play(self):
    if self.dim_size == 12:
      under_line = "----------------------------------------------------------------------------\n"
    else: 
      under_line = "----------------------------------------------------------------------\n" 
    stop_play_input = input("Hit enter to play again. To stop type stop:\n").lower()
    if stop_play_input == "stop":
      print("\n---------------------------------------------------------------------------------------------------------------")
      Minesweeper.start_menu(self)
    elif stop_play_input == "":
      print(under_line)
      Minesweeper.get_difficulty_input(self)
    elif stop_play_input == "exit":
      exit()
    else: 
      print('\n' + under_line)
      Minesweeper.get_difficulty_input(self)

Minesweeper()

