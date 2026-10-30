# `RTBuddyBuiltinEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000ba240b0`; metaclass vtable `0xfffffe00084996c0`; class vtable `0xfffffe0008499168`
- Registration (init): `0xfffffe000a949b3c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (5; 5 in total)

- [`RTBuddyCoreAnalyticsEndpoint`](RTBuddyCoreAnalyticsEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyCrashlogEndpoint`](RTBuddyCrashlogEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyEntropyEndpoint`](RTBuddyEntropyEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyIOReportingEndpoint`](RTBuddyIOReportingEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyTraceKitEndpoint`](RTBuddyTraceKitEndpoint.md) — `com.apple.driver.RTBuddy`

## Strings in its kext that name it (4)

- `bool RTBuddyBuiltinEndpoint::initWithOptions(IOSlaveProcessor *, IOSlaveEndpoint::Action, void *, uint32_t, const char *, unsigned int)`
- `site.RTBuddyBuiltinEndpoint`
- `RTBuddyBuiltinEndpoint`
- `RTBuddyBuiltinEndpoint.cpp`
