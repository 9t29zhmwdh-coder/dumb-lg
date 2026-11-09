# Audio routing: Apple TV, LG TV, soundbar

Goal: Dolby Atmos from an Apple TV 4K reaches a soundbar through the TV, instead of the TV speakers playing the sound.

**Verification status:** Built from vendor documentation and community reports (linked at the bottom). Not yet confirmed on the 75QNED916QE. Menu labels differ between firmware versions.

## The signal chain

```
Apple TV 4K --HDMI--> LG TV (any HDMI input) --eARC port--> Soundbar
```

The soundbar must sit on the TV port that is labelled eARC (some LG models label it eARC/ARC). The Apple TV goes into any other HDMI input. Community reports say Atmos from an Apple TV 4K does not pass over plain ARC, so eARC is the safe route.

Connecting the soundbar to the Apple TV over Bluetooth cannot carry Dolby Atmos. That is why the HDMI route matters.

## Soundbars without an HDMI input (example: Samsung HW-S60D)

Some soundbars have only one HDMI output (eARC) and no HDMI input. According to retailer spec sheets this is the case for the Samsung HW-S60D, which also lists an optical input. Such a bar cannot take the Apple TV directly, so the TV with eARC is the only route to Dolby Atmos:

- On the soundbar, use the HDMI OUT (TV-eARC) socket and connect it to the TV's eARC port.
- Optical (TOSLINK) cannot carry Atmos. It is fine as a fallback for stereo or Dolby Digital.
- The HW-S60D is listed as decoding Dolby Atmos, Dolby Digital Plus and Dolby TrueHD, so the bar itself is not the limit.

## What a working link looks like

On the reference TV the Home screen lists the soundbar as the audio output with the note "HDMI(ARC) device". That means the TV found the bar and uses it, but it negotiated plain ARC. For Atmos from an Apple TV 4K you want eARC. If your TV shows ARC here, check that the cable sits in the port labelled eARC and that SIMPLINK and the bar's CEC option are on.

## Setup, in this order

1. **Cabling.** Use a cable rated Ultra High Speed (HDMI 2.1) between TV and soundbar. Put nothing between them: no HDMI switch, no hub, no splitter. A device in this path is the most likely reason for "only the TV speakers work".
2. **TV sound output.** Settings, Sound, Sound Out: choose the HDMI (eARC/ARC) soundbar entry, not TV Speaker. The TV speaker setting is the default and sends no sound to the bar.
3. **TV digital output.** In the same menu, set the digital sound output to Pass Through (the label may read Auto or Bitstream on some versions). PCM downmixes and loses Atmos.
4. **HDMI-CEC.** Enable SIMPLINK (LG's name for CEC) on the TV and the matching CEC option on the soundbar (Samsung calls it Anynet+). eARC negotiation relies on it.
5. **Apple TV.** Settings, Video and Audio, Audio Format: leave Change Format off or set to Auto, and set Dolby Atmos to Auto or On. Pick the soundbar as audio output if it is listed.
6. **Power cycle once.** Switch off TV, soundbar and Apple TV, unplug the HDMI cable at the soundbar for ten seconds, plug it back in, then power on in this order: soundbar, TV, Apple TV.

## Check that Atmos arrives

- Play content that is labelled Dolby Atmos (Apple TV+ has plenty).
- The soundbar display or its app should show Dolby Atmos. Many bars show plain Dolby Digital Plus when Atmos is not arriving.
- If the soundbar shows PCM, the TV is downmixing: revisit step 3.

## Troubleshooting

| Symptom | Likely cause | What to try |
|---------|--------------|-------------|
| Sound only with TV speaker selected | Soundbar not selected in Sound Out, or eARC link not up | Step 2, then step 6 |
| No sound at all after switching to the bar | HDMI hub or switch in the path | Remove it, connect directly |
| Sound works, but no Atmos | Output set to PCM, or Apple TV set to a fixed format | Steps 3 and 5 |
| Link drops after TV standby | CEC disabled or out of sync | Step 4, then step 6 |
| Crackle or dropouts | Cable not rated for the bandwidth | Swap in an Ultra High Speed cable |

If you use an HDMI hub that sits between the sources and the TV, take it out of the audio path first and test with the Apple TV connected straight to the TV. Reintroduce the hub only afterwards, and only if it explicitly supports eARC passthrough.

Direct connection of the Apple TV to the soundbar's HDMI input is Apple's own recommendation when the bar has such an input, with the bar's HDMI output going to the TV. With a bar that has no HDMI input, this option does not exist.

## Sources

- [Apple Community: Apple TV 4K 3rd generation eARC sound issues](https://discussions.apple.com/thread/255077815)
- [Apple Community: Atmos picture and sound with a soundbar ARC output](https://discussions.apple.com/thread/253411757)
- [Samsung: eARC on your Samsung TV and soundbar](https://ushl.samsung.com/us/support/answer/ANS10006962)
- [Best Buy: Samsung HW-S60D specifications](https://www.bestbuy.com/site/6577565.p)
- [LG 2022 audio setup guide (Nakamichi helpdesk)](https://www.helpdesk.nakamichi-usa.com/lg-tv-2022-audio)
