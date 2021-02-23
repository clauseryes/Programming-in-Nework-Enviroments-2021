def correct_seq(seq):
    for i in seq:
        if i != 'A' and i != 'T' and i != 'C' and i != 'G':
            return False
    return True

def count_bases(seq):
    a, c, t, g = 0, 0, 0, 0
    for ch in seq:
        if ch == "A":
            a += 1
        elif ch == "C":
            c += 1
        elif ch == "G":
            g += 1
        else:
            t += 1
    return a, c, g, t


dna_sequence = input("Enter a dna sequence: ")
if correct_seq(dna_sequence):
    print("Total length: ", len(dna_sequence))
    a, c, g, t = count_bases(dna_sequence)
    print("A: ", a)
    print("C: ", c)
    print("T: ", t)
    print("G: ", g)
else:
    print("Not a valid seq.")