import http.server
import http.client
import json

def ensembl_info(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    info_dict = json.loads(data)
    return info_dict

print(ensembl_info('/info/species')['species'][90]['common_name'])
#print(ensembl_info('/info/assembly/' + 'homo_sapiens')['karyotype'])
#print(ensembl_info('/info/assembly/' + 'horse' + '/' + '20')['length'])
#print(ensembl_info('/info/assembly/:species')
print(len(ensembl_info('/info/species')["species"]))



