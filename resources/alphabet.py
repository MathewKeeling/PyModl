# alphabet. Doesn't include octaves.

def note_to_number(note):
    return alphabet[note]

def number_to_note(number):
    while number > 11:
        number = number - 12
    return alphabetArray[number]

alphabet = {
    'A' : 0,
    'A♯/B♭': 1,
    'B' : 2,
    'C' : 3,
    'C♯/D♭': 4,
    'D' : 5,
    'D♯/E♭': 6,
    'E' : 7,
    'F' : 8,
    'F♯/G♭': 9,
    'G' : 10,
    'G♯/A♭': 11,
}

alphabetArray = [
    'A',
    'A♯/B♭',
    'B',
    'C',
    'C♯/D♭',
    'D',
    'D♯/E♭',
    'E',
    'F',
    'F♯/G♭',
    'G',
    'G♯/A♭'
]