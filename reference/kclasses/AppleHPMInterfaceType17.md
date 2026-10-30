# `AppleHPMInterfaceType17`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14c0` (5,312 bytes)
- Metaclass: `0xfffffe000b94ef28`; metaclass vtable `0xfffffe00080fc788`; class vtable `0xfffffe00080fbc28`
- Registration (init): `0xfffffe0008f88228`
- Superclasses: [`AppleHPMInterfaceType10`](AppleHPMInterfaceType10.md) → [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType17` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (6)

- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start - Failed to get spmi provider\n\n`
- `AppleHPMInterfaceType17`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start - Failed to create interrupt source\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17:setupMatchingForUFP can't find AppleHPMInterfaceType16\n\n`
- `site.AppleHPMInterfaceType17`
