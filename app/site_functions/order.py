from flaskext.mysql import MySQL
from flask import Flask, current_app
from settings import app_setup
import googlemaps
from datetime import datetime
import pprint

app = app_setup()
mysql = MySQL()
mysql.init_app(app)
gmaps = googlemaps.Client(key='AIzaSyB7BkwSe4-5V14C3wY301HVolGN2IdO2PA')

class Order:

    def __init__(self, transID):       
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from orders where transID =" + str(transID) ) 
        row = cursor.fetchone()
        self.items = row[4]
        self.totalCost = row[2]
        self.orderPlacedTime = row[3]
        self.deliveryAddress = row[5]
        self.storeAddress = row[6]
        self.deliveryEstimateTotalSeconds = row[7]
        self.deliveryDistanceMeters = row[8]
        self.deliveryDistanceMiles = row[9]
        self.speed = row[10]
    
    
    def getTimeUntilDelivered(self):
        if datetime.now() < self.orderPlacedTime:
            return -1
            #raise('Order Placed In The Future')
        try:
            ## delivery estimate time from google API - (current time - order placed time)
            timeUntilDelivered = self.deliveryEstimateTotalSeconds - ( datetime.now() - self.orderPlacedTime ).seconds
            return timeUntilDelivered if timeUntilDelivered > 0 else 0
        except:
            return 'error'
        
    def getDeliveryStatus(self):
        timeUntilDelivered = self.getTimeUntilDelivered()
        if timeUntilDelivered == 'error':
            return 'Unknown'
        elif timeUntilDelivered == 0:
            return 'Delivered'
        elif timeUntilDelivered < 0:
            return 'Preparing Shipment' ## actually an error, orderPlacedTime is in the future
        else:
            return 'Out For Delivery'
    
    def getCurrentLocation(self):
        timeUntilDelivered = self.getTimeUntilDelivered()
        print (timeUntilDelivered)
        if timeUntilDelivered == 0:
            return self.deliveryDistanceMeters
        elif timeUntilDelivered < 0:
            return 0
        else:
            return (self.deliveryEstimateTotalSeconds - timeUntilDelivered) * self.speed       ## time elapsed * speed


def getClosestStore(address):
    closestStore = ('store', None)
    cursor = mysql.connect().cursor()
    cursor.execute("select  CONCAT('\\'', store.street, ', ', store.city, ', ', store.state, '\\'') from store") 
    listOfStores = cursor.fetchall()#, '1107 S King Rd, San Jose, CA', 'walmart mountain view, CA', 'safeway shoreline blvd mountain view, CA']
    for store in listOfStores:
        distanceMatrix = gmaps.distance_matrix(str(store[0]), address, mode='driving', departure_time=datetime.now(), units='imperial')
        tempDistance = distanceMatrix['rows'][0]['elements'][0]['distance']['value']
        #print store        
        #print distanceMatrix['rows'][0]['elements'][0]['distance']['text']
        #print tempDistance
        #print '--------'
        if (closestStore[1] == None):
            closestStore = (store, tempDistance)
        elif(tempDistance < closestStore[1]):
            closestStore = (store, tempDistance)
        else:
            pass
    return closestStore


def getDeliveryInfo(deliveryAddress):
    try:
        #distanceMatrix = gmaps.distance_matrix(self.storeAddress, self.deliveryAddress, mode='driving', departure_time=datetime.now(), units='imperial')
        #deliveryEstimateSeconds = distanceMatrix['rows'][0]['elements'][0]['duration_in_traffic']['value']     
        closestStore = getClosestStore(deliveryAddress)
        print ("CLOSEST " + str(closestStore))
        directions = gmaps.directions( str(closestStore) , deliveryAddress, mode='driving', departure_time=datetime.now(), units='imperial')
        
        deliveryEstimateTotalSeconds = directions[0]['legs'][0]['duration_in_traffic']['value']
        deliveryDistanceMeters = directions[0]['legs'][0]['distance']['value']
        deliveryDistanceMiles = directions[0]['legs'][0]['distance']['text']
        speed = round(float(deliveryDistanceMeters)/float(deliveryEstimateTotalSeconds),5)  ## meters per second
        return closestStore, deliveryAddress, deliveryEstimateTotalSeconds, deliveryDistanceMeters, deliveryDistanceMiles, speed
    except Exception as e:
        print(e)


def debug_stage():
    items1 = ['item1', 'item2', 'item3']
    orderPlacedTime1 = datetime.strptime('2016-10-22 19:11:12', '%Y-%m-%d %H:%M:%S')
    deliveryAddress = '1 Washington Square, San Jose, CA'
    order1 = Order(items1, 52, orderPlacedTime1, *getDeliveryInfo(deliveryAddress))
    
    print(order1.getTimeUntilDelivered())
    print(order1.getDeliveryStatus())
    print(order1.speed)
    print(order1.getCurrentLocation())


if __name__ == '__main__':
    debug_stage()
