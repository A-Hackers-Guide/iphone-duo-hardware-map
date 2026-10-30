# `/usr/lib/system/libsystem_sanitizers.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 165,584 bytes.

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
heap-buffer-overflow
Registers: pc=%p fp=%p sp=%p\n
config != SANITIZERS_CONFIG_NONE
SanitizersAllocationTracesMinSize
segment
global
operator()
add
trace.cpp
No traces were collected, use env var `SanitizersAllocationTraces={all,tagged}` to enable
compiler_abi.cpp
(uintptr_t)addr == report.access.address
stack-buffer-underflow
stack
Allocation
not logging due to it being disabled in config\n
not logging due to previously seen pc:%p\n
0
__asan_abi_stack_malloc_n
stack-buffer-overflow
alloc.isValid()
pc_cache.h
_pthread_getspecific_direct(PThreadSlot) != nullptr
isInitialized()
allocation_map.h
accessSize <= 16
getAllocationInfo
__TRIFactors
mach_time.h
kr == 0
'%.*s' 
%s trace on thread %llu at MAT %llu\n
insertion_index < N
setConfig
log_bounds_safety_soft_trap
trace_depot.h
(size % vm_page_size) == 0
shadowVal != ShadowValue::Valid
WRITE
READ
Deallocation
poisonAllocation
trap hit with pc %p\n
calling os_fault_with_payload to send telemetry\n
Failed to map VM region of size %zu (%zu pages)\n
report_generator.cpp
[%p, %p), size: %td\n
  %2lu. %p in %s + %zu (%s)\n
millisecondsToMachTicks
length <= MaxTraceLength
success
trace_extractor.h
(size % sizeof(GlobalVar)) == 0
Faulty %s of size %zu at address %p\n
all
BoundsSafetySoftTrapsVerbosity
yes
PreviousHook != RingBuffer::pthreadIntrospectionCallback
allocation metadata unavailable
__asan_abi_stack_malloc_always_n
freed 
vm.debug_range_enabled
shadow.cpp
not logging due to max log count of %u reached\n
tagged
BoundsSafetySoftTrapsMaxNumLogs
ring_buffer.cpp
corrupted shadow
runtime.cpp
1
malloc_logger.h
overflow
unimplemented
failed to log trap with error code: %d\n
SanitizersChildProcessPropagation
insert
__asan_abi_stack_free_n
__asan_globals
addGlobalBufferOverflowInfo
BoundsSafety soft trap hit
stack-use-after-scope
getAllocationEnd
BoundsSafety soft trap[#%u][#%u][#%u]:
=================================================================\n
soft_trap_logger.h
Failed to record pc (%p) in set of pcs to ignore\n
__asan_locate_address
createReport
*shadowVal > 0x8
BoundsSafetySoftTrapsDisablePcFilter
malloc_logger != loggerFunc
copy
leftrz_sz == 0
redzoneSize >= 16
SanitizersAllocationTraces
sanitizer_config
insertTrace
getTextSegmentRange
introspection.h
dstSize > 0
stack variable
not logging due to kernel reporting EQFULL previously\n
SanitizersAddress
BoundsSafetySoftTrapsTrapOnUnexpectedLogFailure
install
get
use-after-free
internal_helpers.h
fillStackVarInfo
numVars != 0
Address Sanitizer: %s at address %p\n
failed to log trap with EQFULL(%d). Logging now disabled\n
SanitizersAllocationTracesDurationInSeconds
__TEXT
debugger_abi.cpp
globals.cpp
getGlobalsSection
frameDescription != __null
stackVar.offset != 0
initRuntime
poison
Failed to load trace depot and/or allocation map
mapCommon
frame_header.magicConstant != kRetiredStackFrameMagic
\n
BoundsSafetySoftTrapsDisableLogging
ringBuffer != 0
vm_helpers.h
addressIsInMem(addr)
SanitizersExitCode
production
on
_pthread_getspecific_direct(PThreadSlot) == nullptr
create
copyNonTerminated
getStackVar
!cfg.enable
Located at offset %td of %s%s 
[Sanitizers] FATAL: vm.debug_range_enabled sysctl could not be enabled\n[Sanitizers] HINT: Check that the device is in developer mode.\n
allocationBegin <= access.address && access.address < allocationEnd
allocSize > userSize
freeRingBuffer
allocation
endPtr % 8 == 0
SanitizersAllocationTracesMaxSize
stack-use-after-return
addHeapBufferOverflowInfo
global variable
Fault
BlockInfo::isValidBlockAddress(blockAddress)
__DATA
addUseAfterFreeInfo
soft_traps_runtime.cpp
!config.isDefault()
initRingBuffer
Failed to load `sanitizers_report_globals`
underflow
n >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)
global-buffer-overflow
(base & (ASAN_SHADOW_ALIGNMENT - 1)) == 0
pc != nullptr
initPthreadIntrospection
pthreadIntrospectionCallback
retrieveTraces
sectionCount < MaxSectionCount
heap-use-after-free
getShadowValue
SanitizersPrintReportToStderr
SanitizersAllocationTracesMemoryBudget
size >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)
registerSection
heap
setLoggerConfig
sanitizers_config.cpp
addDeallocTrace
allocationEnd
```
