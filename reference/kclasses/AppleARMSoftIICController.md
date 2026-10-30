# `AppleARMSoftIICController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9346c0`; metaclass vtable `0xfffffe0007fbf500`; class vtable `0xfffffe0007fbef08`
- Registration (init): `0xfffffe0008718734`
- Superclasses: [`AppleARMIICController`](AppleARMIICController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMSoftIICController` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `iic,soft`, `IOProbeScore` = `100`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) on `iic,soft`
- [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) on `iic,soft`
- [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) on `iic,soft`

## Strings in its kext that name it (2)

- `AppleARMSoftIICController`
- `site.AppleARMSoftIICController`
