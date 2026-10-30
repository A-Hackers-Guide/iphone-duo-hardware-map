# `ANEDriverDebugClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md)
- Object size: `0x188` (392 bytes)
- Metaclass: `0xfffffe000b94c1a0`; metaclass vtable `0xfffffe00080be8b0`; class vtable `0xfffffe00080be2b8`
- Registration (init): `0xfffffe0008d40a78`
- Superclasses: [`IOUserClient2022`](IOUserClient2022.md) → [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (9)

- `ANEDriverDebugClient`
- `virtual void ANEDriverDebugClient::stop(IOService *)`
- `virtual bool ANEDriverDebugClient::init(task_t, OSDictionary *)`
- `virtual IOReturn ANEDriverDebugClient::clientDied()`
- `virtual IOReturn ANEDriverDebugClient::clientClose()`
- `site.ANEDriverDebugClient`
- `virtual void ANEDriverDebugClient::free()`
- `ANEDriverDebugClient: %s : %s (%p) pid: %d\n`
- `%s - New ANEDriverDebugClient for process: %s (pid %d)\n`
