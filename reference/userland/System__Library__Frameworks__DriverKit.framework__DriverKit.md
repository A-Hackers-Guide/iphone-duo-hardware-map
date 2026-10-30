# `/System/Library/Frameworks/DriverKit.framework/DriverKit`

iOS 27.2 dyld shared cache image. Version `509.40.11.0.0`. **[DSC]**

## Linked libraries (2)

- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libc++.1.dylib`

## Strings (476)

```
IODispatchQueue::Create(%s, %s, %d)\n
OSDynamicCast(OSString, key.object)
%s - can't free %d channels of dimension %d
uint64_t
memory exhausted
is action\n
[%#qx] INVOKE REPLY:
              0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F\n
noq
usage: %s <server name> <server tag> <bundle ID> <bundle executable path> [<bundle executable path>] ...\n
IOService:/
serial->ivars->maxIndex >= 2
queueArray
%s allocated %p\n
DATA
SERIALIZATION
integer
kr == KERN_SUCCESS
is local target\n
OSObjectAllocate
!(MACH_PORT_VALID(hdr->msgh_remote_port))
int
serviceCount %d\n
0 == lock->count
%s - %s <= 0!
count < INT16_MAX
priv->queueArray
IOUserClientQueueExternalMethod
OSCollectionsRunInitializers(%s)\n
!err
Fatal error: %s::init() method failed during copy-in\n
OSMetaClassBasePrivate.h
IORecursiveConditionLockTryLock
OSSerializationSize
newNElements
key
abstime
OSScanStringsInMachO
DidAction
ivar(nElements)
^{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}
(kIOLockAssertOwned == type) || (kIOLockAssertNotOwned == type)
bundlePathFromExecutablePath
source != nullptr
IOReportElement
%s - %s > INT_MAX / sizeof(%s)!\n
remoteQueueCount
B32@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24
kOSSerializeDictionary == (kOSSerializeTypeMask & key)
virtual IOReturn IOStateReporter_IVars::updateChannelValues(int)
sendRights
IORecursiveConditionLockHaveLock(lvars->reentrantLock)
allocLen >= newLength
B24@?0r*8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
[%#qx] 0x%016qx: %s\n
CreateMapping fail(0x%x)\n
/
SetWorkGroupPort_Impl
ret == 0
superEntry
OSCreateSerializationFromBytesWithCopyInHandler
OSFindClass
refs <= mach->msgh_body.msgh_descriptor_count
OSObjectCopyOut
server
debug
free
group
__osstringinfo
tempPathLen < sizeof(tempPath)
OSSerializationTypeID
~IOStateReporter_IVars
^{IOUserServer_IVars=}
maximum object count
remote
__DATA
syntax error
i24@?0Q8^^{OSObject}16
SYMBOL
IOReportChannelUnit
Assertion failed: (%s), function %s, file %s, line %d.\n
lvars->ipcchannel
dsource
kflags
hex
IORecursiveConditionLockHaveLock
WillWait
%strue
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
IOStateReporter::_swap* already in use
remoteMethodsCount
_IODispatchQueueSleep
newNChannels
handleAddChannelSwap
/DriverKit
IOProviderClass
OSDictionaryGetEntry_block_invoke
Assertion failed: (%s), file %s, line %d.\n
com.motu.driver
size >= sizeof(OSObject_Instantiate_Rpl)
EndWait
virtual IOReturn IOReporter_IVars::handleSwapPrepare(int)
handleSwapCleanup
debug=0x%qx\n
kIOReturnSuccess == ret
no services left, exiting\n
_NewUserClient_Impl
idx < serial->ivars->maxIndex
aes_decrypt_key
uflags
Load module %s\n
IOReturn IOReporter_IVars::updateReportChannel(int, uint32_t &, uint8_t *&, size_t &)
incrementChannelState() cannot be used after setChannelState()!\n
OSAction_IOUserClient_KernelCompletion
uioserver
ivars->queue->OnQueue()
OSCollections.cpp
%s: inconsistent size for SHA512 context
Invoke
LockTest ok\n
vstr
ckey
OSUnserializeXML.y
MACH_PORT_NULL != remotePriv->objectRef
OSObjectLogInternal
%s%qd\n
overrideChannelState() cannot be used after setChannelState()!\n
!lvars->mappings
notsync || !remote || (msgid == IOService_Start_ID) || queue->OnQueue()
%u
OnQueue SDK version 0x%x\n
idx < source->ivars->maxIndex
IORecursiveConditionLockLock
B32@?0Q8Q16Q24
~IOReporter_IVars
%sbacktrace:\n
rwlock
convert_mach_time_to_nsec
msgid == action->ivars->msgid
%s-Default
Server
finalizeBuffer
length <= kOSSerializeDataMask
ivar(nChannels)
_absolutetime_to_nanoseconds
<internal error>
loadEntry
buildBoolean
OSUnserializeXML: can't alloc temp memory
replySize <= rpc.replySize
0 == err
ret == KERN_SUCCESS
[0{OSMetaClassBaseRemotePrivate=^{IOUserServer_IVars}{?=^{OSMetaClassBaseRemotePrivate}^^{OSMetaClassBaseRemotePrivate}}QIII^Q^Q}]
data
OSScanClassesInMachO(%s)\n
BOOLEAN
buildSet
(desc->methodOptionsOffset + desc->methodOptionsSize) <= descSize
IONameMatch
gatedReturnCommand
remoteMethods
open(kIOKitUserServerClientType) %s (0x%x)\n
msg
serial != nullptr
Failed to find class: %s
OSDictionarySetValueInternal
IORPCMessageFromMach
returnCommand_block_invoke
allocLen >= length
IOStateReporter::handleAddChannelSwap ivar(lastUpdateTimes) unset despite non-NULL ivar(currentStates)
virtual IOReturn IOStateReporter_IVars::handleSetStateID(uint64_t, int, uint64_t)
I
Found class: %s\n
uniq->string == this
OSSerializationAddBinaryObject
ckey || searchkey
IOReportChannelConfig
objectRef
set
MACH_PORT_NULL != objectName1
%s:%d: failed assertion `%s'\n
release_ret == KERN_SUCCESS
IOReportGroupName
SHA512_Init
OSObjectAllocate 0x%qx %s remote %d, flags %#x, qc %d, mc %d\n
len <= kOSSerializeDataMask
IOReportSubGroupName
unexpected end of buffer
string
OSCopyOutObjects
100 == count
mach_msg: 
IOTimerDispatchSourceQueue-%s-%p
ivars
Wait
OSCollectionTypeName
handleCreateLegend
%s: inconsistent size for SHA384 context
kern.backtrace.user
_nanoseconds_to_absolutetime
str != NULL
virtual IOReturn IOStateReporter_IVars::handleSwapPrepare(int)
ret == kIOReturnSuccess
ivars->waiter == token
server->serviceCount
Registered: %s\n
/Info.plist
allocLen >= bufferLen
retain
lvars->queue
LockTest
bundlePath != NULL
OSUnserializeBinary
OSStringCreate(\"%s\", %ld should be %ld)\n
Boot args: %s\n
IOUserClass
WakeupWithOptions
freeBuffer
handleSwapPrepare
array
OSObjectFree
SetEventlinkPort_Impl
uiomachchannel
content:
^Q
QueueForObject
size != 0
OSCreateObjectFromSerializationInternal
IOReporter::_swap* already in use
IOReportChannels
format
SleepWithDeadline
OSScanClassesInMachO
\n
(kOSSerializeArray == (kOSSerializeTypeMask & key)) || (kOSSerializeSet == (kOSSerializeTypeMask & key))
virtual IOReturn IOReporter_IVars::copyElementValues(int, IOReportElementValues *)
refs <= maxObjectCount
IOReturn IOStateReporter_IVars::_getStateIndices(uint64_t, uint64_t, int *, int *)
%s - %s <= 0!\n
Register class: %s (super %s) object %p ref %qd\n
serverTagStrEnd[0] == '\\0'
size >= queueCount * sizeof(machReply->objects[0])
%s: class not found\n
OSCollectionEntryDictionaryCount
%s - %s > INT_MAX / sizeof(%s)!
Failed to mmap file %s, size %lld at %p in mapped region %p->%p: %s\n
buildArray
uioserver.cpp
reply->__hdr.msgid == OSObject_Instantiate_ID
remoteQueues
Create_Impl
oldcount < INT16_MAX
0 == lvars->reentrantLock->thread
OSSerializationValue
buildString
(desc->queueNamesOffset + desc->queueNamesSize) <= descSize
ThreadStart
OSSerializationGetStringLength
%s: inconsistent size for AES encrypt context\n
BAD REPLY SIZE 0x%x\n
%s: %s\n
failed to copy in object: 0x%x
OSRegisterClass
IORWLockAlloc
[%#qx] INVOKE MSG:
OSDataAppendBytes
dk
false
i24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^Q16
!loadEntry
reset
q1->OnQueue()
CopyNextNotification ret 0x%x\n
service == nullptr
S
free %s %p 0x%qx %d\n
GetReference
/* %04lx: */ %-96s /* |%-16s| */\n
true
IOService::Stop_async\n
no services, exiting\n
__DATA_CONST
IOThreadStart
SET
oldcount > 0
%s<NULL>\n
Kernel requested exit (%s)\n
Cancel_Impl
%s\"%s\"\n
OSMetaClassBaseRemotePrivate
buildDictionary
duplicate dictionary key
IOLockAssert
Root
CreatePropertyMatchingDictionary
Map
remotePrivate
size
Failed to fstat %s: %s\n
getHexData
IOService::finalize\n
gatedGetCommand
OSCollectionEntryDictionaryApply
IOReportLegend
0 == deadline
(count + idx) <= serial->ivars->maxIndex
IOInterruptDispatchSourceThread
B16@?0^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSString_IVars}^{OSString_LocalIVars})}8
B40@?0Q8^{OSSerialization=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})(?=^{OSSerialization_IVars}^{OSSerialization_LocalIVars})}16(OSCollectionEntry=^{OSObject}Q)24(OSCo
[%#qx] %p %#qx flags %#qx object %#qx \n
Open file: %s\n
OSStringCreate
IORWLockUnlock
Failed to open %s: %s\n
[%#qx] SERVER REPLY:
0 == lvars->reentrantLock->count
%s was called out of locked context!
_NO_NAME_4
Default
self != NULL
virtual IOReturn IOStateReporter_IVars::handleSetStateByIndices(int, int, uint64_t, uint64_t)
value.object
NULL == ivars->waiter
OSCopyInObjects_block_invoke_2
swapNChannels
!upgrade
v24@?0r^v8Q16
swapNElements
virtual IOReturn IOReporter_IVars::setElementValues(int, IOReportElementValues *, uint64_t)
OSUnserializeXML: %s near line %d\n
IOUserServerMain_block_invoke_3
OSSerializationAppendBytes
%s%s\n
IOHistogramSegmentConfig
InvokeRemote
init
rlock
B24@?0Q8Q16
oldsize == buflen
meta
MACH_PORT_DEAD != remotePriv->objectRef
q2
lvars->reentrantLock
class %s duplicate\n
IORWLockRead
DispatchConcurrent_f
OSRegisterClasses
createTimerDispatchSource
OSStringHash
OSAction__IOBlockStorageDevice_KernelCompletion
%s(0x%lx):\n
serialOut
__osclassinfo
(replyTo == 0) == (0 != (kIORPCMessageOneway & message->flags))
OSCollectionEntryTypeID
IODataQueueDispatchSourceShared.h
clock_get_calendar_microtime
OSCollectionEntryArrayCount
%s: segment size overflow
objectRefsListEntry.le_prev
v8@?0
IORWLockWrite
virtual const IOReportElementValues *IOReporter_IVars::getElementValues(int)
clock_get_calendar_nanotime
serial->ivars->bufLen == 0 || serial->ivars->buffer != nullptr
%s: inconsistent size for SHA256 context
SHA256_Init
objectRefsListEntry.le_next
???
lock
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
refcount
DeliverNotifications_block_invoke
IOService::SetPowerState(%s, %d) ack kernel\n
%s[%d]:\n
OSSerializationArrayApply
remotePriv
~IOHistogramReporter_IVars
%s: kIOUserServerMethodStart failed, exiting\n
lvars->recvport == hdr->msgh_local_port
[%#qx] SERVER MSG:
%s: inconsistent size for AES decrypt context\n
buildNumber
(null)
!parent
IOUserServerMain
idx < maxIndex
%s doesn't support shrinking
-
release
pthread_self() == lock->thread
IOTimerDispatchSource: *** DRIVERKIT CLIENT BUG ***: double timer cancellation
Invoke from %s 0x%qx, q %s refs %llx rpcKernel %d %s\n
q2->OnQueue()
OSMetaClassBasePrivate
forward reference detected
kern.bootargs
%s queue: %s\n
CopyCurrentThread
buffer
idx < size
NUMBER
OSSerializationDictionaryApply
virtual void IOReporter_IVars::handleSwapCleanup(int)
aes_encrypt_key
{CompactArray<IODispatchQueue *>=(?=^^{IODispatchQueue}^{IODispatchQueue})I}
IOLib.cpp
clock_get_system_nanotime
OSMetaClassBase::InvokeRemote(0x%x) 0x%qx 0x%qx %p %p\n
GetLength
%sfalse\n
roundSerializationSize
virtual IOReturn IOReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
int64_t
Bad msg:
lvars->waitTokens
Using guard pages: requested guard size is %zu, rounding up to %zu\n
KERN_SUCCESS == ret
WakeAtTime_Impl
OSMetaClassAllocate
SHA384_Init
lock->count
err == 0
OSDictionaryApply_block_invoke
maximum object reference count
dict
Dispatch
kr == kIOReturnSuccess
IOService::SetDispatchQueue(%s, %s)\n
STRING
Failed to cast object of type %s to %s
queue
local
Failed to mmap region of size %zu: %s\n
%s was called out of config locked context!
nanosecs
ARRAY
count && tags
IOService::Stop kernel done 0x%x\n
KERN_SUCCESS == kr
ivar(segmentCount)
virtual void IOStateReporter_IVars::handleSwapCleanup(int)
is canceled action\n
BAD REPLY ID 0x%x\n
0x%02x, 
Create
Cancel
q1
OSMetaClassBase
oneway || (replySize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage)))
self == OSDynamicCast(IOThread, self)
DICT
OSDataCreate
buildData
OSObjectPortFinalize
OSCollectionEntryArrayApply
virtual IOReturn IOStateReporter_IVars::handleAddChannelSwap(uint64_t, const OSString *)
Q
sendSize >= (sizeof(IORPCMessageMach) + sizeof(IORPCMessage))
operator[]
IORecursiveConditionLockUnlock
serial
_OSObjectCopyIn
IODispatchQueue::Create(Default) %p\n
%s[%d] key:\"%s\"\n
IOPropertyMatch
length
IOReportChannelInfo
plist
kIOReturnSuccess == kr
%s %d queues\n
OSCopyInObjects
^^{OSMetaClassBaseRemotePrivate}
OSObjectTryRetain
%{public}s
%s
```
