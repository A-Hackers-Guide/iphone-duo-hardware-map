# `ApplePPMEntity`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x80` (128 bytes)
- Metaclass: `0xfffffe000b9dbe28`; metaclass vtable `0xfffffe00082bbf90`; class vtable `0xfffffe00082bbe80`
- Registration (init): `0xfffffe0009b8c3a0`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (22)

- `virtual IOReturn ApplePPM::startActivity(ApplePPMEntity *, uint32_t)`
- `virtual uint32_t ApplePPMEntity::getCurrentBudget()`
- `ApplePPMEntity *ApplePPMKernelClient::getEntityForSubclientIndex(int)`
- `ApplePPMEntity`
- `virtual bool ApplePPMEntity::pushTelemetry(OSDictionary *)`
- `bool ApplePPM::removeEntity(ApplePPMEntity *)`
- `virtual bool ApplePPMEntity::init(ApplePPM *, ApplePPMClientProperties *, ApplePPMKernelClient *)`
- `uint32_t ApplePPM::getObjectIndexFromEntityArray(ApplePPMEntity *)`
- `static ApplePPMEntity *ApplePPMEntity::withParentAndClientProperties(ApplePPM *, ApplePPMClientProperties *, ApplePPMKernelClient *)`
- `site.ApplePPMEntity`
- `virtual bool ApplePPM::addNewEntity(ApplePPMEntity *)`
- `virtual uint32_t ApplePPMEntity::getRequestedBudget()`
- `ApplePPMEntity *ApplePPMKernelClient::getEntityForClientId(uint8_t)`
- `OSDictionary *ApplePPMEntity::copyClientProperties()`
- `virtual IOReturn ApplePPMCPMS::admissionCheckOfValue(ApplePPMEntity *, CPMSPPMPowerBudget *, CPMSPPMPowerBudget *, bool)`
- `ApplePPMEntity *ApplePPM::getEntityFromClientId(UniqueClientID_t)`
- `virtual void ApplePPMEntity::initBudgetReporter()`
- `virtual void ApplePPM::updateActiveEntityList(ApplePPMEntity *)`
- `virtual IOReturn ApplePPM::stopActivity(ApplePPMEntity *)`
- `ApplePPMEntity.cpp`
- `virtual PowerLevelProfile *ApplePPMEntity::getCurrentPowerLevel()`
- `void ApplePPMEntity::populateTGraphClientData(ApplePPMTGraphClientData *)`
