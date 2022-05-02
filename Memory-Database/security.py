import hmac # safer way of comparing strings
from user import User

# create mapping from users database to avoid iteration each time
# commented out is the dict versions, better to use objects from User class

users = [
    User(1, "bob", "asdf")
]

# users = [
#     {
#         "id": 1,
#         "username": "bob",
#         "password": "asdf"
#     }
# ]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and hmac.compare_digest(user.password, password):
        return user

# payload is the contents of the Flask-JWT token (returned from auth)
def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
