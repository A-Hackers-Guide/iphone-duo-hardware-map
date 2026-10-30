# `AppleS5L8940XI2CController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleS5L8940XI2C`](../kexts/com.apple.driver.AppleS5L8940XI2C.md)
- Object size: `0x1e0` (480 bytes)
- Metaclass: `0xfffffe000b993e78`; metaclass vtable `0xfffffe00081c56f8`; class vtable `0xfffffe00081c5140`
- Registration (init): `0xfffffe000947f284`
- Superclasses: [`AppleARMIICController`](AppleARMIICController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleS5L8940XI2CController` in [`com.apple.driver.AppleS5L8940XI2C`](../kexts/com.apple.driver.AppleS5L8940XI2C.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `i2c,s5l8940x`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) on `i2c,s5l8940x`
- [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) on `i2c,s5l8940x`
- [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) on `i2c,s5l8940x`

## Strings in its kext that name it (11)

- `site.AppleS5L8940XI2CController`
- `AppleS5L8940XI2CController::start: %s required function device_reset not found\n`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, filter tunable was malformed in the registry`
- `AppleS5L8940XI2CController`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, tbuf tunable was malformed in the registry`
- `AppleS5L8940XI2CController::_runInterruptMode timeout waiting for interrupt\n`
- `AppleS5L8940XI2CController::start: %s this: %p _i2cBaseAddress: %#lx, external-bus=%d, use-table-div=%d, alwayson=%d, usePSD=%d, powerOffDelay=%u\n`
- `AppleS5L8940XI2CController::_unjamBus Bus unjam unsuccessful, SMSTA: %08x\n`
- `AppleS5L8940XI2CController[%s]: Malformed %s property: Expecting 2x32-bit mask tunable`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, trigger level tunable was malformed in the registry`
- `AppleS5L8940XI2CController::_unjamBus Attempting recovery\n`
