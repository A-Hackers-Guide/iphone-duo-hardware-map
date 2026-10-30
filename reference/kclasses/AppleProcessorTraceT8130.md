# `AppleProcessorTraceT8130`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b993938`; metaclass vtable `0xfffffe00081bf4d0`; class vtable `0xfffffe00081beec0`
- Registration (init): `0xfffffe00094668d0`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8130` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8130`

## Strings in its kext that name it (9)

- `site.AppleProcessorTraceT8130`
- `AppleProcessorTraceT8130`
- `virtual void AppleProcessorTraceT8130::refeatureCore(bool)`
- `virtual void AppleProcessorTraceT8130::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8130::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8130::platformStopTracingOnCore(bool)`
- `virtual bool AppleProcessorTraceT8130::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8130::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8130::stopTracingOnCluster(bool)`
