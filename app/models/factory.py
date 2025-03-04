from app.models.Pokemon import Pokemon
from app.models.Pokemons_Favorites import PokemonFavorites
from app.models.Users import User

class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": User,
            "pokemons": Pokemon,
            "pokemons_favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"La coleccion enviada: {collection_name} no existe")