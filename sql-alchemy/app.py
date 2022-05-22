from flask import Flask # type: ignore
from flask_restful import Api   # type: ignore
from flask_jwt import JWT   # type: ignore

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = "matt"  # hide in a production environment
api = Api(app)

jwt = JWT(app, authenticate, identity)  

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

# set debug=True to make errors easier to identify
if __name__ == "__main__":
    app.run(port=500, debug=True)
