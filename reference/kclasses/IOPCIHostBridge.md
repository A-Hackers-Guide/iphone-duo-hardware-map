# `IOPCIHostBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba18de0`; metaclass vtable `0xfffffe00083d5638`; class vtable `0xfffffe00083d4f20`
- Registration (init): `0xfffffe000a333634`
- Superclasses: [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 4 in total)

- [`AppleEmbeddedPCIE`](AppleEmbeddedPCIE.md) — `com.apple.driver.AppleEmbeddedPCIE`

## Strings in its kext that name it (7)

- `IOPCIHostBridgeData`
- `site.IOPCIHostBridge`
- `IOPCIHostBridge`
- `site.IOPCIHostBridgeData`
- `virtual IOReturn IOPCIHostBridgeData::powerStateDidChangeTo(IOPMPowerFlags, unsigned long, IOService *)`
- `IOReturn IOPCIHostBridgeData::removePCIEPowerChild(IOPowerConnection *)`
- `IOReturn IOPCIHostBridgeData::addPCIEPowerChild(IOService *)`
