# `AppleHPMARMI2C`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x140` (320 bytes)
- Metaclass: `0xfffffe000b94f158`; metaclass vtable `0xfffffe0008104bf8`; class vtable `0xfffffe0008104478`
- Registration (init): `0xfffffe0008fa9acc`
- Superclasses: [`AppleHPMARM`](AppleHPMARM.md) → [`AppleHPMEmbedded`](AppleHPMEmbedded.md) → [`AppleHPM`](AppleHPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `AppleHPMBusDevice` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMBusDevice`
- `AppleHPMI2CType1` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `usbc,cd3215`
- `AppleHPMI2CType2` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `usbc,cd3217`
- `AppleHPMI2CType3` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `usbc,sn201202x,iic`

## Strings in its kext that name it (9)

- `site.AppleHPMARMI2C`
- `AppleHPMARMI2C::start - no Rid found, defaulting to 0\n`
- `AppleHPMARMI2C::start - hpmI2CRetries boot-arg: %u ms\n`
- `AppleHPMARMI2C::start - hpmI2CRetryInterval boot-arg: %u ms\n`
- `AppleHPMARMI2C`
- `AppleHPMARMI2C::start - hpmI2CNonCompliant boot-arg: %u\n`
- `AppleHPMARMI2C::start - i2c retry interval set to: %u ms\n`
- `AppleHPMARMI2C::start - hpmlog boot-arg: 0x%X\n`
- `AppleHPMARMI2C::start - Unable to read hpmlog boot-arg\n`
