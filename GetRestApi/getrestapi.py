from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource():
    data = {
        'id': 1,
        'name': 'Sample Resource',
        'description': 'This is a sample resource for demonstration purposes.'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
