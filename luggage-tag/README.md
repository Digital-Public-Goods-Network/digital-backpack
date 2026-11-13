# Luggage tag (proposal)

The luggage tag is the basic information that identifies a backpack. It's what the registry
points to. The formal definition is in [luggage-tag.schema.json](luggage-tag.schema.json).

```yaml
name: Riverbend Food Pantry
country: US
registration: US-EIN 12-3456789
website: https://riverbendpantry.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

## Fields

| Field | Required | Description | Example |
|---|---|---|---|
| `name` | Yes | Organization name | Riverbend Food Pantry |
| `country` | No | Two-letter country code (ISO 3166-1) where the organization is registered or based | `US` |
| `registration` | No | Government registration or tax ID, with its scheme. Use an [org-id.guide](https://org-id.guide) code where one exists. | `US-EIN 12-3456789` |
| `website` | No | Any URL for the organization: website, social media page, or directory listing | `https://riverbendpantry.example.org` |
| `references` | No | Others who can confirm the organization is real, such as a fiscal sponsor or a platform that has verified it | See below |

Each reference:

| Field | Required | Description | Example |
|---|---|---|---|
| `name` | Yes | Name of the reference | TechSoup |
| `comment` | No | Note from the reference, such as a verification status or relationship | `ELIGIBLE` |
| `url` | No | Link to the reference's record or contact page | |

Leave any optional field blank if it doesn't apply.

## Compared with other formats

| Tag | nonprofit-backpack prototype | TechSoup samples | PDC base fields | Candid Premier API | Charity Navigator API |
|---|---|---|---|---|---|
| `name` | `title` | `title` | `organization_name` | `summary.organization_name` | `name` |
| `country` | `registration.country` | `x-civic.registration_country` | `organization_country` | (US only) | `country` |
| `registration` | `registration.id` | `x-civic.registration` | `organization_tax_id` | `summary.ein` | `ein` |
| `website` | (not stored) | `resource` | `organization_website` | `summary.website_url` | `organization_url` |
| `references` | — | `x-civic.verifiable_by` | — | — | — |

In OKF files, `name` is stored as `title`.

## Differences from the nonprofit-backpack prototype

1. Adds `website` and `references`.
2. Moves `country` out of `registration`, so an unregistered organization still has one.
3. Leaves the summary and tags on `about.md`.

## Examples

[examples/README.md](examples/README.md) has tags for TechSoup's 15 sample backpacks, plus a
village group, a fiscally sponsored project, and a small volunteer group.
