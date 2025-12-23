from fastapi import FastAPI, HTTPException
from aiobreaker import CircuitBreaker, CircuitBreakerError
import httpx
import logging
from datetime import timedelta
import uvicorn

app = FastAPI()

# Stop trying after 5 failures, wait 60s before testing again
breaker = CircuitBreaker(fail_max=3, timeout_duration=timedelta(seconds=60))

@breaker
async def call_payment_service(data: dict):
    async with httpx.AsyncClient() as client:
        logging.info("Calling payment service")
        response = await client.post(
            "https://httpbin.org/delay/10",
            json=data, timeout=3.0
        )
        return response.json()

@app.post("/payments")
async def process_payment(data: dict):
    try:

        result = await call_payment_service(data)
        return result
    except httpx.ReadTimeout:
        logging.warning("Payment service timeout")
        raise HTTPException(
            status_code=503,
            detail="Payment service unavailable"
        )
    except CircuitBreakerError:
        logging.warning("Circuit breaker is OPEN")
        raise HTTPException(
            status_code=503,
            detail="Payment service unavailable (circuit breaker open)"
        )
    except httpx.HTTPStatusError as exc:
        logging.error(f"Upstream error: {exc}")
        raise HTTPException(
            status_code=502,
            detail="Payment service error"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)