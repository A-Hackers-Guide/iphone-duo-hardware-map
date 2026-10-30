# `AppleProcessorTraceT8112`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b993910`; metaclass vtable `0xfffffe00081bee28`; class vtable `0xfffffe00081be818`
- Registration (init): `0xfffffe0009465138`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8112` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8112`

## Strings in its kext that name it (9)

- `site.AppleProcessorTraceT8112`
- `virtual void AppleProcessorTraceT8112::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8112::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8112::unconfigureCluster(bool)`
- `AppleProcessorTraceT8112`
- `virtual void AppleProcessorTraceT8112::refeatureCore(bool)`
- `virtual bool AppleProcessorTraceT8112::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8112::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8112::unconfigureCore(bool)`
