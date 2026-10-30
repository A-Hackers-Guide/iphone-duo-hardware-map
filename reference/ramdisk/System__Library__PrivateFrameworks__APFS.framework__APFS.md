# `/System/Library/PrivateFrameworks/APFS.framework/APFS`

From the upgrade restore ramdisk (141-29011-104.dmg). 638,144 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2560)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,406)

```
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: Hit error scanning blob in ino %llu, err %d\n
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
com.apple.apfs.volume.skip_eapfs
%s:%d: rdlock == 0 failed %d\n
fts_openbyid_
btree_node_free_list_entry_validate
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
process_volumes
%s:%d: %s omap check failed with error: %d\n
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: skipping already seen dir %llu\n
e:
obj_delete_and_free_by_oid
encrypted
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
%@num_sr=%zu 
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
fssize=
%s:%d: %s unable to get doc-id tree: %d\n
obj_mem_mgr_init
obj_destroy_complete
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%@data_ondisk_fclones=%llu 
%s:%d: unlock == 0 failed %d\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s chunk %lld recent zone count underflow\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
_fd_dev_write
%s:%d: %s lookup_next_snapshot() returned %d\n
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: done err = %d\n
kern.rage_vnode
nx_reaper_obj_get
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
exec
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
obj_checkpoint_get
apfs-clonegroup-lock-mutex
%s:%d: %s Error: tx[%lld] failed to start: %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
spaceman_free_fs_deduct_block_counts
%s:%d: %s failed to find valid checkpoint: %d\n
jobj_size_for_key_val
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
obj-mem-mgr-lock
%@num_total_files=%zu 
bt_update_last_leaf
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
apfs-stream-id-lock
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
obj_release
rdisk
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
Any
61706673-7575-6964-0100-766f6c756d00
%s:%d: %s btree_node_insert failed: %d\n
com.apple.apfs.volume.encrypted
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
hash=
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: %s failed to set up spaceman for demo mode: %d\n
object-cache-list-lock
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
union
%s:%d: %s failed to write checkpoint data block %lld: %d\n
%@prepro_t=%llu 
sha384
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s failed to get reap list tail: %d\n
omap_destroy
btree_delete
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
object-cache-flush-lock
%@msu_purgble_clone_blk=%llu 
com.apple.apfs.volume.case_sensitive
IONVRAM-DELETE-PROPERTY
%s:%d: Corrupt dstream in xattr ino %llu\n
61706673-7575-6964-0000-766f6c756d00
spaceman_alloc
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
spaceman-dev-lock
BSD Name
fd_dev_close
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s unable to get fs extentref tree: %d\n
%ss%d
FIXUP
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
DirStats
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
wb_average_io_count
obj_write_prepare
%s:%d: %s object type 0x%x not reapable: %d\n
AppleAPFSContainerScheme
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s failed to attach graft to object cache: %d\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
Unknown type %d
spaceman_decrement_free_queue_count
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
invalid lock flags: 0x%x\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
tx_mgr_free_tx
%s:%d: %s error getting mapping tree: %d\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
spaceman_alloc_iterate_chunks
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
<100
%s/apfs
%s:%d: ordered iteration must be reset once finished\n
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: failed to get purgeable info for ino %llu: %s (%d)\n
nx-global-extent-manipulation-lock
%s:%d: %s object type 0x%x not reapable?: %d\n
%@incompat=0x%llx 
%@time=%ld 
%@pmv_t=%llu 
atime
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: failed to open container device %s: %s\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
loadtmpcp
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s:%d: failed to iterate purgeable extents of dir %llu: %s (%d)\n
nx_reaper
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
nx_corruption_detected_int
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
  values: %9s %9s %9s %9s %9s %9s\n
apfs-snapmeta-oid-lock
%@src_fsroot_depth=%llu 
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
wb_average_time
%@cloned_apps_blk=%llu 
sha3_256
quarantine
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: graft with invalid fs block size: %u\n
Write burst: Total time between bursts
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
,
defragment=no
61706673-7575-6964-0140-766f6c756d00
nx_check_checkpoint_map_block
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
%s:%d: failed to statfs(%s): %s (%d)\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
btree_node_debug_stats
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
%s:%d: %s omap tree sanity check failed: %d\n
%@(%d:%d)
%@ip_freeq_curr=%llu 
spaceman_sanity_check
fd_is_eapfs
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
fd_dev_read_extended
%s:%d: failed to fts_read(): %s (%d)\n
IOMatchCategory
userquota
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%@roincompat=0x%llx 
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s Container corruption detected by %s:%u!\n
tx_enter_internal
%@num_sh=%zu 
Write burst: Total time
Write burst: Total number of I/Os
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
spaceman_fq_tree_insert
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s:%d: can't get the device block size (%s). assuming 512\n
apfs_reap_snapshots
tx_checkpoint_space_check
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
DirRecord
%@fl=%d
nx_checkpoint_find_highest_xid
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
spaceman_upgrade_sm_version_0_to_1
spaceman_iterate_free_extents_internal
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%@purge_from_data=%llu 
%@msu_shared_clone_blk=%llu 
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
nx_metadata_range_optimize
Histogram for free extents sizes, number of buckets is
obj_cache_remove_graft_persistent_ephemeral
tx_flush
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
uid=
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s omap snapshot tree sanity check failed: %d\n
fsindex=
DstreamID
%02hhx
spaceman_check_allocation_status_internal
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
%s:%s
IODeviceTree:/options
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
-apfs_newvf_enabled
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
btree_node_space_stats
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
nx_get_evict_mapping_tree
nx_reaper_next_record
unwritten=no
spaceman_free
parse_state_into_args
%s:%d: %s omap tree type 0x%x is bad\n
%s/nx
apfs-snap-delete-lock
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
SnapName
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s container cleanly-unmounted flag set.\n
_APFSVolumeAddUnlockRecordsOrHints
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
%s:%d: %s spaceman chunk count is bad: %lld\n
Get count overflowed for object %p!\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
AppleEmbeddedNVMeController
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
i16@?0^{purge_entry=i^{?}IQS}8
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
obj_checkpoint_check_for_unknown
%@oc_hit=%llu 
spaceman_cab_sanity_check
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
com.apple.apfs.volume.role
Number of directories
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%s:%d: %s failed to create reap list: %d\n
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%@xp_data=%lld 
Write burst: Burst count
object-lock
obj_checksum_verify_phys
%@purge_from_user=%llu 
%@%s
fd_is_root
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
%@data_num_fclones=%llu 
spaceman_trim_free_blocks
<40
obj_cache_remove_reverted_fs_objects
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
%@data_size_hardlnks=%llu 
bt_insert
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
Xattr
nx_checkpoint_find_valid_checkpoint
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
skipsanity
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
RoleValue
Number of extents
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
apfs-rename-lock
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s unable to get omap tree: %d\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
invalid tweak type %d\n
%s:%d: failed to disable rapid-aging vnodes: %s (%d)\n
%s:%d: skipping already seen ino %llu\n
%s%s
nx_tx_wait_flush
case=sensitive
%s:%d: %s chunk %lld recent zone count overflow\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
com.apple.apfs.container.size
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s:%d: processing file %llu with %u extents\n
browse
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
spaceman_ip_bm_block_free
nx_checkpoint_load_data
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
io_get_num_device_blocks
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%d: skipping already seen file %llu\n
%s:%d: %s xid %lld sync/barrier failed: %d\n
volname=
btree_check_recent_sanity
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%s:%d: Corrupt dstream ext in ino %llu\n
%s:%d: device initialization failed: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
obj_cache_flush_write
FileExtent
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
nx_check_recent_sanity
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
spaceman-fxc-lock
%@num_dirs=%zu 
%@addcg_t=%llu 
sha256
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
%s:%d: %s error updating metadata ranges tree: %d\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
com.apple.apfs.volume.allow_ext_vek_classes
/dev/
__APFSPurgeExtentIteratorCopyState
    keys: %9s %9s %9s %9s %9s %9s\n
\t%16p %s\n
61706673-7575-6964-0200-766f6c756d00
Write burst: Total number of bytes written
com.apple.apfs.iterator.extent.purge.cursor.urgency
%s:%d: %s iter_next returned %d\n
IOBlockStorageDevice
suid
com.apple.apfs.stream.restore.alloc.estimate.override
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%@xp_desc=%lld 
%s:%d: %s error modifying omap: %d\n
%s:%d: %s unable to get extentref tree %lld: %d\n
purging_util.c
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
%s:%d: %s omap snapshot count %d seems excessive\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
omap_reap
bt_merge_nodes
Statistics
gbitmap_reap
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
btree_node_reap
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s tx_leave failed with error: %d\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
spaceman_set_bits_in_bm
apfs_free_data_blocks
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
0123456789ABCDEF
groupquota
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s reverting on error: %d\n
Max volume count
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
unexpected storagetype: 0x%x\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
nx_metadata_fragmented_sanity_check
nx-volume_group-lock
%@disk_free_start=%llu 
Attempting to reuse a non-candidate chunk zone info\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
jobj_validate_key_val
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
%s:%d: invalid arguments\n
%s:%d: failed to get purgeable extents for file %llu: %s (%d)\n
%s:%d: no stat info requested\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
invalid unlock flags: 0x%x\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
SnapMetadata
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
spaceman_fs_bounds_clear
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
%s:%d: failed to enable rapid-aging vnodes: %s (%d)\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
com.apple.apfs.volume.effaceable
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
apfs_reap
%s:%d: dir %llu no longer has a desired urgency\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s superblock failed sanity checks: %d\n
com.apple.apfs.volume.encrypted.acm
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
%s:%d: %s btree check called with non-root btree node: %d\n
apfs-incompat-features-lock
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
APFSPurgeExtentIteratorCreate
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
%s:%d: %s unable allocate space that should be there: %d\n
APFSContainerResizePrepare
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
object-cache-lock
nx_tx_wait_closed
FileInfo
sha3_384_4k
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
wb_period_threshold
APFS_INODES
%@src_fsroot_nodes=%llu 
%@msg='%s' 
omap_sanity_check
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%@num_files=%zu 
61706673-7575-6964-0300-766f6c756d00
spaceman_chunk_zone_info_compare
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
setup_metadata_rolling
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
obj_cache_graft_attach
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
nx_reaper_add_sub_object
AppleAPFSMedia
%@num_total_dirs=%zu 
    keys: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s cib %lld index %d should be %lld\n
nx_check_recent_sanity_omap
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
%s:%d: %s tx xid %lld took %lld us to close\n
%@dev=%s result=%d 
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
Number of files
%@ranges_to_move=%zu 
demomode
spaceman_ip_freed
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
jobj_size_for_large_key_val
%s:%d: reaper thread is exiting, returning EBUSY\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s unable to get snapshot tree: %d\n
%s:%d: %s failed to fix up checkpoint data: %d\n
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
com.apple.apfs.volume.reserve_size
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
Invalid
%s\n
defragment=yes
bt_remove_internal
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: %s spaceman chunks per cib is bad: %d\n
obj_checkpoint_start
uuid_from_role
spaceman_chunk_zone_info_recent_decrement
com.apple.apfs.container.extaddr
spaceman_free_extent_cache_reset
tx_unmount
%s:%d: %s First sync/barrier failed: %d\n
not handling the current tx!\n
%@src_fsroot_2nd_nodes=%llu 
perm
com.apple.apfs.volume.volume_uuid
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
apfs-global-snap-lock
nx_checkpoint_traverse
CloneMap
spaceman-free-lock
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
empty_password
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
VCCInput1
<80
i8@?0
%sr%s
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
sha3_512
61706673-7575-6964-0180-766f6c756d00
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%@tgt_fsroot_nodes=%llu 
%s:%d: %s lookup returned unexpected error while iterating: %d\n
create_handle_lock
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
com.apple.apfs.stream.create.read.alignment
com.apple.apfs.stream.restore.skip.snapshot
apfs_roll_keygen
%s:%d: *** unknown obj type %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
omap=physical
btree_node_val_range_validate
LockedOut
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s found mapping tree with old subtype\n
password=
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
apfs-dir-size-lock
dir
START
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
CryptoState
authapfs_validate_node
%s:%d: %s unable to get omap: %d\n
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s *** unknown expanded obj type %hhu\n
obj_cache_flush_prepare
obj_cache_remove
apfs-integrity-meta-lock
%s:%d: %s obj_modify() failed: %d\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
%s:%d: %s tx manager initialization failed: %d\n
wb_average_capacity
obj_modify
%s:%d: %s Failed to get next extent: %d\n
%@full_clones=%llu 
supplemental_tree_destroy
com.apple.apfs.iterator.extent.purge.path
type = %u, req_tree != fs_root\n
apfs-pfkur-tree-oid-lock
%s:%d: %s Invalid reap list free entry %d\n
com.apple.apfs.iterator.extent.purge.cursor.atime
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
Removable
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: %s object cache initialization failed: %d\n
%s:%d: %s reap list object free list erroneously empty?\n
%s:%d: %s waiting for available tx to open: xid %lld\n
%@purge_all=%llu 
v0,sha512
%s:%d: %s btree_node is null\n
apfs-dir-stats-id-lock
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
%s:%d: %s failed to get omap tree for reaping: %d\n
spaceman-space-usage-lock
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
tx_leave
defwrite
spaceman-ip-lock
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
apfs_reap_extentref_blocks
iterate_purge
<UNKNOWN>
nx_check_superblock
bt_merge_up
spaceman_allocation_init
com.apple.apfs.volume.create_synchronous
%s:%d: %s spaceman IP bm block count is bad: %d\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
parse_options_into_args
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
auto
automounted
btree_iterate_nodes
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
SYSTEM_GRAFT_4K_OBJS
61706673-7575-6964-01c0-766f6c756d00
%s:%d: %s error searching spaceman free queue tree: %d\n
getDeviceHandle
capacity: leaves %llu / %llu => %.2f %% used\n
obj_init
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
nx-txn-blocks-lock
%@%s:%d 
AppleAPFSContainer
jfs_get_tree_in_snap
%ss%d:%lld
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
io_get_device_features
PurgeableTombstone
spaceman_modify_bits
nx_superblock_agrees_with_container_superblock
APFS
%s:%d: %s invalid object size: %d size_phys %d\n
_APFSVolumeRemoveUnlockRecordsOrHint
%s:%d: %s unable to get spaceman: %d\n
%s:%d: %s spaceman IP bitmap free head %d out of range\n
virtual
spaceman-lock
APFSGetExclavePath
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
%s:%d: %s unable to get prev doc-id tree: %d\n
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
? 01234567890abcdefghijklmnopqrstuvwxyz+-*/_'#$&%()=[]\"\\
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
spaceman_alloc_fxc_scan_wait
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
APFSContainerCommitTemporaryCheckpoint
%s:%d: %s unable to get snap meta tree %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
apfs_sanity_check_tree_type
%s:%d: stop iteration requested\n
tx_finish
nx_mount
APFSGetFragmentationHistogram
apfs-phys-lock-state-mutex
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
(ent->fts_info == FTS_D) || (ent->fts_info == FTS_F)
wb_average_time_between
%s:%d: %s ***: expanded obj type found on unsupported volume\n
obj_read
invalid crypto index %d\n
apfs-omap-lock
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: %s cab %d index %d should be %d\n
nx_reaper_add_ext
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
spaceman_checkpoint_traverse
com.apple.apfs.volume.name
APFSStreamRestoreWrite
apfs-flags-lock
%s:%d: %s tree_iter_init() returned %d\n
%@purge_full_2=%llu 
sha512_256
%s:%d: %s Tree iteration threw %d at cursor %llu\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
%s:%d: %s tx_finish() failed, %d\n
%@data_ondisk_hardlnks=%llu 
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
physical object dirty count underflow\n
spaceman_free_extent_cache_remove
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
%s:%d: %s object cache bootstrap failed: %d\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
nx_tx_finish_wait
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
spaceman-czic-scan-lock
com.apple.apfs.volume.fs_index
match_jobj_expanded_type_to_tree_type
<%d
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s Final sync/barrier failed: %d\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
keygen_nvram_prop
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s unable to get fs snap meta tree: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
com.apple.apfs.volume.cprotect
apfs-global-lock
%s:%d: failed to read fd from fts: %s (%d)\n
nx-resize-spaceman-lock
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
%@max_stack=%zu 
case=insensitive
VCCInput0
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s doc-id tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
fstree=btree
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
APFSVolumeResetUnlockRecordWithOptions
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
FULL
nx_reaper_checkpoint_traverse
61706673-7575-6964-0020-766f6c756d00
btree_node_insert_internal
%s:%d: %s unable to allocate chunk zone info cache\n
nx_metadata_range_add
%@purge_full=%llu 
com.apple.apfs.volume.group_sibling_fsindex
Extentref tree node count
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%@num_sb=%zu 
sha3_384
spaceman-czic-lock
make_large_jkey_header_from_jobj
nx_check_omap
%@encoded_len=%zu 
Root tree node count
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
%s:%d: object memory manager failed to create lock, error: %d\n
Expanded
sha512
checkpoint
APFS_BTREE_NODES
sealed, fext, req_tree != fs_root
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
APFS_TREE_LOOKUP_ZONE
%@src_fsroot_2nd_depth=%llu 
bt_lookup_copy_out
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
lookup_jobj_ext
%s:%d: %s failed to delete mapping, error: %d\n
Physical Interconnect Location
%@tmp_blk=%llu 
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
%s:%d: %s Hit %d looking up first snapshot\n
spaceman_free_extent_cache_setup
61706673-7575-6964-0008-766f6c756d00
btree_node_child_val
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
Reference count overflowed for object %p!\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
e-apfs
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
btree_check_ext
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
object-cache-reset-lock
%s:%d: failed to get fd for fts: %s (%d)\n
mount_apfs
com.apple.apfs.container.extlist
Histogram for number of files per directory, number of buckets is
<20
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s bogus phase, %u\n
%@max_mem=%llu 
btree_node_child_id_update
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
fts_read_fd_
BSD Minor
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
APFSPurgeExtentIteratorCreateWithState
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
omap=btree
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: %s reaper has tail with no head\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
%@ever_cloned=%llu 
%@data_num_hardlnks=%llu 
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
btree_node_key_range_validate
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
com.apple.apfs.volume.noautomount_at_create
AppleAPFSVolume
level %d: %d nodes %.2f average descendents\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
%@data_size_fclones=%llu 
authapfs_integrity_meta_get_internal
jobj_release
%s:%d: failed to get purgeable extents: %s (%d)\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
nx_reap_list_sanity_check
spaceman_fxc_update_smallest_with_successor
%s:%d: %s error getting next checkpoint data block address %d: %d\n
%@time=%llu 
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
obj_get_async_read
%s:%d: urgency %#06x done\n
supplemental_tree_get_descriptor
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
obj_cache_remove_new_fs_objects
spaceman_fxc_print_stats
nx_tx_finish_wait_for_dirty_data
omap_recent_sanity_callback
com.apple.apfs.container.fstype
Role
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
level %d: %d nodes\n
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s waiting for transaction to finish\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
%s:%d: %s unable to get fs root tree: %d\n
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
current tx not closed/flushing?!\n
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
IOService
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
nx_check
fd_dev_read_helper
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
61706673-7575-6964-0240-766f6c756d00
spaceman_set_up_ip_reverse_mapping_tree
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
com.apple.apfs.iterator.extent.purge.batch_size
APFSStreamFingerprintWrite
btree_node_check
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
apfs-doc-id-lock
%@num_cg=%zu 
dev_init
fd_dev_write_extended
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
make_purgeable_extents_iterator
%s:%d: failed to allocate memory for extent iterator\n
%s:%d: failed to open fts on ino %llu: %s (%d)\n
tx-mgr-lock
tinyobjcache
sha3_256_4k
%s:%d: %s failed to move all entries: %d\n
APFSVolumeConvertToUserCrypto
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
%s:%d: failed to get path for ino %llu: %s (%d)\n
com.apple.apfs.iterator.extent.purge.urgency
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: fts_read() returned error: %s (%d)\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
nx_tx_wait_open
protect
61706673-7575-6964-0010-766f6c756d00
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
com.apple.apfs.iterator.extent.purge.version
Internal
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
%@features=0x%llx 
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
/dev/rdisk%llus%llu
dev_init_common
ro
61706673-7575-6964-02c0-766f6c756d00
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%@snap_t=%llu 
%@disk_free_curr=%llu 
%s:%d: wrlock == 0 failed %d\n
fsquota=
spaceman_ip_block_alloc
large_key_val_to_jobj
%s:%d: %s spaceman cab count is bad: %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
spaceman_sanitize_datazones
%s:%d: %s validation failed for checkpoint at index %d: %d\n
com.apple.apfs.iterator.extent.purge.options
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
%@freeQ_d=%lld 
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
stream_restore_lock
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s failed to get reap list head: %d\n
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
com.apple.apfs.volume.allow_unwritten
jobj_allocate
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
%s:%d: %s unable to get spaceman free queue tree: %d\n
/Library/Caches/com.apple.xbs/459BBF28-708D-4433-906E-92FA8362163B/TemporaryDirectory.3gCnMN/Sources/apfs_framework/nx/obj.c
61706673-7575-6964-0004-766f6c756d00
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
apfs_sanity_check
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
obj_checksum_verify
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%d: %s failed to update rightmost leaf field: %d\n
Histogram for number of files of sizes in a specific range, number of buckets is
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s/apfs_data
obj_delete_internal
Total Size of purgeable files
%s:%d: *** Can't release unknown obj type %d\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
disk
%@total_t=%llu 
btree_node_compact
%s:%d: %s failed to update allocate zone %llu: error %d\n
com.apple.apfs.stream.create.embed.crc
key_val_to_jobj
%s:%d: expected inode entry but got nothing\n
AppleAPFSSnapshot
nx_tx_wait_closing
%s:%d: %s error getting cab %d @ %lld: %d\n
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
%s:%d: can't get features for device (%s)\n
not handling the flushing tx!\n
omap_find_next_snapshot_xid
bt_shift_or_split
spaceman_trim_free_extent_callback
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
%s:%d: can't get block count (%s)\n
w:
%llu%s
Object mapping tree node count
%s:%d: %s prev doc-id tree sanity check failed: %d\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
untitled
rw
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
nx-omap-lock
spaceman_chunk_zone_info_list_remove
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
tx_checkpoint_write
%s:%d: %s xid %lld second sync/barrier failed: %d\n
spaceman_chunk_zone_info_recent_increment
spaceman_freed
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s omap_destroy returned %d!\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%@dirstats=%llu 
recent zone chunk should have only ONE reference when being moved to the recent list!\n
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
%s:%d: failed to open volume device %s: %s\n
%s:%d: expected inode entry but got extent %#llx:+%#llx\n
Purgeable
%@mnt_t=%llu 
%s:%d: Corrupt xattr in ino %llu\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
61706673-7575-6964-0001-766f6c756d00
spaceman_fq_tree_find_overlap
apfs-im-cache-lock
61706673-7575-6964-0002-766f6c756d00
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s Error %d, reinitializing\n
authapfs_validate_node_hash
%s:%d: %s Fusion is not supported anymore\n
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s spaceman IP base address is bad: %lld\n
Reference count underflowed for object %p!\n
nx_reaper_sanity_check
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%@oc_miss=%llu 
createtmpcp
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
obj_alloc
nx_tx_wait
IODeviceTree:/filesystems
omap=ephemeral
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
Device Characteristics
nx_tx_wait_frozen
%s:%d: %s couldn't allocate memory for checkpoint map block\n
com.apple.apfs.volume.quota_size
capacity: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
%@findcg_t=%llu 
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
gid=
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
APFS_4K_OBJS
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
Number of snapshots
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s reaper check failed with error: %d\n
rolling-stats-lock
nx_tx_wait_closed_prev_flushing
DirSize
role=
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
spaceman_free_extent_cache_insert
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s unsupported tree type: %d\n
%@num_sc=%zu 
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
spaceman_free_completed
%s:%d: %s container block size too small for device block size (%d < %d)\n
Backoff
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
%s:%d: can't get solidstate for device (%s)\n
SiblingMap
%@vers=%s 
omap_cleanup
com.apple.apfs.container.extlen
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
committmpcp
com.apple.apfs.container.blksize
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
APFSCaptureFinishCaptureForFile
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
%s:%d: %s extentref tree %lld: %d\n
Protocol Characteristics
%@decloned=%llu 
%s:%d: %s probe of external device... skipping recent sanity checks.\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
w
%s:%d: expected file %llu but got mode %#o ino %llu\n
com.apple.apfs.container.tidemark
_APFSVolumeOperation
System
=%d
%s:%d: %s omap xid %lld > spaceman xid %lld\n
%s:%d: %s failed to initialize free extent cache, error %d\n
 
%@mv_t=%llu 
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
spaceman_clear_bits_in_bm
APFSContainerGetBootDevice
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s tx xid %lld took %lld us to flush\n
conformance
rdonly
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
obj_create_internal
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
spaceman_fxc_tree_node_recycle_smallest
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
obj_checkpoint_known
image-format-read-only
dev
btree_node_insert
%s:%d: processing dir %llu\n
%s:%d: failed to skip fts for ino %llu: %s (%d)\n
%s:%d: %s failed to get object oid %lld: %d\n
spaceman_get_metazone_alloc_index
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
new address mismatch on redirty 0x%llx 0x%llx\n
spaceman_fxtp_add_child
%@pure_cloned_apps_blk=%llu 
%@tmp_cloned_blk=%llu 
fsreserve=
spaceman_cib_sanity_check
nx_mount_initiate_free_space_trims
APFSContainerGetFreespaceInfo
%s:%d: %s snap meta tree %lld: %d\n
obj_checkpoint_done
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
btree_node_entry_update
%s:%d: %s Tree delete oid %llu threw %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
Release count overflowed for object %p!\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
APFS_8K_OBJS
IOMedia
sha3_512_4k
61706673-7575-6964-0040-766f6c756d00
61706673-7575-6964-0080-766f6c756d00
btree_node_sanity_check
spaceman_chunk_zone_info_cache_init
spaceman_ip_bm_block_alloc
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
__APFSPurgeExtentIteratorCreate
nx_check_reaper
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: failed to get bulk purgeable extents: %s (%d)\n
%s:%d: unexpected mode %#o for ino %llu\n
spaceman_free_extent_cache_search
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%@source_meta_size=%llu 
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
Small free extents count
%s:%d: %s Can't get tree: %d\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: failed to init extended fields on drec %lld from blob.\n
%@ip_freeq_start=%llu 
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
nx-tree-node-compact-lock
APFSPurgeExtentIteratorIterate
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s failed nx_check sanity: %d\n
jobj_validate_large_key_val
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
apfs_checkpoint_traverse
%s:%d: %s Trash unfinished tx xid=0x%llx\n
PhysExtent
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
virtual object dirty count underflow\n
SiblingLink
61706673-7575-6964-00c0-766f6c756d00
%s:%d: %s obj_modify(fs %lld) failed: %d\n
iterate_purge_directory
nx_tx_flush_busy
Inode
authapfs_valid_hash_type
make_jkey_from_jobj
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
spaceman_fxc_update_length
%s:%d: %s %s tree: PATH TOO LONG: %d\n
sealed=yes
61706673-7575-6964-0280-766f6c756d00
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
Number of purgeable files
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
Target Disk Mode
%@num_src=%llu num_dst=%llu 
/
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
spaceman_unreserve
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
%s:%d: %s failed to write superblock to block 0: %d\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: %s cab %d cib count %d should be %d\n
follow
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
nx_dev_init
3288.52.1
delta_canonicalize_record
owners
%s:%d: %s spaceman blocks per chunk is bad: %d\n
paddr
%@tgt_fsroot_depth=%llu 
spaceman_metazone_init
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
ephemeral
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
apfs-fext-tree-oid-lock
nx_unblock_physical_range
unwritten
Number of volumes
VCParams
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
io_get_device_block_size
%s:%d: %s error unreserving space, %lld blocks: %d\n
apfs-phys-ext-oid-lock
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
spaceman_chunk_zone_info_add
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
<60
length
BSD Major
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
%s:%d: APFS_IOUC_VOLUME_CONVERT_TO_USER_CRYPTO failed for disk %s: %s
%s:%d: invalid state dictionary\n
%s:%d: UR_WIPE [ VOLUME = %s, ret = %d ]\n
%s:%d: kAPFSPurgeExtentIteratorOptions was not an integer CFNumber\n
%s:%d: kAPFSPurgeExtentIteratorCursorUrgency was not an integer CFNumber\n
%s:%d: tx_enter failed: %u\n
%s:%d: invalid options dictionary\n
%s:%d: kAPFSPurgeExtentIteratorUrgency was invalid (%llu)\n
%s:%d: failed to get requested attributes: %s (%d)\n
%s:%d: kAPFSPurgeExtentIteratorPath was not a valid CFString\n
%s:%d: options was not a CFDictionary\n
%s:%d: UR_RESET_UPDATE [ OP = %u, SRC UUID = %s, DST UUID = %s, VOLUME = %s, ret = %d ]\n
%s:%d: failed to create bsd name for container: %llx\n
%s:%d: delta_canonicalize() returned EILSEQ...\n
%s:%d: failed to get exclave base dirs, error %d (%s)
%s:%d: fsgetpath failed for base_dir %llu, error %d (%s)
%s:%d: invalid source of APFS container\n
%s:%d: nvram is not supported on this system\n
%s:%d: failed to get free extent info from spaceman, error = %d\n
%s:%d: Failed to transfer extents from %s to %s: %d
%s:%d: failed to allocate source callback state\n
%s:%d: Failed to set io registry property for key %s: %s (0x%08x)\n
%s:%d: incorrect version (actual %llu, expected %u)\n
%s:%d: invalid combination of options (actual %#llx, expected %#llx)\n
%s:%d: state was not a CFDictionary\n
%s:%d: kAPFSPurgeExtentIteratorCursorUrgency was invalid (%llu)\n
%s:%d: container_iouc failed for disk %s: %s
%s:%d: kAPFSPurgeExtentIteratorUrgency was not an integer CFNumber\n
%s:%d: kAPFSPurgeExtentIteratorBatchSize was not an integer CFNumber\n
%s:%d: failed to create APFS volume match dictionary\n
%s:%d: failed to allocate memory for exclave base dirs (%d base dirs were requested)
%s:%d: APFS_IOUC_CONTAINER_RESIZE_PREPARE for %s %lld failed with %d\n
%s:%d: cant find entries matching %s - %s\n
%s:%d: could not open metrics log file %s: %s
%s:%d: timed out waiting for container quiet after op %d on volume %s\n
%s:%d: Failed to create CFstring string from C string %s\n
%s:%d: failed to create state dictionary\n
%s:%d: failed to get parent for volume 0x%llx\n
%s:%d: computed_len=%llu, embedded_len=%llu\n
%s:%d: failed to generate metadata rolling keys for the DATA volume in APFS container %s, error = %d\n
%s:%d: Failed to find property with the key %s\n
%s:%d: invalid arguments (active %#x, optional %#x, required %#x)\n
%s:%d: failed to open path: %s (%d)\n
%s:%d: kAPFSPurgeExtentIteratorVersion was not an integer CFNumber\n
%s:%d: kAPFSPurgeExtentIteratorCursorAtime was not an integer CFNumber\n
%s:%d: failed to load the container\n
%s:%d: comp_crc=0x%x embed_crc=0x%x\n
%s:%d: UR_REMOVE [ UUID = %s, tag = %d, VOLUME = %s, ret = %d ]\n
%s:%d: kAPFSPurgeExtentIteratorOptions must include at least one option\n
%s:%d: failed to retrieve tidemark from free extent info in spaceman\n
%s:%d: volume roles property isnt of correct type. Expected CFArray\n
%s:%d: Failed to create fragmentation histogram entry for %s\n
%s:%d: Failed to move file %s to %s: %d
%s:%d: iterate_purge() returned with ret = %d\n
%s:%d: found multiple data volumes\n
%s:%d: failed to stat: %s (%d)\n
%s:%d: failed to lookup data volume - %s\n
%s:%d: Cannot fetch information about volume '%s' - %s\n
%s:%d: failed to get the APFS container disk path CString from source\n
%s:%d: Failed to create fragmentation histogram array for %s\n
%s:%d: failed to load the container: %u\n
%s:%d: kAPFSPurgeExtentIteratorOptions had invalid options specified (%#llx)\n
%s:%d: unexpected attributes were returned\n
%s:%d: failed to allocate source handle\n
%s:%d: failed to create purgeable extent iterator: %s (%d)\n
%s:%d: fsctl failed with ENOSPC, retrying...
%s:%d: UR_ADD_UPDATE_SET [ OP = %u, SRC UUID = %s, DST UUID = %s, VOLUME = %s, ret = %d ]\n
%s:%d: Cannot get index of volume '%s'\n
%s:%d: creating a purge extent iterator is currently only supported on the root of an enhanced apfs volume\n
%s:%d: failed to get exclave base dirs (number of records), error %d (%s)
%s:%d: failed to get exclave base dirs after retries
%s:%d: UR_ADD_UPDATE_SET [ OP = %u, UUID = %s, VOLUME = %s, ret = %d ]\n
%s:%d: failed to allocate APFSPurgeExtentIterator\n
%s:%d: failed to get parent for container 0x%llx\n
%s:%d: len=%llu embed_len=%llu\n
%s:%d: computed_crc=%x, embedded_crc=%x
%s:%d: tx_leave failed: %u\n
%s:%d: failed to get block size from source\n
%s:%d: kAPFSPurgeExtentIteratorBatchSize was invalid (%llu), must be between %u and %u\n
%s:%d: cannot create state from a completed iterator\n
%s:%d: failed to get the APFS container device handle\n
```
