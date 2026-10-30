# `/usr/lib/system/libsystem_malloc.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 565,264 bytes.

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
Failed to map tiny rack hashed_regions\n
\"xzones\": {\n
Failed to madvise block at blockp: %p, error: %d\n
Sibelius
BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:
realloc(%p, 0x%lx) = %p\n
Small recirc depot is empty\n
                \"atomic_value\": \"0x%llx\",\n
poison_free(%p, 0x%lx)\n
small free list metadata inconsistency (headers[previous] != previous size)
*** can't mvm_protect(%u) region at %p with size %lu\n
small free list metadata inconsistency (bad next_msize)
%s    \"slice_entry_count\": %u \n
invalid
valloc (%p/%llu): 
*** malloc_get_all_zones: error reading num_zones at %p\n
Corruption at %p: unexpected nonzero msize %u\n
Fragments subject to reclamation=%ly
MallocXzoneInitialChunkThreshold
BUG IN LIBMALLOC: Unexpected guard bitmap state!
            \"max_count\": %u, \n
PROBABILISTIC_GUARD_MALLOC_TARGETED_COVERAGE:enable=1
malloc_zone_free (%p): 
BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed
\"segment_groups\": {\n
MallocProbGuardDebugLogThrottleInMillis
OOB + UAF
Failed to map small rack magazines\n
    \"large_chunk_slots\": %d,\n
                \"xsg_locked\": \"0x%llx\",\n
NO ZONE for ptr %p\n
com.apple.WebKit.WebContent
multi-segment metadata slab
free (%p/%llu): 
*** sending SIGSTOP to help debug\n
        \"slice_metadata\": \"%p\", \n
MallocXzoneEarlyAlloc must be 0 or 1.\n
DISABLED
blocks\n
MallocTracing
        \"slice_count\": %u, \n
long-range OOB
low
MallocXzoneThreadCaching must be one of 0,1 - got %ld\n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:737)
    } \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug
Small region [unknown address] was returned to the OS\n
wifid
    
\"defer_small\": %s, \n
Nano maximum magazines limited to number of physical CPUs [%d]\n
MallocXzoneGuardSmallDensity
evicting %p from quarantine, size = 0x%lx\n
>=
Failed to map guarded range: %d\n
\", \n
    \"%p\": {\n
Failed to read large entries\n
com.apple.quicklook.extension.previewUI
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:474)
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:324)
unknown
*** FATAL ERROR - ProbGuard: invalid pointer passed to realloc.\n
                \"xsg_waiters\": \"0x%llx\",\n
        \"xca_alloc_head\": \"0x%llx\",\n
Invalid xzone_ptr_buckets value %ld - ignored.\n
\n(Use 'atos' for a symbolic stack)\n
Malloc
        \"user_slices\": %u,\n
MallocXzoneLargeHugeBigSplit
*** error for object %p: pointer being freed was not allocated\n
segment metadata slab
launchd
kern.bootargs
*** malloc_get_all_zones: error reading zones at %p\n
ZeroOnFree
MallocEnableMSLAtLimitWarning
single_free
Nano maximum magazines set to %d\n
XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tNarrow Bucketing: %d\n\tGuard Pages: %d (Tiny: %d, %d/%d; Small: %d, %d/%d)\n\tGuard Objects: (Large: %d [%d+%d/%d; max %d, quarantine %u, reinit %d, bigsplit %u])\n\tScribble: %d\n\t
%s%y[%d]; 
notifyd
    \"small_guard_density\": %d \n
            \"id\": %u, \n
                \"timestamp\": \"%llu\", \n
BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1
*** can't mprotect(0x0) region for new postlude guard page at %p\n
wakeboardd
zero-on-free bincompat
\"defer_tiny\": %s, \n
        \"front\": %d, \n
ENABLED
DeltaForceClient
BUG IN LIBMALLOC: failed to overwrite mfm arena
BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug
*** FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n.\n
Scalable zone %p: inUse=%u(%u) touched=%u allocated=%u flags=0x%x\n
__pgm_opt_out
xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)
Disabling ASLR slide on large allocations\n
+%u,
BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1079)
 (slot=%u), counter=%d\n*** in-use ptr in free list slot=%u count=%d ptr=%p\n
, 
%s\n(Use 'atos' for a symbolic stack)\n
can't unmap excess guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
c
\"batch_size\": %u, \n
    \"max_len\": %u, \n
        \"huge_alloc_counter\": \"%u\", \n
MallocXzoneListUpgradePeriod
*** Will sleep once for %d seconds to leave time to attach\n
        \"id\": \"%s\", \n
MallocXzoneBatchSize
will sleep for %d seconds on heap corruption\n
_MallocMaxMagazines
ThumbnailExtensionSecure
        \"xca_head_seqno\": \"0x%llx\",\n
