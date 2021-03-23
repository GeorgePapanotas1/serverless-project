from itertools import islice
import time
import json
import pandas

def process(m):
    test = []
    for i in range(len(m) - 1):
        test.append(m[i].split(','))
    df = pandas.DataFrame(test, columns =["id","vendor_id","pickup_datetime","dropoff_datetime","passenger_count","pickup_longitude","pickup_latitude","dropoff_longitude","dropoff_latitude","store_and_fwd_flag","trip_duration"])
    # # print("\n")
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    print(parsed[0])
    # send data to mappers 
    # data = json.dumps(m)
    # sd = json.loads(data)
    # print(sd) #paizei gamo to xristo m
    # print("\n")

n = 100  #chunk size
filename = 'fares.csv'
with open(filename) as json_file:
    # data = json.load(json_file)
    for n_lines in iter(lambda: tuple(islice(json_file, 1)), ()):
        first = n_lines
        break

    for n_lines in iter(lambda: tuple(islice(json_file, n)), ()):
        process(n_lines)
        time.sleep(5)


        