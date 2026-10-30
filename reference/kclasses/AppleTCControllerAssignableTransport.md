# `AppleTCControllerAssignableTransport`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x10f8` (4,344 bytes)
- Metaclass: `0xfffffe000b94f1d8`; metaclass vtable `0xfffffe0008106620`; class vtable `0xfffffe0008105b60`
- Registration (init): `0xfffffe0008faf524`
- Superclasses: [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCControllerAssignableTransport` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDevice`

## Strings in its kext that name it (9)

- `site.AppleTCControllerAssignableTransport`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::probe - matchingclass = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::configureTBTPortObject(@0x%x) - CIO already provisioned\n\n`
- `AppleTCControllerAssignableTransport`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::createUSB3PortObject(@0x%x) - creating usb3 port object tunnelAdapterType=%d\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::poweredStart(@0x%x) - start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::start(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::configureTBTPortObject(@0x%x) - Failed to activate transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerAssignableTransport::probe - failed!\n\n`
