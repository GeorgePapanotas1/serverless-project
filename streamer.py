from itertools import islice
import time
import json
import pandas

def process(m):
    processed = [] #initiate new array
    for i in range(len(m) - 1):
        processed.append(m[i].split(',')) #for each of the items, push them to the processed array (incoming tuple is immutable)

    df = pandas.DataFrame(processed, columns =["id","vendor_id","pickup_datetime","dropoff_datetime","passenger_count","pickup_longitude","pickup_latitude","dropoff_longitude","dropoff_latitude","store_and_fwd_flag","trip_duration"])
    result = df.to_json(orient="records")
    parsed = json.loads(result)

    # convert the array to json. Here we must send the data to the mappers
    print(parsed[0])
    

n = 100  
filename = 'fares.csv'
with open(filename) as json_file: #read initial csv file
    for n_lines in iter(lambda: tuple(islice(json_file, n)), ()): # split the csv in batches
        process(n_lines) # Send current batch
        time.sleep(5) #sleep for 5 s


        