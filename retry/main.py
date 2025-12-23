from fastapi import FastAPI, HTTPException
from tenacity import retry, stop_after_attempt, wait_exponential
import httpx
import uvicorn
import random

app = FastAPI()

@retry(
    stop=stop_after_attempt(3),  # Try 3 times max
    wait=wait_exponential(multiplier=1, min=2, max=10)  # Wait 2s, 4s, 8s
)
async def fetch_external_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

@app.get("/data")
async def get_data():
    try:
        return await fetch_external_data("https://api.example.com/data")
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching data")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)