\"use_early_alloc\": %s, \n
data_large
_Malloc
DefaultScalableMallocZone
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:365)
Screen Sharing
MallocProbGuardMemoryBudgetInKB
MallocXzoneGuardTinyRun
        \"in_use\": 1, \n
        \"slot_state\": \"0x%llx\",\n
[%lu small regions have been vm_deallocate'd]\n
\"chunk_threshold\": %u, \n
Failed to map small rack hashed_regions\n
CitiAuthenticator
    \"tag_data\": %d, \n
*** DefaultMallocError called
        \"xca_walk_locked\": \"0x%llx\",\n
Corruption of tiny freelist %p: size too small (%u/%u)\n
com.apple.WebKit.WebContent.EnhancedSecurity.Development
Banco Galicia
Unsupported protect debug flags %u\n
        \"size\": %zu, \n
        \"batch_count\": %u, \n
BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind
sec_transition_policy
CollectionsPoster
    \"head\": %llu, \n
MallocAggressiveMadvise
MallocCheckZeroOnFreeCorruption
tiny_free_try_depot_unmap_no_lock hash lookup failed: %p\n
 \n
BUG IN LIBMALLOC: mach_timebase_info failed
*** Will sleep for %d seconds to leave time to attach\n
launchd_sim.development
    \"last_sample_abs\": %llu, \n
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not allocated
Failed to map small rack\n
Magazine=%d \t
ExternalQuickLookSatellite-arm64
managedassetsd
Web App
MallocXzoneSlotUpgradeThreshold
MallocErrorAbort
free_definite_size(%p, 0x%lx)\n
callservicesd
MallocXzonePerClusterSegmentGroups must be 0 or 1.\n
BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1118)
BUG IN LIBMALLOC: asking for start of chunk with invalid kind
MallocProbGuardSampleRate
Messages
\"segment_group_count\": %u, \n
sysctlbyname(\"vm.malloc_ranges\") denied\n
cameracaptured
com.apple.Safari.SearchHelper
GroupSessionService
        \"runq_full\": [\n
MallocXzoneDeferLarge
(unable to safely further examine remote process)\n
        \"skip_size\": %zu, \n
        } \n
Quarantine: size: %llu, address range: [%p - %p)\n
%s value (%s) invalid - ignored.\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug
com.apple.Safari.CredentialExtractionHelper
com.apple.Safari.SandboxBroker
SecureAllocator_process_aegirposter
libmalloc
Pointer %p to metadata being freed (2)\n
IMTransferAgent
default
    \"enabled\": %d, \n
End xzone malloc JSON\n
MallocXzoneListUpgradeThresholdCluster
SecureAllocator_GuardObjects
\"guard_object_config\": {\n
        }
                \"contentions\": %lu,\n
        \"block_size\": %u,\n
        \"metadata_addr\": \"%p\", \n
*** can't allocate pages: mach_vm_map(size=%lu) failed (error code=%d)\n
MallocDoNotProtectPrelude
Tiny free sizes:\n
MessagesAirlockService
        \"kind\": \"%s\", \n
MallocXzoneThreadCacheActivationTime
\tMagazine %d: 
\"range_group_count\": %u, \n
MallocXzoneInitialSlotThreshold
/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging
quicklookd
%s}
Maximum magazines defaulted to %d\n
AllowInternalSecurityPolicy
Safari
not LP64
disabled known process
small_freelist_chunk
Attempted to register zone more than once: %p\n
BUG IN LIBMALLOC: pointer range initial overwrite failed
%ld, counter=%d\n*** invariant broken for %p (next %p is not a free pointer)\n
    \"large_guard_force_quarantine\": %d,\n
                \"head\": \"EMPTY\" \n
com.apple.quicklook.ThumbnailsAgent
IMTranscoderAgent
            } \n
Invalid size %zu for ptr %p\n
ClockFace
ProbGuard zone: slots: %u, slots in use: %u, size in use: %llu, max size in use: %llu, allocated size: %llu\n
BUG IN LIBMALLOC: asking for size of chunk with invalid kind
malloc_max_magazines must be positive - ignored.\n
MallocCheckHeapAbort
poison_alloc(%p, 0x%lx, 0x%lx)\n
MallocXzoneDataOnly must be 0 or 1.\n
Small recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
        \"block_size\": %llu, \n
MallocXzonePtrBucketCount
  [%p, %p) size=%zd\n
BUG IN LIBMALLOC: Failed to allocate xzm zone
small_free_list_find_by_ptr: ptr is not free (ptr metadata !SMALL_IS_FREE), ptr=%p msize=%d metadata=0x%x\n
FATAL ERROR - unable to allocate magazine array
    \"tiny_run_size\": %d, \n
        \"remaining\": %zu, \n
