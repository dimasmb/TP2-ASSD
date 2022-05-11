import pyaudio
import wave

chunk = 1024


def play(wavToPlay):
    # open the file for reading.
    wf = wave.open(wavToPlay, 'rb')

    # create an audio object

    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    # read data (based on the chunk size)

    data = wf.readframes(chunk)

    # Playing the WAV
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)

        # cleanup stuff.

    stream.close()
    p.terminate()


def getNotesToMidi():
    notesToMidi = [
        {
            'noteName': 'C_1',
            'noteMidiIndex': 0
        },
        {
            'noteName': 'C#_1',
            'noteMidiIndex': 1
        },
        {
            'noteName': 'D_1',
            'noteMidiIndex': 2
        },
        {
            'noteName': 'D#_1',
            'noteMidiIndex': 3
        },
        {
            'noteName': 'E_1',
            'noteMidiIndex': 4
        },
        {
            'noteName': 'F_1',
            'noteMidiIndex': 5
        },
        {
            'noteName': 'F#_1',
            'noteMidiIndex': 6
        },
        {
            'noteName': 'G_1',
            'noteMidiIndex': 7
        },
        {
            'noteName': 'G#_1',
            'noteMidiIndex': 8
        },
        {
            'noteName': 'A_1',
            'noteMidiIndex': 9
        },
        {
            'noteName': 'A#_1',
            'noteMidiIndex': 10
        },
        {
            'noteName': 'B_1',
            'noteMidiIndex': 11
        },
        {
            'noteName': 'C_2',
            'noteMidiIndex': 12
        },
        {
            'noteName': 'C#_2',
            'noteMidiIndex': 13
        },
        {
            'noteName': 'D_2',
            'noteMidiIndex': 14
        },
        {
            'noteName': 'D#_2',
            'noteMidiIndex': 15
        },
        {
            'noteName': 'E_2',
            'noteMidiIndex': 16
        },
        {
            'noteName': 'F_2',
            'noteMidiIndex': 17
        },
        {
            'noteName': 'F#_2',
            'noteMidiIndex': 18
        },
        {
            'noteName': 'G_2',
            'noteMidiIndex': 19
        },
        {
            'noteName': 'G#_2',
            'noteMidiIndex': 20
        },
        {
            'noteName': 'A_2',
            'noteMidiIndex': 21
        },
        {
            'noteName': 'A#_2',
            'noteMidiIndex': 22
        },
        {
            'noteName': 'B_2',
            'noteMidiIndex': 23
        },
        {
            'noteName': 'C_3',
            'noteMidiIndex': 24
        },
        {
            'noteName': 'C#_3',
            'noteMidiIndex': 25
        },
        {
            'noteName': 'D_3',
            'noteMidiIndex': 26
        },
        {
            'noteName': 'D#_3',
            'noteMidiIndex': 27
        },
        {
            'noteName': 'E_3',
            'noteMidiIndex': 28
        },
        {
            'noteName': 'F_3',
            'noteMidiIndex': 29
        },
        {
            'noteName': 'F#_3',
            'noteMidiIndex': 30
        },
        {
            'noteName': 'G_3',
            'noteMidiIndex': 31
        },
        {
            'noteName': 'G#_3',
            'noteMidiIndex': 32
        },
        {
            'noteName': 'A_3',
            'noteMidiIndex': 33
        },
        {
            'noteName': 'A#_3',
            'noteMidiIndex': 34
        },
        {
            'noteName': 'B_3',
            'noteMidiIndex': 35
        },
        {
            'noteName': 'C_4',
            'noteMidiIndex': 36
        },
        {
            'noteName': 'C#_4',
            'noteMidiIndex': 37
        },
        {
            'noteName': 'D_4',
            'noteMidiIndex': 38
        },
        {
            'noteName': 'D#_4',
            'noteMidiIndex': 39
        },
        {
            'noteName': 'E_4',
            'noteMidiIndex': 40
        },
        {
            'noteName': 'F_4',
            'noteMidiIndex': 41
        },
        {
            'noteName': 'F#_4',
            'noteMidiIndex': 42
        },
        {
            'noteName': 'G_4',
            'noteMidiIndex': 43
        },
        {
            'noteName': 'G#_4',
            'noteMidiIndex': 44
        },
        {
            'noteName': 'A_4',
            'noteMidiIndex': 45
        },
        {
            'noteName': 'A#_4',
            'noteMidiIndex': 46
        },
        {
            'noteName': 'B_4',
            'noteMidiIndex': 47
        },
        {
            'noteName': 'C_5',
            'noteMidiIndex': 48
        },
        {
            'noteName': 'C#_5',
            'noteMidiIndex': 49
        },
        {
            'noteName': 'D_5',
            'noteMidiIndex': 50
        },
        {
            'noteName': 'D#_5',
            'noteMidiIndex': 51
        },
        {
            'noteName': 'E_5',
            'noteMidiIndex': 52
        },
        {
            'noteName': 'F_5',
            'noteMidiIndex': 53
        },
        {
            'noteName': 'F#_5',
            'noteMidiIndex': 54
        },
        {
            'noteName': 'G_5',
            'noteMidiIndex': 55
        },
        {
            'noteName': 'G#_5',
            'noteMidiIndex': 56
        },
        {
            'noteName': 'A_5',
            'noteMidiIndex': 57
        },
        {
            'noteName': 'A#_5',
            'noteMidiIndex': 58
        },
        {
            'noteName': 'B_5',
            'noteMidiIndex': 59
        },
        {
            'noteName': 'C_6',
            'noteMidiIndex': 60
        },
        {
            'noteName': 'C#_6',
            'noteMidiIndex': 61
        },
        {
            'noteName': 'D_6',
            'noteMidiIndex': 62
        },
        {
            'noteName': 'D#_6',
            'noteMidiIndex': 63
        },
        {
            'noteName': 'E_6',
            'noteMidiIndex': 64
        },
        {
            'noteName': 'F_6',
            'noteMidiIndex': 65
        },
        {
            'noteName': 'F#_6',
            'noteMidiIndex': 66
        },
        {
            'noteName': 'G_6',
            'noteMidiIndex': 67
        },
        {
            'noteName': 'G#_6',
            'noteMidiIndex': 68
        },
        {
            'noteName': 'A_6',
            'noteMidiIndex': 69
        },
        {
            'noteName': 'A#_6',
            'noteMidiIndex': 70
        },
        {
            'noteName': 'B_6',
            'noteMidiIndex': 71
        },
        {
            'noteName': 'C_7',
            'noteMidiIndex': 72
        },
        {
            'noteName': 'C#_7',
            'noteMidiIndex': 73
        },
        {
            'noteName': 'D_7',
            'noteMidiIndex': 74
        },
        {
            'noteName': 'D#_7',
            'noteMidiIndex': 75
        },
        {
            'noteName': 'E_7',
            'noteMidiIndex': 76
        },
        {
            'noteName': 'F_7',
            'noteMidiIndex': 77
        },
        {
            'noteName': 'F#_7',
            'noteMidiIndex': 78
        },
        {
            'noteName': 'G_7',
            'noteMidiIndex': 79
        },
        {
            'noteName': 'G#_7',
            'noteMidiIndex': 80
        },
        {
            'noteName': 'A_7',
            'noteMidiIndex': 81
        },
        {
            'noteName': 'A#_7',
            'noteMidiIndex': 82
        },
        {
            'noteName': 'B_7',
            'noteMidiIndex': 83
        },
        {
            'noteName': 'C_8',
            'noteMidiIndex': 84
        },
        {
            'noteName': 'C#_8',
            'noteMidiIndex': 85
        },
        {
            'noteName': 'D_8',
            'noteMidiIndex': 86
        },
        {
            'noteName': 'D#_8',
            'noteMidiIndex': 87
        },
        {
            'noteName': 'E_8',
            'noteMidiIndex': 88
        },
        {
            'noteName': 'F_8',
            'noteMidiIndex': 89
        },
        {
            'noteName': 'F#_8',
            'noteMidiIndex': 90
        },
        {
            'noteName': 'G_8',
            'noteMidiIndex': 91
        },
        {
            'noteName': 'G#_8',
            'noteMidiIndex': 92
        },
        {
            'noteName': 'A_8',
            'noteMidiIndex': 93
        },
        {
            'noteName': 'A#_8',
            'noteMidiIndex': 94
        },
        {
            'noteName': 'B_8',
            'noteMidiIndex': 95
        },
        {
            'noteName': 'C_9',
            'noteMidiIndex': 96
        },
        {
            'noteName': 'C#_9',
            'noteMidiIndex': 97
        },
        {
            'noteName': 'D_9',
            'noteMidiIndex': 98
        },
        {
            'noteName': 'D#_9',
            'noteMidiIndex': 99
        },
        {
            'noteName': 'E_9',
            'noteMidiIndex': 100
        },
        {
            'noteName': 'F_9',
            'noteMidiIndex': 101
        },
        {
            'noteName': 'F#_9',
            'noteMidiIndex': 102
        },
        {
            'noteName': 'G_9',
            'noteMidiIndex': 103
        },
        {
            'noteName': 'G#_9',
            'noteMidiIndex': 104
        },
        {
            'noteName': 'A_9',
            'noteMidiIndex': 105
        },
        {
            'noteName': 'A#_9',
            'noteMidiIndex': 106
        },
        {
            'noteName': 'B_9',
            'noteMidiIndex': 107
        },
        {
            'noteName': 'C_10',
            'noteMidiIndex': 108
        },
        {
            'noteName': 'C#_10',
            'noteMidiIndex': 109
        },
        {
            'noteName': 'D_10',
            'noteMidiIndex': 110
        },
        {
            'noteName': 'D#_10',
            'noteMidiIndex': 111
        },
        {
            'noteName': 'E_10',
            'noteMidiIndex': 112
        },
        {
            'noteName': 'F_10',
            'noteMidiIndex': 113
        },
        {
            'noteName': 'F#_10',
            'noteMidiIndex': 114
        },
        {
            'noteName': 'G_10',
            'noteMidiIndex': 115
        },
        {
            'noteName': 'G#_10',
            'noteMidiIndex': 116
        },
        {
            'noteName': 'A_10',
            'noteMidiIndex': 117
        },
        {
            'noteName': 'A#_10',
            'noteMidiIndex': 118
        },
        {
            'noteName': 'B_10',
            'noteMidiIndex': 119
        },
        {
            'noteName': 'C_11',
            'noteMidiIndex': 120
        },
        {
            'noteName': 'C#_11',
            'noteMidiIndex': 121
        },
        {
            'noteName': 'D_11',
            'noteMidiIndex': 122
        },
        {
            'noteName': 'D#_11',
            'noteMidiIndex': 123
        },
        {
            'noteName': 'E_11',
            'noteMidiIndex': 124
        },
        {
            'noteName': 'F_11',
            'noteMidiIndex': 125
        },
        {
            'noteName': 'F#_11',
            'noteMidiIndex': 126
        },
        {
            'noteName': 'G_11',
            'noteMidiIndex': 127
        }
    ]
    return notesToMidi

def getIndexToInstrument():

    indexToInstrument = [
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
        {
            'instrument': 0
        },
    ]
    return indexToInstrument
