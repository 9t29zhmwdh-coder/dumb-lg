<div align="center">
  <img src="RayStudio.png" alt="RayStudio Logo" width="120"/>
  <h1>dumb-lg</h1>
</div>

[🇩🇪 Deutsche Version](README.de.md)

**Turn a smart LG TV into a plain, high quality HDMI display. No apps, no tracking, Dolby Atmos through eARC. Documentation and Python tooling.**

A practical guide for getting the best picture and clean surround sound out of an LG webOS TV that you only use as a screen, with an Apple TV 4K as the source and a soundbar on eARC. Written around the LG 75QNED916QE (2023), useful for most webOS 6 to 8 models.

[![CI](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/ci.yml/badge.svg)](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/ci.yml) [![CodeQL](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/codeql.yml/badge.svg)](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/codeql.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/9t29zhmwdh-coder/dumb-lg/badge)](https://scorecard.dev/viewer/?uri=github.com/9t29zhmwdh-coder/dumb-lg)
![Platform](https://img.shields.io/badge/platform-LG%20webOS-lightgrey) ![Python](https://img.shields.io/badge/python-3.12-orange) ![AI | Claude Code](https://img.shields.io/badge/AI-Claude%20Code-black)

> **How it runs:** Nothing is installed on the TV. This repository is documentation plus a small checker script for the writing rules. You follow the guides and change settings on your own devices.

---

**In practice:** After following the guides your TV shows only what your HDMI sources send. It does not need the internet, shows no ads, and sends no viewing data. The soundbar gets the Dolby signal from the Apple TV through the TV's eARC port.

## Why no custom firmware?

The original idea was to flash a custom OS. A research pass found that this is not realistic:

- There is no custom firmware project for webOS. What exists is rooting plus the [webOS Homebrew Channel](https://www.webosbrew.org), which gives a shell and extra apps but does not replace the OS.
- Rooting exploits ([RootMyTV](https://github.com/RootMyTV/RootMyTV.github.io), [dejavuln-autoroot](https://github.com/throwaway96/dejavuln-autoroot), [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)) are mostly patched on recent firmware.
- The picture pipeline (panel tuning, local dimming, HDR tone mapping) is LG's proprietary part. A replacement OS would make the picture worse, not better.

So this project reaches the same goal differently: configure the TV as a display, isolate it from the network, and fix the audio path. Details in [docs/rooting.md](docs/rooting.md) and [ARCHITECTURE.md](ARCHITECTURE.md).

## Guides

| Guide | What it covers |
|-------|----------------|
| [Picture settings](docs/picture-settings.md) | Best picture from HDMI sources, Apple TV output format |
| [Audio routing](docs/audio-routing.md) | Apple TV to TV to soundbar with Dolby Atmos over eARC, troubleshooting |
| [Privacy settings](docs/privacy-settings.md) | Switch off tracking, ads and recommendations on the TV |
| [Network isolation](docs/network-isolation.md) | Run the TV without internet or in a locked down VLAN |
| [Rooting (optional)](docs/rooting.md) | Honest status, risks, why it is not needed here |

## Requirements

- An LG webOS TV with an eARC capable HDMI port
- A soundbar or receiver with eARC or ARC
- An Apple TV 4K (any other HDMI source works for the picture guides)
- Python 3.12 only if you want to run the repository checks

## Quick Start

1. Read [Audio routing](docs/audio-routing.md) first if sound is your problem.
2. Work through [Picture settings](docs/picture-settings.md) and [Privacy settings](docs/privacy-settings.md) on the TV.
3. Decide between the no network option and a VLAN in [Network isolation](docs/network-isolation.md).

Run the repository checks:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 tools/style_check.py .
```

## Status of the guides

The settings names come from vendor documentation and community reports. Menu labels differ between firmware versions. Each guide marks what is verified on the 75QNED916QE and what is not yet. See [ROADMAP.md](ROADMAP.md).

## Uninstall / Cleanup

There is nothing to uninstall: the repository changes no device. Delete the cloned folder to remove everything. Settings you changed on the TV are reverted under Settings, General, Reset to Initial Settings.

---

**Author:** [Rafael Yilmaz](https://github.com/9t29zhmwdh-coder) · **Status:** Early Release · ![version](https://img.shields.io/github/v/release/9t29zhmwdh-coder/dumb-lg?color=6b7280&style=flat-square) · **License:** MIT
