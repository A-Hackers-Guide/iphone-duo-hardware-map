# `/System/DriverKit/usr/lib/system/libsystem_malloc.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 527,920 bytes.

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
Maximum magazines defaulted to %d\n
sysctlbyname(\"vm.malloc_ranges\") denied\n
thread cache slab
Nanozonev2 %p: blocks in use: %llu, size in use: %llu allocated size: %llu, allocated regions: %d, region holes: %d\n
*** DefaultMallocError called
launchd.testing
        \"xca_head_seqno\": \"0x%llx\",\n
MallocXzoneGuardSmallDensity
QuickLookUIService
backboardd
    }
MallocXzoneDeferTiny must be one of 0,1 - got %ld\n
BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_se
Incorrect checksum for freed object %p: probably modified after being freed.\nCorrupt value: %p\n
BUG IN LIBMALLOC: mach_vm_map() overwrite failed
    \"reclaimable_bytes_min\": %llu, \n
memalign (%p/%llu,%llu): 
Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n
*** error for object %p: pointer being freed was not allocated\n
SanitizerMallocZone
%s\n
\"allocation_front_count\": %u, \n
                \"head_seqno\": \"0x%llx\", \n
MallocNanoZone
presenced
Failed to map tiny rack\n
\n}
large_chunk
%s value invalid: [%s] - ignored.\n
MallocXzoneSmallThrashLimitSize
MallocXzoneLargeHugeBigSplit
        \"skip_addr\": \"%p\", \n
data_large
mzone index slab
*** FATAL ERROR - ProbGuard: memory budget too small.\n
MallocSpaceEfficient
%lu small regions:\n
QuickLookUIExtension
MallocProbGuardDebugLogThrottleInMillis
DefaultScalableMallocZone
ThumbnailExtension
ExternalQuickLookSatellite-x86_64
visionOS bincompat list
MallocProbGuardSampleRate
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
mobilewifitool
MallocXzoneThreadCacheActivationContentions
MallocHelp
    \"%p\": {\n
Web
MBS_PROD
            \"behavior\": %u \n
down
Tiny region [%p-%p, %y] \t
    \"tiny_run_size\": %d, \n
\"reclaim_buffer\": { \n
MallocXzoneMemtagTagData
MallocXzoneDataOnly
ENABLED
MallocScribble
PGM
CollectionsPoster
\"bucketing_key\": \"%016llx%016llx\", \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug
mach_vm_range_create() denied\n
\"narrow_bucketing\": %d, \n
                \"xsg_locked\": \"0x%llx\",\n
ProbGuardMallocZone
mach_vm_protect ret: %d\n
MallocXzoneEarlyAlloc
BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jro
MallocZeroOnAlloc must be 0 or 1.\n
BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed
MobileSMS
        \"is_pristine\": %d,\n
Failed to generate PGM report for fault address %p: slot is unexpectedly allocated with bounds %d\n
%p 
crash
i68@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
Heap corruption detected, free list is damaged at %p\n*** Incorrect guard value: %llu\n
MallocXzoneGuardTinyRun
%s    \"slice_entry_count\": %u \n
        \"id\": %d, \n
\"thread_cache_activation_time\": %llu, \n
BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:458)
            \"id\": %u, \n
        \"guards\": %u,\n
MallocNanoMaxMagazines
    } \n
        \"mzone\": %d, \n
        \"is_preallocated\": %d,\n
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not valid
*** FATAL ERROR - ProbGuard: invalid pointer passed to realloc.\n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:474)
BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone
BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/lib
launchd.development
\"batch_size\": %u, \n
            {\n
                \"allocations\": %lu,\n
BUG IN LIBMALLOC: Can't upgrade from XZM_SLOT_CPU
BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_m
MallocQuarantineMaxSizeInMB
VTDecoderXPCService
LetsGoClient
        \"xca_alloc_idx\": \"0x%llx\",\n
all
MallocEarlyMallocSecTransitionSupport
*** error with %p: msize=%d\n
FaceTime
}, \n
        \"xca_on_empty_list\": \"0x%llx\",\n
MallocXzoneHugeCacheSize
pointer %p being reallocated was not allocated\n
        \"size\": %zu, \n
CAN MADVISE
ThumbnailExtension_macOS
\"slice_size\": %zu, \n
\"use_early_alloc\": %s, \n
                \"contentions\": \"%llu\", \n
