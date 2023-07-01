import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = os.environ.get("MONGO_DBNAME")
COLLECTION = "movies"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# Read in CRUD
# to find specific collections we can pass a dictionary in as a parameter coll.find({"key": "value"})
# to find the first document that statisfies the criteria we can also use .find_one()
documents = coll.find()

for doc in documents:
    print(doc)