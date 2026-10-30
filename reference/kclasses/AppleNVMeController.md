# `AppleNVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x428` (1,064 bytes)
- Metaclass: `0xfffffe000ba17460`; metaclass vtable `0xfffffe00083c0a98`; class vtable `0xfffffe00083c0118`
- Registration (init): `0xfffffe000a2a1f3c`
- Superclasses: [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 7 in total)

- [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) — `com.apple.iokit.IONVMeFamily`

## Strings in its kext that name it (12)

- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeController.cpp`
- `site.AppleNVMeController`
- `AppleNVMeController`
- `AppleNVMeController.cpp`
- `virtual IOReturn AppleNVMeController::performNVMeShutdownTasks()`
- `\"AppleNVMeController::PolledIO, trying to do polled IO with polled command in flight, inPolledIOSelector = 0x%08x\\n\" @%s:%d`
- `virtual void AppleNVMeController::CreateHousekeepingTimerEventSource()`
- `\"AppleNVMeController::PolledIO: Invalid key length %d\\n\" @%s:%d`
- `nvme: \"AppleNVMeController::HandleControllerPowerOff, ShutdownNVMe() completed with status = 0x%08x\\n\" @%s:%d`
- `IOReturn AppleNVMeController::ProcessTunnelCommand(AppleNVMeRequest *, AppleNVMeBuffer *, AppleNVMeBuffer *)`
- `virtual IOReturn AppleNVMeController::UpdateMspBfhParams(void *, uint32_t)`
- `virtual IOReturn AppleNVMeController::GetNANDInfo(uint64_t *)`
