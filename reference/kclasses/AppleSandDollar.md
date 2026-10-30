# `AppleSandDollar`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md)
- Object size: `0x3e0` (992 bytes)
- Metaclass: `0xfffffe000b937fc8`; metaclass vtable `0xfffffe0007ffd810`; class vtable `0xfffffe0007ffd0b8`
- Registration (init): `0xfffffe0008a09698`
- Superclasses: [`AppleMesa`](AppleMesa.md) → [`AppleSPIBiometricSensor`](AppleSPIBiometricSensor.md) → [`AppleBiometricSensor`](AppleBiometricSensor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSandDollar` in [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md): `IOProviderClass` = `AppleARMSPIDevice`, `IONameMatch` = `['biosensor,mesa']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) on `biosensor,mesa`

## Strings in its kext that name it (3)

- `AppleSandDollar`
- `/Library/Caches/com.apple.xbs/56F15675-1195-4005-99F1-4A3BD4B8790B/TemporaryDirectory.afkHo1/Sources/AppleBiometricSensor/AppleSandDollar.cpp`
- `site.AppleSandDollar`
