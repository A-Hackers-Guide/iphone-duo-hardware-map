# `/System/Library/Filesystems/apfs.fs/apfs_condenser`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 457,040 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2000)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

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
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
</dict>
</plist>
```

## Strings (1,266)

```
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
spaceman_sanitize_datazones
%s:%d: ***: unknown obj type %d\n
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
bt_remove_internal
%s:%d: %s Error reinitializing free extent cache: %d\n
not handling the current tx!\n
%s:%d: apfs_mount failed with error -> %d\n
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
jobj_allocate
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
nx_mount_initiate_free_space_trims
** Number of new fsroot tree nodes %lld\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
%s:%d: %s Failed to get next extent: %d\n
spaceman_fxc_print_stats
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
btree_check_ext
%s:%d: %s couldn't allocate memory for superblock of size %d\n
spaceman_free
nx_metadata_range_add
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: %s object type 0x%x not reapable?: %d\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
invalid lock flags: 0x%x\n
!((apfs)->apfs_main_apfs != ((void*)0))
** Done!\n
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: rdlock == 0 failed %d\n
apfs-omap-lock
%s:%d: %s omap_destroy returned %d!\n
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
%s:%d: %s failed to get omap tree for reaping: %d\n
nx_check_omap
%s/apfs_data
%s:%d: failed to open volume device %s: %s\n
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
spaceman_free_extent_cache_setup
Get count overflowed for object %p!\n
IOMedia
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
omap_find_next_snapshot_xid
spaceman_decrement_free_queue_count
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
protect
invalid unlock flags: 0x%x\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
apfs-incompat-features-lock
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: %s failed to clean up doc-id trees, error %d\n
supplemental_tree_get
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
spaceman_ip_bm_block_free
spaceman_alloc_iterate_chunks
%s:%d: %s ***: expanded type seen on in-memory obj\n
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s failed to delete prev doc-id tree, error %d\n
    keys: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%d: %s obj_modify() failed: %d\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
authapfs_validate_node
%s:%d: %s not enough space to enter transaction\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
DELETE
btree_delete
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
nx_reaper_add_ext
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
current tx not closed/flushing?!\n
%s:%d: remove_snapshot failed with error -> %d\n
%s:%d: %s failed to delete mapping, error: %d\n
%s:%d: failed to init extended fields on drec %lld from blob.\n
check_stale_doc_id_index
%s:%d: %s encryption type %llx unsupported\n
obj_cache_flush_prepare
omap_expunge_oids_below_watermark
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
rdonly
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
supplemental_tree_destroy
nx_check_recent_sanity_omap
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
nx_tx_wait_frozen
Copied %llu fsroot tree records into new fsroot tree\n
physical size
%s:%d: %s failed to get doc-id tree key count, error %d\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
snap_name
ro
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s failed to fetch the extentref tree (error %d)\n
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
spaceman_set_bits_in_bm
apfs_crypto_mount
%s:%d: %s doc-id tree sanity check failed: %d\n
nx-volume_group-lock
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s failed to initialize free extent cache, error %d\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
spaceman-czic-scan-lock
apfs-doc-id-lock
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
%s/apfs
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
** Deleting old fsroot tree by invoking omap_expunge_oids_below_watermark\n
fsroot_iterator
%s:%d: %s failed to get reap list tail: %d\n
mark_doc_id_index_for_rebuild_if_needed
btree_node_check
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
%s:%d: %s find_next_snap(%llu) returned %d\n
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
apfs-integrity-meta-lock
nx_reap_list_sanity_check
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: obj is NULL or not apfs object!\n
jobj_merge_maybe_clamp_64
%s:%d: %s error getting next checkpoint map block address %d: %d\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
watchdog_timeout
    -v    Enable verbose output.\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
