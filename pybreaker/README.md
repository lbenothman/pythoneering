# PyBreaker - Circuit Breaker Pattern

Stop waiting for broken services to respond. **Fail fast instead.** 🔥

## The Problem

Your API keeps calling a dead service for 30 seconds every time. Everything slows down. Users leave.

## The Solution

Use pybreaker. After a few failures, it stops trying completely—returns an error instantly without making the call. Your app stays fast while the broken service fixes itself.

## How it works

**Fails 5 times → stops calling for 60 seconds → tries once → works? Resume. Still broken? Wait another 60 seconds.**

Fast systems don't keep knocking on broken doors. They move on and check back later.

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

See `main.py` for a complete FastAPI example using the circuit breaker pattern with `aiobreaker`.