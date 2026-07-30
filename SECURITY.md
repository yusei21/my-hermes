# Security policy

## Reporting vulnerabilities

Do not disclose exploitable vulnerabilities in a public issue. Contact the repository owner privately with reproduction steps, affected versions, impact, and any proposed mitigation.

## Secrets

Never commit API keys, access tokens, cookies, private keys, passwords, or unredacted environment files. Local secrets belong in ignored environment files or an external secrets manager.

## Agent safety baseline

- Tool access is denied by default.
- Filesystem, network, process, and credential capabilities must be granted independently.
- Destructive or externally visible actions require elevated policy and may require human approval.
- Generated code and downloaded content are untrusted.
- Memory and retrieved documents are untrusted context and may contain prompt injection.
- Self-improvement produces reviewable candidates; it must not mutate the active runtime directly.
- Logs and traces must redact secrets and sensitive personal information.
- Every execution path must support cancellation, timeouts, and resource limits.

## Dependency and provenance policy

Dependencies must be pinned through lockfiles before production use. Reused or adapted upstream material must be recorded in `NOTICE.md` with its source revision, copyright, license, modifications, and retained license location.
