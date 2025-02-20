from app import mongo

class Pokemon:
    def __init__(self, collection):
        self.collection = mongo.db.pokemons[collection]

    


    def find_all(self):
        data = Pokemon.collection.find()
        return list(data)
    
   
    def find_by_id(self, object_id):
        datum = Pokemon.collection.find_one({
            "_id": object_id
        })
        return datum
    

    def create(self, data):
        datum =self.collection_insertone(data)
        return str(datum.inserted_id)

    def update(self,object_id, data):
        datum = self.collection.update_one({
            "_id":object_id
        },{
            "$set":data
        })
        return datum
    

    def delate (self,object_id):
        return self.collection.delate_one({"_id":object_id})
    
    
