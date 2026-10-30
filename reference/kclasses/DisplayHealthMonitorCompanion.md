# `DisplayHealthMonitorCompanion`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DisplayHealthMonitorCompanion`](../kexts/com.apple.driver.DisplayHealthMonitorCompanion.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b9dfe18`; metaclass vtable `0xfffffe00082db1e8`; class vtable `0xfffffe00082dac90`
- Registration (init): `0xfffffe0009c39f78`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DeviceTreeName` in [`com.apple.driver.DisplayHealthMonitorCompanion`](../kexts/com.apple.driver.DisplayHealthMonitorCompanion.md): `IOProviderClass` = `IOService`, `IONameMatch` = `display-health-monitor`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/display-health-monitor`](../devicetree/root__display-health-monitor.md) on `display-health-monitor`

## Strings in its kext that name it (18)

- `DisplayHealthMonitorCompanion::start: IOService::start failed\n`
- `DisplayHealthMonitorCompanion`
- `DisplayHealthMonitorCompanion::logHealthCheck: display=%llu powerMask=%llu | globalHealth=%llu periodicHealthCheck=%llu failureRatio=%llu%%\n`
- `DisplayHealthMonitorCompanion::start: startTightbeam failed\n`
- `DisplayHealthMonitorCompanion::initTightbeam: tb_endpoint_create_with_value failed\n`
- `DisplayHealthMonitorCompanion::loggingTimerFired: snapshot failed (%u)\n`
- `DisplayHealthMonitorCompanion::initTightbeam: exclaveStart failed\n`
- `DisplayHealthMonitorCompanion: CoreAnalyticsSendEvent failed (display=%llu, powerMask=%llu, err=%d)\n`
- `DisplayHealthMonitorCompanionInterface_c.c`
- `DisplayHealthMonitorCompanion::initTightbeam: Companion interface init error (%u)\n`
- `site.DisplayHealthMonitorCompanion`
- `DisplayHealthMonitorCompanion::start: startCoreAnalyticsTimer failed\n`
- `DisplayHealthMonitorCompanion::startLoggingTimer: failed to create timer\n`
- `DisplayHealthMonitorCompanion: logging enabled with interval %u seconds (boot-arg)\n`
- `DisplayHealthMonitorCompanion::coreAnalyticsTimerFired: snapshot failed (%u)\n`
- `DisplayHealthMonitorCompanion: CoreAnalytics interval overridden to %u seconds (boot-arg)\n`
- `DisplayHealthMonitorCompanion::init: IOService::init failed\n`
- `DisplayHealthMonitorCompanion::startCoreAnalyticsTimer: failed to create timer\n`
