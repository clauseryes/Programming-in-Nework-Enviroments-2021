import http.client
import json
import Seq1

def print_colored(message, data, color):
    from termcolor import cprint, colored
    print(colored(message,color), end="")
    print(data)

DICT_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)

try:
    for key, id in DICT_GENES.items():
        connection.request('GET', ENDPOINT + id + PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            # print(json.dumps(response_dict, indent=4, sort_keys=True))
            sequence = Seq1.Seq(response_dict['seq'])
            s_length = sequence.len()
            percentages = sequence.percentages()
            most_freq_base = sequence.most_freq_base(sequence.count())
            print_colored('Gene: ', key, 'yellow')
            print('Total length:', s_length)
            print(percentages)
            print('Most frequent base:', most_freq_base)
            print(' ')

except KeyError:
    print('The gene is not inside our dictionary. Choose one of the following:', list(DICT_GENES.keys()))