# `CoreAnalyticsHub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.CoreAnalyticsFamily`](../kexts/com.apple.iokit.CoreAnalyticsFamily.md)
- Object size: `0x148` (328 bytes)
- Metaclass: `0xfffffe000b9df3a0`; metaclass vtable `0xfffffe00082c7200`; class vtable `0xfffffe00082c6ca8`
- Registration (init): `0xfffffe0009c081fc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `CoreAnalyticsHub` in [`com.apple.iokit.CoreAnalyticsFamily`](../kexts/com.apple.iokit.CoreAnalyticsFamily.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `CoreAnalyticsHub`

## Strings in its kext that name it (36)

- `IOReturn CoreAnalyticsHub::createReporters()`
- `CoreAnalyticsHub`
- `IOReturn CoreAnalyticsHub::setClientGated(CoreAnalyticsUserClient *)`
- `void CoreAnalyticsHub::handleDemoTimerExpiry(IOTimerEventSource *)`
- `IOReturn CoreAnalyticsHub::serializePayload(OSObject *, OSSerialize *, size_t *)`
- `virtual void CoreAnalyticsHub::free()`
- `virtual void CoreAnalyticsHub::close(IOService *, IOOptionBits)`
- `virtual void CoreAnalyticsHub::stop(IOService *)`
- `void CoreAnalyticsHub::incrementEventNameSerializeTooLarge(OSString *)`
- `IOReturn CoreAnalyticsHub::__newUserClientGated(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `%s::%d:CoreAnalyticsHub start completed\n`
- `IOReturn CoreAnalyticsHub::setupNewUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient *)`
- `IOReturn CoreAnalyticsHub::sendUpEventAndPayload(OSString *, OSObject *)`
- `void CoreAnalyticsHub::incrementEventNameRateLimit(OSString *)`
- `void CoreAnalyticsHub::testDemoOversizedMessage()`
- `void CoreAnalyticsHub::incrementEventNameSerializeFailure(OSString *)`
- `%s::%d:CoreAnalyticsHub start\n`
- `%s::%d:CoreAnalyticsHub stop\n`
- `site.CoreAnalyticsHub`
- `void CoreAnalyticsHub::incrementEventNameSharedDataQueueFull(OSString *)`
- `uint64_t CoreAnalyticsHub::getIndexForEventName(OSString *)`
- `%s::%d:CoreAnalyticsHub failed to successfully start\n`
- `void CoreAnalyticsHub::testDemoNormalMessage()`
- `%s::%d:gCoreAnalyticsHub is NULL, returning kIOReturnNotReady\n`
- `void CoreAnalyticsHub::incrementEventNameFailed(OSString *)`
- `virtual bool CoreAnalyticsHub::start(IOService *)`
- `%s::%d:CoreAnalyticsHub free\n`
- `void CoreAnalyticsHub::incrementEventNameReceived(OSString *)`
- `void CoreAnalyticsHub::handleNagTimerExpiry(IOTimerEventSource *)`
- `void CoreAnalyticsHub::handleUserClientRetryTimerExpiry(IOTimerEventSource *)`
- `%s::%d:gCoreAnalyticsHub is NULL, returning kIOReturnNotReady\n`
- `%s::%d:CoreAnalyticsHub free\n`
- `%s::%d:CoreAnalyticsHub stop\n`
- `%s::%d:CoreAnalyticsHub failed to successfully start\n`
- `%s::%d:CoreAnalyticsHub start completed\n`
- `%s::%d:CoreAnalyticsHub start\n`
