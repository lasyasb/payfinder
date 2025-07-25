
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from flask import send_from_directory
import os


app = Flask(__name__)
CORS(app)

model_path = os.path.join(os.path.dirname(__file__), 'model', 'salary_model.pkl')
model = joblib.load(model_path)

@app.route("/")
def serve_index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

@app.route("/script.js")
def serve_script():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "script.js")

@app.route("/style.css")
def serve_css():
    return send_from_directory("../frontend", "style.css")
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = pd.DataFrame([{
        "Job Title": data["job"],
        "Location": data["location"],
        "Education": data["education"],
        "Experience": data["experience"]
    }])
    prediction = model.predict(input_data)[0]
    return jsonify({"predicted_salary": round(prediction, 2)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
