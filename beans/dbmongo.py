from pymongo import MongoClient

class DbMongo():
    def __init__(self, location, banco, port = 27017):
        self.client = MongoClient(location, port)
        self.db = self.client[banco]
        
    def insert(self,table,value):
        try:
            collection = self.db[table]
            _id = collection.insert_one(value).inserted_id
            return _id
        except Exception as e:
            print(e)
            return None
    
    def insert_list(self, table, listvalues):
        try:
            if(isinstance(listvalues,dict)):
                return self.insert(table,listvalues)
            collection = self.db[table]
            _ids = collection.insert_many(listvalues).inserted_ids
            return _ids
        except Exception as e:
            print(e)
            return None
    
    def select_one(self, table, query):
        try:
            collection = self.db[table]
            values = collection.find_one(query)
            return values
        except Exception as e:
            print(e)
            return None
        
    def select(self, table, query):
        try:
            collection = self.db[table]
            values = [doc for doc in collection.find(query)]
            return values
        except Exception as e:
            print(e)
            return None
    
    def update_one(self, table, id, value):
        try:
            collection = self.db[table]
            _id = collection.replace_one({"_id": id}, value).upserted_id
            return _id
        except Exception as e:
            print(e)
            return None
        