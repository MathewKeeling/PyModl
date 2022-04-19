#  This file will contain methods to generate various scales of various keys.
#  Generate Major Scales
#  Generate Minor Scales
#  Generate Chromatic Scales
#  Generate Pentatonic Scales
from resources.alphabet import *
import os

class Scale:
    def __init__(self, key, intonation, tonality):
        self.key = key.upper()
        self.intonation = intonation
        self.calculateIntonation()
        self.tonality = tonality
        self.rules = []
        self.notes = [''] * 8
        if tonality == 'major':
            self.rules = [2, 2, 1, 2, 2, 2, 1]
        elif tonality == 'minor':
            self.rules = [2, 1, 2, 2, 1, 2, 2]
        for x in range(0, 8):
            if x == 0:
                self.notes[x] = noteToNumber(self.key) + self.intonation
            if x != 0:
                # rule minus 1 because first letter has no rule applied
                self.notes[x] = self.notes[ x - 1 ] + self.rules[x - 1]
        for x in range(0, 8):
            self.notes[x] = numberToNote(self.notes[x])
        return
    
    def calculateIntonation(self):
        count = 0
        for letter in self.intonation:
            if letter == '#':
                count = count + 1
            if letter =="b":
                count = count - 1
        self.intonation = count

    def name(self):
        intonation = ''
        if self.intonation > 0:
            intonation = '#' * self.intonation
        if self.intonation < 0:
            intonation = 'b' * abs(self.intonation)
        overview = "{}{} {}".format(self.key, intonation, self.tonality)
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
    scale = Scale(keys[key][0], keys[key][1], keys[key][2])
    #print(scale.name())
    #print(scale.notes)