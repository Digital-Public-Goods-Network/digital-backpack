Read these before doing any work in this repo — they have the full project
context and these instructions override any default behavior:

- `README.md` — project motivation, problem statement, design principles.
- `SCHEMA.md` — the `organization.md` schema as it stands today.
- `DECISIONS.md` — open design questions, standardization challenges found
  while drafting real examples, and unresolved next steps.

## Conventions

- New `organization.md` drafts go in `examples/`, named
  `<ein-without-hyphens>-<org_name_lower_snake_case>.md` (e.g.
  `300108263-example_org_inc.md`).
- The `draft-organization-md` skill (`.claude/skills/draft-organization-md/`)
  generates drafts from 990 data. It is still under active iteration, not
  validated — expect to refine it as new example orgs surface issues.
- When drafting a new example surfaces a schema tension, standardization
  challenge, or open question, record it in `DECISIONS.md` rather than only
  fixing it ad hoc — that log is how the schema improves over time.
- `ideas/` is intentionally untracked in git (not yet in `.gitignore`,
  excluded by convention for now) — don't assume its absence means it
  doesn't exist.
