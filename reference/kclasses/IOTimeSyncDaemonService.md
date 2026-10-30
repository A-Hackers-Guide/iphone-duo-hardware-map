# `IOTimeSyncDaemonService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.plugin.IOgPTPPlugin`](../kexts/com.apple.plugin.IOgPTPPlugin.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000ba210b0`; metaclass vtable `0xfffffe000847cfc0`; class vtable `0xfffffe000847ca60`
- Registration (init): `0xfffffe000a8960e0`
- Superclasses: [`IOTimeSyncDaemonServiceBase`](IOTimeSyncDaemonServiceBase.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOTimeSyncDaemonService` in [`com.apple.plugin.IOgPTPPlugin`](../kexts/com.apple.plugin.IOgPTPPlugin.md): `IOProviderClass` = `IOTimeSyncRootService`, `IOMatchCategory` = `IOTimeSyncDaemonService`, `IOProbeScore` = `0`

## Strings in its kext that name it (10)

- `IOTimeSyncDaemonServiceProcess`
- `site.IOTimeSyncDaemonServiceProcess`
- `IOTimeSyncDaemonService`
- `NULL == fIOTimeSyncDaemonService`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOgPTPPlugin/IOTimeSyncDaemonService.cpp`
- `site.IOTimeSyncDaemonService`
- `IOTimeSyncDaemonService::deregisterProcess %d\n`
- `IOTimeSyncDaemonService::processWatchdogTimerFire failed to remove dead process\n`
- `IOTimeSyncDaemonService::registerProcess %d\n`
- `provider is not an fIOTimeSyncDaemonService\n`
