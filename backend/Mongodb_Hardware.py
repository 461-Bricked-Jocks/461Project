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

data_base = client["Projects"]
collection_projects = data_base["projects"]
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

def checkIn(project, name, qty): #todo
    hardwareSet = collection_hardware.find_one({"name": name})
    if hardwareSet:
        availability = int(hardwareSet["availability"])
        capacity = int(hardwareSet["capacity"])
        #updating project sets
        projectName = collection_projects.find_one({"Name": project})
        if projectName:
            x = hardwareSet["ID"]
            #amount = collection_projects["Allocated"][x]
            amount = int(collection_projects.find_one({"Name": project})["Allocation"][x])
        

            if qty >= 0 and qty <= amount: 
                #if(qty > )
                availability = availability + int(qty) # IDK if this the right way to get this value
                projectHamount = amount - int(qty)

                if (availability <= int(capacity)):
                    collection_hardware.update_one({"name": name}, {"$set": {"availability": str(availability)}})

                    #collection_projects.update_one({"Name": project}, {"$set": {"Allocated"[x]: }})
                    #updating project
                    query = {"Name": project}
                    update = {
                        "$set": {
                            f'Allocation.{x}': projectHamount
                        }
                    }
                    collection_projects.update_one(query, update)

                    #response = {"Access": True, "availability": availability, "capacity": capacity}
                    response = {"Access": True}
                else:
                    collection_hardware.update_one({"name": name}, {"$set": {"availability": str(capacity)}}) 
                    #response = {"Error Hardware set": "more than original capacity"}
                    query = {"Name": project}   # Kiet Added as of 11/9
                    update = {
                        "$set": {
                            f'Allocation.{x}': 0
                        }
                    }
                    collection_projects.update_one(query, update)
                    response = {"Access": True}
                    #response = {"Access": True, "availability": availability, "capacity": capacity}
                return response

            elif qty > amount: # Kiet Added as of 11/9
                availability += amount
                collection_hardware.update_one({"name": name}, {"$set": {"availability": str(availability)}})
                query = {"Name": project}
                update = {
                    "$set": {
                        f'Allocation.{x}': 0
                    }
                }
                collection_projects.update_one(query, update)

            else:
                #response = {"Access": False, "Error": "qty error"}
                response = {"Access": False}
        
            return response


    else:
        response = {"Access": False}
        #response = {"Access":False, "Error": "Hardware set name error"}
        #response = {"Access": False, "availability": availability, "capacity": capacity}
    
        return response

    

    
def checkOut(project, name, qty): #todo
    print("initial")
        
    print(collection_hardware.find_one({"name": name}))
    hardwareSet = collection_hardware.find_one({"name": name})
    
    if hardwareSet:
        print("checkpoint 1")
        availability = int(hardwareSet["availability"])
        capacity = int(hardwareSet["capacity"])

        
        projectName = collection_projects.find_one({"Name": project})
        if projectName:
            print("checkpoint 2")
            x = hardwareSet["ID"]
            print(x)
            amount = collection_projects.find_one({"Name": project})["Allocation"][x]
            print(amount)
            print(qty)
            print(type(int(qty)))
            print
        #x = collection_projects.find_one({"name": project})["ID"]
        #amount = collection_projects["Allocated"][x]

            #if int(qty) >= 0 and int(qty) <= int(amount):
            if qty >= 0:
                print(availability)
                if(qty > availability):
                    print("checkpoint 3A")
                    
                    
                    #response = {"Access": False, "Error": "Quantity error"}
                    response = {"Access": False}
                else:
                    print("checkpoint 3B")
                    availability =  int(availability) - int(qty)
                    print(availability)
                    collection_hardware.update_one({"name": name}, {"$set": {"availability": str(availability)}})

                    ##updating project hardware amount
                    projectHamount = int(amount) + int(qty)
                    query = {"Name": project}
                    update = {
                        "$set": {
                            f'Allocation.{x}': projectHamount
                        }
                    }
                    collection_projects.update_one(query, update)


                    
                    #response = {"Access": True, "availability": availability, "capacity": capacity}
                    response = {"Access": True}
                return response

            else:
                print("this is no bueno")
                #response = {"Access": False, "Error": "qty error"}
                response = {"Access": False}

            return response
    else:
        #response = {"Access": False, "Error": "Hardware set name error"}
        response = {"Access": False}
    return response

def availability_capacity(name): #todo
    hardwareSet = collection_hardware.find_one({"name": name})
    if hardwareSet:
        availability = hardwareSet["availability"]
        capacity = hardwareSet["capacity"]
   
        #print("capacity: ", capacity)
        response = {"Access": True, "availability": availability, "capacity": capacity}
        #response = {"Access": True}
    else:
        response = {"Access": False, "Error": "Hardware set name error" }
        #print(response)
        
    return response


'''
def main():
    #queryHWSet1Availability()
    projectHardware_name = input("enter projectHardware: ")
    availability_capacity(projectHardware_name)
    project_name = input("enter projectname: ")
    in_0 = input("enter amount checkIn: ")
    #checkIn(project_name, projectHardware_name, in_0)
    checkOut(project_name, projectHardware_name, in_0)
    #checkOut(projectHardware_name, 30)
    #availability_capacity(projectHardware_name)
    #checkIn(projectHardware_name, 20)
    #availability_capacity(projectHardware_name)
    
    in_1 = input("enter amount checkOut: ")
    checkOut(projectHardware_name, in_1)
    
   
    availability_capacity(projectHardware_name)
'''
# if __name__ == "__main__":
#     checkOut("Project1","Hardware Set 1",100)
