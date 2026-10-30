# `AppleConvergedPCIICEBB`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md)
- Object size: `0x3c0` (960 bytes)
- Metaclass: `0xfffffe000b93b570`; metaclass vtable `0xfffffe0008034518`; class vtable `0xfffffe0008033df8`
- Registration (init): `0xfffffe0008b22298`
- Superclasses: [`AppleConvergedPCIBB`](AppleConvergedPCIBB.md) → [`IOAppleConvergedPCI`](IOAppleConvergedPCI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleConvergedPCIICEBB` in [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md): `IOProviderClass` = `IOPCIDevice`, `IONameMatch` = `['baseband-pcie', 'pci8086,7660']`, `IOMatchCategory` = `AppleConvergedPCIICEBB`

## Strings in its kext that name it (4)

- `site.AppleConvergedPCIICEBB`
- `AppleConvergedPCIICEBB`
- `AppleConvergedPCIICEBB::probe ok\n`
- `AppleConvergedPCIICEBB.cpp`
