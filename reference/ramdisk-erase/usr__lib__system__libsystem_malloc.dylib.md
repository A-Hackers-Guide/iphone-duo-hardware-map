# `/usr/lib/system/libsystem_malloc.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 565,264 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 3128)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0, upward)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6, upward)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0, upward)`
- `/usr/lib/system/libcorecrypto.dylib (compatibility version 1.0.0, current version 2109.40.22, upward)`

## Entitlements

```xml
  - no entitlements
```

## Strings (969)

```
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)
MallocSanitizerZone: Not poisoning allocation %p of size %lu with redzone size %lu due to missing pointers!\n
MallocXzoneGuardLargeReinit
*** error %d\n
BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:995)
 (slot=%u), counter=%d\n*** previous incorrectly set slot=%u count=%d ptr=%p\n
wakeboardd
\"desc\": \"xzone malloc\", \n
Failed to map nanov2 region at %p\n
MallocXzoneThreadCaching
Huge cache requires deferred reclamation for large.\n
sec_transition_policy
\"guard_page_config\": {\n
\"segment_group_front_count\": %u, \n
        \"in_use\": 1, \n
%s value (%s) invalid - ignored.\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug
MallocCheckZeroOnFreeCorruption
stderr
%ld, counter=%d\n*** invariant broken for small free %p followed by %p in region [%p-%p] (end marker incorrect) should be %d; in fact %d\n
xzone malloc front random
small free list metadata inconsistency (headers[previous] != previous size)
\"mte_config\": {\n
        \"lock\": %u, \n
                \"allocations\": %lu,\n
pointer_xzones
%s value invalid - values must sum to %d, not %d - ignored.\n
MallocXzoneDeferTiny must be one of 0,1 - got %ld\n
BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2603)
Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n
vm.malloc_ranges
IINA
SpeedGame
Corruption of tiny freelist %p: size too small (%u/%u)\n
BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1137)
BUG IN LIBMALLOC: Slice count too large in init_segment
MessagesAirlockService
TelephonyBlastDoorService
        \"guards\": %u,\n
Nano maximum magazines limited to number of physical CPUs [%d]\n
SecureAllocator_process_aegirposter
        \"xca_head_seqno\": \"0x%llx\",\n
sysctlbyname(\"vm.malloc_ranges\") denied\n
Arena #%d: base address %p. Blocks - active: %d, madvisable: %d, madvising: %d, madvised: %d, unused: %d\n
mobilewifitool
 %c[%p, %p) size=%zd\n
arkitd
Failed to create carveout at 0x%lx in malloc guarded range 0x%lx: %d\n
        \"segment\": \"%p\", \n
PROBABILISTIC_GUARD_MALLOC_TARGETED_COVERAGE:enable=1
FATAL ERROR - ProbGuard: invalid pointer passed to realloc
MallocXzoneThreadCaching must be one of 0,1 - got %ld\n
tiny free list metadata inconsistency (bad next_msize)
*** error with %p: msize=%d, free: %x\n
%s}
    \"busy\": %llu, \n
FaceTime
\"reclaim_buffer\": { \n
            \"size\": %u, \n
        \"base\": \"%p\", \n
                    
FATAL ERROR - ProbGuard: memory budget too small
MallocXzoneListUpgradePeriod
%s(%d,%p) malloc: 
BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1033)
mach_vm_protect ret: %d\n
MallocXzonePerClusterSegmentGroups must be 0 or 1.\n
Tiny free sizes:\n
\"initial_slot_config\": %d, \n
*** FATAL ERROR - unable to allocate magazine array.\n
segment table slab
MallocXzoneGuardTinyDensity
Maximum magazines defaulted to %d\n
QuickLookUIService
com.apple.SafariPlatformSupport.Helper
SINGLE
incorrect size information for %p - block header was damaged\n
        \"runq_quarantine\": [\n
UNKNOWN
adding guard pages for large allocator blocks\n
high
Maximum magazines set to %d\n
        \"direction\": \"%s\"\n
xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)
mach_vm_range_create() denied\n
launchd.development
identityservicesd
                \"operations\": %lu,\n
MallocLargeExpandedCacheThreshold
small_free_list_remove_ptr_no_clear: Internal invariant broken (prev ptr of next) for %p, next_prev=%p\n
disabled known process
\"guard_object_config\": {\n
        \"sequestered\": %d,\n
\"guard_zones\": {\n
*** can't allocate pages: mach_vm_map(size=%lu) failed (error code=%d)\n
i68@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
use-after-free
tiny_free_list_remove_ptr: Internal invariant broken (prev ptr of next): ptr=%p, next_prev=%p\n
BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1079)
iOS bincompat list
small_chunk
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:971
*** can't mprotect(0x0) region for new postlude guard page at %p\n
com.apple.Safari.History
xbs chroot
Unsupported guarded metadata allocation at address 0x%lx of size 0x%lx with flags %d and label %d\n
        \"is_pristine\": %d,\n
%d 
valloc (%p/%llu): 
Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n
\"segment_groups\": {\n
*** Will sleep once for %d seconds to leave time to attach\n
** invalid pointer in free list: %p\n
i32@?0Q8Q16r*24
MallocDeferredReclaimBufferMaxCount
MallocXzoneGuardTinyRun
non-page-aligned, non-allocated pointer %p being freed\n
small free list metadata inconsistency (previous_msize > index)
                \"timestamp\": \"%llu\", \n
MallocXzoneDeferSmall must be one of 0,1 - got %ld\n
                \"slot_config\": \"%s\",\n
\"thread_cache_activation_contentions\": %lu, \n
unknown
\"is_main\": %d, \n
MallocXzoneGuardLargeChunkMax
*** set a breakpoint in malloc_error_break to debug\n
%s\n
PESmobile
BUG IN CLIENT OF LIBMALLOC: not an allocated block
normal_segment
Failed to create guard block at %p (%d)\n
MallocNanoMaxMagazines
MallocLargeCache
Large expanded cache threshold set to %lly\n
HubbleBlastDoorService
{\n
next_slot (1-based) = %d
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2216)
MallocZeroOnFree must be 0 or 1.\n
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2730)
poison_alloc(%p, 0x%lx, 0x%lx)\n
QuickLookUIExtension
  [%p, %p) size=%zd (bump)\n
ProbGuard zone: slots: %u, slots in use: %u, size in use: %llu, max size in use: %llu, allocated size: %llu\n
no sleep on heap corruption\n
,\n
        \"range_group\": \"%p\", \n
MallocDeferredReclaim must be one of 0,1 - got %ld\n
malloc_zone_free (%p): 
will sleep once for %d seconds on heap corruption\n
Failed to read szone structure\n
Advised MADV_FREE=%ly
com.apple.WebKit.WebContent.Development
mfm_arena info\n
\"batch_size\": %u, \n
MallocMaxMagazines
MallocXzonePerClusterSegmentGroups
MallocRecircRetainedRegions must be positive - ignored.\n
    \"tail\": %llu, \n
MallocDeferredReclaim
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7608)
malloc_entropy
%s\n(Use 'atos' for a symbolic stack)\n
            \"address\": \"%p\", \n
BUG IN CLIENT OF LIBMALLOC: MTE tag mismatch (probable double-free)
                \"head\": \"EMPTY\" \n
pointer_large
    Block %d: base %p; metadata: %p, size %d (class %d) in-use: %d 
MallocXzoneMemtagTagData
BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug
Failed to map small rack hashed_regions\n
        \"on_multi_segment\": %d\n
MallocZeroOnFree
c
        \"chunk_capacity\": %u, \n
BUG IN LIBMALLOC: Unexpected chunk kind
... but not protecting postlude guard page\n
BUG IN LIBMALLOC: bad chunk kind
\"bucketing_key\": \"%016llx%016llx\", \n
BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/lib
\ttiny=%u(%u) small=%u(%u) large=%u(%u)\n
com.apple.WebKit.Networking.Development
MobileSMS
        \"allocation_slots\": [\n
    \"large_guard_reinit\": %d,\n
\nRegion %d: base address %p\n
malloc_max_magazines must be positive - ignored.\n
BUG IN LIBMALLOC: pointer range initial overwrite failed
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1021)
    \"enabled\": %d, \n
BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1
Pointer %p to metadata being freed\n
        \"bucket\": %u,\n
guard_chunk
malloc_zone_malloc_with_options: unsupported options 0x%llx\n
%lu small regions:\n
                \"last_chunk_empty_ts\": %llu\n
Digital Performer
malloc_with_options (%p/%llu,%llu): 
\tNot empty enough to be moved to recirc depot
wifid
wifianalyticsd
\"slot_initial_threshold\": %u, \n
%s    \"addr\": \"%p\", \n
malloc_zone_register allocation failed\n
Scalable zone %p: inUse=%u(%u) touched=%u allocated=%u flags=0x%x\n
freelists\n
Corruption at %p: unexpected msizes %u/%u\n
MallocQuarantineZone
MallocXzoneDeferTiny
EnableBootArgs
mediaserverd
vmd
Failed to map guarded range: %d\n
*** FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4.\n
Failed to get scalable zone info\n
%s    \"reclaim_id\": %llu, \n
MallocProbGuardLeftAlignPercentage
MallocSpaceEfficient
BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7
malloc_zero_on_free_sample_period must be positive - ignored.\n
multi_free
BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl
Failed when changing state from MADVISING to MADVISED, block_metap = %p, blockp = %p\n
CAN MADVISE
Sibelius
DefaultScalableMallocZone
BUG IN LIBMALLOC: Failed to overwrite malloc metadata
    \"large_guards_enabled\": %d,\n
End xzone malloc JSON\n
MallocXzoneEarlyAlloc
Web App
    \"head\": %llu, \n
            \"segments\": { \n
i32@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
\"addr\": \"%p\", \n
FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n
_MallocMaxMagazines
ExternalQuickLookSatellite-x86_64
\"use_early_alloc\": %s, \n
                \"contentions\": \"%llu\", \n
            \"max_count\": %u, \n
MallocDoNotProtectPrelude
small_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
        \"xca_free_count\": \"0x%llx\",\n
MallocCheckHeapStart
will abort on heap corruption\n
can't unmap excess guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
ExternalQuickLookSatellite-arm64
CitiAuthenticator
i44@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
                \"head\": \"NOT_CACHED\", \n
Attempted to register zone more than once: %p\n
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2731)
%s    \"kind\": \"%s\", \n
        \"xca_on_empty_list\": \"0x%llx\",\n
FATAL ERROR - ProbGuard: bad configuration
Invalid size %zu for ptr %p\n
enabled
MallocCheckHeapEach
BUG IN LIBMALLOC: unknown segment group id
        \"list_config\": \"%s\",\n
ProbGuard configuration: %u kB budget, 1/%u sample rate, %u/%u/%u allocations/metadata/slots\n
ptr %p not in heap\n
com.apple.quicklook.extension.previewUI
wifip2pd
vm.reclaim.enabled
MallocErrorAbort
DefaultPurgeableMallocZone
MallocErrorSleep
    \"entries\": [ \n
], \n
        \"xca_walk_locked\": \"0x%llx\",\n
out-of-bounds
all
failed to load MallocStackLogging.framework\n
    \"large_chunk_slots\": %d,\n
        \"skip_size\": %zu, \n
MallocXzoneListConfig
ProbGuardAllProcesses
BUG IN LIBMALLOC: asking for size of chunk with invalid kind
Guarded Range Config (base/size/carveout): 0x%lx / 0x%lx / 0x%lx\n
Large expanded cache threshold defaulted to %lly\n
BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:10
BUG IN CLIENT OF LIBMALLOC: double free detected
            {\n
            \"density\": %u,\n
segment metadata slab
Failed to generate PGM report for fault address %p: slot is unexpectedly allocated with bounds %d\n
mediaplaybackd
\"segment_size\": %zu, \n
        \"guard_config\": {\n
guard_page
huge_chunk
*** FATAL ERROR - ProbGuard: zone integrity check failed.\n
MallocSmallFreelist
adding guard pages to all regions\n
 (slot=%u), counter=%d\n*** in-use ptr in free list slot=%u count=%d ptr=%p\n
    ] \n
        \"last_dealloc_ts\": \"%llu\", \n
MallocXzoneMadviseWorkaround
%s
MallocSanitizerZone: Not unpoisoning %p of size %lu due to missing pointers!\n
    \"reclaimable_bytes_min\": %llu, \n
            \"reuse\": %u\n
com.apple.WebKit.GPU.Development
WebSheet
none
MallocXzoneInitialChunkThreshold
BUG IN LIBMALLOC: ulock_wait failure
VTEncoderXPCService
BUG IN LIBMALLOC: failed to overwrite mfm arena
MallocProbGuardDebug
MallocXzoneMemtagEnable
maild
    \"large_guard_density\": %d,\n
MallocProbGuardDebugLogThrottleInMillis
BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7764)
MallocDebugReport
libmalloc
Tiny recirc depot is empty\n
                \"chunk_start\": \"%p\", \n
Can't deallocate_pages at %p\n
Failed to deallocate at address %p of size 0x%lx: %d\n
%ld, counter=%d\n*** invariant broken for %p (next %p is not a free pointer)\n
DeltaForceClient
MallocEarlyMallocSecTransitionSupport
MallocXzoneGuardedData
BUG IN LIBMALLOC: unexpected error from mach_vm_range_create()
multi_segment
MallocDeferredReclaimBufferCount
*** sleeping to help debug\n
                \"head_seqno\": \"0x%llx\", \n
Malloc Config Outputs:\n\tProcess Identity: %u\n\tEnable Xzone Malloc: %d\n\tEnable Nano On Xzone: %d\n\tXzone Enablement Reason: %s\n
Failed to map small rack\n
%s value invalid: [%s] - ignored.\n
BUG IN LIBMALLOC: Attempting to free to non-chunk slice
Stack for last operation where the malloc check succeeded: 
BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1118)
fmfd
%s    \"slice_entry_count\": %u \n
BUG IN LIBMALLOC: asking for start of chunk with invalid kind
backboardd
MallocSecureAllocator in environment
Unsupported protect debug flags %u\n
MallocXzoneHugeCacheSize
Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n
msl_turn_off_stack_logging
    \"tiny_run_size\": %d, \n
    } \n
, allocated slots: %d, free slots = %d, occupancy: %d%%\n
MallocXzoneSlotUpgradeThresholdCluster
Untouched=%ly 
%s must be 0 or 1.\n
Banco Galicia
true
MallocXzoneGuarded
BUG IN LIBMALLOC: Unexpected guard bitmap state!
Failed to map small oobe pointer\n
*** FATAL ERROR - ProbGuard: bad configuration.\n
MallocTagAll
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)
launchd_sim.debug
com.apple.SafariFoundation.CredentialProviderExtensionHelper
        \"skip_addr\": \"%p\", \n
Nano maximum magazines set to %d\n
>=
FATAL ERROR - unable to allocate magazine array
Safari
            \"behavior\": %u \n
BUG IN CLIENT OF LIBMALLOC: free to empty or invalid chunk detected (likely double-free)
Failed to map tiny rack\n
keychainsharingmessagingd
\"segment_group_count\": %u, \n
(unable to safely further examine remote process)\n
\"defer_small\": %s, \n
*** malloc_zone_unregister() failed for %p\n
BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:
Recirc depot \t
\"defer_tiny\": %s, \n
MallocZeroOnAlloc
Tiny region [%p-%p, %y] \t
\"multi_segment_size\": %zu, \n
Enabling ASLR slide on large allocations\n
        \"segment_group\": %zu, \n
unknown slab
MallocNanoMaxMagazines must be positive - ignored.\n
MallocXzoneDataOnly
BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug
MallocCheckHeapAbort
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1022)
can't allocate region\n:*** mach_vm_map(size=%lu, flags: %x) failed (error code=%d)\n
        \"addr\": \"%p\", \n
*** Recommend using 'setenv MallocCheckHeapStart %d; setenv MallocCheckHeapEach %d' to narrow down failure\n
MallocAggressiveMadvise
ThumbnailExtension
CommCenter
realloc(%p, 0x%lx) = %p\n
 size         : %zd\n
            \"count\": %u, \n
MallocLargeCache must be 0 or 1.\n
MallocAggressiveMadvise must be 0 or 1.\n
Corruption detected in block %p of size %u at offset %u, first 32 bytes at that offset are %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02
valloc(0x%lx) = %p\n
Pointer %p to metadata being freed (2)\n
BUG IN LIBMALLOC: invalid executable_boothash string
BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind
BUG IN LIBMALLOC: mach_timebase_info failed
MallocXzoneMaxListConfig
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2905)
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d count=%d ptr=%p\n
not LP64
    \"large_guard_reuse\": %d\n
malloc_zone_malloc_with_options: reserved TSD bit set\n
free(%p)\n
small_free_list_find_by_ptr: ptr is not free (ptr metadata !SMALL_IS_FREE), ptr=%p msize=%d metadata=0x%x\n
com.apple.WebKit.Networking
AegirPoster
        \"block_size\": %u,\n
MallocXzoneGuardLargeDensity
BUG IN LIBMALLOC: failed to allocate memory
    \"max_block_size\": %d \n
com.apple.WebKit.WebContent.EnhancedSecurity
mDNSResponder
tvOS feature flag
memalign (%p/%llu,%llu): 
_Malloc
pointer %p being freed was not allocated\n
com.apple.Safari.CredentialExtractionHelper
 address      : %p\n
        \"front\": %d, \n
__DATA
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5356)
realloc (%p->%p/%llu): 
xzm: failed to initialize deferred reclamation buffer [%d] %s (step %d)\n
%s\"%p\": {\n
        \"remaining\": %zu, \n
                \"xz_idx\": %d, \n
FATAL ERROR - ProbGuard: invalid pointer passed to free
free_definite_size(%p, 0x%lx)\n
small free list metadata inconsistency (bad next_msize)
 arena        : [%p, %p)\n
ProbGuard: %9s 0x%llx, fill state: %3u/%u\n
MallocXzoneSlotConfig
MallocXzoneHugeCacheMaxEntryBytes
%ld, counter=%d\n*** invariant broken for tiny block %p this msize=%d - size is too small\n
com.apple.WebKit.WebContent.CaptivePortal.Development
BUG IN CLIENT OF LIBMALLOC: invalid address
MallocProbGuardSampleRate
... but not protecting prelude guard page\n
MallocXzoneInitialSlotConfig
low
malloc (%p/%llu): 
Sanitizer
Failed to read large entries\n
WhatIf
    \"reclaimable_bytes\": %llu, \n
            }
MessagesBlastDoorService
com.apple.WebKit.WebContent
LetsGoClient
memalign(0x%lx, 0x%lx)\n
IMTransferAgent
  Class %d: 
msl_copy_msl_lite_hooks
ThumbnailExtension_macOS
avconferenced
ReportCrash
        \"quarantine\": %u,\n
MallocXzoneThreadCacheActivationContentions
%p 
Tiny recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
        \"id\": \"%s\", \n
        \"kind\": \"%s\", \n
MallocNanoZone
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug
\n
tiny_free_try_depot_unmap_no_lock hash lookup failed: %p\n
            \"max_entry_slices\": %u, \n
guard_object
Nanozonev2 %p: blocks in use: %llu, size in use: %llu allocated size: %llu, allocated regions: %d, region holes: %d\n
MallocSimpleStackLogging
d
    \"%p\": {\n
MallocXzoneBatchSize
*** OBSOLETE: malloc_debug()\n
Large allocator active blocks - total %y:\n
can't unmap excess trailing guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
    \"small_guard_density\": %d \n
__pgm_opt_out
MallocTagAllInternal
BUG IN CLIENT OF LIBMALLOC: memory corruption of free block
%ld, counter=%d\n*** invariant broken for tiny free %p followed by %p in region %p [%p-%p] (end marker incorrect) should be %d; in fact %d\n
Magazine=%d \t
logd
MediaAnalysisBlastDoorService
MallocXzoneHugeChunkOffsets
AudioConverterService
Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n
 size %-8zd:\n
s
%s    \"segment_group\": %lu, \n
    \"data_guards_enabled\": %d, \n
                \"free_count\": \"0x%llx\", \n
BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7548)
sanitizer_malloc_with_options: unsupported options 0x%llx\n
MallocSecureAllocator
MallocReportConfig
*** FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n.\n
MallocGuardEdges
MTE
%s    \"dirty_count\": %zu, \n
        \"free\": \"0x%x\",\n
MallocXzoneDeferLarge must be one of 0,1 - got %ld\n
/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging
    
            \"type\": \"%s\",\n
        \"xz_caches\": {\n
        \"slice_count\": %u, \n
MallocXzoneSlotUpgradeThreshold
XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tNarrow Bucketing: %d\n\tGuard Pages: %d (Tiny: %d, %d/%d; Small: %d, %d/%d)\n\tGuard Objects: (Large: %d [%d+%d/%d; max %d, quarantine %u, reinit %d, bigsplit %u])\n\tScribble: %d\n\t
*** malloc_get_all_zones: error reading zones at %p\n
%ld, counter=%d\n*** invariant broken for %p (next in free list %p is not a free pointer)\n
[%lu small regions have been vm_deallocate'd]\n
kern.bootargs
realloc(%p, 0x%lx): size(%p) = 0x%lx - redzone 0x%lx)\n
Failed to map tiny rack region_generation\n
JumpJump-mobile
    }
SecureAllocator_GuardObjects
BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:83
Non-aligned pointer %p being freed (2)\n
launchd
Unrecognized value for MallocDebugReport (%s) - using 'stderr'\n
*** error for object %p: pointer being freed was not allocated\n
Failed to map tiny rack hashed_regions\n
        \"xzone\": %d, \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug
%ld, counter=%d\n*** invariant broken for region end %p - %p\n
BUG IN LIBMALLOC: ulock_wake failure
%s    \"body_addr\": \"%p\", \n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:176)
\"bin_step\": %d, \n
                \"allocs\": \"%llu\" \n
xzm: unsupported value for MallocXzoneHugeCacheMaxEntryBytes (%ld)
BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:458)
MallocErrorStop
BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1134)
MallocSanitizerRedzoneSize
launchd_sim.development
    \"large_max_chunks\": %d,\n
Slots (#, state, offset, size, block address):\n
MallocProbGuardMetadata
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976
size(%p) = 0x%lx\n
Non-aligned pointer %p being freed\n
Screen Sharing
    \"buffer_len\": %u, \n
        \"block_size\": %llu, \n
\"thread_caches\": [ \n
*** malloc_get_all_zones: error reading zones_address at %p\n
small_free_list_remove_ptr_no_clear: Internal invariant broken (next ptr of prev) for %p, prev_next=%p\n
BUG IN LIBMALLOC: couldn't find executable_boothash
Corruption of free object %p: msizes %u/%u disagree\n
SafariViewService
  [%p, %p) size=%zd\n
*** FATAL ERROR - ProbGuard: invalid pointer passed to realloc.\n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:365)
at szone_check counter=%d\n
GroupSessionService
visionOS bincompat list
                \"chunk\": \"%p\",\n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:660)
%4u, %9s, %4u, %4u, %p\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug
NO ZONE for ptr %p\n
size(%p) = 0x%lx - redzone 0x%lx\n
            \"id\": %u, \n
down
        \"tagged\": %d,\n
            { \"count\": %u }
    \"small_run_size\": %d, \n
Quarantine: size: %llu, address range: [%p - %p)\n
SecureAllocator_GuardObjectsDeferredReclaim
AllowInternalSecurityPolicy
        \"used\": %u,\n
}\n
single_free
\tEmpty enough to be moved to recirc depot
Failed to read ProbGuard zone at %p\n
},\n
\n(Use 'atos' for a symbolic stack)\n
Corruption at %p: unexpected nonzero msize %u\n
BUG IN CLIENT OF LIBMALLOC: ignored previous invalid free due to MTE tag mismatch in soft mode (probable double-free)
poison_free(%p, 0x%lx)\n
MTLCompilerService
Size classes with allocated blocks: 
imagent
    \"last_sample_abs\": %llu, \n
                \"xsg_waiters\": \"0x%llx\",\n
MallocXzoneSmallThrashLimitSize
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:283)
searchpartyd
IMDPersistenceAgent
        \"next\": \"%p\", \n
pointer
metapool metadata slab
        ],\n
        \"metadata_addr\": \"%p\", \n
data
msl_handle_memory_event
WalletBlastDoorService
Begin xzone malloc JSON:\n
multi_body
__TRIFactors
MallocXzoneListUpgradeThreshold
DefaultMallocZone
MallocSpaceEfficient must be 0 or 1.\n
%s%y[%d]; 
        \"size\": %u \n
Double free of object %p\n
invalid
Failed to map nanozonev2_s at %p\n
MallocXzoneSlotUpgradeThresholdSingle
BUG IN LIBMALLOC: Can't upgrade from XZM_SLOT_CPU
        \"xca_alloc_idx\": \"0x%llx\",\n
MallocSanitizerZone
Malloc MTE debug mode (MallocTagAll=1) requires the process to be started with MTE enabled.\n
MallocAllowInternalSecurity
com.apple.SafariServices.ExtensionHelper
ASVAssetViewer
\"chunk_threshold\": %u, \n
MallocProbGuardMemoryBudgetInKB
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:324)
false
                \"contentions\": %lu,\n
ProbGuard
free (%p/%llu): 
Failed to map small rack magazines\n
MBS_PROD
enabling abort() on bad malloc or free\n
crash
MallocSanitizerZoneDebug
Failed to map small region at %p\n
Allocations in use=%d \t Bytes in use=%ly (%d%%) \t
\n\tSizes in use: 
BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1031)
    \"tag_data\": %d, \n
            \"length\": %u,\n
MallocEnableMSLAtLimitWarning
cameracaptured
        \"chunk_count\": %llu, \n
MallocXzoneListUpgradeThresholdSingle
msl_initialize
tiny_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:340)
Fragments subject to reclamation=%ly
ThumbnailExtensionSecure
managedassetsd
MallocXzoneGuardSmallRun
MobileSafari
large entry %p reallocated is not properly in table\n
BUG IN LIBMALLOC: unsupported allocation front count
BUG IN LIBMALLOC: Failed to allocate xzm zone
SecureAllocator_process_CollectionsPoster
NanoV2 Config:\n\tNano On Xzone: %d\n
enabling scribbling to detect mods to free blocks\n
\"ptr_bucket_count\": %d, \n
        \"xca_on_partial_list\": \"0x%llx\",\n
MallocXzoneThreadCacheActivationPeriod
MallocTracing
process feature flag
%ld, counter=%d\n*** invariant broken: null msize ptr=%p num_small_regions=%d end=%p\n
malloc_zero_on_free_enabled must be 0 or 1 - ignored.\n
%d: %p; 
%ld, counter=%d\n*** invariant broken for free block %p this msize=%d\n
i28@?0Q8Q16C24
        \"bucket\": %d, \n
        \"empty\": %u,\n
Intel
\", \n
        }\n
        \"mzone\": %d, \n
CLUSTER
MallocXzoneGuardSmallDensity
BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak
mzone index slab
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:975
BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type
presenced
%s    \"dispositions\": \"
MallocXzoneDataOnly must be 0 or 1.\n
msl_fork_prepare
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1010)
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:474)
calloc(0x%lx, 0x%lx) = %p\n
launchd_sim
                \"atomic_value\": \"0x%llx\",\n
Unable to map small linkage pointer %p\n
MallocXzoneMemtagMaxBlockSize
\tRecirc depot: 
i24@?0Q8^v16
purgeable zone does not support guard pages\n
 \n
freed
unpoison(%p, 0x%lx)\n
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:969)
        \"block_size\": %u, \n
MallocProbGuardAllocations
%ld, counter=%d\n*** invariant broken for leader block %p - %d %d\n
*** error with %p: msize=%d\n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:403)
Unsupported wrapped zone version: %u\n
\"range_groups\": {\n
Maximum magazines limited to ncpuclusters (%d)\n
PGM
BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:159)
        \"runq_full\": [\n
DISABLED
Malloc
MallocDoNotProtectPostlude
msl_stack_logging_locked
prl_client_app
        ]\n
large_chunk
MallocStackLogging
BUG IN LIBMALLOC: mach_vm_map() overwrite failed
    \"tiny_guard_density\": %d, \n
\"defer_large\": %s, \n
        \"user_slices\": %u,\n
MallocXzoneSmallThrashThreshold
        \"size\": %zu, \n
\"thread_cache_activation_time\": %llu, \n
*** error %d
msl_turn_on_stack_logging
Incorrect checksum for freed object %p: probably modified after being freed.\nCorrupt value: %p\n
%s    \"reclaim_id\": -1, \n
\"narrow_bucketing\": %d, \n
        \"batch_count\": %u, \n
                \"xsg_locked\": \"0x%llx\",\n
MallocXzoneThreadCacheActivationTime
MallocXzoneGuardLargeReuse
MallocEarlyMallocSecTransitionSupport must be 0 or 1.\n
 high water   : %zd\n
*** DefaultMallocError called
MallocSanitizerNoPoisoning
 (slot=%u), counter=%d\n*** unaligned ptr in free list slot=%u count=%d ptr=%p\n
 *
\"segment_group_ids_count\": %u, \n
huge_segment
MallocProbGuard
MallocXzoneDeferLarge
\"max_slot_config\": %d, \n
\"thread_cache_activation_period\": %lu, \n
MallocProbGuardSlots
_MallocNanoMaxMagazines
MallocXzoneEarlyAlloc must be 0 or 1.\n
[%lu tiny regions have been vm_deallocate'd]\n
polarisd
                \"head\": \"0x%llx\", \n
*** OBSOLETE: malloc_singlethreaded()\n
\"xzones\": {\n
MallocExperiment=
        { \n
\"range_group_count\": %u, \n
                \"seqno\": \"0x%llx\" \n
%y[%d] 
default
Small region [unknown address] was returned to the OS\n
        \"segment_group_id\": %d, \n
MallocXzoneDataThrashThreshold
            \"%d\": {\n
BUG IN LIBMALLOC: xzm_locked not implemented
MallocXzoneInitialSlotThreshold
+%u,
    \"sampling_period_abs\": %llu, \n
long-range OOB
disabled
*** MallocCheckHeap: FAILED check at operation #%d\n
        } \n
OOB + UAF
For region %p, first block: %d (%p), last block: %d (%p)\n
ClockFace
com.apple.Safari.SearchHelper
    \"max_len\": %u, \n
        \"meta\": \"0x%llx\",\n
ZeroOnFree
i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b
MallocXzoneSlotUpgradePeriod
*** malloc_get_all_zones: error reading num_zones at %p\n
will sleep for %d seconds on heap corruption\n
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d  count=%u ptr=%p\n
pointer %p being reallocated was not allocated\n
%ld, counter=%d\n*** invariant broken for %p (previous %p is not a free pointer)\n
    \"guard_pages_enabled\": %d, \n
,
\n}
Internal Security Policy: %d\n
    \"%d\": {\n
launchd.testing
    \"large_guard_force_quarantine\": %d,\n
                \"xsc_ptr\": \"0x%llx\",\n
MallocQuarantineMaxItems
arm64 tvOS
FATAL ERROR - ProbGuard: zone integrity check failed
nano zone abandoned due to inability to reserve vm space.\n
MallocXzoneGuardLarge
BUG IN LIBMALLOC: sysctlbyname(\"vm.malloc_ranges\") failed
}, \n
ENABLED
MallocZeroOnAlloc must be 0 or 1.\n
Small recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
Current Allocation Blocks By Size Class/Context [CPU]\n
        \"segment_cache\": { \n
multi-segment metadata slab
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not allocated
QuickLookSatellite
\"slice_size\": %zu, \n
tiny_chunk
MallocXzoneListUpgradeThresholdCluster
MallocHelp
Small region %p [%p-%p, %y] \t
audiomxd
%s    \"used\": %u, \n
        \"runq_partial\": [\n
BUMP (free list empty)
*** Will sleep for %d seconds to leave time to attach\n
calloc (%p/%llu*%llu): 
%ld, counter=%d\n*** invariant broken for blocker block %p - %d %d\n
        \"on_partial_list\": %d,\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug
Disabling ASLR slide on large allocations\n
realitycamerad
environment variables that can be set for debug:\n- MallocLogFile <f> to create/append messages to file <f> instead of stderr\n- MallocGuardEdges to add 2 guard pages for each large block\n- MallocDoNotProtectPrelude to disable protection (
CollectionsPoster
Messages
BUG IN LIBMALLOC: Invalid xzone slot config
MallocXzoneLargeHugeBigSplit
MallocLargeDisableASLR
msl_fork_parent
MallocXzoneSegmentDeallocate
Maximum magazines limited to number of logical CPUs (%d)\n
Large allocator death row cache not configured\n
mediaparserd
HardenedRuntime
\"allocation_front_count\": %u, \n
Unsupported MallocXzoneAllocationFronts\n
\"max_list_config\": %d, \n
Purgeable zone %p: inUse=%u(%y) flags=%d\n
notifyd
com.apple.Safari.SandboxBroker
            } \n
        \"slice_metadata\": \"%p\", \n
        \"alloc_idx\": %u,\n
MallocXzoneDeferSmall
        \"is_preallocated\": %d,\n
Maximum magazines must be positive - ignored.\n
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1009)
Region cookie corrupted for region %p (value is %x)[%p]\n
callservicesd
\"spans\": {\n
%lu tiny regions:\n
        \"thread\": \"%p\",\n
Heap corruption detected, free list is damaged at %p\n*** Incorrect guard value: %llu\n
MallocXzonePtrBucketCount
Tiny region [unknown address] was returned to the OS\n
        \"huge_alloc_counter\": \"%u\", \n
launchd.debug
data_large
BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone
FATAL ERROR - invalid bitarray level
BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6854)
double free for ptr %p\n
up
        \"in_use\": 0 \n
ProbGuardMallocZone
*** FATAL ERROR - ProbGuard: memory budget too small.\n
Failed to madvise block at blockp: %p, error: %d\n
msl_set_flags_from_environment
malloc_nano_max_magazines must be positive - ignored.\n
ptr %p in registered zone %p\n
Failed to map tiny region at %p\n
Failed to allocate segment from range group - out of space\n
        }
MallocHelperZone
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1035)
evicting %p from quarantine, size = 0x%lx\n
com.apple.SafariServices
small_freelist_chunk
MallocXzoneGuardLargeSlots
macOS bincompat list
i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=b63b1QSSI
Failed to map tiny rack magazines\n
Failed to map region %p\n
Failed to map small rack region_generation\n
MallocNanoOnXzone
%s    \"swapped_count\": %zu, \n
executable_boothash
last
IDSBlastDoorService
IMTranscoderAgent
zero-on-free bincompat
, 
checks heap after operation #%d and each %d operations\n
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7872)
BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:990)
malloc(0x%lx) = %p\n
, madvised
videocodecd
\"thread_cache_enabled\": %s, \n
        \"xca_seqno\": \"0x%llx\",\n
small free sizes:\n
com.apple.WebKit.GPU
com.apple.WebKit.WebContent.EnhancedSecurity.Development
        \"id\": %d, \n
MallocXzoneHasRanges
FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not valid
MallocQuarantineMaxSizeInMB
\"mzone\": %d, \n
MallocXzoneTinyThrashThreshold
MallocRecircRetainedRegions
*** sending SIGSTOP to help debug\n
SanitizerMallocZone
blocks\n
        \"early_budget\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:412)
Web
%s    \"slice_count\": %u, \n
com.apple.WebKit.WebContent.CaptivePortal
        \"slot_config\": \"%s\",\n
*** FATAL ERROR - ProbGuard: invalid pointer passed to free.\n
MallocSanitizerZone: Not poisoning deallocation %p of size %lu due to missing pointers!\n
CPU
        \"xca_alloc_head\": \"0x%llx\",\n
        \"slot_state\": \"0x%llx\",\n
allocated
VTDecoderXPCService
BUG IN LIBMALLOC: not MFM owned
Deferred reclamation cannot be used for xzones without large\n
Small recirc depot is empty\n
bridgeOS
unused
SecureAllocator_HugeChunkOffsets
MallocScribble
msl_fork_child
tiny_free_list_remove_ptr: Internal invariant broken (next ptr of prev): ptr=%p, prev_next=%p\n
    \"%u\": {\n
FULL
MallocXzoneGuardLargeQuarantine
MallocCheckHeapSleep
com.apple.quicklook.ThumbnailsAgent
\"deallocate_segment\": %s, \n
                \"chunk\": \"%p\", \n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:737)
Wrapped
   Slot %5d: %p, size %y
quicklookd
BUG IN LIBMALLOC: invalid executable_boothash length
Invalid xzone_ptr_buckets value %ld - ignored.\n
BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1140
BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed
MallocXzoneAllocationFronts
malloc_large_expanded_cache_threshold must be positive - ignored.\n
\tMagazine %d: 
*** can't mvm_protect(%u) region at %p with size %lu\n
thread cache slab
BUG IN LIBMALLOC: pthread_key_init_np failed
```
