from flask import Flask

# create a Flask object, using a unique name
app = Flask(__name__)

# create a route, (/ for the homepage), and a method which returns something
@app.route("/")
def home():
    return "Hello, world!"

app.run(port=5000)

# USEFUL THEORY:
# An API takes in some data and returns other data, following processing 
# REST API: a web server responds to requests with 'resources'
# a REST API is stateless - one request cannot depend on another

# web server - software designed to accept incoming web requests
# a server sees the verb, the path & the protocol only
# # for example: GET, /login, HTTP/1.1 with host https://twitter.com
# other verbs are POST, DELETE, PUT (check, create, modify), OPTIONS, HEAD