from pathlib import Path
import termcolor

def seq_ping():
    print('OK')

def take_out_first_line(seq):
    return seq[seq.find('\n'):].replace('\n', '')

def seq_read_fasta(filename):
    seq = take_out_first_line(Path(filename).read_text())
    return seq

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for d in seq:
        if d == 'A':
            a += 1
        elif d == 'C':
            c += 1
        elif d == 'G':
            g += 1
        else:
            t += 1
    return {'A': a, 'C': c, 'G': g, 'T': t}

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    empty_str = ''
    for base in seq:
        empty_str += complement[base]
    return empty_str

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
        #if Seq.is_valid_sequence_2(strbases):
            print("New sequence created!")
        else:
            self.strbases = 'Error'
            print('Incorrect sequence!')

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence ' + str(i) + ' : (Length: ' + str(list_sequences[i].len()) + ' ) ' + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

