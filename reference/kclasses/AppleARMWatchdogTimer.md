# `AppleARMWatchdogTimer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMWatchdogTimer`](../kexts/com.apple.driver.AppleARMWatchdogTimer.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b934e78`; metaclass vtable `0xfffffe0007fcc208`; class vtable `0xfffffe0007fcbc90`
- Registration (init): `0xfffffe0008744500`
- Superclasses: [`IOWatchdog`](IOWatchdog.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMWatchdogTimer` in [`com.apple.driver.AppleARMWatchdogTimer`](../kexts/com.apple.driver.AppleARMWatchdogTimer.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `wdt,s5l8960x`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) on `wdt,s5l8960x`

## Strings in its kext that name it (6)

- `AppleARMWatchdogTimer.cpp`
- `site.AppleARMWatchdogTimer`
- `site.AppleARMWatchdogTimerFunctionExpireWatchdog`
- `AppleARMWatchdogTimer`
- `AppleARMWatchdogTimerFunctionExpireWatchdog`
- `AppleARMWatchdogTimer::start: _wdtBaseAddress: %#lx _wdtResetCount=%#x _SMCWatchdogAvailable=%d\n`
