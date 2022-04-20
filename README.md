# GuitarModes
Blending my passion for guitar with my desire to learn software development.

## Overview
When I played guitar as a kid I fundamentally didn't understand the way modes / positions of the major scale worked.

Recently, I have been learning music theory. I am understanding things a lot more clearly now.

I want to make an app that helps with recall for various aspects of guitar playing...

Visualization of the fret board w/ different tunings.

CAGED review, modes and positions, etc.

We'll see where this goes.

## Plans
First I want to establish a way to generate a fretboard in plaintext that reflects a theoretical fretboard.

I would then like to dynamically emphasize different notes corresponding to different music theory concepts.

The goal is to create something that is interactive and/or demonstrative for learning purposes.

### Examples:
* What's a full tone higher than a C note?
* To which major or minor scale does C Locrian belong?
* To which scale does the following sequence of notes belong? 
 * C-D-E-F-G-A-B-C
* The highlighted notes belong to which scale?
* The highlighted notes belong to which mode?
* What are the notes of the C Dorian Mode?


## Changelog

### Version 0.4 - 2022/04/19
* Neglected changelog for three weeks
* Refactored some bits.
* Added the ability to generate modes and select them.

```
#  sample output
Key of F.
F key signature: 
['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F']
F Ionian
['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F']
G Dorian
['G', 'A', 'A#', 'C', 'D', 'E', 'F', 'G']
A Phrygian
['A', 'A#', 'C', 'D', 'E', 'F', 'G', 'A']
A# Lydian
['A#', 'C', 'D', 'E', 'F', 'G', 'A', 'A#']
C Mixolydian
['C', 'D', 'E', 'F', 'G', 'A', 'A#', 'C']
D Natural Minor (Aeolian)
['D', 'E', 'F', 'G', 'A', 'A#', 'C', 'D']
E Locrian
['E', 'F', 'G', 'A', 'A#', 'C', 'D', 'E']
```

### Version 0.3 - 2022/04/01
* Implemented intonation flag.
* I'm tired

```
# Sample output
A# minor
['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']
Fb minor
['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
```


### Version 0.2 - 2022/04/01
* renamed python files for fretboard and scales
* created a functional generator for scales of both major and minor, without a working flag for sharpness
```
# Sample output
MAJOR SCALES
         A major
         ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A']
         B major
         ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']
         C major
         ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
         D major
         ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']
         E major
         ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
         F major
         ['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F']
         G major
         ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']
MINOR SCALES
         A minor
         ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
         B minor
         ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B']
         C minor
         ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#', 'C']
         D minor
         ['D', 'E', 'F', 'G', 'A', 'A#', 'C', 'D']
         E minor
         ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
         F minor
         ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#', 'F']
         G minor
         ['G', 'A', 'A#', 'C', 'D', 'D#', 'F', 'G']
```

### Version 0.1 - 2022/03/31
Everything you see here:
* Goals described
* Made a method to generate all the notes of a fretboard
* I'm tired.

```
# Sample output
['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']
['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D']
['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
```
