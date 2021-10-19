import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from views.main import MainView


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 200)
        self.setWindowIcon(QtGui.QIcon("assets/images/icons/app.ico"))
        self.setWindowTitle("Text To Handwriting")
        layout = QVBoxLayout()
        MainView(layout).render()
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())
