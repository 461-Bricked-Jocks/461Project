from pymongo.mongo_client import MongoClient

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

# Users
data_base = client["Users"] #name of the database

collection_users = data_base["user_password"] #name of collection

# Projects
data_base = client["Projects"]

collection_projects = data_base["projects"]

# Hardware Sets
data_base = client["Hardware"] #name of the database

collection_hardware = data_base["hardware_set"] #name of collection
