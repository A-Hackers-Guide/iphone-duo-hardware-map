# `AppleEmbeddedPCIE`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedPCIE`](../kexts/com.apple.driver.AppleEmbeddedPCIE.md)
- Object size: `0x228` (552 bytes)
- Metaclass: `0xfffffe000b943888`; metaclass vtable `0xfffffe0008088cb0`; class vtable `0xfffffe00080884a8`
- Registration (init): `0xfffffe0008c4eeb0`
- Superclasses: [`IOPCIHostBridge`](IOPCIHostBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`APCIECoreRCGen5`](APCIECoreRCGen5.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (60)

- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s output buffer must be %ld bytes long (recvd %d)\n`
- `void AppleEmbeddedPCIE::_buildPortProperties(IOService *)`
- `virtual void AppleEmbeddedPCIEPort::_applyTunablesFromData(const OSData *, regRead_t, regWrite_t, const char *)`
- `AppleEmbeddedPCIE[%u]::start this = %p, _debugFlags = 0x%x\n`
- `virtual bool AppleEmbeddedPCIE::start(IOService *)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s Terminating port's link partner nub\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %02x:%02x:%02x[%04x] (0x%llx/0x%llx) -> 0x%08x%s\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %p has no APCIe port property\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %02x:%02x:%02x[%04x] (0x%llx/0x%llx) -> 0x%04x%s\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s probe\n\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s %s: failed to set hot-plug property %p in property table %p\n`
- `AppleEmbeddedPCIE::configure: No ranges defined\n`
- `AppleEmbeddedPCIEPortControlPrivate.cpp`
- `AppleEmbeddedPCIE`
- `site.AppleEmbeddedPCIEBarrier`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s GetMessagedInterruptAddress for %s, vector %d\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s failed to find %s device for RID 0:%d:%d\n`
- `void AppleEmbeddedPCIEPort::disableGatedWrapper(uint32_t *)`
- `site.AppleEmbeddedPCIEPortControlFunction`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s [%s()] RX payload counter saturated; use a smaller measurement interval.\n`
- `virtual uint32_t AppleEmbeddedPCIEPort::_findSIDForRID(rid_t, IOPCIDevice *)`
- `AppleEmbeddedPCIEPort *AppleEmbeddedPCIE::getPort(uint32_t) const`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s GTB-to-PTM circuitry not supported on this platform\n`
- `IOPCIDevice *AppleEmbeddedPCIEPort::_findDeviceForRID(rid_t)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s Attempted unaligned 4B read from %02x:%02x:%02x[%04x], returning all Fs\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s resetting probe timeout\n\n`
- `virtual void AppleEmbeddedPCIEPort::_findDART()`
- `virtual IOReturn AppleEmbeddedPCIEPort::_mapRIDToSID(IOPCIDevice *)`
- `void AppleEmbeddedPCIEPort::unlockStateLock()`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s _subordinateBus = %u\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s [%s()] Failed to get device memory for nub %s, skipping mmio timeout increase\n\n`
- `virtual IOReturn AppleEmbeddedPCIE::busProbe(IOPCIDevice *, uint32_t)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s child %s attached without AppleEmbeddedPCIEPort property\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s Scanning children\n`
- `void AppleEmbeddedPCIEPort::waitForLinkUpGated(AbsoluteTime *, bool *)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s [%s()] TX payload counter saturated; use a smaller measurement interval.\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s phy: 0x%llx = 0x%x\n`
- `virtual void AppleEmbeddedPCIEPort::setNub(IOPCIDevice *)`
- `AppleEmbeddedPCIE.cpp`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %s tunables being applied\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s auto-enabling port %u\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s resumed port %u\n`
- `virtual IOReturn AppleEmbeddedPCIEPort::_unmapRIDFromSID(IOPCIDevice *)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %02x:%02x:%02x[%04x] (0x%llx/0x%llx) <- 0x%02x%s\n`
- `AppleEmbeddedPCIEBarrier`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %s tunable: offset/mask/value=0x%08x/0x%08x/0x%08x, 0x%08x -> 0x%08x\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s reporter %s (%p) type %d, status 0x%x header {%08x %08x %08x %08x}\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s %s: failed to initialize IOPCIDevice\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s _secondaryBus = %u\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s Adding range %016llx len %016llx\n`
- `void AppleEmbeddedPCIE::_handleAEREvent(IOPCIEventSource *, const IOPCIEvent *)`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s Attempted unaligned 4B write to %02x:%02x:%02x[%04x]\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Simulated %splug for %s: 0x%08x\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s %s: failed to create IOPCIDevice name object\n`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s %02x:%02x:%02x[%04x] (0x%llx/0x%llx) <- 0x%08x%s\n`
- `virtual uint32_t AppleEmbeddedPCIEPort::_numTxNPRequests()`
- `AppleEmbeddedPCIEUserClient.cpp`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s _configBaseAddress = %p _configBaseAddressPhys = %p\n`
- `site.AppleEmbeddedPCIEUserClient`
- `[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Invalid error injection type %llu\n`
