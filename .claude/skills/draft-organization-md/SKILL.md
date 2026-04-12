---
name: draft-organization-md
description: >
  Draft an organization.md file for a US nonprofit from its 990 data. Use this
  whenever the user wants to generate, draft, or auto-populate an
  organization.md (or "org.md") file for a specific nonprofit, gives a
  ProPublica Nonprofit Explorer link or EIN and asks for a profile/summary
  document, or asks to turn 990 data into the project's nonprofit
  self-description schema. Also trigger if the user pastes raw 990 data or
  financials for an organization and asks for it to be "written up" or
  "turned into a draft" in this project's format — even if they don't say
  "organization.md" by name.
---

# Draft an organization.md file from 990 data

This skill turns 990 data for a nonprofit into a draft `organization.md` file
— the self-description document format this project is designing as an
alternative data layer for the nonprofit sector (see the project's
`README.md` for the full rationale). The 990 is a starting point, not the
ceiling: a lot of what makes `organization.md` valuable has no 990 analog at
all, so a good draft is explicit about what it inferred, what it's guessing
at, and what the org itself needs to fill in.

## Step 1: Get the 990 data

Today, the data source is ProPublica's Nonprofit Explorer
(projects.propublica.org/nonprofits). The user may hand you a link, pasted
text, or a rough summary of the org's financials — work with whatever they
give you, and ask for a ProPublica link or EIN if you don't have enough to
find the filing.

Treat this step as a swappable data-fetch, not a ProPublica-specific parser.
The project's plan is to move to the GivingTuesday 990 API once this skill is
working, because it exposes the same underlying data through a cleaner API
rather than a scraped public filing. Concretely: keep the fields you need
(name, EIN, tax status/exemption date, NTEE code, fiscal year end, address,
revenue/expense/asset breakdowns, officer compensation, program service
descriptions) as a plain intermediate list, and treat "where did these values
come from" as a separate concern from "how do I lay them out in the
document." That way swapping the source later means changing how the list
gets populated, not rewriting the drafting logic below.

## Step 2: Populate the frontmatter

```yaml
schema_version: "0.1"
name: <legal name from 990>
ein: "<EIN, as a quoted string — leading zeros matter>"
tax_status: 501(c)(3)   # or whatever applies
tax_exempt_since: <YYYY-MM>
ntee_code: <code, if available>
fiscal_year_end: "<MM-DD>"
size_tier: <small | medium | large — judge from revenue; no fixed
  thresholds are set yet, so use your judgment relative to the org's
  sector/NTEE category>
website: <org's website, not ProPublica's>
hq:
  city: <city>
  state: <state>
  country: US
last_updated: <today's date, YYYY-MM-DD>
```

If a field genuinely isn't in the 990 or available source data, omit it
rather than guessing — frontmatter is meant to be reliable structured data,
so don't quietly fill gaps here the way you will in prose sections below.

**Website is the one exception to "just omit it."** The 990 doesn't always
list a website (some filers leave it blank or list "N/A"), but it's valuable
enough — and easy enough for a human to just supply — that you should ask
the user for it rather than silently dropping the field. If it's not
explicitly listed on the filing, stop and ask the user for the org's
website before finishing the draft, rather than guessing at a plausible-
looking URL or leaving it out unremarked.

## Step 3: Draft the narrative and structured sections

Work through each section in this order: Mission, Theory of change, Programs,
Financials, Metrics, Governance, Data posture, Contact, What we're looking
for.

**Financials, Governance**: these come straight from the 990 — revenue
breakdown by source, expenses, net assets, officer/executive compensation,
board chair. Link to the filing itself (ProPublica URL, or whatever source
you used) and to audited financials if the org publishes them, rather than
duplicating every line item.

