import Seq0

FOLDER = './Sequences/'
ID = 'U5.txt'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
print('-----| Exercise 7 |------')
print('Gene U5:')
print('Frag: ' + U5_seq[0:20])
print('Rev: ' + str(Seq0.seq_complement(U5_seq[0:20])))