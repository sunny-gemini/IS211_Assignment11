from crypt import methods
from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db
from flask import request
import pandas as pd


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route('/add', methods=[ 'GET', 'POST'])
def add():
    if request.form:
        text = text=request.form['todoitem']
        email = email=request.form['email']
        priority = priority=request.form['priority']
        data = Todo(text , email , priority)
        db.session.add(data)
        db.session.commit()
        print(request.form)
        message = "ITEM ADDEDD TO YOUR ITEM LIST"
    return render_template("index.html", message=message)





@app.route('/view_list', methods=['POST'])
def view_list():
    data = Todo.query.order_by(Todo.id)
    print(data)
    return render_template('view_list.html', items=data )
 

@app.route('/delete/<int:id>')
def delete(id):
    delete_item = Todo.query.get_or_404(id)
    db.session.delete(delete_item)
    db.session.commit()
    data = Todo.query.order_by(Todo.id)
    m = 'ITEM DELETED FROM YOUR LIST'

    return render_template("view_list.html",message =m ,items=data)
