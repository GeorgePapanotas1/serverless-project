import pandas
import json

df = pandas.read_csv('test.csv')
result = df.to_json(orient="records")
parsed = json.loads(result)

with open('data.json', 'w') as outfile:
    json.dump(parsed, outfile)
    