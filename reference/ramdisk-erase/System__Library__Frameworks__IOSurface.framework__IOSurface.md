# `/System/Library/Frameworks/IOSurface.framework/IOSurface`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 380,048 bytes.

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
IOSurfaceAppendTransaction got non-success return from kernel
Client disconnected pid=%d
IOSurfaceQueryTransactionList got null buffer
IOSurface creation failed: %08x parentID: %08x property: %@
%s
IOSurface.framework versus IOSurface.kext version mismatch
Client connected pid=%d
IOSurface creation failed: %08x parentID: %08x properties: %@%s
IOSurfaceClientInvalidate failed: %08x
Received client method %lu (%s) from client %d
IOSurface client memory mapping is %lu bytes but client claims allocation size of %lu bytes
[IOSurfaceTransactionListImpl eventPortAtIndex] invalid index %zu
IOSurfaceAppendTransaction got null buffer
IOSurfaceAppendTransaction got null transaction
Surface %d created by client pid=%d
Failed to map client shared memory object from pid %d
IOSurfaceDisallowForever() invoked too late, connection to IOSurface.kext already established
IOSurface creation failed. IOSurface open failed: %08x %s
IOSurface creation failed. IOSurface service not present
Received unknown client method %lu from client %d
[IOSurfaceTransactionListImpl transactionAtIndex] failed to create transaction at index %zu
IOSurfacePruneTransactionList got null buffer
IOSurface Deserialization failure for key %{public}s: %@
[IOSurfaceTransactionListImpl transactionAtIndex] invalid index %zu
IOSurfaceQueryTransactionList failed to allocate memory
IOSurface.framework API explicitly disallowed.
Client is providing a shmem for its own mapping, pid %d
[IOSurfaceTransaction fromSerialized] got nil event from serialized data
IOSurfaceQueryTransactionList got non-success return from kernel
IOSurface.framework not allowed to iterate kernel services (%08x).  API disallowed.
Surface %d released by client pid=%d
IOSurfaceAddressOffset
4:2:0
IOSurfaceTimingInfo
/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
ExtraData
This object may only be decoded by an NSXPCCoder.
IOSurfacePlaneHTPCVerticalHeaderGroupingMode
Transform
BorderFillAlpha
BorderFillRedY
IOSurfaceAcceleratorAbortCaptures
-[IOSurfaceRemoteRemoteClient _getClient:inboundExtradata:outboundExtraData:]
IOSurfaceRemoteMethodClientSignalEvent
IOSurfaceColorSpaceID
IOSurfaceYCbCrMatrix
IOSurfaceTransferFunction
IOSurfacePlaneCompressedTileWidth
_ioSurfaceEventNotificationCallback2
IOSurfaceRemoteMethodClientDecrementUseCountForCategory
MemoryObject
Options
IOSurfaceName
IOSurfacePlaneBytesPerRowOfCompressedTileHeaderGroups
kIOSurfaceMethodIncrementUseCountForCategory failed: %08x\n
LockInScaler
IOSurfaceAcceleratorConditionalTransferSurfaceWithSwap
IOSurfaceRemoteMethodClientRemoveAllValues
EDRFactor
IOSurfaceBytesPerRow
IOSurfaceScalerTimes
IOSurfacePlaneHorizontalPixelOffsetWithinCompressedTileArray
sRGB
IOSurfaceRemoteMethodClientRelease
IOSurfaceRemoteMethodClientUnlock
SetExtraData
HistogramWidth
Internal error during notification request %08x
PlaneIndex
SMPTE_ST_428_1
IOSurfaceClientCopyValue getValueMethod kernel call failed %08x\n
IOSurfaceAcceleratorBlitSurfaceWithSwap
IOSurfaceRemoteProtocol.m
BorderFillWidth
IOSurfaceRemoteMethodClientIsInUse
Invalid parameter not satisfying: %@
%4d
IOSurfaceAddressRanges
ITU_R_709_2
DV 4:2:0
CreationProperties
%s\n
HistogramHeight
IOSurfaceAcceleratorGetServiceObject
IOSurfacePlaneWidth
YCbCrMatrix#
IEC_sRGB
IOSurfaceDecoderTimes
IOSurfaceMemoryPoolSize
/Library/Caches/com.apple.xbs/329888F6-71E8-4CF7-B533-B96C049D3738/TemporaryDirectory.BvI3iR/Sources/IOSurface/IOSurfaceUser/IOSurfaceClient.m
IOSurfaceRemoteMethodInitialize
DebugLogBlock
0x%08x
IOSurfaceChromaLocationBottomField
Average
AlphaChannelMode
kIOSurfaceTouchEventTimes
IOSurfacePlaneCompressedTileDataRegionOffset
IOSurfaceHostOnly
HistogramOffsetY
IOSurfacePlaneComponentBitOffsets
%@: surface is not planar
IOSurfaceSharedEvent.m
DebugLogQueue
CFTypeRef  _Nullable _ioSurfaceDeserializedFromXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull)
IOSurfacePlaneOffset
AlphaChannelIsOpaque
IOSurfaceDisplayDitherCrThresholds
_iosConnectInitalize() unable to open IOSurface kernel service: %08x\n%d existing clients:\n%s\n
HistogramMaxPixelValue
IOSurfaceAcceleratorAbortTransfers
IOSurfaceRemoteMethodClientCreate
Method
IOSurfaceWidth
VersatileSenselArrayPattern
IOSurfaceMemoryPoolEntitlement
, 
ZeroFill
IOSurfaceRemoteMethodClientSetPurgeable
IOSurfacePlaneComponentTypes
HDRImageStatisticsInfoFiltered
ReferenceRasterHeight
HorizontalDisparityAdjustment
IOSurfacePlaneWidthInCompressedTiles
IOSurfacePlaneDataRegionBytesPerSlice
IOSurfaceAcceleratorGetTypeID
IOSurfaceAcceleratorSetFilterCoefficients
IOSurfaceElementHeight
TransferFunction
NewState
EventValue
ChromaLocationTopField
id = 
Minimum
IOSurfaceMemoryPoolInfo
 (likely per client IOSurface limit of 16384 reached)
