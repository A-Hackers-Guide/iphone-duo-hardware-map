# `AppleDiagnosticDataAccessReadOnly`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md)
- Object size: `0x1c8` (456 bytes)
- Metaclass: `0xfffffe000b940808`; metaclass vtable `0xfffffe000804fe20`; class vtable `0xfffffe000804f8c0`
- Registration (init): `0xfffffe0008b712d4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleNANDDiagnosticDataAccess` in [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md): `IOProviderClass` = `AppleNANDConfigAccess`, `IOMatchCategory` = `AppleDiagnosticDataAccess`, `IOProbeScore` = `99`
- `AppleNORDiagnosticDataAccess` in [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md): `IOProviderClass` = `AppleARMNORFlashDevice`, `IONameMatch` = `diagnostic-data,format1`, `IOProbeScore` = `99`

## Device-tree nodes it binds (4) [DT]

- [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-data.md) on `diagnostic-data,format1`
- [`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md) on `diagnostic-data,format1`
- [`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md) on `diagnostic-data,format1`
- [`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md) on `diagnostic-data,format1`

## Strings in its kext that name it (4)

- `AppleDiagnosticDataAccessReadOnly`
- `site.AppleDiagnosticDataAccessReadOnly`
- `AppleDiagnosticDataAccessReadOnly.cpp`
- `\"AppleDiagnosticDataAccessReadOnly does not support unloading\" @%s:%d`
