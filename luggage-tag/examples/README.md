# Example luggage tags

Tags for TechSoup's 15 synthetic sample backpacks
([okf-civic-sample](https://github.com/TechSoup/okf-civic-sample)), plus three cases they don't
include. All organizations are fictional. TechSoup's keep their `synthetic-` prefix, as TechSoup
asks. See [../README.md](../README.md) for the fields.

```yaml
name:           # required
country:
registration:   # a government registration number, if there is one
website:        # any URL: the org's own site, a social page, a directory listing
references:     # who you can ask whether this organization is real
  - name:       # who the reference is
    comment:    # the reference's own message, in its words
    url:        # optional: where to read more
```

## How the TechSoup tags were drafted

| Line | Taken from the TechSoup bundle |
|---|---|
| `name` | `title` in the main record |
| `country` | `registration_country` |
| `registration` | `registration`: the scheme and the ID |
| `website` | `resource`, the org's website |
| `references` → `name` | `verifiable_by`, which TechSoup defines as "who you can ask" |
| `references` → `comment` | the status line of TechSoup's determination in `verification.md` |

## Three more cases

A village group with no registration or website:

```yaml
name: Nyando Women's Water Group
country: KE
registration:
website:
references:
  - name: Kisumu Community Health Network
    comment: Funds the group's borehole repairs
  - name: Chief's office, Ahero location
```

A fiscally sponsored project with no registration of its own:

```yaml
name: Eastside Youth Media Lab
country: US
registration:
website: https://eastsideyouthmedialab.example.org
references:
  - name: Community Arts Fund
    comment: Fiscal sponsor; US-EIN 00-1000099
```

A small volunteer group that files the IRS e-Postcard (990-N):

```yaml
name: Alder Township Toy Drive
country: US
registration: US-EIN 00-1000098
website: https://aldertoydrive.example.org
references:
```

## TechSoup's 15 samples

```yaml
name: synthetic-Black Mountain Workforce Partnership
country: US
registration: IRS-EIN 00-1000008
website: https://synthetic-black-mountain-workforce.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Central Valley Farmworker Law Center
country: US
registration: IRS-EIN 00-1000005
website: https://synthetic-cv-farmworker-law.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Corporación Río Vivo
country: CO
registration: NIT 900.000.000-0
website: https://synthetic-rio-vivo.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Crescent City Career Lab
country: US
registration: IRS-EIN 00-1000012
website: https://synthetic-crescent-city-career-lab.example.org
references:
  - name: TechSoup
    comment: PENDING RE-VALIDATION — the determination on file has expired
```

```yaml
name: synthetic-Cumberland Gap Health Cooperative
country: US
registration: IRS-EIN 00-1000007
website: https://synthetic-cumberland-gap-health.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Eastside Harvest Collective
country: US
registration: IRS-EIN 00-1000001
website: https://synthetic-eastside-harvest.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE — with one open flag
```

```yaml
name: synthetic-Frogtown Community Table
country: US
registration: IRS-EIN 00-1000009
website: https://synthetic-frogtown-table.example.org
references:
  - name: TechSoup
    comment: APPROVE, 88% confidence (MODERATE)
```

```yaml
name: synthetic-Fundacja Prawo i Schronienie
country: PL
registration: KRS 0000000000
website: https://synthetic-prawo-schronienie.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Gulf Corridor Justice Project
country: US
registration: IRS-EIN 00-1000011
website: https://synthetic-gulf-corridor.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Motor City Trades Institute
country: US
registration: IRS-EIN 00-1000003
website: https://synthetic-motor-city-trades.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-North Star Immigrant Defense
country: US
registration: IRS-EIN 00-1000010
website: https://synthetic-north-star-defense.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Nyando Community Health Trust
country: KE
registration: Kenya public-benefit-organization framework PBO/0000/0000
website: https://synthetic-nyando-health.example.org
references:
  - name: TechSoup
    comment: INSUFFICIENT EVIDENCE — no determination reached
```

```yaml
name: synthetic-Riverbend Air Alliance
country: US
registration: IRS-EIN 00-1000002
website: https://synthetic-riverbend-air.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Sierra Foothills Community Health
country: US
registration: IRS-EIN 00-1000006
website: https://synthetic-sierra-foothills-health.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

```yaml
name: synthetic-Valle Verde Food Network
country: US
registration: IRS-EIN 00-1000004
website: https://synthetic-valle-verde.example.org
references:
  - name: TechSoup
    comment: ELIGIBLE
```

## License

Drafted from [TechSoup/okf-civic-sample](https://github.com/TechSoup/okf-civic-sample)
(commit `85dd8c1`), © TechSoup, licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Reference comments quote the
status line of each sample's simulated verification. This page is shared under CC BY-SA 4.0.
