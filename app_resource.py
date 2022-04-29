from flask import Flask, request
from flask_restful import Resource, Api # type: ignore


app = Flask(__name__)
# delete/hide this for production
app.secret_key = "matt"
api = Api(app)

items = [] # type: ignore

# REST APIs work with Resources - data returned from endpoints
# every resource needs to be a class, inheriting from resource

# example (note methods must return a dict but don't require jsonify)
# class Student(Resource):
#     def get(self, name):
#         return {"student": name}

# # @app.route decorator not required 
# api.add_resource(Student, "/student/<string:name>")
# get_json() optional params: force=True will ignore header & parse as json
# silent=True will return None if error 

class Item(Resource):

    def get(self, name):
        item = next(filter(lambda i: i["name"] == name, items), None)
        return {"item": None}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda i: i["name"] == name, items), None) is not None:
            return {"message": "An item with name '{}' already exists"
            .format(name)}, 400
        request_data = request.get_json()
        item = {"name": name, "price": request_data["price"]}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


class ItemList(Resource):

    def get(self):
        return {"item_list": items}


# api.add_resource(items, "/items")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

# debug=True will make errors easier to identify
app.run(port=500, debug=True)
