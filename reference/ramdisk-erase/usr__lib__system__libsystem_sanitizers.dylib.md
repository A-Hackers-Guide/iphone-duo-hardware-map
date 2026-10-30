# `/usr/lib/system/libsystem_sanitizers.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 165,584 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2200)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/system/libsystem_sanitizers.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libmacho.dylib (compatibility version 1.0.0, current version 1040.0.0)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`

## Entitlements

```xml
  - no entitlements
```

## Strings (176)

```
__DATA
getGlobalsSection
heap-use-after-free
stack variable
SanitizersAllocationTracesMinSize
addHeapBufferOverflowInfo
insertTrace
compiler_abi.cpp
poison
tagged
SanitizersAddress
malloc_logger != loggerFunc
allocation metadata unavailable
stack-use-after-return
stack
Located at offset %td of %s%s 
[%p, %p), size: %td\n
soft_trap_logger.h
log_bounds_safety_soft_trap
calling os_fault_with_payload to send telemetry\n
SanitizersAllocationTracesDurationInSeconds
__asan_abi_stack_malloc_n
runtime.cpp
endPtr % 8 == 0
BoundsSafety soft trap hit
size >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)
copy
Failed to map VM region of size %zu (%zu pages)\n
__TRIFactors
PreviousHook != RingBuffer::pthreadIntrospectionCallback
success
underflow
__asan_abi_stack_malloc_always_n
frame_header.magicConstant != kRetiredStackFrameMagic
stackVar.offset != 0
global-buffer-overflow
addUseAfterFreeInfo
WRITE
sanitizers_config.cpp
BoundsSafetySoftTrapsDisableLogging
mapCommon
fillStackVarInfo
[Sanitizers] FATAL: vm.debug_range_enabled sysctl could not be enabled\n[Sanitizers] HINT: Check that the device is in developer mode.\n
BoundsSafetySoftTrapsDisablePcFilter
mach_time.h
trace_depot.h
heap-buffer-overflow
READ
'%.*s' 
getAllocationEnd
allocationBegin <= access.address && access.address < allocationEnd
Failed to load `sanitizers_report_globals`
alloc.isValid()
frameDescription != __null
heap
Deallocation
0
length <= MaxTraceLength
retrieveTraces
allocation
vm.debug_range_enabled
shadow.cpp
No traces were collected, use env var `SanitizersAllocationTraces={all,tagged}` to enable
__asan_abi_stack_free_n
(size % sizeof(GlobalVar)) == 0
addGlobalBufferOverflowInfo
getAllocationInfo
add
SanitizersAllocationTraces
Address Sanitizer: %s at address %p\n
sectionCount < MaxSectionCount
vm_helpers.h
initPthreadIntrospection
pthreadIntrospectionCallback
segment
(uintptr_t)addr == report.access.address
operator()
pc_cache.h
yes
ring_buffer.cpp
allocation_map.h
introspection.h
*shadowVal > 0x8
BoundsSafetySoftTrapsVerbosity
getTextSegmentRange
Failed to load trace depot and/or allocation map
addressIsInMem(addr)
poisonAllocation
allocSize > userSize
not logging due to kernel reporting EQFULL previously\n
not logging due to previously seen pc:%p\n
stack-buffer-underflow
global
!config.isDefault()
SanitizersPrintReportToStderr
on
malloc_logger.h
dstSize > 0
__asan_globals
(size % vm_page_size) == 0
corrupted shadow
=================================================================\n
(base & (ASAN_SHADOW_ALIGNMENT - 1)) == 0
getShadowValue
production
setConfig
createReport
stack-use-after-scope
!cfg.enable
accessSize <= 16
unimplemented
Registers: pc=%p fp=%p sp=%p\n
  %2lu. %p in %s + %zu (%s)\n
BoundsSafetySoftTrapsMaxNumLogs
numVars != 0
Allocation
failed to log trap with error code: %d\n
SanitizersExitCode
sanitizer_config
trace.cpp
__TEXT
overflow
registerSection
copyNonTerminated
getStackVar
setLoggerConfig
soft_traps_runtime.cpp
insertion_index < N
SanitizersChildProcessPropagation
SanitizersAllocationTracesMemoryBudget
shadowVal != ShadowValue::Valid
freed 
Fault
SanitizersAllocationTracesMaxSize
BoundsSafetySoftTrapsTrapOnUnexpectedLogFailure
millisecondsToMachTicks
initRingBuffer
insert
n >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)
internal_helpers.h
leftrz_sz == 0
trap hit with pc %p\n
Failed to record pc (%p) in set of pcs to ignore\n
failed to log trap with EQFULL(%d). Logging now disabled\n
kr == 0
trace_extractor.h
global variable
\n
not logging due to it being disabled in config\n
config != SANITIZERS_CONFIG_NONE
_pthread_getspecific_direct(PThreadSlot) == nullptr
install
use-after-free
allocationEnd
pc != nullptr
not logging due to max log count of %u reached\n
1
ringBuffer != 0
BlockInfo::isValidBlockAddress(blockAddress)
get
stack-buffer-overflow
redzoneSize >= 16
_pthread_getspecific_direct(PThreadSlot) != nullptr
globals.cpp
report_generator.cpp
initRuntime
__asan_locate_address
debugger_abi.cpp
Faulty %s of size %zu at address %p\n
all
isInitialized()
%s trace on thread %llu at MAT %llu\n
BoundsSafety soft trap[#%u][#%u][#%u]:
freeRingBuffer
create
addDeallocTrace
```
