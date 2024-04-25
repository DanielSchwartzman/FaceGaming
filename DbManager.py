from pymongo.mongo_client import MongoClient


class DbManager:
    def __init__(self):
        uri = "mongodb+srv://DanielSchwart:<Password>@facegaming.eyyfifn.mongodb.net/?retryWrites=true&w=majority&appName=FaceGaming"
        client = MongoClient(uri)
        db = client["FaceGamingDB"]
        self.collection = db["Users"]

    def PostToDB(self, Data):
        self.collection.insert_one(Data)

    def ReadFromDbById(self, _id):
        return self.collection.find({"_id": _id})

    def UpdateDB(self, _id, Data):
        self.collection.update({"_id": _id}, {"$set": {"KeyMapping": Data}})
