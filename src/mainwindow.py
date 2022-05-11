# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout, QLabel, QSlider, QCheckBox
from PyQt5 import QtCore

# Project modules
from src.ui.mainwindow import Ui_Sintetizador

# Utilities
import mido
from midi2audio import FluidSynth
import pygame


class MainWindow(QMainWindow, Ui_Sintetizador):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setupPyMixer()
        self.setupBtns()
        self.midi_file = mido.MidiFile()
        self.play_from_start=True
        self.midi_filename=""
        self.midi_synth=""
        self.tracks_sliders=[]
        self.reverb_retraso = 0
        self.reverb_ganancia = 0
        self.echo_retraso = 0
        self.echo_ganancia = 0
        self.flanger_retraso = 0
        self.flanger_ganancia = 0
        self.flanger_freq = 0

    def setupBtns(self):
        self.pushButton_Abrir.clicked.connect(self.AbrirClicked)
        self.pushButton_Abrir.setStyleSheet("QPushButton"
                                         "{"
                                         "background-color : rgb(172, 172, 172);"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color : lightblue;"
                                         "}"
                                         )
        self.pushButton_Guardar.clicked.connect(self.GuardarClicked)
        self.pushButton_Guardar.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : rgb(172, 172, 172);"
                                            "}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color : lightblue;"
                                            "}"
                                            )
        self.pushButton_Play.clicked.connect(self.PlayClicked)
        self.pushButton_Play.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : rgb(172, 172, 172);"
                                            "}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color : lightblue;"
                                            "}"
                                            )
        self.pushButton_Stop.clicked.connect(self.StopClicked)
        self.pushButton_Stop.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : rgb(172, 172, 172);"
                                            "}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color : lightblue;"
                                            "}"
                                            )
        self.pushButton_Graficar.clicked.connect(self.Graficar)
        self.pushButton_Graficar.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : rgb(172, 172, 172);"
                                            "}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color : lightblue;"
                                            "}"
                                            )
        self.pushButton_Sintetizar.clicked.connect(self.Sintetizar)
        self.pushButton_Sintetizar.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : rgb(172, 172, 172);"
                                            "}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color : lightblue;"
                                            "}"
                                            )

    def PlayOrPause(self):
        if self.play_from_start:
            self.pushButton_Play.setText("PLAY")
        else:
            self.pushButton_Play.setText("PAUSE")

    def setupPyMixer(self):
        # ------------------------------------------------------------------
        # Configuro el mixer de pygame
        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 1024  # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(.8)
        # -----------------------------------------------------------------

    def AbrirClicked(self):
        filename, type_midi = QFileDialog.getOpenFileName(self, "Open file", "", "MIDI(*.mid)")
        self.midi_filename=filename.replace("/", "\\")
        if self.midi_filename!="":
            self.RecieveFile()

    def RecieveFile(self):
        self.midi_file = mido.MidiFile(self.midi_filename)
        self.play_from_start=True
        self.PlayOrPause()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.midi_filename)
        self.clearTracks()
        for i, track in enumerate(self.midi_file.tracks):
            self.tracks_sliders.append(self.buildTrack(i, track.name))

    def buildTrack(self, n, track_name):
        horizontalLayout = QHBoxLayout()

        # label = QLabel(self.scrollAreaWidgetContents)
        label = QCheckBox(self.scrollAreaWidgetContents)
        label.setChecked(True)
        label.setText(str(n) + ". " +track_name)
        horizontalLayout.addWidget(label)

        horizontalSlider = QSlider(self.scrollAreaWidgetContents)
        horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setValue(100)
        horizontalLayout.addWidget(horizontalSlider)

        self.verticalLayout_3.addLayout(horizontalLayout)
        return horizontalSlider

    def clearTracks(self):
        self.tracks_sliders=[]
        for i in reversed(range(self.verticalLayout_3.count())):
            for a in reversed(range(self.verticalLayout_3.itemAt(i).count())):
                self.verticalLayout_3.itemAt(i).itemAt(a).widget().setParent(None)
            self.verticalLayout_3.itemAt(i).setParent(None)

    def GuardarClicked(self):
        save_filename, save_type = QFileDialog.getSaveFileName(self, "Save file", "", "MIDI(*.mid);;WAV(*.wav);;MP3(*.mp3)")
        print(save_filename)
        if save_filename != "":
            if save_type=="MIDI(*.mid)":
                file.save('newsong.mid')
            elif save_type=="WAV(*.wav)":
                fs = FluidSynth(sound_font='font.sf2')
                fs.midi_to_audio(self.midi_filename, save_filename)
            elif save_type == "MP3(*.mp3)":
                fs = FluidSynth(sound_font='font.sf2')
                fs.midi_to_audio(self.midi_filename, save_filename)

    def PlayClicked(self):
        if self.play_from_start:
            self.play_from_start=False
            self.PlayOrPause()
            pygame.mixer.music.play()
        elif pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pushButton_Play.setText("PLAY")
        else:
            pygame.mixer.music.unpause()
            self.pushButton_Play.setText("PAUSE")

    def StopClicked(self):
        pygame.mixer.music.stop()
        self.play_from_start = True
        self.PlayOrPause()

    def Sintetizar(self):
        tracklist=[]
        volumelist=[]
        for i in range(self.verticalLayout_3.count()):
            if not self.verticalLayout_3.itemAt(i).itemAt(0).widget().isChecked():
                tracklist.append(i)
            volumelist.append(self.verticalLayout_3.itemAt(i).itemAt(1).widget().value())
        self.midi_synth=mido.MidiFile(self.midi_filename)

        for a, track in enumerate(self.midi_synth.tracks):
            for msg in track:
                if msg.type=='note_on':
                    msg.velocity = int(msg.velocity*volumelist[a]/100)

        for a in tracklist:
            del self.midi_synth.tracks[a]

        self.midi_synth.save("nowSynth.mid")
        self.play_from_start = True
        self.PlayOrPause()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("nowSynth.mid")
        if self.checkBox_Reverb.isChecked():
            self.reverb_retraso = self.horizontalSlider_Reverb_Retraso.value()
            self.reverb_ganancia = self.horizontalSlider_Reverb_Ganancia.value()
        if self.checkBox_Echo.isChecked():
            self.echo_retraso = self.horizontalSlider_Echo_Retraso.value()
            self.echo_ganancia = self.horizontalSlider_Echo_Ganancia.value()
        if self.checkBox_Flanger.isChecked():
            self.flanger_retraso = self.horizontalSlider_Flanger_Retraso.value()
            self.flanger_ganancia = self.horizontalSlider_Flanger_Ganancia.value()
            self.flanger_freq = self.horizontalSlider_Flanger_Frecuencia.value()

    def Graficar(self):
        pass