# FastAPI GZip Middleware

Automatically compress large responses to reduce bandwidth usage by 60-80%.

## The Problem

```python
from fastapi import FastAPI

app = FastAPI()  # No compression

@app.get("/data")
async def get_data():
    # Returns 500KB uncompressed - wastes bandwidth
    return {"users": [{"id": i, "data": "x" * 1000} for i in range(500)]}
```

## The Solution

```python
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)  # Compress responses > 1KB

@app.get("/data")
async def get_data():
    # Returns ~100KB compressed - saves 80% bandwidth
    return {"users": [{"id": i, "data": "x" * 1000} for i in range(500)]}
```

## Benefits

- **60-80% bandwidth reduction** for JSON/text responses
- **Faster transfers** on slow connections
- **Lower data costs** for mobile users
- **Automatic** - no code changes needed

## Why minimum_size Matters

**Compressing tiny responses makes them larger:**
```python
# Small response: 50 bytes uncompressed
{"status": "ok", "count": 5}

# Same response compressed: ~70 bytes (LARGER!)
# Compression adds overhead: headers + dictionary + compressed data
# Only worth it when savings > overhead (typically 1KB+)
```

**That's why we use minimum_size:**
```python
app.add_middleware(GZipMiddleware, minimum_size=1000)
# Skip compression for small responses (< 1KB)
# Only compress large responses where savings > overhead
```

## Configuration

**Default settings (recommended):**
```python
app.add_middleware(GZipMiddleware, minimum_size=1000)
# Only compresses responses larger than 1KB
```

**Custom minimum size:**
```python
# Compress everything larger than 500 bytes
app.add_middleware(GZipMiddleware, minimum_size=500)

# Don't do this - makes tiny responses larger!
app.add_middleware(GZipMiddleware, minimum_size=0)
```

## Installation

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Usage

```bash
python3 main.py

# Compare sizes - large response
curl -w "\nSize: %{size_download} bytes\n" http://localhost:8000/large
curl -H "Accept-Encoding: gzip" --compressed -w "\nCompressed: %{size_download} bytes\n" http://localhost:8000/large

# Small response - won't be compressed (< 1KB)
curl http://localhost:8000/small
```

## When to Use

Use for APIs serving large JSON/text responses, especially for mobile clients or slow connections.

## When NOT to Use

Don't compress already-compressed content (images, videos) or if a reverse proxy handles compression (nginx, CloudFlare).