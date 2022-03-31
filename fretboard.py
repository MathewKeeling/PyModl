
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

tunings = {
    'standard': ['E', 'A', 'D', 'G', 'B', 'E'],
    'dropC'   : ['C', 'A', 'D', 'G', 'B', 'E'],
    'dropD'   : ['D', 'A', 'D', 'G', 'B', 'E'],
    'dropDD'  : ['D', 'A', 'D', 'G', 'B', 'D'],
    'dadgad'  : ['D', 'A', 'D', 'G', 'A', 'D']
}

alphabet = {
    'a' : 1,
    'a#': 2,
    'b' : 3,
    'c' : 4,
    'c#': 5,
    'd' : 6,
    'd#': 7,
    'e' : 8,
    'f' : 9,
    'f#': 10,
    'g' : 11,
    'g#': 12,
}

test = Fretboard(24)
test.tune(tunings['standard'])
test.populateFretBoard()

