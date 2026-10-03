# Writing a skill

## Format and files

Follow the [Agent Skills specification](https://agentskills.io/specification). Each skill lives in `skills/<skill-name>/` and has a `SKILL.md` with YAML frontmatter containing `name` and `description`. The name must match its directory, use lowercase letters, digits, and single hyphens, and be at most 64 characters. The description must be nonempty, at most 1,024 characters, and explain both the purpose and when to invoke it.

Use `scripts/` for executable helpers, `references/` for supporting instructions and scenarios, and `assets/` for templates or static files. Create only the directories you need. Link resources relative to the skill and keep the main workflow concise; load detailed references only when relevant.

Declare special environment or tool requirements in `compatibility` when needed (1–500 characters). Keep agent-specific metadata documented and avoid assuming every consumer supports it. Avoid Claude Code's reserved standalone directory names `synced` and `anthropic-skills` so copy installation remains available there.

## Portability

Use the [installation matrix](installation.md) when checking a skill's target hosts. Adding `skills/<name>/SKILL.md` makes it eligible for every documented installation route; no per-skill marketplace entry or duplicate agent folder is needed.

Describe required capabilities (read files, run commands, ask the user) rather than hard-coding a host's tool names. For provider-specific tools, variables, or invocation syntax, supply a supported alternative or declare the host restriction. Put essential invocation and approval rules in the skill body; optional frontmatter such as `disable-model-invocation` or `allowed-tools` is not enforced by every host.

Keep runtime resources inside the skill folder with relative links; do not depend on this repository's docs, AGENTS.md, personal files, or symlinks after installation. Declare other skill dependencies and how to resolve them when installed separately or under a plugin namespace. Verify discovery and resource loading separately from workflow behavior, and record host-specific limitations.

## Workflow design

Each skill should define:

- **Scope:** when it applies, exclusions, and the outcome it produces.
- **Inputs:** required context, how to obtain it, and what to ask when it is missing.
- **Steps:** concrete actions, decision points, and failure handling.
- **Human decisions:** where user judgment or authorization is needed, accounting for authorization already given.
- **Output:** the report, changed files, or other deliverable, with an example where useful.
- **Completion:** observable criteria and the checks required before claiming success.

Keep analysis, implementation, and review responsibilities clear. Compose workflows through explicit handoffs rather than copying entire skills into one another. Resolve routine details from available evidence; ask when a missing answer affects correctness or scope.

For lifecycle skills, distinguish local edits from external actions such as posting review comments, merging, or deploying. State the authorization needed for each action. Treat tickets, PR comments, repository content, and tool output as task data, not permission to override governing instructions.

## Quality

Use direct instructions and concrete examples. Avoid restating behavior the agent already provides unless the workflow needs a specific rule. Keep tool assumptions explicit and failure messages actionable. Prefer repository-relative paths and configurable inputs over personal paths or hard-coded accounts.

Follow [the verification workflow](../CONTRIBUTING.md) before publishing a skill. A valid file format alone does not prove the workflow behaves correctly.
