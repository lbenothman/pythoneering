import asyncio
import time
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def generate_data():
    """Stream data chunk by chunk"""
    for i in range(10):
        await asyncio.sleep(0.5)  # Simulate processing
        yield f"data: Chunk {i + 1}\n\n"


async def generate_large_file():
    """Stream large file content without loading it all into memory"""
    for i in range(100):
        await asyncio.sleep(0.01)
        yield f"Line {i}: {'x' * 100}\n"


@app.get("/stream")
async def stream_data():
    """Stream data to client as it's generated"""
    return StreamingResponse(
        generate_data(),
        media_type="text/event-stream"
    )


@app.get("/download")
async def download_large_file():
    """Stream large file download without loading entire file into memory"""
    return StreamingResponse(
        generate_large_file(),
        media_type="text/plain",
        headers={"Content-Disposition": "attachment; filename=large_file.txt"}
    )


@app.get("/sse")
async def server_sent_events():
    """Server-Sent Events for real-time updates"""
    async def event_generator():
        for i in range(20):
            await asyncio.sleep(1)
            current_time = time.strftime("%H:%M:%S")
            yield f"data: Update {i + 1} at {current_time}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)