malloc_with_options (%p/%llu,%llu): 
{\n
        \"quarantine\": %u,\n
pointer_xzones
MallocProbGuardLeftAlignPercentage
ptr %p in registered zone %p\n
Purgeable zone %p: inUse=%u(%y) flags=%d\n
Failed to read large entries\n
GroupSessionService
com.apple.SafariServices
purgeable zone does not support guard pages\n
Advised MADV_FREE=%ly
%ld, counter=%d\n*** invariant broken for tiny block %p this msize=%d - size is too small\n
Tiny region [unknown address] was returned to the OS\n
 (slot=%u), counter=%d\n*** previous incorrectly set slot=%u count=%d ptr=%p\n
BUG IN CLIENT OF LIBMALLOC: double free detected
small_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
can't allocate region\n:*** mach_vm_map(size=%lu, flags: %x) failed (error code=%d)\n
\"max_slot_config\": %d, \n
multi_segment
MallocXzoneInitialSlotThreshold
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:340)
\"max_list_config\": %d, \n
            { \"count\": %u }
multi_body
\n(Use 'atos' for a symbolic stack)\n
%ld, counter=%d\n*** invariant broken for small free %p followed by %p in region [%p-%p] (end marker incorrect) should be %d; in fact %d\n
Small region %p [%p-%p, %y] \t
Region cookie corrupted for region %p (value is %x)[%p]\n
ExternalQuickLookSatellite-arm64
unknown slab
enabling scribbling to detect mods to free blocks\n
BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_s
memalign(0x%lx, 0x%lx)\n
BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_introspect.c:1031)
\", \n
MallocXzoneDeferTiny
\"ptr_bucket_count\": %d, \n
        \"front\": %d, \n
MallocXzoneGuardLarge
Failed to map small rack hashed_regions\n
double free for ptr %p\n
i28@?0Q8Q16C24
malloc_zone_free (%p): 
mediaserverd
cameracaptured
BUG IN LIBMALLOC: invalid executable_boothash string
Failed to create guard block at %p (%d)\n
MallocXzoneInitialChunkThreshold
%ld, counter=%d\n*** invariant broken for blocker block %p - %d %d\n
        { \n
            \"length\": %u,\n
malloc_zone_malloc_with_options: unsupported options 0x%llx\n
bridgeOS
%d 
MallocDebugReport
\"range_group_count\": %u, \n
        \"xca_seqno\": \"0x%llx\",\n
%s(%d,%p) malloc: 
    \"busy\": %llu, \n
        \"chunk_count\": %llu, \n
BUG IN LIBMALLOC: ulock_wait failure
com.apple.SafariFoundation.CredentialProviderExtensionHelper
mDNSResponder
            \"%d\": {\n
                \"head\": \"EMPTY\" \n
BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type
Failed to map small oobe pointer\n
s
MallocXzoneGuardTinyDensity
MallocSmallFreelist
MallocXzoneGuarded
MallocExperiment=
no sleep on heap corruption\n
*** FATAL ERROR - ProbGuard: bad configuration.\n
 size         : %zd\n
\"defer_large\": %s, \n
        \"thread\": \"%p\",\n
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d  count=%u ptr=%p\n
small free list metadata inconsistency (bad next_msize)
    Block %d: base %p; metadata: %p, size %d (class %d) in-use: %d 
malloc_nano_max_magazines must be positive - ignored.\n
MallocLargeCache must be 0 or 1.\n
arm64 tvOS
                \"chunk_start\": \"%p\", \n
        \"addr\": \"%p\", \n
        \"bucket\": %u,\n
ProbGuard zone: slots: %u, slots in use: %u, size in use: %llu, max size in use: %llu, allocated size: %llu\n
MallocXzoneHasRanges
Large allocator active blocks - total %y:\n
BUG IN LIBMALLOC: Failed to overwrite malloc metadata
vmd
            \"max_count\": %u, \n
        \"slot_config\": \"%s\",\n
\"thread_cache_activation_period\": %lu, \n
malloc_max_magazines must be positive - ignored.\n
calloc(0x%lx, 0x%lx) = %p\n
MallocXzoneSlotUpgradeThresholdCluster
BUG IN LIBMALLOC: ulock_wake failure
MallocRecircRetainedRegions must be positive - ignored.\n
BUG IN CLIENT OF LIBMALLOC: ignored previous invalid free due to MTE tag mismatch in soft mode (probable double-free)
callservicesd
 (slot=%u), counter=%d\n*** unaligned ptr in free list slot=%u count=%d ptr=%p\n
launchd_sim
realitycamerad
PESmobile
\"is_main\": %d, \n
MallocXzoneDataOnly must be 0 or 1.\n
            \"reuse\": %u\n
MallocQuarantineMaxItems
macOS bincompat list
false
        \"slice_metadata\": \"%p\", \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug
i44@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
\"thread_cache_activation_contentions\": %lu, \n
 size %-8zd:\n
\"spans\": {\n
adding guard pages to all regions\n
environment variables that can be set for debug:\n- MallocLogFile <f> to create/append messages to file <f> instead of stderr\n- MallocGuardEdges to add 2 guard pages for each large block\n- MallocDoNotProtectPrelude to disable protection (
BUG IN LIBMALLOC: unexpected error from mach_vm_range_create()
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:403)
poison_alloc(%p, 0x%lx, 0x%lx)\n
MallocSanitizerZone: Not poisoning allocation %p of size %lu with redzone size %lu due to missing pointers!\n
BUG IN LIBMALLOC: pthread_key_init_np failed
    ] \n
        \"empty\": %u,\n
