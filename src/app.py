# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys

# Main window ui import
from src.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
