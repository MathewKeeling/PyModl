#  this file will store the modes of the Major scale in all keys
#  https://blog.landr.com/music-modes/

#  How to Construct Major & Minor Scales
#    https://hubguitar.com/music-theory/constructing-the-minor-scale
#  How to Construct Major Scales
#    "Whole, Whole, Half, Whole, Whole, Whole, Half"
#  How to Construct Minor Scales
#    "Whole, Half, Whole, Whole, Half, Whole, Whole"

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
    'key'   :     ['A'],
    'tonality':   ['major'],
    'ionian':        ['', '', '', '', '', '', '', ''],
    'dorian':        ['', '', '', '', '', '', '', ''],
    'phrygian':      ['', '', '', '', '', '', '', ''],
    'lydian':        ['', '', '', '', '', '', '', ''],
    'mixolydian':    ['', '', '', '', '', '', '', ''],
    'aeolian':       ['', '', '', '', '', '', '', ''],
    'locrian':       ['', '', '', '', '', '', '', '']
}

bMajorsScale = {
    'key'   :     ['B'],
    'tonality':   ['major'],
    'ionian':        ['', '', '', '', '', '', '', ''],
    'dorian':        ['', '', '', '', '', '', '', ''],
    'phrygian':      ['', '', '', '', '', '', '', ''],
    'lydian':        ['', '', '', '', '', '', '', ''],
    'mixolydian':    ['', '', '', '', '', '', '', ''],
    'aeolian':       ['', '', '', '', '', '', '', ''],
    'locrian':       ['', '', '', '', '', '', '', '']
}

cMajorScale = {
    'key'   :       ['C'],
    'tonality':     ['major'],
    'c_ionian':     ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
    'd_dorian':     ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
    'e_phrygian':   ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'],
    'f_lydian':     ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
    'g_mixolydian': ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'a_aeolian':    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
    'b_locrian':    ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
}

dMajorsScale = {
    'key'   :       ['D'],
    'tonality':     ['major'],
    'd_ionian':     ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
    'e_dorian':     ['E', 'F#', 'G', 'A', 'B', 'C#', 'D', 'E'],
    'f#_phrygian':  ['F#', 'G', 'A', 'B', 'C#', 'D', 'E', 'F#'],
    'g_lydian':     ['G', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G'],
    'a_mixolydian': ['A', '', '', '', '', '', '', ''],
    'b_aeolian':    ['B', '', '', '', '', '', '', ''],
    'c#_locrian':   ['C#', '', '', '', '', '', '', ''],
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
    'key'   :     ['G'],
    'tonality':   ['major'],
    'ionian':        ['', '', '', '', '', '', '', ''],
    'dorian':        ['', '', '', '', '', '', '', ''],
    'phrygian':      ['', '', '', '', '', '', '', ''],
    'lydian':        ['', '', '', '', '', '', '', ''],
    'mixolydian':    ['', '', '', '', '', '', '', ''],
    'aeolian':       ['', '', '', '', '', '', '', ''],
    'locrian':       ['', '', '', '', '', '', '', '']
}




#  debug
for entry in cMajorScale:
    print(entry)
    print('\t', cMajorScale[entry])
    