# `MogulAuthI2CRelayInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b9373c0`; metaclass vtable `0xfffffe0007ff0d90`; class vtable `0xfffffe0007ff0818`
- Registration (init): `0xfffffe000899dc64`
- Superclasses: [`AppleAuthCPRelayInterface`](AppleAuthCPRelayInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `MogulAuthI2CRelayInterface` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `['mogul,a1222']`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) on `mogul,a1222`
- [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) on `mogul,a1222`
- [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) on `mogul,a1222`

## Strings in its kext that name it (11)

- `site.MogulAuthI2CRelayInterface`
- `MogulAuthI2CRelayInterface`
- `MogulAuthI2CRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: error code\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: _read failed\n`
- `MogulAuthI2CRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: _write failed\n`
- `MogulAuthI2CRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: zone:%d, address:0x%x, length:%d\n`
- `MogulAuthI2CRelayInterface::_read: bus error during certificate read\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: error:0x%x`
