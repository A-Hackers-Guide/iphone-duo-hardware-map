# `/System/Library/Filesystems/apfs.fs/apfs_migrator`

From the upgrade restore ramdisk (141-29011-104.dmg). 855,440 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2288)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
```

## Linked libraries (5)

- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
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

## Strings (2,625)

First 2,500 of 2,625.
```
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
splitter_dump_clonegroups
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
%@data_size_hardlnks=%llu 
%s:%u Err: VFC conversion failed with %u\n
\tFinal      : %u/%u, delta: %+lli/%+lli\n
%ss%d:%lld
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: *** Unknown file info type %llu\n
%s:%u Err: insert_purgeable_record failed for source inode: %u\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
supplemental_tree_create
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
spaceman-czic-scan-lock
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
%s:%d: %s could not unwrap crypto-id %lld (err %d)\n
obj_release
MoveDrecToRoot
%s:%u Err: walk_file_extents (AnalyzeFext) for DS %llu failed: %u\n
IOBlockStorageDriver
%s:%d: %s sm_fs_reserve_alloc_count underflow, sm_fs_reserve_alloc_count %lld, new fs_reserve_block_count %lld, old fs_reserve_block_count %lld alloc_count %lld\n
SnapName
%s:%d: %s Failed to create purgeable record (drec) for lookup (ino %llu): %d (%s)\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
omap_find_next_snapshot_xid
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
%s:%d: %s set cloneinfo_id_epoch to %llu\n
%@purge_from_data=%llu 
\tTotal delta: %.02f%%/%.02f%%\n
%s:%d: %s fs tree type 0x%x invalid, using virtual btree instead\n
%@purge_full=%llu 
= Move namespace\n
%s:%d: %s obj_create failed - %d\n
MoverBase_PostMove_iterate_jobjs
ROOT has DirStats (ID: %llu), removing...\n
MoverBase_Remove
%s:%d: %s large key size (%u) on record (%llu) is too small\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
%@data_size_fclones=%llu 
%s:%d: %s failed to get omap tree for reaping: %d\n
%s:%u Err: Inner namespace scan failed for [%s]: %u\n
Mover_OnCryptoId
VOL_CPROTECTED
%@src_fsroot_depth=%llu 
IOBlockStorageDevice
unwritten
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%u: Setting timeout to extra %u seconds starting from this point (+%u:%02u)\n
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
clean_up_doc_id_trees_if_needed
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
extend_timeout
Mover_OnXattr
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
SYSTEM_GRAFT_4K_OBJS
nx_metadata_range_optimize
%s:%u: User volume passed for v1->v2 migration, swapping to use Data volume @ index [%u] as source and User volume @ index [%u] as target\n
Features:\n
%s:%d: %s this volume requires valid UUID option specified\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
Preprocessor_ScanDstreams_iterate_jobjs
+TMP
\tAPFS_FEATURE_VOLGRP_SYSTEM_INO_SPACE
%s:%d: %s failed to clean up doc-id trees, error %d\n
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
\t\t\tReplacing fext range [%llu - %llu] (%llu) for DS %llu\n
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
Internal
%s:%d: %s extentref tree type 0x%x invalid, using physical btree instead\n
io_get_volume_uuid
Preprocessor_AnalyzeFext
Incompat:
%s:%d: %s no space for a new file system (slot %d, max %d)\n
%@dev=%s result=%d 
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%u Err: fts_open() for %s failed with %u\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
nx_superblock_agrees_with_container_superblock
spaceman-space-usage-lock
%s:%d: %s failed to increment crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
j_sibling_link_t.sibling_id
61706673-7575-6964-02c0-766f6c756d00
key_size_for_jobj
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
bad pext.\n
%s:%u Err: Fatal: Free space is projected to be below the min free blocks for rootfs (%lli <= %u) after flush\n
 [Data: %llu / User: %llu]
iDiags
%s:%d: %s error updating snapshot tree: %d\n
%s:%u Err: dev_init %s failed with %u\n
spaceman_alloc_fxc_scan_wait
decode
after mount
APP FILE 
filter_purgeable_flags_for_vol
PurgeableTombstone
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
assertion failed: %s
fs_obj_create_name_checked
obj_cache_graft_attach
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
nx_reaper_checkpoint_traverse
%s:%d: %s omap tree sanity check failed: %d\n
union
ephemeral
nx_corruption_detected_int
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s: no tree\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s failed to create doc-id tree, error %d\n
INSERT
= Create clonegroups
%s:%u Err: MoveCryptoId for xattr cryptoId %llu failed: %u\n
AppleAPFSMedia
%s:%d: %s error getting cib %d @ %lld: %d\n
SiblingMap
__apfs_dec_parent_nlink
%s:%u Err: Flush failed with %u\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
spaceman_metazone_init
%s:%u Err: Overflow: 0x%llx + 0x%llx == 0x%llx\n
\tAPFS_FEATURE_STRICTATIME
%s:%d: %s spaceman_alloc() FAILED, err: %d xid: %lld paddr: %lld blocks requested: %lld blocks allocated: %lld\n
%@max_stack=%zu 
\tXattr DS #%llu\n
%s:%d: %s Coludn't remove dir stats key from (group:%llu inum:%llu priv_id:%llu): %s\n
protect
\tAPFS_FEATURE_VOLGRP_SYSTEM_INO_SPACE\n
Trying to update a namedstream inode %llx on volume %s\n
Target volume encryption type: 
Would return EALREADY if no changes were made (dry run mode was enabled or volume(s) already migrated)
nx_check_superblock
%s:%d: %s omap snapshot tree sanity check failed: %d\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
tx_leave
%s: %10llu records in %8llu nodes, %4llu depth, approx size: 
%s:%d: %s mount for ramdisk\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
Metrics: %s\n
%s:%u Err: Failed to update ROOT ino: %u\n
%s:%d: %s failed to get reap list head: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj.c
%s:%u Err: Timeout exceeded during ClonegroupFinder stage\n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s cab %d index %d should be %d\n
exec
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s fs root tree creation failed: %d\n
\t\t\tRemove old siblink %llu from drec #%llu [%s] -> ino #%llu\n
%s:%u Err: create_sibling_link failed for ino #%llu, drec #%llu [%s]: %u\n
apfs_reap
jdev_fext_read_data
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
spaceman_free_extent_cache_remove
spaceman_fxtp_add_child
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s xid %lld second sync/barrier failed: %d\n
BinLog map size: %zu entries\n                 %zu bytes\n       written : %llu bytes\n
%s:%d: %s Quota %llu is smaller than reserve %llu\n
sealed, fext, req_tree != fs_root
invalid lock flags: 0x%x\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
Shared clones filenames:
%s:%u: Generated a merged extentref tree with %llu pexts in %llu blocks\n
%s:%u Err: inode (%llu) dstream size (%llu) != previously recorded (%llu) from ino (%llu)\n
Trying to freeze [%s]\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s:%u Err: Timeout exceeded during Preprocessing stage\n
authapfs_integrity_meta_get_internal
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s allocated unwritten file extents are now supported\n
purgeable size
Release count overflowed for object %p!\n
ScanFext
 (readonly)
init_dir_stats_xfields
supplemental_tree_get_descriptor
rolling-stats-lock
jobj_refcnt_merge
%s:%u Err: Timeout exceeded during Clonegroups creation stage\n
%s:%d: %s Failed to set purgeable drec's dir gen-count: error %d\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s failed insert (group:%llu inum:%llu priv_id:%llu) err:%s\n
spaceman_chunk_zone_info_list_remove
tx_flush
\t%s : 
%s:%d: %s Encrypted volume is not allowed with special role = 0X%x\n
%s:%d: %s cannot insert file extent record for extent of %lld bytes at offset %lld of data stream %lld in transaction %lld: %s(%d)\n
%s:%d: %s failed to restore orig_fext, ino %llu, pbn 0x%llx, laddr 0x%llx, len %llu, crypto_id %llu, error %d\n
%s:%d: %s failed to free allocated blocks, ino %llu, 0x%llx+%llu, error %d\n
nx-tree-node-compact-lock
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
kern.osreleasetype == [%s]\n
%s:%u Err: apfs_update_phys_range (%llu, %llu, +1) failed with %u\n
APFS_4K_OBJS
\tAPFS_FEATURE_HARDLINK_MAP_RECORDS\n
sanity_check_alloced_blocks
%s:%u Err: Failed to increment refcount for dstream id %llu of the source inode: %d\n
%s:%d: %s error updating chained key for calculating dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
MoverBase_OnPurgeDrec
jobj_to_large_key_val
%@num_files=%zu 
Using fallback path\n
Source volume encryption type: 
/.DocumentRevisions-V100
%s:%u Err: apfs_update_phys_range (%llu, %llu, -1) failed with %u\n
< ??? >
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
spaceman_trim_free_extent_callback
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
btree rightmost leaf mismatch! (expected %lld found %lld)\n
demomode
tx_unmount
Requested forced secondary_fs_root but the tree is missing\n
DirRecord
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
ObjCache max size is set to %u objects 
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s Failed to find successor node in length tree: %d\n
Preprocessor_ProcessDstreams
%s:%d: Volume role 0x%x is not supported
===============================\n= Pre-processing dstreams%s\n===============================\n
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
dropCloneMapping
ProcessFexts
%s:%d: %s updating grandparent failed w/%d\n
%s:%u Err: Failed to get target apfs object oid %llu: %u\n
spaceman_ip_bm_block_free
%s:%u Err: Failed to insert new purgeable record on %s, ino %llu dstream %llu - file ID didn't match; new %llu != old %llu\n
%s\n
%s:%u Warn: update_jobj after apfs_clonegroup_insert_inode failed for ino %llu: %u\n
%s:%d: %s crypto_obj_insert of new crypto_id %lld should not have failed (ret %d)\n
UpdateInoMap
doc_id_tree_destroy
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
Protocol Characteristics
nx_tx_wait_closing
fd_dev_close
%s:%d: %s fext_tree_remove returned %d\n
... Can't find a purgeable inode for purgeable drec on either source or target - removing purgeable drec %llu\n
%@tmp_cloned_blk=%llu 
%@src_fsroot_nodes=%llu 
%llu/%llu %llu%%\r
%s:%u Err: Unable to determine memory size, assuming the worst\n
%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
%s:%u Err: eAPFS versions are different on source (v%u) and target (v%u)\n
Flush
CryptoID refs:
nx_mount
%s:%u Err: Inner scan has failed, most likely we ran out of memory\n
         oc_phys_dirty_count: %16llu\t(~%8llu MB)\n
