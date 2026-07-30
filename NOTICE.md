# Notices and references

My Hermes is an independent project. It is not endorsed by, affiliated with, or maintained by Nous Research, Anthropic, OpenAI, Microsoft, LangChain, All Hands AI, SWE-agent, Mem0, the Model Context Protocol project, or the maintainers of ECC.

This repository is designed from original code and architectural study. When source code is incorporated or adapted, the relevant copyright notice, license text, source path, version or commit, and modification note must be recorded here before merge.

## Current provenance status

The current implementation and documentation are original project work. The projects below are architectural and comparative references only. No source code, prompts, tests, schemas, configuration, documentation text, or assets from those projects are intentionally bundled or adapted in this repository unless a later entry explicitly records that reuse.

## Primary references

### Hermes ecosystem

- **NousResearch/hermes-agent** — reference for agent runtime, model-provider integration, tools, plugins, messaging gateways, memory, scheduling, MCP support, and trajectory generation. Repository: `https://github.com/NousResearch/hermes-agent`. License must be verified at the exact revision before any code reuse.
- **NousResearch/hermes-agent-self-evolution** — reference for evaluated skill, prompt, and code improvement workflows. Repository: `https://github.com/NousResearch/hermes-agent-self-evolution`. License must be verified at the exact revision before any code reuse.
- **NousResearch/hermes-example-plugins** — reference for extension and plugin design. Repository: `https://github.com/NousResearch/hermes-example-plugins`. License must be verified at the exact revision before any code reuse.

### Agent engineering and orchestration

- **affaan-m/ECC** — reference for planning, testing, implementation, review, verification, memory, reusable skills, hooks, rules, and security scanning. Repository: `https://github.com/affaan-m/ECC`. The project identifies itself as MIT-licensed; preserve its license and copyright notices for any reused code.
- **All-Hands-AI/OpenHands** — reference for coding-agent runtime, workspace isolation, tool execution, GitHub workflows, and issue resolution. Repository: `https://github.com/All-Hands-AI/OpenHands`. Verify component-level licenses before reuse.
- **SWE-agent/SWE-agent** — reference for agent-computer interfaces, patch workflows, context management, and software-engineering evaluation. Repository: `https://github.com/SWE-agent/SWE-agent`. Verify the license at the exact revision before reuse.
- **langchain-ai/langgraph** — reference for durable state graphs, checkpoints, human approval, interruption, and resumption. Repository: `https://github.com/langchain-ai/langgraph`. Verify the license at the exact revision before reuse.
- **microsoft/autogen** — reference for typed multi-agent communication, supervision, and distributed execution. Repository: `https://github.com/microsoft/autogen`. Verify the license at the exact revision before reuse.

### Memory and interoperability

- **mem0ai/mem0** — reference for persistent memory, semantic retrieval, user profiles, and memory provenance. Repository: `https://github.com/mem0ai/mem0`. Verify the license at the exact revision before reuse.
- **modelcontextprotocol/servers** — reference implementations for Model Context Protocol integrations. Repository: `https://github.com/modelcontextprotocol/servers`. Individual server directories may have separate notices or dependencies; audit each one.

### Community Hermes projects inspected as references

- `https://github.com/yantrikos/yantrikdb-hermes-plugin`
- `https://github.com/paperclipinc/hermes-operator`
- `https://github.com/TheAiSingularity/hermesclaw`
- `https://github.com/protemplate/hermes-agent-railway`
- `https://github.com/mudrii/hermes-agent-docs`

These community repositories are references only. No code from them is included unless a later entry explicitly records the copied or adapted material and its license.

## Required reuse record

Every pull request that copies, translates, ports, adapts, or substantially derives code, configuration, prompts, documentation, tests, schemas, or assets from another project must add an entry containing:

1. Upstream repository and exact file path.
2. Commit SHA or release tag.
3. Upstream copyright holder.
4. Applicable license and link or retained local license path.
5. Description of copied or adapted material.
6. Description of local modifications.
7. Files in this repository containing the derived material.
8. Reviewer confirmation that attribution and redistribution requirements were checked.

Suggested entry format:

```text
### YYYY-MM-DD — component name
- Upstream: owner/repository
- Upstream path: path/to/file
- Revision: commit-or-tag
- Copyright: holder
- License: SPDX identifier or exact license name
- Local files: path/to/local/file
- Modifications: summary
- Retained notice/license: path or explanation
- Reviewed by: GitHub handle or pull request
```

Dependencies installed normally through a package manager should be recorded in lockfiles and dependency manifests. Bundled, vendored, patched, or modified dependencies require an explicit notice entry.
