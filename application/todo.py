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

@TodoAPI.route('/<int:id>')
def get_todo(id):

    todo = Todo.query.filter(Todo.id == id).first()
    if todo is None:
        return 'Todo not found', 404
    return jsonify(todo.to_dict()), 200

@TodoAPI.route('/<string:taskname>')
def get_todo_name(taskname):
    todo = Todo.query.filter(Todo.taskname == taskname).all()
    jsontodo = [td.to_dict() for td in todo]
    return jsonify(jsontodo), 200

@TodoAPI.route('/', methods=['GET'])
def get_all():
    todo = Todo.query.all()
    jsontodo = [td.to_dict() for td in todo]
    return jsonify(jsontodo), 200

@TodoAPI.route('<int:id>', methods=['PUT'])
def edit_todo(id):

    Todo.query.filter(Todo.id == id).update(request.json)
    todo = Todo.query.filter(Todo.id == id).first_or_404()
    db.session.commit()
    return jsonify(todo.to_dict()), 200

    # taskname = request.json['taskname']
    # difficulty = request.json['taskdifficulty']
    # duedate = request.json['duedate']

    # task = Todo.query.get(id)

    # try:
    #     newtask = Todo.from_dict(request.json)
    # except KeyError as e:
    #     return jsonify(f'Missing key: {e.args[0]}'), 400

    # if task is None:
    #     db.session.add(newtask)
    #     db.session.commit()
    #     return jsonify(), 200

    # else:
    #     task.taskname = taskname
    #     task.difficulty = difficulty
    #     task.duedate = duedate
    #     db.session.commit()
    #     return jsonify(), 200

@TodoAPI.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):

    todo = Todo.query.filter(Todo.id == id).first()
    if todo is None:
        return 'Todo not found', 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify(), 200
