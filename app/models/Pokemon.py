from app import mongo

class Pokemon:
    collection = mongo.db.pokemons

    @staticmethod
    def find_all():
        pokemons = Pokemon.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = Pokemon.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon
    
    @staticmethod
    def create(data):
        pokemon =Pokemon.collection_insertone(data)
        return pokemon.inserted.id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = pokemon .collection.update_one({
            "_id":pokemon_id
        },{
            "$set":data
        })
        return pokemon
    
    @staticmethod
    def delate (pokemon_id):
        return Pokemon.collection.delate_one({"_id":pokemon_id})
    
    
