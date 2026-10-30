# `ApplePMP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md)
- Object size: `0x220` (544 bytes)
- Metaclass: `0xfffffe000b987cb0`; metaclass vtable `0xfffffe0008198488`; class vtable `0xfffffe0008197f30`
- Registration (init): `0xfffffe000936835c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePMP` in [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `PMPEndpoint1`

## Strings in its kext that name it (59)

- `site.ApplePMPv2RegistryEntry`
- `static IOReturn ApplePMPUserClient::_getNumDVFSDomains(OSObject *, void *, IOExternalMethodArguments *)`
- `\"ApplePMPUserClient: %s:%u REQUIRE failed: %s\" @%s:%d`
- `static IOReturn ApplePMPUserClient::_pmuTelemetryEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPThermal`
- `IOReturn ApplePMP::_sendEHubNodeCommand(UInt32, UInt64)`
- `static IOReturn ApplePMPUserClient::_pBattDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual bool ApplePMP::start(IOService *)`
- `ApplePMPUserClient.cpp`
- `void ApplePMP::_pmonMessageHandler(mbi_msg_t)`
- `static IOReturn ApplePMPUserClient::_fastDieControllerDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPThermalUserClient`
- `IOReturn ApplePMP::_powerStateHandlerGated(void *, void *, void *)`
- `static IOReturn ApplePMPUserClient::_pBattEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPThermal`
- `/ApplePMP/ApplePMPv2UserClient.cpp`
- `void ApplePMP::_pBattMessageHandler(mbi_msg_t)`
- `site.ApplePMPv2UserClient`
- `static IOReturn ApplePMPUserClient::_fastDieControllerSetLifeTimeServoTempTarget(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_samplerEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_ping(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_setDVFSStates(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPv2.cpp`
- `site.ApplePMPThermalUserClient`
- `static IOReturn ApplePMPUserClient::_fastDieControllerEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `void ApplePMP::_createWatchdogTimers()`
- `static IOReturn ApplePMPUserClient::_pmuTelemetryDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPv2`
- `ApplePMPEvent`
- `static IOReturn ApplePMPUserClient::_samplerDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMP: CLPC setAETSMaxControlEffortFunction failed\n`
- `void ApplePMP::_readyMessageHandler(mbi_msg_t)`
- `void ApplePMP::_initMemoryAckHandler(mbi_msg_t)`
- `IOReturn ApplePMP::_sendEHubTimeSeriesCommand(UInt32, UInt32, IOMemoryDescriptor *, UInt32 *)`
- `ApplePMP: Connected to AppleCLPC\n`
- `void ApplePMP::_messageHandler(void *, void *)`
- `ApplePMPv2UserClient`
- `void ApplePMP::_getNumDVFSStates(UInt64, UInt64 *, UInt64 *, UInt64 *)`
- `static IOReturn ApplePMPUserClient::_pmSendCommand(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPv2RegistryEntry`
- `ApplePMP`
- `\"ApplePMP: %s:%u REQUIRE failed: %s\" @%s:%d`
- `virtual IOReturn ApplePMP::setProperties(OSObject *)`
- `IOReturn ApplePMP::_sendPMCommand(UInt32, UInt64, UInt64, UInt64, UInt64)`
- `site.ApplePMPUserClient`
- `virtual bool ApplePMPUserClient::start(IOService *)`
- `static IOReturn ApplePMPUserClient::_getDVFSDomainName(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPControlFunction`
- `ApplePMPv2`
- `bool ApplePMP::clpcPerfControllerArrivalHandler(void *, IOService *, IONotifier *)`
- `static IOReturn ApplePMPUserClient::_samplerConfigCustomReg(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_getNumDVFSStates(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMP.cpp`
- `static IOReturn ApplePMPUserClient::_setProperty(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPEvent`
- `ApplePMPUserClient`
- `ApplePMPControlFunction`
- `static IOReturn ApplePMPUserClient::_getDVFSStateName(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMP`
