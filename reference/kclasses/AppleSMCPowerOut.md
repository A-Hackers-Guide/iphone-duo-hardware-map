# `AppleSMCPowerOut`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b99b350`; metaclass vtable `0xfffffe00081fd7e0`; class vtable `0xfffffe00081fd288`
- Registration (init): `0xfffffe000966b8a4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCPowerOut` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-power-out']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-power-out`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-power-out.md) on `smc-power-out`

## Strings in its kext that name it (16)

- `AppleSMCPowerOut: Init\n`
- `AppleSMCPowerOut: SMC key for PowerBudget is unavailable, not proceeding\n`
- `AppleSMCPowerOut: unsupported Function Key\n`
- `AppleSMCPowerOut: client registration attempt returned Error 0x%08x\n`
- `AppleSMCPowerOut: failed to get ppmProvider\n`
- `AppleSMCPowerOut: admission check, request:%dmW, decision:%dmW\n`
- `AppleSMCPowerOut: Plug event from SMC\n`
- `AppleSMCPowerOut: smc key write %d unsuccessful\n`
- `AppleSMCPowerOut: Matching with PPM failed\n`
- `AppleSMCPowerOut: received budget, timescale %d, reason %d, value %d mW\n`
- `site.AppleSMCPowerOut`
- `AppleSMCPowerOut: PPM client is Null\n`
- `AppleSMCPowerOut`
- `AppleSMCPowerOut: SMC key:0x%x read unsuccessful result:%s!\n`
- `AppleSMCPowerOut: RegisterService\n`
- `AppleSMCPowerOut: PPM Client is Null\n`
