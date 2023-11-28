import sys
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setWindowTitle("Expense Tracker")
    
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit the Qaction
        exit_action = QAction("")
         
if __name__ == "__main__" :
    # Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800,600)
    window.show()
    sys.exit(app.exec())