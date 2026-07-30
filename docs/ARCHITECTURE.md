# Architecture

## Objective

My Hermes is structured as a durable agent runtime rather than a single prompt loop. A task is represented by persistent state, explicit transitions, typed tool calls, policy decisions, evidence, and evaluation results.

## Execution pipeline

```text
request
  -> classify risk and complexity
  -> load scoped memory
  -> create or validate plan
  -> execute permissioned steps in a sandbox
  -> collect deterministic evidence
  -> independent review
  -> verify acceptance criteria
  -> replan or finish
  -> write provenance-aware memory
  -> evaluate possible skill improvements
```

## Core boundaries

### Runtime

The runtime owns task state, transitions, cancellation, budgets, retries, and event emission. It does not directly implement provider APIs or tools.

### Model router

The model router maps a role and task requirement to a configured provider and model. It applies token, latency, quality, and cost policies. Provider-specific payloads remain behind adapters.

### Tools

Tools expose typed input and output schemas. Every invocation receives a capability decision, timeout, resource budget, and audit identifier. Tools are denied by default.

### Sandbox

Commands, generated code, and untrusted files execute in an isolated environment with explicit filesystem mounts, network policy, CPU and memory limits, and process timeouts.

### Memory

Memory records include content, type, source, confidence, scope, timestamps, retention policy, and invalidation status. Retrieval is selective and must not silently override current evidence.

### Roles

- Planner: decomposes work and defines acceptance criteria.
- Executor: performs approved steps.
- Reviewer: examines artifacts from an independent context.
- Verifier: runs deterministic checks against acceptance criteria.
- Researcher: gathers and ranks external evidence.

Roles are policies and capabilities, not necessarily separate model processes.

### Skills

A skill is a versioned procedure with an input schema, output schema, required capabilities, evaluation suite, provenance, and rollback metadata. A candidate skill is not promoted until it beats the current version on defined benchmarks without violating safety or cost limits.

### Observability

Every task emits structured events for state transitions, model calls, tool calls, policy decisions, artifacts, errors, token use, cost, and evaluation outcomes. Sensitive values must be redacted before persistence.

## State model

Initial states:

```text
CREATED
PLANNING
AWAITING_APPROVAL
EXECUTING
REVIEWING
VERIFYING
REPLANNING
SUCCEEDED
FAILED
CANCELLED
```

Transitions are validated centrally. Terminal states cannot transition further.

## Security invariants

1. No secret may be written to logs, prompts persisted as artifacts, or source control.
2. Network and filesystem access are explicit capabilities.
3. Destructive actions require elevated policy and, where configured, human approval.
4. Retrieved memory is untrusted context until corroborated.
5. Generated code is untrusted until sandboxed tests and review succeed.
6. Self-modification creates a candidate change; it never writes directly to the active runtime.
7. Every external artifact retains source and license provenance.

## Initial implementation phases

### Phase 1: trustworthy runtime

Persistent task model, transition validation, budgets, event log, typed tool protocol, unit tests, and CI.

### Phase 2: execution

Provider adapters, sandbox driver, filesystem and command tools, planner/executor/reviewer/verifier policies.

### Phase 3: memory and skills

Scoped memory, provenance, skill registry, benchmark runner, candidate promotion, rollback.

### Phase 4: integrations

MCP, GitHub, messaging gateways, desktop/API surfaces, scheduling, distributed workers.

### Phase 5: controlled evolution

Trajectory datasets, offline evaluation, prompt and skill optimization, canary releases, and regression monitoring.
