#  https://www.ece.iastate.edu/~alexs/classes/2016_Spring_575/HW/HW5/files/piano-key-freq-wikipedia.pdf 


def insert_identifier(string, fulcrum, symbol, octave):
    #  method that implants octave idenfiers into names of notes
    #  fulcrum: the character that separates the accidental equivalents
    #  symbol:  the symbol that is unique to the string type
    #    helmholtz: pass the "′" PRIME (U+2032)  
    #    scientific: pass the integer 1 to get a multiple of 1.
    #  octave: the octave index value
    if fulcrum in string:
        index = string.index(fulcrum)
        string = string[:index] + "{}".format(octave * symbol) + string[index:]
    else:
        pass
    return string

# consider investigating enums for selection of helmholtz vs scientific type for method

# updated to use delegation
# read Headfirst Design Patterns (Eric and Elizabeth Freeman) (Recommended by M.S.)
# methods should be verbs
def format_helmholtz(noteName, octave):
    return "{}{}".format(noteName, octave * "′")

def format_scientific_name(noteName, octave):
    return "{}{}".format(noteName, octave)

def get_canonical_name(noteName, octave, format_note):
    canonicalName = format_note(noteName, octave)
    canonicalName = canonicalName.lower()
    return insert_identifier(canonicalName, "/", "′", octave)


def generateNotesList():
    for x in range(1, 89):
        keyNumber = x
        frequencyHz = 440 * 2 ** ((keyNumber - 49) / 12)
        offset = 8
        octave = ( x + offset ) // 12
        noteCount = (x-1) % 12
        noteName = alphabetArray[noteCount]
        helmholtzName = get_canonical_name(noteName, octave, format_helmholtz)
        scientificName = get_canonical_name(noteName, octave, format_scientific_name)
        print("[{}, \"{}\", \"{}\", {}],".format(keyNumber, helmholtzName, scientificName, frequencyHz))

