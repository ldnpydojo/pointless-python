#! /usr/bin/env python
from audiolazy import *

ode = [
    ('e4', 1), ('e4', 1), ('f4', 1), ('g4', 1), ('g4', 1), ('f4', 1), ('e4', 1),
    ('d4', 1),
    ('c4', 1), ('c4', 1), ('d4', 1), ('e4', 1), ('e4', 1.5), ('d4', 0.5), ('d4', 2.0)
] + [
    ('e4', 1), ('e4', 1), ('f4', 1), ('g4', 1), ('g4', 1), ('f4', 1), ('e4', 1),
    ('d4', 1),
    ('c4', 1), ('c4', 1), ('d4', 1), ('e4', 1), ('d4', 1.5), ('c4', 0.5), ('c4', 2.0)
]


rate = 44100 # Sampling rate, in samples/second
s, Hz = sHz(rate) # Seconds and hertz
ms = 1e-3 * s
notes_played = None
for i, (n, dur) in enumerate(ode):
    gen = karplus_strong if i < len(ode) // 2 else sinusoid # Chooses the
    # generator depending on where we are in the song
    freq = str2freq(n) # Translates string notation to frequency
    new_note = gen(freq * Hz).take(dur * .4 * s)
    if notes_played is None:
        notes_played = new_note
    else:
        notes_played += new_note

with AudioIO(True) as player: # True means "wait for all sounds to stop"
      player.play(notes_played, rate=rate)
