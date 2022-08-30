import sys
import re


def get_key(counter, line):
    wd, catg, wnc = line.split()
    key = str(counter) + '_' + catg
    return key

def chk_valid(line):
    if not re.match(r'^%%%.*', line):
        return True

def read_sbn_line(line):
    #For each line in sbn get word, concept, wnc, role

    first_col, second_col = line.split('\t')[:2]
    wd, catg, wnc = first_col.split('.')
    role_tuple = tuple((l[i], l[i + 1]) for i in range(0, len(l), 2))

    return

def read_sbn(pmb_cont):
    #Read all rows in the sbn format in pmb annotation and store
    # it in a dicitionary of nested tuples format

    pmb_ds = {}
    for line in pmb_cont:
        if chk_valid(line):
            key = get_key(counter, line)
            pmb_ds[key] = read_sbn_line(line)

    return pmb_ds


def read_pmb(sbn_all_rows):
    #Read all rows in the sbn format in pmb annotation and store
    # it in a dicitionary of nested tuples format

    pmb_ds = {}
    index = 0
    for row in sbn_all_rows:
        if not re.match(r'^%%%.*', row) and len(
                row.strip().split()) > 0:  # to not consider empty lines and comments in sbn

            try:
                # get all sbn information in a nested tuple format

                m = re.match(r'([^\s]*)\s+([^%]*)\s*(.*)', row)
                lex = m.group(1)
                role = m.group(2).strip()
                if len(lex.split('.')) > 2:
                    lex_word, lex_catg, lex_concept = lex.split('.')
                    if re.match(r'.*Name.*', role):
                        m = re.match(r'.*Name\s+"(.*)".*', role)
                        role_tuple = ('Name', m.group(1))
                    else:
                        role_tuple = ()
                        l = role.split()
                        if len(l) > 0:
                            role_tuple = tuple((l[i], l[i + 1]) for i in range(0, len(l), 2))
                else:
                    role_tuple = role
                    lex_catg = lex

                key = str(index) + "_" + lex_catg
                pmb_ds[key] = (lex, role_tuple)
                index += 1

            except:

                print("ERROR in format of SBN: %s" % row)
                exit()

    return pmb_ds

def find_all_verb_arg(key, pmb_ds):
    index = int(re.match(r'(\d+)_', key)[1])
    verb_row = pmb_ds[key]
    verb_concept = verb_row[0]
    verb_arg = iter(verb_row[1])

    list_arg = []
    while True:
        try:
            role, pos = next(verb_arg)
            pos1 = int(pos)
            find_index = str(index + pos1) + '_'
            for key in pmb_ds:
                if find_index in key:
                    arg = pmb_ds[key]
            list_arg.append((role, pos, arg))
        except StopIteration:
            break
    return tuple(list_arg)

def find_verb_arg(verb, rel_name, pmb_ds):
    for key in pmb_ds:
        if re.match(r'.*v_*', key):
            verb_concept = pmb_ds[key][0]
            if verb in verb_concept:
                list_arg = find_all_verb_arg(key, pmb_ds)
                for arg in list_arg:
                    rel = arg[0]
                    ent = arg[2]
                    if rel_name.lower() in rel.lower():
                        return ent
                        # print('%s :::: %s :::: %s ' % (verb, rel, ent))


def get_gnp(line, pmb_ds):
    print('sriram')

def get_vib(line, pmb_ds):
    print('sriram')

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

    #open the file in Hindi wordnet dir and read the hnd meaning.
    #Apply additional rules given by the linguist


    return wd

def add_hindi_wd(pmb_ds):
    # for each concept word get the equivalent Hindi word from the Hindi 'Wordnet'

    for line in pmb_ds:
        hnd_wd = get_hnd_wd(line, pmb_ds)
        pmb_ds[line] = pmb_ds[line] + (hnd_wd,)

    return pmb_ds



def gen_hindi(pmb_ds):
    print('sriram')

if __name__ == '__main__':

    # read the pmb file and store in pmb data structure
    f = open(sys.argv[1], 'r')
    pmb_cont = f.readlines()
    pmb_ds = read_pmb(pmb_cont)

    #Get Hindi word from Hindi wordnet (Verbnet Dir)
    add_hindi_wd(pmb_ds)

    # Loop through the pmb ds and apply the rules
    add_gnp_vib(pmb_ds)

    # generate Hindi words
    gen_hindi(pmb_ds)

    # Re-ordering of words

