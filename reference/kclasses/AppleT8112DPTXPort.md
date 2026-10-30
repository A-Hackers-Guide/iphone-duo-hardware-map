# `AppleT8112DPTXPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x390` (912 bytes)
- Metaclass: `0xfffffe000b941288`; metaclass vtable `0xfffffe0008057728`; class vtable `0xfffffe0008056c38`
- Registration (init): `0xfffffe0008b92b30`
- Superclasses: [`AppleDPTXPort`](AppleDPTXPort.md) → [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 5 in total)

- [`AppleT602XDPTXPort`](AppleT602XDPTXPort.md) — `com.apple.driver.AppleDisplayCrossbar`
- [`AppleT8122DPTXPort`](AppleT8122DPTXPort.md) — `com.apple.driver.AppleDisplayCrossbar`

## IOKit personalities that instantiate it (1)

- `AppleT8112DPTXPort` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['dptx-phy,t8112']`

## Strings in its kext that name it (3)

- `AppleT8112DPTXPort`
- `AppleT8112DPTXPort.cpp`
- `site.AppleT8112DPTXPort`
