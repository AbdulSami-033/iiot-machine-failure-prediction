import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Load model
model = joblib.load("model.pkl")

# Load dataset
data = pd.read_csv("simulated_iiot_dataset.csv")

# Features
X = data[["temperature", "pressure", "vibration", "humidity"]]

# Labels
y = data["machine_failure"]

# Predictions
predictions = model.predict(X)

print("\n====================================")
print(" MACHINE CONDITION MONITORING SYSTEM ")
print("====================================")

# Test Cases
for i in range(5):

    sample = X.iloc[i:i+1]

    prediction = model.predict(sample)

    temp = sample.iloc[0]["temperature"]
    pressure = sample.iloc[0]["pressure"]
    vibration = sample.iloc[0]["vibration"]

    print(f"\nTest Case {i+1}")

    print("Temperature:", temp)
    print("Pressure:", pressure)
    print("Vibration:", vibration)

    # Intelligent Decisions
    if prediction[0] == 0:

        print("STATUS: NORMAL")

        print("ACTION: Continue Monitoring")

    elif vibration > 0.7 and temp > 70:

        print("STATUS: CRITICAL")

        print("ACTION: EMERGENCY SHUTDOWN")

        print("ALERT: High Risk Machine Failure")

    else:

        print("STATUS: WARNING")

        print("ACTION: Maintenance Required")

# Performance Metrics
accuracy = accuracy_score(y, predictions)
precision = precision_score(y, predictions)
recall = recall_score(y, predictions)
f1 = f1_score(y, predictions)

print("\n====================================")
print(" PERFORMANCE METRICS ")
print("====================================")

print("Accuracy :", round(accuracy*100,2), "%")
print("Precision:", round(precision*100,2), "%")
print("Recall   :", round(recall*100,2), "%")
print("F1 Score :", round(f1*100,2), "%")

# Graph
plt.figure(figsize=(10,5))

plt.plot(data["vibration"][:100])

plt.title("Machine Vibration Monitoring")

plt.xlabel("Time")

plt.ylabel("Vibration Level")

plt.grid(True)

plt.show()
