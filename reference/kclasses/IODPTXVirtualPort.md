# `IODPTXVirtualPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md)
- Object size: `0x270` (624 bytes)
- Metaclass: `0xfffffe000b9f38c0`; metaclass vtable `0xfffffe0008363060`; class vtable `0xfffffe00083626c8`
- Registration (init): `0xfffffe000a0af534`
- Superclasses: [`IODPTXPort`](IODPTXPort.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IODPTXVirtualPort` in [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['AAPL,atc-dpphy', 'AAPL,atc-dpin', 'AAPL,dptx-phy']`, `IOPropertyMatch` = `{'VirtualMode': 1}`, `IOProbeScore` = `1000000`

## Strings in its kext that name it (3)

- `IODPTXVirtualPort.cpp`
- `site.IODPTXVirtualPort`
- `IODPTXVirtualPort`
