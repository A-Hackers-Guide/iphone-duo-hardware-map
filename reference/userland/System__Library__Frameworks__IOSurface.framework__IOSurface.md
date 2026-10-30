# `/System/Library/Frameworks/IOSurface.framework/IOSurface`

iOS 27.2 dyld shared cache image. Version `403.1.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 13 classes, 4 protocols, 188 methods, 72 properties

### Class pages

Every class and protocol, with its methods: [`IOSurface`](../objc/IOSurface_IOSurface.md), [`IOSurfaceDebugDescription`](../objc/IOSurfaceDebugDescription_IOSurface.md), [`IOSurfaceMemoryPool`](../objc/IOSurfaceMemoryPool_IOSurface.md), [`IOSurfaceRemotePerSurfaceGlobalState`](../objc/IOSurfaceRemotePerSurfaceGlobalState_IOSurface.md), [`IOSurfaceRemotePerSurfacePerClientState`](../objc/IOSurfaceRemotePerSurfacePerClientState_IOSurface.md), [`IOSurfaceRemoteRemoteClient`](../objc/IOSurfaceRemoteRemoteClient_IOSurface.md), [`IOSurfaceRemoteServer`](../objc/IOSurfaceRemoteServer_IOSurface.md), [`IOSurfaceSharedEvent`](../objc/IOSurfaceSharedEvent_IOSurface.md), [`IOSurfaceSharedEventListener`](../objc/IOSurfaceSharedEventListener_IOSurface.md), [`IOSurfaceTransaction`](../objc/IOSurfaceTransaction_IOSurface.md), [`IOSurfaceTransactionList`](../objc/IOSurfaceTransactionList_IOSurface.protocol.md), [`IOSurfaceTransactionListImpl`](../objc/IOSurfaceTransactionListImpl_IOSurface.md), [`IOSurfaceWiringAssertion`](../objc/IOSurfaceWiringAssertion_IOSurface.md), [`NSCoding`](../objc/NSCoding_IOSurface.protocol.md), [`NSObject`](../objc/NSObject_IOSurface.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_IOSurface.protocol.md), [`_IOSurfaceDebugDescription`](../objc/_IOSurfaceDebugDescription_IOSurface.md)

### Classes

`IOSurface`, `IOSurfaceDebugDescription`, `IOSurfaceMemoryPool`, `IOSurfaceRemotePerSurfaceGlobalState`, `IOSurfaceRemotePerSurfacePerClientState`, `IOSurfaceRemoteRemoteClient`, `IOSurfaceRemoteServer`, `IOSurfaceSharedEvent`, `IOSurfaceSharedEventListener`, `IOSurfaceTransaction`, `IOSurfaceTransactionListImpl`, `IOSurfaceWiringAssertion`, `_IOSurfaceDebugDescription`

### Protocols

`IOSurfaceTransactionList`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) length;
@property (TQ,R) kernelFullListLength;
@property (TQ,R) selectedLength;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (Tq,R) allocationSize;
@property (Tq,R) width;
@property (Tq,R) height;
@property (T^v,R) baseAddress;
@property (TI,R) pixelFormat;
@property (Tq,R) bytesPerRow;
@property (Tq,R) bytesPerElement;
@property (Tq,R) elementWidth;
@property (Tq,R) elementHeight;
@property (TI,R) surfaceID;
@property (TI,R) seed;
@property (TQ,R) planeCount;
@property (TB,R,GisInUse) inUse;
@property (Ti,R) localUseCount;
@property (TB,R) allowsPixelSizeCasting;
@property (TQ,R,D) virtualAddress;
@property (TQ,R,D) allocationSize;
@property (TI,R,D) surfaceID;
@property (TI,R,D) pixelFormat;
@property (T@"NSString",R,D) pixelFormatString;
@property (TQ,R,D) width;
@property (TQ,R,D) height;
@property (TQ,R,D) dirtySize;
@property (TQ,R,D) residentSize;
@property (T@"NSString",R,D) name;
@property (TB,R,D) isWired;
@property (TQ,R) poolId;
@property (T@"IOSurfaceRemotePerSurfaceGlobalState",&,N,V_globalState) globalState;
@property (T^{__IOSurfaceClient=},R,N) surface;
@property (TI,R,N) debugRefCount;
@property (Ti,N,V_pid) pid;
@property (T@"NSMutableDictionary",&,N,V_surfaceStates) surfaceStates;
@property (T@"NSObject<OS_xpc_object>",&,N,V_remoteConnection) remoteConnection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_disconnectedQueue) disconnectedQueue;
@property (T@?,C,N,V_disconnectedHandler) disconnectedHandler;
@property (T@"NSObject<OS_xpc_object>",&,N,V_listener) listener;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableArray",&,N,V_clients) clients;
@property (TQ) signaledValue;
@property (TI,R,V_eventPort) eventPort;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (TB,R) supportsRollback;
@property (T@"IOSurfaceSharedEvent",R,V_event) event;
@property (TQ,R,V_waitValue) waitValue;
@property (TB,R,V_isWrite) isWrite;
@property (TQ,R,V_length) length;
@property (TQ,R,V_kernelFullListLength) kernelFullListLength;
@property (TQ,R,V_selectedLength) selectedLength;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) virtualAddress;
@property (TQ,R) allocationSize;
@property (TI,R) surfaceID;
@property (TI,R) pixelFormat;
@property (T@"NSString",R) pixelFormatString;
@property (TQ,R) width;
@property (TQ,R) height;
@property (TQ,R) residentSize;
@property (TQ,R) dirtySize;
@property (T@"NSString",R) name;
@property (TQ,R) traceID;
@property (TB,R) isWired;
```

