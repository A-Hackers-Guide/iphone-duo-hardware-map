# `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit`

From the upgrade restore ramdisk (141-29011-104.dmg). 731,904 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 2392)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libSystem.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (476)

```
ivars->waiter == token
returnCommand_block_invoke
!loadEntry
(count + idx) <= serial->ivars->maxIndex
ARRAY
OSSerializationAddBinaryObject
OSObjectLogInternal
is local target\n
OSMetaClassBase
0 == lvars->reentrantLock->thread
virtual IOReturn IOReporter_IVars::handleSwapPrepare(int)
%s: inconsistent size for SHA512 context
OSMetaClassBase::InvokeRemote(0x%x) 0x%qx 0x%qx %p %p\n
group
msg
%s: kIOUserServerMethodStart failed, exiting\n
is action\n
IODispatchQueue::Create(Default) %p\n
i24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^Q16
serial
convert_mach_time_to_nsec
OSDictionaryApply_block_invoke
OSDynamicCast(OSString, key.object)
virtual IOReturn IOReporter_IVars::copyElementValues(int, IOReportElementValues *)
%sbacktrace:\n
Default
kOSSerializeDictionary == (kOSSerializeTypeMask & key)
OSSerializationSize
newNChannels
virtual IOReturn IOStateReporter_IVars::handleSetStateID(uint64_t, int, uint64_t)
server
OSCopyOutObjects
B24@?0r*8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
OSAction__IOBlockStorageDevice_KernelCompletion
IOLib.cpp
/
Boot args: %s\n
IORPCMessageFromMach
rlock
LockTest ok\n
DATA
source != nullptr
virtual IOReturn IOStateReporter_IVars::handleSwapPrepare(int)
kern.bootargs
IORecursiveConditionLockUnlock
IODispatchQueue::Create(%s, %s, %d)\n
OSCollectionEntryArrayCount
OSCollections.cpp
MACH_PORT_NULL != remotePriv->objectRef
CopyCurrentThread
^^{OSMetaClassBaseRemotePrivate}
sendSize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage))
class %s duplicate\n
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
I
unexpected end of buffer
OSObjectAllocate
no services, exiting\n
__DATA_CONST
IOReportGroupName
buildBoolean
IOService::SetDispatchQueue(%s, %s)\n
len <= kOSSerializeDataMask
%s\"%s\"\n
forward reference detected
MACH_PORT_DEAD != remotePriv->objectRef
%s: class not found\n
OSObjectFree
!upgrade
%s queue: %s\n
Create_Impl
_NewUserClient_Impl
v24@?0r^v8Q16
Found class: %s\n
idx < maxIndex
[%#qx] SERVER MSG:
clock_get_calendar_nanotime
Assertion failed: (%s), file %s, line %d.\n
Using guard pages: requested guard size is %zu, rounding up to %zu\n
reply->__hdr.msgid == OSObject_Instantiate_ID
OSSerializationAppendBytes
buildData
OSUnserializeXML: %s near line %d\n
refcount
STRING
ivar(nElements)
virtual IOReturn IOStateReporter_IVars::updateChannelValues(int)
0 == lvars->reentrantLock->count
(kOSSerializeArray == (kOSSerializeTypeMask & key)) || (kOSSerializeSet == (kOSSerializeTypeMask & key))
Wait
OSCollectionEntryDictionaryCount
~IOHistogramReporter_IVars
buffer
SET
uniq->string == this
!err
rwlock
bundlePathFromExecutablePath
~IOReporter_IVars
Register class: %s (super %s) object %p ref %qd\n
_OSObjectCopyIn
superEntry
operator[]
data
OSStringCreate
value.object
hex
0 == err
self != NULL
SetEventlinkPort_Impl
LockTest
_IODispatchQueueSleep
DICT
%s - %s <= 0!
int64_t
virtual IOReturn IOStateReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
%s: inconsistent size for AES encrypt context\n
sendRights
kern.backtrace.user
plist
kr == KERN_SUCCESS
q2->OnQueue()
true
local
lock->count
OSDictionarySetValueInternal
IOService::finalize\n
IOService::Stop_async\n
loadEntry
OSSerializationDictionaryApply
!parent
objectRefsListEntry.le_prev
OSAction_IOUserClient_KernelCompletion
(desc->queueNamesOffset + desc->queueNamesSize) <= descSize
Cancel
IOUserClientQueueExternalMethod
OSCollectionEntryArrayApply
err == 0
format
IORWLockUnlock
vstr
IOReportLegend
SHA256_Init
(kIOLockAssertOwned == type) || (kIOLockAssertNotOwned == type)
BAD REPLY ID 0x%x\n
OSRegisterClasses
OSCollectionsRunInitializers(%s)\n
set
WillWait
freeBuffer
{CompactArray<IODispatchQueue *>=(?=^^{IODispatchQueue}^{IODispatchQueue})I}
Invoke from %s 0x%qx, q %s refs %llx rpcKernel %d %s\n
size >= queueCount * sizeof(machReply->objects[0])
allocLen >= length
B40@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24(OSCo
Invoke
IOUserServerMain
100 == count
OSScanClassesInMachO(%s)\n
GetReference
str != NULL
SYMBOL
(desc->methodOptionsOffset + desc->methodOptionsSize) <= descSize
oneway || (replySize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage)))
[%#qx] INVOKE MSG:
<internal error>
OSScanStringsInMachO
%s%qd\n
oldcount < INT16_MAX
uioserver
IORecursiveConditionLockHaveLock(lvars->reentrantLock)
allocLen >= newLength
%s - %s > INT_MAX / sizeof(%s)!
release
IOService:/
service == nullptr
[%#qx] SERVER REPLY:
dsource
idx < size
B32@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24
IOStateReporter::handleAddChannelSwap ivar(lastUpdateTimes) unset despite non-NULL ivar(currentStates)
abstime
Failed to cast object of type %s to %s
KERN_SUCCESS == kr
Q
uflags
S
maximum object count
OSObjectPortFinalize
IONameMatch
/Info.plist
content:
serial->ivars->maxIndex >= 2
objectRefsListEntry.le_next
%s%s\n
KERN_SUCCESS == ret
OSObjectAllocate 0x%qx %s remote %d, flags %#x, qc %d, mc %d\n
SHA512_Init
maximum object reference count
string
msgid == action->ivars->msgid
ivars
tempPathLen < sizeof(tempPath)
B16@?0^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSString_IVars}^{OSString_LocalIVars})}8
OSDataAppendBytes
Failed to fstat %s: %s\n
OnQueue SDK version 0x%x\n
OSCopyInObjects
IOReportChannelInfo
incrementChannelState() cannot be used after setChannelState()!\n
IOTimerDispatchSourceQueue-%s-%p
Failed to find class: %s
retain
IODataQueueDispatchSourceShared.h
ckey
%s - %s > INT_MAX / sizeof(%s)!\n
pthread_self() == lock->thread
IOUserServerMain_block_invoke_3
Open file: %s\n
%s %d queues\n
virtual IOReturn IOReporter_IVars::setElementValues(int, IOReportElementValues *, uint64_t)
^Q
_absolutetime_to_nanoseconds
Failed to mmap region of size %zu: %s\n
[%#qx] 0x%016qx: %s\n
v8@?0
OSCopyInObjects_block_invoke_2
idx < serial->ivars->maxIndex
finalizeBuffer
overrideChannelState() cannot be used after setChannelState()!\n
IORWLockRead
OSCollectionEntryTypeID
%s was called out of locked context!
IORecursiveConditionLockLock
IORecursiveConditionLockHaveLock
Create
OSSerializationGetStringLength
QueueForObject
SHA384_Init
_nanoseconds_to_absolutetime
OSObjectTryRetain
WakeupWithOptions
%s-Default
buildArray
/* %04lx: */ %-96s /* |%-16s| */\n
key
0 == lock->count
CopyNextNotification ret 0x%x\n
EndWait
handleSwapPrepare
%s: segment size overflow
virtual IOReturn IOStateReporter_IVars::handleSetStateByIndices(int, int, uint64_t, uint64_t)
memory exhausted
%s - can't free %d channels of dimension %d
IOReturn IOStateReporter_IVars::_getStateIndices(uint64_t, uint64_t, int *, int *)
nanosecs
remotePriv
OSSerializationArrayApply
server->serviceCount
buildNumber
no services left, exiting\n
lvars->recvport == hdr->msgh_local_port
NUMBER
handleCreateLegend
remoteQueueCount
q1
IOReportChannelConfig
i24@?0Q8^^{OSObject}16
serial->ivars->bufLen == 0 || serial->ivars->buffer != nullptr
OSLoadBundleByPath
_NO_NAME_4
objectRef
%strue
clock_get_system_nanotime
ivars->queue->OnQueue()
OSCollectionEntryDictionaryApply
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
usage: %s <server name> <server tag> <bundle ID> <bundle executable path> [<bundle executable path>] ...\n
OSRegisterClass
Root
%s allocated %p\n
__osstringinfo
size != 0
IOService::SetPowerState(%s, %d) ack kernel\n
serialOut
failed to copy in object: 0x%x
ivar(nChannels)
array
MACH_PORT_NULL != objectName1
is canceled action\n
ThreadStart
ckey || searchkey
IOReportChannels
debug=0x%qx\n
%u
self == OSDynamicCast(IOThread, self)
OSStringHash
%s: inconsistent size for SHA384 context
OSCreateObjectFromSerializationInternal
remoteMethods
oldsize == buflen
OSObjectCopyOut
bundlePath != NULL
^{IOUserServer_IVars=}
debug
size
CreatePropertyMatchingDictionary
IOProviderClass
%s(0x%lx):\n
IORecursiveConditionLockTryLock
/DriverKit
remoteQueues
              0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F\n
Registered: %s\n
Dispatch
Failed to open %s: %s\n
OSSerializationValue
%s[%d] key:\"%s\"\n
virtual void IOStateReporter_IVars::handleSwapCleanup(int)
???
IORWLockWrite
ret == kIOReturnSuccess
handleAddChannelSwap
swapNElements
IOHistogramSegmentConfig
dk
getHexData
GetLength
OSStringCreate(\"%s\", %ld should be %ld)\n
count && tags
virtual const IOReportElementValues *IOReporter_IVars::getElementValues(int)
syntax error
buildString
Fatal error: %s::init() method failed during copy-in\n
OSUnserializeBinary
IOReportChannelUnit
DispatchConcurrent_f
OSMetaClassAllocate
virtual IOReturn IOReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
0x%02x, 
kIOReturnSuccess == kr
[0{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}]
replySize <= rpc.replySize
q1->OnQueue()
[%#qx] %p %#qx flags %#qx object %#qx \n
allocLen >= bufferLen
int
OSMetaClassBaseRemotePrivate
SERIALIZATION
OSCollectionTypeName
remoteMethodsCount
noq
duplicate dictionary key
serverTagStrEnd[0] == '\\0'
lvars->waitTokens
IOService::Stop kernel done 0x%x\n
newNElements
IOReturn IOReporter_IVars::updateReportChannel(int, uint32_t &, uint8_t *&, size_t &)
open(kIOKitUserServerClientType) %s (0x%x)\n
clock_get_calendar_microtime
count < INT16_MAX
%s[%d]:\n
length <= kOSSerializeDataMask
mach_msg: 
createTimerDispatchSource
^{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}
SetWorkGroupPort_Impl
ret == KERN_SUCCESS
IOReporter::_swap* already in use
IOReportSubGroupName
kflags
uioserver.cpp
SleepWithDeadline
Map
release_ret == KERN_SUCCESS
kIOReturnSuccess == ret
free %s %p 0x%qx %d\n
oldcount > 0
queue
DeliverNotifications_block_invoke
%sfalse\n
InvokeRemote
lvars->queue
IOUserClass
gatedGetCommand
IOThreadStart
ivar(segmentCount)
notsync || !remote || (msgid == IOService_Start_ID) || queue->OnQueue()
IORWLockAlloc
init
uiomachchannel
IOReportElement
false
OSUnserializeXML.y
IOPropertyMatch
roundSerializationSize
OSFindClass
IOLockAssert
%s:%d: failed assertion `%s'\n
swapNChannels
~IOStateReporter_IVars
dict
lvars->ipcchannel
kr == kIOReturnSuccess
serviceCount %d\n
OSDictionaryGetEntry_block_invoke
%s - %s <= 0!\n
remote
free
reset
B32@?0Q8Q16Q24
serial != nullptr
aes_encrypt_key
%s: inconsistent size for AES decrypt context\n
queueArray
Failed to mmap file %s, size %lld at %p in mapped region %p->%p: %s\n
IOStateReporter::_swap* already in use
(replyTo == 0) == (0 != (kIORPCMessageOneway & message->flags))
length
OSUnserializeXML: can't alloc temp memory
Assertion failed: (%s), function %s, file %s, line %d.\n
Kernel requested exit (%s)\n
__osclassinfo
IOInterruptDispatchSourceThread
virtual void IOReporter_IVars::handleSwapCleanup(int)
meta
B24@?0Q8Q16
%s: inconsistent size for SHA256 context
remotePrivate
OSSerializationTypeID
aes_decrypt_key
[%#qx] INVOKE REPLY:
0 == deadline
%s<NULL>\n
handleSwapCleanup
OSCreateSerializationFromBytesWithCopyInHandler
buildSet
NULL == ivars->waiter
lock
idx < source->ivars->maxIndex
OSMetaClassBasePrivate
buildDictionary
BAD REPLY SIZE 0x%x\n
WakeAtTime_Impl
DidAction
OSDataCreate
IOTimerDispatchSource: *** DRIVERKIT CLIENT BUG ***: double timer cancellation
refs <= mach->msgh_body.msgh_descriptor_count
%s doesn't support shrinking
lvars->reentrantLock
!lvars->mappings
BOOLEAN
%s was called out of config locked context!
-
ret == 0
q2
Load module %s\n
integer
OSScanClassesInMachO
Server
uint64_t
(null)
Bad msg:
Cancel_Impl
com.motu.driver
CreateMapping fail(0x%x)\n
gatedReturnCommand
size >= sizeof(OSObject_Instantiate_Rpl)
!(MACH_PORT_VALID(hdr->msgh_remote_port))
OSMetaClassBasePrivate.h
\n
refs <= maxObjectCount
__DATA
priv->queueArray
%s
%{public}s
```
