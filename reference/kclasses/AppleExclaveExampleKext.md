# `AppleExclaveExampleKext`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.ExclaveKextClient`](../kexts/com.apple.ExclaveKextClient.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9e0360`; metaclass vtable `0xfffffe00082df698`; class vtable `0xfffffe00082df140`
- Registration (init): `0xfffffe0009c5f7c8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DeviceTreeName` in [`com.apple.ExclaveKextClient`](../kexts/com.apple.ExclaveKextClient.md): `IOProviderClass` = `IOService`, `IONameMatch` = `exclaves-test`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (2) [DT]

- [`/exclaves-test`](../devicetree/root__exclaves-test.md) on `exclaves-test`
- [`/exclaves-test`](../devicetree/root__exclaves-test.md) on `exclaves-test`

## Strings in its kext that name it (10)

- `site.AppleExclaveExampleKext`
- `AppleExclaveExampleKext.cpp`
- `AppleExclaveExampleKext received async notification\n`
- `AppleExclaveExampleKextResult`
- `AppleExclaveExampleKext`
- `AppleExclaveExampleKext does not have a workloop\n`
- `AppleExclaveExampleKext result:%d\n`
- `site.AppleExclaveExampleKextUserClient`
- `AppleExclaveExampleKextUserClient`
- `AppleExclaveExampleKext_tightbeam.c`
