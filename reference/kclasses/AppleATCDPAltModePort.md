# `AppleATCDPAltModePort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b941350`; metaclass vtable `0xfffffe0008059a00`; class vtable `0xfffffe0008059010`
- Registration (init): `0xfffffe0008b97754`
- Superclasses: [`AppleATCDPNativePort`](AppleATCDPNativePort.md) → [`AppleATCDPPort`](AppleATCDPPort.md) → [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleATCDPAltModePort` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `AAPL,atc-dpphy`, `IOPropertyMatch` = `{'port-type': '<data 22 chars>'}`

## Strings in its kext that name it (2)

- `AppleATCDPAltModePort`
- `site.AppleATCDPAltModePort`
