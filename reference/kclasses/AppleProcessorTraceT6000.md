# `AppleProcessorTraceT6000`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x288` (648 bytes)
- Metaclass: `0xfffffe000b993378`; metaclass vtable `0xfffffe00081b84e0`; class vtable `0xfffffe00081b7ed0`
- Registration (init): `0xfffffe00094403c0`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT6000` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6000`

## Strings in its kext that name it (9)

- `AppleProcessorTraceT6000`
- `site.AppleProcessorTraceT6000`
- `virtual void AppleProcessorTraceT6000::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT6000::unconfigureCluster(bool)`
- `virtual bool AppleProcessorTraceT6000::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT6000::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT6000::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6000::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT6000::refeatureCore(bool)`