Moving folder %s -> %s\n
%s:%u: Would be loading regular checkpoint\n
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
%s:%u Err: Parent dir ino (%llu) is missing for cloned ino %llu->%llu\n
v8@?0
Preprocessor_UpdateDsMap
%s:%u Err: remove_jobj for j_clone_mapping_t failed: %u\n
update_size_tracking_no_gencount_bump
%s:%d: %s failed to set dir stats key for <%llu, %llu> clone mapping, error %d\n
spaceman_fxc_update_smallest_with_successor
%s:%d: Unable to parse volume UUID, err = %d\n
MoverBase_ReplaceDirStats
%s:%u Err: remove_jobj for %s from 1st tree failed: %u\n
%s:%d: %s unsupported tree type, %d\n
%s:%u Err: FreeQ flushing: spaceman_drain_free_queues failed with %u\n
%s:%d: %s failed to fetch the extentref tree (error %d)\n
%s:%d: %s FS will NOT have extended vek protection classes\n
btree_node_insert
iOS version\n
\tMove dirstats for Source Ino %llu from dir %llu to dir %llu, if any\n
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
%s:%u Warn: Purgeable drec for ino %llu is of kind %u, and not KIND_NEW\n
convert
%s:%u Err: Failed to remove dir drec from source path: %u\n
Statistics
Bytes (Read)
%s:%d: %s failed to delete fs root tree after fs creation failed: %d\n
%s:%u Err: Failed to create a merge extentRef tree: %u\n
get_dir_stats
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
\tAPFS_INCOMPAT_EXTENDED_VEK_CLASSES\n
reserved_82
IODeviceTree:/filesystems
%s:%d: %s Volume inconsistency detected by %s:%u!\n
%@prepro_t=%llu 
%@freeQ_d=%lld 
%s:%u Warn: [%s] inode (%llu) has INODE_DIR_STATS_ORIGIN but no INO_EXT_TYPE_DIR_STATS_KEY XF\n
sha3_512_4k
obj_checkpoint_start
Merge snapshots
CryptoID refs:\n
%s:%u Err: reference_phys_range %llu, %llu bytes failed: %u\n
dir_stats_move_origin
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
phys footprint    
Mover_MoveDrec_Rehashing
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
%s:%d: %s failed to compare currently available space: error %d\n
FIXUP
%s:%d: %s waiting for transaction to finish\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
obj-id %llu type %u still has refcount %d\n
physical size
%s:%u Err: Can't find DSID (%llu) for LBA [%llu - %llu] (%llu) counts %u/%u in sharedClonesMap\n
%s:%d: obj is NULL or not apfs object!\n
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
Clonegroup tree has been created, OID %llx\n
Any
authapfs_integrity_meta_create
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
apfs_reap_extentref_blocks
  values: %9s %9s %9s %9s %9s %9s\n
Preprocessor_ScanFext
%s:%u Err: Dir %llu flagged as dir-stats-origin but has no dir-size key!\n
%s:%d: %s invalid object size: %d size_phys %d\n
spaceman-fxc-lock
IOMatchCategory
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
ScanXattr
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
skipsanity
apfs_migrator
%s:%d: *** Can't allocate unknown obj type %d\n
Hardlinks              : %zu\n
dir_stats_move_regular_origin
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
kern.osversion
%s:%u Err: FreeQ flushing: tx_leave failed with %u\n
after preprocessor
lookup_purgeable_drec
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
Total Time (Read)
apfs-incompat-features-lock
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s Failed to release reference to crypto ID %lld for data stream %lld: %s(%d)\n
obj_checksum_verify
%s:%u Err: Failed to assign new parent and name to source inode : %u\n
\t\t\tAdd siblink %llu to drec %llu [%s]\n
%s:%d: %s find_next_snap(%llu) returned %d\n
empty_password
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s failed to extend existing extent %lld:%lld of inode %lld: %s(%d)\n
Our PID is %u\n
bt_insert
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%u Err: Inner namespace scan failed after multiple retries: %u\n
%s:%u Err: Failed to create a new volume @ %s [%u]: %u\n
+APP
%s:%u Err: Parent ino (%llu) is missing for source ino %llu \n
update_dir_stats
Detected IOCTL as 0x%lx (%zu)\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
CloneHardlink
jobj_size_for_large_key_val
fs_make_phys_range_writable
%s:%u Err: Failed to add PURGEABLE_EXT_TYPE_DIR_GEN_COUNT XF into PurgeRec for ino %llu into %s: %u\n
%@num_cg=%zu 
Final     target fs_root
%s:%d: %s Hit %d looking up first snapshot\n
%s (%s)
splitter_dump
Total Time (Write)
!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))
Reference count underflowed for object %p!\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
Scanning inodes, expected to see %llu\n
btree_node_entry_update
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
%s:%d: locking id %llu, which is already locked by this thread\n
%@encoded_len=%zu 
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
61706673-7575-6964-0240-766f6c756d00
%s:%d: %s waiting for available tx to open: xid %lld\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
\t\tDS not found
%ss%d
apfs-flags-lock
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: %s failed to increment the refcount for pext %lld, %s (%d)\n
%@fl=%d
.app/
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
Preprocessor_ScanXattr_walk_file_extents
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s failed to enter tx, error %d\n
jobj_allocate
0x%llx-0x%*llx:%u
\t\tRelinked drec #%llu [%s] to ino #%llu\n
Before draining freeQs
spaceman_cib_sanity_check
%02hhx
spaceman_unreserve
%@purge_from_user=%llu 
\tDS #%llu ref %u\n
%s:%u Err: Failed to insert new value into renumber map\n
%s:%d: %s bogus phase, %u\n
nx-global-extent-manipulation-lock
unwritten=no
%s:%d: %s tx_finish() failed, %d\n
createtmpcp
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
apfs_clonegroup_update_locked
%s:%d: can't get block count (%s)\n
reserved_78
%s:%u Err: clone_mapping_add_ino failed for ino %llu: %u\n
%s:%u Err: MoveCryptoId for cryptoId %llu failed: %u\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
%s:%d: %s dir-stats %llu maintains purgeable rsrc size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
\tAPFS_INCOMPAT_EXPANDED_RECORDS\n
%s:%d: %s object cache initialization failed: %d\n
VOL_UNENCRYPTED\n
\tAPFS_INCOMPAT_ENC_ROLLED\n
%s:%d: %s clonegroups enabled for this volume\n
lookup_purgeable_drec_as_record
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
%s:%d: %s unsupported tree type: %d\n
nx_tx_flush_busy
%s:%u Err: Failed to add live view extentRef tree: %u\n
apfs-global-lock
Size
reserved_79
jobj_size_for_key_val
%s:%u: Setting timeout to %llu seconds (%llu:%02llu)\n
make_purgeable_drec_xfs_from_record
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
CryptoState
%@ever_cloned=%llu 
%s:%u Err: Name collision detected after normalization [%s] -> ino #%llu collides with [%s] -> ino #%llu\n
%s:%d: %s Failed to lookup purgeable drec (id %llu): error %d\n
IOMedia
%s:%d: %s Inserting snap_name failed, %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
Available now
\tAPFS_CONFORMANCE_FORMAT
%s:%d: wrlock == 0 failed %d\n
%s:%d: %s failed inserting hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
exp-dir-stats
%s:%u Err: update_jobj for j_inode_t %llu into source failed: %u\n
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s Failed to set purgeable rec's dir gen-count: error %d\n
spaceman_fxc_update_length
=======================\nStages timing:
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%@max_mem=%llu 
%s:%d: %s unable to get reaper: %d\n
apfs_clonegroup_lock
xART
nx_checkpoint_load_data
%s:%u Err: unable to mount NX container @ %s\n
===============================\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
update_size_tracking
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%u Err: Abort requested\n
%s:%u Err: Source and target volumes cannot be the same\n
we asked for %lld blocks but got %lld (orig %lld, blks_this_allocation %lld)\n
ino
Move extras
com.apple.apfs.
none
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
apfs-stream-id-lock
%s:%d: %s object type 0x%x not reapable?: %d\n
%s:%d: %s couldn't remove (group:%llu inum:%llu priv_id:%llu) err:%s\n
removal
%s:%d: %s FS will NOT be encrypted.\n
after PostMove
dumpCore
apfsuuid
sha3_384
fsquota=
spaceman_sanitize_datazones
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
Preprocessor_CloneFext
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
Physical Interconnect Location
spaceman_allocation_init
+1
%s:%u Err: Failed to mount target APFS volume @ %s [%u], error %u\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
make_large_jkey_header_from_jobj
%s:%d: %s Couldn't get active extentref tree, err=%d\n
%@mnt_t=%llu 
lookup_expanded_purgeable_record
%s:%d: %s failed to update rightmost leaf field: %d\n
jdev_fext_write_data() corrupts encrypted data
%s:%d: %s failed updating hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld\n
%s:%d: %s Failed to insert purgeable record (record): %d (%s)\n
61706673-7575-6964-0000-766f6c756d00
Metadata Size (estimated)   : %16llu\t(~%8llu MB)\n
Mover_OnInode_iterate_jobjs
reserved_81
             Time  : %15llu %16.3f Bps %16.3f MBps\n
%s:%d: %s clonegroup tree creation failed: %s\n
%s:%u Err: doc_id_tree_insert failed with %u for docId %u inode %llu\n
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
%s:%u Err: Outer scan has failed, most likely we ran out of memory\n
%s:%u Err: Unable to find uuid of source volume, err = %d\n
%s:%u Err: New volume @ %s [%u] has different index (%u) after apfs_newfs\n
modification
%s:%d: %s ino %lld file extent %lld:%lld extends beyond alloced_size %lld (fsize %lld). fixing it.\n
VM
%@source_meta_size=%llu 
AnalyzeXattr
%s:%u Err: FreeQ flushing: tx_enter failed with %u\n
uuid_from_role
Iterator_ProcessDrec
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%@findcg_t=%llu 
%s:%u Err: CryptoIncRef failed with: %u\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
%s:%d: Why are we comparing a chunk to itself?\n
Reserved Data
         Hits               : %16llu\t(~%8llu MB)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
Silent mode enabled, only splitter errors and warnings would be printed. Note: this doesn't affect messages from the core APFS.
%s:%d: %s Failed to find host inode (id %llu) for purgeable drec lookup, falling back to ino %llu\n
cst->ep_retain_count <= cst->hdr.retain_count
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu): %s\n
conformance
%s:%u Err: ProcessFile failed for %s: %u\n
%s:%u Err: walk_file_extents for DS %llu failed: %u\n
%s:%d: %s couldn't get clonegroup tree err:%s\n
not handling the flushing tx!\n
legacy_get_ek
%@msu_shared_clone_blk=%llu 
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
Mover_OnInode_DocId
type = %u, req_tree != fs_root\n
update_jobj
total size
extentref.owner_id
spaceman-czic-lock
%s:%d: Splitter cache size is zero\n
%s:%u Err: Failed to move %s -> %s: %u\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
\nCan't find string #%llu\n
%s:%u Err: Offset mismatch: %llu != %llu\n
%s:%u Err: Iteration failed: %u\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
%s:%u Err: fsctl(APFSIOC_DEBUG_STATS) failed for dstream of %s : %u\n
reserved_74
\nFailed to read string, %llu bytes\n
spaceman_fxc_print_stats
%s:%d: %s btree_node_key_update failed: %d\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n
... Removing Inode for %llu\n
orphan_snap_check_iterator
nx_reaper_obj_get
nx_check_recent_sanity
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
tx_mgr_free_tx
%s:%d: %s failed to remove head_fext, ino %llu, laddr 0x%llx, error %d\n
Processed %zu/%llu inodes, recorded %zu shared ranges\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%s:%u Err: iterate_jobjs failed with %u\n
w:
nx_tx_finish_wait
Group #%llu (%zu inodes)\n\t
nx_get_evict_mapping_tree
%s:%d: %s removal of replaced free extent failed: %d\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%u Err: Failed to clone inode %llu\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
atime
nx_tx_wait_flush
Before Dump
spaceman_free_fs_deduct_block_counts
j_inode_t
virtual
xattr_obj_id
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
%@tgt_fsroot_depth=%llu 
%s:%d: %s unable to get omap tree: %d\n
%s:%u Err: Volumes already mounted\n
... Fixing purgeable record atime on %s, ino %llu - new %llu != old %llu\n
%@decloned=%llu 
0x%llx-0x%llx:%d
         Size max           : %16llu\t(~%8llu MB)\n
