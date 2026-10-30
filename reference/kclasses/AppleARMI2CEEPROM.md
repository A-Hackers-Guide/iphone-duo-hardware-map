# `AppleARMI2CEEPROM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9348a8`; metaclass vtable `0xfffffe0007fc36b8`; class vtable `0xfffffe0007fc3130`
- Registration (init): `0xfffffe00087224d0`
- Superclasses: [`AppleARMNORFlashController`](AppleARMNORFlashController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMI2CEEPROM` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `eeprom,i2c`

## Device-tree nodes it binds (4) [DT]

- [`/arm-io/i2c3/display-eeprom`](../devicetree/root__arm-io__i2c3__display-eeprom.md) on `eeprom,i2c`
- [`/arm-io/i2c3/display-eeprom-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi.md) on `eeprom,i2c`
- [`/arm-io/i2c3/display-eeprom-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2.md) on `eeprom,i2c`
- [`/arm-io/i2c3/display-eeprom-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi.md) on `eeprom,i2c`

## Strings in its kext that name it (3)

- `AppleARMI2CEEPROM`
- `AppleARMI2CEEPROM.cpp`
- `site.AppleARMI2CEEPROM`
