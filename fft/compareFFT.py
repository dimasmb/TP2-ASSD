import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy import signal


#########################################
# Compare FFT                           #
# Compares FFT generated in C and       #
# FFT from Scipy Python Library         #
# Plots both results                    #
#########################################

def compareFFT (fileNameForTime,fileNameForFreq):

    #########################################
    # Open File with DataSet generated in C #
    # First Line: Sampling Frequency        #
    # Second Line: dataSet in Time          #
    #########################################

    dataSet = open(fileNameForTime,"r")
    fileData = dataSet.readlines()
    fileWithDataInFreq = open(fileNameForFreq,"r")
    fileDataInFreq = fileWithDataInFreq.readlines()

    # Sample spacing

    T = 1.0 / float(fileData[0])

    #########################################
    # Dataset with Signal in Time           #
    #########################################

    fileData = fileData[1].split(",")
    dataSet.close()

    y = [float(i) for i in fileData]
    x = np.linspace(0.0, len(y) * T, len(y))

    #################################################################
    # Python Signal in Frequency (To Compare)                       #
    # using FFT                                                     #
    # https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html  #
    #################################################################

    xPythonFourier = fftfreq(len(y), T)[:len(y)//2]
    yPythonFourier = fft(y)

    #########################################
    # C Signal in Frequency                 #
    #########################################

    fileDataInFreq = fileDataInFreq[0].split(",")
    fileWithDataInFreq.close()
    fileDataInFreqFloat = [float(i) for i in fileDataInFreq]
    fileDataInFreqToPlot = []

    for i in range(len(fileDataInFreqFloat)//2):
        fileDataInFreqToPlot.append(fileDataInFreqFloat[i] * 2.0 / len(y))

    #########################################
    # Plots in Time                         #
    #########################################

    plt.plot (x, y, label = "Signal From DataSet (C generated)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (V)")
    plt.title("Sample Signal in Time")
    plt.grid()
    plt.legend()
    plt.show()

    #########################################
    # Plots in Frequency                    #
    #########################################

    # FFT Generated in Python
    plt.plot(xPythonFourier, 2.0/len(y) * np.abs(yPythonFourier[0:len(y)//2]), label = "Generated in Python",linewidth=2)

    # FFT Generated in C
    plt.plot (xPythonFourier, fileDataInFreqToPlot, label = "Generated in C",linewidth=1)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Sample Signal in Frequency")
    plt.grid()
    plt.legend()
    plt.show()

compareFFT("dataSet.txt","outputDataSet.txt")
