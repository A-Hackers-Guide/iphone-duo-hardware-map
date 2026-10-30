# `/System/Library/Frameworks/IOSurface.framework/IOSurface`

From the upgrade restore ramdisk (141-29011-104.dmg). 380,048 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 4176)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/Frameworks/IOSurface.framework/IOSurface (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (13 classes, 4 protocols)

Classes: `IOSurface`, `IOSurfaceDebugDescription`, `IOSurfaceMemoryPool`, `IOSurfaceRemotePerSurfaceGlobalState`, `IOSurfaceRemotePerSurfacePerClientState`, `IOSurfaceRemoteRemoteClient`, `IOSurfaceRemoteServer`, `IOSurfaceSharedEvent`, `IOSurfaceSharedEventListener`, `IOSurfaceTransaction`, `IOSurfaceTransactionListImpl`, `IOSurfaceWiringAssertion`, `_IOSurfaceDebugDescription`

Protocols: `IOSurfaceTransactionList`, `NSCoding`, `NSObject`, `NSSecureCoding`

## Strings (797)

```
_cfTypeID
surfaceDescriptions
flush:
getBytes:length:
setListener:
_event
_layoutInfo
initWithSerializedData:numWritten:actualLength:selectedLength:
_mtx
initWithSurface:mappedAddress:mappedSize:extraData:
isSysMemOnly
kernelFullListLength
setDisconnectedHandler:
isWrite
componentsJoinedByString:
elementHeightOfPlaneAtIndex:
TQ,R,V_kernelFullListLength
_handleClientConnection:
globalStateForSurface:mappedAddress:mappedSize:extraData:
height
length
setGlobalState:
TI,R,V_eventPort
T#,R
T@\"NSString\",?,R,C
T@\"NSMutableDictionary\",&,N,V_surfaceStates
_poolPort
addObject:
registryID
.cxx_construct
_pid
isInUseForAnyOtherCategory:
name
performSelector:withObject:
signaledValue
.cxx_destruct
bytesPerElement
_mach_port
allowsPixelSizeCasting
formattedDescription:
notifyListener:atValue:block:
protectionOptions
shutdown
substringFromIndex:
unlockWithOptions:seed:
TI,R,D
_listener
_refcount
debugRefCount
setSurfaceStates:
copyDebugInfo
decrementUseCount
setObject:forKeyedSubscript:
addClientReferenceToSurfaceWithExtraData:
T@\"NSString\",R,C
release
supportsRollback
bytes
conformsToProtocol:
setValue:forKey:
T@\"IOSurfaceRemotePerSurfaceGlobalState\",&,N,V_globalState
TQ,R,V_selectedLength
_globalTraceObjectID
_mapped_size
isMemberOfClass:
numberWithUnsignedLong:
waitUntilSignaledValue:timeoutMS:
T^{__IOSurfaceClient=},R,N
_waitValue
allAttachments
encodeWithCoder:
initWithOptions:
residentSize
setAllAttachments:
isInUse
inUse
setDisconnectedQueue:
TQ,R
_queue
initWithIOSurfaceClient:
surfaceID
bytesPerRowOfPlaneAtIndex:
globalState
seed
stringWithCString:encoding:
stringWithUTF8String:
attachmentForKey:
raise:format:
_isWrite
_remoteConnection
ensureMemory:
numberWithUnsignedInt:
supportsProtectionOptions:
timestampAtIndex:
_lock
_surfaceStates
initWithBytes:length:
globalTraceObjectID
isEqual:
setTimestamp:atIndex:
TI,R,N
_disconnectedQueue
_eventOptions
remoteConnection
virtualAddress
baseAddressOfPlaneAtIndex:
traceID
UTF8String
_selectedLength
T@\"NSString\",R
_globalState
_kernelFullListLength
hash
clients
newChildSurfaceWithProperties:
waitValue
removeAllObjects
removeClientReferenceToSurface
_getClient:inboundExtradata:outboundExtraData:
TQ,R,V_waitValue
T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnectedQueue
T@\"NSObject<OS_xpc_object>\",&,N,V_listener
_csid
elementWidthOfPlaneAtIndex:
_surface
autorelease
initWithProperties:
setQueue:
_length
_addSurface:mappedAddress:mappedSize:extraData:
bytesPerElementOfPlaneAtIndex:
incrementUseCount
Ti,R
_handleError:
disconnectedHandler
elementHeight
isMemoryRegionUsed
unsignedIntegerValue
_impl
_txnCache
currentHandler
objectForKey:
_basicInfo
copy
dirtySize
initWithSurfaceID:
defaultManager
stringWithFormat:
_handleClientDisconnected:
debugDescription
isDisplayable
retain
setPid:
T^v,R
isInUseForCategory:
T@?,C,N,V_disconnectedHandler
_eventPort
intValue
lastPathComponent
numberWithUnsignedLongLong:
removeObjectForKey:
unsignedLongLongValue
initWithCoder:
localUseCount
performSelector:
selectedLength
self
TB,R,V_isWrite
description
initWithDispatchQueue:
stringByPaddingToLength:withString:startingAtIndex:
TB,R
_notificationPort
surfaceStates
widthOfPlaneAtIndex:
TI,R
_signaledValue
removeAllAttachments
setObject:forKey:
setPurgeable:oldState:
stringWithFileSystemRepresentation:length:
T@\"NSMutableArray\",&,N,V_clients
TQ,R,D
_clients
incrementUseCountForCategory:
lockWithOptions:seed:
rangeOfString:
removeObject:
transactionAtIndex:
width
zone
fromSerialized:
T@\"NSObject<OS_xpc_object>\",&,N,V_remoteConnection
_notifyEventPort:event:atValue:block:
baseAddress
initWithIOSurface:
T@\"IOSurfaceSharedEvent\",R,V_event
_name
initWithBasicInfo:layoutInfo:name:
newWiringAssertion
surface
cStringUsingEncoding:
encodeXPCObject:forKey:
initWithMachPort:
respondsToSelector:
_handleMessage:
initWithListener:options:
Ti,N,V_pid
arrayWithObjects:count:
count
initWithSurfaceID:mappedAddress:mappedSize:extraData:
initWithRemoteConnection:disconnectedQueue:disconnectedHandler:
pid
_dispatchQueue
numberOfUseCountCategories
objectAtIndex:
supportsSecureCoding
_serializedData
countByEnumeratingWithState:objects:count:
decodeXPCObjectOfType:forKey:
performSelector:withObject:withObject:
pixelFormat
removeAttachmentForKey:
_poolId
Tq,R
decrementUseCountForCategory:
isKindOfClass:
_extraData
elementWidth
event
eventPort
initWithClientBuffer:
poolId
setAttachment:forKey:
_removeSurface:
TB,R,GisInUse
superclass
_mapped_address
mergeExtraData:
dealloc
TQ
allocationSize
class
heightOfPlaneAtIndex:
initWithSharedEvent:waitValue:isWrite:
TQ,R,V_globalTraceObjectID
numberWithInt:
pixelFormatString
retainCount
setRemoteConnection:
setSignaledValue:
objectForKeyedSubscript:
addEntriesFromDictionary:
TB,R,D
TQ,R,V_length
_disconnectedHandler
bytesPerRow
handleFailureInFunction:file:lineNumber:description:
isWired
disconnectedQueue
init
listener
planeCount
T@\"NSString\",R,D
setClients:
strongToWeakObjectsMapTable
eventPortAtIndex:
queue
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
isProxy
{shared_ptr<IOSurfaceTransactionSerialized[]>=\"__ptr_\"^{?}\"__cntrl_\"^{__shared_weak_count}}
v16@0:8
Vv16@0:8
B24@0:8@\"Protocol\"16
v20@0:8I16
{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}
@\"IOSurfaceSharedEvent\"
B
@\"IOSurfaceTransaction\"24@0:8Q16
@48@0:8^{__IOSurfaceClient=}16^v24Q32@40
@44@0:8I16^v20Q28@36
i24@0:8@16
q16@0:8
^v24@0:8Q16
v44@0:8I16@20Q28@?36
@24@0:8^{__IOSurfaceClient=}16
@\"NSMutableArray\"
@40@0:8@16@24@?32
{?=\"clientAddress\"Q\"surfaceID\"I\"pixelFormat\"I\"retainCount\"I\"yCbCrMatrix\"I\"cacheMode\"I\"mapCacheAttribute\"I\"purgeableState\"I\"purgeableStateAPI\"I\"allocOffset\"Q\"allocSize\"Q\"isGlobal\"C\"isAllocated\"C\"isWired\"C\"pad\"C\
{?=\"offset\"Q\"width\"Q\"height\"Q\"bytesPerRow\"Q\"bytesPerElement\"I\"elementWidth\"I\"elementHeight\"I}
@16@0:8
@32@0:8:16@24
@24@0:8Q16
^v16@0:8
B20@0:8I16
Q16@0:8
Q
v48@0:8^{__IOSurfaceClient=}16^v24Q32@40
@24@0:8:16
B24@0:8:16
@24@0:8@16
B32@0:8Q16Q24
^{__IOSurfaceClient=}16@0:8
v24@0:8@?16
#16@0:8
@\"NSObject<OS_xpc_object>\"
@40@0:8r^{?=QIIIIIIIIQQCCCCIQQQQQQQ}16r^{?=QQQQIII}24@32
{unordered_map<unsigned long, IOSurfaceTransaction *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned 
B24@0:8@16
v32@0:8Q16Q24
^v
B24@0:8Q16
Q24@0:8Q16
^{IONotificationPort=}
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
^{__IOSurfaceClient=}36@0:8I16@20^@28
v20@0:8i16
@?
r^Q
@\"NSObject<OS_dispatch_queue>\"
I16@0:8
@36@0:8@16Q24B32
B16@0:8
@\"NSString\"16@0:8
@56@0:8{shared_ptr<IOSurfaceTransactionSerialized[]>=^{?}^{__shared_weak_count}}16Q32Q40Q48
v24@0:8@16
q24@0:8Q16
I
@24@0:8r^v16
@40@0:8:16@24@32
^{_NSZone=}16@0:8
@20@0:8I16
v24@0:8Q16
v40@0:8@16Q24@?32
@?16@0:8
I24@0:8Q16
v24@0:8@\"NSCoder\"16
v32@0:8@16@24
^{__IOSurfaceClient=}
@\"NSString\"
@24@0:8@\"NSCoder\"16
i16@0:8
i
@\"NSMutableDictionary\"
B24@0:8#16
i28@0:8I16^I20
@32@0:8@16@24
@\"IOSurfaceRemotePerSurfaceGlobalState\"
IOSurfaceAppendTransaction got null buffer
%s
IOSurfaceQueryTransactionList failed to allocate memory
IOSurfaceClientInvalidate failed: %08x
IOSurface Deserialization failure for key %{public}s: %@
IOSurface.framework API explicitly disallowed.
IOSurface creation failed: %08x parentID: %08x properties: %@%s
IOSurface client memory mapping is %lu bytes but client claims allocation size of %lu bytes
[IOSurfaceTransactionListImpl transactionAtIndex] failed to create transaction at index %zu
IOSurfaceAppendTransaction got non-success return from kernel
IOSurfaceDisallowForever() invoked too late, connection to IOSurface.kext already established
Client is providing a shmem for its own mapping, pid %d
[IOSurfaceTransactionListImpl eventPortAtIndex] invalid index %zu
IOSurfaceAppendTransaction got null transaction
IOSurface creation failed. IOSurface service not present
Received client method %lu (%s) from client %d
Failed to map client shared memory object from pid %d
[IOSurfaceTransactionListImpl transactionAtIndex] invalid index %zu
IOSurfaceQueryTransactionList got non-success return from kernel
IOSurfacePruneTransactionList got null buffer
IOSurface creation failed: %08x parentID: %08x property: %@
IOSurface.framework versus IOSurface.kext version mismatch
Client disconnected pid=%d
Surface %d created by client pid=%d
IOSurfaceQueryTransactionList got null buffer
IOSurface.framework not allowed to iterate kernel services (%08x).  API disallowed.
Client connected pid=%d
[IOSurfaceTransaction fromSerialized] got nil event from serialized data
IOSurface creation failed. IOSurface open failed: %08x %s
Surface %d released by client pid=%d
Received unknown client method %lu from client %d
iosCacheSet
FixUpscaling
IOSurfaceSubsampling
TransferFunction#
IOSurfacePlaneBytesPerCompressedTileHeader
BorderFillHeight
IOSurfaceAcceleratorGetServiceObject
IOSurfaceAcceleratorTransferSurface
IOSurfaceRemoteMethodClientCreateMachPort
IOSurfaceRemoteMethodClientSignalEvent
IOSurfaceElementHeight
IOSurfaceAddressOffset
DCI_P3
key
Buffer
dict
IOSurfaceName
SMPTE_240M_1995
IOSurfaceRemoteMethodClientCopyDataValueBytes
IOSurfaceRemoteMethodClientGetBulkAttachments
SetExtraData
GetExtraData
EBU_3213
RectangleHeight
IOSurfaceAddressFormat
IOSurfaceSliceCount
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
IOSurfaceRemoteMethodClientBindAccel
height = 
IOSurfaceDecoderTimes
_iosConnectInitalize() unable to open IOSurface kernel service: %08x\n%d existing clients:\n%s\n
_iosConnectInitalize
IOSurfaceAcceleratorTransferSurfaceWithSwap
BufferSize
%@%@
IEC_sRGB
IOSurfacePrefetchPages
IOSurfaceClientGetValue getValueMethod kernel call failed %08x\n
i
IOSurfaceRemoteRemoteClient { remote_pid=%d }
IOSurfaceAllocSize
0x%08x
TemporalBottomFirst
IOSurfacePlaneHorizontalPixelOffsetWithinCompressedTileArray
 (likely sandbox violation)
/Library/Caches/com.apple.xbs/329888F6-71E8-4CF7-B533-B96C049D3738/TemporaryDirectory.BvI3iR/Sources/IOSurface/IOSurfaceUser/IOSurfaceClient.m
IOSurfaceRemoteMethodClientRemoveAllValues
<IOSurfaceNotifier %p refcnt=%d notificationPort=%p callback=%p, refcon=%p>
name = 
IOSurfaceBufferTileMode
IOFenceAllowTearing
IOSurfaceMemoryPoolSize
SkipAsyncCallback
Failed to unserialize data from kernel: %@
Method
OldState
IOSurfaceOffset
IOSurfacePlaneWidth
IOSurfacePlaneElementWidth
IOUserClientCreator
Options
EventPort
ChromaSubsampling
ProtocolVersion
IOSurfacePlaneComponentBitOffsets
IOSurfaceTransferFunction
Minimum
MasteringDisplayColorVolume
IOSurfaceIsPrivate
IOSurfacePlaneExtendedPixelsOnTop
%@%d
Category
DolbyVisionRPUData
IOSurfaceAcceleratorAbortCaptures
IOSurfaceRemoteMethodGetDebugInfo
ChromaLocationBottomField
ClientProvidedShmem
IOSurfaceAddressRanges
ITU_R_2100_ICtCp
IOSurfacePixelAspectRatio
IOSurfaceDisplayDitherCbThresholds
IOSurfaceDecrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
com.apple.iosurface.unrecognized-code-points
BUG: Missing state?!?
EventOperation
ReferenceRasterHeight
IOSurfaceUseReserve
IOSurfacePlaneHTPCPredictionSelector
_iosConnectInitalize() unable to locate IOSurface kernel service
IOSurfaceClientCopyValue getValueMethod kernel call failed %08x\n
BorderFillX
HistogramPixelBins
FieldDetail
IOSurfaceDefaultAttachments
HistogramHeight
Layout
PropertiesDictionary
MachPort
PixelAspectRatio
IOSurfacePlaneBytesPerRowOfTileData
HistogramBinMode
ColorRemapMode
1
Kernel Surfaces
ErrorCode
DebugSurfaceIDList
ExtraData
IOSurfacePlaneHeight
Average
category out of range
IOSurfaceAcceleratorGetTypeID
v8@?0
IOSurfaceRemoteMethodClientGetPlaneState
com.apple.IOSurface.Remote
IOSurfaceRemoteProtocol.m
IOSurfacePlaneInfo
This object may only be encoded by an NSXPCCoder.
DV 4:2:0
NearestFilter
IOSurfaceAcceleratorGetID
Failed to unserialize data from kernel.
IOSurfaceDisplayDitherThresholds
IOSurfaceHostOnly
IOSurfaceNotifier
object
IOSurfaceHeight
SMPTE_ST_2084_PQ
IOSurfaceMemoryPoolEntitlement
IOSurfacePlaneCompressedTileHeight
IOSurfacePlaneExtendedPixelsOnBottom
GetYCbCrMatrix
SpatialFirstLineEarly
IOSurfacePlaneCompressionFootprint
OptOutBlitClip
BorderFillAlpha
IOSurfaceRemoteMethodClientIncrementUseCountForCategory
IOSurfacePlaneSize
4:1:1
TransferFunction
PremultipliedAlpha
IOSurfaceBufferTileFormat
IOSurfaceProhibitUseCount
FieldCount
\n
IOSurfacePlaneCompressedTileWidth
BorderFillRedY
%@: surface is not planar
IOSurfacePixelFormat
BottomLeft
ReferenceRasterWidth
IOSurfaceRemoteMethodClientCreate
PlaneIndex
IOSurfaceDisplayDitherCrThresholds
IOSurfaceScalerTimes
BorderFillBlueCr
HistogramWidth
IOSurfaceRemoteMethodClientIsInUseForAnyOtherCategory
AcceleratorID
SMPTE_ST_428_1
HorizontalSpacing
IOSurfacePlaneVerticalPixelOffsetWithinCompressedTileArray
CleanAperture
TemporalTopFirst
RectangleLeft
IOSurfaceMemoryPoolCacheModeSwitchEnabled
IOSurfacePlaneCompressionType
IOSurfacePlaneHTPCVerticalHeaderGroupingMode
result == kIOReturnSuccess
block
IOSurfaceRemoteMethodInitialize
Height
sRGB
IOSurfaceRemoteMethodClientDecrementUseCountForCategory
MemoryObject
Limits
4:2:0
IOSurfacePlaneBase
IOSurfacePlaneBytesPerElement
IOSurfacePixelSizeCastingAllowed
%@: plane index (%ld) out of bounds (%ld)
IOSurfaceDirection
IOSurfaceChromaLocationTopField
TopLeft
IOCoreSurfaceRoot
This object may only be decoded by an NSXPCCoder.
IOSurfaceTimingInfo
Transform
HistogramOffsetX
ZeroFill
IOSurfaceAcceleratorConfigurePerformanceStats
IOSurfaceSharedEvent.m
IOSurfaceIsGlobal
IOSurfacePlaneHeaderRegionBytesPerSlice
SidebandVideoPropertiesLookupID
, 
kIOSurfaceTrapRemoveBulkAttachments failed: %08x\n
IOSurfaceAcceleratorBlitSurfaceWithSwap
BUG: refcount is already zero
DebugSurfaceRefCount
UseGamma
IOSurfacePlaneWidthInCompressedTiles
IOSurfaceAcceleratorAbortTransfers
IOSurfaceRemoteMethodClientRelease
IOSurfaceRemoteMethodClientDecrementUseCount
sid: %08x traceID: %016llx virt: %016llx fmt: %s dims: %5d x %5d size: %7s name: %@
PlaneState
TransferFunctionIndex
width = 
IOSurfaceContentHeadroom
ColorPrimaries#
IOSurfacePlaneHeightInCompressedTiles
IOSurfaceMemoryPoolInfo
IOSurfaceGPUGlobalRO
_iosaLookupStubs
void _ioSurfaceSerializeToXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull, CFTypeRef _Nonnull)
IOSurface.port
IOSurfaceFieldCount
pid
ContentLightLevelInfo
IOSurfaceIncrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
kIOSurfaceMethodDecrementUseCountForCategory failed: %08x\n
IOSurfaceAcceleratorSetFilterCoefficients
IOSurfaceEventNotification
SurfaceID
Bottom
IOSurfacePreallocPages
CreationProperties
IOService
v16@?0@\"IOSurfaceRemoteRemoteClient\"8
SurfaceState
EventValue
<not set>
HDRImageStatisticsInfoRaw
SceneIllumination
RectangleWidth
IOSurfaceSysMemOnly
ForceMaxSpeed
BorderFillY
IOSurfaceRemoteServer.m
IOSurfaceICCProfile
IOSurfaceAcceleratorTransformSurface
IOSurfaceAcceleratorSetCustomFilter
-[IOSurfaceRemoteRemoteClient _getClient:inboundExtradata:outboundExtraData:]
IOSurfaceRemoteMethodClientUnlock
DebugLogBlock
AcceleratorField
IOSurfaceWidth
IOSurfacePlaneComponentRanges
IOSurfaceColorSpaceID
aYCC
HorizontalOffset
IOSurfaceChromaSubsampling
DitherControl
!
IPT
Left
IOSurfaceGPUTimes
IsDisplayable
IOSurfaceIsInUse: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceRemoteMethodClientNeedsBindAccel
IOSurfaceRemoteMethodClientIsInUseForCategory
value
IOSurfacePlaneOffset
IOSurfaceProtectionOptions
Identity
_iosCacheDict
IOSurfaceAcceleratorCreate
NewState
IOSurfaceClass
HDRImageStatisticsInfoFiltered
IOSurfaceSuperbuffer
IOSurfaceMemoryPoolZerofillEnabled
IOSurfaceAcceleratorBlitSurface
%s, Line=%d, Error=%s\n
GammaLevel
Maximum
kIOSurfaceMethodRemoveValue failed: %08x\n
iokit-float
kIOSurfaceMethodIncrementUseCountForCategory failed: %08x\n
IOSurfaceCacheMode
IOSurfaceYCbCrMatrix
IOSurfacePlaneExtendedPixelsOnRight
IOSurfaceBytesPerElement
ITU_R_709_2
Width
IOSurfaceFieldDetail
Top
v16@?0@\"NSObject<OS_xpc_object>\"8
IOSurfaceGammaLevel
VerticalSpacing
AlphaChannelMode
StraightAlpha
IOSurfaceAllocateFromSuperbuffer
IOSurfacePlaneCompressedTileDataRegionOffset
/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
-[IOSurfaceRemotePerSurfacePerClientState removeClientReferenceToSurface]
Center
IOSurfacePlaneComponentBitDepths
IOSurfacePlaneComponentTypes
pixelFormat = 
ITU_R_2100_HLG
VerticalOffset
IOSurfaceClient.m
HistogramMaxPixelValue
IOSurfacePlaneBytesPerRow
YCbCrMatrix#
%s\n
IOSurfaceAcceleratorCaptureSurface
com.apple.IOSurfaceRemoteServer
CFTypeRef  _Nullable _ioSurfaceDeserializedFromXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull)
JEDEC_P22
IOSurfaceEnableStatistics
BorderFillGreenCb
IOSurfaceRemoteMethodClientRemoveValue
IOSurfaceRemoteMethodClientIncrementUseCount
IOSurfaceRemoteMethodClientGetYCbCrMatrix
User Clients
BasicInfo
IOSurfacePlaneBitsPerElement
IOSurfacePlaneComponentNames
 
IOSurfaceMemoryRegion
IOSurfaceCleanAperture
AlphaChannelIsOpaque
IOSurfacePurgeWhenNotInUse
IOSurfaceResetDefaultAttachmentsWhenNotInUse
IOSurfacePlaneElementHeight
IOSurfaceNonPurgeable
IOSurfacePlaneCompressedTileHeaderRegionOffset
IOSurfacePlaneExtendedPixelsOnLeft
MetalSharedTexture
IOSurfaceRemoteMethodClientLock
IOSurfaceRemoteMethodClientCopyAllValues
IOSurfaceType
4:2:2
CustomFilter
LockInScaler
IOSurfaceClientSetSurfaceNotify failed %08x\n
IsInUse
NeedsBindAccelerator
IOSurfaceBytesPerRow
IOSurfaceColorPrimaries
IOSurfaceChromaLocationBottomField
RectangleTop
HorizontalDisparityAdjustment
IOSurfaceEncoderTimes
kIOSurfaceTouchEventTimes
AGXUseNearestChromaFiltering
%4d
ITU_R_601_4
P3_D65
IOSurfaceMapCacheAttribute
IOSurfacePlaneBytesPerTileData
 (likely per client IOSurface limit of 16384 reached)
_iosConnectInitalize() unable to open IOSurface kernel service: %08x
HistogramOffsetY
ITU_R_2020
IOSurfaceDisplayTimes
IOSurfaceSharedEventAddEventListener
IOSurfaceRemoteMethodClientSetBulkAttachments
ChromaLocationTopField
IOSurfaceDisplayDitherYThresholds
AlphaOverride
IOSurfaceAcceleratorGetStatistics
IOSurfaceDefaultBulkAttachments
IOSurfaceRemoteMethodClientSetValue
PropertyKey
Invalid parameter not satisfying: %@
IOSurfaceAddress
SMPTE_C
Linear
IOSurfacePlaneBytesPerRowOfCompressedTileHeaderGroups
wakePort
_ioSurfaceEventNotificationCallback2
IOSurfaceRemoteMethodClientSetPurgeable
DebugLogQueue
SpatialFirstLineLate
IOSurfaceAcceleratorConditionalTransferSurfaceWithSwap
IOSurfaceSharedEventAddEventListener failed: %08x\n
YCbCrMatrixIndex
EDRFactor
IOSurfaceColorSpace
id = 
kIOSurfaceTrapRemoveCoreVideoBridgedValues failed: %08x\n
BorderFillWidth
Internal error during notification request %08x
IOSurfaceRemoteMethodClientIsInUse
Client Surfaces
ColorPrimariesIndex
kIOSurfaceMethodSetCoreVideoBridgedKeys failed: %08x\n
IOSurfaceIsInUseForCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceIsInUseForAnyOtherCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceAcceleratorGetRunLoopSource
isSetValues
LookupID
IOSurfaceElementWidth
VersatileSenselArrayPattern
DisplayMaskRectangle
IOSurfaceEDRFactor
IOSurfacePlaneDataRegionBytesPerSlice
IOSurfaceGetUseCount: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceRemotePerSurfaceGlobalState
IOSurfaceMemoryPool
_IOSurfaceDebugDescription
IOSurfaceTransaction
IOSurfaceTransactionList
NSCoding
IOSurfaceSharedEventListener
IOSurfaceRemotePerSurfacePerClientState
IOSurfaceDebugDescription
IOSurfaceTransactionListImpl
NSSecureCoding
IOSurfaceWiringAssertion
IOSurface
IOSurfaceRemoteRemoteClient
NSObject
IOSurfaceSharedEvent
IOSurfaceRemoteServer
```
