# `AppleT8112DisplayCrossbar`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x170` (368 bytes)
- Metaclass: `0xfffffe000b941490`; metaclass vtable `0xfffffe000805da80`; class vtable `0xfffffe000805d388`
- Registration (init): `0xfffffe0008b9e2c0`
- Superclasses: [`AppleDisplayCrossbar`](AppleDisplayCrossbar.md) → [`IODPSwitch`](IODPSwitch.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8112DisplayCrossbar` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `display-crossbar,t8112`, `IOProbeScore` = `100000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) on `display-crossbar,t8112`

## Strings in its kext that name it (2)

- `site.AppleT8112DisplayCrossbar`
- `AppleT8112DisplayCrossbar`
