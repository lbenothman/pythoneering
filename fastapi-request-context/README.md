# FastAPI Request Context

Store and access request-scoped data (request ID, user info) throughout async request lifecycle.

## The Problem

```python
# Passing context everywhere manually
async def process_order(user_id: str, request_id: str):
    await log(user_id, request_id, "Processing")
    await validate(user_id, request_id)
    await save(user_id, request_id)

@app.post("/order")
async def create_order(user_id: str):
    request_id = str(uuid.uuid4())
    # Pass context to every function - tedious and error-prone
    return await process_order(user_id, request_id)
```

## The Solution

```python
from contextvars import ContextVar

# Context variables - async-safe
request_id_var: ContextVar[str] = ContextVar("request_id")
user_id_var: ContextVar[str] = ContextVar("user_id")

# Set once in middleware
class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id_var.set(str(uuid.uuid4()))
        user_id_var.set(request.headers.get("X-User-ID"))
        return await call_next(request)

# Access anywhere without passing parameters
async def process_order():
    request_id = request_id_var.get()
    user_id = user_id_var.get()
    await log("Processing")  # Has access to context
    await validate()  # Has access to context
    await save()  # Has access to context
```

## Benefits

- **No manual parameter passing** - Access context anywhere
- **Async-safe** - Works correctly with asyncio and concurrent requests
- **Clean code** - No cluttering function signatures with context params
- **Request isolation** - Each request has its own context

## Use Cases

**Request tracing:**
```python
# Set in middleware
request_id_var.set(str(uuid.uuid4()))

# Access in any function
async def process():
    request_id = request_id_var.get()
    logger.info(f"[{request_id}] Processing started")
```

**User context:**
```python
# Set in middleware from auth token
user_id_var.set(token.user_id)

# Access in business logic
async def get_user_data():
    user_id = user_id_var.get()
    return await db.get_user(user_id)
```

**Correlation IDs for distributed tracing:**
```python
correlation_id_var.set(request.headers.get("X-Correlation-ID"))

# Pass to downstream services
async def call_service():
    headers = {"X-Correlation-ID": correlation_id_var.get()}
    await http_client.post(url, headers=headers)
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

# Basic request (auto-generated request ID)
curl http://localhost:8000/

# With custom request ID and user ID
curl -H "X-Request-ID: custom-123" -H "X-User-ID: user-456" http://localhost:8000/

# Test async context preservation
curl -X POST -H "X-User-ID: alice" http://localhost:8000/process

# Nested async calls
curl -H "X-User-ID: bob" http://localhost:8000/nested
```

## When to Use

Use for storing request-scoped data (request ID, user info, correlation IDs) that needs to be accessed throughout the request lifecycle in async APIs.

## When NOT to Use

Don't use for data that should be explicitly passed (function parameters are clearer) or for global application state (use dependency injection instead).