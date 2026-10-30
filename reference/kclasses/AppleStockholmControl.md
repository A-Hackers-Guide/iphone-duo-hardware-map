# `AppleStockholmControl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b9a5018`; metaclass vtable `0xfffffe0008237c88`; class vtable `0xfffffe00082376e8`
- Registration (init): `0xfffffe000977db90`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleHammerfestControl` in [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md): `IOProviderClass` = `IOService`, `IONameMatch` = `nfc,secondary,gpio`, `IOMatchCategory` = `AppleStockholmControl`
- `AppleStockholmControl` in [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md): `IOProviderClass` = `IOService`, `IONameMatch` = `nfc,primary,gpio`, `IOMatchCategory` = `AppleStockholmControl`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) on `nfc,primary,gpio`
- [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) on `nfc,secondary,gpio`

## Strings in its kext that name it (16)

- `AppleStockholmControlSPMIErrorTimeStamp`
- `AppleStockholmControlSPMIError`
- `AppleStockholmControlConfig`
- `AppleStockholmControlUserClient`
- `[%llu] ERR: %s::%s:%d Failed to create AppleStockholmControlConfig`
- `ERR: %s::%s:%d failed to attach AppleStockholmControlConfig\n`
- `AppleStockholmControl`
- `[%llu] ERR: %s::%s:%d failed to attach AppleStockholmControlConfig`
- `[%llu] ERR: %s::%s:%d failed starting AppleStockholmControlConfig`
- `ERR: %s::%s:%d failed starting AppleStockholmControlConfig\n`
- `[%llu] ERR: %s::%s:%d Failed to init AppleStockholmControlConfig`
- `site.AppleStockholmControlConfig`
- `site.AppleStockholmControlUserClient`
- `ERR: %s::%s:%d Failed to init AppleStockholmControlConfig\n`
- `ERR: %s::%s:%d Failed to create AppleStockholmControlConfig\n`
- `site.AppleStockholmControl`
