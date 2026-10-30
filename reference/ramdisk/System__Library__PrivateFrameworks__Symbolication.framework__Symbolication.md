# `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,133,088 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 39 (Size: 6264)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (21)

- `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication (compatibility version 1.0.0, current version 64578.132.1)`
- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1)`
- `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Network.framework/Network (compatibility version 1.0.0, current version 6681.52.5)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (97 classes, 6 protocols)

Classes: `NSArray`, `VMUAbstractSerializer`, `VMUAnalyticsEvent`, `VMUAnalyzerBase`, `VMUAnalyzerSummaryField`, `VMUArchitecture`, `VMUAttributeGraphRegionIdentifier`, `VMUAttributeGraphTypeIdentifier`, `VMUAutoreleasePoolsAnalyzer`, `VMUBacktrace`, `VMUBacktraceRecursionInfo`, `VMUCachedPointerFieldInfo`, `VMUCallTreeLeafNode`, `VMUCallTreeNode`, `VMUCallTreePseudoNode`, `VMUCallTreeRoot`, `VMUCallTreeRootWithBacktrace`, `VMUClassInfo`, `VMUClassInfoMap`, `VMUClassPatternMatcher`, `VMUDebugTimer`, `VMUDepthGraph`, `VMUDepthGraphEnumerator`, `VMUDirectDominees`, `VMUDirectedGraph`, `VMUDominatedByGraphEnumerator`, `VMUDominatesGraphEnumerator`, `VMUDominatorCallTreeCreator`, `VMUDominatorGraph`, `VMUDominatorRoots`, `VMUDomtreeName`, `VMUDuplicatesAnalyzer`, `VMUFakeSampler`, `VMUFieldInfo`, `VMUFieldValue`, `VMUFlattenGraphEnumerator`, `VMUGraphEnumerator`, `VMUGraphStackLogReader`, `VMUGroupBy`, `VMUGroupByNode`, `VMUGroupType`, `VMUHeapAndVMAggregator`, `VMUHeapAndVMAggregatorOptions`, `VMUIOSurfaceDebugDescription`, `VMUInverseDepthGraphEnumerator`, `VMUKernelCoreMemoryScanner`, `VMUKernelRuntimeMetadataChunkInfo`, `VMULeakDetector`, `VMULeaksAnalyzer`, `VMUMallocZoneAggregate`, `VMUMutableClassInfo`, `VMUMutableFieldInfo`, `VMUNodeGroup`, `VMUNodeToStringMap`, `VMUNonOverlappingRangeArray`, `VMUOSTransactionsAnalyzer`, `VMUObjectGraph`, `VMUObjectIdentifier`, `VMUObjectIdentifierDriverKitSupport`, `VMUObjectLabelHandlerInfo`, `VMUOptionParser`, `VMUPeakFootprintAnalyzer`, `VMUProcInfo`, `VMUProcList`, `VMUProcessDescription`, `VMUProcessLedger`, `VMUProcessObjectGraph`, `VMUProcessObjectGraphRefiner`, `VMUProgressBar`, `VMURangeArray`, `VMURangeToStringMap`, `VMUReferenceTreeAnalyzer`, `VMUReverseGraphEnumerator`, `VMURuntimeMetadataChunkInfo`, `VMUSampler`, `VMUScanOverlay`, `VMUSimpleDeserializer`, `VMUSimpleSerializer`, `VMUStackLogConsolidator`, `VMUStackLogReaderBase`, `VMUSwiftRemoteMirrorCallbackCache`, `VMUSwiftRuntimeInfo`, `VMUSymbolStore`, `VMUTask`, `VMUTaskMemoryCache`, `VMUTaskMemoryScanner`, `VMUTaskStackLogReader`, `VMUTaskThreadStates`, `VMUTerminalColorizer`, `VMUTraceTreeAnalyzer`, `VMUTraceTreeAnalyzerResult`, `VMUVMRegion`, `VMUVMRegionIdentifier`, `VMUVMRegionRangeInfo`, `VMUVMRegionTracker`, `VMUWiredMemoryInfo`, `__VMULeaksMarkerObject`

