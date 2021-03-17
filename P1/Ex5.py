from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': ( Length: ' + str(sequence.len()) + ' ) ' + str(sequence))
    a, c, g, t = sequence.count_bases()
    print('A: ' + str(a) + ', C: ' + str(c) + ', T: ' + str(t) + ', G: ' + str(g))

print('-----| Practice 1, Exercise 5 |------')
s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq('Invalid seq')

print_result(1, s1)
print_result(2, s2)
print_result(3, s3)