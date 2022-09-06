import sys


def get_key(counter, first_col):
    # get uniq key for the dictionary

    if len(first_col.split('.')) > 2:
        wd, catg, wnc = first_col.split('.')
        key = str(counter) + '_' + catg
    else:
        key = str(counter) + '_' + first_col
    return key


def chk_valid(line):
    # check if the line is valid to read and store in the Data structure

    if line[0] != '%' and len(line.strip()) > 0:
        return True

def read_sbn_line(line):

    # For each line in sbn get word, concept, wnc, role

    print(line)
    info_line =  line.split('%')[0]
    elements = info_line.split()
    wn_concept = elements[0]
    second_col = elements[1:]

    if len(second_col) > 1:
        role_tuple = tuple((second_col[i], second_col[i + 1]) for i in range(0, len(second_col), 2))
    elif len(second_col) == 1:
        role_tuple = (second_col[0])
    else:
        role_tuple = ()
    return (wn_concept, role_tuple)


def read_sbn(pmb_cont):
    #Read all rows in the sbn format in pmb annotation and store
    # it in a dicitionary of nested tuples format

    pmb_ds = {}
    index = 0
    for line in pmb_cont:
        if chk_valid(line):
            first_col = line.split()[0]
            key = get_key(index, first_col)
            pmb_ds[key] = read_sbn_line(line)
            index += 1

    return pmb_ds


def get_gnp(line, pmb_ds):
    print('')


def get_vib(line, pmb_ds):
    print('')


def add_gnp_vib(pmb_ds):
    #add gender, number, person information for each word in English for
    # giving to Hindi generator

    gnp = ''
    vib = ''
    for line in pmb_ds:
        gnp = get_gnp(line, pmb_ds)
        vib = get_vib(line, pmb_ds)
        pmb_ds[line] = pmb_ds[line] + (gnp, vib)

    return pmb_ds


def get_hnd_wd(line, pmb_ds):

    # open the file in Hindi wordnet dir and read the hnd meaning.
    # Apply additional rules given by the linguist

    wd = ''
    return wd


def add_hindi_wd(pmb_ds):
    # for each concept word get the equivalent Hindi word from the Hindi 'Wordnet'

    for line in pmb_ds:
        hnd_wd = get_hnd_wd(line, pmb_ds)
        pmb_ds[line] = pmb_ds[line] + (hnd_wd,)

    return pmb_ds


def gen_hindi(pmb_ds):
    print('')


if __name__ == '__main__':

    # read the pmb file and store in pmb data structure
    f = open(sys.argv[1], 'r')
    pmb_cont = f.readlines()
    pmb_ds = read_sbn(pmb_cont)

    # Get Hindi word from Hindi wordnet (Verbnet Dir)
    add_hindi_wd(pmb_ds)
    for key in pmb_ds:
        print(key,pmb_ds[key])
    exit()

    # Loop through the pmb ds and apply the rules
    add_gnp_vib(pmb_ds)

    # generate Hindi words
    gen_hindi(pmb_ds)

    # Re-ordering of words