%s:%d: %s object type 0x%x not reapable: %d\n
set_cloneinfo_id_epoch
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
%s:%d: %s tx_finish() failed, %d\n
0
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
%s:%d: Unable to start a new transaction due to error -> %d\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
UNKNOWN TXN TYPE
obj_cache_remove_graft_persistent_ephemeral
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
AppleAPFSVolume
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
%s:%d: %s spaceman chunk count is bad: %lld\n
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s Fusion is not supported anymore\n
** Moving snapshot %s to purgatory..\n
quarantine
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
spaceman_fxc_update_length
obj-mem-mgr-lock
** Updating the superblock..\n
nx_corruption_detected_int
spaceman_chunk_zone_info_add
%s:%d: %s extentref tree %lld: %d\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
jobj_to_key_val
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
dev
Requested forced secondary_fs_root but the tree is missing\n
addition
%s:%d: graft with invalid fs block size: %u\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
dev_init
nx-omap-lock
%s:%d: %s failed to delete doc-id tree, error %d\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s invalid object size: %d size_phys %d\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
RR_HOLE
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s omap tree sanity check failed: %d\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
obj_cache_flush_write
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: can't get block count (%s)\n
obj_create_internal
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
%s:%d: %s reaper has tail with no head\n
fs_tx_enter_internal
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
3288.52.1
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: Please delete remaining %llu snapshots before running the condenser\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
duplicate_jobj_op_to_shadow_fs_root
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
spaceman_metazone_init
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
nx_tx_finish_wait
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
%s:%d: %s omap xid %lld > spaceman xid %lld\n
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
** obj_id of current fsroot tree <%lld> and that of new fsroot tree <%lld>\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%s:%d: rmdir %s returned an error -> %s\n
io_get_num_device_blocks
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
nx-tree-node-compact-lock
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
spaceman_alloc_fxc_scan_wait
rolling-stats-lock
%s:%d: %s failed to find valid checkpoint: %d\n
virtual object dirty count underflow\n
obj_checkpoint_known
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
nx_tx_wait_open
apfs_condenser
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
obj_delete_internal
%s:%d: %s unable to get snapshot tree: %d\n
%s:%d: %s failed to enter tx - %s(%d)\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
nx_checkpoint_load_data
Release count overflowed for object %p!\n
spaceman_cib_sanity_check
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
invalid tweak type %d\n
spaceman_free_fs_deduct_block_counts
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
spaceman_free_extent_cache_search
obj_modify
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
btree_node_entry_update
%s:%d: %s fs extentref tree sanity check failed: %d\n
obj_cache_remove_reverted_fs_objects
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
tx_leave
owners
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
%s:%d: %s failed nx_check sanity: %d\n
tx_checkpoint_write
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
obj_checkpoint_done
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
%s%s%llx
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
%s:%d: spaceman_info failed with error -> %d\n
spaceman_get_metazone_alloc_index
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
spaceman_trim_free_extent_callback
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
** Spaceman free queue count <%llu> and xid is <%llu>\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
btree_node_insert_internal
not handling the flushing tx!\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
apfs-phys-lock-state-mutex
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
removal
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%d: %s Inserting snap_name failed, %d\n
%s:%d: %s failed to get doc-id tree, error %d\n
clear_invalid_fixups
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%d: %s object cache initialization failed: %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
%s:%d: omap_expunge_oids_below_watermark failed with error -> %d\n
jfs_get_tree_in_snap
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
nx_tx_wait_closed_prev_flushing
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s First sync/barrier failed: %d\n
update
apfs_create_doc_id_tree_if_needed
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
spaceman_free_extent_cache_remove
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
capacity: leaves %llu / %llu => %.2f %% used\n
nx_checkpoint_find_valid_checkpoint
spaceman_fxc_tree_node_recycle_smallest
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
jobj_validate_key_val
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
orphan_snap_check_iterator
%s:%d: can't get features for device (%s)\n
%ss%d:%lld
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
ephemeral
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: %s sanity checking all container state... please be patient.\n
obj_cache_remove
Reference count underflowed for object %p!\n
,
%s:%d: %s fext_tree_remove returned %d\n
=%d
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
spaceman-dev-lock
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
obj_checkpoint_start
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
Physical Interconnect Location
apfs_reap_extentref_blocks
%s:%d: %s couldn't allocate memory for checkpoint map block\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
spaceman_fq_tree_insert
purgatory.
rdisk
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
\t%16p %s\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
spaceman_sanity_check
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
AppleAPFSContainerScheme
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
bt_merge_up
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%s:%d: tree_node_count for current fsroot tree failed\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
<%d
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s container cleanly-unmounted flag set.\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: Using a reserved name %s for a snapshot is disallowed\n
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s unable to get omap snapshot tree: %d\n
nx_reaper_obj_get
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
** Entering a transaction..\n
Device Characteristics
dev_init_common
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s reverting on error: %d\n
%s:%d: %s failed to fix up checkpoint data: %d\n
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s Final sync/barrier failed: %d\n
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
%s:%d: tx_leave failed with error -> %d\n
Internal
total_count
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
nx_check_superblock
nx_reaper_add_sub_object
descendants
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
bt_lookup_copy_out
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
object-lock
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
capacity: all    %llu / %llu => %.2f %% used\n
spaceman_fxtp_add_child
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
spaceman_fxc_update_smallest_with_successor
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
obj_init
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s object cache bootstrap failed: %d\n
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
%s:%d: %s xid %lld sync/barrier failed: %d\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
unexpected storagetype: 0x%x\n
spaceman_get_new_chunk_for_allocation_zone
nx_get_evict_mapping_tree
%s:%d: %s tx_leave failed with error: %d\n
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
setup_demo_mode
btree_node_space_stats
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
spaceman_unreserve
sealed, fext, req_tree != fs_root
%s:%d: %s X %d\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
apfs_sanity_check
%s:%d: %s set apfs_fixup_flags to %#llx\n
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
fs_index
** Finishing transaction..\n
Removable
%s:%d: %s spaceman IP block count is bad: %lld\n
insert_jobj
%s:%d: don't know how to merge refcounts on objects of type %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
APFS_4K_OBJS
START
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s error searching spaceman free queue tree: %d\n
** Number of current fsroot tree nodes %lld\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
loadtmpcp
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
spaceman_chunk_zone_info_recent_decrement
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
** Deleting old fsroot tree..\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
apfs_free_data_blocks
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
omap_cleanup
%s:%d: %s waiting for transaction to finish\n
%s:%d: apfs_crypto_mount(%s) failed with error -> %d\n
watchdog timer not created for condenser
gbitmap_reap
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
jobj_size_for_key_val
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
lookup_jobj_ext
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: %s Can't get tree: %d\n
spaceman_chunk_zone_info_recent_increment
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
nx-global-extent-manipulation-lock
spaceman_iterate_free_extents_internal
jobj_type_from_possibly_large_key
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
new address mismatch on redirty 0x%llx 0x%llx\n
%s:%d: %s waiting for available tx to open: xid %lld\n
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s failed to fetch the fext tree (error %d)\n
%s:%d: %s *** unknown expanded obj type %hhu\n
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
apfs-clonegroup-lock-mutex
jobj_to_large_key_val
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
bt_shift_or_split
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
obj_alloc
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s mount for ramdisk\n
nx_tx_wait_closing
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
object-cache-flush-lock
spaceman_check_allocation_status_internal
groupquota
apfs-snapmeta-oid-lock
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
createtmpcp
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s unable to get omap tree: %d\n
%s:%d: %s failed to write superblock to block 0: %d\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
spaceman_fq_tree_find_overlap
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
apfs
%s:%d: %s lookup_next_snapshot() returned %d\n
%s/nx
FIXUP
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
resource fork size
object-cache-lock
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s omap snapshot count %d seems excessive\n
key_val_to_jobj
%s:%d: %s btree check called with non-root btree node: %d\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
%s (%s)
omap_sanity_check
io_get_device_features
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
apfs-pfkur-tree-oid-lock
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
%s:%d: Couldn't unmount %s, err %d\n
%s:%d: Could not look up metadata for snapshot %s\n
%s:%d: Could not delete snapshot '%s' because volume '%s' is set to root from it\n
apfs-snap-delete-lock
fs_tx_leave_ext
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
obj_checkpoint_check_for_unknown
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
/dev/
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
cst %llu hit zero retain count but still has ep related retain count (%u)\n
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
suid
apfs_checkpoint_traverse
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%s:%d: %s Inserting snap_meta failed, %d\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s failed to create reap list: %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
capacity: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
nx_tx_wait_closed
%s:%d: nx_mount failed with error -> %d\n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
nx_mount
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
apfs-im-cache-lock
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
MODVAL
btree_node_sanity_check
Reference count overflowed for object %p!\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
fs_rename_snapshot
%s:%d: %s fs root tree sanity check failed: %d\n
purgeable size
%s:%d: %s superblock failed sanity checks: %d\n
apfs_reap
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
%s:%d: %s failed to set up spaceman for demo mode: %d\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s failed to remove first, error %d\n
%s:%d: %s unable to get reaper: %d\n
nx-txn-blocks-lock
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
object-cache-list-lock
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
APFS_BTREE_NODES
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
full clone size
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
apfs_sanity_check_tree_type
Invalid fs index: %s
move_snapshot_to_purgatory
clone size
%s:%d: *** unknown obj type %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
%s:%d: %s failed to leave tx, error %d\n
%s:%d: could not mount the volume due to an error %d\n
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
level %d: %d nodes\n
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
remove_snapshot
apfs-global-snap-lock
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
%s:%d: %s set cloneinfo_id_epoch to %llu\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
spaceman_trim_free_blocks
s:i:p:vw:
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
automounted
match_jobj_expanded_type_to_tree_type
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
  values: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s reap list object free list erroneously empty?\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
