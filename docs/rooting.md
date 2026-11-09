# Rooting (optional, not needed)

Rooting gives a shell on the TV and lets you install apps through the Homebrew Channel. It does not replace the operating system, and it does not improve the picture. This project does not need it.

**Verification status:** Status compiled from the projects' own pages. Whether the 75QNED916QE firmware is exploitable is not yet checked.

## Reference device

- Model: LG 75QNED916QE
- Installed software version: 04.60.85 (read from Settings, Software Update)
- Offered update: 04.60.92, not installed. Automatic update is off.
- The TV's open source license list names MediaTek and Realtek drivers (for example Bluetooth). This is no sign of an open bootloader.

The software version was never updated by the owner, so 04.60.85 is probably the factory version.

Do not install the offered update if you want to keep the option of rooting. The projects below state that updates close the exploit, and downgrading is not supported.

## Status of known tools

| Tool | Notes |
|------|-------|
| [RootMyTV](https://github.com/RootMyTV/RootMyTV.github.io) | Never worked on webOS 8 (2023 models), patched on most others |
| [dejavuln-autoroot](https://github.com/throwaway96/dejavuln-autoroot) | webOS 3.5 and newer, 2024 models patched from the start, much recent firmware patched |
| [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot) | webOS 4.0 and newer |
| [LGTV-Firmware-Downgrade](https://github.com/tudos4/LGTV-Firmware-Downgrade) | Downgrade guide for webOS 4 to 6, not officially supported |

The community site [webosbrew.org](https://webosbrew.org) is the central entry point. The site CanI.RootMy.TV is referenced by those projects to check a firmware version.

## Official firmware for USB recovery

LG Switzerland offers no firmware download for the 75QNED916QE.AEU. Its support page lists only manuals. A page for the 75QNED916QA in East Africa lists firmware files, but they belong to a different model code and must not be used. LG's generic USB update steps (FAT32 drive, folder `LG_DTV`, `.epk` file) apply only to models with an official file. Not checked: the German page and the .AEK and .AVS variants.

Consequence: there is no official recovery file and no way to copy the installed firmware without root. If the TV stops booting, the realistic options are LG service and the factory reset in the menu.

## Risks

- A firmware update can close the exploit. If you lose access, you may not be able to root again.
- Downgrading is not officially supported and can brick the TV.
- A rooted TV is not a custom OS. LG's closed picture pipeline stays in place.
- Warranty and support can be affected.

## Recommendation

Do not root for this project. The goals (best picture, no tracking, clean audio) are reached with settings and network isolation alone. Treat rooting as a separate hobby project.
