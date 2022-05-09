class Notes:
    def __init__(self):
        self.keyNumber = 0
        self.scientificName = ''
        self.frequencyHz = 0

    def generateNote(self, keyNumber):
        self.keyNumber = keyNumber
        self.frequencyHz = 440 * 2 ** ((keyNumber - 49) / 12)


notes = []

for x in range(0,89):
    note = Notes()
    note.generateNote(x)
    notes.append(note)


for note in notes:
    print(note.frequencyHz)
