import googlemaps
from datetime import datetime
import pprint

gmaps = googlemaps.Client(key='AIzaSyB7BkwSe4-5V14C3wY301HVolGN2IdO2PA')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
#directions_result = gmaps.directions("San Jose State University", "San Jose, CA", mode="driving", departure_time=now)

distanceMatrix = gmaps.distance_matrix('San Jose State University, San Jose, CA', '777 Story Rd, San Jose ,CA', mode='driving', departure_time=now, units='imperial')


#pprint.pprint(geocode_result)

#pprint.pprint(reverse_geocode_result)

#pprint.pprint(directions_result)

#pprint.pprint(distanceMatrix)

for x, y in distanceMatrix['rows'][0]['elements'][0]['distance'].iteritems(): 
	print x, y
#secondsUntilArrival = distanceMatrix['rows'][0]['elements'][0]['duration_in_traffic']['value']
#print secondsUntilArrival
