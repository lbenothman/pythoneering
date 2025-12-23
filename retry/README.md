# Retry Pattern Example

This example demonstrates the Retry pattern using FastAPI and the Tenacity library.

## Overview

The Retry pattern automatically retries failed operations with configurable backoff strategies. This is useful for handling transient failures in distributed systems.

## Features

- **Exponential Backoff**: Waits 2s, 4s, 8s between retries
- **Stop After Attempt**: Maximum of 3 retry attempts
- **Async Support**: Works with async/await patterns
- **FastAPI Integration**: Example endpoint demonstrating retry logic

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
uv run uvicorn main:app --reload
```

Then access the endpoint:

```bash
curl http://localhost:8000/data
```

## How It Works

The `@retry` decorator from tenacity wraps the `fetch_external_data` function:

- If the HTTP request fails, it automatically retries
- Uses exponential backoff: 2s, 4s, 8s between attempts
- Stops after 3 failed attempts
- Raises the final exception if all retries fail

## Configuration

- `stop=stop_after_attempt(3)`: Try up to 3 times
- `wait=wait_exponential(multiplier=1, min=2, max=10)`: Wait 2^x seconds between retries (capped at 10s)