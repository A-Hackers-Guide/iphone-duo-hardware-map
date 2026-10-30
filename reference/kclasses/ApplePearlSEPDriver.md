# `ApplePearlSEPDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePearlSEPDriver`](../kexts/com.apple.driver.ApplePearlSEPDriver.md)
- Object size: `0xb88` (2,952 bytes)
- Metaclass: `0xfffffe000b988768`; metaclass vtable `0xfffffe000819f7e0`; class vtable `0xfffffe000819f0f0`
- Registration (init): `0xfffffe00093af868`
- Superclasses: [`IOSEPBiometricService`](IOSEPBiometricService.md) → [`IOBiometricService`](IOBiometricService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`ApplePearlExclaveSEPDriver`](ApplePearlExclaveSEPDriver.md) — `com.apple.driver.ApplePearlExclaveSEPDriver`

## IOKit personalities that instantiate it (1)

- `ApplePearlSEPDriver` in [`com.apple.driver.ApplePearlSEPDriver`](../kexts/com.apple.driver.ApplePearlSEPDriver.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,sprl`, `IOMatchCategory` = `com_apple_driver_ApplePearlSEPDriver`, `IOProbeScore` = `1000`

## Strings in its kext that name it (38)

- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlUserClient.cpp`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlSEPDriver.cpp`
- `ApplePearlSEPDriver:%s:%s mapped to ANE\n`
- `ApplePearlSEPDriver:%s Could not map object to ANE. ArmFunction:%p Allocated:%d\n`
- `_alsHidService->open(_driver, 0, nullptr, ((IOHIDEventService::Action) __builtin_load_member_function_pointer(*_driver, &ApplePearlSEPDriver::alsHidEventServiceCallback) ? : (IOHIDEventService::Action) OSMetaClassBase:: _ptmf2ptf(_driver, (void (OSMetaClassBase::*)(void)) &ApplePearlSEPDriver::alsHi`
- `ApplePearlSEPDriver:%s Object%s mapped to ISP\n`
- `ApplePearlSEPDriver:%s: %s IOBMD:%p VA:%p dva offset:%X size:%u\n`
- `com.apple.tracked.ApplePearlSEPDriver`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlLogging.cpp`
- `ApplePearlSEPDriver:%s Could not unmap object from ANE. ArmFunction:%p\n`
- `ApplePearlSEPDriver:%s Object%s mapped to ANE\n`
- `ApplePearlSEPDriver:%s Object%s unmapped from ANE\n`
- `site.ApplePearlSEPDriver`
- `ApplePearlSEPDriver:%s AppleARMFunctions mapped\n`
- `ApplePearlSEPDriver:%s ISP Powered On\n`
- `ApplePearlSEPDriver:%s: %s IOBMD VA:%p\n`
- `ApplePearlSEPDriver:%s ANE Powered On\n`
- `ApplePearlSEPDriver:%s before mapDynamicObject fourcc:%s IOBMDTest:%p dvaOffset:0x%X objSize:%d\n`
- `ApplePearlSEPDriver`
- `ApplePearlSEPDriver:%s Could not unmap object from ISP. ArmFunction:%p\n`
- `ApplePearlSEPDriver:%s Object allocated and%s mapped to SEP\n`
- `ApplePearlSEPDriver:%s: %s dva offset:%X size:%u\n`
- `ApplePearlSEPDriver:%s after mapDynamicObject fourcc:%s IOBMDTest:%p dvaOffset:0x%X objSize:%d\n`
- `ApplePearlSEPDriver:%s Object%s unmapped from ISP\n`
- `ApplePearlSEPDriver:%s - unmapping: %s IOBMD:%p VA:%p dva offset:%X size:%u\n`
- `ApplePearlSEPDriver:%s _S3DynamicIOBMD(Perm+Temp) initialized\n`
- `ApplePearlSEPDriver:%s:%s mapped to ISP\n`
- `ApplePearlSEPDriver:%s Object properties read\n`
- `ApplePearlSEPDriver:%s Could not map object to ISP. ArmFunction:%p Allocated:%d\n`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlFrameSupport.cpp`
- `%s -> ApplePearlSEPDriver::unmapMemoryFromSEP -> 0x%x\n`
- `%s -> ApplePearlSEPDriver::getPagesFromUnalignedMemoryDescriptor -> 0x%x\n`
- `%s -> ApplePearlSEPDriver::mapMemoryForSEP -> 0x%x\n`
- `%s -> ApplePearlSEPDriver::loadDCNKernels -> 0x%x\n`
- `%s <- ApplePearlSEPDriver::getPagesFromUnalignedMemoryDescriptor\n`
- `%s <- ApplePearlSEPDriver::mapMemoryForSEP\n`
- `%s <- ApplePearlSEPDriver::loadDCNKernels\n`
- `%s <- ApplePearlSEPDriver::unmapMemoryFromSEP\n`
