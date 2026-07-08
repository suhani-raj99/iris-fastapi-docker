from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")