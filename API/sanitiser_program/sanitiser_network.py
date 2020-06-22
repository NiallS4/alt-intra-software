import requests
import json

class SanitiserNetwork:
	def __init__(self, numSanitisers=0, sanitisers=[]):
		self.numSanitisers = numSanitisers
		self.sanitisers = sanitisers

	def add(self, sanitiser):
		self.sanitisers.append(sanitiser)
		self.numSanitisers += 1

	def getNetworkStatus(self):
		for sanitiser in self.sanitisers:
			print(sanitiser)
			print()

		return "Number of Sanitiser: {}".format(self.numSanitisers)


url = "http://127.0.0.1:5000/"

# User Registration Request Methods

# POST /register
def register_user(username, password):
	headers = {
		"Content-Type": "application/json"
	}

	data = {
		"username": username,
		"password": password
	}

	response = requests.request("POST", url + "register", data=json.dumps(data))
	return response.text

# POST /auth
def get_jwt_token(username, password):
	headers = {
		"Content-Type": "application/json"
	}

	data = {
		"username": username,
		"password": password
	}

	response = requests.request("POST", url + "auth", data=json.dumps(data), headers=headers)
	print(response.text)

	return json.loads(response.text)["access_token"]


# Sanitiser Request Methods

# GET /sanitisers
def get_sanitisers():
	response = requests.request("GET", url + "sanitisers")
	return response.text

# POST /sanitiser/<string:_id>
def register_sanitiser(_id, JWT_TOKEN):
	headers = {
		"Content-Type": "application/json",
		"Authorization": "jwt " + JWT_TOKEN
	}

	data = {
		"capacity": 270.0,
		"curr_level": 250.00
	}

	response = requests.request("POST", url + "sanitiser/" + str(_id), data=json.dumps(data), headers=headers)
	return response.text

# PUT /sanitiser/<string:_id>
def update_sanitiser(_id, data, JWT_TOKEN):
	headers = {
		"Content-Type": "application/json",
		"Authorization": "jwt " + JWT_TOKEN
	}

	response = requests.request("PUT", url + "sanitiser/" + str(_id), data=json.dumps(data), headers=headers)
	return response.text

# DELETE /sanitiser/<string:_id>
def delete_sanitiser(_id, JWT_TOKEN):
	headers = {
	"Authorization": "jwt " + JWT_TOKEN
	}

	response = requests.request("DELETE", url + "sanitiser/" + str(_id), headers=headers)
	return response.text

def main():
	# Sample user registration
	print(register_user("admin", "test"))
	jwt = get_jwt_token("niall", "abc")

	print(get_sanitisers())
	print(update_sanitiser(2, data = {
		"capacity": 300.0,
		"curr_level": 10.0,
		"status": "off",
		"num_uses": 100,
		"led_col": 32768
		}, JWT_TOKEN=jwt)
	)
	delete_sanitiser(1, jwt)
	print(get_sanitisers())

if __name__ == "__main__":
	main()
