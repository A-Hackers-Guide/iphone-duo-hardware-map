# `/usr/lib/system/libdyld.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 363,504 bytes.

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
shared cache slide v2 does not support binds
linker optimization hints
__TEXT segment permissions is not 'r-x'
album file has too many slices (%u, max=%u)
thumbv7s
malformed trie, node offset=0x%04lX past end=0x%04lX
xrOS-kernelKit
distance between fixups (%ld) is not encodable in chain for fixup at %.*s+0x%0lX
unknown mh.filetype %d
code signature not 16-byte aligned, fileOffset=0x%08X
bind opcodes
LC_SEGMENT
chain overflow index out of range %d (max=%d) in segment #%d
DYLD_CHAINED_PTR_64_OFFSET
weak-link,upward
too many segments %llu (max 255)
duplicate segment name '%s'
LC_DYLD_INFO
N/A
watchOS-exclaveKit
LC_LOAD_WEAK_DYLIB
v32@?0{Platform=^{PlatformInfo}I}8{Version32=I}24{Version32=I}28
invalid arm64 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
watchOS-exclaveCore
album entry next-offset=0x%X not after triple string
DYLD_CHAINED_PTR_SHARED_CACHE_V2
section '%s/%s' align field (1 << %d) that is too large for VM to support
%s slice extends beyond end of file
chained fixups, seg_info_offset for segment #%d exceeds LINKEDIT size
indirect symbol table
LC_DYLD_INFO_ONLY
v24@?0r^{load_command=II}8^B16
c++ exception thrown in static initializer
chained fixups, pointer_format=%d in segment #%d does not match pointer size
weak-link
malformed mach-o contains LC_DYLD_INFO_ONLY and local relocations
bad or unknown fileoffset/size for LINKEDIT
weak-link,lazy-load
/System/Library/PrivateFrameworks/Dyld.framework/Dyld
malformed import table, unknown imports_format=%d
multiple LC_MAIN or LC_UNIXTHREAD load commands found
LC_ID_DYLINKER
/System/DriverKit/usr/lib/libSystem.dylib
__DATA segment permissions is not 'rw-'
arm64e.kernel
__playground
load command #%d LC_UUID size wrong
/usr/lib/system/libsystem_kernel.dylib
load command #%d LC_SEGMENT filesize (%lu) too large
section '%s' segment name '%s' does not match containing segment's name '%s'
%.*s segment index %d too large
external relocations
LC_SYMTAB
platformAndVersions_block_invoke
bridgeOS
album entry next-offset=0 but count is wrong
x86_64
launchable
tvOS-simulator
bridgeOS-kernelKit
MH_EXECUTE has MH_DYLIB_IN_CACHE bit set
LC_LOAD_DYLIB
%.*s missing preceding REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB
cpu type/subtype in slice (%s) does not match fat header (%s)
armv7em
x86_64 shared cache slide v2, 4-byte stride, target is vm offset
malformed uleb128 for child node offset at 0x%04lX
0 && \"unknown arch\"
%s segment permissions has invalid bits set (0x%08X)
album entry next-offset=0x%X past end of file
%.*s has unknown library special ordinal (%d)
zippered(macOS/Catalyst)
armv7m
chained fixups, in segment #%d overflow page_start[%d]=0x%04X is before previous at 0x%04X\n
authenticated arm64e, 8-byte stride, target segIndex/offset8
Header.cpp
LC_REEXPORT_DYLIB
iOS
overlapping slices
thumbv8.1m.main
section '%s' size too large 0x%lX
tvOS-kernelKit
duplicate %s slices
arm64e.old
chained fixups, unknown pointer_format (%d)
malformed uleb128 in resolvers payload for %.*s
v24@?0r^v8r^v16
watchOS-simulator
macOS-exclaveKit
malformed trie node, child node name extends beyond trie data
dyldFrameworkVtable_block_invoke
arm64e.x1
BIND_OPCODE_DO_BIND_ADD_ADDR_IMM_SCALED
linkeditFileOffset != 0 && \"LINKEDIT segment not found\"
free standing
REBASE_OPCODE_DO_REBASE_ULEB_TIMES_SKIPPING_ULEB
thread_key_t %lu, larger than uint32_t
LC_SUB_LIBRARY
LC_VERSION_MIN_TVOS
lazy-load
chained fixups, symbols_format unknown (%d)
FunctionVariants tableCount=%u is too large for size=%lu
LC_ENCRYPTION_INFO
tvOS
growTo
chained fixups, dyld_chained_starts_in_segment for segment #%d overruns imports table
LC_MAIN not allowed for driverkit
LC_DATA_IN_CODE
segment load command has an empty segment name
album overlapping slices %d and %d
REBASE_OPCODE_DO_REBASE_IMM_TIMES
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) is too large, load commands end at %p
/System/ExclaveKit/usr/lib/system/
CString.cpp
kr == 0
handle && \"Dyld.framework is required\"
BIND_OPCODE_DO_BIND_ADD_ADDR_ULEB
load commands do not fit in __TEXT segment filesize
LC_FILESET_ENTRY
iOS-kernelKit
DYLD_CHAINED_PTR_32
load command #%d unknown required load command 0x%08X
can't have LC_MAIN and LC_UNIXTHREAD load commands
__DATA_CONST segment missing SG_READ_ONLY flag
sepOS
%.*s pointer rebase is in executable segment '%.*s'
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) too small
weak-def
LC_ATOM_INFO
scrName:     %s\n
trie too deep > 255
re-export
malformed mach-o contains LC_DYLD_INFO_ONLY and external relocations
watchOS
v48@?0{Slice={CString=*Q}{span<const unsigned char, 18446744073709551615UL>=*Q}}8^B40
multiple LC_SEGMENT_SPLIT_INFO load commands found
%.*s pointer rebase is in non-writable segment '%.*s'
armv6m
load command #%d LC_LINKER_OPTION size too small
section '%s/%s' align field (1 << %d) does not match address (0x%llX)
chained fixups, imports array overlaps symbols
multiple LC_FUNCTION_STARTS load commands found
too many LC_RPATHs
dyld cache info
arm64e.kernel.v2
weak-link,delay-init
mh.sizeofcmds extends beyond buffer size
mergeable dylib info
LC_SUB_UMBRELLA
rebase opcodes terminated early at offset %zu of %zu
big endian mach-o file
!sMemoryManagerInitialized
%.*s segment offset 0x%08llX beyond segment '%.*s' size (0x%08llX)
file range of segment '%s' overlaps segment '%s'
macOSX
Platform
unsupported thread-local, larger than 4GB
chained fixups, unknown pointer_format in segment #%d
vmOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
generic 64-bit, 4-byte stride, target vmoffset
upward
objPath:     %s\n
multiple LC_DYLD_EXPORTS_TRIE load commands found
v24@?0r^v8^B16
Array.h
/usr/lib/dyld
%.*s text binds not supported for architecture
BIND_OPCODE_DO_BIND
authenticated arm64e, 8-byte stride, target vmadddr
MH_DYLIB is missing LC_ID_DYLIB
missing __TEXT segment
v16@?0^{TerminatorList=^{TerminatorList}Q[7{Terminator=^?^v}]}8
v28@?0r^v8B16^B20
x86_64h
DYLD_CHAINED_PTR_ARM64E
arm64e shared cache, 8-byte stride, target vmoffset
duplicate LC_RPATH '%s'
LC_???
malformed mach-o image: indirect symbol table iundefsym != iextdefsym+nextdefsym
v28@?0r^v8I16^B20
LC_RPATH
chained fixups, page_size not 4KB or 16KB in segment #%d
LC_BUILD_VERSION
'%s' segment vm range wraps
PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE
arm64_32
LC_FUNCTION_STARTS
Image.cpp
chained fixups, starts_offset exceeds LC_DYLD_CHAINED_FIXUPS size
load command #%d %.*s size too small
objSubType:  0X%02X\n
TPRO regions should not be writable on entry to dyld\n
dyld_introspection.cpp
album entry next-offset=0x%X not 16-byte aligned
chained fixups, dyld_chained_starts_in_segment[%d].segment_offset does match actual segment offset
LINKEDIT content '%s' extends beyond end of segment
rebase opcodes
load command #%d LC_ROUTINES_64 size too small
firmware
vmOffset too large for %s
{Error={CStringBuilderBufferOverflowSafe<128>={span<char, 18446744073709551615UL>=*Q}QiC[128]}C}24@?0{span<dyld::ThreadLocalVariables::Thunk, 18446744073709551615UL>=^{Thunk}Q}8
arm64e.x1.kernel
<main-executable>
macCatalyst
visionOS-exclaveCore
fat file has too many slices (%d)
trunc
unknown bind opcode 0x%02X
authenticated arm64e, 8-byte stride, target vmoffset
duplicate linked dylib are deprecated ('%s')
LC_DYLD_CHAINED_FIXUPS
malformed mach-o image: indirect symbol table ilocalsym != 0
segment '%s' filesize (0x%lX) exceeds vmsize (0x%lX)
visionOS-simulator
v32@?0{CString=*Q}8^B24
thread-local
%.*s has library ordinal too large (%d) max (%d)
%.*s unknown bind type %d
target vm address not in any segment
DYLD_CHAINED_PTR_X86_64_KERNEL_CACHE
malformed uleb128 in value payload for %.*s
LC_FUNCTION_VARIANT_FIXUPS
arm64
LC_ENCRYPTION_INFO_64
invalid x86_64 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
arm64e.x2.kernel
armv7
malformed mach-o image: indirect symbol table too large
v56@?0r*8r*16Q24C32C36S40I44^B48
chained fixups, max_valid_pointer (0x%x) too small for image last vm address 0x%llx
B56@?0{CString=*Q}8Q24Q32Q40^B48
multiple LC_MAIN load commands
err.noError()
%.*s text bind is in non-executable segment
chained fixups, imports_count (%d) exceeds max of %d
DYLD_CHAINED_PTR_ARM64E_USERLAND24
malformed load command (%d of %d) at offset=0x%lX with mh=%p, size (0x%X) is too large, load commands end at offset 0x%lX
LC_LINKER_OPTION found in non-object file
/usr/lib/system/libsystem_pthread_debug.dylib
armv6
trie cycle at node offset=0x%04llX
v24@?0{span<const mach_o::MappedSegment, 18446744073709551615UL>=^{MappedSegment}Q}8
_dyld_legacy_introspection_vtable
%.*s pointer bind is in non-writable segment '%.*s'
load command #%d LC_ENCRYPTION_INFO size wrong
bind ordinal (%u) too large in fixup at %.*s+0x%0lX
makeFromRawSlice
macOS
pthread_key_create() failed
chained fixups, pointer_format not same for all segments %d and %d
vmAddress (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
v48@?0{CString=*Q}8{span<const unsigned char, 18446744073709551615UL>=*Q}24^B40
malformed mach-o has no LINKEDIT
unknown platform
implOffset
OverflowSafeArray failed to allocate %llu bytes, vm_allocate returned: %d\n
chained fixups, unknown imports_format (%d)
upward,delay-init
load command #%d %.*s path offset too small
unknown
local relocations
load command #%d LC_ROUTINES not support in 64-bit mach-o
range.fileOffset >= _linkeditFileOffset
dynamic-resolver
armv7s
malformed trie, childNodeOffset==0
GradedArchitectures.cpp
LC_SUB_CLIENT
LC_UNIXTHREAD
load command #%d LC_ROUTINES size too small
16777228--2147483636
%.*s missing preceding BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM
chained fixups, imports_offset exceeds LC_DYLD_CHAINED_FIXUPS size
malformed uleb128 for terminal payload size at offset=0x%04lX
weak-link,upward,delay-init
weak bind opcodes
load command #%d %.*s name offset too small
iOS-simulator
file does not start with album magic
<weak-def-coalesce>
macOS-exclaveCore
visionOS-kernelKit
v56@?0{Slice={Architecture=ii}{span<const unsigned char, 18446744073709551615UL>=*Q}QC}8^B48
re-export name change not nul terminated
invalid FunctionVariantsRuntimeTable length %lu for count=%u
buffer does not start with MH_MAGIC[_64]
__LINKEDIT segment permissions is not 'r--'
iOS-exclaveCore
malformed load command (%d of %d) at %p with mh=%p, off end of load commands
multiple LC_FUNCTION_VARIANT_FIXUPS load commands found
chained fixups, in segment #%d page_start[%d]=0x%04X exceeds page size
DYLD_CHAINED_PTR_ARM64E_KERNEL
DYLD_CHAINED_PTR_ARM64E_USERLAND
load command #%d string extends beyond end of load command
section in segment '%s' has an empty section name
p->value != 0 && \"PlatformInfo value uninitialized, this might be a problem with C++ static initializers order\"
REBASE_OPCODE_DO_REBASE_ADD_ADDR_ULEB
album entry triple string missing nul terminator
loadableFrom
multiple LC_DYLD_INFO load commands found
malformed load command (%d of %d) at offset=0x%lX with mh=%p, off end of load commands
LC_MAIN
/usr/lib/system/libsystem_pthread.dylib
arm64.x2
chained fixups, page_start array overflows size
addend (%lld) cannot fit in fixup at %.*s+0x%0lX
missing LC_LOAD_DYLIB (must link with at least libSystem.dylib)
Mac Catalyst
chained fixups, different max_valid_pointer values seen in different segments
chained fixups, in segment #%d page_start[%d]=0x%04X multi-start chains not supported in 64-bit archs
firmware format does not support binds
generic 64-bit, 4-byte stride, target vmadddr
???
found LC_ID_DYLIB found in non-MH_DYLIB
malformed load command (%d of %d) at offset=0x%lX with mh=%p, cmdsize=0x%X is not pointer sized
/System/ExclaveKit/usr/lib/libSystem.dylib
file too small
authenticated arm64e, 4-byte stride, for kernel cache
malformed mach-o image: symbol table too large
v40@?0{PlatformAndVersions={Platform=^{PlatformInfo}I}{Version32=I}{Version32=I}{Version32=I}{Version32=I}}8
v16@?0{Architecture=ii}8
arm64e.x2
load command #%d LC_ROUTINES_64 not support in 32-bit mach-o
iOS-exclaveKit
MH_MAGIC
i386
DYLD_CHAINED_PTR_ARM64E_FIRMWARE
tableOffsets[%d]=0x%08X which is > total size 0x%08lX
code signature
LC_DYLD_INFO not allowed in .o files
LC_LOAD_UPWARD_DYLIB
LC_FUNCTION_VARIANTS
tvOS-exclaveCore
tvOS-exclaveKit
incompatible platforms: %s - %s
visionOS
xrOS-simulator
duplicate slice triple for %d and %d
armv8m.main
DYLD_CHAINED_PTR_64
malformed load command (%d of %d) at offset=0x%lX with mh=%p, size (0x%X) too small
load command #%d LC_SEGMENT size (%lu) does not match section count (%u)
v44@?0{Architecture=ii}8Q16Q24C32^B36
malformed mach-o contains LC_DYLD_CHAINED_FIXUPS and external relocations
LC_VERSION_MIN_IPHONEOS
objModTime:  0x%08X\n
macOS-kernelKit
/usr/lib/system/
symbol table
thumbv7
invalid bindOrdinal (%d) out of range (max=%d)
unknown FunctionVariantsRuntimeTable::Kind (%d)
LC_DYLD_EXPORTS_TRIE
invalid i386 flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
armv4t
thumbv6m
last entry in FunctionVariantsRuntimeTable entries is not 'default'
multiple LC_FUNCTION_VARIANTS load commands found
v8@?0
v40@?0^I8{CString=*Q}16B32B36
thumbv7k
chained fixups, in segment #%d overflow page_start[%d]=0x%04X exceeds page size
LC_LOAD_DYLINKER
%.*s unknown rebase type %d
BIND_SYMBOL_FLAGS_NON_WEAK_DEFINITION
LC_TARGET_TRIPLE
section '%s/%s' start address overlaps previous section
unknown rebase opcode 0x%02X
generic 32-bit, 4-byte stride
LC_SUB_FRAMEWORK
LC_DYLD_ENVIRONMENT
load command #%d LC_SYMTAB size wrong
range.fileOffset+range.size <= _linkeditFileOffset+_linkeditContent.size()
watchOS-kernelKit
kern.grade_cputype
arm64.x1
load command #%d %.*s not a dylib load command
scrDir:      %s\n
/usr/lib/system/libsystem_platform_debug.dylib
section '%s' end address 0x%lX is beyond containing segment's end address 0x%0lX
section '%s/%s' start offset overlaps previous section
libPath:     %s\n
v52@?0{CString=*Q}8i24B28C32Q36^B44
malformed uleb128 in flags for %.*s
<invalid-lib-ordinal>
%.*s missing preceding BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB
FunctionVariantFixups segOffset=0x%08X exceeds segment size (0x%llX)
LC_VERSION_MIN_WATCHOS
load command #%d string start offset too small
load command #%d LC_?? size is wrong
%.*s text rebase is in writable segment '%.*s'
%.*s text bind is in writable segment
missing LC_UUID load command
LC_SEGMENT_64
LC_LINKER_OPTION
load command #%d string offset (%u) outside cmd size (%lu)
load command #%d LC_DYLD_INFO size wrong
section '%s/%s' has offset=0 but is not a zero-fill section type
delay-init
chained fixups
multiple LC_ATOM_INFO load commands found
xrOS-exclaveKit
slice headers extend beyond end of file
__TEXT
load commands do not fit in __TEXT segment vmsize
malformed uleb128
riscv32
{Error={CStringBuilderBufferOverflowSafe<128>={span<char, 18446744073709551615UL>=*Q}QiC[128]}C}40@?0{CString=*Q}8{span<const unsigned char, 18446744073709551615UL>=*Q}24
mis-aligned LINKEDIT string pool, fileOffset=0x%08X
<this-image>
section '%s' has an empty segment name
v32@?0{span<const unsigned char, 18446744073709551615UL>=*Q}8^B24
mh.sizeofcmds too large
multiple LC_UNIXTHREAD load commands
symbol strings
%.*s pointer bind is in executable segment '%.*s'
1-byte stride, for x86_64 kernel cache
multiple LC_DYLD_CHAINED_FIXUPS load commands found
segment '%s' file offset out of order
missing LC_MAIN or LC_UNIXTHREAD in main executable
init
album entry beyond end of file
album entry triple string contains nul
FunctionVariants is too small
LC_MAIN not allowed in .o files
album file too short for slice count
DYLD_CHAINED_PTR_32_CACHE
DYLD_CHAINED_PTR_64_KERNEL_CACHE
multiple LC_SYMTAB load commands found
file does not start with FAT_MAGIC
arm64e.x1.old
load command #%d LC_DYSYMTAB size wrong
%.*s text rebase is in non-executable segment '%.*s'
thread locals not initialized
%.*s missing preceding BIND_OPCODE_SET_DYLIB_ORDINAL
malformed mach-o contains LC_DYLD_CHAINED_FIXUPS and local relocations
function variants
/usr/lib/system/libsystem_platform.dylib
driverKit
ifGrowableEnsureSpaceForAppending
arm64e.v1
multiple LC_DYSYMTAB load commands found
multiple LC_ID_DYLIB found
segment '%s' vm address out of order
LC_LINKER_OPTION has count=%d, only 1 or 2 is valid
segment '%s' content (fileOffset: 0x%lX -> 0x%lX) extends beyond end of file (length: 0x%llX)
chained fixups, seg_count exceeds number of segments
buffer too small
visionOS-exclaveKit
authenticated arm64e, 4-byte stride, target vmaddr
load commands length (%llu) exceeds length of file (%llu)
duplicate linked dylib '%s'
__DATA_CONST segment permissions is not 'rw-'
(_kind != Kind::reExport) && (_kind != Kind::absolute)
n <= _usedCount
arm64e.kernel.v1
too many LC_UUID load commands
lazy bind opcodes
armv8.1m.main
malformed mach-o contains LC_DYLD_INFO and LC_DYLD_CHAINED_FIXUPS
load command #%d LC_FILESET_ENTRY size too small
dyld cache thread-local format too old
malformed import table, imports_offset too large
entry %d extends to 0x%08X which beyond total size 0x%08lX
LC_ID_DYLIB
load command #%d LC_SEGMENT fileoff (%lu) too large
Symbol.cpp
0
ppc
__LINKEDIT
Platform.cpp
Allocator.cpp
BIND_OPCODE_DO_BIND_ULEB_TIMES_SKIPPING_ULEB
__chain_fixups
album entry triple string extends past end of file
multiple LC_ENCRYPTION_INFO_64 load commands found
multiple LC_ROUTINES[_64] load commands found
load command #%d %.*s not supported in .o files
v48@?0{CString=*Q}8Q24Q32^B40
mis-aligned LINKEDIT content '%s', fileOffset=0x%08X
xrOS-exclaveCore
slice is not page aligned
REBASE_OPCODE_DO_REBASE_ULEB_TIMES
thumbv7m
malformed import table, imports[%d].name_offset (%d) out of range
album slice extends past end of file
arm64e
thumbv8m.main
function variant fixups
LC_CODE_SIGNATURE
LINKEDIT overlap of %s and %s
load command #%d LC_SEGMENT[_64] size too small
authenticated arm64e, 4-byte stride, target vmoffset
multiple LC_ID_DYLIB load commands found
LC_SEGMENT_SPLIT_INFO
can't zip with invalid platform
load command #%d LC_ENCRYPTION_INFO_64 size wrong
/usr/lib/system/host/liblaunch_sim.dylib
allocStart != 0
malformed thread-local, offset=0x%lX is larger than total size=0x%lX
chained fixups, seg_count does not match number of segments
DYLD_CHAINED_PTR_32_FIRMWARE
PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE_V3
future
v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32
v92@?0{CString=*Q}8i24B28C32Q36B44i48{CString=*Q}52B68q72B80^B84
chained fixups, unknown header version (%d)
DYLD_CHAINED_PTR_ARM64E_SEGMENTED
multiple LC_TARGET_TRIPLE load commands found
section '%s/%s' has a non-zero reloff field
size (%llu) of thread-locals section %.*s is not a multiple of %lu
FunctionVariantFixups segIndex=%d exceeds number of segments (%lu)
too many linked dylibs
vm range of segment '%s' overlaps segment '%s'
function starts
load command #%d has too few strings (%d) expected (%d)
origlibPath: %s\n
%.*s text rebase not supported for architecture
malformed import table, symbols_offset too large
linkeditBytes
absolute
v20@?0{LinkEditRange=IIi}8
/System/DriverKit/usr/lib/system/
malformed trie, terminalSize extends beyond trie data at offset=0x%04lX
malformed uleb128 in function variants payload for %.*s
section '%s/%s' has a zero-fill section type, but offset field is not zero
fat file too short
album entry next-offset not forward
data in code
section '%s' start address 0x%lX is before containing segment's address 0x%0lX
/usr/lib/libSystem.B.dylib
exports trie
file does not start with MH_MAGIC[_64]: 0x%08X 0x%08X
old arm64e bind opcodes not supported
LC_VERSION_MIN_MACOSX
section '%s/%s' has a non-zero nreloc field
armv7k
thumbv7em
shared cache fixup formate does not support binds
malformed mach-o image: indirect symbol table iextdefsym != nlocalsym
invalid arm flavor,count (%d,%d), expected 6,68 in LC_UNIXTHREAD
unknown cpu type in LC_UNIXTHREAD
<flat-namespace>
unknown mach-o filetype (%u)
unknown exports flag bits in value payload for %.*s
LC_UUID
vt && \"Dyld.framework missing _dyld_legacy_introspection_vtable\"
album slice size overflow
segIndex (%d) and segOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX
__TEXT segment fileoffset is not zero
LC_DYSYMTAB
xrOS
```
