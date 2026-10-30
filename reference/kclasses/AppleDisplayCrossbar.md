# `AppleDisplayCrossbar`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x170` (368 bytes)
- Metaclass: `0xfffffe000b941238`; metaclass vtable `0xfffffe0008055ff8`; class vtable `0xfffffe0008055900`
- Registration (init): `0xfffffe0008b8ce1c`
- Superclasses: [`IODPSwitch`](IODPSwitch.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 7 in total)

- [`AppleT600xDisplayCrossbar`](AppleT600xDisplayCrossbar.md) — `com.apple.driver.AppleDisplayCrossbar`
- [`AppleT602XDisplayCrossbar`](AppleT602XDisplayCrossbar.md) — `com.apple.driver.AppleDisplayCrossbar`
- [`AppleT8112DisplayCrossbar`](AppleT8112DisplayCrossbar.md) — `com.apple.driver.AppleDisplayCrossbar`

## IOKit personalities that instantiate it (1)

- `AppleDisplayCrossbar` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `AAPL,display-crossbar`

## Strings in its kext that name it (2)

- `site.AppleDisplayCrossbar`
- `AppleDisplayCrossbar`
