from additive import Additive
from instrument import Instrument
from playWav import play
from playWav import getNotesToMidi

if __name__ == '__main__':

    # It can be guitar, trumpet, violin or saxo
    instrument = Instrument("violin")

    # Happy Birthday Sample

    #music = ["C_05","C_05","D_05","C_05","F_05","E_05","C_05","C_05","D_05","C_05","G_05","F_05"]

    # Chord B
    chord = ["G_04","B_04","D_04"]

    myInstrument = Additive(instrument)
    myInstrument.doINeedToPlot = True
    myInstrument.getTimeSignal(normalize=True)
    myInstrument.getFrequencySignal()
    myInstrument.getFundamentalFrequency()
    myInstrument.getADSRforHarmonic()
    myInstrument.additiveSynthetizer()
    #myInstrument.noteFromAdditiveSynthetizer(60,1,1)
    #myInstrument.noteFromAdditiveSynthetizer(60,1,2)
    #myInstrument.noteFromAdditiveSynthetizer(60,1,3)
    #myInstrument.noteFromAdditiveSynthetizer(60,1,4)
    #myInstrument.createMusicToTest(music=music, allNoteDurationInSeconds = 0.25, wavMusic="music.wav")
    #play("music.wav")

    myInstrument.createChord(noteChords=chord, noteChordDurationInSeconds=3,wavChordOutput="chordOutput.wav")
    play("chordOutput.wav")