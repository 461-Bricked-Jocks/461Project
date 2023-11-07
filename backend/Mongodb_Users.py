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


#creating database for Users 
data_base = client["Users"] #name of the database
#data_base = client.Users
collection_users = data_base["user_password"] #name of collection
#collection_users = data_base.user_password


def existingAccount(username, password):
    username = cipher.encrypt(username,3,1)
    password = cipher.encrypt(password,3,1)
    if collection_users.find_one({"username": username, "password": password}) is not None:
        response = {"Access": True, "Username": username, "Password": password}
        return response
    response = {"Access": False}
    return response

##checking if user exist or not
def does_username_exist(username):
    existing_user = collection_users.find_one({"username": username})
    if(existing_user is None):
        return False
    else:
        return True
    

def create_user(username, password):
    username = cipher.encrypt(username,3,1)
    password = cipher.encrypt(password,3,1)
    if does_username_exist(username):
        # print("Username taken")
        response = {"Access": False}
        return response
    #username unique
    collection_users.insert_one({"username": username, "password": password, "projects": []})
    # print("User creation succesful")
    response = {"Access": True}
    return response

# if __name__ == '__main__':
#     new_user = input("enter username: ")
#     new_password = input("enter password: ")

#     create_user(new_user, new_password)
