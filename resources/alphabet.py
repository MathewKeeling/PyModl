def noteToNumber(note):
    return alphabet[note]

def numberToNote(number):
    if number > 11:
        number = number - 12
    return alphabetArray[number]

alphabet = {
    'A' : 0,
    'A#': 1,
    'B' : 2,
    'C' : 3,
    'C#': 4,
    'D' : 5,
    'D#': 6,
    'E' : 7,
    'F' : 8,
    'F#': 9,
    'G' : 10,
    'G#': 11,
}

alphabetArray = [
    'A',
    'A#',
    'B',
    'C',
    'C#',
    'D',
    'D#',
    'E',
    'F',
    'F#',
    'G',
    'G#'
]

#  debug

print(numberToNote(2))