import Seq1

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': ( Length: ' + str(sequence.len()) + ' ) ' + str(sequence))
    a, c, g, t = sequence.count_bases()
    print('Bases:', sequence.count())

print('-----| Practice 1, Exercise 6 |------')

list_sequences = list(Seq1.test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])