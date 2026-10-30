# `AppleTCControllerType14`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1118` (4,376 bytes)
- Metaclass: `0xfffffe000b94eca8`; metaclass vtable `0xfffffe00080f3ec0`; class vtable `0xfffffe00080f3400`
- Registration (init): `0xfffffe0008f66f14`
- Superclasses: [`AppleTCControllerType10`](AppleTCControllerType10.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCControllerType14` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDevice`

## Strings in its kext that name it (6)

- `%s::%s(0x%x@0x%x): AppleTCControllerType14::start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::hpmInterruptAction(@0x%x) - Interrupt Recieved\n\n`
- `site.AppleTCControllerType14`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::processInterruptEvents(@0x%x) - interrupts = 0x%x 0x%x 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::processInterruptEvents(@0x%x) - Start\n\n`
- `AppleTCControllerType14`
