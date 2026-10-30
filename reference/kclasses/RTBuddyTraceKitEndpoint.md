# `RTBuddyTraceKitEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000ba24060`; metaclass vtable `0xfffffe0008498d98`; class vtable `0xfffffe0008498838`
- Registration (init): `0xfffffe000a949418`
- Superclasses: [`RTBuddyBuiltinEndpoint`](RTBuddyBuiltinEndpoint.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (19)

- `void RTBuddyTraceKitEndpoint::_setEndpointActiveGated(bool)`
- `IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)`
- `virtual void RTBuddyTraceKitEndpoint::kdebugCallback(kd_callback_type, void *)`
- `IOReturn RTBuddyTraceKitEndpoint::releaseChunkCPUTrace(rtbuddy_cputrace_chunk_t)_block_invoke`
- `void RTBuddyTraceKitEndpoint::_waitForStateTransitionsGated()`
- `site.RTBuddyTraceKitEndpoint`
- `void RTBuddyTraceKitEndpoint::_waitForOutstandingRequestsGated()`
- `RTBuddyTraceKitEndpoint.cpp`
- `IOReturn RTBuddyTraceKitEndpoint::_hostVersionGated()`
- `void RTBuddyTraceKitEndpoint::_waitForBusyACKGated(void *)`
- `IOReturn RTBuddyTraceKitEndpoint::attach(rtbuddy_trace_attach_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke`
- `IOReturn RTBuddyTraceKitEndpoint::_resetGated()`
- `IOReturn RTBuddyTraceKitEndpoint::_powerStateCallbackGated(const unsigned long *, const unsigned long *)`
- `IOReturn RTBuddyTraceKitEndpoint::_unconfigureGated()`
- `IOReturn RTBuddyTraceKitEndpoint::_enableGated(const bool)`
- `IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke`
- `RTBuddyTraceKitEndpoint`
- `IOReturn RTBuddyTraceKitEndpoint::_flushGated()`
- `void RTBuddyTraceKitEndpoint::_waitForEndpointActiveGated()`
