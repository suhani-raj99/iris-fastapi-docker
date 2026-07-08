# Iris Flower Prediction API using FastAPI & Docker

## Project Overview

This project demonstrates how to deploy a Machine Learning model using FastAPI and Docker.

A Random Forest Classifier is trained on the Iris dataset and exposed through a REST API for predictions.

# Technologies Used

- Python
- FastAPI
- Scikit-learn
- Joblib
- Docker
- Uvicorn

## Project Structure

```
Task 3 Docker Project/
│── app.py
│── train_model.py
│── model.pkl
│── requirements.txt
│── Dockerfile
│── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:
  http://localhost:8000/docs
```

## Run using Docker

Build Image

```bash
docker build -t iris-api .
```

Run Container

```bash
docker run -p 8000:8000 iris-api
```

## API Endpoint

### POST /predict

Example Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example Response

```json
{
  "prediction": "Setosa"
}
```

## Author

               #Suhani Raj