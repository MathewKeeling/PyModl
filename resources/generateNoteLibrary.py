#  https://www.ece.iastate.edu/~alexs/classes/2016_Spring_575/HW/HW5/files/piano-key-freq-wikipedia.pdf 

from alphabet import *

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

#  Delegation Example
#    Note: consider investigating enums for selection of helmholtz vs scientific type for method
def format_helmholtz(noteName, octave):
    return "{}{}".format(noteName, octave * "′")

def format_scientific_name(noteName, octave):
    return "{}{}".format(noteName, octave)

def get_canonical_name(noteName, octave, format_note):
    canonicalName = format_note(noteName, octave)
    canonicalName = canonicalName.lower()
    return insert_identifier(canonicalName, "/", "′", octave)

def generate_notes_list():
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

# test
generate_notes_list()





