# Project modules
import mido
import numpy as np
import pandas as pd
from mido import MidiFile

from src.app import main

if __name__ == "__main__":
    main()

# carga de archivo y visualización de la estructura
# archivo_midi = MidiFile('concierto_de_aranjuez.mid')
# print('info', archivo_midi)
# print('length', archivo_midi.length)
# print('charset', archivo_midi.charset)
# print('ticks_per_beat', archivo_midi.ticks_per_beat)