**Mission**: every 990 has this — it's Part III, Line 1 ("Briefly describe
the organization's mission"). Extract it directly and quote/adapt it from the
filing; do not guess or infer it from the org's name or NTEE code. If your
data source's summary view doesn't surface this field (some scraped or
summarized sources only expose financials), that's a sign you need to go
back to the actual filing — the full 990 PDF or e-file XML — rather than
drafting around the gap. If, after checking the real filing, the mission
line genuinely isn't retrievable through the tools available to you, leave
the section as an explicit placeholder (`<!-- Org to add: not retrievable
from the 990 filing text available -->`) rather than writing inferred prose
— an invented mission statement is worse than no mission statement, since a
reader has no way to tell it's a guess just by reading it.

**Theory of change, "What we're looking for"**: unlike mission, these are
never on the 990 at all — there's no line item to go find. Write your
best-effort version from what you do have — the real mission text you just
extracted, program service descriptions, NTEE code, org name. Mark anything
inferred this way with an inline HTML comment, e.g.:

```markdown
<!-- Inferred from NTEE code and program descriptions; org should confirm or replace -->
```

The point isn't to hedge everything — write real, specific prose, not
mush — it's to make clear to the org reading the draft which sentences are
your best guess versus which came straight from source data, so they know
what needs a human check before publishing.

**Programs**: match the structure to how the org actually operates, don't
force a template. An org with multiple distinct program areas gets a full
list with type/description/scale/population served/outcomes tracked for
each. An org that really runs one core program (like a single school, a
single clinic) should get one lighter entry rather than an artificially
padded list — add a comment noting why (e.g. `<!-- Note: this org runs a
single core program; a multi-entry programs list would add little value
here -->`).

**Metrics**: pull anything genuinely on the 990 (e.g., program-service
revenue as a percent of total revenue) into a structured `metrics` YAML
block with `metric`, `value`, `unit`, `year`, and a `methodology_note`
explaining how you calculated it. Then — this matters — add a comment
block listing the benchmark metrics this org type would actually want that
the 990 simply doesn't capture (enrollment, cost-per-client, financial aid
rate, student-to-faculty ratio, whatever's relevant to its NTEE
category/program model), formatted like this:

```markdown
# Org would ideally add:
# - metric: <name>
# - metric: <name>
# These are standard <sector> benchmarks but not derivable from 990.
```

This is one of the more important parts of the draft — it's the clearest
illustration of the whole project's thesis, that the 990 misses most of what
would actually make an org legible to funders and peers.

**Data posture**: describe what the org likely collects, publishes, and
restricts, based on its program model. If the org's population served
implies FERPA (schools), HIPAA (health/clinical services), or similar
constraints, say so explicitly and add a `data_constraints` note (e.g.
`data_constraints: [FERPA]`) — and write the "shares publicly" /
"restricted" language more cautiously than you would for an org with no such
constraints.

**Contact**: infer role-keyed addresses only if you have real evidence for
them (org's own website, published contact page). Don't invent plausible-
looking emails — if you can't find real contact info, leave the section as
a placeholder comment instead (`<!-- Org to add contact points -->`).

## Step 4: Save the output

Name the file `<ein>-<org_name>.md` and write it to `examples/`, where:

- `<ein>` is the org's EIN with the hyphen removed (e.g. `300108263`)
- `<org_name>` is the org's registered name in `lower_snake_case` (lowercase,
  words separated by underscores, punctuation stripped)

For example, an org with EIN `30-0108263` and registered name "Example
Org Inc" would produce `examples/300108263-example_org_inc.md`.

Never overwrite an existing draft for a different org — if a file with the
same name already exists, check with the user before replacing it.

## A note on judgment

This is not a mechanical fill-in-the-fields process. Different organizations will need different
structures. Some structured data is necessary and should be populated via the YAML in the
frontmatter. Beyond that, organizations should have full agency over how they're represented in
their organization.md file. Given that, always the org's actual 990 and situation before drafting,
and let the shape of the document follow from that, rather than forcing every org through an
identical template.
