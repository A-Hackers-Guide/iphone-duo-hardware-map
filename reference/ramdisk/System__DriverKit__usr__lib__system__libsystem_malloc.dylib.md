# `/System/DriverKit/usr/lib/system/libsystem_malloc.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 527,920 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 2816)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/DriverKit/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/System/DriverKit/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/System/DriverKit/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/System/DriverKit/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/System/DriverKit/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/System/DriverKit/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/System/DriverKit/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6, upward)`
- `/System/DriverKit/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0, upward)`
- `/System/DriverKit/usr/lib/system/libcorecrypto.dylib (compatibility version 1.0.0, current version 2109.40.22, upward)`

## Entitlements

```xml
  - no entitlements
```

## Strings (946)

```
sanitizer_malloc_with_options: unsupported options 0x%llx\n
Failed to map tiny rack region_generation\n
MallocSecureAllocator
*** OBSOLETE: malloc_debug()\n
searchpartyd
        \"in_use\": 0 \n
MallocXzoneListUpgradeThresholdSingle
IMTranscoderAgent
%s    \"addr\": \"%p\", \n
\"xzones\": {\n
        \"xz_caches\": {\n
                \"free_count\": \"0x%llx\", \n
high
%ld, counter=%d\n*** invariant broken for %p (previous %p is not a free pointer)\n
com.apple.WebKit.WebContent
huge_segment
will sleep for %d seconds on heap corruption\n
MallocErrorStop
com.apple.Safari.SandboxBroker
\"reclaim_buffer\": { \n
Invalid xzone_ptr_buckets value %ld - ignored.\n
malloc_zero_on_free_sample_period must be positive - ignored.\n
Maximum magazines limited to ncpuclusters (%d)\n
Maximum magazines limited to number of logical CPUs (%d)\n
*** error %d
\"bucketing_key\": \"%016llx%016llx\", \n
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
    \"%p\": {\n
        \"segment\": \"%p\", \n
        \"xca_free_count\": \"0x%llx\",\n
MallocQuarantineZone
AudioConverterService
Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n
Failed to map tiny rack hashed_regions\n
    \"large_guard_reuse\": %d\n
MallocXzoneThreadCaching must be one of 0,1 - got %ld\n
BUG IN LIBMALLOC: Invalid xzone slot config
Safari
        \"size\": %zu, \n
                    
        \"bucket\": %u,\n
MallocXzoneInitialSlotThreshold
%p 
environment variables that can be set for debug:\n- MallocLogFile <f> to create/append messages to file <f> instead of stderr\n- MallocGuardEdges to add 2 guard pages for each large block\n- MallocDoNotProtectPrelude to disable protection (
    \"large_chunk_slots\": %d,\n
Incorrect checksum for freed object %p: probably modified after being freed.\nCorrupt value: %p\n
        \"base\": \"%p\", \n
        \"empty\": %u,\n
MallocScribble
FATAL ERROR - ProbGuard: memory budget too small
MallocXzoneListUpgradeThreshold
%s    \"kind\": \"%s\", \n
MallocXzoneDeferSmall
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:2216)
ASVAssetViewer
CommCenter
        \"runq_full\": [\n
                \"contentions\": \"%llu\", \n
%s    \"dirty_count\": %zu, \n
        }
                \"atomic_value\": \"0x%llx\",\n
MallocXzoneSlotUpgradeThresholdSingle
MallocQuarantineMaxItems
free(%p)\n
ThumbnailExtension
\"desc\": \"xzone malloc\", \n
MallocCheckZeroOnFreeCorruption
unpoison(%p, 0x%lx)\n
%s must be 0 or 1.\n
huge_chunk
Failed to map tiny rack magazines\n
*** error with %p: msize=%d, free: %x\n
wifianalyticsd
\"segment_group_front_count\": %u, \n
MallocXzoneMemtagMaxBlockSize
\tNot empty enough to be moved to recirc depot
%s    \"segment_group\": %lu, \n
FATAL ERROR - ProbGuard: bad configuration
\tEmpty enough to be moved to recirc depot
avconferenced
            \"address\": \"%p\", \n
                \"head_seqno\": \"0x%llx\", \n
MallocXzoneEarlyAlloc must be 0 or 1.\n
... but not protecting prelude guard page\n
xzm: failed to initialize deferred reclamation buffer [%d] %s (step %d)\n
VTEncoderXPCService
iOS bincompat list
Attempted to register zone more than once: %p\n
MallocAggressiveMadvise must be 0 or 1.\n
MallocSanitizerZone: Not poisoning deallocation %p of size %lu due to missing pointers!\n
        \"last_dealloc_ts\": \"%llu\", \n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7608)
FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4
MallocLargeDisableASLR
MBS_PROD
                \"xsg_locked\": \"0x%llx\",\n
                \"chunk\": \"%p\", \n
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not allocated
%s\n(Use 'atos' for a symbolic stack)\n
DeltaForceClient
i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b
FATAL ERROR - ProbGuard: zone integrity check failed
DefaultScalableMallocZone
tiny free list metadata inconsistency (bad next_msize)
%y[%d] 
MallocErrorSleep
com.apple.WebKit.Networking
MediaAnalysisBlastDoorService
MallocXzoneListUpgradePeriod
Corruption at %p: unexpected nonzero msize %u\n
*** can't mprotect(0x0) region for new postlude guard page at %p\n
                \"xz_idx\": %d, \n
        \"xca_seqno\": \"0x%llx\",\n
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:283)
%s    \"body_addr\": \"%p\", \n
BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:458)
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:342)
Scalable zone %p: inUse=%u(%u) touched=%u allocated=%u flags=0x%x\n
c
        \"tagged\": %d,\n
MallocZeroOnFree
malloc (%p/%llu): 
size(%p) = 0x%lx\n
com.apple.WebKit.GPU.Development
com.apple.Safari.History
kern.bootargs
MallocSanitizerNoPoisoning
MallocXzoneSegmentDeallocate
%ld, counter=%d\n*** invariant broken for tiny free %p followed by %p in region %p [%p-%p] (end marker incorrect) should be %d; in fact %d\n
ExternalQuickLookSatellite-x86_64
MallocXzoneDataThrashThreshold
\n(Use 'atos' for a symbolic stack)\n
managedassetsd
backboardd
{\n
            \"max_entry_slices\": %u, \n
Current Allocation Blocks By Size Class/Context [CPU]\n
Wrapped
BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1079)
    \"small_run_size\": %d, \n
        \"chunk_capacity\": %u, \n
invalid
MallocProbGuardAllocations
MallocXzoneSmallThrashThreshold
MallocEnableMSLAtLimitWarning
visionOS bincompat list
\", \n
BUG IN LIBMALLOC: asking for size of chunk with invalid kind
Tiny region [unknown address] was returned to the OS\n
BUG IN LIBMALLOC: unsupported allocation front count
arm64 tvOS
\"guard_object_config\": {\n
true
        \"kind\": \"%s\", \n
MallocXzoneInitialChunkThreshold
MallocXzoneGuardLargeQuarantine
*** error %d\n
BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1118)
size(%p) = 0x%lx - redzone 0x%lx\n
Allocations in use=%d \t Bytes in use=%ly (%d%%) \t
\"mzone\": %d, \n
MallocProbGuardLeftAlignPercentage
Huge cache requires deferred reclamation for large.\n
ENABLED
ptr %p not in heap\n
com.apple.WebKit.WebContent.EnhancedSecurity
JumpJump-mobile
%s value invalid - values must sum to %d, not %d - ignored.\n
MallocXzoneSlotConfig
Failed to map small rack magazines\n
%s    \"reclaim_id\": -1, \n
        \"is_preallocated\": %d,\n
MallocDeferredReclaimBufferCount
MallocXzoneGuardLargeDensity
MallocEarlyMallocSecTransitionSupport must be 0 or 1.\n
Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n
Failed to deallocate at address %p of size 0x%lx: %d\n
i24@?0Q8^v16
Can't deallocate_pages at %p\n
*** malloc_get_all_zones: error reading zones_address at %p\n
enabling abort() on bad malloc or free\n
End xzone malloc JSON\n
BUG IN LIBMALLOC: unknown segment group id
com.apple.Safari.CredentialExtractionHelper
ReportCrash
 high water   : %zd\n
        \"skip_addr\": \"%p\", \n
BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:990)
notifyd
Failed when changing state from MADVISING to MADVISED, block_metap = %p, blockp = %p\n
CitiAuthenticator
                \"last_chunk_empty_ts\": %llu\n
MallocAggressiveMadvise
calloc (%p/%llu*%llu): 
BUG IN LIBMALLOC: mach_timebase_info failed
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:403)
logd
BUG IN LIBMALLOC: couldn't find executable_boothash
\"segment_size\": %zu, \n
*** OBSOLETE: malloc_singlethreaded()\n
MallocSimpleStackLogging
FaceTime
macOS bincompat list
all
d
BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK
MallocCheckHeapEach
com.apple.WebKit.WebContent.CaptivePortal
\"allocation_front_count\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7764)
Stack for last operation where the malloc check succeeded: 
free (%p/%llu): 
Quarantine: size: %llu, address range: [%p - %p)\n
BUG IN LIBMALLOC: invalid executable_boothash length
... but not protecting postlude guard page\n
\n\tSizes in use: 
PGM
FULL
executable_boothash
MallocTagAll
malloc_max_magazines must be positive - ignored.\n
mediaparserd
com.apple.WebKit.WebContent.EnhancedSecurity.Development
},\n
    \"max_block_size\": %d \n
        ],\n
Malloc MTE debug mode (MallocTagAll=1) requires the process to be started with MTE enabled.\n
\"mte_config\": {\n
BUG IN CLIENT OF LIBMALLOC: invalid address
\"spans\": {\n
*** Recommend using 'setenv MallocCheckHeapStart %d; setenv MallocCheckHeapEach %d' to narrow down failure\n
launchd_sim.debug
tvOS feature flag
    \"%u\": {\n
data
adding guard pages to all regions\n
For region %p, first block: %d (%p), last block: %d (%p)\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug
Failed to map guarded range: %d\n
MallocProbGuard
BUG IN LIBMALLOC: unexpected error from mach_vm_range_create()
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:324)
MallocNanoOnXzone
        \"user_slices\": %u,\n
CPU
*** sleeping to help debug\n
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
launchd.testing
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:
prl_client_app
    \"last_sample_abs\": %llu, \n
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d count=%d ptr=%p\n
can't unmap excess guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
            \"length\": %u,\n
_MallocNanoMaxMagazines
MallocXzoneSlotUpgradePeriod
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:737)
        \"xca_on_partial_list\": \"0x%llx\",\n
multi-segment metadata slab
Nanozonev2 %p: blocks in use: %llu, size in use: %llu allocated size: %llu, allocated regions: %d, region holes: %d\n
\"slot_initial_threshold\": %u, \n
%s    \"slice_count\": %u, \n
low
MallocDoNotProtectPrelude
MobileSMS
zero-on-free bincompat
    \"tail\": %llu, \n
PROBABILISTIC_GUARD_MALLOC_TARGETED_COVERAGE:enable=1
Slots (#, state, offset, size, block address):\n
_Malloc
MallocSanitizerZone: Not unpoisoning %p of size %lu due to missing pointers!\n
Failed to map small region at %p\n
Digital Performer
,
        \"segment_cache\": { \n
MallocXzoneHugeCacheMaxEntryBytes
malloc(0x%lx) = %p\n
        \"lock\": %u, \n
FATAL ERROR - ProbGuard: invalid pointer passed to realloc
unused
%ld, counter=%d\n*** invariant broken for leader block %p - %d %d\n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:660)
failed to load MallocStackLogging.framework\n
memalign(0x%lx, 0x%lx)\n
com.apple.quicklook.ThumbnailsAgent
Failed to generate PGM report for fault address %p: slot is unexpectedly allocated with bounds %d\n
Invalid size %zu for ptr %p\n
MallocSecureAllocator in environment
\"narrow_bucketing\": %d, \n
MallocZeroOnAlloc must be 0 or 1.\n
 (slot=%u), counter=%d\n*** previous incorrectly set slot=%u count=%d ptr=%p\n
PESmobile
    \"small_guard_density\": %d \n
    Block %d: base %p; metadata: %p, size %d (class %d) in-use: %d 
Corruption detected in block %p of size %u at offset %u, first 32 bytes at that offset are %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02
        \"next\": \"%p\", \n
            } \n
calloc(0x%lx, 0x%lx) = %p\n
non-page-aligned, non-allocated pointer %p being freed\n
    \"%d\": {\n
Tiny free sizes:\n
*** set a breakpoint in malloc_error_break to debug\n
pointer %p being freed was not allocated\n
MallocXzoneDeferTiny must be one of 0,1 - got %ld\n
Corruption at %p: unexpected msizes %u/%u\n
    \"large_max_chunks\": %d,\n
    \"tag_data\": %d, \n
                \"operations\": %lu,\n
large_chunk
MallocSmallFreelist
BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind
Non-aligned pointer %p being freed\n
Small recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
audiomxd
com.apple.WebKit.WebContent.CaptivePortal.Development
                \"head\": \"EMPTY\" \n
MallocReportConfig
purgeable zone does not support guard pages\n
        \"slice_metadata\": \"%p\", \n
MallocSpaceEfficient
tiny_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
vm.malloc_ranges
down
        \"slot_state\": \"0x%llx\",\n
NO ZONE for ptr %p\n
poison_alloc(%p, 0x%lx, 0x%lx)\n
identityservicesd
    }
BUG IN LIBMALLOC: Unexpected chunk kind
BUG IN LIBMALLOC: asking for start of chunk with invalid kind
%s    \"dispositions\": \"
Enabling ASLR slide on large allocations\n
%ld, counter=%d\n*** invariant broken for region end %p - %p\n
MallocXzoneTinyThrashThreshold
MallocXzoneDataOnly
Web App
ProbGuardMallocZone
Maximum magazines set to %d\n
    
%s    \"used\": %u, \n
use-after-free
MallocQuarantineMaxSizeInMB
 size         : %zd\n
unknown
\nRegion %d: base address %p\n
MallocEarlyMallocSecTransitionSupport
realitycamerad
        \"huge_alloc_counter\": \"%u\", \n
Failed to create guard block at %p (%d)\n
blocks\n
guard_chunk
NanoV2 Config:\n\tNano On Xzone: %d\n
    \"large_guard_force_quarantine\": %d,\n
checks heap after operation #%d and each %d operations\n
videocodecd
            \"max_count\": %u, \n
freed
ThumbnailExtension_macOS
%s\"%p\": {\n
                \"head\": \"0x%llx\", \n
out-of-bounds
com.apple.WebKit.Networking.Development
AegirPoster
\"range_group_count\": %u, \n
\"thread_caches\": [ \n
%4u, %9s, %4u, %4u, %p\n
MallocXzoneThreadCaching
MallocDebugReport
BUG IN LIBMALLOC: sysctlbyname(\"vm.malloc_ranges\") failed
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
FATAL ERROR - unable to allocate magazine array
        ]\n
MallocErrorAbort
FATAL ERROR - invalid bitarray level
Recirc depot \t
cameracaptured
maild
i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=b63b1QSSI
com.apple.SafariServices
pointer_large
malloc_zone_malloc_with_options: reserved TSD bit set\n
mDNSResponder
process feature flag
BUG IN LIBMALLOC: Unexpected guard bitmap state!
*** FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4.\n
BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak
Intel
MallocXzonePerClusterSegmentGroups must be 0 or 1.\n
BUG IN CLIENT OF LIBMALLOC: memory corruption of free block
MallocZeroOnAlloc
tiny_free_list_remove_ptr: Internal invariant broken (next ptr of prev): ptr=%p, prev_next=%p\n
            {\n
                \"slot_config\": \"%s\",\n
small_freelist_chunk
MallocXzoneGuardTinyDensity
SanitizerMallocZone
    } \n
MallocXzoneEarlyAlloc
Unable to map small linkage pointer %p\n
arkitd
        \"bucket\": %d, \n
MallocExperiment=
i44@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
MallocProbGuardSlots
%s value (%s) invalid - ignored.\n
CAN MADVISE
Large expanded cache threshold defaulted to %lly\n
small free list metadata inconsistency (bad next_msize)
com.apple.quicklook.extension.previewUI
allocated
        \"chunk_count\": %llu, \n
small_chunk
BUG IN LIBMALLOC: invalid executable_boothash string
BUG IN LIBMALLOC: ulock_wait failure
        \"used\": %u,\n
ProbGuard configuration: %u kB budget, 1/%u sample rate, %u/%u/%u allocations/metadata/slots\n
MallocXzoneGuardLargeChunkMax
MallocXzonePerClusterSegmentGroups
MallocProbGuardMemoryBudgetInKB
com.apple.SafariFoundation.CredentialProviderExtensionHelper
BUG IN LIBMALLOC: not MFM owned
 arena        : [%p, %p)\n
    \"tiny_run_size\": %d, \n
 \n
MallocXzoneGuardSmallDensity
Internal Security Policy: %d\n
freelists\n
tiny_free_list_remove_ptr: Internal invariant broken (prev ptr of next): ptr=%p, next_prev=%p\n
IMTransferAgent
can't unmap excess trailing guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
MallocCheckHeapStart
BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_s
%lu tiny regions:\n
        \"runq_partial\": [\n
MallocXzoneGuardedData
MallocXzoneBatchSize
IDSBlastDoorService
presenced
\"defer_small\": %s, \n
\"range_groups\": {\n
pointer
ProbGuard: %9s 0x%llx, fill state: %3u/%u\n
memalign (%p/%llu,%llu): 
, 
none
malloc_nano_max_magazines must be positive - ignored.\n
MallocXzoneLargeHugeBigSplit
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7872)
adding guard pages for large allocator blocks\n
%ld, counter=%d\n*** invariant broken for small free %p followed by %p in region [%p-%p] (end marker incorrect) should be %d; in fact %d\n
Banco Galicia
BUG IN LIBMALLOC: failed to overwrite mfm arena
%s    \"reclaim_id\": %llu, \n
                \"seqno\": \"0x%llx\" \n
, madvised
Large allocator death row cache not configured\n
        \"guards\": %u,\n
metapool metadata slab
*** malloc_get_all_zones: error reading zones at %p\n
will sleep once for %d seconds on heap corruption\n
HardenedRuntime
MallocRecircRetainedRegions must be positive - ignored.\n
Tiny region [%p-%p, %y] \t
BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_se
BUG IN LIBMALLOC: pointer range initial overwrite failed
IMDPersistenceAgent
mobilewifitool
                \"head\": \"NOT_CACHED\", \n
MallocNanoZone
Advised MADV_FREE=%ly
Web
Malloc
*** DefaultMallocError called
Purgeable zone %p: inUse=%u(%y) flags=%d\n
*** FATAL ERROR - unable to allocate magazine array.\n
Unsupported guarded metadata allocation at address 0x%lx of size 0x%lx with flags %d and label %d\n
        \"in_use\": 1, \n
wakeboardd
MallocXzoneInitialSlotConfig
%s\n
MallocXzoneSlotUpgradeThresholdCluster
BUG IN LIBMALLOC: pthread_key_init_np failed
    \"large_guard_density\": %d,\n
MallocXzoneGuardTinyRun
malloc_zone_register allocation failed\n
Maximum magazines defaulted to %d\n
MallocZeroOnFree must be 0 or 1.\n
i28@?0Q8Q16C24
\"initial_slot_config\": %d, \n
MallocSpaceEfficient must be 0 or 1.\n
\tRecirc depot: 
callservicesd
        \"segment_group\": %zu, \n
*** Will sleep once for %d seconds to leave time to attach\n
BUG IN LIBMALLOC: mach_vm_map() overwrite failed
launchd.debug
ThumbnailExtensionSecure
VTDecoderXPCService
                \"xsc_ptr\": \"0x%llx\",\n
MallocHelperZone
tiny_chunk
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:365)
\"max_list_config\": %d, \n
\"deallocate_segment\": %s, \n
            \"reuse\": %u\n
segment table slab
Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n
        \"block_size\": %u,\n
        \"free\": \"0x%x\",\n
Unsupported wrapped zone version: %u\n
valloc(0x%lx) = %p\n
  [%p, %p) size=%zd (bump)\n
    \"tiny_guard_density\": %d, \n
%ld, counter=%d\n*** invariant broken for tiny block %p this msize=%d - size is too small\n
%s
next_slot (1-based) = %d
%s%y[%d]; 
__DATA
MallocXzoneThreadCacheActivationTime
\"max_slot_config\": %d, \n
__TRIFactors
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug
*** FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n.\n
mach_vm_range_create() denied\n
launchd_sim.development
\"addr\": \"%p\", \n
            \"count\": %u, \n
MallocXzonePtrBucketCount
_MallocMaxMagazines
MallocRecircRetainedRegions
data_large
MallocXzoneDataOnly must be 0 or 1.\n
MallocCheckHeapAbort
BUG IN LIBMALLOC: xzm_locked not implemented
Small region %p [%p-%p, %y] \t
MessagesAirlockService
\"thread_cache_activation_time\": %llu, \n
Small region [unknown address] was returned to the OS\n
Unsupported protect debug flags %u\n
    \"large_guards_enabled\": %d,\n
        \"allocation_slots\": [\n
Unsupported MallocXzoneAllocationFronts\n
Failed to map region %p\n
mediaserverd
\"slice_size\": %zu, \n
MallocXzoneMemtagTagData
FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n
crash
no sleep on heap corruption\n
%lu small regions:\n
not LP64
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
WebSheet
        \"early_budget\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:273
            \"type\": \"%s\",\n
        \"slice_count\": %u, \n
BUG IN CLIENT OF LIBMALLOC: free to empty or invalid chunk detected (likely double-free)
MallocProbGuardMetadata
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:474)
}, \n
CLUSTER
BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1137)
Failed to get scalable zone info\n
LetsGoClient
        \"skip_size\": %zu, \n
vmd
ClockFace
disabled known process
\"thread_cache_activation_period\": %lu, \n
BUG IN LIBMALLOC: Failed to allocate xzm zone
guard_object
MallocXzoneGuardLargeReuse
\tMagazine %d: 
unknown slab
%d 
MallocXzoneGuardLarge
small_free_list_find_by_ptr: ptr is not free (ptr metadata !SMALL_IS_FREE), ptr=%p msize=%d metadata=0x%x\n
false
\"is_main\": %d, \n
        \"addr\": \"%p\", \n
Small recirc depot is empty\n
MTE
            \"id\": %u, \n
            \"density\": %u,\n
malloc_zero_on_free_enabled must be 0 or 1 - ignored.\n
Unrecognized value for MallocDebugReport (%s) - using 'stderr'\n
\"multi_segment_size\": %zu, \n
up
        \"xca_alloc_idx\": \"0x%llx\",\n
  Class %d: 
MallocDeferredReclaim
\"use_early_alloc\": %s, \n
nano zone abandoned due to inability to reserve vm space.\n
\n
double free for ptr %p\n
MTLCompilerService
com.apple.Safari.SearchHelper
com.apple.SafariServices.ExtensionHelper
WhatIf
        \"front\": %d, \n
        \"quarantine\": %u,\n
pointer_xzones
multi_free
MallocMaxMagazines
MallocLargeCache
MallocXzoneHugeCacheSize
%ld, counter=%d\n*** invariant broken for blocker block %p - %d %d\n
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d  count=%u ptr=%p\n
+%u,
MallocSanitizerRedzoneSize
fmfd
 address      : %p\n
, allocated slots: %d, free slots = %d, occupancy: %d%%\n
MallocXzoneGuardSmallRun
MallocProbGuardSampleRate
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
}\n
enabled
Large expanded cache threshold set to %lly\n
*** sending SIGSTOP to help debug\n
BUG IN LIBMALLOC: Failed to overwrite malloc metadata
BUG IN CLIENT OF LIBMALLOC: double free detected
mfm_arena info\n
OOB + UAF
MallocHelp
[%lu tiny regions have been vm_deallocate'd]\n
small free list metadata inconsistency (previous_msize > index)
Messages
    \"max_len\": %u, \n
*** FATAL ERROR - ProbGuard: bad configuration.\n
vm.reclaim.enabled
BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:6854)
BUG IN CLIENT OF LIBMALLOC: MTE tag mismatch (probable double-free)
BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segm
TelephonyBlastDoorService
            }
BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice
Double free of object %p\n
Pointer %p to metadata being freed (2)\n
\"bin_step\": %d, \n
    \"reclaimable_bytes_min\": %llu, \n
        \"id\": %d, \n
Malloc Config Outputs:\n\tProcess Identity: %u\n\tEnable Xzone Malloc: %d\n\tEnable Nano On Xzone: %d\n\tXzone Enablement Reason: %s\n
BUG IN CLIENT OF LIBMALLOC: ignored previous invalid free due to MTE tag mismatch in soft mode (probable double-free)
Failed to map small rack\n
Magazine=%d \t
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug
BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.
s
    \"data_guards_enabled\": %d, \n
MallocTracing
small free list metadata inconsistency (headers[previous] != previous size)
GroupSessionService
Failed to map nanov2 region at %p\n
launchd_sim
\"defer_tiny\": %s, \n
small_free_list_remove_ptr_no_clear: Internal invariant broken (next ptr of prev) for %p, prev_next=%p\n
\"guard_zones\": {\n
\"thread_cache_activation_contentions\": %lu, \n
        \"is_pristine\": %d,\n
*** error for object %p: pointer being freed was not allocated\n
large entry %p reallocated is not properly in table\n
wifip2pd
    \"guard_pages_enabled\": %d, \n
Deferred reclamation cannot be used for xzones without large\n
CollectionsPoster
Failed to map nanozonev2_s at %p\n
Arena #%d: base address %p. Blocks - active: %d, madvisable: %d, madvising: %d, madvised: %d, unused: %d\n
BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_m
malloc_large_expanded_cache_threshold must be positive - ignored.\n
** invalid pointer in free list: %p\n
\ttiny=%u(%u) small=%u(%u) large=%u(%u)\n
            { \"count\": %u }
Failed to map tiny rack\n
%s}
\"chunk_threshold\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:412)
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/lib
pointer %p being reallocated was not allocated\n
        \"runq_quarantine\": [\n
sec_transition_policy
MallocGuardEdges
Pointer %p to metadata being freed\n
  [%p, %p) size=%zd\n
i68@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
        \"size\": %u \n
Nano maximum magazines set to %d\n
Large allocator active blocks - total %y:\n
Failed to allocate segment from range group - out of space\n
Failed to map small rack hashed_regions\n
BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_introspect.c:1033)
BUG IN LIBMALLOC: ulock_wake failure
MallocCheckHeapSleep
MallocLargeExpandedCacheThreshold
BUG IN LIBMALLOC: bad chunk kind
            \"segments\": { \n
normal_segment
*** can't allocate pages: mach_vm_map(size=%lu) failed (error code=%d)\n
   Slot %5d: %p, size %y
single_free
*** FATAL ERROR - ProbGuard: memory budget too small.\n
%ld, counter=%d\n*** invariant broken: null msize ptr=%p num_small_regions=%d end=%p\n
        }\n
BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:
BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone
BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_
incorrect size information for %p - block header was damaged\n
BUG IN LIBMALLOC: failed to allocate memory
        \"sequestered\": %d,\n
mach_vm_protect ret: %d\n
BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:159)
        \"guard_config\": {\n
malloc_with_options (%p/%llu,%llu): 
at szone_check counter=%d\n
QuickLookSatellite
 size %-8zd:\n
        \"direction\": \"%s\"\n
\"segment_group_count\": %u, \n
Corruption of free object %p: msizes %u/%u disagree\n
BUG IN CLIENT OF LIBMALLOC: not an allocated block
 *
\"batch_size\": %u, \n
        \"list_config\": \"%s\",\n
mzone index slab
realloc (%p->%p/%llu): 
Failed to read ProbGuard zone at %p\n
        \"meta\": \"0x%llx\",\n
Failed to read szone structure\n
%ld, counter=%d\n*** invariant broken for %p (next %p is not a free pointer)\n
        \"segment_group_id\": %d, \n
        \"xca_on_empty_list\": \"0x%llx\",\n
        \"xca_head_seqno\": \"0x%llx\",\n
MallocProbGuardDebugLogThrottleInMillis
%d: %p; 
MallocXzoneMaxListConfig
xbs chroot
    \"large_guard_reinit\": %d,\n
                \"chunk\": \"%p\",\n
MallocXzoneListConfig
DefaultMallocZone
poison_free(%p, 0x%lx)\n
Failed to create carveout at 0x%lx in malloc guarded range 0x%lx: %d\n
        \"on_partial_list\": %d,\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug
BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1134)
small_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
QuickLookUIService
MallocNanoMaxMagazines must be positive - ignored.\n
        \"range_group\": \"%p\", \n
MallocLargeCache must be 0 or 1.\n
Untouched=%ly 
*** FATAL ERROR - ProbGuard: zone integrity check failed.\n
MallocXzoneAllocationFronts
MallocStackLogging
wifid
MallocXzoneMemtagEnable
MallocXzoneDeferLarge must be one of 0,1 - got %ld\n
        { \n
MallocTagAllInternal
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:969)
MallocAllowInternalSecurity
(unable to safely further examine remote process)\n
[%lu small regions have been vm_deallocate'd]\n
MessagesBlastDoorService
    \"entries\": [ \n
        \"xzone\": %d, \n
QuickLookUIExtension
free_definite_size(%p, 0x%lx)\n
Tiny recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
default
*** MallocCheckHeap: FAILED check at operation #%d\n
SpeedGame
\n}
thread cache slab
enabling scribbling to detect mods to free blocks\n
will abort on heap corruption\n
ExternalQuickLookSatellite-arm64
MallocXzoneListUpgradeThresholdCluster
Screen Sharing
%s    \"swapped_count\": %zu, \n
        \"slot_config\": \"%s\",\n
BUG IN LIBMALLOC: Can't upgrade from XZM_SLOT_CPU
Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n
stderr
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
            \"behavior\": %u \n
*** FATAL ERROR - ProbGuard: invalid pointer passed to free.\n
*** malloc_get_all_zones: error reading num_zones at %p\n
launchd.development
*** can't mvm_protect(%u) region at %p with size %lu\n
    \"head\": %llu, \n
MallocXzoneMadviseWorkaround
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
 (slot=%u), counter=%d\n*** unaligned ptr in free list slot=%u count=%d ptr=%p\n
    \"busy\": %llu, \n
UNKNOWN
MallocXzoneHasRanges
MallocXzoneGuarded
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug
Sanitizer
launchd
i32@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
    \"reclaimable_bytes\": %llu, \n
\"segment_group_ids_count\": %u, \n
                \"allocs\": \"%llu\" \n
 %c[%p, %p) size=%zd\n
    ] \n
MallocXzoneThreadCacheActivationPeriod
DISABLED
Tiny recirc depot is empty\n
Failed to map small oobe pointer\n
Begin xzone malloc JSON:\n
\"guard_page_config\": {\n
        \"on_multi_segment\": %d\n
MallocXzoneHugeChunkOffsets
BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7548)
Fragments subject to reclamation=%ly
SafariViewService
i32@?0Q8Q16r*24
        \"block_size\": %llu, \n
\"thread_cache_enabled\": %s, \n
        \"thread\": \"%p\",\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug
ptr %p in registered zone %p\n
mediaplaybackd
IINA
\"segment_groups\": {\n
                \"xsg_waiters\": \"0x%llx\",\n
segment metadata slab
xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)
malloc_entropy
malloc_zone_free (%p): 
        \"id\": \"%s\", \n
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
com.apple.WebKit.WebContent.Development
BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_introspect.c:1031)
        \"xca_walk_locked\": \"0x%llx\",\n
Size classes with allocated blocks: 
Nano maximum magazines limited to number of physical CPUs [%d]\n
Maximum magazines must be positive - ignored.\n
tiny_free_try_depot_unmap_no_lock hash lookup failed: %p\n
polarisd
            \"%d\": {\n
multi_segment
Non-aligned pointer %p being freed (2)\n
        \"batch_count\": %u, \n
com.apple.SafariPlatformSupport.Helper
            \"size\": %u, \n
guard_page
multi_body
MallocXzoneDeferLarge
MallocXzoneDeferSmall must be one of 0,1 - got %ld\n
Corruption of tiny freelist %p: size too small (%u/%u)\n
>=
MobileSafari
Heap corruption detected, free list is damaged at %p\n*** Incorrect guard value: %llu\n
MallocXzoneDeferTiny
sysctlbyname(\"vm.malloc_ranges\") denied\n
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segme
BUG IN LIBMALLOC: Slice count too large in init_segment
quicklookd
BUMP (free list empty)
MallocXzoneGuardLargeSlots
MallocXzoneSmallThrashLimitSize
        \"block_size\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:176)
    \"sampling_period_abs\": %llu, \n
                \"timestamp\": \"%llu\", \n
Failed to madvise block at blockp: %p, error: %d\n
BUG IN LIBMALLOC: Attempting to free to non-chunk slice
MallocDoNotProtectPostlude
last
\"defer_large\": %s, \n
Disabling ASLR slide on large allocations\n
        \"alloc_idx\": %u,\n
MallocDeferredReclaimBufferMaxCount
%s(%d,%p) malloc: 
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not valid
HubbleBlastDoorService
], \n
MallocXzoneSlotUpgradeThreshold
realloc(%p, 0x%lx): size(%p) = 0x%lx - redzone 0x%lx)\n
 (slot=%u), counter=%d\n*** in-use ptr in free list slot=%u count=%d ptr=%p\n
imagent
,\n
                \"contentions\": %lu,\n
                \"allocations\": %lu,\n
ProbGuard zone: slots: %u, slots in use: %u, size in use: %llu, max size in use: %llu, allocated size: %llu\n
*** error with %p: msize=%d\n
%ld, counter=%d\n*** invariant broken for free block %p this msize=%d\n
can't allocate region\n:*** mach_vm_map(size=%lu, flags: %x) failed (error code=%d)\n
MallocXzoneThreadCacheActivationContentions
xzm: unsupported value for MallocXzoneHugeCacheMaxEntryBytes (%ld)
malloc_zone_malloc_with_options: unsupported options 0x%llx\n
Failed to read large entries\n
long-range OOB
%ld, counter=%d\n*** invariant broken for %p (next in free list %p is not a free pointer)\n
small free sizes:\n
        } \n
        \"mzone\": %d, \n
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:340)
BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed
BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type
keychainsharingmessagingd
        \"metadata_addr\": \"%p\", \n
xzone malloc front random
DefaultPurgeableMallocZone
MallocXzoneGuardLargeReinit
MallocNanoMaxMagazines
%s    \"slice_entry_count\": %u \n
SINGLE
disabled
                \"chunk_start\": \"%p\", \n
BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jro
*** malloc_zone_unregister() failed for %p\n
Region cookie corrupted for region %p (value is %x)[%p]\n
com.apple.WebKit.GPU
    \"buffer_len\": %u, \n
MallocProbGuardDebug
%s value invalid: [%s] - ignored.\n
MallocSanitizerZoneDebug
\"ptr_bucket_count\": %d, \n
        \"remaining\": %zu, \n
        \"xca_alloc_head\": \"0x%llx\",\n
__pgm_opt_out
FATAL ERROR - ProbGuard: invalid pointer passed to free
Guarded Range Config (base/size/carveout): 0x%lx / 0x%lx / 0x%lx\n
MallocSanitizerZone: Not poisoning allocation %p of size %lu with redzone size %lu due to missing pointers!\n
realloc(%p, 0x%lx) = %p\n
MallocDeferredReclaim must be one of 0,1 - got %ld\n
XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tNarrow Bucketing: %d\n\tGuard Pages: %d (Tiny: %d, %d/%d; Small: %d, %d/%d)\n\tGuard Objects: (Large: %d [%d+%d/%d; max %d, quarantine %u, reinit %d, bigsplit %u])\n\tScribble: %d\n\t
MallocSanitizerZone
Failed to map small rack region_generation\n
bridgeOS
    \"enabled\": %d, \n
Failed to map tiny region at %p\n
small_free_list_remove_ptr_no_clear: Internal invariant broken (prev ptr of next) for %p, next_prev=%p\n
WalletBlastDoorService
*** FATAL ERROR - ProbGuard: invalid pointer passed to realloc.\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug
evicting %p from quarantine, size = 0x%lx\n
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:5356)
*** Will sleep for %d seconds to leave time to attach\n
valloc (%p/%llu): 
```