curproc
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
tx_unmount
tinyobjcache
%s%s
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
spaceman_fs_bounds_clear
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
fd_dev_close
bt_merge_nodes
virtual
nx_tx_finish_wait_for_dirty_data
%s:%d: %s unable to get fs snap meta tree: %d\n
omap_recent_sanity_callback
apfs-stream-id-lock
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
authapfs_seal_break
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
%s:%d: %s unable to get omap: %d\n
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
btree_node_child_id_update
%s:%d: %s unsupported tree type, %d\n
key_size_for_jobj
%s:%d: %s Deleted the shadow_fs_root tree %p\n
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
spaceman_ip_freed
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: unlock == 0 failed %d\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s unsupported tree type: %d\n
disk
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: reaper thread is exiting, returning EBUSY\n
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
nx_checkpoint_find_highest_xid
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
Entered fs index (%llu) is invalid\n
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
make_jkey_from_jobj
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
com.apple.apfs.
nx_checkpoint_traverse
exp_dir_stats_refcnt_merge
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
nx_check_checkpoint_map_block
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
clean_up_doc_id_trees_if_needed
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
crypto mount -> %s\n
%s:%d: %s failed to enter tx, error %d\n
%s:%d: %s cab %d index %d should be %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
Protocol Characteristics
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
%s:%d: %s failed to fetch the integrity object (error %d)\n
make_large_jkey_header_from_jobj
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
jobj_release
nx_superblock_agrees_with_container_superblock
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
spaceman_ip_bm_block_alloc
%s:%d: %s unable to get fs root tree: %d\n
prevent_synthetic_object_operation
spaceman-fxc-lock
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
_fd_dev_write
apfs_mount
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
Attempting to reuse a non-candidate chunk zone info\n
spaceman_allocation_init
rw
attr tag
%s:%d: %s tx_enter_frozen() failed: %d\n
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
nx_check_reaper
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s:%d: %s tx_leave failed: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
Please provide a device path\n
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s snap meta tree %lld: %d\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
num children
obj_cache_remove_new_fs_objects
obj-id %llu type %u still has refcount %d\n
** Iterating over fsroot tree records..\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
tx_checkpoint_space_check
%s:%d: Could not delete snapshot '%s' because volume '%s' is set to revert to it at the next mount\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s container block size too small for device block size (%d < %d)\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
IOBlockStorageDevice
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
obj_checksum_verify
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
tx_mgr_free_tx
auto
blocks_in_txn
level %d: %d nodes %.2f average descendents\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
spaceman-lock
/private/var/tmp/RecoveryTemp
%s:%d: %s error getting cab %d @ %lld: %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
exec
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
%s:%d: %s omap snapshot tree sanity check failed: %d\n
%s:%d: %s overprovisioning volume can only mount r/o\n
physical object dirty count underflow\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
btree_check_recent_sanity
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
spaceman_modify_bits
%s:%d: %s Trash unfinished tx xid=0x%llx\n
** Creating a new fsroot tree..\n
spaceman-czic-lock
%s:%d: %s %lld:%lld error: %d\n
%s:%d: obj_modify returned an error -> %d\n
Target Disk Mode
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
spaceman_free_extent_cache_reset
invalid watchdog timeout in seconds: %s
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
bt_update_last_leaf
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
fd_dev_read_helper
spaceman_chunk_zone_info_compare
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
nx-resize-spaceman-lock
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
<80
spaceman_ip_block_alloc
%s:%d: %s failed to get reap list head: %d\n
atime
%s:%d: %s error getting cib %d @ %lld: %d\n
APFS_TREE_LOOKUP_ZONE
%s:%d: %s btree_node is null\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
spaceman_free_completed
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
omap_destroy
spaceman_chunk_zone_info_cache_init
APFS_8K_OBJS
%s:%d: %s unable to get doc-id tree: %d\n
%s:%d: %s omap tree type 0x%x is bad\n
spaceman_clear_bits_in_bm
authapfs_validate_node_hash
authapfs_valid_hash_type
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
apfs-global-lock
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
union
%s:%d: %s spaceman cab count is bad: %d\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
obj_release
tx_flush
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
%s:%d: device initialization failed: %d\n
nx_tx_wait_flush
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
spaceman-ip-lock
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
cst->ep_retain_count <= cst->hdr.retain_count
%s:%d: %s unable to get snap meta tree %lld: %d\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%sr%s
%s:%d: %s chunk %lld recent zone count overflow\n
follow
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
invalid crypto index %d\n
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
tx_enter_internal
 Limiting condenser to %u seconds \n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: %s created doc-id tree, oid %llu\n
