# `/System/Library/Filesystems/apfs.fs/apfs_iosd`

From the upgrade restore ramdisk (141-29011-104.dmg). 337,312 bytes.

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
omap_destroy
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
btree_node_insert
spaceman_stats_free_extent_cb
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
%s:%d: %s invalid object size: %d size_phys %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
reserved metadata space underflow: %lld (%lld)\n
mem_max_pos_change
apfs-snap-delete-lock
bt_insert
APFS_8K_OBJS
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s error unreserving space, %lld blocks: %d\n
/private/var
/var
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
btree_node_child_id_update
bt_update_last_leaf
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
zeroes
match_jobj_expanded_type_to_tree_type
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
Cannot create dispatch queue to perform battery monitoring
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
obj_read
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
com.apple.filesystems.apfs
class_D_main_forks_rolled
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
large_key_val_to_jobj
com.apple.filesystems.apfs_iosd.hash_validation
btree_node_val_range_validate
alloc_times_evicted
omap_records_total
Failed to send PFKT stats report (gen. %llu) to Splunk: unknown error.\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
IOService
apfs_sanity_check
%s:%d: %s obj_modify(fs %lld) failed: %d\n
can not delete an object w/a non-current xid %lld o == %p\n
/private/var/MobileSoftwareUpdate/smstats
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s bogus phase, %u\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
nx_reap_list_sanity_check
subtype
exit_location
main_forks_rolled
class_E_rsrc_forks_rolled
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
btree_node_insert_internal
smChunksEmpty=%20[0-9]
Release count overflowed for object %p!\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
spaceman_alloc_iterate_chunks
cache_count
contains_rootfs
starting_cursor
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
time_accessed
DEFERRING XPC activity on volume
error: must be run as superuser
Failed to create session info dictionary
spaceman_free_extent_cache_insert
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
CACHE_DELETE_AMOUNT
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
spaceman_fq_tree_insert
rsrc_forks_rolled
pfkt_stats
btree_node_child_val
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
virtual
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
ca_stats_report
com.apple.filesystems.apfs_iosd_ier_battery_monitoring
Received kIOMessageServiceIsTerminated.
apfs-flags-lock
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s reverting on error: %d\n
smChunkFullnessFragDist=%20[0-9]
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
gc_mem_freed_by_omm
keybag_stashed_or_unlocked
btree_node_key_range_validate
%s:%d: %s btree_node_insert failed: %d\n
jobj_size_for_large_key_val
build version has changed to %s\n
apfs_sanity_check_tree_type
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s failed to create reap list: %d\n
spaceman_ip_bm_block_alloc
class_B_main_forks_rolled
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
spaceman_cab_sanity_check
get_hits
failed set state to DONE
%s:%d: %s lookup_next_snapshot() returned %d\n
rdisk
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: %s chunk %lld recent zone count overflow\n
/private/preboot/cryptex1/current/%s
root
Cache Delete needs %llu\n
Cannot create dispatch queue to perform APFS FX defrag
apfs-global-lock
btree_delete
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
com.apple.apfs.stats
ASPStorage
com.apple.system.powersources.timeremaining
com.apple.filesystems.apfs_iosd.cryptex_stats_report
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
rolling-stats-lock
alloc_times_called
%s:%d: unlock == 0 failed %d\n
apfs_reap
%s:%d: %s obj_modify() failed: %d\n
spaceman-space-usage-lock
    -d [-d] [-d]   Increase debug logging verbosity\n
