#  this file will store the modes of the Major scale in all keys
#  https://blog.landr.com/music-modes/

#  How to Construct Major & Minor Scales
#    https://hubguitar.com/music-theory/constructing-the-minor-scale
#  How to Construct Major Scales
#    "Whole, Whole, Half, Whole, Whole, Whole, Half"
#  How to Construct Minor Scales
#    "Whole, Half, Whole, Whole, Half, Whole, Whole"

#  3 notes per string scales/modes form
#  https://www.anyonecanplayguitar.co.uk/three-note-per-string-scales/
    #  F Ionian through E Locrian

#  C Major Scale Bias
#  https://music.stackexchange.com/questions/17760/why-is-music-theory-built-so-tightly-around-the-c-major-scale

#  If you want to build a mode of the major scale:
#  Know that there are seven modes of the major scale:
#    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Locrian
#    A good mnemonic is: I Don't Particularly Like Modes A Lot
#      IDPLMAL
#  To generate a mode, start at the nth degree of the scale through
#    its succeeding octave

#  If you want to find the parent scale of a particular mode:
#  Take the [(X) (Mode)] and count backwards
#  Example: C Phrygian
#    Phrygian is the third degree of a particular scale.
#    Count backwards from three, starting at the letter C
#      3: C
#      2: B
#      1: A
#    C Phrygian is a member of the A Major Scale
#    Parent scale: A Major

aMajorsScale = {
    'key'   :        ['A'],
    'tonality':      ['major'],
    'ionian':        ['A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A'],
    'dorian':        ['B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B'],
    'phrygian':      ['C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭'],
    'lydian':        ['D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D'],
    'mixolydian':    ['E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E'],
    'aeolian':       ['F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭'],
    'locrian':       ['G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭']
}

bMajorsScale = {
    'key'   :        ['B'],
    'tonality':      ['major'],
    'ionian':        ['B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B'],
    'dorian':        ['C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭'],
    'phrygian':      ['D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭'],
    'lydian':        ['E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E'],
    'mixolydian':    ['E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E'],
    'aeolian':       ['F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭'],
    'locrian':       ['A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭']
}

cMajorScale = {
    'key'   :        ['C'],
    'tonality':      ['major'],
    'ionian':        ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
    'dorian':        ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
    'phrygian':      ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'],
    'lydian':        ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
    'mixolydian':    ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'aeolian':       ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
    'locrian':       ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
}

dMajorsScale = {
    'key'   :        ['D'],
    'tonality':      ['major'],
    'ionian':        ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
    'dorian':        ['E', 'F#', 'G', 'A', 'B', 'C#', 'D', 'E'],
    'phrygian':      ['F#', 'G', 'A', 'B', 'C#', 'D', 'E', 'F#'],
    'lydian':        ['G', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G'],
    'mixolydian':    ['A', '', '', '', '', '', '', ''],
    'aeolian':       ['B', '', '', '', '', '', '', ''],
    'locrian':       ['C#', '', '', '', '', '', '', '']
}

eMajorsScale = {
    'key'   :        ['E'],
    'tonality':      ['major'],
    'ionian':        ['', '', '', '', '', '', '', ''],
    'dorian':        ['', '', '', '', '', '', '', ''],
    'phrygian':      ['', '', '', '', '', '', '', ''],
    'lydian':        ['', '', '', '', '', '', '', ''],
    'mixolydian':    ['', '', '', '', '', '', '', ''],
    'aeolian':       ['', '', '', '', '', '', '', ''],
    'locrian':       ['', '', '', '', '', '', '', '']
}

fMajorsScale = {
    'key'   :     ['F'],
    'tonality':   ['major'],
    'ionian':        ['', '', '', '', '', '', '', ''],
    'dorian':        ['', '', '', '', '', '', '', ''],
    'phrygian':      ['', '', '', '', '', '', '', ''],
    'lydian':        ['', '', '', '', '', '', '', ''],
    'mixolydian':    ['', '', '', '', '', '', '', ''],
    'aeolian':       ['', '', '', '', '', '', '', ''],
    'locrian':       ['', '', '', '', '', '', '', '']
}

gMajorsScale = {
    'key'   :        ['G'],
    'tonality':      ['major'],
    'ionian':        ['G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G'],
    'dorian':        ['A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A'],
    'phrygian':      ['B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B'],
    'lydian':        ['C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C'],
    'mixolydian':    ['D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D'],
    'aeolian':       ['E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E'],
    'locrian':       ['F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭']
}



#  debug
#for entry in cMajorScale:
#    print(entry)
#    print('\t', cMajorScale[entry])