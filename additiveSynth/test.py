import wave
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
from scipy import signal
from scipy.io import wavfile
from scipy.signal import spectrogram

fs, dataTime = wavfile.read('guitar.wav')
print(dataTime.ndim)
print(fs)

plt.specgram(dataTime, fs)
plt.grid(True, which='both')
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.show()