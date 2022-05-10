class Notes:
    def __init__(self, note):
        self.keyNumber = note[0]
        self.helmholtzName = note[1]
        self.scientificName = note[2]
        self.frequencyHz = note[3]

    #  Deprecated function (probably)
    def generateNote(self, keyNumber):
        self.keyNumber = keyNumber
        self.frequencyHz = 440 * 2 ** ((keyNumber - 49) / 12)


notes = []

for x in range(0,89):
    note = Notes()


for note in notes:
    print(note.frequencyHz)
