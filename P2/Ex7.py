from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
PORT_2 = 8082
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.read_fasta('../Session-04/FRAT1.txt')
i = 0
count = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    if count % 2 == 0:
        print(c_2.talk('Fragment ' + str(count) + ' : ' + fragment))
    else:
        print(c.talk('Fragment ' + str(count) + ' : ' + fragment))





