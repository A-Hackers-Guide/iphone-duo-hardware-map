# `AppleProcessorTraceT8120`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b993780`; metaclass vtable `0xfffffe00081bb250`; class vtable `0xfffffe00081bac40`
- Registration (init): `0xfffffe000944fc50`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8120` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8120`

## Strings in its kext that name it (9)

- `virtual void AppleProcessorTraceT8120::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8120::refeatureCore(bool)`
- `site.AppleProcessorTraceT8120`
- `virtual bool AppleProcessorTraceT8120::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8120::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8120::unconfigureCluster(bool)`
- `AppleProcessorTraceT8120`
- `virtual void AppleProcessorTraceT8120::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8120::defeatureCore(bool)`
