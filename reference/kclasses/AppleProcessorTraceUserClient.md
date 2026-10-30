# `AppleProcessorTraceUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b993870`; metaclass vtable `0xfffffe00081bcff0`; class vtable `0xfffffe00081bca00`
- Registration (init): `0xfffffe000945e238`
- Superclasses: [`IOUserClient2022`](IOUserClient2022.md) → [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (40)

- `AppleProcessorTraceUserClient::externalMethodConfigure\n`
- `AppleProcessorTraceUserClient::clientClose\n`
- `AppleProcessorTraceUserClient::externalMethodAttach\n`
- `AppleProcessorTraceUserClient::start\n`
- `AppleProcessorTraceUserClient::registerNotificationPort(%u)\n`
- `AppleProcessorTraceUserClient::interruptSession\n`
- `AppleProcessorTraceUserClient::externalMethodRequestBuffer\n`
- `AppleProcessorTraceUserClient::externalMethodPause\n`
- `AppleProcessorTraceUserClient::externalMethodUnconfigure\n`
- `AppleProcessorTraceUserClient::externalMethodAddTask\n`
- `AppleProcessorTraceUserClient::externalMethodResume\n`
- `AppleProcessorTraceUserClient::externalMethodGetSystemMetadata\n`
- `AppleProcessorTraceUserClient::externalMethodStop\n`
- `AppleProcessorTraceUserClient::initWithTask\n`
- `AppleProcessorTraceUserClient::externalMethodReleaseChunk\n`
- `AppleProcessorTraceUserClient::clientMemoryForType(%u)\n`
- `AppleProcessorTraceUserClient::externalMethodStart\n`
- `IOReturn AppleProcessorTrace::attachToSessionGated(MethodAttachArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodResume(OSObject *, void *, IOExternalMethodArguments *)`
- `site.AppleProcessorTraceUserClient`
- `IOReturn AppleProcessorTrace::configureGated(MethodConfigArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `virtual IOReturn AppleProcessorTraceUserClient::registerNotificationPort(mach_port_t, UInt32, UInt32)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodConfigure(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodStart(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodReleaseChunk(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodPause(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleProcessorTraceUserClient::clientClose()`
- `void AppleProcessorTraceUserClient::interruptSession()`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodRequestBuffer(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodRequestBuffer(OSObject *, void *, IOExternalMethodArguments *)_block_invoke`
- `virtual bool AppleProcessorTraceUserClient::start(IOService *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodAttach(OSObject *, void *, IOExternalMethodArguments *)`
- `AppleProcessorTraceUserClient.cpp`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodStop(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleProcessorTraceUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodUnconfigure(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodAddTask(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual bool AppleProcessorTraceUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `AppleProcessorTraceUserClient`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodGetSystemMetadata(OSObject *, void *, IOExternalMethodArguments *)`
