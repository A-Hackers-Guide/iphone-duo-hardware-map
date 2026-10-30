# `AppleProcessorTraceT8103`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9939b0`; metaclass vtable `0xfffffe00081c08c8`; class vtable `0xfffffe00081c02b8`
- Registration (init): `0xfffffe000946cf20`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8103` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8103`

## Strings in its kext that name it (9)

- `virtual void AppleProcessorTraceT8103::refeatureCore(bool)`
- `AppleProcessorTraceT8103`
- `virtual void AppleProcessorTraceT8103::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8103::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8103::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8103::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8103::platformStopTracingOnCore(bool)`
- `site.AppleProcessorTraceT8103`
- `virtual bool AppleProcessorTraceT8103::getTracePowerStateForCluster(bool)`
