from app import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200),nullable=False)
	priority = db.Column(db.String(200),nullable=False)
	email = db.Column(db.String(200),nullable=False)

	def __init__(self, text, priority ,email):
		self.text = text
		self.priority = priority
		self.email = email
	


	def __repr__(self):
		return '<Name %r>' % self.id

db.create_all()
db.session.commit()
