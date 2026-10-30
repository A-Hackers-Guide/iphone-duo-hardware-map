# `AppleProcessorTraceT8101`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9939d8`; metaclass vtable `0xfffffe00081c0f70`; class vtable `0xfffffe00081c0960`
- Registration (init): `0xfffffe000946ea90`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8101` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8101`

## Strings in its kext that name it (9)

- `AppleProcessorTraceT8101`
- `virtual void AppleProcessorTraceT8101::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8101::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8101::platformStopTracingOnCore(bool)`
- `site.AppleProcessorTraceT8101`
- `virtual void AppleProcessorTraceT8101::defeatureCore(bool)`
- `virtual bool AppleProcessorTraceT8101::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8101::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8101::refeatureCore(bool)`
