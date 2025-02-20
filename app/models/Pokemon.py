from app import mongo
from app.models.super_clase import SuperClass

class Pokemon (SuperClass):
    def __init__(self):
        super().__init__("pokemons")
    
    def create ():
        raise NotImplementedError("Los pokemones no se pueden crear")
    
    def delate (self):
        raise NotImplementedError("Los pokemones no se pueden eliminar")
    
    def update (self, object_id, data):
        raise NotImplementedError("Los pokemnes no se pueden actualizar")