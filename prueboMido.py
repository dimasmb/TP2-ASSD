import pygame
import mido

def play_music(midi_filename):
    '''Stream music_file in a blocking manner'''
    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)  # check if playback has finished


file=mido.MidiFile('La_pantera_rosa.mid')
newmidi=mido.MidiFile(type=file.type, ticks_per_beat=file.ticks_per_beat)

for i, track in enumerate(file.tracks):
    # print('Track {}: {}'.format(i, track.name)) #Me fijo los tracks que tiene
    newmidi.tracks.append(track)
    newtrack=mido.MidiTrack(track)
    newmidi.tracks.append(newtrack)

for i, track in enumerate(newmidi.tracks):
    print('Track {}: {}'.format(i, track.name))
    if i%2:
        first=True
        for msg in track:
            if msg.type=='note_on' and msg.velocity==0:
                # first=False
                msg.time=msg.time+5

newmidi.save('newsong.mid')    #guardo el midi modificado con un nuevo nombre
midi_filename = 'newsong.mid'
#------------------------------------------------------------------
# Configuro el mixer de pygame
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024  # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(.8)
#-----------------------------------------------------------------
# Pongo play y escucho interrumpciones
try:
    # use the midi file you just saved
    play_music(midi_filename)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit