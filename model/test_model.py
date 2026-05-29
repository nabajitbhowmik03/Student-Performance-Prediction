import joblib
import numpy as np

model = joblib.load("student_model.pkl")

sample_input = np.array([[4.0, 85, 70, 3]])  

prediction = model.predict(sample_input)

print("Predicted Score:", prediction[0])
