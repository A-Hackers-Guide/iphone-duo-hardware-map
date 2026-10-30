# `ANEDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md)
- Object size: `0x828` (2,088 bytes)
- Metaclass: `0xfffffe000b94c400`; metaclass vtable `0xfffffe00080c3b90`; class vtable `0xfffffe00080c3638`
- Registration (init): `0xfffffe0008d997dc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`H1xANELoadBalancer`](H1xANELoadBalancer.md) — `com.apple.driver.AppleH16ANEInterface`

## Strings in its kext that name it (25)

- `ANEDriverDebugClient`
- `virtual void ANEDriverDebugClient::stop(IOService *)`
- `ANEDriver.cpp`
- `ANEDriverECCmdProvideXnuContentFileSize`
- `ANEDriverECCmdPersistentClientUpcallAck`
- `ANEDriverECCmdRestoreExclaveState`
- `virtual bool ANEDriverDebugClient::init(task_t, OSDictionary *)`
- `ANEDriverECCmdResumeExclaveWork`
- `ANEDriverECCmdSaveExclaveState`
- `virtual IOReturn ANEDriverDebugClient::clientDied()`
- `virtual IOReturn ANEDriverDebugClient::clientClose()`
- `ANEDriverECCmdQueryForResult`
- `site.ANEDriver`
- `ANEDriver`
- `ANEDriverECCmdPreparePowerOff`
- `ANEDriverRoot`
- `ANEDriverECCmdStartFirmwareRecoveryProcess`
- `site.ANEDriverDebugClient`
- `virtual void ANEDriverDebugClient::free()`
- `ANEDriverECCmdEndFirmwareRecoveryProcess`
- `ANEDriverECCmdPauseExclaveWork`
- `ANEDriverDebugClient: %s : %s (%p) pid: %d\n`
- `%s: %s: aneDriverEnabled=1 boot-arg set - ANEDriver is enabled!\n`
- `%s - New ANEDriverDebugClient for process: %s (pid %d)\n`
- `%s: %s: ANEDriver::start, res: %d\n`
