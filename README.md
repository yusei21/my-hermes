# My Hermes (test)

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

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`NOTICE.md`](NOTICE.md).

## Security

Do not commit API keys or credentials. Use environment variables or a secrets manager. Tool access must be denied by default and explicitly granted per task.
