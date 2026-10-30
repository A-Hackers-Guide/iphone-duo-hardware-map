# `ApplePPMKernelClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x50` (80 bytes)
- Metaclass: `0xfffffe000b9dbea0`; metaclass vtable `0xfffffe00082bd660`; class vtable `0xfffffe00082bd560`
- Registration (init): `0xfffffe0009b95294`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (20)

- `site.ApplePPMKernelClient`
- `ApplePPMKernelClient.cpp`
- `virtual IOReturn ApplePPMKernelClient::getMinMaxClientPowerPolicy(uint8_t, clientPowerPolicyRange *)`
- `virtual IOReturn ApplePPMKernelClient::ackClientBudget(CPMSPPMPowerBudgetAck *)`
- `ApplePPMEntity *ApplePPMKernelClient::getEntityForSubclientIndex(int)`
- `virtual IOReturn ApplePPMKernelClient::setBudgetWithValue(void *, uint32_t, uint32_t)`
- `ApplePPMKernelClient`
- `virtual bool ApplePPMEntity::init(ApplePPM *, ApplePPMClientProperties *, ApplePPMKernelClient *)`
- `static ApplePPMEntity *ApplePPMEntity::withParentAndClientProperties(ApplePPM *, ApplePPMClientProperties *, ApplePPMKernelClient *)`
- `virtual IOReturn ApplePPMKernelClient::admissionCheckWithValue(CPMSPPMPowerBudget *, CPMSPPMPowerBudget *, uint32_t)`
- `IOReturn ApplePPMCPMS::processClientRegistration(ApplePPM *, IOService *, ApplePPMKernelClient::ClientInfoData *, ApplePPMKernelClient *, bool)`
- `virtual IOReturn ApplePPMKernelClient::admissionCheckWithValue(uint32_t, uint32_t, uint32_t *)`
- `virtual IOReturn ApplePPMKernelClient::setBudgetWithValueMultiClient(void *)`
- `ApplePPMEntity *ApplePPMKernelClient::getEntityForClientId(uint8_t)`
- `bool ApplePPM::mapClientAndEntity(OSObject *, bool, ApplePPMKernelClient::ClientInfoData *)`
- `virtual IOReturn ApplePPMKernelClient::pushTelemetry(uint32_t, OSDictionary *)`
- `virtual IOReturn ApplePPMKernelClient::endInteraction()`
- `static ApplePPMKernelClient *ApplePPMKernelClient::withParentAndClient(ApplePPM *, IOService *, ApplePPMKernelClient::ClientInfoData *, uint8_t)`
- `bool ApplePPM::createAndAddEntity(ApplePPMClientProperties *, ApplePPMKernelClient *)`
- `virtual IOReturn ApplePPMKernelClient::setBudgetWithValue(uint32_t, uint32_t, uint32_t)`
