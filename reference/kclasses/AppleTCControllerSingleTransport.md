# `AppleTCControllerSingleTransport`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1108` (4,360 bytes)
- Metaclass: `0xfffffe000b94eeb0`; metaclass vtable `0xfffffe00080fac50`; class vtable `0xfffffe00080fa190`
- Registration (init): `0xfffffe0008f84ad8`
- Superclasses: [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCControllerSingleTransport` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `hpmSingleTransport`

## Strings in its kext that name it (25)

- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - no interrupt source found\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - Enabling Debug, Flags = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - IONVRAM check failed\n\n`
- `site.AppleTCControllerSingleTransport`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - no interrupt source found to add\n\n`
- `AppleTCControllerSingleTransport`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::setAccessoryID(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - Interrupt added to workloop\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Failed to find Bus Controller, trying older method\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - No gpio function\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - Pins will be set in the upsidedown orientation.\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Super failed to start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Warning: No I2C Interface\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Failed to get workloop\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - failed to match on dock\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Failed to get dockPhandle\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::evaluateHpd(0x%x) - fhpdgpio not found\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - Failed to get command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::setPinConfiguration(@0x%x) - Could not reconfigure pin configuration dictionary\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::evaluateHpd(0x%x) - HPD = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - In Restore\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::setAccessoryID(@0x%x) - Status = 0x%x accessoryID = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - In OTA\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start - Failed to get interrupt provider\n\n`
