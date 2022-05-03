from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# note you would normally store this info in a database (not a dict in mem)
stores = [
    {
       "name": "My Wonderful Store",
       "items": [
           {
               "name": "My Item",
               "price": 15.99
           }
       ]

    }
]

# render HTML code from flask application (illustrative only)
# you would only do this for flask web apps, not for flask APIs
@app.route("/")
def home():
    return render_template("index.html") # flask auto looks in templates folder


# flask notation to illustrate the available verbs in a list (GET, POST etc)
# default is a GET request
# methods will always need to return jsonify(dict)
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()   # request holds an active request's data
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)   # use jsonify as always need to return a STR

# flask notation of <string:name> to pass parameter name to the method
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "That store doesn't exist"})    

@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})

# to test these post requests in Postman:
# add {Content-Type: application/json} to Params
# in the Body, select raw, and add a dict of variables required
@app.route("/store/<string:name>/item", methods=["POST"])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "That store doesn't exist"}) 
    
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "That store doesn't exist"})    


app.run(port=5000)