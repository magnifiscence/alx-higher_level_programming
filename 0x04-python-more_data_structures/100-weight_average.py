#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    nume = 0
    deno = 0

    for tup in my_list:
        nume += tup[0] * tup[1]
        deno += tup[1]

    return (nume / deno)
