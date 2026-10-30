# `AppleProcessorTraceT6030`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9937d0`; metaclass vtable `0xfffffe00081bba60`; class vtable `0xfffffe00081bb450`
- Registration (init): `0xfffffe0009452494`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT6030` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6030`

## Strings in its kext that name it (9)

- `virtual bool AppleProcessorTraceT6030::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT6030::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6030::stopTracingOnCluster(bool)`
- `site.AppleProcessorTraceT6030`
- `virtual void AppleProcessorTraceT6030::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT6030::unconfigureCluster(bool)`
- `AppleProcessorTraceT6030`
- `virtual void AppleProcessorTraceT6030::refeatureCore(bool)`
- `virtual void AppleProcessorTraceT6030::unconfigureCore(bool)`
