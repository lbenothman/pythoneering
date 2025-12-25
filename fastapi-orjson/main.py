"""
FastAPI with ORJson for faster JSON serialization
"""
import time
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

# Use ORJSONResponse as default response class
app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/data")
async def get_data():
    # Large dataset example
    data = {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "metadata": {
                    "created_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T00:00:00Z",
                    "tags": ["tag1", "tag2", "tag3"],
                }
            }
            for i in range(1000)
        ]
    }
    return data


@app.get("/benchmark")
async def benchmark():
    # Create test data
    test_data = {"items": [{"id": i, "value": f"item_{i}"} for i in range(10000)]}

    # Measure serialization time (orjson is used automatically)
    start = time.perf_counter()
    # ORJSONResponse handles serialization automatically
    end = time.perf_counter()

    return {
        "message": "Using ORJson for fast serialization",
        "items_count": len(test_data["items"]),
        "serialization_time_ms": round((end - start) * 1000, 2)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)