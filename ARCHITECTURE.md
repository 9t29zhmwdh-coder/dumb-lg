# Architecture

## Shape of the project

dumb-lg is a documentation project with a small Python tool. There is no service, no binary and nothing that runs on the TV.

```
docs/        guides (picture, audio, privacy, network, rooting)
tools/       style_check.py: checks Markdown for dashes and eszett
tests/       unit tests for the tool
.github/     CI, CodeQL, Scorecard, Dependabot
```

## Decision: configure the TV, do not replace its OS

A research pass found no custom firmware for webOS, only rooting that adds a shell and apps. Replacing the OS would need an open bootloader, drivers for the panel, local dimming and HDR tone mapping, and none of that is open. The result would be a worse picture. The goal of a plain, high quality display is reached with settings, network isolation and a clean audio path instead. See [docs/rooting.md](docs/rooting.md).

## Threat model (short)

| Threat (STRIDE) | Where | Measure |
|-----------------|-------|---------|
| Information disclosure | TV sends viewing data to the vendor | Privacy settings, no network or isolated VLAN |
| Tampering | Unvetted rooting tools run code on the TV | Rooting documented as optional, with risks, no instructions or payloads in this repo |
| Spoofing, tampering | Dependencies of the checker tool | Pinned versions, `pip-audit` in CI, Dependabot |
| Tampering | CI supply chain | Actions pinned to commit SHAs, least-privilege tokens |

The repository contains no secrets, no credentials and no exploit code.
