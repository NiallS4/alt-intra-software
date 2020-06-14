from flask import Flask, reqeust
from flask_cors import CORS, cross_origin

@application.route('/api/register_dispenser', methods=['POST'])
def registerDispenser():
    data = request.get_json()
