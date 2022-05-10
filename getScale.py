#  This file will contain methods to generate scales in their various keys with their various modes.
#  Generate Major Scales
#  Generate Minor Scales
#  Generate Chromatic Scales
#  Generate Pentatonic Scales
from resources.alphabet import *

class newScale:
    def __init__(self, key, intonation, tonality):
        self.key = key.upper()
        self.intonation = intonation
        self.calculateIntonation()
        self.tonality = tonality
        self.rules = []
        self.keySignature = ['']
        self.calculateKeySignature()
        self.name = self.calculateName()
        self.modesInKey = {}
        self.calculateModes()
        
    def calculateKeySignature(self):
        if self.tonality == 'major':
            self.rules = [2, 2, 1, 2, 2, 2, 1]
            self.keySignature = self.keySignature * 8
        elif self.tonality == 'minor':
            self.rules = [2, 1, 2, 2, 1, 2, 2]
            self.keySignature = self.keySignature * 8
        elif self.tonality == 'chromatic':
            pass
        elif self.tonality == 'pentatonic':
            pass
        for x in range(0, len(self.rules) + 1):
            if x == 0:
                self.keySignature[x] = noteToNumber(self.key) + self.intonation
            if x != 0:
                # rule minus 1 because first letter has no rule applied
                self.keySignature[x] = self.keySignature[ x - 1 ] + self.rules[x - 1]
        for x in range(0, len(self.rules) + 1):
            self.keySignature[x] = numberToNote(self.keySignature[x])
        return

    def calculateIntonation(self):
        count = 0
        for letter in self.intonation:
            if letter == '#':
                count = count + 1
            if letter =="b":
                count = count - 1
        self.intonation = count

    def calculateModes(self):
        modes = {
                'Ionian':                     [0, 1, 2, 3, 4, 5, 6, 0],  # tonic through tonic
                'Dorian':                     [1, 2, 3, 4, 5, 6, 0, 1],  # supertonic through supertonic
                'Phrygian':                   [2, 3, 4, 5, 6, 0, 1, 2],  # mediant through mediant
                'Lydian':                     [3, 4, 5, 6, 0, 1, 2, 3],  # subdominant through subdominant
                'Mixolydian':                 [4, 5, 6, 0, 1, 2, 3, 4],  # dominant through dominant
                'Natural Minor (Aeolian)':    [5, 6, 0, 1, 2, 3, 4, 5],  # submediant through submediant
                'Locrian':                    [6, 0, 1, 2, 3, 4, 5, 6],  # leading tone through leading tone
        }
        keySignatureIndex = 0
        for mode in modes:
            selectedMode = '{} {}'.format(self.keySignature[keySignatureIndex], mode)
            keySignatureIndex = keySignatureIndex + 1
            self.modesInKey[selectedMode] = ['']
            self.modesInKey[selectedMode] = self.modesInKey[selectedMode] * 8
            for x in range (0, 8):
                self.modesInKey[selectedMode][x] = self.keySignature[modes[mode][x]]


    def calculateName(self):
        intonation = ''
        if self.intonation > 0:
            intonation = '#' * self.intonation
        if self.intonation < 0:
            intonation = 'b' * abs(self.intonation)
        name = "{}{} {}".format(self.key, intonation, self.tonality)
        return name


keys = {
    'aMajor': ['A', '', 'major'],
    'bMajor': ['B', '', 'major'],
    'cMajor': ['C', '', 'major'],
    'dMajor': ['D', '', 'major'],
    'eMajor': ['E', '', 'major'],
    'fMajor': ['F', '', 'major'],
    'gMajor': ['G', '', 'major'],
    'aMinor': ['a', '', 'minor'],
    'bMinor': ['b', '', 'minor'],
    'cMinor': ['c', '', 'minor'],
    'dMinor': ['d', '', 'minor'],
    'eMinor': ['e', '', 'minor'],
    'fMinor': ['f', '', 'minor'],
    'gMinor': ['g', '', 'minor']
}

for key in keys:
    scale = newScale(keys[key][0], keys[key][1], keys[key][2])
    print("\n", scale.key, scale.tonality, "Key Signature:", scale.keySignature)
    for mode in scale.modesInKey:
        print("   ",mode)
        print("      ", scale.modesInKey[mode][:])
    #print(scale.modesInKey)

