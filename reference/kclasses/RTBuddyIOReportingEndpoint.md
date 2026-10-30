# `RTBuddyIOReportingEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000ba23d10`; metaclass vtable `0xfffffe0008494eb8`; class vtable `0xfffffe0008494960`
- Registration (init): `0xfffffe000a9316a4`
- Superclasses: [`RTBuddyBuiltinEndpoint`](RTBuddyBuiltinEndpoint.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (11)

- `IOReporter *RTBuddyIOReportingEndpoint::_addReporter(const io_reporting_reporter_t &, OSBoundedPtr<const uint8_t>)`
- `IOReturn RTBuddyIOReportingEndpoint::_updateRemoteReportersGated()`
- `RTBuddyIOReportingEndpoint.cpp`
- `site.RTBuddyIOReportingEndpoint`
- `void RTBuddyIOReportingEndpoint::_messageHandler(void *, void *)`
- `bool RTBuddyIOReportingEndpoint::_initWithOptions(IOSlaveProcessor *)`
- `IOReporter *RTBuddyIOReportingEndpoint::_getReporter(uint64_t)`
- `RTBuddyIOReportingEndpoint`
- `void RTBuddyIOReportingEndpoint::_apInitiatedUpdateGated()`
- `virtual bool RTBuddyIOReportingEndpoint::start(IOService *)`
- `nullptr != (_epIOReporting = RTBuddyIOReportingEndpoint::withOptions(this))`