huge_chunk
small free list metadata inconsistency (previous_msize > index)
        \"bucket\": %d, \n
}\n
BUG IN LIBMALLOC: sysctlbyname(\"vm.malloc_ranges\") failed
    \"head\": %llu, \n
                \"timestamp\": \"%llu\", \n
*** FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4.\n
},\n
\"segment_group_count\": %u, \n
Can't deallocate_pages at %p\n
pointer %p being freed was not allocated\n
com.apple.WebKit.Networking.Development
searchpartyd
  [%p, %p) size=%zd (bump)\n
            \"address\": \"%p\", \n
at szone_check counter=%d\n
Messages
Corruption at %p: unexpected nonzero msize %u\n
** invalid pointer in free list: %p\n
tiny_free_try_depot_unmap_no_lock hash lookup failed: %p\n
com.apple.WebKit.GPU.Development
    \"data_guards_enabled\": %d, \n
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:660)
BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:990)
Untouched=%ly 
xbs chroot
        \"id\": \"%s\", \n
BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:6854)
FATAL ERROR - ProbGuard: zone integrity check failed
sec_transition_policy
enabling abort() on bad malloc or free\n
calloc (%p/%llu*%llu): 
Corruption detected in block %p of size %u at offset %u, first 32 bytes at that offset are %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02X %02X %02X %02X | %02X %02X %02X %02X %02
Failed to allocate segment from range group - out of space\n
        \"in_use\": 0 \n
multi-segment metadata slab
__TRIFactors
realloc (%p->%p/%llu): 
        \"skip_size\": %zu, \n
            \"count\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.
,
high
NO ZONE for ptr %p\n
BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1118)
        \"early_budget\": %u, \n
data
Invalid size %zu for ptr %p\n
MallocXzoneSlotUpgradeThresholdSingle
xzm: unsupported value for MallocXzoneHugeCacheMaxEntryBytes (%ld)
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug
failed to load MallocStackLogging.framework\n
MobileSafari
            \"density\": %u,\n
                \"chunk\": \"%p\", \n
guard_chunk
... but not protecting prelude guard page\n
Non-aligned pointer %p being freed\n
MallocXzoneDeferSmall must be one of 0,1 - got %ld\n
*** MallocCheckHeap: FAILED check at operation #%d\n
tiny free list metadata inconsistency (bad next_msize)
Failed to map small rack region_generation\n
incorrect size information for %p - block header was damaged\n
wifip2pd
 address      : %p\n
    \"tag_data\": %d, \n
Double free of object %p\n
com.apple.Safari.SandboxBroker
pointer_large
MallocXzoneDataThrashThreshold
MallocSecureAllocator in environment
, 
xzone malloc front random
MallocSpaceEfficient must be 0 or 1.\n
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
AudioConverterService
JumpJump-mobile
,\n
    \"tiny_guard_density\": %d, \n
        \"segment_group_id\": %d, \n
End xzone malloc JSON\n
BUMP (free list empty)
FATAL ERROR - invalid bitarray level
\ttiny=%u(%u) small=%u(%u) large=%u(%u)\n
%s    \"reclaim_id\": %llu, \n
MallocXzoneThreadCaching must be one of 0,1 - got %ld\n
MallocXzoneListUpgradeThresholdCluster
MallocDeferredReclaimBufferMaxCount
MallocZeroOnFree
default
\"desc\": \"xzone malloc\", \n
MallocXzoneListConfig
small free sizes:\n
launchd_sim.development
*** FATAL ERROR - ProbGuard: invalid pointer passed to free.\n
MallocXzoneMadviseWorkaround
Maximum magazines must be positive - ignored.\n
ASVAssetViewer
BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_introspect.c:1033)
\"defer_tiny\": %s, \n
BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
invalid
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
[%lu tiny regions have been vm_deallocate'd]\n
\"bin_step\": %d, \n
disabled
Allocations in use=%d \t Bytes in use=%ly (%d%%) \t
not LP64
            \"type\": \"%s\",\n
Wrapped
Tiny free sizes:\n
BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7764)
*** malloc_zone_unregister() failed for %p\n
FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n
tiny_free_list_remove_ptr: Internal invariant broken (next ptr of prev): ptr=%p, prev_next=%p\n
stderr
Failed to map tiny rack region_generation\n
%s}
Malloc MTE debug mode (MallocTagAll=1) requires the process to be started with MTE enabled.\n
BUG IN LIBMALLOC: mach_timebase_info failed
%ld, counter=%d\n*** invariant broken for %p (previous %p is not a free pointer)\n
managedassetsd
    
    \"max_len\": %u, \n
        \"used\": %u,\n
