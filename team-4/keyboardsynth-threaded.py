#! /usr/bin/env python

# Joe's attempt to make receiving note signals more reliable by using the python
# threading tutorial - limited success
from audiolazy import *
import sys
import threading

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

class play_note(threading.Thread):
    
    def __init__(self, note_nr):
        threading.Thread.__init__(self)
        self.note_nr = note_nr
    def run(self):
        note = karplus_strong(octave[self.note_nr-1][1] * Hz)
        sound = note.take(int(.2 * s))
        with AudioIO(True) as player:
            player.play(sound, rate=rate)

#get_ch()
#Some friendly folks from stackoverflow.com found a cross-platform solution to
#grab a character from the cmd prompt
# http://code.activestate.com/recipes/134892/
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except AttributeError:
                self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys, termios # import termios now or else you'll get the Unix version on the Mac

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        import Carbon
        Carbon.Evt #see if it has this (in Unix, it doesn't)

    def __call__(self):
        import Carbon
        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''
        else:
            #
            # The event contains the following info:
            # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            #
            # The message (msg) contains the ASCII char which is
            # extracted with the 0x000000FF charCodeMask; this
            # number is converted to an ASCII character with chr() and
            # returned
            #
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg & 0x000000FF)


def main():
    print "press r to finish playing!"
    #original_octave() Plays an octave of notes while playing the note an octave above
    #semitones() plays each note in an octave in sequence
    #all_notes_in_octave() plays every note in an octive at once
    getch=_Getch()
    while True:
        char = getch()
        print char
        if char == 'r':
            return
        try:
            background = play_note(int(char))
            background.start()
        except ValueError:
            print "You should be using integers only!"
main() 