BorderFillHeight
User Clients
IOSurfaceClientSetSurfaceNotify failed %08x\n
Limits
IOSurfacePlaneBytesPerRow
IOSurfacePlaneBytesPerCompressedTileHeader
IOSurfaceDecrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
SkipAsyncCallback
IOSurfaceRemoteMethodClientIsInUseForAnyOtherCategory
NeedsBindAccelerator
<not set>
P3_D65
ITU_R_2100_HLG
TemporalTopFirst
TemporalBottomFirst
BorderFillGreenCb
v16@?0@\"NSObject<OS_xpc_object>\"8
!
IOSurfaceElementWidth
4:2:2
IOSurfaceResetDefaultAttachmentsWhenNotInUse
IOCoreSurfaceRoot
_iosCacheDict
IOSurfaceAcceleratorCreate
IOSurfaceRemoteMethodGetDebugInfo
IOSurfaceNotifier
This object may only be encoded by an NSXPCCoder.
%@: plane index (%ld) out of bounds (%ld)
Width
Height
Bottom
IOSurfacePlaneVerticalPixelOffsetWithinCompressedTileArray
IOSurfacePlaneExtendedPixelsOnRight
pid
IOSurfaceFieldCount
MasteringDisplayColorVolume
IOSurfacePlaneBytesPerTileData
IOSurfacePlaneExtendedPixelsOnBottom
CustomFilter
ColorRemapMode
IOSurfaceRemoteMethodClientRemoveValue
CleanAperture
IOSurfaceGammaLevel
IOSurfacePlaneHeaderRegionBytesPerSlice
FixUpscaling
com.apple.IOSurfaceRemoteServer
IOSurfaceRemoteMethodClientIsInUseForCategory
EventPort
FieldDetail
width = 
ITU_R_2100_ICtCp
Maximum
DisplayMaskRectangle
IOSurfaceDisplayTimes
IOSurfaceAcceleratorGetID
ProtocolVersion
object
IOSurfacePlaneComponentBitDepths
TransferFunction#
Center
ErrorCode
IOSurfacePixelSizeCastingAllowed
IOSurfaceSubsampling
IOSurfaceAddress
DolbyVisionRPUData
%s, Line=%d, Error=%s\n
value
TransferFunctionIndex
IOSurfacePlaneSize
IOSurfaceProtectionOptions
IOSurfaceDirection
HorizontalOffset
IOSurfaceDisplayDitherThresholds
IOFenceAllowTearing
IOSurfaceSharedEventAddEventListener failed: %08x\n
BUG: refcount is already zero
IOSurface.port
IOSurfaceColorPrimaries
VerticalSpacing
IOSurfaceNonPurgeable
IOSurfaceUseReserve
 (likely sandbox violation)
