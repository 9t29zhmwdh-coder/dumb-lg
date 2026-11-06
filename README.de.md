<div align="center">
  <img src="RayStudio.png" alt="RayStudio Logo" width="120"/>
  <h1>dumb-lg</h1>
</div>

[🇬🇧 English Version](README.md)

**Mach aus einem smarten LG-TV einen schlichten HDMI-Bildschirm mit Top-Bild. Keine Apps, kein Tracking, Dolby Atmos über eARC. Dokumentation und Python-Tooling.**

Eine praktische Anleitung, um aus einem LG-webOS-TV, den du nur als Bildschirm brauchst, das beste Bild und sauberen Surround-Sound herauszuholen. Quelle ist ein Apple TV 4K, dazu eine Soundbar an eARC. Gedacht für den LG 75QNED916QE (2023), nützlich für die meisten webOS-6-bis-8-Modelle.

[![CI](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/ci.yml/badge.svg)](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/ci.yml) [![CodeQL](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/codeql.yml/badge.svg)](https://github.com/9t29zhmwdh-coder/dumb-lg/actions/workflows/codeql.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/9t29zhmwdh-coder/dumb-lg/badge)](https://scorecard.dev/viewer/?uri=github.com/9t29zhmwdh-coder/dumb-lg)
![Platform](https://img.shields.io/badge/platform-LG%20webOS-lightgrey) ![Python](https://img.shields.io/badge/python-3.12-orange) ![AI | Claude Code](https://img.shields.io/badge/AI-Claude%20Code-black)

> **So läuft es:** Auf dem TV wird nichts installiert. Das Repo besteht aus Dokumentation und einem kleinen Prüfskript für die Schreibregeln. Du folgst den Anleitungen und stellst Einstellungen an deinen eigenen Geräten um.

---

**In der Praxis:** Nach den Anleitungen zeigt dein TV nur noch, was deine HDMI-Quellen senden. Er braucht kein Internet, zeigt keine Werbung und sendet keine Nutzungsdaten. Die Soundbar bekommt das Dolby-Signal vom Apple TV über den eARC-Anschluss des TVs.

## Warum keine eigene Firmware?

Die ursprüngliche Idee war, ein eigenes OS aufzuspielen. Die Recherche zeigt, dass das nicht realistisch ist:

- Es gibt kein Custom-Firmware-Projekt für webOS. Vorhanden sind Rooting und der [webOS Homebrew Channel](https://www.webosbrew.org). Das gibt eine Shell und Zusatz-Apps, ersetzt aber das OS nicht.
- Die Rooting-Exploits ([RootMyTV](https://github.com/RootMyTV/RootMyTV.github.io), [dejavuln-autoroot](https://github.com/throwaway96/dejavuln-autoroot), [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)) sind auf neuer Firmware meist gepatcht.
- Die Bildpipeline (Panel-Abstimmung, Local Dimming, HDR-Tonemapping) ist LGs proprietärer Teil. Ein Ersatz-OS würde das Bild verschlechtern, nicht verbessern.

Dieses Projekt erreicht das gleiche Ziel anders: den TV als Display konfigurieren, vom Netz trennen und den Audio-Weg reparieren. Details in [docs/rooting.md](docs/rooting.md) und [ARCHITECTURE.md](ARCHITECTURE.md).

## Anleitungen

| Anleitung | Inhalt |
|-----------|--------|
| [Bildeinstellungen](docs/picture-settings.md) | Bestes Bild von HDMI-Quellen, Apple-TV-Ausgabeformat |
| [Audio-Routing](docs/audio-routing.md) | Apple TV zu TV zu Soundbar mit Dolby Atmos über eARC, Fehlersuche |
| [Datenschutz-Einstellungen](docs/privacy-settings.md) | Tracking, Werbung und Empfehlungen am TV abschalten |
| [Netzwerk-Isolation](docs/network-isolation.md) | TV ohne Internet oder in einem abgeschotteten VLAN betreiben |
| [Rooting (optional)](docs/rooting.md) | Ehrlicher Stand, Risiken, warum es hier nicht nötig ist |

## Voraussetzungen

- Ein LG-webOS-TV mit eARC-fähigem HDMI-Anschluss
- Eine Soundbar oder ein Receiver mit eARC oder ARC
- Ein Apple TV 4K (für die Bild-Anleitungen geht jede HDMI-Quelle)
- Python 3.12, nur falls du die Repo-Prüfungen laufen lassen willst

## Schnellstart

1. Lies zuerst [Audio-Routing](docs/audio-routing.md), wenn der Ton dein Problem ist.
2. Arbeite [Bildeinstellungen](docs/picture-settings.md) und [Datenschutz-Einstellungen](docs/privacy-settings.md) am TV durch.
3. Entscheide dich in [Netzwerk-Isolation](docs/network-isolation.md) zwischen der Variante ohne Netz und einem VLAN.

Repo-Prüfungen ausführen:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 tools/style_check.py .
```

## Stand der Anleitungen

Die Einstellungsnamen stammen aus Herstellerdokumentation und Erfahrungsberichten. Menübezeichnungen unterscheiden sich je nach Firmware. Jede Anleitung markiert, was auf dem 75QNED916QE geprüft ist und was noch nicht. Siehe [ROADMAP.md](ROADMAP.md).

## Deinstallation / Aufräumen

Es gibt nichts zu deinstallieren: Das Repo verändert kein Gerät. Lösche den geklonten Ordner, dann ist alles weg. Am TV geänderte Einstellungen setzt du unter Einstellungen, Allgemein, Auf Werkseinstellungen zurücksetzen zurück.

---

**Author:** [Rafael Yilmaz](https://github.com/9t29zhmwdh-coder) · **Status:** Early Release · ![version](https://img.shields.io/github/v/release/9t29zhmwdh-coder/dumb-lg?color=6b7280&style=flat-square) · **License:** MIT
