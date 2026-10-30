# `AppleATCDPINAdapterPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0x328` (808 bytes)
- Metaclass: `0xfffffe000b941530`; metaclass vtable `0xfffffe000805ff70`; class vtable `0xfffffe000805f588`
- Registration (init): `0xfffffe0008ba64dc`
- Superclasses: [`AppleATCDPINAdapterPortBase`](AppleATCDPINAdapterPortBase.md) → [`AppleATCDPPort`](AppleATCDPPort.md) → [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleATCDPINAdapterPort` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `AAPL,atc-dpin`

## Strings in its kext that name it (6)

- `AppleATCDPINAdapterPort.cpp`
- `AppleATCDPINAdapterPortBase.cpp`
- `AppleATCDPINAdapterPortBase`
- `AppleATCDPINAdapterPort`
- `site.AppleATCDPINAdapterPortBase`
- `site.AppleATCDPINAdapterPort`
