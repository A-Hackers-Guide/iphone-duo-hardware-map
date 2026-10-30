# `ApplePCIePIODMA`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePCIePIODMAGen3p0`](../kexts/com.apple.driver.ApplePCIePIODMAGen3p0.md)
- Object size: `0x180` (384 bytes)
- Metaclass: `0xfffffe000b987160`; metaclass vtable `0xfffffe0008188628`; class vtable `0xfffffe0008188030`
- Registration (init): `0xfffffe00092f404c`
- Superclasses: [`ApplePIODMA`](ApplePIODMA.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePCIePIODMAGen3p0` in [`com.apple.driver.ApplePCIePIODMAGen3p0`](../kexts/com.apple.driver.ApplePCIePIODMAGen3p0.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pcie-apiodma,gen3p0`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) on `pcie-apiodma,gen3p0`
- [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) on `pcie-apiodma,gen3p0`

## Strings in its kext that name it (6)

- `virtual void ApplePCIePIODMA::_applyTunablesFromData(const OSData *, regRead_t, regWrite_t, const char *)`
- `site.ApplePCIePIODMA`
- `ApplePCIePIODMA.cpp`
- `ApplePCIePIODMA`
- `virtual bool ApplePCIePIODMA::start(IOService *)`
- `uint8_t ApplePCIePIODMA::getBaseAddressRegisterIndex(IOByteCount)`
