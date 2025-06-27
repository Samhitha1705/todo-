from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from . import db

main = Blueprint('main', __name__)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))


@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/delete/<int:task_id>')
def delete(task_id):
    todo = Todo.query.get_or_404(task_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/api/todos', methods=['GET'])
def api_get_todos():
    todos = Todo.query.all()
    return jsonify({'todos': [t.task for t in todos]})
