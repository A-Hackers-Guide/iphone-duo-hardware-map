# `AKSAnalytics`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.security.AKSAnalytics`](../kexts/com.apple.security.AKSAnalytics.md)
- Object size: `0x1a8` (424 bytes)
- Metaclass: `0xfffffe000b931a70`; metaclass vtable `0xfffffe0007f86350`; class vtable `0xfffffe0007f85df8`
- Registration (init): `0xfffffe0008608ce8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AKSAnalytics` in [`com.apple.security.AKSAnalytics`](../kexts/com.apple.security.AKSAnalytics.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AKSAnalytics`

## Strings in its kext that name it (26)

- `void AKSAnalytics::enqueueEvent(DPSerializedEvent)`
- `virtual void AKSAnalyticsUserClient::stop(IOService *)`
- `void AKSAnalyticsUserClient::configureAnalytics(uint64_t)`
- `AKSAnalytics.cpp`
- `site.AKSAnalytics`
- `virtual IOReturn AKSAnalyticsUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `AKSAnalytics Kext`
- `bool AKSAnalytics::drainEventQueues()`
- `void AKSAnalytics::lockStateThreadCallHandler(keybag_handle_t)`
- `Failed to start AKSAnalytics`
- `AKSAnalytics stopping`
- `void AKSAnalytics::registerLockNotificationsAsync()_block_invoke_2`
- `virtual bool AKSAnalyticsUserClient::start(IOService *)`
- `AKSAnalytics started`
- `site.AKSAnalyticsUserClient`
- `\"invalid AKSAnalytics event category %u\" @%s:%d`
- `AKSAnalyticsUserClient`
- `detected multiple instances of AKSAnalytics driver`
- `IOReturn AKSAnalyticsUserClient::sendDataToUser(uint8_t *, size_t)`
- `virtual IOReturn AKSAnalyticsUserClient::clientClose()`
- `AKSAnalytics built %s %s\n`
- `AKSAnalytics`
- `%s: AKSAnalytics user client started\n`
- `%s: AKSAnalytics user client stopping\n`
- `AKSAnalytics notification port initialized to %p\n`
- `%s: AKSAnalytics user client closing\n`