segment table slab
MallocXzoneListUpgradeThresholdSingle
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d  count=%u ptr=%p\n
Corruption of free object %p: msizes %u/%u disagree\n
com.apple.SafariServices
BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:458)
MallocSpaceEfficient must be 0 or 1.\n
IINA
\"reclaim_buffer\": { \n
            \"length\": %u,\n
CLUSTER
calloc (%p/%llu*%llu): 
QuickLookUIExtension
Intel
up
            \"reuse\": %u\n
memalign (%p/%llu,%llu): 
MallocSanitizerNoPoisoning
ptr %p not in heap\n
Purgeable zone %p: inUse=%u(%y) flags=%d\n
Large allocator death row cache not configured\n
EnableBootArgs
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1010)
Tiny recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
Digital Performer
        \"runq_partial\": [\n
MBS_PROD
MallocDeferredReclaim must be one of 0,1 - got %ld\n
MallocXzoneSegmentDeallocate
Failed to map small oobe pointer\n
 %c[%p, %p) size=%zd\n
\"segment_size\": %zu, \n
com.apple.WebKit.Networking.Development
    \"tail\": %llu, \n
*** error with %p: msize=%d\n
Failed to get scalable zone info\n
%lu tiny regions:\n
MobileSafari
\"slice_size\": %zu, \n
MallocXzoneThreadCacheActivationPeriod
MallocXzoneDeferTiny must be one of 0,1 - got %ld\n
MallocXzoneGuardTinyDensity
MallocSimpleStackLogging
pointer %p being reallocated was not allocated\n
        \"guard_config\": {\n
        \"meta\": \"0x%llx\",\n
*** OBSOLETE: malloc_singlethreaded()\n
MallocCheckHeapSleep
%ld, counter=%d\n*** invariant broken for region end %p - %p\n
tvOS feature flag
ProbGuardAllProcesses
xbs chroot
\"initial_slot_config\": %d, \n
        \"segment_group_id\": %d, \n
MallocXzoneHugeCacheSize
Failed to allocate segment from range group - out of space\n
Failed to create carveout at 0x%lx in malloc guarded range 0x%lx: %d\n
MallocProbGuardSlots
malloc_zone_malloc_with_options: unsupported options 0x%llx\n
Internal Security Policy: %d\n
pointer %p being freed was not allocated\n
MTE
        \"bucket\": %d, \n
                \"allocations\": %lu,\n
MallocXzoneGuardLargeQuarantine
*** sleeping to help debug\n
Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n
    \"entries\": [ \n
            \"address\": \"%p\", \n
*** FATAL ERROR - ProbGuard: memory budget too small.\n
MallocXzoneDataThrashThreshold
MallocXzoneHugeCacheMaxEntryBytes
small_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
IDSBlastDoorService
Maximum magazines limited to ncpuclusters (%d)\n
%lu small regions:\n
\"max_slot_config\": %d, \n
large_chunk
unused
%d: %p; 
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7872)
NanoV2 Config:\n\tNano On Xzone: %d\n
size(%p) = 0x%lx - redzone 0x%lx\n
com.apple.WebKit.GPU
\"defer_large\": %s, \n
*** FATAL ERROR - ProbGuard: bad configuration.\n
launchd.testing
searchpartyd
mfm_arena info\n
multi_free
msl_handle_memory_event
BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:995)
ASVAssetViewer
\"bucketing_key\": \"%016llx%016llx\", \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug
realitycamerad
\"thread_cache_activation_period\": %lu, \n
BUG IN LIBMALLOC: unsupported allocation front count
memalign(0x%lx, 0x%lx)\n
HubbleBlastDoorService
SpeedGame
BUG IN CLIENT OF LIBMALLOC: double free detected
nano zone abandoned due to inability to reserve vm space.\n
MallocXzoneSlotConfig
presenced
WhatIf
mzone index slab
enabling abort() on bad malloc or free\n
s
\"thread_caches\": [ \n
pointer
            \"size\": %u, \n
%ld, counter=%d\n*** invariant broken: null msize ptr=%p num_small_regions=%d end=%p\n
\"guard_page_config\": {\n
MallocProbGuardDebug
BUG IN LIBMALLOC: mach_vm_map() overwrite failed
Non-aligned pointer %p being freed\n
Advised MADV_FREE=%ly
                \"chunk_start\": \"%p\", \n
MallocXzoneGuardLargeSlots
Large expanded cache threshold defaulted to %lly\n
freelists\n
,\n
        \"xca_on_partial_list\": \"0x%llx\",\n
        \"is_preallocated\": %d,\n
MallocProbGuardMetadata
Failed to map nanov2 region at %p\n
BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice
ReportCrash
WalletBlastDoorService
                \"seqno\": \"0x%llx\" \n
        \"on_multi_segment\": %d\n
