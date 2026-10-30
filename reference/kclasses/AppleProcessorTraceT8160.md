# `AppleProcessorTraceT8160`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b993350`; metaclass vtable `0xfffffe00081b7e38`; class vtable `0xfffffe00081b7828`
- Registration (init): `0xfffffe000943bfb0`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceT8160` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) on `apple-processor-trace,t8160`

## Strings in its kext that name it (6)

- `virtual void AppleProcessorTraceT8160::defeatureCore(bool)`
- `uint64_t AppleProcessorTraceT8160::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8160::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT8160`
- `void AppleProcessorTraceT8160::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `site.AppleProcessorTraceT8160`
