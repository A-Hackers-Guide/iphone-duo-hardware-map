# `AppleT8122DPTXPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x3a8` (936 bytes)
- Metaclass: `0xfffffe000b9413f0`; metaclass vtable `0xfffffe000805bde8`; class vtable `0xfffffe000805b2f8`
- Registration (init): `0xfffffe0008b9c47c`
- Superclasses: [`AppleT8112DPTXPort`](AppleT8112DPTXPort.md) → [`AppleDPTXPort`](AppleDPTXPort.md) → [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 3 in total)

- [`AppleT8132DPTXPort`](AppleT8132DPTXPort.md) — `com.apple.driver.AppleDisplayCrossbar`
- [`AppleT8152DPTXPort`](AppleT8152DPTXPort.md) — `com.apple.driver.AppleDisplayCrossbar`

## IOKit personalities that instantiate it (1)

- `AppleT8122DPTXPort` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['dptx-phy,t8122']`

## Strings in its kext that name it (3)

- `site.AppleT8122DPTXPort`
- `AppleT8122DPTXPort.cpp`
- `AppleT8122DPTXPort`
