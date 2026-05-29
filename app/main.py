from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

from app.schema import StudentInput

app = FastAPI(
    title="Student Performance Prediction API",
    description="Predict student performance using Machine Learning",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = joblib.load("model/student_model.pkl")
except Exception:
    raise RuntimeError("Model not found. Train the model first.")

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running"}

@app.post("/predict")
def predict_performance(data: StudentInput):
    try:
        input_data = np.array([[
            float(data.study_hours),
            float(data.attendance_percentage),
            float(data.previous_score),
            float(data.assignments_completed)
        ]])

        raw_prediction = model.predict(input_data)[0]

        prediction = min(raw_prediction, 99.99)

        if prediction >= 80:
            category = "Excellent"
        elif prediction >= 60:
            category = "Good"
        elif prediction >= 40:
            category = "Average"
        else:
            category = "Needs Improvement"

        return {
            "predicted_score": round(float(prediction), 2),
            "performance_category": category
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
