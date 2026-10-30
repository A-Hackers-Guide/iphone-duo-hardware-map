# `ApplePCIEHostBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedPCIE`](../kexts/com.apple.driver.AppleEmbeddedPCIE.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b943900`; metaclass vtable `0xfffffe0008089ff0`; class vtable `0xfffffe00080898c8`
- Registration (init): `0xfffffe0008c78644`
- Superclasses: [`IOPCI2PCIBridge`](IOPCI2PCIBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`APCIECoreRCGen5p1HostBridge`](APCIECoreRCGen5p1HostBridge.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (4)

- `ApplePCIEHostBridge`
- `site.ApplePCIEHostBridge`
- `virtual IOService *ApplePCIEHostBridge::probe(IOService *, SInt32 *)`
- `ApplePCIEHostBridge.cpp`