%s:%d: %s encryption type %llx unsupported\n
%s:%d: cannot change role of system-unique volume\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%@pure_cloned_apps_blk=%llu 
%s:%u Err: ExtentRef_GetRange (%llu, %llu) failed with %u\n
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
%s:%u Err: APFS_IOUC_VOLUME_CREATE_KEYBAG_ONLY failed with status: %x, %u\n
VOL_PFKEY
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
%@%s:%d 
%s:%u Err: Preprocessor stage scanner failed with %u\n
crypto_cache->type != CRYPTO_OBJ_TYPE_EP
%s:%u Err: Failed to get source apfs object oid %llu: %u\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
rdisk
alloc_space_for_write_with_hint_and_spino
%s:%u Err: insert_jobj failed: %u\n
\tSplitted range [%llu - %llu] (%llu) LBA [%llu - %llu] -> LBA [%llu - %llu], flags: 0x%x\n
             Bytes : %15llu %16.3f avg size\n
AppleAPFSVolume
nx-omap-lock
%s:%u Err: Failed to mount volume(s): %u\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
Found old purgeable record for ino %llu\n
Current free space              : 
Coarse approx. of metadata      : 
spaceman_fxc_tree_node_recycle_smallest
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
ObjCache Size current       : %16llu\t(~%8llu MB)\n
%s:%d: %s attribution tags are supported on this volume\n
\tFinal      : %llu, delta: %+lli\n
%s:%u Err: cp_dec_ref for cryptoId %llu has failed: %u\n
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
\tAPFS_ROCOMPAT_CLONE_MAPPING\n
xid
OnCryptoId
%s:%d: %s directory has an illegal hardlinked child (dir: %lld ; child ino %lld)\n
\nBad type: %u, %u or %u expected in msg 0x%llx offset 0x%llx\n
btree_node_val_range_validate
bt_shift_or_split
cst %llu hit zero retain count but still has ep related retain count (%u)\n
%s:%u Err: Hardlinked drec #%llu [%s] has no sibling ID\n
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%s:%u Err: tx_enter failed: %u\n
%s:%u Warn: Warning: Can't find dstream_id for ID in forced_fs_root %llu: %u\n
%s:%u Warn: apfs_clonegroup_insert_inode failed for ino %llu: %u, ignoring\n
%s:%d: %s directory has an illegal sub-directory (dir: %lld ; sub-dir ino %lld)\n
%s:%d: %s failed to initialize free extent cache, error %d\n
FULL
%s:%d: %s omap checkpoint %s traverse failed: %d\n
THAWED\n
%s:%u Err: Cannot resolve source volume path [%s]\n
mark_doc_id_index_for_rebuild_if_needed
%s:%d: %s fs private dir creation failed: %d\n
Root level files found : %zu\n
apfs-clonegroup-lock-mutex
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s expanded record found on unsupported volume\n
%s:%u: ... oid: %llu, xid: %llu, %llu pexts in %llu blocks\n
UpdateRenMap
%s:%d: %s fs root dir creation failed: %d\n
obj_cache_remove_new_fs_objects
%@total_t=%llu 
%@tmp_blk=%llu 
/mobile
APFS_BTREE_NODES
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
%s:%d: %s Failed to get fsys oid %lld - %s\n
\t\t\t\t\t... removing fext\n
%s:%u Err: fsctl(APFSIOC_DEBUG_STATS) failed for fexts of dsid %llu for %s: %u\n
fs_lookup_snapshot_metadata_by_xid
apfs_clonegroup_unlock
omap_cleanup
role=
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
spaceman_fs_bounds_clear
jobj_type_from_possibly_large_key
%s:%d: %s Cannot find extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
%s:%d: %s fs omap initialization failed: %d\n
%s:%u Err: Failed to iterate inodes: %u\n
         oc_free_count      : %16llu\t(~%8llu MB)\n