MallocXzoneThreadCacheActivationPeriod
Internal Security Policy: %d\n
adding guard pages for large allocator blocks\n
unpoison(%p, 0x%lx)\n
up
__DATA
Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n
MallocStackLogging
\"slot_initial_threshold\": %u, \n
    \"large_max_chunks\": %d,\n
    \"buffer_len\": %u, \n
SINGLE
BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segm
com.apple.WebKit.GPU
\"initial_slot_config\": %d, \n
FULL
poison_free(%p, 0x%lx)\n
launchd.debug
com.apple.SafariPlatformSupport.Helper
    \"guard_pages_enabled\": %d, \n
        \"meta\": \"0x%llx\",\n
BUG IN LIBMALLOC: invalid executable_boothash length
Enabling ASLR slide on large allocations\n
MallocErrorSleep
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:412)
launchd_sim.debug
MallocXzoneGuardSmallRun
MallocHelperZone
*** sending SIGSTOP to help debug\n
MallocAllowInternalSecurity
 (slot=%u), counter=%d\n*** in-use ptr in free list slot=%u count=%d ptr=%p\n
com.apple.WebKit.Networking
CommCenter
Screen Sharing
__pgm_opt_out
Maximum magazines limited to number of logical CPUs (%d)\n
MallocLargeDisableASLR
 (slot=%u), counter=%d\n*** ptr not in szone slot=%d count=%d ptr=%p\n
Unable to map small linkage pointer %p\n
c
BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug
*** malloc_get_all_zones: error reading zones at %p\n
malloc_zero_on_free_enabled must be 0 or 1 - ignored.\n
%ld, counter=%d\n*** invariant broken for leader block %p - %d %d\n
MessagesAirlockService
disabled known process
%s    \"used\": %u, \n
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:342)
Failed to create carveout at 0x%lx in malloc guarded range 0x%lx: %d\n
*** sleeping to help debug\n
 %c[%p, %p) size=%zd\n
    \"reclaimable_bytes\": %llu, \n
xzm: failed to initialize deferred reclamation buffer [%d] %s (step %d)\n
\"segment_size\": %zu, \n
        \"last_dealloc_ts\": \"%llu\", \n
Web App
\nRegion %d: base address %p\n
Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n
        \"list_config\": \"%s\",\n
MallocXzoneListUpgradeThresholdSingle
BUG IN LIBMALLOC: pointer range initial overwrite failed
\"deallocate_segment\": %s, \n
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:176)
Failed to get scalable zone info\n
            \"size\": %u, \n
                \"last_chunk_empty_ts\": %llu\n
  Class %d: 
enabled
BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:
 arena        : [%p, %p)\n
metapool metadata slab
Malloc
valloc(0x%lx) = %p\n
FATAL ERROR - unable to allocate magazine array
com.apple.WebKit.WebContent.EnhancedSecurity.Development
BUG IN CLIENT OF LIBMALLOC: not an allocated block
\"segment_group_ids_count\": %u, \n
%s value (%s) invalid - ignored.\n
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:737)
BUG IN LIBMALLOC: unsupported allocation front count
 \n
    \"%d\": {\n
MallocXzoneThreadCaching
MallocSanitizerZoneDebug
com.apple.Safari.History
%s    \"segment_group\": %lu, \n
        \"xca_alloc_head\": \"0x%llx\",\n
MallocXzoneTinyThrashThreshold
MallocXzoneSegmentDeallocate
NanoV2 Config:\n\tNano On Xzone: %d\n
Maximum magazines limited to ncpuclusters (%d)\n
com.apple.quicklook.ThumbnailsAgent
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segme
arkitd
BUG IN CLIENT OF LIBMALLOC: MTE tag mismatch (probable double-free)
Failed to map guarded range: %d\n
tiny_chunk
Pointer %p to metadata being freed\n
wifianalyticsd
polarisd
        \"sequestered\": %d,\n
next_slot (1-based) = %d
Attempted to register zone more than once: %p\n
quicklookd
        \"guard_config\": {\n
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_seg
    \"small_guard_density\": %d \n
    \"large_guards_enabled\": %d,\n
mediaplaybackd
WhatIf
            \"segments\": { \n
        \"xzone\": %d, \n
