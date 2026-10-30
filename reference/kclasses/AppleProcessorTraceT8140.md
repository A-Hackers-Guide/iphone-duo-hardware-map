# `AppleProcessorTraceT8140`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2b8` (696 bytes)
- Metaclass: `0xfffffe000b993898`; metaclass vtable `0xfffffe00081bda30`; class vtable `0xfffffe00081bd420`
- Registration (init): `0xfffffe000945e488`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8140` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8140`

## Strings in its kext that name it (6)

- `AppleProcessorTraceT8140`
- `uint64_t AppleProcessorTraceT8140::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `void AppleProcessorTraceT8140::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `site.AppleProcessorTraceT8140`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8140::getChunkForCluster(unsigned int, uint64_t)`
- `virtual void AppleProcessorTraceT8140::defeatureCore(bool)`
