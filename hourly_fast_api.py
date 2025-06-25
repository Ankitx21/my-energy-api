from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the data once
df = pd.read_csv("hourly_energy_summary.csv")

@app.get("/")
def welcome():
    return {"message": "Energy API – All Data Grouped by Date"}

@app.get("/all_energy")
def get_all_energy():
    grouped_data = {}

    for date, group in df.groupby("Date"):
        grouped_data[date] = group[['Hour', 'Energy_Actual', 'Energy_Predicted', 'Energy_LowerBound']].to_dict(orient='records')

    return grouped_data
