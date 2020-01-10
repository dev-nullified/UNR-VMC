from flask import render_template, redirect
from app import app


@app.route('/')
def index():
    if True:
        return redirect('/login')
    else:
        return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
    pass

@app.route('/logout')
def logout():
    # unathenticate
    return redirect('/')

@app.route('/students', methods=['GET'])
def students():
    pass

@app.route('/student/<int: id>', methods=['GET'])
def student(id):
    pass

@app.route('/report', methods=['GET'])
def report():
    pass

@app.route('/create', methods=['PUT', 'GET'])
def create():
    pass

@app.route('/view/<int: id>', methods=['GET'])
def view(id):
    pass

@app.route('/delete/<int: id>', methods=['DELETE'])
def delete(id):
    pass

@app.route('/import', methods=['PUT', 'GET'])
def upload():
    pass

@app.route('/nofications')
def nofications():
    pass

@app.route('/stats', methods=['GET'])
def stats():
    pass

@app.route('/about')
def about():
    return render_template("about.html")