fs_tx_enter_internal
%s:%u Warn: Boot-args timeout has incorrect value: %lli, ignored\n
after Collect Clonegroups
%s:%d: %s dir-stats key %llu is busy even though we hold the inode lock\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
get_vol_crypto(apfs) == VOL_PFKEY
... Creating new purgeable record on %s, ino %llu dstream %llu size %llu\n
io_get_device_features
%s:%d: %s fs_update_snap_metadata() returned %d\n
basic_string
VOL_CPROTECTED\n
spaceman_ip_freed
%s:%u Err: Failed to scan xattrs for ino %llu: %u\n
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
splitting [%llu - %llu] (%llu) LBA [%llu - %llu] 
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
\n------------------ PAGE #%U ------------------\n\n
\tCloned ino #%llu -> #%llu\n
AppleAPFSSnapshot
61706673-7575-6964-0080-766f6c756d00
\tAPFS_INCOMPAT_UNWRITTEN_EXTENTS\n
we asked for %lld blocks but got zero (paddr %lld) from spaceman_alloc() and no error.\n
usage: apfs_migrator [options] <source volume device path>\n or apfs_migrator convert <log_file> - to convert binary log into text\n or apfs_migrator decode '<compacted metrics string>' - to convert compacted binary metrics into text\n\nOpt
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
dev_init on source volume %s\n
In IP freeQ  
%s:%d: %s failed to delete fs extentref tree after fs creation failed: %d\n
? 01234567890abcdefghijklmnopqrstuvwxyz+-*/_'#$&%()=[]\"\\
obj_cache_remove_reverted_fs_objects
%s:%u Err: dstream for ino (%llu) dstream size (%llu) != previously recorded (%llu) from ino (%llu)\n
authapfs_valid_hash_type
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
\t%16p %s\n
%@%s
%s:%d: IOObject %s is not %s\n
Mover_OnInode_walk_file_extents
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
===============================\n= Post-processing dstreams\n===============================
apfs-snap-delete-lock
nx_reaper_add_sub_object
spaceman_get_metazone_alloc_index
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
0
ROCompat:\n
Preprocessing extras
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%u: Creating target APFS volume @ %s [%u]\n
ino_phys_size_ext
Post-move: update Dir Stats/nLinks, split trees if needed
Reference count overflowed for object %p!\n
bt_remove_internal
supplemental_tree_destroy
%s:%d: %s spaceman IP base address is bad: %lld\n
 KMGT
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
Creating clonegroups
%s:%u Err: decrement_dstream_id_refcnt for ID %llu failed: %u\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
THAWED
attach_volume_keybag
Non-shared content of /tmp      : 
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
Initial namespace scan has been finished\nRoot level dirs found  : %zu\n
\nREADONLY MODE!!!\n
/dev/
%s:%d: %s object cache bootstrap failed: %d\n
Legacy scanning...
Failed to read kern.osreleasetype\n
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
%s:%u Err: Failed to get an extentRef tree (oid: %llu) for a snapshot xid %llu: %u\n
%s:%d: %s failed to delete mapping, error: %d\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
role=d
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%u Err: ScanDStreams failed with %u\n
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
nx_check_reaper
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
\tAPFS_FEATURE_EXTENDED_VEK_CLASSES
\nBad type: %u in msg 0x%llx offset 0x%llx\n
spaceman-ip-lock
%s:%d: %s %s: could not remove inode obj-id %lld (name: %s)\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
spaceman_chunk_zone_info_add
rdonly
\tAPFS_ROCOMPAT_ATTRIBUTION_TAG\n
Preprocessor_ScanPurgeables
invalid unlock flags: 0x%x\n
on error exit
userquota
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
%s:%d: %s Cannot restore unwritten status of extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s ***: expanded type seen on in-memory obj\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
API error: extra reference specified along with non-zero XID
doc_id_tree_invalid_crypto
Shared ranges found   : %zu\n
%s:%d: %s failed to enter tx to update size tracking for ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
com.apple.system.fs.speculative_telemetry
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
Preprocessor_FinalizeCryptoState
%@num_sr=%zu 
Shared hardlinks found: %zu\n
%s:%d: %s failed to get shadow dir-stats %llu for calculating dir-stats %llu (ino %llu): %s (%d); size tracking may go out of sync\n
%s:%d: cannot change role of SideCar volume\n
set_cloneinfo_id_epoch
All shared Apps                 : 
CreateClonegroups
btree_node_debug_stats
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
UserVol: %u
obj_cache_flush_write
obj_delete_and_free_by_oid
%s:%d: %s error starting move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
apfs
%s:%u Warn: Warning: Can't find dstream_id for ID in fs_root %llu: %u\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
OnFext
%s:%u Err: Failed to update extent: %u
mark
nx_check_recent_sanity_omap
%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n
!!! WARNING !!!\nThese metrics are NOT splunk-worthy. DO NOT send the decoded string to splunk!\n
%s:%u Err: Exception in PostMove\n
%s:%d: Unable to find volume %s\n
nx_metadata_fragmented_sanity_check
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%@oc_hit=%llu 
%s:%u Err: Renumber loop detected\n
DStream has fext(s) with ExtRef > 1
dir_stats_origin_can_be_moved
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
<%d
61706673-7575-6964-0001-766f6c756d00
tx_finish
get_vol_crypto(apfs) == VOL_CPROTECTED
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
API error: extra reference specified along with non-zero XID\n
Mover_OnDrec
\t%llu\t%u / %u%s\n
\t\t\tCryptoId %llu --\n
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s container block size too small for device block size (%d < %d)\n
/mobile/
Preprocessing dstreams
%s:%d: %s failed to%s update the <%llu, %llu> clone mapping, error %d\n
%s:%d: %s error finishing move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
%s:%u Err: Temporary checkpoint should be enabled on iOS, even for a dry run mode, use '-o loadtmpcp' or '-o createtmpcp'\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
         Misses             : %16llu\t(~%8llu MB)\n
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
omap=ephemeral
Using IOKit disk size (%llu) instead of statfs (%llu)\n
%s:%d: %s failed to delete prev doc-id tree, error %d\n
%@time=%ld 
\tTotal delta: %+lli 
%s:%d: %s unable to get spaceman: %d\n
jobj_release
apfs_lock_id
jobj_merge_maybe_clamp_64
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s unable to get omap: %d\n
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
100
clone_inode
%s:%d: %s tx_leave failed: %d\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
invalid offset (%llu) for last fext lookup\n
%@(%d:%d)
Expanded
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
nx-txn-blocks-lock
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s omap tree type 0x%x is bad\n
%s:%d: %s superblock failed sanity checks: %d\n
%s:%u Err: Target role volume is already eAPFSv2, bailing out\n
%s:%d: %s failed to get fsys oid %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
dev
%s:%d: %s First sync/barrier failed: %d\n
obj_alloc
= Create clonegroups\n
%s:%u Err: Failed to update target parent ino #%llu: %u\n
\t\tDS not found\n
reserved_80
%s:%d: %s was NOT able to update/decrement crypto state %lld, err = %d\n
%s:%u Err: insert_jobj for %s into 2nd tree failed: %u\n
%s:%d: %s failed to create fs: %d\n
= Converting volume %c with role %s\n
%s:%u Warn: ROOT inode had INODE_DIR_STATS_ORIGIN but no INO_EXT_TYPE_DIR_STATS_KEY XF, removing flags\n
.asset
%s:%d: %s Failed to create supplemental tree (type %d): %d\n
Source volume incompat flags: %llx.%llx.%llx\n
This is a dry run, using it as a chance to test all splitter_*msg functions
%s:%u Warn: Cannot find j_crypto_state_t %llu, skipping\n
%s:%u Err: ObjectId %llu is already in the renumber map, points to old ID %llu\n
nx_check
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
\tAPFS_INCOMPAT_DATALESS_SNAPS
!(ino->iflags & (JI_RAW_ENCRYPTED))
Expected free space after split : 
%s:%u: testing split_infomsg\n
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
%sr%s
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
Mover_OnSibling
Attaching keybag for target volume at index %u with UUID %s\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
%s:%u Err: fs_lookup_name_with_parent_id failed for drec #%llu ino:%llu [%s]: %u\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%u Err: ProcessDStreams failed with %u\n
%s:%d: %s Quota %llu is smaller than what's currently allocated and reserved %llu\n
%s:%d: %s Deleted the shadow_fs_root tree %p\n
Update
%s:%d: %s failed to decrement the crypto state refcount for crypto_id %lld, %s (%d)\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
obj_checkpoint_done
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: failed to init extended fields on drec %lld from blob.\n
%@oc_miss=%llu 
%s:%u Err: FextScanner (ScanFext) for xattr failed with %u\n
%s:%u Err: Failed to insert last pext: %u\n
ReplaceFext_InsertTail
get_purgeable_record_id_for_lookup
%s:%d: %s error updating chained key for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s doc-id tree creation failed: %d\n
rb
fs_is_phys_range_writable
%s:%u Err: Failed to remove extent: %u
Unknown type %d
%s:%d: %s lookup_next_snapshot() returned %d\n
loadtmpcp
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
spaceman-free-lock
fs_destroy_shadow_fs_root_tree
SetDirNlink
%@num_sc=%zu 
%@addcg_t=%llu 
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%@num_src=%llu num_dst=%llu 
ScanDstreams
%s:%d: %s prev doc-id tree sanity check failed: %d\n
%s:%d: %s failed to get next physical extent, error %s(%d)\n
ino-lock
%s:%d: Volume role 0x%x is not supported in container\n
Post move, source volume processing\nDRecs purged       : %zu\n
%s:%u Warn: fs_get_inode failed to get inode for parent dir of (%s) Ino# %llu, skipping\n
%s:%u Err: Can't find ino #%llu\n
%sDrec #%llu [%s] -> ino #%llu\n
%s:%d: %s object type 0x%x not reapable: %d\n
\tAPFS_INCOMPAT_EXTENDED_VEK_CLASSES
... [%s]\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
START
%s:%d: %s unable to get fs root tree: %d\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
quarantine
MoverBase_SetDirNlink
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
capacity: %9d %9d %9d %9d %9d %9d\n
nx_dev_init
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
... Moving DRec [%s] Inode %llu from [%s] to ROOT\n
%s:%d: %s Unsupported flags being used on purgeable record: %llx. Truncating...\n
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s omap xid %lld > spaceman xid %lld\n
strictatime
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
61706673-7575-6964-0140-766f6c756d00
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
%s:%u Err: Preprocessor scanner failed with %u\n
spaceman_iterate_free_extents_internal
addition
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
virtual object dirty count underflow\n
%s:%u Err: Failed to init iteration for an extentRef tree (oid: %llu) for a snapshot xid %llu: %u\n
CryptoDecRef
%s:%u Err: dereference_phys_range %llu, %llu bytes failed: %u\n
insert_purgeable_record
%s:%d: %s could not get dir-stats %llu: %s (%d)\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
apfs_free_data_blocks_if_needed
%s:%d: %s key.hdr.kind != NEW && numsnapshots == 0\n
%s:%d: %s failed to remove tail_fext, ino %llu, laddr 0x%llx, error %d\n
%@num_sb=%zu 
%s:%u Err: Flags mismatch: %x != %x\n
%s:%d: %s failed to create reap list: %d\n
CryptoStates moved : %zu\n
===============================\n= Processing inodes%s\n===============================\n
\tIno not found\n
apfs_checkpoint_traverse
apfs-phys-ext-oid-lock
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
Mover_OnXattr_walk_file_extents
DirNLink updated   : %zu\n
\tAPFS_FEATURE_STRICTATIME\n
MoverBase_Insert
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
obj_init
%s:%d: %s Failed to get next extent: %d\n
fsindex=
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
apfs-dir-stats-id-lock
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
61706673-7575-6964-0280-766f6c756d00
reserved_77
FindVolumeByRole
%s:%d: unlock == 0 failed %d\n
%s:%d: %s failed to cleanup orphan fext %lld, for dstream id %lld, %s (%d)\n
%s:%d: %s Cannot update extent at offset %lld in inode %lld: %s(%d)\n
CloneXattr
\t\t\t\t\t... skipped
AppleAPFSContainerScheme
%s:%d: %s Invalid reap list free entry %d\n
Secondary fs_root tree has been created, OID %llx\n
%s:%d: Unknown subtype %d for file info object %lld\n
%s:%u Err: Failed to update refcount for j_crypto_state_t %llu on target volume: %u\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
final
FindDirByPath
= Prepare stage
%s:%u Err: Failed to lookup normalized drec [%s] -> ino #%llu: %u\n
\t\t\t
object-lock
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
--Total--
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
Verbose file logging (%s) was enabled by boot-arg '%s'\n
iOS version
%s:%d: %s ino %lld did not have a source-purge-id\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
%s:%u Err: Exception in %s\n
... Skipping new purgeable record on %s, ino %llu dstream %llu - fsize didn't match; new %llu != old %llu\n
j_purgeable_t.file_id
Verbose logging is already enabled
Shared ranges          : %zu\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
\t\t\tOffs: %6llu: ExtRef [%8llu - %8llu] (%6llu), ref %u\n
btree_node_key_range_validate
purgatory.
%s:%d: Container corruption detected by %s:%u!\n
rw
jdev_fext_read_data() corrupts encrypted data
child_size_calculator_cb
level %d: %d nodes %.2f average descendents\n
nx_checkpoint_traverse
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
%s:%d: %s expanded records are now supported\n
 inline
btree_node_check
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: %s tx_enter_frozen() failed: %d\n
obj_read
apfs_split_timeout
Dirs found             : %zu / %zu %.02f%%\n
UpdateRangeMap
\t\t\tAddref new fext LBA [%llu - %llu) (%llu)\n
spaceman_free_extent_cache_setup
mount_volumes
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
%s:%d: %s *** failed to set dest dstream on ino %lld (from %lld, ret = %d)\n
%s:%u: Estimated source metadata size: %llu\n
%s:%d: %s spaceman IP bitmap free head %d out of range\n
fs_insert_fext_record
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
dump
Post-Move
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
btree_node_insert_internal
Preprocessor_FinalizeCryptoState_walk_file_extents
MoverBase_OnPostMoveObj_clone_mapping_add_ino
dereference
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%@incompat=0x%llx 
%s:%u Dbg: testing split_debugmsg\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
ProcessDstreams
MobileAsset
%s:%d: %s failed to fetch the integrity object (error %d)\n
Insert
physical object dirty count underflow\n
obj_create_internal
%@num_dirs=%zu 
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%u Err: Failed to insert dir drec into target path: %u\n
j_sibling_map_t.file_id
%s:%d: %s failed to get object oid %lld: %d\n
%s:%u Err: ProcessFext failed for fext offs %llu of dsid %llu for %s: %u\n
%s:%d: %s ino %llu is flagged to maintain dir-stats but has no dir-stats key\n
%s:%d: Couldn't set sparse bytes extended attribute on ino %lld, error %d\n
object-cache-reset-lock
%@msu_purgble_clone_blk=%llu 
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
%s:%u Err: Failed to scan sub-dirs for ino %llu: %u\n
\tInserting ino #%llu into clones map on Source\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
%s:%u Err: Somehow we failed to find a sibling with a parent_id for ino #%llu that is not in the known inner drecs\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
%s:%d: %s failed to destroy omap after fs creation failed: %d\n
Post-move: ClearPurgeInosWithoutPurgeRec
gid=
%15llu / %8llu %15.6f/call : %s\n
bad timeout value: %s
Move
%s:%u Warn: Can't find ino #%llu\n
%s:%u Err: DT_DIR in drec.flags [==%u] and S_ISDIR(ino->mode [==%u]) do not agree\n
%s:%d: %s failed to remove first, error %d\n
<100
nx_reaper
%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n
ClearPurgeInosWithoutPurgeRec
SHARED DS #%llu has %llu shared bytes:\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: %s source inode(%lld) marked sparse, but missing extended field\n
%s:%d: %s Can't get tree: %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
VOL_UNENCRYPTED
update
_fs_add_xattr
%s:%u Err: Failed to insert new DSID: %u\n
%@time=%llu 
apfs-pfkur-tree-oid-lock
%s:%d: %s Error reinitializing free extent cache: %d\n
Backup
%s:%u Err: ** BOGUS FEXT FLAGS = 0x%02x (crypto_flags = 0x%llx)\n
Preprocessor_ProcessFexts
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: %s failed to decrement crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
%s:%u Err: Failed to advance iterator: %u\n
apfs_clonegroup_remove_dir_stats_key
In freeQ     
= Post move
OnSibling
%s:%u Err: No snapshots were found to be merged\n
DirSize
crypto_obj_free
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
Renumber map:\n===============================
\tInode has hardlinks (nlink %u) : scheduled for processing\n
apfs_sanity_check
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: *** unknown obj type %d\n
REG FILE 
61706673-7575-6964-0020-766f6c756d00
%s:%d: %s xid %lld sync/barrier failed: %d\n
nx_mount_initiate_free_space_trims
apfs_lock_phys_range first_pbn 0, last_pbn 0x%llx\n
%s:%u: Success\n
large_key_val_to_jobj
%s:%u Warn: fs_get_inode failed to get inode for dir (%s) Ino# %llu, skipping\n
doc_id_tree_create
%s:%d: %s chunk %lld recent zone count underflow\n
Preprocessor_ProcessFexts_spaceman_alloc
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
fs_map_file_offset_ext
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
j_file_extent_t
Checkpoint desc/data blocks available:\n\tInitial    : %u/%u\n
update_nchildren
after merging snapshots
GetIOKitDeviceIOStats
unknown option provided: %s
after preprocessor scan
FinalizeCryptoState
%s:%u Err: Failed to update drec #%llu [%s]: %u\n
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s invalid reap_id (%llu), must be smaller than nr_next_reap_id (%llu)\n
61706673-7575-6964-0180-766f6c756d00
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%s:%d: %s directory sizing aborted (dir: %lld)\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
Found ID for [%s] : %llu\n
apfs_clonegroup_lookup_locked
%s:%d: %s probe of external device... skipping recent sanity checks.\n
com.apple.ResourceFork
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%u Err: MoveNamespace failed with %u\n
sha512
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
%s:%u Dbg: TX (%llu) is opened for a dry run, but final tx_leave with flush is requested\n
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s extentref tree %lld: %d\n
fsreserve=
recent zone chunk should have only ONE reference when being moved to the recent list!\n
User role volume is already present at slice %u, forcing a wet run for eAPFS v2 conversion\n
Preprocessor_ProcessSharedMetrics
MoverBase_PostMove_Purge_iterate_jobjs
hw.memsize
/tmp/
%s:%d: %s failed to look up shadow dir-stats %llu: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s failed to wait on reaper: %d\n
Using fallback path
= Preprocess namespace
%s:%u Err: apfs_create_doc_id_tree_if_needed failed with %u\n
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
tx_enter_internal
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: %s failed to fetch the fext tree (error %d)\n
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%s:%d: %s danger - crypto id %lld had refcnt %d\n
%s:%u Err: update_jobj for j_inode_t %llu into target failed: %u\n
SetOCSize
%s:%d: %s unable to get snapshot tree: %d\n
nx_tx_wait_closed_prev_flushing
Alloc bitmap for %zu entries, %zu bit(s) per entry, %zu bytes\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
val_size_for_jobj
PhysExtent
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
%@src_fsroot_2nd_nodes=%llu 
%s:%d: %s Failed to insert purgeable record (drec): %d (%s)\n
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%s:%d: failed to open volume device %s: %s\n
volname=Data
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
!apfs->apfs_readonly
dStats.origin_id
obj_checkpoint_check_for_unknown
%s:%u Err: update_jobj(j_dir_stats_t) failed for %llu: %u\n
Total size   
MODKEY
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
%@purge_all=%llu 
UpdateDsMap
sha3_384_4k
nx-volume_group-lock
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
spp_get_dstream_id
com.apple.fs.symlink
_fd_dev_write
%s
com.apple.fs.altlink
PostMove
apfs-doc-id-lock
%s:%d: %s stable checkpoint indices: desc %d data %d\n
spaceman-dev-lock
%@cloned_apps_blk=%llu 
%s:%u Err: Failed to update source parent ino #%llu: %u\n
sha3_256
length
Run
%s:%d: device initialization failed: %d\n
User role volume is already present at slice %u, forcing a dryrun for eAPFS v2 conversion\n
Preprocessor_ProcessFexts_dev_read_data
reserved_72
%s:%d: %s Unexpected unwritten extent for offset %lld of data stream %lld in inode %lld\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%s:%d: %s key @ %p key.hdr.obj_id %lld val @ %p val.kind %d refcnt %d owning_obj_id 0x%llx\n
%@ip_freeq_curr=%llu 
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
root
attr tag
resource fork size
id is zero\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
OnInode
         Evicted by alloc   : %16llu\t(~%8llu MB)\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
