import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

# Sample input (same order as training)
sample_input = np.array([[4.0, 85, 70, 3]])  
# study_hours, attendance_percentage, previous_score, assignments_completed

prediction = model.predict(sample_input)

print("Predicted Score:", prediction[0])
