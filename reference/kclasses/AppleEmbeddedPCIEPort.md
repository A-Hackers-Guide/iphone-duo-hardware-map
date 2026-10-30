# `AppleEmbeddedPCIEPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedPCIE`](../kexts/com.apple.driver.AppleEmbeddedPCIE.md)
- Object size: `0x1e48` (7,752 bytes)
- Metaclass: `0xfffffe000b9438b0`; metaclass vtable `0xfffffe00080896e8`; class vtable `0xfffffe0008088d68`
- Registration (init): `0xfffffe0008c5e968`
- Superclasses: [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`APCIECoreRCGen5Port`](APCIECoreRCGen5Port.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (31)

- `virtual void AppleEmbeddedPCIEPort::_applyTunablesFromData(const OSData *, regRead_t, regWrite_t, const char *)`
- `AppleEmbeddedPCIEPortControlPrivate.cpp`
- `void AppleEmbeddedPCIEPort::disableGatedWrapper(uint32_t *)`
- `site.AppleEmbeddedPCIEPortControlFunction`
- `virtual uint32_t AppleEmbeddedPCIEPort::_findSIDForRID(rid_t, IOPCIDevice *)`
- `AppleEmbeddedPCIEPort *AppleEmbeddedPCIE::getPort(uint32_t) const`
- `IOPCIDevice *AppleEmbeddedPCIEPort::_findDeviceForRID(rid_t)`
- `virtual void AppleEmbeddedPCIEPort::_findDART()`
- `virtual IOReturn AppleEmbeddedPCIEPort::_mapRIDToSID(IOPCIDevice *)`
- `void AppleEmbeddedPCIEPort::unlockStateLock()`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s child %s attached without AppleEmbeddedPCIEPort property\n`
- `void AppleEmbeddedPCIEPort::waitForLinkUpGated(AbsoluteTime *, bool *)`
- `virtual void AppleEmbeddedPCIEPort::setNub(IOPCIDevice *)`
- `virtual IOReturn AppleEmbeddedPCIEPort::_unmapRIDFromSID(IOPCIDevice *)`
- `virtual uint32_t AppleEmbeddedPCIEPort::_numTxNPRequests()`
- `virtual IOReturn AppleEmbeddedPCIEPort::setDesiredLinkSpeed(uint32_t)`
- `void AppleEmbeddedPCIEPort::setMaximumLinkSpeed(uint32_t)`
- `site.AppleEmbeddedPCIEPort`
- `void AppleEmbeddedPCIEPort::exitDeepSleep()`
- `IOReturn AppleEmbeddedPCIEPort::enableGated(uint32_t *)`
- `AppleEmbeddedPCIEPortControlFunction`
- `AppleEmbeddedPCIEPort.cpp`
- `IOReturn AppleEmbeddedPCIEPort::reenableThreadCall(thread_call_t)_block_invoke`
- `AppleEmbeddedPCIEPort`
- `bool AppleEmbeddedPCIEPort::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `_state != AppleEmbeddedPCIEPortEnabling`
- `void AppleEmbeddedPCIEPort::setStateLocked(enum AppleEmbeddedPCIEPortState, const char *)`
- `virtual void AppleEmbeddedPCIEPort::_registerAsInterruptController()`
- `void AppleEmbeddedPCIEPort::lockStateLock()`
- `site.AppleEmbeddedPCIEPort *`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s child %s attached without AppleEmbeddedPCIEPort property\n`
