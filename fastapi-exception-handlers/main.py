"""
FastAPI Exception Handlers
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


# Custom exception
class ItemNotFoundError(Exception):
    pass


# Global handler
@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "Item not found"}
    )


# Clean endpoint - no try/catch needed
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id > 100:
        raise ItemNotFoundError()
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)