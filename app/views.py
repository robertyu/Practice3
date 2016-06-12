from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

@app.route('/')
@app.route('/index')
def index():
	tsklst = models.User.query.order_by('id asc').all()
	return render_template('index.html',title='TEST',tsklst=tsklst)

@app.route('/_add')
def add_():
	toDo = request.args.get('task')
	test = models.User(task = str(toDo))
	db.session.add(test)
	db.session.flush()
	db.session.refresh(test)
	db.session.commit()
	content = "<div class='disp' id= " + str(test.id) + "><div class='left'>"+test.task+"</div><input type='checkbox' class='chkbk' id= " + str(test.id) + "></div>"
	return content
# return u.id

@app.route('/_delete')
def delete_():
	toDo = request.args.get('id')
	u = models.User.query.get(toDo)
	db.session.delete(u)
	db.session.commit()
	return render_template('index.html')