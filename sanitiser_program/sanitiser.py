from sanitiser_network import SanitiserNetwork

class Sanitiser:
	def __init__(self, _id, capacity, curr_level, status="off", num_uses=0, led_col=32768):
		self.id = _id
		self.capacity = capacity
		self.curr_level = curr_level
		self.status = status
		self.num_uses = num_uses
		self.led_col = led_col

	def turnOnOff(self):
		# Turn on/off sanitiser
		if self.status == "off":
			self.status = "on"
		else:
			self.status = "off"

	def useSanitiser(self):
		# Send dispense signal first to avoid delay

		if self.currLevel >= 20: # 20 ml sanitiser
			self.currLevel -= 20
			self.numUses += 1
			changeLedCol(32768) # Green
			return True
		else:
			changeLedCol(16711680) # Red
			return False # Sanitiser empty


	def changeLedCol(self, col):
		if col == 16711680:
			# Display constant red light (empty)
			pass
		if col == 32768:
			# Flash green light (success)
			pass

	def __str__(self):
		return """ID: {} \nCapacity: {} \nRemaining Sanitiser: {} \nStatus: {} \nNumber of Uses: {} \nLED Colour: {}""".format(
			self.id, self.capacity, self.curr_level, self.status, self.num_uses, self.led_col)

def main():
	network = SanitiserNetwork()
	sanitiser = Sanitiser(0, 300, 300, 120)
	network.add(sanitiser)

	sanitiser = Sanitiser(1, 300, 300, 120)
	network.add(sanitiser)

	sanitiser = Sanitiser(2, 300, 280, 90, numUses=1)
	network.add(sanitiser)

	print(network.getNetworkStatus())

if __name__ == "__main__":
	main()
