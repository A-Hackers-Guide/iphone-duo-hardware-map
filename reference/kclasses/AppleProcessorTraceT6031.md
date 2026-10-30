# `AppleProcessorTraceT6031`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x288` (648 bytes)
- Metaclass: `0xfffffe000b993708`; metaclass vtable `0xfffffe00081ba378`; class vtable `0xfffffe00081b9d68`
- Registration (init): `0xfffffe000944c158`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT6031` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6031`

## Strings in its kext that name it (9)

- `virtual void AppleProcessorTraceT6031::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT6031::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT6031::refeatureCore(bool)`
- `virtual void AppleProcessorTraceT6031::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6031::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT6031::defeatureCore(bool)`
- `AppleProcessorTraceT6031`
- `virtual bool AppleProcessorTraceT6031::getTracePowerStateForCluster(bool)`
- `site.AppleProcessorTraceT6031`