%s
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
i32@?0Q8^{xzm_segment_s=(?={?=[16C]{?=^{xzm_segment_s}^^{xzm_segment_s}}[24C]^{xzm_segment_group_s}{?=[56C]}II{?=[56C]}IC{?=[56C]}I{?=[56C]}^v{?=[56C]}^v{?=[56C]}Q}[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=
        \"batch_count\": %u, \n
MallocAggressiveMadvise
        \"segment\": \"%p\", \n
*** can't allocate pages: mach_vm_map(size=%lu) failed (error code=%d)\n
will abort on heap corruption\n
    \"large_chunk_slots\": %d,\n
XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tNarrow Bucketing: %d\n\tGuard Pages: %d (Tiny: %d, %d/%d; Small: %d, %d/%d)\n\tGuard Objects: (Large: %d [%d+%d/%d; max %d, quarantine %u, reinit %d, bigsplit %u])\n\tScribble: %d\n\t
Large allocator death row cache not configured\n
        \"block_size\": %u, \n
MallocXzoneHugeCacheMaxEntryBytes
Malloc Config Outputs:\n\tProcess Identity: %u\n\tEnable Xzone Malloc: %d\n\tEnable Nano On Xzone: %d\n\tXzone Enablement Reason: %s\n
\tRecirc depot: 
SpeedGame
Failed to read ProbGuard zone at %p\n
MallocSanitizerZone: Not poisoning deallocation %p of size %lu due to missing pointers!\n
QuickLookSatellite
zero-on-free bincompat
MallocSanitizerNoPoisoning
Recirc depot \t
last
\tMagazine %d: 
MallocDeferredReclaimBufferCount
MallocXzonePerClusterSegmentGroups
malloc (%p/%llu): 
keychainsharingmessagingd
can't unmap excess guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
        \"range_group\": \"%p\", \n
vm.reclaim.enabled
MallocDoNotProtectPrelude
BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_
WalletBlastDoorService
BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1079)
MallocSanitizerZone
com.apple.WebKit.WebContent.EnhancedSecurity
\"multi_segment_size\": %zu, \n
\"guard_page_config\": {\n
        \"slot_state\": \"0x%llx\",\n
ThumbnailExtensionSecure
MTLCompilerService
    \"small_run_size\": %d, \n
%4u, %9s, %4u, %4u, %p\n
FATAL ERROR - ProbGuard: bad configuration
\n
*** error with %p: msize=%d, free: %x\n
        \"block_size\": %llu, \n
nano zone abandoned due to inability to reserve vm space.\n
        \"xca_free_count\": \"0x%llx\",\n
Fragments subject to reclamation=%ly
wakeboardd
    \"large_guard_reuse\": %d\n
        \"size\": %u \n
MallocQuarantineZone
\"addr\": \"%p\", \n
BUG IN LIBMALLOC: xzm_locked not implemented
MallocXzoneSlotUpgradeThreshold
_MallocMaxMagazines
BUG IN LIBMALLOC: bad chunk kind
guard_page
MallocCheckHeapAbort
BUG IN LIBMALLOC: failed to allocate memory
BUG IN LIBMALLOC: failed to overwrite mfm arena
        \"xca_walk_locked\": \"0x%llx\",\n
single_free
out-of-bounds
size(%p) = 0x%lx\n
Non-aligned pointer %p being freed (2)\n
notifyd
AegirPoster
blocks\n
        \"allocation_slots\": [\n
], \n
malloc_large_expanded_cache_threshold must be positive - ignored.\n
%y[%d] 
Failed to madvise block at blockp: %p, error: %d\n
MallocXzoneDeferLarge must be one of 0,1 - got %ld\n
MallocGuardEdges
%s\"%p\": {\n
true
ProbGuard: %9s 0x%llx, fill state: %3u/%u\n
MallocXzoneMemtagMaxBlockSize
MallocXzoneThreadCacheActivationTime
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:273
%s    \"kind\": \"%s\", \n
            } \n
Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n
MallocXzoneSlotConfig
BUG IN LIBMALLOC: asking for start of chunk with invalid kind
com.apple.Safari.SearchHelper
MallocSecureAllocator
tvOS feature flag
MallocDeferredReclaim must be one of 0,1 - got %ld\n
Maximum magazines set to %d\n
                \"xsg_waiters\": \"0x%llx\",\n
MessagesBlastDoorService
    \"enabled\": %d, \n
CLUSTER
guard_object
malloc_zero_on_free_sample_period must be positive - ignored.\n
MallocCheckZeroOnFreeCorruption
Unrecognized value for MallocDebugReport (%s) - using 'stderr'\n
\"guard_zones\": {\n
        \"metadata_addr\": \"%p\", \n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug
BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
MallocSanitizerZone: Not unpoisoning %p of size %lu due to missing pointers!\n
MallocXzoneEarlyAlloc must be 0 or 1.\n
MallocErrorStop
maild
ReportCrash
MallocNanoMaxMagazines must be positive - ignored.\n
MallocXzoneListUpgradePeriod
MallocTracing
Small recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
process feature flag
                \"xsc_ptr\": \"0x%llx\",\n
