# `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,696,064 bytes.

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
copyBytesFromAddress:size:to:error:
getCoreFileLedgerInternalCompressed:
getCoreFileLedgerTaggedFootprintCompressed:
getTaskThreads:count:error:
isBackedBySelfTask
initWithCString:encoding:
dealloc
_dsc_range
copyBytesFromAddress:size:to:
existingMappingForAddress:size:fullyContainedOnly:
getCoreFilePPid:
getCoreFileLedgerPhysFootprint:
_touch_regions
coreFileProcPath
withBytes:
initWithTask:touchMappedRegions:
mappingSliceForAddress:size:error:
stringWithUTF8String:
_root_map
_task
dictionaryWithObjects:forKeys:count:
getCoreFileUdataPtrs:udataPtrsCount:
getCoreFileUserstack:
getStateForThread:flavor:oldState:oldStateCnt:error:
getCoreFileLedgerPurgeableNonvolatileCompressed:
initWithBytes:length:encoding:
_accessCount
coreFileIsExclavecore
getCoreFileLedgerPageTable:
is64Bit
_addressMask
code
coreFileHasInfoForMemoryAnalysis
.cxx_destruct
enumerateCoreFileDumpedRegions:
getCoreFileLedgerAlternateAccountingCompressed:
init
getCoreFileLedgerNetworkNonvolatile:
getCoreFileProcFlags:
initWithoutExclaveMetadataForCoreFileWithPath:label:error:
suspendTargetWithError:
_is64Bit
coreFileIsExclave
getCoreFileDyldAllImageInfosAddr:
getCoreFileLedgerWiredMem:
_dsc_slide
_reclaimed_nodes
getCoreFileLedgerNeuralFootprintCompressed:
getCoreFileArgsLen:
getCoreFileLedgerTaggedFootprint:
_region_info_block
errorWithDomain:code:userInfo:
getCoreFileAddressingMask:
getCoreFileProcStarttimeSec:
tryGettingUnsafeBytesForAddress:size:
TB,R,N
_core_file_metadata
getCoreFileExclaveVmFlagsForAddress:exclaveVmFlags:
getCoreFileLedgerGraphicsFootprint:
coreFileMachVmRegionRecurseSubmapShort64:size:nestingDepth:info:error:
mappingForAddress:size:error:
sliceFromAddress:size:
T@\"NSString\",R,N
coreFileMachVmPageRangeQuery:size:dispositions:dispositionsCount:usePhysFootprint:error:
getCoreFileLedgerNeuralFootprint:
initWithUnderlyingMapping:remoteStart:remoteSize:
releaseMappedMemoryCacheForTask:
remoteRange
setRegionInfoBlock:
_underlyingMapping
coreFileParentProcPath
enumerateMappingsWithBlock:
getCoreFileOwnedVmObjects:ownedObjectsByteCount:
localAddressForRemoteAddress:
.cxx_construct
_isBackedBySelfTask
_localMappedAddress
getCoreFileArchitecture:
getCoreFileLedgerNetworkNonvolatileCompressed:
unsafeBytes
withBytesFromAddress:size:block:
UTF8String
_suspension_count
initWithDomain:code:userInfo:
remoteBaseAddress
_size
_targetAddressMask
TB,R,N,V_is64Bit
_count
getCoreFileLedgerAlternateAccounting:
initWithName:reason:userInfo:
stringWithFormat:
_mapping_range_overrides
_remoteBaseAddress
getCoreFileDirtyFlags:
T@\"CSMemoryMapping\",R,N,V_underlyingMapping
getCoreFilePid:
_remoteSliceRange
coreFileRegionFilenameForAddress:
setMappingRangeOverrides:overrideCount:
coreFileMachVmRegionRecurseSubmap64:size:nestingDepth:info:error:
lookUpMappedMemoryCacheForTask:
TQ,R,N,V_remoteBaseAddress
_target_page_size
clear
coreFileMachVmPurgableControlForAddress:control:state:
size
TB,R,N,V_isBackedBySelfTask
_lock
coreFileProcName
getCoreFileDyldSharedCacheRange:
getCoreFileLedgerMediaFootprint:
getCoreFileProcStarttimeUSec:
sliceFromAddress:
underlyingMapping
_purpose_label
_suspension_token
getCoreFileLedgerMediaFootprintCompressed:
TQ,R,N
TQ,R,N,V_localMappedAddress
Tr^v,R,N
getCoreFileLedgerGraphicsFootprintCompressed:
getCoreFileLedgerPurgeableNonvolatile:
getMappedMemoryCacheForTask:purposeLabel:
resumeTargetWithError:
TQ,R,N,V_size
getCoreFileLedgerIokitMapped:
initialize
_total_mapped_size
coreFileParentProcName
getCoreFileProcArgc:
unsafeBytesForAddress:size:
getCoreFileLedgerInternal:
getCoreFileLedgerPhysFootprintLifetimeMax:
initWithCoreFilePath:label:error:
initWithTask:touchMappedRegions:label:
readPointerFromAddress:outValue:
unsafeBytesForAddress:size:outTrailingSize:
T{_CSRange=QQ},R,N
lengthAfterAddress:
localMappedAddress
v16@0:8
r^v40@0:8Q16Q24^Q32
@32@0:8I16B20@24
B24@0:8^Q16
{vector<CSMappingRangeOverride, std::allocator<CSMappingRangeOverride>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}
{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}
@24@0:8Q16
{_CSRange=\"location\"Q\"length\"Q}
B
@24@0:8I16B20
@\"NSString\"
@\"CSMemoryMapping\"
r^v32@0:8Q16Q24
@36@0:8Q16Q24B32
B24@0:8^@16
i32@0:8Q16^Q24
B48@0:8Q16Q24^v32^@40
B40@0:8^^I16^I24^@32
B56@0:8^Q16^Q24^I32^{vm_region_submap_short_info_64=iiIQIISCCiiISS}40^@48
v40@0:8Q16Q24@?32
Q24@0:8Q16
Q
I
@40@0:8@16@24^@32
B48@0:8I16i20^I24^I32^@40
B56@0:8^Q16^Q24^I32^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQISS}40^@48
B60@0:8Q16Q24Q32^Q40B48^@52
Q16@0:8
v24@0:8@?16
v20@0:8I16
B32@0:8^Q16^Q24
B32@0:8^{?=Q[0{?=QQQQQQ{?=b1b3b2}}]}16^Q24
B24@0:8^I16
B32@0:8Q16^I24
{unique_ptr<CSCppCoreFileMetadata, std::default_delete<CSCppCoreFileMetadata>>=\"\"{?=\"__ptr_\"^{CSCppCoreFileMetadata}}}
@40@0:8@16Q24Q32
r^v16@0:8
@28@0:8I16@20
@20@0:8I16
B24@0:8^i16
{OrderedMemoryMappings=\"_map\"{set<CSMemoryMapping *, CompareMappedRegionNode, std::allocator<CSMemoryMapping *>>=\"__tree_\"{__tree<CSMemoryMapping *, CompareMappedRegionNode, std::allocator<CSMemoryMapping *>>=\"__begin_node_\"^v\"\"{?=\
{vector<CSMemoryMapping *, std::allocator<CSMemoryMapping *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}
@?
v40@0:8Q16Q24^v32
{_CSRange=QQ}16@0:8
@32@0:8Q16Q24
B16@0:8
v32@0:8^{?={_CSRange=QQ}BB}16Q24
@40@0:8Q16Q24^@32
B24@0:8^{_CSRange=QQ}16
B24@0:8^{_CSArchitecture=ii}16
@16@0:8
B36@0:8Q16i24^i28
{optional<unsigned long long>=\"\"(?=\"__null_state_\"c\"__val_\"Q)\"__engaged_\"B}
Succesfully created kext symbol owners.\n
Unable to access flatbuffer symbols schema at %s
get_remote_thread_dispatch_queue2 thread_info(THREAD_IDENTIFIER_INFO) call failed for pid %u thread %u, err %d
SYMBOLICATOR %p CREATED BY CSSymbolicatorCreateWithSymbolOwnersAndCSCppTask\n
[Invalid macho header] no load commands
Bad abbrev table offset in compile unit\n
Child symbol archive address 0x%x could not be relocated to real address\n
[Invalid macho header] minimum load command overflow
[Invalid macho header] dylinker load command is too small for content fields
Sampling current thread of current analysis process is not safe - ignoring requesting to do so\n
[Invalid macho header] sections size overflow
Failed to locate official Exclave Kit binaries on disk
The archive's version is not supported. A malformed file? \n
Couldn't find a valid DSC header in mapped range %llx - %llx
SAMPLING_SAMPLE_BOTH_REGULAR_AND_SWIFT_ASYNC will override SAMPLING_IGNORE_SWIFT_ASYNC
Client side event: Unhandled xpc type\n
[Invalid macho header] inadequate size of a load command
Ref addr is not within the bounds of any compile unit
Timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
memory.address() [%p] should equal memory.mapped_region() [%p]... possible unexpected offset?
Unable to determine special slide 2.
[Invalid macho header] load command size overflow
[Invalid macho header] dylib load command is too small for content fields
SYMBOLICATOR %p DESTRUCTED\n
Failed to relocate address %#llx in flatbuffer SOD
Failed to parse flatbuffer conformant json string -- likely the JSON is not formatted correctly\n
error handling EST message: %s (%u)\n
Failed to mmap %s\n
Missing page in pid %d, create of symbol owner data for [%s] failed, err code %d\n
Unexpected DWARF version parsing DW_AT_ranges: %d\n
Error during directory iteration: %s \n
[Invalid macho header] load command at %#llx goes beyond bounds
[Invalid macho header] inadequate sum of sections size
Invalid analyzed archive entry for object file %s from archive %s at offset 0x%llx\n
Out of bounds compile unit\n
No symbol owners pointer in flatbuffer\n
[Invalid macho header] size of load commands overflow
Attempting to map range %llu-%llu length %llu past end of file %llu in: %s\n
sample_remote_thread_with_frame_filter failed to get thread state for pid %u thread %u
[Invalid macho header] inadequate segment load command vm size
Failed to get dsc path for task\n
No string extracted from DWARF5 path list
Failed to load flatbuffer symbols schema file
The archive's size is too small. A malformed file? \n
Possible reference cycle in DIE
Attempt to relocate address [0x%llx], which is outside segment deltas\n
Failed to start process notifications for pid %d (%d)\n
Missing page in pid %d, sampling of thread failed, err code %d\n
Path is not a directory: %s\n
[Invalid macho header] dylib load command name offset is invalid
SYMBOLICATOR %p CREATING SYMBOL OWNER DATA: %s\n
Failed to parse flatbuffer symbols schema
Unable to create symbolicator from dyld compact info for pid %d.\n
Unsupported compile unit type\n
Could not remap archive address to real in debug maps
Symbol archive address 0x%x could not be relocated to real address\n
Unable to create symbolicator from dyld compact info for pid: %d. Shared cache UUID is missing\n
[Invalid macho header] dysymtab load command is too small for content fields
Fat header is malformed\n
[Invalid macho header] inadequate sections size
[Invalid macho header] section size overflow
[Invalid macho header] uuid load command is too small for content fields
%s parsing abbrev table -- stopping DWARF analysis of %s\n
Symbol %s [%llx -> %llx) outside of relocations in mmap SOD\n
Provided dSYM: [%s] does not match symbol owner %p\n
Compile unit with bad address_size\n
CSSymbolicatorCreateWithCSCppMachTaskFlagsAndNotification exception failure: %s
Unable to determine a special slide 1.
Transformed binary is invalid
Failed to find symbolicators in flatbuffer created from JSON\n
[Invalid macho header] dylinker load command name offset is invalid
FAILED: dyld %s of %s\n
TEXT_text_location %llx outside of relocations in mmap SOD\n
Unable to create process info for pid %d, task %d. Is dyld loaded for this binary yet?\n
Failed to read dyld info for process %d (%d)\n
Malformed fat header\n
Out-of-bounds abstract origin or specification offset
Failed to find matching kernels in %s\n
Missing page in pid %d, read of header data for [%s] failed, err code %#x\n
pid %d Failure reading CFI info at %s\n
[Invalid macho header] unreasonable number of sections
[Invalid macho header] section not contained in segment
[Invalid macho header] function starts load command is too small for content fields
Could not remap archive address to real in debug maps inline enumeration
Caught EXC_BAD_ACCESS at 0x%llx, valid page mapping, page query flags (0x%x)\n
Failed to access directory: %s\n
Connection invalidated: %s\n
Could not read UUID of running kernel\n
get_remote_thread_dispatch_queue2 thread_info(THREAD_EXTENDED_INFO) call failed for pid %u thread %u, err %d
[Invalid macho header] minimum load command goes beyond bounds
[Invalid macho header] segment load command is too small for content fields
[header: %s] Ignoring '%.16s %.16s' section [%#llx-%#llx] not contained in '%.16s' segment range [%#llx-%#llx]\n
Unable to determine kernel slide.
failure while allocating exception port: %s\n
Failed to create mmap archive: %s\n
Region %s [%llx -> %llx) outside of relocations in mmap SOD\n
Found matching kernel in %s\n
Remapped bytes from target are not valid at %#llx
Missing page in pid %d, checking for second frame failed, err code %d\n
Unable to acquire mach service port, symbol cache unavailable\n
[Invalid macho header] load command out of bounds
CSCppMachTaskContainer task_for_pid failed for process %u, err %d
Caught exception in sample_remote_thread_with_frame_filter for pid %u: %s\n
Requested vm range length in %s does not exist in file.\n
%s -- stopping DWARF analysis of %s\n
Empty function_name in mach-o header: %s\n
Unexpected number of symbol owners in flatbuffer created from JSON: %u\n
Out of bounds children index iterating inline ranges
thread_info failed due to %s
Caught exception in %s:\n %s\n
Attempt to mmap %s failed, %s\n
DWARF %d form %u is unrecognized for reading non-indexed ranges.\n
[CoreSymbolication] In DWARF data from %s:\n  .debug_line[%llx] file = %d is not a valid index\n
Empty object_file_path in mach-o header: %s\n
Source info %s [%llx -> %llx) outside of relocations in mmap SOD\n
Historical timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
Caught exception in get_remote_thread_dispatch_queue2 for pid %u: %s
[Invalid macho header] fileset entry load command is too small for content fields
Corrupt archive entry in %s -- no acceptable header found for entry %s\n
Found running kernel dummy entry.\n
UUID found in both ExclaveCore and ExclaveKit\n
[Invalid macho header] source version load command is too small for content fields
Corrupt macho header at %#llx\n
Unable to determine architecture of the kernel
Unable to create any kext symbol owners.\n
Error reading kernels directory: %s\n
[Invalid macho header] symtab load command is too small for content fields
Segments in dSYM [%s] could not be matched to task header\n
Mmap string table has reached its maximum size of 4G. Mmap archive will not be created\n
arm64_32v8
Invalid abbrev tag 
%s%s
Enums must have integer base types
%s(
<Invalid symbol name>
Load Timestamp
NameAllocated, 
infinity
\\\\
Cursor overflow, attempt to read uint64
DebugMap, 
a documentation comment should be on a line on its own
expecting: 
default value of `
DW_OP_bra has invalid opcode offset
repeated
can't suspend
failed to read register number: %llu
__OBJC_R
Cursor overflow, attempt to read uint32
Cursor overflow, attempt to skip FORM_block1
Cursor overflow, attempt to skip FORM_string
`force_align` is not a valid attribute for Enums. 
file_extension
arm
kCSSymbolOwnerDataFaultedFromSelfDyldSharedCache
Cursor overflow, attempt to read three bytes
Symbol %s [0x%llx, 0x%llx) outside of relocations in mmap SOD
kernel
error: 
std::unique_ptr
The numeric value of the format specifier is too large
kCSSymbolOwnerDataIsObjCRetainReleaseSupported
%u.%u.%u
OSBundlePath
MangledNameSourceDwarfMIPSLinkage, 
'.
]
End of input while parsing format specifier precision
x19
CSCppFileMemory *new_file_memory_for_uuid_and_arch(const char *, const UUID &, CSCppArchitecture, uint32_t)
int
streaming
a bool
Integral value outside the range of the char type
x27
depth
DW_OP_reg: No read register callback provided
__LINKINFO
short
Failed to parse flatbuffer conformant json string -- likely the JSON is not formatted correctly\n
_$sS
Segments
hw.cpu64bit_capable
unexpected force_align value '
v16@?0^v8
rpc request and response types must be tables
__DATA __all_image_info
cpsr
CSSymbolOwnerGetContentForRange() failed to find segment containing part of section
unknown escape code in string constant
cpp_type can only be used with a hashed field
OutOfBoundsException
__kernel__
fixed-length array in table must be wrapped in struct
a union type effectively adds two fields with non-negative ids, its id must be that of the second field (the first field is the type field and not explicitly declared in the schema);\nfield: 
~rc
, Path: 
_byte_vector
Symbol archive address 0x%x could not be relocated to real address\n
Stack size less than 2 elements for DW_OP_minus
CS_TEST_EXCLAVECORE_DIR
uint8
oneof
DW_OP_bregx: No read register callback provided
Unable to create symbolicator from dyld compact info for pid: %d. Shared cache UUID is missing\n
.dSYM
Attempt to use ISA64Big when it is not defined
__eh_frame
JIT'ed code?
arm64v8
NList, 
` is not part of enum `
arm64e
%u.%u.%u.%u
Yes
Cursor overflow, attempt to read dwarf_offset
nested_flatbuffer attribute may only apply to a vector of ubyte
Stack empty for DW_OP_dup
\nFrame count is %d:\n
IsMarked, 
unknown field: 
cl_kernels
current
, field name: 
memory.address() [%p] should equal memory.mapped_region() [%p]... possible unexpected offset?
__PPLTEXT
__AUTH_CONST
\tUUID: %s\n
Unknown conversion function: 
 missing or set twice, field: 
x12
.map
extend
 out of 
r8
any64bit
RegionDestructionFailureException
Unhandled dwarf attribute 
fnv1a_16
addrable bits
archive_shmem
, raw_TEXT_text_section: (
failed to read core file header
escape code must be followed by 
 does not allow the 
 kCSSymbolOwnerDataFaultedFromTask
\n
`.
.symbolsarchive
kCSSymbolOwnerDataFoundBinaryNextToDsym
__PRELINK
v24@?0r^{fileset_entry_command=IIQQ(lc_str=I)I}8^B16
required
 SEGMENT
__OBJC
floating-point constant expected
no root type set to parse json with
x11
Stack size less than 2 elements for DW_OP_or
/System/ExclaveKit/System/Library/dyld/
Unhandled form in read data binding 
Optional scalars are not yet supported in at least one of the specified programming languages.
_type
kCSEndOfTime
x14
No
illegal type syntax
could not open file, or it is not a Mach-O core file
Binaries
minor_version
kCSNull
Invalid offset to address table header in TDwarfAddressTableStream
$$$indirect-local-symbol$$$
double
native_custom_alloc
Attempting to map range %llu-%llu length %llu past end of file %llu in: %s\n
CSCppFileMemory 
_generated
The fill option contains an invalid value
The type does not fit in the mask
<CSSourceInfo: %p> [0x%08llx -> 0x%08llx) %s:%d
field id's must be consecutive from 0, id 
x23
/System/Cryptexes/Rosetta/System/x86Support/System/Library/dyld/
 ; 
/System/Library/PrivateFrameworks/Swift/libswiftDemangle.dylib
Path
%02hhX%02hhX%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX-%02hhX%02hhX%02hhX%02hhX%02hhX%02hhX
Cursor overflow, attempt to read uint16
 kCSSymbolOwnerDataFaultedFromSelfDyldSharedCache
\tPath: %s\n
IsExternal, 
uint
native_inline
, id: 
: type of argument mismatch, expecting: 
Attempt to set cursor outside bounds
$$$debug-map-fake-mangled-name$$$
__DATA
Default values for strings and vectors are not supported in one of the specified programming languages
> type.
\\r
r5
r3
[Invalid macho header] no load commands
Cursor overflow, attempt to read ULEB
' cannot be mapped to a union because member '
The argument index is invalid
com.apple.coresymbolicationd
Caught exception in create_sampling_context_for_task:\n%s\n
exclaves - unable to analyze this vsip_version version using this tool
Stack size less than 2 elements for DW_OP_xor
DW_OP_skip has invalid opcode offset
/System/Library/dyld/
i386
/
invalid number: 
psr
CSSampling
ExceptionSafeThread
<null>
CS_DO_NOT_DEMANGLE_SWIFT
field names should be lowercase snake_case, got: 
zero-padding
__TEXT __stub_helper
%s: %s failed 
Stack size less than 2 elements for DW_OP_swap
failure while allocating exception port: %s\n
v16@?0^{dyld_image_s=}8
__UNIXSTACK
v40@?0r*8^v16{UUID=[16C]}24
IsFunction, 
_Z
byte
_sysenter_trap
shmem
x7
CS_TEST_EXCLAVEKIT_DIR
_x1
/private/preboot/Cryptexes/ExclaveOS
default
%u.%u
structs may contain only scalar or struct fields
must specify the underlying integer type for this enum (e.g. ': short', which was the default).
recursion-eliding sample discarded due to internal inconsistency
/System/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/dyld/
.symbols
[Invalid macho header] section size overflow
Cursor overflow, attempt to read uint8
ulong
[Invalid macho header] dysymtab load command is too small for content fields
 kCSSymbolOwnerDataFoundBinaryViaDsymPlist
 kCSSymbolOwnerDataEmpty
union value type may only be table/struct/string
Client side event: Unhandled xpc type\n
/System/Cryptexes/Rosetta/System/Library/dyld/
libc++.
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppSymbolOwnerCache.cpp
__debug_info
Region %s [%llx -> %llx) outside of relocations in mmap SOD\n
Cache stats:
txm
sample_remote_thread_with_frame_filter failed to get thread state for pid %u thread %u
dyld_shared_cache_
null-uuid                           
/private/preboot/
Merged, 
\"
Attempting to set mapping range override using CSRange with invalid length
CSSymbolOwnerGetContentForRange() gave unexpected length for on-disk content of a segment
Invalid analyzed archive entry for object file %s from archive %s at offset 0x%llx\n
_dyld_all_image_infos
Vectors of unions are not yet supported in at least one of the specified programming languages.
file_identifier
 hex digits
precision
CSCppCoreFileMemory
Stack empty for DW_OP_drop
int16
x10
ReportCrash
__objc_imageinfo
IsObjcMethod, 
unknown enum value: 
/usr/local/libexec/rosetta/runtime
Stack size less than 2 elements for DW_OP_plus
 | 
offset64
, max_TEXT_text_section: (
service
r14
fatal: invalid enum underlying type
MACH_HEADER
' to value of <
, originally at: 
Error decoding symbol owner from signature
x18
exclaves - failed to read segmentinfo_page
%u
$$$function-starts-fake-mangled-name$$$
shared
Child symbol archive address 0x%x could not be relocated to real address\n
DW_OP_call2 is not implemented.
Attempting to create CSRange with invalid length
user define attributes must be declared before use: 
Failed to start process notifications for pid %d (%d)\n
content != nullptr
 to 
x3
Field 
sfixed64
native_type_pack_name
CoreSymbolication target process: %s  pid: %d  path: %s\n                  parent process: %s  pid: %d  path: %s\n
x13
Stack empty for DW_OP_abs
size 0 structs not allowed
Remapped bytes from target are not valid at %#llx
illegal Unicode sequence (unpaired high surrogate)
missing type field for this union value: 
bytes
[Invalid macho header] uuid load command is too small for content fields
unordered_map::at: key not found
warning: 
unknown enum: 
 and 
0x
results
/private/preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
armv7k
Invalid specification abbrev index in DWARF: 
IsKnownLength, 
can't deprecate fields in a struct
underlying 
_target_page_size should be populated when targeting live tasks
CIE parse error: CIE augmentation string was too large for the fixed sized buffer of %d bytes.\n
<unknown>
Fixed-length array size is incorrect.
Stack size less than 2 elements for DW_OP_lt
[0x%016llx 0x%016llx] 
fnv1_64
r11
%s %s %sDATA:%p retain count (%d)\n
invalid utf-8 byte order mark
_dyld_process_info_for_each_image provided CoreSymbolication with invalid UTF-8 in path: %s, macho header address: %#llx, uuid: %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x\n
exclaves - unable to analyze this vsit_version using this tool
/private/preboot/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
<none>
namespace
cannot have more than one json object in a file
Size
major_version
[Invalid macho header] minimum load command goes beyond bounds
vector
Unhandled form in read string binding 
sptm
kern.exclaves_status
illegal character in string constant
invalid number, the exponent suffix of hexadecimal floating-point literals is mandatory: \"
CSCppDyldSplitSharedCache:\n
Corrupt archive entry in %s -- no acceptable header found for entry %s\n
/System/
long
bitset reset argument out of range
Sampling current thread of current analysis process is not safe - ignoring requesting to do so\n
/System/ExclaveCore/
field already exists: 
hash
FlexBuffers map has duplicate keys
Stack size less than 2 elements for DW_OP_ge
__restrict
message
cannot parse nested_flatbuffer as bytes unless --json-nested-bytes is set
Stack empty for DW_OP_bra
DW_OP_bit_piece is not implemented.
[Invalid macho header] inadequate sections size
v32@?0Q8r^{UUID=[16C]}16^v24
/Applications/
B24@?0{shared_ptr<CSCppSymbolOwner>=^{CSCppSymbolOwner}^{__shared_weak_count}}8
The argument index value is too large for the number of arguments supplied
x8
arm64_32
__PAGEZERO
__debug_abbrev
__DWARF
\\\"
vm info
CSSymbolOwnerGetContentForRange() gave null content
only one field may be set as 'key'
integer constant
The width option should not have a leading zero
dyld
mach
CSCppArchitecture: cannot answer is64Bit for cpu_type 
map
Caught exception in sample_remote_thread_with_frame_filter for pid %u: %s\n
v16@?0^{dyld_shared_cache_s=}8
a floating-point
a pointer
coldestElided
armv7f
NameSourceNlist, 
__Z
___Z
The only supported default for vectors is `[]`.
union
kCSSymbolOwnerDataEmpty
 cpuSubtype 
rad
enum
<Bad file name in .debug_info>
fnv1a_32
 formatting argument
x21
FORM_strx offset overflow
 kCSSymbolOwnerDataFoundBinaryNextToDsym
ip
Value is not initialized
KCSSymbolOwnerDataIsTextSegmentOnly
x6
x26
DW_OP_fbreg is not implemented
__text
Q16@?0^v8
cos
_start_wqthread
DW_OP_call_ref is not implemented.
proto
[Invalid macho header] source version load command is too small for content fields
main bin spec
float32
1
Type
01234567
r0
\t
flexbuffer attribute may only apply to a vector of ubyte
struct: wrong number of initializers: 
Cannot assign token starting with '
x15
CIE
OSBundleLoadAddress
union types vector smaller than union values vector for: 
The archive's version is not supported. A malformed file? \n
__debug_rnglists
shared can only be defined on strings
sfixed32
The argument index starts with an invalid character
v16@?0^{__CFData=}8
Historical timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
IsDyldStub, 
package
DYLD-STUB$$
_$s
nested_flatbuffer
/System/Library/Kernels
_$S
: 
deg
\\'
ENTRY COUNT: %zd\n
Could not remap archive address to real in debug maps
v16@?0r*8
DWARF %d form %u is unrecognized for reading non-indexed ranges.\n
MangledNameValid, 
Failed to load flatbuffer symbols schema file
FBS
_vas__segmentinfo_table
[Invalid macho header] minimum load command overflow
$$$debug-map-fake-name$$$
don't know how to parse .proto declaration starting with 
v16@?0r^{Symbolicator=[1C]}8
__DATA_CONST
DW_FORM_indirect not handled yet... 
Cursor overflow, attempt to read LEB
float
Stack size less than 2 elements for DW_OP_mod
Address
__TEXT
dyld_sim_shared_cache_
[Invalid macho header] dylinker load command is too small for content fields
%s parsing abbrev table -- stopping DWARF analysis of %s\n
ushort
option
only tables can be union elements in the generated language: 
0b
<CSSourceInfo: %p> [0x%016llx -> 0x%016llx) %s:%d
/SWE/
dyld_v
\tSegments:
\t%5.5fs create time\n
Cursor overflow, attempt to read FORM_string
invalid number: \"
unique_lock::unlock: not locked
/mach
reserved
UUID_String
B48@?0Q8Q16Q24*32Q40
Unknown typeRef
__debug_str
\t\t%s 0x%llx - 0x%llx\n
not a valid value for this field
__OBJC_CONST
flexbuffer
Unhandled CSCppSymbolOwnerData type_id: 
illegal UTF-8 sequence
\\t
Couldn't find _sigtramp symbol in expected dylibs\n
found_containing_segment
/System/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
Simulator
r12
x86_64
NONE
cpp_str_type
Developer
The format string contains an invalid escape sequence
0123456789abcdef
exclaves - failed to read vas_segment_t
Stack size less than 2 elements for DW_OP_eq
v48@?0{_CSRange=QQ}8^{_CSTypeRef=QQ}24^{_CSTypeRef=QQ}32Q40
create_symbol_owner_data -- UUID: 
$$$indirect-absolute-symbol$$$
out of range index into nlist array
Unknown hashing algorithm for 16 bit types: 
sign
libdispatch.dylib
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppCFDataMemory.cpp
all fields must have an 'id' attribute when --require-explicit-ids is used
CoreSymbolication target process: %s  pid: %d  path: %s\nCouldn't determine parent process ID\n
bitset set argument out of range
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSMemoryMappingCache.mm
Stack size less than 2 elements for DW_OP_and
__debug_addr
v32@?0^Q8^Q16*24
maximum parsing depth 
cpp_type
x9
CSCppCFDataMemory
$$$function-starts-fake-name$$$
Timeline modification failed -- dylibs overlap by 0x%llx:\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n    0x%llx-0x%llx [0x%llx] (%llu-%llu) %s\n
0123456789.
input file is empty
AppleInternal
error: UNIMPLEMENTED opcode DW_OP_xderef_size
traw_symbol_owner_data->retain_count() == 1
%p
NameSourceDwarfMIPSLinkage, 
null
bit_flags
Malformed fat header\n
internal: 
\\/
Failed to mmap %s\n
[0x%08x -> 0x%08x) %s [%s]
CSSymbolicatorCreateWithCSCppMachTaskFlagsAndNotification exception failure: %s
field `
An argument index may not have a negative value
MemoryCacheNotFoundException
enum value already exists: 
re
Encountered symbol with bad name reference during binary search
, text_len: 
The type option contains an invalid value for a string formatting argument
Unhandled form in read flag binding 
 LIVE
x28
attempted object resurrection
v24@?0r*8^v16
failed to parse 'vm info' LC_NOTE
Unhandled form in read ref binding 
fnv1_32
r13
Failed to relocate address %#llx in flatbuffer SOD
FunctionStarts, 
CSSymbolicator for core file
NameSourceDwarf, 
`vector64` attribute can only be applied on vectors.
CoreSymbolication - creating symbolicator for remote process\n
r4
%02hhX%02hhX%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX/%02hhX%02hhX%02hhX%02hhX%02hhX%02hhX/
[Invalid macho header] section not contained in segment
+inf
sint32
x1
x20
CoreSymbolication dyld load/unload notifier queue
r7
[Invalid macho header] load command out of bounds
-
\t%s: %llu\n
sint64
!override_range_overflows
Daemon Disconnect Queue
field id's must be non-negative number, field: 
/System/Library/Caches/com.apple.dyld/
com.apple.sptm
 instead got: 
uint64
kCSSymbolOwnerDataFaultedFromTask
.cdhash
\t%zd peak entries, %zdMB peak footprint\n
[CoreSymbolication] In DWARF data from %s:\n  .debug_line[%llx] file = %d is not a valid index\n
type referenced but not defined (check namespace): 
idempotent
v44@?0B8Q12Q20r*28r*36
liblibc_plat.dylib
ASSERT(%s) %s %d, %s\n
FORM_strx index overflow
keyPC
Cursor overflow, attempt to read dwarf_address
_$e
get_remote_thread_dispatch_queue2 thread_info(THREAD_EXTENDED_INFO) call failed for pid %u thread %u, err %d
Found _sigtramp symbol after %u tries\n
hottestElided
__TEXT_EXEC
attempting to access outside bounds of CSMemoryMapping
v16@?0r^{CSCppDyldSharedCache=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b1b19QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQIIQQQQIIQ}8
\t%zd entries, %zdMB footprint\n
MangledNameAllocated, 
Underlying type for union is not yet supported in at least one of the specified programming languages.
memory read of %u bytes at address 0x%8.8llx failed: 0x%8.8x
v24@?0{_CSTypeRef=QQ}8
$e
ReportCrashService
[Invalid macho header] segment load command is too small for content fields
\t%zd resymbolications attempted. (%zd replacements)\n
exclaves - found overlapping vas_segment_ts
Stack size less than 2 elements for DW_OP_gt
Unknown DWARF DW_OP value.
cmd
csharp_partial
Stack empty for DW_OP_neg
 reached
_dispatch_queue_offsets
CoreSymbolication warning: Unable to locate CIE at 0x%8.8x = 0x%8.8x - (0x%8.8x + 4)\n
[Invalid macho header] load command size overflow
%u.%u.%u.%u.%u
__debug_line
either all fields or no fields must have an 'id' attribute
../
x2
Caught exception in get_remote_thread_dispatch_queue2 for pid %u: %s
__PLK
Base relative index not in bounds of current address table in TDwarfAddressTableStream
Stack size less than 2 elements for DW_OP_shl
/System/Volumes/Data/SWE
 are both 
optional
libsystem_platform.dylib
[Invalid macho header] dylib load command name offset is invalid
v92@?0{UUID=[16C]}8i24{_CSArchitecture=ii}28Q36{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={
Null abbrev discovered in DWARF at index 
\t%s: %s (%llu)\n
native_custom_alloc can only be used with a table or struct definition
 + 1\"
alternate form
DW_OP_push_object_address is not implemented.
Inlined function %s [0x%llx, 0x%llx) outside of relocations in mmap SOD
CSCppTaskMemory pid:
/usr/lib/dyld
/System/Volumes/Preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
arm64
<No path>
UNLOAD
Unknown symbolicator signature type.
SEGMENT
basic_string
[Invalid macho header] inadequate segment load command vm size
_development
v24@?0^v8^v16
MangledNameSourceDwarf, 
$s
float64
v32@?0r^v8Q16Q24
string
Fields cannot be both optional and required.
, name: 
import
enum values need to be qualified by an enum type
-inf
too many unnamed fields in nested array
r2
v36@?0r*8Q16Q24i32
armv7
IsOmitFramePointer, 
only vectors of scalars are allowed to be 64-bit.
lr
!CSRangeIntersectsRange(prev->range, next->range)
Flags
Process exists but has not fully started -- dyld has initialized but libSystem has not
kCSSymbolOwnerDataFaultedFromDiskDyldSharedCache
v20@?0r*8I16
Fat header is malformed\n
nested vector types not supported (wrap in table first)
[]
failed to allocate dummy port representing thread
Unimplemented range list entry kind
Lock, 
'native_inline' can only be defined on structs, vector of structs or vector of tables
string constant
Stack size less than 2 elements for DW_OP_le
The archive's size is too small. A malformed file? \n
[Invalid macho header] symtab load command is too small for content fields
__debug_ranges
%s -- stopping DWARF analysis of %s\n
/usr/lib/swift/libswiftDemangle.dylib
only short, ushort, int, uint, long and ulong data types support hashing.
Unable to create symbolicator from dyld compact info for pid %d.\n
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSCppReferenceCount.hpp
aot_shared_cache
Attempt to mmap %s failed, %s\n
bool
Array defaults are not supported yet.
dyld_shared_cache
Stack empty for DW_OP_not
unique_lock::lock: already locked
Dwarf, 
attribute `vector64` implies `offset64` and isn't required.
Stack empty for DW_OP_plus_uconst
[Invalid macho header] sections size overflow
v24@?0^v8^B16
.
cpp_ptr_type
The type option contains an invalid value for 
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/Library/dyld/
inf
value
x4
[%3d] %#8.8llx %s %s\n
_objc_msgSend
Stack empty after evaluation
CoreSymbolication warning: Unable to locate CIE with ID 0x%8.8x\n
/Library/Caches/com.apple.xbs/87167522-396B-4CA2-A570-64FCCA6FFEDE/TemporaryDirectory.NUrcbM/Sources/CoreSymbolication/CoreSymbolication/CSBase.cpp
<redacted>
end of file in comment
key
Union
/private/preboot/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
ltmp
force_align
, value: 
fixed32
System
libsystem_kernel.dylib
__crashreporter_info__: %s\n
datatype already exists: 
The format specifier contains malformed Unicode characters
r6
task crashinfo
CSSymbolOwnerGetContentForRange() gave null content when requesting whole segment VM range
Stack size less than 2 elements for DW_OP_over
Stack size less than 3 elements for DW_OP_rot
uint32
only a non-optional scalar field can be used as a 'key' field
sin
Stack empty for DW_OP_deref
Unload Timestamp
error: UNIMPLEMENTED opcode DW_OP_xderef
/System/Cryptexes/Incoming/OS/System/Library/dyld/
[Invalid macho header] inadequate sum of sections size
attribute name must be either identifier or string: 
atan
CSMemoryMapping failed to deallocate underlying mapping with error %s (%d)
__OBJC_RO
file_identifier must be exactly 
ERROR, no symbol owners in signature
native_type
, raw_bytes_for_text: 
Arrays are not yet supported in all the specified programming languages.
incomplete enum declaration, values not found
unknown root type: 
[Invalid macho header] dylinker load command name offset is invalid
.atlas
OSBundleMachOHeaders
write_errno
__RESTRICT
Unknown hashing algorithm for 64 bit types: 
native_default
 option
ArithmeticException
IsJavaMethod, 
/System/Cryptexes/ExclaveOS
0
Length
rpc already exists: 
The format specifier should consume the input or end with a '}'
The format specifier for 
v24@?0{shared_ptr<CSCppSymbolOwner>=^{CSCppSymbolOwner}^{__shared_weak_count}}8
string_view::substr
\t%05.2f%% hit rate (%zd of %zd lookups hit, with %zd waits)\n
cpp_str_flex_ctor
exclaves - invalid exclave metadata
DW_OP_regx: No read register callback provided
kCSSymbolOwnerDataFoundDsym
illegal type id for: 
Expected `]` in vector default
 kCSSymbolOwnerDataFaultedFromDiskDyldSharedCache
0123456789-+.
0X
x16
.0
float constant
invalid offset and/or length for opcodes buffer
Stack empty for DW_OP_deref_size
Overflow calculating start of header in TDwarfAddressTableStream
Entry
x17
r9
Cursor overflow, attempt to skip FORM_block
service already exists: 
\\n
ExclaveKit
[Invalid macho header] size of load commands overflow
length of fixed-length array must be an integer value
false
[
CoreSymbolication - creating symbolicator for current process\n
sp
CoreSymbolication warning: error parsing %s at 0x%8.8llx in:\n\t__TEXT [0x%8.8llx - 0x%8.8llx) __eh_frame [0x%8.8llx - 0x%8.8llx) %s\n
[header: %s] Ignoring '%.16s %.16s' section [%#llx-%#llx] not contained in '%.16s' segment range [%#llx-%#llx]\n
int32
enum already exists: 
DW_OP_deref_size: No read memory callback provided
armv5tej
_gLoadedKextSummaries
 kCSSymbolOwnerDataFaultedFromDisk
Source info %s [%llx -> %llx) outside of relocations in mmap SOD\n
'key' field must be string, scalar type or fixed size array of scalars
unique_lock::lock: references null mutex
__DATA_DIRTY __all_image_info
unable to load include file: 
The precision option does not contain a value or an argument index
Override ranges must not overlap
test_value != 0
test_value >= value
Failed to create mmap archive: %s\n
/mach_kernel
ByteVector
include
content_length <= segment_vm_range.length
Symbol %s [%llx -> %llx) outside of relocations in mmap SOD\n
all image infos
DW_OP_call4 is not implemented.
v8@?0
system
UNNAMED
IsPrivateExternal, 
only non-scalar fields in tables may be 'required'
Replacement argument isn't a standard signed or unsigned integer type
attempting to access outside bounds of CSMemoryMappingSlice
__LINKEDIT
%s/%s
__debug_line_str
x5
x22
Caught exception in sample_remote_thread_with_frame_filter:\n%s\n
Error during directory iteration: %s \n
end of file
v32@?0Q8r*16r*24
Unsupported DW_ATE encoding in value argument: %u
<SymbolicationSession: %p> flags: 0x%x process count: %llu
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
illegal Unicode sequence (unpaired low surrogate)
End of input while parsing an argument index
locale-specific form
infnanINFNAN
pc
__.SYMDEF
Vector defaults may only be `[]`.
, found: 
fnv1_16
cpp_ptr_type_get
Overflow
[Invalid macho header] unreasonable number of sections
PRIVATE_KEY:0x%llx 
kCSAllTimes
com.apple.txm
IsThumb, 
Failed to parse flatbuffer symbols schema
 
<Invalid path>
declaration expected
01
length of fixed-length array must be positive and fit to uint16_t type
Index out of range for DW_OP_pick
Incomplete type in struct is not allowed, type name: 
 in 
Unable to access flatbuffer symbols schema at %s
\\x{
NULL
\n\n
CSSymbolOwnerGetContentForRange() failed to find segment
/System/DriverKit/System/Library/dyld/
 for symbol entry.
libsystem_pthread.dylib
length == mapping_content_vm_range_and_source.vm_range.length
armv6
.x1
<Invalid file path>
/%s
pP
%0hhx
failed to parse thread load command
LOAD
NameValid, 
deprecated
exclaves - unable to determine dyld shared cache range for ExclaveKit target
syntax
Error decoding symbolicator from signature
; 
field name can not be the same as table/struct name
type mismatch or invalid value, an initializer of non-string field must be trivial ASCII string: type: 
v24@?0r*8Q16
.eEpP
bit flag out of range of underlying integral type
nan
B28@?0I8Q12^B20
[Invalid macho header] dylib load command is too small for content fields
v40@?0^v8r^{CSCppArchiveEntry=[16c][12c][6c][6c][8c][10c][2c]}16Q24^B32
' is not a table type.
\\u{
content_getting_found_segment
DW_OP_deref: No read memory callback provided
root type must be a table
rpc_service
kCSSymbolOwnerDataFoundBinaryViaDsymPlist
$$$bad-name-in-nlist$$$
table
get_remote_thread_dispatch_queue2 thread_info(THREAD_IDENTIFIER_INFO) call failed for pid %u thread %u, err %d
[Invalid macho header] function starts load command is too small for content fields
Requested vm range length in %s does not exist in file.\n
Wrong refcount on traw_symbol_owner_data
code: 
default values are not supported for struct fields, table fields, or in structs.
wrong number of unnamed fields in table vector
DW_OP_breg: No read register callback provided
x86_64h
uint16
<CSRegion: %p> [0x%016llx -> 0x%016llx) %s
failed to open core file
Name
.stripped.sharedcache
__DWARFA
struct
No symbol owners pointer in flatbuffer\n
<CSSymbol: %p> %s
cannot parse value starting with: 
true
/usr/
Mmap string table has reached its maximum size of 4G. Mmap archive will not be created\n
v16@?0r^{InlineSymbol=[1C]}8
<CSSymbolicator: %p> %s (pid:%d%s) {\n
}
__sigtramp
error: DW_OP_deref_size attempted to dereference a value with a size larger than a target address.
FDE
.dSYM/Contents/Resources/DWARF/
.development
unable to locate include file: 
DW_OP_div divide by zero
entry
/private/preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
IsObjcMethodValid, 
/System/Volumes/Preboot/Cryptexes/ExclaveOS
Processing header for %s\n
 - %s
kCSSymbolOwnerDataIsObjCGCSupported
r15
Caught exception in get_remote_thread_dispatch_queue2:\n%s\n
failed to parse 'addrable bits' LC_NOTE
Process exists but _dyld_process_info_create() failed with error %#x
fields using 64-bit offsets are not yet supported in at least one of the specified programming languages.
 use(s) of pre-declaration enum not accounted for: 
Out of bounds children index iterating inline ranges
native_include
x24
<Invalid filename>
[0x%016llx -> 0x%016llx) %s [%s]
int64
', alignment must be a power of two integer ranging from the type's natural alignment 
enum value does not fit, \"
a character
fp
x0
v16@?0r^v8
%@\n
$S
machdep.virtual_address_size
mapped_memory_resume_target
exclaves - invalid segmentinfo_page address
mapped_memory->_target_page_size.has_value()
underlying type of bit_flags enum must be unsigned
attribute
r10
swift_demangle_getSimplifiedDemangledName
int8
Anonymous
Leaking private implementation, verify all objects have similar annotations
symbols.fbs
0123456789abcdefghijklmnopqrstuvwxyz
[%3d] %#8.8llx fp:%#8.8llx %s %s\n
error handling EST message: %s (%u)\n
armv4t
UNIVERSE
<deduplicated_symbol>
unknown
includes must come before declarations
DW_OP_piece is not implemented.
__image_info
create_mmap_archive_arch_specific (TEXT_text) -- UUID: 
fixed64
CSSymbolOwnerGetContentForRange() gave nonsensical segment content length
Stack size less than 2 elements for DW_OP_ne
Process exists but has not started -- it is launched-suspended
, flags:
original_order
v32@?0r*8Q16Q24
__OBJC_RW
__TEXT SEGMENT
tan
extensions
/System/x86Support/System/Library/dyld/
__PPLTRAMP
Stack size less than 2 elements for DW_OP_shr
Empty object_file_path in mach-o header: %s\n
!
CSCppTaskMemory: retired memory must be contained by live memory
nested_flatbuffer attribute must be a string (the root type)
an integer
x25
 would clash with generated functions for field 
\xf0R
InvalidCSRangeBoundsException
[Invalid macho header] inadequate size of a load command
v24@?0r^{macho_fat64_arch={fat_arch_64=iiQQII}}8^B16
ubyte
[Invalid macho header] load command at %#llx goes beyond bounds
any
MangledNameSourceNlist, 
asin
The format string terminates at a '{'
, constant does not fit 
exclaves - failed to dup() core file file descriptor
/System/ExclaveKit/
 @ 
<CSSymbolOwner: %p> %s %s%s
Unhandled dwarf attribute in Debug Line Table 
the default 'null' is reserved for declaring optional scalar fields, it conflicts with declaration of enum '
` for 
acos
treating warnings as errors, failed due to above warnings
Using automatic argument numbering in manual argument numbering mode
Cursor overflow, attempt to skip FORM_block2
attribute already found: 
memory read of %u bytes at address 0x%8.8llx failed: %s
OSBundleExecutablePath
load binary
exclaves - failed to get any segmentinfo_pages
CSCppDyldSharedCache path:
/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/
v24@?0r^{macho_fat_arch={fat_arch=iiIII}}8^B16
, DSYM Path: 
kern.uuid
vector64
root_type
Using manual argument numbering in automatic argument numbering mode
The value of the argument index exceeds its maximum value
os_security_config_get_for_task
TEXT_text_location %llx outside of relocations in mmap SOD\n
The replacement field misses a terminating '}'
Failed to find memory cache for the given task
/System/Volumes/Data/home
Unable to acquire mach service port, symbol cache unavailable\n
required field is missing: 
constant name expected
all enum values must be unique: 
__FAILED
v16@?0^{dyld_cache_mapping_info=QQQII}8
, TEXT_text_section.value(): 
kCSBeginningOfTime
group
oneof '
The argument index should end with a ':' or a '}'
armv7s
kCSSymbolOwnerDataFaultedFromDisk
illegal character: 
, (symbol owner: 
Unimplemented: 
, archive_TEXT_text: 
com.apple.CoreSymbolication
only string and vectors can have `offset64` attribute applied
[Invalid macho header] fileset entry load command is too small for content fields
, 
illegal Unicode sequence (multiple high surrogates)
__TEXT runtime_entry
CoreSymbolication warning: fde.addrRange.location 0x%8.8llx isn't in  the __TEXT segment [0x%8.8llx - 0x%8.8llx)\n
Attempt to use ISA32Big when it is not defined
Unknown hashing algorithm for 32 bit types: 
Unexpected number of symbol owners in flatbuffer created from JSON: %u\n
mapped_memory_suspend_target
SYMB
SYMBOL OWNER: %s\n
kCSNow
unexpected floating-point constant: 
0B
Offset not in bounds of TDwarfAddressTableStream
) 
_kasan
identifier
Cursor overflow, attempt to skip ULEB
OSBundleUUID
 characters
v56@?0{mapped_memory_core_file_dumped_region_info_t=QQQQii}8^B48
Stack size less than 2 elements for DW_OP_shra
/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
, is_dyld_shared_cache: 
over release
<Invalid region name>
CSCppTaskMemory: range values must not overlap
_length
r1
DriverKit
Failed to find symbolicators in flatbuffer created from JSON\n
fnv1a_64
/{}/{}/{}/{}/{}
<CSRegion: %p> [0x%08llx -> 0x%08llx) %s
\t%zd misses (%zd create, %zd failed)\n
Empty function_name in mach-o header: %s\n
type mismatch: expecting: 
failed to parse 'task crashinfo' LC_NOTE
thread_info failed due to %s
Transformed binary is invalid
/System/Cryptexes/OS/System/Library/dyld/
Attempt to release an unhandled typeID
Base relative index overflow in TDwarfAddressTableStream
id
field set more than once: 
__TEXT __stubs
exclaves - failed to read segmentinfo
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
:
)
/usr/lib/system/libsystem_platform.dylib
Cursor overflow, attempt to skip FORM_block4
_
Could not remap archive address to real in debug maps inline enumeration
Union defaults must be NONE
type must be integral
cannot extend unknown message type: 
Protobuf has non positive number in reserved ids
ERROR, unhandled signature version
CSCppArchitecture: cannot answer isLittleEndian for cpu_type 
libstdc++.
__debug_str_offs
CSMemoryMappingSlice
CSMemoryMapping
CSMemoryMappingCache
```