PFKT did not publish result for volume: %x.\n
Failed to create Notification Port
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
type = %u, req_tree != fs_root\n
%s:%d: %s error deleting empty snapshot tree: %d\n
/
mem_max_times_decreased
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
btree_node_free_list_entry_validate
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
apfs defrag is still working... (progress state: %u)\n
Unknown PFKT stats version: %llu\n
jfs_get_tree_in_snap
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
^v8@?0
%s:%d: %s btree_node_key_update failed: %d\n
AppleAPFSContainer
spaceman_fq_tree_find_overlap
spaceman_cib_sanity_check
apfs
Resuming IER.
apfs-integrity-meta-lock
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
nand-fragmentation
default
btree_node_sanity_check
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
ephemeral
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
CACHE_DELETE_VOLUME
AppleAPFSVolume
DONE: Suspending cryptex stats report until next interval
where [options] are\n
resume
Cannot find entries matching %s - %u\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
smChunkFragsForDataZone
invalid crypto index %d\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
spaceman_ip_bm_block_free
alloc_times_freed
failed
Successfully registered for io notifications
apfs-doc-id-lock
%s:%d: %s unable to get snapshot tree: %d\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
e-apfs
-apfs_newvf_enabled
count_lowest_overcommitted
APFS reported defrag status idle
spaceman_fxc_update_smallest_with_successor
Reference count overflowed for object %p!\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
hash_validation
com.apple.filesystems.apfs_iosd.obj_cache_stats_report
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s Can't get tree: %d\n
disk
setupCacheDelete returned %d\n
class_E_main_forks_rolled
PFKTResult
Failed to send PFKT stats report (gen. %llu) to Splunk: %s.\n
obj_init
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
version
start_time
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s failed to get reap list head: %d\n
invalid lock flags: 0x%x\n
%s:%d: %s error getting mapping tree: %d\n
com.apple.filesystems.apfs_iosd_fx_defrag
bytes_leaked
jobj_release
smFragCountDist=%20[0-9]
mem_max_current
alloc_times_alloced
nx-resize-spaceman-lock
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s error modifying omap: %d\n
times_lowest_overcommitted
/dev/
total_time
RTCReporting framework is absent, unregistering activity
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
sealed, fext, req_tree != fs_root
smChunkFragsForDataZone=%20[0-9]
Allocated %s object with OID %lld flags %llx type %x %d from\n
gc_times_called_by_vm
Failed to create payload dictionary for volume: %x.\n
lite
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
spaceman_clear_bits_in_bm
spaceman_get_new_chunk_for_allocation_zone
get_times_called
gc_mem_freed_by_vm
mem
times_alloc_failed
pause
/private/preboot/Cryptexes/OS
fexts_encountered
succeeded
Cryptex stats report sent to Splunk.
error: failed to open container for cache eviction
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
nx_reaper_add_ext
smFragSizeMetaZoneDist=%20[0-9]
%s:%d: %s omap_destroy returned %d!\n
%s:%d: %s iter_next returned %d\n
spaceman_free_fs_deduct_block_counts
mem_lowest_overcommitted
obj_modify
obj_create_internal
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
v16@?0^v8
jobj_validate_large_key_val
obj_destroy_complete
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
spaceman_ip_freed
alloc_times_exceeded_max
Failed to query battery status: %d. Exiting.\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
disabled
apfs_mem_max
APFS_4K_OBJS
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
%s:%d: %s removal of replaced free extent failed: %d\n
DEFERRING: stopped defrag on %s\n
roll_cycles
%s:%d: wrlock == 0 failed %d\n
apfs-stream-id-lock
APFS_TREE_LOOKUP_ZONE
spaceman_decrement_free_queue_count
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
mem_max_highest
block_size
class_A_main_forks_rolled
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
1
Failed to get RunLoopSource
build version has not changed, do not send report
%02hhx
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
com.apple.filesystems.apfs_iosd.cache_eviction
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s failed to get omap tree for reaping: %d\n
spaceman_iterate_free_extents_internal
spaceman-dev-lock
spaceman_get_metazone_alloc_index
recent zone chunk should have only ONE reference when being moved to the recent list!\n
IODeviceTree:/filesystems
current
oid
com.apple.filesystems.apfs_iosd_cryptex_stats_report
/var/mobile/Library/Caches/com.apple.apfs_iosd.stats.plist
sparse_bytes_written
authapfs_validate_node_hash
bt_lookup_copy_out
class_C_rsrc_forks_rolled
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
enabled
omap_reap
spaceman_freed
Failed to create payload dictionary
%ss%d:%lld
nx-txn-blocks-lock
smFragCountDist
Reference count underflowed for object %p!\n
global
usage: apfs_iosd [options]\n
fexts_produced
triggering eviction for keys cache %s\n
apfs-dir-stats-id-lock
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
hw_memsize
obj_cache_stats_report
failed to set xpc activity state to %d (current state: %d)\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
gc_times_called_by_omm
epoch
AppleAPFSMedia
ier_battery_monitoring
cryptex_stats_report
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
new address mismatch on redirty 0x%llx 0x%llx\n
invalid tweak type %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
Pausing IER.
%s:%d: %s Failed to find successor node in length tree: %d\n
btree_node_compact
nx-omap-lock
\n
smFragSizeMetaZoneDist
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
mem_max_times_increased
time_created
Failed to create user info dictionary for volume: %x.\n
PFKT stats report (gen. %llu) sent to Splunk.\n
drain_time
btree rightmost leaf field is set for physical tree!\n
mem_max_lowest
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
bt_remove_internal
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
make_large_jkey_header_from_jobj
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
spaceman-free-lock
APFS indicates further chunks need defrag, re-starting...
apfs-im-cache-lock
apfs_reap_snapshots
spaceman_chunk_zone_info_load_recent_chunks
get_misses
IOGeneralInterest
%ss%d
spaceman_chunk_zone_info_add
.dmg
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
omap_find_next_snapshot_xid
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s chunk %lld recent zone count underflow\n
%s:%d: Why are we comparing a chunk to itself?\n
class_C_main_forks_rolled
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
spaceman_alloc_fxc_scan_wait
ephemeral_mem
class_A_rsrc_forks_rolled
Failed to find DATA volume
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s Container corruption detected by %s:%u!\n
obj_cache_remove_new_fs_objects
Failed to register to kIOPSNotifyTimeRemaining notifications to perform ier battery monitoring: %d\n
failed to set cryptex stats report state to DONE
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
nx-tree-node-compact-lock
np_ephemeral_mem
/var/mobile
btree_node_reap
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
mem_max_overcommitted
AppleNVMeController
CACHE_DELETE_URGENCY_LIMIT
com.apple.notifyd.matching
xattrs_rolled
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
spaceman_free
spaceman_trim_free_extent_callback
/dev/disk%d
length
apfs-snapmeta-oid-lock
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: *** unknown obj type %d\n
Failed to create user info dictionary
obj_cache_lock_by_state, invalid oc_lock_state %d\n
spaceman_free_completed
times_increased
defrag starting on %s\n
%sr%s
smStatsErrorLoc
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
apfs-dir-size-lock
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
jobj_size_for_key_val
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
/private/var/mobile
Failed IER status query: %s (%d). Cannot report ier stats to Splunk.\n
bytes_rolled
PFKT result had unexpected type for volume: %x.\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
\t%16p %s\n
spaceman_chunk_zone_info_recent_decrement
%s:%d: %s *** unknown expanded obj type %hhu\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
inodes_processed
failed to set cryptex stats report state to DEFER
bt_merge_up
%s:%d: %s unable to get fs object 0x%llx: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
obj_get_async_read
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
v16@?0^{__CFDictionary=}8
IOMatchCategory
%s:%d: %s unable to get omap: %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
mem_max_neg_change
%s%s
%s:%d: %s failed to get reap list tail: %d\n
omap_sanity_check
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
spaceman_fxc_tree_node_recycle_smallest
storage
cache_eviction
com.apple.filesystems.apfs_iosd.fx_defrag
Failed to send Cryptex stats report to Splunk: unknown error.
supplemental_tree_destroy
obj_delete_and_free_by_oid
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
RoleValue
authapfs_integrity_meta_get_internal
apfs-rename-lock
obj_cache_remove_reverted_fs_objects
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
Attempting to reuse a non-candidate chunk zone info\n
size
Failed to %s IER thread: %s (%d)\n
Failed to create session info dictionary for volume: %x.\n
apfs-pfkur-tree-oid-lock
spaceman_sanity_check
ier_telemetry
v12@?0i8
IER stats report (gen. %u) sent to Splunk.\n
full
spaceman_free_extent_cache_search
%s:%d: %s sfq %d count underflow %lld - %lld\n
Failed to send IER stats report (gen. %u) to Splunk: %s.\n
CacheDeletePurgeSpaceWithInfo returned no results.
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
smChunksFull
omap_cleanup
com.apple.apfs.hash_violation.bt_node
omap_records_rolled
Get count overflowed for object %p!\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s unsupported tree type: %d\n
%s:%d: %s Tree delete oid %llu threw %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
devices
mem_max_time_modified
shared_bytes_preserved
%s:%d: Invalid or unknown hash type: %d\n
jobj_validate_key_val
:%20[0-9]
smChunksFull=%20[0-9]
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
failed to stop defrag on %s : %s\n
Failed IER status query: %s (%d). Continuing.\n
apfs_free_data_blocks
smFragSizeDist
smStatsVersion
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
spaceman_ip_block_alloc
CacheDeletePurgeSpaceWithInfo failed!
cache eviction XPC activity complete
AppleAPFSSnapshot
key_val_to_jobj
smChunkIndexForDataZone=%20[0-9]
invalid unlock flags: 0x%x\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
spaceman_set_bits_in_bm
failed to set cache eviction state to DONE
spaceman-fxc-lock
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
apfs-omap-lock
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
nx_corruption_detected_int
nx-volume_group-lock
smChunksEmpty
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
v16@?0^{_xpc_activity_s=}8
paddr
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
gbitmap_reap
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
v8@?0
get_graft_lut_reduction failed with error %s(%d)\n
obj_alloc
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
type
Failed to send IER stats report (gen. %u) to Splunk: unknown error.\n
DEFERRING cryptex stats report XPC activity
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
jobj_allocate
spaceman_alloc
spaceman_unreserve
bt_shift_or_split
%s:%d: %s updating grandparent failed w/%d\n
IER status %d is not actionable. Exiting.\n
defrag running for 1 hour, terminating now
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
smFragCountMetaZoneDist
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s %lld:%lld error: %d\n
obj_release
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
spaceman_fs_bounds_clear
spaceman_chunk_zone_info_compare
mem_max_times_overcommitted
os_cryptex_lut_reduction
Failed to send Cryptex stats report to Splunk: %s.\n
Deferring while waiting for long-running CacheDelete purge.
supplemental_tree_get_descriptor
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
obj_checksum_verify
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
object-lock
PFKT stats report (gen. %llu) already sent to Splunk.\n
transcribe_time
apfs-phys-ext-oid-lock
spaceman_free_extent_cache_remove
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
/var/mobile/Library/Caches/com.apple.apfs_iosd.hints.plist
com.apple.filesystems.apfs_iosd.ca_stats_report
class_D_rsrc_forks_rolled
%s:%d: spaceman_stats took too more than %u seconds, aborting!\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
spaceman-lock
spaceman_set_up_ip_reverse_mapping_tree
spaceman_check_allocation_status_internal
times_decreased
IER status: %d, percent: %d, is_charging: %d.\n
mount_apfs
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s reap list object free list erroneously empty?\n
%s:%d: %s error getting cab %d @ %lld: %d\n
spaceman_modify_bits
DONE: Suspending defrag until next interval
nx_reaper_add_sub_object
spaceman_chunk_zone_info_list_remove
can't initiate defrag on %s : %s\n
dh
pfkt_telemetry
get_file_num_extents failed with error %s(%d)\n
end_time
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
error retrieving defrag state: %s\n
error
apfs-clonegroup-lock-mutex
btree_node_entry_update
lookup_jobj_ext
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
%s:%d: %s Failed to get next extent: %d\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
r+
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
Can't convert ProductBuildVersion to CString
spaceman_fxtp_add_child
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: %s object type 0x%x not reapable: %d\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
apfs-incompat-features-lock
%s:%d: %s Hit %d looking up first snapshot\n
make_jkey_from_jobj
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: Container corruption detected by %s:%u!\n
/private/preboot/cryptex1/current/os.dmg
current_id
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
class_B_rsrc_forks_rolled
spaceman_fxc_update_length
smFragCountMetaZoneDist=%20[0-9]
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
smFragSizeDist=%20[0-9]
neg_change
num_os_cryptex_extents
generation
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
More than %llu are avaliable, no cache delete needed.\n
apfs-fext-tree-oid-lock
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
obj_delete_internal
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
    -h             Display usage\n
