# `AppleARMPMUCharger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md)
- Object size: `0x4a8` (1,192 bytes)
- Metaclass: `0xfffffe000b9337d0`; metaclass vtable `0xfffffe0007fb0d70`; class vtable `0xfffffe0007fb0798`
- Registration (init): `0xfffffe00086e7c34`
- Superclasses: [`AppleARMPMUPowerSource`](AppleARMPMUPowerSource.md) → [`IOPMPowerSource`](IOPMPowerSource.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMCharger` in [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md): `IOProviderClass` = `IOService`, `IONameMatch` = `charger`, `IOProbeScore` = `1000`

## Strings in its kext that name it (7)

- `AppleARMPMUCharger: dock %lu inputCurrentLimit %lu chargeLimit NONE\n`
- `/Library/Caches/com.apple.xbs/FBB9B734-F955-49B1-83B2-A607CD738984/TemporaryDirectory.jIvHmi/Sources/AppleARMPMU/AppleARMPMUCharger.cpp`
- `site.AppleARMPMUCharger`
- `AppleARMPMUCharger: dock %lu inputCurrentLimit %lu chargeLimit %lu\n`
- ` AppleARMPMUCharger::%s(displayCapacity*1000=%d _previousDisplayCapacity*1000=%d slope=%d connected=%d):  newDisplayCapacity*1000=%d, maxChangeAmount*1000=%d, diff=%u now=%u nextUpdate=%u cis=%u\n`
- `AppleARMPMUCharger`
- ` AppleARMPMUCharger::%s(displayCapacity*1000=%d _previousDisplayCapacity*1000=%d slope=%d):  newDisplayCapacity*1000=%d, now=%u nextUpdate=%u\n`
