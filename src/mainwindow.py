# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout, QLabel, QSlider
from PyQt5 import QtCore

# Project modules
from src.ui.mainwindow import Ui_Sintetizador

# Utilities
import mido
from midi2audio import FluidSynth


class MainWindow(QMainWindow, Ui_Sintetizador):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setupBtns()
        self.midi_file = mido.MidiFile()
        self.midi_filename=""
        self.tracks_sliders=[]

    def setupBtns(self):
        self.pushButton_Abrir.clicked.connect(self.AbrirClicked)
        self.pushButton_Guardar.clicked.connect(self.GuardarClicked)

    def AbrirClicked(self):
        self.midi_filename, type_midi = QFileDialog.getOpenFileName(self, "Open file", "", "MIDI(*.mid)")
        if self.midi_filename!="":
            self.RecieveFile()

    def GuardarClicked(self):
        save_filename, save_type = QFileDialog.getSaveFileName(self, "Save file", "", "MIDI(*.mid);;WAV(*.wav);;MP·(*.mp3)")
        # print(save_filename)
        if save_filename != "":
            if save_type=="MIDI(*.mid)":
                file.save('newsong.mid')
            elif save_type=="WAV(*.wav)":
                fs = FluidSynth(sound_font='font.sf2')
                fs.midi_to_audio(self.midi_filename, save_filename)
            elif save_type == "MP3(*.mp3)":
                fs = FluidSynth(sound_font='font.sf2')
                fs.midi_to_audio(self.midi_filename, save_filename)

    def RecieveFile(self):
        self.midi_file = mido.MidiFile(self.midi_filename)
        self.clearTracks()
        for i, track in enumerate(self.midi_file.tracks):
            self.tracks_sliders.append(self.buildTrack(i, track.name))

    def buildTrack(self, n, track_name):
        horizontalLayout = QHBoxLayout()

        label = QLabel(self.scrollAreaWidgetContents)
        label.setText(str(n) + ". " +track_name)
        horizontalLayout.addWidget(label)

        horizontalSlider = QSlider(self.scrollAreaWidgetContents)
        horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        horizontalLayout.addWidget(horizontalSlider)

        self.verticalLayout_3.addLayout(horizontalLayout)
        return horizontalSlider

    def clearTracks(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            for a in reversed(range(self.verticalLayout_3.itemAt(i).count())):
                self.verticalLayout_3.itemAt(i).itemAt(a).widget().setParent(None)