from pathlib import Path

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

