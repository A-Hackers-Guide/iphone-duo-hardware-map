# `AppleS5L8920XPWM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleS5L8920XPWM`](../kexts/com.apple.driver.AppleS5L8920XPWM.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b993d50`; metaclass vtable `0xfffffe00081c4868`; class vtable `0xfffffe00081c4288`
- Registration (init): `0xfffffe000947b450`
- Superclasses: [`AppleARMPWM`](AppleARMPWM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleS5L8920XPWM` in [`com.apple.driver.AppleS5L8920XPWM`](../kexts/com.apple.driver.AppleS5L8920XPWM.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pwm,s5l8920x`

## Strings in its kext that name it (6)

- `\"ApplePWM: %s:%u \" \"AppleS5L8920XPWM: Failed to send droop event message\" @%s:%d`
- `AppleS5L8920XPWM::start: _pwmBaseAddress: %#lx\n`
- `AppleS5L8920XPWM.cpp`
- `site.AppleS5L8920XPWM`
- `void AppleS5L8920XPWM::_pulseInterruptOccurred(IOInterruptEventSource *, int)`
- `AppleS5L8920XPWM`
