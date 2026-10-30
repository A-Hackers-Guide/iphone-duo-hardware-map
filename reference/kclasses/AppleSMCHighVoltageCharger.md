# `AppleSMCHighVoltageCharger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0x208` (520 bytes)
- Metaclass: `0xfffffe000b99b690`; metaclass vtable `0xfffffe0008203a00`; class vtable `0xfffffe00082034a8`
- Registration (init): `0xfffffe000968a5e8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCHighVoltageCharger` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['portmicro,smc-ccg2']`, `IOProbeScore` = `1000`

## Strings in its kext that name it (7)

- `IOReturn AppleSMCHighVoltageCharger::receiveNotification(void *, UInt32, IOService *, void *, vm_size_t)`
- `void AppleSMCHighVoltageCharger::_interruptAction(uint8_t, uint8_t)`
- `AppleSMCHighVoltageCharger`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCHighVoltageCharger/AppleSMCHighVoltageCharger.cpp`
- `site.AppleSMCHighVoltageCharger`
- `AppleSMCHighVoltageCharger.cpp`
- `AppleSMCHighVoltageCharger::%s: self=%p event=%x arg=%x\n`
