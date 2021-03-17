import Seq1

def print_results(sequence, gene_list):
    for gene in gene_list:
        new_seq = sequence.read_fasta('./Sequences/' + gene + '.txt')
        print('Gene ' + gene + ': Most frequent Base: ' + str(new_seq.most_frequent_base(sequence.count()))

gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']

print_results(Seq1.sequence, gene_list)