purgeable zone does not support guard pages\n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:176)
i28@?0Q8Q16C24
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2905)
BUG IN LIBMALLOC: sysctlbyname(\"vm.malloc_ranges\") failed
non-page-aligned, non-allocated pointer %p being freed\n
launchd_sim.debug
MallocSecureAllocator
false
enabled
    \"busy\": %llu, \n
data
pointer_xzones
MallocXzoneGuardLargeReinit
MallocXzoneDataOnly
BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1137)
com.apple.WebKit.WebContent.Development
        \"xca_on_empty_list\": \"0x%llx\",\n
xzone malloc front random
avconferenced
%s    \"swapped_count\": %zu, \n
MallocXzoneThreadCacheActivationContentions
disabled
QuickLookUIService
MallocNanoZone
MallocXzoneDeferSmall
MallocXzoneGuarded
Failed to map tiny region at %p\n
tiny_free_list_remove_ptr: Internal invariant broken (next ptr of prev): ptr=%p, prev_next=%p\n
\n\tSizes in use: 
    ] \n
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d count=%d ptr=%p\n
Failed to read ProbGuard zone at %p\n
MallocDoNotProtectPostlude
Arena #%d: base address %p. Blocks - active: %d, madvisable: %d, madvising: %d, madvised: %d, unused: %d\n
sanitizer_malloc_with_options: unsupported options 0x%llx\n
%y[%d] 
Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n
        \"next\": \"%p\", \n
FATAL ERROR - ProbGuard: bad configuration
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug
malloc_large_expanded_cache_threshold must be positive - ignored.\n
vm.reclaim.enabled
MallocSpaceEfficient
Tiny region [%p-%p, %y] \t
BUG IN CLIENT OF LIBMALLOC: MTE tag mismatch (probable double-free)
launchd_sim
mediaserverd
MallocXzoneInitialSlotConfig
videocodecd
                \"operations\": %lu,\n
        \"free\": \"0x%x\",\n
Size classes with allocated blocks: 
BUG IN LIBMALLOC: Slice count too large in init_segment
BUG IN CLIENT OF LIBMALLOC: not an allocated block
                \"slot_config\": \"%s\",\n
Failed to generate PGM report for fault address %p: slot is unexpectedly allocated with bounds %d\n
BUG IN CLIENT OF LIBMALLOC: memory corruption of free block
MallocCheckHeapEach
Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n
%s    \"used\": %u, \n
MallocXzoneDeferTiny
i68@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
Unrecognized value for MallocDebugReport (%s) - using 'stderr'\n
[%lu tiny regions have been vm_deallocate'd]\n
can't unmap excess trailing guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
multi_segment
Incorrect checksum for freed object %p: probably modified after being freed.\nCorrupt value: %p\n
audiomxd
        \"allocation_slots\": [\n
                \"xz_idx\": %d, \n
                \"head_seqno\": \"0x%llx\", \n
        \"is_pristine\": %d,\n
%ld, counter=%d\n*** invariant broken for tiny block %p this msize=%d - size is too small\n
\"mzone\": %d, \n
MallocXzoneGuardLargeChunkMax
will sleep once for %d seconds on heap corruption\n
** invalid pointer in free list: %p\n
mediaparserd
\"allocation_front_count\": %u, \n
SecureAllocator_HugeChunkOffsets
Deferred reclamation cannot be used for xzones without large\n
\"range_groups\": {\n
mach_vm_protect ret: %d\n
%s    \"dirty_count\": %zu, \n
MallocXzoneMemtagTagData
mach_vm_range_create() denied\n
BUG IN LIBMALLOC: bad chunk kind
Non-aligned pointer %p being freed (2)\n
%ld, counter=%d\n*** invariant broken for small free %p followed by %p in region [%p-%p] (end marker incorrect) should be %d; in fact %d\n
arm64 tvOS
\"bin_step\": %d, \n
MallocXzoneMemtagMaxBlockSize
*** FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4.\n
can't allocate region\n:*** mach_vm_map(size=%lu, flags: %x) failed (error code=%d)\n
                \"chunk\": \"%p\",\n
BUG IN LIBMALLOC: couldn't find executable_boothash
BUG IN CLIENT OF LIBMALLOC: ignored previous invalid free due to MTE tag mismatch in soft mode (probable double-free)
logd
mDNSResponder
pointer_large
MallocXzoneGuardLargeReuse
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2216)
msl_fork_parent
BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:990)
        \"size\": %u \n
