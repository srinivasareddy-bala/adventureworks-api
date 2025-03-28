from fastapi import FastAPI, Query, HTTPException
import pandas as pd

app = FastAPI()

# Load the CSV data (Replace 'data.csv' with your actual file path)
DATA_FILE = "data.csv"
df = pd.read_csv(DATA_FILE)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/data")
def get_all_data():
    """Fetch all data from the CSV."""
    return df.to_dict(orient="records")

@app.get("/data/{row_id}")
def get_row_by_id(row_id: int):
    """Fetch a specific row by index (assuming 0-based index)."""
    if row_id < 0 or row_id >= len(df):
        raise HTTPException(status_code=404, detail="Row not found")
    return df.iloc[row_id].to_dict()

@app.get("/filter")
def filter_data(column: str = Query(...), value: str = Query(...)):
    """Filter data based on a column and value."""
    if column not in df.columns:
        raise HTTPException(status_code=400, detail="Invalid column name")
    
    filtered_df = df[df[column].astype(str) == value]
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="No matching records found")
    
    return filtered_df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