type = %u, req_tree != fs_root\n
remove_jobj
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
btree_node_child_val
btree_node_val_range_validate
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
Condensing took too long!
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s:%d: failed to open container device %s: %s\n
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
obj_cache_graft_attach
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
apfs-fext-tree-oid-lock
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
nx_check_recent_sanity
jobj_validate_large_key_val
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
main
obj_checksum_verify_phys
btree_node_debug_stats
spaceman_checkpoint_traverse
mkdir: %s: %s\n
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
nx_reaper_checkpoint_traverse
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
spaceman_freed
__OSINSTALL_ENVIRONMENT
%s/apfs_condenser.%d
%s/apfs_condenser.%d.%lld
spaceman_chunk_zone_info_list_remove
defwrite
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
%s:%d: %s doc-id tree creation failed: %d\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
nx_unblock_physical_range
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: %s xid %lld second sync/barrier failed: %d\n
browse
doc_id_tree_invalid_crypto
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
/private/var/tmp
%s:%d: Could not move snapshot %s to purgatory due to error %d\n
nx_reaper
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
%s:%d: %s failed to get fsys oid %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
object-cache-reset-lock
%s:%d: %s tx xid %lld took %lld us to flush\n
fs_insert_snapshot_metadata
image-format-read-only
nx_metadata_range_optimize
%s:%d: %s ***: expanded type seen on in-memory obj!\n
exp-dir-stats
obj_checkpoint_get
omap_reap
skipsanity
%s:%d: %s failed to get omap %lld: %d\n
apfs_mount_livefs
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: %s error getting mapping tree: %d\n
** Crypto mountpoint has been deleted..\n
doc_id_tree_create
%s:%d: %s unable to get spaceman: %d\n
apfs-flags-lock
%s:%d: can't get solidstate for device (%s)\n
checkpoint
%s:%d: %s failed to create doc-id tree, error %d\n
INSERT
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
obj_mem_mgr_init
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
    -s    Name of the snapshot to be deleted.\n
