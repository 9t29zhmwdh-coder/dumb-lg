# Network isolation

Goal: the TV cannot send data out or be reached from other devices.

**Verification status:** Concept guide, generic by design. Exact menu paths of your router are not covered.

## Option A: no network at all (recommended)

A TV used only as a display needs no network. Do not connect it to Wi-Fi, do not plug in an Ethernet cable, and skip every network step in the first setup.

What you lose: firmware updates, built-in apps (intended), casting to the TV over the network. What keeps working: everything over HDMI, including HDMI-CEC power control and eARC audio.

Trade-off: no security updates. With no network connection there is also no remote attack surface, which outweighs the missing patches for a display.

## Option B: isolated VLAN

Use this if the TV must be on the network, for example when its Wi-Fi cannot be disabled during setup.

1. Create a separate network (VLAN) for the TV.
2. Add a firewall rule that blocks traffic from that network to the internet.
3. Add a firewall rule that blocks traffic from that network to your other internal networks.
4. Allow only what you need, usually nothing.
5. Check the router's client list to confirm the TV sits in the isolated network and shows no outbound connections.

The same ideas apply to any router with VLAN and firewall support, including UniFi.

## Verification

- Open the TV's network status and confirm it reports no internet connection.
- Watch your router's logs for DNS requests from the TV for a day. A silent TV means the isolation holds.
