# Nonprofit Backpacks: An agency-preserving data infrastructure for nonprofits

## What this is

A brainstorm and early design project exploring a new infrastructure to serve as a primary data layer for the global social sector . The core idea: nonprofits maintain a standardized but flexible self-description document to serve as their nonprofit backpack — called here organization.md — analogous to how a software project might maintain a CLAUDE.md or AGENTS.md file. It lives close to the organization, is maintained by the organization, and is designed to benefit the organization (not just the regulator or researcher consuming it).

**Important scope note**: The goal is not to build a better 990 or other registry or platform. It's to reimagine how a data ecosystem designed to support nonprofits directly could work — one where the 990's de facto non-tax uses (discoverability, transparency, research, categorization) are treated as first-class citizens with aligned incentives, rather than accidental byproducts of a tax compliance form.

## Some current challenges with using 990 data

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

Orgs should be able to use their file to auto-populate grant applications and other data-entry contexts. An LLM handles the translation between the org's file and whatever form the destination requires. One implementation path might be a browser extension with access to the org's file

## Design principles

Solutions here should:

- **Leverage the Lindy Effect**: A viable solution should get more durable the longer it's in use,
  not more fragile. Prefer design choices that reward longevity (file
  conventions, open formats) over those that require ongoing coordination
  (centralized registries, platform lock-in).
- **Center Org-first incentives**: The org maintaining the file should benefit directly
  from keeping it current. If the value flows only to consumers (funders,
  researchers), the behavior won't sustain.
- **Avoid chokepoints**: Central hosting can exist as a convenience,
  but the standard must be viable without it.

## Related docs

- [`SCHEMA.md`](SCHEMA.md) — the working draft schema `organization.md` 
- [`QUESTIONS.md`](QUESTIONS.md) — open design questions, standardization
  challenges found while drafting real examples, and unresolved next steps.
