from app.models.Pokemon import Pokemon 
from app.models.Pokemons_Favorites import PokemonsFavorites
from app.models.Users import Users

class ModelFactory:
    @staticmethod
    def get_models(collection_name):
        models = {
            "users": Users,
            "pokemons": Pokemon,
            "Pokemon_Favorites": PokemonsFavorites
        }
        if collection_name in  models:
            return models [collection_name]()
        raise ValueError(f"La coleccion enviada:{collection_name} no existe")