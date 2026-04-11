# Organization.md: An agency-preserving digital backpack for nonprofits

## What this is

A brainstorm and early design project exploring an alternative to 990 data as
the primary data layer for the US nonprofit sector. The core idea: nonprofits
maintain a standardized but flexible self-description document — `organization.md`
— analogous to how a software project maintains a `CLAUDE.md`. It lives close to
the organization, is maintained by the organization, and is designed to benefit
the organization (not just the regulator or researcher consuming it).

**Important scope note**: The goal is not to build a better 990. It's to
reimagine how a data ecosystem designed to support nonprofits directly could
work — one where the 990's de facto non-tax uses (discoverability, transparency,
research, categorization) are treated as first-class citizens with aligned
incentives, rather than accidental byproducts of a tax compliance form.

## The problem with 990 data

- Not all nonprofits file the same form (990, 990-EZ, 990-N, 990-PF)
- It's a tax form — programmatic data is a second-class citizen
- Incentives are inverted: filers bear the cost, researchers and funders get
  the value
- Data is extracted from PDFs, messy, delayed (often 18+ months lag)
- Key benchmarks (enrollment, cost-per-client, financial aid rate) have no
  990 analog at all

## The CLAUDE.md analogy

CLAUDE.md works because:

- The entity being described maintains it (not a regulator)
- It's human-authored but machine-consumable
- It's close to the work
- The owner benefits directly from keeping it current

`organization.md` applies the same logic: nonprofits maintain a document that
makes them more legible to funders, partners, and data systems. Better
legibility → better access to funding, benchmarks, and partnerships. That's
the feedback loop that sustains the behavior.

## Value proposition for orgs

- Better discoverability by funders and partners
- Access to peer benchmarks (e.g., cost-per-client compared to similar orgs)
- An external manifestation of their work that's interoperable with AI tools
  and data systems — which increasingly mediate access to funding

## Proposed solution components

Beyond the schema itself, there are three additional components that make the
ecosystem work:

**1. Trust / digital signatures**

An org's file needs some form of validation that it represents a real registered
organization. Initially this comes from government records (EIN). Over time,
existing ecosystem actors that already validate orgs for their own purposes
(e.g., TechSoup verifies nonprofit status before granting software access) could
cryptographically sign a subset of an org's file. This lets trust established
on one platform transfer to another — lowering barriers to access for new orgs.
An extension: platforms could provide not just a binary signed/unsigned signal
but a more granular measure of how far the file's self-reported data deviates
from government records.

**2. Discoverability (robots.txt analogy)**

Funders, researchers, and platforms need to know where to find these files.
The model is robots.txt: a loosely defined but widely understood file convention
at a predictable location (`org.org/organization.md`). Any crawler knows where
to look and how to parse what it finds. A central registry can coexist as a
convenience layer but shouldn't be required — file-convention discoverability
is more resilient and avoids a gatekeeper.

**3. Grant application auto-population**

Orgs should be able to use their file to auto-populate grant applications and
other data-entry contexts. This is the PDC "common application" goal, but
without requiring all platforms to standardize fields. An LLM handles the
translation between the org's file and whatever form the destination requires.
One implementation path: a browser extension with access to the org's file.

## Design principles

- **Lindy**: A viable solution should get more durable the longer it's in use,
  not more fragile. Prefer design choices that reward longevity (file
  conventions, open formats) over those that require ongoing coordination
  (centralized registries, platform lock-in).
- **Org-first incentives**: The org maintaining the file should benefit directly
  from keeping it current. If the value flows only to consumers (funders,
  researchers), the behavior won't sustain.
- **No monetizable chokepoint**: Central hosting can exist as a convenience,
  but the standard must be viable without it.

## Schema design decisions so far

### Structure

YAML frontmatter for structured/queryable fields + markdown prose for
narrative sections. Follows the Jekyll/academic paper model: structured
abstract, freeform content.

### Universal sections

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

### Key open design questions

1. **Metrics standardization**: Should metrics be picked from a controlled
   vocabulary, or fully self-defined? Freeform is more honest; controlled
   vocab enables benchmarking.

2. **Revenue model field**: Revenue composition means different things across
   org types (tuition vs. contributions vs. fee-for-service). Need either a
   `revenue_model` field or convention for disambiguating.

3. **Asset composition**: Net assets are not comparable across orgs without
   knowing how much is real property vs. liquid endowment. Needs a flag or
   additional field.

4. **NTEE-based field modules**: Single-program orgs (like schools) and
   multi-program orgs (like fiscal intermediaries) have different structural
   needs. Schools also face FERPA constraints. A `data_constraints` field
   (e.g., `[FERPA, HIPAA]`) would signal why data posture is limited.

5. **Discoverability**: File convention at a predictable URL
   (`org.org/organization.md`) vs. central registry vs. both. File convention
   is more resilient and avoids a gatekeeper; registry enables querying.

6. **last_updated norm**: A stale document may be worse than none. What's
   the community norm for update frequency, and how does a consumer signal
   staleness?

7. **Naming**: `organization.md` is the working name, but it's not settled.
   The `*.md` framing signals key properties of the concept (plain text,
   human+machine readable, versioned). The right name should reinforce those
   signals without being so generic it loses meaning.

## Standardization challenges identified

Drafting two very different organizations (GlobalGiving and Shore Country Day
School) surfaced these tensions:

- **Single-program orgs** make a programs list feel ceremonial
- **Revenue composition** signals different things for tuition-driven vs.
  contribution-driven orgs, even on the same 990 line
- **Net assets** include real property for some orgs (campus) and not others
- **FERPA/HIPAA** constrain data posture for schools and health orgs
- **Key benchmarks for many org types have no 990 analog** — entirely
  dependent on self-report

## Next steps (not yet decided)

- Refine the schema based on early examples
- Draft additional examples from a different sectors (health, housing, arts) to stress-test
- Design the publication/consumption model (where does the file live, who crawls it)
- Consider the minimum viable version: what's the smallest schema that delivers
  real benchmarking value?
