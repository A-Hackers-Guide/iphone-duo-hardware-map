# `SharedDARTMapperProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AudioSharedDARTMapperProxy`](../kexts/com.apple.driver.AudioSharedDARTMapperProxy.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000ba39b58`; metaclass vtable `0xfffffe00084a3cd0`; class vtable `0xfffffe00084a3778`
- Registration (init): `0xfffffe000a99bc0c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DeviceTreeName` in [`com.apple.driver.AudioSharedDARTMapperProxy`](../kexts/com.apple.driver.AudioSharedDARTMapperProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['audio-shared-dart-proxy']`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) on `audio-shared-dart-proxy`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/SharedDARTMapper/Proxy/Source/SharedDARTMapperProxy.cpp`
- `SharedDARTMapperProxy`
- `site.SharedDARTMapperProxy`
