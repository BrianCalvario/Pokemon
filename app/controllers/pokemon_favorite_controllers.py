from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.schemas.Pokemon_Favorites_Schema import PokemonFavoritoSchema 
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import ModelFactory

bp = Blueprint("favorite_pokemon",__name__, url_prefix="/favorite-pokemons")
RM = ResponseManager
FP_MODEL = ModelFactory.get_models("po0kemon_favorites")
FP_SCHEMA = PokemonFavoritoSchema()

@bp.route("/", method=["POST"])
def create():
    try:
        data =request.json
        data= FP_SCHEMA.validate(data)
        fp= FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print (err)
        return RM.error("Es necesario enviar todos los parametros")

@bp.route("/<string:user_id>",methods=["DELETE"])
def delete (id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route("/<string:user_id>",methods=["GET"])
def get_all(user_id):
    data =FP_MODEL.find_all(user_id)
    return RM.success(data)