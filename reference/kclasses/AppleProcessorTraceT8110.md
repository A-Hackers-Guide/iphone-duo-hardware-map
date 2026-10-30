# `AppleProcessorTraceT8110`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9933c8`; metaclass vtable `0xfffffe00081b9230`; class vtable `0xfffffe00081b8c20`
- Registration (init): `0xfffffe0009442d84`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8110` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8110`

## Strings in its kext that name it (9)

- `virtual bool AppleProcessorTraceT8110::getTracePowerStateForCluster(bool)`
- `site.AppleProcessorTraceT8110`
- `virtual void AppleProcessorTraceT8110::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8110::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8110::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8110::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8110::refeatureCore(bool)`
- `AppleProcessorTraceT8110`
- `virtual void AppleProcessorTraceT8110::defeatureCore(bool)`
