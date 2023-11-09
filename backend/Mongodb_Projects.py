from pymongo.mongo_client import MongoClient

from flask import Flask, jsonify, request
import pymongo
import cipher

import Mongodb_Hardware
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

data_base = client["Projects"]

collection_projects = data_base["projects"]

document_project = {"Name": "Project 1", "Description": "app", "ProjectID": "000"}
#collection_projects.insert_one(document_project)

def does_project_nameexist(name):
    existing_name = collection_projects.find_one({"Name": name})
    if existing_name is None:
        return False
    else:
        return True

def does_project_IDexist(projectid):
    existing_projectid = collection_projects.find_one({"ProjectID": projectid})
    if existing_projectid is None:
        return False
    else:
        return True

def create_project(name, description, username ):
    if does_project_nameexist(name):
        response = {"Access": False}
        return response

    collection_projects.insert_one({"Name": name, "Description": description, "Users": []})
    response = join_project(username, name)
    return response

def join_project(username, projectName):
    if  username in collection_projects.find_one({"Name": projectName})["Users"]: # Unused?
        response = {"Access": False, "Message": "User Already In Project"}
        return response
    if (does_project_nameexist(projectName)):
        print("this runs")
        data = collection_projects.find_one({"Name": projectName})["_id"]
        query = {"_id": data}
        print(query)
        update = {
            "$push": {
                "Users": username
            }
        }
        collection_projects.update_one(query, update)
        
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        data = collection_users.find_one({"username": username})["_id"]
        query = {"_id": data}
        update = {
            "$push": {
                "projects": projectName
            }
        }
        collection_users.update_one(query, update)
        response = {"Access": True }
        return response
    else:
        response = {"Access": False, "Message": "Project Does Not Exists" }
        return response
    
def leave_project(username, projectName):
    if len(collection_projects.find_one({"Name": projectList})) == 1:
        response = {"Access": False}
        return response
    if  username not in collection_projects.find_one({"Name": projectName})["Users"]: # Unused?
        response = {"Access": False }
        return response
    if (does_project_nameexist(projectName)):
        data = collection_projects.find_one({"Name": projectName})["_id"]
        query = {"_id": data}
        update = {
            "$pull": {
                "Users": username
            }
        }
        collection_users.update_one(query, update)
        
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        data = collection_users.find_one({"username": username})["_id"]
        query = {"_id": data}
        update = {
            "$pull": {
                "projects": projectName
            }
        }
        collection_users.update_one(query, update)
        response = {"Access": True }
        return response
    else:
        response = {"Access": False }
        return response

def projectList(username):

    try:
        collections = client["Users"] # name of the database
        collection_users = collections["user_password"] # name of collection
        project_list = collection_users.find_one({"username": username})["projects"]
        
        mylist = []
        for project in project_list:
            info_list = []
            info_list.append(project)
            info_list.append(collection_projects.find_one({"Name": project})["Description"])
            

            collections_HW = collections["hardware_set"]

            Sets = []
            tracker = 0
            for item in collections_HW:
                hw = []
                hardwareData = Mongodb_Hardware.availability_capacity(item["name"])
                hw.append(hardwareData["capacity"])
                hw.append(hardwareData["availability"])
                hw.append(collection_projects.find_one({"Name": project})["Allocated"][tracker])
                Sets.append(hw)
                tracker += 1
            info_list.append(Sets)
            mylist.append(info_list)

            # hw1 = []
            # hardwareData = Mongodb_Hardware.availability_capacity("Hardware Set 1")
            # hw1.append(hardwareData["capacity"])
            # hw1.append(hardwareData["availability"])
            # hw1.append(collection_projects.find_one({"Name": project})["Allocated"][0])

            # hw2 = []
            # hardwareData = Mongodb_Hardware.availability_capacity("Hardware Set 2")
            # hw2.append(hardwareData["capacity"])
            # hw2.append(hardwareData["availability"])
            # hw2.append(collection_projects.find_one({"Name": project})["Allocated"][1])

            # hwSets = []
            # hwSets.append(hw1)
            # hwSets.append(hw2)

            # info_list.append(hwSets)
            # mylist.append(info_list)
            
        response = {"projectList": mylist}
        return response
    except Exception as e:
        print(f'Error accessing the users collection: {e}')

# if __name__ == '__main__':
#     x = 0
#     data = collection_projects.find_one({"Name": "Project5"})["_id"]
#     query = {"_id": data}
#     print(query)
#     update = {
#         "$set": {
#             f'Allocated.{x}': 3
#         }
#     }
#     collection_projects.update_one(query, update)