# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog

# Project modules
from src.ui.mainwindow import Ui_Sintetizador


class MainWindow(QMainWindow, Ui_Sintetizador):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.setupBtns()

    # def setupBtns(self):
    #     self.pushButton_Abrir.clicked.connect(self.AbrirClicked)
    #
    # def AbrirClicked(self):
    #     fname = QFileDialog.getOpenFileName(self, "Open file", "", "MIDI(*.mid)")
    #     self.line_Examinar.setText(fname[0])
    #
    # def GuardarClicked(self):
    #     pass