v16@?0@\"IOSurfaceRemoteRemoteClient\"8
IOSurfaceRemoteMethodClientLock
IOSurfaceClass
IOSurfaceChromaLocationTopField
IOSurfaceChromaSubsampling
IOSurfaceAllocateFromSuperbuffer
_iosConnectInitalize() unable to open IOSurface kernel service: %08x
_iosConnectInitalize() unable to locate IOSurface kernel service
IOSurfaceRemoteServer.m
Client Surfaces
IOSurfaceDefaultBulkAttachments
IOSurfaceRemoteMethodClientCopyAllValues
Kernel Surfaces
sid: %08x traceID: %016llx virt: %016llx fmt: %s dims: %5d x %5d size: %7s name: %@
com.apple.IOSurface.Remote
LookupID
EventOperation
GetExtraData
IOSurfacePlaneComponentNames
IOSurfaceDisplayDitherCbThresholds
IOSurfacePurgeWhenNotInUse
IOSurfaceAcceleratorGetStatistics
void _ioSurfaceSerializeToXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull, CFTypeRef _Nonnull)
name = 
IOSurfaceColorSpace
RectangleTop
BufferSize
OldState
GammaLevel
IOSurfaceSysMemOnly
IOSurfacePlaneCompressionFootprint
v8@?0
ChromaSubsampling
ClientProvidedShmem
IOSurfacePlaneBytesPerElement
UseGamma
IOSurfaceEventNotification
DebugSurfaceRefCount
IOSurfaceBytesPerElement
IOSurfacePlaneHeight
\n
SpatialFirstLineEarly
category out of range
kIOSurfaceMethodDecrementUseCountForCategory failed: %08x\n
IOSurfaceIsInUse: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceClient.m
ITU_R_2020
IOSurfaceFieldDetail
IOUserClientCreator
i
IOSurfaceAcceleratorTransferSurfaceWithSwap
-[IOSurfaceRemotePerSurfacePerClientState removeClientReferenceToSurface]
IOSurfaceRemoteMethodClientGetPlaneState
IOSurfaceRemoteMethodClientNeedsBindAccel
IOSurfaceMemoryRegion
DCI_P3
IOSurfaceIsInUseForAnyOtherCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceAcceleratorTransferSurface
SurfaceState
YCbCrMatrixIndex
IOSurfacePlaneElementHeight
IOSurfaceDisplayDitherYThresholds
IOSurfaceDefaultAttachments
IOSurfaceMemoryPoolCacheModeSwitchEnabled
IOSurfacePlaneCompressedTileHeight
1
MachPort
GetYCbCrMatrix
IOSurfacePixelAspectRatio
IsDisplayable
IOService
BUG: Missing state?!?
PropertyKey
ChromaLocationBottomField
Linear
aYCC
IOSurfaceSuperbuffer
IOSurfaceGPUGlobalRO
IOSurfaceSharedEventAddEventListener
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
BasicInfo
PixelAspectRatio
IOSurfaceEncoderTimes
IOSurfaceRemoteMethodClientDecrementUseCount
AcceleratorField
DebugSurfaceIDList
%@%@
IPT
BorderFillX
IOSurfaceAcceleratorConfigurePerformanceStats
_iosaLookupStubs
IOSurfaceRemoteRemoteClient { remote_pid=%d }
IOSurfaceRemoteMethodClientSetValue
Category
IOSurfacePlaneExtendedPixelsOnLeft
IOSurfaceAcceleratorGetRunLoopSource
IOSurfaceRemoteMethodClientCopyDataValueBytes
SurfaceID
IsInUse
IOSurfaceCleanAperture
VerticalOffset
BottomLeft
ReferenceRasterWidth
MetalSharedTexture
IOSurfaceGetUseCount: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
%@%d
PropertiesDictionary
_iosConnectInitalize
IOSurfacePlaneComponentRanges
ITU_R_601_4
HDRImageStatisticsInfoRaw
RectangleLeft
IOSurfaceAcceleratorTransformSurface
Buffer
HorizontalSpacing
Top
IOSurfaceGPUTimes
IOSurfaceMapCacheAttribute
IOSurfacePlaneBytesPerRowOfTileData
BorderFillY
wakePort
com.apple.iosurface.unrecognized-code-points
IOSurfaceIncrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceAllocSize
ContentLightLevelInfo
RectangleHeight
IOSurfacePlaneHeightInCompressedTiles
IOSurfaceSliceCount
IOSurfaceProhibitUseCount
ForceMaxSpeed
IOSurfaceClientGetValue getValueMethod kernel call failed %08x\n
SMPTE_240M_1995
Identity
StraightAlpha
IOSurfacePlaneCompressionType
OptOutBlitClip
result == kIOReturnSuccess
IOSurfaceRemoteMethodClientIncrementUseCount
IOSurfacePlaneElementWidth
ColorPrimaries#
JEDEC_P22
Left
SceneIllumination
IOSurfacePrefetchPages
IOSurfacePlaneExtendedPixelsOnTop
FieldCount
IOSurfaceIsGlobal
SMPTE_ST_2084_PQ
SpatialFirstLineLate
RectangleWidth
IOSurfaceEDRFactor
iokit-float
BorderFillBlueCr
HistogramBinMode
IOSurfaceOffset
IOSurfacePlaneBitsPerElement
IOSurfaceMemoryPoolZerofillEnabled
DitherControl
IOSurfaceAcceleratorSetCustomFilter
IOSurfaceRemoteMethodClientCreateMachPort
IOSurfaceRemoteMethodClientSetBulkAttachments
Failed to unserialize data from kernel: %@
PremultipliedAlpha
IOSurfaceAddressFormat
Failed to unserialize data from kernel.
<IOSurfaceNotifier %p refcnt=%d notificationPort=%p callback=%p, refcon=%p>
IOSurfacePlaneInfo
IOSurfacePlaneBase
IOSurfaceCacheMode
 
