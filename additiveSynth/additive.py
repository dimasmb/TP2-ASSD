import overlapAndAdd
from playWav import getNotesToMidi
import wave
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
from scipy import signal
from scipy.io import wavfile

class Additive():

    def __init__(self, instrument):

        self.f0s = []                                               #Harmonic Frequencies of a given wavSample
        self.instrumentType = instrument.Name                       #Instrument Type that is being additive Synthetized
        self.f0sAmplitudes = []                                     #Harmonic Amplitudes of a given wavSample
        self.harmonicCount = 0                                      #Amount of relevant Harmonics of a given wavSample
        self.partials = []                                          #Additive Partials of a given wavSample
        self.additiveSyntethizedSignal = []                         #Syntethized Output Signal
        self.doINeedToPlot = False                                  #If set to True, plots will be generated
        self.doICreateWavSample = True                              #If set to True, WAV Files will be generated
        self.noteNumber = 0                                         #Just to test and label different Note generation

        if self.instrumentType == 'guitar':
            self.f0s.append(195.8299)
            self.f0sAmplitudes.append(7848.82)
            self.harmonicCount = 7
            self.myDelay = 44111

        elif self.instrumentType == 'sax':
            self.f0s.append(252)
            self.f0sAmplitudes.append(262.63)
            self.harmonicCount = 8
            self.myDelay = 39071

        elif self.instrumentType == 'trumpet':
            self.f0s.append(441.1)
            self.f0sAmplitudes.append(1495.3)
            self.harmonicCount = 8
            self.myDelay = 42110

        elif self.instrumentType == 'violin':
            self.f0s.append(436.84)
            self.f0sAmplitudes.append(1204.02)
            self.harmonicCount = 8
            self.myDelay = 43515

        self.wavFilePath = instrument.Name + '.wav'                 #FileName
        self.sampleName = instrument.Name + '.wav'                  #FileName
        self.sampleShortName = self.wavFilePath.replace('.wav','')

    ################################################################
    # Function Name: getTimeSignal                                 #
    # Gets information from Wav File and plots signal in Time      #
    # If normalize TRUE, it will plot between 1 and -1             #
    ################################################################
    def getTimeSignal(self, normalize=False):

        self.fs, self.dataInTime = wavfile.read(self.wavFilePath)

        # Check if wav signal got multiple channels (stereo)
        if self.dataInTime.ndim != 1:
            self.dataInTime = self.dataInTime[:, 0]     # keeping just 1 channel (mono channel)

        if self.dataInTime.shape[0] >=(10**5):
            self.dataInTime = self.dataInTime[0:10**5]
        
        if normalize is True:
            self.dataNorm = []
            for i in self.dataInTime:
                self.dataNorm.append((i/2**16.)*2)      # int 16 format
            self.dataInTime = np.array(self.dataNorm)
        
        self.stepLength = self.dataInTime.shape[0]/self.fs

        self.time = np.linspace(0., self.stepLength, self.dataInTime.shape[0])

        if self.doINeedToPlot == True:
            plt.plot(self.time, self.dataInTime, label= self.sampleName.replace('.wav',''), color='#77DD77')
            plt.legend()
            plt.grid()
            plt.title('Signal in Time')
            plt.xlabel("Time [s]")
            plt.ylabel("Amplitude")
            plt.show()

    ################################################################
    # Function Name: getFrequencySignal                            #
    # Gets information FFT of a WAV signal time                    #
    # WAV Time signal must be initialized before                   #
    ################################################################
    def getFrequencySignal(self):
        # The function computes the 1-D n-point DFT of a real-valued array by means of an FFT

        self.fft = fft.rfft(self.dataNorm)  #ploting this will lose imaginary part
        self.fft = abs(self.fft[:])         #magnitud

        self.freqs = fft.rfftfreq(self.dataInTime.shape[0], d=1./self.fs)

        if self.doINeedToPlot == True:

            plt.plot(self.freqs, self.fft, label= self.sampleName.replace('.wav',''), color='#77DD77')
            plt.legend()
            plt.grid()
            plt.title('Fast Fourier Transform')
            plt.xlabel("Frequency [Hz]")
            plt.ylabel("Amplitude")
            plt.show()

    ################################################################
    # Function Name: getFundamentalFrequency                       #
    # Get Harmonic peaks based on fundamental Frequency provided   #
    # in class constructor. Based on that it will look for rele-   #
    # vant harmonics in f0 * n checking the maximum in +-50 samples#
    ################################################################
    def getFundamentalFrequency(self):
        #assume that the f0 is in the maximum amplitude freq

        self.maxAmplitude = np.amax(self.fft)

        frequencyN = 2

        for i in range(0, len(self.fft)):
            tempData = []
            if(self.freqs[i] > (frequencyN*self.f0s[0])) and (frequencyN <= self.harmonicCount):
                for k in range(i-50, i+50):
                    tempData.append(self.fft[k])
                freqN = max(tempData)

                harmonicIndex = int(np.where(self.fft == freqN)[0])
                harmonicAmplitude = self.fft[harmonicIndex]
                harmonicFreq = self.freqs[harmonicIndex]

                self.f0s.append(harmonicFreq)
                self.f0sAmplitudes.append(harmonicAmplitude)

                frequencyN += 1
        if self.doINeedToPlot == True:

            plt.plot(self.freqs, self.fft, label= self.sampleName.replace('.wav',''), color='#77DD77')
            plt.plot(self.f0s, self.f0sAmplitudes, 's')
            plt.title('FFT with Harmonic Relevant Peaks')
            plt.legend()
            plt.grid()
            plt.xlabel("Frequency [Hz]")
            plt.ylabel("Amplitude")
            plt.show()

    ################################################################
    # Function Name: getADSRforHarmonic                            #
    # Gets envelopes for each partial based on previously calcula- #
    # ted harmonics.                                                #
    ################################################################
    def getADSRforHarmonic(self):

        self.envolvs = []
        self.spectogramTime = np.arange(0,self.dataInTime.shape[0]/self.fs,1/self.fs)
        self.spectogramSampleFreqs,self.spectogramTimeSegments,self.spectogramData = signal.spectrogram(self.dataInTime, self.fs, nperseg=512)

        freqPosition = 0

        for m in range (0, len (self.f0s)):
            for n in range (freqPosition, len(self.spectogramSampleFreqs)):
                if self.spectogramSampleFreqs[n] <= self.f0s[m] and self.spectogramSampleFreqs[n+1] > self.f0s[m]:

                    # I have found my Harmonic within the spectogram

                    partialEnvelope = np.interp(self.spectogramTime,self.spectogramTimeSegments,self.spectogramData[n])

                    # I get the envelope for that harmonic

                    self.envolvs.append(partialEnvelope)

                    freqPosition = n

                    break

        if self.doINeedToPlot == True:
            for harmonicNumber in range(0,len(self.f0s)):
                plt.plot(self.envolvs[harmonicNumber],label= self.sampleName.replace('.wav','') + ' Harmonic N°:' + str (harmonicNumber + 1), color='#77DD77')
                plt.grid()
                plt.title('Envelope for Harmonic Number: ' + str (harmonicNumber + 1) + ' in Time')
                plt.legend()
                plt.xlabel('Samples')
                plt.ylabel('Amplitude')
                plt.show()

    ################################################################
    # Function Name: additiveSynthetizer                           #
    # It creates synthetized signal based on envelopes previosuly  #
    # calculated and harmonics                                     #
    # Final result is the synth instrument                         #
    # If syntethizeNote set to TRUE                                #
    # It synthetizes the note based on that                        #
    # It creates wav file with synthetized signal                  #
    ################################################################
    def additiveSynthetizer(self, syntethizeNote = False, delayInTime = 0):
        maxLength = 0
        normalizer = 0
        self.partials = []
        self.additiveSyntethizedSignal = []

        for i in range(0,len(self.envolvs)):
            if maxLength < len(self.envolvs[i]):
                maxLength = len(self.envolvs[i])

        for i in range(0,len(self.envolvs)):
            if maxLength > len(self.envolvs[i]):
                empty = np.zeros(maxLength - len(self.envolvs[i]))
                self.envolvs[i] = np.concatenate([self.envolvs[i], empty])

        samples = np.arange(len(self.envolvs[0])) / self.fs

        for i in range(0,len(self.f0s)):
            partialSum = np.sin(2*np.pi*self.f0s[i]*samples)
            partialSum = np.multiply(partialSum,self.envolvs[i])
            normalizer = normalizer + np.amax(self.envolvs[i])

            self.partials.append(partialSum)

        for i in range(0,len(self.partials[0])):
            finalValue = 0

            for j in range(0,len(self.partials)):
                finalValue = finalValue + self.partials[j][i]

            self.additiveSyntethizedSignal.append(finalValue)


        self.addDelayNote = np.zeros(int (self.myDelay * delayInTime))
        self.additiveSyntethizedSignal = np.concatenate([self.addDelayNote, self.additiveSyntethizedSignal ])
        self.additiveSyntethizedSignal = [i*(1/normalizer) for i in self.additiveSyntethizedSignal]
        self.additiveSyntethizedSignalForWav = [i*32767 for i in self.additiveSyntethizedSignal]
        self.additiveSyntethizedSignalForWav = np.int16(self.additiveSyntethizedSignalForWav)

        if self.doINeedToPlot == True:

            ## In Time

            plt.plot(self.time, self.dataInTime, label= self.sampleName.replace('.wav',''), color='#77DD77')
            plt.plot(self.time, self.additiveSyntethizedSignal, label= self.sampleName.replace('.wav','') + ' Syntethized', color='#FCB7AF', alpha=0.5)
            plt.legend()
            plt.grid()
            plt.title('Signal in Time')
            plt.xlabel("Time [s]")
            plt.ylabel("Amplitude")
            plt.show()

            ## In frequency

            self.fftSynthetized = fft.rfft(self.additiveSyntethizedSignal)  # If we plot this, we lose imaginary part
            self.fftSynthetized = abs(self.fftSynthetized[:])  # Calculating magnitude
            self.freqsSynthetized = fft.rfftfreq(len(self.additiveSyntethizedSignal), d=1. / self.fs)

            plt.plot(self.freqs, self.fft, label= self.sampleName.replace('.wav',''), color='#77DD77')
            plt.plot(self.freqsSynthetized, self.fftSynthetized, label= self.sampleName.replace('.wav','') + ' Syntethized', color='#FCB7AF',alpha=0.5)
            plt.legend()
            plt.grid()
            plt.title('Fast Fourier Transform')
            plt.xlabel("Frequency [Hz]")
            plt.ylabel("Amplitude")
            plt.show()


        if self.doICreateWavSample == True:

            self.noteNumber = self.noteNumber + 1
            wavfile.write(self.sampleName.replace('.wav','') + '-syntethized' + str(self.noteNumber) + '.wav', self.fs, self.additiveSyntethizedSignalForWav)

        if syntethizeNote == True:

            self.f0s = []
            self.f0sAmplitudes = []

            if self.instrumentType == 'guitar':
                self.f0s.append(195.8299)
                self.f0sAmplitudes.append(7848.82)
                self.harmonicCount = 7

            elif self.instrumentType == 'sax':
                self.f0s.append(252)
                self.f0sAmplitudes.append(262.63)
                self.harmonicCount = 17

            elif self.instrumentType == 'trumpet':
                self.f0s.append(441.1)
                self.f0sAmplitudes.append(1495.3)
                self.harmonicCount = 11

            elif self.instrumentType == 'violin':
                self.f0s.append(436.84)
                self.f0sAmplitudes.append(1204.02)
                self.harmonicCount = 9

            self.getFundamentalFrequency()
            self.getADSRforHarmonic()

    ################################################################
    # Function Name: noteFromAdditiveSynthetizer                   #
    # Creates a note from a given synthetized additive instrument  #
    # It receives which note in string Name or in Midi Format      #
    # and its duration                                             #
    ################################################################
    def noteFromAdditiveSynthetizer(self, midiNote, midiNoteTime,delayInTime = 0):

        midiNoteTime = 44078 * midiNoteTime

        noteF0 = self.convertFromMidiToF0(midiNote)                     #I get fundamental frequency of a given note

        self.f0s = np.arange(noteF0, noteF0 * self.harmonicCount, noteF0)

        for i in range(0, len(self.envolvs)):

            tempTimeForNote = np.linspace(0, len(self.envolvs[i]), len(self.envolvs[i]))

            envelopeTimeToNoteTime = midiNoteTime / len(self.envolvs[i])

            timeFunction = envelopeTimeToNoteTime * tempTimeForNote

            self.envolvs[i] = overlapAndAdd.olaAlgorithm(self.envolvs[i], np.ones(250), timeFunction, 0)

        self.additiveSynthetizer(syntethizeNote=True,delayInTime=delayInTime)

    ################################################################
    # Function Name: createMusicToTest                             #
    # Creates a wav music file from a given array of notes         #
    # with same duration for all notes                             #
    ################################################################
    def createMusicToTest(self, music, allNoteDurationInSeconds,wavMusic):

        notesInMidi = getNotesToMidi()

        infiles = []
        num = 2

        noteDuration = allNoteDurationInSeconds

        for note in music:
            noteIndex = next((index for (index, d) in enumerate(notesInMidi) if d["noteName"] == note), None)
            self.noteFromAdditiveSynthetizer(int (notesInMidi[noteIndex]["noteMidiIndex"]), noteDuration)
            infiles.append(str(self.sampleShortName) + "-syntethized" + str(num) + ".wav")
            num = num + 1

        data= []

        for infile in infiles:

            w = wave.open(infile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()

        output = wave.open(wavMusic, 'wb')
        output.setparams(data[0][0])

        for i in range (0,len(infiles)):
            output.writeframes(data[i][1])

        output.close()

    ################################################################
    # Function Name: createChord                                   #
    # Creates a chord based on array of notes                      #
    # with same duration for all notes                             #
    ################################################################
    def createChord(self,noteChords,noteChordDurationInSeconds,wavChordOutput):

        soundNotesWav = []

        notesInMidi = getNotesToMidi()

        num = 1

        infiles = []

        start = 0

        self.doICreateWavSample = False

        for note in noteChords:

            noteIndex = next((index for (index, d) in enumerate(notesInMidi) if d["noteName"] == note), None)

            if start == 0:

                self.noteFromAdditiveSynthetizer(notesInMidi[noteIndex]["noteMidiIndex"], noteChordDurationInSeconds)
                self.newChord = self.additiveSyntethizedSignal
            elif start != 0:

                self.noteFromAdditiveSynthetizer(notesInMidi[noteIndex]["noteMidiIndex"], noteChordDurationInSeconds)
                self.newChord = np.add(self.newChord, self.additiveSyntethizedSignal)

            start = start + 1

        max = np.amax(self.newChord)

        self.newChordTemp = [i*(1/max) for i in self.newChord]
        self.newChordForWav = [i*32767 for i in self.newChordTemp]
        self.newChordForWav = np.int16(self.newChordForWav)

        wavfile.write(wavChordOutput, self.fs, self.newChordForWav)

        self.doICreateWavSample = True

    def convertFromMidiToF0(self,midiNoteValue):

        # https://newt.phys.unsw.edu.au/jw/notes.html#:~:text=m%20for%20the%20note%20A4,)%2F12(440%20Hz).

        f0 = 2 ** ((midiNoteValue - 69) / 12) * 440

        return f0
