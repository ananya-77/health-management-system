# backend/load_data.py

import pandas as pd
import pymongo

# Load Kaggle datasets
treatment_df = pd.read_csv('data/patient_treatment.csv')
hospital_df = pd.read_csv('data/hospital_records.csv')

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["health_monitoring"]

# Define collections
treatment_collection = db["treatment_data"]
hospital_collection = db["hospital_data"]

# Clear existing data to avoid duplicates
treatment_collection.delete_many({})
hospital_collection.delete_many({})

# Load data into MongoDB
treatment_collection.insert_many(treatment_df.to_dict(orient="records"))
hospital_collection.insert_many(hospital_df.to_dict(orient="records"))

print("Data loaded successfully into MongoDB.")
