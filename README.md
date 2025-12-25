# Pythoneering

A collection of practical Python code samples and concepts with working examples.

## Purpose

This repository provides hands-on code examples demonstrating Python concepts and patterns. Each folder contains:
- `main.py` - A working code example
- `README.md` - Explanation of the concept
- `pyproject.toml` - Dependencies and project configuration

## How to Use This Repository

1. **Learn by Running** - Each example is runnable. Install dependencies and execute the code to see it in action.
2. **Use uv for Fast Setup** - All projects use `uv` for dependency management. It's faster than pip and handles virtual environments automatically.
3. **Read the Code First** - Before running an example, read through `main.py` to understand what it does.
4. **Experiment** - Modify the examples to test your understanding. Break things and fix them.
5. **Check the README** - Each project's README explains the problem it solves and how it works.

## Tips & Examples

### Language Features & Syntax

| Tip | Description | Link |
|-----|-------------|------|
| **Walrus Operator (:=)** | Assign and use variables in one expression. Avoid duplicate function calls and write cleaner conditions. | [Read more →](./walrus-operator/README.md) |
| **contextlib.suppress** | Clean exception handling without try-except blocks. Intentionally ignore specific exceptions with readable code. | [Read more →](./contextlib-suppress/README.md) |
| **functools.partial** | Pre-fill function arguments to create specialized versions. Reduce code repetition and build reusable function factories. | [Read more →](./functools-partial/README.md) |

### Performance & Profiling

| Tip | Description | Link |
|-----|-------------|------|
| **cProfile** | Find performance bottlenecks by measuring execution time. Compare implementations and verify optimization improvements. | [Read more →](./cprofile-profiling/README.md) |
| **tracemalloc** | Track memory usage and find memory leaks. Compare memory efficiency of different implementations. | [Read more →](./tracemalloc-profiling/README.md) |

### Web Development & APIs

| Tip | Description | Link |
|-----|-------------|------|
| **FastAPI Exception Handlers** | Centralize error handling without repetitive try/catch blocks. Consistent error responses across all endpoints. | [Read more →](./fastapi-exception-handlers/README.md) |
| **FastAPI with ORJson** | Speed up JSON serialization by 2-3x using orjson instead of standard library json. | [Read more →](./fastapi-orjson/README.md) |
| **FastAPI Streaming Response** | Stream data to clients without loading everything into memory. Perfect for large files and real-time updates. | [Read more →](./fastapi-streaming-response/README.md) |
| **FastAPI GZip Middleware** | Automatically compress large responses to reduce bandwidth usage by 60-80%. | [Read more →](./fastapi-compress-responses/README.md) |
| **FastAPI Request Context** | Store and access request-scoped data throughout async request lifecycle using contextvars. | [Read more →](./fastapi-request-context/README.md) |
| **FastAPI Rate Limiting** | Protect your API from abuse by limiting request rates per IP or user. | [Read more →](./fastapi-rate-limit/README.md) |

### Resilience & Design Patterns

| Tip | Description | Link |
|-----|-------------|------|
| **Retry Pattern** | Handle transient failures with automatic retries and exponential backoff. Perfect for flaky network calls. | [Read more →](./retry/README.md) |
| **Circuit Breaker Pattern** | Fail fast when services are down. Protect applications from cascading failures and improve resilience. | [Read more →](./pybreaker/README.md) |

## License

MIT License - See [LICENSE](./LICENSE) for details.