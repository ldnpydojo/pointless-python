from audiolazy import *

octave = [
    ('C', 261.63,),
    ('C#', 277.18,),
    ('D', 293.66,),
    ('E#', 311.13,),
    ('E', 329.63,),
    ('F', 349.23,),
    ('F#', 369.99,),
    ('G', 392.00,),
    ('A#', 415.30,),
    ('A', 440.00,),
    ('B#', 466.16,),
    ('B', 493.88,),
]


rate = 44100 # Sampling rate, in samples/second
s, Hz = sHz(rate) # Seconds and hertz
ms = 1e-3 * s

def original_octave():
    for note_name, freq in octave:
        note1 = karplus_strong(freq * Hz) # Pluck "digitar" synth
        note2 = zeros(300 * ms).append(karplus_strong(2*freq * Hz))
        notes = (note1 + note2) * .5
        sound = notes.take(int(2 * s)) # 2 seconds of a Karplus-Strong note
        with AudioIO(True) as player: # True means "wait for all sounds to stop"
            player.play(sound, rate=rate)


def semitones():
    for note_name, freq in octave:
        note1 = karplus_strong(freq * Hz) # Pluck "digitar" synth
        # note2 = zeros(300 * ms).append(karplus_strong(2*freq * Hz))
        # notes = (note1 + note2) * .5
        sound = note1.take(int(.5 * s)) # 2 seconds of a Karplus-Strong note
        with AudioIO(True) as player: # True means "wait for all sounds to stop"
            player.play(sound, rate=rate)

#semitones()


def all_notes_in_octave():
    notes = None
    for note_name, freq in octave:
        note = karplus_strong(freq * Hz)
        if notes is None:
            notes = note
        else:
            notes = notes + note

    sound = notes.take(int(.5 * s))
    with AudioIO(True) as player:
        player.play(sound, rate=rate)

#play_octave()

def play_note(note_nr):
    note = karplus_strong(octave[note_nr-1][1] * Hz)
    sound = note.take(int(.2 * s))
    with AudioIO(True) as player:
        player.play(sound, rate=rate)
        

def main():
    while True:
        import msvcrt
        char = msvcrt.getch()#
        if char == 'r':
            return
        play_note(int(char))

main()