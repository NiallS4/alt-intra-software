from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

sanitisers = []

class Sanitiser(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("capacity",
		type=float,
		required=True,
		help="This field cannot be left blank"
		)
	parser.add_argument("currLevel",
		type=float,
		required=False
		)
	parser.add_argument("numUses",
		type=int,
		required=False
		)

	# Returns sanitiser with given id
	def get(self, _id):
		sanitiser = next(filter(lambda x: x["id"] == _id, sanitisers), None)
		return {"sanitiser": sanitiser}, 200 if sanitiser else 404

	# Creates a new sanitiser
	def post(self, _id):
		# Checks if sanitiser with given id already exists
		if next(filter(lambda x: x["id"] == _id, sanitisers), None) is not None:
			return {"message": "An item with id '{}' already exists".format(_id)}, 400

		data = Sanitiser.parser.parse_args()

		sanitiser = {"id": _id,
			"capacity": data["capacity"],
			# Current level is defaulted to the capacity unless explicitly specified otherwise
			"currLevel": data["currLevel"] if data["currLevel"] else data["capacity"],
			"numUses": 0
		}
		sanitisers.append(sanitiser)
		return sanitiser, 201

	# Deletes sanitiser with given id
	def delete(self, _id):
		global sanitisers
		sanitisers = list(filter(lambda x: x["id"] != _id, sanitisers))
		return {"message": "Sanitiser with id '{}' deleted".format(_id)}

	# Updates sanitiser data for given sanitiser id
	def put(self, _id):
		data = Sanitiser.parser.parse_args()
		sanitiser = next(filter(lambda x: x["id"] == _id, sanitisers), None)
		if sanitiser is None:
			sanitiser = {"id": _id,
				"capacity": data["capacity"],
				"currLevel": data["currLevel"],
				"numUses": data["numUses"]
			}
			sanitisers.append(sanitiser)
		else:
			sanitiser.update(data)
		return sanitiser


class SanitiserList(Resource):
	# Returns a list of all sanitisers
	def get(self):
		return {"sanitisers": sanitisers}


api.add_resource(Sanitiser, "/sanitiser/<int:_id>")
api.add_resource(SanitiserList, "/sanitisers")

app.run(port=5000, debug=True)

