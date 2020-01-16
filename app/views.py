from flask import render_template, redirect, request, jsonify
from app.models.person import Person
from app.models.report import Report
from app import app, db


@app.route('/')
def index():
    # if True:
    # return redirect('/login')
    # else:
    return render_template("home.html")


@app.route('/login', methods=['GET'])
def login():
    pass


@app.route('/logout')
def logout():
    # unathenticate
    return redirect('/')


@app.route('/students', methods=['GET'])
def students():
    people = Person.query.order_by(Person.id).all()
    return render_template("")


@app.route('/student/<int:id>', methods=['GET'])
def student(id):
    person_to_display = Person.query.get_or_404(id)
    return render_template("")


@app.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_person(id):
    person_to_delete=Person.query.get_or_404(id)
    try:
        db.session.delete(person_to_delete)
        db.session.commit()
        return redirect('/students')
    except:
        return 'There was a problem with deleting this Person.'

@app.route('/reports', methods=['GET'])
def report():
    all_reports = Report.query.order_by(Report.lastUsed).all
    return render_template("reports.html")


@app.route('/create', methods=['PUT', 'GET'])
def create():
    pass


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    report_view = Report.query.get_or_404(id)
    return render_template("")


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    report_to_delete = Report.query.get_or_404(id)
    try:
        db.session.delete(report_to_delete)
        db.session.commit()
        return redirect('/reports')
    except:
        return 'There was a problem with deleting this Report.'


@app.route('/import', methods=['PUT', 'GET'])
def upload():
    if request.method=='PUT':
        pass
    else:
        return redirect('/')


@app.route('/nofications')
def nofications():
    pass


@app.route('/stats', methods=['GET'])
def stats():
    pass


@app.route('/about')
def about():
    return render_template("about.html")


# Brandon F Temporart
import datetime

@app.route('/api/listreports')
def getReports():

    tempdict = {
        'NumberOfReports': '3',
        'Reports': [
            {
                'Name': "Test Report one",
                'Description': "This is test report one",
                'LastRun': datetime.datetime.utcnow()
            },
            {
                'Name': "Test Report Two",
                'Description': "This is test report two",
                'LastRun': datetime.datetime.utcnow()
            },
            {
                'Name': "Test Report three",
                'Description': None,
                'LastRun': datetime.datetime.utcnow()
            },
        ]
    }

    return jsonify(tempdict)

