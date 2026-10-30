# `AppleARMBootPerf`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b934070`; metaclass vtable `0xfffffe0007fb42b0`; class vtable `0xfffffe0007fb3d58`
- Registration (init): `0xfffffe00086f21ec`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMBootPerf` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleARMBootPerf`

## Strings in its kext that name it (10)

- `AppleARMBootPerf: Warning: profile->magic (0x%x) != 'BTRC'\n`
- `AppleARMBootPerf: Error: failed to publish profile data (%d)\n`
- `AppleARMBootPerf: Error: profile handoff region size is 0, nothing to copy\n`
- `AppleARMBootPerf: Error: failed to publish profile data on resume (%d)\n`
- `AppleARMBootPerf: Error: profile handoff region not found (%d)\n`
- `AppleARMBootPerf`
- `AppleARMBootPerf: Warning: profile->pc_bytes (%u) is not supported\n`
- `site.AppleARMBootPerf`
- `AppleARMBootPerf: Warning: buffer size (0x%llx) is less than %lu\n`
- `AppleARMBootPerf: Warning: profile->count (%u) > maxPossibleCount (%u)\n`
