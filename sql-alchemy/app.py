from flask import Flask # type: ignore
from flask_restful import Api   # type: ignore
from flask_jwt import JWT   # type: ignore

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

# turns off Flask SQLAlchemy mod tracker, SQLAlchemy mod tracker still on (better)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.secret_key = "matt"  # hide in a production environment
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() # creates data.db (line 14) & all tables if not present

jwt = JWT(app, authenticate, identity)  

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")

# set debug=True to make errors easier to identify
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=500, debug=True)
