from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

mongo_uri = os.getenv("MONGO_URI")
print("MONGO_URI:", mongo_uri)
client = MongoClient(mongo_uri)

db = client["student_db"]
collection = db["students"]

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # ✅ Handle both JSON and form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        print("Received Data:", data)  # ✅ Debug

        # Optional validation
        if not data:
            return jsonify({"error": "No data received"}), 400

        collection.insert_one(data)

        return jsonify({"message": "Data submitted successfully"}), 200

    except Exception as e:
        print("ERROR:", str(e))  # ✅ Debug
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)