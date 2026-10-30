# `AppleHPMARMSPMI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x160` (352 bytes)
- Metaclass: `0xfffffe000b94ec30`; metaclass vtable `0xfffffe00080f2528`; class vtable `0xfffffe00080f1da0`
- Registration (init): `0xfffffe0008f63db0`
- Superclasses: [`AppleHPMARM`](AppleHPMARM.md) → [`AppleHPMEmbedded`](AppleHPMEmbedded.md) → [`AppleHPM`](AppleHPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleHPMARMSPMIType1` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `usbc,spmi`
- `AppleHPMARMSPMIType2` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `usbc,sn201202x,spmi`
- `AppleHPMARMSPMIType3` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `usbc,cbtl1702,spmi`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) on `usbc,cbtl1702,spmi`

## Strings in its kext that name it (19)

- `AppleHPMARMSPMI::start - failed to register wake event int\n`
- `AppleHPMARMSPMI::start - interrupt-type and interrupts not equal length, things will not work. No SPMI slee/wake support\n`
- `AppleHPMARMSPMI::start - failed to register sleep event int\n`
- `AppleHPMARMSPMI::start - interrupt-type isn't 32-byte aligned no interrupts at all.\n`
- `AppleHPMARMSPMI::writeRegs - Transaction aborted due to SPMI Driver sleeping\n`
- `AppleHPMARMSPMI::readIECSReg - 0x%X exceeding max length of 64\n`
- `AppleHPMARMSPMI::sendHPMReset(@0x%x) - Workaround successful, out of ADFU\n`
- `AppleHPMARMSPMI::writeIECSReg - 0x%X exceeding max length of 64\n`
- `AppleHPMARMSPMI::failureRegisterDump - Mode = 0x%x 0x%x 0x%x 0x%x\n`
- `AppleHPMARMSPMI::readRegs - Transaction aborted due to SPMI Driver sleeping\n`
- `AppleHPMARMSPMI::readRegs - WARNING: Actual register length for addr 0x%x is shorter than expected, expected 0x%x, IECS returned 0x%x\n`
- `AppleHPMARMSPMI`
- `site.AppleHPMARMSPMI`
- `AppleHPMARMSPMI::start - RTPC disabled due to missing events or timers\n`
- `AppleHPMARMSPMI::sendHPMReset(@0x%x) - Workaround entry found, resetting port\n`
- `AppleHPMARMSPMI::start - Missing interrupt property, Check the EDT, AppleHPM will not be fully functional\n`
- `virtual bool AppleHPMARMSPMI::start(IOService *)`
- `AppleHPMARMSPMI::start - Missing interrupt-type property, doing legacy interrupt handling, no SPMI sleep/wake support\n`
- `AppleHPMARMSPMI::failureRegisterDump - [Reg 0x2d] = 0x%x 0x%x 0x%x 0x%x\n`
