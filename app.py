import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.sanitiser import Sanitiser, SanitiserList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "my_key"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Sanitiser, "/sanitiser/<string:_id>")
api.add_resource(SanitiserList, "/sanitisers")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
	app.run(port=5000, debug=True)

