# `AppleSPIMCController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPIMC`](../kexts/com.apple.driver.AppleSPIMC.md)
- Object size: `0x1e10` (7,696 bytes)
- Metaclass: `0xfffffe000b99bae0`; metaclass vtable `0xfffffe0008207280`; class vtable `0xfffffe0008206c00`
- Registration (init): `0xfffffe00096a5f70`
- Superclasses: [`AppleARMSPIController`](AppleARMSPIController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPIMCController` in [`com.apple.driver.AppleSPIMC`](../kexts/com.apple.driver.AppleSPIMC.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `spi-1,spimc`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) on `spi-1,spimc`

## Strings in its kext that name it (5)

- `AppleSPIMCController::start: canot create Stats\n`
- `AppleSPIMCControllerStats`
- `AppleSPIMCController`
- `site.AppleSPIMCControllerStats`
- `site.AppleSPIMCController`
