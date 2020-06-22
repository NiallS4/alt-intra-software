from db import db

class SanitiserModel(db.Model):
	__tablename__ = "sanitisers"

	# Database columns
	_id = db.Column(db.Integer, primary_key=True)
	capacity = db.Column(db.Float(precision=2))
	curr_level = db.Column(db.Float(precision=2))
	status = db.Column(db.String())
	num_uses = db.Column(db.Integer())
	led_col = db.Column(db.Integer())

	def __init__(self, _id, capacity, curr_level, status, num_uses, led_col):
		self._id = _id
		self.capacity = capacity
		self.curr_level = curr_level
		self.status = status
		self.num_uses = num_uses
		self.led_col = led_col

	def json(self):
		return {"name": self._id, "price": self.capacity, "current level": self.curr_level,
				"status": self.status, "number of uses": self.num_uses, "led colour": self.led_col}

	@classmethod
	def find_by_name(cls, _id):
		return cls.query.filter_by(_id=_id).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
