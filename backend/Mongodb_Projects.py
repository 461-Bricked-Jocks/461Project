from pymongo.mongo_client import MongoClient

from flask import Flask, jsonify, request
import pymongo

uri = "mongodb+srv://Claudio98cm:AtlasCeltics08@users.wi78xyi.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
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
    return existing_name is not None

def does_project_IDexist(projectid):
    existing_projectid = collection_projects.find_one({"ProjectID": projectid})
    return existing_projectid is not None

#joining exisitng project
def existing_project(projectid):
    if does_project_IDexist(projectid):
        return True
    else:
        return False

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

def login_projectid(projectid):
    if (existing_project(projectid)):
        print("project access granted")
        return True

    print("projectid doesn't exist")
    return False

if __name__ == '__main__':

    new_project_name = input("enter project name: ")
    new_project_description = input("enter project description: ")
    new_project_id = input("enter project id: ")

    create_project(new_project_name, new_project_description, new_project_id)

    existing_project_id = input("enter project id: ")
    login_projectid(existing_project_id)