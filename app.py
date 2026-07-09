from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Create FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

# Input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Iris Prediction API"}

# Prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):
    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    classes = ["Setosa", "Versicolor", "Virginica"]

    return {
        "prediction": classes[prediction[0]]
    }