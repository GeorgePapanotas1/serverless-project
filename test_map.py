import json
import functools

def addition(n):
    return n + n

def getMyData():
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
    center_long = -73.89936203417709
    center_lat = 40.67686451914928
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
        
def myReducer(n):
    res = []
    for i in n:
        counter = 0
        for j in range(len(i[1])):
            
            counter+=1
        res.append([i[0], counter])
    return res

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(first_mapper, getMyData())

# print(shuffle(list(result)))


print(myReducer(shuffle(list(result))))
# print (functools.reduce(lambda a,b : a+b,list(result)))
# print(getMyData())