, allocated slots: %d, free slots = %d, occupancy: %d%%\n
adding guard pages to all regions\n
MallocSanitizerZone: Not poisoning deallocation %p of size %lu due to missing pointers!\n
FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4
Maximum magazines must be positive - ignored.\n
free(%p)\n
Failed to map small region at %p\n
JumpJump-mobile
            { \"count\": %u }
%s value invalid - values must sum to %d, not %d - ignored.\n
Corruption at %p: unexpected msizes %u/%u\n
%s must be 0 or 1.\n
true
            \"density\": %u,\n
MallocXzoneSlotUpgradeThresholdCluster
*** FATAL ERROR - ProbGuard: zone integrity check failed.\n
wifianalyticsd
backboardd
    \"large_guard_reuse\": %d\n
        \"early_budget\": %u, \n
        \"xca_alloc_idx\": \"0x%llx\",\n
%ld, counter=%d\n*** invariant broken for tiny free %p followed by %p in region %p [%p-%p] (end marker incorrect) should be %d; in fact %d\n
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2730)
launchd.development
com.apple.WebKit.GPU.Development
                \"chunk\": \"%p\", \n
multi_body
ProbGuardMallocZone
%s value invalid: [%s] - ignored.\n
Failed to map nanozonev2_s at %p\n
unpoison(%p, 0x%lx)\n
\"addr\": \"%p\", \n
        \"chunk_capacity\": %u, \n
FULL
next_slot (1-based) = %d
MallocXzoneMemtagEnable
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7608)
Double free of object %p\n
msl_copy_msl_lite_hooks
MallocXzoneSlotUpgradeThresholdSingle
Unsupported wrapped zone version: %u\n
MallocSecureAllocator in environment
], \n
MallocSanitizerZone: Not unpoisoning %p of size %lu due to missing pointers!\n
imagent
,
FATAL ERROR - ProbGuard: invalid pointer passed to realloc
MallocErrorSleep
\"thread_cache_activation_time\": %llu, \n
        \"on_partial_list\": %d,\n
MallocXzoneSlotUpgradePeriod
malloc_zone_register allocation failed\n
malloc_zero_on_free_sample_period must be positive - ignored.\n
*** error %d
                \"allocs\": \"%llu\" \n
Enabling ASLR slide on large allocations\n
*** error %d\n
process feature flag
\"segment_group_ids_count\": %u, \n
        \"chunk_count\": %llu, \n
        \"tagged\": %d,\n
huge_chunk
malloc (%p/%llu): 
%s
com.apple.SafariServices.ExtensionHelper
FaceTime
            }
BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7
Wrapped
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2731)
small free list metadata inconsistency (previous_msize > index)
    \"reclaimable_bytes_min\": %llu, \n
        { \n
BUG IN LIBMALLOC: Unexpected chunk kind
MallocExperiment=
realloc(%p, 0x%lx): size(%p) = 0x%lx - redzone 0x%lx)\n
BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1031)
%s    \"dispositions\": \"
    \"max_block_size\": %d \n
normal_segment
thread cache slab
BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6854)
FATAL ERROR - ProbGuard: invalid pointer passed to free
MallocDeferredReclaimBufferCount
xzm: unsupported value for MallocXzoneHugeCacheMaxEntryBytes (%ld)
BUG IN LIBMALLOC: Can't upgrade from XZM_SLOT_CPU
BUG IN LIBMALLOC: Attempting to free to non-chunk slice
BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone
%ld, counter=%d\n*** invariant broken for free block %p this msize=%d\n
%ld, counter=%d\n*** invariant broken for %p (next in free list %p is not a free pointer)\n
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)
\"multi_segment_size\": %zu, \n
                \"head\": \"NOT_CACHED\", \n
        \"segment_group\": %zu, \n
*** malloc_zone_unregister() failed for %p\n
checks heap after operation #%d and each %d operations\n
%ld, counter=%d\n*** invariant broken for leader block %p - %d %d\n
small free sizes:\n
Failed to deallocate at address %p of size 0x%lx: %d\n
i32@?0Q8Q16r*24
Slots (#, state, offset, size, block address):\n
malloc_entropy
enabling scribbling to detect mods to free blocks\n
i24@?0Q8^v16
        \"used\": %u,\n
BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7764)
MallocXzoneTinyThrashThreshold
MallocSmallFreelist
*** MallocCheckHeap: FAILED check at operation #%d\n
MallocEarlyMallocSecTransitionSupport must be 0 or 1.\n
MallocStackLogging
BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1033)
Malloc Config Outputs:\n\tProcess Identity: %u\n\tEnable Xzone Malloc: %d\n\tEnable Nano On Xzone: %d\n\tXzone Enablement Reason: %s\n
MallocAggressiveMadvise must be 0 or 1.\n
FATAL ERROR - ProbGuard: memory budget too small
high
malloc_nano_max_magazines must be positive - ignored.\n
small_free_list_remove_ptr_no_clear: Internal invariant broken (prev ptr of next) for %p, next_prev=%p\n
mediaplaybackd
        \"mzone\": %d, \n
