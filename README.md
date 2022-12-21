# GuitarModes
Blending my passion for guitar with my desire to learn software development.

## Overview
I have been playing guitar for 13 years. Until this spring, I did not know any music theory beyond a few things:
* Major / Minor Triads
* Pentatonic Scale (Four-Five frets worth)
  * Flattened Fifth Note
* Major Scale from the Ionian Mode through the first octave of Phrygian.

Recently, I have been learning music theory. It's dramatically changed the way I see the guitar. A ton of things are falling into place. (Learning songs, writing music, being able to think of my riffs in terms of notes, etc...)

This project is the synthesis of my desires to learn software development and music theory. This application will provide the user with tools to practice scales and other music theory bits.

## Plans
### My plans from basic to incredibly ambitious are:
 - [x] Establish a way to generate a fretboard in plaintext that reflects a theoretical fretboard.
 - [x] Integrate hz and octaves, differentiate based on that instead of arbitrary index values.
 - [X] Modify getFretBoard.py such that it displays octaves of the notes (targeting version 0.23)
 - [ ] Modify getFretBoard such that it is object oriented.
 - [ ] Modify getFredboard.py such that the notes are all padded w/ spacing.
 - [ ] Establish clear definitions and use cases separating 'Aristotelian' Notes from 'Octave Defined' notes. (My language limiting my world, again.)
 - [ ] Dynamically emphasize different notes corresponding to different music theory concepts.
 - [ ] Implement ASIO integration--monitor input--come up with a very basic Rocksmith type thing for practicing.
 - [ ] Make a mobile version.

### Examples:
* What's a full tone higher than a C note?
* To which major or minor scale does C Locrian belong?
* To which scale does the following sequence of notes belong? 
 * C-D-E-F-G-A-B-C
* The highlighted notes belong to which scale?
* The highlighted notes belong to which mode?
* What are the notes of the C Dorian Mode?

## Anticipated Changes
* Ability to use either sharp or flat notes. 
  * Typically, Major keys' B, E, A, D, and G's accidentals are referred to by flats and not sharps.
  * Typically, Minor keys' B and E's accidentals are referred to by flats and not sharps.
* Depending on how I approach the algorithms to quiz you on key signatures / scale positions / modes...
  * It's going to be a problem that the current system cannot account for octaves of notes. I may simply have to use frets as a fulcrum.