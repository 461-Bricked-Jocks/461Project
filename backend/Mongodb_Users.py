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

'''
document_users = {"username": "cm", "password": "123"}
#if (does_username_exist(document_users["username"]):
collection_users.insert_one(document_users)


#query if username exist
#document_users = {"username": "cm", "password": "123"}

#prompt the user to enter they're wanted username
myquery = {"username":"cm"}
x = collection_users.find_one(myquery)
print(x['username'])
if (x['username']=='cm'):
    print("username exist\n")
else:
    print("Username not found\n")
'''

def existingAccount(username, password):
    username = cipher.encrypt(username)
    password = cipher.encrypt(password)
    if does_username_exist(username):
        if collection_users.find_one({"username": username, "password": password}) is not None:
            data = collection_users.find_one({"username": username, "password": password})['projects']
            response = {"Access": True, "Projects": data}
            return response
    response = {"Access": False}
    return response

##checking if user exist or not
def does_username_exist(username):
    existing_user = collection_users.find_one({"username": username})
    return existing_user is not None


def create_user(username, password):
    username = cipher.encrypt(username)
    password = cipher.encrypt(password)
    if does_username_exist(username):
        # print("Username taken")
        response = {"Access": False}
        return response


    #username unique
    collection_users.insert_one({"username": username, "password": password, "projects": []})
    # print("User creation succesful")
    response = {"Access": True}
    return response


def login_user(username, password):
    
    if existingAccount(username, password):
        print("Access granted")
        return True

if __name__ == '__main__':
    new_user = input("enter username: ")
    new_password = input("enter password: ")

    create_user(new_user, new_password)
    login_user(new_user, new_password)



'''
##############
app = Flask(__name__)

def register_user():
    data = request.get_json()

    #checking if the username exist
    existing_username =  collection_users.find_one({"username": data["username"]})
    if existing_username:
        return jsonify({"message" : "Username already exists. Choose a different one"})

    #if username unique
    collection_users.insert_one({"username": "cm", "password": "123"})
    return jsonify({"message": "User succesfully registere"}), 201

#if __name__ == '__main__':
#    app.run(debug=True)
'''

'''
if(collection_users.find(document_users.keys()) != False):
    collection_users.insert_one(document_users)
'''