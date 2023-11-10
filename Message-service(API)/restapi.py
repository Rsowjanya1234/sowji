from flask import Flask, request, jsonify,render_template
 
import requests
 
import json
 
from flask_cors import CORS

app=Flask(__name__)
 
@app.route('/')
 
def home():
 
	return render_template('user_input.html')
 
# Load the configuration from a JSON file
 
with open("config.json", "r") as config_file:
 
    config = json.load(config_file)
 
    messages_api_url = config.get("messages_api_url")
 
# Route to fetch all messages from the messages management application
 
@app.route('/messages', methods=['GET'])
 
def fetch_messages():
 
    response = requests.get(f"{messages_api_url}/get_messages")
 
    if response.status_code == 200:
 
        messages = response.json()
 
        return jsonify(messages)
 
    else:
 
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500
 
# Route to fetch a single message by ID from the messages management application
 
@app.route('/messages/<int:message_id>', methods=['GET'])
 
def fetch_message(message_id):
 
    response = requests.get(f"{messages_api_url}/messages/{message_id}")
 
    if response.status_code == 200:
 
        message = response.json()
 
        return jsonify(message)
 
    else:
 
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500
 
# Route to create a new message in the messages management application
 
@app.route('/messages', methods=['POST'])
 
def create_message():
 
    data = request.json
 
    response = requests.post(f"{messages_api_url}/create_message", json=data)
 
    if response.status_code == 201:
 
        return jsonify({"message": "Message created successfully"})
 
    else:
 
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500
 
# Route to update a message by ID in the messages management application
 
@app.route('/messages/<int:message_id>', methods=['PUT'])
 
def update_message(message_id):
 
    data = request.json
 
    response = requests.put(f"{messages_api_url}/update_messages/{message_id}", json=data)
 
    if response.status_code == 200:
 
        return jsonify({"message": "Message updated successfully"})
 
    else:
 
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500
 
# Route to delete a message by ID in the messages management application
 
@app.route('/messages/<int:message_id>', methods=['DELETE'])
 
def delete_message(message_id):
 
    response = requests.delete(f"{messages_api_url}/delete_messages/{message_id}")
 
    if response.status_code == 200:
 
        return jsonify({"message": "Message deleted successfully"})
 
    else:
 
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500
 
if __name__ == '__main__':
 
    CORS(app)
 
    app.run(debug=True)