*** FATAL ERROR - unable to allocate magazine array.\n
visionOS bincompat list
                    
MallocScribble
\"is_main\": %d, \n
%s    \"body_addr\": \"%p\", \n
            {\n
guard_object
BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl
MallocXzoneGuardLargeDensity
Maximum magazines limited to number of logical CPUs (%d)\n
BUG IN LIBMALLOC: unknown segment group id
MobileSMS
                \"head\": \"0x%llx\", \n
        \"bucket\": %u,\n
Can't deallocate_pages at %p\n
double free for ptr %p\n
huge_segment
CAN MADVISE
MallocXzoneThreadCaching
BUG IN LIBMALLOC: unexpected error from mach_vm_range_create()
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976
*** error with %p: msize=%d, free: %x\n
        ]\n
\n
AegirPoster
PESmobile
\"ptr_bucket_count\": %d, \n
        \"guards\": %u,\n
Stack for last operation where the malloc check succeeded: 
realloc (%p->%p/%llu): 
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1022)
%ld, counter=%d\n*** invariant broken for %p (previous %p is not a free pointer)\n
        \"lock\": %u, \n
MallocXzoneListConfig
%ld, counter=%d\n*** invariant broken for blocker block %p - %d %d\n
Corruption detected in block %p of size %u at offset %u, first 32 bytes at that offset are %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02
MallocErrorStop
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:340)
SafariViewService
com.apple.WebKit.WebContent.EnhancedSecurity
SecureAllocator_GuardObjectsDeferredReclaim
MallocQuarantineMaxItems
incorrect size information for %p - block header was damaged\n
Heap corruption detected, free list is damaged at %p\n*** Incorrect guard value: %llu\n
DefaultMallocZone
QuickLookSatellite
\"thread_cache_activation_contentions\": %lu, \n
MallocLargeCache
BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7548)
Maximum magazines set to %d\n
msl_fork_child
        ],\n
__TRIFactors
all
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1021)
use-after-free
FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n
large entry %p reallocated is not properly in table\n
Failed to map region %p\n
            \"segments\": { \n
MallocLargeExpandedCacheThreshold
xzm: failed to initialize deferred reclamation buffer [%d] %s (step %d)\n
vmd
            \"max_entry_slices\": %u, \n
  Class %d: 
FATAL ERROR - invalid bitarray level
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:971
Recirc depot \t
Region cookie corrupted for region %p (value is %x)[%p]\n
        \"last_dealloc_ts\": \"%llu\", \n
MallocNanoMaxMagazines
mobilewifitool
            \"behavior\": %u \n
\"thread_cache_enabled\": %s, \n
guard_page
    Block %d: base %p; metadata: %p, size %d (class %d) in-use: %d 
Tiny region [unknown address] was returned to the OS\n
%s    \"segment_group\": %lu, \n
BUG IN LIBMALLOC: pthread_key_init_np failed
%p 
Failed to read szone structure\n
MallocXzoneGuardedData
*** Recommend using 'setenv MallocCheckHeapStart %d; setenv MallocCheckHeapEach %d' to narrow down failure\n
no sleep on heap corruption\n
\"mte_config\": {\n
Allocations in use=%d \t Bytes in use=%ly (%d%%) \t
MallocXzoneGuardSmallRun
BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:83
SanitizerMallocZone
malloc_with_options (%p/%llu,%llu): 
IMDPersistenceAgent
    \"%d\": {\n
MallocEarlyMallocSecTransitionSupport
com.apple.WebKit.Networking
VTDecoderXPCService
%d 
        \"direction\": \"%s\"\n
MallocZeroOnFree
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:403)
MallocQuarantineMaxSizeInMB
small_chunk
msl_turn_on_stack_logging
com.apple.WebKit.WebContent.CaptivePortal.Development
iOS bincompat list
\"guard_zones\": {\n
\nRegion %d: base address %p\n
ThumbnailExtension_macOS
BUG IN LIBMALLOC: failed to allocate memory
MallocLargeCache must be 0 or 1.\n
MallocZeroOnAlloc must be 0 or 1.\n
ProbGuard
MallocProbGuardAllocations
 size         : %zd\n
    \"large_guard_reinit\": %d,\n
\n}
MallocDeferredReclaim
*** malloc_get_all_zones: error reading zones_address at %p\n
MallocHelperZone
MallocZeroOnAlloc
MallocDebugReport
},\n
MallocXzoneEarlyAlloc
MallocProbGuard
ProbGuard: %9s 0x%llx, fill state: %3u/%u\n
MallocProbGuardLeftAlignPercentage
BUG IN CLIENT OF LIBMALLOC: free to empty or invalid chunk detected (likely double-free)
        \"slot_config\": \"%s\",\n
    \"data_guards_enabled\": %d, \n
            \"count\": %u, \n
