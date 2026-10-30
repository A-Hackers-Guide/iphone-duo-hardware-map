# `AppleInterruptControllerV3`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleInterruptControllerV3`](../kexts/com.apple.driver.AppleInterruptControllerV3.md)
- Object size: `0x4e8` (1,256 bytes)
- Metaclass: `0xfffffe000b952880`; metaclass vtable `0xfffffe000812bef0`; class vtable `0xfffffe000812b878`
- Registration (init): `0xfffffe000906bd04`
- Superclasses: [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleInterruptControllerV3` in [`com.apple.driver.AppleInterruptControllerV3`](../kexts/com.apple.driver.AppleInterruptControllerV3.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `aic,3`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) on `aic,3`

## Strings in its kext that name it (10)

- `AppleInterruptControllerV3::start: _aicRevision = %d _aicBaseAddress = %p _aicNumVectors = 0x%08x Num Shared Timestamps = %u \n`
- `\"AppleInterruptControllerV3::handleInterrupt: unexpected vectorType: 0x%08x, IACK=0x%08x\" @%s:%d`
- `AppleInterruptControllerV3::startInterruptTimestamping: Timestamp already enabled for requested interrupt\n`
- `\"AppleInterruptControllerV3::startInterruptTimestamping: invalid config: 0x%08x\" @%s:%d`
- `site.AppleInterruptControllerV3`
- `\"AppleInterruptControllerV3::getTimestamp: invalid config: 0x%08x\" @%s:%d`
- `\"AppleInterruptControllerV3::stopInterruptTimestamping: invalid config: 0x%08x\" @%s:%d`
- `AppleInterruptControllerV3.cpp`
- `AppleInterruptControllerV3::_aicPlatformQuiesceActions: Unmask %u interrupts required in SLP_MEDIA\n`
- `AppleInterruptControllerV3`
