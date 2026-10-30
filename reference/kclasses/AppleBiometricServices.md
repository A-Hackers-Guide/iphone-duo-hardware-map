# `AppleBiometricServices`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleBiometricServices`](../kexts/com.apple.driver.AppleBiometricServices.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b938100`; metaclass vtable `0xfffffe0007ffeca0`; class vtable `0xfffffe0007ffe748`
- Registration (init): `0xfffffe0008a149ac`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleBiometricServices` in [`com.apple.driver.AppleBiometricServices`](../kexts/com.apple.driver.AppleBiometricServices.md): `IOProviderClass` = `AppleMesaSEPDriver`, `IOMatchCategory` = `com_apple_driver_AppleBiometricServices`

## Strings in its kext that name it (26)

- `ERROR: AppleBiometricServices::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `site.AppleBiometricServices`
- `site.AppleBiometricServicesUserClient`
- `AppleBiometricServices-UserClient`
- `ERROR: AppleBiometricServicesUserClient::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `AppleBiometricServices`
- `AppleBiometricServicesUserClient`
- `ERROR: AppleBiometricServicesUserClient::%s: terminate() failed.\n\n`
- `/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/AppleBiometricServices/AppleBiometricServices.cpp`
- `/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/AppleBiometricServices/AppleBiometricServicesUserClient.cpp`
- `AppleBiometricServicesUserClient::%s <- selector:%u, arguments:%p, dispatch:%p, target:%p, reference:%p\n`
- `AppleBiometricServices::%s <- provider:%p\n`
- `AppleBiometricServices::%s <- provider:%p --> void\n`
- `AppleBiometricServicesUserClient::%s <- owningTask:%p, securityToken:%p, type:%u, properties:%p\n`
- `AppleBiometricServicesUserClient::%s -> kIOReturnSuccess\n`
- `AppleBiometricServices::%s <- inData:%p, outData:%p, outSize:%p --> _provider->performCommand\n`
- `AppleBiometricServicesUserClient::%s -> success:%d\n`
- `AppleBiometricServicesUserClient::%s <- \n`
- `AppleBiometricServicesUserClient::%s <- provider:%p\n`
- `AppleBiometricServicesUserClient::%s <- inObj:%p, inRef:%p, inArg:%p\n`
- `AppleBiometricServicesUserClient::%s -> err:0x%x\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.AppleBiometricServices'!\n`
- `AppleBiometricServices::%s -> result:%d\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.AppleBiometricServices-UserClient'!\n`
- `AppleBiometricServicesUserClient::%s <- provider:%p --> super::stop\n`
- `AppleBiometricServicesUserClient::%s: in md = %p out md = %p  out md size %d\n\n`
