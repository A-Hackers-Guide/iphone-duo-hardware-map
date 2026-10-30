# `RTBuddyEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000ba23cc0`; metaclass vtable `0xfffffe00084942d8`; class vtable `0xfffffe00084941c0`
- Registration (init): `0xfffffe000a92f24c`
- Superclasses: [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Direct subclasses (4; 4 in total)

- [`RTBuddyKdebugEndpoint`](RTBuddyKdebugEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyManagementEndpoint`](RTBuddyManagementEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyOSLogEndpoint`](RTBuddyOSLogEndpoint.md) — `com.apple.driver.RTBuddy`
- [`RTBuddySyslogEndpoint`](RTBuddySyslogEndpoint.md) — `com.apple.driver.RTBuddy`

## Strings in its kext that name it (9)

- `%s:%d Assertion failed: %s : RTBuddyEndpointService doesn't work with built-in endpoints: %u\n`
- `RTBuddyEndpoint.cpp`
- `site.RTBuddyEndpointService`
- `site.RTBuddyEndpointPSEventSource`
- `RTBuddyEndpoint *RTBuddy::createEndpoint(unsigned int)`
- `RTBuddyEndpointPSEventSource`
- `RTBuddyEndpointService`
- `RTBuddyEndpoint`
- `site.RTBuddyEndpoint`
