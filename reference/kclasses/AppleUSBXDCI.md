# `AppleUSBXDCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBXDCI`](../kexts/com.apple.driver.AppleUSBXDCI.md)
- Object size: `0x2650` (9,808 bytes)
- Metaclass: `0xfffffe000ba1e5a0`; metaclass vtable `0xfffffe000843c818`; class vtable `0xfffffe000843bf40`
- Registration (init): `0xfffffe000a65b0a8`
- Superclasses: [`IOUSBDeviceController`](IOUSBDeviceController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 13 in total)

- [`AppleUSBXDCIARM`](AppleUSBXDCIARM.md) — `com.apple.driver.AppleUSBXDCIARM`

## Strings in its kext that name it (60)

- `%s@%s: %s::%s: could not allocate AppleUSBXDCIEndpoint for endpoint 0x%02x\n`
- `%s@%s: %s::%s: could not allocate AppleUSBXDCIEndpoint for endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:Tag not in device tree, continuing\n`
- `AppleUSBXDCI::%s:failed stopDeviceController 0x%08x\n`
- `AppleUSBXDCI::%s:completed with status 0x%08x\n`
- `AppleUSBXDCI::%s:endpoint 0x%02x not active\n`
- `AppleUSBXDCI::%s:Missed frame %d on EP %d\n`
- `AppleUSBXDCI::%s:error: did not find a resting TRB block for endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:speed %d linkState %d return status 0x%08x\n`
- `AppleUSBXDCI::%s:kEpCommandEndXfer failed as XferResNotAvailable for ep 0x%02x\n`
- `AppleUSBXDCI.cpp`
- `AppleUSBXDCI::%s:device is in disconnected state\n`
- `AppleUSBXDCI::%s:not on bus\n`
- `AppleUSBXDCI::%s:event %d controlState %d\n`
- `AppleUSBXDCI::%s:returning TRB block %p (phys 0x%llx)\n`
- `AppleUSBXDCI::%s:control transfer in state %d\n`
- `AppleUSBXDCI::%s:resetting core\n`
- `AppleUSBXDCI::%s:starting DCTL: 0x%08x DSTS: 0x%08x\n`
- `AppleUSBXDCI::%s:failed to %s stall for endpoint 0x%02x with error 0x%08x\n`
- `AppleUSBXDCI::%s:endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:failed provideEndpointIDsForConfiguration\n`
- `AppleUSBXDCI::%s:interface count %d\n`
- `AppleUSBXDCI::%s:Performing first remote wake attempt since boot\n`
- `AppleUSBXDCI::%s:Setting DCTL.DEVCTRLHLT timed out DSTS: 0x%08x\n`
- `AppleUSBXDCI::%s:failed to create _eventHandlers[kDeviceEventHandlerIndex]\n`
- `AppleUSBXDCI::%s:called without being on bus\n`
- `AppleUSBXDCI::%s:endpoint 0x%02x transferredLength %d trbStatus 0x%x\n`
- `AppleUSBXDCITRBBlock-debug`
- `AppleUSBXDCI::%s:bus time expired\n`
- `AppleUSBXDCI::%s:failed to schedule IORequest for endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:unexpected event %d\n`
- `AppleUSBXDCI::%s:epIndex %d depcmd 0x%x param0 0x%x param1 0x%x param2 0x%x\n`
- `AppleUSBXDCI::%s:command 0x%x param 0x%x\n`
- `AppleUSBXDCI::%s:Core version register value: 0x%08x\n`
- `AppleUSBXDCITRBPool`
- `AppleUSBXDCI::%s:prepare failed for dma command req %p, result: 0x%x\n`
- `AppleUSBXDCI::%s:kEpCommandStartXfer failed as IsocIntervalExpired for ep 0x%02x\n`
- `site.AppleUSBXDCITRBBlock`
- `AppleUSBXDCI::%s:Bus event %d\n`
- `AppleUSBXDCI::%s:completed with %d endpoints assigned\n`
- `AppleUSBXDCI::%s:status 0x%08x\n`
- `AppleUSBXDCI::%s:ignoring event %d for inactive endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:invalid request on EP0_IN endpoint\n`
- `AppleUSBXDCI::%s:failed to powerOn the controller\n`
- `AppleUSBXDCI::%s:clearing endpoint stall for 0x%02x\n`
- `AppleUSBXDCI::%s:Command Completion interrupt not received on time\n`
- `AppleUSBXDCI::%s:kEpCommandStartXfer success for ep 0x%02x XferResIndex %d\n`
- `AppleUSBXDCI::%s:Pending IO on ep 0x%02x, but interface does not want remote wake\n`
- `AppleUSBXDCI::%s:Setting DCTL.DEVCTRLHLT timed out DSTS: 0x%08x. Trying to reset the controller.\n`
- `AppleUSBXDCI::%s:Ran out of TRBs. Failed to schedule IO for ep:%02x\n`
- `AppleUSBXDCI::%s:returning TRB block %p (phys 0x%llx) to pool\n`
- `AppleUSBXDCI::%s:transfer resource not available\n`
- `AppleUSBXDCI::%s:\n`
- `AppleUSBXDCI::%s:usb2phy suspend\n`
- `AppleUSBXDCI::%s:event %d on endpoint 0x%02x\n`
- `AppleUSBXDCI::%s:failed to allocate TRB block from _standardTRBPool\n`
- `AppleUSBXDCI::%s:unable to allocate usb ep0 out buffer descriptor\n`
- `AppleUSBXDCI::%s:Failed with status 0x%08x (ep 0x%02x , type %d, mps %d, interval %d)\n`
- `AppleUSBXDCI::%s:IO timeout (%p) for endpoint %02x, returning it\n`
- `AppleUSBXDCI::%s:Unable to allocate serializer\n`
