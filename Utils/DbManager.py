from bson import ObjectId
from pymongo.mongo_client import MongoClient


############################################################################
class DbManager:
    """
    Class that manages all the MongoDB Database access

    __init__ : self-explanatory

    PostToDB : Used to "Post"(Add) the given Data under a new randomly generated UserId, and stores the given ID
    in a .txt file in the current directory. UserId.txt is subsequently used to Read and Update the user Data on future use

    ReadFromDbById : Used to get all the currently stored information under the given ID key.

    UpdateDB : Updates the current Data under the given ID key.
    """

    def __init__(self):
        uri = "mongodb+srv://Public:lGaLKy8MX6qEfaUA@facegaming.eyyfifn.mongodb.net/?retryWrites=true&w=majority&appName=FaceGaming"
        client = MongoClient(uri)
        db = client["FaceGamingDB"]
        self.collection = db["Users"]

    def PostToDB(self, Data):
        result = self.collection.insert_one({"KeyMapping": Data})
        file = open("UserId.txt", "w")
        file.write(str(result.inserted_id))
        file.close()

    def ReadFromDbById(self, _id):
        return self.collection.find({"_id": ObjectId(_id)})

    def UpdateDB(self, _id, Data):
        self.collection.update({"_id": ObjectId(_id)}, {"$set": {"KeyMapping": Data}})
############################################################################
