from itertools import islice
import time
import json

def process(m):
    # send data to mappers 
    data = json.dumps(m)
    sd = json.loads(data)
    print(sd[0]) #paizei gamo to xristo m

n = 100  #chunk size
filename = 'data.json'
with open(filename) as json_file:
    data = json.load(json_file)

    for n_lines in iter(lambda: tuple(islice(data, n)), ()):
        process(n_lines)
        time.sleep(5)


        