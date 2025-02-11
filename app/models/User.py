from app import mongo

class Users:
    collection = mongo.db.users

    @staticmethod
    def find_all():
        user = Users.collection.find()
        return list(user)
    
    @staticmethod
    def find_by_id(user_id):
        user = Users.collection.find_one({
            "_id": user_id
        })
        return user
    
    @staticmethod
    def create(data):
        user = Users.collection_insertone(data)
        return user.inserted.id
    
    @staticmethod
    def update(user_id, data):
        user = Users.collection.update_one({
            "_id":user_id
        },{
            "$set":data
        })
        return user
    
    @staticmethod
    def delate (user_id):
        return Users.collection.delate_one({"_id":user_id})
    
    