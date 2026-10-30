# `com_apple_driver_FairPlayIOKit`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.FairPlayIOKit`](../kexts/com.apple.driver.FairPlayIOKit.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b9e1960`; metaclass vtable `0xfffffe00082e39d8`; class vtable `0xfffffe00082e32c0`
- Registration (init): `0xfffffe0009c81a88`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `FairPlayIOKit` in [`com.apple.driver.FairPlayIOKit`](../kexts/com.apple.driver.FairPlayIOKit.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `FairPlayIOKit`, `IOProbeScore` = `1000`

## Strings in its kext that name it (60)

- `site.com_apple_driver_FairPlayIOKitUserClient`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] Error: bad input structure length\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] Error: invalid input parameters\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] 2nd IOAESAccelerator::performAES randomV returned %d\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES scrambler returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES (UID) returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Error: null pointer detected\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOAESAccelerator::performAES UID returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] Error: invalid input parameters\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateSeed] Error: null pointer parameter\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] Error: null pointer for input parameter\n`
- `[com_apple_driver_FairPlayIOKit::GetProductID] Error: The ProductID length doesn't match!!!\n`
- `[com_apple_driver_FairPlayIOKit::isJ42dDevice] Error: GetProductID() returns %x\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] Bad VSegInfoLength for In-Field Seed detected\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] Failed to get product ID\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOBufferMemoryDescriptor::prepare returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucExchangeWithHoover] ProvInfoIOKit::exchangeWithHoover returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] ProvInfoIOKit::encryptedSUInfo returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] bad input structure length\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] ProvInfoIOKit::ucEncryptWithWrappedKey returned %d\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] IOService::serviceMatching returned NULL (probably means no Hoover on the device)\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] Hoover response is larger than response buffer (%u vs %u)\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOBufferMemoryDescriptor::prepare returned %d\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] unsupported seed segment offset\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOAESAccelerator::performAES returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateSeed] Error: ProvInfoIOKit::generateSeed returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Returned error: %x\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] Error: null pointer detected\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES GID returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOBufferMemoryDescriptor::prepare returned %d\n`
- `com_apple_driver_FairPlayIOKitUserClient`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateInFieldSeed] Error: null pointer parameter\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] Error: bad input structure lengths\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] ProvInfoIOKit::getEncryptedSeedSegment returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] null pointer parameter detected\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] Error: null pointer for input structure\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES in-field returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] bad pointer for input or output structure\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `com_apple_driver_FairPlayIOKit`
- `site.com_apple_driver_FairPlayIOKit`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOAESAccelerator::performAES GID returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] IOAVService::createAUPPacket returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOAESAccelerator::performAES returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateInFieldSeed] Error: ProvInfoIOKit::generateInFieldSeed returned %d\n`
- `[com_apple_driver_FairPlayIOKit::GetDeviceProperty] Error: The string length is not correct!\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Error: invalid seed version (%u)\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] Error: invalid seed version (%u)\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] PIKDecryptWithFixedSharedKey returned %d\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOBufferMemoryDescriptor::prepare returned %d\n`
- `[com_apple_driver_FairPlayIOKit::GetDeviceProperty] Error: The data length is not correct!\n`
