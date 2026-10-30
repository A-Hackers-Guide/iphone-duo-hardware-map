# `RTBuddyCrashlogEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x130` (304 bytes)
- Metaclass: `0xfffffe000ba23d88`; metaclass vtable `0xfffffe0008495bf0`; class vtable `0xfffffe0008495698`
- Registration (init): `0xfffffe000a934690`
- Superclasses: [`RTBuddyBuiltinEndpoint`](RTBuddyBuiltinEndpoint.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (8)

- `RTBuddyCrashlogEndpoint`
- `site.RTBuddyCrashlogEndpoint`
- `RTBuddyCrashlogEndpoint.cpp`
- `IOReturn RTBuddyCrashlogEndpoint::_synchronize(IsPolling, bool, IOCommandGate::Action, void *, void *, void *, void *)`
- `void RTBuddyCrashlogEndpoint::setCrashlogBufferAddress(IOPhysicalAddress, size_t)`
- `void RTBuddyCrashlogEndpoint::_messageHandler(void *, void *)`
- `void RTBuddyCrashlogEndpoint::_allocateLocalBuffer()`
- `IOReturn RTBuddyCrashlogEndpoint::_checkForCrashGated(uintptr_t)`
