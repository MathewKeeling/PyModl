modes_dictionary = {
        'ionian':       [0, 1, 2, 3, 4, 5, 6, 0],  # tonic through tonic
        'dorian':       [1, 2, 3, 4, 5, 6, 0, 1],  # supertonic through supertonic
        'phrygian':     [2, 3, 4, 5, 6, 0, 1, 2],  # mediant through mediant
        'lydian':       [3, 4, 5, 6, 0, 1, 2, 3],  # subdominant through subdominant
        'mixolydian':   [4, 5, 6, 0, 1, 2, 3, 4],  # dominant through dominant
        'aeolian':      [5, 6, 0, 1, 2, 3, 4, 5],  # submediant through submediant
        'locrian':      [6, 0, 1, 2, 3, 4, 5, 6],  # leading tone through leading tone
}

modes_array = [
        ['ionian',      [0, 1, 2, 3, 4, 5, 6, 0]],  # tonic through tonic
        ['dorian',      [1, 2, 3, 4, 5, 6, 0, 1]],  # supertonic through supertonic
        ['phrygian',    [2, 3, 4, 5, 6, 0, 1, 2]],  # mediant through mediant
        ['lydian',      [3, 4, 5, 6, 0, 1, 2, 3]],  # subdominant through subdominant
        ['mixolydian',  [4, 5, 6, 0, 1, 2, 3, 4]],  # dominant through dominant
        ['aeolian',     [5, 6, 0, 1, 2, 3, 4, 5]],  # submediant through submediant
        ['locrian',     [6, 0, 1, 2, 3, 4, 5, 6]]   # leading tone through leading tone
]