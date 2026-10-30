# `AppleThunderboltHALGenericACIO`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x468` (1,128 bytes)
- Metaclass: `0xfffffe000b9d2708`; metaclass vtable `0xfffffe0008289ec8`; class vtable `0xfffffe00082896e0`
- Registration (init): `0xfffffe00099c09bc`
- Superclasses: [`AppleThunderboltGenericHAL`](AppleThunderboltGenericHAL.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleThunderboltHALType5`](AppleThunderboltHALType5.md) — `com.apple.driver.AppleThunderboltNHI`
- [`AppleThunderboltHALType7`](AppleThunderboltHALType7.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltHALGenericACIO::poweredStart - fInterruptEventSource[%d] = %p\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - equal = %d\n`
- `%lldus AppleThunderboltHALGenericACIO<%p>::enableDART - enable = %d fDARTEnabled = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::registerWrite32 - offset = 0x%08x data = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::destroyRegisterRanges - staring iteration\n`
- `%lldus AppleThunderboltHALGenericACIO::handleInterrupt - src %p index = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR: failed to create DARTVMAllocator\n`
- `%lldus AppleThunderboltHALGenericACIO<%p>::portChangeNotification - message = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to create RX mapper for hopID %d, index %d!\n`
- `%lldus AppleThunderboltHALGenericACIO<%p>::portChangeNotification - ERROR - couldn't schedule port change event on queue! tmp_status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::setWorkLoopForInterrupt - switching int %d to main workloop.\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - connected = %d connect_count = 0x%x cable_speed = 0x%x legacy_adapters = %d link_training_mode = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::registerRead32 - offset = 0x%08x result = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::free\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - data_status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: invalid SID partitioning scheme! fDartSIDPartitioning = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltHALGenericACIO::finalize\n`
- `%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to set DART allocator for TX hop ID %d\n`
- `%lldus AppleThunderboltHALGenericACIO::unpoweredStart - fDock = %p status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::poweredStart - fDartSIDPartitioning = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::start\n`
- `%lldus AppleThunderboltHALGenericACIO<%p>::enableDART - enable DART\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::enablePowerManagement - status = 0x%x\n`
- `\"AppleThunderboltHALGenericACIO::determineSIDPartitioning() failed - Invalid ACIO IOMapper count %zu. Expected either a single mapper or %zu mappers for %zu NHI rings.\" @%s:%d`
- `virtual IOReturn AppleThunderboltHALGenericACIO::unpoweredStart()`
- `%lldus AppleThunderboltHALGenericACIO<%p>::portChangeEvent - fPortEventCallback = %p fPortEventCallbackOwner = %p fEnabled = %d message=0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO<%p>::waitForAppleHPMWake - fAppleHPMIsAsleep = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::registerRead32 - offset = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::poweredStart - status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::registerRead32ForRange - range = %d offset = 0x%08x (0x%lx)\n`
- `%lldus AppleThunderboltHALGenericACIO::registerWrite16 - offset = 0x%08x data = 0x%04x\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::registerWrite32ForRange - range = %d offset = 0x%08x (0x%lx) data = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::handleDedicatedInterrupt - src %p index = %d fDedicatedInterruptCallback = %p fDedicatedInterruptCallbackOwner = %p\n`
- `%lldus AppleThunderboltHALGenericACIO::registerRead8 - offset = 0x%08x result = 0x%02x\n`
- `%lldus AppleThunderboltHALGenericACIO::start - return status = 0x%x\n`
- `%lldus AppleThunderboltHALGenericACIO::stopInterruptPollTimer\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::unpoweredStart - status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR: failed to set DARTVMAllocator\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::setupRegisterRanges - register range %d not found.\n`
- `%lldus AppleThunderboltHALGenericACIO::destroyPowerManagement\n`
- `%lldus AppleThunderboltHALGenericACIO::initializeMappers - done, status = 0x%08x, alignment = 0x%x\n`
- `AppleThunderboltHALGenericACIO`
- `%lldus AppleThunderboltHALGenericACIO(%d)::setWorkLoopForInterrupt - switching int %d to dedicated workloop.\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::registerRead32ForRange - range = %d offset = 0x%08x (0x%lx) result = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::createDeviceMemoryForRange - memory = %p, status = 0x%08x\n`
- `AppleThunderboltHALGenericACIO.cpp`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - ERROR: could not resolve cable state\n`
- `%lldus AppleThunderboltHALGenericACIO::unpoweredStart - fPortChangeNotifier = %p status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::destroyRegisterRanges - finished iteration\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - resolve cable state took - timeTaken = %llu ns start = %llu ns deadline = %llu ns now = %llu ns status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO::unpoweredStart - bootargs: acio = 0x%08x, tb_poll_interrupts = %d\n`
- `%lldus AppleThunderboltHALGenericACIO::unpoweredStart - dock_parent_function = %p status = 0x%08x\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::unpoweredStart - couldn't resolve dock_parent.\n`
- `%lldus AppleThunderboltHALGenericACIO::setupDARTAllocator - ERROR null mapper passed\n`
- `%lldus AppleThunderboltHALGenericACIO::initializeMappers - ERROR: failed to create TX mapper for hopID %d, index %d!\n`
- `%lldus AppleThunderboltHALGenericACIO(%d)::getCableState - is_active = %d cable_gen = 0x%x cio_gen = 0x%x dpod = %d orientation = %d\n`
- `site.AppleThunderboltHALGenericACIO`
- `%lldus AppleThunderboltHALGenericACIO<%p>::enableDART - disable DART\n`
