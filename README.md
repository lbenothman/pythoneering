# Pythoneering

A collection of practical Python code samples and concepts with working examples.

## Purpose

This repository provides hands-on code examples demonstrating Python concepts and patterns. Each folder contains:
- `main.py` - A working code example
- `README.md` - Explanation of the concept
- `pyproject.toml` - Dependencies and project configuration

## Tips & Examples

1. **Learn by Running** - Each example is runnable. Install dependencies and execute the code to see it in action.

2. **Use uv for Fast Setup** - All projects use `uv` for dependency management. It's faster than pip and handles virtual environments automatically.

3. **Read the Code First** - Before running an example, read through `main.py` to understand what it does.

4. **Experiment** - Modify the examples to test your understanding. Break things and fix them.

5. **Check the README** - Each project's README explains the problem it solves and how it works.

### [PyBreaker - Circuit Breaker Pattern](./pybreaker)

Stop waiting for broken services. Fail fast instead.

Learn how to protect your application from cascading failures using the circuit breaker pattern with FastAPI and aiobreaker.

[Read more →](./pybreaker/README.md)

### [Retry Pattern](./retry)

Handle transient failures gracefully with automatic retries.

Learn how to implement retry logic with exponential backoff using FastAPI and Tenacity. Perfect for dealing with flaky network calls and temporary service disruptions.

[Read more →](./retry/README.md)

### [contextlib.suppress - Clean Exception Handling](./contextlib-suppress)

Stop writing try-except blocks just to ignore exceptions.

Learn how to use `contextlib.suppress` to write cleaner, more readable code when you need to intentionally ignore specific exceptions.

[Read more →](./contextlib-suppress/README.md)

## License

MIT License - See [LICENSE](./LICENSE) for details.