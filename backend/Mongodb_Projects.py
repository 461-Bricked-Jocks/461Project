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

def create_project(name, description):
    if does_project_nameexist(name):
        response = {"Access": False}
        return response
    
    # if does_project_IDexist(projectid):
    #     print("projectid taken")
    #     return False
    
    collection_projects.insert_one({"Name": name, "Description": description, "Users": []})
    response = {"Access": True}
    return response

def join_project(username, password, projectName):
    if  username in collection_projects.find_one({"Name": projectName})["Users"]: # Unused?
        response = {"Access": False }
        return response
    if (does_project_nameexist(projectName)):
        data = collection_projects.find_one({"Name": projectName})["_id"]
        query = {"_id": data}
        update = {
            "$push": {
                "Users": username
            }
        }
        collection_projects.update_one(query, update)
        
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        data = collection_users.find_one({"username": username, "password": password})["_id"]
        query = {"_id": data}
        update = {
            "$push": {
                "projects": projectName
            }
        }
        collection_projects.update_one(query, update)
    else:
        response = {"Access": False }
        return response
    
def leave_project(username, password, projectName):

    # TODO Don't Leave unless there exists more than 1 user
    
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
        collection_projects.update_one(query, update)
        
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        data = collection_users.find_one({"username": username, "password": password})["_id"]
        query = {"_id": data}
        update = {
            "$pull": {
                "projects": projectName
            }
        }
        collection_projects.update_one(query, update)
    else:
        response = {"Access": False }
        return response

def projectList(username, password): #  TODO Do I need to encrpty again?
    # username = cipher.encrypt(username,3,1)
    # password = cipher.encrypt(password,3,1)
    try:
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        project_list = collection_users.find_one({"username": username, "password": password})["projects"]
        
        mylist = []
        for project in project_list:
            info_list = []
            info_list.append(project)
            info_list.append(collection_projects.find_one({"name": project})["Description"])

            hardwareData = Mongodb_Hardware.availability_capacity("Hardware Set 1")
            info_list.append(hardwareData["capacity"])
            info_list.append(hardwareData["availability"])

            hardwareData = Mongodb_Hardware.availability_capacity("Hardware Set 2")
            info_list.append(hardwareData["capacity"])
            info_list.append(hardwareData["availability"])
            
            mylist.append(info_list)
            
        response = {"projectList": mylist}
        return response
    except Exception as e:
        print(f'Error accessing the users collection: {e}')

# if __name__ == '__main__':

#     # collection_projects.insert_one({"Name": "Project5", "Description": "Minecraft", "ProjectID": "005", "Users": []})
#     data = collection_projects.find_one({"Name": "Project5", "Description": "Minecraft", "ProjectID": "005", "Users": []})["_id"]
#     print(data)
#     query = {"_id": data}
#     qty = 5
#     update = {
#         "$push": {
#             "Users": qty
#         }
#     }
#     result = collection_projects.update_one(query, update)
#     print(result)