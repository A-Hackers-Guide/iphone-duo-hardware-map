# `AppleProcessorTraceT6020`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x288` (648 bytes)
- Metaclass: `0xfffffe000b993730`; metaclass vtable `0xfffffe00081baa20`; class vtable `0xfffffe00081ba410`
- Registration (init): `0xfffffe000944dfdc`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT6020` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6020`

## Strings in its kext that name it (9)

- `virtual bool AppleProcessorTraceT6020::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT6020::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6020::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT6020::refeatureCore(bool)`
- `virtual void AppleProcessorTraceT6020::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT6020::defeatureCore(bool)`
- `site.AppleProcessorTraceT6020`
- `AppleProcessorTraceT6020`
- `virtual void AppleProcessorTraceT6020::unconfigureCluster(bool)`