Protocols: `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `VMUCommonGraphInterface`, `VMUStackLogReader`

## Strings (6,419)

First 2,500 of 6,419.
```
UnsafeUnretainedRef
{unique_ptr<
VAS_DATA
task peeking transformer guard queue
INSTANCE
v16@?0@\"VMUMutableClassInfo\"8
strcmp((const char*)(&newStringRegion[encoded]), (const char*)bytes) == 0
NSNotFound
The provided memory graph file is corrupted
NSConcreteMutableData (Bytes Storage)
/usr/lib/libobjc.A.dylib
CFBundleShortVersionString
OS_nw_array
_isaTranslator
Kernel Pointers Into User Space
SEL
PRV
One or both of the AsyncTask and AsyncTask Slab metadata isas isn't known, so skipping precise scanning of AsyncTasks and AsyncTask Slabs.\n
\tCall stack: %s\n
_controlView
SYMBOLICATION_LOG_SWIFT_REMOTE_MIRROR_MEMORY_READS
  CS_NX
neural
pthread_t
AUTORELEASEPOOLS
_os_trace_realloc
$1: $2
ARM64E
pat
strings_
value_field
unknown-%u
pthread start routine argument
__NSMallocBlock__
buffer
_objc_debug_swift_stable_abi_bit
LiIcCqQsSfdB@*?#:^
com.apple.dt.Symbolication.VMUDirectedGraph
(VMUBacktraceUniquing): Invalid parent node %#x\n
%@:%u
(VMUBacktraceUniquing) expandUniquingTable(): mach_vm_deallocate failed. [%p]\n
, std::__bucket_list_deallocator<
v16@?0^{dyld_image_s=}8
__NSCFBoolean
_sorted?  %s\n
Class.data.protocols.lists (protocol_list_t)
CGSEventAppendix
VM_KERN_MEMORY_OSKEXT
network_nonvolatile
Found no malloc zones in target process
Number of addresses sent to VMUSymbolStore by client classes:\nFor backtrace sample: %zu\nFor binary sections: %zu\nFor global variables: %zu\nFor malloc stack logging: %zu\nFor hex found in node labels: %zu\nTotal unique addresses to be sa
__NSDictionaryI
__NSOrderedSetI
DriverKit
VM_KERN_MEMORY_KEXT
Won't attempt precise Swift Concurrency allocation scanning because couldn't find %s\n
float[]
signature
_bytes
_observer
childOfInstance()
toolsBuildVersionMonotonic
 %7s
v32@?0@\"NSString\"8@\"NSDictionary\"16^B24
building VMUProcessDescription
ObjC
SWIFT_OPAQUE_EXISTENTIAL
DATA
Request Message
Selecting labels that have duplicates
MallocStackLoggingLiteZone
%#10lx - %#10lx %@%@ %@%@ %@%@\n
__NSSingleObjectSetI
forward
targetPlatform
=======
WindowManager
BinaryInfoDwarfUUIDKey
<unknown binary>
S/A
Unexpected range type value %x from malloc zone enumerator\n
No malloc zone statistics available for malloc zone %@\n
@\"CSMemoryMappingSlice\"24@?0Q8Q16
UIFoundation
OSMetaClass
(ROOT LEAK|CYCLE): (VM: .*)  0x.*
transaction exists
taskgated
_malloc_zone_
Weak-With-Unscannable-Owner-Pointer-Applied
_callbacks
SWIFT_ERROR_EXISTENTIAL
  SPECULATIVE
initObjectIdentifier
backtraceUniquingTableFlags
v28@?0I8Q12@\"VMUKernelRuntimeMetadataChunkInfo\"20
libCoreLib.dylib
NSConcreteMapTable
ADMIN_REGION  PTR_IN_USE
\n\nIf after processing this memgraph with other cli tools and verifying the UUIDs you still see non-symbolicated addresses for '%@', please file a Radar to 'Symbolication | Xcode' and attach the memgraph, the dSYM and the non-symbolicated 
 | 
[%.*f seconds] \"%@\"  Created at: %@
(root)
_edgeCapacity || (!groupEdges && !_edgeCount)
AttributeGraph graph data
%#18qx - %#18qx %@%@ %@%@ %@%@\n
SWIFT_EXISTENTIAL_METATYPE
Leaks count
enumerating %@ by calling %@ in %@%s\n
Total number in stack
%c
.X1
__NSCFType
_objc_debug_indexed_isa_magic_mask
--------
nodeToTimestampTable
run_state
[coder allowsKeyedCoding]
gOSMetaClassBasePrivateLayout
<unknown-binary>
Failure calling sysctl to get proc buf
self.inverted
WTF::tryFastAlignedMalloc
  REUSABLE
(empty)
notifyd
B12@?0B8
scan nodes into the graph, while recording symbols of __DATA regions and stacks
llvm::allocate_buffer(unsigned long, unsigned long)
 + 
Class.
SHM
The memory graph file only contains labels for contents of readonly memory of the target process, so only those items can be shown.\n
[%llu]
Unknown
  PAGED_OUT
depth
uniquing_table->numNodes < MAX_UNIQUING_TABLE_NODES
% FRAG
CFBundleVersion
xpc_date_t
NSAccessibilityWeakReferenceContainer
VMUTaskMemoryCache initialization
unused  unknown system shared lib __DATA
regions.count == *regionCountInOut
TouchBarServer
__CFString
creating symbolicator signature
NSConcretePointerArray
__NS
RefFromUnalignedSourceToAlignedInterior
pc
agendaIdx != 0
(VMUBacktraceUniquing) allocate_pages(): virtual memory exhausted! (XRBacktraceRepository)
__NSSingleEntryDictionaryI
NSOrderedSet
%@: '%@'%@
v36@?0I8Q12I20I24Q28
dyld
_NSInlineData
wired_mem
[]
WTF::tryFastCompactMalloc
_children.callbacks
__NSConcreteMallocBlock
iOS
referenceDetailsLarge
cpsr
/(AppKit|UIKit(Core))\\.framework|/libswiftAppKit.dylib
_observedObject
kernelcache combined __LINKEDIT
[nodeToTimestampTable] nodeNamespaceSize %u  %lu bytes\n\n
ShortVersionString
internal
%s  %@-%@ [%@] %s/%s  %@
AsyncTask Slab
-[VMUProcessObjectGraphRefiner assessReferencePriority]
[Original Uniquing Table] %llu bytes\n\n
Compressed %s to %s (%2.1f%% reduction @ %s saved/s) in %3.6fs\n
WTF::fastZeroedMalloc
$
  '%@'
swift
-[VMUGraphStackLogReader copyOriginalUniquingTable:]_block_invoke_2
__NSCFSet
===========
$%@
(0x[a-fA-F0-9]*)\\s*-\\s*(0x[a-fA-F0-9]*)\\s*(\\S*)\\s*(\\S*)\\s*<(\\S{32})>\\s*(.*)
_arr
%10zu  _sourceAddressToReferencePriorityDict.count\n
RefFromNamedIvarToNonObjectInterior
GuardMalloc in the target process may be using too much VM
-[VMUVMRegion splitOutRange:fromRegionIndex:regions:newZoneName:reason:]
-[VMUTraceTreeAnalyzer traceTreeForAddress:outputStyle:]
com.apple.SamplingTools
%s
v32@?0@\"VMUMutableClassInfo\"8Q16@\"VMUTaskMemoryCache\"24
VM_KERN_MEMORY_WAITQ
malloc<%llu>
couldn't open %s for reading call tree\n
setting up VMUScanOverlay
v16@?0r^v8
<null-uuid>
realloc
NSAlert
Unable to open/create sample file %s\n
Getting fields for Swift value type %s\n
values_ptr
untracked
dispatch_queue_t (serial)
^{_CFStreamCallBacks=}
MALLOC_BIG
LAUNCHERDATA
*** Can't suspend task %d: %s\n
VM_KERN_COUNT_MAP_KALLOC_LARGE_DATA
immutable
Motion
Value
         The process will be suspended and may cause system instability.\n
No process corpse slots currently available - waiting to get one\n
Symbolication.framework _get_symbol_owner found requested symbol %s in unexpected non-Swift library %s\n
mallocs
Process:         %@ [%@]\nPath:            %@\nLoad Address:    %#qx\nIdentifier:      %@\nVersion:         %@\n%@Code Type:       %@\n%@Parent Process:  %@ [%@]\nTarget Type:     %@\n
__NSCFCalendar
VM_KERN_MEMORY_SECURITY
Failed to find xzm zone introspection structure
directedGraphInfo
Error occured while printing autoreleasePools per thread.\n
failed to expand uniquing table to %llu bytes\n
NSMutableCharacterSet
RefFromNSCache
MMAP
%.2f
hash_table_modify
kalloc_ext
OS_os_transaction
PropertyList.Element
Class.data.methods.lists (method_list_t)
graphNodeCount
mds
B20@?0{_VMUDirectedGraphEdge=III}8
Setting region name in %s based on _zoneNames[zone_index] for  %s\n
objc::DenseMap
v16@?0i8B12
asyncLength
The graph version (%ld) is too new.  The latest graph version this tool supports is %d.
pruning tree to matching nodes
Failed to determine task_t for pid %u %@
markMachOLibraries
v32@?0{_VMURange=QQ}8I24i28
TEXT_EXEC
Instances: %lu   Total bytes: %lu   Average bytes: %.1f   %@
_
xpc_int64_t
inline content length %ld
RefFromNSMallocBlock
  COPIED
BYTES
VM_KERN_MEMORY_PTE
NSApplication
CFSet
@(#)
__NSWeakBlockVariable__
Physical footprint:         %s\nPhysical footprint (peak):  %s\nIdle exit:                  %s\n
NSPointerArray
NSOutputStream
inline 
Float64
VMUScanTypeExactUnsafeUnretained
core file
%@.%@
VM_KERN_MEMORY_MLOCK
pthread_mutex_t
sourceInfoRanges
userMarked
target process is using %s which doesn't work with memory analysis tools
Symbolication_Internal_ForSwift.VMUAttributeGraphTypeIdentifier
swift_reflection_projectExistential
SWIFT_CLASS_INSTANCE
__SwiftValue
q24@?0@\"VMUClassInfo\"8@\"VMUClassInfo\"16
Unreadable Binary Images:\n
Thread_<multiple>
_objc_debug_autoreleasepoolpage_next_offset
item count: %ld
        Empty\n
warning: zone enumerator for \"%s\" reported '%s' %#llx (%llu bytes) in region: [%#llx-%#llx] %s\n
_malloc_zone
-[VMUClassInfo encodeWithCoder:]
ADMIN_REGION
      
ALI
ROOT LEAK: 
VOLATILE
x12
PPC
RefFromNamedIvarPlusOffsetToNonObject
Analysis of sampling %@ (pid %d) every %d milliseconds\n
Target task not available for analysis
TIGHTBEAM
<unavailable>
OBJC_CLASS_$_%@
+[VMUDirectedGraph encapsulateData:to:withSupplementalDataTag:error:dataGeneratorBlock:]
dispatch_queue_t (concurrent)
imageOffset
C++
-[VMUMallocZoneAggregate enumerateHeapAndVMSortedBy:withBlock:]
JSC::CompleteSubspace::tryAllocateSlow
NSCalendar
xpc_session_t
RefFromNamedIvarToObject
q
__weak
classInfosDerivedFromStackBacktraces
%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx
%@
buildTrain
\"%@
media_footprint
cuml_mallocs
additionalProperties
    +%5llu %#llx[%u]  %-13s  %s %s\n
VM_KERN_COUNT_MAP_KERNEL
symbolicateBacktraceUniquingTable
 MTE TPRO JIT 
Showing object labels that have at least %lu duplicates.  Pass the \"-minimumCount <count>\" argument to change the threshold.\n
non-object from 
_malloc_type
__outerOp
flatten
*** -[VMUTaskStackLogReader liteMSLPayloadforMallocAddress:size:] error %d from task_peek\n
%10llu  TOTAL REFS\n
 S=
add remaining nodes to tree
.*
has_sec_transition
__completion
[VMUGetSetOfNSSliceNames() containsObject:ivarName]
SAMPLING_TOOLS_ALL_PROCESSES
    %s %5d %s\n
didPhysFootprintDirtyAccounting
srcAddressToExtraAutoreleaseCountDict
Swift.
memgraph refinement - remove lower-priority references
NonstrongSelfRefToLeak
CFType
x14
x20
[Dead Nodes Marking Map] Count: %u\n\n
StartRoutineOffsetKey
swift_reflection_asyncTaskSlabAllocations unavailable on bridgeOS
DT_NO_SCAN_OVERLAY
-[VMUProcessObjectGraphRefiner _findInterestingClassInfos]_block_invoke
BadRefFromSwiftMetadata
SurfaceID: %#x  %llux%llu (%s) %s
%@ pid %u [%s]
%#llx --> %llu  STRING_LENGTH CACHE MISS OF %s\n
.peer.0x
Physical footprint (peak)
sendRights
content length %ld  %s in VM:  %@
 %*s
unloaded kmod %llu
[%.*s]
-[%@ %s]: %s
:
 as '
ALLOCATED
recordRegions
_objc_indexed_classes_count
MallocHelperZone_0x
WTF::tryFastCompactRealloc
swift_reflection_ownsAddress
elements
bplist0
1@\"`
SWIFT_BUILTIN
no associated pthread
failed to read content - bad data length %llu causes range overflow
0
region
You have access to multiple processes that match the partial name %s:\n
lr
warning: zone fixup failed - block %#llx from zone \"%s\" discovered in region [%#llx-%#llx] already claimed by \"%s\"\n
\n\nIf after processing this memgraph with other cli tools you still see non-symbolicated addresses for some binary images, please file a Radar to 'Symbolication | Xcode' and attach the memgraph and the non-symbolicated output of interest.
v32@?0@\"NSTextCheckingResult\"8Q16^B24
NSLocale
-[VMUSimpleSerializer serializeNullTerminatedBytes:]
pthread_rwlock_t
Swift.__
ADMIN_REGION  PTR_REGION
VM_KERN_COUNT_WIRED_BOOT
__NSConcreteWeakBlockVariable
CGFloat
Activity Monitor
NSData
Thread_
serial
hottestElided
failed to resolve canonical path for %s in dyld shared cache.
%llu   
NUL
%d: %d -> %d%s\n
__AUTH_CONST __objc_
commpage
__CFNotification
___kCFBooleanFalse
length: %lu  \"%@\"
 %@
binarySectionNameRanges
JSC::
NSDragDestination
_delegate
queue
purgeable_nonvolatile_compressed
^{IOUserServer_IVars}
[fh offsetInFile] == supplementalHeaderOffset
v24@?0^Q8Q16
$1: malloc[$2]
error in %@ <classes> pattern '%@' - no starting bracket [: %s
buf
%@  %@
owned unmapped
 %10s
Cannot answer isLittleEndian for cpuType is %d cpuSubtype is %d
  (in 
allProcessesMode
markStacks
_BaseClass
_protocol
%-36s  %-60s  %s\n
VMUCallTreeRoot
SCAN_VM_REGIONS_WITH_UNKNOWN_PATHS
swift_reflection_typeRefForMangledTypeName
ALLOCATION
has-length-byte
x19
remoteMethods
_Class
__DATA_DIRTY __objc_
, Roots Present
Object
B32@?0Q8@\"VMUTaskMemoryCache\"16^Q24
%@%@\n
%@----\n
SYMBOLICATION_LABELS_FOR_ALL_OSXPCOBJECTS
kextd
slice
_window
reverse
VMUSimpleSerializer.mm
VM_KERN_COUNT_BOOT_STOLEN
__CFRuntimeEnumerateClassTable
pthreadOffsets
std::enable_if
_secondItem
VM_KERN_COUNT_WIRED_MANAGED
libsystem_malloc.dylib
DT_PRECISELY_SCAN_SWIFT_SINGLE_PAYLOAD_ENUMS
unsigned char
3!`
-[VMUDirectedGraph _adjustAdjacencyMap]
swift_reflection_asyncTaskSlabPointer
OS_xpc_session
Found SWIFT_UNKNOWN field \"%s\" (type %s) in class %s\n
At end of VM region
VM_KERN_MEMORY_ANY
_connection
bt_library
VM: %@ fragmentation
__DATA __objc
<VMUArchitecture: %p> 0x%x,0x%x %@ - %@
v24@?0@\"NSString\"8^@16
__NSObserver
%s RECURSION %u, LEVEL %u
Class (objc_class)
OS_xpc_fd
StrongSelfRefToLeak
Class.data.protocols (protocol_array_t)
        not counted in TOTAL below
__ZL22future_named_class_map
<unknown connection>
Unable to suspend target task: %s (%d)\n
I24@?0Q8I16B20
[25i]
=
retainCount
shared memory
VM_KERN_MEMORY_KALLOC_SHARED
parentPageOffset
x9
IOLockAlloc
keys
%@: %.128s...   SHA256: %@
-[VMUSimpleDeserializer copyDeserializedNullTerminatedBytesWithError:]
_removeEntryFromMarkingRegion_block_invoke
 Guard
graphics
 --> %@
Block %p [%llu] is %s\n
Process %d: %u leak%s for %llu total leaked bytes.\n
_weakReference
$1
amfi_interface_query_bootarg_state
launchd.development
invocation function 
operator 
(0x[a-fA-F0-9]*)\\s*-\\s*(0x[a-fA-F0-9]*)\\s*(\\S*)\\s*\\(([0-9\\- \\.\\?]*)\\)\\s*<(\\S{36})>\\s*(.*)
VMUOptionParserDomain
icu::UVector32
/System/
libsystem_kernel.dylib
thread_suspend2
CFArray
'
ledger
%s+ %llu
__DATA 
introspect structure %s for the malloc zone has no enumerator function in %s
unordered_map
objectRefsListEntryNext
NSTimer
v32@?0@\"NSString\"8@16^B24
VM_KERN_MEMORY_HV
watchOS Simulator
%c)
/(Core(Text|UI|Graphics|Video|Image|Media(IOServices)?|PDF)|ATS|ColorSync|ImageIO|Metal(Kit)?|OpenGL|Quartz(Core)?|QTKit|VideoToolbox|OpenCL|QD|IOSurface)\\.framework|/libswiftCore(Graphics|Image).dylib
Zone %s\n
_dispatch_calloc
nonUTF8-binary-path
Time to initialize sampling context:  %0.2f
swift_reflection_infoForInstance
__NSFrozenOrderedSetM
GUARD
VM_KERN_MEMORY_OSFMK
SInt32
 [no process]
x6
---
swift_reflection_copyDemangledNameForTypeRef
icu::DecimalFormat
elem_size
__NSArray0
.internalProps
RefFromNamedIvarToObjectInterior
%@  %@  %@
malloc_zone_realloc
error in %@ <classes> pattern '%@' - cannot match the start of a class name
    Old region name was %s\n
[Stack Log Reader - VM Region Tracker] Region count: %u\n\n
[Full Stack Log History] dataOffset: %llu  dataSize: %llu  %s\n\n
Decompressed %s to %s (reversed %2.1f%% reduction) in %3.6fs\n
__NSCFDictionary
libgmalloc.B.dylib
VM_KERN_COUNT_LOPAGE
%@  Connection: %@
[Function Name Ranges] Count: %u  Uniqued string count: %u\n\n
char*
RefFromNoSymbolGlobalVariableToAlignedInterior
 [group up]
xpc_data_t
[__block capture]
Protocol: <couldn't read name>
archiving userMarked
strong
VMUScanTypeExactUnowned
%-*llx
Instances: %lu   Bytes: %lu   %@
buildReferenceTree
NSMutableOrderedSet
xpc_uint64_t
SwiftNativeNSObject
VM_KERN_MEMORY_NONE
Class[]
%.0fK
/usr/lib/
error: core's page size doesn't match the host system (%u KB vs %u KB), cannot continue\n
LaunchServices
DisplayName
CNODE
VM_KERN_MEMORY_LIBKERN
VM_KERN_MEMORY_IPC
VM_KERN_MEMORY_MTAG
VM_KERN_MEMORY_FIRST_DYNAMIC
_objc_debug_indexed_isa_index_mask
K
v52@?0I8{?=Qb60b4@}12@\"VMUVMRegion\"36^B44
Class.data.properties.lists (property_list_t)
exclave
Target process is an ancestor and permitting live process for ancestors so not generating a corpse to save resources by default.\n
%lu
^Q
std::
os_transaction_t
No-Change
%#llx[%llu] --> %p[%llu]  READ_BYTES CACHE HIT\n
pdf_named_malloc
Gigacage::mallocArray
: 0x
Class.methodCache._buckets (bucket_t)
C
@selector(%@)
::
The DT_REPORT_IOKIT_REGION_LEAKS env var is set so leaked IOKit, IOSurface, or IOAccelerator regions will be reported, if -vmalso is passed to 'leaks'\n
__NSFrozenArrayM
v20@?0I8@\"NSString\"12
RefFromNotificationCenter
Swift
-[VMUGraphStackLogReader populateBacktraceUniquingTableWithStackLogs:]_block_invoke
[Region Symbol Name Ranges] Count: %u  Uniqued string count: %u\n\n
Duplicates total size
swift_allocObject
OS_xpc_double
media
WebKit Owned
v28@?0I8Q12@\"VMURuntimeMetadataChunkInfo\"20
__CFSafelyReallocateWithAllocator
Symbolication: could not read object label handler plist from %@
 [group contain]
Memgraph is corrupt due to malloc zone enumeration failure. The malloc heap of the target process was in an inconsistent state such as when being modified.
q24@?0@\"NSString\"8@\"NSString\"16
%02x
unrecognized option '%s'
VMUProcessObjectGraphRefiner
Time spent sampling with CFI:  %0.4f
VM_KERN_MEMORY_KALLOC
1.2.12
PPC-64
OS_os_log
task_start_peeking
missing ivar at index: %d in class: %@
_swift_debug_sideTablePointerMask
PGZ
children
DefaultMallocZone_0x
v32@?0@\"VMUFieldInfo\"8Q16^B24
c
libgmalloc.dylib
ownedPhysFootprintAdjustmentForMemgraph
[Backtrace Uniquing Table] %llu node capacity  %u nodes full  %llu bytes\n\n
uchar[]
/System/Library/Extensions
AsyncTask
dispatch_mach_msg_t
*[]
void
rawValue
x13
 R=
remove junk edges from object graph
Q16@?0^v8
GMmalloc
[fatal] %s\n
___kCFBooleanTrue
archiving node labels
 in %@
Getting fields for class %s\n
VM_KERN_MEMORY_%lld
SInt64
os_transaction_get_description
_.([@
RefFromCaptureToUnalignedInterior
SWAPPED
zone
__NSGlobalBlock__
background
binary
File does not contain a memory graph in the correct format
Unable to create secure temp file\n
taskStackLogReader
 OBJECTID
\n%s%s\n
Out of memory: failed to expand %s from %u to %u entries
Swift weak reference storage
VM_KERN_COUNT_MAP_KERNEL_DATA
Peak physical footprint was %.2f times higher than current -- past memory use was much higher. This can be analyzed with the Allocations instrument
Binary Images:
bug_type
Total allocations size
__TEXT __info_plist
NSMutableSet
Data parameter cannot be nil.
swift_reflection_childOfMetadata
<< TOTAL >>
Memory graph was not recorded with -fullContent so no transaction descriptions are available
[%#qx to %#qx] (length: %qd)\n
sepOS
*** task_malloc_get_all_zones: target has no active zones\n
WebKit Malloc
*
%s ELIDED %u LEVELS OF RECURSION THROUGH %s
metaclass for %@
VM_KERN_MEMORY_PHANTOM_CACHE
libclosure.dylib
/libclang_rt.tsan
ulong[]
_viewController
class_createInstance
{shared_ptr<
START 
nodeNamespaceSize
class
malloc size pattern '%@' was not of expected format '[size]' or '[lowerSizeBound-upperSizeBound]'
list
Thread_%x
Failed to get info for metadata of class %s\n\n
 (%@)
Class
<no-type>
bmalloc_
%u %s OF '%s'
__IncompleteProtocol
Frozen
 [inlined]
VM_KERN_MEMORY_ZONE
%@%s%*s%s
{vector<
v12@?0I8
SYMBOLICATION_DISABLE_WEBKIT_POINTER_PACKING_WORKAROUND
\xf0Q
os_transaction_get_timestamp
<%@ %p>
gOSMetaClassBaseRemotePrivateLayout
memgraph file is malformed - unable to deserialize.
root VM region
\n
RefFromLargeNonobjectToStart
WARNING: Forcing live process analysis for a system-critical process (pid %d).\n
%-*s
<%@>
SWAP
[Object Info] Compact: %d Large: %d (%2.2f%%)\n\n
64b
0x%08x 
, 
Key
%qu unique stacks\n
Class.data.readonly (class_ro_t)
^{%@_IVars}
REFERENCES THAT WERE KEPT:\n
SWIFT_STRUCT
SIZE
NSInteger
tvOS
configd
coresymbolicationd
B16@?0@\"VMUVMRegion\"8
NSMenu
Bad field index %u in document, count is %u
Float32
--x
[Stack Log Reader - nodeToStackIndexTable] nodeNamespaceSize %u  %lu bytes\n\n
%#llx
%@-%@~%@
yyyy-MM-dd HH:mm:ss.SSS ZZZ
Ignoring 0-size and/or 0-stride field\n
_objc_class_abi_version
_objc_debug_isa_magic_mask
default.
Date/Time:       %@\nLaunch Time:     %@\nOS Version:      %@\nReport Version:  %d\n
Memory Scanning
AttributeGraph Data (old mapping)
coreservicesd
unretained
Swift Task Owned
VMULeakDetector
xpc_dictionary_t
Q16@?0r*8
 (Storage)
icu::BMPSet
\n    
CoreGraphics
JSC::tryAllocateMemory
__NSDate
classInfo.instanceSize >= tableOffset + tableSize
%sbinary plist:  %@
ReportPanic
malloc-block
__NSCFLocale
%u (%.1fM) %@
RefFromSwiftTaskOwnedFakeNode
SWIFT_WEAK_REFERENCE
ISSUE:  Region user_tag should already be set; setting to VM_MEMORY_MALLOC in %s based on enumeration range for  %s\n
libswiftRemoteMirror version or it wasn't new enough
*** task_malloc_get_all_zones: can't get target task symbolicator\n
_dispatch_continuation_alloc_from_heap
WTF::
v24@?0r*8@\"NSString\"16
_swift_reflection_libraryVersion
BinaryInfoArchitectureKey
x3
parse error with line: '%s'\n
purgeable_nonvolatile_compress
swift_bufferAllocate
Protocol
RefFromNamedIvarPlusOffsetToNonObjectInterior
EXCLAVEDRIVERKIT
parentPage
unsupported flavor %d, skipping fixup
tvOS Simulator
Thread %u  %s\n
AttributeGraph
Analysis of sampling %@ (pid %d) every %d millisecond\n
No matching kernel found.
Not creating classinfo for zero-sized AttributeGraph value\n\n
cuml_vm_dirty
Could not get node for swift metadata allocation pool
icu::UVector64
NSUUID
step 2 -- enumerate stack log records to record unique backtrace IDs for objects of interest
%@  %#llx
on dirty page  unused system shared lib __DATA
process-only VM submap
couldn't get framework name associated with the malloc zone
geo::MallocZoneAllocator::callocate(unsigned long, unsigned long)
VMUAnalysisSummaryKey
dispatch_data_t
v28@?0I8I12I16^B20
com.apple.dt.Symbolication.VMUSimpleSerializer
vmu_create_backtrace_uniquing_table_from_archive
_bits
libxpc.dylib
/usr/lib/system/libsystem_kernel.dylib
exhaustible
x4
non-object in zone 
_keys
internal_compressed
node->refcount == 0
 (MTE Enabled
NSConcreteHashTable
OS_dispatch_queue_concurrent
OS_dispatch_semaphore
libclang_rt.tsan
largest
VMUObjectIdentifier.m
<no symbol>
allMarkedAddresses
deeper
Failed to create symbolicator.
unused but dirty shlib __DATA
VM_KERN_MEMORY_REASON
sp
  RECURSION COLLAPSED
MAX
_children
Process %d: %u nodes malloced for %llu KB\n
%s kept pid %u suspended for too long - exiting to prevent watchdog timer from killing that process.
DATA_CONST
mediaplaybackd
videocodecd
showsPhysFootprint
Memory graph has bizarrely high %s count %zu\n
(<
_xpc_alloc
 SIMPLER: %s\n
VMUProcessObjectGraphRefiner.mm
v20@?0I8B12I16
_buffer
on dirty page  
__AUTH_CONST
-[VMUTaskMemoryScanner addRootNodesFromTaskWithError:]_block_invoke
sampling all threads
region->firstBlockIndexOnPageArray
PreserveMemgraphSampleAndSymbolStore
v24@?0{_CSTypeRef=QQ}8
>
Usage: %s %s\n\n
Swift._SetStorage<
x10
(ROOT LEAK|CYCLE): 0x[0-9a-f]+ \\[(.*)\\].*
location != NSNotFound
    FAILED STRUCTURE TYPE ENCODING: %s\n
DVT_
JSC::CompleteSubspace::allocatorForSlow
live task
GPU Carveout (reserved)
[%.*f seconds] %@
Code Type
couldn't get introspect structure symbol name from %s
v36@?0Q8@\"VMUClassInfo\"16I24^B28
Gigacage::tryMalloc
%+*d: <extra space>[%u] (%s)
loadSwiftReflectionLibraries
_objc_indexed_classes
<PTHREAD_T>
endOfLastPageWithAllocations - startOfFirstPageWithAllocations
.app/
Q16@?0Q8
kernPageSize
VMUScanTypeExactWeak
/System/Library/PrivateFrameworks/
OS_xpc_endpoint
libsystem_malloc%s.dylib
=====
^@\"IODispatchQueue\"
Version %llu of memory graph is not supported by the currently installed tools
v16@?0^?8
Gigacage::tryRealloc
^{NSSliceExternalPersonalityProperties}
toolName
[srcAddressToExtraAutoreleaseCountDict] Count: %lu\n\n
slab
classVersion
[@@@spacing@@@]
content length 0
%u (%.2fM) %@
 (%@:%@)
Frames
x5
<unclaimed>
__swift_debug_allocationPoolBackPointerOffset
, std::__unordered_map_hasher<
kernel
Q16@?0^{?=QQQQQQQQQQ}8
traceTreeRoot || traceListString
/tmp/%@_%@_XXXX.sample.txt
SWIFT_NO_PAYLOAD_ENUM
Error in enumerating malloc zone %@ - allocation is excessively large: %#llx-%#llx[%llu].%s\n
length: %lu  %@:  \"%@\"
v20@?0^{_VMUDirectedGraphEdge=III}8I16
x27
ARM64
Base - this should get overridden by subclasses
No malloc zones in target process\n
/(JavaVM|Ruby|Python|Tcl|Tk)\\.framework/|/ruby/|/lib(tcl|tk|python|perl|swiftCore|swiftObjectiveC|c\\+\\+abi)[^/]*\\.dylib
DISKLOGS
__OBJC 
Failed to create CSSymbolicatorRef, unable to determine cpu type for %s
*** getStackLoggingSharedMemoryAddressFromTask: couldn't find libsystem_malloc dylib in target task\n
%.*s%@\n
Submap
v36@?0I8I12I16I20I24^B28
ivars
Metadata
v24@?0@\"VMUFieldInfo\"8I16I20
_dispatch_strdup_if_mutable
llvm::safe_calloc(unsigned long, unsigned long)
+
swift_reflection_projectEnumValue
v24@?0@\"VMUVMRegion\"8^B16
%s[%d]: warning: memory marking timeout encountered - marked objects may be incorrect from this point forward\n
_os_trace_malloc
__NSOperationInternal
failed to create mapped memory cache: %s
Swift unowned reference storage
targetType
VMUMaxRange(newVMRangeForZone) == rangeStartInRegion
VM ledger tag %llu
neural_footprint_compressed
/usr/lib/swift/libswiftCore.dylib
USER
OS_xpc_string
^{NSSliceExternalAcquisitionProperties}
mutable
 ATTRIBUTES 
Out of memory: failed to expand references array from %u to %u edges
Inverted call tree:
__typed_operator_new_impl
Size
__NSDictionaryM
Hard
libclang_rt.asan
coalesceIdenticalRegions
VM_KERN_MEMORY_IOKIT
VM_KERN_COUNT_WIRED
stackList
pthread_once_t
  !! %s %s  when analyzing object instance: %#llx
<VMUProcInfo: %@ (PID %d)>
Malloc enumeration
geo::MallocZoneAllocator::allocate(unsigned long, unsigned long)
NSMutableAttributedString
collectVMpageStatistics: error in mach_vm_page_range_query: %s\n
_xpc_dictionary_get_transaction
backtraces
Unable to initialize compression stream.
metaclass
OS_xpc_data
icu::number::impl::DecimalFormatFields
[nodeToMSLPayloadTable] nodeNamespaceSize %u  %lu bytes\n\n
Memgraph file contained full stack log history header, but failed to store the actual stack log data.
   DispatchQueue_%qu: %@  (%s)
%d %c
_allocate
BuildVersion
xpc_serializer_t
_referenceItem
short[]
...%@
Backtrace Excluded
!_swiftMetadataClassInfo
SWIFT_RAW_POINTER
1A
pthread_mutexattr_t
VMUObjectLabelHandlers
nodeToMSLPayloadTable
[SourceInfo Ranges] Count: %u  Uniqued string count: %u\n\n
xpc_string_t
legacy_context
Payload-
firstEntryOffset
archiving thread / binary / regionSymbol to range mappings
32b
BigEndian
content length %ld entire VM:  %@
RefToParentAutoreleasePoolPage
_Tt
VM_KERN_MEMORY_SKYWALK
VMUGraphStackLogReader.m
VMUDirectedGraphToolCompatibilityVersionKey
dbMallocRawFinish
5!2
_refcounts
_addEntryToMarkingRegion_block_invoke
keys_ptr
long long
%9lu %9lu %9.1f   %s
%s%s%@
VM:
_superview
VM_KERN_MEMORY_COMPRESSOR
regionData
x21
{?=Qb60b4@}12@?0I8
Unique entries in autoreleasepools
!
_repObject
JS VM Reservations
targetIsDebuggable
storage_impl_ptr
-[VMUGraphStackLogReader enumerateMSLRecordsAndPayloads:]
[Binary Images List] \n\n
Reason: %@\n\n
dirty
xpc_connection_t
%#llx  FAIL! NO VM REGION FOR STRING LENGTH\n
RefFromThreadStack
v24@?0Q8I16I20
target process's footprint is too large, or system memory pressure is too high
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime pre-dating the stable ABI has been loaded
libswiftRemoteMirror.dylib
Gigacage::
vasprintf unexpectedly failed
step 3 -- from uniqueBacktraceToObjectsMap, create uniqueBacktraceToObjectsMap
com.apple.xpc.anonymous
%@=
isTranslatedByRosetta
regionDataExtra
Rosetta Runtime Routines
vmu_swift_reflection_asyncTaskSlabPointer error: %s\n
error: core's pointer size doesn't match the host system, cannot continue\n
\t
TOTAL, minus reserved VM space
MALLOC
utility
VMUScanTypeExistential
Allocations count
__DATA_CONST __objc_
caulk::alloc::darwin_resource
STACK OF 
_CFXNotificationObjcObserverRegistration
NSTextInputContext
I
x22
MetaClass
_zone
malloc in std::map<
VM_KERN_MEMORY_CPUTRACE
archiving region data
 PURGE  
Total memory of autorelease pools and content blocks
transactions exist
inline
_objc_debug_isa_magic_value
deadNodes
Call tree:
_lowGlo
bmalloc_allocate...
%#llx %@
_objc_debug_taggedpointer_mask
short
i24@?0^v8Q16
Compressed %s to %s (%2.1f%% reduction) in %3.6fs\n
the provided call tree file %s contains non-UTF8 data\n
double[]
WTF::tryFastMalloc
swift_reflection_dumpInfoForInstance
RefFromNamedIvarToUnalignedInterior
alloc_size
com.apple.CF
<%@ %#llx> [%llu]
key_field
default
%*llx
pid_for_task(%x) failed with error %d: %s
                
-w-
VMUTask initialization
Symbolication_Internal_ForSwift.VMUAttributeGraphRegionIdentifier
initMemoryScanner
__NSTaggedDate
populateUniquingTable convert VM region tracker's from old to new stackIDs
Thread
Failed to create VMUProcInfo for pid: %d
%#llx[%llu] --> %p[%llu]  READ_BYTES CACHE MISS (UNVALIDATED)\n
__VMUAssociatedObjectsObjcAbandonedMarkerKey
Gigacage::malloc
\nApple-internal options:\n
__NSCFConstantString
symbolLocation
^(.+) with unmangled suffix (.+)
VM_KERN_MEMORY_MBUF
_objc_debug_isa_class_mask
[VM Region list string content] \n\n
)
controlView
VM_KERN_MEMORY_KALLOC_TYPE
Thread_%u
[Exclave Flag Data] Count: %u\n\n
phys_footprint
bool[]
__DATA __objc_
zalloc (no zone)
-
Ozone
[%@:%@]
processGraphInfo
 (in %s)
VMUEnumeratorValidation
VM: unknown region type
SWIFT_TUPLE
markOthers
x25
     ** %u:  
s
ARM
VM_KERN_MEMORY_COUNT
non-inline
Fig Subclass
Symbolication.framework _get_symbol_owner did not find requested symbol %s\n
v24@?0Q8^B16
@\"NSMutableDictionary\"64@?0I8Q12Q20i28@\"VMUClassInfo\"32@\"VMUVMRegion\"40Q48@\"NSArray\"56
corpse creation encountered the unexpected error %s (%d)
diagnosticd
%qu
^
%@ (translated)
VMUVMRegionIdentifier.m
childPage
cuml_malloc_bytes
objectGraphInfo
DUPLICATE OBJECTS
NSDate
OS_xpc_int64
_mmap
_firstRealizedClass
[Thread Name Ranges] Count: %u  Uniqued string count: %u\n\n
loaded %s for %@ introspection\n
*16@?0Q8
basic_string
CMMMemMgr::New(unsigned long)
ORIGINAL: %s\n
unable to inspect heap ranges of target process; it may be using a malloc replacement library without the required support
%@ -- failed to read content due to memory allocation failure - is length reasonable?
fwrite
 Other
overrides
llvm::BumpPtrAllocatorImpl
\n%u leak%s excluded (not printed)\n
VM_KERN_MEMORY_CPU
_SwiftValue
[Thread Names For Thread Ports] Count: %u  Uniqued string count: %u\n\n
regionSymbolNameRanges
VMUAnalysisDataKey
\\((.+) in _([0-9A-Z]+)\\)
%s[%d]: error: memory marking region could not be allocated\n
PTR_IN_USE
%@  QOS %s
[Stack Log Reader - nodeToMSLPayloadTable] nodeNamespaceSize %u  %lu bytes\n\n
[Stack Log Reader - SourceInfo Ranges] Count: %u  Uniqued string count: %u\n\n
Error. Compression failed.
%s\n\n
sipDisabled
2
[fh offsetInFile] == supplementalDataOffset
   COALESCED AUTORELEASES: %u
WTF::fastCompactZeroedMalloc
====\n
/usr
char[]
unmapped
build tree from selected nodes
OS_dispatch_queue
B16@?0@?<B@?Q@\"VMUTaskMemoryCache\"^Q>8
EMPTY
STACK: 
  %@
fixupCoreRegions
 zone structure
/Contents/Resources/DWARF/
Build Info:      %@\n
NSView
.acquisitionProps
.personalityProps
SWIFT_CLASS_EXISTENTIAL
dominators
error in % <region-description> pattern '%@': %s
OS_xpc_dictionary (Storage)
RefFromNamedIvarPlusOffsetToObject
LONG-LIVED XPC TRANSACTIONS
ARC
__strong
introspect structure %s for the malloc zone has invalid enumerator function address %#llx in %s
{_NSRange=
alloc_typed
%10llu  TOTAL GOOD REFS\n
%@-%@
(address & (1ull << 63)) == 0
Setting region name in %s based on _zoneNames[_blocks[i].isa_index for  %s\n
v24@?0@\"VMUClassInfo\"8I16I20
?
seed
/usr/lib/system/libsystem_blocks.dylib
marking malloc VM regions
Next enumeration range not contiguous with current
archiving nodeToStackIDTable
nonsensically small offset for field \"%s\" of +%u%s; ignoring all fields in this closure context\n
char
maxTimestampDelta
\x81a
VMUHeapAndVMAggregator
__ZL21InitialAllocationPool
 not
_children.singleChildKey
isa
UserEventAgent
watchdogd
ZER
$1: <$2>
error in malloc size pattern '%@':  if upper bound of size is given, it must be %llu or more
__NSConcreteUUID
OS_xpc_connection
Failed to look up metadata for class %s\n\n
com.apple.dt.memorytools
entryIndex < region->entry_capacity
  type %s
========
x2
invalid task corpse info provided to VMUProcessLedger
-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke_3
zone_security_array
, std::allocator<
__NSCFOutputStream
VMUSimpleSerializer
Error setting sysctl: %s. %d.\n
Setting region name in %s based on malloc zone structure address for  %s\n
 %*s %*s %*s
/System
  load address 
<unknown-symbol> %#qx + %qu
_$sBb
_objc
Carousel
ReportCrashService
Destructive mutation attempted while traversing graph!
C16@?0I8C12
swift_allocError
VMUAnalysisWarningKey
v24@?0Q8Q16
Unable to retrieve ledger template info in VMUProcessLedger
vmu_remove_stack_from_backtrace_uniquing_table
llvm::DenseMap<TypeNameCacheKey, std::pair<const char *, size_t>>
OS_dispatch_mach_msg
RefFromUnalignedSourceToUnalignedInterior
v24@?0*8@\"VMUVMRegion\"16
framePtrs
securityd
q24@?0@\"NSNumber\"8@\"NSNumber\"16
node
XAtomicAllocator::reserve(int)
_os_trace_zalloc
unused  unknown system shared lib __TEXT
dyld shared cache combined __LINKEDIT
(kernel)
VMUMallocZoneAggregate.m
-[VMUClassInfoMap _applyTypeOverlay:]
id[]
Failed to map remote region: [%#llx-%#llx] %s %s (%llu %s)%s (error: %s)\n
v32@?0@\"NSNumber\"8@\"VMUProcInfo\"16^B24
commpage (reserved)
VIRTUAL
_objc_debug_taggedpointer_obfuscator
ARM LR
zoneNames
malloc<%s>
SWIFT_UNMANAGED_REFERENCE
VM_KERN_MEMORY_STACK
VM_KERN_MEMORY_FILE
Task stack
%@ %s%@
[Reference Details Large] Compact: %d Large: %d (%2.2f%%)\n\n
\xb1
com.apple.CFNetwork
============
remoteQueues
metaClassPrivate
COW
%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s) } }\n
_otherBits
No leaks detected
libdyld.dylib
%@ / %@
libswiftCore.dylib
%@  %@  %#qx%@
regions
getting node labels
threadAndDispatchQueueName
element
EASM_CNODE
__swift_concurrency_debug_asyncTaskSlabMetadata
   %s\n
        %lu       %@\n
_swift_debug_nativeWeakReferencePointerIsSideTable
VMUClassInfoMap.mm
key
Main Thread
JS VM Isolated Heap
%*s'%@'%s%s%s [%@] - %s, %s%s {
type %s  value: %@
VMUScanTypeNone
dbReallocFinish
%s\n
icu::UnicodeSet
OS_xpc_uuid
OS_object
_objc_debug_original_metaclass_map
mdworker
stackLogReader
ARM Simple
visionOS Simulator
/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector
iokit_mapped
graphics_footprint_compressed
className
Unable to unarchive `referenceDetailsLarge`.
SYMBOLICATION_DEBUG_SWIFT_ASYNC
v24@?0I8i12@?<v@?^v>16
REFERENCES THAT WERE REMOVED:\n
childOfMetadata()
%#llx is not in any region.  
machTime
uint32_t
_noteBlocksInRegion
zone: %s
thread_resume2
{unordered_map<
remove junk nodes from object graph
VMUDestructiveMutationWhileEnumeratingException
    =====     =====   =======   =======
identifying root regions
Binary images description not available\n\n
_menu
@\"VMUMutableFieldInfo\"8@?0
content length %ld at offset %llu in VM:  %@
Object_id=
%@  purgableVolatile: %s
_instrumented_or_legacy
Leak
  FICTITIOUS
String
v28@?0I8I12^{?=QQ}16I24
xpc_double_t
<<couldn't convert to UTF8>>
  CS_TAINTED
/usr/lib/libboringssl.dylib
audiomxd
TERM
No object labels had %lu duplicates.
addChildCountsIntoNode
VMUTaskMemoryScanner.m
%sUNUSED SPACE AT START\n
flags
x16
ProductBuildVersion
ReadOnly portion of Libraries: Total=%s resident=%s(%.0f%%) swapped_out_or_unallocated=%s(%.0f%%)\n
couldn't find libsystem_malloc dylib in target task
%@  %@:%u
Malloc enumeration of zone \"%@\" failed to get full information about malloc metadata and/or allocations with the error \"%s (%d)\". It is likely that the target was suspended while malloc metadata was being modified.
_swiftTaskAllocationBlockIndexes
ProjectName
swift_reflection_childOfInstance
%u (%.1fK) %@
RefFromNamedGlobalVariable
 + %u
VM_KERN_COUNT_MAP_KALLOC
WTF::tryFastCalloc
error in malloc size pattern '%@':  size must be %llu or more
__TEXT
_supermenu
%u
symbol name not found
powerd
binaryImagesDescription
struct
zone_array
Field is single-payload enum containing a pointer (with a nil representation of NULL). Treating as a struct and not varianting.\n
unused __DATA
DIRTY
VM_KERN_MEMORY_RECOUNT
[Binary Section Name Ranges] Count: %u  Uniqued string count: %u\n\n
couldn't create symbolicator for %s
graphIs64bit
FirstTLSslotKey
  no associated pthread
%@%@ --> %@
INSTANCES
SYMBOLICATION_NO_SWIFT_REMOTE_MIRROR
spindump_agent
/System/Library/(Private)?Frameworks/[^/]*\\.framework/
STACK LOGS FAILED TO SAVE
building call tree from references
llvm::safe_realloc(void*, unsigned long)
^{NSSliceInternalProperties}
!_swiftTaskOwnedClassInfo
unknown-process
Q
*** Symbolication:  Can't read zone 0x%qx (error %@)\n
%g
UNKNOWN
Thread Sanitizer
%s[%d]: notice: memory marking disabled due to presence of NSZombieEnabled=\"%s\" environment variable\n
VMUGraphStackLogReader
v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24
v32@?0@\"VMUAnalyzerSummaryField\"8Q16^B24
error in %@ <classes> pattern '%@': %s
: 
Weak references in Swift content may be misidentified as retaining references.
vtable for 
v16@?0@?<@\"CSMemoryMappingSlice\"@?QQ>8
rw-
__NSCFInputStream
_rawValue
%#llx[%llu] --> %p[%llu] in %s  READ_BYTES CACHE MISS (VALIDATED)  -------------\n
compactEdgeList
WTF::fastCompactStrDup
*** getStackLoggingSharedMemoryAddressFromTask: couldn't find ___mach_stack_logging_shared_memory_address in target task\n
==== REMOVED %llu JUNK EDGES OUT OF %llu  (%2.2f%%) ====\n
OSObj
___CFRuntimeClassTableCount
%.1fT
%@ (in %@)
1
enum payload  %s  scanType %s (may be changed), of field %s, of object at %p of class %s  size %u stride %u\n
%#llx FAIL! STRING_LENGTH COULD NOT MAP, ALTHOUGH FOUND REGION %s\n
int
archiving VMUObjectGraph and VMUDirectedGraph
<deduplicated_symbol>
populateUniquingTable get backtraces from libmalloc into our backtrace uniquing table
x23
\n%@
VMUMemoryMarking.m
%lld bytes into %@
^{OSMetaClassPrivate}
DT_PRINT_NAME_SIMPLIFICATION
Hardware Model:  %@\n
v28@?0Q8@\"NSObject<OS_dispatch_mach_msg>\"16i24
RefFromNamedGlobalVariableToAlignedInterior
machine-wide VM submap
VM_KERN_COUNT_RESERVED
-[VMUObjectIdentifier setupIsaTranslator]
fp
NONVOL
preparing to enumerate %@\n
uint64_t[]
SourceVersion
swift_reflection_typeRefForInstance
/S/L/F/
/S/L/
sqlite3MemRealloc
WTF::tryFastCompactZeroedMalloc
swift_reflection_metadataForObject
OS_xpc_
content length %ld  %s + %llu in VM:  %@
kern.wq_max_constrained_threads
regionDataSerializer
RSDNT
VMUArchitecture unhandled cpuType
vector
some
_objc_debug_autoreleasepoolpage_ptr_mask
 %@PURGE=%c
/usr/lib/((lib[^/]*\\.dylib)|dyld|system)|/libswift(Darwin|Dispatch).dylib
VMUObjectGraph.m
@
pattern
com.apple.Symbolication
_objc_debug_autoreleasepoolpage_child_offset
ExclaveCore
dyldSharedCacheBase
/u/l/s/
path
SWIFT_MULTI_PAYLOAD_ENUM
%4d
pthread_t structure %+4lld
 =  
base
free
libsystem_trace.dylib
unowned
i32@?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16@\"NSString\"24
__1::
__NSSetM
VMUTaskMemoryCache
r--
WTF::fastCompactMemDup
storage
%+6lld: %s%s
TOTAL FOR STACK
Swift Metadata
WTF::fastCompactAlignedMalloc
: %@
unknown type
x24
%.1fM
_blocks
chunk
%#llx-%#llx[%llu]
Platform:        %@\n
target process may be using too much VM
threadNamesForThreadPorts
_malloc_zones
REGION DETAIL
_guts
Failure calling sysctl to get process list buffer size
Version
non-root VM region
swift_allocEmptyBox
RefFromNonrootVMRegion
  scanType %s
reserved VM address space (unallocated)
RefFromAttributeGraphFakeNode
NSBlock
mslRecordsCount
NSNotification
OS_xpc_array
SWIFT_THICK_FUNCTION
graphEdgeCount
LaunchCFMApp
queueArray
meta
GMrealloc
swift_reflection_createReflectionContextWithDataLayout
yyyy-MM-dd HH:mm:ss Z
Kernel
%u %c
Total entries in autoreleasepools
RefWithNoPriority
Malloc zone count is %u but zoneIndex is %u for %@\n
VM_KERN_MEMORY_BSD
__NSConcreteGlobalBlock
libswift_Concurrency
processDescriptionString
i24@?0r^v8r^v16
Unable to resume target task: %s (%d)\n
Closure context
NSURL
: VM: 
printLeakTree
___CFRuntimeClassTable
Unicode
i
v28@?0@\"VMUFieldInfo\"8@\"VMUFieldInfo\"16I24
OS_xpc_pointer
v20@?0@\"VMUMutableFieldInfo\"8I16
 Aborting
_table_addStorageBlock
 (Roots Present)
info
 (empty)
os_transaction_get_ra
archiving nodeToTimestampTable
BlockVariable
x26
_CFXNotificationRegistrationBase
%p + %llu
allProcesses
%sGAP OF %#llx BYTES\n
Error in enumerating malloc zone %@ - allocation is not in a VM region: %@ %s\n
%p
archivedClassInfos
(VMUBacktraceUniquing) expandUniquingTable(): VMCopyFailed
std::__
RefFromKernelIntoUserSpace
Class: 
Unable to read __DATA __objc_imageinfo from %s\n
asyncFrames
[Class Layouts] Class info count: %d\n\n
SHADOW_CNODE
%@\n
__NSOrderedSetM
fopen
VMUClassInfo.mm
childOfTypeRef()
targetIsTranslated
hottestElided: %u  coldestElided: %u  depth: %u  %#llx
charged to process physical footprint
v32@?0Q8@\"VMUClassInfo\"16^B24
Failed to map remote region at [%#llx-%#llx]\n
version
step 4 -- build call tree by iterating the uniqueBacktraceToObjectsMap
Firmware
 %llu
struct OSClassScan
_firstItem
FRAG SIZE
DT_PRINT_FIG_SUBCLASSES
Leaks total size
%#*llx (%-*s) %@
__NSCFData
RefFromUnusedBinaryImage
SelfRefToNonLeak
unnamed_zone_0x%qx
internalized node
VM_KERN_MEMORY_KALLOC_DATA
Catalyst
SYMBOLICATION_EXCLAVES_INTROSPECTOR_FRAMEWORK_PATH
~mobile/
VM: %@ (in %@)
_internalEdge
Could not read swift metadata block back pointer
%#llx (in %s)
ulong
StartAddress
Failed to get DYLD info for %@ with error %s (%d). Assuming it's a minimal corpse which can't be analyzed, which we sometimes see for processes which use a lot of memory.
v32@?0*8@\"VMUVMRegion\"16@\"VMUVMRegion\"24
classMapVersion
0K
[srcAddressToExtraAutoreleaseCountDict] Count: %u\n\n
Thread %llu  %@
VMUKernelCoreMemoryScanner.m
WTF::fastAlignedMalloc
%@ (%@)
/usr/lib
sourceLine
/libclang_rt.asan
malloc
WTF::tryFastZeroedMalloc
bmpSet
RefFromNamedIvarToNonObject
PTR_REGION
media_footprint_compressed
VMUVMRegion.m
JSC::LocalAllocator::allocateSlowCase
_submenu
unused __
 %s
_objc_debug_tag60_permutations
populateUniquingTable read stack log records
select all dominator roots as roots of the tree
swift_reflection_asyncTaskSlabAllocations
NSLayoutAnchor
%#llx[%llu] FAIL! READ_BYTES (UNVALIDATED) COULD NOT MAP\n
Thread_%qu
SYMBOLICATION_LOG_SWIFT_UNKNOWN_FIELDS
Argument num %d utf8 null: %s\n
SYMBOLICATION_DISABLE_FALSE_TASK_LEAKS_WORKAROUND
%@.%@ (%@)
%08X
swift_reflection_destroyReflectionContext
*** getStackLoggingSharedMemoryAddressFromTask: can't get target task symbolicator\n
, std::equal_to<
%s: %s\n\n
Payload-Empty
Weak 
   
VM_KERN_MEMORY_LOG
i32@?0*8Q16Q24
[Thread Name For Thread Ports] Count: %u  Uniqued string count: %u\n\n
qb
Malformed non-compressed header
%9lu %9lu %9.1f   %@
Nothing to symbolicate. All addresses in the memgraph are already symbolicated.
%@ -- failed to read content due to insufficient buffer length
! 
concurrent
 [root]
processSnapshotGraph
CYCLE BACK TO 
os_security_config_get_for_task
%u (%.0fK) %@
_swift_debug_sideTablePointerRightShift
NSZombieEnabled
STACK
r-x
VMUProcessDescription is examining:\n   process: %@  pid: %d  path: %@  _binaryImages count: %zu\n   parent process: %@  pid: %d  path: %@\n
OS_xpc_dictionary
subfield
tagged_nofootprint
%.1fG
^block parameter must be non-nil.
Found first slab at %p,%s in same block\n
llvm::safe_malloc(unsigned long)
_children.elements
kern.wq_max_threads
no corpse slots are available
COUNT
VM_KERN_MEMORY_EXCLAVES_SHARED
collectable_bytes
/
X86-64
NSWeakObjectValue
mach_vm_tag_describe
  DIRTY
pthread_cond_t
launchd
sysdiagnose
swift_reflection_addImage
stringID < _stringRegCapacity
targetMSLStatus
-[VMUGraphStackLogReader copyOriginalUniquingTable:]
iOS Simulator
couldn't find introspect structure symbol %s in %s
firstDominates
-[VMUDirectedGraph _dfsCore:colors:visitBlock:examineBlock:]
NSDictionary
__
%s%@
-[VMUGraphStackLogReader populateBacktraceUniquingTableWithStackLogs:]
tagged_nofootprint_compressed
 END
Memory graph is too large to open
uniqued_stack < MAX_UNIQUING_TABLE_NODES
Class.data (class_rw_t)
RefFromWebKitOwnedFakeNode
mach_memory_info_redacted
mapped
label: %.*s
([fh offsetInFile] % 16) == 0
%s %#llx-%#llx[%llu]\n
NSActionCell
v16@?0@\"NSObject<OS_xpc_object>\"8
_variantForNSSlice
+%llu bytes
    UNION TYPE ENCODING: %s\n
bitfield:
Exctracting labels
Failed to read symbol data from the dSYM: '%@'.
mapped file
_swift_concurrency
WTF::fastCompactCalloc
OS_dispatch_source
        %@
VMUSymbolStore failed to sparsify some of resymbolicated symbol owners.\n
%-*s %#*llx %@
--
Kernel generated only a minimal corpse with error %s (%d) - examining live process instead
backtraceUniquingTableContents
[Stack Log Reader - backtraceUniquingTableContents] %llu bytes\n\n
length
\t[%3d] %#08.8qx  {%s.%s + %#qx} %s\n
AttributeGraph Owned
Failed to get udata pointers for core file.
@autoreleasepool content
Class.data.extended (class_rw_ext_t)
Failed to get addressing mask for %@ core file.
 (reserved)
VM_KERN_MEMORY_PMAP
_objc_debug_autoreleasepoolpage_parent_offset
sqlite3MemMalloc
%d
xpc_endpoint_t
_modelObserver
B16@?0@?<B@?Q@\"VMUTaskMemoryScanner\"@\"VMUTaskMemoryCache\">8
v16@?0^{__CFRuntimeClass=q*^?^?^?^?^?^?^?^?^?Q}8
__block [capture]
<unknown register index %u>
strdup
__NSCFAttributedString
 __objc_imageinfo
long
_0x
x0
/CoreData\\.framework/|/libsql[^/]*\\.dylib|/libswiftCoreData.dylib
  context %#llx
___CFPasteboardReservedBase
YES
xpc_pointer_t
SYMBOLICATION_LOG_ZONE_INTROSPECTION_LOOKUP
/usr/lib/liboah.dylib
purgeable_nonvolatile
SEL[]
<unnamed %s>
No matching libraries found in this memgraph
/System/Library/
-[VMUObjectGraph archiveDictionaryRepresentation:options:]
vmu_stack_frames_for_uniqued_stack
swift_allocBox
OS_xpc_uint64
___mach_stack_logging_shared_memory_address
\\n
!_autoreleasepoolContentClassInfo
Exited process
VMUScanTypeExactStrong
x15
non-object
Region
/usr/lib/swift/libswiftRemoteMirror.dylib
OS_xpc_serializer
0123456789ABCDEF
REGION TYPE
marking malloc allocations in VM regions
___CFRuntimeClassTables
_os_trace_calloc
RefFromLargeNoncollectionObjectToAlignedInterior
vm.get_owned_vmobjects
_objc_debug_indexed_isa_magic_value
[VM Regions] Count: %u\n\n
zone %s - using analysis tool's' %s to look for zone introspect struct for target process's %s\n
reserved
malloc_bytes
Could not get current swift metadata allocation pool
%s (in %s)
Target process is using %s so not generating corpse for better performance.\n
error %@ reading num_zones at %qx
0x%qx
%ld
id?
Autorelease pool pages not associated with a thread\n
__NSMS1
NSMutableDictionary
NSCellAuxiliary
^@
JSC::IsoMemoryAllocatorBase::tryAllocateAlignedMemory
identifier
\"%@\" (from %s)
originalUniquingTableContents
*** Symbolication:  Can't read pointers from zone %@ (error %d)\n
atomic 
No autorelease pools
reallocf
B8@?0
Exclave memory tag %hhu
VMUProcessObjectGraph
swift::swift_slowAllocTyped
VM: %@
AppKit
v16@?0@8
Metaclass.data (metaclass_rw_v2_t)
SWIFT_UNOWNED_REFERENCE
Which process? (letter or PID) 
Error. Compression output buffer full.
-[VMUTaskMemoryScanner _initializeRegionMallocBlockCounts]
WTF::tryFastCompactAlignedMalloc
NSMenuItem
%s analysis of pid %u reached time limit of %llu seconds, exiting.
coldestElided
/usr/lib/system/
libswift_Concurrency.dylib
_ptov_table
v44@?0I8{_CSNotificationData={_CSTypeRef=QQ}(?={Ping=I}{DyldLoad={_CSTypeRef=QQ}}{DyldUnload={_CSTypeRef=QQ}})}12
higher
Sort by top of stack, same collapsed (when >= 5):\n
%*s}
__NSConcreteStackBlock
Symbolication.framework _get_symbol_owner found requested symbol %s in unexpected Swift library %s\n
???
!_autoreleasepoolBoundaryClassInfo
/usr/lib/libSystem.B.dylib
markMallocAreas_block_invoke
logd
/S/L/PF/
edges
Found no VM regions in target process
Bytes after previous region: %llu  
======
NSIndexPath
unexpected configuration. leaks is expected to either run with library validation or to be debuggable
%-*s %@-%@ [%@] %s/%s SM=%s%@%@%@  %@
v16@?0I8I12
VMUSymbolStore failed to create the symbolicator from signature.\n
v32@?0@\"NSNumber\"8@\"NSArray\"16^B24
Detected no-payload of field %s, of object at %p of class %s. Treating as a non-payload case and not scanning the subfield.\n
BadRefToCollectionClassStorage
%@ + %llu
/(CFNetwork|IO)\\.framework/
Unable to unarchive `referenceDetails`.
Gigacage::tryAllocateZeroedVirtualPages
__NSArrayI_Transfer
_swift_debug_nativeWeakReferenceMarkerValue
/private/var/mobile/
stackid
;1
%@ %@: '%@[]'
Abandoned
swift_reflection_dumpTypeRef
a
, shared with
WindowServer
commonAddressBits
B32@?0@\"NSString\"8Q16^B24
<UNNAMED_%s_class_%#llx>
user-interactive
watchOS
%*u: %s%s%@;%@
  [->%@]
Writable regions: Total=%s written=%s(%.0f%%) resident=%s(%.0f%%) swapped_out=%s(%.0f%%) unallocated=%s(%.0f%%)\n
CFNetwork
invert rootLeakAddressToStackIDMap to produce stackID --> {size,count,root-leak-call-tree-root} map
%@ + %llu%@%@
hasRootsPresent
Unable to get thread state for thread %u of remote process %d: %@\n
[capture]
error: '%@' for ivar: %s
dispatch_workloop_t
Total number in stack (recursive counted multiple, when >=%d):\n
Class (swift_class_t)
%sUNUSED SPACE AT END\n
peak
[Symbol Store] \n\n
Error getting info for slab, scanning block %p [%llu] conservatively\n
Class.data.properties (property_array_t)
SWIFT_ARRAY
refcount
OS_dispatch_mach
network
MALLOC_PTR
coreaudiod
< process and analysis tool header unavailable >\n
nextDominates
graphEncodingVersion
%@%@
.items
_swift_debug_refcountIsSideTableMarkerValue
 %10s %10s %10s %7s
SInt16
float
int64_t[]
server
(
determineOSClassInstanceSize
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR
\t\tframe pointer %#llx\n
{ location:%@  length:%@ }
-[VMUDirectedGraph decapsulateSupplementalData:forTag:]
-----------------------------------------------------------------------
    %*s:  %s
   %s  %s  %s
%s flag supplied with no argument
Malloc
__DATA_DIRTY __all_image_info
infoForTypeRef() gave { .Kind = %s, .Size = %u, .Alignment = %u, .Stride = %u, .NumFields = %u}\n
unused __TEXT
MMIO
__AUTH
macOS
__unowned
| 
com.apple.lsd
[Stack Log Reader - nodeToTimestampTable] nodeNamespaceSize %u  %lu bytes\n\n
v20@?0I8*12
referenceDetails
VMUBacktraceUniquing.c
%d %@
        %@        %lu\n
-[VMUProcessObjectGraphRefiner isBadReferenceToCollectionClassStorage:]
NSNumber
SYMBOLICATION_SHOW_BACKTRACE_TIMINGS
NSPathStore2
create dominator graph
zone_info
$_0::operator()
client
xctest
length:remoteAddress:
Unable to retrieve ledger entry info in VMUProcessLedger
region: [%#llx-%#llx] %s %s (%llu %s)%s  %s\n
collectVMpageStatistics
========================
-[VMUGraphStackLogReader initWithCoder:]
 -- loaded from target process
Memory indirectly held only by autorelease pools
old_backtraces_contained - uniquing_table->backtraces_contained <= 1
%#llx[%llu] --> %p[%llu]  FAIL! READ_BYTES CACHE HIT, BUT NEED TO MAP MORE\n
 a
nextEmptyEntry
uint32_t[]
Identifier
malformed type encoding
shortVersion
%*s
DYLD_IMAGE_SUFFIX
Invalid IPS header: %@
init()
_CFXNotificationObjectRegistration
_container
   COUNT (non-coalesced)
tag
CoreMedia
Unable to deserialize the memgraph %@
Duplicates count
v24@?0r*8Q16
targetIsGetTaskAllow
Protocol: %@
processName
{CGRect=
WTF::fastMemDup
%s RECURSION LEVEL %u
%+*d: %s%s%s[capture];
  REF
_Atomic 
Cannot answer is64Bit for cpuType is %d cpuSubtype is %d
WebKit Using System Malloc
  [
%@%@%@
\x83
Bootstrap Dictionary
regionDataSerializerCompressed
alternate_accounting_compressed
rwx
_getRegionMallocStatistics_block_invoke_3
CFBundle
pseudo-isas for AsyncTasks and Slabs
Unable to initialize inflate: %d (%s)
memgraph refinement - remove impossible references
 Guard Page
FigBaseClass symbol name
%-*s %*s-%-*s [%@] %s/%s %s%s%-*s%s  %s
claimed region: [%#llx-%#llx] %s %s (%llu %s)%s - type '%s' range: [%#lx-%#lx]\n
v16@?0Q8
ARM64_32
generated corpse for pid %u
libswift
-[VMUObjectGraph(UsefulAlgorithms) isRootNode:]
AttributeGraph_0x
OS_nw_frame
RefFromNonobjectToUnalignedInterior
B44@?0I8{?=Qb60b4@}12@\"NSString\"36
RefFromNonobjectToStart
sysctl.proc_cputype
Memory size of autoreleasepool content blocks
Invalid minRegionAddress %#llx and/or maxRegionAddress %#llx\n
/usr/lib/system/libsystem_platform.dylib
VM_KERN_MEMORY_UBC
< content unavailable >\n
__NSFrozenSetM
%@ -- failed to read content from %#llx-%#llx[%ld] %@\n
VM_KERN_COUNT_WIRED_STATIC_KERNELCACHE
collectable
objc
error %@ reading zones_address at %qx
no posix thread
v20@?0I8^B12
OS_dispatch_workloop
\"file://
DT_SKIP_PRECISE_SCANNING_SWIFT_ASYNC_ALLOCATIONS
VMUScanTypeConservative
Dispatch Thread %@ Limit: %u reached in %u of %u samples -- too many dispatch threads blocked in synchronous operations\n
Swift._DictionaryStorage<
v16@?0@\"NSString\"8
BaseClass
[Node Labels] NO NODE LABELS\n\n
enumerating references for guessNonObjects
data.
_objc_debug_indexed_isa_index_shift
VMUDirectedGraphCompatibilityVersionNumberInGraphKey
swift_reflection_dumpInfoForMetadata
__NSOrderedSetReversed
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime with stable ABI has been loaded
boardd
,
JSC::tryAllocateAlignedMemory
, std::char_traits<
B32@?0Q8@\"VMUTaskMemoryScanner\"16@\"VMUTaskMemoryCache\"24
_NSViewAuxiliary
page_table
ExclaveKit
v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24
B28@?0I8I12I16*20
SWIFT_SINGLE_PAYLOAD_ENUM
thread %d
VM_KERN_COUNT_MANAGED
Async Frames
sparseEdgeList
RegionEndOffsetKey
Bailing because slab %p [%llu] does not fit inside container\n
geo::MallocZoneAllocator::reallocate(void*, unsigned long)
xpc_array_t
\n\"
File does not contain memory graph version information (not in correct format)
NSMutableArray
*** Error: calling task_try_peek() before task_start_peeking()\n
Value has size %llu, but Remote Mirror reports a size of %u.  Ignoring Remote Mirror output and scanning conservatively.\n
%8u
(thread)
int32_t
const 
 (%s%@%sStorage)
Sample analysis of process %d written to file %s\n
NSString
_NSThreadData
<couldn't read content>
IsAppleCode
childPageOffset
union
int64_t
description
options
_parent
%+3d \"%@\" size %u (%s)  %@
threadNameRanges
VMUDirectedGraphDomain
com.apple.dt.Symbolication.VMUObjectGraph
%#llx is in %#llx-%#llx;  bytes after start: %llu  bytes before end: %llu\n
graphics_footprint
VMUDirectedGraph.m
pdf_named_calloc
MergedGlobals
unused  unknown system shared lib
PAGES
Classes
unscanned
__NSArrayM
RefFromAssociatedObjects
, Specific
WTF::tryFastCompactCalloc
!_webkitOwnedClassInfo
TIMING:  %s\n
    %s\n
swift_reflection_classIsSwiftMask
swift_reflection_dumpInfoForTypeRef
/usr/
NSManagedObjectID
MTE
VMUTraceTreeAnalyzer.m
__AUTH __objc_
WTF::fastMalloc
buildLeakTree
CFString
Zalloc bits
VM_KERN_MEMORY_LTABLE
get malloc zones array
pas_msl_malloc_logging_slow
<
RefFromThreadRegister
network_nonvolatile_compressed
int32_t[]
_values
ROOT CYCLE: 
RefFromNoSymbolGlobalVariable
__NSExactBlockVariable__
X86
[@@@spacing@@@]%@
RefFromMergedGlobals
ExecutablePath
x:%g y:%g w:%g h:%g
%@  dirty: %s  swapped: %s
[invalid usage]: %s\n\n
tagged_footprint_compressed
l
exclaveFlagData
%s in analysis process, for %s in target process
can't expand backtrace uniquing table from %llu nodes to %llu nodes (exceeds maximum %u)\n
MallocStackLoggingLiteZone_Wrapper
<couldn't read name>
Process exited
x7
v16@?0@\"VMUAnalyzerSummaryField\"8
%#llx  FAIL! STRING_LENGTH DID NOT FIND NULL TERMINATOR IN %llu BYTES FOR STRING LENGTH OF %.*s\n
%10qu
%s 
_NSBindingInfo
MALLOC ZONE
boringssl_legacy_ctx
x17
%c%c%@%c
__NSDictionary0
v32@?0@\"VMUMutableFieldInfo\"8Q16^B24
backtraceUniquingTableSize
 %8zx
LastTLSslotKey
Failed to create CSSymbolicatorRef for pid %u %@
v16@?0@\"VMUMutableFieldInfo\"8
RESIDENT
gather VM region data
VM_KERN_COUNT_STOLEN
fields
*** task_malloc_get_all_zones: %@\n
Unowned-Applied
 REGION
 (char[])
SpringBoard
operator_new_impl
TEXT
 %8s
v60@?0I8I12I16{?=^{?}{?=QIQ}^{?}}20
/(Security(Foundation|Interface|HI)?|Kerberos(Helper)?|TrustEvaluationAgent)\\.framework/|/lib(crypto|ssl|sasl2)[^/]*\\.dylib|/sasl2/
_context
Getting fields for closure context at %p\n
region 
%@  %s:%u
cuml_regions
q24@?0@8@16
    
Invalid bug type in IPS header.
nodes
Unable to compress data: %d (%s)
v36@?0I8Q12Q20{?=Q}28
_ancestorWithLayerForLastLayerGeometryUpdate
Nothing to symbolicate. This dSYM does not contain symbols for '%@' binary. For more information, please compare the UUIDs.
__NSSetI
thread-specific-data key 43
neural_footprint
Unable to initialize deflate: %d (%s)
]
__NSCFArray
previousRunloopsAndModes
nodeIndex < _graph.nodeNamespaceSize
cfprefsd
id 
/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
.
on dirty page  unused system shared lib 
Bytes before following region: %llu
%@:  \"%@\"
LEAKS
v16@?0^v8
IOMalloc_internal
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: loading info for Swift runtime at %s
v40@?0{msl_disk_stack_logging_record=I{?=Q}QQ}8
[VM Region Tracker] Region count: %u\n\n
Chunk %s\n
NSMapTable
RefFromObjectToAlignedInterior
dyldSharedCacheLength
_indexedEdges < VMUGraphNameNone
objectDetails
> 
_CFXNotificationRegistrationContainer
_swift_debug_refcountIsSideTableMarkerMask
bluetoothd
content
owns
  CS_VALIDATED
DART_CNODE
^{_CFStreamClient=}
hidd
plist
0@!`
__unsafe_unretained
__SwiftNativeNSError
%10llu  TOTAL BAD REFS\n
Swift reflection is unavailable. All Swift content will be scanned conservatively.
NO-FIELD  
Binary Images:\n
Class.data.methods (method_array_t)
_FigBaseObjectFinalize
NO STACK\n
%10llu  priority %u %s\n
q24@?0@\"VMUVMRegion\"8@\"VMUVMRegion\"16
SHARED
tagged pointer %@
, std::hash<
Call graph:\n
%-*u %@
_gT1Sz
IGNORE THIS FRAME
error in malloc size pattern '%@': lower bound of size (%llu) should be <= upper bound of size (%llu)
double
snapshotDate
long[]
%u (%.2fK) %@
re
count
%s%s\n
_zones
NO
framePtr
physFootprint
_swift_debug_nativeWeakReferenceMarkerMask
 Metadata
sum_size
OS_xpc_date
WTF::fastStrDup
boringssl_concrete_boringssl_ctx
OS_dispatch_
Reply Message
__DATA
%@ %@
stringSpan
___swift_reflection_version
VM_KERN_COUNT_EXCLAVES_CARVEOUT
key: \"%@\"
weak
oah_get_x86_thread_state
pages
  
_NSKVODeallocSentinel
%7llu
name
vmu_create_backtrace_uniquing_table
RefToFakeNode
Unknown core region
0x0
B36@?0I8{?=Qb60b4@}12
Unable to unarchive `compactEdgeList`.
_AGGraphVMRegionBaseAddress
Stack of %@
pthread_condattr_t
@\"NSString\"40@?0@\"VMUObjectLabelHandlerInfo\"8^v16Q24Q32
__swift_concurrency_debug_asyncTaskMetadata
SHRMOD
RefToChildAutoreleasePoolPage
NULL
DT_DO_NOT_PRECISELY_SCAN_SWIFT_MULTI_PAYLOAD_ENUMS
metadata
[%@] Invalid task port provided to initializer.
DefaultMallocZone
----\n
swift_reflection_infoForMetadata
native
VMUScanTypeSwiftWeak
%lld
\t...\n
%u  stringID %u %@\n
_client
com.apple.main-thread
%#llx[%llu] FAIL! READ_BYTES COULD NOT MAP, ALTHOUGH FOUND REGION %s\n
DIRTY+SWAP
vmRegionTracker
edgeList
Couldn't create task memory cache
VMUSymbolStore
WTF::fastCompactMalloc
array_entries
Symbolication: could not find object label handler plist %@.plist
physFootprintPeak
symbolStore
couldn't get address of introspect structure symbol %s in %s
WTF::fastRealloc
identifying strongly-connected-components (cycles) in the graph
values
exitStatus
%u:%u:%u
(unknown)
details
DT_REPORT_IOKIT_REGION_LEAKS
error in malloc size pattern '%@':  size must be a multiple of %llu, or a range like '[lowerSizeBound-upperSizeBound]'
        
File is missing metadata required for analysis.
I386 ESP
cameracaptured
regionAttributesData
expected 1 binary in ExclaveCore target, but found %zu
v16@?0@?<v@?Ii@?<v@?^v>>8
Gigacage::tryMallocArray
NSHashTable
MULTIPLE RANGES OF RECURSION: %zu\n
runningAsRoot
[Stack Log Reader - originalUniquingTableContents] \n\n
[Region Attributes Data] Count: %u\n\n
icu::UnicodeSetStringSpan
extra
No duplicates detected
NSArray
NSLayoutConstraint
binary plist:  {
CONTENT:
%lu ADDITIONAL CHILDREN\n
@ `
v56@?0{mapped_memory_core_file_dumped_region_info_t=QQQQii}8^B48
objectRef
Storage)
RefFromStackToAutoreleasePoolPage
alternate_accounting
message
wifid
oah_get_runtime_location
 %.*s:%@ 
Memory graph file content is obsolete development version, no longer supported\n
__swift_debug_allocationPoolPointer
stack guard for thread %d
max_size
immortal
Memgraph Resymbolication Error
swift_slowAlloc
clean
OS_dispatch_queue_serial
callBacks
SYMBOLICATION_DEBUG_REMOTE_MIRROR_OUTPUT_FOR_SWIFT_SUBFIELDS
markIOSurfaces
nodeToStackIdTable
, std::less<
unknown
!_classDataClassInfo
RefFromCollectionToObject
SANITIZER
vm_region: %s\n
__NSStackBlock__
dispatch_queue_serial_num
RefFromObjectToStart
%3llu%%
,...
{RefCounts<swift::
(VMUBacktraceUniquing): Invalid PC 0x%llx at frame %u for stackID %llu\n
objc::detail::DenseMapPair
Address Sanitizer
char*[]
bool
VSIZE
154
counting allocations
Illegal attempt to scan memory of mach_task_self()
JSC::IsoAlignedMemoryAllocator
xpc_activity_t
%#llx[%llu] --> 0x0[0]  NOT FOUND  READ_BYTES CACHE HIT\n
Soft
site
archiving nodeToMSLPayloadTable
ReportMemoryException
VMUTaskMemoryScanner does not support kernel cores.
streamLock
...\"
%#llx[%llu] FAIL! READ_BYTES REGION NOT FOUND\n
VMUTaskErrorDomain
vm.self_region_footprint
%#llx [%llu]
struct OSMetaClassPrivate
 
NSInputStream
dispatch_semaphore_t
xpc_uuid_t
_value
JIT
Memory directly held only by autorelease pools
*** Error: calling task_peek() before task_start_peeking()\n
step 1 -- build map table with live malloc block addresses as keys
ADMIN_REGION  PTR_REGION  PTR_IN_USE
Found process %d (%s) from partial name %s\n
*** task_malloc_get_all_zones: error %@ reading zones at %qx\n
compute dominators (%lu): changeCount = %lu, skipCount = %lu, lastChangedIndex = %ld
^block parameters must be non-nil.
autoreleasepool boundary
Process %d: %u object%s abandoned for %llu total abandoned bytes.\n
_dataSource
_owner
--->  
 for ACTIVE TRANSACTION with
kernelmanagerd
Call graph:
v8@?0
.*%@
value
 (VERY BAD)
Found cached field \"%s\"\n
Setting region name in %s based on enumeration range for  %s\n
CFIndex
VMUVMRegionCurrentVersion
, std::default_delete<
x8
add child counts
IPS length is invalid.
Slab %p [%llu], next slab %p\n
_malloc_type_
coldestFrameIsNotThreadId
%s in target process is different than in analysis process, which can cause problems analyzing memory.  You may need to relaunch the target process and analysis process to get the new version of the framework.  The dyld shared cache may als
PRT
page
com.apple.
_nextResponder
Dummy no payload field
entries[entryIndex] == 0
storage_bitmap_ptr
v32@?0@8@16^B24
swift_reflection_childOfTypeRef
dispatch_queue_t
_buff
SWIFT_CLOSURE_CONTEXT
conservative
tagged_footprint
__NSSingleObjectArrayI
instance size %d, allocation size %d
autoreleasePoolOffsets
%s:%u
VMULeakDetectorDomain
BadRefToNonObjectTypedByIvar
%#llx + %llu
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime with stable ABI has already been loaded, ignoring this other one.
%s%.*s%s
JSC::FastMallocAlignedMemoryAllocator
 (
__NSArrayI
_NSModelObservingTracker
MALLOC_DATA
pthread_attr_t
/(Web(Kit|Core)|JavaScriptCore)\\.framework/
_outlined
nonUTF8-binary-name
VMUStackLogConsolidator
keyPC
```
