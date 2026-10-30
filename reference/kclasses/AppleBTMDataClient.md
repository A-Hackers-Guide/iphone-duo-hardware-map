# `AppleBTMDataClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md)
- Object size: `0x48` (72 bytes)
- Metaclass: `0xfffffe000b989098`; metaclass vtable `0xfffffe00081a72f8`; class vtable `0xfffffe00081a7258`
- Registration (init): `0xfffffe00093dc69c`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (2; 2 in total)

- [`AppleBTMDataClientPPM`](AppleBTMDataClientPPM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleBTMDataClientSMC`](AppleBTMDataClientSMC.md) — `com.apple.driver.ApplePhoneBTM`

## Strings in its kext that name it (19)

- `AppleBTMDataClientPPM`
- `site.AppleBTMDataClientSMC`
- `AppleBTMDataClientSMC.cpp`
- `AppleBTMDataClient`
- `values[i] < kAppleBTMDataClientCount`
- `site.AppleBTMDataClientPPM`
- `AppleBTMDataClient.cpp`
- `void AppleBTMDataClient::publish(void *)`
- `AppleBTMDataClientSMC`
- `count <= kAppleBTMDataClientCount`
- `AppleBTMDataClientPPM.cpp`
- `virtual IOReturn AppleBTMDataClientSMC::initialize(IOService *, OSObject *)`
- `virtual IOReturn AppleBTMDataClientPPM::publishSynchronous(OSArray *)`
- `site.AppleBTMDataClient`
- `static void AppleBTMDataClientPPM::eventHandler(OSObject *, IOInterruptEventSource *, int)`
- `virtual IOReturn AppleBTMDataClientPPM::initialize(IOService *, OSObject *)`
- `static bool AppleBTMDataClientSMC::serviceMatchNotification(void *, void *, IOService *, IONotifier *)`
- `static bool AppleBTMDataClientPPM::serviceMatchNotification(void *, void *, IOService *, IONotifier *)`
- `static void AppleBTMDataClientSMC::eventHandler(OSObject *, IOInterruptEventSource *, int)`
