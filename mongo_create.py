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

# Create in CRUD
new_doc = {
    "title": "The Godfather",
    "year": 1972,
    "actors": [
        "Al Pacino",
        "Marlon Brando"
    ],
    "synopsis": "Widely regarded as one of the greatest films of all time, this mob drama, based on Mario Puzo's novel of the same name, focuses on the powerful Italian-American crime family of Don Vito Corleone (Marlon Brando). When the don's youngest son, Michael (Al Pacino), reluctantly joins the Mafia, he becomes involved in the inevitable cycle of violence and betrayal. Although Michael tries to maintain a normal relationship with his wife, Kay (Diane Keaton), he is drawn deeper into the family business.",
    "genre": "Drama",
    "rating": 97
}


# grab the collection and use the insert_one method, passing in the new_doc
coll.insert_one(new_doc)

# read the data in the collections
documents = coll.find()

for doc in documents:
    print(doc)