num children
RR_HOLE
%s:%u Err: %s failed with %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
authapfs_validate_node
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
apfs-fext-tree-oid-lock
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%u Err: insert_jobj for %s into %s failed: %u\n
%s:%u Warn: cp_dec_ref for cryptoId %llu has failed because of ENOENT (dropped to zero prematurely?), skipping\n
omap_reap
committmpcp
%s:%d: %s inode %llu was marked sparse but didn't have a sparse bytes extended field?\n
fs_update_unwritten_extent_record
\n\n
level %d: %d nodes\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
OnXattr
OnDrec
bt_merge_nodes
jobj_validate_key_val
%s:%d: can't get solidstate for device (%s)\n
spaceman_chunk_zone_info_recent_increment
%s:%u: Cache/Meta ratio is %llu / %llu == ~%llu, prefetch set to %s\n
\tAPFS_FEATURE_DEFRAG\n
Cannot open file %s\n
\t\tReplace fext in DS #%llu\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
SideCar
Remove
initial
BSD Major
Iterator_iterate_jobj
Features:
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s apfs_update_phys_range for satisfiable range failed on 0x%llx+%llu, error %d\n
%s:%d: object memory manager failed to create lock, error: %d\n
spaceman_free_extent_cache_insert
%s:%d: graft with invalid fs block size: %u\n
\tAPFS_INCOMPAT_INCOMPLETE_RESTORE
AddIterator
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
can't have a negative refcnt on crypto state %llu refcnt %d\n
obj_cache_flush_prepare
%s:%d: %s failed to set dir-stats key %llu on ino %llu: %s (%d)\n
Recovery
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
%s:%d: %s fext_ref_extent_key for fext %llu with crid %llu failed with %d\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
loading
\tAPFS_INCOMPAT_NORMALIZATION_INSENSITIVE\n
%s:%d: %s failed to set sparse byte count on inode %lld\n
\tino flags: %llx (Purgeable? %u)\n
\t\t\t\t\t... removing fext
%s:%d: %s Couldn't rename snap %llx to %s\n
duplicate_jobj_op_to_shadow_fs_root
j_dir_rec_t
%s:%d: %s error unreserving space, %lld blocks: %d\n
dispatch_source_create for watchdog has failed\n
MoverBase_MoveTo2ndTree
%s:%d: %s overprovisioning volume can only mount r/o\n
%s:%d: %s Couldn't remove extent at pbn %llu, err=%d\n
object-cache-flush-lock
MoverBase_PostMove
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: %s snapmeta tree type 0x%x invalid, using physical btree instead\n
%s:%u Err: remove_jobj(ROOT, j_dir_stats_t) failed: %u\n
%s:%d: %s spaceman cab count is bad: %d\n
omap=btree
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
Preprocessor_ProcessFexts_dev_write_data
spaceman_ip_block_alloc
%s:%d: %s bad overprovisioning volume configuration: reserve %lld quota %lld\n
Final     volume 2 fs_root
%s:%d: %s ino %llu is flagged as dir-stats origin but has no dir-stats key\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s/apfs_data
%s:%u Err: apfs_crypto_io_enable failed with %u\n
%s:%d: cannot change role of xART volume\n
ProcessInodes
%s:%d: %s omap_destroy returned %d!\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s error updating metadata ranges tree: %d\n
%s:%u Err: Failed to update ino #%llu: %u\n
+REG
apfs_reap_snapshots
mount_apfs
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
follow
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
Preprocessor_CryptoIncRef
apfs_update_phys_range
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
apfs-global-snap-lock
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
current tx not closed/flushing?!\n
All storage: Writes: %15llu %16.3f IOPS\n
BinlogFile: limit reached: %llu >= %llu\n
%s:%d: %s Volume role 0x%x already exists in container uuid %s\n
obj_mem_mgr_init
Source volume incompat: 
%s:%u Err: failed to insert cloned xattr %llu:%s with %u\n
%s:%u Err: Cannot resolve target volume path [%s]\n
%s:%d: %s fext_tree_update returned %d\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
%s:%u: User role volume is already present at slice %u, bailing out\n
reserved_76
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: Sparse bytes removed from inode %lld that didn't have an extended field.\n
obj_cache_remove_graft_persistent_ephemeral
[%s] has DirStats (ID: %llu), reassigning it to ROOT...\n
obj_checksum_verify_phys
%s:%d: %s error getting cab %d @ %lld: %d\n
DstreamID
Purgeable DS %llu [%u/%u]:
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
= Prepare stage\n
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
io_get_num_device_blocks
nx_checkpoint_find_valid_checkpoint
%s:%d: %s rapid-aged %llu inodes\n
User
<20
%6.02f%c%c
DirStats
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%u Err: Source volume has %llu snapshots, can't continue\n
Attaching class M sec key for source volume at index %u with UUID %s\n
fs_get_inode_with_hint
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%u Err: Clonegroup scanner failed with %u\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
Failed to read kern.osreleasetype
%s:%u: Would be %s temporary checkpoint\n
jobj_to_key_val
Very verbose mode was enforced by boot-arg '%s'\n
%s:%d: %s ino %llu is being moved but we don't know how to account for it (from_dir %llu/%llu, to_dir %llu/%llu); size tracking may go out of sync\n
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
Mover_OnFext_apfs_update_phys_range
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s tree_remove(%llu) failed\n
%s:%d: %s Cannot start transaction with XID %lld: %s(%d)\n
%s:%d: Volume role %d is not allowed at fs index %d\n
Dir 
%s:%u Err: Was not able to find a CryptoId for the old fext\n
Preprocessor_ProcessDstreams_walk_file_extents
ino-io-lock
curproc
obj_checkpoint_get
%s:%u Err: lookup_jobj for j_sibling_map_t %llu failed with %u\n
spaceman_free_extent_cache_search
=%d
unknown
dereference_phys_range
%s:%d: unlocking id %llu, which is not locked\n
apfs_sanity_check_tree_type
btree_node_child_val
%s:%d: %s failed to update allocate zone %llu: error %d\n
Installer
Memory usage %s:\n
-apfs_newvf_enabled
DStream refcount > 1
\tAdding dirstats for Clone Ino %llu to dir %llu, if any\n
%s:%u Err: ProcessFexts failed with %u\n
%s:%u Err: Exception in clonegroup finder\n
\t
%s:%d: %s failed to remove dir stats key from <%llu, %llu> clone mapping, error %d\n
Legacy scanning...\n
spaceman-lock
%s:%d: %s failed to delete fs clonegroup tree after fs creation failed: %d\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: don't know how to merge refcounts on objects of type %d\n
before tx_leave
%s:%u Err: clone_large_ea_extents failed for xattr %llu:%s with %u\n
nx_unblock_physical_range
clone size
%s:%u Err: spp_extentref_get_range (%llu, %llu) failed with %u\n
Combine
nx_tx_wait_closed
((&crypto_cache->free_list)->tqh_first == ((void*)0))
%s:%d: %s existing file system (slot %d)\n
j_dir_stats_t
\tClearPurgeIno: cleared INODE_IS_PURGEABLE on ino %llu in purgeableInoSet\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%u Warn: Timeout is too low, resetting to a default value\n
Preprocessing inodes
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s failed to write superblock to block 0: %d\n
/private/var
kind == NEW && refcnt = %d\n
%s:%u Err: Timeout exceeded during PostMove MoveObj stage\n
apfs_create_doc_id_tree_if_needed
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
omap_sanity_check
jfs_get_tree_in_snap
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
tx-mgr-lock
nx_tx_finish_wait_for_dirty_data
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
key_val_to_jobj
check_stale_doc_id_index
apfs_unlock_id
%s:%d: %s failed to lookup pos %lld in obj-id %lld err %d\n
multiKeyEncryption
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
Bytes (Write)
Timeout timer callback has been fired
\nFailed to read from file, in the middle of ReadSparse\n
%s:%u Err: Failed to lookup j_crypto_state_t %llu: %u\n
btree_node_compact
fs_rename_snapshot
One of the parameters is NULL\n
Shared MobileAssets             : 
%s:%u Err: Failed to combine extentRef trees: %u\n
%s:%d: %s chunk %lld recent zone count overflow\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s Couldn't insert extent, err=%d\n
%s:%u: Success, skipping tx_leave because of dry run mode\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
After Dump
Operations (Read)
DirStats upgraded  : %zu\n
dir_stats_update_reconciliation
spaceman_trim_free_blocks
%s:%d: %s Attempted to %s range %llu+%llu but it isn't entirely there! (found gap at %llu, next range at %llu+%llu)\n
fext_get_crypto_id
%s:%d: %s fs creation failed: %d ... cleaning up...\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
%s:%u Err: ReplaceFext failed: %u\n
apfs-integrity-meta-lock
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
%s:%d: %s apfs_free_data_blocks_if_needed(%llu,%llu) failed: %d %s\n
%s:%d: %s failed to delete doc-id tree, error %d\n
%s:%d: %s failed to delete fs snap metadata tree after fs creation failed: %d\n
%s:%d: %s failed to delete fs fext tree after fs creation failed: %d\n
%s:%u Err: Inode %llu, failed to replace DS: has %llu, expected %llu: \n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
Overprovision
nx_checkpoint_find_highest_xid
fs_get_inode
%s:%d: %s Couldn't reopen transaction to clean up: %d\n
%s:%d: %s deleting extent %lld %lld with invalid owning_obj_id %lld while apfs_num_snapshots is 0, this will cause overallocation\n
%s:%d: %s apfs_update_phys_range failed, err = %d\n
obj_destroy_complete
Target volume incompat: 
MS ASSET 
Invalid
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s cannot insert new ep %llu because the policy cache is full\n
convert_volume
apfs_migrator_verbose.log
apfs_release_objects
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
%s:%u Err: Failed to detect proper IOCTL to use\n
update_dir_stats_key_on_ino_and_clone_mapping
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
Enterprise data
Preprocessor_ScanDstreams_walk_file_extents
\tReplace DS #%llu -> #%llu in ino #%llu\n
%s:%d: %s not enough space to enter transaction\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
MoverBase_OnPostMoveObj_TYPE_INO
\tAPFS_FEATURE_DEFRAG
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
FileInfo
MODVAL
obj_delete_internal
%@snap_t=%llu 
converter_main_ios
paddr
nx-resize-spaceman-lock
nx_reaper_sanity_check
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
apfs_is_volume_uuid_allowed
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s error searching snapshot tree: %d\n
uid=
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
tx_checkpoint_write
GetDstreamSize_compressed_ino_phys_size
%s:%d: %s cib %lld index %d should be %lld\n
\nUnknown command: %llu in msg 0x%llx offset 0x%llx\n
lookup_jobj_ext
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
%s:%d: %s reverting on error: %d\n
perm
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: Sparse bytes removed from inode %lld internal flags: 0x%llx iflags 0x%llx, new_sparse_bytes %lld; name %s parent-id %lld), but it wasn't marked sparse.\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
/Volumes
unused1
%s:%u Err: Source volume conversion failed with %u\n
obj_write_prepare
%s:%u Err: Failed to insert tail extent: %u\n
%s:%d: %s reaper has tail with no head\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
%s:%d: %s %s: could not remove dir rec for obj-id %lld (name: %s)\n
target
Fexts moved : %zu\n
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
defragment=no
tinyobjcache
%s:%d: Cannot statfs /private/var\n
readonly
can not delete an object w/a non-current xid %lld o == %p\n
AVWo:nNMIvsEShrl:p:m:t:g:
dumpcg
%s:%u Err: IOCTL detection failed on 0x%lx (%zu) with %u\n
zero_tail_of_last_block
%s:%u Err: Path should be starting with /\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
writable
j_purgeable_t.dstream_id
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s Value too small:%u (group:%llu inum:%llu priv_id:%llu)\n
Main
AnalyzeFext
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
e:
%s:%u Err: Timeout exceeded during Move stage\n
%s:%u Err: tree_lookup_le LBA %llu returned %u\n
MoveFolder
%s:%d: %s omap snapshot count %d seems excessive\n
%s:%d: %s tx xid %lld took %lld us to close\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
\tAPFS_INCOMPAT_INCOMPLETE_RESTORE\n
%s:%d: %s Couldn't acquire lock on %llu-%llu, err=%d\n
%s:%u Err: Can't allocate %zu bytes for the ProcessFexts buffer\n
j_dir_rec_t.sibling_id
Scanning fexts in Xattr DS #%llu\n
%s:%u Err: remove_sibling_link failed for ino #%llu, drec #%llu [%s]: %u\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s dir-stats %llu maintains purgeable size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
authapfs_seal_break
%s:%d: %s failed to enter tx - %s(%d)\n
btree_node_space_stats
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
\tAPFS_INCOMPAT_DATALESS_SNAPS\n
Preprocessor_CryptoDecRef
obj_modify
w
+ASSET
nx_reaper_wait
%s finished in %llu msec (%02llu:%02llu)\n
spaceman_decrement_free_queue_count
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%u Warn: testing split_warnmsg\n
%s:%d: %s dir-stats %llu maintains clone size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
%s:%d: %s doc-id tree sanity check failed: %d\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
descendants
InsertPurgeRec
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
61706673-7575-6964-0010-766f6c756d00
tx_checkpoint_space_check
Mover_OnFext
\tAPFS_INCOMPAT_PFKUR_VOLUME
spaceman_free
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
Cannot use -S without -l
%s:%u Dbg: TX (%llu) is opened in NON dry run mode, all changes would be flushed\n
%s:%u Err: OnCryptoId for cryptoId %llu->%llu, DS %llu, fext flags %u failed: %u\n
Created %llu clonegroups, found %zu clones\n
cp_os_version
Purgeable
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
setup_demo_mode
ProcessDrec
capacity: leaves %llu / %llu => %.2f %% used\n
%s:%d: reaper thread is exiting, returning EBUSY\n
defragment=yes
%s:%d: cp_os_version: unable to parse osversion `%s'\n
%@data_ondisk_hardlnks=%llu 
%s:%u Err: Failed to alloc %llu bytes: %u\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
         oc_dirty_count     : %16llu\t(~%8llu MB)\n
\tAPFS_INCOMPAT_SEALED_VOLUME
\tAPFS_INCOMPAT_SECONDARY_FSROOT
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: %s %s: could not insert inode obj-id %lld (name: %s)\n
omap=physical
= Move namespace
spaceman_free_extent_cache_reset
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
/private/var/mobile
spaceman_alloc
spaceman_set_up_ip_reverse_mapping_tree
object-cache-lock
%@roincompat=0x%llx 
image-format-read-only
%s:%d: %s failed to fix up checkpoint data: %d\n
%s:%u: nx_mount %s %s\n
\tAPFS_INCOMPAT_EXPANDED_RECORDS
%s:%d: %s failed to load inode %lld ret %d on volume: %s\n
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
\tNormalized and hashed: [%s] [0x%x]\n
%s:%u Err: update_jobj for j_inode_t failed: %u\n
%s:%u Err: Create tmp checkpoint: tx_enter failed with %u\n
%s:%d: %s clone mapping is enabled for this volume\n
UpdateCryptoMap
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%u Dbg: TX (%llu) is opened but dry run mode would not call tx_leave\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
apfs_free_data_blocks
\t\t\t\t\t... skipped\n
%s:%d: can't get the device block size (%s). assuming 512\n
UNKNOWN TXN TYPE
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
j_inode_t.private_id
vector
\nFailed to read value, %llu bytes\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
sha256
%s:%d: %s failed to get doc-id tree, error %d\n
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
PurgeInos cleared  : %zu\n
Final 2nd source fs_root
PrepareToMoveFolder
%s:%d: ** BOGUS FEXT FLAGS = 0x%02x (crypto_flags = 0x%llx)\n
apfs_mount_livefs
%s:%d: %s failed to init xfield %d for dir-stats %llu: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s obj_modify() failed: %d\n
\tAPFS_INCOMPAT_UNWRITTEN_EXTENTS
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
spaceman_modify_bits
fext_cloner
%s:%d: %s fs fext tree creation failed: %d\n
%@data_ondisk_fclones=%llu 
%s:%u Err: ReplaceFext_InsertTail failed with: %u
%s:%u Err: Failed to get fs_root tree: %u\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%u Warn: FindDirByPath (%s) failed with %u, skipping\n
%s:%u Err: Failed to lookup j_crypto_state_t %llu on source volume: %u\n
%s:%u Err: walk_file_extents for xattr failed with %u\n
sha384
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
%s:%d: %s ino %llu has different group_id (existing: %llu new: %llu)\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
%s:%d: %s couldn't allocate memory for checkpoint map block\n
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
%s:%d: %s *** unknown expanded obj type %hhu\n
OnPostMoveObj
%s:%d: %s failed to enter tx to %s dir-stats %llu as needing reconciliation: %s (%d); size tracking may go out of sync\n
omap_recent_sanity_callback
hash=
%s:%u Err: One of the parameters is NULL\n
%s/apfs
         Meta
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
CloneFext
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
capacity: %9s %9s %9s %9s %9s %9s\n
\tAPFS_ROCOMPAT_CLONE_MAPPING
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
after Move
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
<80
APFS_TREE_LOOKUP_ZONE
nx_metadata_range_add
%s:%d: %s unable to get fs snap meta tree: %d\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
= Preprocess namespace\n
%s:%d: %s fs snap meta tree sanity check failed: %d\n
spaceman_chunk_zone_info_compare
dev_init
%s:%d: %s Unsupported flags being used on purgeable drec: %llx. Truncating...\n
%s:%d: %s obj_modify failed - %d\n
%s:%d: %s bt_move_entries %d failed: %d\n
\tAPFS_INCOMPAT_PFKUR_VOLUME\n
\tPreFlush   : %llu, delta: %+lli\n
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
%s:%u Err: Scan section has failed, most likely we ran out of memory\n
max phys footprint
unused2
insert_phys_extent
Allowing ObjCache size up to 
dir_stats_get_flags
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
fssize=
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
... Skipping new purgeable record on %s, ino %llu dstream %llu - owner UID didn't match\n
Clones                 : %zu\n
btree_node_sanity_check
nx_check_omap
%s:%u Err: Failed to get apfs object oid %llu: %u\n
\tAPFS_FEATURE_DEFRAG_PRERELEASE\n
AnalyzePurgeable
bt_merge_up
%s:%d: %s unable to read cib %lld @ %lld: %d\n
61706673-7575-6964-0002-766f6c756d00
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
spaceman_alloc_iterate_chunks
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
suid
61706673-7575-6964-0004-766f6c756d00
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
spaceman_fs_bounds_set
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
nx_check_checkpoint_map_block
Memory size: %llu bytes (~%.02fGB), using %llu bytes (~%.02fGB) for object cache\n
%s:%u Err: GetCryptoId for cryptoId %llu, flags %u failed: %u\n
reserved_73
insert_jobj
%s:%d: %s Cannot mark space for %zu bytes at offset %lld in dstream %lld of inode %lld as writable: %s(%d)\n
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
%s:%u Err: Failed to move xattrs for ino %llu: %u\n
%s:%d: %s error finishing move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
fs_write_stream
%@vers=%s 
password=
<redacted>
Preprocessor_CloneHardlink
%s:%d: %s invalid zero len, paddr %llu\n
%s:%u: Success, flushing TX (%llu)\n
%s:%u Err: Can't get inode for folder id %llu\n
%s:%u Err: Cannot set new siblingId for drec #%llu [%s]\n
btree_node_child_id_update
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
/dev
ConfigurePrefetchFlags
Final     volume 1 fs_root
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
\tAPFS_FEATURE_EXTENDED_VEK_CLASSES\n
%s:%d: Volume role 0x%x is not allowed for an unencrypted volume\n
... Skipping new purgeable record on %s, ino %llu dstream %llu - error sizing purgeable directory : %u\n
new address mismatch on redirty 0x%llx 0x%llx\n
-apfs_split_debug
BSD Minor
ro
Baseband data
spaceman_cab_sanity_check
%s:%d: %s Would have attempted to create an entry with kind == NEW and refcnt == %d! (flags=0x%x, existing val len_and_kind=0x%llx owning_obj_id=%llu refcnt=%d)\n
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
%s:%u Err: Outer namespace scan failed after multiple retries: %u\n
%s:%d: %s sfq %d count underflow %lld - %lld\n
Failed to decode\n
%s:%u Err: Dump failed, most likely we ran out of memory\n
One of the parameters is NULL
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
\tAPFS_INCOMPAT_CASE_INSENSITIVE
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/fscommon/purging.c
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s spaceman chunk count is bad: %lld\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
\t\t%s : scheduled for processing\n
%s:%d: %s Purgeable start time (%llu) is unsupported on purgeable drecs.\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
make_jkey_from_jobj
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
%@num_sh=%zu 
%s:%d: %s failed to update <%llu, %llu> clone mapping, error %d\n
Attempting to reuse a non-candidate chunk zone info\n
dispatch_source_create for watchdog has failed
%@pmv_t=%llu 
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
Operations (Write)
%s:%d: %s failed to finish writing to obj-id %lld (pos %lld / new_size %lld)\n
%s:%d: %s BUG BUG BUG: ino %lld non-contiguous extents! prev_fext %lld:%lld (%lld) and orig_fext %lld:%lld (%lld)\n
j_crypto_state_t
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
apfs-dir-size-lock
%s%s
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
spp_get_crypto_id
PathFlags_Evaluate
, enabling timeout avoidance measures
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
<UNKNOWN>
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
auto
%s:%d: %s container cleanly-unmounted flag set.\n
Preprocessing scan
\tAPFS_INCOMPAT_SEALED_VOLUME\n
unexpected storagetype: 0x%x\n
not 
%sDS #%llu counts %u/%u\n
%s:%d: %s Failed to create purgeable record (drec): %d (%s)\n
btree_delete
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
===============================
jdev_fext_write_data
%s:%u Err: FolderExtractor failed: %u\n
sha3_256_4k
%s:%d: %s iter_next returned %d\n
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%u Err: User volume passed for v1->v2 migration but no Data volume found\n
apfs-phys-lock-state-mutex
delta_from_dir_stats
%s:%d: %s Fusion is not supported anymore\n
%s:%u Err: Secondary fs root tree creation failed: %u\n
invalid crypto index %d\n
All shared clones               : 
%s:%u Err: Failed to insert a cloned inode: %u\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
Got ENOENT, retrying [%u attempts left]...\n
%s:%u Err: Bad volume index for [%s] : %i\n
All storage: Reads : %15llu %16.3f IOPS\n
apfs_is_volume_fsindex_allowed
%s:%d: %s failed to look up dir-stats %llu for origin inode %llu: %s (%d)\n
apfs-rename-lock
%s:%d: can't get features for device (%s)\n
APFS_8K_OBJS
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%u Err: Failed to remove ino %llu from purgeableInoSet\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
icp_dec_ref
Initial   source fs_root
btree_node_free_list_entry_validate
Removable
%s:%d: %s UUID %s is not allowed, error %d\n
Post-move: PurgeDrecs
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%@src_fsroot_2nd_depth=%llu 
%s:%u Err: doc_id_tree_remove failed with %u for docId %u\n
%s:%d: %s tx_leave failed with error: %d\n
%s:%u Err: Failed to update source inode: %u\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
browse
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%u Err: Failed to detect fext structure version:\n
reserved_83
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
ino_set_rage
Final     source fs_root
API error: extra refcount specified along with non-zero XID
%s:%d: %s stopped updating dir-stats due to chain being too long\n
dev_init on target volume %s\n
\t\t\t\t\t... trimming to (%llu)\n
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
%s:%d: %s couldn't insert record err:%s\n
%s:%d: %s Final sync/barrier failed: %d\n
j_dstream_id_t
obj_checkpoint_known
IOService
fd_dev_write_extended
Object Cache usage
VOL_ONEKEY
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
%s:%u Err: Can't get extentref tree for a target volume: %u\n
Renumber %s %llu -> %llu\n
j_xattr_t
\tAPFS_INCOMPAT_SECONDARY_FSROOT\n
SnapMetadata
invalid crypto id %llu
%s:%d: %s could not alloc %zd bytes @ pos %lld for obj-id %lld (err %d)\n
%s:%d: %s failed to get a new default crypto-id, ino %lld\n
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
%s:%d: %s Inserting snap_meta failed, %d\n
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
io_get_device_block_size
%s:%d: %s Could not set fs bounds for guarantee %lld and quota %lld: %d\n
%@disk_free_curr=%llu 
\t\tCloning fext [%8llu - %8llu] (%6llu) -> LBA [%8llu - %8llu], CID: %8llu, flags: 0x%x\n
===============================\n= Post-processing dstreams\n===============================\n
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
owners
splitter_dumpFallbackEx
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
OnInsertPurgeRec
obj_cache_remove
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%@ip_freeq_start=%llu 
%s:%u Err: Failed to insert cloned fext into DS #%llu: %u\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%u Err: Source volume crypto (%u) is different from target volume crypto (%u), can't migrate\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
SNAP_DELETE_TXN
 %c:%llu
%@xp_data=%lld 
apfs-omap-lock
apfs-im-cache-lock
%s:%u Err: rangeLba(%llu) + rangeLen(%llu) (%llu) <= lba (%llu)\n
%@num_total_files=%zu 
j_sibling_map_t
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
supplemental_tree_get
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
total_count
splitter_main_ios
%s:%u Err: Failed to update inode %llu: %u\n
%s:%d: %s Tree delete oid %llu threw %d\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
can not lock id zero\n
OnPurgeDrec
invalid tweak type %d\n
btree_iterate_nodes
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
after tx_leave
%s:%u Err: walk_file_extents (AnalyzeFextCrypto) for DS %llu failed: %u\n
btree_node_reap
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
wb
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
match_jobj_expanded_type_to_tree_type
%s:%u Err: Failed to scan source volume post migration for conversion: %u\n
Max stack              : %zu\n
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
%s:%u Err: Failed to mount source APFS volume @ %s [%u], error %u\n
ReplaceDirStats
%sIno #%llu counts %u/%u\n
omap_destroy
dev_init_common
GetDstreamSize_ino_phys_size
%s:%d: %s Cannot allocate space for %zu bytes at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%u Err: Failed to convert volume with role %s\n
%s:%u Err: xf_get docID failed with %u on on ino %llu\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: %s reap list object free list erroneously empty?\n
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
ProcessFext
%s:%d: failed to open container device %s: %s\n
%s:%u: Mounting target APFS volume @ %s [%u]\n
Incompat:\n
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
update_dir_stats_by_key_ext
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
%s:%u Err: 2nd Outer namespace scan failed: %u\n
Preprocessor_OnDrec
fs_is_content_protected(apfs)
obj_get_async_read
<40
spaceman_chunk_zone_info_cache_init
spaceman_upgrade_sm_version_0_to_1
\tAPFS_CONFORMANCE_FORMAT\n
reserved_71
dir_stats_moved
%s:%d: %s failed to get doc-id tree key count, error %d\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
61706673-7575-6964-0200-766f6c756d00
%s:%u Err: Failed to insert matching PurgeRec for ino %llu into %s: %u\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
APFS_INODES
Hardware
spaceman_sanity_check
%@xp_desc=%lld 
\nREADONLY MODE!!!\n\n
%s:%d: %s invalid ref count %d for non NULL zero ref tree\n
%s:%d: cannot change role of Backup volume\n
%s:%d: %s fs snapshot metadata tree creation failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
defwrite
update_sparse_bytes
object-cache-list-lock
crypto_hash_insert
%u\n
%s:%d: %s set apfs_fixup_flags to %#llx\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%u Err: Failed to scan purgeable dir-recs: %u\n
Shared clones only between Apps : 
GetSingularExtentRefTree
Scanning fexts in DS #%llu\n
%s:%d: %s invalid crypto object type %u\n
%s:%u Err: Failed to analyze xattrs for ino %llu: %u\n
btree_check_recent_sanity
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
bt_update_last_leaf
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
Timeout timer callback has been fired\n
%@data_num_fclones=%llu 
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: %s %s: could not insert dir rec for obj-id %lld (name: %s)\n
%s:%d: %s fext tree type 0x%x invalid, using physical btree instead\n
%@purge_full_2=%llu 
main
%s:%u: Timeout was overriden via boot-args\n
Shared clones found   : %zu\n
%s:%u Err: FextScanner (ScanFext) for DstreamId (%llu) failed with %u\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%u Err: ProcessInodes failed with %u\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
MoveTo2ndTree
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
%s:%d: %s failed to get reap list tail: %d\n
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s failed to find host inode (id %llu) for purgeable rec lookup, falling back to ino %llu's atime\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
apfs_clonegroup_update_dir_stats_key
spaceman_chunk_zone_info_recent_decrement
not handling the current tx!\n
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
Paths:
%s:%u Err: FindDirByPath (%s) failed with %u\n
\tInserting ino #%llu into clones map on Target\n
ScanInode
 shared
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
no-name
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
 
%s:%u Err: Failed to update dir ino: %u\n
%s:%d: %s error starting move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
fd_dev_read_extended
VOL_PFKEY\n
trying to zero the superblock!\n
%s:%d: %s failed to leave tx, error %d\n
PURGEABLE ino: %llu flags: %x\n
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%u Err: Can't get extentRef tree: %u\n
Unknown: %u\n
Mover_OnInode
spaceman_checkpoint_traverse
%s:%u Err: Timeout exceeded during PostMove PurgeDRec stage\n
%@num_total_dirs=%zu 
Scanning for clonegroups
%s:%u Err: Failed to insert pext: %u\n
After draining freeQs
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
    keys: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
remove_jobj
SiblingLink
%s:%d: %s Trying to delete space for extent %lld %lld which has invalid owning_obj_id %lld\n
Preprocessing core
API error: extra refcount specified along with non-zero XID\n
%s:%u Warn: fs_get_inode failed to get inode for (%s) Ino# %llu, skipping\n
ReplaceFext
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s failed to init extended fields for dir-stats object on ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
apfs_mount
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
\tAPFS_FEATURE_HARDLINK_MAP_RECORDS
CloneMap
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
ROCompat:
DstreamIds moved   : %zu\n
,
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s cab %d cib count %d should be %d\n
/System
Scanning Outer again...
Preprocessor_ScanDstreams
Reached the max sane freeQ drain attempts limit. Most likely we'll hit an ENOSPC later.
\t\t\t\tFound fext [%llu - %llu] (%llu) LBA [%llu - %llu] CID: %8llu flags: 0x%x\n
         oc_phys_free_count : %16llu\t(~%8llu MB)\n
authapfs_validate_node_hash
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
%s:%u Warn: Cannot find j_crypto_state_t %llu on source volume, skipping\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
spp_extentref_get_range
reference
blocks_in_txn
%s:%u Err: remove_jobj for j_inode_t failed: %u\n
\tScanning dstreams from ino #%llu:\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
nx_tx_wait
Mount
%s:%u Err: Failed to attach the volume keybag: %u\n
Mover_OnInode_clone_mapping_add_ino
%s:%d: Failed to remove sparse bytes attribute from ino %lld, but it was successfully got, errro %d\n
case=insensitive
%s:%u Err: Lba end (0x%llx + 0x%llx) outside of bitmap: 0x%llx > 0x%zx\n
Moving %sDrec #%llu [%s] -> ino #%llu\n
checkpoint
spaceman_ip_bm_block_alloc
j_dir_rec_t.file_id
%s:%d: %s found mapping tree with old subtype\n
61706673-7575-6964-0008-766f6c756d00
proc_pid_rusage failed with %u\n
\tAPFS_FEATURE_DEFRAG_PRERELEASE
fs_tx_leave_ext
FreeQ:\n\tInitial    : %llu\n
... Removing DRec for [%s]\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%u..
%s:%d: %s created doc-id tree, oid %llu\n
%s:%d: %s btree_node is null\n
%s:%d: %s error modifying omap: %d\n
\tAPFS_ROCOMPAT_ATTRIBUTION_TAG
ino %lld pos:len %lld:%lld fext %lld:%lld (%lld)\n
\t\t\tCryptoId %llu ++\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
reserved_75
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
Initial   volume 1 fs_root
nx_reaper_add_ext
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
%s:%d: Cannot find entries matching %s : %u\n
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%u Err: testing split_errmsg\n
%s:%u Err: Somehow we have current obj id (%llu) larger than max obj value we moved (%llu)\n
\tOnInode: added ino %llu to purgeableInoSet\n
\t\t\t\t\tDeref LBA [%llu - %llu) (%llu)\n
bt_lookup_copy_out
ino %lld illogical file extent %lld:%lld != alloced_size %lld (fsize %lld)\n
Debug Internal verbosity enabled
ProcessSharedMetrics
61706673-7575-6964-0040-766f6c756d00
nx_tx_wait_frozen
Preprocessor_CloneXattr
Xattr
%s:%d: Unable to get UUID for volume %s\n
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%u Err: unable to remount NX container @ %s\n
\nConverting eAPFS v1 -> eAPFS v2\n
61706673-7575-6964-0300-766f6c756d00
%@features=0x%llx 
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: ***: unknown obj type %d\n
\n
%@disk_free_start=%llu 
Device Characteristics
%s:%d: %s Trash unfinished tx xid=0x%llx\n
Performed %zu freeQ drain iteration(s)\n
e-apfs
prevent_synthetic_object_operation
Ranges moved: %zu\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%u Err: Outer namespace scan failed: %u\n
Mover_PostMove_FolderExtractor
icp_new_crypto
Could not open metrics log file %s
Paths:\n
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s *** failed to set rdev as an extended field of ino %lld (ret %d)\n
%s:%d: %s Container corruption detected by %s:%u!\n
System
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
Object Cache usage\n
\tOnInsertPurgeRec: removed ino %llu from purgeableInoSet\n
%s%s%llx
%s:%d: %s unable to get spaceman free queue tree: %d\n
FROZEN
Preprocessor_UpdateRangeMap
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
j_purgeable_t
%s:%u Err: FextScanner (AnalyzeFextCrypto) for xattr failed with %u\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: %s snap meta tree %lld: %d\n
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s:%d: %s %llu blocks are already reserved in container, Cannot reserve more than %llu blocks in the container\n
apfs_mark_inconsistent_
encrypted
\tAPFS_INCOMPAT_CASE_INSENSITIVE\n
%s:%d: %s Cannot trim extent at offset %lld in inode %lld from %lld to %lld bytes: %s(%d)\n
%s:%u Err: Failed to mount volume(s)\n
%s:%u Err: Can't get extentref tree for a source volume: %u\n
%s:%u Err: lookup_jobj(j_dir_stats_t) failed for %llu: %u\n
%s:%d: %s failed to update dir-stats %llu: %s (%d)\n
apfs_clonegroup_insert_inode
%s:%u Warn: Warning: The volume path %s won't work with encrypted volumes, use rdisk instead\n
=======================\nStages timing:\n
spaceman_set_bits_in_bm
purgeable rsrc size
%s:%d: invalid object size: %d size_phys %d\n
%s:%u Err: CloneAllXattrs failed: %u\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
Files found            : %zu / %zu %.02f%%\n
===============================\n= Processing ranges%s\n===============================\n
Target Disk Mode
61706673-7575-6964-00c0-766f6c756d00
%s:%d: %s failed to find valid checkpoint: %d\n
%llx.%llx.%llx\n
Preprocessor_ScanXattr
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
Memory size: %llu bytes (~%.02fGB)%s\n
nx_tx_wait_open
%s:%u Err: apfs_container_iouc (%s) failed with status: 0x%x, %u\n
ino_has_vnode(ino)
%s:%d: %s Unknown flags being used on purgeable record: %x. Truncating...\n
sealed=yes
Data
New target volume name: %s\n
spaceman_fq_tree_find_overlap
fs_make_hole_range_writable
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%u Err: Bad volume index for [%s] - %i\n
MoveDrec
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
\t%llu was %llu\n
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
fstree=btree
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
%s:%u Err: Unable to find a free slot for a new volume\n
Preprocessor_AnalyzeXattr_walk_file_extents
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
%s:%u Err: Fext cloning failed: %u\n
%s:%d: %s fs extentref tree creation failed: %d\n
automounted
 (%s)
fd_dev_read_helper
%s:%d: %s Shadow fs_root does not exist\n
%s:%d: %s got err %d writing at pos %lld in obj-id %lld (blkcount %llu, len %zd)\n
/dev/rdisk%llus%llu
%@mv_t=%llu 
%s:%d: %s failed to increment the crypto state refcount for crypto_id %lld, %s (%d)\n
gbitmap_reap
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s error getting mapping tree: %d\n
61706673-7575-6964-01c0-766f6c756d00
%s:%d: %s Error: tx[%lld] failed to start: %d\n
Enhanced APFS should be enabled to allow migrator in a non dry-run mode
Cache
VOL_ONEKEY\n
Preprocessor_ProcessInodes
j_sibling_link_t
<60
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
creating
%s:%d: %s X %d\n
Initial   volume 2 fs_root
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
%s:%d: %s tx_enter() failed: %d\n
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
Preprocessor_ReplaceFext
dir-stats
get_dir_stats_by_key
jobj_validate_large_key_val
%s:%u Err: remove_jobj for %s failed: %u\n
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
%s:%u Err: Failed to read data from LBA %llu, %zu bytes: %u\n
apfs-snapmeta-oid-lock
%+zi shared files found\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%u Err: Could not sync and freeze volume: %s : %u\nContinuing as is...\n
Scanning Outer...
kern.osreleasetype
update_file_extent
Total ranges to move  : %zu\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
61706673-7575-6964-0100-766f6c756d00
Dump metrics: %s\n
/
+8
%s:%u Err: Unable to find uuid of target volume, err %u\n
%s:%d: %s %s: could not update parent obj-id %lld on create of obj-id %lld (name: %s)\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%u Err: Failed to move siblings for ino %llu: %u\n
Inode
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
full clone size
%s:%d: %s Cannot insert purgeable record with zero atime (ino %llu).\n
sha3_512
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
fs_insert_snapshot_metadata
move_snapshot_to_purgatory
Preprocessor_AnalyzePurgeable
\t\tDS id: %llu, refcnt: %u\n
Scanning [%s]...\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
groupquota
%s:%d: %s tx xid %lld took %lld us to flush\n
Reached the max sane freeQ drain attempts limit. Most likely we'll hit an ENOSPC later.\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
\tOnPostMoveObj: added ino %llu to purgeableInoSet\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
Preprocessor_UpdateInoMap
MoverBase_InsertPurgeRec
= Post move\n
LBA [%llu - %llu] (%llu) counts %u/%u\n
%s:%d: %s unable to get snap meta tree %lld: %d\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: *** Can't release unknown obj type %d\n
... Skipping new purgeable record on %s, ino %llu dstream %llu - gen count didn't match: %llu != %llu\n
Fexts moved        : %zu\n
CryptoIncRef
%s:%u Err: %s for cryptoId %llu->%llu, flags %u failed: %u\n
%s:%d: %s Coludn't update dir stats key on (group:%llu inum:%llu priv_id:%llu): %s\n
\tAPFS_INCOMPAT_ENC_ROLLED
exp_dir_stats_refcnt_merge
%@tgt_fsroot_nodes=%llu 
\tCloning DS #%llu -> #%llu\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
reference_phys_range
%s:%u Err: Failed to lookup j_crypto_state_t %llu on target volume: %u\n
sha512_256
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
!((apfs)->apfs_main_apfs != ((void*)0))
%s:%u Err: Create tmp checkpoint: tx_leave failed with %u\n
Disk usage %s:\n
%s:%d: %s failed to allocate temporary block memory\n
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
%s:%u Err: Failed to lookup dstats key %llu for ino %llu : %u\n
Shared clones filenames:\n
%s:%d: %s failed to attach graft to object cache: %d\n
%s:%u: Flushed temporary checkpoint: xid %llu\n
clear_invalid_fixups
%s:%u Err: Failed to iterate snapshots: %u\n
%s:%u Err: apfs_clonegroup_insert_inode failed for ino %llu: %u\n
remove_dir_stats_key_on_ino_and_clone_mapping
UUID
%s:%d: %s unable to get prev doc-id tree: %d\n
... Skipping [%s]\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
Would %sneed drec rehashing\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s unable to allocate chunk zone info cache\n
%s:%d: %s tx manager initialization failed: %d\n
Shared content of /tmp          : 
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
nx_reaper_next_record
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
spaceman_fq_tree_insert
```
