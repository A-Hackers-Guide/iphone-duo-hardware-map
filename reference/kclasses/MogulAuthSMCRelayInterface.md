# `MogulAuthSMCRelayInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b937410`; metaclass vtable `0xfffffe0007ff19f0`; class vtable `0xfffffe0007ff1478`
- Registration (init): `0xfffffe00089a05d8`
- Superclasses: [`AppleAuthCPRelayInterface`](AppleAuthCPRelayInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `MogulAuthSMCRelayInterface` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['mogul,a1222']`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) on `mogul,a1222`
- [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) on `mogul,a1222`
- [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) on `mogul,a1222`

## Strings in its kext that name it (14)

- `site.MogulAuthSMCRelayInterface`
- `MogulAuthSMCRelayInterface`
- `MogulAuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu`
- `MogulAuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: error code\n`
- `MogulAuthSMCRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `MogulAuthSMCRelayInterface::transferData: Success!`
- `MogulAuthSMCRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: error:0x%x`
- `MogulAuthSMCRelayInterface::transferData: Transfer failed after %d retries!`
- `MogulAuthSMCRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: zone:%d, address:0x%x, length:%d\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: _write failed\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: _read failed\n`