## Strings (432)

```
IOSurfaceDisallowForever() invoked too late, connection to IOSurface.kext already established
IOSurface creation failed: %08x parentID: %08x property: %@
IOSurface creation failed. IOSurface service not present
%s
IOSurface Deserialization failure for key %{public}s: %@
Failed to map client shared memory object from pid %d
Received unknown client method %lu from client %d
Client is providing a shmem for its own mapping, pid %d
IOSurfaceAppendTransaction got null buffer
IOSurface creation failed: %08x parentID: %08x properties: %@%s
Surface %d released by client pid=%d
Surface %d created by client pid=%d
[IOSurfaceTransactionListImpl transactionAtIndex] failed to create transaction at index %zu
[IOSurfaceTransactionListImpl eventPortAtIndex] invalid index %zu
IOSurfaceAppendTransaction got null transaction
IOSurfacePruneTransactionList got null buffer
IOSurface.framework versus IOSurface.kext version mismatch
IOSurfaceAppendTransaction got non-success return from kernel
IOSurfaceQueryTransactionList failed to allocate memory
[IOSurfaceTransactionListImpl transactionAtIndex] invalid index %zu
Received client method %lu (%s) from client %d
IOSurface client memory mapping is %lu bytes but client claims allocation size of %lu bytes
IOSurface.framework not allowed to iterate kernel services (%08x).  API disallowed.
IOSurfaceClientInvalidate failed: %08x
Client connected pid=%d
Client disconnected pid=%d
[IOSurfaceTransaction fromSerialized] got nil event from serialized data
IOSurfaceQueryTransactionList got non-success return from kernel
IOSurface.framework API explicitly disallowed.
IOSurface creation failed. IOSurface open failed: %08x %s
IOSurfaceQueryTransactionList got null buffer
IOSurfacePlaneBase
IOSurfacePlaneBitsPerElement
IOSurfacePlaneComponentNames
kIOSurfaceMethodRemoveValue failed: %08x\n
key
Failed to unserialize data from kernel: %@
height = 
Center
Top
DV 4:2:0
4:2:0
HDRImageStatisticsInfoFiltered
IOSurfacePlaneBytesPerTileData
BorderFillBlueCr
IOSurfaceTransferFunction
IOSurfaceIsPrivate
MetalSharedTexture
AlphaOverride
HistogramOffsetX
1
IOSurfaceRemoteRemoteClient { remote_pid=%d }
IOSurfaceRemoteMethodClientNeedsBindAccel
IOSurfaceIsGlobal
IOSurfaceDisplayDitherThresholds
IOSurfacePlaneCompressionFootprint
SurfaceID
PropertyKey
CleanAperture
ForceMaxSpeed
IOSurfaceAcceleratorBlitSurfaceWithSwap
JEDEC_P22
Average
IOSurfaceAcceleratorTransferSurfaceWithSwap
v16@?0@\"IOSurfaceRemoteRemoteClient\"8
-[IOSurfaceRemoteRemoteClient _getClient:inboundExtradata:outboundExtraData:]
BUG: Missing state?!?
IOSurfaceRemoteMethodClientCopyAllValues
IOSurfaceRemoteMethodClientIsInUseForCategory
IOSurfaceAllocSize
TemporalBottomFirst
IOSurfaceDecoderTimes
kIOSurfaceMethodDecrementUseCountForCategory failed: %08x\n
IOSurfaceAcceleratorAbortTransfers
IOSurfaceRemoteMethodClientCreate
isSetValues
HorizontalOffset
SpatialFirstLineEarly
IOSurfacePlaneExtendedPixelsOnTop
IOSurfaceClientGetValue getValueMethod kernel call failed %08x\n
HistogramBinMode
HistogramOffsetY
ZeroFill
result == kIOReturnSuccess
IOSurfaceColorSpaceID
ITU_R_709_2
BorderFillGreenCb
IOSurfaceNotifier
ChromaLocationTopField
object
CFTypeRef  _Nullable _ioSurfaceDeserializedFromXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull)
IOSurfaceHeight
%@: plane index (%ld) out of bounds (%ld)
IOSurfacePlaneCompressedTileHeaderRegionOffset
category out of range
IOSurfaceRemoteMethodClientGetYCbCrMatrix
Failed to unserialize data from kernel.
Method
OldState
IOSurfaceNonPurgeable
IOSurfaceSuperbuffer
DebugLogBlock
IOSurfacePlaneSize
ITU_R_2100_ICtCp
v16@?0@\"NSObject<OS_xpc_object>\"8
GetYCbCrMatrix
ClientProvidedShmem
id = 
EBU_3213
IEC_sRGB
VerticalOffset
, 
_iosConnectInitalize() unable to open IOSurface kernel service: %08x\n%d existing clients:\n%s\n
SkipAsyncCallback
IOSurfaceDirection
IOSurfaceContentHeadroom
SMPTE_C
UseGamma
ITU_R_2100_HLG
RectangleHeight
IOSurfaceDisplayTimes
IOSurfaceEncoderTimes
IOSurfaceProtectionOptions
IOSurfaceName
IOSurfaceEnableStatistics
IOCoreSurfaceRoot
Transform
User Clients
Invalid parameter not satisfying: %@
IOSurfaceCleanAperture
IOSurfaceMemoryPoolZerofillEnabled
IOSurfaceIncrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
FixUpscaling
DitherControl
IOSurfaceRemoteServer.m
IOSurfaceRemoteMethodClientGetBulkAttachments
StraightAlpha
IOSurfacePlaneVerticalPixelOffsetWithinCompressedTileArray
IOSurfacePlaneExtendedPixelsOnRight
IOSurfaceAcceleratorSetFilterCoefficients
BUG: refcount is already zero
EventOperation
IOSurfaceElementHeight
%4d
%@: surface is not planar
IOSurfaceAddressOffset
IOSurfaceMemoryPoolCacheModeSwitchEnabled
ErrorCode
FieldCount
ChromaLocationBottomField
IPT
SpatialFirstLineLate
VerticalSpacing
IOSurfaceMemoryPoolEntitlement
%@%d
BufferSize
MachPort
ChromaSubsampling
IOSurfaceAddress
BottomLeft
IOSurfaceGPUGlobalRO
IOSurfaceRemoteMethodClientCopyDataValueBytes
PlaneIndex
DebugSurfaceRefCount
RectangleWidth
RectangleTop
IOSurfacePurgeWhenNotInUse
kIOSurfaceMethodIncrementUseCountForCategory failed: %08x\n
IOSurfaceAcceleratorGetServiceObject
IOSurfaceRemoteMethodGetDebugInfo
YCbCrMatrixIndex
Bottom
Minimum
IOSurfacePrefetchPages
IOSurfacePlaneHTPCPredictionSelector
IOSurfaceSharedEventAddEventListener failed: %08x\n
block
Options
SetExtraData
IOSurfacePlaneHeight
IOSurfacePixelFormat
ITU_R_2020
HorizontalSpacing
OptOutBlitClip
AcceleratorID
SMPTE_ST_2084_PQ
IOSurfaceDefaultAttachments
IOSurfaceHostOnly
com.apple.IOSurfaceRemoteServer
IOSurfaceRemoteMethodClientSetBulkAttachments
EDRFactor
DisplayMaskRectangle
IOSurfaceTimingInfo
IOSurfaceIsInUseForCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
iosCacheSet
CustomFilter
BorderFillY
HistogramWidth
IOSurfaceRemoteMethodClientSetPurgeable
IOSurfacePlaneBytesPerRow
AlphaChannelMode
IOSurfacePlaneBytesPerCompressedTileHeader
kIOSurfaceTrapRemoveBulkAttachments failed: %08x\n
IOSurfaceRemoteMethodClientRelease
DebugLogQueue
TransferFunction#
IOSurfaceEDRFactor
IOSurfaceAcceleratorTransferSurface
IOSurfaceAcceleratorSetCustomFilter
_iosaLookupStubs
IOSurfaceEventNotification
IOSurfaceRemoteMethodClientDecrementUseCount
IOSurfacePixelSizeCastingAllowed
IOSurfacePlaneComponentRanges
IOSurfaceChromaLocationTopField
%s\n
IOSurfaceAcceleratorCaptureSurface
PixelAspectRatio
DebugSurfaceIDList
IOSurfacePlaneComponentTypes
DCI_P3
ContentLightLevelInfo
IOSurfaceBufferTileFormat
IOFenceAllowTearing
_iosCacheDict
IOSurfaceYCbCrMatrix
Linear
IOSurfacePlaneHeaderRegionBytesPerSlice
IOSurfaceIsInUseForAnyOtherCategory: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
Limits
EventValue
void _ioSurfaceSerializeToXPCDictionaryWithKey(__strong xpc_object_t _Nonnull, const char * _Nonnull, CFTypeRef _Nonnull)
IOSurfacePlaneBytesPerElement
AlphaChannelIsOpaque
SMPTE_ST_428_1
HDRImageStatisticsInfoRaw
SceneIllumination
IOSurfaceWidth
IOSurfaceSubsampling
width = 
IOSurfaceChromaSubsampling
PremultipliedAlpha
IOSurfaceGPUTimes
TopLeft
Maximum
VersatileSenselArrayPattern
HorizontalDisparityAdjustment
IOSurfacePlaneDataRegionBytesPerSlice
/Library/Caches/com.apple.xbs/329888F6-71E8-4CF7-B533-B96C049D3738/TemporaryDirectory.BvI3iR/Sources/IOSurface/IOSurfaceUser/IOSurfaceClient.m
IOSurfaceRemoteMethodClientIsInUse
AcceleratorField
ColorPrimaries#
4:1:1
pid
Layout
GetExtraData
ExtraData
IOSurfaceChromaLocationBottomField
CreationProperties
IOSurfacePlaneExtendedPixelsOnBottom
BorderFillX
IOSurfaceRemoteMethodClientCreateMachPort
ColorPrimariesIndex
IOSurfaceClass
IsDisplayable
IOSurfaceAcceleratorConfigurePerformanceStats
IOSurfaceAcceleratorAbortCaptures
com.apple.iosurface.unrecognized-code-points
IOSurfaceRemoteMethodClientDecrementUseCountForCategory
name = 
IOSurfaceAddressRanges
YCbCrMatrix#
IOSurfacePlaneHorizontalPixelOffsetWithinCompressedTileArray
kIOSurfaceTrapRemoveCoreVideoBridgedValues failed: %08x\n
Buffer
FieldDetail
%@%@
IOSurfaceAddressFormat
BorderFillHeight
_ioSurfaceEventNotificationCallback2
!
IOSurfaceRemoteMethodInitialize
IOSurfaceRemoteMethodClientRemoveAllValues
IOSurfaceType
TransferFunction
IOSurfacePlaneHTPCVerticalHeaderGroupingMode
IOSurfaceAcceleratorGetStatistics
ReferenceRasterHeight
IOSurfaceUseReserve
IOService
IOSurfaceAcceleratorTransformSurface
IOSurfaceRemoteMethodClientLock
PlaneState
NeedsBindAccelerator
 
v8@?0
%s, Line=%d, Error=%s\n
IOSurfaceColorSpace
IOSurfaceSysMemOnly
IOSurfaceDecrementUseCountForCategory: error: Attempt to change use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOSurfaceIsInUse: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
_iosConnectInitalize
_iosConnectInitalize() unable to open IOSurface kernel service: %08x
NearestFilter
ColorRemapMode
pixelFormat = 
4:2:2
IOSurfacePlaneWidthInCompressedTiles
iokit-float
HistogramHeight
IOSurfaceAcceleratorGetID
sRGB
IOSurfaceRemoteMethodClientGetPlaneState
IOSurfacePlaneWidth
IOSurfacePlaneOffset
This object may only be encoded by an NSXPCCoder.
DolbyVisionRPUData
 (likely sandbox violation)
Internal error during notification request %08x
IOSurfaceRemoteMethodClientSetValue
SurfaceState
IOSurfaceElementWidth
IOSurfacePlaneComponentBitOffsets
P3_D65
Identity
BorderFillAlpha
/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
value
PropertiesDictionary
<not set>
IOSurfaceFieldCount
IOSurfacePlaneCompressedTileWidth
i
BorderFillWidth
IOSurfacePlaneInfo
IOSurfacePlaneElementWidth
IOSurfaceMemoryRegion
aYCC
Width
IOSurfacePlaneCompressedTileDataRegionOffset
IOSurfacePlaneBytesPerRowOfCompressedTileHeaderGroups
IOSurfacePlaneBytesPerRowOfTileData
IOSurfacePlaneExtendedPixelsOnLeft
HistogramMaxPixelValue
IOSurfaceAcceleratorConditionalTransferSurfaceWithSwap
-[IOSurfaceRemotePerSurfacePerClientState removeClientReferenceToSurface]
IOSurfaceRemoteMethodClientIncrementUseCount
sid: %08x traceID: %016llx virt: %016llx fmt: %s dims: %5d x %5d size: %7s name: %@
BasicInfo
Category
This object may only be decoded by an NSXPCCoder.
0x%08x
IOSurfaceScalerTimes
IOSurfaceDefaultBulkAttachments
IOSurfacePlaneCompressionType
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
IOSurfaceRemoteMethodClientRemoveValue
MemoryObject
IOSurfaceICCProfile
IOSurfaceFieldDetail
IOSurfaceAcceleratorBlitSurface
IOSurfaceSharedEvent.m
NewState
IOSurfaceCacheMode
IOSurfaceAcceleratorGetTypeID
IOSurfaceClientSetSurfaceNotify failed %08x\n
TransferFunctionIndex
IOSurfaceBytesPerRow
TemporalTopFirst
RectangleLeft
IOSurfaceDisplayDitherCrThresholds
IOSurfaceAllocateFromSuperbuffer
IOSurfaceMemoryPoolSize
IOSurfaceClient.m
wakePort
ITU_R_601_4
ReferenceRasterWidth
IOSurfaceResetDefaultAttachmentsWhenNotInUse
IOSurfaceRemoteMethodClientIsInUseForAnyOtherCategory
IOSurfaceGammaLevel
MasteringDisplayColorVolume
IOSurfaceDisplayDitherYThresholds
IOSurfaceMapCacheAttribute
IOSurfacePlaneCompressedTileHeight
IOSurfaceProhibitUseCount
IOSurfaceRemoteMethodClientBindAccel
IOSurfaceRemoteProtocol.m
IOSurface.port
AGXUseNearestChromaFiltering
LockInScaler
Client Surfaces
SMPTE_240M_1995
kIOSurfaceMethodSetCoreVideoBridgedKeys failed: %08x\n
IOSurfaceAcceleratorGetRunLoopSource
IOSurfaceRemoteMethodClientSignalEvent
IOSurfaceRemoteMethodClientIncrementUseCountForCategory
IsInUse
ProtocolVersion
IOSurfaceBufferTileMode
IOSurfaceDisplayDitherCbThresholds
kIOSurfaceTouchEventTimes
SidebandVideoPropertiesLookupID
IOSurfaceGetUseCount: error: Attempt to query use count on an IOSurface (%p) created with kIOSurfaceProhibitUseCount.
IOUserClientCreator
HistogramPixelBins
<IOSurfaceNotifier %p refcnt=%d notificationPort=%p callback=%p, refcon=%p>
IOSurfaceMemoryPoolInfo
 (likely per client IOSurface limit of 16384 reached)
LookupID
dict
IOSurfaceOffset
\n
IOSurfacePreallocPages
IOSurfaceSharedEventAddEventListener
EventPort
IOSurfacePlaneElementHeight
IOSurfacePlaneComponentBitDepths
Left
IOSurfaceSliceCount
IOSurfaceBytesPerElement
IOSurfaceColorPrimaries
_iosConnectInitalize() unable to locate IOSurface kernel service
BorderFillRedY
com.apple.IOSurface.Remote
Height
IOSurfacePixelAspectRatio
IOSurfaceClientCopyValue getValueMethod kernel call failed %08x\n
IOSurfaceAcceleratorCreate
Kernel Surfaces
IOSurfacePlaneHeightInCompressedTiles
IOSurfaceRemoteMethodClientUnlock
GammaLevel
```
