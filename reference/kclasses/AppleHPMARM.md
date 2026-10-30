# `AppleHPMARM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b94ecd0`; metaclass vtable `0xfffffe00080f46d8`; class vtable `0xfffffe00080f3f58`
- Registration (init): `0xfffffe0008f67984`
- Superclasses: [`AppleHPMEmbedded`](AppleHPMEmbedded.md) → [`AppleHPM`](AppleHPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleHPMARMI2C`](AppleHPMARMI2C.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMARMSPMI`](AppleHPMARMSPMI.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (37)

- `AppleHPMARM can't find AppleSMC\n`
- `AppleHPMARMSPMI::start - failed to register wake event int\n`
- `site.AppleHPMARMI2C`
- `AppleHPMARMSPMI::start - interrupt-type and interrupts not equal length, things will not work. No SPMI slee/wake support\n`
- `AppleHPMARM`
- `AppleHPMARMSPMI::start - failed to register sleep event int\n`
- `AppleHPMARMSPMI::start - interrupt-type isn't 32-byte aligned no interrupts at all.\n`
- `AppleHPMARMI2C::start - no Rid found, defaulting to 0\n`
- `AppleHPMARMI2C::start - hpmI2CRetries boot-arg: %u ms\n`
- `AppleHPMARMSPMI::writeRegs - Transaction aborted due to SPMI Driver sleeping\n`
- `site.AppleHPMARM`
- `AppleHPMARMSPMI::readIECSReg - 0x%X exceeding max length of 64\n`
- `AppleHPMARMSPMI::sendHPMReset(@0x%x) - Workaround successful, out of ADFU\n`
- `AppleHPMARMSPMI::writeIECSReg - 0x%X exceeding max length of 64\n`
- `AppleHPMARM::start - hpmI2CRetryInterval boot-arg: %u ms\n`
- `AppleHPMARMSPMI::failureRegisterDump - Mode = 0x%x 0x%x 0x%x 0x%x\n`
- `AppleHPMARMSPMI::readRegs - Transaction aborted due to SPMI Driver sleeping\n`
- `AppleHPMARM::start - hpmPowerDelaySrc boot-arg: %u ms\n`
- `AppleHPMARMSPMI::readRegs - WARNING: Actual register length for addr 0x%x is shorter than expected, expected 0x%x, IECS returned 0x%x\n`
- `AppleHPMARMSPMI`
- `AppleHPMARMI2C::start - hpmI2CRetryInterval boot-arg: %u ms\n`
- `AppleHPMARM::start - hpmPowerDelaySnk boot-arg: %u ms\n`
- `AppleHPMARM::startSMCDelayUVDM -- SMC key write failed 0x%x\n`
- `site.AppleHPMARMSPMI`
- `AppleHPMARMSPMI::start - RTPC disabled due to missing events or timers\n`
- `AppleHPMARMI2C`
- `AppleHPMARM can't find AppleSMCFamily\n`
- `AppleHPMARMI2C::start - hpmI2CNonCompliant boot-arg: %u\n`
- `AppleHPMARMSPMI::sendHPMReset(@0x%x) - Workaround entry found, resetting port\n`
- `AppleHPMARMI2C::start - i2c retry interval set to: %u ms\n`
- `AppleHPMARMSPMI::start - Missing interrupt property, Check the EDT, AppleHPM will not be fully functional\n`
- `AppleHPMARM::start - hpmI2CRetries boot-arg: %u ms\n`
- `AppleHPMARMI2C::start - hpmlog boot-arg: 0x%X\n`
- `virtual bool AppleHPMARMSPMI::start(IOService *)`
- `AppleHPMARMSPMI::start - Missing interrupt-type property, doing legacy interrupt handling, no SPMI sleep/wake support\n`
- `AppleHPMARMI2C::start - Unable to read hpmlog boot-arg\n`
- `AppleHPMARMSPMI::failureRegisterDump - [Reg 0x2d] = 0x%x 0x%x 0x%x 0x%x\n`
