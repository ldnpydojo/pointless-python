### Team 4

We decided to complete two topics with one solution and chose to create a synthesizer, or anything with some sound coming out.

We split into two teams and used the `audiolazy` module to create:

N.B. pyAudio may need to be [manually installed](http://people.csail.mit.edu/hubert/pyaudio/)

#### ode2joysynth.py

This takes an input of a list of tuples, where each tuple contains a pitch (using scientific pitch notation) and a duration ( in units of 0.4s).
The notes are turned into frequencies which are played in sequence using a Karplus–Strong string synthesizer and a sinusoidal synthesizer.

#### keyboardsynthesizer.py

This is formed of several files:
*	keyboardsyth-orig.py - Only works on Windows
*	keyboardsynth-allplatform.py - (Hopefully) works on all platforms
*	keyboardsynth-threaded.py - Aims to lose fewer KeyDown events by using the threading library - quick post-Dojo hack.


In their default configuration these files allow the user to play notes on a sythesizer using keys 0-9 on the keyboard (press r to exit)
The files also contain several functions that were used to tinker with `audiolazy`:
*	original_octave() - Plays an octave of notes while playing the note an octave above
*	semitones() - plays each note in an octave in sequence
*	all_notes_in_octave() - plays every note in an octive at once

