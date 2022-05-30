from resources.alphabet import *
from resources.tunings import *

class Fretboard:
    def __init__(self, stringCount, fretDepth):
        self.stringCount = stringCount
        self.fretDepth = fretDepth
        self.fretBoard = []
    
    def tune(self, tuning):
        self.tuning = tuning

    def populate_fret_board(self):
        strings, frets = (self.stringCount, self.fretDepth)
        self.fretBoard = [[0 for x in range(self.fretDepth)] for x in range(self.stringCount)]
        
        for string in range(0, self.stringCount ):
            for fret in range(0, self.fretDepth):
                note = self.tuning[string]
                note = note_to_number(note)
                note = note + fret
                while note > 11:
                    note = note - 12
                note = number_to_note(note)
                self.fretBoard[string][fret] = note

test = Fretboard(6, 25)
test.tune(tunings['dropC'])
test.populate_fret_board()

for string in test.fretBoard:
    print(string)