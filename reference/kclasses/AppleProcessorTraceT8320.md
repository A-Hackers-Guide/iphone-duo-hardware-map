# `AppleProcessorTraceT8320`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x1e0` (480 bytes)
- Metaclass: `0xfffffe000b993988`; metaclass vtable `0xfffffe00081c0220`; class vtable `0xfffffe00081bfc10`
- Registration (init): `0xfffffe0009468d0c`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8320` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8320`

## Strings in its kext that name it (6)

- `AppleProcessorTraceT8320`
- `site.AppleProcessorTraceT8320`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8320::getChunkForCluster(unsigned int, uint64_t)`
- `uint64_t AppleProcessorTraceT8320::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `void AppleProcessorTraceT8320::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual void AppleProcessorTraceT8320::defeatureCore(bool)`
