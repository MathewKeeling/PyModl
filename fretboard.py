from resources.alphabet import *
from resources.tunings import *


class Fretboard:
    def __init__(self, fretDepth):
        self.stringCount = 6
        self.fretDepth = fretDepth
        self.fretBoard = [ [], [], [], [], [], [] ]
        self.tuning = []
    
    def tune(self, tuning):
        self.tuning = tuning

    def populateFretBoard(self):
        for string in range(self.stringCount):
            print("I'm the {} string!".format(self.tuning[string]))

            for fret in range(self.fretDepth):
                fret = fret + 1
                print("\tI'm fret {}!".format(fret))


test = Fretboard(24)
test.tune(tunings['standard'])
test.populateFretBoard()

