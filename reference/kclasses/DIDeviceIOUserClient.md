# `DIDeviceIOUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md)
- Object size: `0x158` (344 bytes)
- Metaclass: `0xfffffe000b941090`; metaclass vtable `0xfffffe0008052d20`; class vtable `0xfffffe0008052738`
- Registration (init): `0xfffffe0008b85af4`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (24)

- `static IOReturn DIDeviceIOUserClient::StashFileInformation(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn DIDeviceIOUserClient::GetCacheStats(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn DIDeviceIOUserClient::DrainDormantQueue(OSObject *, void *, IOExternalMethodArguments *)`
- `uint64_t DIDeviceIOUserClient::ioMem(IOMemoryDescriptor *, size_t, uint64_t, size_t, kDIIODirectDir)`
- `virtual void DIDeviceIOUserClient::stop(IOService *)`
- `bool AppleDiskImageDevice::onIOClientClose(DIDeviceIOUserClient *)`
- `IOReturn AppleDiskImageDevice::ValidateAndSetupCommonParams(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp`
- `static IOReturn DIDeviceIOUserClient::Connect(OSObject *, void *, IOExternalMethodArguments *)`
- `site.DIDeviceIOUserClient`
- `mach_port_t DIDeviceIOUserClient::findNotificationPort(unsigned int)`
- `virtual bool DIDeviceIOUserClient::start(IOService *)`
- `static IOReturn DIDeviceIOUserClient::RequestGracefulShutdown(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn DIDeviceIOUserClient::AllocPortsArray(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual void DIDeviceIOUserClient::free()`
- `DIDeviceIOUserClient`
- `IOReturn AppleDiskImageDevice::ReconnectForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `bool AppleDiskImageDevice::setIOProvider(DIDeviceIOUserClient *)`
- `virtual IOReturn DIDeviceIOUserClient::clientClose()`
- `virtual bool DIDeviceIOUserClient::initWithTask(task_t, void *, UInt32)`
- `static IOReturn DIDeviceIOUserClient::GetRequestsStats(OSObject *, void *, IOExternalMethodArguments *)`
- `IOReturn AppleDiskImageDevice::InitForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `[%d] %s::%d: Client is not entitled to use DIDeviceIOUserClient\n`
- `[%d] %s::%d: Client has entitlement to use DIDeviceIOUserClient.\n`
