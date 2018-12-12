from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def home():
	return '<h1>Hello cruel world</h1>'

class Page(db.Model):
	qid = db.Column(db.Integer(), primary_key=True)
	content_type = db.Column(db.String(255))
	content = db.Column(db.Text())
	created = db.Column(db.DateTime())
	updated = db.Column(db.DateTime())
	expires = db.Column(db.DateTime())
	lifetime = db.Column(db.Time())
	owner = db.Column(db.Integer())

	def __init__(self, content):
		self.content = content

	def __repr__(self):
		return "<qid {}> {}".format(self.qid, self.content)

if __name__=='__main__':
	app.run()
