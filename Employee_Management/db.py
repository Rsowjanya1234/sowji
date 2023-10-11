import sqlite3


# Create a SQLite database and table
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, role TEXT)''')
conn.commit()
conn.close()

def create_employee(request):
    try:
        data = request.get_json()
        name = data['name']
        role = data['role']

        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, role) VALUES (?, ?)", (name, role))
        conn.commit()
        conn.close()
        return jsonify({"message": "Employee created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_employees():
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        conn.close()
        employee_list = [{"id": emp[0], "name": emp[1], "role": emp[2]} for emp in employees]
        return jsonify(employee_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_employee(id):
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
        employee = cursor.fetchone()
        conn.close()
        if employee:
            return jsonify({"id": employee[0], "name": employee[1], "role": employee[2]})
        else:
            return jsonify({"message": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_employee(id, request):
    try:
        data = request.get_json()
        name = data['name']
        role = data['role']

        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET name=?, role=? WHERE id=?", (name, role, id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Employee updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def delete_employee(id):
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Employee deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
