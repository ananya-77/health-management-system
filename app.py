# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["health_monitoring"]

@app.route('/patients', methods=['GET'])
def get_patients():
    # Fetch patient data from MongoDB
    patients = list(db.hospital_data.find({}, {"_id": 0}))  # Exclude MongoDB _id for cleaner response
    return jsonify(patients)

@app.route('/treatments', methods=['GET'])
def get_treatments():
    # Fetch treatment data from MongoDB
    treatments = list(db.treatment_data.find({}, {"_id": 0}))  # Exclude MongoDB _id for cleaner response
    return jsonify(treatments)

if __name__ == "__main__":
    app.run(debug=True)
