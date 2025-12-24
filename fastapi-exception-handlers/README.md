# FastAPI Exception Handlers

Centralize error handling without repetitive try/catch blocks. FastAPI feature.

## The Problem

```python
# Repetitive try/catch in every endpoint
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    try:
        if item_id > 100:
            raise ItemNotFoundError()
        return {"item_id": item_id}
    except ItemNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"error": "Item not found"}
        )

# Same try/catch repeated everywhere
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    try:
        if product_id > 100:
            raise ItemNotFoundError()
        return {"product_id": product_id}
    except ItemNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"error": "Item not found"}
        )
```

## The Solution

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom exception
class ItemNotFoundError(Exception):
    pass

# Global handler - define once
@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "Item not found"}
    )

# Clean endpoints - just raise the exception
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id > 100:
        raise ItemNotFoundError()
    return {"item_id": item_id}
```

## Benefits

**Eliminate repetitive error handling:**
```python
# Before: Try/catch in every endpoint
@app.get("/endpoint1")
async def endpoint1():
    try:
        # logic
    except SomeError:
        return error_response

@app.get("/endpoint2")
async def endpoint2():
    try:
        # logic
    except SomeError:
        return error_response

# After: Define handler once, use everywhere
@app.exception_handler(SomeError)
async def handle_error(request, exc):
    return error_response

@app.get("/endpoint1")
async def endpoint1():
    # Just raise when needed
    raise SomeError()

@app.get("/endpoint2")
async def endpoint2():
    # Just raise when needed
    raise SomeError()
```

**Consistent error responses:**
```python
# All ItemNotFoundError exceptions return the same format
# No risk of inconsistent error messages across endpoints
```

**Cleaner endpoint code:**
```python
# Focus on business logic, not error handling
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id > 100:
        raise ItemNotFoundError()  # Handler takes care of response
    return {"item_id": item_id}
```

**Multiple exception handlers:**
```python
class ItemNotFoundError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

@app.exception_handler(ItemNotFoundError)
async def handle_not_found(request, exc):
    return JSONResponse(status_code=404, content={"error": "Not found"})

@app.exception_handler(UnauthorizedError)
async def handle_unauthorized(request, exc):
    return JSONResponse(status_code=401, content={"error": "Unauthorized"})
```

## Installation

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install dependencies
uv sync
```

## Usage

Run the FastAPI server:

```bash
python3 main.py
```

Test the endpoints:
```bash
# Valid item (returns item)
curl http://localhost:8000/items/50

# Invalid item (triggers exception handler)
curl http://localhost:8000/items/150
```

## When to Use

- Multiple endpoints handle the same exception types
- You want consistent error responses across your API
- Reducing boilerplate try/catch code
- Centralizing error handling logic
- Building APIs with clean, maintainable code

## When NOT to Use

Don't use for exceptions that need endpoint-specific handling. Use regular try/catch when error handling differs per endpoint.