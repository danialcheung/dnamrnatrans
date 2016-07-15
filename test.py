
# DNA -> mRNA Dictionary
DNA_mRNA_bank = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U'
}

# the 'lazy' mRNA -> Protein dictionary. Does not include the single cases.
mRNA_protein_bank = {
    ('UUU', 'UUC'): 'Phe',
    ('UAA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'): 'Leu',
    ('AUU', 'AUC', 'AUA'): 'Ile',
    ('GUU', 'GUC', 'GUA', 'GUG'): 'Val',
    ('UCU', 'UCC', 'UCA', 'UCG'): 'Ser',
    ('CCU', 'CCC', 'CCA', 'CCG'): 'Pro',
    ('ACU', 'ACC', 'ACA', 'ACG'): 'Thr',
    ('GCU', 'GCC', 'GCA', 'GCG'): 'Ala',
    ('UAU', 'UAC'): 'Tyr',
    ('CAU', 'CAC'): 'His',
    ('AAU', 'AAC'): 'Gin',
    ('AAA', 'AAG'): 'Lys',
    ('GAU', 'GAC'): 'Asp',
    ('GAA', 'GAG'): 'Glu',
    ('UGU', 'UGC'): 'Cys',
    ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'): 'Arg',
    ('AGU', 'AGC'): 'Ser',
    ('GGU', 'GGC', 'GGA', 'GGG'): 'Gly'
}

# Makes a working dictionary from the 'lazy' dictionary by making each sequence a key for their respective protein.
mRNA_protein_assorted = {}
for k, v in mRNA_protein_bank.items():
    for key in k:
        mRNA_protein_assorted[key] = v
# Add Single Cases
mRNA_protein_assorted['UGG'] = 'Trp'
mRNA_protein_assorted['AUG'] = 'Met'

# Splits things into chunks of three. Returns iterable.
# Source: http://sorucevap.netgez.com/en-pythonic-parcalar-bir-liste-uzerinde-yineleme-yolu-nedir
def chunker(sequence, size):
    try:
        return (sequence[pos:pos + size] for pos in xrange(0, len(sequence), size))
    except TypeError:
        print(
            'ERROR! Your sequence may not be correct. Look at the mRNA output and see if there is an AUG.')


# Converts an iterable to a list in chunks of three letters per item.
def iterable_to_list(sequence):
    a = []
    mRNA_translate = chunker(sequence, 3)
    for x in mRNA_translate:
        a.append(x)
    return a


# Removes anything before the AUG Sequence
def remove_beg(sequence):
    try:
        for i, v in enumerate(list(sequence)):
            if v == 'A' and sequence[i + 1] == 'U' and sequence[i + 2] == 'G':
                return sequence[i:]
    except IndexError:
        print('ERROR! We could\'t find the starting sequence.')


# Translates from mRNA -> Protein. Also handles stop sequences.
def translate_seq(sequence):
    proteins = []
    for x in sequence:
        if x == 'UAA' or x == 'UGA' or x == 'UAG':
            return proteins
        else:
            proteins.append(mRNA_protein_assorted.get(x))
    print 'ERROR! No ending Sequence found!'
    return ''


# DNA -> mRNA -> Protein
def DNA_to_Protein():
    seq = raw_input('Enter DNA Sequence Here (in CAPS and no spaces please): ')
    mRNA_seq_string = ''

    # Transcribes DNA -> mRNA
    try:
        for i in seq:
            mRNA_seq_string += DNA_mRNA_bank.get(i)
    except TypeError:
        print('ERROR! Invalid console_input or not in CAPS.')

    print ''
    print 'mRNA Sequence is: ' + mRNA_seq_string

    mRNA_seq_string = remove_beg(mRNA_seq_string)
    mRNA_seq = iterable_to_list(mRNA_seq_string)
    proteins = translate_seq(mRNA_seq)

    print 'Proteins are: ' + '-'.join(proteins)
    print ''


# mRNA -> Protein
def mRNA_to_Protein():
    seq = raw_input('Enter mRNA Sequence Here (in CAPS and no spaces please): ')

    mRNA_seq_string = remove_beg(seq)
    mRNA_seq = iterable_to_list(mRNA_seq_string)
    proteins = translate_seq(mRNA_seq)

    print ''
    print 'Proteins are: ' + '-'.join(proteins)
    print ''


# Start Menu
while (True):
    print('1. DNA -> mRNA -> Protein(s)')
    print('2. mRNA -> Proteins')
    print('3. Quit')
    console_input = raw_input('Type the number of desired operation: ')

    if console_input == '1':
        DNA_to_Protein()
    elif console_input == '2':
        mRNA_to_Protein()
    elif console_input == '3':
        print('')
        print('There are five levels.')
        break
    else:
        print('Invalid console_input. Please try again.')