fx_defrag
authapfs_validate_node
AppleAPFSContainerScheme
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
spaceman_chunk_zone_info_recent_increment
Failed to create dictionary for purging.
RTCReporting framework is absent, not registering for IO notifications
APFS_BTREE_NODES
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
smStatsError
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
APFS_INODES
smChunkIndexForDataZone
%s:%d: %s error searching spaceman free queue tree: %d\n
failed set state to DEFER
fs_lookup_snapshot_metadata_by_xid
smChunkFullnessFragDist
unexpected storagetype: 0x%x\n
%s_%u
Successfully purged %llu bytes.\n
com.apple.filesystems.apfs_iosd
policy
apfs-global-snap-lock
apfs_reap_extentref_blocks
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
nx-global-extent-manipulation-lock
obj_cache_stats
alloc_times_cached
scale_transcriber
bt_merge_nodes
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
dev_name
pos_change
Cannot create dispatch queue to perform cryptex report
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: %s failed to move all entries: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
obj_cache_remove
spaceman-ip-lock
Failed to register for io notifications, result:0x%x\n
authapfs_valid_hash_type
spaceman_free_extent_cache_reset
apfs-phys-lock-state-mutex
nx_reaper_sanity_check
Failed IER status query: %s (%d). Cannot report ier stats to Splunk.\n
Failed to send PFKT stats report (gen. %llu) to Splunk: unknown error.\n
failed to set cache eviction state to DONE\n
object cache stats for container %s not added to array\n
Failed to %s IER thread: %s (%d)\n
get_file_num_extents failed with error %s(%d)\n
Failed to register for io notifications, result:0x%x\n
Failed to send IER stats report (gen. %u) to Splunk: %s.\n
PFKT stats report (gen. %llu) sent to Splunk.\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
failed to collect spaceman stats: %s (%d)\n
RTCReporting framework is absent, unregistering activity\n
failed to set object cache stats report state to DEFER\n
error: unexpected format for device %s: %s (%d)\n
APFS indicates further chunks need defrag, re-starting...\n
failed to stop defrag on %s : %s\n
failed to set xpc activity state to %d (current state: %d)\n
Failed to send Cryptex stats report to Splunk: %s.\n
PFKT did not publish result for volume: %x.\n
Failed to create object cache stats dictionary\n
Failed to create devices array\n
apfs defrag is still working... (progress state: %u)\n
failed set state to DEFER\n
Failed to send IER stats report (gen. %u) to Splunk: unknown error.\n
failed to statfs root directory: %s (%d)\n
failed to truncate spaceman stats file: %s (%d)\n
DONE: completed stats report\n
key %s not added to dictionary\n
DEFERRING object cache stats report XPC activity\n
More than %llu are avaliable, no cache delete needed.\n
error: must be run as superuser\n
Failed IER status query: %s (%d). Continuing.\n
Resuming IER.\n
DEFERRING cryptex stats report XPC activity\n
IER status %d is not actionable. Exiting.\n
failed to set object cache stats report state to DONE\n
Failed to create payload dictionary\n
Failed to send object cache stats report to Splunk: unknown error.\n
error: failed to allocate set: %s (%d)\n
error: fsgetpath failed for ino %llu: %s (%d)\n
Cache Delete needs %llu\n
Cannot create dispatch queue to perform battery monitoring\n
Failed to send object cache stats report to Splunk: %s.\n
error retrieving defrag state: %s\n
Failed to create dictionary for purging.\n
Cannot create dispatch queue to perform APFS FX defrag\n
failed set state to DONE\n
Cannot create dispatch queue to perform cryptex report\n
PFKT stats report (gen. %llu) already sent to Splunk.\n
Failed to send PFKT stats report (gen. %llu) to Splunk: %s.\n
Failed to create user info dictionary\n
CacheDeletePurgeSpaceWithInfo returned no results.\n
Received kIOMessageServiceIsTerminated.\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
reporting stats from file\n
START: Initiating object cache stats report\n
defrag starting on %s\n
Cryptex stats report sent to Splunk.\n
error: failed to open container for cache eviction\n
failed set stats_report xpc activity state to DONE\n
Failed to create session info dictionary\n
Successfully purged %llu bytes.\n
Failed to query battery status: %d. Exiting.\n
DONE: Suspending object cache stats report until next interval\n
DEFERRING XPC activity on volume\n
Deferring while waiting for long-running CacheDelete purge.\n
Can't convert ProductBuildVersion to CString\n
Failed to create session info dictionary for volume: %x.\n
Failed to create payload dictionary for volume: %x.\n
PFKT result had unexpected type for volume: %x.\n
Failed to register to kIOPSNotifyTimeRemaining notifications to perform ier battery monitoring: %d\n
Cannot create dispatch queue to perform object cache report\n
defrag running for 1 hour, terminating now\n
APFS reported defrag status idle\n
RTCReporting framework is absent, not registering for IO notifications\n
Cannot find entries matching %s - %u\n
Failed to find DATA volume\n
Failed to create user info dictionary for volume: %x.\n
object cache stats for container %s not added to dictionary\n
setupCacheDelete returned %d\n
DEFERRING: stopped defrag on %s\n
CacheDeletePurgeSpaceWithInfo failed!\n
Failed to get RunLoopSource\n
IER stats report (gen. %u) sent to Splunk.\n
failed to parse spaceman stats file: %s (%d)\n
%s event was %s\n
IER status: %d, percent: %d, is_charging: %d.\n
Pausing IER.\n
Successfully sent object cache stats report to Splunk.\n
error: failed to get graft info: %s (%d)\n
failed to set cryptex stats report state to DEFER\n
Unknown PFKT stats version: %llu\n
Failed to send object cache stats report to Splunk: unknown error (missing description).\n
can't initiate defrag on %s : %s\n
DONE: Suspending cryptex stats report until next interval\n
failed to set cryptex stats report state to DONE\n
Failed to send Cryptex stats report to Splunk: unknown error.\n
Successfully registered for io notifications\n
triggering eviction for keys cache %s\n
failed to create xpc dictionary\n
error: failed to fetch stats for device %s: %s (%d)\n
build version has not changed, do not send report\n
build version has changed to %s\n
get_graft_lut_reduction failed with error %s(%d)\n
Failed to create Notification Port\n
cache eviction XPC activity complete\n
reporting stats from live container\n
Failed to collect object cache stats: %s (%d)\n
DONE: Suspending defrag until next interval\n
```
