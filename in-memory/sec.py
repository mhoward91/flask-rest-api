# SECURITY
# JWT extension creates a new "/auth" endpoint
# /auth is sent a username & password, which JWT extension sends to authenticate func.
# authenticate function retrieves object & compares password
# it returns a jwt token which calls the identity function 
# which uses the jwt token to get the user ID, and subsequently the correct user 

import hmac # safer way of comparing strings
from basic_user import User

# create mapping from users database to avoid repeated iterations through the users list

users = [
    User(1, "bob", "asdf")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and hmac.compare_digest(user.password, password):
        return user

# payload is the contents of the Flask-JWT token (returned from the authenticate function)
def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
