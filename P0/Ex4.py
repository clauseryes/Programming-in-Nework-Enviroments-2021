import Seq0

FOLDER = './Sequences/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']
base_list = ['A', 'C', 'T', 'G']

print('-----| Exercise 4 |------')
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + '.txt')
    print('\n' + 'Gene ' + gene + ':')
    for base in base_list:
        print(base + ': ' + str(Seq0.seq_count_base(sequence, base)))

