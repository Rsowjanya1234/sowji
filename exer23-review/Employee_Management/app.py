from flask import Flask, request, jsonify
from db_code import create_employee, get_employees, get_employee, update_employee, delete_employee

app = Flask(__name__)

# Create an employee
@app.route('/api/employees', methods=['POST'])
def create_employee_route():
    return create_employee(request)

# Read all employees
@app.route('/api/employees', methods=['GET'])
def get_employees_route():
    return get_employees()

# Read an employee by ID
@app.route('/api/employees/<int:id>', methods=['GET'])
def get_employee_route(id):
    return get_employee(id)

# Update an employee by ID
@app.route('/api/employees/<int:id>', methods=['PUT'])
def update_employee_route(id):
    return update_employee(id, request)

# Delete an employee by ID
@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee_route(id):
    return delete_employee(id)

if __name__ == '__main__':
    app.run(debug=True)
