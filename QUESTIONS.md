# Open questions and learnings

A running log of unresolved design questions, findings from drafting real
examples, and next steps. There are MANY more important questions to this work than are listed here,
so this shouldn't be assumed to be a complete list. Instead, it's meant to help begin trying to organize
some of the challenges we've surfaced so far.

## Key open design questions

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

8. **`size_tier` thresholds**: No fixed revenue thresholds are defined for
   small/medium/large. The drafting skill currently just says "use your
   judgment relative to the org's sector/NTEE category." May need real
   thresholds once more orgs are drafted.

## Standardization challenges identified

Drafting backpacks for real organizations based on available data surfaced these tensions:

- **Single-program orgs** make a programs list feel ceremonial
- **Revenue composition** signals different things for tuition-driven vs.
  contribution-driven orgs, even on the same 990 line
- **Net assets** include real property for some orgs (campus) and not others
- **FERPA/HIPAA** constrain data posture for schools and health orgs
- **Key benchmarks for many org types have no 990 analog** — entirely
  dependent on self-report
- **Website** isn't always listed on the 990 (blank or "N/A"). It's valuable
  enough that the drafting skill now stops and asks the user for it rather
  than guessing or silently omitting it.

## Next steps (not yet decided)

- Refine the suggested draft schema based on early examples
- Draft additional examples from different sectors (health, housing, arts) to
  stress-test the schema and surface more issues
- Design the publication/consumption model (where does the file live, who
  crawls it)
- Consider the minimum viable version: what's the smallest schema that
  delivers real benchmarking value?
- Continue iterating on the `draft-organization-md` skill — it is not yet
  validated and needs more rounds of testing and refinement.
