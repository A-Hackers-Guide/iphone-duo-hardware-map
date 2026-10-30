# `IOTimeSyncService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOTimeSyncFamily`](../kexts/com.apple.iokit.IOTimeSyncFamily.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000ba1e018`; metaclass vtable `0xfffffe0008434648`; class vtable `0xfffffe0008434078`
- Registration (init): `0xfffffe000a60b450`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 6 in total)

- [`IOTimeSyncDomain`](IOTimeSyncDomain.md) — `com.apple.plugin.IOgPTPPlugin`
- [`IOTimeSyncFilteredService`](IOTimeSyncFilteredService.md) — `com.apple.iokit.IOTimeSyncFamily`
- [`IOTimeSyncTranslationMach`](IOTimeSyncTranslationMach.md) — `com.apple.iokit.IOTimeSyncFamily`

## Strings in its kext that name it (12)

- `NULL == fIOTimeSyncServiceLock`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp`
- `NULL == fIOTimeSyncService`
- `site.IOTimeSyncService`
- `site.IOTimeSyncServiceDaemonClient`
- `IOTimeSyncServiceDaemonClient`
- `site.IOTimeSyncService::ExpansionData`
- `fIOTimeSyncService != nullptr`
- `IOTimeSyncService`
- `IOTimeSyncService::sendNotification: notification=%u arg0=%llu arg1=%llu`
- `IOTimeSyncService::sendGeneralSyncUpdate unknown sync client\n`
