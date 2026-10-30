# `/usr/lib/libPCITransport.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 347,936 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 2624)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/libPCITransport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libIOACIPC.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libIOACIPCBB.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libIOABP.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libRemoteTelephonyTransport.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (462)

```
getTypeString
~info
%s::%s::%p::%d: add interface %d\n
removeBH
TelephonyBasebandPCITransportDeregisterTimeEvent
com.apple.WirelessIPC.baseband.pci_bh
%s::%s::%p::%d: read register 0x%x\n
%s::%s::%p::%d: already pending for interface %d\n
v12@?0B8
%s: failed to create Oversteer transport internal\n
PCI
fFreeIO.size() == ( fNumIO + fAdditionalNumIO )
mapRegion
v16@?0^{?=CC[2C]IQ}8
TelephonyBasebandPCITransportMapRegionwithClientData
TelephonyBasebandTransportIsValid
TelephonyBasebandTransportCreate
cellular
v20@?0I8I12i16
kABPPDPInboundPacketDropped
mapRegionAsync
%s::%s::%p::%d: failed to create task close in\n
%s: %s (%#x), arg %p\n
timesync
%s::%s::%p::%d: failed to deregister time event 0x%08x\n
unblockRead
%s::%s::%p::%d: interface added\n
!fNotifyTask
v20@?0i8I12I16
pci error (unsupported variant: daleipc): 
fAsync
%s: Oversteer: no tu transport object\n
abortChannelAsync
PCITransportKernel.cpp
!fQueue
validateParams
%s::%s::%p::%d: fRegistered\n\n
%s: a notification block is already registered. deregister it before registering a new block\n
%s::%s::%p::%d: buffer %p, length %u, cookie %u, dDtor %p, timeout %u\n
%s::%s::%p::%d: %s (%u): param 0x%x: status 0x%x\n
unmap region
)
%s: invalid interface number %d\n
%s::%s::%p::%d: reg %u, buffer %p, size %u\n
qmux1
: (
%s::%s::%p::%d: free:%zu active:%zu additional:%u\n
release
kACIPCPDPControlCommandDropped
sendImageAsync_block_invoke
mapRegionAsync_block_invoke
%s::%s::%p::%d: failed to create task map region\n
~task
%s: no tu transport object\n
%s: invalid number of io\n
allocate
ioCompletion
invalid
%s: could not get matching service\n
PCITransportTH.cpp
write_block_invoke
send image
%s::%s::%p::%d: send image failed 0x%x\n
imageCompletion
TelephonyBasebandPCITransportMapRegion
PCISystem.cpp
Callback.
%s: block must be provided\n
v28@?0i8^v12I20I24
%s::%s::%p::%d: read failed 0x%x\n
%s: failed to create ioPool\n
%s::%s::%p::%d: buffer %p, size %u, dDtor %p\n
TelephonyBasebandPCITransport.cpp
fActiveIO.size() == 0
%s: got time event for domain %u with only %u args\n
cmdCompletion
map::at:  key not found
TelephonyBasebandTransportReadRegister
it != mth.end()
%s::%s::%p::%d: %u\n
lf-trace
unmapRegion
setEventNotificationPort
%s::%s::%p::%d: domain %u\n
unmapRegionAsync_block_invoke
fActive
%s::%s::%p::%d: %s failed, complete 0x%x, size %u, cookie %u\n
time sync
notify
%s::%s::%p::%d: Semaphore wait timed out!\n\n
TelephonyBasebandTransportRead
TelephonyBasebandPCITransportUnmapRegion
qdss
IOAppleConvergedIPCControl
eventNotification
%s::%s::%p::%d: failed to create task open in\n
%s::%s::%p::%d: status 0x%x, buff %p, size %u, code %u\n
map region
pdp error: 
AppleConvergedIPCPDPManager
%s::%s::%p::%d: failed to create task open out\n
task
insertBH_block_invoke
%s: invalid io size\n
kACIPCPDPWriteTimeout
%s::%s::%p::%d: domain %u, count %u, cb %p\n
com.apple.WirelessIPC.baseband.pci_workloop
init
v20@?0B8B12I16
pci error: 
TelephonyBasebandTransportFree
%s::%s::%p::%d: failed to create bh\n
%s::%s::%p::%d: failed to create task read register\n
%s::%s::%p::%d: %s: failed to init\n
%s::%s::%p::%d: region %u, buffer %p, length %u\n
unmapRegionAsync
rom
trace
at
readRegister
fEventNotificationPort
kABPPDPWriteFailed
kABPPDPReadFailed
v28@?0I8^v12^v20
kABPPDPControlResponseFailed
%s::%s::%p::%d: reg %u, buffer %p, length %u, timeout %u\n
%s: creating Oversteer transport \n
deregisterTimeEvent_block_invoke
kABPPDPControlResponseDropped
TelephonyBasebandPCITransportFree
setNotify
%s: Timeout waiting for deregistering kernel notifications\n
kACIPCPDPOutboundPacketDropped
readAsync_block_invoke
ioFree
virtual_timesync
IOAppleConvergedIPCInterface
fCBL.empty()
generateCallback_block_invoke
%s: could not create matching dictionary\n
kACIPCPDPControlResponseFailed
%s::%s::%p::%d: failed to create task write\n
control
%s::%s::%p::%d: failed to create task read\n
%s::%s::%p::%d: unmap region failed 0x%x\n
%s: %s (%u), arg1 %p, arg2 %p\n
kACIPCPDPBadControlCommand
readInternal
TelephonyBasebandPCITransportTimesync
v24@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8^v16
kACIPCPDPInboundPacketDropped
%s::%s::%p::%d: region %u, buffer %p, length %u, cb %p\n
%s: failed to validate Oversteer transport parameters\n
TelephonyBasebandPCITransportReadRegister
%s::%s::%p::%d: --done\n
init_block_invoke
%s: IOABPControlClass::stop() returned failure\n
%s: IOABPControlClass::start() returned failure\n
%s: PDPListener::start() returned failure\n
kABPPDPControlCommandDropped
TelephonyBasebandPCITransportRegisterTimeEvent
ACIPCInterfaceProviderDevice
~ioPool
%s::%s::%p::%d: time sync failed 0x%x\n
th
%s: cannot use optimized transport\n
%s::%s::%p::%d: %p\n
readAsync
rctth
kABPPDPOutboundPacketDropped
%s::%s::%p::%d: buffer %p, length %u, dDtor %p, timeout %u\n
timesyncAsync_block_invoke
%s::%s::%p::%d: completion %u\n
%s: invalid control driver\n
%s: unknown PCI variant\n
%s::%s::%p::%d: status 0x%x, region %u\n
TelephonyBasebandPCITransportIsValid
gnss
%s: IOABPControlClass::registerEventCallback() returned %#x\n
kABPPDPBadBearerMapping
%s::%s::%p::%d: failed to create task time sync\n
notifyPDP
PCITransport
TelephonyBasebandPCITransportWrite
unsupported variant: daleipc
qmux2
v20@?0i8I12i16
vector
%s::%s::%p::%d: \n
TelephonyBasebandPCITransportUnblockRead
boot
deregisterTimeEvent
PCIEvent.cpp
%s: status block is required\n
readRegisterInternal
%s::%s::%p::%d: status 0x%x, region %u, buff %p, size %u\n
%s::%s::%p::%d: region %u, cb %p\n
TelephonyBasebandTransportUnblockRead
v8@?0
info
diag
ari
boot_logger
v28@?0i8^v12^v20
v32@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8^v16^v24
%s::%s::%p::%d: interface removed\n
%s::%s::%p::%d: time event already registered for domain %u\n
%s: unsupported PCI variant: daleipc\n
%s: service is NULL - must successfully start() first\n
v36@?0^v8I16{shared_ptr<pci::transport::ioPool>=^{ioPool}^{__shared_weak_count}}20
%s::%s::%p::%d: status 0x%x, buff %p, size %u\n
%s::%s::%p::%d: %s: status 0x%x\n
eraseTH
hsfiler
%s: invalid configuration\n
PCITransportBH.cpp
kABPPDPBadControlResponse
PCITransportTask.cpp
fBind->getCIO()
%s::%s::%p::%d: failed to insert in system\n
%s::%s::%p::%d: time event not registered for domain %u\n
readRegister_block_invoke
%s::%s::%p::%d: domain %u, cb %p\n
mediactl
%s: no params\n
v12@?0I8
read
IOGeneralInterest
registerTimeEvent_block_invoke
TelephonyBasebandPCITransportRead
TelephonyBasebandTransportWrite
!fRunLoopRef
v24@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8I16i20
%s::%s::%p::%d: open pipe failed 0x%x\n
kACIPCPDPBadMuxHeader
%s::%s::%p::%d: failed to create task notify\n
ACIPCInterfaceProtocol
%s::%s::%p::%d: %s complete 0x%x, size %u, cookie %u\n
: 
timesyncAsync
ioAlloc
%s: failed to create transport internal\n
AirshipDaleBasebandControl
%s::%s::%p::%d: close pipe failed 0x%x\n
pci error (unsupported variant: unknown): 
kACIPCPDPWriteFailed
%s::%s::%p::%d: map region failed 0x%x\n
transport
TelephonyBasebandPCITransportFlushRead
iqtrace
%s::%s::%p::%d: failed to open 0x%x\n
%s::%s::%p::%d: notify interface removed\n
read register
v24@?0i8^^v12I20
%s: bad argument\n
TelephonyBasebandPCITransportCreate
unrecognized error code
%s::%s::%p::%d: failed to create kernel instance\n
open pipe
, 
%s::%s::%p::%d: %s: \n
size <= fSize
%s: invalid parameters\n
%s::%s::%p::%d: %p free:%zu active:%zu additional:%u\n
fAdditionalNumIO == 0
bh
open
AppleBasebandPCIPDPManagerBase
kABPPDPWriteTimeout
com.apple.WirelessIPC.baseband.pci_client
%s: client cannot issue read for async transport\n
%s: \n
system
TelephonyBasebandTransportFlushRead
dpl
dir == kPCITransportDirectionIn || dir == kPCITransportDirectionOut
close pipe
%s: got time event for domain %u with status 0x%08x\n
TelephonyBasebandTransportSendImage
mmapdebug
write
registerEventNotification
~th
sendImageInternal
complete
vcom
cb
false
%s: PDPListener::registerEventCallback() returned %#x\n
%s: failed to validate ioPool parameters\n
writeAsync_block_invoke
%s::%s::%p::%d: failed to create task unmap region\n
flushRead
AppleConvergedIPCRingIndex
basic_string
ioPool
sendImageAsync
~bind
refs
kABPPDPBadMuxHeader
writeAsync
sendImage_block_invoke
it != mbh.end()
lv-trace
~bh
~Listener
!fBind
%s::%s::%p::%d: %s: poisoned completion, status 0x%x\n
TelephonyBasebandPCITransportSendImage
AppleConvergedIPCBBControl
pbl
PCITransportIOPool.cpp
!called
%s::%s::%p::%d: write failed 0x%x\n
sendImage
registerTimeEvent
%s: no memory\n
%s: could not add interest notification on service: %#x\n
kACIPCPDPControlCommandFailed
kACIPCPDPControlResponseDropped
writeInternal
read_block_invoke
fStatus != kIOReturnInvalid
com.apple.telephony.ipc
close
kACIPCPDPReadFailed
%s::%s::%p::%d: failed to create task send image\n
%s: transport %p is not valid\n
AppleConvergedIPCRingDirection
%s::%s::%p::%d: num:%u size:%u\n
kABPPDPBadControlCommand
kACIPCPDPBadControlResponse
flushRead_block_invoke
sahara
it != fActiveIO.end()
poison
insertBH
%s::%s::%p::%d: in addComp added %u, started %u, service 0x%x\n
PCIPDPEvent.cpp
kABPPDPControlCommandFailed
kACIPCPDPCloningFailed
AppleBasebandPCIControl
ACIPCControlVariant
%s: PDPListener::stop() returned failure\n
%s::%s::%p::%d: failed to register time event 0x%08x\n
startChannelAsync
%s::%s::%p::%d: failed to start\n
%s::%s::%p::%d: deregister time event for domain %u failed 0x%x\n
AP-triggered baseband reset
%s: failed to open control driver\n
start
bind
%s::%p::%d::%s: failed to create task open in
%s::%p::%d::%s: reg %u, buffer %p, size %u
%s::%p::%d::%s: failed to create task map region
%s::%p::%d::%s: open pipe failed 0x%x
%s::%p::%d::%s: write failed 0x%x
could not add interest notification on service: %#x
%s::%p::%d::%s: failed to register time event 0x%08x
%s::%p::%d::%s: failed to create task unmap region
%s::%p::%d::%s: free:%zu active:%zu additional:%u
%s::%p::%d::%s: add interface %d
status block is required
%.*P
%s::%p::%d::%s: status 0x%x, region %u
%s::%p::%d::%s: failed to create task close in
%s::%p::%d::%s: failed to insert in system
%s::%p::%d::%s: failed to create kernel instance
%s::%p::%d::%s: %s failed, complete 0x%x, size %u, cookie %u
service is NULL - must successfully start() first
%s::%p::%d::%s: failed to create task open out
invalid interface number %d
%s::%p::%d::%s: %s: poisoned completion, status 0x%x
%s::%p::%d::%s: %u
%s::%p::%d::%s: num:%u size:%u
%s::%p::%d::%s: fRegistered\n
%s::%p::%d::%s: region %u, buffer %p, length %u
IOABPControlClass::stop() returned failure
failed to open control driver
a notification block is already registered. deregister it before registering a new block
%s::%p::%d::%s: failed to create bh
PDPListener::stop() returned failure
IOABPControlClass::registerEventCallback() returned %#x
PDPListener::registerEventCallback() returned %#x
failed to validate ioPool parameters
cannot use optimized transport
%s::%p::%d::%s: status 0x%x, buff %p, size %u
%s::%p::%d::%s: status 0x%x, buff %p, size %u, code %u
%s::%p::%d::%s: failed to create task read register
client cannot issue read for async transport
no params
%s::%p::%d::%s: %s (%u): param 0x%x: status 0x%x
%s::%p::%d::%s: time event not registered for domain %u
%s::%p::%d::%s: failed to deregister time event 0x%08x
%s::%p::%d::%s: status 0x%x, region %u, buff %p, size %u
%s::%p::%d::%s: %s: status 0x%x
%s::%p::%d::%s: failed to start
%s::%p::%d::%s: time event already registered for domain %u
could not create matching dictionary
%s::%p::%d::%s: domain %u, cb %p
%s::%p::%d::%s: region %u, cb %p
transport %p is not valid
failed to create transport internal
%s::%p::%d::%s: %p free:%zu active:%zu additional:%u
no memory
%s::%p::%d::%s: interface removed
Timeout waiting for deregistering kernel notifications
%s::%p::%d::%s: reg %u, buffer %p, length %u, timeout %u
%s::%p::%d::%s: domain %u
%s::%p::%d::%s: already pending for interface %d
failed to create Oversteer transport internal
invalid number of io
%s::%p::%d::%s: %p
got time event for domain %u with only %u args
unknown PCI variant
%s::%p::%d::%s: buffer %p, length %u, dDtor %p, timeout %u
%s::%p::%d::%s: buffer %p, size %u, dDtor %p
invalid configuration
invalid io size
%s::%p::%d::%s: 
%s::%p::%d::%s: in addComp added %u, started %u, service 0x%x
%s::%p::%d::%s: interface added
%s::%p::%d::%s: unmap region failed 0x%x
block must be provided
%s::%p::%d::%s: failed to create task read
invalid parameters
%s::%p::%d::%s: close pipe failed 0x%x
%s::%p::%d::%s: time sync failed 0x%x
unsupported PCI variant: daleipc
failed to create ioPool
%s::%p::%d::%s: domain %u, count %u, cb %p
%s::%p::%d::%s: region %u, buffer %p, length %u, cb %p
Oversteer: no tu transport object
%s::%p::%d::%s: read failed 0x%x
got time event for domain %u with status 0x%08x
%s::%p::%d::%s: deregister time event for domain %u failed 0x%x
%s (%#x), arg %p
%s::%p::%d::%s: buffer %p, length %u, cookie %u, dDtor %p, timeout %u
%s::%p::%d::%s: failed to create task send image
%s::%p::%d::%s: failed to create task time sync
failed to validate Oversteer transport parameters
%s::%p::%d::%s: failed to open 0x%x
%s::%p::%d::%s: send image failed 0x%x
%s::%p::%d::%s: failed to create task notify
%s::%p::%d::%s: failed to create task write
%s::%p::%d::%s: completion %u
%s::%p::%d::%s: Semaphore wait timed out!\n
creating Oversteer transport 
%s::%p::%d::%s: map region failed 0x%x
%s (%u), arg1 %p, arg2 %p
IOABPControlClass::start() returned failure
%s::%p::%d::%s: --done
%s::%p::%d::%s: notify interface removed
%s::%p::%d::%s: read register 0x%x
invalid control driver
PDPListener::start() returned failure
could not get matching service
%s::%p::%d::%s: %s: 
%s::%p::%d::%s: %s: failed to init
no tu transport object
%s::%p::%d::%s: %s complete 0x%x, size %u, cookie %u
bad argument
```
