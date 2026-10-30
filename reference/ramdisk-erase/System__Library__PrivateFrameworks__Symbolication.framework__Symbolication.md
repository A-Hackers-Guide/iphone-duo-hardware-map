# `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,133,088 bytes.

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
VMUDestructiveMutationWhileEnumeratingException
traceTreeRoot || traceListString
core file
 + 
!_classDataClassInfo
TIMING:  %s\n
graphics_footprint
id[]
i32@?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16@\"NSString\"24
kalloc_ext
\tCall stack: %s\n
SEL
[Class Layouts] Class info count: %d\n\n
JSC::LocalAllocator::allocateSlowCase
Unowned-Applied
location != NSNotFound
VMUGraphStackLogReader.m
(kernel)
_os_trace_zalloc
markMallocAreas
Call graph:
%lld
thread
(ROOT LEAK|CYCLE): <(.*) 0x[0-9a-f]+>* \\[\\d+\\].*
        see MALLOC ZONE table below
_FigBaseObjectFinalize
long
ARM LR
content
__outerOp
Class.
Binary Images:\n
cpsr
remove junk nodes from object graph
SWIFT_CLASS_INSTANCE
targetIsGetTaskAllow
key_field
reserved VM address space (unallocated)
VM_KERN_MEMORY_COMPRESSED_DATA
-[VMUObjectIdentifier setupIsaTranslator]
%u %c
no posix thread
__NSCFError
_parent
buffer
objectRefsListEntryNext
Total allocations size
 [inlined]
length: %lu  \"%@\"
%c)
(VMUBacktraceUniquing) expandUniquingTable(): mach_vm_deallocate failed. [%p]\n
dispatch_queue_t (concurrent)
NSCellAuxiliary
%@ -- failed to read content from %#llx-%#llx[%ld] %@\n
, shared with
< process and analysis tool header unavailable >\n
No object labels had %lu duplicates.
sampling all threads
malloc<%s>
stackList
concurrent
Allocations count
vmu_swift_reflection_asyncTaskSlabPointer error: %s\n
NSMutableArray
OS_dispatch_workloop
_submenu
Class.methodCache._buckets (bucket_t)
VM_KERN_MEMORY_MBUF
___kCFBooleanFalse
exitStatus
framePtr
graphCompatibilityVersion
 (Roots Present)
MMAP
SANITIZER
free
SYMBOLICATION_NO_SWIFT_REMOTE_MIRROR
v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24
The graph version (%ld) is too new.  The latest graph version this tool supports is %d.
     ** %u:  
NSView
markMallocAreas_block_invoke
AUTORELEASEPOOLS
%*s
content length %ld at offset %llu in VM:  %@
Getting fields for Swift value type %s\n
 %*s
VM_KERN_MEMORY_KALLOC_SHARED
.peer.0x
Inverted call tree:
v16@?0@?<@\"CSMemoryMappingSlice\"@?QQ>8
data.
No matching libraries found in this memgraph
OS_xpc_pointer
   
$1
VM_KERN_MEMORY_IPC
pthread_mutexattr_t
v36@?0I8Q12Q20{?=Q}28
NSUUID
queue
Thread_
q24@?0@\"VMUVMRegion\"8@\"VMUVMRegion\"16
threadNameRanges
/u/l/
Exctracting labels
pdf_named_malloc
_os_trace_calloc
some
VM_KERN_MEMORY_IOKIT
__NSConcreteWeakBlockVariable
%@=
<
__NSOrderedSetReversed
!_osxpcDictionaryClassInfo
SWIFT_CLOSURE_CONTEXT
PTR_IN_USE
coldestFrameIsNotThreadId
run_state
archiving thread / binary / regionSymbol to range mappings
-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke_3
Found no VM regions in target process
com.apple.dt.Symbolication.VMUSimpleSerializer
SWIFT_NO_PAYLOAD_ENUM
  !! %s %s  when analyzing object instance: %#llx
[Stack Log Reader - nodeToMSLPayloadTable] nodeNamespaceSize %u  %lu bytes\n\n
Gigacage::malloc
__1::
%#llx[%llu] FAIL! READ_BYTES REGION NOT FOUND\n
NSInteger
IsAppleCode
The memory graph file only contains labels for contents of readonly memory of the target process, so only those items can be shown.\n
VM: %@
%s[%d]: notice: memory marking disabled due to presence of NSZombieEnabled=\"%s\" environment variable\n
collectable
thread-specific-data key 43
%@  %s:%u
%9lu %9lu %9.1f   %@
String
SWIFT_EXISTENTIAL_METATYPE
regions.count == *regionCountInOut
immortal
,
newAddressWidth >= addressWidth
GMcalloc
, std::equal_to<
_children
a
SelfRefToNonLeak
SWIFT_UNKNOWN
Classes
<no-type>
WTF::fastCalloc
icu::UVector64
OS_xpc_endpoint
com.apple.main-thread
RefFromAutoreleasePoolToObject
regionDataExtra
slab
AttributeGraph Data
shared memory
double
v28@?0I8Q12@\"VMUKernelRuntimeMetadataChunkInfo\"20
swift_bufferAllocate
Class.data.extended (class_rw_ext_t)
watchdogd
Could not read swift metadata block back pointer
sourceFile
Class.data (class_rw_v2_t)
WARNING: Forcing live process analysis for a system-critical process (pid %d).\n
 (empty)
introspect structure %s for the malloc zone has no enumerator function in %s
i24@?0r^v8r^v16
__CFNotification
B8@?0
identifier
 =  
%+3d \"%@\" size %u (%s)  %@
stack guard for thread %d
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime pre-dating the stable ABI has been loaded
r--
v32@?0@\"NSNumber\"8@\"VMUProcInfo\"16^B24
Address Sanitizer
VM_KERN_COUNT_MANAGED
[Stack Log Reader - backtraceUniquingTableContents] %llu bytes\n\n
uint32_t[]
/System/Library/(Private)?Frameworks/[^/]*\\.framework/
error: core's page size doesn't match the host system (%u KB vs %u KB), cannot continue\n
_os_trace_malloc
=
CFData
Swift unowned reference storage
gOSMetaClassBaseRemotePrivateLayout
, std::allocator<
OS_xpc_array
Failed to get addressing mask for %@ core file.
Failed to find xzm zone introspection structure
OS_xpc_dictionary
=======
/libclang_rt.tsan
!
Found first slab at %p,%s in same block\n
__NSDictionaryI
VM_KERN_COUNT_BOOT_STOLEN
!_backtraceUniquingTable || !_originalUniquingTable
xzm_malloc_zone_introspect
nodes
    no autorelease pool\n
