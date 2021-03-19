from models.item import ItemModel
from flask_restful import Resource
from models.item import ItemModel

class Item(Resource):
    def get(self):
        return {'message': 'Item not found'}
