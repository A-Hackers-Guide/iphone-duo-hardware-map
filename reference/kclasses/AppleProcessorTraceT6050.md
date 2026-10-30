# `AppleProcessorTraceT6050`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x708` (1,800 bytes)
- Metaclass: `0xfffffe000b993848`; metaclass vtable `0xfffffe00081bc968`; class vtable `0xfffffe00081bc358`
- Registration (init): `0xfffffe0009459aec`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT6050` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6050`

## Strings in its kext that name it (6)

- `virtual void AppleProcessorTraceT6050::defeatureCore(bool)`
- `site.AppleProcessorTraceT6050`
- `AppleProcessorTraceT6050`
- `void AppleProcessorTraceT6050::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `uint64_t AppleProcessorTraceT6050::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6050::getChunkForCluster(unsigned int, uint64_t)`
