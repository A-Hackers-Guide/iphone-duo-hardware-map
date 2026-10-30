# `APCIECoreRCGen5PLCE`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b9d0c20`; metaclass vtable `0xfffffe0008265f30`; class vtable `0xfffffe0008265958`
- Registration (init): `0xfffffe0009890b44`
- Superclasses: [`ApplePLCE`](ApplePLCE.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `APCIECoreRCGen5PLCE` in [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `plce,t8160`, `IOProbeScore` = `5000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) on `plce,t8160`
- [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) on `plce,t8160`

## Strings in its kext that name it (16)

- `virtual uint32_t APCIECoreRCGen5PLCE::readScratchRegister(unsigned int)`
- `virtual void APCIECoreRCGen5PLCE::writeScriptRun(unsigned int, uint32_t)`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`
- `virtual void APCIECoreRCGen5PLCE::writeScriptDone(unsigned int, uint32_t)`
- `site.APCIECoreRCGen5PLCE`
- `virtual void APCIECoreRCGen5PLCE::writeScratchRegister(unsigned int, uint32_t)`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptDone(unsigned int)`
- `virtual bool APCIECoreRCGen5PLCE::start(IOService *)`
- `virtual uint64_t APCIECoreRCGen5PLCE::getScratchPhysAddr(unsigned int)`
- `APCIECoreRCGen5PLCE.cpp`
- `virtual uint32_t APCIECoreRCGen5PLCE::readErrorStatus(unsigned int)`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptRun(unsigned int)`
- `APCIECoreRCGen5PLCE`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`
