# `AppleARMCPU`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000b934048`; metaclass vtable `0xfffffe0007fb3cc0`; class vtable `0xfffffe0007fb36e8`
- Registration (init): `0xfffffe00086f175c`
- Superclasses: [`IOCPU`](IOCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMCPU` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `cpu`, `IOProbeScore` = `100`

## Strings in its kext that name it (15)

- `AppleARMCPUPerformanceArbiter`
- `AppleARMCPU`
- `bool AppleARMCPU::_validateConfiguration()`
- `AppleARMCPUPerformanceArbiter::stop\n`
- `AppleARMCPUPerformanceArbiter::start\n`
- `AppleARMCPU.cpp`
- `AppleARMCPUPerformanceArbiter::init\n`
- `AppleARMCPUPerformanceServiceNub`
- `AppleARMCPUPerformanceArbiter::probe\n`
- `AppleARMCPUPerformanceArbiter::free\n`
- `site.AppleARMCPUPerformanceServiceNub`
- `site.AppleARMCPUPerformanceArbiter`
- `AppleARMCPU-AllCPU-Initialized`
- `site.AppleARMCPU`
- `AppleARMCPU-BootCPU-Initialized`
