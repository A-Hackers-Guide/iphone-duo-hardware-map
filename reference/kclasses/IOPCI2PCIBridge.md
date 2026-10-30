# `IOPCI2PCIBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md)
- Object size: `0x148` (328 bytes)
- Metaclass: `0xfffffe000ba18e30`; metaclass vtable `0xfffffe00083d6600`; class vtable `0xfffffe00083d5ed8`
- Registration (init): `0xfffffe000a3336a4`
- Superclasses: [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`ApplePCIEHostBridge`](ApplePCIEHostBridge.md) — `com.apple.driver.AppleEmbeddedPCIE`

## IOKit personalities that instantiate it (3)

- `IOPCI2PCIBridge-Name` in [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md): `IOProviderClass` = `IOPCIDevice`, `IONameMatch` = `pci-bridge`
- `IOPCI2PCIBridge-PCI` in [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md): `IOProviderClass` = `IOPCIDevice`, `IOPCIMatch` = `0x00261011`
- `IOPCI2PCIBridge-i386` in [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md): `IOProviderClass` = `IOPCIDevice`

## Strings in its kext that name it (3)

- `IOPCI2PCIBridge`
- `site.IOPCI2PCIBridge`
- `void IOPCI2PCIBridge::handleInterrupt(IOInterruptEventSource *, int)`
