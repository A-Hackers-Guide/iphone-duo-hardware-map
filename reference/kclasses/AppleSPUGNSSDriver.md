# `AppleSPUGNSSDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000b99cf40`; metaclass vtable `0xfffffe0008217588`; class vtable `0xfffffe0008217030`
- Registration (init): `0xfffffe00096d365c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUGNSSDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['gnss']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) on `gnss`

## Strings in its kext that name it (9)

- `AppleSPUGNSSDriver`
- `AppleSPUGNSSDriverUserClient::clientClose[%s]`
- `site.AppleSPUGNSSDriverUserClient`
- `site.AppleSPUGNSSDriver`
- `AppleSPUGNSSDriverUserClient`
- `AppleSPUGNSSDriverUserClient::start[%s] -> %d [ret=%x]`
- `AppleSPUGNSSDriver::_setEventQueueGated kIOReturnExclusiveAccess`
- `AppleSPUGNSSDriver::_setDataNotificationPortGated kIOReturnNotReady`
- `AppleSPUGNSSDriver::_setDataQueueGated kIOReturnExclusiveAccess`
