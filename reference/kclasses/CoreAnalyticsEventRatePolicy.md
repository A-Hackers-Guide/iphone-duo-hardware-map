# `CoreAnalyticsEventRatePolicy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.CoreAnalyticsFamily`](../kexts/com.apple.iokit.CoreAnalyticsFamily.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9df370`; metaclass vtable `0xfffffe00082c6c10`; class vtable `0xfffffe00082c6b80`
- Registration (init): `0xfffffe0009c05490`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (7)

- `bool CoreAnalyticsEventRatePolicy::initWithWorkloop(IOWorkLoop *)`
- `void CoreAnalyticsEventRatePolicy::sendBudgetExceededReport()`
- `CoreAnalyticsEventRatePolicy`
- `uint32_t CoreAnalyticsEventRatePolicy::incrementCountForEvent(OSString *)`
- `site.CoreAnalyticsEventRatePolicy`
- `void CoreAnalyticsEventRatePolicy::zeroOutPerEventCounts()`
- `void CoreAnalyticsEventRatePolicy::createBudgetDicts(OSArray *) const`
