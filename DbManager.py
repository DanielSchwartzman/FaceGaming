from bson import ObjectId
from pymongo.mongo_client import MongoClient


class DbManager:
    def __init__(self):
        uri = "mongodb+srv://Public:lGaLKy8MX6qEfaUA@facegaming.eyyfifn.mongodb.net/?retryWrites=true&w=majority&appName=FaceGaming"
        client = MongoClient(uri)
        db = client["FaceGamingDB"]
        self.collection = db["Users"]

    def PostToDB(self, Data):
        result = self.collection.insert_one(Data)
        file = open("UserId.txt", "w")
        file.write(str(result.inserted_id))
        file.close()

    def ReadFromDbById(self, _id):
        return self.collection.find({"_id": ObjectId(_id)})

    def UpdateDB(self, _id, Data):
        self.collection.update({"_id": ObjectId(_id)}, {"$set": {"KeyMapping": Data}})
