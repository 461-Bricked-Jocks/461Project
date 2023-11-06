from pymongo.mongo_client import MongoClient

from flask import Flask, jsonify, request
import pymongo
import cipher

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

def create_project(name, description, projectid):
    if does_project_nameexist(name):
        print("Project name taken")
        return False
    
    if does_project_IDexist(projectid):
        print("projectid taken")
        return False
    
    collection_projects.insert_one({"Name": name, "Description": description, "ProjectID": projectid})
    print("project creation succesful")
    return True

def join_projectid(projectName):
    if (does_project_nameexist(projectName)):
        data = collection_projects.find_one({"Name": projectName})
        response = {"Name": data["Name"], "Description": data["Description"]}  # TODO 
        return 
    else:
        response = {"Access": False }
        return response

def projectList(username, password): #  TODO Incomplete need to return all the project names, description, hardware sets
    username = cipher.encrypt(username,3,1)
    password = cipher.encrypt(password,3,1)
    try:
        collections = client["Users"] #name of the database
        collection_users = collections["user_password"] #name of collection
        projects = collection_users.find_one({"username": username, "password": password})["projects"]
        return projects
    except Exception as e:
        print(f'Error accessing the users collection: {e}')

# TODO Return All the project names, description, hardware sets

######## TODO Leave Project ##############


if __name__ == '__main__':

    new_project_name = input("enter project name: ")
    new_project_description = input("enter project description: ")
    new_project_id = input("enter project id: ")

    create_project(new_project_name, new_project_description, new_project_id)

    existing_project_id = input("enter project id: ")
    login_projectid(existing_project_id)