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

def create_project(name, description, username ):

    print(name)
    print(description)
    print(username)

    if does_project_nameexist(name):
        response = {"Access": False}
        return response
    
    allocated = [0,0]
    
    collection_projects.insert_one({"Name": name, "Description": description, "Users": [], "Allocation": allocated})
    
    print("problem")
    response = join_project(username, name)
    print(response)
    return response

def join_project(username, projectName):
    # if  username in collection_projects.find_one({"Name": projectName})["Users"]: # Unused?
    #     response = {"Access": False, "Message": "User Already In Project"}
    #     return response
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
        print("error1")
        
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
        print("error2")
        response = {"Access": True }
        return response
    else:
        response = {"Access": False, "Message": "Project Does Not Exists" }
        return response
    
def leave_project(username, projectName):
    print("hello")
    print(len(collection_projects.find_one({"Name": projectName})["Users"]))
    if len(collection_projects.find_one({"Name": projectName})["Users"]) == 1:
        print("first if")
        response = {"Access": False}
        return response
    # if  username not in collection_projects.find_one({"Name": projectName})["Users"]: # Unused?
    #     print("second if")
    #     response = {"Access": False }
    #     return response
    if (does_project_nameexist(projectName)):
        print("third if")
        data = collection_projects.find_one({"Name": projectName})["_id"]
        query = {"_id": data}
        update = {
            "$pull": {
                "Users": username
            }
        }
        collection_projects.update_one(query, update)
        
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
        print("else")
        response = {"Access": False }
        return response

def projectList(username):

    collections = client["Users"] # name of the database
    collection_users = collections["user_password"] # name of collection
    project_list = collection_users.find_one({"username": username})["projects"]
    # print(project_list)
    
    mylist = []
    for project in project_list:
        # print(project)
        info_list = []
        info_list.append(project)
        info_list.append(collection_projects.find_one({"Name": project})["Description"])
        # print(info_list)
        

        collections_HW = client["Hardware"]
        x = collections_HW["hardware_set"]
        collections_HWS = x.find()
        # print(collections_HWS)

        Sets = []
        tracker = 0
        # print(tracker)
        for item in collections_HWS:
            # print(item)
        
            hw = []
            hardwareData = Mongodb_Hardware.availability_capacity(item["name"])
            hw.append(hardwareData["capacity"])
            hw.append(hardwareData["availability"])
            # print(hw)
            temp = collection_projects.find_one({"Name": project})["Allocation"][tracker]
            # print(temp)
            hw.append(temp)
            # print(hw)
            Sets.append(hw)
            tracker += 1
        info_list.append(Sets)
        mylist.append(info_list)
        # print()
        
    response = {"projectList": mylist}
    return response

# if __name__ == '__main__':
#     projectList(":;5oyn")
    # collections_HW = client["Hardware"]
    # x = collections_HW["hardware_set"]
    # collections_HWS = x.find({})

    # Sets = []
    # tracker = 0
    # print(collections_HWS)
    # for item in collections_HWS:
    #     print(tracker)
        
        
    #     hw = collection_projects.find_one({"Name": "Project1"})["Allocation"][tracker]
    #     tracker += 1
    #     print(hw)
        

    # print(Sets)
    