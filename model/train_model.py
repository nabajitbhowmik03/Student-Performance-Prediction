import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_excel("data/students.xlsx", engine="openpyxl")

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nDataset description:")
print(df.describe())

df = df.dropna()

X = df[['study_hours', 'attendance_percentage', 'previous_score', 'assignments_completed']]
y = df['final_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print("\nModel R2 Score:", accuracy)

joblib.dump(model, "model/student_model.pkl")

print("\nModel saved successfully!")
