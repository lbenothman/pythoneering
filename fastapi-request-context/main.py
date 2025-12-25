"""
FastAPI Request Context with contextvars (async-safe)
"""
import uuid
from contextvars import ContextVar
from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Context variables - async-safe
request_id_var: ContextVar[Optional[str]] = ContextVar("request_id", default=None)
user_id_var: ContextVar[Optional[str]] = ContextVar("user_id", default=None)


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Set up request context"""

    async def dispatch(self, request: Request, call_next):
        # Set context
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_var.set(request_id)

        user_id = request.headers.get("X-User-ID")
        if user_id:
            user_id_var.set(user_id)

        # Process request
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id

        return response


app.add_middleware(RequestContextMiddleware)


def get_request_id() -> Optional[str]:
    """Get current request ID from context"""
    return request_id_var.get()


def get_user_id() -> Optional[str]:
    """Get current user ID from context"""
    return user_id_var.get()


async def log_action(action: str):
    """Access context without passing parameters"""
    request_id = get_request_id()
    user_id = get_user_id()
    print(f"[{request_id}] User {user_id}: {action}")


@app.get("/")
async def root():
    """Access request context anywhere"""
    return {
        "request_id": get_request_id(),
        "user_id": get_user_id() or "anonymous",
    }


@app.post("/process")
async def process():
    """Context preserved across async calls"""
    await log_action("Started processing")

    # Nested async function - context still available
    async def do_work():
        await log_action("Doing work")
        return f"Processed by request {get_request_id()}"

    result = await do_work()
    await log_action("Finished processing")

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)