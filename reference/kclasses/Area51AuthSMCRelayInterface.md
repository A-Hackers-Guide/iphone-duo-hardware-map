# `Area51AuthSMCRelayInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b937460`; metaclass vtable `0xfffffe0007ff27b8`; class vtable `0xfffffe0007ff2240`
- Registration (init): `0xfffffe00089a4128`
- Superclasses: [`AppleAuthCPRelayInterface`](AppleAuthCPRelayInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Area51AuthSMCRelayInterface` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['area51']`

## Strings in its kext that name it (9)

- `Area51AuthSMCRelayInterface`
- `site.Area51AuthSMCRelayInterface`
- `Area51AuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu`
- `Area51AuthSMCRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `Area51AuthSMCRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `Area51AuthSMCRelayInterface::transferData: Transfer failed after %d retries!`
- `Area51AuthSMCRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `Area51AuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu`
- `Area51AuthSMCRelayInterface::transferData: Success!`
