from flask import Blueprint, jsonify, request

from . import db
from .models import Todo

TodoAPI = Blueprint('todo_api', __name__)


@TodoAPI.route('/create', methods=['POST'])
def create_todo():

    try:
        todo = Todo.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(todo)
    db.session.commit()
    return jsonify(), 200


@TodoAPI.route('/<name>')
def get_todo(taskname):
    todo = Todo.query.filter(Todo.taskname == taskname).first()
    if todo is None:
        return 'Todo not found', 404
    return jsonify(todo.to_dict()), 200