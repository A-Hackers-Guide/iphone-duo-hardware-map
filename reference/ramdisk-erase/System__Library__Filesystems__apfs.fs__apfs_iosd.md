# `/System/Library/Filesystems/apfs.fs/apfs_iosd`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 337,312 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2528)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
```

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression (compatibility version 1.0.0, current version 182.40.4)`
- `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>PURGE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
		<string>PURGEABLE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.apfs.get-dstreams</key>
	<true/>
	<key>com.apple.private.apfs.get-file-exts</key>
	<true/>
	<key>com.apple.private.apfs.get-graft-info</key>
	<true/>
	<key>com.apple.private.apfs.key-cache-eviction</key>
	<true/>
	<key>com.apple.private.apfs.keyrolling.operation</key>
	<true/>
	<key>com.apple.private.apfs.omm.ctl</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleAPFSUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (793)

```
com.apple.apfs.hash_violation.bt_node
smFragCountDist
%s:%d: %s error modifying omap: %d\n
mem_max_pos_change
IER status %d is not actionable. Exiting.\n
Resuming IER.
authapfs_integrity_meta_get_internal
apfs-doc-id-lock
spaceman-fxc-lock
btree_node_key_range_validate
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
disk
omap_records_rolled
authapfs_validate_node
nx_corruption_detected_int
mem_max_times_overcommitted
ca_stats_report
Failed to create session info dictionary for volume: %x.\n
starting_cursor
%s:%d: %s Error %d, reinitializing\n
\n
^v8@?0
can't initiate defrag on %s : %s\n
error: must be run as superuser
spaceman_unreserve
spaceman-free-lock
/dev/disk%d
hash_validation
APFS_INODES
smChunkFullnessFragDist=%20[0-9]
where [options] are\n
:%20[0-9]
get_misses
devices
succeeded
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
smFragSizeDist=%20[0-9]
spaceman_trim_free_extent_callback
cache_eviction
PFKT did not publish result for volume: %x.\n
%s:%d: %s Failed to get next extent: %d\n
AppleAPFSContainer
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: %s failed to get newnode minkey: %d\n
supplemental_tree_get_descriptor
nx-volume_group-lock
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
com.apple.filesystems.apfs_iosd.obj_cache_stats_report
epoch
class_A_main_forks_rolled
Failed to send PFKT stats report (gen. %llu) to Splunk: unknown error.\n
%s:%d: %s chunk %lld recent zone count overflow\n
CacheDeletePurgeSpaceWithInfo failed!
Cryptex stats report sent to Splunk.
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
virtual
%s:%d: %s failed to get omap tree for reaping: %d\n
/private/preboot/cryptex1/current/os.dmg
Failed to send IER stats report (gen. %u) to Splunk: %s.\n
class_D_rsrc_forks_rolled
apfs-dir-stats-id-lock
obj_cache_remove_new_fs_objects
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
block_size
shared_bytes_preserved
class_B_main_forks_rolled
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
get_times_called
mem_max_neg_change
v12@?0i8
DONE: Suspending cryptex stats report until next interval
apfs_reap_snapshots
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
spaceman_free_fs_deduct_block_counts
time_created
apfs
com.apple.filesystems.apfs_iosd.ca_stats_report
failed set state to DONE
spaceman_free_extent_cache_search
%s:%d: %s reap list object free list erroneously empty?\n
obj_init
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
fs_lookup_snapshot_metadata_by_xid
APFS_4K_OBJS
zeroes
oid
AppleNVMeController
scale_transcriber
%s:%d: %s lookup_next_snapshot() returned %d\n
type = %u, req_tree != fs_root\n
Failed to get RunLoopSource
%s:%d: %s omap_destroy returned %d!\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
gbitmap_reap
%s:%d: *** unknown obj type %d\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
Reference count overflowed for object %p!\n
spaceman_ip_bm_block_alloc
IER stats report (gen. %u) sent to Splunk.\n
Failed to find DATA volume
Failed to send Cryptex stats report to Splunk: unknown error.
apfs-clonegroup-lock-mutex
%s:%d: %s bt_move_entries %d failed: %d\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
usage: apfs_iosd [options]\n
transcribe_time
spaceman_cab_sanity_check
spaceman_freed
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
spaceman_sanity_check
/var/mobile/Library/Caches/com.apple.apfs_iosd.hints.plist
IOGeneralInterest
%s:%d: %s bogus phase, %u\n
APFS indicates further chunks need defrag, re-starting...
spaceman_free_extent_cache_insert
spaceman_fxtp_add_child
spaceman_free
APFS_TREE_LOOKUP_ZONE
nx_reaper_add_ext
start_time
apfs-stream-id-lock
gc_mem_freed_by_omm
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: spaceman_stats took too more than %u seconds, aborting!\n
object-lock
spaceman_fq_tree_find_overlap
Cache Delete needs %llu\n
Cannot create dispatch queue to perform cryptex report
%s:%d: *** Unknown file info type %llu\n
length
size
Cannot find entries matching %s - %u\n
Pausing IER.
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
AppleAPFSContainerScheme
Get count overflowed for object %p!\n
com.apple.filesystems.apfs
get_hits
get_file_num_extents failed with error %s(%d)\n
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
disabled
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
RoleValue
Failed IER status query: %s (%d). Cannot report ier stats to Splunk.\n
Failed to create session info dictionary
apfs-fext-tree-oid-lock
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
smChunkFragsForDataZone
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
PFKT stats report (gen. %llu) sent to Splunk.\n
smFragCountMetaZoneDist
smFragCountMetaZoneDist=%20[0-9]
\t%16p %s\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s obj_modify() failed: %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
spaceman_fs_bounds_clear
Failed to send IER stats report (gen. %u) to Splunk: unknown error.\n
DONE: Suspending defrag until next interval
bt_update_last_leaf
jobj_size_for_large_key_val
smFragCountDist=%20[0-9]
obj_release
spaceman_modify_bits
spaceman_fq_tree_insert
mem_lowest_overcommitted
DEFERRING: stopped defrag on %s\n
Failed to create payload dictionary for volume: %x.\n
%s:%d: %s Tree delete oid %llu threw %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s sfq %d count underflow %lld - %lld\n
spaceman_set_bits_in_bm
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
com.apple.filesystems.apfs_iosd.fx_defrag
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
alloc_times_alloced
exit_location
bytes_rolled
fexts_produced
%s:%d: unlock == 0 failed %d\n
apfs_reap_extentref_blocks
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
omap_reap
mem_max_current
apfs defrag is still working... (progress state: %u)\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
Failed IER status query: %s (%d). Continuing.\n
smStatsVersion
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
spaceman_get_metazone_alloc_index
spaceman_chunk_zone_info_recent_increment
times_lowest_overcommitted
/private/var/mobile
btree_delete
Reference count underflowed for object %p!\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
CACHE_DELETE_URGENCY_LIMIT
alloc_times_cached
times_alloc_failed
pause
Deferring while waiting for long-running CacheDelete purge.
authapfs_valid_hash_type
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
obj_delete_internal
np_ephemeral_mem
spaceman_free_extent_cache_remove
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
generation
Cannot create dispatch queue to perform battery monitoring
lookup_jobj_ext
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
AppleAPFSMedia
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
obj_cache_stats
gc_times_called_by_vm
IOService
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
spaceman_decrement_free_queue_count
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
hw_memsize
mem_max_time_modified
paddr
Failed to create payload dictionary
Failed to register to kIOPSNotifyTimeRemaining notifications to perform ier battery monitoring: %d\n
%s:%d: %s btree_node_key_update failed: %d\n
can not delete an object w/a non-current xid %lld o == %p\n
obj_get_async_read
spaceman_check_allocation_status_internal
apfs_mem_max
sparse_bytes_written
apfs-global-snap-lock
%s:%d: %s ***: expanded type seen on in-memory obj!\n
pos_change
com.apple.filesystems.apfs_iosd.cryptex_stats_report
apfs_sanity_check
nx-resize-spaceman-lock
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
cache_count
com.apple.filesystems.apfs_iosd.hash_validation
pfkt_stats
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
nx-txn-blocks-lock
spaceman_iterate_free_extents_internal
spaceman_alloc
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
storage
alloc_times_exceeded_max
ASPStorage
More than %llu are avaliable, no cache delete needed.\n
com.apple.filesystems.apfs_iosd_fx_defrag
class_E_rsrc_forks_rolled
apfs-snap-delete-lock
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
times_decreased
full
apfs-phys-lock-state-mutex
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
omap_sanity_check
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
Received kIOMessageServiceIsTerminated.
btree_node_compact
%s:%d: %s Tree iteration threw %d at cursor %llu\n
nx-global-extent-manipulation-lock
spaceman-lock
%s:%d: %s block range %lld:%lld out of bounds %lld\n
apfs-global-lock
apfs_sanity_check_tree_type
btree_node_insert_internal
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
defrag starting on %s\n
apfs-integrity-meta-lock
apfs-dir-size-lock
%s:%d: %s iter_next returned %d\n
key_val_to_jobj
SYSTEM_GRAFT_4K_OBJS
obj_checksum_verify
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
supplemental_tree_destroy
%s:%d: %s chunk %lld recent zone count underflow\n
fx_defrag
ephemeral_mem
mem_max_times_increased
setupCacheDelete returned %d\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
AppleAPFSSnapshot
smFragSizeDist
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
class_C_main_forks_rolled
%s:%d: %s object type 0x%x not reapable: %d\n
%s:%d: %s failed to get reap list head: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
Attempting to reuse a non-candidate chunk zone info\n
spaceman_chunk_zone_info_list_remove
bytes_leaked
%s:%d: %s unable to get fs object 0x%llx: %d\n
smFragSizeMetaZoneDist=%20[0-9]
type
resume
current_id
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
DEFERRING XPC activity on volume
Failed to create user info dictionary
%sr%s
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
obj_cache_remove_reverted_fs_objects
apfs-phys-ext-oid-lock
invalid lock flags: 0x%x\n
r+
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
dev_name
class_B_rsrc_forks_rolled
apfs-omap-lock
spaceman_fxc_update_smallest_with_successor
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
jobj_size_for_key_val
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
alloc_times_evicted
    -d [-d] [-d]   Increase debug logging verbosity\n
