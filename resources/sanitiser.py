from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.sanitiser import SanitiserModel


class Sanitiser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("capacity",
                        type=float,
                        required=True,
                        help="This field is required."
                        )
    parser.add_argument("curr_level",
                        type=float,
                        required=True,
                        help="This field is required."
                        )
    parser.add_argument("status",
                        type=str,
                        default="off",
                        required=False
                        )
    parser.add_argument("num_uses",
                        type=int,
                        default=0,
                        required=False
                        )
    parser.add_argument("led_col",
                        type=int,
                        default=32768,
                        required=False
                        )

    # Returns sanitiser with given id
    def get(self, _id):
        sanitiser = SanitiserModel.find_by_name(_id)
        if sanitiser:
            return sanitiser.json()
        return {"message": "Sanitiser with id '{}' not found.".format(_id)}, 404

    # Registers a new sanitiser
    # @jwt_required() # JWT security token required to call method
    def post(self, _id):
        if SanitiserModel.find_by_name(_id):
            return {'message': "An sanitiser with name '{}' already exists.".format(_id)}, 400

        data = Sanitiser.parser.parse_args()

        sanitiser = SanitiserModel(_id, **data)

        try:
            sanitiser.save_to_db()
        except:
            return {"message": "An error occurred registering the sanitiser."}, 500

        return sanitiser.json(), 201

    # Deletes sanitiser with given id
    # @jwt_required()
    def delete(self, _id):
        sanitiser = SanitiserModel.find_by_name(_id)
        if sanitiser:
            sanitiser.delete_from_db()
            return {"message": "Sanitiser with id '{}' deleted.".format(_id)}

        return {"message": "Sanitiser not found."}

    # Update sanitiser with given id
    # @jwt_required()
    def put(self, _id):
        data = Sanitiser.parser.parse_args()

        sanitiser = SanitiserModel.find_by_name(_id)

        if sanitiser:
            sanitiser.curr_level = data["capacity"]
            sanitiser.curr_level = data["curr_level"]
            sanitiser.status = data["status"]
            sanitiser.num_uses = data["num_uses"]
            sanitiser.led_col = data["led_col"]
        else:
            return {"message": "Sanitiser with id {} does not exist. Use POST to register a new sanitiser.".format(_id)}

        sanitiser.save_to_db()

        return sanitiser.json()


class SanitiserList(Resource):
    # Returns all sanitisers
    def get(self):
        return {"sanitisers": list(map(lambda x: x.json(), SanitiserModel.query.all()))}
