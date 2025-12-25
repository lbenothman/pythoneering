# FastAPI Streaming Response

Stream data to clients without loading everything into memory first.

## The Problem

```python
@app.get("/large-file")
async def get_large_file():
    # Loads entire file into memory - causes OOM for large files
    with open("huge_file.txt") as f:
        data = f.read()  # 5GB file = 5GB RAM usage
    return data
```

## The Solution

```python
from fastapi.responses import StreamingResponse

async def file_generator():
    with open("huge_file.txt") as f:
        for line in f:
            yield line  # Stream line by line

@app.get("/large-file")
async def get_large_file():
    return StreamingResponse(file_generator(), media_type="text/plain")
```

## Benefits

- **Low memory usage** - Process data chunk by chunk
- **Faster time to first byte** - Start sending data immediately
- **Real-time updates** - Server-Sent Events for live data

## Use Cases

**Large file downloads:**
```python
async def file_chunks():
    with open("video.mp4", "rb") as f:
        while chunk := f.read(64 * 1024):  # 64KB chunks
            yield chunk

@app.get("/video")
async def stream_video():
    return StreamingResponse(file_chunks(), media_type="video/mp4")
```

**Server-Sent Events:**
```python
async def event_stream():
    while True:
        data = await get_realtime_data()
        yield f"data: {data}\n\n"
        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Database result streaming:**
```python
async def query_results():
    async for row in database.execute("SELECT * FROM huge_table"):
        yield f"{row}\n"

@app.get("/export")
async def export_data():
    return StreamingResponse(query_results(), media_type="text/csv")
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

# Stream events (watch data arrive in real-time)
curl http://localhost:8000/stream

# Download streamed file
curl http://localhost:8000/download -o output.txt

# Server-Sent Events
curl http://localhost:8000/sse
```

## When to Use

Use when handling large files, real-time updates, or data that shouldn't be loaded entirely into memory.