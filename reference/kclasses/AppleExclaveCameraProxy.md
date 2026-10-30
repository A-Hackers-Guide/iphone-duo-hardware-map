# `AppleExclaveCameraProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b93a4b8`; metaclass vtable `0xfffffe000800b340`; class vtable `0xfffffe000800ade8`
- Registration (init): `0xfffffe0008a3b140`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `isp-exclave` in [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `isp,isp-exclave-proxy`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/isp-exclave-proxy`](../devicetree/root__arm-io__isp-exclave-proxy.md) on `isp,isp-exclave-proxy`

## Strings in its kext that name it (10)

- `AppleExclaveCameraProxy:%s - Booting in legacy mode, will not register\n\n`
- `AppleExclaveCameraProxy:%s - [%d] assert - aborting!\n`
- `site.AppleExclaveCameraProxy`
- `AppleExclaveCameraProxy`
- `AppleExclaveCameraProxy:%s - Platform ID: 0x%X\n`
- `AppleExclaveCameraProxy:%s - registered: %s\n`
- `AppleExclaveCameraProxy:%s - Serial logging has been enabled\n`
- `AppleExclaveCameraProxy:%s - Override ISP platformID in the registry to 0x%08X\n`
- `AppleExclaveCameraProxy:%s - registered: %s\n`
- `AppleExclaveCameraProxy:%s - Platform ID: 0x%X\n`
