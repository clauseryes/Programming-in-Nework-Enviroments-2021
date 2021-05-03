from Seq1 import Seq
import pathlib
import jinja2


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {
        'number': seq_number,
        'sequence': sequence
    }
    contents = read_template_html_file('./html/get.html').render(context=context)
    return contents

def info(sequence):
    s = Seq(sequence)
    response = 'Total length: ' + str(Seq.len(s)) + "\r" + str(Seq.percentages(s)) + '\r'
    return response

def comp(sequence):
    s = Seq(sequence)
    response = Seq.complement(s)
    return response

def rev(sequence):
    s = Seq(sequence)
    response = Seq.reverse(s)
    return response

def gene(seq_name):
    path = './Sequences/' + seq_name + '.txt'
    s = Seq()
    s.read_fasta(path)
    context = {
        'gene_name': seq_name,
        'gene_contents': s.strbases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents





