import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1️⃣ Load dataset
df = pd.read_excel("data/students.xlsx", engine="openpyxl")

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nDataset description:")
print(df.describe())

# 2️⃣ Handle missing values (simple way)
df = df.dropna()

# 3️⃣ Separate features and target
X = df[['study_hours', 'attendance_percentage', 'previous_score', 'assignments_completed']]
y = df['final_score']

# 4️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 6️⃣ Test model accuracy
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print("\nModel R2 Score:", accuracy)

# 7️⃣ Save the model
joblib.dump(model, "model/student_model.pkl")

print("\nModel saved successfully!")
