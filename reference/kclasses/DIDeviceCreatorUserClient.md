# `DIDeviceCreatorUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000b940f80`; metaclass vtable `0xfffffe0008051658`; class vtable `0xfffffe0008051070`
- Registration (init): `0xfffffe0008b75dfc`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (16)

- `site.DIDeviceCreatorUserClient`
- `static IOReturn DIDeviceCreatorUserClient::CreateDevice(OSObject *, void *, IOExternalMethodArguments *)`
- `bool AppleDiskImageDevice::setCreatorUC(DIDeviceCreatorUserClient *)`
- `virtual void DIDeviceCreatorUserClient::stop(IOService *)`
- `virtual IOReturn DIDeviceCreatorUserClient::message(UInt32, IOService *, void *)`
- `virtual IOReturn DIDeviceCreatorUserClient::clientClose()`
- `virtual IOReturn DIDeviceCreatorUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `virtual void DIDeviceCreatorUserClient::free()`
- `virtual bool DIDeviceCreatorUserClient::initWithTask(task_t, void *, UInt32)`
- `DIDeviceCreatorUserClient`
- `static IOReturn DIDeviceCreatorUserClient::QuarantineDevice(OSObject *, void *, IOExternalMethodArguments *)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp`
- `virtual bool DIDeviceCreatorUserClient::start(IOService *)`
- `[%d] %s::%d: Client has entitlement to use DIDeviceCreatorUserClient.\n`
- `[%d] %s::%d: Client is not entitled to use DIDeviceCreatorUserClient\n`
- `[%d] %s::%d: Can't allocate lock for DIDeviceCreatorUserClient\n`
