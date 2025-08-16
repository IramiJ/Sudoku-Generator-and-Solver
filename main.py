import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("Sudoku")
  self.setGeometry(0,0,450,450)

def main():
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == "__main__":
 main()