MallocDeferredReclaim
Guarded Range Config (base/size/carveout): 0x%lx / 0x%lx / 0x%lx\n
*** FATAL ERROR - unable to allocate magazine array.\n
fmfd
can't unmap excess trailing guard region\n*** mach_vm_deallocate(addr=%p, size=%lu) failed (code=%d)\n
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7872)
MallocLargeExpandedCacheThreshold
IMTranscoderAgent
\"range_groups\": {\n
MallocXzoneGuardedData
BUG IN LIBMALLOC: Failed to allocate xzm zone
will sleep for %d seconds on heap corruption\n
*** error %d
*** error %d\n
malloc_zone_malloc_with_options: reserved TSD bit set\n
realloc(%p, 0x%lx) = %p\n
com.apple.Safari.CredentialExtractionHelper
    \"large_guard_density\": %d,\n
                \"contentions\": %lu,\n
BUG IN CLIENT OF LIBMALLOC: memory corruption of free block
long-range OOB
Corruption of tiny freelist %p: size too small (%u/%u)\n
                \"allocs\": \"%llu\" \n
xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)
i24@?0Q8^v16
\"segment_groups\": {\n
        \"segment_cache\": { \n
kern.bootargs
MallocDoNotProtectPostlude
%ld, counter=%d\n*** invariant broken for %p (next in free list %p is not a free pointer)\n
small free list metadata inconsistency (headers[previous] != previous size)
prl_client_app
\"thread_caches\": [ \n
multi_free
Begin xzone malloc JSON:\n
\"mte_config\": {\n
MallocProbGuardAllocations
BUG IN LIBMALLOC: couldn't find executable_boothash
Failed to map small region at %p\n
mediaparserd
\"defer_small\": %s, \n
        \"free\": \"0x%x\",\n
... but not protecting postlude guard page\n
small_free_list_remove_ptr_no_clear: Internal invariant broken (next ptr of prev) for %p, prev_next=%p\n
com.apple.SafariServices.ExtensionHelper
Digital Performer
BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK
*** Will sleep for %d seconds to leave time to attach\n
                \"slot_config\": \"%s\",\n
MallocProbGuardSlots
sanitizer_malloc_with_options: unsupported options 0x%llx\n
i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b
i32@?0Q8Q16r*24
freed
BUG IN LIBMALLOC: Invalid xzone slot config
*** malloc_get_all_zones: error reading zones_address at %p\n
size(%p) = 0x%lx - redzone 0x%lx\n
Magazine=%d \t
Safari
    \"large_guard_reinit\": %d,\n
MallocTagAll
MallocXzoneInitialSlotConfig
logd
        \"in_use\": 1, \n
MallocErrorAbort
wifid
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:2216)
    \"last_sample_abs\": %llu, \n
        \"chunk_capacity\": %u, \n
MallocXzoneGuardLargeReinit
Failed to map tiny rack hashed_regions\n
%ld, counter=%d\n*** invariant broken for free block %p this msize=%d\n
avconferenced
IMDPersistenceAgent
        \"on_partial_list\": %d,\n
normal_segment
Failed to map region %p\n
com.apple.WebKit.WebContent.Development
                    
BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment
Small recirc depot is empty\n
%s    \"dirty_count\": %zu, \n
        \"lock\": %u, \n
none
small_freelist_chunk
ProbGuard configuration: %u kB budget, 1/%u sample rate, %u/%u/%u allocations/metadata/slots\n
%d: %p; 
BUG IN LIBMALLOC: unknown segment group id
evicting %p from quarantine, size = 0x%lx\n
small_free_list_find_by_ptr: ptr is not free (ptr metadata !SMALL_IS_FREE), ptr=%p msize=%d metadata=0x%x\n
        \"huge_alloc_counter\": \"%u\", \n
        \"runq_partial\": [\n
, allocated slots: %d, free slots = %d, occupancy: %d%%\n
MallocXzoneGuardLargeQuarantine
MallocXzoneMaxListConfig
   Slot %5d: %p, size %y
*** can't mvm_protect(%u) region at %p with size %lu\n
        \"xz_caches\": {\n
%s\n(Use 'atos' for a symbolic stack)\n
For region %p, first block: %d (%p), last block: %d (%p)\n
MallocCheckHeapSleep
Large expanded cache threshold defaulted to %lly\n
\n\tSizes in use: 
        \"next\": \"%p\", \n
+%u,
Failed to deallocate at address %p of size 0x%lx: %d\n
            }
                \"xz_idx\": %d, \n
        \"on_multi_segment\": %d\n
unused
_MallocNanoMaxMagazines
MallocXzoneBatchSize
BUG IN CLIENT OF LIBMALLOC: invalid address
%s    \"body_addr\": \"%p\", \n
        }
