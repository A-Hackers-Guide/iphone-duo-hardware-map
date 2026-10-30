# `AppleProcessorTraceBringUp`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b993960`; metaclass vtable `0xfffffe00081bfb78`; class vtable `0xfffffe00081bf568`
- Registration (init): `0xfffffe0009468a60`
- Superclasses: [`AppleProcessorTrace`](AppleProcessorTrace.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProcessorTraceBringUp` in [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apple-processor-trace,bring-up`

## Strings in its kext that name it (2)

- `AppleProcessorTraceBringUp`
- `site.AppleProcessorTraceBringUp`
