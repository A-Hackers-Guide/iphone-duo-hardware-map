# `AppleSMCACAMDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b99b4f8`; metaclass vtable `0xfffffe00082009e0`; class vtable `0xfffffe0008200478`
- Registration (init): `0xfffffe000967f2dc`
- Superclasses: [`AppleSMCBinaryLogDriver`](AppleSMCBinaryLogDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCACAMDriver` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-acam']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-acam`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-acam.md) on `smc-acam`
- [`/arm-io/smc/iop-smc-nub/smc-acam`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-acam.md) on `smc-acam`

## Strings in its kext that name it (5)

- `virtual bool AppleSMCACAMDriver::start(IOService *)`
- `AppleSMCACAMDriver`
- `AppleSMCACAMDriver.cpp`
- `site.AppleSMCACAMDriver`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp`
