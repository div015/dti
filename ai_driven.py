import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Sample dataset: user behavior data
# Columns: ['age', 'medication_intake_frequency', 'previous_missed_doses', 'time_since_last_dose']
# 'target' is whether they missed a dose (1) or not (0)

data = {
    'age': [70, 65, 80, 60, 75, 50],
    'medication_intake_frequency': [1, 2, 1, 3, 2, 1],  # frequency per day
    'previous_missed_doses': [0, 2, 1, 0, 3, 0],
    'time_since_last_dose': [6, 10, 12, 3, 15, 4],
    'target': [0, 1, 1, 0, 1, 0]  # Target: 0 for no missed dose, 1 for missed dose
}

df = pd.DataFrame(data)

# Prepare the features (X) and target (y)
X = df[['age', 'medication_intake_frequency', 'previous_missed_doses', 'time_since_last_dose']]
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model (Decision Tree for simplicity)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Predict if a user is likely to miss a dose
def predict_missed_dose(user_data):
    prediction = model.predict([user_data])
    if prediction == 1:
        return "Reminder: User is likely to miss a dose. Send reminder."
    else:
        return "No action needed."

# Example user data (age=70, frequency=1, previous missed doses=2, time since last dose=8)
user_data = [70, 1, 2, 8]
print(predict_missed_dose(user_data))
