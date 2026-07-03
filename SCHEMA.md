# `organization.md` schema

This describes the `organization.md` schema as it stands today. It's a
working draft, not a spec — see [`DECISIONS.md`](DECISIONS.md) for open
questions and unresolved tensions that may still change it.

For the project's motivation and design principles, see [`README.md`](README.md).

## Structure

YAML frontmatter for structured/queryable fields + markdown prose for
narrative sections. Follows the Jekyll/academic paper model: structured
abstract, freeform content.

## Universal sections

- **Identity** (frontmatter): name, EIN, NTEE code, size tier, fiscal year
  end, HQ, website, last_updated
- **Mission**: one-paragraph statement
- **Theory of change**: freeform prose
- **Programs**: structured list entries (type, description, scale, population
  served, outcomes tracked)
- **Financials**: summary + pointers to authoritative sources (990, audited
  financials) — not duplicating, just anchoring
- **Metrics**: structured YAML blocks with `metric`, `value`, `unit`, `year`,
  `methodology_note`
- **Governance**: leadership, board chair, CEO compensation (per 990)
- **Data posture**: what they collect, share publicly, share on request
- **Contact**: role-keyed contact points
- **What we're looking for**: freeform, could be semi-structured

## Reference examples

See `examples/` for drafted `organization.md` files, named
`<ein-without-hyphens>-<org_name_lower_snake_case>.md`.