SINGLE
MallocXzoneSmallThrashThreshold
PGM
\ttiny=%u(%u) small=%u(%u) large=%u(%u)\n
        \"in_use\": 0 \n
MallocMaxMagazines
*** OBSOLETE: malloc_debug()\n
wifip2pd
AudioConverterService
i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b
%s\"%p\": {\n
BUG IN LIBMALLOC: xzm_locked not implemented
MallocQuarantineZone
    \"reclaimable_bytes\": %llu, \n
        \"base\": \"%p\", \n
MallocXzoneMaxListConfig
MallocSanitizerRedzoneSize
%s    \"slice_count\": %u, \n
Small region %p [%p-%p, %y] \t
VTEncoderXPCService
 *
        \"segment_cache\": { \n
    \"%u\": {\n
tiny_chunk
%s    \"kind\": \"%s\", \n
com.apple.SafariFoundation.CredentialProviderExtensionHelper
    \"large_max_chunks\": %d,\n
ptr %p in registered zone %p\n
        \"xca_seqno\": \"0x%llx\",\n
        \"empty\": %u,\n
__DATA
Failed when changing state from MADVISING to MADVISED, block_metap = %p, blockp = %p\n
_MallocNanoMaxMagazines
                \"contentions\": \"%llu\", \n
unknown slab
BUG IN LIBMALLOC: invalid executable_boothash string
MallocXzoneListUpgradeThreshold
BUG IN LIBMALLOC: Invalid xzone slot config
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not valid
... but not protecting postlude guard page\n
size(%p) = 0x%lx\n
BUG IN LIBMALLOC: not MFM owned
\"slot_initial_threshold\": %u, \n
allocated
Current Allocation Blocks By Size Class/Context [CPU]\n
 size %-8zd:\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug
LetsGoClient
metapool metadata slab
BUG IN LIBMALLOC: invalid executable_boothash length
Large expanded cache threshold set to %lly\n
BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:159)
Failed to map tiny rack region_generation\n
ThumbnailExtension
MallocXzoneMadviseWorkaround
MallocSanitizerZone: Not poisoning allocation %p of size %lu with redzone size %lu due to missing pointers!\n
 (slot=%u), counter=%d\n*** unaligned ptr in free list slot=%u count=%d ptr=%p\n
        \"range_group\": \"%p\", \n
        \"sequestered\": %d,\n
                \"free_count\": \"0x%llx\", \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug
tiny free list metadata inconsistency (bad next_msize)
com.apple.SafariPlatformSupport.Helper
\"narrow_bucketing\": %d, \n
MallocRecircRetainedRegions
MallocXzoneSmallThrashLimitSize
msl_turn_off_stack_logging
        \"skip_addr\": \"%p\", \n
 high water   : %zd\n
    }
out-of-bounds
BUG IN LIBMALLOC: ulock_wait failure
Sanitizer
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1009)
valloc(0x%lx) = %p\n
    \"tiny_guard_density\": %d, \n
        \"list_config\": \"%s\",\n
vm.malloc_ranges
i32@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
                \"xsc_ptr\": \"0x%llx\",\n
MallocXzoneDeferLarge must be one of 0,1 - got %ld\n
msl_initialize
\tRecirc depot: 
\tNot empty enough to be moved to recirc depot
macOS bincompat list
 arena        : [%p, %p)\n
*** FATAL ERROR - ProbGuard: invalid pointer passed to free.\n
DefaultPurgeableMallocZone
Tiny recirc depot is empty\n
MallocXzoneDeferSmall must be one of 0,1 - got %ld\n
Pointer %p to metadata being freed\n
BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak
    \"large_guard_density\": %d,\n
BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:10
   Slot %5d: %p, size %y
BUG IN CLIENT OF LIBMALLOC: invalid address
}, \n
malloc_zero_on_free_enabled must be 0 or 1 - ignored.\n
MallocCheckHeapStart
at szone_check counter=%d\n
Failed to map small rack region_generation\n
        \"block_size\": %u, \n
MallocTagAllInternal
tiny_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
MallocAllowInternalSecurity
malloc_zone_malloc_with_options: reserved TSD bit set\n
        \"id\": %d, \n
BUG IN LIBMALLOC: ulock_wake failure
Large allocator active blocks - total %y:\n
        \"xz_caches\": {\n
        \"segment\": \"%p\", \n
malloc(0x%lx) = %p\n
Failed to map tiny rack magazines\n
Unsupported guarded metadata allocation at address 0x%lx of size 0x%lx with flags %d and label %d\n
%s    \"addr\": \"%p\", \n
\"deallocate_segment\": %s, \n
%s(%d,%p) malloc: 
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:283)
maild
 address      : %p\n
