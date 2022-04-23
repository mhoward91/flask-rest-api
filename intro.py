from flask import Flask

# create an object of Flask, using a unique name
app = Flask(__name__)

# create an route, for the homepage
@app.route("/")
# create a method which returns something, method name not relevant
def home():
    return "Hello, world!"

app.run(port=5000)

# THEORY
# An API is a program that takes in some data and gives back some other 
# data, usually after processing it.
# REST API: how a web server responds to requests with resources
# REST is stateless - one request cannot depend on another

# web server - a piece of software designed to accept incoming web requests
# a server sees the verb, the path & the protocol only
# # for example: GET /login HTTP/1.1 with host https://twitter.com
# other verbs are POST, DELETE, PUT (make sure is there), OPTIONS, HEAD