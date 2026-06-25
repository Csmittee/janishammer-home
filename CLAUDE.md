# CLAUDE.md — janishammer-home
> Version 1.0 — 2026-06-25
> Changes: Initial creation — governance seed
> Previous: NONE

Project: Janishammer Home — Root company landing page, binds all 4 brands
Domain: janishammer.com
BUS ID: N/A (parent brand — not a BUS site)

Governance: ALL rules at janishammer-central/RULES.md + .claude/rules/
Read janishammer-central CLAUDE.md before reading anything in this repo.

Injector:
  injector-config.js — YES — sync from assets.janishammer.com
  injector-core.js   — YES — sync from assets.janishammer.com
  NOTE: blog/index.html uses broken injector-versions.js reference via jsDelivr

Local key files:
  index.html               — EN homepage (480L) — links all brands
  blog/index.html          — Blog listing — BROKEN injector-versions.js ref
  scripts/generate_blog.py — Airtable → bilingual blog HTML

Critical constraint: blog/index.html loads injector-versions.js via jsDelivr
CDN but that file does not exist in the repo — injector will silently fail to
load on the blog listing page. See RETROFIT_QUEUE item #5.

Tech: Vanilla HTML/CSS/JS · Airtable · Python build · GitHub Actions · Cloudflare Pages
