#  https://www.ece.iastate.edu/~alexs/classes/2016_Spring_575/HW/HW5/files/piano-key-freq-wikipedia.pdf 

from alphabet import *

def insert_identifier(string, fulcrum, symbol, octave):
    '''adds octave identifiers to notes
       fulcrum: the character that separates the accidental equivalents
       symbol:  the symbol that is unique to the string type
         helmholtz: pass the "′" PRIME (U+2032)  
         scientific: pass the integer 1 to get a multiple of 1.
       octave: the octave index value'''
    if fulcrum in string:
        index = string.index(fulcrum)
        string = string[:index] + "{}".format(octave * symbol) + string[index:]
    else:
        pass
    return string

def format_hpn(note_name, octave):
    '''format HPN: Helmholtz Pitch Notation'''
    hpn = "{}{}".format(note_name, octave * "′")
    hpn = insert_identifier(hpn, "/", "′", octave)
    return hpn

def format_spn(note_name, octave):
    '''format SPN: Scientific Pitch Notation'''
    spn = "{}{}".format(note_name, octave)
    spn = insert_identifier(spn, "/", 1, octave)
    return spn

def get_frequency(key_number):
    return 440 * 2 ** ((key_number - 49) / 12)

def get_note_name(index):
    note_count = ( (index - 1) % 12 )
    return alphabet_array[note_count]

def get_octave(index):
    offset = 8
    return ( index + offset ) // 12

def get_pn_name(note_name, octave, format_note):
    '''Gets name of note in (H/S) Pitch Notation'''
    note_name = format_note(note_name, octave).lower()
    return note_name

def generate_note(index):
    note = []
    note.append(index)
    note.append(get_pn_name(get_note_name(index), get_octave(index), format_hpn))
    note.append(get_pn_name(get_note_name(index), get_octave(index), format_spn))
    note.append(get_frequency(index))
    return note

def generate_notes_list():
    notes_array = [
        ["NOTE_NUMBER", "HELMHOLTZ_NAME", "SCIENTIFIC NAME", "FREQUENCY_HZ"]
        ]
    for x in range(1, 89):
        notes_array.append(generate_note(x))
        pass
    return notes_array