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

def checkIn(name, qty): #todo
    hardwareSet = collection_hardware.find_one({"name": name})
    if hardwareSet:
        avilability = hardwareSet["availability"]
        capacity = hardwareSet["capacity"]
        
        if int(qty) >= 0: 
            #if(qty > )
            avilability = int(avilability) + int(qty) # IDK if this the right way to get this value
            if (avilability <= int(capacity)):
                collection_hardware.update_one({"name": name}, {"$set": {"availability": str(avilability)}}) 
                response = {"availability": avilability}
            else:
                collection_hardware.update_one({"name": name}, {"$set": {"availability": str(capacity)}}) 
                response = {"Error Hardware set": "more than original capacity"}
                print(response)


        else:
            response = {"Error Hardware set": "qty error"}
            print(response)

    else:
        response = {"Error Hardware set": "name error"}
        print(response)
    

    
def checkOut(name, qty): #todo
    hardwareSet = collection_hardware.find_one({"name": name})
    if hardwareSet:
        avilability = hardwareSet["availability"]

        if int(qty) >= 0:
            if(qty > avilability):
                avilability = int(avilability) - int(avilability)
 
            #avilability =  int(avilability) - int(qty)
    
                collection_hardware.update_one({"name": name}, {"$set": {"availability": str(avilability)}}) 
                response = {"availability": avilability}
            else:
                avilability =  int(avilability) - int(qty)


                #print(avilability, 'here')
                collection_hardware.update_one({"name": name}, {"$set": {"availability": str(avilability)}}) 

                response = {"availability": avilability}
        else:
            response = {"Error Hardware set": "qty error"}
            print(response)
    else:
        response = {"Error Hardware set": "name error"}
        print(response)
    
    return response

def availability_capacity(name): #todo
    hardwareSet = collection_hardware.find_one({"name": name})
    if hardwareSet:
        avilability = hardwareSet["availability"]
        capacity = hardwareSet["capacity"]
   
        print("capacity: ", capacity)
        response = {"Access": True, "availability": avilability, "capacity": capacity}
        print(response)
    else:
        response = {"Access": False, "Error Hardware set": "error" }
        print(response)
        
    return response



def main():
    #queryHWSet1Availability()
    projectHardware_name = input("enter projectHardware: ")
    availability_capacity(projectHardware_name)
    in_0 = input("enter amount checkIn: ")
    checkIn(projectHardware_name, in_0)
    #checkOut(projectHardware_name, 30)
    #availability_capacity(projectHardware_name)
    #checkIn(projectHardware_name, 20)
    #availability_capacity(projectHardware_name)
    in_1 = input("enter amount checkOut: ")
    checkOut(projectHardware_name, in_1)
   
   
    availability_capacity(projectHardware_name)

if __name__ == "__main__":
    main()
