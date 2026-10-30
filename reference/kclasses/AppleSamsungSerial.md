# `AppleSamsungSerial`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSamsungSerial`](../kexts/com.apple.driver.AppleSamsungSerial.md)
- Object size: `0x128` (296 bytes)
- Metaclass: `0xfffffe000b99e320`; metaclass vtable `0xfffffe000822adf0`; class vtable `0xfffffe000822a7c0`
- Registration (init): `0xfffffe000972b7b4`
- Superclasses: [`AppleMMIOSerial`](AppleMMIOSerial.md) → [`AppleOnboardSerialBusInterface`](AppleOnboardSerialBusInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSamsungSerial` in [`com.apple.driver.AppleSamsungSerial`](../kexts/com.apple.driver.AppleSamsungSerial.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['uart-1,samsung']`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) on `uart-1,samsung`

## Strings in its kext that name it (2)

- `site.AppleSamsungSerial`
- `AppleSamsungSerial`
