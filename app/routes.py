from flask import current_app as app
from flask import render_template


# homepage
@app.route('/')
def hello():
    return render_template('hello.html')
