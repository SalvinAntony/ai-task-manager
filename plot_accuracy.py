import pandas as pd
import matplotlib.pyplot as plt

# Load the accuracy log
df = pd.read_csv("accuracy_log.csv", names=["Timestamp", "Accuracy"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["Accuracy"], marker='o', linestyle='-')
plt.title("Model Accuracy Over Time")
plt.xlabel("Time")
plt.ylabel("Accuracy")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("accuracy_plot.png")  # Save to file
plt.show()
