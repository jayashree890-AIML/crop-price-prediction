from fastapi import FastAPI, UploadFile, File
import pandas as pd
import uvicorn
import os

app = FastAPI()

# Load dataset
df = pd.read_csv("daily_price.csv")  # Ensure this file is in the backend folder

@app.get("/trends")
def get_trends():
    trends = df.groupby("commodity")["price"].mean().to_dict()
    return {"average_price": trends}

@app.post("/predict")
async def predict_crop(file: UploadFile = File(...)):
    # For now, just return a dummy response (Replace with ML model later)
    return {
        "crop": "Wheat",
        "market_trend": {
            "latest_price": 250,
            "demand_index": 85
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
