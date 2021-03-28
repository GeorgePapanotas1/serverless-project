import json
import math


def calculateDistance(lat1, lon1, lat2, lon2):
    R = (6371)
    φ1 = lat1 * math.pi/180
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180

    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

def getMyData():
    # Extract pickup_long and pickup_lang
    transformed_data = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for el in data: 
            thisdict = {
                "pickup_longitude" : el["pickup_longitude"],
                "pickup_latitude" : el["pickup_latitude"],
                "dropoff_longitude" : el["dropoff_longitude"],
                "dropoff_latitude" : el["dropoff_latitude"],
                "trip_duration" : el["trip_duration"],
                "passenger_count" : el["passenger_count"]
            }
            transformed_data.append(thisdict)
    return transformed_data


def mapper(n):

    trip_distance = calculateDistance(n["pickup_latitude"], n["pickup_longitude"], n["dropoff_latitude"], n["dropoff_longitude"])
    if(trip_distance > 10 and n["passenger_count"] >= 2 and n["trip_duration"] > 600):
        return ['kati', 1]

def reducer(n):
    counter = 0
    for i in n:
        if(i!=None):
            counter+=1
    return counter
print(reducer(list(map(mapper, getMyData()))))
 	














#  μεγαλύτερες του ενός χιλιομέτρου , διάρκειας μεγαλύτερης των 10 λεπτών , με περισσότερους από δύο πελάτεs




#  pickup_longitude
#  pickup_latitude

#  dropoff_longitude
#  dropoff_latitude


#  trip_duration > 600 (in seconds > 600)

#  passenger_count > 2