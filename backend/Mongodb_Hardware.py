from pymongo.mongo_client import MongoClient

from flask import Flask, jsonify, request
import pymongo

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

uri = "mongodb+srv://Claudio98cm:AtlasCeltics08@users.wi78xyi.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri,
                    tls=True,
                    tlsAllowInvalidCertificates=True)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


##database for Harware
data_base = client["Hardware"] #name of the database
collection_hardware = data_base["hardware_set"] #name of collection

#insert document in collection
#change name to desciprion
'''
document_hardware = {"name": "Hardware Set 1", "capacity": "50", "availability": "50"}

document_hardware_id = collection_hardware.insert_one(document_hardware).inserted_id
print(document_hardware_id)
print(document_hardware)
#had this one going
#collection_hardware.insert_one(document_hardware)

#Query documents in the collection
#result = collection.find({"name": "project1"})
#prompt the user to enter they're wanted username

myquery = {"name":"project1"}
x = collection_hardware.find_one(myquery)
print(x['name'])
if (x['name']=='project1'):
    print("name exist\n")
else:
    print("name not found\n")
'''

def checkIn(name, qty): # TODO
    hardwareSet = collection_hardware.find_one({"name": name})
    availability = int(collection_hardware["availability"]) + qty # IDK if this the right way to get this value
    availability = str(availability)
    
def checkOut(name, qty): # TODO
    pass

def main():
    #queryHWSet1Availability()
    print("aa")

if __name__ == "__main__":
    main()
