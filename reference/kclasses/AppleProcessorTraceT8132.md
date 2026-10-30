# `AppleProcessorTraceT8132`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2b8` (696 bytes)
- Metaclass: `0xfffffe000b993300`; metaclass vtable `0xfffffe00081b71a0`; class vtable `0xfffffe00081b6b90`
- Registration (init): `0xfffffe000943899c`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8132` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8132`

## Strings in its kext that name it (6)

- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8132::getChunkForCluster(unsigned int, uint64_t)`
- `virtual void AppleProcessorTraceT8132::defeatureCore(bool)`
- `uint64_t AppleProcessorTraceT8132::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `AppleProcessorTraceT8132`
- `void AppleProcessorTraceT8132::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `site.AppleProcessorTraceT8132`
