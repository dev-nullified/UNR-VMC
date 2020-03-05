from flask import render_template, redirect, request, jsonify, Response
from .models.person import Person, PersonSchema
# from app.models.report import Report
from . import db
from app.utils.report import ReportRunner
from flask import current_app as app


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


@app.route('/person', methods=['GET'])
def students():
    return render_template("persons.html")


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
    return render_template("reports.html")


@app.route('/create', methods=['PUT', 'GET'])
def create():
    pass
    #try:
        #db.session.commit()
        #return redirect('/reports')
    #except:
        #return 'There was a problem creating this report'


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
        # try:
            # db.session.commit()
            # return redirect('/reports')
        # except:
            # return 'There was a problem creating this report'
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

@app.route('/api/reports')
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

@app.route('/api/Person')
def getPerson():
    pass

@app.route('/test/reportbuilder')
def getReportWizard():
    return render_template("reportWizard2.html")

@app.route('/test/reportOutput')
def getReportTest():

    queryResult = ReportRunner()
    result = queryResult.run_report(["id","nshe","firstName"], None, None)
        
    return jsonify(result)

@app.route('/test/reportbuilder2')
def getReportBuilderTest():
    return render_template("reportWizard3.html")


@app.route('/test/fieldmetadata')
def getFieldMetadata():
    report = ReportRunner()
    fields = report.get_query_filter_for_web(model=Person)
    return fields




@app.route('/test/studen/')
def getMockStudents():
    fakeData = {
        'f_name': "johnny",
        'l_name': "adam"
    }

    return jsonify(fakeData)



# API ROUTES FOR REPORTS


# Submit rules to run
@app.route('/api/report/rules', methods=['POST'])
def reportRules():

    request_data = request.get_json()
    # request_data = request.form

    print(request_data)

    report = ReportRunner()

    report.run_report(request_data)

    # print("\n\n RULES BUILT: ")
    # print(rules_built)

    request_validation = True

    if request_validation:

        return Response(status=201)




# Get all avalible filters for building a report
@app.route('/api/report/filters', methods=['GET'])
def reportFilters():
    report = ReportRunner()
    filters = report.get_query_filter_for_web(model=Person)

    return jsonify(filters)