notesNames = [     
    ["INDEX", "HELMHOLTZ NAME", "SCIENTIFIC NAME", "FREQUENCY (HZ)"],
    [1, "a", "A0", 27.5],
    [2, "a♯/b♭", "A♯0/B♭0", 29.13523509488062],
    [3, "b", "B0", 30.86770632850775],
    [4, "c′", "C1", 32.70319566257483],
    [5, "c♯′/d♭′", "C♯1/D♭1", 34.64782887210901],
    [6, "d′", "D1", 36.70809598967594],
    [7, "d♯′/e♭′", "D♯1/E♭1", 38.890872965260115],
    [8, "e′", "E1", 41.20344461410875],
    [9, "f′", "F1", 43.653528929125486],
    [10, "f♯′/g♭′", "F♯1/G♭1", 46.2493028389543],
    [11, "g′", "G1", 48.999429497718666],
    [12, "g♯′/a♭′", "G♯1/A♭1", 51.91308719749314],
    [13, "a′", "A1", 55.0],
    [14, "a♯′/b♭′", "A♯1/B♭1", 58.27047018976124],
    [15, "b′", "B1", 61.7354126570155],
    [16, "c′′", "C2", 65.40639132514966],
    [17, "c♯′′/d♭′′", "C♯2/D♭2", 69.29565774421802],
    [18, "d′′", "D2", 73.41619197935188],
    [19, "d♯′′/e♭′′", "D♯2/E♭2", 77.78174593052023],
    [20, "e′′", "E2", 82.4068892282175],
    [21, "f′′", "F2", 87.30705785825097],
    [22, "f♯′′/g♭′′", "F♯2/G♭2", 92.4986056779086],
    [23, "g′′", "G2", 97.99885899543733],
    [24, "g♯′′/a♭′′", "G♯2/A♭2", 103.82617439498628],
    [25, "a′′", "A2", 110.0],
    [26, "a♯′′/b♭′′", "A♯2/B♭2", 116.54094037952248],
    [27, "b′′", "B2", 123.47082531403103],
    [28, "c′′′", "C3", 130.8127826502993],
    [29, "c♯′′′/d♭′′′", "C♯3/D♭3", 138.59131548843604],
    [30, "d′′′", "D3", 146.8323839587038],
    [31, "d♯′′′/e♭′′′", "D♯3/E♭3", 155.56349186104046],
    [32, "e′′′", "E3", 164.81377845643496],
    [33, "f′′′", "F3", 174.61411571650194],
    [34, "f♯′′′/g♭′′′", "F♯3/G♭3", 184.9972113558172],
    [35, "g′′′", "G3", 195.99771799087463],
    [36, "g♯′′′/a♭′′′", "G♯3/A♭3", 207.65234878997256],
    [37, "a′′′", "A3", 220.0],
    [38, "a♯′′′/b♭′′′", "A♯3/B♭3", 233.08188075904496],
    [39, "b′′′", "B3", 246.94165062806206],
    [40, "c′′′′", "C4", 261.6255653005986],
    [41, "c♯′′′′/d♭′′′′", "C♯4/D♭4", 277.1826309768721],
    [42, "d′′′′", "D4", 293.6647679174076],
    [43, "d♯′′′′/e♭′′′′", "D♯4/E♭4", 311.1269837220809],
    [44, "e′′′′", "E4", 329.6275569128699],
    [45, "f′′′′", "F4", 349.2282314330039],
    [46, "f♯′′′′/g♭′′′′", "F♯4/G♭4", 369.9944227116344],
    [47, "g′′′′", "G4", 391.99543598174927],
    [48, "g♯′′′′/a♭′′′′", "G♯4/A♭4", 415.3046975799451],
    [49, "a′′′′", "A4", 440.0],
    [50, "a♯′′′′/b♭′′′′", "A♯4/B♭4", 466.1637615180899],
    [51, "b′′′′", "B4", 493.8833012561241],
    [52, "c′′′′′", "C5", 523.2511306011972],
    [53, "c♯′′′′′/d♭′′′′′", "C♯5/D♭5", 554.3652619537442],
    [54, "d′′′′′", "D5", 587.3295358348151],
    [55, "d♯′′′′′/e♭′′′′′", "D♯5/E♭5", 622.2539674441618],
    [56, "e′′′′′", "E5", 659.2551138257398],
    [57, "f′′′′′", "F5", 698.4564628660078],
    [58, "f♯′′′′′/g♭′′′′′", "F♯5/G♭5", 739.9888454232688],
    [59, "g′′′′′", "G5", 783.9908719634985],
    [60, "g♯′′′′′/a♭′′′′′", "G♯5/A♭5", 830.6093951598903],
    [61, "a′′′′′", "A5", 880.0],
    [62, "a♯′′′′′/b♭′′′′′", "A♯5/B♭5", 932.3275230361799],
    [63, "b′′′′′", "B5", 987.7666025122483],
    [64, "c′′′′′′", "C6", 1046.5022612023945],
    [65, "c♯′′′′′′/d♭′′′′′′", "C♯6/D♭6", 1108.7305239074883],
    [66, "d′′′′′′", "D6", 1174.6590716696303],
    [67, "d♯′′′′′′/e♭′′′′′′", "D♯6/E♭6", 1244.5079348883237],
    [68, "e′′′′′′", "E6", 1318.5102276514797],
    [69, "f′′′′′′", "F6", 1396.9129257320155],
    [70, "f♯′′′′′′/g♭′′′′′′", "F♯6/G♭6", 1479.9776908465376],
    [71, "g′′′′′′", "G6", 1567.981743926997],
    [72, "g♯′′′′′′/a♭′′′′′′", "G♯6/A♭6", 1661.2187903197805],
    [73, "a′′′′′′", "A6", 1760.0],
    [74, "a♯′′′′′′/b♭′′′′′′", "A♯6/B♭6", 1864.6550460723597],
    [75, "b′′′′′′", "B6", 1975.533205024496],
    [76, "c′′′′′′′", "C7", 2093.004522404789],
    [77, "c♯′′′′′′′/d♭′′′′′′′", "C♯7/D♭7", 2217.4610478149766],
    [78, "d′′′′′′′", "D7", 2349.31814333926],
    [79, "d♯′′′′′′′/e♭′′′′′′′", "D♯7/E♭7", 2489.0158697766474],
    [80, "e′′′′′′′", "E7", 2637.02045530296],
    [81, "f′′′′′′′", "F7", 2793.825851464031],
    [82, "f♯′′′′′′′/g♭′′′′′′′", "F♯7/G♭7", 2959.955381693075],
    [83, "g′′′′′′′", "G7", 3135.9634878539946],
    [84, "g♯′′′′′′′/a♭′′′′′′′", "G♯7/A♭7", 3322.437580639561],
    [85, "a′′′′′′′", "A7", 3520.0],
    [86, "a♯′′′′′′′/b♭′′′′′′′", "A♯7/B♭7", 3729.3100921447194],
    [87, "b′′′′′′′", "B7", 3951.066410048992],
    [88, "c′′′′′′′′", "C8", 4186.009044809578]
]

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

generateNotesList()

#for note in notesNames:
#    print(note)



