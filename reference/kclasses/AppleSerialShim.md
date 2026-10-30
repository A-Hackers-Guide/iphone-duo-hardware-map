# `AppleSerialShim`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b99e548`; metaclass vtable `0xfffffe000822c340`; class vtable `0xfffffe000822bde8`
- Registration (init): `0xfffffe000972d6a4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleSerialShimGeneral` in [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['dockchannel-uart']`, `IOProbeScore` = `1000`
- `AppleSerialShimUart` in [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['uart0', 'uart1', 'uart2', 'uart3', 'uart4', 'uart5', 'uart6', 'uart7', 'uart8'`, `IOPropertyMatch` = `{'boot-console': ''}`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) on `dockchannel-uart`
- [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) on `uart0`

## Strings in its kext that name it (3)

- `AppleSerialShim`
- `[%s] Started AppleSerialShim.\n`
- `site.AppleSerialShim`
