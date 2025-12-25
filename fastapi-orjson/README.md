# FastAPI with ORJson

Speed up JSON serialization - orjson is 2-3x faster than standard library json.

## The Problem

```python
from fastapi import FastAPI

app = FastAPI()  # Uses slow standard library json

@app.get("/data")
async def get_data():
    return {"users": [{"id": i} for i in range(10000)]}  # Slow serialization
```

## The Solution

```python
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)  # Use orjson globally

@app.get("/data")
async def get_data():
    return {"users": [{"id": i} for i in range(10000)]}  # Fast serialization
```

## Benefits

- **2-3x faster** JSON serialization
- **Drop-in replacement** - no code changes needed
- **Better type support** - handles datetime, UUID automatically

## Installation

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Usage

```bash
python3 main.py
curl http://localhost:8000/data
```

## When to Use

Use for APIs with large JSON payloads or high traffic where performance matters.