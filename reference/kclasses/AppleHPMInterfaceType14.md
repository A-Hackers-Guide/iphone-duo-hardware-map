# `AppleHPMInterfaceType14`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14b0` (5,296 bytes)
- Metaclass: `0xfffffe000b94ed70`; metaclass vtable `0xfffffe00080f6c70`; class vtable `0xfffffe00080f6118`
- Registration (init): `0xfffffe0008f7d448`
- Superclasses: [`AppleHPMInterfaceType10`](AppleHPMInterfaceType10.md) → [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType14` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (7)

- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::start\n\n`
- `site.AppleHPMInterfaceType14`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `AppleHPMInterfaceType14`
