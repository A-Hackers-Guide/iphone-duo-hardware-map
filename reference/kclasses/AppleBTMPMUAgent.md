# `AppleBTMPMUAgent`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md)
- Object size: `0x230` (560 bytes)
- Metaclass: `0xfffffe000b989070`; metaclass vtable `0xfffffe00081a71c0`; class vtable `0xfffffe00081a7098`
- Registration (init): `0xfffffe00093dc0c4`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (5; 18 in total)

- [`AppleAvusBTM`](AppleAvusBTM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleBTMAONPMUAgent`](AppleBTMAONPMUAgent.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleCotaBTM`](AppleCotaBTM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleFermiumBTM`](AppleFermiumBTM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleSeraBTM`](AppleSeraBTM.md) — `com.apple.driver.ApplePhoneBTM`

## Strings in its kext that name it (10)

- `AppleBTMPMUAgent::free\n`
- `AppleBTMPMUAgent`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: spec input is NULL\" @%s:%d`
- `AppleBTMPMUAgent.cpp`
- `site.AppleBTMPMUAgent`
- `void AppleBTMPMUAgent::ppmArrivalHandler(IOService *)`
- `bool AppleBTMPMUAgent::initWithParent(AppleBTM *, IOService *)`
- `void AppleBTMPMUAgent::initializePmuSampleSpec(int, const pmuDataLayout *)`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: length %d exceeds maximum %d\" @%s:%d`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: length == 0\" @%s:%d`
