import googlemaps
from datetime import datetime
from math import radians, sqrt, sin, cos, atan2


def google_geo(APIkey,location_from,location_to,travel_model):

    gmaps = googlemaps.Client(key=APIkey)

    # Geocoding an address
    geocode_result = gmaps.geocode(location_from)

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(location_from,
                                         location_to,
                                         mode=travel_model,
                                         departure_time=now)
    data = [directions_result[0]['bounds']['northeast'], directions_result[0]['bounds']['southwest']]

    print('Distance: ', directions_result[0]['legs'][0]['distance']['text'])
    print('How long will it take: ', directions_result[0]['legs'][0]['duration']['text'])

    return difference_coor(data[0],data[1])



def geocalc(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon1 - lon2

    EARTH_R = 6372.8

    y = sqrt(
        (cos(lat2) * sin(dlon)) ** 2
        + (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
        )
    x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = atan2(y, x)
    return "As the crow flies: {} km long".format(round(EARTH_R * c,2))




def difference_coor(x,y):
    a = []

    for item in x:

        a.append(x[item])
    for item in y:

        a.append(y[item])


    return geocalc(a[0],a[1],a[2],a[3])



location_from = input("Enter exact address of location from 'maps.google.com" '\n'
                      "Example : Piccadilly Circus, Soho, London W1D 7ET, UK")
location_to = input("Enter exact address of location from 'maps.google.com" '\n'
                      "(Example : Apsley Way, London W1J 7JZ, UK):")

API_Key = input("Enter the API Key from you get from developer.google.com/geolocation")

travel_models = input('Which travel model?:'"\n"'driving'"\n"'walking'"\n"'bicycling'"\n"'Please give exact name')

print(google_geo(API_Key,location_from,location_to,travel_models))