BUG IN CLIENT OF LIBMALLOC: free to empty or invalid chunk detected (likely double-free)
free(%p)\n
Unsupported guarded metadata allocation at address 0x%lx of size 0x%lx with flags %d and label %d\n
        \"user_slices\": %u,\n
BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice
BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:159)
                \"head\": \"0x%llx\", \n
CPU
executable_boothash
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug
Sanitizer
IINA
                \"atomic_value\": \"0x%llx\",\n
        \"kind\": \"%s\", \n
        \"alloc_idx\": %u,\n
MallocMaxMagazines
Small region [unknown address] was returned to the OS\n
MallocNanoOnXzone
MallocXzoneHugeChunkOffsets
videocodecd
%ld, counter=%d\n*** invariant broken for tiny free %p followed by %p in region %p [%p-%p] (end marker incorrect) should be %d; in fact %d\n
%s must be 0 or 1.\n
MallocEarlyMallocSecTransitionSupport must be 0 or 1.\n
FATAL ERROR - ProbGuard: invalid pointer passed to realloc
DefaultMallocZone
%ld, counter=%d\n*** invariant broken for region end %p - %p\n
*** can't mprotect(0x0) region for new postlude guard page at %p\n
MTE
DeltaForceClient
\"segment_group_front_count\": %u, \n
MallocProbGuardMemoryBudgetInKB
MallocLargeCache
BUG IN LIBMALLOC: Unexpected chunk kind
BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7548)
SafariViewService
MediaAnalysisBlastDoorService
CitiAuthenticator
                \"head\": \"NOT_CACHED\", \n
*** OBSOLETE: malloc_singlethreaded()\n
                \"seqno\": \"0x%llx\" \n
OOB + UAF
TelephonyBlastDoorService
MallocProbGuardMetadata
MallocXzoneGuardLargeReuse
IDSBlastDoorService
    \"max_block_size\": %d \n
DISABLED
*** FATAL ERROR - logical_ncpus %% phys_ncpus != 0\n.\n
small_free_list_remove_ptr_no_clear: Internal invariant broken (prev ptr of next) for %p, next_prev=%p\n
*** malloc_get_all_zones: error reading num_zones at %p\n
will sleep once for %d seconds on heap corruption\n
MallocXzonePtrBucketCount
*** Will sleep once for %d seconds to leave time to attach\n
\"chunk_threshold\": %u, \n
allocated
Arena #%d: base address %p. Blocks - active: %d, madvisable: %d, madvising: %d, madvised: %d, unused: %d\n
Size classes with allocated blocks: 
MallocTagAllInternal
Huge cache requires deferred reclamation for large.\n
Intel
    \"%u\": {\n
com.apple.WebKit.WebContent.CaptivePortal
_Malloc
realloc(%p, 0x%lx): size(%p) = 0x%lx - redzone 0x%lx)\n
Tiny recirc depot is empty\n
%s    \"swapped_count\": %zu, \n
        \"runq_quarantine\": [\n
%s value invalid - values must sum to %d, not %d - ignored.\n
MallocXzoneGuardLargeDensity
MallocCheckHeapStart
Tiny recirc depot: total bytes: %llu, in-use bytes: %llu, allocations: %llu, regions: %d (min # retained regions: %d)\n
\"xzones\": {\n
checks heap after operation #%d and each %d operations\n
        \"direction\": \"%s\"\n
Stack for last operation where the malloc check succeeded: 
large entry %p reallocated is not properly in table\n
Scalable zone %p: inUse=%u(%u) touched=%u allocated=%u flags=0x%x\n
Failed to map small rack magazines\n
Banco Galicia
Nano maximum magazines limited to number of physical CPUs [%d]\n
ClockFace
 high water   : %zd\n
MallocZeroOnAlloc
non-page-aligned, non-allocated pointer %p being freed\n
(unable to safely further examine remote process)\n
\tEmpty enough to be moved to recirc depot
        \"tagged\": %d,\n
MallocSanitizerRedzoneSize
huge_segment
BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1137)
d
                \"free_count\": \"0x%llx\", \n
MallocXzoneGuardLargeChunkMax
malloc(0x%lx) = %p\n
>=
\tNot empty enough to be moved to recirc depot
BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:7608)
MallocCheckHeapEach
                \"chunk\": \"%p\",\n
        ],\n
        \"segment_group\": %zu, \n
Large expanded cache threshold set to %lly\n
*** set a breakpoint in malloc_error_break to debug\n
DefaultPurgeableMallocZone
        \"slice_count\": %u, \n
MallocXzoneListUpgradeThreshold
HardenedRuntime
    \"sampling_period_abs\": %llu, \n
        ]\n
        \"base\": \"%p\", \n
Failed to map nanov2 region at %p\n
MallocXzoneSlotUpgradePeriod
BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:365)
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:324)
imagent
freelists\n
        \"xca_on_partial_list\": \"0x%llx\",\n
