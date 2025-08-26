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


  for row in range(9):
   row_cells = []
   for col in range(9):
    class cell(QLineEdit):
     def __init__(self, mainwindow):
      super().__init__()
      self.mainwindow = mainwindow
      self.setFixedSize(50,50)
      self.setMaxLength(1)
      self.setAlignment(Qt.AlignHCenter)
      self.setReadOnly(True)
     def focusInEvent(self, event):
      self.setStyleSheet("background-color: yellow;")
      if self.mainwindow.selected_number is not None:
        self.setText(self.mainwindow.selected_number)
      print(cells)
      super().focusInEvent(event)
     def focusOutEvent(self, event):
      self.setStyleSheet("")
      super().focusOutEvent(event)

    c = cell(self)
    grid.addWidget(c, row, col)
    row_cells.append(c)
   cells.append(row_cells)
  generate_board(cells)
  central_widget.setLayout(grid)
  
  grid.setSpacing(0)
  grid.setContentsMargins(0,0,0,0)

 def select_number(self, num):
  self.selected_number = str(num)
  self.statusBar().showMessage(f"Selected number: {num}", 0)

def generate_board(board):
 for i in range(25):
  row = random.randint(0, 7)
  column = random.randint(0, 7)
  c = board[row][column]
  c.setText(str(random.randint(1,9)))

def main():
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()