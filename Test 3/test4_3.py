from pymongo import MongoClient
from random import randint
import datetime
import urllib2
import time
import sys

#Connection to Mongo DB example:
#Test number 1: Test number 1 Francois Doray - ct 

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

try:
    client = MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e

db = client.mydb
collection = db.my_collection

#insertion:
#start = time.time()
response = urllib2.urlopen('http://python.org/')
html = response.read()

total = 0
upper = 0
bigger = 0

if len(sys.argv) > 1 and str(sys.argv[1]) > 1:
    for i in range(0,int(sys.argv[1])):
        html.append(html)

for x in range(0, 1000):
    i = randint(0,10000)
    j = randint(0,10000)
    start = time.time()
    ##response = urllib2.urlopen('http://python.org/')
    #html = response.read()
    doc = {"name":"Alberto","surname":"N","twitter":"@Altons","id":i*j,"Acident date": datetime.datetime.utcnow(),"nick":"Alb.","gender":"M","face":"/Altons2","id":27*(i*j),"Borndate": datetime.datetime.utcnow(),"person":"Alb.","G":"M","T":"/Altons2","X":17*(i*j),"page1":html,"page2":html,"page3":html,"page4":html,"page5":html,"page6":html,"page7":html,"page8":html,"page9":html,"page10":html,"page11":html,"page12":html,"page13":html,"page14":html,"page15":html,"page16":html,"page17":html,"page18":html,"page19":html,"page20":html,"page21":html,"page22":html,"page23":html,"page24":html,"page25":html,"page26":html,"page27":html,"page28":html,"page29":html,"page30":html}

    #"page": html}
    collection.insert(doc)
    end = time.time()
    begin_end = end - start
    if begin_end >0.02:
        upper+=1
    if begin_end >bigger:
        bigger = begin_end

    print begin_end
    total += begin_end
#see the status:
print ("Mean Total")
print (total/1000)
print ("Upper limit:")
print (upper)
print ("Bigger:")
print (bigger)

client.database_names()
db.collection_names()

collection.drop()
