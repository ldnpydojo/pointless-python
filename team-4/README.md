###Team 4

We decided to complete two topics with one solution and chose to create a synthesizer, or anything with some sound coming out.

We split into two teams and used the `audiolazy` module to create:

#### ode2joysynth.py

This takes an input of a list of tuples, where each tuple contains a pitch (using scientific pitch notation) and a duration ( in units of 0.4s).
The notes are turned into frequencies which are played in sequence using a Karplus–Strong string synthesizer and a sinusoidal synthesizer.


