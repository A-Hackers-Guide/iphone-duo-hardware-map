# `/usr/lib/system/libdyld.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 363,504 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 31 (Size: 3064)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (12)

- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3, upward)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15, upward)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6, upward)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2, upward)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1, upward)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0, upward)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1, upward)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, upward)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0, upward)`
- `/usr/lib/libc++abi.dylib (compatibility version 1.0.0, current version 2200.32.0, upward)`
- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0, upward)`

## Entitlements

```xml
  - no entitlements
```

## Strings (552)

```
v32@?0{span<const unsigned char, 18446744073709551615UL>=*Q}8^B24
LC_FUNCTION_STARTS
load command #%d string extends beyond end of load command
%.*s missing preceding BIND_OPCODE_SET_DYLIB_ORDINAL
LC_LOAD_DYLINKER
LC_MAIN
malformed mach-o image: symbol table too large
album file has too many slices (%u, max=%u)
v48@?0{Slice={CString=*Q}{span<const unsigned char, 18446744073709551615UL>=*Q}}8^B40
unknown
trie too deep > 255
too many LC_UUID load commands
can't have LC_MAIN and LC_UNIXTHREAD load commands
origlibPath: %s\n
MH_MAGIC
malformed uleb128 in function variants payload for %.*s
segment '%s' vm address out of order
visionOS-exclaveCore
multiple LC_FUNCTION_STARTS load commands found
multiple LC_DYLD_EXPORTS_TRIE load commands found
LC_SEGMENT_64
load command #%d LC_DYLD_INFO size wrong
rebase opcodes
LC_UUID
load command #%d %.*s size too small
DYLD_CHAINED_PTR_64
DYLD_CHAINED_PTR_ARM64E_FIRMWARE
duplicate segment name '%s'
LC_ENCRYPTION_INFO_64
n <= _usedCount
%.*s segment offset 0x%08llX beyond segment '%.*s' size (0x%08llX)
malformed import table, imports_offset too large
malformed uleb128 for child node offset at 0x%04lX
malformed mach-o has no LINKEDIT
tvOS
album entry next-offset=0 but count is wrong
chained fixups
LC_SUB_FRAMEWORK
platformAndVersions_block_invoke
section '%s' has an empty segment name
zippered(macOS/Catalyst)
weak-def
malformed uleb128
pthread_key_create() failed
malformed trie, childNodeOffset==0
unknown FunctionVariantsRuntimeTable::Kind (%d)
file range of segment '%s' overlaps segment '%s'
LC_DYLD_EXPORTS_TRIE
section '%s/%s' has a non-zero nreloc field
v28@?0r^v8I16^B20
arm64e
chained fixups, imports_count (%d) exceeds max of %d
malformed uleb128 in value payload for %.*s
buffer does not start with MH_MAGIC[_64]
LC_VERSION_MIN_WATCHOS
section '%s/%s' has offset=0 but is not a zero-fill section type
scrName:     %s\n
malformed mach-o image: indirect symbol table iundefsym != iextdefsym+nextdefsym
/usr/lib/system/libsystem_kernel.dylib
/usr/lib/system/host/liblaunch_sim.dylib
macOSX
%.*s missing preceding BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB
0 && \"unknown arch\"
duplicate linked dylib '%s'
LINKEDIT overlap of %s and %s
LC_SEGMENT
/usr/lib/system/libsystem_pthread_debug.dylib
iOS
REBASE_OPCODE_DO_REBASE_ULEB_TIMES_SKIPPING_ULEB
armv7m
multiple LC_TARGET_TRIPLE load commands found
REBASE_OPCODE_DO_REBASE_ADD_ADDR_ULEB
shared cache fixup formate does not support binds
multiple LC_ATOM_INFO load commands found
load command #%d LC_?? size is wrong
cpu type/subtype in slice (%s) does not match fat header (%s)
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) too small
authenticated arm64e, 4-byte stride, target vmoffset
thumbv7m
__chain_fixups
vmAddress (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
ppc
armv8.1m.main
mh.sizeofcmds extends beyond buffer size
LC_DYLD_ENVIRONMENT
malformed mach-o image: indirect symbol table too large
invalid x86_64 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
chained fixups, seg_count exceeds number of segments
multiple LC_FUNCTION_VARIANTS load commands found
LC_LINKER_OPTION found in non-object file
FunctionVariantFixups segOffset=0x%08X exceeds segment size (0x%llX)
load command #%d %.*s not a dylib load command
macCatalyst
<invalid-lib-ordinal>
/usr/lib/system/libsystem_platform_debug.dylib
free standing
malformed trie, terminalSize extends beyond trie data at offset=0x%04lX
{Error={CStringBuilderBufferOverflowSafe<128>={span<char, 18446744073709551615UL>=*Q}QiC[128]}C}40@?0{CString=*Q}8{span<const unsigned char, 18446744073709551615UL>=*Q}24
DYLD_CHAINED_PTR_ARM64E
macOS
watchOS-exclaveCore
Platform.cpp
%.*s has unknown library special ordinal (%d)
section in segment '%s' has an empty section name
range.fileOffset+range.size <= _linkeditFileOffset+_linkeditContent.size()
Platform
thumbv8.1m.main
BIND_OPCODE_DO_BIND_ADD_ADDR_IMM_SCALED
LC_DATA_IN_CODE
__DATA_CONST segment permissions is not 'rw-'
fat file has too many slices (%d)
arm64e.kernel.v1
PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE_V3
found LC_ID_DYLIB found in non-MH_DYLIB
too many LC_RPATHs
visionOS-kernelKit
big endian mach-o file
v48@?0{CString=*Q}8Q24Q32^B40
missing LC_LOAD_DYLIB (must link with at least libSystem.dylib)
section '%s/%s' start address overlaps previous section
tvOS-exclaveKit
iOS-kernelKit
duplicate LC_RPATH '%s'
macOS-exclaveCore
REBASE_OPCODE_DO_REBASE_IMM_TIMES
unknown rebase opcode 0x%02X
album entry beyond end of file
album entry next-offset=0x%X not 16-byte aligned
kern.grade_cputype
arm64e.x1.old
segIndex (%d) and segOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
missing LC_MAIN or LC_UNIXTHREAD in main executable
load command #%d string offset (%u) outside cmd size (%lu)
visionOS-simulator
v8@?0
re-export
exports trie
LC_VERSION_MIN_TVOS
load command #%d LC_ENCRYPTION_INFO size wrong
armv6m
malformed load command (%d of %d) at offset=0x%lX with mh=%p, size (0x%X) too small
arm64.x1
BIND_SYMBOL_FLAGS_NON_WEAK_DEFINITION
generic 32-bit, 4-byte stride
album entry next-offset not forward
load command #%d LC_SEGMENT fileoff (%lu) too large
_dyld_legacy_introspection_vtable
ifGrowableEnsureSpaceForAppending
linkeditBytes
0
unsupported thread-local, larger than 4GB
BIND_OPCODE_DO_BIND
vmOffset too large for %s
v44@?0{Architecture=ii}8Q16Q24C32^B36
__TEXT
chained fixups, dyld_chained_starts_in_segment for segment #%d overruns imports table
code signature
unknown platform
dyld cache thread-local format too old
malformed load command (%d of %d) at offset=0x%lX with mh=%p, size (0x%X) is too large, load commands end at offset 0x%lX
LC_UNIXTHREAD
v20@?0{LinkEditRange=IIi}8
init
invalid bindOrdinal (%d) out of range (max=%d)
%s slice extends beyond end of file
duplicate linked dylib are deprecated ('%s')
malformed mach-o contains LC_DYLD_CHAINED_FIXUPS and local relocations
<main-executable>
'%s' segment vm range wraps
unknown mach-o filetype (%u)
album entry triple string missing nul terminator
chained fixups, pointer_format not same for all segments %d and %d
multiple LC_SEGMENT_SPLIT_INFO load commands found
LC_FUNCTION_VARIANTS
armv7
distance between fixups (%ld) is not encodable in chain for fixup at %.*s+0x%0lX
FunctionVariants tableCount=%u is too large for size=%lu
segment '%s' file offset out of order
mis-aligned LINKEDIT content '%s', fileOffset=0x%08X
LC_ID_DYLINKER
future
lazy-load
BIND_OPCODE_DO_BIND_ULEB_TIMES_SKIPPING_ULEB
mergeable dylib info
range.fileOffset >= _linkeditFileOffset
tvOS-simulator
DYLD_CHAINED_PTR_64_KERNEL_CACHE
malformed mach-o contains LC_DYLD_INFO_ONLY and external relocations
dyld cache info
load command #%d has too few strings (%d) expected (%d)
section '%s/%s' align field (1 << %d) that is too large for VM to support
armv4t
upward,delay-init
load command #%d LC_ROUTINES_64 not support in 32-bit mach-o
%.*s text binds not supported for architecture
LC_SYMTAB
v56@?0r*8r*16Q24C32C36S40I44^B48
thumbv6m
thumbv8m.main
file too small
album file too short for slice count
mh.sizeofcmds too large
LC_LOAD_WEAK_DYLIB
xrOS-simulator
duplicate %s slices
__DATA segment permissions is not 'rw-'
thread-local
vt && \"Dyld.framework missing _dyld_legacy_introspection_vtable\"
%.*s unknown bind type %d
chained fixups, unknown header version (%d)
indirect symbol table
LC_DYLD_INFO
/System/ExclaveKit/usr/lib/libSystem.dylib
arm64e shared cache, 8-byte stride, target vmoffset
/usr/lib/libSystem.B.dylib
multiple LC_DYSYMTAB load commands found
bind opcodes
macOS-exclaveKit
absolute
LC_LOAD_DYLIB
load command #%d LC_SYMTAB size wrong
%s segment permissions has invalid bits set (0x%08X)
shared cache slide v2 does not support binds
chained fixups, pointer_format=%d in segment #%d does not match pointer size
load commands do not fit in __TEXT segment filesize
unknown cpu type in LC_UNIXTHREAD
arm64e.v1
addend (%lld) cannot fit in fixup at %.*s+0x%0lX
dynamic-resolver
handle && \"Dyld.framework is required\"
album entry triple string contains nul
x86_64
riscv32
%.*s pointer bind is in non-writable segment '%.*s'
multiple LC_DYLD_INFO load commands found
LC_DYLD_INFO_ONLY
segment load command has an empty segment name
p->value != 0 && \"PlatformInfo value uninitialized, this might be a problem with C++ static initializers order\"
(_kind != Kind::reExport) && (_kind != Kind::absolute)
chained fixups, different max_valid_pointer values seen in different segments
vmOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
chained fixups, in segment #%d page_start[%d]=0x%04X exceeds page size
DYLD_CHAINED_PTR_32_FIRMWARE
function variants
malformed thread-local, offset=0x%lX is larger than total size=0x%lX
%.*s missing preceding BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM
%.*s text bind is in non-executable segment
unknown mh.filetype %d
section '%s' size too large 0x%lX
%.*s pointer rebase is in non-writable segment '%.*s'
GradedArchitectures.cpp
missing LC_UUID load command
objModTime:  0x%08X\n
implOffset
%.*s text bind is in writable segment
invalid arm flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
tvOS-exclaveCore
watchOS-kernelKit
DYLD_CHAINED_PTR_ARM64E_SEGMENTED
malformed uleb128 for terminal payload size at offset=0x%04lX
load command #%d LC_LINKER_OPTION size too small
LC_MAIN not allowed in .o files
/usr/lib/system/libsystem_platform.dylib
segment '%s' filesize (0x%lX) exceeds vmsize (0x%lX)
xrOS-exclaveKit
DYLD_CHAINED_PTR_32_CACHE
__playground
malformed mach-o contains LC_DYLD_INFO and LC_DYLD_CHAINED_FIXUPS
load command #%d string start offset too small
xrOS-exclaveCore
chained fixups, symbols_format unknown (%d)
load commands length (%llu) exceeds length of file (%llu)
v40@?0^I8{CString=*Q}16B32B36
chained fixups, page_size not 4KB or 16KB in segment #%d
DYLD_CHAINED_PTR_SHARED_CACHE_V2
multiple LC_ROUTINES[_64] load commands found
data in code
v52@?0{CString=*Q}8i24B28C32Q36^B44
overlapping slices
missing __TEXT segment
load command #%d LC_FILESET_ENTRY size too small
iOS-simulator
iOS-exclaveCore
%.*s unknown rebase type %d
v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32
__TEXT segment fileoffset is not zero
thumbv7em
chained fixups, max_valid_pointer (0x%x) too small for image last vm address 0x%llx
v32@?0{Platform=^{PlatformInfo}I}8{Version32=I}24{Version32=I}28
external relocations
section '%s/%s' start offset overlaps previous section
LC_???
load command #%d LC_ROUTINES size too small
bridgeOS
B56@?0{CString=*Q}8Q24Q32Q40^B48
weak-link
mis-aligned LINKEDIT string pool, fileOffset=0x%08X
LC_FILESET_ENTRY
invalid arm64 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
section '%s' end address 0x%lX is beyond containing segment's end address 0x%0lX
section '%s/%s' has a zero-fill section type, but offset field is not zero
objSubType:  0X%02X\n
arm64e.kernel.v2
%.*s pointer bind is in executable segment '%.*s'
loadableFrom
upward
load command #%d LC_ENCRYPTION_INFO_64 size wrong
/System/DriverKit/usr/lib/libSystem.dylib
FunctionVariantFixups segIndex=%d exceeds number of segments (%lu)
multiple LC_FUNCTION_VARIANT_FIXUPS load commands found
load command #%d %.*s not supported in .o files
/System/Library/PrivateFrameworks/Dyld.framework/Dyld
armv7k
multiple LC_DYLD_CHAINED_FIXUPS load commands found
sepOS
xrOS
chained fixups, imports array overlaps symbols
1-byte stride, for x86_64 kernel cache
malformed uleb128 in resolvers payload for %.*s
LC_VERSION_MIN_IPHONEOS
file does not start with FAT_MAGIC
/usr/lib/system/
v40@?0{PlatformAndVersions={Platform=^{PlatformInfo}I}{Version32=I}{Version32=I}{Version32=I}{Version32=I}}8
v32@?0{CString=*Q}8^B24
LC_ENCRYPTION_INFO
LC_CODE_SIGNATURE
section '%s' start address 0x%lX is before containing segment's address 0x%0lX
slice is not page aligned
album entry triple string extends past end of file
chained fixups, unknown imports_format (%d)
DYLD_CHAINED_PTR_X86_64_KERNEL_CACHE
invalid FunctionVariantsRuntimeTable length %lu for count=%u
too many segments %llu (max 255)
function starts
linker optimization hints
size (%llu) of thread-locals section %.*s is not a multiple of %lu
armv8m.main
<flat-namespace>
load command #%d LC_SEGMENT[_64] size too small
macOS-kernelKit
fat file too short
PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE
file does not start with album magic
armv7em
chained fixups, imports_offset exceeds LC_DYLD_CHAINED_FIXUPS size
entry %d extends to 0x%08X which beyond total size 0x%08lX
weak-link,upward,delay-init
scrDir:      %s\n
driverKit
dyldFrameworkVtable_block_invoke
album overlapping slices %d and %d
chained fixups, unknown pointer_format in segment #%d
LC_SUB_CLIENT
__TEXT segment permissions is not 'r-x'
visionOS
v28@?0r^v8B16^B20
TPRO regions should not be writable on entry to dyld\n
file does not start with MH_MAGIC[_64]: 0x%08X 0x%08X
/System/DriverKit/usr/lib/system/
chained fixups, starts_offset exceeds LC_DYLD_CHAINED_FIXUPS size
watchOS
arm64.x2
Allocator.cpp
growTo
chained fixups, seg_count does not match number of segments
LC_DYLD_INFO not allowed in .o files
section '%s' segment name '%s' does not match containing segment's name '%s'
REBASE_OPCODE_DO_REBASE_ULEB_TIMES
/usr/lib/system/libsystem_pthread.dylib
libPath:     %s\n
Symbol.cpp
makeFromRawSlice
DYLD_CHAINED_PTR_ARM64E_USERLAND
multiple LC_SYMTAB load commands found
vm range of segment '%s' overlaps segment '%s'
dyld_introspection.cpp
x86_64 shared cache slide v2, 4-byte stride, target is vm offset
too many linked dylibs
invalid i386 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
Array.h
duplicate slice triple for %d and %d
LC_TARGET_TRIPLE
target vm address not in any segment
Header.cpp
weak bind opcodes
watchOS-exclaveKit
weak-link,upward
load command #%d LC_SEGMENT filesize (%lu) too large
rebase opcodes terminated early at offset %zu of %zu
authenticated arm64e, 8-byte stride, target vmoffset
MH_DYLIB is missing LC_ID_DYLIB
MH_EXECUTE has MH_DYLIB_IN_CACHE bit set
malformed mach-o contains LC_DYLD_INFO_ONLY and local relocations
LC_SUB_LIBRARY
%.*s pointer rebase is in executable segment '%.*s'
album slice extends past end of file
arm64e.x2
launchable
multiple LC_ID_DYLIB load commands found
generic 64-bit, 4-byte stride, target vmadddr
DYLD_CHAINED_PTR_32
malformed mach-o image: indirect symbol table ilocalsym != 0
xrOS-kernelKit
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) is too large, load commands end at %p
arm64
arm64e.x2.kernel
authenticated arm64e, 4-byte stride, target vmaddr
weak-link,delay-init
weak-link,lazy-load
%.*s segment index %d too large
__DATA_CONST segment missing SG_READ_ONLY flag
album slice size overflow
unknown bind opcode 0x%02X
delay-init
???
multiple LC_ID_DYLIB found
malformed import table, imports[%d].name_offset (%d) out of range
bind ordinal (%u) too large in fixup at %.*s+0x%0lX
FunctionVariants is too small
Mac Catalyst
{Error={CStringBuilderBufferOverflowSafe<128>={span<char, 18446744073709551615UL>=*Q}QiC[128]}C}24@?0{span<dyld::ThreadLocalVariables::Thunk, 18446744073709551615UL>=^{Thunk}Q}8
kr == 0
load commands do not fit in __TEXT segment vmsize
malformed load command (%d of %d) at offset=0x%lX with mh=%p, off end of load commands
can't zip with invalid platform
DYLD_CHAINED_PTR_ARM64E_USERLAND24
LC_LOAD_UPWARD_DYLIB
LC_SUB_UMBRELLA
watchOS-simulator
malformed load command (%d of %d) at %p with mh=%p, off end of load commands
v16@?0^{TerminatorList=^{TerminatorList}Q[7{Terminator=^?^v}]}8
armv7s
%.*s has library ordinal too large (%d) max (%d)
chained fixups, seg_info_offset for segment #%d exceeds LINKEDIT size
LC_VERSION_MIN_MACOSX
LC_BUILD_VERSION
arm64_32
malformed import table, symbols_offset too large
malformed mach-o contains LC_DYLD_CHAINED_FIXUPS and external relocations
load command #%d %.*s path offset too small
visionOS-exclaveKit
OverflowSafeArray failed to allocate %llu bytes, vm_allocate returned: %d\n
v92@?0{CString=*Q}8i24B28C32Q36B44i48{CString=*Q}52B68q72B80^B84
chained fixups, in segment #%d page_start[%d]=0x%04X multi-start chains not supported in 64-bit archs
malformed trie, node offset=0x%04lX past end=0x%04lX
section '%s/%s' align field (1 << %d) does not match address (0x%llX)
v56@?0{Slice={Architecture=ii}{span<const unsigned char, 18446744073709551615UL>=*Q}QC}8^B48
multiple LC_MAIN load commands
function variant fixups
LC_LINKER_OPTION
%.*s text rebase is in writable segment '%.*s'
malformed trie node, child node name extends beyond trie data
symbol table
symbol strings
objPath:     %s\n
!sMemoryManagerInitialized
album entry next-offset=0x%X not after triple string
firmware format does not support binds
generic 64-bit, 4-byte stride, target vmoffset
re-export name change not nul terminated
LC_REEXPORT_DYLIB
bridgeOS-kernelKit
malformed uleb128 in flags for %.*s
arm64e.x1.kernel
chained fixups, unknown pointer_format (%d)
LC_MAIN not allowed for driverkit
v24@?0r^{load_command=II}8^B16
v24@?0r^v8r^v16
Image.cpp
arm64e.x1
BIND_OPCODE_DO_BIND_ADD_ADDR_ULEB
segment '%s' content (fileOffset: 0x%lX -> 0x%lX) extends beyond end of file (length: 0x%llX)
album entry next-offset=0x%X past end of file
multiple LC_MAIN or LC_UNIXTHREAD load commands found
load command #%d %.*s name offset too small
DYLD_CHAINED_PTR_64_OFFSET
multiple LC_UNIXTHREAD load commands
malformed mach-o image: indirect symbol table iextdefsym != nlocalsym
thumbv7s
chained fixups, in segment #%d overflow page_start[%d]=0x%04X is before previous at 0x%04X\n
v48@?0{CString=*Q}8{span<const unsigned char, 18446744073709551615UL>=*Q}24^B40
tableOffsets[%d]=0x%08X which is > total size 0x%08lX
LC_RPATH
LC_DYLD_CHAINED_FIXUPS
chained fixups, in segment #%d overflow page_start[%d]=0x%04X exceeds page size
authenticated arm64e, 8-byte stride, target segIndex/offset8
allocStart != 0
v24@?0r^v8^B16
chained fixups, dyld_chained_starts_in_segment[%d].segment_offset does match actual segment offset
local relocations
load command #%d LC_DYSYMTAB size wrong
load command #%d LC_SEGMENT size (%lu) does not match section count (%u)
DYLD_CHAINED_PTR_ARM64E_KERNEL
chain overflow index out of range %d (max=%d) in segment #%d
buffer too small
iOS-exclaveKit
incompatible platforms: %s - %s
CString.cpp
old arm64e bind opcodes not supported
LC_LINKER_OPTION has count=%d, only 1 or 2 is valid
N/A
<weak-def-coalesce>
thread locals not initialized
lazy bind opcodes
trunc
bad or unknown fileoffset/size for LINKEDIT
LC_ID_DYLIB
tvOS-kernelKit
%.*s missing preceding REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB
multiple LC_ENCRYPTION_INFO_64 load commands found
LC_FUNCTION_VARIANT_FIXUPS
thread_key_t %lu, larger than uint32_t
/usr/lib/dyld
arm64e.old
unknown exports flag bits in value payload for %.*s
%.*s text rebase is in non-executable segment '%.*s'
LINKEDIT content '%s' extends beyond end of segment
/System/ExclaveKit/usr/lib/system/
<this-image>
x86_64h
trie cycle at node offset=0x%04llX
LC_SEGMENT_SPLIT_INFO
err.noError()
v24@?0{span<const mach_o::MappedSegment, 18446744073709551615UL>=^{MappedSegment}Q}8
16777228--2147483636
armv6
code signature not 16-byte aligned, fileOffset=0x%08X
LC_DYSYMTAB
load command #%d LC_ROUTINES not support in 64-bit mach-o
__LINKEDIT segment permissions is not 'r--'
c++ exception thrown in static initializer
chained fixups, page_start array overflows size
malformed load command (%d of %d) at offset=0x%lX with mh=%p, cmdsize=0x%X is not pointer sized
linkeditFileOffset != 0 && \"LINKEDIT segment not found\"
slice headers extend beyond end of file
thumbv7
__LINKEDIT
v16@?0{Architecture=ii}8
thumbv7k
authenticated arm64e, 4-byte stride, for kernel cache
last entry in FunctionVariantsRuntimeTable entries is not 'default'
load command #%d unknown required load command 0x%08X
i386
malformed import table, unknown imports_format=%d
LC_ATOM_INFO
load command #%d LC_UUID size wrong
load command #%d LC_ROUTINES_64 size too small
%.*s text rebase not supported for architecture
arm64e.kernel
section '%s/%s' has a non-zero reloff field
firmware
authenticated arm64e, 8-byte stride, target vmadddr
```
