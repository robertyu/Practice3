from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), index=True, unique=False)
    description = db.Column(db.String(100), index=True, unique=False)

    def __repr__(self):
    	return '<User %r>' % (self.task)