from fastapi import FastAPI, Query, HTTPException
import pandas as pd

app = FastAPI()

CUSTOMERS_DATA_FILE = "customers_api.csv"
SALES_DATA_FILE = "sales_api.csv"

df_customers = pd.read_csv(CUSTOMERS_DATA_FILE)
df_sales = pd.read_csv(SALES_DATA_FILE)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/data/customers")
def get_all_data():
    """Fetch all customers data from the CSV."""
    return df_customers.astype(str).to_dict(orient="records")

@app.get("/data/sales")
def get_all_data():
    """Fetch all sales data from the CSV."""
    return df_sales.to_dict(orient="records")

@app.get("/data/sales/{row_id}")
def get_row_by_id(row_id: int):
    """Fetch a specific row by index (assuming 0-based index)."""
    if row_id < 0 or row_id >= len(df_sales):
        raise HTTPException(status_code=404, detail="Row not found")
    return df_sales.iloc[row_id].to_dict()

@app.get("/data/customers/{row_id}")
def get_row_by_id(row_id: int):
    """Fetch a specific row by index (assuming 0-based index)."""
    if row_id < 0 or row_id >= len(df_customers):
        raise HTTPException(status_code=404, detail="Row not found")
    return df_customers.iloc[row_id].to_dict()

    
    return filtered_df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
