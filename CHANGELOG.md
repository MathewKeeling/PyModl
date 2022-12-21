# Changelog
## Version 0.26 - 2022-12-
* Created a circle of fifths generator

## Version 0.25 - 2022-12-21
* Updated Changelog
  * Changed dates from YYYY/MM/DD to YYYY-MM-DD.
  * Added some missing dates.
  * Moved it to its own file: CHANGELOG.md
* Moved py files into a lib directory

## Version 0.24 - 2022-12-21
* Improved Readability on code.
* I neglected to include a version number, but it's PR #2

## Version 0.23 - 2022-05-30
* Fretboard now generates fretboard w/ Pitch Notation.
* Updated goals to incldue making get_fretboard object oriented
  * This would allow for easily selecting different views.
  * It would probably be advisable to add a non Pitch Notation value/attribute to each note arrayIndex/object.

## Version 0.22875 - 2022-05-29
* Achilles Paradox
* Renamed get_note_library.py to pitch_notation
  * Refactored. Reduced redundancy. Made it easier to read.
  * It's purpose is more clear now.
  * Generates HPN and SPN names.
    * Helmholtz Pitch Notation
    * Scientific Pitch Notation

## Version 0.2275 - 2022-05-29
* Hilarious version numbers
* Cleaned up resources. (Modes, Keys, Alphabet)
* Help from M.S. using delegation to clean up the methods in generateNoteLibrary.py

## Version 0.225 - 2022-05-10
* Fixed the getScale.py function to not produce unintelligble messes of output
* Added pretty print and better naming of output.
* Updated goals.
### Sample Output from getScale.py
```
 G minor Key Signature: ['G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G']
    G Ionian
       ['G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G']
    A Dorian
       ['A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'A']
    A♯/B♭ Phrygian
       ['A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭']
    C Lydian
       ['C', 'D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C']
    D Mixolydian
       ['D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D']
    D♯/E♭ Natural Minor (Aeolian)
       ['D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭']
    F Locrian
       ['F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F']
```

## Verson 0.22 - 2022-05-10
* Implemented a means to generate hemholtz name
* Implemented method that makes the generation of the hemholtz and scientific names conform to DRY principles
  * Factored out the common factor between hemholtz and scientific so its abstract

### Sample code from the fretboard generation
#### Note that version 0.23 will have octave numerals included in the names:
```
['C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C']
['G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G']
['C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C']
['F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F']
['A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A']
['D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D']
```

## Version 0.21 2022-05-10
* Renamed versioning scheme.
  * Added a digit following the decimal.
* First version 0.2X
* Implemented a means to generate the code to store the names of everything in a list.
  ### Sample Output
    ```
    ...
    [36, "", "G#3/Ab3", 207.65234878997256],
    [37, "", "A3", 220.0],
    [38, "", "A#3/Bb3", 233.08188075904496],
    [39, "", "B3", 246.94165062806206],
    [40, "", "C4", 261.6255653005986],
    [41, "", "C#4/Db4", 277.1826309768721],
    [42, "", "D4", 293.6647679174076],
    [43, "", "D#4/Eb4", 311.1269837220809],
    [44, "", "E4", 329.6275569128699],
    [45, "", "F4", 349.2282314330039],
    [46, "", "F#4/Gb4", 369.9944227116344],
    [47, "", "G4", 391.99543598174927],
    [48, "", "G#4/Ab4", 415.3046975799451],
    ...
    ```

## Version 0.15 - 2022-05-08
* First Working Version
  * I'm going to break this going forward.
  * I need to implement a method to differentiate between keys via hz and octave. Currenly everything is just relative to some indexes I came up with.
  * More information here: https://www.ece.iastate.edu/~alexs/classes/2016_Spring_575/HW/HW5/files/piano-key-freq-wikipedia.pdf 


## Version 0.14 - 2022-04-19
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

## Version 0.13 - 2022-04-01
* Implemented intonation flag.
* I'm tired

```
# Sample output
A# minor
['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']
Fb minor
['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
```


## Version 0.12 - 2022-04-01
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

## Version 0.11 - 2022-03-31
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