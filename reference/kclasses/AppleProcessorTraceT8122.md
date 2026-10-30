# `AppleProcessorTraceT8122`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b993820`; metaclass vtable `0xfffffe00081bc2c0`; class vtable `0xfffffe00081bbcb0`
- Registration (init): `0xfffffe0009457a44`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8122` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8122`

## Strings in its kext that name it (9)

- `virtual void AppleProcessorTraceT8122::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8122::refeatureCore(bool)`
- `site.AppleProcessorTraceT8122`
- `virtual bool AppleProcessorTraceT8122::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8122::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8122::unconfigureCluster(bool)`
- `AppleProcessorTraceT8122`
- `virtual void AppleProcessorTraceT8122::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8122::unconfigureCore(bool)`
