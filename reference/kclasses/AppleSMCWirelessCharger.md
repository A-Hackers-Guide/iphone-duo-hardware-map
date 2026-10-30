# `AppleSMCWirelessCharger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMCWirelessCharger`](../kexts/com.apple.driver.AppleSMCWirelessCharger.md)
- Object size: `0x458` (1,112 bytes)
- Metaclass: `0xfffffe000b99b8f8`; metaclass vtable `0xfffffe0008205b80`; class vtable `0xfffffe0008205538`
- Registration (init): `0xfffffe000969fffc`
- Superclasses: [`AppleAirPowerCharger`](AppleAirPowerCharger.md) → [`AppleC26Charger`](AppleC26Charger.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `SMCWirelessCharger` in [`com.apple.driver.AppleSMCWirelessCharger`](../kexts/com.apple.driver.AppleSMCWirelessCharger.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-ext-charger']`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) on `smc-ext-charger`

## Strings in its kext that name it (22)

- `AppleSMCWirelessCharger: successfully registered for audio notifications\n`
- `/Library/Caches/com.apple.xbs/A89B338A-901F-4901-9BB6-565FF3779AD0/TemporaryDirectory.NfDpto/Sources/AppleC26Charger/AppleSMCWirelessCharger.cpp`
- `AppleSMCWirelessCharger: stopping\n`
- `AppleSMCWirelessCharger: dumping register memory\n`
- `AppleSMCWirelessCharger::_wirelessDockNotificationCallout: %d\n`
- `AppleSMCWirelessCharger`
- `AppleSMCWirelessCharger: dumping exception frame\n`
- `AppleSMCWirelessCharger: region code 0x%x\n`
- `AppleSMCWirelessCharger: Puck classifier evt %d: %d => %d\n`
- `AppleSMCWirelessCharger: map %d: base 0x%x length 0x%x\n`
- `AppleSMCWirelessCharger::_displayNotificationCallout: %d\n`
- `AppleSMCWirelessCharger::_wiredDockNotificationCallout: %d\n`
- `AppleSMCWirelessCharger: too hot !!!\n`
- `AppleSMCWirelessCharger: dumping global reserve map\n`
- `AppleSMCWirelessCharger: failed to register for audio notifications\n`
- `site.AppleSMCWirelessChargerUserClient`
- `AppleSMCWirelessCharger::_audioNotificationCallout: %d\n`
- `site.AppleSMCWirelessCharger`
- `AppleSMCWirelessCharger.cpp`
- `AppleSMCWirelessCharger: starting\n`
- `AppleSMCWirelessChargerUserClient`
- `AppleSMCWirelessCharger: comms not ready\n`
