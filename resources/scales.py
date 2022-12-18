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

# Major Scales
aMajorScale = {
    'key'   :           ['A'],    
    'ionian':           ['A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A'],    
    'dorian':           ['B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B'],    
    'phrygian':         ['C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭'],
    'lydian':           ['D', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D'],
    'mixolydian':       ['E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E'],
    'aeolian':          ['F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭'],
    'locrian':          ['G♯/A♭', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G♯/A♭'],
}

bMajorScale = {
    'key'   :           ['B'],   
    'ionian':           ['B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B'],
    'dorian':           ['C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭'],
    'phrygian':         ['D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭'],
    'lydian':           ['E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E'],
    'mixolydian':       ['F♯/G♭', 'G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭'],
    'aeolian':          ['G♯/A♭', 'A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭'],
    'locrian':          ['A♯/B♭', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A♯/B♭'],
}

cMajorScale = {
    'key'   :           ['C'],   
    'ionian':           ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
    'dorian':           ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
    'phrygian':         ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'],
    'lydian':           ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
    'mixolydian':       ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'aeolian':          ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
    'locrian':          ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B'],
}

dMajorScale = {
    'key'   :           ['D'],   
    'ionian':           ['D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D'],
    'dorian':           ['E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D', 'E'],
    'phrygian':         ['F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭'],
    'lydian':           ['G', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G'],
    'mixolydian':       ['A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A'],
    'aeolian':          ['B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B'],
    'locrian':          ['C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭'],
}

eMajorScale = {
    'key'   :           ['E'],   
    'ionian':           ['E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D♯/E♭', 'E'],
    'dorian':           ['F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭'],
    'phrygian':         ['G♯/A♭', 'A', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭'],
    'lydian':           ['A', 'B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A'],
    'mixolydian':       ['B', 'C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B'],
    'aeolian':          ['C♯/D♭', 'D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭'],
    'locrian':          ['D♯/E♭', 'E', 'F♯/G♭', 'G♯/A♭', 'A', 'B', 'C♯/D♭', 'D♯/E♭'],
}

fMajorScale = {
    'key'   :           ['F'],   
    'ionian':           ['F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'E', 'F'],
    'dorian':           ['G', 'A', 'A♯/B♭', 'C', 'D', 'E', 'F', 'G'],
    'phrygian':         ['A', 'A♯/B♭', 'C', 'D', 'E', 'F', 'G', 'A'],
    'lydian':           ['A♯/B♭', 'C', 'D', 'E', 'F', 'G', 'A', 'A♯/B♭'],
    'mixolydian':       ['C', 'D', 'E', 'F', 'G', 'A', 'A♯/B♭', 'C'],
    'aeolian':          ['D', 'E', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D'],
    'locrian':          ['E', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'E'],
}

gMajorScale = {
    'key'   :           ['G'],   
    'ionian':           ['G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G'],
    'dorian':           ['A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A'],
    'phrygian':         ['B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B'],
    'lydian':           ['C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C'],
    'mixolydian':       ['D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D'],
    'aeolian':          ['E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E'],
    'locrian':          ['F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭'],
}

# Minor Scales
aMinorScale = {
    'key'   :           ['a'],
    'tonality':         ['minor'],
    'aeolian':          ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
    'locrian':          ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'ionian':           ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
    'dorian':           ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
    'phrygian':         ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'],
    'lydian':           ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
    'mixolydian':       ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
 }

bMinorScale = {
    'key'   :           ['b'],
    'tonality':         ['minor'],
    'aeolian':          ['B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B'],
    'locrian':          ['C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭'],
    'ionian':           ['D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D'],
    'dorian':           ['E', 'F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D', 'E'],
    'phrygian':         ['F♯/G♭', 'G', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭'],
    'lydian':           ['G', 'A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G'],
    'mixolydian':       ['A', 'B', 'C♯/D♭', 'D', 'E', 'F♯/G♭', 'G', 'A'],
}

cMinorScale = {
    'key'   :           ['c'],
    'tonality':         ['minor'],
    'aeolian':          ['C', 'D', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C'],
    'locrian':          ['D', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'D'],
    'ionian':           ['D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'D', 'D♯/E♭'],
    'dorian':           ['F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F'],
    'phrygian':         ['G', 'G♯/A♭', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G'],
    'lydian':           ['G♯/A♭', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'G♯/A♭'],
    'mixolydian':       ['A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭'],
}

dMinorScale = {
    'key'   :           ['d'],
    'tonality':         ['minor'],
    'aeolian':          ['D', 'E', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D'],
    'locrian':          ['E', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'E'],
    'ionian':           ['F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'E', 'F'],
    'dorian':           ['G', 'A', 'A♯/B♭', 'C', 'D', 'E', 'F', 'G'],
    'phrygian':         ['A', 'A♯/B♭', 'C', 'D', 'E', 'F', 'G', 'A'],
    'lydian':           ['A♯/B♭', 'C', 'D', 'E', 'F', 'G', 'A', 'A♯/B♭'],
    'mixolydian':       ['C', 'D', 'E', 'F', 'G', 'A', 'A♯/B♭', 'C'],
}

eMinorScale = {
    'key'   :           ['e'],
    'tonality':         ['minor'],
    'aeolian':          ['E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E'],
    'locrian':          ['F♯/G♭', 'G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭'],
    'ionian':           ['G', 'A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G'],
    'dorian':           ['A', 'B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A'],
    'phrygian':         ['B', 'C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B'],
    'lydian':           ['C', 'D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C'],
    'mixolydian':       ['D', 'E', 'F♯/G♭', 'G', 'A', 'B', 'C', 'D'],
}

fMinorScale = {
    'key'   :           ['f'],
    'tonality':         ['minor'],
    'aeolian':          ['F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'C♯/D♭', 'D♯/E♭', 'F'],
    'locrian':          ['G', 'G♯/A♭', 'A♯/B♭', 'C', 'C♯/D♭', 'D♯/E♭', 'F', 'G'],
    'ionian':           ['G♯/A♭', 'A♯/B♭', 'C', 'C♯/D♭', 'D♯/E♭', 'F', 'G', 'G♯/A♭'],
    'dorian':           ['A♯/B♭', 'C', 'C♯/D♭', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭'],
    'phrygian':         ['C', 'C♯/D♭', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C'],
    'lydian':           ['C♯/D♭', 'D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'C♯/D♭'],
    'mixolydian':       ['D♯/E♭', 'F', 'G', 'G♯/A♭', 'A♯/B♭', 'C', 'C♯/D♭', 'D♯/E♭'],
}

gMinorScale = {
    'key'   :           ['g'],
    'tonality':         ['minor'],
    'aeolian':          ['G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G'],
    'locrian':          ['A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'A'],
    'ionian':           ['A♯/B♭', 'C', 'D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭'],
    'dorian':           ['C', 'D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C'],
    'phrygian':         ['D', 'D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D'],
    'lydian':           ['D♯/E♭', 'F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭'],
    'mixolydian':       ['F', 'G', 'A', 'A♯/B♭', 'C', 'D', 'D♯/E♭', 'F'],
}

#  debug
#for entry in cMajorScale:
#    print(entry)
#    print('\t', cMajorScale[entry])



