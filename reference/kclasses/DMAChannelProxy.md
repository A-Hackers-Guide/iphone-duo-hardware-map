# `DMAChannelProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b9dfd18`; metaclass vtable `0xfffffe00082da898`; class vtable `0xfffffe00082da320`
- Registration (init): `0xfffffe0009c3422c`
- Superclasses: [`DMAChannelECProxyInterface`](DMAChannelECProxyInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DeviceTreeName` in [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['admac-leap-s-proxy', 'admac-base-s-proxy', 'admac-ec-proxy']`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (4) [DT]

- [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) on `admac-ec-proxy`
- [`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) on `admac-ec-proxy`
- [`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) on `admac-ec-proxy`
- [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) on `admac-ec-proxy`

## Strings in its kext that name it (2)

- `DMAChannelProxy`
- `site.DMAChannelProxy`
