""" count function """

def count(sequence, item):
    """ code to execute the count """
    var_c = 0
    for var_c in sequence:
        if var_c == item:
            var_c += 1
            return var_c
        return None
