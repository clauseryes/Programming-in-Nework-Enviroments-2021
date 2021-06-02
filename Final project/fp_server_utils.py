import pathlib
import jinja2
from Seq1 import Seq



def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def list_species(info_dict, limit):
    new_dict = info_dict["species"]
    list_species = []
    try:
        for n in range(0, int(limit)):
            list_species.append(new_dict[n]["common_name"])
        context = {
            "limit": limit,
            "list_species": list_species,
            "number_species": len(new_dict)}
        content = read_template_html_file("./html/list_species.html").render(context=context)
    except IndexError:
        content = read_template_html_file('./html/error.html').render()
    return content

def karyotype(info_dict):
    context = {
        "karyotype": info_dict['karyotype']}
    content = read_template_html_file("./html/karyotype.html").render(context=context)
    return content

def chromo_length(info_dict):
    context = {
        "chromo_length": info_dict['length']}
    content = read_template_html_file("./html/chromo_length.html").render(context=context)
    return content

def gene_seq(info_dict):
    context = {
        'id': info_dict['id'],
        "gene_seq": info_dict['seq']}
    content = read_template_html_file("./html/gene_seq.html").render(context=context)
    return content

def gene_info(info_dict):
    context = {
        "start": info_dict["desc"].split(":")[3],
        'end': info_dict["desc"].split(":")[4],
        'length': len(info_dict['seq']),
        'id': info_dict['id'],
        'chromosome': info_dict["desc"].split(":")[2]}
    content = read_template_html_file("./html/gene_info.html").render(context=context)
    return content

def gene_calculations(info_dict):
    s = Seq(info_dict['seq'])
    percentages = Seq.percentages(s)
    context = {
        'id': info_dict['id'],
        "percentages": percentages,
        'length': len(info_dict['seq'])}
    content = read_template_html_file("./html/gene_calculations.html").render(context=context)
    return content


