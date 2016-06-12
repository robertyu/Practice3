from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
    	return '<User %r>' % (self.task)