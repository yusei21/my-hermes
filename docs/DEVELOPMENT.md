# Development workflow

## Objective

Changes should be reviewable, reversible, tested, and attributable. Work is published from focused branches through pull requests rather than committed directly to `main`.

## Branch naming

Use one category and a short kebab-case scope:

- `feat/<scope>` for new behavior
- `fix/<scope>` for defect corrections
- `docs/<scope>` for documentation-only work
- `test/<scope>` for test infrastructure or coverage
- `refactor/<scope>` for behavior-preserving restructuring
- `chore/<scope>` for maintenance and repository operations

Examples:

```text
feat/tool-registry
fix/terminal-timeout
docs/reference-governance
```

## Required pull request content

Each pull request should include:

1. Problem and intended result.
2. Files and architectural boundaries affected.
3. Validation commands and observed results.
4. Security, privacy, permissions, and secret-handling impact.
5. Compatibility and migration impact.
6. Provenance statement identifying third-party material or stating that the change is original work.
7. Documentation and `NOTICE.md` updates when applicable.

## Validation baseline

Run the checks configured by the repository before requesting review:

```bash
ruff check .
mypy src
pytest
```

A change should not weaken coverage thresholds, typing, security invariants, or deterministic validation without an explicit rationale in the pull request.

## Provenance and notices

Architectural inspiration alone should be identified as a reference in `NOTICE.md`. Copying or adapting implementation material requires a detailed reuse record before merge.

A reuse record is required for source code, prompts, rules, schemas, tests, configuration, documentation, generated assets, and nontrivial translations or ports. Record the exact upstream revision and local destination. Do not rely on a repository home page alone when an exact source path is available.

License compatibility must be checked before material enters the branch. Unverified material must not be merged. Preserve required copyright notices and license text.

## Security review triggers

Request explicit security review when a change introduces or modifies:

- command or code execution;
- filesystem or network access;
- credentials, tokens, or provider authentication;
- tool permissions or approval bypasses;
- sandbox boundaries;
- persistence of prompts, memories, traces, or user data;
- self-modification or automatic skill promotion;
- dependency installation or executable downloads.

## Merge policy

Prefer squash merging for focused branches so the target branch retains one coherent change. Delete the source branch after merge unless it is intentionally long-lived. Do not merge while required checks are failing or provenance information is incomplete.
