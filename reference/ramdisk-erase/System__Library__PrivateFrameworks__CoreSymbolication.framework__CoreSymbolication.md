# `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,696,064 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3936)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1)`
- `/usr/lib/libRosetta.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (3 classes, 0 protocols)

Classes: `CSMemoryMapping`, `CSMemoryMappingCache`, `CSMemoryMappingSlice`

## Strings (1,453)

```
CSMemoryMappingSlice
CSMemoryMapping
CSMemoryMappingCache
getCoreFileLedgerNetworkNonvolatile:
getTaskThreads:count:error:
resumeTargetWithError:
TB,R,N,V_isBackedBySelfTask
existingMappingForAddress:size:fullyContainedOnly:
getCoreFileLedgerIokitMapped:
getCoreFileLedgerMediaFootprintCompressed:
getCoreFileLedgerNeuralFootprintCompressed:
getCoreFileUserstack:
enumerateCoreFileDumpedRegions:
Tr^v,R,N
_purpose_label
coreFileMachVmPurgableControlForAddress:control:state:
localMappedAddress
setRegionInfoBlock:
_dsc_range
coreFileIsExclave
getCoreFileLedgerMediaFootprint:
_total_mapped_size
getCoreFileLedgerNetworkNonvolatileCompressed:
readPointerFromAddress:outValue:
setMappingRangeOverrides:overrideCount:
suspendTargetWithError:
getCoreFileExclaveVmFlagsForAddress:exclaveVmFlags:
getCoreFileLedgerInternalCompressed:
getCoreFileLedgerWiredMem:
getCoreFileProcFlags:
initWithBytes:length:encoding:
initWithUnderlyingMapping:remoteStart:remoteSize:
is64Bit
_dsc_slide
_target_page_size
_touch_regions
getCoreFileOwnedVmObjects:ownedObjectsByteCount:
remoteBaseAddress
coreFileRegionFilenameForAddress:
getCoreFileProcArgc:
initWithName:reason:userInfo:
initialize
getCoreFileLedgerPhysFootprint:
coreFileMachVmPageRangeQuery:size:dispositions:dispositionsCount:usePhysFootprint:error:
coreFileProcName
getCoreFileDirtyFlags:
initWithDomain:code:userInfo:
underlyingMapping
unsafeBytesForAddress:size:outTrailingSize:
localAddressForRemoteAddress:
mappingForAddress:size:error:
withBytes:
_suspension_count
copyBytesFromAddress:size:to:error:
coreFileIsExclavecore
errorWithDomain:code:userInfo:
getCoreFileLedgerInternal:
getStateForThread:flavor:oldState:oldStateCnt:error:
sliceFromAddress:
.cxx_destruct
_lock
getCoreFileLedgerAlternateAccounting:
_core_file_metadata
T@\"CSMemoryMapping\",R,N,V_underlyingMapping
TQ,R,N,V_size
_accessCount
_remoteSliceRange
coreFileParentProcName
dictionaryWithObjects:forKeys:count:
enumerateMappingsWithBlock:
_size
getCoreFileLedgerPhysFootprintLifetimeMax:
getCoreFileLedgerPurgeableNonvolatile:
initWithoutExclaveMetadataForCoreFileWithPath:label:error:
isBackedBySelfTask
sliceFromAddress:size:
TQ,R,N,V_localMappedAddress
TQ,R,N,V_remoteBaseAddress
coreFileParentProcPath
getCoreFileLedgerAlternateAccountingCompressed:
init
size
coreFileMachVmRegionRecurseSubmap64:size:nestingDepth:info:error:
getCoreFileLedgerTaggedFootprintCompressed:
getCoreFileProcStarttimeSec:
getMappedMemoryCacheForTask:purposeLabel:
remoteRange
TQ,R,N
_count
getCoreFileDyldSharedCacheRange:
getCoreFileLedgerTaggedFootprint:
mappingSliceForAddress:size:error:
unsafeBytes
unsafeBytesForAddress:size:
getCoreFileDyldAllImageInfosAddr:
withBytesFromAddress:size:block:
dealloc
getCoreFileArchitecture:
getCoreFileProcStarttimeUSec:
stringWithUTF8String:
T{_CSRange=QQ},R,N
_is64Bit
_region_info_block
copyBytesFromAddress:size:to:
getCoreFileLedgerPageTable:
releaseMappedMemoryCacheForTask:
TB,R,N,V_is64Bit
.cxx_construct
_suspension_token
coreFileHasInfoForMemoryAnalysis
getCoreFileLedgerNeuralFootprint:
initWithTask:touchMappedRegions:label:
T@\"NSString\",R,N
getCoreFilePPid:
getCoreFilePid:
clear
code
coreFileMachVmRegionRecurseSubmapShort64:size:nestingDepth:info:error:
getCoreFileLedgerPurgeableNonvolatileCompressed:
lengthAfterAddress:
_mapping_range_overrides
_underlyingMapping
getCoreFileAddressingMask:
initWithCString:encoding:
initWithCoreFilePath:label:error:
UTF8String
_isBackedBySelfTask
_remoteBaseAddress
_targetAddressMask
stringWithFormat:
_root_map
getCoreFileLedgerGraphicsFootprint:
getCoreFileLedgerGraphicsFootprintCompressed:
tryGettingUnsafeBytesForAddress:size:
TB,R,N
lookUpMappedMemoryCacheForTask:
_task
coreFileProcPath
_addressMask
_reclaimed_nodes
getCoreFileArgsLen:
getCoreFileUdataPtrs:udataPtrsCount:
_localMappedAddress
initWithTask:touchMappedRegions:
B24@0:8^i16
v32@0:8^{?={_CSRange=QQ}BB}16Q24
Q16@0:8
{_CSRange=QQ}16@0:8
r^v40@0:8Q16Q24^Q32
Q24@0:8Q16
B16@0:8
B
@32@0:8I16B20@24
v40@0:8Q16Q24^v32
v16@0:8
{_CSRange=\"location\"Q\"length\"Q}
@40@0:8@16@24^@32
@24@0:8I16B20
@36@0:8Q16Q24B32
i32@0:8Q16^Q24
B40@0:8^^I16^I24^@32
@16@0:8
r^v32@0:8Q16Q24
B56@0:8^Q16^Q24^I32^{vm_region_submap_short_info_64=iiIQIISCCiiISS}40^@48
B36@0:8Q16i24^i28
B24@0:8^{_CSArchitecture=ii}16
{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}
{unique_ptr<CSCppCoreFileMetadata, std::default_delete<CSCppCoreFileMetadata>>=\"\"{?=\"__ptr_\"^{CSCppCoreFileMetadata}}}
@40@0:8@16Q24Q32
@24@0:8Q16
@\"CSMemoryMapping\"
@32@0:8Q16Q24
B56@0:8^Q16^Q24^I32^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQISS}40^@48
B60@0:8Q16Q24Q32^Q40B48^@52
B32@0:8^{?=Q[0{?=QQQQQQ{?=b1b3b2}}]}16^Q24
B24@0:8^I16
Q
@28@0:8I16@20
v20@0:8I16
B24@0:8^{_CSRange=QQ}16
@\"NSString\"
B24@0:8^@16
@40@0:8Q16Q24^@32
B48@0:8Q16Q24^v32^@40
B48@0:8I16i20^I24^I32^@40
B24@0:8^Q16
B32@0:8Q16^I24
{optional<unsigned long long>=\"\"(?=\"__null_state_\"c\"__val_\"Q)\"__engaged_\"B}
{OrderedMemoryMappings=\"_map\"{set<CSMemoryMapping *, CompareMappedRegionNode, std::allocator<CSMemoryMapping *>>=\"__tree_\"{__tree<CSMemoryMapping *, CompareMappedRegionNode, std::allocator<CSMemoryMapping *>>=\"__begin_node_\"^v\"\"{?=\
v40@0:8Q16Q24@?32
v24@0:8@?16
{vector<CSMappingRangeOverride, std::allocator<CSMappingRangeOverride>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}
{vector<CSMemoryMapping *, std::allocator<CSMemoryMapping *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}
@?
r^v16@0:8
I
@20@0:8I16
B32@0:8^Q16^Q24
Caught exception in sample_remote_thread_with_frame_filter for pid %u: %s\n
SYMBOLICATOR %p CREATING SYMBOL OWNER DATA: %s\n
Out of bounds compile unit\n
Caught EXC_BAD_ACCESS at 0x%llx, valid page mapping, page query flags (0x%x)\n
[Invalid macho header] dylib load command name offset is invalid
Found matching kernel in %s\n
Failed to parse flatbuffer conformant json string -- likely the JSON is not formatted correctly\n
SYMBOLICATOR %p CREATED BY CSSymbolicatorCreateWithSymbolOwnersAndCSCppTask\n
CSCppMachTaskContainer task_for_pid failed for process %u, err %d
No string extracted from DWARF5 path list
get_remote_thread_dispatch_queue2 thread_info(THREAD_EXTENDED_INFO) call failed for pid %u thread %u, err %d
UUID found in both ExclaveCore and ExclaveKit\n
memory.address() [%p] should equal memory.mapped_region() [%p]... possible unexpected offset?
[Invalid macho header] size of load commands overflow
Provided dSYM: [%s] does not match symbol owner %p\n
Unable to determine architecture of the kernel
Malformed fat header\n
DWARF %d form %u is unrecognized for reading non-indexed ranges.\n
Out-of-bounds abstract origin or specification offset
Source info %s [%llx -> %llx) outside of relocations in mmap SOD\n
Error reading kernels directory: %s\n
Transformed binary is invalid
[Invalid macho header] no load commands
[Invalid macho header] inadequate sections size
Fat header is malformed\n
Sampling current thread of current analysis process is not safe - ignoring requesting to do so\n
Couldn't find a valid DSC header in mapped range %llx - %llx
Segments in dSYM [%s] could not be matched to task header\n
Missing page in pid %d, checking for second frame failed, err code %d\n
failure while allocating exception port: %s\n
The archive's size is too small. A malformed file? \n
[header: %s] Ignoring '%.16s %.16s' section [%#llx-%#llx] not contained in '%.16s' segment range [%#llx-%#llx]\n
FAILED: dyld %s of %s\n
Mmap string table has reached its maximum size of 4G. Mmap archive will not be created\n
CSSymbolicatorCreateWithCSCppMachTaskFlagsAndNotification exception failure: %s
Found running kernel dummy entry.\n
Error during directory iteration: %s \n
Failed to find symbolicators in flatbuffer created from JSON\n
No symbol owners pointer in flatbuffer\n
[Invalid macho header] dylinker load command is too small for content fields
Corrupt archive entry in %s -- no acceptable header found for entry %s\n
[Invalid macho header] minimum load command overflow
Empty function_name in mach-o header: %s\n
Historical timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
Out of bounds children index iterating inline ranges
Unable to create process info for pid %d, task %d. Is dyld loaded for this binary yet?\n
Failed to mmap %s\n
[Invalid macho header] load command out of bounds
[Invalid macho header] sections size overflow
Unable to create any kext symbol owners.\n
[Invalid macho header] function starts load command is too small for content fields
Attempting to map range %llu-%llu length %llu past end of file %llu in: %s\n
Compile unit with bad address_size\n
SAMPLING_SAMPLE_BOTH_REGULAR_AND_SWIFT_ASYNC will override SAMPLING_IGNORE_SWIFT_ASYNC
Invalid analyzed archive entry for object file %s from archive %s at offset 0x%llx\n
TEXT_text_location %llx outside of relocations in mmap SOD\n
error handling EST message: %s (%u)\n
Failed to locate official Exclave Kit binaries on disk
[Invalid macho header] minimum load command goes beyond bounds
[Invalid macho header] section size overflow
[Invalid macho header] symtab load command is too small for content fields
Missing page in pid %d, create of symbol owner data for [%s] failed, err code %d\n
Possible reference cycle in DIE
thread_info failed due to %s
SYMBOLICATOR %p DESTRUCTED\n
[CoreSymbolication] In DWARF data from %s:\n  .debug_line[%llx] file = %d is not a valid index\n
Failed to load flatbuffer symbols schema file
[Invalid macho header] inadequate segment load command vm size
%s -- stopping DWARF analysis of %s\n
Failed to find matching kernels in %s\n
Failed to read dyld info for process %d (%d)\n
Unsupported compile unit type\n
Could not remap archive address to real in debug maps
Symbol %s [%llx -> %llx) outside of relocations in mmap SOD\n
Failed to relocate address %#llx in flatbuffer SOD
Failed to start process notifications for pid %d (%d)\n
Caught exception in get_remote_thread_dispatch_queue2 for pid %u: %s
Child symbol archive address 0x%x could not be relocated to real address\n
Unable to create symbolicator from dyld compact info for pid: %d. Shared cache UUID is missing\n
[Invalid macho header] fileset entry load command is too small for content fields
[Invalid macho header] inadequate sum of sections size
Unexpected DWARF version parsing DW_AT_ranges: %d\n
Remapped bytes from target are not valid at %#llx
Unexpected number of symbol owners in flatbuffer created from JSON: %u\n
Missing page in pid %d, read of header data for [%s] failed, err code %#x\n
Missing page in pid %d, sampling of thread failed, err code %d\n
Path is not a directory: %s\n
[Invalid macho header] inadequate size of a load command
[Invalid macho header] dylib load command is too small for content fields
Failed to parse flatbuffer symbols schema
[Invalid macho header] load command size overflow
Could not remap archive address to real in debug maps inline enumeration
Client side event: Unhandled xpc type\n
[Invalid macho header] segment load command is too small for content fields
[Invalid macho header] unreasonable number of sections
[Invalid macho header] section not contained in segment
Attempt to relocate address [0x%llx], which is outside segment deltas\n
Unable to determine a special slide 1.
Unable to access flatbuffer symbols schema at %s
Connection invalidated: %s\n
pid %d Failure reading CFI info at %s\n
Unable to create symbolicator from dyld compact info for pid %d.\n
[Invalid macho header] uuid load command is too small for content fields
[Invalid macho header] dylinker load command name offset is invalid
Caught exception in %s:\n %s\n
Failed to get dsc path for task\n
Attempt to mmap %s failed, %s\n
Symbol archive address 0x%x could not be relocated to real address\n
The archive's version is not supported. A malformed file? \n
[Invalid macho header] load command at %#llx goes beyond bounds
Corrupt macho header at %#llx\n
Failed to access directory: %s\n
[Invalid macho header] source version load command is too small for content fields
Bad abbrev table offset in compile unit\n
Unable to determine special slide 2.
Could not read UUID of running kernel\n
sample_remote_thread_with_frame_filter failed to get thread state for pid %u thread %u
Requested vm range length in %s does not exist in file.\n
Unable to determine kernel slide.
Succesfully created kext symbol owners.\n
%s parsing abbrev table -- stopping DWARF analysis of %s\n
Ref addr is not within the bounds of any compile unit
get_remote_thread_dispatch_queue2 thread_info(THREAD_IDENTIFIER_INFO) call failed for pid %u thread %u, err %d
Unable to acquire mach service port, symbol cache unavailable\n
[Invalid macho header] dysymtab load command is too small for content fields
Empty object_file_path in mach-o header: %s\n
Failed to create mmap archive: %s\n
Region %s [%llx -> %llx) outside of relocations in mmap SOD\n
Timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
Cursor overflow, attempt to skip FORM_block2
`vector64` attribute can only be applied on vectors.
x23
libsystem_kernel.dylib
FBS
The value of the argument index exceeds its maximum value
DW_FORM_indirect not handled yet... 
create_mmap_archive_arch_specific (TEXT_text) -- UUID: 
bit flag out of range of underlying integral type
struct
/System/Volumes/Data/SWE
DriverKit
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppReferenceCount.hpp
<deduplicated_symbol>
kCSNow
original_order
rpc request and response types must be tables
unknown field: 
NULL
dyld
armv7s
__LINKEDIT
[Invalid macho header] inadequate sections size
MangledNameSourceNlist, 
value
The type option contains an invalid value for 
\\\\
/System/Library/dyld/
force_align
Stack empty for DW_OP_drop
DW_OP_div divide by zero
unique_lock::lock: already locked
Union defaults must be NONE
id
Cannot assign token starting with '
0123456789-+.
streaming
_Z
attempting to access outside bounds of CSMemoryMappingSlice
ltmp
SYMBOL OWNER: %s\n
%@\n
NameValid, 
DebugMap, 
<CSSymbolicator: %p> %s (pid:%d%s) {\n
MangledNameAllocated, 
liblibc_plat.dylib
Attempt to release an unhandled typeID
\t%zd entries, %zdMB footprint\n
<Invalid file path>
OSBundlePath
escape code must be followed by 
float32
Integral value outside the range of the char type
v44@?0B8Q12Q20r*28r*36
Requested vm range length in %s does not exist in file.\n
Empty function_name in mach-o header: %s\n
Union
__TEXT __stub_helper
_objc_msgSend
__PLK
System
x86_64
any
<Invalid filename>
UNLOAD
%s/%s
Optional scalars are not yet supported in at least one of the specified programming languages.
native_default
DW_OP_skip has invalid opcode offset
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
/private/preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
[Invalid macho header] inadequate sum of sections size
%u.%u
__OBJC_RW
_type
\\'
<CSSourceInfo: %p> [0x%016llx -> 0x%016llx) %s:%d
i386
v24@?0r*8Q16
$s
only a non-optional scalar field can be used as a 'key' field
archive_shmem
__text
r9
Stack size less than 2 elements for DW_OP_mod
arm64e
Cursor overflow, attempt to read ULEB
bitset reset argument out of range
TEXT_text_location %llx outside of relocations in mmap SOD\n
Failed to parse flatbuffer conformant json string -- likely the JSON is not formatted correctly\n
The replacement field misses a terminating '}'
DW_OP_bregx: No read register callback provided
v32@?0r^v8Q16Q24
__TEXT SEGMENT
Unknown conversion function: 
Stack size less than 2 elements for DW_OP_and
The archive's size is too small. A malformed file? \n
keyPC
DW_OP_reg: No read register callback provided
Type
Unexpected number of symbol owners in flatbuffer created from JSON: %u\n
all image infos
Expected `]` in vector default
__FAILED
kCSSymbolOwnerDataFoundDsym
ubyte
dyld_shared_cache
x7
__DATA
__OBJC_CONST
v56@?0{mapped_memory_core_file_dumped_region_info_t=QQQQii}8^B48
root_type
memory read of %u bytes at address 0x%8.8llx failed: %s
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppCFDataMemory.cpp
warning: 
could not open file, or it is not a Mach-O core file
 | 
__debug_str
%s%s
Attempt to mmap %s failed, %s\n
%s parsing abbrev table -- stopping DWARF analysis of %s\n
\t%s: %s (%llu)\n
CSCppTaskMemory: retired memory must be contained by live memory
r12
_start_wqthread
Process exists but _dyld_process_info_create() failed with error %#x
Unhandled form in read string binding 
txm
Stack size less than 3 elements for DW_OP_rot
v16@?0^v8
Error decoding symbolicator from signature
The precision option does not contain a value or an argument index
.
.eEpP
r0
DW_OP_breg: No read register callback provided
CS_TEST_EXCLAVECORE_DIR
field id's must be non-negative number, field: 
x2
type must be integral
all enum values must be unique: 
file_extension
fnv1a_16
[Invalid macho header] unreasonable number of sections
%u.%u.%u
, field name: 
The fill option contains an invalid value
ArithmeticException
v16@?0r^{CSCppDyldSharedCache=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b1b19QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQIIQQQQIIQ}8
, raw_TEXT_text_section: (
either all fields or no fields must have an 'id' attribute
<Invalid region name>
fixed-length array in table must be wrapped in struct
\"
x18
com.apple.coresymbolicationd
/System/Library/Caches/com.apple.dyld/
`.
, value: 
fixed32
x28
invalid offset and/or length for opcodes buffer
error handling EST message: %s (%u)\n
entry
v24@?0r^{macho_fat64_arch={fat_arch_64=iiQQII}}8^B16
\t%zd misses (%zd create, %zd failed)\n
error: 
include
]
__restrict
\tSegments:
 missing or set twice, field: 
fnv1a_32
[Invalid macho header] load command out of bounds
libc++.
\t%s: %llu\n
uint16
int
unknown enum value: 
float constant
field set more than once: 
\t%05.2f%% hit rate (%zd of %zd lookups hit, with %zd waits)\n
__OBJC
default value of `
x26
task crashinfo
__TEXT
Unknown hashing algorithm for 32 bit types: 
too many unnamed fields in nested array
Stack empty for DW_OP_deref_size
__.SYMDEF
Using manual argument numbering in automatic argument numbering mode
Segments
InvalidCSRangeBoundsException
` for 
field `
cpp_type
Address
__debug_rnglists
com.apple.sptm
FORM_strx index overflow
int32
nested vector types not supported (wrap in table first)
DW_OP_call_ref is not implemented.
ExceptionSafeThread
KCSSymbolOwnerDataIsTextSegmentOnly
v32@?0Q8r^{UUID=[16C]}16^v24
ip
addrable bits
DW_OP_bit_piece is not implemented.
system
machdep.virtual_address_size
Attempting to set mapping range override using CSRange with invalid length
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/Library/dyld/
armv6
v40@?0r*8^v16{UUID=[16C]}24
<none>
, raw_bytes_for_text: 
_$s
identifier
content_getting_found_segment
NameSourceNlist, 
infinity
_generated
01
Cursor overflow, attempt to read three bytes
double
 does not allow the 
x8
Stack size less than 2 elements for DW_OP_le
Stack size less than 2 elements for DW_OP_lt
symbols.fbs
x0
ASSERT(%s) %s %d, %s\n
Attempting to create CSRange with invalid length
__PRELINK
__debug_ranges
__DWARFA
/System/Library/Kernels
declaration expected
\\x{
Path
/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSBase.cpp
Cursor overflow, attempt to skip ULEB
kCSEndOfTime
__DATA __all_image_info
 in 
r13
MemoryCacheNotFoundException
Stack size less than 2 elements for DW_OP_swap
kCSSymbolOwnerDataFaultedFromSelfDyldSharedCache
v16@?0r*8
ENTRY COUNT: %zd\n
$$$debug-map-fake-mangled-name$$$
x1
CSSymbolOwnerGetContentForRange() gave null content
Stack size less than 2 elements for DW_OP_over
%s %s %sDATA:%p retain count (%d)\n
__debug_line
int16
cos
%s: %s failed 
 to 
x14
kernel
Binaries
Unsupported DW_ATE encoding in value argument: %u
___Z
Incomplete type in struct is not allowed, type name: 
x13
 SEGMENT
illegal character: 
default
recursion-eliding sample discarded due to internal inconsistency
kCSSymbolOwnerDataFoundBinaryNextToDsym
enum
locale-specific form
Name
__DATA_CONST
$$$bad-name-in-nlist$$$
failed to parse 'vm info' LC_NOTE
[Invalid macho header] load command size overflow
Anonymous
string_view::substr
nested_flatbuffer attribute may only apply to a vector of ubyte
v24@?0^v8^B16
/
v24@?0r^{macho_fat_arch={fat_arch=iiIII}}8^B16
long
native_custom_alloc
The format string terminates at a '{'
wrong number of unnamed fields in table vector
exclaves - failed to read vas_segment_t
_x1
float64
x27
content != nullptr
error: UNIMPLEMENTED opcode DW_OP_xderef
/System/DriverKit/System/Library/dyld/
Cursor overflow, attempt to read dwarf_offset
deprecated
deg
CoreSymbolication target process: %s  pid: %d  path: %s\nCouldn't determine parent process ID\n
DW_OP_regx: No read register callback provided
The archive's version is not supported. A malformed file? \n
v16@?0^{__CFData=}8
<redacted>
0123456789abcdef
x19
__TEXT __stubs
Symbol archive address 0x%x could not be relocated to real address\n
kCSNull
) 
Failed to load flatbuffer symbols schema file
fnv1_16
Stack empty for DW_OP_abs
any64bit
 + 1\"
\nFrame count is %d:\n
error: DW_OP_deref_size attempted to dereference a value with a size larger than a target address.
Stack size less than 2 elements for DW_OP_eq
[CoreSymbolication] In DWARF data from %s:\n  .debug_line[%llx] file = %d is not a valid index\n
v16@?0r^{InlineSymbol=[1C]}8
<CSSourceInfo: %p> [0x%08llx -> 0x%08llx) %s:%d
Stack size less than 2 elements for DW_OP_xor
nested_flatbuffer
syntax
unable to locate include file: 
_target_page_size should be populated when targeting live tasks
results
)
Inlined function %s [0x%llx, 0x%llx) outside of relocations in mmap SOD
The type does not fit in the mask
bitset set argument out of range
v16@?0^{dyld_image_s=}8
DYLD-STUB$$
DWARF %d form %u is unrecognized for reading non-indexed ranges.\n
<CSSymbol: %p> %s
NList, 
ERROR, no symbol owners in signature
; 
The argument index should end with a ':' or a '}'
[Invalid macho header] section size overflow
constant name expected
cannot extend unknown message type: 
psr
Stack size less than 2 elements for DW_OP_shr
Stack size less than 2 elements for DW_OP_ge
/System/Volumes/Preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
[Invalid macho header] fileset entry load command is too small for content fields
CSCppArchitecture: cannot answer isLittleEndian for cpu_type 
%u
can't deprecate fields in a struct
Caught exception in sample_remote_thread_with_frame_filter:\n%s\n
Offset not in bounds of TDwarfAddressTableStream
native_include
cpp_str_type
, (symbol owner: 
_$S
[Invalid macho header] load command at %#llx goes beyond bounds
[0x%016llx -> 0x%016llx) %s [%s]
armv4t
failed to read register number: %llu
arm64_32
[Invalid macho header] sections size overflow
<Bad file name in .debug_info>
sptm
 @ 
v24@?0r*8^v16
LOAD
Failed to start process notifications for pid %d (%d)\n
hottestElided
required field is missing: 
' to value of <
dyld_shared_cache_
fnv1a_64
_dyld_process_info_for_each_image provided CoreSymbolication with invalid UTF-8 in path: %s, macho header address: %#llx, uuid: %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x\n
/System/x86Support/System/Library/dyld/
', alignment must be a power of two integer ranging from the type's natural alignment 
message
file_identifier
OSBundleExecutablePath
Using automatic argument numbering in manual argument numbering mode
v24@?0{shared_ptr<CSCppSymbolOwner>=^{CSCppSymbolOwner}^{__shared_weak_count}}8
Simulator
Symbol %s [%llx -> %llx) outside of relocations in mmap SOD\n
length of fixed-length array must be an integer value
not a valid value for this field
oneof '
Developer
CoreSymbolication target process: %s  pid: %d  path: %s\n                  parent process: %s  pid: %d  path: %s\n
mach
, found: 
r4
DW_OP_deref_size: No read memory callback provided
CSCppFileMemory *new_file_memory_for_uuid_and_arch(const char *, const UUID &, CSCppArchitecture, uint32_t)
Unknown typeRef
Could not remap archive address to real in debug maps inline enumeration
}
: 
The format specifier should consume the input or end with a '}'
v16@?0^{dyld_cache_mapping_info=QQQII}8
<CSSymbolOwner: %p> %s %s%s
com.apple.txm
The format specifier contains malformed Unicode characters
An argument index may not have a negative value
get_remote_thread_dispatch_queue2 thread_info(THREAD_EXTENDED_INFO) call failed for pid %u thread %u, err %d
[Invalid macho header] dysymtab load command is too small for content fields
\t%zd peak entries, %zdMB peak footprint\n
r6
OSBundleLoadAddress
IsThumb, 
x6
__TEXT runtime_entry
DW_OP_call4 is not implemented.
DW_OP_piece is not implemented.
unknown enum: 
 would clash with generated functions for field 
Stack empty for DW_OP_not
field id's must be consecutive from 0, id 
 out of 
Remapped bytes from target are not valid at %#llx
Unknown symbolicator signature type.
fatal: invalid enum underlying type
RegionDestructionFailureException
Cursor overflow, attempt to read uint64
Replacement argument isn't a standard signed or unsigned integer type
failed to read core file header
v24@?0{_CSTypeRef=QQ}8
uint
/System/Cryptexes/ExclaveOS
fp
x21
depth
Unable to create symbolicator from dyld compact info for pid %d.\n
memory.address() [%p] should equal memory.mapped_region() [%p]... possible unexpected offset?
unknown
[Invalid macho header] no load commands
IsFunction, 
unable to load include file: 
cannot have more than one json object in a file
The format specifier for 
 kCSSymbolOwnerDataFoundBinaryViaDsymPlist
a floating-point
Out of bounds children index iterating inline ranges
Failed to find memory cache for the given task
major_version
missing type field for this union value: 
<CSRegion: %p> [0x%08llx -> 0x%08llx) %s
exclaves - failed to read segmentinfo
test_value != 0
/mach_kernel
no root type set to parse json with
JIT'ed code?
Sampling current thread of current analysis process is not safe - ignoring requesting to do so\n
<Invalid path>
kCSSymbolOwnerDataEmpty
IsJavaMethod, 
CSSampling
exclaves - unable to determine dyld shared cache range for ExclaveKit target
Stack size less than 2 elements for DW_OP_ne
Daemon Disconnect Queue
.x1
attempted object resurrection
/Applications/
 hex digits
asin
Wrong refcount on traw_symbol_owner_data
Invalid offset to address table header in TDwarfAddressTableStream
Cursor overflow, attempt to skip FORM_block
kCSSymbolOwnerDataIsObjCGCSupported
Corrupt archive entry in %s -- no acceptable header found for entry %s\n
ushort
uint64
includes must come before declarations
\\t
[%3d] %#8.8llx %s %s\n
[Invalid macho header] function starts load command is too small for content fields
shared can only be defined on strings
type mismatch or invalid value, an initializer of non-string field must be trivial ASCII string: type: 
cpp_ptr_type_get
Stack size less than 2 elements for DW_OP_shl
proto
expecting: 
/{}/{}/{}/{}/{}
Stack size less than 2 elements for DW_OP_or
Region %s [%llx -> %llx) outside of relocations in mmap SOD\n
, text_len: 
IsPrivateExternal, 
-inf
don't know how to parse .proto declaration starting with 
optional
\\n
sp
kCSSymbolOwnerDataFaultedFromDisk
cl_kernels
ulong
Vectors of unions are not yet supported in at least one of the specified programming languages.
minor_version
v16@?0r^v8
Malformed fat header\n
, archive_TEXT_text: 
x12
CSCppDyldSharedCache path:
\tPath: %s\n
\n
attribute already found: 
infnanINFNAN
Stack empty for DW_OP_neg
0123456789.
unexpected floating-point constant: 
0b
can't suspend
thread_info failed due to %s
.atlas
<Invalid symbol name>
'key' field must be string, scalar type or fixed size array of scalars
pc
v24@?0r^{fileset_entry_command=IIQQ(lc_str=I)I}8^B16
1
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSMemoryMappingCache.mm
[Invalid macho header] minimum load command overflow
atan
enum already exists: 
\\/
The format string contains an invalid escape sequence
\\\"
pP
enum values need to be qualified by an enum type
import
x3
UUID_String
failure while allocating exception port: %s\n
dyld_sim_shared_cache_
flexbuffer attribute may only apply to a vector of ubyte
CoreSymbolication warning: Unable to locate CIE with ID 0x%8.8x\n
Field 
input file is empty
x22
Mmap string table has reached its maximum size of 4G. Mmap archive will not be created\n
string constant
libsystem_platform.dylib
libstdc++.
No
Could not remap archive address to real in debug maps
FunctionStarts, 
[]
`force_align` is not a valid attribute for Enums. 
x25
B28@?0I8Q12^B20
Encountered symbol with bad name reference during binary search
ReportCrash
Error during directory iteration: %s \n
/System/ExclaveKit/
' cannot be mapped to a union because member '
\\r
vm info
.dSYM/Contents/Resources/DWARF/
byte
offset64
CoreSymbolication - creating symbolicator for current process\n
x5
[header: %s] Ignoring '%.16s %.16s' section [%#llx-%#llx] not contained in '%.16s' segment range [%#llx-%#llx]\n
sample_remote_thread_with_frame_filter failed to get thread state for pid %u thread %u
CSSymbolOwnerGetContentForRange() gave unexpected length for on-disk content of a segment
DW_OP_call2 is not implemented.
NameSourceDwarf, 
union value type may only be table/struct/string
Overflow
Stack size less than 2 elements for DW_OP_minus
Unhandled dwarf attribute in Debug Line Table 
unknown escape code in string constant
field names should be lowercase snake_case, got: 
map
01234567
armv7
, id: 
%p
CSCppDyldSplitSharedCache:\n
.map
failed to allocate dummy port representing thread
CS_DO_NOT_DEMANGLE_SWIFT
Failed to mmap %s\n
floating-point constant expected
End of input while parsing format specifier precision
a pointer
<SymbolicationSession: %p> flags: 0x%x process count: %llu
FORM_strx offset overflow
main bin spec
kern.exclaves_status
fields using 64-bit offsets are not yet supported in at least one of the specified programming languages.
v40@?0^v8r^{CSCppArchiveEntry=[16c][12c][6c][6c][8c][10c][2c]}16Q24^B32
/private/preboot/
precision
libsystem_pthread.dylib
coldestElided
%02hhX%02hhX%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX%02hhX%02hhX%02hhX%02hhX/
[Invalid macho header] minimum load command goes beyond bounds
unique_lock::lock: references null mutex
short
string
The numeric value of the format specifier is too large
_dispatch_queue_offsets
CIE parse error: CIE augmentation string was too large for the fixed sized buffer of %d bytes.\n
/System/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/dyld/
End of input while parsing an argument index
CIE
IsOmitFramePointer, 
r14
_sysenter_trap
[Invalid macho header] inadequate size of a load command
PRIVATE_KEY:0x%llx 
.0
acos
_byte_vector
The argument index is invalid
x4
Process exists but has not fully started -- dyld has initialized but libSystem has not
__LINKINFO
Source info %s [%llx -> %llx) outside of relocations in mmap SOD\n
reserved
Stack empty for DW_OP_deref
Stack size less than 2 elements for DW_OP_shra
Stack empty after evaluation
SEGMENT
, name: 
DW_OP_fbreg is not implemented
[Invalid macho header] section not contained in segment
only short, ushort, int, uint, long and ulong data types support hashing.
Array defaults are not supported yet.
datatype already exists: 
lr
shmem
Length
 use(s) of pre-declaration enum not accounted for: 
mapped_memory->_target_page_size.has_value()
~rc
%s(
__OBJC_RO
_kasan
content_length <= segment_vm_range.length
.dSYM
/System/Volumes/Preboot/Cryptexes/ExclaveOS
hash
 characters
CoreSymbolication dyld load/unload notifier queue
r1
IsObjcMethod, 
only vectors of scalars are allowed to be 64-bit.
Flags
x86_64h
Historical timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
CoreSymbolication - creating symbolicator for remote process\n
length == mapping_content_vm_range_and_source.vm_range.length
 
 - %s
[Invalid macho header] source version load command is too small for content fields
Attempt to use ISA32Big when it is not defined
, DSYM Path: 
Fixed-length array size is incorrect.
, constant does not fit 
/private/preboot/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
__TEXT_EXEC
kCSSymbolOwnerDataFoundBinaryViaDsymPlist
Attempting to map range %llu-%llu length %llu past end of file %llu in: %s\n
NONE
__PPLTEXT
unordered_map::at: key not found
v32@?0Q8r*16r*24
libdispatch.dylib
kCSSymbolOwnerDataFaultedFromDiskDyldSharedCache
failed to parse 'task crashinfo' LC_NOTE
exclaves - unable to analyze this vsit_version using this tool
v32@?0r*8Q16Q24
/usr/lib/swift/libswiftDemangle.dylib
Attempt to use ISA64Big when it is not defined
size 0 structs not allowed
root type must be a table
cpsr
length of fixed-length array must be positive and fit to uint16_t type
, originally at: 
MangledNameSourceDwarfMIPSLinkage, 
__eh_frame
CSCppCFDataMemory
v20@?0r*8I16
Null abbrev discovered in DWARF at index 
__Z
illegal type id for: 
ERROR, unhandled signature version
end of file
 formatting argument
Value is not initialized
0
Fields cannot be both optional and required.
kCSSymbolOwnerDataFaultedFromTask
OSBundleUUID
inf
nested_flatbuffer attribute must be a string (the root type)
<CSRegion: %p> [0x%016llx -> 0x%016llx) %s
[%3d] %#8.8llx fp:%#8.8llx %s %s\n
Failed to create mmap archive: %s\n
 kCSSymbolOwnerDataFaultedFromDiskDyldSharedCache
group
Caught exception in create_sampling_context_for_task:\n%s\n
MACH_HEADER
out of range index into nlist array
, flags:
Load Timestamp
Merged, 
a union type effectively adds two fields with non-negative ids, its id must be that of the second field (the first field is the type field and not explicitly declared in the schema);\nfield: 
sfixed64
namespace
v32@?0^Q8^Q16*24
shared
\\u{
Unknown DWARF DW_OP value.
struct: wrong number of initializers: 
Unimplemented: 
integer constant
failed to parse 'addrable bits' LC_NOTE
ExclaveKit
v92@?0{UUID=[16C]}8i24{_CSArchitecture=ii}28Q36{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={
IsKnownLength, 
r2
/System/ExclaveCore/
arm64
B48@?0Q8Q16Q24*32Q40
Default values for strings and vectors are not supported in one of the specified programming languages
Vector defaults may only be `[]`.
invalid number: \"
Yes
int8
std::unique_ptr
failed to open core file
\t%zd resymbolications attempted. (%zd replacements)\n
/System/
Cursor overflow, attempt to skip FORM_string
field already exists: 
Arrays are not yet supported in all the specified programming languages.
rpc_service
 option
unique_lock::unlock: not locked
create_symbol_owner_data -- UUID: 
exclaves - invalid exclave metadata
memory read of %u bytes at address 0x%8.8llx failed: 0x%8.8x
/System/ExclaveKit/System/Library/dyld/
a character
failed to parse thread load command
Stack empty for DW_OP_plus_uconst
traw_symbol_owner_data->retain_count() == 1
\n\n
Overflow calculating start of header in TDwarfAddressTableStream
 reached
only string and vectors can have `offset64` attribute applied
bytes
Index out of range for DW_OP_pick
dyld_v
$$$indirect-local-symbol$$$
cpp_ptr_type
x15
\t\t%s 0x%llx - 0x%llx\n
illegal Unicode sequence (unpaired high surrogate)
%u.%u.%u.%u.%u
UNNAMED
uint8
oneof
NameSourceDwarfMIPSLinkage, 
flexbuffer
sint32
a bool
__sigtramp
nan
[Invalid macho header] dylib load command is too small for content fields
\t%5.5fs create time\n
_dyld_all_image_infos
cmd
v36@?0r*8Q16Q24i32
attribute
an integer
the default 'null' is reserved for declaring optional scalar fields, it conflicts with declaration of enum '
cpp_str_flex_ctor
.stripped.sharedcache
__image_info
maximum parsing depth 
code: 
native_inline
kCSSymbolOwnerDataIsObjCRetainReleaseSupported
Timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
extensions
x24
CoreSymbolication warning: Unable to locate CIE at 0x%8.8x = 0x%8.8x - (0x%8.8x + 4)\n
SYMB
attempting to access outside bounds of CSMemoryMapping
[Invalid macho header] segment load command is too small for content fields
/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/
CSCppFileMemory 
IsObjcMethodValid, 
cannot parse nested_flatbuffer as bytes unless --json-nested-bytes is set
type mismatch: expecting: 
false
must specify the underlying integer type for this enum (e.g. ': short', which was the default).
service
' is not a table type.
NameAllocated, 
end of file in comment
true
exclaves - unable to analyze this vsip_version version using this tool
/System/Cryptexes/Incoming/OS/System/Library/dyld/
kCSBeginningOfTime
$e
The only supported default for vectors is `[]`.
'.
CSSymbolOwnerGetContentForRange() gave null content when requesting whole segment VM range
/usr/lib/dyld
Unhandled CSCppSymbolOwnerData type_id: 
Lock, 
Dwarf, 
Unload Timestamp
type referenced but not defined (check namespace): 
The argument index value is too large for the number of arguments supplied
sign
Child symbol archive address 0x%x could not be relocated to real address\n
Size
Attempt to set cursor outside bounds
Base relative index not in bounds of current address table in TDwarfAddressTableStream
underlying type of bit_flags enum must be unsigned
fnv1_64
__debug_abbrev
CSSymbolicator for core file
union types vector smaller than union values vector for: 
0X
Processing header for %s\n
__DWARF
int64
service already exists: 
/System/Cryptexes/Rosetta/System/x86Support/System/Library/dyld/
illegal character in string constant
exclaves - found overlapping vas_segment_ts
CSSymbolOwnerGetContentForRange() failed to find segment
.cdhash
Cursor overflow, attempt to read LEB
$$$indirect-absolute-symbol$$$
 kCSSymbolOwnerDataEmpty
kCSAllTimes
ByteVector
treating warnings as errors, failed due to above warnings
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
Invalid specification abbrev index in DWARF: 
native_custom_alloc can only be used with a table or struct definition
zero-padding
armv5tej
Invalid analyzed archive entry for object file %s from archive %s at offset 0x%llx\n
$$$function-starts-fake-mangled-name$$$
The argument index starts with an invalid character
CoreSymbolication warning: error parsing %s at 0x%8.8llx in:\n\t__TEXT [0x%8.8llx - 0x%8.8llx) __eh_frame [0x%8.8llx - 0x%8.8llx) %s\n
CSMemoryMapping failed to deallocate underlying mapping with error %s (%d)
only tables can be union elements in the generated language: 
_
` is not part of enum `
incomplete enum declaration, values not found
Failed to find symbolicators in flatbuffer created from JSON\n
x9
Caught exception in get_remote_thread_dispatch_queue2 for pid %u: %s
Unable to create symbolicator from dyld compact info for pid: %d. Shared cache UUID is missing\n
vector
armv7f
__debug_addr
Cursor overflow, attempt to read uint8
Enums must have integer base types
underlying 
rpc already exists: 
[Invalid macho header] uuid load command is too small for content fields
%u.%u.%u.%u
__DATA_DIRTY __all_image_info
Transformed binary is invalid
FDE
[Invalid macho header] inadequate segment load command vm size
v16@?0^{dyld_shared_cache_s=}8
sin
CSCppCoreFileMemory
:
Q16@?0^v8
%s -- stopping DWARF analysis of %s\n
 kCSSymbolOwnerDataFaultedFromDisk
default values are not supported for struct fields, table fields, or in structs.
Cursor overflow, attempt to read uint32
Base relative index overflow in TDwarfAddressTableStream
CSSymbolicatorCreateWithCSCppMachTaskFlagsAndNotification exception failure: %s
+inf
__AUTH_CONST
[Invalid macho header] size of load commands overflow
, is_dyld_shared_cache: 
 for symbol entry.
illegal Unicode sequence (unpaired low surrogate)
 instead got: 
option
sint64
internal: 
r7
get_remote_thread_dispatch_queue2 thread_info(THREAD_IDENTIFIER_INFO) call failed for pid %u thread %u, err %d
Caught exception in get_remote_thread_dispatch_queue2:\n%s\n
exclaves - invalid segmentinfo_page address
%02hhX%02hhX%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX%02hhX%02hhX%02hhX%02hhX
arm64_32v8
[Invalid macho header] dylib load command name offset is invalid
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppSymbolOwnerCache.cpp
.symbols
<null>
Unhandled form in read flag binding 
file_identifier must be exactly 
native_type_pack_name
AppleInternal
Cursor overflow, attempt to read FORM_string
, 
illegal UTF-8 sequence
B24@?0{shared_ptr<CSCppSymbolOwner>=^{CSCppSymbolOwner}^{__shared_weak_count}}8
CSSymbolOwnerGetContentForRange() gave nonsensical segment content length
DW_OP_bra has invalid opcode offset
__PPLTRAMP
aot_shared_cache
hw.cpu64bit_capable
CSCppArchitecture: cannot answer is64Bit for cpu_type 
-
Cursor overflow, attempt to skip FORM_block4
, max_TEXT_text_section: (
Failed to relocate address %#llx in flatbuffer SOD
test_value >= value
__crashreporter_info__: %s\n
!
__debug_str_offs
CSCppTaskMemory: range values must not overlap
rad
Entry
Error decoding symbol owner from signature
r10
__OBJC_R
__RESTRICT
Cursor overflow, attempt to read dwarf_address
_length
enum value does not fit, \"
/private/preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
null-uuid                           
../
_$sS
CoreSymbolication warning: fde.addrRange.location 0x%8.8llx isn't in  the __TEXT segment [0x%8.8llx - 0x%8.8llx)\n
only one field may be set as 'key'
extend
fixed64
Unable to access flatbuffer symbols schema at %s
write_errno
[0x%08x -> 0x%08x) %s [%s]
MangledNameSourceDwarf, 
structs may contain only scalar or struct fields
Unknown hashing algorithm for 64 bit types: 
_vas__segmentinfo_table
found_containing_segment
v16@?0r^{Symbolicator=[1C]}8
/SWE/
/usr/local/libexec/rosetta/runtime
/System/Cryptexes/Rosetta/System/Library/dyld/
Unhandled dwarf attribute 
v24@?0^v8^v16
exclaves - failed to dup() core file file descriptor
Stack size less than 2 elements for DW_OP_gt
/private/preboot/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
field name can not be the same as table/struct name
vector64
required
 cpuSubtype 
only non-scalar fields in tables may be 'required'
x20
\tUUID: %s\n
x10
ReportCrashService
[Invalid macho header] symtab load command is too small for content fields
Unhandled form in read data binding 
/private/preboot/Cryptexes/ExclaveOS
bool
Override ranges must not overlap
uint32
cpp_type can only be used with a hashed field
idempotent
The width option should not have a leading zero
/System/Cryptexes/OS/System/Library/dyld/
OutOfBoundsException
[Invalid macho header] dylinker load command name offset is invalid
__UNIXSTACK
IsExternal, 
union
fnv1_32
r3
Stack size less than 2 elements for DW_OP_plus
Cursor overflow, attempt to read uint16
_development
$$$function-starts-fake-name$$$
invalid number: 
Protobuf has non positive number in reserved ids
.development
IsMarked, 
attribute `vector64` implies `offset64` and isn't required.
__debug_info
illegal type syntax
package
Symbol %s [0x%llx, 0x%llx) outside of relocations in mmap SOD
CSCppTaskMemory pid:
r8
Found _sigtramp symbol after %u tries\n
[Invalid macho header] dylinker load command is too small for content fields
 ; 
/System/Library/PrivateFrameworks/Swift/libswiftDemangle.dylib
cannot parse value starting with: 
Underlying type for union is not yet supported in at least one of the specified programming languages.
repeated
basic_string
UNIVERSE
Caught exception in sample_remote_thread_with_frame_filter for pid %u: %s\n
/usr/
_gLoadedKextSummaries
No symbol owners pointer in flatbuffer\n
0B
, Path: 
__debug_line_str
float
user define attributes must be declared before use: 
invalid number, the exponent suffix of hexadecimal floating-point literals is mandatory: \"
x11
__PAGEZERO
kern.uuid
: type of argument mismatch, expecting: 
table
unknown root type: 
 kCSSymbolOwnerDataFaultedFromSelfDyldSharedCache
 kCSSymbolOwnerDataFoundBinaryNextToDsym
<unknown>
Unknown hashing algorithm for 16 bit types: 
unexpected force_align value '
os_security_config_get_for_task
/System/Volumes/Data/home
MangledNameValid, 
Leaking private implementation, verify all objects have similar annotations
0123456789abcdefghijklmnopqrstuvwxyz
r15
<No path>
alternate form
exclaves - failed to get any segmentinfo_pages
arm
 and 
all fields must have an 'id' attribute when --require-explicit-ids is used
[
Process exists but has not started -- it is launched-suspended
v8@?0
[0x%016llx 0x%016llx] 
native_type
The type option contains an invalid value for a string formatting argument
x17
__objc_imageinfo
a documentation comment should be on a line on its own
key
> type.
Failed to parse flatbuffer symbols schema
%0hhx
r5
mapped_memory_resume_target
 LIVE
__kernel__
attribute name must be either identifier or string: 
0x
re
!CSRangeIntersectsRange(prev->range, next->range)
Unable to acquire mach service port, symbol cache unavailable\n
over release
/mach
Unhandled form in read ref binding 
swift_demangle_getSimplifiedDemangledName
/usr/lib/system/libsystem_platform.dylib
Stack empty for DW_OP_bra
Unimplemented range list entry kind
IsDyldStub, 
$S
enum value already exists: 
!override_range_overflows
armv7k
current
$$$debug-map-fake-name$$$
bit_flags
Couldn't find _sigtramp symbol in expected dylibs\n
arm64v8
Cursor overflow, attempt to skip FORM_block1
Empty object_file_path in mach-o header: %s\n
_$e
sfixed32
exclaves - failed to read segmentinfo_page
CS_TEST_EXCLAVEKIT_DIR
Client side event: Unhandled xpc type\n
Cache stats:
load binary
com.apple.CoreSymbolication
FlexBuffers map has duplicate keys
\xf0R
 kCSSymbolOwnerDataFaultedFromTask
illegal Unicode sequence (multiple high surrogates)
null
csharp_partial
mapped_memory_suspend_target
DW_OP_deref: No read memory callback provided
Invalid abbrev tag 
x16
CSSymbolOwnerGetContentForRange() failed to find segment containing part of section
Stack empty for DW_OP_dup
DW_OP_push_object_address is not implemented.
v48@?0{_CSRange=QQ}8^{_CSTypeRef=QQ}24^{_CSTypeRef=QQ}32Q40
/%s
invalid utf-8 byte order mark
 are both 
.symbolsarchive
r11
Fat header is malformed\n
, TEXT_text_section.value(): 
OSBundleMachOHeaders
'native_inline' can only be defined on structs, vector of structs or vector of tables
tan
\t
error: UNIMPLEMENTED opcode DW_OP_xderef_size
/System/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
```
