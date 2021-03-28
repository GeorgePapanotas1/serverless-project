import json

def getMyData():
    # Extract pickup_long and pickup_lang
    transformed_data = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for el in data: 
            thisdict = {
                "pickup_longitude": el['pickup_longitude'],
                "pickup_latitude": el['pickup_latitude'],
            }
            transformed_data.append(thisdict)
        return transformed_data


def first_mapper(n):

    #mapper logic, use a random spot in New York and use it to split the city in quarters
    center_long = -73.89936203417709
    center_lat = 40.67686451914928

    # Split logic. dd | aa
    #              -------
    #              cc | bb

    if float(n['pickup_longitude']) > center_long and float(n['pickup_latitude']) > center_lat:
        return ['aa', 1]
    elif float(n['pickup_longitude']) > center_long and float(n['pickup_latitude']) < center_lat:
        return ['bb', 1]
    elif float(n['pickup_longitude']) < center_long and float(n['pickup_latitude']) < center_lat:
        return ['cc', 1]
    elif float(n['pickup_longitude']) < center_long and float(n['pickup_latitude']) > center_lat:
        return ['dd', 1]

def shuffle(n):
    a = ["aa", []]
    b = ["bb", []]
    c = ["cc", []]
    d = ["dd", []]
    for i in n:
        if i[0] == "aa":
            a[1].append(1)
        elif i[0] == "bb":
            b[1].append(1)
        elif i[0] == "cc":
            c[1].append(1)
        elif i[0] == "dd":
            d[1].append(1)
    return [a, b, c, d]
    # Shuffle the mapped data into eg ["aa", [1,1,1]] 
        
def myReducer(n):
    res = []
    for i in n:
        counter = 0
        for j in range(len(i[1])):
            
            counter+=1
        res.append([i[0], counter])
    return res

print(myReducer(shuffle(list(map(first_mapper, getMyData())))))
