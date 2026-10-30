# `AppleGenericMultitouchDecider`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b946820`; metaclass vtable `0xfffffe00080b9da0`; class vtable `0xfffffe00080b9848`
- Registration (init): `0xfffffe0008d1912c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `Decider - DockChannel` in [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md): `IOProviderClass` = `AppleDockChannelDevice`, `IONameMatch` = `gen-mt-decider`
- `Decider - Mailbox` in [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['MTPEndpoint1']`
- `Decider - SPI` in [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md): `IOProviderClass` = `AppleARMSPIDevice`, `IONameMatch` = `gen-mt-decider`

## Strings in its kext that name it (33)

- `void AppleGenericMultitouchDeciderHelper::setAuthCPService(IOService *)`
- `void AppleGenericMultitouchDeciderHelper::trustStateDetermined(bool)`
- `void AppleGenericMultitouchDecider::recordUltimateDecision(bool, bool)`
- `virtual bool AppleGenericMultitouchDecider::start(IOService *)`
- `site.AppleGenericMultitouchDecider`
- `void AppleGenericMultitouchDeciderHelper::authenticityStateDetermined(bool)`
- `bool AppleGenericMultitouchDeciderHelper::processStatesReady()`
- `bool AppleGenericMultitouchDecider::setupMatchingCallback()`
- `static bool AppleGenericMultitouchDecider::launchIOService(const char *, IOService *)`
- `site.AppleGenericMultitouchDeciderHelper`
- `bool AppleGenericMultitouchDecider::createDeciderHelpers()`
- `auto AppleGenericMultitouchDecider::createDeciderHelpers()::(anonymous class)::operator()(IORegistryEntry *) const`
- `/Library/Caches/com.apple.xbs/18870140-AD72-47E9-90F7-D7C84661AAD4/TemporaryDirectory.zANmYd/Sources/AppleGenericMultitouch/Kext/AppleGenericMultitouchDecider.cpp`
- `virtual void AppleGenericMultitouchDecider::stop(IOService *)`
- `const char *AppleGenericMultitouchDecider::getInterfaceNameForIndex(UInt32)`
- `bool AppleGenericMultitouchDecider::authCPMatched(void *, IOService *, IONotifier *)`
- `AppleGenericMultitouchDeciderHelper *AppleGenericMultitouchDecider::findHelperForInterface(UInt32)`
- `IOReturn AppleGenericMultitouchDecider::helperStateChangedGated(AppleGenericMultitouchDeciderHelper *)`
- `void AppleGenericMultitouchDecider::processAllStatesReady()`
- `bool AppleGenericMultitouchDeciderHelper::init(StateChangedCallback, void *, UInt32, IORegistryEntry *)`
- `virtual IOService *AppleGenericMultitouchDecider::probe(IOService *, SInt32 *)`
- `bool AppleGenericMultitouchDecider::areAllStatesDetermined()`
- `AppleGenericMultitouchDeciderHelper`
- `AppleGenericMultitouchDecider`
- `IOReturn AppleGenericMultitouchDeciderHelper::authCPInterest(void *, UInt32, IOService *, void *, vm_size_t)`
- `void AppleGenericMultitouchDeciderHelper::checkBootArgs()`
- `auto AppleGenericMultitouchDecider::start(IOService *)::(anonymous class)::operator()(AppleGenericMultitouchDecider *) const`
- `virtual void AppleGenericMultitouchDeciderHelper::free()`
- `static void AppleGenericMultitouchDecider::helperStateChangedCallback(AppleGenericMultitouchDeciderHelper *, void *)`
- `[Decider] Starting AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Stopping AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Stopped AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Successfully started AppleGenericMultitouchDecider\n%s line %d`
