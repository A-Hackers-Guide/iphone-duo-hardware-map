# `AppleProcessorTraceT8310`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9938c0`; metaclass vtable `0xfffffe00081be0d8`; class vtable `0xfffffe00081bdac8`
- Registration (init): `0xfffffe00094609b8`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8310` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8310`

## Strings in its kext that name it (9)

- `virtual void AppleProcessorTraceT8310::unconfigureCluster(bool)`
- `AppleProcessorTraceT8310`
- `virtual void AppleProcessorTraceT8310::unconfigureCore(bool)`
- `site.AppleProcessorTraceT8310`
- `virtual void AppleProcessorTraceT8310::stopTracingOnCluster(bool)`
- `virtual bool AppleProcessorTraceT8310::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8310::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8310::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8310::refeatureCore(bool)`
