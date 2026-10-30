# `IISAudioIsolatedStreamECProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b9ef558`; metaclass vtable `0xfffffe00082fa370`; class vtable `0xfffffe00082f9e10`
- Registration (init): `0xfffffe0009eb085c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IISAudioIsolatedStreamECProxy` in [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['iisaudio,isolated-stream-proxy']`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/audio-sllb-proxy`](../devicetree/root__arm-io__audio-sllb-proxy.md) on `iisaudio,isolated-stream-proxy`
- [`/arm-io/audio-hp-proxy`](../devicetree/root__arm-io__audio-hp-proxy.md) on `iisaudio,isolated-stream-proxy`

## Strings in its kext that name it (3)

- `IISAudioIsolatedStreamECProxy`
- `site.IISAudioIsolatedStreamECProxy`
- `/Library/Caches/com.apple.xbs/5D58D6FB-4B9B-48DB-AF57-4EB20C99A843/TemporaryDirectory.zSX0o6/Sources/AppleARMIISAudio/src/kext/IsolatedStreamECProxy/IOService/IISAudioIsolatedStreamECProxy.cpp`
