# `ANEExclaveProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b94c178`; metaclass vtable `0xfffffe00080bd8c8`; class vtable `0xfffffe00080bd370`
- Registration (init): `0xfffffe0008d3f9d0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ANEExclaveProxy` in [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['ane,ane1-exclave-proxy', 'ane,ane-exclave-proxy']`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/ane-exclave-proxy`](../devicetree/root__arm-io__ane-exclave-proxy.md) on `ane,ane-exclave-proxy`
- [`/arm-io/ane1-exclave-proxy`](../devicetree/root__arm-io__ane1-exclave-proxy.md) on `ane,ane1-exclave-proxy`

## Strings in its kext that name it (4)

- `getANEExclaveProxyServiceHandle`
- `site.ANEExclaveProxy`
- `ANEExclaveProxy`
- `setupANEExclaveProxyService`