pixelFormat = 
IOSurfaceICCProfile
IOSurfacePreallocPages
HistogramPixelBins
IOSurfaceIsPrivate
AcceleratorID
ColorPrimariesIndex
IOSurfaceType
SidebandVideoPropertiesLookupID
kIOSurfaceMethodRemoveValue failed: %08x\n
HistogramOffsetX
block
IOSurfaceRemoteMethodClientIncrementUseCountForCategory
isSetValues
4:1:1
SMPTE_C
TopLeft
kIOSurfaceTrapRemoveCoreVideoBridgedValues failed: %08x\n
NearestFilter
AlphaOverride
IOSurfaceRemoteMethodClientBindAccel
IOSurfaceRemoteMethodClientGetBulkAttachments
IOSurfacePlaneHTPCPredictionSelector
kIOSurfaceTrapRemoveBulkAttachments failed: %08x\n
IOSurfaceAcceleratorCaptureSurface
IOSurfaceRemoteMethodClientGetYCbCrMatrix
key
AGXUseNearestChromaFiltering
IOSurfaceHeight
EBU_3213
IOSurfaceEnableStatistics
kIOSurfaceMethodSetCoreVideoBridgedKeys failed: %08x\n
IOSurfaceBufferTileFormat
IOSurfacePlaneCompressedTileHeaderRegionOffset
IOSurfaceIsInUseForCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
Layout
IOSurfacePixelFormat
IOSurfaceBufferTileMode
IOSurfaceAcceleratorBlitSurface
PlaneState
dict
height = 
IOSurfaceContentHeadroom
iosCacheSet
IOSurfaceTransactionListImpl
IOSurface
IOSurfaceSharedEvent
IOSurfaceSharedEventListener
IOSurfaceWiringAssertion
IOSurfaceMemoryPool
IOSurfaceTransactionList
NSObject
NSSecureCoding
NSCoding
IOSurfaceRemoteServer
IOSurfaceDebugDescription
IOSurfaceRemotePerSurfaceGlobalState
IOSurfaceRemotePerSurfacePerClientState
IOSurfaceRemoteRemoteClient
_IOSurfaceDebugDescription
IOSurfaceTransaction
initWithProperties:
setSurfaceStates:
_length
dealloc
_layoutInfo
shutdown
_removeSurface:
bytesPerRowOfPlaneAtIndex:
decrementUseCountForCategory:
rangeOfString:
setListener:
supportsProtectionOptions:
T@?,C,N,V_disconnectedHandler
initWithRemoteConnection:disconnectedQueue:disconnectedHandler:
TI,R
componentsJoinedByString:
pixelFormatString
TI,R,D
count
currentHandler
retain
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
_poolId
_eventPort
objectForKeyedSubscript:
zone
T@\"NSObject<OS_xpc_object>\",&,N,V_remoteConnection
setGlobalState:
incrementUseCountForCategory:
setAttachment:forKey:
_globalTraceObjectID
_name
eventPort
removeAllAttachments
setRemoteConnection:
T@\"NSString\",R,D
TI,R,N
addEntriesFromDictionary:
isMemberOfClass:
protectionOptions
widthOfPlaneAtIndex:
_signaledValue
formattedDescription:
_notificationPort
debugDescription
clients
T@\"IOSurfaceSharedEvent\",R,V_event
surfaceDescriptions
TQ,R
allowsPixelSizeCasting
initWithListener:options:
lockWithOptions:seed:
TB,R,D
isProxy
Ti,N,V_pid
isSysMemOnly
waitValue
respondsToSelector:
_dispatchQueue
_mapped_size
addObject:
eventPortAtIndex:
initWithOptions:
planeCount
substringFromIndex:
UTF8String
notifyListener:atValue:block:
incrementUseCount
numberWithUnsignedInt:
removeAttachmentForKey:
supportsRollback
_kernelFullListLength
conformsToProtocol:
initWithSerializedData:numWritten:actualLength:selectedLength:
newChildSurfaceWithProperties:
T@\"NSObject<OS_xpc_object>\",&,N,V_listener
TB,R,GisInUse
TQ
flush:
stringWithCString:encoding:
strongToWeakObjectsMapTable
_mapped_address
_globalState
newWiringAssertion
removeObjectForKey:
T@\"NSMutableArray\",&,N,V_clients
T@\"NSString\",?,R,C
_eventOptions
initWithClientBuffer:
_addSurface:mappedAddress:mappedSize:extraData:
decrementUseCount
disconnectedQueue
handleFailureInFunction:file:lineNumber:description:
localUseCount
setPurgeable:oldState:
_handleMessage:
initWithBasicInfo:layoutInfo:name:
raise:format:
_basicInfo
allAttachments
arrayWithObjects:count:
hash
TQ,R,D
elementWidth
isKindOfClass:
objectAtIndex:
remoteConnection
_getClient:inboundExtradata:outboundExtraData:
_handleClientConnection:
_pid
description
setTimestamp:atIndex:
unsignedLongLongValue
T@\"NSMutableDictionary\",&,N,V_surfaceStates
TQ,R,V_selectedLength
mergeExtraData:
globalState
kernelFullListLength
selectedLength
setDisconnectedHandler:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnectedQueue
fromSerialized:
T@\"NSString\",R
encodeWithCoder:
Ti,R
_isWrite
disconnectedHandler
numberWithUnsignedLongLong:
setClients:
supportsSecureCoding
dirtySize
_cfTypeID
elementHeightOfPlaneAtIndex:
initWithMachPort:
performSelector:
stringWithFormat:
TB,R
T^v,R
encodeXPCObject:forKey:
event
retainCount
T@\"NSString\",R,C
_poolPort
initWithSharedEvent:waitValue:isWrite:
isMemoryRegionUsed
lastPathComponent
name
setDisconnectedQueue:
setPid:
_surfaceStates
isInUseForAnyOtherCategory:
setValue:forKey:
surfaceID
waitUntilSignaledValue:timeoutMS:
_surface
elementHeight
stringByPaddingToLength:withString:startingAtIndex:
stringWithFileSystemRepresentation:length:
_csid
baseAddress
bytes
defaultManager
elementWidthOfPlaneAtIndex:
initWithCoder:
listener
timestampAtIndex:
T^{__IOSurfaceClient=},R,N
addClientReferenceToSurfaceWithExtraData:
attachmentForKey:
objectForKey:
removeObject:
_lock
_mach_port
residentSize
signaledValue
unlockWithOptions:seed:
initWithSurfaceID:
superclass
_event
_remoteConnection
copy
inUse
seed
setObject:forKey:
isWrite
_clients
_disconnectedHandler
copyDebugInfo
Tq,R
_refcount
decodeXPCObjectOfType:forKey:
globalStateForSurface:mappedAddress:mappedSize:extraData:
isInUseForCategory:
pixelFormat
removeClientReferenceToSurface
traceID
pid
registryID
bytesPerElement
debugRefCount
intValue
surfaceStates
T@\"IOSurfaceRemotePerSurfaceGlobalState\",&,N,V_globalState
TB,R,V_isWrite
TQ,R,V_kernelFullListLength
_impl
isDisplayable
performSelector:withObject:
self
TQ,R,V_globalTraceObjectID
_queue
_txnCache
height
_mtx
ensureMemory:
virtualAddress
.cxx_destruct
isWired
queue
_disconnectedQueue
_listener
initWithSurfaceID:mappedAddress:mappedSize:extraData:
unsignedIntegerValue
isInUse
setObject:forKeyedSubscript:
numberWithInt:
removeAllObjects
release
bytesPerElementOfPlaneAtIndex:
isEqual:
length
_serializedData
surface
TI,R,V_eventPort
_extraData
numberOfUseCountCategories
transactionAtIndex:
_waitValue
heightOfPlaneAtIndex:
initWithBytes:length:
stringWithUTF8String:
init
initWithDispatchQueue:
setQueue:
.cxx_construct
autorelease
cStringUsingEncoding:
getBytes:length:
numberWithUnsignedLong:
performSelector:withObject:withObject:
_selectedLength
_handleClientDisconnected:
_notifyEventPort:event:atValue:block:
globalTraceObjectID
initWithIOSurface:
initWithSurface:mappedAddress:mappedSize:extraData:
TQ,R,V_length
poolId
width
_handleError:
baseAddressOfPlaneAtIndex:
bytesPerRow
setAllAttachments:
T#,R
class
setSignaledValue:
TQ,R,V_waitValue
allocationSize
countByEnumeratingWithState:objects:count:
initWithIOSurfaceClient:
@24@0:8:16
@\"IOSurfaceTransaction\"24@0:8Q16
i28@0:8I16^I20
B16@0:8
B24@0:8@16
@40@0:8:16@24@32
I24@0:8Q16
i16@0:8
^{__IOSurfaceClient=}36@0:8I16@20^@28
@\"NSMutableDictionary\"
Vv16@0:8
v24@0:8@16
v24@0:8@\"NSCoder\"16
^v16@0:8
@\"IOSurfaceRemotePerSurfaceGlobalState\"
@16@0:8
v20@0:8I16
@40@0:8r^{?=QIIIIIIIIQQCCCCIQQQQQQQ}16r^{?=QQQQIII}24@32
@\"NSString\"
@32@0:8:16@24
B24@0:8#16
r^Q
@?16@0:8
{unordered_map<unsigned long, IOSurfaceTransaction *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned 
^v24@0:8Q16
v24@0:8Q16
^{IONotificationPort=}
@48@0:8^{__IOSurfaceClient=}16^v24Q32@40
@24@0:8@16
^v
@\"NSObject<OS_xpc_object>\"
{?=\"offset\"Q\"width\"Q\"height\"Q\"bytesPerRow\"Q\"bytesPerElement\"I\"elementWidth\"I\"elementHeight\"I}
@36@0:8@16Q24B32
@\"IOSurfaceSharedEvent\"
@56@0:8{shared_ptr<IOSurfaceTransactionSerialized[]>=^{?}^{__shared_weak_count}}16Q32Q40Q48
@24@0:8@\"NSCoder\"16
q16@0:8
^{__IOSurfaceClient=}16@0:8
v24@0:8@?16
i24@0:8@16
B24@0:8@\"Protocol\"16
@\"NSMutableArray\"
^{__IOSurfaceClient=}
Q
B
{shared_ptr<IOSurfaceTransactionSerialized[]>=\"__ptr_\"^{?}\"__cntrl_\"^{__shared_weak_count}}
I16@0:8
B32@0:8Q16Q24
@32@0:8@16@24
I
@\"NSObject<OS_dispatch_queue>\"
@24@0:8Q16
v32@0:8@16@24
v20@0:8i16
@?
{?=\"clientAddress\"Q\"surfaceID\"I\"pixelFormat\"I\"retainCount\"I\"yCbCrMatrix\"I\"cacheMode\"I\"mapCacheAttribute\"I\"purgeableState\"I\"purgeableStateAPI\"I\"allocOffset\"Q\"allocSize\"Q\"isGlobal\"C\"isAllocated\"C\"isWired\"C\"pad\"C\
#16@0:8
@20@0:8I16
v32@0:8Q16Q24
v48@0:8^{__IOSurfaceClient=}16^v24Q32@40
B24@0:8:16
@24@0:8^{__IOSurfaceClient=}16
q24@0:8Q16
Q24@0:8Q16
v40@0:8@16Q24@?32
B24@0:8Q16
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@40@0:8@16@24@?32
i
Q16@0:8
^{_NSZone=}16@0:8
@\"NSString\"16@0:8
{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}
v44@0:8I16@20Q28@?36
@44@0:8I16^v20Q28@36
@24@0:8r^v16
B20@0:8I16
v16@0:8
```
