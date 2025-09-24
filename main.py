import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QGridLayout, QPushButton)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.selected_number = None
  self.setWindowTitle("Sudoku")
  self.setGeometry(0,0,450,450)
  self.setMaximumHeight(450)
  self.setMaximumWidth(450)
  self.initUI()

 def initUI(self):
  central_widget = QWidget()
  self.setCentralWidget(central_widget)
  a = 2
  for n in range(1, 10):
    btn = QPushButton(str(n))
    btn.clicked.connect(lambda _, num=n: self.select_number(num))
    self.statusBar().addPermanentWidget(btn)


  cells = []
  grid = QGridLayout()
  class cell(QLineEdit):
     def __init__(self, mainwindow):
      super().__init__()
      self.mainwindow = mainwindow
      self.setFixedSize(50,50)
      self.setMaxLength(1)
      self.setAlignment(Qt.AlignHCenter)
      self.setReadOnly(True)
      self.preset = False
     def focusInEvent(self, event):
      if self.mainwindow.selected_number is not None and not self.preset:
        self.setText(self.mainwindow.selected_number)
      super().focusInEvent(event)
     def focusOutEvent(self, event):
      self.setStyleSheet("")
      super().focusOutEvent(event)
     def enterEvent(self, event):
      if self.preset == False:
       self.setStyleSheet("background-color: red;")
#       self.setText(self.mainwindow.selected_number)
      super().enterEvent(event)
     def leaveEvent(self, event):
      if self.preset == False:
       self.setStyleSheet("")
      super().leaveEvent(event)
   

  for row in range(9):
   row_cells = []
   for col in range(9):
    c = cell(self)
    grid.addWidget(c, row, col)
    row_cells.append(c)
   cells.append(row_cells)
   
#  generate_board(cells)
  
  central_widget.setLayout(grid)
  
  grid.setSpacing(0)
  grid.setContentsMargins(0,0,0,0)

  board = generate_puzzle()
  sync_to_gui(board, cells)

 def select_number(self, num):
  self.selected_number = str(num)
  self.statusBar().showMessage(f"Selected number: {num}", 0)

def is_valid(board, row, col, num):
 if num in board[row]:
  return False
 if num in [board[r][col] for r in range(9)]:
  return False
 start_row, start_col = 3 * (row // 3), 3 * (col // 3)
 for r in range(start_row, start_row + 3):
  for c in range(start_col, start_col + 3):
   if board[r][c] == num:
    return False
 return True

def find_empty(board):
 for r in range(9):
  for c in range(9):
   if board[r][c] == 0:
    return r, c
 return None

def fill_board(board):
 empty = find_empty(board)
 if not empty:
  return True
 row, col = empty
 numbers = list(range(1, 10))
 random.shuffle(numbers)
 for num in numbers:
  if is_valid(board, row, col, num):
   board[row][col] = num
   if fill_board(board):
    return True
   board[row][col] = 0
 return False

def count_solutions(board):
 empty = find_empty(board)
 if not empty:
  return 1
 row, col = empty
 count = 0
 for num in range(1, 10):
  if is_valid(board, row, col, num):
   board[row][col] = num
   count += count_solutions(board)
   board[row][col] = 0
   if count > 1:
    break
 return count

def generate_puzzle(removals=10):
 board = [[0 for _ in range(9)] for _ in range(9)]
 fill_board(board)
 attempts = removals
 while attempts > 0:
  row, col = random.randint(0, 8), random.randint(0, 8)
  while board[row][col] == 0:
   row, col = random.randint(0, 8), random.randint(0, 8)
  backup = board[row][col]
  board[row][col] = 0
  board_copy = [r[:] for r in board]
  if count_solutions(board_copy) != 1:
   board[row][col] = backup
   attempts -= 1
 return board

def sync_to_gui(board, qlineedit_board):
 for row in range(9):
  for col in range(9):
   value = board[row][col]
   cell = qlineedit_board[row][col]
   if value == 0:
    cell.clear()
   else:
    cell.setText(str(value))
    cell.preset = True
    cell.setStyleSheet("background-color: #c2bebe;")

# def generate_board(board):
#  for i in range(25):
#   numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#   row = random.randint(0, 8)
#   column = random.randint(0, 8)
#   section = []
#   for i in range(9):
#    section.append(board[row][i])
#   for i in range(9):
#    section.append(board[i][column])
  

# # "Determining the Square section "     
#   square_width = row // 3
#   square_height = column // 3
#   for width in range(3):
#    for height in range(3):
#     section.append(board[square_width*3+width][square_height*3+height])

#   for cell in section:
#    if cell.text() is not None and cell.text() in numbers:
#     numbers.remove(cell.text())

#   c = board[row][column]
#   index = random.randint(0, len(numbers)-1)
#   c.setText(numbers[index])

def main():
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()