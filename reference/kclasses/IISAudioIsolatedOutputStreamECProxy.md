# `IISAudioIsolatedOutputStreamECProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9ef580`; metaclass vtable `0xfffffe00082fa968`; class vtable `0xfffffe00082fa408`
- Registration (init): `0xfffffe0009eb1434`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IISAudioIsolatedOutputStreamECProxy` in [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['iisaudio,isolated-output-stream-proxy']`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/audio-speaker-tx-stream-proxy`](../devicetree/root__arm-io__audio-speaker-tx-stream-proxy.md) on `iisaudio,isolated-output-stream-proxy`
- [`/arm-io/audio-receiver-tx-stream-proxy`](../devicetree/root__arm-io__audio-receiver-tx-stream-proxy.md) on `iisaudio,isolated-output-stream-proxy`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/5D58D6FB-4B9B-48DB-AF57-4EB20C99A843/TemporaryDirectory.zSX0o6/Sources/AppleARMIISAudio/src/kext/IsolatedStreamECProxy/IOService/IISAudioIsolatedOutputStreamECProxy.cpp`
- `IISAudioIsolatedOutputStreamECProxy`
- `site.IISAudioIsolatedOutputStreamECProxy`
