""" provide a string 'sequence' and count how many 'item' in the sequence."""

def count(sequence, item): 
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
            return sum