segment table slab
Nano maximum magazines set to %d\n
FATAL ERROR - logical_ncpus / phys_ncpus not 1, 2, or 4
%ld, counter=%d\n*** invariant broken for %p (next %p is not a free pointer)\n
segment metadata slab
Failed to map tiny region at %p\n
tiny_free_try_depot_unmap_no_lock objects_in_use not zero: %d\n
PROBABILISTIC_GUARD_MALLOC_TARGETED_COVERAGE:enable=1
MallocXzoneDeferSmall
BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:969)
%ld, counter=%d\n*** invariant broken: null msize ptr=%p num_small_regions=%d end=%p\n
malloc_entropy
BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:283)
launchd
BUG IN LIBMALLOC: asking for size of chunk with invalid kind
*** Recommend using 'setenv MallocCheckHeapStart %d; setenv MallocCheckHeapEach %d' to narrow down failure\n
com.apple.WebKit.WebContent.CaptivePortal.Development
    \"tail\": %llu, \n
MallocXzoneMemtagEnable
BUG IN LIBMALLOC: Attempting to free to non-chunk slice
BUG IN CLIENT OF LIBMALLOC: pointer being freed was not allocated
free_definite_size(%p, 0x%lx)\n
BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak
small_chunk
MallocXzoneAllocationFronts
i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=b63b1QSSI
com.apple.WebKit.WebContent
%s    \"addr\": \"%p\", \n
BUG IN LIBMALLOC: Slice count too large in init_segment
BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:
audiomxd
        } \n
pointer
Deferred reclamation cannot be used for xzones without large\n
Slots (#, state, offset, size, block address):\n
low
BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_malloc.c:5356)
BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind
MallocEnableMSLAtLimitWarning
free (%p/%llu): 
BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/C0D3D5A0-BC51-4BD2-A584-837B06C80F54/TemporaryDirectory.jroUWK/Sources/libmalloc_driverkit/src/xzone_malloc/xzone_segment.c:1134)
iOS bincompat list
*** OBSOLETE: malloc_debug()\n
MallocSimpleStackLogging
 *
%s    \"dispositions\": \"
        }\n
Unsupported MallocXzoneAllocationFronts\n
BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug
MallocRecircRetainedRegions
Failed to read szone structure\n
Failed to map tiny rack magazines\n
\"mzone\": %d, \n
UNKNOWN
use-after-free
malloc_zone_register allocation failed\n
vm.malloc_ranges
unknown
\"thread_cache_enabled\": %s, \n
WebSheet
%s    \"slice_count\": %u, \n
        \"remaining\": %zu, \n
        \"runq_full\": [\n
*** FATAL ERROR - ProbGuard: zone integrity check failed.\n
%s%y[%d]; 
com.apple.quicklook.extension.previewUI
    \"entries\": [ \n
VTEncoderXPCService
BUG IN LIBMALLOC: not MFM owned
  [%p, %p) size=%zd\n
\"guard_object_config\": {\n
Failed when changing state from MADVISING to MADVISED, block_metap = %p, blockp = %p\n
IMTransferAgent
mfm_arena info\n
                \"operations\": %lu,\n
MallocXzoneSmallThrashThreshold
Disabling ASLR slide on large allocations\n
tiny_free_list_remove_ptr: Internal invariant broken (prev ptr of next): ptr=%p, next_prev=%p\n
Pointer %p to metadata being freed (2)\n
[%lu small regions have been vm_deallocate'd]\n
%s    \"reclaim_id\": -1, \n
MallocReportConfig
%lu tiny regions:\n
Current Allocation Blocks By Size Class/Context [CPU]\n
Failed to map small rack\n
Failed to map nanozonev2_s at %p\n
Corruption of free object %p: msizes %u/%u disagree\n
Quarantine: size: %llu, address range: [%p - %p)\n
BUG IN LIBMALLOC: Unexpected guard bitmap state!
MallocAggressiveMadvise must be 0 or 1.\n
MallocZeroOnFree must be 0 or 1.\n
Corruption at %p: unexpected msizes %u/%u\n
HubbleBlastDoorService
    \"large_guard_force_quarantine\": %d,\n
        \"block_size\": %u,\n
MallocXzoneDeferLarge
MallocXzoneGuardLargeSlots
valloc (%p/%llu): 
ptr %p not in heap\n
            \"max_entry_slices\": %u, \n
FATAL ERROR - ProbGuard: memory budget too small
Unsupported wrapped zone version: %u\n
Unsupported protect debug flags %u\n
MallocProbGuard
FATAL ERROR - ProbGuard: invalid pointer passed to free
MallocProbGuardDebug
Invalid xzone_ptr_buckets value %ld - ignored.\n
, madvised
identityservicesd
MallocXzonePerClusterSegmentGroups must be 0 or 1.\n
```
