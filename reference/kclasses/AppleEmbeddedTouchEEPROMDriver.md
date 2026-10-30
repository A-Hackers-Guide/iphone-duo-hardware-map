# `AppleEmbeddedTouchEEPROMDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTouchEEPROM`](../kexts/com.apple.driver.AppleEmbeddedTouchEEPROM.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b944250`; metaclass vtable `0xfffffe0008093a30`; class vtable `0xfffffe00080934d8`
- Registration (init): `0xfffffe0008c94928`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEmbeddedTouchEEPROM` in [`com.apple.driver.AppleEmbeddedTouchEEPROM`](../kexts/com.apple.driver.AppleEmbeddedTouchEEPROM.md): `IOProviderClass` = `AppleARMNORFlashDevice`, `IONameMatch` = `display-generic-data,rw`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md) on `display-generic-data,rw`
- [`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md) on `display-generic-data,rw`

## Strings in its kext that name it (8)

- `TouchEEPROMDriver::%s: [ENTRY] AppleEmbeddedTouchEEPROMDriver::start() called with provider=%p\n`
- `TouchEEPROMDriver::%s: [ERROR] Failed to cast provider to AppleEmbeddedTouchEEPROMDriver\n`
- `site.AppleEmbeddedTouchEEPROMDriver`
- `TouchEEPROMDriver::%s: AppleEmbeddedTouchEEPROMDriver class instance not found\n\n`
- `site.AppleEmbeddedTouchEEPROMDriverUC`
- `AppleEmbeddedTouchEEPROMDriver`
- `TouchEEPROMDriver::%s: [EXIT] AppleEmbeddedTouchEEPROMDriver::start() completed successfully\n`
- `AppleEmbeddedTouchEEPROMDriverUC`
