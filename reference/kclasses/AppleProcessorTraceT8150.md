# `AppleProcessorTraceT8150`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b9932b0`; metaclass vtable `0xfffffe00081b6450`; class vtable `0xfffffe00081b5e40`
- Registration (init): `0xfffffe0009433228`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8150` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8150`

## Strings in its kext that name it (6)

- `site.AppleProcessorTraceT8150`
- `virtual void AppleProcessorTraceT8150::defeatureCore(bool)`
- `AppleProcessorTraceT8150`
- `uint64_t AppleProcessorTraceT8150::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `void AppleProcessorTraceT8150::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8150::getChunkForCluster(unsigned int, uint64_t)`
