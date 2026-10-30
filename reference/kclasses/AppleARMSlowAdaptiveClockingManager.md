# `AppleARMSlowAdaptiveClockingManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b934b00`; metaclass vtable `0xfffffe0007fc5d48`; class vtable `0xfffffe0007fc5790`
- Registration (init): `0xfffffe0008733804`
- Superclasses: [`IOSlowAdaptiveClockingManager`](IOSlowAdaptiveClockingManager.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMSlowAdaptiveClockingManager` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `sacm`

## Device-tree nodes it binds (2) [DT]

- [`/sacm-general`](../devicetree/root__sacm-general.md) on `sacm`
- [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) on `sacm`

## Strings in its kext that name it (4)

- `AppleARMSlowAdaptiveClockingManager`
- `AppleARMSlowAdaptiveClockingManager::newUserClient - Creating a %s\n`
- `AppleARMSlowAdaptiveClockingManager::newUserClient - ERROR - unsupported UserClient type\n`
- `site.AppleARMSlowAdaptiveClockingManager`
