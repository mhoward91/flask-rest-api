# REST APIs work with Resources - data returned from endpoints
# every resource needs to be a class, inheriting from resource
# every method in a resource must use the same params (defined when res. added)
# methods must return a dict but don't require jsonify
# get_json() retrieves request request body (json payload) as a python dict for use
# optional params: force=True will ignore header & parse as json
# silent=True will return None if error 
# # @app.route decorator not required with flask_restful

# JWT extension creates a new "/auth" endpoint
# /auth is sent a username & password, which JWT extension sends to authenticate func.
# authenticate function retrieves object & compares password
# it returns a jwt token which calls the identity function 
# which uses the jwt token to get the user ID, and subsequently the correct user 

from flask import Flask, request
from flask_restful import Resource, Api, reqparse # type: ignore
from flask_jwt import JWT, jwt_required # type: ignore

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "matt" # delete/hide this for production
api = Api(app)

jwt = JWT(app, authenticate, identity)  

items = [] # type: ignore


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
        )

    @jwt_required()   # this means authentication required prior to use of method
    def get(self, name):
        item = next(filter(lambda i: i["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda i: i["name"] == name, items), None):
            return {"message": "An item with name '{}' already exists"
            .format(name)}, 400
        request_data = request.get_json()
        item = {"name": name, "price": request_data["price"]}
        items.append(item)
        return item, 201

    def put(self, name):
        # parses valid json payload args, placing valid ones in request_data  
        request_data = Item.parser.parse_args()

        item = next(filter(lambda x: x["name"] == name, items), None)
        if not item:
            item = {"name": name, "price": request_data["price"]}
            items.append(item)
        else:
            item.update(request_data)
        return item, 200

    # overriding list with new list containing all elements apart from name
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}


class ItemList(Resource):

    def get(self):
        return {"item_list": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

# debug=True will make errors easier to identify
app.run(port=500, debug=True)
