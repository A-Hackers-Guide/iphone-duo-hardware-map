# `TrustedClockingKEXT`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.audio.TrustedClockingKEXT`](../kexts/com.apple.audio.TrustedClockingKEXT.md)
- Object size: `0x18c8` (6,344 bytes)
- Metaclass: `0xfffffe000ba39c58`; metaclass vtable `0xfffffe00084a4d20`; class vtable `0xfffffe00084a4788`
- Registration (init): `0xfffffe000a9a6650`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `TrustedClockingKEXT` in [`com.apple.audio.TrustedClockingKEXT`](../kexts/com.apple.audio.TrustedClockingKEXT.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `TrustedClockingKEXT`

## Strings in its kext that name it (31)

- `TrustedClockingUserClient::start - Failed to cast provider to TrustedClockingKEXT\n`
- `TrustedClockingKEXTImpl::startKernelWorkloop - No state for useCaseID %u\n`
- `TrustedClockingKEXT::setupTransportAndPublisherForCallbacks - transport=%p publisher=%p\n`
- `TrustedClockingKEXT::trustedStartIO - transport service unavailable\n`
- `TrustedClockingKEXT::stop - Stopping AoE Clocking driver...\n`
- `TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - stop failed\n`
- `TrustedClockingKEXT::start - AoE Clocking driver started successfully!\n`
- `TrustedClockingKEXT::probe - Probing hardware...\n`
- `site.TrustedClockingKEXT`
- `TrustedClockingKEXTImpl::processKernelWorkloop [%u] - Exiting\n`
- `TrustedClockingKEXT::free - Goodbye from the kernel!\n`
- `TrustedClockingKEXT::trustedSignalIO - transport service unavailable\n`
- `TrustedClockingKEXTImpl::stopKernelWorkloop - No state for useCaseID %u\n`
- `TrustedClockingKEXT_c.c`
- `TrustedClockingKEXT::trustedTransactionalMessage - Trusted domain is sending message %llu to identifier %llu\n`
- `TrustedClockingKEXT::trustedStopIO - Trusted domain called StopIO for identifier %llu\n`
- `TrustedClockingKEXTImpl::registerUseCaseState - add failed for useCaseId %u\n`
- `TrustedClockingKEXT::trustedTransactionalMessage - Message Transaction %llu successfully sent to identifier %llu\n`
- `TrustedClockingKEXT::trustedStopIO - transport service unavailable\n`
- `TrustedClockingKEXT::trustedSignalIO - Trusted domain called SignalIO for identifier %llu\n`
- `TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - PM notify failed\n`
- `TrustedClockingKEXT::trustedTransactionalMessage - message service unavailable\n`
- `TrustedClockingKEXTImpl::startKernelWorkloop [%u] - failed to signal start\n`
- `TrustedClockingKEXT::start - Starting AoE Clocking driver...\n`
- `TrustedClockingKEXTImpl::triggerWorkloopDataAvailability - No state for useCaseID %u\n`
- `TrustedClockingKEXT`
- `TrustedClockingKEXTImpl::startKernelWorkloop [%u] - PM notify failed\n`
- `TrustedClockingKEXT::init - Hello from the kernel!\n`
- `TrustedClockingKEXTImpl::registerUseCaseState - registered useCaseId %u\n`
- `TrustedClockingKEXT::start - Failed to start super class\n`
- `TrustedClockingKEXT::start - Failed to start impl\n`
