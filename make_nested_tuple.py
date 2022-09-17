def make_tuple_by_slicing(input_tuple,starting_number,ending_number):
    output = (input_tuple[:starting_number]) + ((input_tuple[starting_number:ending_number]),) + (input_tuple[ending_number:])

    return output

def make_multi_nested_tuple(input_tuple, **kwargs):
    output_tuple = input_tuple
    for k,v in kwargs.items():
        output_tuple = make_tuple_by_slicing(output_tuple, int(k), v) 

    return output_tuple


def read_verb_row(row):

    input_tuple = tuple(row.split())
    count = len(row.split('#'))
    input_dic = {}
    for i in range(0, count):
        input_dic[str(i+1)] = i+3

    print("Input Tuple: ",input_tuple)
    print("Nested Tuple: %s" % input_dic)
    output_tuple = make_multi_nested_tuple(input_tuple, **input_dic)
    return output_tuple
    
verb_row = "give.v.03 Agent#karwA -1 TAM#A_TAM +1 TIME#Time +2 Recipient#saMpraxAna +3 Theme#karma +4"
print(read_verb_row(verb_row))
