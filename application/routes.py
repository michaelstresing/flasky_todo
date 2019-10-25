from flask import current_app as app
from flask import render_template

from .models import Todo
from .todo import TodoAPI

app.register_blueprint(TodoAPI, url_prefix='/todo')

# homepage
@app.route('/')
def hello():
    return render_template('hello.html',
                             todos=[td.to_dict() for td in Todo.query.all()]
                            )