userquota
%s:%d: %s unable to get fs extentref tree: %d\n
%s:%d: %s prev doc-id tree sanity check failed: %d\n
total size
Reserved space < reserved metadata: %llu < %llu\n
spaceman_set_up_ip_reverse_mapping_tree
spaceman_upgrade_sm_version_0_to_1
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s omap check failed with error: %d\n
apfs-rename-lock
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s error modifying omap: %d\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s spaceman chunks per cib is bad: %d\n
%s:%d: %s failed to get object oid %lld: %d\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
tx-mgr-lock
%s:%d: %s tx xid %lld took %lld us to close\n
%s:%d: %s Shadow fs_root does not exist\n
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
%s:%d: %s fs_update_snap_metadata() returned %d\n
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s iter_next returned %d\n
** Unmounting the volume..\n
BSD Minor
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
perm
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
apfs-dir-stats-id-lock
apfs-dir-size-lock
SNAP_DELETE_TXN
FULL
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
%s:%d: %s bogus phase, %u\n
<UNKNOWN>
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
btree_node_compact
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
jobj_size_for_large_key_val
nx_tx_wait
    -w    Watchdog timeout in seconds.\n
%ss%d
%s:%d: %s found mapping tree with old subtype\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
obj_write_prepare
Usage: apfs_condenser -p <device_path> -i <fs_index> [-s <name_of_the_snapshot>] [-v] [-w <timeout>] \n
BSD Major
assertion failed: %s
APFS_INODES
%s:%d: %s Invalid reap list free entry %d\n
<20
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%s:%d: object memory manager failed to create lock, error: %d\n
spaceman_alloc
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
tx_finish
%s:%d: Unable to create a new fs_root tree due to error -> %d\n
%s:%d: %s spaceman IP base address is bad: %lld\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
%s:%d: %s tx manager initialization failed: %d\n
nx_check
%s:%d: %s Hit %d looking up first snapshot\n
nx_reaper_sanity_check
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: %s sfq %d count underflow %lld - %lld\n
    -p    Synthesized path for the container.\n
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
apfs_release_objects
purgeable rsrc size
obj_delete_and_free_by_oid
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list for cleaning: %d\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
apfs_reap_snapshots
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
%s:%d: %s failed to attach graft to object cache: %d\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: this operation is not supported on sealed volumes\n
dir-stats
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
paddr
%s:%d: Deleting old fsroot tree returned error -> %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
obj_read
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
path
%s:%d: %s unable to allocate chunk zone info cache\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
strictatime
%s:%d: %s unable to get prev doc-id tree: %d\n
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
%s:%d: %s cab %d cib count %d should be %d\n
%s:%d: %s large key size (%u) on record (%llu) is too small\n
large_key_val_to_jobj
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
obj_destroy_complete
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
spaceman_free_extent_cache_insert
%s:%d: Number of free blocks %lld and number of current fsroot nodes %lld. There isnt enough free space to continue..\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
v8@?0
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
fs_destroy_shadow_fs_root_tree
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: Unable to insert record into new fsroot tree due to error -> %d\n
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s unable to get spaceman free queue tree: %d\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
btree_node_free_list_entry_validate
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%s:%d: wrlock == 0 failed %d\n
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
apfs-phys-ext-oid-lock
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s chunk %lld recent zone count underflow\n
%s:%d: %s failed to compare currently available space: error %d\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
btree_iterate_nodes
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
obj_get_async_read
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: Invalid or unknown hash type: %d\n
fd_dev_write_extended
val_size_for_jobj
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
%s:%d: %s tx_enter() failed: %d\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%02hhx
unable to create watchdog timer for condenser!
%s:%d: %s cib %lld index %d should be %lld\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
%s:%d: %s spaceman IP bm block count is bad: %d\n
bad pext.\n
MODKEY
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
spaceman-space-usage-lock
nx_tx_flush_busy
can't have a negative refcnt on crypto state %llu refcnt %d\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s Error: tx[%lld] failed to start: %d\n
btree_node_key_range_validate
committmpcp
%s:%d: Unable to get the volume's fsroot tree due to error -> %d\n
IOService
%s:%d: %s error updating metadata ranges tree: %d\n
<40
length
spaceman-free-lock
btree_node_insert
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
demomode
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
fs_lookup_snapshot_metadata_by_xid
supplemental_tree_get_descriptor
recent zone chunk should have only ONE reference when being moved to the recent list!\n
bt_insert
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%s:%d: Unknown subtype %d for file info object %lld\n
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
    -i    Desired filesystem slice.\n
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
nx_reaper_next_record
btree_node_reap
sanity_check_alloced_blocks
verbose
%s:%d: %s Tree delete oid %llu threw %d\n
doc_id_tree_destroy
nx_dev_init
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
spaceman_cab_sanity_check
%s:%d: iterate_raw_jobjs_with_hint failed with error -> %d\n
%s:%d: %s Couldn't rename snap %llx to %s\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
fd_dev_read_extended
nx_metadata_fragmented_sanity_check
%s:%d: %s expanded record found on unsupported volume\n
<60
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
jobj_refcnt_merge
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
<100
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
authapfs_integrity_meta_get_internal
io_get_device_block_size
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
```
