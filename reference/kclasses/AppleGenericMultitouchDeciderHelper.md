# `AppleGenericMultitouchDeciderHelper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9467f8`; metaclass vtable `0xfffffe00080b97b0`; class vtable `0xfffffe00080b9720`
- Registration (init): `0xfffffe0008d190f0`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (13)

- `void AppleGenericMultitouchDeciderHelper::setAuthCPService(IOService *)`
- `void AppleGenericMultitouchDeciderHelper::trustStateDetermined(bool)`
- `void AppleGenericMultitouchDeciderHelper::authenticityStateDetermined(bool)`
- `bool AppleGenericMultitouchDeciderHelper::processStatesReady()`
- `site.AppleGenericMultitouchDeciderHelper`
- `AppleGenericMultitouchDeciderHelper *AppleGenericMultitouchDecider::findHelperForInterface(UInt32)`
- `IOReturn AppleGenericMultitouchDecider::helperStateChangedGated(AppleGenericMultitouchDeciderHelper *)`
- `bool AppleGenericMultitouchDeciderHelper::init(StateChangedCallback, void *, UInt32, IORegistryEntry *)`
- `AppleGenericMultitouchDeciderHelper`
- `IOReturn AppleGenericMultitouchDeciderHelper::authCPInterest(void *, UInt32, IOService *, void *, vm_size_t)`
- `void AppleGenericMultitouchDeciderHelper::checkBootArgs()`
- `virtual void AppleGenericMultitouchDeciderHelper::free()`
- `static void AppleGenericMultitouchDecider::helperStateChangedCallback(AppleGenericMultitouchDeciderHelper *, void *)`
