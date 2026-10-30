# `AppleTCControllerType12`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1118` (4,376 bytes)
- Metaclass: `0xfffffe000b94ef50`; metaclass vtable `0xfffffe00080fd2e0`; class vtable `0xfffffe00080fc820`
- Registration (init): `0xfffffe0008f89200`
- Superclasses: [`AppleTCControllerType10`](AppleTCControllerType10.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCControllerType12` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDevice`

## Strings in its kext that name it (5)

- `%s::%s(0x%x@0x%x): AppleTCControllerType12::createUSB3PortObject(@0x%x) - creating usb3 port object tunnelAdapterType=%d\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::start - Overriding mux settings 0x%x\n\n`
- `AppleTCControllerType12`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::start - Overriding USB3 settings 0x%x\n\n`
- `site.AppleTCControllerType12`
