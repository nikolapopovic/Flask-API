import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


employees = [
    {
        'id': 0,
        'first_name': 'Nikola',
        'last_name': 'Popovic',
        'address': 'Beogradska 22'
    },
    {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'address': 'Francuska 1'
    }
]

departments = [
    {
        'id': 0,
        'department': 'Frontend Development',
        'position': 'Junior Frontend Developer'
    },
    {
        'id': 1,
        'department': 'Backend Development',
        'position': 'Junior Backend Developer'
    }
]

@app.route('/employees', methods=['GET'])
def api_name():
    results = employees

    if 'name' in request.args:
        name = str(request.args['name'])    
        results = []
        for employee in employees:
            if employee['name'] == name:
                results.append(employee)
            
    return jsonify(results)

@app.route('/departments', methods=['GET'])
def api_department():
    results = departments
    
    if 'department' in request.args:
        department = str(request.args['department'])
        results = []
        for sector in departments:
            if sector['department'] == department:
                results.append(sector)    
            
    return jsonify(results)

@app.route('/employees', methods=['POST'])
def addEmployee():

    newEmployee = {
        'id' : request.json['id'],
        'first_name' : request.json['first_name'],
        'last_name' : request.json['last_name'],
        'address' : request.json['address']
    }

    employees.append(newEmployee)
    return jsonify({'employees' : employees})

@app.route('/departments', methods=['POST'])
def addDepartment():
    newDepartment = {
        'id' : request.json['id'],
        'department' : request.json['department'],
        'position' : request.json['position']
    }
    departments.append(newDepartment)
    return jsonify({'departments' : departments})

app.run()