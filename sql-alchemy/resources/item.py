from models.item_model import ItemModel
from flask_restful import Resource, reqparse # type: ignore
from flask_jwt import jwt_required # type: ignore
from flask import request

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
        )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every item needs a store id."
        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exists".format(name)}, 400
        
        request_data = request.get_json()
        
        item = ItemModel(name, request_data["price"], request_data["store_id"])
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item"}, 500
        
        return item.json(), 201

    def put(self, name):
        # parses valid json payload args, placing valid ones in request_data  
        request_data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if not item:
            item = ItemModel(name, request_data["price"], request_data["store_id"])
        else:
            item.price = request_data["price"]
            item.store_id = request_data["store_id"]
        
        item.save_to_db()
        
        return item.json()
            
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {"message": "Item deleted"}

class ItemList(Resource):

    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}