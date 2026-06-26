# PROJECT_STATE.md — janishammer-home
> Version 1.0 — 2026-06-25
> Changes: Initial creation — bootstrap scan
> Previous: NONE

## Status: LIVE
## Domain: https://janishammer.com
## Last observed state: EN+TH homepage live. Blog active (6 EN + 6 TH posts generated). contact.html, iflex.html and TH mirrors present.
## Tech stack: Vanilla HTML/CSS/JS · Airtable · Python build · GitHub Actions · Cloudflare Pages
## Injector version: UNKNOWN — loads directly from assets.janishammer.com without version pinning. blog/index.html broken — references injector-versions.js which does not exist.

## Folder structure:
  Compliant: NO
  Issues: All HTML files at repo root (index.html, blog.html, contact.html, iflex.html). No /public/ folder. th/ subfolder for TH mirrors. blog/ subdirectory used for generated posts.

## SEO status (from scan):
  OG tags:   partial — og:title, og:description, og:image, og:url present on index.html. og:type MISSING. Twitter cards MISSING.
  Canonical: missing on all pages
  Schema:    missing — no schema.org markup found
  Hreflang:  missing — EN/TH pages not linked

## Security status (from scan):
  No issues found. All Airtable credentials in GitHub Secrets.

## Open issues observed:
  - blog/index.html: loads injector-versions.js via jsDelivr CDN — file does not exist in repo — injector will fail silently on blog listing page
  - og:type missing on index.html
  - Twitter card meta tags missing on all pages
  - No canonical tags on any page
  - No schema.org markup (LocalBusiness on homepage, Article on blog posts)
  - No hreflang on bilingual pages

## Session log (newest first):
### 2026-06-25 — Bootstrap scan
Seed CLAUDE.md, CC_CHAT_LOG.md, PROJECT_STATE.md created. No source files touched.
