"""
FastAPI Rate Limiting with SlowAPI
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# Create limiter - rate limit by IP address
limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Custom rate limit exceeded handler
@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Rate limit exceeded",
            "message": "Too many requests. Please try again later.",
        },
    )


@app.get("/")
@limiter.limit("5/minute")  # 5 requests per minute
async def root(request: Request):
    return {"message": "Rate limited to 5 requests per minute"}


@app.get("/strict")
@limiter.limit("2/minute")  # Stricter limit
async def strict_endpoint(request: Request):
    return {"message": "Strict rate limit: 2 requests per minute"}


@app.get("/generous")
@limiter.limit("20/minute")  # More generous limit
async def generous_endpoint(request: Request):
    return {"message": "Generous rate limit: 20 requests per minute"}


@app.post("/api/data")
@limiter.limit("10/hour")  # Different time window
async def create_data(request: Request):
    return {"message": "Rate limited to 10 requests per hour"}


@app.get("/unlimited")
async def unlimited(request: Request):
    """No rate limit on this endpoint"""
    return {"message": "No rate limit"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)