import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QGridLayout, QPushButton)

class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("Sudoku")
  self.setGeometry(0,0,450,450)
  self.initUI()

 def initUI(self):
  central_widget = QWidget()
  self.setCentralWidget(central_widget)

  cells = []
  grid = QGridLayout()
  for row in range(9):
   row_cells = []
   for col in range(9):
    cell = QLineEdit()
    cell.setFixedSize(50,50)
    cell.setMaxLength(1)
    grid.addWidget(cell, row, col)
    row_cells.append(cells)
  cells.append(row_cells)
  central_widget.setLayout(grid)
  self.selected_number = None
  for n in range(1, 10):
    btn = QPushButton(str(n))
    btn.clicked.connect(lambda _, num=n: self.select_number(num))
    self.statusBar().addPermanentWidget(btn)

 def select_number(self, num):
  self.selected_num = num
  self.statusBar().showMessage(f"Selected number: {num}", 0)


def main():
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()