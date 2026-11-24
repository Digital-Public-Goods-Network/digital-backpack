"""Regenerate the example bundles with the library, unpacked so they read well on GitHub.

The fetchers are injected with stubs so the US example is reproducible without network or an LLM key.
That injection point (`resolve(..., lookup_ein=, crawl_site=, draft=)`) is also how an integrator swaps
in their own registry or scraper.   Run:  python examples/make_examples.py
"""
from __future__ import annotations

import io
import shutil
import zipfile
from pathlib import Path

from nonprofit_backpack import Intake, build, confirm, resolve
from nonprofit_backpack import bundle
from nonprofit_backpack.draft import Draft
from nonprofit_backpack.propublica import LookupResult, PAGE
from nonprofit_backpack.scrape import Page

ROOT = Path(__file__).parent
FIXED_AT = "2026-10-21T12:00:00Z"
bundle.now_iso = lambda: FIXED_AT          # every timestamp, and the log.md date heading, stay fixed across runs


def unpack(bp, dest: Path):
    shutil.rmtree(dest, ignore_errors=True)
    with zipfile.ZipFile(io.BytesIO(bp.to_bytes())) as z:
        z.extractall(dest)
    print(f"wrote {dest.relative_to(ROOT.parent)}")


# --- US: typed name + stubbed EIN lookup + stubbed crawl + stubbed draft -----------------------------
def fake_lookup(ein):
    return LookupResult(name="Riverbend Food Pantry Inc", source={
        "id": "propublica", "resource": PAGE.format(ein=ein.replace("-", "")),
        "title": f"IRS record for EIN {ein} via ProPublica Nonprofit Explorer"}, fields=[
        ("name", "Riverbend Food Pantry Inc", "IRS name on record; the everyday name may differ"),
        ("country", "US", ""), ("registration_id", ein, "the EIN")])


def fake_crawl(url):
    return [Page(url, "Riverbend Food Pantry", "We distribute groceries to households in Riverbend County, Ohio…")]


def fake_draft(material):
    return Draft(model="openrouter:anthropic/claude-sonnet-4.5", texts={
        "summary": "Riverbend Food Pantry distributes groceries to households in Riverbend County, Ohio, through a weekly "
                   "client-choice pantry and a mobile delivery route.[^website]"},
        tags=["food-security", "families", "direct-service", "volunteer-run", "local"])


us = Intake.from_file(ROOT / "facts-us.yaml")
us.id = "0f3d2a1b-9c8e-4d7f-8a6b-5c4d3e2f1a0b"
resolved = resolve(us, lookup_ein=fake_lookup, crawl_site=fake_crawl, draft=fake_draft, log=print)
creator = "human:7f1e6c0a-3b2d-4e8f-9a1b-2c3d4e5f6a7b"
bp = build(resolved, creator, log=print)
confirm(bp, creator, ["organization.md"])         # the organization self-confirms the registration facts only
unpack(bp, ROOT / "us-riverbend-food-pantry")

# --- KE: everything typed, no fetching (so no tags: only the LLM writes them) ------------------------
ke = Intake.from_file(ROOT / "facts-ke.yaml")
ke.id = "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
resolved = resolve(ke, fetch=False, log=print)
creator = "human:c2a9d4e1-7b3f-4c6a-8d2e-1f0a9b8c7d6e"
bp = build(resolved, creator, log=print)
confirm(bp, creator)                                # everything self-confirmed
unpack(bp, ROOT / "ke-maji-safi-initiative")
