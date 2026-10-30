# `IOTimeSyncClockManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOTimeSyncFamily`](../kexts/com.apple.iokit.IOTimeSyncFamily.md)
- Object size: `0x148` (328 bytes)
- Metaclass: `0xfffffe000ba1ddb8`; metaclass vtable `0xfffffe0008430610`; class vtable `0xfffffe00084300b8`
- Registration (init): `0xfffffe000a5fdb7c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOTimeSyncClockManager` in [`com.apple.iokit.IOTimeSyncFamily`](../kexts/com.apple.iokit.IOTimeSyncFamily.md): `IOProviderClass` = `IOTimeSyncRootService`, `IOMatchCategory` = `IOTimeSyncClockManager`, `IOProbeScore` = `0`

## Strings in its kext that name it (27)

- `site.IOTimeSyncClockManagerUserClient`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp`
- `NULL == fIOTimeSyncClockManager`
- `IOTimeSyncClockManager`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp`
- `NULL == fIOTimeSyncClockManagerLock`
- `IOTimeSyncClockManagerUserClient`
- `site.IOTimeSyncClockManager`
- `IOTimeSyncClockManager::begin waitQuiet\n`
- `IOTimeSyncClockManager::delayedClockIDLookup registered service\n`
- `IOTimeSyncClockManager::addgPTPServices adding IOTimeSyncgPTPManager\n`
- `IOTimeSyncClockManager::addTSNCaptureServices requesting matching\n`
- `IOTimeSyncClockManager::free\n`
- `IOTimeSyncClockManager::addTSNCaptureServices adding services\n`
- `IOTimeSyncClockManager::removegPTPServices removing IOTimeSyncgPTPManager\n`
- `IOTimeSyncClockManager::stop\n`
- `IOTimeSyncClockManager::start registered service\n`
- `IOTimeSyncClockManager::start\n`
- `IOTimeSyncClockManager::matched first IONF interface\n`
- `IOTimeSyncClockManager:: Generated random clockID %llx\n`
- `provider is not an IOTimeSyncClockManager\n`
- `IOTimeSyncClockManager::end waitQuiet\n`
- `IOTimeSyncClockManager::failed delayed clock ID lookup.\n`
- `IOTimeSyncClockManager::init\n`
- `IOTimeSyncClockManagerUserClient: missing entitlement %s\n`
- `IOTimeSyncClockManager::matched first TSN interface\n`
- `IOTimeSyncClockManager::Using interface %s %s%u for identifier\n`
