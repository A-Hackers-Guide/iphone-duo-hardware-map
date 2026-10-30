# `AppleCotaBTM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b988fd0`; metaclass vtable `0xfffffe00081a6550`; class vtable `0xfffffe00081a6420`
- Registration (init): `0xfffffe00093d9364`
- Superclasses: [`AppleBTMPMUAgent`](AppleBTMPMUAgent.md)

## Direct subclasses (3; 4 in total)

- [`AppleAintreeBTM`](AppleAintreeBTM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleBakuBTM`](AppleBakuBTM.md) — `com.apple.driver.ApplePhoneBTM`
- [`AppleEstBTM`](AppleEstBTM.md) — `com.apple.driver.ApplePhoneBTM`

## Strings in its kext that name it (14)

- `IOReturn AppleCotaBTM::PMUInterruptHandler(IOInterruptEventSource *, int)`
- `IOReturn AppleCotaBTM::readPICtrl()`
- `AppleCotaBTM::start success\n`
- `AppleCotaBTM::start (%p)\n`
- `IOReturn AppleCotaBTM::readLowVoltageResidency()`
- `virtual bool AppleCotaBTM::initWithProvider(IOService *)`
- `virtual IOReturn AppleCotaBTM::resetWorstCaseIVTrigger()`
- `virtual IOReturn AppleCotaBTM::configSampling()`
- `site.AppleCotaBTM`
- `IOReturn AppleCotaBTM::readDutyCycles()`
- `AppleCotaBTM.cpp`
- `AppleCotaBTM`
- `virtual IOReturn AppleCotaBTM::readSamples()`
- `static AppleCotaBTM *AppleCotaBTM::withParent(AppleBTM *, IOService *)`
