# `AppleATCDPHDMIPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x2f8` (760 bytes)
- Metaclass: `0xfffffe000b9411e8`; metaclass vtable `0xfffffe00080550b0`; class vtable `0xfffffe00080546c0`
- Registration (init): `0xfffffe0008b8994c`
- Superclasses: [`AppleATCDPNativePort`](AppleATCDPNativePort.md) → [`AppleATCDPPort`](AppleATCDPPort.md) → [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleATCDPHDMIPort` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `AAPL,atc-dpphy`, `IOPropertyMatch` = `{'port-type': '<data 22 chars>'}`

## Strings in its kext that name it (2)

- `AppleATCDPHDMIPort`
- `site.AppleATCDPHDMIPort`
