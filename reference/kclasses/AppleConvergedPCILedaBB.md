# `AppleConvergedPCILedaBB`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md)
- Object size: `0x3c8` (968 bytes)
- Metaclass: `0xfffffe000b93b6b0`; metaclass vtable `0xfffffe000803a968`; class vtable `0xfffffe000803a228`
- Registration (init): `0xfffffe0008b31560`
- Superclasses: [`AppleConvergedPCIBB`](AppleConvergedPCIBB.md) → [`IOAppleConvergedPCI`](IOAppleConvergedPCI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleConvergedPCILedaBB` in [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md): `IOProviderClass` = `IOPCIDevice`, `IONameMatch` = `['baseband-pcie-leda', 'pci106b,1c04', 'baseband-pcie-pandia']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) on `baseband-pcie-leda`

## Strings in its kext that name it (2)

- `AppleConvergedPCILedaBB`
- `site.AppleConvergedPCILedaBB`
