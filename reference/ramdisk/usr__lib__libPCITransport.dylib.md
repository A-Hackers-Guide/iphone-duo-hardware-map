# `/usr/lib/libPCITransport.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 347,936 bytes.

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
%s::%s::%p::%d: Semaphore wait timed out!\n\n
%s::%s::%p::%d: failed to start\n
%s::%s::%p::%d: time event already registered for domain %u\n
readRegister_block_invoke
!fBind
%s: failed to create Oversteer transport internal\n
unsupported variant: daleipc
fAdditionalNumIO == 0
%s: Timeout waiting for deregistering kernel notifications\n
sendImageAsync_block_invoke
size <= fSize
TelephonyBasebandPCITransportFree
vector
%s::%s::%p::%d: map region failed 0x%x\n
writeAsync
gnss
iqtrace
deregisterTimeEvent_block_invoke
map region
: 
pci error (unsupported variant: daleipc): 
%s::%s::%p::%d: open pipe failed 0x%x\n
%s: unsupported PCI variant: daleipc\n
th
%s::%s::%p::%d: reg %u, buffer %p, size %u\n
v8@?0
TelephonyBasebandTransportFree
%s: failed to validate Oversteer transport parameters\n
vcom
readRegisterInternal
it != mbh.end()
boot_logger
kABPPDPWriteTimeout
v20@?0I8I12i16
open pipe
%s::%s::%p::%d: time event not registered for domain %u\n
%s::%s::%p::%d: unmap region failed 0x%x\n
AppleBasebandPCIPDPManagerBase
v28@?0i8^v12I20I24
init
)
%s: IOABPControlClass::start() returned failure\n
~th
flushRead
startChannelAsync
%s::%s::%p::%d: failed to create task open out\n
timesyncAsync
%s::%s::%p::%d: failed to deregister time event 0x%08x\n
v28@?0i8^v12^v20
PCITransportBH.cpp
%s::%s::%p::%d: %s (%u): param 0x%x: status 0x%x\n
v20@?0i8I12I16
time sync
v24@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8^v16
%s::%s::%p::%d: failed to create task map region\n
%s::%s::%p::%d: region %u, buffer %p, length %u, cb %p\n
poison
ari
ACIPCInterfaceProviderDevice
kACIPCPDPBadControlResponse
%s::%s::%p::%d: \n
insertBH
%s::%s::%p::%d: completion %u\n
refs
%s: IOABPControlClass::stop() returned failure\n
%s: a notification block is already registered. deregister it before registering a new block\n
kACIPCPDPBadMuxHeader
info
%s: invalid parameters\n
basic_string
%s::%s::%p::%d: num:%u size:%u\n
%s::%s::%p::%d: failed to create task write\n
unrecognized error code
sahara
%s: failed to open control driver\n
kACIPCPDPControlResponseFailed
fAsync
%s::%s::%p::%d: domain %u, count %u, cb %p\n
task
%s::%s::%p::%d: %s: failed to init\n
abortChannelAsync
PCITransportIOPool.cpp
unmapRegion
%s: %s (%#x), arg %p\n
%s: PDPListener::registerEventCallback() returned %#x\n
fEventNotificationPort
map::at:  key not found
TelephonyBasebandPCITransportRegisterTimeEvent
%s: invalid interface number %d\n
fBind->getCIO()
qmux2
deregisterTimeEvent
unmap region
%s: IOABPControlClass::registerEventCallback() returned %#x\n
registerEventNotification
timesyncAsync_block_invoke
%s::%s::%p::%d: domain %u\n
Callback.
~bh
kABPPDPBadControlResponse
%s::%s::%p::%d: failed to create task send image\n
unblockRead
~info
TelephonyBasebandPCITransport.cpp
TelephonyBasebandTransportRead
TelephonyBasebandTransportReadRegister
dpl
PCITransportKernel.cpp
%s::%s::%p::%d: close pipe failed 0x%x\n
read register
notify
%s: could not add interest notification on service: %#x\n
kACIPCPDPControlCommandFailed
%s: cannot use optimized transport\n
%s::%s::%p::%d: status 0x%x, buff %p, size %u\n
%s::%s::%p::%d: failed to create task unmap region\n
~task
rctth
ACIPCInterfaceProtocol
!called
%s::%s::%p::%d: %s complete 0x%x, size %u, cookie %u\n
start
kACIPCPDPReadFailed
%s::%s::%p::%d: failed to create task close in\n
%s::%s::%p::%d: %s: poisoned completion, status 0x%x\n
AppleConvergedIPCRingDirection
%s::%s::%p::%d: %p\n
kACIPCPDPOutboundPacketDropped
kACIPCPDPControlCommandDropped
%s::%s::%p::%d: status 0x%x, region %u, buff %p, size %u\n
%s::%s::%p::%d: %s: \n
bh
%s: block must be provided\n
readInternal
sendImage_block_invoke
TelephonyBasebandTransportWrite
TelephonyBasebandTransportCreate
TelephonyBasebandPCITransportWrite
TelephonyBasebandPCITransportUnblockRead
v28@?0I8^v12^v20
%s: got time event for domain %u with only %u args\n
writeInternal
complete
TelephonyBasebandPCITransportMapRegionwithClientData
AppleBasebandPCIControl
dir == kPCITransportDirectionIn || dir == kPCITransportDirectionOut
%s: invalid io size\n
imageCompletion
%s: invalid control driver\n
PCIEvent.cpp
false
eventNotification
v16@?0^{?=CC[2C]IQ}8
%s::%s::%p::%d: failed to register time event 0x%08x\n
%s::%s::%p::%d: read register 0x%x\n
sendImageInternal
%s::%s::%p::%d: region %u, cb %p\n
PCITransportTask.cpp
ioAlloc
!fNotifyTask
setEventNotificationPort
PCIPDPEvent.cpp
%s::%s::%p::%d: failed to create bh\n
%s: no tu transport object\n
%s: transport %p is not valid\n
TelephonyBasebandPCITransportFlushRead
AppleConvergedIPCRingIndex
validateParams
generateCallback_block_invoke
%s::%s::%p::%d: send image failed 0x%x\n
cb
TelephonyBasebandPCITransportRead
, 
kABPPDPOutboundPacketDropped
kABPPDPControlCommandDropped
unmapRegionAsync
%s::%s::%p::%d: %u\n
TelephonyBasebandPCITransportMapRegion
%s::%s::%p::%d: in addComp added %u, started %u, service 0x%x\n
v20@?0B8B12I16
close
read
notifyPDP
pdp error: 
fStatus != kIOReturnInvalid
pci error (unsupported variant: unknown): 
com.apple.WirelessIPC.baseband.pci_workloop
%s: \n
TelephonyBasebandPCITransportCreate
fActiveIO.size() == 0
com.apple.WirelessIPC.baseband.pci_bh
%s::%s::%p::%d: --done\n
allocate
%s: got time event for domain %u with status 0x%08x\n
%s::%s::%p::%d: region %u, buffer %p, length %u\n
com.apple.WirelessIPC.baseband.pci_client
%s: status block is required\n
%s::%s::%p::%d: buffer %p, length %u, dDtor %p, timeout %u\n
TelephonyBasebandPCITransportUnmapRegion
pci error: 
kABPPDPWriteFailed
v36@?0^v8I16{shared_ptr<pci::transport::ioPool>=^{ioPool}^{__shared_weak_count}}20
%s::%s::%p::%d: failed to create task time sync\n
removeBH
release
read_block_invoke
PCISystem.cpp
diag
v20@?0i8I12i16
close pipe
%s::%s::%p::%d: deregister time event for domain %u failed 0x%x\n
TelephonyBasebandTransportIsValid
qmux1
sendImage
registerTimeEvent_block_invoke
kACIPCPDPControlResponseDropped
%s::%s::%p::%d: domain %u, cb %p\n
unmapRegionAsync_block_invoke
IOGeneralInterest
readAsync
readAsync_block_invoke
%s::%s::%p::%d: add interface %d\n
transport
PCI
%s::%s::%p::%d: read failed 0x%x\n
AppleConvergedIPCPDPManager
kABPPDPInboundPacketDropped
kACIPCPDPWriteFailed
%s::%s::%p::%d: failed to create task notify\n
TelephonyBasebandPCITransportTimesync
write
kABPPDPControlResponseFailed
kACIPCPDPInboundPacketDropped
%s: failed to validate ioPool parameters\n
%s::%s::%p::%d: buffer %p, size %u, dDtor %p\n
%s::%s::%p::%d: status 0x%x, buff %p, size %u, code %u\n
~bind
cellular
%s::%s::%p::%d: time sync failed 0x%x\n
registerTimeEvent
v24@?0i8^^v12I20
%s: bad argument\n
control
%s: client cannot issue read for async transport\n
qdss
virtual_timesync
%s::%s::%p::%d: %s failed, complete 0x%x, size %u, cookie %u\n
kABPPDPBadControlCommand
PCITransportTH.cpp
%s::%s::%p::%d: reg %u, buffer %p, length %u, timeout %u\n
trace
IOAppleConvergedIPCControl
ioPool
readRegister
%s::%s::%p::%d: failed to create task open in\n
getTypeString
TelephonyBasebandTransportUnblockRead
hsfiler
%s::%s::%p::%d: failed to insert in system\n
%s::%s::%p::%d: interface removed\n
%s::%s::%p::%d: %s: status 0x%x\n
it != mth.end()
TelephonyBasebandPCITransportIsValid
com.apple.telephony.ipc
fFreeIO.size() == ( fNumIO + fAdditionalNumIO )
ioCompletion
kABPPDPControlResponseDropped
v12@?0B8
mediactl
IOAppleConvergedIPCInterface
%s: no params\n
%s: no memory\n
mapRegion
%s::%s::%p::%d: failed to create task read\n
boot
!fRunLoopRef
%s::%s::%p::%d: %p free:%zu active:%zu additional:%u\n
%s::%s::%p::%d: fRegistered\n\n
v24@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8I16i20
sendImageAsync
ioFree
TelephonyBasebandPCITransportSendImage
pbl
%s: PDPListener::stop() returned failure\n
write_block_invoke
at
~ioPool
v32@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8^v16^v24
kABPPDPBadMuxHeader
kABPPDPBadBearerMapping
eraseTH
it != fActiveIO.end()
%s: unknown PCI variant\n
writeAsync_block_invoke
%s::%s::%p::%d: buffer %p, length %u, cookie %u, dDtor %p, timeout %u\n
%s::%s::%p::%d: failed to create task read register\n
bind
TelephonyBasebandTransportSendImage
TelephonyBasebandPCITransportDeregisterTimeEvent
%s: invalid configuration\n
send image
%s: could not create matching dictionary\n
kABPPDPReadFailed
%s: Oversteer: no tu transport object\n
%s: failed to create transport internal\n
rom
init_block_invoke
%s::%s::%p::%d: interface added\n
setNotify
%s: PDPListener::start() returned failure\n
PCITransport
!fQueue
v12@?0I8
kACIPCPDPBadControlCommand
%s::%s::%p::%d: already pending for interface %d\n
TelephonyBasebandPCITransportReadRegister
lv-trace
%s: failed to create ioPool\n
mapRegionAsync
insertBH_block_invoke
%s::%s::%p::%d: failed to open 0x%x\n
%s: service is NULL - must successfully start() first\n
mapRegionAsync_block_invoke
TelephonyBasebandTransportFlushRead
%s: creating Oversteer transport \n
ACIPCControlVariant
AP-triggered baseband reset
: (
flushRead_block_invoke
%s::%s::%p::%d: free:%zu active:%zu additional:%u\n
open
%s::%s::%p::%d: write failed 0x%x\n
system
AppleConvergedIPCBBControl
AirshipDaleBasebandControl
lf-trace
mmapdebug
cmdCompletion
invalid
%s: could not get matching service\n
fCBL.empty()
%s::%s::%p::%d: failed to create kernel instance\n
fActive
~Listener
%s: %s (%u), arg1 %p, arg2 %p\n
kABPPDPControlCommandFailed
kACIPCPDPWriteTimeout
kACIPCPDPCloningFailed
%s: invalid number of io\n
%s::%s::%p::%d: notify interface removed\n
timesync
%s::%s::%p::%d: status 0x%x, region %u\n
no params
%s::%p::%d::%s: read failed 0x%x
invalid control driver
PDPListener::start() returned failure
could not create matching dictionary
a notification block is already registered. deregister it before registering a new block
%s::%p::%d::%s: status 0x%x, buff %p, size %u
no memory
%s::%p::%d::%s: 
%s::%p::%d::%s: %s (%u): param 0x%x: status 0x%x
%s::%p::%d::%s: close pipe failed 0x%x
%s (%u), arg1 %p, arg2 %p
service is NULL - must successfully start() first
cannot use optimized transport
%s::%p::%d::%s: reg %u, buffer %p, length %u, timeout %u
invalid io size
%s::%p::%d::%s: time sync failed 0x%x
%s::%p::%d::%s: map region failed 0x%x
PDPListener::stop() returned failure
block must be provided
failed to create ioPool
%s::%p::%d::%s: domain %u
%s::%p::%d::%s: failed to deregister time event 0x%08x
%s::%p::%d::%s: already pending for interface %d
%s::%p::%d::%s: %s complete 0x%x, size %u, cookie %u
%s::%p::%d::%s: open pipe failed 0x%x
%s::%p::%d::%s: time event already registered for domain %u
Timeout waiting for deregistering kernel notifications
PDPListener::registerEventCallback() returned %#x
%s::%p::%d::%s: failed to create task open out
%s::%p::%d::%s: status 0x%x, buff %p, size %u, code %u
%s::%p::%d::%s: completion %u
%s::%p::%d::%s: fRegistered\n
%s::%p::%d::%s: write failed 0x%x
%s (%#x), arg %p
%.*P
%s::%p::%d::%s: failed to create task read
%s::%p::%d::%s: failed to create task time sync
%s::%p::%d::%s: failed to create task map region
%s::%p::%d::%s: %u
%s::%p::%d::%s: add interface %d
%s::%p::%d::%s: Semaphore wait timed out!\n
failed to create Oversteer transport internal
%s::%p::%d::%s: notify interface removed
%s::%p::%d::%s: read register 0x%x
%s::%p::%d::%s: deregister time event for domain %u failed 0x%x
%s::%p::%d::%s: region %u, buffer %p, length %u
%s::%p::%d::%s: --done
%s::%p::%d::%s: failed to start
%s::%p::%d::%s: unmap region failed 0x%x
IOABPControlClass::stop() returned failure
IOABPControlClass::start() returned failure
could not get matching service
%s::%p::%d::%s: failed to create bh
invalid interface number %d
%s::%p::%d::%s: %p
%s::%p::%d::%s: failed to create kernel instance
%s::%p::%d::%s: buffer %p, length %u, dDtor %p, timeout %u
%s::%p::%d::%s: failed to register time event 0x%08x
%s::%p::%d::%s: status 0x%x, region %u
%s::%p::%d::%s: failed to create task close in
client cannot issue read for async transport
%s::%p::%d::%s: %p free:%zu active:%zu additional:%u
%s::%p::%d::%s: time event not registered for domain %u
failed to validate ioPool parameters
%s::%p::%d::%s: buffer %p, size %u, dDtor %p
%s::%p::%d::%s: buffer %p, length %u, cookie %u, dDtor %p, timeout %u
%s::%p::%d::%s: domain %u, cb %p
%s::%p::%d::%s: failed to create task unmap region
failed to open control driver
could not add interest notification on service: %#x
%s::%p::%d::%s: failed to create task write
%s::%p::%d::%s: %s: 
Oversteer: no tu transport object
failed to create transport internal
%s::%p::%d::%s: in addComp added %u, started %u, service 0x%x
%s::%p::%d::%s: %s failed, complete 0x%x, size %u, cookie %u
%s::%p::%d::%s: send image failed 0x%x
got time event for domain %u with only %u args
%s::%p::%d::%s: failed to create task notify
%s::%p::%d::%s: %s: status 0x%x
got time event for domain %u with status 0x%08x
bad argument
unsupported PCI variant: daleipc
failed to validate Oversteer transport parameters
no tu transport object
IOABPControlClass::registerEventCallback() returned %#x
%s::%p::%d::%s: %s: failed to init
invalid parameters
invalid number of io
%s::%p::%d::%s: num:%u size:%u
status block is required
%s::%p::%d::%s: failed to create task send image
%s::%p::%d::%s: reg %u, buffer %p, size %u
%s::%p::%d::%s: failed to create task read register
%s::%p::%d::%s: %s: poisoned completion, status 0x%x
transport %p is not valid
%s::%p::%d::%s: free:%zu active:%zu additional:%u
%s::%p::%d::%s: failed to insert in system
%s::%p::%d::%s: interface removed
%s::%p::%d::%s: failed to create task open in
invalid configuration
%s::%p::%d::%s: failed to open 0x%x
%s::%p::%d::%s: interface added
unknown PCI variant
%s::%p::%d::%s: domain %u, count %u, cb %p
%s::%p::%d::%s: region %u, buffer %p, length %u, cb %p
%s::%p::%d::%s: status 0x%x, region %u, buff %p, size %u
%s::%p::%d::%s: region %u, cb %p
creating Oversteer transport 
```
