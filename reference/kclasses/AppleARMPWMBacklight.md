# `AppleARMPWMBacklight`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b9348d0`; metaclass vtable `0xfffffe0007fc3ca8`; class vtable `0xfffffe0007fc3750`
- Registration (init): `0xfffffe00087236a8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMPWMBacklight` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMPWMDevice`, `IONameMatch` = `backlight,pwm`

## Strings in its kext that name it (11)

- `%s::%s: AppleARMPWMBacklight::callPlatformFunction (\"%s\",waitForFunction = %d,p1 = %p,p2 = %p) \n`
- `AppleARMPWMBacklightControllerUpdateFunction`
- `%s::%s: AppleARMPWMBacklight::defaultBrightness = %d\n`
- `AppleARMPWMBacklight`
- `site.AppleARMPWMBacklightControllerUpdateFunction`
- `site.AppleARMPWMBacklight`
- `%s::%s: AppleARMPWMBacklight::callPlatformFunction( signature = 0x%x )\n`
- `%s::%s: AppleARMPWMBacklight -> change to %d %p\n`
- `%s::%s: AppleARMPWMBacklight::callPlatformFunction (calling super) \n`
- `%s::%s: AppleARMPWMBacklight::start complete\n`
- `%s::%s: AppleARMPWMBacklight::start: no backlight enable function\n`
