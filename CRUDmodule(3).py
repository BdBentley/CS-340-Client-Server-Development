from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='password'):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:30814/AAC' % (username, password))
        # Where xxxxx is your unique port number
        self.database = self.client['AAC']
        print("Connected Properly")

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("Entry has been created")
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query,{"_id": False})
            print("Cursor has been returned")
            return cursor
        else:
            raise Exception("No results found")

    # Create a method to implement the U in CRUD
    def update(self, query, data):
        if query is not None:
            result = self.database.animals.update_many(query, data)
            return dumps(self.read(data))
        else:
            raise Exception("No results to update")

    # Create a method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query)
            return dumps(self.read(query))
        else:
            raise Exception("No file to delete")
