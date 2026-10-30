# `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

From the upgrade restore ramdisk (141-29011-104.dmg). 487,312 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2112)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
```

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression (compatibility version 1.0.0, current version 182.40.4)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.sep.ramdisk</key>
	<true/>
	<key>com.apple.container.crypto.io</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.devicebackup</key>
	<true/>
	<key>com.apple.private.apfs.create-sealed-snapshot</key>
	<true/>
	<key>com.apple.private.apfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.apfs.get-dstreams</key>
	<true/>
	<key>com.apple.private.apfs.get-file-exts</key>
	<true/>
	<key>com.apple.private.apfs.revert-to-snapshot</key>
	<true/>
	<key>com.apple.private.iopol.case_sensitivity</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.system-async-io</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.move-data-extents</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>
```

## Strings (1,295)

```
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
resource fork size
nx_checkpoint_load_data
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
attr tag
APFS_INODES
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
 out-of-line data size: %llu alloced_size %llu
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
full clone size
prevent_synthetic_object_operation
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
nx_reaper_add_ext
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
jobj_validate_large_key_val
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: %s unable to get doc-id tree: %d\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s prev doc-id tree sanity check failed: %d\n
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
obj_cache_flush_prepare
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
nx_tx_wait
apfs-flags-lock
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s couldn't read superblock of size %d\n
obj_alloc
spaceman_decrement_free_queue_count
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
%s:%d: failed to stat img4 file: %s (%d)\n
%s:%d: %s failed to remove first, error %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
asv_read_data_from_extent
asv_save_compressed_inode_num
supplemental_tree_get
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
APFS_BTREE_NODES
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
committmpcp
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s tx_leave failed: %d\n
nx_checkpoint_find_highest_xid
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
physical object dirty count underflow\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
groupquota
%s:%d: ***: unknown obj type %d\n
nx_unblock_physical_range
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
object-cache-flush-lock
%s:%d: %s chunk %lld recent zone count overflow\n
nx_tx_wait_frozen
%s:%d: %s failed to enter tx - %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
%s:%d: %s ***: expanded type seen on in-memory obj\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
strictatime
Checking snapshot with transaction %llu\n
 :: %s {flags: 0x%x data-len: %u
%s:%d: Duplicate entry for inode %lld\n
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
lookup_jobj_ext
check_stale_doc_id_index
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s error searching snapshot tree: %d\n
purgeable size
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
tx_flush
%s:%d: %s xid %lld second sync/barrier failed: %d\n
%s:%d: failed to open img4 file: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
%s:%d: %s spaceman cab count is bad: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
spaceman_chunk_zone_info_recent_increment
Name for id %llu not found
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
nx_check_reaper
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
%s:%d: unlock == 0 failed %d\n
btree_check_recent_sanity
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
nx_check
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
invalid crypto index %d\n
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
invalid unlock flags: 0x%x\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
IOBlockStorageDevice
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
%s:%d: graft with invalid fs block size: %u\n
spaceman_upgrade_sm_version_0_to_1
%s:%d: %s chunk %lld recent zone count underflow\n
apfs-pfkur-tree-oid-lock
%s:%d: can't get block count (%s)\n
num children
match_jobj_expanded_type_to_tree_type
nx-tree-node-compact-lock
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: using 16k root hash\n
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
exp-dir-stats
%s:%d: %s failed to find valid checkpoint: %d\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
dev_init
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
fd_dev_read_helper
nx_reaper_add_sub_object
spaceman_get_metazone_alloc_index
%s:%d: %s container block size too small for device block size (%d < %d)\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
  values: %9s %9s %9s %9s %9s %9s\n
mark_doc_id_index_for_rebuild_if_needed
nx_reaper_next_record
%s:%d: %s Couldn't rename snap %llx to %s\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
spaceman_chunk_zone_info_compare
nx_tx_wait_closed_prev_flushing
%s:%d: Inode %lld has inline compressed data of type: %u\n
spaceman_fxc_tree_node_recycle_smallest
jobj_merge_maybe_clamp_64
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s doc-id tree sanity check failed: %d\n
new address mismatch on redirty 0x%llx 0x%llx\n
invalid filesystem index (%ld) for %s
asv_mount_container
%s:%d: Cannot allocate memory to track excessive space allocations in data stream %lld\n
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
nx_tx_wait_closed
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: don't know how to merge refcounts on objects of type %d\n
spaceman_ip_bm_block_free
nx-omap-lock
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
unexpected storagetype: 0x%x\n
usage: %s [options] <volume_path>\n
MODVAL
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s Unaligned file extent %lld in the data stream %lld\n
obj_checksum_verify_phys
nx_checkpoint_traverse
%s:%d: %s unable to get fs object 0x%llx: %d\n
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
dev_init_common
BSD Minor
jobj_size_for_large_key_val
%s:%d: %s spaceman chunks per cib is bad: %d\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
spaceman-lock
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
apfs
make_jkey_from_jobj
bad pext.\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
spaceman-czic-lock
}
apfs_reap_snapshots
btree_node_reap
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
nx_mount
obj_delete_and_free_by_oid
Cannot get filesystem superblock for snapshot %lld
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s set cloneinfo_id_epoch to %llu\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
btree_iterate_nodes
obj_read
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s failed to get reap list tail: %d\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
tx_mgr_free_tx
/dev/r
%s:%d: %s error unreserving space, %lld blocks: %d\n
obj_cache_remove_reverted_fs_objects
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%s:%d: %s Cannot allocate %lld bytes to validate hash record at offset %lld in data stream %lld\n
obj_modify
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
spaceman_freed
%s:%d: %s %lld:%lld error: %d\n
sanity_check_alloced_blocks
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
spaceman_check_allocation_status_internal
large_key_val_to_jobj
nx_reaper_obj_get
%s:%d: %s failed to get object oid %lld: %d\n
nx_check_recent_sanity
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
%s:%d: %s failed to get omap tree for reaping: %d\n
btree_node_space_stats
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
atime
validate_hash_of_record
apfs-global-lock
bt_remove_internal
bt_update_last_leaf
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
spaceman_free_extent_cache_setup
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
obj_delete_internal
spaceman_fs_bounds_clear
Cannot extract root node digest out of %s
%s:%d: Cannot find volume %s\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
spaceman_ip_block_alloc
%s:%d: Cannot mount container on %s - %s(%d)\n
%s:%d: %s large key size (%u) on record (%llu) is too small\n
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%s:%d: wrlock == 0 failed %d\n
%s:%d: Duplicate entry for data stream %lld\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
level %d: %d nodes %.2f average descendents\n
apfs_mount_livefs
can't have a negative refcnt on crypto state %llu refcnt %d\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: %s Unaligned offset %lld in the hash record of data stream %lld\n
%s:%d: *** unknown obj type %d\n
RR_HOLE
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
%s:%d: %s obj_modify() failed: %d\n
spaceman_metazone_init
main
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
%s:%d: unexpected payload type length : %d\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
spaceman_trim_free_blocks
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: %s failed to delete mapping, error: %d\n
%s:%d: %s unable to get prev doc-id tree: %d\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
read_data_for_hash_record
Removable
%s:%d: %s Deleted the shadow_fs_root tree %p\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
demomode
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s unable to get snap meta tree %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s tx xid %lld took %lld us to flush\n
%s:%d: Unsupported offline AppleFSCompression extended attribute for inode %lld\n
ino-lock
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
fext_collector
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
spaceman_chunk_zone_info_recent_decrement
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s unable to get fs root tree: %d\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
nx_mount_initiate_free_space_trims
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
auto
spaceman_free_extent_cache_remove
btree_node_val_range_validate
<20
val_size_for_jobj
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
obj_cache_remove_new_fs_objects
Cannot find snapshot with transaction %llu
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
%s:%d: %s error getting mapping tree: %d\n
spaceman_modify_bits
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
fs_rename_snapshot
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
obj_checkpoint_done
,
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
apfs-global-snap-lock
bt_insert
MODKEY
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
<100
%s:%d: %s unable to allocate chunk zone info cache\n
btree_node_insert_internal
Encrypted
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s X %d\n
%s:%d: %s object type 0x%x not reapable?: %d\n
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
%s:%d: %s omap tree sanity check failed: %d\n
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
obj_destroy_complete
rw
skipsanity
tx_checkpoint_write
%s:%d: DANGER! got the same extent for logical addr %lld twice!\n
APFS_4K_OBJS
%s:%d: %s found mapping tree with old subtype\n
spaceman_checkpoint_traverse
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
suid
io_get_num_device_blocks
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
%s:%d: %s xid %lld sync/barrier failed: %d\n
fs_tx_enter_internal
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
spaceman_fq_tree_find_overlap
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
%s:%d: %s fs_update_snap_metadata() returned %d\n
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
%s:%d: %s Invalid reap list free entry %d\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
spaceman-ip-lock
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
com.apple.ResourceFork
%s:%d: Cannot allocate mempry to track state of inode %lld with compressed flag set\n
authapfs_select_root_hash
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
AppleAPFSContainerScheme
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
key_val_to_jobj
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
btree_node_key_range_validate
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
%s:%d: %s *** unknown expanded obj type %hhu\n
apfs-phys-ext-oid-lock
supplemental_tree_destroy
fd_dev_close
%s:%d: %s object type 0x%x not reapable: %d\n
fd_dev_write_extended
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
Failed to allocate %zu bytes
authapfs_validate_node_hash
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
_fd_dev_write
jobj_validate_key_val
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
nx_check_omap
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
 file-size: %llu alloced-size: %llu
btree_node_child_val
%s:%d: %s failed to insert fext in fext_tree: %d\n
nx-global-extent-manipulation-lock
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
tx-mgr-lock
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
owners
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
%s:%d: %s encryption type %llx unsupported\n
apfs-im-cache-lock
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s set apfs_fixup_flags to %#llx\n
nx_metadata_range_add
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
nx_tx_wait_closing
com.apple.fs.symlink
%s:%d: %s fs root tree sanity check failed: %d\n
spaceman_set_bits_in_bm
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s unable to get omap: %d\n
unable to mount APFS volume @ %s [%ld]
%ss%d:%lld
btree_node_insert
Physical Interconnect Location
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s cib %lld index %d should be %lld\n
%s:%d: %s failed to set up spaceman for demo mode: %d\n
%s:%d: %s unable to get spaceman free queue tree: %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
exec
spaceman_chunk_zone_info_add
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
nx_dev_init
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: %s failed to enter tx, error %d\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
object-cache-list-lock
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s volume's seal is broken\n
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
tx_leave
%s:%d: %s cab %d index %d should be %d\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: %s failed to fetch the fext tree (error %d)\n
clean_up_doc_id_trees_if_needed
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%s:%d: %s unable to get fs snap meta tree: %d\n
%s:%d: %s tree_delete() failed: %d\n
asv_extract_hash_blob
capacity: leaves %llu / %llu => %.2f %% used\n
\t%16p %s\n
%s:%d: unexpected payload data size: %lu != %lu\n
%s:%d: %s Error %d, reinitializing\n
apfs_free_data_blocks
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
spaceman_free_fs_deduct_block_counts
apfs_reap_extentref_blocks
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
Internal
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
clear_invalid_fixups
btree_node_free_list_entry_validate
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
virtual
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: failed to open container device %s: %s\n
%s:%d: %s tx_leave failed with error: %d\n
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
spaceman_allocation_init
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
jfs_get_tree_in_snap
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
Cannot find snapshot '%s'
apfs-dir-stats-id-lock
%s:%d: %s doc-id tree creation failed: %d\n
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
%s:%d: failed to decode img4: %d\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
<60
%s:%d: %s fext_tree_remove returned %d\n
obj_init
spaceman_alloc_fxc_scan_wait
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
%s:%d: %s Final sync/barrier failed: %d\n
doc_id_tree_invalid_crypto
jobj_to_large_key_val
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
authapfs_validate_node
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
current tx not closed/flushing?!\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
%s:%d: %s expanded record found on unsupported volume\n
%s:%d: %s is not an APFS volume\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
obj_get_async_read
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
nx_reaper_sanity_check
apfs-omap-lock
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
cst->ep_retain_count <= cst->hdr.retain_count
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
omap_destroy
spaceman-free-lock
where [options] are\n       -h             display usage\n       -v [-v]        increase verbosity\n       -d             increase APFS logging level from error to debug\n       -q             print the content of filesystem (files, folders
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
nx_corruption_detected_int
%s:%d: %s started cleaning snapshots %lld-%lld\n
nx_reap_list_sanity_check
%s:%d: %s couldn't allocate memory for superblock of size %d\n
follow
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
<%d
%s:%d: %s failed to write checkpoint map block %lld: %d\n
 {
apfs-integrity-meta-lock
%s:%d: %s failed to delete doc-id tree, error %d\n
set_cloneinfo_id_epoch
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
omap_sanity_check
spaceman_sanity_check
%s:%d: %s Trash unfinished tx xid=0x%llx\n
%s:%d: failed to map img4 file (%lld) bytes: %s (%d)\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
paddr
%s:%d: %s Inserting snap_name failed, %d\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
obj_checkpoint_known
%s:%d: %s Cannot find file extent to validate data hash at offset %lld of data stream %lld: %s(%d)\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s btree check called with non-root btree node: %d\n
createtmpcp
apfs-fext-tree-oid-lock
<80
%s/nx
removal
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
fd_dev_read_extended
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
capacity: %9d %9d %9d %9d %9d %9d\n
descendants
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
userquota
tinyobjcache
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
Name for %llu (last %llu) not found
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
nx_tx_wait_flush
apfs_create_doc_id_tree_if_needed
%s:%d: %s Hit %d looking up first snapshot\n
%s:%d: %s lookup_next_snapshot() returned %d\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
spaceman_fxtp_add_child
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
=%d
%s:%d: %s failed to load inode %lld ret %d on volume: %s\n
%s:%d: %s failed to delete prev doc-id tree, error %d\n
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
perm
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s failed to check volume's seal - %s(%d)\n
clone size
jobj_allocate
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s failed nx_check sanity: %d\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
tx_unmount
purgatory.
quarantine
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
uid/gid/mode: %u/%u/0x%x bsd_flags: 0x%x internal_flags: 0x%llx
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
spaceman_fxc_update_smallest_with_successor
%s:%d: Unknown subtype %d for file info object %lld\n
jobj_type_from_possibly_large_key
FS root scan for names has failed
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
protect
%02hhx
%s:%d: %s reverting on error: %d\n
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
/%s
%s:%d: %s failed to get child val %d of node %llu - %s(%d)\n
<40
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s unable to get fs extentref tree: %d\n
%s:%d: %s container cleanly-unmounted flag set.\n
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
%s:%d: %s failed to fetch the extentref tree (error %d)\n
blocks_in_txn
%s:%d: %s unable to get spaceman: %d\n
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
%s:%d: %s tx manager initialization failed: %d\n
Get count overflowed for object %p!\n
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
spaceman_free_extent_cache_search
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s/apfs
obj_checkpoint_get
automounted
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
Data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
apfs_release_objects
doc_id_tree_destroy
%s:%d: %s failed to fetch the integrity object (error %d)\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s omap snapshot count %d seems excessive\n
spaceman-dev-lock
%s:%d: %s not enough space to enter transaction\n
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
invalid tweak type %d\n
btree_node_child_id_update
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
total size
nx_check_superblock
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s unable to get snapshot tree: %d\n
apfs-doc-id-lock
supplemental_tree_get_descriptor
nx_metadata_fragmented_sanity_check
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
omap_find_next_snapshot_xid
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
io_get_device_features
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
Ambiguous snapshot specification - choose either name or transaction to select a snapshot
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
type = %u, req_tree != fs_root\n
make_large_jkey_header_from_jobj
object-cache-reset-lock
obj_create_internal
loadtmpcp
spaceman_chunk_zone_info_load_recent_chunks
Cannot access integrity record on volume %s
asv_process_decmpfs_xattr
%s:%d: %s Failed to get next extent: %d\n
FULL
%s:%d: %s failed to get fsys oid %lld: %d\n
omap_recent_sanity_callback
spaceman_fxc_print_stats
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
SNAP_DELETE_TXN
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
Could not initialize the NX container from %s
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
spaceman_ip_bm_block_alloc
spaceman_fq_tree_insert
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
fs_lookup_snapshot_metadata_by_xid
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
obj_cache_remove
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: %s waiting for available tx to open: xid %lld\n
%s:%d: %s omap_destroy returned %d!\n
Target Disk Mode
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s failed to compare currently available space: error %d\n
setup_demo_mode
fs_insert_snapshot_metadata
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
Release count overflowed for object %p!\n
apfs-dir-size-lock
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
%s:%d: %s find_next_snap(%llu) returned %d\n
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
tx_checkpoint_space_check
%s:%d: %s tx_finish() failed, %d\n
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
orphan_snap_check_iterator
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
rolling-stats-lock
spaceman_set_up_ip_reverse_mapping_tree
nx_tx_wait_open
check_data_hashes
%s:%d: %s failed to leave tx, error %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
jobj_to_key_val
nx-volume_group-lock
%s:%d: %s omap check failed with error: %d\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
0
%s:%d: %s snap meta tree %lld: %d\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
isys
%s:%d: %s Failed to find successor node in length tree: %d\n
btree rightmost leaf field is set for physical tree!\n
key_size_for_jobj
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
virtual object dirty count underflow\n
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: Sealing of encrypted volumes is not supported\n
apfs_sanity_check_tree_type
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
physical size
%s:%d: %s omap xid %lld > spaceman xid %lld\n
%s:%d: %s reaper has tail with no head\n
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
update
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
%s:%d: %s failed to get reap list head: %d\n
spaceman_trim_free_extent_callback
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
 embedded data size: %u
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
btree_node_seal_validate
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
Cannot validate a seal on the unsealed volume %s
authapfs_seal_break
bt_merge_up
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
apfs_sanity_check
%s:%d: %s btree node oid %lld, xid %lld: failed to validate hash of child node %d in node %lld - %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
nx_tx_flush_busy
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
sealed, fext, req_tree != fs_root
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
apfs_checkpoint_traverse
%s:%d: %s tx_enter() failed: %d\n
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
jobj_release
%s:%d: %s Shadow fs_root does not exist\n
dir-stats
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
%s:%d: %s error modifying omap: %d\n
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
%s:%d: %s Incorrect hash digest size for the hash record at offset %lld in data stream %lld: on-disk %d, expected %d\n
skipsanity,ro
spaceman_free_extent_cache_insert
BSD Major
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
%s:%d: %s Fusion is not supported anymore\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
rdonly
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
obj_cache_flush_write
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
jobj_size_for_key_val
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
spaceman_unreserve
<UNKNOWN>
%s:%d: %s extentref tree %lld: %d\n
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s waiting for transaction to finish\n
%s:%d: Inode %lld is missing its resource fork\n
%s:%d: %s failed to get doc-id tree key count, error %d\n
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
APFS_8K_OBJS
obj_cache_graft_attach
FS root scan for inodes has failed
%s:%d: %s bogus phase, %u\n
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
%s:%d: %s Cannot collect all file extent records for data stream %lld: %s(%d)\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: can't get features for device (%s)\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
apfs_reap
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
spaceman_cab_sanity_check
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
bt_lookup_copy_out
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
spaceman-space-usage-lock
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s btree_node is null\n
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
%s:%d: %s omap tree type 0x%x is bad\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
invalid offset (%llu) for last fext lookup\n
%s:%d: %s Can't get tree: %d\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
%s:%d: %s error updating metadata ranges tree: %d\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%d: Cannot get to the parent of %s\n
purgeable rsrc size
%s:%d: %s superblock failed sanity checks: %d\n
nx-txn-blocks-lock
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
%s:%d: %s failed to fix up checkpoint data: %d\n
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
obj_release
spaceman_chunk_zone_info_cache_init
AppleAPFSVolume
%s:%d: Cannot allocate memory to hold information about data stream for inode %lld\n
%s:%d: %s overprovisioning volume can only mount r/o\n
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
ephemeral
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
nx_tx_finish_wait
On disk hash does not match provided hash:\n\ton-disk:  %s\n\tprovided: %s
%s:%d: %s error getting next checkpoint data block address %d: %d\n
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
duplicate_jobj_op_to_shadow_fs_root
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: %s failed to attach graft to object cache: %d\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
nx_reaper_checkpoint_traverse
%s:%d: %s fs extentref tree sanity check failed: %d\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
bt_shift_or_split
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
btree_check_ext
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
apfs-incompat-features-lock
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
exp_dir_stats_refcnt_merge
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s:%d: %s failed to create reap list: %d\n
obj_cache_remove_graft_persistent_ephemeral
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
%s:%d: %s reap list object free list erroneously empty?\n
dev
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
apfs-clonegroup-lock-mutex
%s:%d: %s omap snapshot tree sanity check failed: %d\n
object-lock
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
obj_write_prepare
 def-prot-class: %u
btree_node_sanity_check
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
INSERT
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
%s:%d: %s Found a hole at offset %lld in the data stream %lld\n
fs_tx_leave_ext
%s:%d: %s omap checkpoint %s traverse failed: %d\n
%s:%d: device initialization failed: %d\n
%s:%d: %s tx xid %lld took %lld us to close\n
DELETE
%s:%d: %s invalid object size: %d size_phys %d\n
%s:%d: %s First sync/barrier failed: %d\n
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
com.apple.apfs.
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
UNKNOWN TXN TYPE
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
%s:%d: Unexpected AppleFSCompression extended attribute record for inode %lld\n
spaceman-fxc-lock
nx_reaper
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%ss%d
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
Processed %lld bytes of data across %lld hash records of %lld data streams\n
length
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
invalid lock flags: 0x%x\n
union
unable to mount NX container @ %s
 uncompressed size: %llu
 sparse-bytes: %llu
%s/apfs_data
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: %s failed to create doc-id tree, error %d\n
remove_jobj
nx_get_evict_mapping_tree
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
%s:%d: %s unable to get omap tree: %d\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
IOService
apfs-snap-delete-lock
%s:%d: %s object cache initialization failed: %d\n
obj_checkpoint_start
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
spaceman_clear_bits_in_bm
%s:%d: %s omap snapshot tree type 0x%x is bad\n
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
authapfs_integrity_meta_get_internal
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
apfs-phys-lock-state-mutex
obj_checksum_verify
%s:%d: object memory manager failed to create lock, error: %d\n
%s:%d: unexpected payload type: %s\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
omap_cleanup
spaceman_ip_freed
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
tx_enter_internal
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
    keys: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
omap_reap
/dev/
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: %s Tree delete oid %llu threw %d\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
Attempting to reuse a non-candidate chunk zone info\n
%s:%d: %s Error reinitializing free extent cache: %d\n
gbitmap_reap
fs_get_inode_with_hint
obj_mem_mgr_init
spaceman_iterate_free_extents_internal
%s:%d: %s unsupported tree type: %d\n
%s:%d: %s mount for ramdisk\n
%s:%d: %s object cache bootstrap failed: %d\n
Reference count overflowed for object %p!\n
%s:%d: %s unsupported tree type, %d\n
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%lld errors detected\n
assertion failed: %s
%s:%d: %s failed to write superblock to block 0: %d\n
%s:%d: %s spaceman chunk count is bad: %lld\n
obj_checkpoint_check_for_unknown
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
%s:%d: Cannot get index of the volume %s\n
APFS_TREE_LOOKUP_ZONE
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
defwrite
not handling the flushing tx!\n
%s:%d: %s Missing file extent at offset %lld in data stream %lld, next extent starts at offset %lld\n
apfs_mount
%s%s%llx
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
btree_delete
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
START
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
IOMedia
fs_destroy_shadow_fs_root_tree
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
%s:%d: %s Error: tx[%lld] failed to start: %d\n
%s:%d: %s failed to get omap %lld: %d\n
level %d: %d nodes\n
%s:%d: %s spaceman IP base address is bad: %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
io_get_device_block_size
nx-resize-spaceman-lock
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s couldn't allocate memory for checkpoint map block\n
tx_finish
hqvdPo:I:x:s:
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
FIXUP
spaceman_alloc_iterate_chunks
curproc
jobj_refcnt_merge
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s failed to clean up doc-id trees, error %d\n
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
unknown option: %s
Compressed data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
%s:%d: using 8k root hash\n
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
obj-id %llu type %u still has refcount %d\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj.c
ino_set_rage
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
btree_node_compact
insert_jobj
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s tx_enter_frozen() failed: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
not handling the current tx!\n
ino-io-lock
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
apfs-snapmeta-oid-lock
!((apfs)->apfs_main_apfs != ((void*)0))
%s:%d: failed to open volume device %s: %s\n
%s:%d: reaper thread is exiting, returning EBUSY\n
spaceman_free_completed
%s:%d: %s created doc-id tree, oid %llu\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
%s:%d: %s Inserting snap_meta failed, %d\n
nx_tx_finish_wait_for_dirty_data
cst %llu hit zero retain count but still has ep related retain count (%u)\n
image-format-read-only
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
object-cache-lock
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
move_snapshot_to_purgatory
%s:%d: %s reaper check failed with error: %d\n
spaceman_free
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: %s failed to get doc-id tree, error %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
BSD Name
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
browse
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: %s spaceman cib count is bad: %d\n
nx_checkpoint_find_valid_checkpoint
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
i40@?0q8Q16^v24^Q32
apfs-stream-id-lock
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s rapid-aged %llu inodes\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%d: %s Not enough room in the extent for %lld bytes at offset %lld in data stream %lld to read %lld bytes\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
Protocol Characteristics
total_count
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
Checked %lld bytes%s at offset %lld of data stream %lld\n
Reference count underflowed for object %p!\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s Hash mismatch for %lld bytes at offset %lld in data stream %lld\n
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: %s iter_next returned %d\n
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
%s:%d: %s error getting cab %d @ %lld: %d\n
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
spaceman_sanitize_datazones
%s:%d: %s Cannot read %lld bytes at physical block %lld which corresponds to offset %lld of data stream %lld: %s(%d)\n
btree_node_check
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
addition
%s:%d: %s cab %d cib count %d should be %d\n
nx_check_recent_sanity_omap
nx_check_checkpoint_map_block
nx_superblock_agrees_with_container_superblock
asv_process_rsrc_xattr
%s:%d: obj is NULL or not apfs object!\n
doc_id_tree_create
spaceman_free_extent_cache_reset
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
apfs-rename-lock
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
Device Characteristics
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
nx_metadata_range_optimize
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
btree_node_entry_update
bt_merge_nodes
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
spaceman_cib_sanity_check
spaceman-czic-scan-lock
 of uncompressed data
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
spaceman_get_new_chunk_for_allocation_zone
spaceman_chunk_zone_info_list_remove
%s:%d: rdlock == 0 failed %d\n
%s:%d: Unexpected size of extended attribute record for inode %lld: expected %zd, got %d\n
authapfs_valid_hash_type
%s:%d: %s failed to initialize free extent cache, error %d\n
btree_node_debug_stats
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
obj-mem-mgr-lock
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
checkpoint
spaceman_alloc
%s:%d: %s failed to get child %d of node %llu - %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
ro
spaceman_fxc_update_length
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
Reserved space < reserved metadata: %llu < %llu\n
xsys
%s:%d: Inode %lld has both resource fork with data stream %lld and compressed data in extended attribute\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
```
