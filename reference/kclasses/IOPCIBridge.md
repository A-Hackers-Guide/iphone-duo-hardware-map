# `IOPCIBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000ba18e08`; metaclass vtable `0xfffffe00083d5de0`; class vtable `0xfffffe00083d56c0`
- Registration (init): `0xfffffe000a333668`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 8 in total)

- [`IOPCI2PCIBridge`](IOPCI2PCIBridge.md) — `com.apple.iokit.IOPCIFamily`
- [`IOPCIHostBridge`](IOPCIHostBridge.md) — `com.apple.iokit.IOPCIFamily`

## Strings in its kext that name it (10)

- `\"Warm reset not implemented in IOPCIBridge\" @%s:%d`
- `virtual IOReturn IOPCIBridge::getNubResources(IOService *)`
- `IOPCIBridge`
- `[PCIe:%u %llu ns] IOPCIBridgeVariables::finishMachineState(%d)\n`
- `IOReturn IOPCIBridge::childClientCrashRecoveryGated(IOPCIDevice *)`
- `site.IOPCIBridge`
- `IOPCIBridge.cpp`
- `IOReturn IOPCIBridge::waitForTerminateThreadCall(thread_call_t)`
- `IOReturn IOPCIBridge::waitForDeviceReady(IOPCIDevice *)`
- `[PCIe:%u %llu ns] IOPCIBridgeVariables::finishMachineState(%d)\n`
