# `ANEHWDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md)
- Object size: `0xe698` (59,032 bytes)
- Metaclass: `0xfffffe000b94c4b8`; metaclass vtable `0xfffffe00080c6870`; class vtable `0xfffffe00080c60d8`
- Registration (init): `0xfffffe0008df2cd0`
- Superclasses: [`ANEDeviceInterface`](ANEDeviceInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`H11ANEIn`](H11ANEIn.md) — `com.apple.driver.AppleH16ANEInterface`

## Strings in its kext that name it (37)

- `ANEHWDevice`
- `\"ANEHWDevice::ANE Timeout panic because fFirmwareTimeoutRecoverySupported: %u\\n\" @%s:%d`
- `void ANEScheduler::panicOnRequestTimeout(ANEHWDevice *, ANEInferenceRequest &)`
- `\"ANEHWDevice::ANECPU ANE%d: %s\" @%s:%d`
- `ANEHWDeviceCallbackThread`
- `ANEHWDeviceClientNotificationMsg`
- `IOReturn ANEHWDevice::ANE_MapMPMMemoryAtOffset(uint64_t, uint64_t)`
- `IOReturn ANEHWDevice::ANE_UnmapMPMMemory_gated(uint64_t, IOBufferMemoryDescriptor *)`
- `ANEHWDevice: program digest SHA256 : %d`
- `\"%s :ANEHWDevice: ffw_calloc failed. Size not supported as it is not size of sIOProcessorChannelDescriptor size=%d, count=%d\\n\" @%s:%d`
- `void ANEHWDeviceConfig::initializeANESoCConfig(const AppleARMIODevice *, ANEHWDevice *)`
- `ANEHWDeviceClientNotificationHandler`
- `ANEHWDevice::ANECPU ANE%d: %s`
- `\"ANE%u: ANEHWDevice::ANE Timeout panic fANEFirmwareEnablePanicOnTimeout=%d unitTestMode=%d\\n\" @%s:%d`
- `IOReturn ANEHWDevice::ANE_startDaemon_gated()`
- `site.ANEHWDeviceClientNotificationMsg`
- `\"ANEHWDevice::Failed to validate ANE register offset %#x with expected value: %#x, read register value %#x\\n\" @%s:%d`
- `site.ANEHWDevice`
- `void *ANEHWDevice::aneAddressToHostAddress(uint64_t)`
- `IOReturn ANEHWDevice::ANE_MapMPMMemory_gated(uint64_t, IOBufferMemoryDescriptor *)`
- `ANEHWDevice - DART Exception - End Logging\n`
- `ANEHWDeviceTimeoutMsg`
- `ANEHWDeviceConfig`
- `site.ANEHWDeviceConfig`
- `static void ANEHWDevice::doorBellRing(void *)`
- `uint32_t ANEHWDevice::getHwRegisterOffset(uint32_t)`
- `site.ANEHWDeviceTimeoutMsg`
- `\"%s :ANEHWDevice: ffw_free failed. Size not supported as it is not a multiple of sIOProcessorChannelDescriptor size=%zu struct size=%zu, count=%zu\\n\" @%s:%d`
- `ANEHWDevice.cpp`
- `\"ANE%u: ANEHWDevice::ANE Timeout: channel=%s cmd=0x%04X (%s), waited=%u ms, timeout=%u ms, fANEFirmwareEnablePanicOnTimeout=%d unitTestMode=%d\\n\" @%s:%d`
- `ANE%d: %s :ANEHWDevice::ANE_startDaemon_gated, start aned daemon\n`
- `[ERROR] %s: %s: ANEHWDevice does not have ANEClientDeviceCore initialized\n`
- `[ERROR] %s: %s: Failed to create ANEHWDeviceTimeoutMsg\n`
- `ANE%d:%s :ANEHWDevice::doorBellRing %d - We don't support more than %d doorbells currently\n`
- `%s: %s: Couldn't register ANEHWDevice as AppleARMFunction parent\n`
- `ANEHWDevice::ANECPU ANE%d: %s`
- `%s: %s: ANEHWDevice::Failed to validate ANE register offset %#x with expected value: %#x, read register value %#x\n`
