# `AppleThunderboltGenericHAL`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x180` (384 bytes)
- Metaclass: `0xfffffe000b9d26b8`; metaclass vtable `0xfffffe0008288e10`; class vtable `0xfffffe00082886f8`
- Registration (init): `0xfffffe00099b3d04`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltHALGenericACIO`](AppleThunderboltHALGenericACIO.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `AppleThunderboltGenericHAL::poweredStart() failed`
- `%lldus AppleThunderboltGenericHAL::lateSleep - state = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::prePCIWake - fPMCallback = %p fPMCallbackOwner = %p\n`
- `%lldus AppleThunderboltGenericHAL::probe\n`
- `%lldus AppleThunderboltGenericHAL::destroyPowerManagement\n`
- `%lldus AppleThunderboltGenericHAL::enableDeepSleep - disable deep sleep - kIOPMDriverAssertionLevelOn\n`
- `%lldus AppleThunderboltGenericHAL::earlyWake - state = 0x%08x\n`
- `AppleThunderboltGenericHAL`
- `%lldus AppleThunderboltGenericHAL(%d)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::poweredStart - status = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::lateSleep - fPMCallback = %p fPMCallbackOwner = %p\n`
- `%lldus AppleThunderboltGenericHAL(%d)<%p>::processSetPMState -  dispatchAsync( processSetPMState)\n`
- `%lldus AppleThunderboltGenericHAL::earlySleep - fPMCallback = %p fPMCallbackOwner = %p\n`
- `%lldus AppleThunderboltGenericHAL::enablePowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::enableDeepSleep - enable deep sleep - kIOPMDriverAssertionLevelOff\n`
- `%lldus AppleThunderboltGenericHAL::start - provider = %p, not of type IOService, status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - powerOverrideOnPriv\n`
- `%lldus AppleThunderboltGenericHAL::systemWillShutdown - kIOMessageSystemWillRestart\n`
- `%lldus AppleThunderboltGenericHAL::free\n`
- `%lldus AppleThunderboltGenericHAL::releaseHardware - messageClients kIOThunderboltMessageHardwareIsAvailable\n`
- `%lldus AppleThunderboltGenericHAL::stop\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware - no competition\n`
- `%lldus AppleThunderboltGenericHAL::powerStateWillChangeTo - whatDevice = %p state = %d\n`
- `%lldus AppleThunderboltGenericHAL(%d)::start - status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::finalize\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware - the hardware is ours.\n`
- `%lldus AppleThunderboltGenericHAL::earlyWake - complete - took %d milliseconds\n`
- `%lldus AppleThunderboltGenericHAL::poweredStart\n`
- `%lldus AppleThunderboltGenericHAL::releaseHardware - wakeup pending client\n`
- `%lldus AppleThunderboltGenericHAL(%d)::start (build %s %s)\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware - IOLockSleep\n`
- `%lldus AppleThunderboltGenericHAL::lateSleep - complete - took %d milliseconds\n`
- `%lldus AppleThunderboltGenericHAL::releaseHardware + client = %p\n`
- `%lldus AppleThunderboltGenericHAL::setPowerState - fPMCallback = %p fPMCallbackOwner = %p\n`
- `%lldus AppleThunderboltGenericHAL::earlyWake - fPMCallback = %p fPMCallbackOwner = %p\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - powerOverrideOffPriv status = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::start\n`
- `%lldus AppleThunderboltGenericHAL::releaseHardware -\n`
- `%lldus AppleThunderboltGenericHAL::prePCIWake - state = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - powerOverrideOnPriv status = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL<%p>::callPlatformFunction - early wake done\n`
- `%lldus AppleThunderboltGenericHAL::systemWillShutdown - kIOMessageSystemWillPowerOff\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - changePowerStateToPriv(%d) status = 0x%08x\n`
- `AppleThunderboltGenericHAL::lateSleep - complete - took %d milliseconds\n`
- `%lldus AppleThunderboltGenericHAL::earlySleep - state = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware - status = 0x%x\n`
- `site.AppleThunderboltGenericHAL`
- `%lldus AppleThunderboltGenericHAL::start - enablePowerManagement\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - powerOverrideOffPriv\n`
- `AppleThunderboltGenericHAL::earlyWake - complete - took %d milliseconds\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware + client = %p\n`
- `AppleThunderboltGenericHAL.cpp`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - state = %lu\n`
- `%lldus AppleThunderboltGenericHAL::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltGenericHAL::releaseHardware + client = %p\n`
- `%lldus AppleThunderboltGenericHAL(%d)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::enablePowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltGenericHAL::lateSleep - state = 0x%08x\n`
- `%lldus AppleThunderboltGenericHAL::acquireHardware - IOLockSleep\n`
- `%lldus AppleThunderboltGenericHAL::forcePowerState - powerOverrideOnPriv\n`