[thread %#llx]:
NSString
v24@?0Q8Q16
firstEntryOffset
failed to expand uniquing table to %llu bytes\n
Malloc enumeration
%-*s
/usr/lib/libboringssl.dylib
alternate_accounting_compressed
/usr/lib/system/
graphEncodingVersion
.app/
default
_remoteObjectInterface
__DATA_CONST __objc_
Unable to write sample file %s\n
autoreleasePoolOffsets
x3
uniquing_table->numNodes < MAX_UNIQUING_TABLE_NODES
\n\"
RefFromStackToAutoreleasePoolPage
No malloc zone statistics available for malloc zone %@\n
__swift_concurrency_debug_asyncTaskSlabMetadata
v16@?0^?8
libsystem_malloc%s.dylib
ARC
@ `
NSPathStore2
mdworker
path
strlen(tag) <= 8
v68@?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60
__NSOrderedSetI
step 4 -- build call tree by iterating the uniqueBacktraceToObjectsMap
infoForTypeRef() gave { .Kind = %s, .Size = %u, .Alignment = %u, .Stride = %u, .NumFields = %u}\n
bluetoothd
dispatch_source_t
symbolStore
remoteQueues
JSC::IsoMemoryAllocatorBase::tryAllocateAlignedMemory
Weak references in Swift content may be misidentified as retaining references.
VM_KERN_MEMORY_PTE
NSURL
DriverKit
v60@?0I8I12I16{?=^{?}{?=QIQ}^{?}}20
allMarkedAddresses
malloc-block
\n%u leak%s excluded (not printed)\n
%@%@\n
BYTES
purgeable_nonvolatile_compress
Unable to unarchive `compactEdgeList`.
__LINKEDIT
^{_CFStreamCallBacks=}
memgraph refinement - remove impossible references
__NSExactBlockVariable__
WTF::tryFastZeroedMalloc
\n%@
boringssl_legacy_ctx
frames
__NSSingleObjectArrayI
%#llx-%#llx[%llu] stringID %u %@\n
Swift._SetStorage<
/usr/lib/system/libxpc.dylib
__unowned
^{%@_IVars}
/(CFNetwork|IO)\\.framework/
non-root VM region
setting up VMUScanOverlay
        %lu       %@\n
archiving userMarked
malformed type encoding
error: core's pointer size doesn't match the host system, cannot continue\n
live task
bplist0
queueArray
xpc_double_t
%u (%.0fK) %@
serial
Class.data.protocols.lists (protocol_list_t)
missing ivar at index: %d in class: %@
         The process will be suspended and may cause system instability.\n
VSIZE
    COUNT     BYTES   AVERAGE   CONTENT
non-object with no stack backtrace
thread_resume2
mutable
asyncFrames
dyldSharedCacheLength
Error getting info for slab, scanning block %p [%llu] conservatively\n
MRC
bool[]
unordered_map
^{IOUserServer_IVars}
libdyld.dylib
__NSArrayI
key: \"%@\"
<%@>
 D=
% of total allocations
%10zu  _sourceAddressToReferencePriorityDict.count\n
RefToParentAutoreleasePoolPage
Swift
pid
children
!_autoreleasepoolContentClassInfo
v56@?0{mapped_memory_core_file_dumped_region_info_t=QQQQii}8^B48
NO
message
_delegate
-[VMUProcessObjectGraphRefiner assessReferencePriority]
rpc.lockd
-[VMUMallocZoneAggregate enumerateHeapAndVMSortedBy:withBlock:]
%@,%@>
void
, 
_table[%u]
/(Security(Foundation|Interface|HI)?|Kerberos(Helper)?|TrustEvaluationAgent)\\.framework/|/lib(crypto|ssl|sasl2)[^/]*\\.dylib|/sasl2/
FRAG SIZE
swift_allocObject
Process %d: %u nodes malloced for %llu KB\n
PPC-64
xpc_date_t
xpc_dictionary_t
ADMIN_REGION  PTR_REGION  PTR_IN_USE
SWAPPED
struct %@
, std::__unordered_map_hasher<
we
VMUSimpleSerializer
\x91
machTime
%@ / %@
_superview
%10llu  TOTAL BAD REFS\n
%s[%d]: warning: memory marking timeout encountered - marked objects may be incorrect from this point forward\n
REGION
iOS Simulator
preparing to enumerate %@\n
/System/Library/PrivateFrameworks/
metaclass
<null-uuid>
_children.elements
 Guard Page
 %@
functionNameRanges
x23
memgraph file is malformed - unable to deserialize.
bmalloc_
GuardMalloc in the target process may be using too much VM
/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
x13
uint64_t[]
Failed to map remote region at [%#llx-%#llx]\n
libsystem_malloc.dylib
VMUOptionParserDomain
%s: %s\n\n
VMUAnalysisSummaryKey
VM_KERN_MEMORY_TRIAGE
^block parameter must be non-nil.
-----------------------------------------------------------------------
Number of addresses sent to VMUSymbolStore by client classes:\nFor backtrace sample: %zu\nFor binary sections: %zu\nFor global variables: %zu\nFor malloc stack logging: %zu\nFor hex found in node labels: %zu\nTotal unique addresses to be sa
No dSYMs were found
std::
x0
MetaClass
Backtrace Excluded
entries[entryIndex] == 0
Code Type
JSC::FastMallocAlignedMemoryAllocator
<< TOTAL >>
LINKEDIT
{unordered_map<
SCAN_VM_REGIONS_WITH_UNKNOWN_PATHS
NonstrongSelfRefToLeak
__NSWeakBlockVariable__
cuml_regions
Memory directly held only by autorelease pools
(ROOT LEAK|CYCLE): (VM: .*)  0x.*
 (
NSWeakObjectValue
SWIFT_SINGLE_PAYLOAD_ENUM
\x81a
phys_footprint_lifetime_max
nextDominates
v24@?0@\"VMUClassInfo\"8I16I20
One or both of the AsyncTask and AsyncTask Slab metadata isas isn't known, so skipping precise scanning of AsyncTasks and AsyncTask Slabs.\n
%#llx (in %s)
boringssl_concrete_boringssl_ctx
step 2 -- enumerate stack log records to record unique backtrace IDs for objects of interest
kern.wq_max_constrained_threads
sourceInfoRanges
slice
! 
referenceDetailsLarge
Total entries in autoreleasepools
%s %#llx-%#llx[%llu]\n
yyyy-MM-dd HH:mm:ss.SSS ZZZ
higher
Class.data (class_rw_t)
        not counted in TOTAL below
START 
bug_type
initMemoryScanner
_allocate
libxpc.dylib
%@:  \"%@\"
replacementIndex < linearCount + 1 && replacementIndex != i
_AGGraphVMRegionBaseAddress
Unable to suspend target task: %s (%d)\n
v24@?0I8i12@?<v@?^v>16
OS_xpc_date
step 1 -- build map table with live malloc block addresses as keys
RefFromLargeNoncollectionObjectToStart
Thread_<multiple>
  REF
constant
__ZL13TypeNameCache
MULTIPLE RANGES OF RECURSION: %zu\n
VMUClassInfo.mm
VMUScanTypeNone
Unable to unarchive `archivedClassInfos`.
Could not get current swift metadata allocation pool
swift_reflection_asyncTaskSlabAllocations unavailable on bridgeOS
_otherBits
dyld shared cache combined __LINKEDIT
At end of VM region
plist
framePtrs
x27
VMUTaskMemoryScanner.m
GMrealloc
controlView
__DATA_DIRTY __all_image_info
malloc in std::vector<
_objc_debug_isa_class_mask
binarySectionNameRanges
<unknown register index %u>
Swift Metadata
%u (%.2fM) %@
RefFromThreadRegister
[%#qx to %#qx] (length: %qd)\n
Failed to generate corpse: %@
__NSSetI
%@----\n
v32@?0@\"NSString\"8@\"NSDictionary\"16^B24
backtraces
<no symbol>
extra
    %s\n
SYMBOLICATION_DEBUG_REMOTE_MIRROR_OUTPUT_FOR_SWIFT_SUBFIELDS
SWIFT_OPAQUE_EXISTENTIAL
agendaIdx != 0
v52@?0I8{?=Qb60b4@}12@\"VMUVMRegion\"36^B44
__NSDate
__NSTaggedDate
Closure context
_SwiftValue
com.apple.CFNetwork
long[]
   %s\n
__NSCFTimer
TRACE
SurfaceID: %#x  %llux%llu (%s) %s
-[VMUGraphStackLogReader populateBacktraceUniquingTableWithStackLogs:]_block_invoke
[Node Labels] NO NODE LABELS\n\n
YES
vector
v32@?0@\"NSNumber\"8@\"NSArray\"16^B24
__NSArrayM
%s kept pid %u suspended for too long - exiting to prevent watchdog timer from killing that process.
Unexpected range type value %x from malloc zone enumerator\n
Thread_%u
3!`
NSOutputStream
content length %ld at %#llx
Frozen
v40@?0c8I12@\"NSString\"16@\"NSString\"24@\"NSString\"32
...%@
owns
RefFromNamedIvarToObject
v24@?0Q8I16I20
__unsafe_unretained
NSNotFound
JIT
Storage)
_dispatch_strdup_if_mutable
swift_reflection_infoForMetadata
CFString
legacy_context
VMUProcessObjectGraphRefiner.mm
@\"NSMutableDictionary\"64@?0I8Q12Q20i28@\"VMUClassInfo\"32@\"VMUVMRegion\"40Q48@\"NSArray\"56
_
nonUTF8-binary-name
swift_reflection_typeRefForMetadata
Malloc
VMUKernelCoreMemoryScanner.m
GMmalloc
_secondItem
_variantForNSSlice
thread_suspend2
\t[%3d] %#08.8qx  {%s.%s + %#qx} %s\n
x21
oah_get_x86_thread_state
VMUTaskMemoryScanner does not support kernel cores.
MallocStackLoggingLiteZone
strdup
Target task not available for analysis
\xa1\xa1
__NSCFArray
error
com.apple.dt.instruments
pthread_t structure %+4lld
className
StartRoutineArgumentOffsetKey
LastTLSslotKey
AsyncTask
identifying root leaks and cycles
buf
.personalityProps
x6
llvm::safe_realloc(void*, unsigned long)
unrecognized option '%s'
swift_reflection_ownsObject
====\n
NSNotification
element
@\"NSString\"16@?0r*8
RefFromNamedIvarToUnalignedInterior
mach_vm_tag_describe
Thread_%x
Unable to gather threads of remote process %d: %@\n
storage_bitmap_ptr
-[VMUObjectGraph(UsefulAlgorithms) isRootNode:]
<PTHREAD_T>
dbReallocFinish
B44@?0I8{?=Qb60b4@}12@\"NSString\"36
ADMIN_REGION  PTR_IN_USE
USER
Total number in stack
neural_footprint_compressed
__NSSetM
No-Change
  (in 
tagged_footprint_compressed
Invalid minRegionAddress %#llx and/or maxRegionAddress %#llx\n
operator new
WTF::
WTF::fastCompactRealloc
__NSFrozenSetM
Zalloc read-only
<%@ %p>
(address & (1ull << 63)) == 0
v36@?0I8Q12I20I24Q28
Failed to create symbolicator.
regionDataSerializerCompressed
%s %.*s
VMUDuplicatesAnalyzer
swift_reflection_asyncTaskSlabPointer
%s - %s
MTE
RefFromNonobjectToStart
1A
TIGHTBEAM
markStacks
pthread_once_t
remove junk edges from object graph
%@%@
IOMalloc_internal
NSPointerArray
ADMIN_REGION
TOTAL, minus reserved VM space
\t\tframe pointer %#llx\n
nodeLabels
%s%@
caulk::alloc::darwin_resource
vasprintf unexpectedly failed
nodeToMSLPayloadTable
bitfield:
region: [%#llx-%#llx] %s %s (%llu %s)%s  %s\n
__NSCFLocale
UnsafeUnretainedRef
libsystem_kernel.dylib
Argument num %d utf8 null: %s\n
ReportMemoryException
DVT_
[Dense Edges] Compact: %d Large: %d (%2.2f%%)\n\n
_malloc_zone_
^@
DisplayName
phys_footprint
addChildCountsIntoNode
content length %ld entire VM:  %@
symbol
region 
PRV
Slab %p [%llu], next slab %p\n
WTF::fastCompactZeroedMalloc
JSC::CompleteSubspace::tryAllocateSlow
%s 
unknown-process
Soft
zalloc (no zone)
%s\n\n
OS_xpc_connection
RefFromNamedIvarPlusOffsetToObject
%@\t%#18llx %@
loadSwiftReflectionLibraries
os_transaction_get_timestamp
qb
owned
VM_KERN_MEMORY_COUNT
\x81
_swift_debug_sideTablePointerLeftShift
utility
thread-specific-data key
SYMBOLICATION_LOG_ZONE_INTROSPECTION_LOOKUP
 (Bytes Storage)
%-3d 
icu::DecimalFormat
dispatch_queue_t
Class: 
markMachOLibraries
ReportCrashService
%#llx [%llu]
-[VMUClassInfoMap encodeWithCoder:]
%@  purgableVolatile: %s
yyyy-MM-dd HH:mm:ss Z
unnamed_zone_0x%qx
VM: unknown region type
MACH_HEADER
  CS_VALIDATED
SEL[]
meta
VMUTaskMemoryCache initialization
alternate_accounting
%ld
objectGraphInfo
malloc
NSKeyValueObservance
Swift._DictionaryStorage<
__NSConcreteStackBlock
/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector
Failed to get udata pointers for core file.
xpc_pipe_t
 (Storage)
 (%@:%@)
media
com.apple.CF
WTF::fastMalloc
icu::BMPSet
Time to initialize sampling context:  %0.2f
pthread_override_s
0@!`
-[VMUVMRegion splitOutRange:fromRegionIndex:regions:newZoneName:reason:]
edgeList
classVersion
xpc_data_t
  [
VM_KERN_MEMORY_SECURITY
tableSize == tableContentsSize
WTF::fastMemDup
, std::default_delete<
error in malloc size pattern '%@':  size must be %llu or more
%@-%@~%@
swift_reflection_typeRefForInstance
_NSKVODeallocSentinel
SHARED
VM_KERN_MEMORY_CPUTRACE
Memgraph Resymbolication Error
Process %d: %u leak%s for %llu total leaked bytes.\n
graphics
 (char[])
<%@ %#llx> [%llu]
%s in target process is different than in analysis process, which can cause problems analyzing memory.  You may need to relaunch the target process and analysis process to get the new version of the framework.  The dyld shared cache may als
%-*s %*s-%-*s [%@] %s/%s %s%s%-*s%s  %s
B36@?0I8{?=Qb60b4@}12
%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx
RefFromNoSymbolGlobalVariableToAlignedInterior
v16@?0@\"NSString\"8
VM_KERN_MEMORY_RECOUNT
int
Destructive mutation attempted while traversing graph!
+ 960
couldn't create new pthread for determine_pthread_offsets\n
audiomxd
*** task_malloc_get_all_zones: target has no active zones\n
Out of memory: failed to expand references array from %u to %u edges
Instances: %lu   Bytes: %lu   %@
DT_REPORT_IOKIT_REGION_LEAKS
CFBundleVersion
pthread_t
S/A
/System/Library/
VMUSymbolStore failed to create the symbolicator from signature.\n
geo::MallocZoneAllocator::callocate(unsigned long, unsigned long)
realloc
AppKit
@
%@.%@
__NSMS1
bmpSet
 + %u
marking malloc VM regions
backtraceUniquingTableContents
idleExitStatus
 END
Found no malloc zones in target process
__NSCFInputStream
float
hottestElided: %u  coldestElided: %u  depth: %u  %#llx
warning: zone fixup failed - block %#llx from zone \"%s\" discovered in region [%#llx-%#llx] already claimed by \"%s\"\n
%s%@\n
VM ledger tag %llu
parse error with line: '%s'\n
tagged_nofootprint_compressed
bool
values_ptr
dyldSharedCacheBase
the provided call tree file %s contains non-UTF8 data\n
_indexedEdges < VMUGraphNameNone
%u (%.1fM) %@
_mmap
EASM_CNODE
mach_memory_info_redacted
\n%s%s\n
-[%s %s] error: malformed serialized data\n
Out of memory: failed to expand %s from %u to %u entries
, std::__bucket_list_deallocator<
_buffer
  CS_TAINTED
      
SHADOW_CNODE
VM_KERN_MEMORY_REASON
bt_library
hash_table_modify
:
Async Frames
VMUVMRegionCurrentVersion
atomic 
[Object Info] Compact: %d Large: %d (%2.2f%%)\n\n
%-*s %#*llx %@
VMUMaxRange(newVMRangeForZone) == rangeStartInRegion
l
Compressed %s to %s (%2.1f%% reduction @ %s saved/s) in %3.6fs\n
chunk
com.apple.SamplingTools
objc::DenseMap
swift_reflection_addImage
deeper
Symbolication.framework _get_symbol_owner did not find requested symbol %s\n
@\"CSMemoryMappingSlice\"24@?0Q8Q16
WebKit Using System Malloc
__block 
VMUTask initialization
VM_KERN_MEMORY_PMAP
processName
}
^
_noteBlocksInRegion
non-object in zone 
Gigacage::
malloc_zone_realloc
Unable to read __DATA __objc_imageinfo from %s\n
TEXT_EXEC
parentPage
type %s  value: %@
MallocStackLoggingLiteZone_Wrapper
archiving nodeToStackIDTable
node: %d at %d (%d edges leaving)\n
referenceDetails
strndup
llvm::safe_malloc(unsigned long)
NSInputStream
findCFTypes
Closure context (unknown layout)
        %u:  
    =====     =====   =======   =======
NSApplication
No matching kernel found.
/private/var/mobile/
154
com.apple.dt.Symbolication.VMUObjectGraph
/System
*** getStackLoggingSharedMemoryAddressFromTask: task_peek failed for shared_memory_address_address\n
RefFromNamedGlobalVariable
strcmp((const char*)(&newStringRegion[encoded]), (const char*)bytes) == 0
Class.data.methods (method_array_t)
gather VM region data
]
^(.+)\\.([^ ]+) \\(.+\\)$
MALLOC ZONE
physFootprint
tagged_footprint
OS_xpc_uuid
swift_reflection_dumpTypeRef
v40@?0@\"NSString\"8{mach_vm_range=QQ}16I32B36
VM_KERN_MEMORY_FIRST_DYNAMIC
CFNetwork
archiving nodeToTimestampTable
create dominator graph
Unable to decompress data: %d (%s)
StartAddress
wifid
Unable to retrieve ledger entry info in VMUProcessLedger
%p %s
WTF::tryFastCompactZeroedMalloc
 zone structure
LaunchCFMApp
__DATA_DIRTY __objc_
zone_security_array
CFArray
@autoreleasepool content
RefWithinCycle
SYMBOLICATION_DEBUG_SWIFT_SUBFIELDS
SWIFT_WEAK_REFERENCE
v28@?0I8I12^{?=QQ}16I24
(0x[a-fA-F0-9]*)\\s*-\\s*(0x[a-fA-F0-9]*)\\s*(\\S*)\\s*\\(([0-9\\- \\.\\?]*)\\)\\s*<(\\S{36})>\\s*(.*)
NSMutableAttributedString
BadRefFromSwiftMetadata
AttributeGraph Data (old mapping)
-[VMUGraphStackLogReader copyOriginalUniquingTable:]_block_invoke_2
IPS length is invalid.
self.inverted
RefFromLargeNoncollectionObjectToAlignedInterior
sum_size
_objc_debug_original_metaclass_map
BinaryInfoDwarfUUIDKey
Leaks total size
{
(VMUBacktraceUniquing) allocate_pages(): virtual memory exhausted! (XRBacktraceRepository)
%@  %@
The provided memory graph file is corrupted
objc::detail::DenseMapPair
        %@
libobjc.A.dylib
-[VMUDirectedGraph _adjustAdjacencyMap]
_markRegionsForMallocZones_block_invoke_4
_objc_debug_indexed_isa_index_shift
[Stack Log Reader] \n\n
VMUScanTypeExactStrong
+[VMUDirectedGraph encapsulateData:to:withSupplementalDataTag:error:dataGeneratorBlock:]
SYMBOLICATION_DEBUG_SWIFT_ASYNC
_swift_debug_sideTablePointerRightShift
  FICTITIOUS
DIRTY+SWAP
/usr/lib/libpthread.dylib
x25
Memory size of autoreleasepool content blocks
%s%s%@
building VMUProcessDescription
rwx
buildLeakTree
----\n
v16@?0@8
symbolLocation
  REUSABLE
mds
 + %llu
Time spent sampling with CFI:  %0.4f
Symbolication: could not find object label handler plist %@.plist
backtraceUniquingTableFlags
isTranslatedByRosetta
pthreadOffsets
%s+ %llu
    UNION TYPE ENCODING: %s\n
__ZL21InitialAllocationPool
%u %s OF '%s'
%#10lx - %#10lx %@%@ %@%@ %@%@\n
PAGES
swift_allocEmptyBox
RefFromNamedIvarPlusOffsetToNonObjectInterior
swift
;1
File does not contain a memory graph in the correct format
_instrumented_or_legacy
error in % <region-description> pattern '%@': %s
__NSCFDictionary
ARM Simple
__strong
UNKNOWN
-w-
Leak
-
values
Count
-[VMUSimpleDeserializer copyDeserializedNullTerminatedBytesWithError:]
=========
task peeking transformer guard queue
%#*llx (%-*s) %@
\t...\n
ARM
NSArray
 --> %@
x10
get malloc zones array
VMUProcessDescription is examining:\n   process: %@  pid: %d  path: %@  _binaryImages count: %zu\n   parent process: %@  pid: %d  path: %@\n
2
_zones
unable to inspect heap ranges of target process; it may be using a malloc replacement library without the required support
\n    
stringID < _stringRegCapacity
toolName
Request Message
[%.*f seconds] %@
<unknown-binary>
%s RECURSION LEVEL %u
unmapped
inverted
init()
 (MTE Enabled
OS_xpc_serializer
commpage (reserved)
Task stack
__DATA 
classMapVersion
/u/l/s/
STACK LOGS FAILED TO SAVE
SYMBOLICATION_DISABLE_FALSE_TASK_LEAKS_WORKAROUND
non-object from 
   %s  %s  %s
(0x[a-fA-F0-9]*)\\s*-\\s*(0x[a-fA-F0-9]*)\\s*(\\S*)\\s*(\\S*)\\s*<(\\S{32})>\\s*(.*)
.X1
<unknown-symbol>
RefFromClosureContext
RefFromNonobjectToUnalignedInterior
DefaultMallocZone
yyyy-MM-dd_HHmmss
targetIsDebuggable
com.apple.dt.memorytools
__NSCFType
unused __
pthread_condattr_t
immutable
REFERENCES THAT WERE KEPT:\n
%+*d: %s%s%s[capture];
coreaudiod
_malloc_zones
[coder allowsKeyedCoding]
64b
__NS
Analysis of sampling %@ (pid %d) every %d millisecond\n
_objc_indexed_classes
Protocol: <couldn't read name>
depth
I386 ESP
metaClassPrivate
Setting region name in %s based on _zoneNames[zone_index] for  %s\n
llvm::DenseMap<TypeNameCacheKey, std::pair<const char *, size_t>>
DIRTY
_swift_reflection_libraryVersion
K
0K
Unreadable Binary Images:\n
Binary images description not available\n\n
v16@?0@\"NSObject<OS_xpc_object>\"8
__objc_empty_cache
stackLogReader
rw-
/usr/
RefFromLargeNonobjectToAlignedInterior
%*s}
q
*** Symbolication:  Can't read pointers from zone %@ (error %d)\n
Binary Images:
  ATTRIBUTES
NSMapTable
%#llx[%llu] --> 0x0[0]  NOT FOUND  READ_BYTES CACHE HIT\n
%#llx --> %llu  STRING_LENGTH CACHE MISS OF %s\n
ADMIN_REGION  PTR_REGION
[%@:%@]
nodeToStackIdTable
network_nonvolatile_compressed
-[VMUVMRegion descriptionWithOptions:maximumLength:memorySizeDivisor:hasFractionalPageSizes:]
find unreferenced VM regions
NSMutableCharacterSet
failed to read content - bad data length %llu causes range overflow
_objc_debug_indexed_isa_index_mask
[Thread Names For Thread Ports] Count: %u  Uniqued string count: %u\n\n
x16
%.1fT
%p + %llu
B16@?0@?<B@?Q@\"VMUTaskMemoryScanner\"@\"VMUTaskMemoryCache\">8
 MTE TPRO JIT 
Malloc enumeration of zone \"%@\" failed to get full information about malloc metadata and/or allocations with the error \"%s (%d)\". It is likely that the target was suspended while malloc metadata was being modified.
basic_string
        %@        %lu\n
RefFromObjectToAlignedInterior
Unable to open/create sample file %s\n
remoteQueueCount
swift_allocError
_malloc_zone
Base - this should get overridden by subclasses
__VMUAssociatedObjectsObjcAbandonedMarkerKey
unused  unknown system shared lib __DATA
archiving nodeToMSLPayloadTable
ivars
Platform:        %@\n
OS_dispatch_queue_concurrent
_firstRealizedClass
unretained
classInfosDerivedFromStackBacktraces
__CFString
%s%.*s%s
~mobile/
__NSFrozenDictionaryM
OS_xpc_activity
malloc in std::unordered_map<
_connection
weak
description
B16@?0I8I12
vmu_remove_stack_from_backtrace_uniquing_table
-[VMUTraceTreeAnalyzer traceTreeForAddress:outputStyle:]
OS_
X86
%sUNUSED SPACE AT END\n
<invalid>
*[]
uniqued_stack < MAX_UNIQUING_TABLE_NODES
enum payload  %s  scanType %s (may be changed), of field %s, of object at %p of class %s  size %u stride %u\n
malloc in std::map<
%*u: %s%s%@;%@
non-inline
showsPhysFootprint
M
%.1fM
VMUEnumeratorValidation
non-object
, std::__unordered_map_equal<
RefFromCaptureToUnalignedInterior
^(.+) with unmangled suffix (.+)
[fatal] %s\n
Zalloc bits
cuml_malloc_bytes
kernel
_ancestorWithLayerForLastLayerGeometryUpdate
========================
+%llu bytes
x9
[Sparse Edges] Edge Count: %u\n\n
Unable to compress data: %d (%s)
[Reference Details] Total Compact and Large: %d\n\n
%@.%@ (%@)
JSC::CompleteSubspace::allocatorForSlow
0x
%s ELIDED %u LEVELS OF RECURSION THROUGH %s
targetType
WeakRef
launchservicesd
exclaveFlagData
VMUSymbolStore failed to sparsify some of resymbolicated symbol owners.\n
Ignoring 0-size and/or 0-stride field\n
_objc_debug_autoreleasepoolpage_ptr_mask
<unnamed %s>
VMUArchitecture unhandled cpuType
        
q24@?0@\"NSNumber\"8@\"NSNumber\"16
[]
dyld
__NSFrozenOrderedSetM
xpc_endpoint_t
OS_xpc_fd
RefFromLeakToNonLeak
ISSUE:  Region user_tag should already be set; setting to VM_MEMORY_MALLOC in %s based on enumeration range for  %s\n
VM_KERN_MEMORY_DIAG
launchd.development
RefWithNoPriority
  [->%@]
_objc_indexed_classes_count
 for ACTIVE TRANSACTION with
v36@?0I8I12I16I20I24^B28
/
%@ (translated)
Target process is using %s so not generating corpse for better performance.\n
couldn't find libsystem_malloc dylib in target task
x15
The memory graph file does not contain any labels for allocations.
$1: <$2>
RefFromNamedIvarPlusOffsetToObjectInterior
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime with stable ABI has been loaded
Thread %llu  %@
purgeable_nonvolatile_compressed
Chunk %s\n
RefToFakeNode
_protocol
vmRegionTracker
-[VMUGraphStackLogReader enumerateMSLRecordsAndPayloads:]
cfprefsd
_xpc_dictionary_get_transaction
__AUTH_CONST __objc_
seed
%sbinary plist:  %@
 Guard
coreservicesd
sysdiagnose
VMU
WTF::fastZeroedMalloc
diagnosticd
fp
Class[]
add child counts
AttributeGraph Owned
Could not get node for swift metadata allocation pool
 
_modelObserver
RESIDENT
VMUVMRegion.m
OS_xpc_pipe
_Tt
SWIFT_BUILTIN
SAMPLING_TOOLS_ALL_PROCESSES
============
pc
B16@?0@\"VMUVMRegion\"8
AGMallocZoneGetCurrentSwiftMetadata
MALLOC_PTR
VM_KERN_MEMORY_SKYWALK
SYMBOLICATION_DISABLE_WEBKIT_POINTER_PACKING_WORKAROUND
WTF::tryFastCalloc
MMIO
Gigacage::tryMallocArray
__TEXT
OS_dispatch_mach_msg
length
__NSMallocBlock__
CFStorageReplaceValues
OS_nw_array
.acquisitionProps
inline
Instances: %lu   Total bytes: %lu   Average bytes: %.1f   %@
unused but dirty shlib __DATA
VM_KERN_MEMORY_FILE
VMUCallTreeRoot
network_nonvolatile
nodeNamespaceSize
  no associated pthread
pas_msl_malloc_logging_slow
WTF::tryFastCompactAlignedMalloc
Size
__NSCFAttributedString
_supermenu
NONVOL
class_createInstance
^block parameters must be non-nil.
Selecting labels that have duplicates
region->firstBlockIndexOnPageArray
ORIGINAL: %s\n
OS_dispatch_source
VM_KERN_MEMORY_EXCLAVES
physFootprintPeak
Invalid IPS header: %@
Error. Compression failed.
DUPLICATE OBJECTS
Failed to create CSSymbolicatorRef, unable to determine cpu type for %s
v16@?0@\"VMUMutableClassInfo\"8
RefFromSwiftTaskOwnedFakeNode
EXCLAVEDRIVERKIT
VM_KERN_MEMORY_KALLOC_DATA
<couldn't read content>
 --> offset %llu
 (in %s)
__NSCFNumber
RefFromMergedGlobalsToAlignedInterior
toolsVersion
x2
0x%08x 
%s%s %s %u of %u  \"%s\"%s, of field \"%s\"  size %u stride %u\n
retainCount
VM_KERN_MEMORY_STACK
_NSThreadData
_observedObject
elements
Dispatch Thread %@ Limit: %u reached in %u of %u samples -- too many dispatch threads blocked in synchronous operations\n
  COPIED
 (%@)
-[VMUGraphStackLogReader copyOriginalUniquingTable:]
iokit_mapped
0!`
WTF::fastCompactMemDup
swift_reflection_createReflectionContextWithDataLayout
dispatch_mach_msg_t
Memory Tag %d
/usr/lib/system/libsystem_blocks.dylib
on dirty page  unused system shared lib 
vmu_create_backtrace_uniquing_table
B32@?0@\"NSString\"8Q16^B24
spindump_agent
%@  dirty: %s  swapped: %s
corpse
NSActionCell
ae
Zone %s\n
dirty
graphNodeCount
coalesceIdenticalRegions
VM_KERN_MEMORY_OSKEXT
int32_t
__NSConcreteUUID
%lu ADDITIONAL CHILDREN\n
  PRESENT
ALLOCATION
VM_KERN_MEMORY_UBC
VM_KERN_COUNT_MAP_KALLOC_LARGE_DATA
      POOL BOUNDARY\n
Setting region name in %s based on _zoneNames[_blocks[i].isa_index for  %s\n
[
%c%c%@%c
: 
VMUTaskMemoryCache initialization failed, likely because the target process no longer exists.\n
Class.data.properties (property_array_t)
PTR_REGION
__swift_concurrency_debug_asyncTaskMetadata
WTF::fastCompactStrDup
swift_reflection_destroyReflectionContext
SYMBOLICATION_LABELS_FOR_ALL_OSXPCOBJECTS
x26
TERM
%@ %@: '%@[]'
 in %@
RefFromLargeNonobjectToStart
RefFromKernelIntoUserSpace
pthread_rwlock_t
BaseClass
ALI
commonAddressBits
%@\n
PropertyList.Element Storage
_values
% FRAG
recordRegions
%9lu %9lu %9.1f   %s
<VMUArchitecture: %p> 0x%x,0x%x %@ - %@
zone: %s
task_start_peeking
RefFromPthreadStructToHottestAutoreleasePoolPage
VAS_DATA
srcAddressToExtraAutoreleaseCountDict
VMUProcessObjectGraph
v20@?0^{_VMUDirectedGraphEdge=III}8I16
q24@?0@\"NSString\"8@\"NSString\"16
has_sec_transition
unknown
%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s) } }\n
/usr/lib/libSystem.B.dylib
pthread_cond_t
archiving backtrace uniquing table
ReportPanic
NSLayoutAnchor
 %10s %10s %10s %7s
VM_KERN_COUNT_RESERVED
expected 1 binary in ExclaveCore target, but found %zu
JSC::tryAllocateAlignedMemory
%@ 
OS_dispatch_
%-36s  %-60s  %s\n
 %.*s:%@ 
SHRMOD
Key
GUARD
com.apple.lsd
os_transaction_get_description
[%.*f seconds] \"%@\"  Created at: %@
add remaining nodes to tree
!_autoreleasepoolBoundaryClassInfo
x18
SHM
Malloc zone count is %u but zoneIndex is %u for %@\n
WindowManager
id 
ulong
NSMenu
client
flags
pthread_mutex_t
x24
_objc_debug_autoreleasepoolpage_begin_offset
 %7s
options
NSTimer
icu::UnicodeSetStringSpan
RefFromNSCache
  DIRTY
Error in enumerating malloc zone %@ - allocation is excessively large: %#llx-%#llx[%llu].%s\n
i32@?0*8Q16Q24
-[VMUGraphStackLogReader populateBacktraceUniquingTableWithStackLogs:]
macOS
%d %@
%+*d: <extra space>[%u] (%s)
%*llx
dbMallocRawFinish
_zone
ObjC
unused 
lr
Error. Compression output buffer full.
%02x
_addEntryToMarkingRegion_block_invoke
Q16@?0Q8
SYMBOLICATION_EXCLAVES_INTROSPECTOR_FRAMEWORK_PATH
%u (%.2fK) %@
__swift_debug_allocationPoolPointer
Weak-With-Scannable-Owner-Pointer-Applied
  PAGED_OUT
VM_KERN_MEMORY_CPU
dispatch_queue_serial_num
%@ %s%@
MallocHelperZone_0x
0123456789ABCDEF
REFERENCES THAT WERE REMOVED:\n
VM_KERN_COUNT_MAP_ZONE
_objc_debug_indexed_isa_magic_value
[nodeToStackIdTable] nodeNamespaceSize %u  %lu bytes\n\n
-[%@ %s]: %s
\t
JSC::
invert rootLeakAddressToStackIDMap to produce stackID --> {size,count,root-leak-call-tree-root} map
-[VMUGraphStackLogReader initWithCoder:]
%#llx[%llu] --> %p[%llu] in %s  READ_BYTES CACHE MISS (VALIDATED)  -------------\n
 as '
C++
NSZombieEnabled
REGION TYPE
ShortVersionString
/System/Library/Extensions
_menu
 a
old_backtraces_contained - uniquing_table->backtraces_contained <= 1
Payload-
_swift_debug_nativeWeakReferenceMarkerValue
VM_KERN_MEMORY_HV
Firmware
ulong[]
/Foundation.framework|/libswiftFoundation.dylib
xpc_session_t
amfiBootArgsPresent
maxTimestampDelta
*** task_malloc_get_all_zones: can't get target task symbolicator\n
x19
  RECURSION COLLAPSED
Foundation
%u %s but no object content labels are available to determine the duration or description.
VMUVMRegionIdentifier.m
 REGION
Symbolication.framework _get_symbol_owner found requested symbol %s in unexpected Swift library %s\n
    %*s:  %s
$_0::operator()
error in %@ <classes> pattern '%@' - no starting bracket [: %s
[invalid usage]: %s\n\n
NSLayoutConstraint
count
ExclaveCore
graphics_footprint_compressed
/(Web(Kit|Core)|JavaScriptCore)\\.framework/
B28@?0I8I12I16*20
I24@?0Q8I16B20
%s (in %s)
<unknown>
STACK OF 
Detected no-payload of field %s, of object at %p of class %s. Treating as a non-payload case and not scanning the subfield.\n
Setting region name in %s based on enumeration range for  %s\n
[Binary Section Name Ranges] Count: %u  Uniqued string count: %u\n\n
i
Main Thread
__NSConcreteMallocBlock
%@_0x%qx
enumerating %@ by calling %@ in %@%s\n
<unknown binary>
ushort
clean
!_classMethodCacheBucketsClassInfo
%sGAP OF %#llx BYTES\n
__NSArray0
on dirty page  unused system shared lib __DATA
kernelmanagerd
_NSInlineData
\\n
[capture]
collectable_bytes
V=
WTF::fastStrDup
VMUAnalysisErrorKey
icu::UnicodeSet
memgraph refinement - remove lower-priority references
Unable to retrieve ledger template info in VMUProcessLedger
i24@?0^v8Q16
directedGraphInfo
__NSCFSet
VMUClassInfoMap.mm
%lu
{CGRect=
queueAlloc
%.0fK
__swift_debug_allocationPoolBackPointerOffset
NSMutableOrderedSet
SWIFT_STRUCT
%u:%u:%u
UnknownZone (%#llx)
_objc_debug_taggedpointer_obfuscator
_isaTranslator
/usr/lib/
OS_dispatch_semaphore
v44@?0I8{?=Qb60b4@}12^B36
Ozone
\n%*s
CONTENT:
Failed to generate corpse: %@ - examining live process instead
label: %.*s
%@:%u
building call tree from references
Cannot answer is64Bit for cpuType is %d cpuSubtype is %d
--
_callbacks
RefFromNamedGlobalVariableToAlignedInterior
CFType
_weakReference
value_field
VM_KERN_MEMORY_MTAG
populateUniquingTable get backtraces from libmalloc into our backtrace uniquing table
int64_t
v16@?0r^v8
couldn't get address of introspect structure symbol %s in %s
Memory graph has bizarrely high %s count %zu\n
WTF::fastCompactAlignedMalloc
xpc_array_t
%s RECURSION %u, LEVEL %u
_swift_concurrency
x1
sparseEdgeList
%d: %d -> %d%s\n
VMUBacktraceUniquing.c
VMULeakDetector
OS_xpc_data
RefFromAssociatedObjects
Field \"%s\" (type %s) has unrecognized kind %d\n
CNODE
NSManagedObjectID
malloc_bytes
WTF::tryFastMalloc
+
\nApple-internal options:\n
%-*u %@
targetMSLStatus
MALLOC_DATA
/usr/lib/swift/libswiftRemoteMirror.dylib
xpc_string_t
metadata
page_table
iOS
unscanned
%g
1@\"`
NO __DATA_DIRTY,__objc_imageinfo section in %s\n
targetPlatform
collectVMpageStatistics
page table in kernel
reallocf
_malloc_type
^{_CFStreamClient=}
toolsBuildVersionMonotonic
Bootstrap Dictionary
Frames
%llu   
*
 not
error in %@ <classes> pattern '%@': %s
ReadOnly portion of Libraries: Total=%s resident=%s(%.0f%%) swapped_out_or_unallocated=%s(%.0f%%)\n
Physical footprint (peak)
swift::swift_slowAllocTyped
ROOT CYCLE: 
uint64_t
Failed to map remote region: [%#llx-%#llx] %s %s (%llu %s)%s (error: %s)\n
Motion
unordered_map::at: key not found
__NSCFString
<couldn't read name>
length:remoteAddress:
x8
No duplicates detected
Metadata
subfield
EMPTY
mallocs
 [group up]
Gigacage::tryAllocateZeroedVirtualPages
OS_os_transaction
TOTAL
[Original Uniquing Table] %llu bytes\n\n
[Reference Details Large] Compact: %d Large: %d (%2.2f%%)\n\n
autoreleasepool boundary
(<
, std::char_traits<
fwrite
Dummy no payload field
(empty)
objectDetails
__DATA __objc
v20@?0r^I8I16
Date/Time:       %@\nLaunch Time:     %@\nOS Version:      %@\nReport Version:  %d\n
mapped file
__NSConcreteGlobalBlock
pseudo-isas for AsyncTasks and Slabs
WindowServer
target process is using %s which doesn't work with memory analysis tools
Class.data.methods.lists (method_list_t)
owned physical footprint (unmapped)
x12
reserved
Memory indirectly held only by autorelease pools
Process %d: %u object%s abandoned for %llu total abandoned bytes.\n
%@.*
/tmp/%@_%@_XXXX.sample.txt
sipDisabled
array_entries
VM_KERN_MEMORY_LTABLE
_swift_debug
[Symbol Store] \n\n
JS VM Isolated Heap
_owner
OS_dispatch_queue_serial
Sample analysis of process %d written to file %s\n
unloaded kmod %llu
[Region Symbol Name Ranges] Count: %u  Uniqued string count: %u\n\n
WTF::tryFastCompactRealloc
libgmalloc.B.dylib
@(#)
Q16@?0^{?=QQQQQQQQQQ}8
machine-wide VM submap
Hardware Model:  %@\n
swift_reflection_dumpInfoForMetadata
xpc_int64_t
__completion
%*s<< %u alignment bytes >>
%.*s...\n
DATA
JSC::tryAllocateMemory
::
Abandoned
OS_xpc_string
!_swiftMetadataClassInfo
exhaustible
C16@?0I8C12
WebKit
B24@?0Q8^{CSUserSuppliedSymbolData={_CSTypeRef=QQ}**QQ}16
VIRTUAL
<unknown connection>
[SourceInfo Ranges] Count: %u  Uniqued string count: %u\n\n
Leaks count
short[]
The DT_REPORT_IOKIT_REGION_LEAKS env var is set so leaked IOKit, IOSurface, or IOAccelerator regions will be reported, if -vmalso is passed to 'leaks'\n
__NSCFOutputStream
forward
childOfMetadata()
VM_KERN_MEMORY_%lld
x20
cuml_mallocs
_CFXNotificationObserverRegistration
OS_xpc_
vm.get_owned_vmobjects
Next enumeration range not contiguous with current
TouchBarServer
TOTAL FOR STACK
%@ %@
%#llx-%#llx[%llu]
@\"VMUMutableFieldInfo\"8@?0
*** getStackLoggingSharedMemoryAddressFromTask: can't get target task symbolicator\n
===========
process-only VM submap
v16@?0^{__CFRuntimeClass=q*^?^?^?^?^?^?^?^?^?Q}8
[Stack Log Reader - nodeToTimestampTable] nodeNamespaceSize %u  %lu bytes\n\n
__AUTH __objc_
  %@
NSConcreteMapTable
Metaclass.data (metaclass_rw_v2_t)
Bailing because field \"%s\" (type %s) has kind SWIFT_UNKNOWN\n
pthread_attr_t
Unable to get thread state for thread %u of remote process %d: %@\n
\"%@\"
PEAK FOOTPRINT
mach_kernel
select all dominator roots as roots of the tree
__NSSingleEntryDictionaryI
dispatch_data_t
unused __DATA
[Function Name Ranges] Count: %u  Uniqued string count: %u\n\n
 S=
getting node labels
NSData
Failed to get DYLD info for %@ with error %s (%d). Assuming it's a minimal corpse which can't be analyzed, which we sometimes see for processes which use a lot of memory.
target process may be using too much VM
Setting region name in %s based on enumeration for  %s\n
x:%g y:%g w:%g h:%g
_internalEdge
zone %s 
std::__
v24@?0@\"NSString\"8^@16
%@%@%@
VMUStackLogConsolidator
couldn't get introspect structure symbol name from %s
BigEndian
$1: $2
loginwindow
_Class
v24@?0@\"VMUFieldInfo\"8I16I20
\n\nIf after processing this memgraph with other cli tools and verifying the UUIDs you still see non-symbolicated addresses for '%@', please file a Radar to 'Symbolication | Xcode' and attach the memgraph, the dSYM and the non-symbolicated 
5!2
RefFromObjectToStart
Bad field index %u in document, count is %u
stackid
keys
%#llx is not in any region.  
deadNodes
swift_reflection_ownsAddress
Object
ALLOCATED
[VM Region Tracker] Region count: %u\n\n
swift_slowAlloc
stringSpan
libswiftRemoteMirror version or it wasn't new enough
%d %c
Thread %u  %s\n
%@ (%@)
NSDictionary
LAUNCHERDATA
VM: %@ (in %@)
error in malloc size pattern '%@': lower bound of size (%llu) should be <= upper bound of size (%llu)
_controlView
StrongSelfRefToLeak
                
 %*s %*s %*s
populateUniquingTable read stack log records
(VMUBacktraceUniquing) expandUniquingTable(): VMCopyFailed
v24@?0{_CSTypeRef=QQ}8
simpleSerializerData
Failed to project enum case for field %s (type %s), of object at %p of class %s. Falling back to conservative scanning.\n
Q16@?0r*8
_objc_debug_swift_stable_abi_bit
populateUniquingTable build map of address --> {nodeIndex,stackID}
Exited process
NSMenuItem
markIOSurfaces
VM_KERN_COUNT_WIRED_STATIC_KERNELCACHE
(root)
objectRefsListEntryPrev
%2.1f
STACK: 
[Region Data Extra] Count: %u\n\n
%qu
graphClassCount
owned unmapped
    %s %5d %s\n
WebKit Owned
\"
_sorted?  %s\n
%@  QOS %s
hidd
v32@?0@\"VMUMutableClassInfo\"8Q16@\"VMUTaskMemoryCache\"24
 (VERY BAD)
instance size %d, allocation size %d
no corpse slots are available
unused __TEXT
Compressed %s to %s (%2.1f%% reduction) in %3.6fs\n
Unable to unarchive `referenceDetailsLarge`.
 %8s
unowned
^{OSMetaClassPrivate}
region
hottestElided
media_footprint
SWIFT_ERROR_EXISTENTIAL
long long
CGFloat
VM: %@ fragmentation
v12@?0I8
--->  
Physical footprint:         %s\nPhysical footprint (peak):  %s\nIdle exit:                  %s\n
xpc_pointer_t
_repObject
VOLATILE
neural_footprint
operator_new_impl
_reserved
nextEmptyEntry
!_webkitOwnedClassInfo
gOSMetaClassBasePrivateLayout
__OBJC 
CoreFoundation
toolRespawnReason
%u block%s  %s bytes
_nextResponder
CFBundle
Failure calling sysctl to get proc buf
__DATA __objc_
[25i]
key
runningAsRoot
user-initiated
 __objc_imageinfo
TOOL_RESPAWN_REASON
VM_KERN_MEMORY_COMPRESSOR
root VM region
CYCLE BACK TO 
_CFXNotificationObjcObserverRegistration
_retainedController
step 3 -- from uniqueBacktraceToObjectsMap, create uniqueBacktraceToObjectsMap
error %@ reading num_zones at %qx
Memgraph is corrupt due to malloc zone enumeration failure. The malloc heap of the target process was in an inconsistent state such as when being modified.
Swift HeapGenericLocalVariable
\n\nIf after processing this memgraph with other cli tools you still see non-symbolicated addresses for some binary images, please file a Radar to 'Symbolication | Xcode' and attach the memgraph and the non-symbolicated output of interest.
identifying strongly-connected-components (cycles) in the graph
.*
swift_reflection_infoForInstance
xpc_connection_t
.internalProps
*** -[VMUTaskStackLogReader liteMSLPayloadforMallocAddress:size:] error %d from task_peek\n
llvm::BumpPtrAllocatorImpl
v28@?0I8I12I16^B20
Call graph:\n
pthread_rwlockattr_t
CFIndex
objc
threadNamesForThreadPorts
x5
_firstItem
previousRunloopsAndModes
Bad field index %u for subfield in document, count is %u
max_size
firstDominates
com.apple.
pat
SYMBOLICATION_LOG_SWIFT_REMOTE_MIRROR_MEMORY_READS
Version
v16@?0Q8
Nothing to symbolicate. This dSYM does not contain symbols for '%@' binary. For more information, please compare the UUIDs.
_NSModelObservingTracker
-[VMUProcessObjectGraphRefiner _findInterestingClassInfos]_block_invoke
JS VM Reservations
array_size
PTR_REGION  PTR_IN_USE
originalUniquingTableContents
AsyncTask Slab
_swift_debug_refcountIsSideTableMarkerValue
Physical footprint
int32_t[]
__NSSingleObjectSetI
__IncompleteProtocol
BadRefToCollectionClassStorage
0x0
File does not contain memory graph version information (not in correct format)
 | 
: %@
Hard
Unknown core region
char
const 
struct OSMetaClassPrivate
%-*s %@-%@ [%@] %s/%s SM=%s%@%@%@  %@
_dyld_process_has_objc_patches
Block %p [%llu] is %s\n
zone_array
v32@?0@\"VMUFieldInfo\"8Q16^B24
%#llx --> %llu  STRING_LENGTH CACHE HIT\n
transaction exists
%@ + %llu%@%@
unused  unknown system shared lib __TEXT
swift_reflection_asyncTaskSlabAllocations
    
   COUNT (non-coalesced)
\"%@
NSXPCInterface
watchOS
notifyd
UserEventAgent
pages
v16@?0@?<v@?Ii@?<v@?^v>>8
XAtomicAllocator::reserve(int)
pid_for_task(%x) failed with error %d: %s
__NSCFConstantString
_window
   DispatchQueue_<multiple>
[Binary Images List] \n\n
ARM64
classInfo.instanceSize >= tableOffset + tableSize
!_swiftTaskOwnedClassInfo
v24@?0*8@\"VMUVMRegion\"16
regionCount
 %llu
Memgraph file contained full stack log history header, but failed to store the actual stack log data.
counting allocations
DT_PRINT_NAME_SIMPLIFICATION
1
CFError
RefFromUnusedBinaryImage
Symbolication: could not read object label handler plist from %@
LiIcCqQsSfdB@*?#:^
binary
_value
RefFromNamedIvarToNonObjectInterior
%@ (%@)  %@  %@
VMUMemoryMarking.m
========
Failure calling sysctl to get buf size
hasRootsPresent
media_footprint_compressed
object
RefFromAttributeGraphFakeNode
%7llu
vmPageSize
 [group contain]
%@ -- failed to read content due to insufficient buffer length
\x83
tag
ProductBuildVersion
_CFXNotificationRegistrationContainer
BadRefToNonObjectTypedByIvar
VM_KERN_MEMORY_KEXT
vtable for 
inline content length %ld
    FAILED STRUCTURE TYPE ENCODING: %s\n
/(Speech[^/]*\\.framework|[^/]*(A|a)udio[^/]*\\.(framework|component|bundle|kext)|AppleHDA.kext)/
build tree from selected nodes
-[VMUDirectedGraph decapsulateSupplementalData:forTag:]
v20@?0I8*12
swift_allocBox
VM_KERN_COUNT_%lld
[Region Attributes Data] Count: %u\n\n
libswift_Concurrency.dylib
  %s:%u
compute dominators (%lu): changeCount = %lu, skipCount = %lu, lastChangedIndex = %ld
_edgeCapacity || (!groupEdges && !_edgeCount)
Swift.__
corpse creation encountered the unexpected error %s (%d)
bytes
PRT
v8@?0
__NSCFData
^{NSSliceExternalAcquisitionProperties}
SWIFT_THICK_FUNCTION
initObjectIdentifier
, Roots Present
__NSOrderedSetM
SWIFT_CLASS_EXISTENTIAL
has-length-byte
*** task_malloc_get_all_zones: error %@ reading zones at %qx\n
%.2f
IOLockAlloc
NSMutableSet
binary plist:  {
_swift_debug_nativeWeakReferencePointerIsSideTable
VM_KERN_MEMORY_MLOCK
nodeIndex < _graph.nodeNamespaceSize
OBJC_CLASS_$_%@
NSSet
_referenceItem
[Stack Log Reader - VM Region Tracker] Region count: %u\n\n
regionData
>
%u (%qu bytes) %@
fopen
Found SWIFT_UNKNOWN field \"%s\" (type %s) in class %s\n
CoreSymbolication failed to resymbolicate all symbol owners
_.([@
%u
/libclang_rt.asan
Stack of %@
DefaultMallocZone_0x
WTF::fastCompactCalloc
Failed to create CSSymbolicatorRef for pid %u %@
_gT1Sz
sepOS
edgeNamespaceSize
Duplicates count
: 0x
VMUAnalysisHeaderKey
_observer
_CFXNotificationObjectRegistration
_objc_debug_taggedpointer_mask
VMUObjectGraph.m
Showing object labels that have at least %lu duplicates.  Pass the \"-minimumCount <count>\" argument to change the threshold.\n
Symbolication_Internal_ForSwift.VMUAttributeGraphRegionIdentifier
creating symbolicator signature
, std::hash<
RefFromNamedIvarToNonObject
Peak physical footprint was %.2f times higher than current -- past memory use was much higher. This can be analyzed with the Allocations instrument
%s%s\n
Bailing because slab %p [%llu] does not fit inside container\n
_bytes
v32@?0@\"VMUMutableFieldInfo\"8Q16^B24
RefFromNoSymbolGlobalVariable
unknown type
___CFRuntimeClassTableCount
mediaplaybackd
objectRef
warning: kernel core support is highly experimental\n
Failed to read symbol data from the dSYM: '%@'.
libCoreLib.dylib
<deduplicated_symbol>
_bits
_objc_debug_autoreleasepoolpage_parent_offset
CMMMemMgr::New(unsigned long)
OS_xpc_uint64
strings_
RefFromWebKitOwnedFakeNode
B16@?0@?<B@?Q@\"VMUTaskMemoryCache\"^Q>8
_swift_debug_refcountIsSideTableMarkerMask
v32@?0@\"NSString\"8@16^B24
 Metadata
%u  stringID %u %@\n
SIZE
unsigned char
node
FirstTLSslotKey
CMMBase::NewInternal(unsigned long, CMMMemMgr&, char const*)
content length %ld  %s in VM:  %@
DT_PRECISELY_SCAN_SWIFT_SINGLE_PAYLOAD_ENUMS
%10qu
VM_KERN_COUNT_MAP_KALLOC
Reason: %@\n\n
couldn't find introspect structure symbol %s in %s
swift_reflection_infoForTypeRef
swift_reflection_childOfInstance
Error in enumerating malloc zone %@ - allocation is not in a VM region: %@ %s\n
%4d
alloc_size
VM_KERN_MEMORY_NONE
DT_SKIP_PRECISE_SCANNING_SWIFT_ASYNC_ALLOCATIONS
ledger
default.
v44@?0I8{_CSNotificationData={_CSTypeRef=QQ}(?={Ping=I}{DyldLoad={_CSTypeRef=QQ}}{DyldUnload={_CSTypeRef=QQ}})}12
v20@?0I8@\"NSString\"12
SWIFT_TUPLE
_swift_debug_nativeWeakReferenceMarkerMask
VM_KERN_MEMORY_LOG
regionAttributesData
[Thread Name Ranges] Count: %u  Uniqued string count: %u\n\n
v16@?0I8I12
_outlined
%s
_context
RefFromMergedGlobals
RefFromThreadStack
[Stack Log Reader - originalUniquingTableContents] \n\n
Cannot answer isLittleEndian for cpuType is %d cpuSubtype is %d
v24@?0I8^{?=QQ}12I20
 [root]
__SwiftNativeNSError
v40@?0{msl_disk_stack_logging_record=I{?=Q}QQ}8
%10llu  priority %u %s\n
%s[%d]: error: memory marking region could not be allocated\n
VM_KERN_MEMORY_LIBKERN
geo::MallocZoneAllocator::reallocate(void*, unsigned long)
CoreGraphics
powerd
BlockVariable
details
claimed region: [%#llx-%#llx] %s %s (%llu %s)%s - type '%s' range: [%#lx-%#lx]\n
%sUNUSED SPACE AT START\n
processGraphInfo
B12@?0B8
Allocations size
tagged pointer %@
refcount
compactEdgeList
VM_KERN_MEMORY_ZONE
peak
ExecutablePath
couldn't get framework name associated with the malloc zone
 %@PURGE=%c
VMUDirectedGraphToolCompatibilityVersionKey
[Dead Nodes Marking Map] Count: %u\n\n
unable to reinsert node when expanding backtrace uniquing table - bad hashing function?\n
NSTextInputContext
B32@?0Q8@\"VMUTaskMemoryCache\"16^Q24
0@ `
char[]
WebKit Malloc
v32@?0Q8@\"VMUClassInfo\"16^B24
swift_reflection_childOfMetadata
os_transaction_t
[Stack Log Reader - Function Name Ranges] Count: %u  Uniqued string count: %u\n\n
_malloc_num_zones
purgeable_nonvolatile
Value
v20@?0@\"VMUMutableFieldInfo\"8I16
...\"
transactions exist
com.apple.xpc.anonymous
/(AppKit|UIKit(Core))\\.framework|/libswiftAppKit.dylib
/(Core(Text|UI|Graphics|Video|Image|Media(IOServices)?|PDF)|ATS|ColorSync|ImageIO|Metal(Kit)?|OpenGL|Quartz(Core)?|QTKit|VideoToolbox|OpenCL|QD|IOSurface)\\.framework|/libswiftCore(Graphics|Image).dylib
v24@?0r^v8@\"NSError\"16
llvm::allocate_buffer(unsigned long, unsigned long)
LONG-LIVED XPC TRANSACTIONS
/usr/lib/system/libsystem_kernel.dylib
Getting fields for class %s\n
buildTrain
VMUScanTypeSwiftWeak
VMUVMRegionDomain
%@
Unable to create secure temp file\n
libclang_rt.tsan
Symbolication.framework _get_symbol_owner found requested symbol %s in unexpected non-Swift library %s\n
%-*llx
Q16@?0^v8
buildReferenceTree
_NSBindingInfo
*** Error: calling task_peek() before task_start_peeking()\n
network
thread %d
taskgated
pthread start routine argument
%.1fG
%u (%.0fM) %@
launchd
%lld bytes into %@
{unique_ptr<
NUL
%#llx  FAIL! STRING_LENGTH DID NOT FIND NULL TERMINATOR IN %llu BYTES FOR STRING LENGTH OF %.*s\n
RefFromNSMallocBlock
Duplicates total size
VMULeakDetectorDomain
^v
%#llx[%llu] --> %p[%llu]  FAIL! READ_BYTES CACHE HIT, BUT NEED TO MAP MORE\n
   DispatchQueue_%qu: %@  (%s)
childOfTypeRef()
PGZ
/usr/lib/liboah.dylib
r-x
std::enable_if
commpage
graphEdgeCount
symbolicateBacktraceUniquingTable
/S/L/PF/
%8llu  address %#llx  parent %u
WTF::tryFastCompactMalloc
streamLock
%10llu  TOTAL REFS\n
([fh offsetInFile] % 16) == 0
Unknown
swift_reflection_typeRefForMangledTypeName
\xb1
Thread %u::  %s\n
ownedPhysFootprintAdjustmentForMemgraph
_BaseClass
%@ pid %u [%s]
\xf0Q
%d
NSConcreteHashTable
kern.wq_max_threads
======
Base URL: %@;  
<unavailable>
-[VMUClassInfoMap _applyTypeOverlay:]
RefToChildAutoreleasePoolPage
CoreMedia
boardd
Unable to resume target task: %s (%d)\n
Class.data.protocols (protocol_array_t)
No process corpse slots currently available - waiting to get one\n
length: %lu  %@:  \"%@\"
unexpected configuration. leaks is expected to either run with library validation or to be debuggable
%@: %.128s...   SHA256: %@
 %10s
___CFRuntimeClassTable
 (malloc)
I386 Simple
Identifier
Kernel Pointers Into User Space
x29
/usr/lib/swift/libswiftCore.dylib
nonUTF8-binary-path
__NSDictionary0
Field is single-payload enum containing a pointer (with a nil representation of NULL). Treating as a struct and not varianting.\n
VM_KERN_MEMORY_OSFMK
VM_KERN_MEMORY_RETIRED
coresymbolicationd
VMUDirectedGraphDomain
Region state after claims:\n
s
___CFRuntimeClassTables
Protocol: %@
__weak
_Atomic 
libswift_Concurrency
taskStackLogReader
x4
@selector(%@)
remoteMethodsCount
v32@?0@8@16^B24
VMUSymbolStore
RefFromNamedIvarPlusOffsetToNonObject
Swift weak reference storage
_removeEntryFromMarkingRegion_block_invoke
NSLocale
[Backtrace Uniquing Table] %llu node capacity  %u nodes full  %llu bytes\n\n
x28
{RefCounts<swift::
[%.*s]
_CFXNotificationRegistrationBase
fields
%#llx[%llu] --> %p[%llu]  READ_BYTES CACHE MISS (UNVALIDATED)\n
__NSStackBlock__
{vector<
MAX
-[VMUDirectedGraph _dfsCore:colors:visitBlock:examineBlock:]
[%llu]
_target
OS_xpc_session
logd
processSnapshotGraph
xpc_serializer_t
$
kextd
node->refcount == 0
Build Info:      %@\n
info
___swift_reflection_version
DATA_CONST
FigBaseClass symbol name
VMUGraphStackLogReader
Found process %d (%s) from partial name %s\n
VMUHeapAndVMAggregator
__DATA
RefFromNamedIvarToObjectInterior
securityd
/System/Library/Frameworks/
Symbolication_Internal_ForSwift.VMUAttributeGraphTypeIdentifier
)
%s flag supplied with no argument
CFSet
__NSCFCalendar
%.*s%@\n
loaded %s for %@ introspection\n
reference
swift_reflection_classIsSwiftMask
%@ -- failed to read content due to memory allocation failure - is length reasonable?
<UNNAMED_%s_class_%#llx>
< binary images list unavailable >\n
VMUScanTypeExistential
RSDNT
[%@] Invalid task port provided to initializer.
swift_reflection_metadataNominalTypeDescriptor
  '%@'
VM_KERN_COUNT_MAP_KERNEL_DATA
StartRoutineOffsetKey
_swiftTaskAllocationBlockIndexes
\\((.+) in _([0-9A-Z]+)\\)
  scanType %s
charged to process physical footprint
JSC::IsoAlignedMemoryAllocator
_container
unused  unknown system shared lib
<unknown-symbol> %#qx + %qu
Process exited
BinaryInfoArchitectureKey
objectContentLevel
__NSFrozenArrayM
VMUProcessObjectGraphRefiner
.
SWIFT_ARRAY
rawValue
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR
archiving node labels
CFBundleShortVersionString
dispatch_group_t
zone
videocodecd
id
[Full Stack Log History] dataOffset: %llu  dataSize: %llu  %s\n\n
> 
<<couldn't convert to UTF8>>
OS_xpc_dictionary (Storage)
VM_KERN_MEMORY_KALLOC
1.2.12
NSBlock
SpringBoard
,...
server
malloc size pattern '%@' was not of expected format '[size]' or '[lowerSizeBound-upperSizeBound]'
v16@?0i8B12
v24@?0r*8@\"NSString\"16
failed to resolve canonical path for %s in dyld shared cache.
 OBJECTID
< content unavailable >\n
swift_reflection_metadataForObject
swift_reflection_dumpInfoForInstance
inline 
VMUSimpleSerializer.mm
VM_KERN_MEMORY_WAITQ
binaryImagesDescription
v36@?0Q8@\"VMUClassInfo\"16I24^B28
SourceVersion
regionSymbolNameRanges
additionalProperties
SwiftNativeNSObject
_viewController
DYLD_IMAGE_SUFFIX
___mach_stack_logging_shared_memory_address
metaclass for %@
-[VMUClassInfo encodeWithCoder:]
%@  %@  %#qx%@
couldn't open %s for reading call tree\n
_AGMallocZoneGetCurrentSwiftMetadata
threadAndDispatchQueueName
*** getStackLoggingSharedMemoryAddressFromTask: couldn't find ___mach_stack_logging_shared_memory_address in target task\n
File is missing metadata required for analysis.
%3llu%%
symbol name not found
_0x
invalid task corpse info provided to VMUProcessLedger
/usr/lib
!_attributeGraphOwnedClassInfo
native
  CS_NX
___kCFBooleanTrue
SInt32
archiving region data
[fh offsetInFile] == supplementalHeaderOffset
Process:         %@ [%@]\nPath:            %@\nLoad Address:    %#qx\nIdentifier:      %@\nVersion:         %@\n%@Code Type:       %@\n%@Parent Process:  %@ [%@]\nTarget Type:     %@\n
pattern
VMUDirectedGraph.m
Unable to initialize compression stream.
Usage: %s %s\n\n
__NSDictionaryM
Swift.
KEEP-BOUNDARIES PLACEHOLDER
Unicode
%+6lld: %s%s
x11
<unclaimed>
SWIFT_MULTI_PAYLOAD_ENUM
%s in analysis process, for %s in target process
wired_mem
swift_reflection_dumpInfoForTypeRef
OS_dispatch_queue
value
TEXT
didPhysFootprintDirtyAccounting
[nodeToMSLPayloadTable] nodeNamespaceSize %u  %lu bytes\n\n
configd
oah_get_runtime_location
PreserveMemgraphSampleAndSymbolStore
%#llx FAIL! STRING_LENGTH COULD NOT MAP, ALTHOUGH FOUND REGION %s\n
NULL
SWIFT_UNMANAGED_REFERENCE
[Node Labels] Count: %u  Uniqued string count: %u\n\n
double[]
%@%@ --> %@
NSDragDestination
reverse
backtraceUniquingTableSize
vtable
REGION DETAIL
AttributeGraph
Nothing to symbolicate. All addresses in the memgraph are already symbolicated.
v16@?0^{dyld_image_s=}8
ARM64_32
Payload-Empty
%@  %#llx
No malloc zones in target process\n
Setting region name in %s based on malloc zone structure address for  %s\n
NSResponder
-[VMUProcessObjectGraphRefiner isBadReferenceToCollectionClassStorage:]
%s analysis of pid %u reached time limit of %llu seconds, exiting.
/usr/lib/((lib[^/]*\\.dylib)|dyld|system)|/libswift(Darwin|Dispatch).dylib
vm_dirty
collectVMpageStatistics: error in mach_vm_page_range_query: %s\n
 SIMPLER: %s\n
RefFromNonobjectToAlignedInterior
RefFromNonrootVMRegion
[srcAddressToExtraAutoreleaseCountDict] Count: %u\n\n
x7
RefFromUnalignedSourceToUnalignedInterior
allProcessesMode
GPU Carveout (reserved)
COW
pruning tree to matching nodes
_table_addStorageBlock
background
swift_reflection_copyDemangledNameForTypeRef
icu::UVector32
NSConcretePointerArray
Weak-With-Unscannable-Owner-Pointer-Applied
VMUTaskMemoryCache
anonymous
^@\"IODispatchQueue\"
enumerate stack logs to populate rootLeakAddressToStackIDMap
NSCalendar
__NSCFBoolean
VMUTaskErrorDomain
_swift_debug_nativeWeakReferencePointerMask
libswift
archiving VMUObjectGraph and VMUDirectedGraph
[Thread Name For Thread Ports] Count: %u  Uniqued string count: %u\n\n
VMUTraceTreeAnalyzer.m
__typed_operator_new_impl
Region
Fig Subclass
Data parameter cannot be nil.
vmu_create_backtrace_uniquing_table_from_archive
OS_object
content length %ld  %s + %llu in VM:  %@
kernelcache combined __LINKEDIT
tvOS Simulator
/S/L/
VMUDirectedGraphCompatibilityVersionNumberInGraphKey
Gigacage::mallocArray
fixupCoreRegions
 %s
sysctl.proc_cputype
/usr
VMUMallocZoneAggregate.m
scan for leaks
version
^{NSSliceExternalPersonalityProperties}
 Aborting
VMUObjectLabelHandlers
scan nodes into the graph, while recording symbols of __DATA regions and stacks
cameracaptured
internal
Memory graph file content is obsolete development version, no longer supported\n
DISKLOGS
Error occured while printing autoreleasePools per thread.\n
Q
ExclaveKit
couldn't create symbolicator for %s
/S/L/F/
__AUTH_CONST
Thread
%@: %s
%@  %@  %@
%@  %@:%u
???
sqlite3MemRealloc
ROOT LEAK: 
(ROOT LEAK|CYCLE): 0x[0-9a-f]+ \\[(.*)\\].*
swift_reflection_childOfTypeRef
icu::UVector
v24@?0@\"VMUVMRegion\"8^B16
STACK
NO STACK\n
xpc_uint64_t
*** Can't suspend task %d: %s\n
_objc_debug_isa_magic_value
SWAP
dominators
com.apple.dt.Symbolication.VMUDirectedGraph
Malformed non-compressed header
Total number in stack (recursive counted multiple, when >=%d):\n
short
systemsoundserverd
Invalid bug type in IPS header.
(VMUBacktraceUniquing): Invalid parent node %#x\n
nodeToTimestampTable
VMUScanTypeConservative
Illegal attempt to scan memory of mach_task_self()
---
: VM: 
Not creating classinfo for zero-sized AttributeGraph value\n\n
Total memory of autorelease pools and content blocks
%u (%.1fK) %@
@\"NSString\"40@?0@\"VMUObjectLabelHandlerInfo\"8^v16Q24Q32
Unique entries in autoreleasepools
WTF::fastCompactMalloc
%@-%@-%@-%@-%@
_TtCs12_SwiftObject
content length 0
NO-FIELD  
malloc<%llu>
VMUScanTypeExactUnowned
0x%qx
OS_xpc_int64
DT_DO_NOT_PRECISELY_SCAN_SWIFT_MULTI_PAYLOAD_ENUMS
Object_id=
libswiftRemoteMirror.dylib
[Stack Log Reader - SourceInfo Ranges] Count: %u  Uniqued string count: %u\n\n
char*[]
%s  %@-%@ [%@] %s/%s  %@
Autorelease pool pages not associated with a thread\n
[@@@spacing@@@]%@
OS_xpc_double
%#llx[%llu] --> %p[%llu]  READ_BYTES CACHE HIT\n
DT_PRINT_FIG_SUBCLASSES
_objc
childPageOffset
Class
TPRO
v28@?0@\"VMUFieldInfo\"8@\"VMUFieldInfo\"16I24
Gigacage::tryAlignedMalloc
OS_dispatch_group
v20@?0I8B12I16
COUNT
kernPageSize
SYMBOLICATION_SHOW_BACKTRACE_TIMINGS
, Specific
graphIs64bit
%#llx
list
Kernel generated only a minimal corpse with error %s (%d) - examining live process instead
LEAKS
c
re
_objc_debug_autoreleasepoolpage_child_offset
_objc_debug_indexed_isa_magic_mask
SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Runtime with stable ABI has already been loaded, ignoring this other one.
internalized node
_blocks
Failed to create VMUProcInfo for pid: %d
{shared_ptr<
LittleEndian
-[VMUTaskMemoryScanner _initializeRegionMallocBlockCounts]
nonsensically small offset for field \"%s\" of +%u%s; ignoring all fields in this closure context\n
Swift reflection is unavailable. All Swift content will be scanned conservatively.
/(JavaVM|Ruby|Python|Tcl|Tk)\\.framework/|/ruby/|/lib(tcl|tk|python|perl|swiftCore|swiftObjectiveC|c\\+\\+abi)[^/]*\\.dylib
        Empty\n
Failed to find the binary in the dSYM: '%@'. %@\n
_dispatch_continuation_alloc_from_heap
-[VMUSimpleSerializer serializeNullTerminatedBytes:]
SYMBOLICATION_LOG_SWIFT_UNKNOWN_FIELDS
allProcesses
 %8zx
NSNumber
storage
Value has size %llu, but Remote Mirror reports a size of %u.  Ignoring Remote Mirror output and scanning conservatively.\n
 %s[%u]
swift_reflection_projectExistential
flatten
*** Error: calling task_try_peek() before task_start_peeking()\n
Memory Scanning
VM_KERN_MEMORY_ANY
asyncLength
uchar[]
geo::MallocZoneAllocator::allocate(unsigned long, unsigned long)
OSObj
Found cached field \"%s\"\n
site
  type %s
NSConcreteMutableData (Bytes Storage)
q24@?0@8@16
ProjectName
B32@?0Q8@\"VMUTaskMemoryScanner\"16@\"VMUTaskMemoryCache\"24
[__block capture]
entryIndex < region->entry_capacity
_getRegionMallocStatistics_block_invoke_3
Unable to initialize deflate: %d (%s)
enumerating references for guessNonObjects
largest
error %@ reading zones_address at %qx
/CoreData\\.framework/|/libsql[^/]*\\.dylib|/libswiftCoreData.dylib
[fh offsetInFile] == supplementalDataOffset
no associated pthread
sqlite3MemMalloc
%8u
os_transaction_get_ra
[Exclave Flag Data] Count: %u\n\n
introspect structure %s for the malloc zone has invalid enumerator function address %#llx in %s
AttributeGraph graph data
RefFromUnalignedSourceToAlignedInterior
=====
DART_CNODE
__NSGlobalBlock__
%c
SWIFT_RAW_POINTER
\"file://
 -- loaded from target process
PPC
X86-64
NSHashTable
_refcounts
OS_nw_frame
_keys
==== REMOVED %llu JUNK EDGES OUT OF %llu  (%2.2f%%) ====\n
malloc-block (possibly Swift)
xpc_activity_t
icu::number::impl::DecimalFormatFields
Thread_%qu
imageOffset
neural
targetIsTranslated
VMUObjectIdentifier.m
This platform cannot map in the memory graph plist at offset %llu of size %llu
shortVersion
_rawValue
RefToUnalignedInterior
libgmalloc.dylib
markOthers
VMUBacktrace (Flavor: %@ Time: %llu Process: %d Thread: %X  Dispatch queue serial num: %lld)\n
Unable to deserialize the memgraph %@
VM:
%#llx  FAIL! NO VM REGION FOR STRING LENGTH\n
Exclave memory tag %hhu
v32@?0@\"VMUAnalyzerSummaryField\"8Q16^B24
exclave
```
