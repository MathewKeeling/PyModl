from resources.pitch_notation import *
from resources.tunings import *

class Fret_Board:
    def __init__(self, string_count, fret_depth):
        self.string_count = string_count
        self.fret_depth = fret_depth
        self.fret_board = []
    
    def tune(self, tuning):
        self.tuning = tuning

    def populate_pn(self):
        self.fret_board = [[0 for x in range(self.fret_depth)] for x in range(self.string_count)]
        for string in range(0, self.string_count ):
            for fret in range(0, self.fret_depth):
                note = self.tuning[string]
                note = note + fret
                note = generate_note(note)
                note = note[2]
                self.fret_board[string][fret] = note

    def populate_canonical(self):
        self.fret_board = [[0 for x in range(self.fret_depth)] for x in range(self.string_count)]
        for string in range(0, self.string_count ):
            for fret in range(0, self.fret_depth):
                note = self.tuning[string]
                note = note_to_number(note)
                note = note + fret
                while note > 11:
                    note = note - 12
                note = number_to_note(note)
                self.fret_board[string][fret] = note

test = Fret_Board(6, 25)
test.tune(tunings_piano['standard'])
test.populate_pn()

for string in test.fret_board:
    print(string)