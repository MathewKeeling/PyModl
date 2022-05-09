notesNames = [
    [83, "", "", 3135.9634878539946],
    [84, "", "", 3322.437580639561],
    [85, "", "", 3520.0],
    [86, "", "", 3729.3100921447194],
    [87, "", "", 3951.066410048992]
]

alphabetArray = [
    'A',
    'A#/Bb',
    'B',
    'C',
    'C#/Db',
    'D',
    'D#/Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'G#/Ab'
]



for x in range(1, 89):
    keyNumber = x
    frequencyHz = 440 * 2 ** ((keyNumber - 49) / 12)

    octaveCount = keyNumber


    noteCount = (x-1) % 12
    noteName = alphabetArray[noteCount]

    helmholtzName = ""
    scientificName = "{}{}".format(noteName,octaveCount)
    

    print("[{}, \"{}\", \"{}\", {}],".format(keyNumber, helmholtzName, scientificName, frequencyHz))