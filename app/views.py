from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

@app.route('/')
@app.route('/index')
def index():
	tsklst = models.User.query.order_by('id asc').all()
	return render_template('index.html',title='Things To-do',tsklst=tsklst)

@app.route('/_add')
def add_():
	toDo = request.args.get('task')
	toDo = str(toDo)
	toDo = toDo[0].upper() + toDo[1:]
	toDe = request.args.get('desc')
	toDe = str(toDe)
	toDe = toDe[0].upper() + toDe[1:]	
	test = models.User(task = str(toDo), description = str(toDe))
	db.session.add(test)
	db.session.flush()
	db.session.refresh(test)
	db.session.commit()
	content = "<div class='disp' id= " + str(test.id) + "><input type='button' class='dele' id= " + str(test.id) + " /><div class='data' id='"+str(test.id)+"'><div class='left' id='"+str(test.id)+"'><h2 id='"+str(test.id)+"' class='h2'>"+ test.task +"</h2><input type='text' class='txtTask' id='"+str(test.id)+"' value='"+ test.task +"' hidden/></div><div class='right' id='"+str(test.id)+"'><p class='p' id='"+str(test.id)+"'>"+ test.description +"</p><textarea class='txtDesc' id='"+str(test.id)+"' hidden>"+ test.description +"</textarea></div></div><input type='button' class='edit' id= " + str(test.id) + " /><input type='button' class='save' id='"+str(test.id)+"' hidden/></div>"
	return content
# return u.id

@app.route('/_delete')
def delete_():
	toDo = request.args.get('id')
	u = models.User.query.get(toDo)
	db.session.delete(u)
	db.session.commit()
	return render_template('index.html')

@app.route('/_edit')
def edit_():
	toDo = request.args.get('id')
	toDo1= request.args.get('task')
	toDo2= request.args.get('desc')
	u    = models.User.query.get(toDo)
	u.task=toDo1
	u.description=toDo2
	db.session.flush()
	db.session.refresh(u)
	db.session.commit()
	return None



