# `AppleHPMInterfaceType3`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14b0` (5,296 bytes)
- Metaclass: `0xfffffe000b94edc0`; metaclass vtable `0xfffffe00080f7fa0`; class vtable `0xfffffe00080f7428`
- Registration (init): `0xfffffe0008f7e29c`
- Superclasses: [`AppleHPMInterfaceType1`](AppleHPMInterfaceType1.md) → [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType3` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (7)

- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `AppleHPMInterfaceType3`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `site.AppleHPMInterfaceType3`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::start\n\n`
