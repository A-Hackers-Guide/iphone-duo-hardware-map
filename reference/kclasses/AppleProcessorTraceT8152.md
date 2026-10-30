# `AppleProcessorTraceT8152`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b9938e8`; metaclass vtable `0xfffffe00081be780`; class vtable `0xfffffe00081be170`
- Registration (init): `0xfffffe0009462974`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8152` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8152`

## Strings in its kext that name it (6)

- `uint64_t AppleProcessorTraceT8152::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8152::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT8152`
- `virtual void AppleProcessorTraceT8152::defeatureCore(bool)`
- `site.AppleProcessorTraceT8152`
- `void AppleProcessorTraceT8152::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
