import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "movieCrazyClub"
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

# Delete in CRUD
# to delete many we can use the .delete_many()
coll.delete_one({'title': 'The Godfather'})


# read the data in the collections
documents = coll.find()

for doc in documents:
    print(doc)