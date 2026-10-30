# `AppleCentauriManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b93af20`; metaclass vtable `0xfffffe0008025be0`; class vtable `0xfffffe0008025668`
- Registration (init): `0xfffffe0008aeb818`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleCentauriManagerBuiltInMatch` in [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md): `IOProviderClass` = `IOPCIDevice`, `IOMatchCategory` = `com.apple.driver.AppleCentauriManager`
- `AppleCentauriManagerPCIMatch` in [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md): `IOProviderClass` = `IOPCIDevice`, `IOPCIMatch` = `0x1900106b`, `IOMatchCategory` = `com.apple.driver.AppleCentauriManager`
- `AppleCentauriManagerProtiumMatch` in [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md): `IOProviderClass` = `IOPCIDevice`, `IOMatchCategory` = `com.apple.driver.AppleCentauriManager`

## Strings in its kext that name it (21)

- `site.AppleCentauriManagerHelper`
- `AppleCentauriManagerHelper`
- `\"(*outMetadata)->setObject(kAppleCentauriManagerSACFunctionProperty, fSlowAdaptiveClockingFunction ? kOSBooleanTrue : kOSBooleanFalse)\" @%s:%d`
- `com.apple.driver.AppleCentauriManager.recovery`
- `site.AppleCentauriManagerLogger`
- `com.apple.driver.AppleCentauriManager`
- `site.AppleCentauriManager`
- `\"AppleCentauriManager: Dext crashed for pci device %s\" @%s:%d`
- `AppleCentauriManagerUserClient`
- `AppleCentauriManagerUSBController.cpp`
- `AppleCentauriManager.cpp`
- `%s::%s: AppleCentauriManagerHelper %s started, ret = %x \n`
- `AppleCentauriManagerLogger`
- `AppleCentauriManagerUSBController`
- `/Library/Caches/com.apple.xbs/EDF630A9-DA40-4C40-85DB-22132A13777B/TemporaryDirectory.D5OprX/Sources/AppleCentauri_kexts/AppleCentauriManager/AppleCentauriManagerLogger.cpp`
- `AppleCentauriManager`
- `%s::%s: AppleCentauriManager %s started, ret = %x \n`
- `site.AppleCentauriManagerUSBController`
- `AppleCentauriManagerHelper.cpp`
- `\"(*outMetadata)->setObject(kAppleCentauriManagerDextRelaunchProperty, relaunchReason)\" @%s:%d`
- `site.AppleCentauriManagerUserClient`
