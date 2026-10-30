# `AOPTouchHIDDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AOPTouchKext`](../kexts/com.apple.driver.AOPTouchKext.md)
- Object size: `0x290` (656 bytes)
- Metaclass: `0xfffffe000b931cb8`; metaclass vtable `0xfffffe0007f8fb60`; class vtable `0xfffffe0007f8f318`
- Registration (init): `0xfffffe00086101e0`
- Superclasses: [`AppleSPUHIDDriver`](AppleSPUHIDDriver.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Event Service` in [`com.apple.driver.AOPTouchKext`](../kexts/com.apple.driver.AOPTouchKext.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (6)

- `AOPTouchHIDDriverChargingState`
- `AOPTouchHIDDriverDataSource`
- `site.AOPTouchHIDDriverDataSource`
- `AOPTouchHIDDriver`
- `site.AOPTouchHIDDriverChargingState`
- `site.AOPTouchHIDDriver`
