# `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 731,904 bytes.

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
rwlock
OSDataCreate
B32@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24
DispatchConcurrent_f
GetReference
returnCommand_block_invoke
NUMBER
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
clock_get_system_nanotime
server
unexpected end of buffer
OnQueue SDK version 0x%x\n
Found class: %s\n
finalizeBuffer
OSSerializationSize
buildData
lvars->recvport == hdr->msgh_local_port
B24@?0r*8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
ivar(nElements)
???
IOService::finalize\n
DICT
serial->ivars->maxIndex >= 2
set
(desc->queueNamesOffset + desc->queueNamesSize) <= descSize
MACH_PORT_NULL != objectName1
OSObjectAllocate
OSObjectAllocate 0x%qx %s remote %d, flags %#x, qc %d, mc %d\n
InvokeRemote
NULL == ivars->waiter
%s[%d]:\n
v8@?0
IORecursiveConditionLockTryLock
IOProviderClass
WakeAtTime_Impl
serial->ivars->bufLen == 0 || serial->ivars->buffer != nullptr
roundSerializationSize
OSCreateSerializationFromBytesWithCopyInHandler
OSMetaClassBase
[%#qx] SERVER MSG:
B32@?0Q8Q16Q24
newNElements
remotePrivate
meta
remote
duplicate dictionary key
              0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F\n
idx < serial->ivars->maxIndex
%s%s\n
IOReportChannels
key
q1->OnQueue()
str != NULL
len <= kOSSerializeDataMask
IOStateReporter::handleAddChannelSwap ivar(lastUpdateTimes) unset despite non-NULL ivar(currentStates)
Dispatch
BAD REPLY SIZE 0x%x\n
!loadEntry
%s\"%s\"\n
length <= kOSSerializeDataMask
~IOReporter_IVars
Failed to open %s: %s\n
OSCollectionEntryArrayApply
remoteQueueCount
OSObjectTryRetain
Cancel
uiomachchannel
%s - %s > INT_MAX / sizeof(%s)!
abstime
Failed to cast object of type %s to %s
sendSize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage))
WakeupWithOptions
OSStringHash
overrideChannelState() cannot be used after setChannelState()!\n
serviceCount %d\n
Cancel_Impl
B16@?0^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSString_IVars}^{OSString_LocalIVars})}8
OSCollectionEntryDictionaryApply
remoteMethods
string
%u
IOTimerDispatchSourceQueue-%s-%p
Failed to mmap region of size %zu: %s\n
gatedGetCommand
IOReportChannelInfo
_NO_NAME_4
virtual void IOStateReporter_IVars::handleSwapCleanup(int)
reply->__hdr.msgid == OSObject_Instantiate_ID
virtual IOReturn IOStateReporter_IVars::handleSwapPrepare(int)
kflags
false
_NewUserClient_Impl
i24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^Q16
virtual IOReturn IOStateReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
clock_get_calendar_microtime
refcount
%s:%d: failed assertion `%s'\n
q2->OnQueue()
IOReturn IOReporter_IVars::updateReportChannel(int, uint32_t &, uint8_t *&, size_t &)
[%#qx] SERVER REPLY:
(count + idx) <= serial->ivars->maxIndex
0x%02x, 
OSLoadBundleByPath
rlock
OSCollectionTypeName
value.object
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
B24@?0Q8Q16
%s: inconsistent size for SHA512 context
_OSObjectCopyIn
buildBoolean
size
OSObjectPortFinalize
retain
newNChannels
debug
__osstringinfo
%strue
\n
OSUnserializeXML: %s near line %d\n
_nanoseconds_to_absolutetime
Map
SET
ckey || searchkey
!parent
buildString
Bad msg:
no services, exiting\n
objectRefsListEntry.le_prev
!upgrade
com.motu.driver
OSSerializationDictionaryApply
%s: inconsistent size for SHA384 context
OSCopyInObjects
__DATA_CONST
[0{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}]
oldcount < INT16_MAX
refs <= mach->msgh_body.msgh_descriptor_count
Boot args: %s\n
[%#qx] INVOKE REPLY:
ivars->queue->OnQueue()
virtual const IOReportElementValues *IOReporter_IVars::getElementValues(int)
OSObjectFree
Registered: %s\n
ret == kIOReturnSuccess
self != NULL
%s %d queues\n
oldsize == buflen
incrementChannelState() cannot be used after setChannelState()!\n
_absolutetime_to_nanoseconds
Root
Wait
IONameMatch
0 == lvars->reentrantLock->thread
buildArray
IORecursiveConditionLockHaveLock(lvars->reentrantLock)
%s<NULL>\n
OSCreateObjectFromSerializationInternal
SHA512_Init
KERN_SUCCESS == ret
IORecursiveConditionLockHaveLock
OSCopyOutObjects
(replyTo == 0) == (0 != (kIORPCMessageOneway & message->flags))
OSDictionaryApply_block_invoke
IOHistogramSegmentConfig
%s: segment size overflow
buildDictionary
nanosecs
size >= queueCount * sizeof(machReply->objects[0])
100 == count
virtual void IOReporter_IVars::handleSwapCleanup(int)
IORWLockWrite
BAD REPLY ID 0x%x\n
gatedReturnCommand
ret == KERN_SUCCESS
SetEventlinkPort_Impl
uniq->string == this
serverTagStrEnd[0] == '\\0'
[%#qx] %p %#qx flags %#qx object %#qx \n
OSDictionarySetValueInternal
Using guard pages: requested guard size is %zu, rounding up to %zu\n
serial
IORWLockRead
ARRAY
err == 0
release_ret == KERN_SUCCESS
LockTest
length
QueueForObject
[%#qx] INVOKE MSG:
failed to copy in object: 0x%x
freeBuffer
OSCollectionEntryDictionaryCount
%s(0x%lx):\n
%s: kIOUserServerMethodStart failed, exiting\n
count && tags
%s - %s > INT_MAX / sizeof(%s)!\n
Failed to fstat %s: %s\n
Assertion failed: (%s), file %s, line %d.\n
q2
<internal error>
Q
kern.bootargs
/DriverKit
size >= sizeof(OSObject_Instantiate_Rpl)
OSDataAppendBytes
idx < source->ivars->maxIndex
ivars
OSSerializationArrayApply
%s was called out of config locked context!
aes_encrypt_key
lock
operator[]
vstr
%s - can't free %d channels of dimension %d
^{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}
Fatal error: %s::init() method failed during copy-in\n
%sfalse\n
Kernel requested exit (%s)\n
!lvars->mappings
lock->count
plist
OSFindClass
IOInterruptDispatchSourceThread
int64_t
OSMetaClassBaseRemotePrivate
/
kIOReturnSuccess == ret
is action\n
!err
virtual IOReturn IOReporter_IVars::handleSwapPrepare(int)
handleAddChannelSwap
msgid == action->ivars->msgid
IORWLockAlloc
IOPropertyMatch
%s doesn't support shrinking
lvars->ipcchannel
IODispatchQueue::Create(Default) %p\n
class %s duplicate\n
integer
(desc->methodOptionsOffset + desc->methodOptionsSize) <= descSize
DeliverNotifications_block_invoke
OSCollectionEntryTypeID
IOReportGroupName
Assertion failed: (%s), function %s, file %s, line %d.\n
group
OSSerializationTypeID
OSObjectLogInternal
swapNChannels
%s: inconsistent size for AES encrypt context\n
IOUserClass
OSSerializationAddBinaryObject
/* %04lx: */ %-96s /* |%-16s| */\n
data
virtual IOReturn IOReporter_IVars::copyElementValues(int, IOReportElementValues *)
~IOStateReporter_IVars
{CompactArray<IODispatchQueue *>=(?=^^{IODispatchQueue}^{IODispatchQueue})I}
open(kIOKitUserServerClientType) %s (0x%x)\n
superEntry
IOThreadStart
allocLen >= length
dict
Create_Impl
WillWait
IOReturn IOStateReporter_IVars::_getStateIndices(uint64_t, uint64_t, int *, int *)
getHexData
priv->queueArray
IOService::SetDispatchQueue(%s, %s)\n
__osclassinfo
IOService::Stop kernel done 0x%x\n
handleCreateLegend
CreateMapping fail(0x%x)\n
B40@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24(OSCo
IOReportLegend
-
count < INT16_MAX
I
OSAction_IOUserClient_KernelCompletion
ThreadStart
self == OSDynamicCast(IOThread, self)
0 == lvars->reentrantLock->count
objectRef
[%#qx] 0x%016qx: %s\n
server->serviceCount
%s queue: %s\n
init
IODataQueueDispatchSourceShared.h
__DATA
virtual IOReturn IOStateReporter_IVars::handleSetStateByIndices(int, int, uint64_t, uint64_t)
remoteMethodsCount
notsync || !remote || (msgid == IOService_Start_ID) || queue->OnQueue()
IOService::SetPowerState(%s, %d) ack kernel\n
OSMetaClassAllocate
ivar(nChannels)
remotePriv
GetLength
OSObjectCopyOut
dsource
OSMetaClassBase::InvokeRemote(0x%x) 0x%qx 0x%qx %p %p\n
%s-Default
refs <= maxObjectCount
msg
OSDynamicCast(OSString, key.object)
buildSet
^{IOUserServer_IVars=}
OSDictionaryGetEntry_block_invoke
%sbacktrace:\n
LockTest ok\n
reset
%s: inconsistent size for AES decrypt context\n
maximum object reference count
noq
SleepWithDeadline
IOService::Stop_async\n
OSScanStringsInMachO
%s%qd\n
/Info.plist
IOReporter::_swap* already in use
Invoke from %s 0x%qx, q %s refs %llx rpcKernel %d %s\n
ivars->waiter == token
OSMetaClassBasePrivate.h
OSAction__IOBlockStorageDevice_KernelCompletion
true
ret == 0
q1
kr == kIOReturnSuccess
SHA256_Init
maximum object count
oldcount > 0
IOUserServerMain_block_invoke_3
OSSerializationValue
IOTimerDispatchSource: *** DRIVERKIT CLIENT BUG ***: double timer cancellation
Open file: %s\n
STRING
is canceled action\n
uioserver.cpp
IOService:/
IOLib.cpp
free %s %p 0x%qx %d\n
no services left, exiting\n
swapNElements
MACH_PORT_NULL != remotePriv->objectRef
OSUnserializeXML: can't alloc temp memory
Register class: %s (super %s) object %p ref %qd\n
DATA
OSCollectionEntryArrayCount
!(MACH_PORT_VALID(hdr->msgh_remote_port))
OSSerializationGetStringLength
virtual IOReturn IOReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
kr == KERN_SUCCESS
loadEntry
kOSSerializeDictionary == (kOSSerializeTypeMask & key)
0 == lock->count
convert_mach_time_to_nsec
content:
forward reference detected
Failed to find class: %s
allocLen >= bufferLen
IOReportChannelUnit
0 == deadline
int
%s was called out of locked context!
OSSerializationAppendBytes
local
usage: %s <server name> <server tag> <bundle ID> <bundle executable path> [<bundle executable path>] ...\n
uioserver
virtual IOReturn IOReporter_IVars::setElementValues(int, IOReportElementValues *, uint64_t)
IOReportChannelConfig
format
CreatePropertyMatchingDictionary
lvars->reentrantLock
%s allocated %p\n
size != 0
allocLen >= newLength
serial != nullptr
memory exhausted
kern.backtrace.user
CopyNextNotification ret 0x%x\n
OSStringCreate
^^{OSMetaClassBaseRemotePrivate}
OSRegisterClass
(null)
is local target\n
serialOut
v24@?0r^v8Q16
OSScanClassesInMachO
IOStateReporter::_swap* already in use
%s: inconsistent size for SHA256 context
replySize <= rpc.replySize
IORecursiveConditionLockLock
(kOSSerializeArray == (kOSSerializeTypeMask & key)) || (kOSSerializeSet == (kOSSerializeTypeMask & key))
SHA384_Init
sendRights
remoteQueues
OSMetaClassBasePrivate
oneway || (replySize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage)))
EndWait
Failed to mmap file %s, size %lld at %p in mapped region %p->%p: %s\n
OSCopyInObjects_block_invoke_2
buildNumber
OSUnserializeXML.y
IORPCMessageFromMach
lvars->waitTokens
OSRegisterClasses
createTimerDispatchSource
OSStringCreate(\"%s\", %ld should be %ld)\n
virtual IOReturn IOStateReporter_IVars::updateChannelValues(int)
i24@?0Q8^^{OSObject}16
~IOHistogramReporter_IVars
aes_decrypt_key
IORecursiveConditionLockUnlock
CopyCurrentThread
Server
virtual IOReturn IOStateReporter_IVars::handleSetStateID(uint64_t, int, uint64_t)
array
Create
%s - %s <= 0!
handleSwapPrepare
lvars->queue
buffer
%s: class not found\n
IOLockAssert
IORWLockUnlock
kIOReturnSuccess == kr
IOReportElement
bundlePath != NULL
idx < size
OSCollections.cpp
queueArray
queue
IODispatchQueue::Create(%s, %s, %d)\n
tempPathLen < sizeof(tempPath)
BOOLEAN
ivar(segmentCount)
Invoke
service == nullptr
%s[%d] key:\"%s\"\n
S
syntax error
KERN_SUCCESS == kr
hex
IOReportSubGroupName
^Q
clock_get_calendar_nanotime
mach_msg: 
DidAction
uflags
SetWorkGroupPort_Impl
(kIOLockAssertOwned == type) || (kIOLockAssertNotOwned == type)
pthread_self() == lock->thread
release
0 == err
OSCollectionsRunInitializers(%s)\n
_IODispatchQueueSleep
%s - %s <= 0!\n
MACH_PORT_DEAD != remotePriv->objectRef
bundlePathFromExecutablePath
source != nullptr
handleSwapCleanup
objectRefsListEntry.le_next
dk
SYMBOL
uint64_t
free
Default
IOUserClientQueueExternalMethod
ckey
idx < maxIndex
debug=0x%qx\n
IOUserServerMain
OSScanClassesInMachO(%s)\n
OSUnserializeBinary
Load module %s\n
SERIALIZATION
%{public}s
%s
```
