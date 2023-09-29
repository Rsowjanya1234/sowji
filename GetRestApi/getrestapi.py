from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from the config.json file
with open('config.json', 'r') as json_file:
    config_data = json.load(json_file)

@app.route('/api/resource', methods=['GET'])  # It should be "methods" instead of "method"
def get_data():
    return jsonify(config_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
