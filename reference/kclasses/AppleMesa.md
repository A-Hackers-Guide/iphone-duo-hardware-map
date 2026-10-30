# `AppleMesa`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md)
- Object size: `0x3d8` (984 bytes)
- Metaclass: `0xfffffe000b937ed8`; metaclass vtable `0xfffffe0007ffbf40`; class vtable `0xfffffe0007ffb7f0`
- Registration (init): `0xfffffe0008a05d44`
- Superclasses: [`AppleSPIBiometricSensor`](AppleSPIBiometricSensor.md) → [`AppleBiometricSensor`](AppleBiometricSensor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleSandDollar`](AppleSandDollar.md) — `com.apple.driver.AppleBiometricSensor`

## IOKit personalities that instantiate it (1)

- `AppleMesa` in [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md): `IOProviderClass` = `AppleARMSPIDevice`, `IONameMatch` = `['biosensor,mesa']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) on `biosensor,mesa`

## Strings in its kext that name it (18)

- `AppleMesaShim`
- `site.AppleMesaShim`
- `/Library/Caches/com.apple.xbs/56F15675-1195-4005-99F1-4A3BD4B8790B/TemporaryDirectory.afkHo1/Sources/AppleBiometricSensor/AppleMesa.cpp`
- `AppleMesaARMFunction`
- `AppleMesa`
- `site.AppleMesaResources`
- `AppleMesaCommand`
- `site.AppleMesa`
- `/Library/Caches/com.apple.xbs/56F15675-1195-4005-99F1-4A3BD4B8790B/TemporaryDirectory.afkHo1/Sources/AppleBiometricSensor/AppleMesaResources.cpp`
- `AppleMesaResources`
- `site.AppleMesaARMFunction`
- `AppleMesaUserClientBase`
- `site.AppleMesaUserClientBase`
- `site.AppleMesaCommand`
- `OSDynamicCast from IOCommandPool's IOCommand to AppleMesaCommand failed.`
- `%s: Failed to get AppleMesa provider!`
- `%s: AppleMesa::handleCMD -- kCMDSetEncryptedParameters buffer too large.`
- `%s: AppleMesa::handleCMD -- Encryted command 0x%x buffer too large.`
