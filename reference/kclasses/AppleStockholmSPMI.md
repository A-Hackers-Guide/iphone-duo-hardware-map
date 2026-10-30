# `AppleStockholmSPMI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md)
- Object size: `0x128` (296 bytes)
- Metaclass: `0xfffffe000b9a4fe0`; metaclass vtable `0xfffffe0008237648`; class vtable `0xfffffe00082370b8`
- Registration (init): `0xfffffe00097783fc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleHammerfestSPMI` in [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `nfc,secondary,spmi`, `IOMatchCategory` = `AppleStockholmControl`
- `AppleStockholmSPMI` in [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `nfc,primary,spmi`, `IOMatchCategory` = `AppleStockholmControl`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) on `nfc,primary,spmi`
- [`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) on `nfc,secondary,spmi`

## Strings in its kext that name it (2)

- `AppleStockholmSPMI`
- `site.AppleStockholmSPMI`
