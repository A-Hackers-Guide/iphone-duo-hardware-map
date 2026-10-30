# `CoreAnalyticsUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.CoreAnalyticsFamily`](../kexts/com.apple.iokit.CoreAnalyticsFamily.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b9df440`; metaclass vtable `0xfffffe00082c8658`; class vtable `0xfffffe00082c8070`
- Registration (init): `0xfffffe0009c0a6ac`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (20)

- `CoreAnalyticsUserClient`
- `IOReturn CoreAnalyticsHub::setClientGated(CoreAnalyticsUserClient *)`
- `virtual bool CoreAnalyticsUserClient::start(IOService *)`
- `virtual bool CoreAnalyticsUserClient::didTerminate(IOService *, IOOptionBits, bool *)`
- `site.CoreAnalyticsUserClient`
- `virtual IOReturn CoreAnalyticsUserClient::clientDied()`
- `static IOReturn CoreAnalyticsUserClient::goto_configureFilter(CoreAnalyticsUserClient *, void *, IOExternalMethodArguments *)`
- `virtual void CoreAnalyticsUserClient::stop(IOService *)`
- `virtual IOReturn CoreAnalyticsUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `virtual IOReturn CoreAnalyticsUserClient::registerNotificationPort(mach_port_t, UInt32, io_user_reference_t)`
- `virtual void CoreAnalyticsUserClient::free()`
- `virtual IOReturn CoreAnalyticsUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `virtual bool CoreAnalyticsUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `IOReturn CoreAnalyticsUserClient::sendDataToUser(uint8_t *, size_t)`
- `virtual IOReturn CoreAnalyticsUserClient::clientClose()`
- `bool CoreAnalyticsUserClient::checkEntitlement(task_t)`
- `%s::%d:CoreAnalyticsUserClient::didTerminate\n`
- `%s::%d:unregistering from _hub, and clearing _hub reference to CoreAnalyticsUserClient\n`
- `%s::%d:CoreAnalyticsUserClient::registerNotificationPort _notificationPort is unexpectedly already set\n`
- `%s::%d:CoreAnalyticsUserClient::externalMethod bad selector %d\n`