Failed to query battery status: %d. Exiting.\n
rdisk
alloc_times_called
build version has changed to %s\n
-apfs_newvf_enabled
failed to set cryptex stats report state to DONE
btree_node_val_range_validate
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
Requested forced secondary_fs_root but the tree is missing\n
class_A_rsrc_forks_rolled
btree_node_sanity_check
failed to set xpc activity state to %d (current state: %d)\n
/var
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s_%u
alloc_times_freed
    -h             Display usage\n
ier_telemetry
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
%s:%d: %s Can't get tree: %d\n
sealed, fext, req_tree != fs_root
APFS_8K_OBJS
invalid tweak type %d\n
error: failed to open container for cache eviction
apfs-im-cache-lock
jobj_release
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
%s:%d: %s tree_delete() failed: %d\n
rolling-stats-lock
bt_lookup_copy_out
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
PFKT stats report (gen. %llu) already sent to Splunk.\n
%s:%d: %s Hit %d looking up first snapshot\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
/dev/
.dmg
com.apple.filesystems.apfs_iosd_ier_battery_monitoring
failed to set cryptex stats report state to DEFER
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
spaceman_chunk_zone_info_recent_decrement
class_D_main_forks_rolled
btree_node_insert
%s:%d: %s Container corruption detected by %s:%u!\n
nx_reap_list_sanity_check
omap_find_next_snapshot_xid
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
spaceman_ip_freed
drain_time
Unknown PFKT stats version: %llu\n
mount_apfs
make_jkey_from_jobj
smStatsError
spaceman_ip_bm_block_free
spaceman_alloc_iterate_chunks
global
get_graft_lut_reduction failed with error %s(%d)\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
v16@?0^{_xpc_activity_s=}8
gc_times_called_by_omm
Failed to send PFKT stats report (gen. %llu) to Splunk: %s.\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: Why are we comparing a chunk to itself?\n
triggering eviction for keys cache %s\n
%s:%d: %s unsupported tree type: %d\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
apfs-snapmeta-oid-lock
btree_node_child_val
unexpected storagetype: 0x%x\n
root
/var/mobile
CACHE_DELETE_AMOUNT
rsrc_forks_rolled
CacheDeletePurgeSpaceWithInfo returned no results.
Successfully registered for io notifications
%s:%d: %s Failed to delete covered node from length tree: %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
APFS_BTREE_NODES
/
current
Failed to send Cryptex stats report to Splunk: %s.\n
authapfs_validate_node_hash
%s:%d: wrlock == 0 failed %d\n
Failed to create Notification Port
bt_insert
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
%s:%d: %s unable to get snapshot tree: %d\n
spaceman-ip-lock
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: Container corruption detected by %s:%u!\n
lite
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
large_key_val_to_jobj
smChunkIndexForDataZone
smChunksEmpty=%20[0-9]
%s:%d: %s reverting on error: %d\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
smChunksFull
apfs-flags-lock
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d: *** Can't release unknown obj type %d\n
jfs_get_tree_in_snap
make_large_jkey_header_from_jobj
nx_reaper_add_sub_object
os_cryptex_lut_reduction
defrag running for 1 hour, terminating now
Cannot create dispatch queue to perform APFS FX defrag
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
bt_shift_or_split
%s%s
invalid unlock flags: 0x%x\n
v8@?0
count_lowest_overcommitted
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%s:%d: %s unable to get omap: %d\n
obj_delete_and_free_by_oid
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
new address mismatch on redirty 0x%llx 0x%llx\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
gc_mem_freed_by_vm
version
build version has not changed, do not send report
apfs_reap
match_jobj_expanded_type_to_tree_type
jobj_allocate
spaceman-dev-lock
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
cryptex_stats_report
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
smFragSizeMetaZoneDist
obj_read
spaceman_cib_sanity_check
Failed to %s IER thread: %s (%d)\n
end_time
spaceman_fxc_tree_node_recycle_smallest
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s error getting cab %d @ %lld: %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
invalid crypto index %d\n
%s:%d: %s %lld:%lld error: %d\n
1
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
dh
inodes_processed
com.apple.filesystems.apfs_iosd.cache_eviction
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
neg_change
/private/var
keybag_stashed_or_unlocked
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
v16@?0^{__CFDictionary=}8
APFS reported defrag status idle
apfs-pfkur-tree-oid-lock
omap_destroy
spaceman_set_up_ip_reverse_mapping_tree
com.apple.apfs.stats
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
IER status: %d, percent: %d, is_charging: %d.\n
xattrs_rolled
RTCReporting framework is absent, unregistering activity
Can't convert ProductBuildVersion to CString
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
time_accessed
nand-fragmentation
btree rightmost leaf field is set for physical tree!\n
apfs_free_data_blocks
smChunkFragsForDataZone=%20[0-9]
/private/preboot/Cryptexes/OS
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
spaceman_stats_free_extent_cb
mem_max_lowest
Successfully purged %llu bytes.\n
Failed to create dictionary for purging.
btree_node_reap
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
bt_merge_nodes
jobj_validate_large_key_val
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
com.apple.system.powersources.timeremaining
apfs-rename-lock
apfs-incompat-features-lock
bt_remove_internal
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
error
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
bt_merge_up
%s:%d: %s failed to create reap list: %d\n
nx_reaper_sanity_check
obj_destroy_complete
mem_max_highest
Failed to register for io notifications, result:0x%x\n
cache eviction XPC activity complete
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
mem_max_times_decreased
num_os_cryptex_extents
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
smChunkFullnessFragDist
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
spaceman_chunk_zone_info_compare
AppleAPFSVolume
Failed to create user info dictionary for volume: %x.\n
roll_cycles
btree_node_entry_update
%s:%d: %s failed to get reap list tail: %d\n
nx-omap-lock
%s:%d: %s error getting mapping tree: %d\n
%s:%d: %s error searching spaceman free queue tree: %d\n
fexts_encountered
failed
%ss%d:%lld
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s *** unknown expanded obj type %hhu\n
enabled
spaceman_alloc_fxc_scan_wait
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
mem_max_overcommitted
class_E_main_forks_rolled
spaceman_free_extent_cache_reset
contains_rootfs
class_C_rsrc_forks_rolled
ier_battery_monitoring
com.apple.filesystems.apfs_iosd_cryptex_stats_report
DEFERRING cryptex stats report XPC activity
jobj_validate_key_val
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
pfkt_telemetry
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
/private/var/MobileSoftwareUpdate/smstats
failed to set cache eviction state to DONE
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s bt_shift_or_split failed with error: %d\n
btree_node_free_list_entry_validate
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
obj_create_internal
mem
obj_cache_stats_report
PFKTResult
PFKT result had unexpected type for volume: %x.\n
RTCReporting framework is absent, not registering for IO notifications
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
%s:%d: %s invalid object size: %d size_phys %d\n
spaceman_chunk_zone_info_add
com.apple.filesystems.apfs_iosd
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
smChunkIndexForDataZone=%20[0-9]
obj_cache_remove
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
spaceman_get_new_chunk_for_allocation_zone
e-apfs
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
times_increased
omap_records_total
failed set state to DEFER
smChunksFull=%20[0-9]
Release count overflowed for object %p!\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
failed to stop defrag on %s : %s\n
btree_node_child_id_update
%s:%d: %s updating grandparent failed w/%d\n
IOMatchCategory
omap_cleanup
spaceman_ip_block_alloc
subtype
policy
%02hhx
nx-tree-node-compact-lock
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s removal of replaced free extent failed: %d\n
spaceman_fxc_update_length
smChunksEmpty
total_time
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
CACHE_DELETE_VOLUME
IODeviceTree:/filesystems
default
ephemeral
obj_alloc
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
error retrieving defrag state: %s\n
/var/mobile/Library/Caches/com.apple.apfs_iosd.stats.plist
main_forks_rolled
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
%s:%d: *** Can't allocate unknown obj type %d\n
obj_modify
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
spaceman_free_completed
com.apple.notifyd.matching
v16@?0^v8
%ss%d
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
spaceman-space-usage-lock
spaceman_clear_bits_in_bm
/private/preboot/cryptex1/current/%s
smStatsErrorLoc
Successfully purged %llu bytes.\n
CacheDeletePurgeSpaceWithInfo failed!\n
Cannot create dispatch queue to perform battery monitoring\n
PFKT stats report (gen. %llu) sent to Splunk.\n
failed to set cache eviction state to DONE\n
failed to collect spaceman stats: %s (%d)\n
failed to set object cache stats report state to DEFER\n
apfs defrag is still working... (progress state: %u)\n
Failed to create dictionary for purging.\n
IER status: %d, percent: %d, is_charging: %d.\n
%s event was %s\n
object cache stats for container %s not added to array\n
Cannot create dispatch queue to perform APFS FX defrag\n
Failed IER status query: %s (%d). Cannot report ier stats to Splunk.\n
Failed to create session info dictionary for volume: %x.\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
failed to create xpc dictionary\n
reporting stats from live container\n
Failed to create session info dictionary\n
Successfully sent object cache stats report to Splunk.\n
object cache stats for container %s not added to dictionary\n
error: must be run as superuser\n
IER status %d is not actionable. Exiting.\n
Cannot create dispatch queue to perform cryptex report\n
Failed to get RunLoopSource\n
Failed to send PFKT stats report (gen. %llu) to Splunk: %s.\n
START: Initiating object cache stats report\n
Failed to create object cache stats dictionary\n
Failed to create user info dictionary\n
Failed to %s IER thread: %s (%d)\n
error: failed to allocate set: %s (%d)\n
error: unexpected format for device %s: %s (%d)\n
defrag starting on %s\n
failed to stop defrag on %s : %s\n
DEFERRING XPC activity on volume\n
Cryptex stats report sent to Splunk.\n
Failed to register for io notifications, result:0x%x\n
Failed to find DATA volume\n
Cannot create dispatch queue to perform object cache report\n
DEFERRING object cache stats report XPC activity\n
error: failed to get graft info: %s (%d)\n
can't initiate defrag on %s : %s\n
Failed to register to kIOPSNotifyTimeRemaining notifications to perform ier battery monitoring: %d\n
build version has not changed, do not send report\n
build version has changed to %s\n
Can't convert ProductBuildVersion to CString\n
key %s not added to dictionary\n
Failed to send Cryptex stats report to Splunk: unknown error.\n
Failed to create user info dictionary for volume: %x.\n
error: failed to open container for cache eviction\n
failed to statfs root directory: %s (%d)\n
DONE: completed stats report\n
CacheDeletePurgeSpaceWithInfo returned no results.\n
DEFERRING cryptex stats report XPC activity\n
RTCReporting framework is absent, not registering for IO notifications\n
PFKT result had unexpected type for volume: %x.\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
reporting stats from file\n
DONE: Suspending object cache stats report until next interval\n
Failed to send object cache stats report to Splunk: unknown error.\n
failed set state to DEFER\n
Failed to create Notification Port\n
Failed to send IER stats report (gen. %u) to Splunk: unknown error.\n
failed to parse spaceman stats file: %s (%d)\n
failed set stats_report xpc activity state to DONE\n
Failed to create payload dictionary\n
APFS reported defrag status idle\n
Deferring while waiting for long-running CacheDelete purge.\n
Failed IER status query: %s (%d). Continuing.\n
get_file_num_extents failed with error %s(%d)\n
Failed to send PFKT stats report (gen. %llu) to Splunk: unknown error.\n
cache eviction XPC activity complete\n
setupCacheDelete returned %d\n
Resuming IER.\n
DONE: Suspending cryptex stats report until next interval\n
Failed to create payload dictionary for volume: %x.\n
Failed to send IER stats report (gen. %u) to Splunk: %s.\n
PFKT did not publish result for volume: %x.\n
failed to truncate spaceman stats file: %s (%d)\n
Failed to create devices array\n
Failed to query battery status: %d. Exiting.\n
get_graft_lut_reduction failed with error %s(%d)\n
Cannot find entries matching %s - %u\n
Successfully registered for io notifications\n
Received kIOMessageServiceIsTerminated.\n
IER stats report (gen. %u) sent to Splunk.\n
Unknown PFKT stats version: %llu\n
error: fsgetpath failed for ino %llu: %s (%d)\n
error: failed to fetch stats for device %s: %s (%d)\n
defrag running for 1 hour, terminating now\n
failed to set cryptex stats report state to DEFER\n
Failed to send Cryptex stats report to Splunk: %s.\n
Failed to collect object cache stats: %s (%d)\n
failed to set object cache stats report state to DONE\n
error retrieving defrag state: %s\n
failed set state to DONE\n
Pausing IER.\n
PFKT stats report (gen. %llu) already sent to Splunk.\n
triggering eviction for keys cache %s\n
RTCReporting framework is absent, unregistering activity\n
Failed to send object cache stats report to Splunk: unknown error (missing description).\n
Cache Delete needs %llu\n
APFS indicates further chunks need defrag, re-starting...\n
DEFERRING: stopped defrag on %s\n
failed to set xpc activity state to %d (current state: %d)\n
DONE: Suspending defrag until next interval\n
failed to set cryptex stats report state to DONE\n
Failed to send object cache stats report to Splunk: %s.\n
More than %llu are avaliable, no cache delete needed.\n
```
