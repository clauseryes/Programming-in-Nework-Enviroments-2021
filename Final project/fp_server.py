import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import fp_server_utils as su
import termcolor
import http.client
import json

PORT = 8080

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

def ensembl_info(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    info_dict = json.loads(data)
    return info_dict


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        #termcolor.cprint(self.requestline, 'green')
        #termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        #print("Resource requested: ", path_name)
        #print("Parameters:", arguments)

        context = {}

        if path_name == "/":
            contents = su.read_template_html_file('./html/index.html').render(context=context)
        elif path_name == '/listSpecies':
            try:
                limit = arguments['limit'][0]
            except KeyError:
                limit = len(ensembl_info('/info/species')["species"])
            try:
                contents = su.list_species(ensembl_info('/info/species'), limit)
            except ValueError:
                contents = su.read_template_html_file('./html/error.html').render()
        elif path_name == '/karyotype':
            try:
                specie = arguments['specie'][0].replace(' ', '_')
                contents = su.karyotype(ensembl_info('/info/assembly/' + specie))
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render()
        elif path_name == '/chromosomeLength':
            try:
                specie = arguments['specie'][0].replace(' ', '_')
                chromo = arguments['chromosome'][0]
                contents = su.chromo_length(ensembl_info('/info/assembly/' + specie + '/' + chromo))
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render()
        elif path_name.startswith('/gene'):
            try:
                gene = arguments['gene'][0]
                if gene in DICT_GENES.keys():
                    gene = DICT_GENES[gene] #now you can search the gene through its name ot ID
                if path_name == '/geneSeq':
                    contents = su.gene_seq(ensembl_info('/sequence/id/' + gene))
                elif path_name == '/geneInfo':
                    contents = su.gene_info(ensembl_info('/sequence/id/' + gene))
                elif path_name == '/geneCalc':
                    contents = su.gene_calculations(ensembl_info('/sequence/id/' + gene))
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render()
        else:
            contents = su.read_template_html_file('./html/error.html').render()



        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()