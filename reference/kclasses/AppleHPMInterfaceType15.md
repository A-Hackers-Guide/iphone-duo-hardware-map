# `AppleHPMInterfaceType15`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14b8` (5,304 bytes)
- Metaclass: `0xfffffe000b94ed48`; metaclass vtable `0xfffffe00080f6080`; class vtable `0xfffffe00080f5528`
- Registration (init): `0xfffffe0008f7ca80`
- Superclasses: [`AppleHPMInterfaceType10`](AppleHPMInterfaceType10.md) → [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType15` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (8)

- `site.AppleHPMInterfaceType15`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::repeaterReset(@0x%x) - Called with target 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `AppleHPMInterfaceType15`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
