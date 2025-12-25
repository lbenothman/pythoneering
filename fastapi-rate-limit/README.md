# FastAPI Rate Limiting

Protect your API from abuse by limiting request rates per IP or user.

## The Problem

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/api/expensive")
async def expensive_operation():
    # No rate limiting - vulnerable to abuse
    # User can spam this endpoint and overload your server
    await expensive_computation()
    return {"status": "done"}
```

## The Solution

```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.post("/api/expensive")
@limiter.limit("5/minute")  # Max 5 requests per minute per IP
async def expensive_operation(request: Request):
    await expensive_computation()
    return {"status": "done"}
```

## Benefits

- **Prevent abuse** - Stop spammers and bots
- **Protect resources** - Prevent server overload
- **Fair usage** - Ensure all users get access
- **Per-endpoint limits** - Different limits for different routes

## Configuration

**Different time windows:**
```python
@limiter.limit("5/minute")   # 5 per minute
@limiter.limit("100/hour")   # 100 per hour
@limiter.limit("1000/day")   # 1000 per day
@limiter.limit("10/second")  # 10 per second
```

**Multiple limits:**
```python
@limiter.limit("5/second;100/minute;1000/hour")
# Must satisfy all limits
```

**Custom key function (rate limit by user ID):**
```python
def get_user_id(request: Request):
    # Get user ID from auth token
    return request.headers.get("X-User-ID", get_remote_address(request))

limiter = Limiter(key_func=get_user_id)
```

**Custom error response:**
```python
from slowapi.errors import RateLimitExceeded

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests"}
    )
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

# Test rate limit (try multiple times quickly)
for i in {1..10}; do curl http://localhost:8000/; done

# You'll see successful responses, then 429 errors

# Different endpoints have different limits
curl http://localhost:8000/strict      # 2/minute
curl http://localhost:8000/generous    # 20/minute
```

## When to Use

Use for public APIs, authentication endpoints, expensive operations, or any endpoint vulnerable to abuse.

## When NOT to Use

Don't use for internal APIs behind authentication if you already have other rate limiting (like API gateway, nginx, CloudFlare).