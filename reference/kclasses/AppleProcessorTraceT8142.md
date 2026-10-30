# `AppleProcessorTraceT8142`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b9933a0`; metaclass vtable `0xfffffe00081b8b88`; class vtable `0xfffffe00081b8578`
- Registration (init): `0xfffffe0009440670`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8142` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8142`

## Strings in its kext that name it (6)

- `void AppleProcessorTraceT8142::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `uint64_t AppleProcessorTraceT8142::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `virtual void AppleProcessorTraceT8142::defeatureCore(bool)`
- `site.AppleProcessorTraceT8142`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8142::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT8142`