none
BUMP (free list empty)
fmfd
Failed to map tiny rack\n
%s    \"reclaim_id\": -1, \n
    \"buffer_len\": %u, \n
%4u, %9s, %4u, %4u, %p\n
tiny_free_list_remove_ptr: Internal invariant broken (prev ptr of next): ptr=%p, next_prev=%p\n
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)
BUG IN LIBMALLOC: Failed to overwrite malloc metadata
launchd.debug
        }\n
            \"%d\": {\n
FATAL ERROR - ProbGuard: zone integrity check failed
MallocZeroOnFree must be 0 or 1.\n
CPU
... but not protecting prelude guard page\n
        \"addr\": \"%p\", \n
last
BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1140
keychainsharingmessagingd
        \"xca_free_count\": \"0x%llx\",\n
UNKNOWN
TelephonyBlastDoorService
i44@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
    \"guard_pages_enabled\": %d, \n
\"spans\": {\n
Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n
BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type
MallocSanitizerZoneDebug
polarisd
            \"type\": \"%s\",\n
MallocXzonePerClusterSegmentGroups
MallocHelp
msl_set_flags_from_environment
*** set a breakpoint in malloc_error_break to debug\n
arkitd
        \"alloc_idx\": %u,\n
Malloc MTE debug mode (MallocTagAll=1) requires the process to be started with MTE enabled.\n
\tEmpty enough to be moved to recirc depot
MallocNanoOnXzone
  [%p, %p) size=%zd (bump)\n
\"max_list_config\": %d, \n
\"segment_group_front_count\": %u, \n
will abort on heap corruption\n
For region %p, first block: %d (%p), last block: %d (%p)\n
\"desc\": \"xzone malloc\", \n
d
MallocNanoMaxMagazines must be positive - ignored.\n
HardenedRuntime
{\n
    \"large_guards_enabled\": %d,\n
MallocGuardEdges
failed to load MallocStackLogging.framework\n
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1035)
prl_client_app
        \"quarantine\": %u,\n
MallocDeferredReclaimBufferMaxCount
 (slot=%u), counter=%d\n*** previous incorrectly set slot=%u count=%d ptr=%p\n
ExternalQuickLookSatellite-x86_64
    \"small_run_size\": %d, \n
Huge cache requires deferred reclamation for large.\n
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5356)
%s    \"reclaim_id\": %llu, \n
identityservicesd
Begin xzone malloc JSON:\n
guard_chunk
MessagesBlastDoorService
Web
    \"sampling_period_abs\": %llu, \n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:660)
msl_fork_prepare
freed
MallocXzoneHugeChunkOffsets
environment variables that can be set for debug:\n- MallocLogFile <f> to create/append messages to file <f> instead of stderr\n- MallocGuardEdges to add 2 guard pages for each large block\n- MallocDoNotProtectPrelude to disable protection (
calloc(0x%lx, 0x%lx) = %p\n
        \"runq_quarantine\": [\n
}\n
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:975
Nanozonev2 %p: blocks in use: %llu, size in use: %llu allocated size: %llu, allocated regions: %d, region holes: %d\n
SecureAllocator_process_CollectionsPoster
crash
com.apple.Safari.History
executable_boothash
%s\n
ProbGuard configuration: %u kB budget, 1/%u sample rate, %u/%u/%u allocations/metadata/slots\n
bridgeOS
        \"thread\": \"%p\",\n
        \"xzone\": %d, \n
MallocXzoneHasRanges
Unable to map small linkage pointer %p\n
i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=b63b1QSSI
                \"last_chunk_empty_ts\": %llu\n
Failed to create guard block at %p (%d)\n
MallocXzoneGuardLarge
adding guard pages for large allocator blocks\n
MallocSanitizerZone
, madvised
com.apple.WebKit.WebContent.CaptivePortal
Guarded Range Config (base/size/carveout): 0x%lx / 0x%lx / 0x%lx\n
stderr
Untouched=%ly 
WebSheet
MallocTagAll
MallocXzoneAllocationFronts
Unsupported MallocXzoneAllocationFronts\n
MallocReportConfig
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:412)
BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1134)
BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/lib
msl_stack_logging_locked
CommCenter
down
MallocRecircRetainedRegions must be positive - ignored.\n
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:969)
small_free_list_remove_ptr_no_clear: Internal invariant broken (next ptr of prev) for %p, prev_next=%p\n
MediaAnalysisBlastDoorService
MallocLargeDisableASLR
MTLCompilerService
BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/A87F8B4A-D222-4612-A6BA-281CF3847D69/TemporaryDirectory.vA7rkl/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2603)
```
