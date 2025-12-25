import uvicorn
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# Add GZip compression middleware
# Compresses responses larger than 1000 bytes (1KB)
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/small")
async def small_response():
    """Small response - won't be compressed"""
    return {"message": "Small data"}


@app.get("/large")
async def large_response():
    """Large response - will be compressed automatically"""
    # Generate large JSON payload
    data = {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "bio": "This is a long biography text that takes up space. " * 10,
                "address": {
                    "street": f"{i} Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "zip": "94102",
                },
                "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
            }
            for i in range(1000)
        ]
    }
    return data


@app.get("/text")
async def large_text():
    """Large text response - highly compressible"""
    text = "This is a repeated line of text that compresses very well. " * 1000
    return {"content": text}


@app.get("/stats")
async def compression_stats():
    """Endpoint to show compression benefit"""
    import sys

    sample_data = {
        "users": [{"id": i, "name": f"User {i}"} for i in range(100)]
    }

    # Approximate size calculation
    uncompressed_size = sys.getsizeof(str(sample_data))

    return {
        "message": "GZip middleware enabled",
        "minimum_compression_size": "1000 bytes",
        "compression_ratio": "typically 60-80% reduction for JSON/text",
        "sample_uncompressed_size": f"{uncompressed_size} bytes",
        "estimated_compressed_size": f"~{uncompressed_size // 3} bytes (estimated)",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)