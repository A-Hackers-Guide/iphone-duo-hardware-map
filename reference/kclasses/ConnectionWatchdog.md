# `ConnectionWatchdog`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AUC`](../kexts/com.apple.AUC.md)
- Object size: `0x70` (112 bytes)
- Metaclass: `0xfffffe000b932070`; metaclass vtable `0xfffffe0007f94860`; class vtable `0xfffffe0007f947d0`
- Registration (init): `0xfffffe000866a3a8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (9)

- `ConnectionWatchdog`
- `IOReturn AUC::hdcp_send_request_gated(const uint8_t *, size_t, ConnectionWatchdog *)`
- `site.ConnectionWatchdog`
- `%s create ConnectionWatchdog [%p]`
- `%s [%p]::%s, created ConnectionWatchdog object \n`
- `%s [%p]::%s, Releasing mStaleConnectionWatchdog_DP object\n`
- `%s [%p]::%s: can't allocate ConnectionWatchdog\n`
- `%s [%p]::%s, Storing mConnectionWatchdog_DP to mStaleConnectionWatchdog_DP object\n`
- `%s %s: ConnectionWatchdog message timer waking up...\n`
