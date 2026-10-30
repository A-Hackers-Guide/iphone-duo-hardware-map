# `AppleProcessorTraceT6040`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x3a8` (936 bytes)
- Metaclass: `0xfffffe000b9932d8`; metaclass vtable `0xfffffe00081b6af8`; class vtable `0xfffffe00081b64e8`
- Registration (init): `0xfffffe0009436220`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleProcessorTraceT6040` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6040`
- `AppleProcessorTraceT6041` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t6040`

## Strings in its kext that name it (6)

- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6040::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT6040`
- `site.AppleProcessorTraceT6040`
- `virtual void AppleProcessorTraceT6040::defeatureCore(bool)`
- `uint64_t AppleProcessorTraceT6040::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `void AppleProcessorTraceT6040::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
