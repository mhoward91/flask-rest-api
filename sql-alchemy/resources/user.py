import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse    # type: ignore

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument(
    "username",
    type=str,
    required=True,
    help="A username is required."
    )
    parser.add_argument(
    "password",
    type=str,
    required=True,
    help="A password is required."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "That user has already been created"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

        