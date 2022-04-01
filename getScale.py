#  This file will contain methods to generate various scales of various keys.
#  Generate Major Scales
#  Generate Minor Scales
#  Generate Chromatic Scales
#  Generate Pentatonic Scales
from resources.alphabet import *
import os

class Scale:
    def __init__(self, key, sharpness, tonality):
        self.key = key
        self.sharpness = sharpness
        self.tonality = tonality
        self.rules = []
        self.notes = [''] * 8
        if tonality == 'major':
            self.rules = [2, 2, 1, 2, 2, 2, 1]
        elif tonality == 'minor':
            self.rules = [2, 1, 2, 2, 1, 2, 2]
        for x in range(0, 8):
            if x == 0:
                self.notes[x] = noteToNumber(self.key)
            if x != 0:
                # rule minus 1 because first letter has no rule applied
                self.notes[x] = self.notes[ x - 1 ] + self.rules[x - 1]
        for x in range(0, 8):
            self.notes[x] = numberToNote(self.notes[x])
        return
    def name(self):
        overview = "{}{} {}".format(self.key, self.sharpness, self.tonality)
        return overview

class Modes:
    def __init__(self, stuff):
        return
    ionian =     [0, 1, 2, 3, 4, 5, 6, 0]  # tonic through tonic
    dorian =     [1, 2, 3, 4, 5, 6, 0, 1]  # supertonic through supertonic
    phrygian =   [2, 3, 4, 5, 6, 0, 1, 2]  # mediant through mediant
    lydian =     [3, 4, 5, 6, 0, 1, 2, 3]  # subdominant through subdominant
    mixolydian = [4, 5, 6, 0, 1, 2, 3, 4]  # dominant through dominant
    aeolian =    [5, 6, 0, 1, 2, 3, 4, 5]  # submediant through submediant
    locrian =    [6, 0, 1, 2, 3, 4, 5, 6]  # leading tone through leading tone

# debug
os.system('cls')

alphabet = 'ABCDEFG'
print("MAJOR SCALES")
for letter in alphabet:
    test = Scale(letter, '', 'major')
    print('\t', test.name())
    print('\t', test.notes)

print("MINOR SCALES")
for letter in alphabet:
    test = Scale(letter, '', 'minor')
    print('\t', test.name())
    print('\t', test.notes)