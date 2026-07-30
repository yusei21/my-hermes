# My Hermes

My Hermes is an experimental, security-first agent engineering platform inspired by the Hermes Agent ecosystem and established open-source agent frameworks.

The project is being built as a modular system with explicit planning, sandboxed execution, independent review, verification, persistent memory, skill evaluation, observability, and controlled self-improvement.

## Current status

Initial architecture and engineering foundation. APIs are unstable.

## Design principles

- Persist task state outside the conversation context.
- Separate planning, execution, review, and verification.
- Treat tools as typed, permissioned capabilities.
- Run untrusted work in isolated environments.
- Record provenance for memories, skills, prompts, and generated artifacts.
- Require measurable evaluations before accepting self-improvements.
- Support multiple model providers without coupling the core to one vendor.
- Preserve upstream attribution and license notices.

## Planned modules

- Agent runtime and state machine
- Model router
- Tool registry and permission policy
- Sandboxed command execution
- Working, episodic, semantic, and project memory
- Planner, executor, reviewer, verifier, and researcher roles
- Skills registry, versioning, evaluation, and rollback
- MCP integration
- Tracing, replay, metrics, and cost controls
- Benchmark and regression suites

## Development workflow

Changes are developed on focused branches and published through pull requests. Branch names use a short category prefix such as `feat/`, `fix/`, `docs/`, `test/`, `refactor/`, or `chore/`.

Every pull request must describe its scope, validation performed, security impact, and provenance impact. Changes that reuse or adapt third-party material must update [`NOTICE.md`](NOTICE.md) before merge. See [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) for the complete workflow.

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)
- [`NOTICE.md`](NOTICE.md)
- [`SECURITY.md`](SECURITY.md)

## Security

Do not commit API keys or credentials. Use environment variables or a secrets manager. Tool access must be denied by default and explicitly granted per task.
