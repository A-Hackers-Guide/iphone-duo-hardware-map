# `AppleSPUHIDDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0x238` (568 bytes)
- Metaclass: `0xfffffe000b99cfe0`; metaclass vtable `0xfffffe00082186a8`; class vtable `0xfffffe0008217e68`
- Registration (init): `0xfffffe00096da1bc`
- Superclasses: [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (7; 20 in total)

- [`AOPTouchHIDDriver`](AOPTouchHIDDriver.md) — `com.apple.driver.AOPTouchKext`
- [`AppleSPUALSColorDriver`](AppleSPUALSColorDriver.md) — `com.apple.driver.AppleALSColorSensor`
- [`AppleSPUALSDriver`](AppleSPUALSDriver.md) — `com.apple.driver.AppleSPU`
- [`AppleSPUALSLuxDriver`](AppleSPUALSLuxDriver.md) — `com.apple.driver.AppleEmbeddedLightSensor`
- [`AppleSPUButtonDriver`](AppleSPUButtonDriver.md) — `com.apple.driver.AppleSPU`
- [`AppleSPUMesaDriver`](AppleSPUMesaDriver.md) — `com.apple.driver.AppleSPU`
- [`AppleSPUSmartCoverDriver`](AppleSPUSmartCoverDriver.md) — `com.apple.driver.AppleSPU`

## IOKit personalities that instantiate it (1)

- `AppleSPUHIDDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (13)

- `AppleSPUHIDDriverUserClient`
- `AppleSPUHIDDriver: set %s kIOHIDEventServiceQueueSize to %d KB\n`
- `AppleSPUHIDDriver: coexID:%d found for service:%s from driver:%s \n`
- `AppleSPUHIDDriver:: matched AppleARMPMUCharger service %p\n`
- `AppleSPUHIDDriver::Unable to match AppleARMPMUCharger service\n`
- `AppleSPUHIDDriver`
- `site.AppleSPUHIDDriverUserClient`
- `AppleSPUHIDDriverUC.cpp`
- `AppleSPUHIDDriver: failed to send timesync report (sz=%u)\n`
- `site.AppleSPUHIDDriver`
- `AppleSPUHIDDriver - failed to register interest for coex service %p, coex index %d\n`
- `AppleSPUHIDDriver::openForClient -> %x`
- `AppleSPUHIDDriver: %s set coex property %d %s, ret=%x, coex-idx=%x`
