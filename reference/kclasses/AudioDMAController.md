# `AudioDMAController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md)
- Object size: `0x960` (2,400 bytes)
- Metaclass: `0xfffffe000b9deff0`; metaclass vtable `0xfffffe00082c4a68`; class vtable `0xfffffe00082c44a0`
- Registration (init): `0xfffffe0009bf0f34`
- Superclasses: [`IODMAController`](IODMAController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AudioDMAController` in [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['admac,v5p0', 'admac-evolution,v5p0']`

## Device-tree nodes it binds (6) [DT]

- [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) on `admac,v5p0`
- [`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) on `admac,v5p0`
- [`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) on `admac-evolution,v5p0`
- [`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) on `admac-evolution,v5p0`
- [`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) on `admac-evolution,v5p0`
- [`/arm-io/admac-leap-s`](../devicetree/root__arm-io__admac-leap-s.md) on `admac-evolution,v5p0`

## Strings in its kext that name it (12)

- `virtual bool AudioDMAController::start(IOService *)`
- `site.AudioDMAController`
- `/Library/Caches/com.apple.xbs/EDB52463-4048-495D-AB86-88E13335F3E1/TemporaryDirectory.lXLcfx/Sources/AudioDMAController/v5p0/Kext/AudioDMAController/AudioDMAController.cpp`
- `AudioDMAController`
- `/Library/Caches/com.apple.xbs/EDB52463-4048-495D-AB86-88E13335F3E1/TemporaryDirectory.lXLcfx/Sources/AudioDMAController/v5p0/Kext/AudioDMAChannel/AudioDMAChannelStateMachine.cpp`
- `powerStateOrdinal < kAudioDMAControllerPowerStateInvalid`
- `/Library/Caches/com.apple.xbs/EDB52463-4048-495D-AB86-88E13335F3E1/TemporaryDirectory.lXLcfx/Sources/AudioDMAController/v5p0/Kext/Interrupt/IOInterruptQueueEventSource.cpp`
- `%s::%s _gatePower(kAudioDMAControllerPowerStateAvailable) failed with %s.`
- `bool AudioDMAController::_filterInterruptAction(IOFilterInterruptEventSource *)`
- `%s::%s _gatePower(kAudioDMAControllerPowerStateSuspended) failed with %s.`
- `AudioDMAController.cpp`
- `void AudioDMAController::_admaInterruptAction(IOInterruptEventSource *, int32_t)`
