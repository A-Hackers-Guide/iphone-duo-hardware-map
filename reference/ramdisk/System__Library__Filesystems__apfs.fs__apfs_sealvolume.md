# `/System/Library/Filesystems/apfs.fs/apfs_sealvolume`

From the upgrade restore ramdisk (141-29011-104.dmg). 759,952 bytes.

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

## Strings (2,324)

```
Skipping unexpected extented attribute %s for inode %lld\n
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
Found directory entry in directory %lld for directory inode %lld which has a sibling\n
%s:%d: %s Failed to create purgeable record (drec): %d (%s)\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
 dstream
%s:%d: %s inode %llu is already in purgatory\n
%s:%d: %s Error looking up dstream id %llu: %d (%s)\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
%@max_mem=%llu 
%s:%d: Cannot allocate memory to track excessive space allocations in data stream %lld\n
%s:%d: %s couldn't remove the last clone mapping of private_id %llu, error %d\n
%s:%d: %s Failed to lookup purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n
%s:%d: %s chunk %lld recent zone count overflow\n
init_dir_stats_xfields
%s:%d: %s failed to remove first, error %d\n
update_file_extent
%s:%d: %s Failed to remove snap_meta record!\n
%s:%d: %s failed to get omap tree for reaping: %d\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
\\r
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
%@snap_t=%llu 
\n
NO-SIGNING-ID
%s:%d: Cannot fetch database header: %s (%d)\n
%s:%d: unexpected payload type length : %d\n
IOMedia
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%@num_src=%llu num_dst=%llu 
%s:%d: %s unable to get omap: %d\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
tx_checkpoint_write
%s:%d: Cannot create new fext tree for volume %s: %s(%d)\n
file-id
apfs_checkpoint_traverse
insert_jobj
%s:%d: %s failed inserting hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
%@ever_cloned=%llu 
%zd
%s:%d: %s failed to get fsroot tree of fs %llu, %s(%d)\n
%s:%d: %s Container corruption detected by %s:%u!\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s failed to find uncompressed size for indoe %llu\n
preflight_tree
get_unwrapped_ekwk_snap
nx-volume_group-lock
 date-added
%s: Unknown xfield xf_type: %d\n
%s:%d: %s failed to enter transaction to clear purgatory dir nchildren %s(%d)
%s:%d: Cannot allocate memory to hold information about data stream for inode %lld\n
apfs-doc-id-lock
%s:%d: %s Unsupported flags being used on purgeable drec: %llx. Truncating...\n
\"%llu\":
 kind
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: %s Failed to update_jobj(ino %llu) after %s purgeability: %d (%s)\n
icp_new_crypto
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s:%d: %s Fusion is not supported anymore\n
%s:%d: %s container cleanly-unmounted flag set.\n
%s:%d: %s Cannot remove purgeable record with zero atime (ino %llu).\n
%s:%d: failed to open container device %s: %s\n
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
%s:%d: %s fs_tx_enter returned %d\n
nx_tx_flush_busy
nx_tx_wait_closing
Cannot serialize extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
%s:%d: %s failed to create doc-id tree, error %d\n
\\u000b
%s:%d: %s Cannot allocate space for %zu bytes at offset %lld in dstream %lld of inode %lld: %s(%d)\n
obj_init
%s:%d: %s failed to get reap list object oid %lld: %d\n
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
%s:%d: Cannot get the fext tree of volume %s: %s(%d)\n
asv_read_data_from_extent
authapfs_validate_node
capacity: %9d %9d %9d %9d %9d %9d\n
supplemental_tree_destroy
%s:%d: Cannot get the filesystem tree of volume %s: %s(%d)\n
com.apple.decmpfs
%s:%d: %s Skipping sibling link for inode with single link count (id: %lld)\n
Cannot load extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
clear
sha3_384
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
 name
spaceman_free_extent_cache_setup
%s:%d: %s ***: expanded obj type found on unsupported volume\n
%s:%d: %s failed to update dir-stats %llu: %s (%d)\n
%s:%d: %s iter_next returned %d\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
_remove_purgeable_record_cb
%s:%d: cannot get ino %llu ekwk %d\n
%s:%d: %s could not unwrap crypto-id %lld (err %d)\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
 hashed_len
%s:%d: %s error finishing move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s Failed to set purgeable rec's dir gen-count: error %d\n
%s:%d: %s directory sizing aborted (dir: %lld)\n
%s:%d: %s Found purgeable record with file ID 0!\n
AppleAPFSContainerScheme
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
%s:%d: %s failed to fetch sub-dir ino %lld\n
%s:%d: %s failed to seal integrity_tree of fs %llu, %s(%d)\n
\\u0019
checkpoint
%@data_ondisk_hardlnks=%llu 
asv_mount_container
spaceman_fxtp_add_child
%s:%d: %s Couldn't acquire lock on %llu-%llu, err=%d\n
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
%s:%d: %s fs_update_snap_metadata() returned %d\n
%s:%d: %s Couldn't copy fext tree into new object, err %d\n
invalid unlock flags: 0x%x\n
%@oc_hit=%llu 
%s%s %d%s
 xf-size
btree_node_val_range_validate
%s:%d: %s unable to get prev doc-id tree: %d\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
refcnt
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
  %4d: <<< ERROR: TOC ENTRY OUT OF BOUNDS >>>\n
ino
duplicate_jobj_op_to_shadow_fs_root
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: Cannot delete old integrity object of volume %s: %s(%d)\n
%s:%d: %s failed to delete doc-id tree, error %d\n
%s:%d: %s error updating chained key for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
make_large_jkey_header_from_jobj
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
FSRoot Tree Debug Output: \n
%s:%d: %s Purgeable start time (%llu) is unsupported on purgeable drecs.\n
%s:%d: %s failed to clean up doc-id trees, error %d\n
%s:%d: Duplicate entry for inode %lld\n
parent:%lld name:%d:%.*s
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
<100
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
%lld:%lld
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
\\u000f
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%@num_cg=%zu 
%@incompat=0x%llx 
 compression type
%s:%d: %s obj_modify of integrity_meta failed - %d\n
descendants
fs_insert_snapshot_metadata
%s:%d: %s failed to remove extent for extent-id %lld @ logical offset %lld:%lld err %d\n
total size
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
spaceman_ip_freed
 name-len
%s:%d: obj is NULL or not apfs object!\n
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
type:%u
spaceman_free_extent_cache_search
%s:%d: %s block range %lld:%lld out of bounds %lld\n
 default-crypto-id
icp_dec_ref
spaceman_fq_tree_find_overlap
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
%s:%d: %s failed to decrement crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
nx_reap_list_sanity_check
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s failed to remove <%llu, %llu> clone mapping, error %d\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
=%d
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%@pure_cloned_apps_blk=%llu 
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
%s:%d: failed to move ino %lld from dir %lld to purgatory : %d\n
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
apfs_clonegroup_delete_inode
btree_check_ext returned non-zero: %d\n
Any
apfs-global-snap-lock
iterate_expanded_purgeable_records
ino %lld illogical file extent %lld:%lld != alloced_size %lld (fsize %lld)\n
%s:%d: %s Couldn't find lock for (group:%llu inum:%llu priv_id:%llu)\n
%s:%d: %s error searching spaceman free queue tree: %d\n
spaceman_chunk_zone_info_cache_init
where [options] are\n       -h             display usage\n       -v [-v]        increase verbosity\n       -d             increase APFS logging level from error to debug\n       -p             show sealer progress\n       -n             per
%s:%d: %s failed to enter tx to update size tracking for ino %llu: %s (%d); size tracking may go out of sync\n
\\u0011
dev_init
trying to zero the superblock!\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
spaceman_chunk_zone_info_recent_increment
Found orphan fext record (offset:%lld, id: %lld), skipping...\n
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
%s:%d: %s BUG BUG BUG: ino %lld non-contiguous extents! prev_fext %lld:%lld (%lld) and orig_fext %lld:%lld (%lld)\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
    keys: %9d %9d %9d %9d %9d %9d\n
R
bad pext.\n
jdev_fext_write_data
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
FIXUP
%s:%d: %s omap snapshot tree sanity check failed: %d\n
%s%s%s%sCKI %d CG %d %lld:%d
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
tx_checkpoint_space_check
%s:%d: %s xid %lld second sync/barrier failed: %d\n
%s:%d: %s stopped updating dir-stats due to chain being too long\n
%s:%d: %s invalid reap_id (%llu), must be smaller than nr_next_reap_id (%llu)\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
 %u:%.*s
private-dir
%s:%d: Cannot extract the expected hash from file %s: %s(%d)
get_vol_crypto(apfs) == VOL_CPROTECTED
set_ino_purgeable_state
%s:%d: failed to allocate %d dir stack entries (%zu bytes)\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
(data: %#llx, flags: %#x)
%s:%d: %s failed to remove dir-stats object (id %llu): %s (%d)\n
%s:%d: %s not enough space to enter transaction\n
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
FULL
%s:%d: %s spaceman_alloc() FAILED, err: %d xid: %lld paddr: %lld blocks requested: %lld blocks allocated: %lld\n
%s:%d: %s omap check failed with error: %d\n
%s:%d: %s Cannot reset inode information for inode %lld: %s(%d)
SiblingLink
%s:%d: %s Failed to update_jobj(ino %llu) when %s is transitioning from pending-purgeable to purgeable: %d (%s)\n
apfs_clonegroup_insert_cookie
tinyobjcache
%s:%d: Found incomplete inode records after update starting with inode %lld\n
refcnt:%d
mark_doc_id_index_for_rebuild_if_needed
obj_cache_graft_attach
last_clone_cb
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
%s:%d: Cannot create new filesystem tree for volume %s: %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
tmp-ino-
nx-txn-blocks-lock
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
xid
%s:%d: %s Cannot find extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
Could not allocate memory
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  val:[[ %s ]]\n
purgatory_cleaner_cb
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
populate_time_from_dict
dir_stats_get_flags
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s tx xid %lld took %lld us to flush\n
Sealing fsroot tree with %llu records\n
 dhash:%lld
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
nx_tx_finish_wait
Removed dstream for compressed inode (id: %lld)\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
\\u0005
id is zero\n
nx_checkpoint_load_data
spaceman_fq_tree_insert
  %4d: k:%5d:%-4d  v:%5d:%-4d  <<< ERROR: KEY/VALUE OUT OF BOUNDS >>>\n
dev_init_common
%s:%d: %s dir-stats %llu maintains clone size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: %s bad clonegroup_mapping_key_t, klen:%u vlen:%u group_id:%llu\n
%s:%d: %s updating grandparent failed w/%d\n
Crypto cache num asserted crypto states (%u) surpassed the limit (%u)\n
%s:%d: %s fext_tree_iterate_fexts failed with %d\n
%s%s %8lld%s
%s:%d: Cannot insert file info object for offset %lld of dstream %lld into new filesystem tree: %s(%d)\n
crypto_obj_free
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
%s:%d: %s Failed to estimate fext tree size for snapshots, err %d\n
spaceman_ip_bm_block_alloc
nx_tx_finish_wait_for_dirty_data
Target Disk Mode
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
,%s%s %#x,%s
apfs-omap-lock
\\\\
orig-file-id: %lld
nx_reaper
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
e:
<%d
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
spaceman_alloc
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%@mnt_t=%llu 
%s:%d: %s failed to allocate record for skipped file extent: %lld\n
CloneMap
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s *** unknown expanded obj type %hhu\n
tx-mgr-lock
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
 document-id
%s:%d: Cannot save information about digest at offset %lld into data stream %lld: %s (%d)\n
fext_get_crypto_id
%s:%d: %s failed to create reap list: %d\n
Reserved space < reserved metadata: %llu < %llu\n
Dead
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s failed to write superblock to block 0: %d\n
apfs_clonegroup_remove_locked
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
assertion failed: %s
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
nx_tx_wait_closed_prev_flushing
%s:%d: %s failed to remove the stale clone mapping <%llu , %llu>, error %d\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
nx-resize-spaceman-lock
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
spaceman_cib_sanity_check
.
%s:%d: %s failed to set the dir-gen-count xf field on the purgeable rec for ino %lld : err %d\n
failed to update inode record %lld: %s(%d)\n
supplemental_tree_copy
%s:%d: %s directory has an illegal sub-directory (dir: %lld ; sub-dir ino %lld)\n
retain_xdstream_crypto_states
fs_get_inode_with_hint
NONAME
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
 sibling-id
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: Inode %lld is missing its resource fork\n
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%s:%d: Extent for %lld, %lld bytes at %lld points to block %lld\n
%s:%d: can't get features for device (%s)\n
id:%lld %s %s
jobj_size_for_large_key_val
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
flags
make_jkey_from_jobj
%s:%d: %s fext_tree_update returned %d\n
\t%16p %s\n
spaceman_metazone_init
,%s%s %d,%s
Skipped %u orphan dstream id records\n
lookup_expanded_purgeable_record
%s:%d: %s error updating metadata ranges tree: %d\n
spaceman-space-usage-lock
w
validate_hashed_tree
asv_save_compressed_inode_num
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%s:%d: %s apfs, filepath or new_fsroot_tree is null\n
%s:%d: %s xf_set error %d for type %u id %llu\n
total written
%s:%d: %s Failed to get file ID from purgeable record key/val: error %d\n
!(ino->iflags & (JI_RAW_ENCRYPTED))
move_snapshot_to_purgatory
%s:%d: graft with invalid fs block size: %u\n
%s:%d: %s error updating snapshot tree: %d\n
ino_phys_size_ext
%s%s %lld/%lld/%lld/%lld%s
asv_empty_purgatory
authapfs_integrity_meta_get_internal
%s:%d: %s superblock failed sanity checks: %d\n
apfs
nx_tx_wait_flush
%s:%d: Got highest hashed dstream id: %llu\n
fixup_decmpfs_xattr
%s:%d: %s Aborting iterative purgeable record removal for id %llu because transaction is closing\n
flags:%u total-count:%llu physical-size:%llu full-clone-size:%llu
update_sparse_bytes
tx_leave
%s:%d: %s reap list object free list erroneously empty?\n
 source-purge-id
 0x%06x:%u:%.*s
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
%@num_dirs=%zu 
unable to mount APFS volume @ %s [%ld]
Invalid
APFS_INODES
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
 unraw-size
Unknown kind %d
xsys
BSD Major
%s:%d: %s expanded record found on unsupported volume\n
fs_make_hole_range_writable
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
obj_checkpoint_get
%s:%d: Sparse bytes removed from inode %lld internal flags: 0x%llx iflags 0x%llx, new_sparse_bytes %lld; name %s parent-id %lld), but it wasn't marked sparse.\n
nx_metadata_fragmented_sanity_check
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s bad clonegroup_key_t, size:%u\n
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: %s extended attribute %llu had an unexpected data stream id: %lld\n
jdump file not specified [-D], skipping extended jdump
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%@disk_free_curr=%llu 
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
quarantine
%@xp_desc=%lld 
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
nlink
move_inode_to_purgatory_ext
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
%@num_files=%zu 
%@msu_shared_clone_blk=%llu 
%s:%d: %s Cannot parse remapping dictionary from %s: %s\n
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%@num_sc=%zu 
BIRTH
%s:%d: %s Couldn't update other (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
\\b
curproc
nx_superblock_agrees_with_container_superblock
obj_cache_remove_new_fs_objects
%@ranges_to_move=%zu 
%s:%d: %s Cannot copy object %lld(%d) to new filesystem tree: %s(%d)\n
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
ino->ekwk == ekwk
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
/dev/r
%s:%d: Inode %lld has both resource fork with data stream %lld and compressed data in extended attribute\n
%s:%d: %s failed to get doc-id tree key count, error %d\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
child_size_calculator_cb
get_purgeable_record_details
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s error searching snapshot tree: %d\n
Skipping sibling link for inode with single link count (id: %lld)\n
len:%lld phys:%lld flags:%llx
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld\n
nx_reaper_sanity_check
obj_get_async_read
%s:%d: %s chunk %lld recent zone count underflow\n
%s:%d: Cannot create overallocated_ranges tree for volume %s: %s(%d)\n
delta_from_dir_stats
bt_merge_nodes
%s:%d: %s Failed to update extended fields when %s WANTS_TO_BE_PURGEABLE on ino %llu: %d (%s)\n
MODVAL
nx_check_recent_sanity
obj-id
btree_node_reap
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
supplemental_tree_get_descriptor
clone size
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s Couldn't insert extent, err=%d\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
CHANGE
unmark
ino_get_ekwk_id
%s:%d: %s object cache bootstrap failed: %d\n
%s:%d: %s tx manager initialization failed: %d\n
 uid/gid/mode
%s:%d: %s did not find purgeable drec for dir %lld (parent id %lld) (fsize %lld)\n
apfs_mount
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
w:
 bsd_flags
gbitmap_reap
%s:%d: %s update of the purgatory dir failed! err %d xid %lld\n
fs_is_phys_range_writable
nx-global-extent-manipulation-lock
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
%s:%d: %s apfs_free_data_blocks_if_needed(%llu,%llu) failed: %d %s\n
%s:%d: %s get_cp_class_for_crypto_id failed (crypto id %llu, error %d)\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
blocks_in_txn
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s unable to get spaceman: %d\n
spaceman_alloc_iterate_chunks
%s:%d: %s Cannot read %lld bytes at physical block %lld which corresponds to offset %lld of data stream %lld: %s(%d)\n
%s:%d: Unexpected size of extended attribute record for inode %lld: expected %zd, got %d\n
orphan_snap_check_iterator
%s:%d: Cannot save information about file extent (dstream %lld, range [%llu:%llu) ): %s(%d)\n
%s:%d: %s decrement dstream id returned ENOENT for private-id %lld (ino %lld)\n
%s:%d: %s could not get dir-stats %llu to untrack ino %llu: %s (%d)\n
dir_stats_set_purgeable_state
fs_destroy_shadow_fs_root_tree
purgeable size
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s error getting mapping tree: %d\n
loadtmpcp
 uncompressed size
 internal_flags
0
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
dir-stats
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
apfs_sealvolume
 alloced_size
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%s:%d: unlock == 0 failed %d\n
%ss%d:%lld
%s:%d: %s Failed to remove existing purgeable record (ino %llu): %d\n
%s:%d: %s failed to allocate temporary block memory\n
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: Cannot save metadata hash to %s: %s(%d)\n
 strict-class-f
btree_iterate_nodes returned non-zero: %d\n
Cannot sort extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
%s:%d: %s could not get dir-stats %llu: %s (%d)\n
%s:%d: %s unsupported tree type: %d\n
%s:%d: DStream %lld has compressed size %zd bytes, we found %d extents\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
nx_reaper_obj_get
spaceman_cab_sanity_check
asv_extract_hash_blob
kind:%d
%@ip_freeq_curr=%llu 
copy_kv_to_new_tree
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s Failed to estimate pfkur tree size for snapshots, err %d\n
%s:%d: Length of the hashed region for digest at offset %lld of data stream %lld does not match: expected %d with block factor %d, got %d\n
btree_node_sanity_check
((&crypto_cache->free_list)->tqh_first == ((void*)0))
%s:%d: %s Failed to remove purgeable record for ino %llu (parent id %llu, internal_flags %#llx) iteratively (err %d).\n
%s:%d: %s failed to get a new default crypto-id, ino %lld\n
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
!ino_is_class_v(apfs, ino)
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s sanity checking all container state... please be patient.\n
Cannot read digest database %s header
apfs-im-cache-lock
scalable_id_is_valid(apfs, id)
%s:%d: %s spaceman chunk count is bad: %lld\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
failed to initialize fsroot tree iterator: %s(%d)\n
authapfs_insert_root_hash
nx_reaper_checkpoint_traverse
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
new address mismatch on redirty 0x%llx 0x%llx\n
btree_check_recent_sanity
Device Characteristics
%s:%d: %s stopped purgatory dir cleanup after %d loops\n
obj_cache_remove_reverted_fs_objects
save_file_info_header
%s:%d: can't get block count (%s)\n
%FT%T
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: %s error adding snapshot: %d\n
%@fl=%d
%s:%d: %s adjusting cow exempt count from %lld to %lld\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
nx_check_checkpoint_map_block
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
New
%s:%d: %s failed to get doc-id tree, error %d\n
%s:%d: %s failed to enter tx, error %d\n
0x%llx-dead
<BAD-CLONEGROUP_MAPPING-KEY-LEN>
ENCRYPTED 
%@num_total_dirs=%zu 
 rdev
%s:%d: %s failed to enter tx to %s dir-stats %llu as needing reconciliation: %s (%d); size tracking may go out of sync\n
%s:%d: failed to stat img4 file: %s (%d)\n
spaceman_iterate_free_extents_internal
\n---------------------------------------------------------------\n
clone_mapping_clear_flags
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
apfs_lock_phys_range first_pbn 0, last_pbn 0x%llx\n
%s:%d: %s Couldn't find name for snap_xid %llu\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
apfs_reap
lookup_purgeable_drec_as_record
%s:%d: %s large key size (%u) on record (%llu) is too small\n
%s:%d: %s Cannot trim extent at offset %lld in inode %lld from %lld to %lld bytes: %s(%d)\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s First sync/barrier failed: %d\n
obj_delete_and_free_by_oid
%s%s %#llx%s
failed to find override hash for %lld: %s(%d)\n
%s:%d: %s did not find purgeable drec for file %lld (parent id %lld) (fsize %lld)\n
%s:%d: %s mount for ramdisk\n
%s:%d: Unsupported offline AppleFSCompression extended attribute for inode %lld\n
%s:%d: %s directory has an illegal hardlinked child (dir: %lld ; child ino %lld)\n
Skipping sibling id XF for directory entry %s (id: %lld) for inode with single link count (id: %lld)\n
fs_map_file_offset_ext
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
group-id: %llu, type: %u
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
, done %lld%% of the fs blocks
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s cannot insert new ep %llu because the policy cache is full\n
purgeable rsrc size
jobj_release
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
Time is more then 30 days in the future
%s:%d: %s iterating over fsroot tree records\n
%s:%d: %s error finishing move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
Conflicting options: [-S] [-s]
%s:%d: %s %s flags 0x%x for clone mapping <%llu, %llu> failed: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s Unsupported flags being used on purgeable record: %llx. Truncating...\n
%s:%d: %s ***: expanded type seen on in-memory obj\n
fs_remove_xattr_with_nstream_inode
invalid crypto index %d\n
%s:%d: %s Lookup for key %s failed in the remapping dictionary\n
%s:%d: %s failed to set dir stats key for <%llu, %llu> clone mapping, error %d\n
%s:%d: %s Failed to update purgeable flags on ino %llu (new flags %u):%d (%s)\n
SAVED 
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
 (%s%s %lld;%s
Found %u potential orphan dstream id records\n
\\u001c
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
apfs_clonegroup_update_locked
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s Invalid residency reason %d ino %llu\n
%s:%d: %s invalid zero len, paddr %llu\n
v8@?0
%s:%d: %s dir-stats %llu maintains purgeable size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: %s oid (%llu) failed to get child %d - %d\n
 REVERTED
%@time=%llu 
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
recursively_remove_extents_of_dir
%s%s %lld (under obj-id: %lld / crypto-id: %lld)%s
Skipping sibling map for inode %lld with single link count (id: %lld)\n
/dev/
lba %llu, len %hu, tweak %llu
file-size: %llu ds-id: %llu flags: 0x%x uid: %u
decrement_dstream_id_for_deletion
%s:%d: %s waiting for available tx to open: xid %lld\n
apfs-dir-size-lock
jobj_allocate
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s failed to increment crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
%@oc_miss=%llu 
create_plist_from_file
sib-id
ino_get_ekwk_uncached
unexpected storagetype: 0x%x\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
jobj_validate_large_key_val
%s:%d: %s failed to update allocate zone %llu: error %d\n
Removed dstream for empty inode (id: %lld)\n
%s:%d: Unknown subtype %d for file info object %lld\n
addition
insert_prev_inode
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
jdev_fext_write_data() corrupts encrypted data
%s:%d: %s failed to free allocated blocks, ino %llu, 0x%llx+%llu, error %d\n
%s:%d: %s failed to create snapshot: %d\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
object-cache-lock
%s:%d: %s couldn't insert record type %u id %llu into new tree, error %d\n
spaceman_fxc_tree_node_recycle_smallest
RR_HOLE
clean_up_doc_id_trees_if_needed
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
PurgeableTomb
hashed:%u hashsz:%u
ino %lld pos:len %lld:%lld fext %lld:%lld (%lld)\n
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
 signing-id-hash
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
%s:%d: %s Cannot create read stream for %s\n
sha3_256_4k
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: %s omap snapshot count %d seems excessive\n
type:%d
%s:%d: %s failed to fetch the extentref tree (error %d)\n
insert_phys_extent
 
compressed 
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
%s:%d: %s Bad blob in (group:%llu inum:%llu priv_id:%llu): %s\n
 dstats-key
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
invalid tweak type %d\n
%@purge_from_user=%llu 
%s:%d: Sparse bytes removed from inode %lld that didn't have an extended field.\n
ino->rsrc_ekwk == cur_ekwk
%s:%d: %s failed to re-insert ext %lld:%lld for obj %lld (ret %d)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
obj_destroy_complete
Time is too far in the past
%s:%d: %s Coludn't update dir stats key on (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: %s Failed to remove snap_name record!\n
skipsanity
FSRoot Tree: %llu (keys: %llu, nodes: %llu)
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
%@src_fsroot_2nd_depth=%llu 
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
spaceman_ip_block_alloc
 nchildren
 def-prot-class
%s:%d: Cannot allocate %lld bytes for data buffer when processing data stream %lld\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s couldn't get tree, err %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: Why are we comparing a chunk to itself?\n
 total read
 purgeable-flags
resource fork size
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
doc_id_tree_create
prevent_synthetic_object_operation
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s Did not find date-added/change/birth/mod/access time in the xml dictionary, remapper will perform no modifications\n
%s:%d: %s remapping xml is empty\n
%s:%d: %s error starting move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s got err %d writing at pos %lld in obj-id %lld (blkcount %llu, len %zd)\n
%s:%d: %s Cannot update extent at offset %lld in inode %lld: %s(%d)\n
spaceman_fs_bounds_clear
subtype
%s:%d: Cannot find information about digest at offset %lld of data stream %lld - %s(%d)\n
\\u001a
jfs_get_tree_in_snap
fext_collector
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
num children
Unexpected extended attribute %s for inode %lld (flags 0x%x)\n
btree_node_debug_stats
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  child:%s\n
%s:%d: %s failed to retain crypto-id %llu for ino %llu, %d\n
spaceman_freed
FileInfo
%s:%d: %s bt_shift_or_split failed with error: %d\n
cst->ep_retain_count > 0
update_purgeable_clone_tracking
%s:%d: %s Couldn't copy pfkur tree into new object, err %d\n
%s%s %-11s%s
 offset
%s:%d: failed to init extended fields on drec %lld from blob.\n
reference
%s:%d: %s cp_corrupt_assert() failed: %s
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%@num_sh=%zu 
nx-tree-node-compact-lock
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
perm
%s:%d: %s xid %lld sync/barrier failed: %d\n
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
%s:%d: failed to open volume device %s: %s\n
APFS_4K_OBJS
Failed to initialize hash override table: %s(%d)\n
update_dir_stats_by_key_ext
Physical Interconnect Location
Requested forced secondary_fs_root but the tree is missing\n
NOHEAD 
%@tmp_cloned_blk=%llu 
%s:%d: %s failed with err %d while getting the cow-exempt-file-count xattr on the root dir\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld\n
apfs_unlock_id
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
invalid offset (%llu) for last fext lookup\n
apfsuuid
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: %s full clone scan failed (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%s:%d: Invalid expected root hash: %s (expected size: %d)\n
sha3_384_4k
bt_update_last_leaf
%s:%d: %s rapid-aged %llu inodes\n
%s: Invalid arguments os: %p xf: %p\n
finalize_digest
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
obj_write_prepare
%s:%d: %s obj_modify() failed: %d\n
%s:%d: %s failed to allocate a new directory record for file id %llu (obj_id %llu): %d (%s)\n
process_xattr_record
ds-id: %llu
fs_insert_fext_record
%s:%d: %s Skipping sibling id XF for directory entry %s (id: %lld) for inode with single link count (id: %lld)\n
Unknown type %d
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
nx_checkpoint_find_valid_checkpoint
%s:%d: %s Cannot create URL for %s\n
remove_clone_mapping_if_last
Data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
%s:%d: %s remove_purgatory_entry failed on %s for file-id %lld err %d\n
set_cloneinfo_id_epoch
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
found potential %s%sorphan dstreamID record %lld\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
L
%s/apfs_data
DELETE 
:
%@src_fsroot_nodes=%llu 
%s:%d: %s create_plist_from_file failed\n
spaceman_fxc_update_smallest_with_successor
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s Checking for solo group returned error: %s\n
%s%s %d,%s
iterate_ino_crypto_state
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%d: %s Cannot open remapping dictionary from %s: error information not available\n
%s:%d: %s ino %llu is being moved but we don't know how to account for it (from_dir %llu/%llu, to_dir %llu/%llu); size tracking may go out of sync\n
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
%s:%d: WARNING WARNING WARNING!!! Invalid root hash: %s (expected: %s)\n
dir_stats_move_origin
Encrypted
physical_size:%llu flags:0x%x
%s:%d: %s failed to load inode %lld ret %d on volume: %s\n
%s:%d: %s spaceman IP base address is bad: %lld\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
tx_mgr_free_tx
%s:%d: %s Cannot initiate a walk of the filesystem tree: %s(%d)\n
%s:%d: %s prev doc-id tree sanity check failed: %d\n
bt_remove_internal
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
\\u0018
update_dir_stats_key_on_ino_and_clone_mapping
dereference
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
apfs_sanity_check_tree_type
  values: %9s %9s %9s %9s %9s %9s\n
\\u001b
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
!(ino->iflags & JI_NAMEDSTREAM)
%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n
%s:%d: %s extended attribute %llu has an unexpected compression type: %u\n
\\u0010
%s:%d: %s Cannot find inode record for inode %lld: %s(%d)\n
Freeing %llu overallocated dstream ranges\n
%s:%d: %s failed to decrement crypto state = %llu, err %d\n
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: Cannot get index of the volume %s\n
%s:%d: Cannot allocate mempry to track state of inode %lld with compressed flag set\n
\\u0014
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
flags 0x%x%s%s oid %lld
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: %s failed to insert root_hash of fs %llu,- %s(%d)\n
%s:%d: %s oid (%llu) unexpected oid at index %d - (%llu!=%llu)\n
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
%s:%d: %s Would have attempted to create an entry with kind == NEW and refcnt == %d! (flags=0x%x, existing val len_and_kind=0x%llx owning_obj_id=%llu refcnt=%d)\n
%s:%d: Failed to lookup last digest in hash db: %s(%d)\n
get_dir_stats
%s:%d: %s Failing with error=%d\n
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
(data: %s, flags: 0x%x)
dir_stats_move_regular_origin
spaceman_allocation_init
%@data_ondisk_fclones=%llu 
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
%s:%d: %s ino %lld no extent covering dstream alloced_size %lld (fsize %lld) pos/len %lld:%lld\n
%s:%d: %s fext_ref_extent_key for fext %llu with crid %llu failed with %d\n
%s:%d: %s failed to remove tail_fext, ino %llu, laddr 0x%llx, error %d\n
%s:%d: %s was NOT able to update/decrement crypto state %lld, err = %d\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
spaceman_unreserve
%s:%d: Cannot delete old fext tree of volume %s: %s(%d)\n
authapfs_volume_seal
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: %s Failed to release reference to crypto ID %lld for data stream %lld: %s(%d)\n
nx_checkpoint_find_highest_xid
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
!((apfs)->apfs_main_apfs != ((void*)0))
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s tree_delete() failed: %d\n
spaceman_trim_free_extent_callback
%@tgt_fsroot_nodes=%llu 
 clonegroup-id
Compressed data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
lookup_purgeable_drec
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
invalid lock flags: 0x%x\n
apfs_reap_snapshots
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s fs_tx_leave failed for integrity_tree of fs %llu, %s(%d)\n
apfs-pfkur-tree-oid-lock
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
0x%llx-0x%llx:%d
flags:0x%x
SnapMetadata
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
can not lock id zero\n
create_empty_extentref_tree
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: %s failed to enter tx - %s(%d)\n
%s:%d: %s fs_tx_enter failed for volume seal of fs %llu, %s(%d)\n
btree_node_child_id_update
obj-id %llu type %u still has refcount %d\n
marking
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
groupquota
%s:%d: Database header has wrong version/size: expected %u/%zu, got %u/%zu\n
%s:%d: %s lookup_next_snapshot() returned %d\n
owners
%s:%d: %s tree_remove(%llu) failed\n
%s:%d: %s Cannot start transaction with XID %lld: %s(%d)\n
%s:%d: %s couldn't delete tree, err %d\n
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
%s:%d: can't get solidstate for device (%s)\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
snap_xid:%llu
%s:%d: %s failed to remove extents iteratively\n
%s:%d: %s Timestamp set by B+I is %llu\n
apfs-global-lock
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
obj_checkpoint_start
%@src_fsroot_2nd_nodes=%llu 
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
\\u0001
%s:%d: %s Failed to set purgeable drec's dir gen-count: error %d\n
no-name
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
%s:%d: %s failed to delete dir entry %lld:%s (file-id %lld) ret=%d\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
 flags
 atime:%llu file-id:%llu
<BAD-CLONEGROUP-KEY-LEN>
spaceman_free
%@num_total_files=%zu 
%s:%d: Database header not found\n
%s:%d: Database header is too small (%zu bytes)\n
jobj_type_from_possibly_large_key
object-cache-reset-lock
apfs-snapmeta-oid-lock
bt_lookup_copy_out
jobj_to_large_key_val
%s:%d: %s Failed to insert purgeable record (drec): %d (%s)\n
remove_jobj
__apfs_dec_parent_nlink
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
%s:%d: %s Invalid reap list free entry %d\n
apfs_clonegroup_check_solo_group
%s:%d: Information about digest at offset %lld of data stream %lld does not match\n
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: %s failed got create jobj for id: %lld (type: %u)\n
%s:%d: %s oid (%llu) failed to compute hash - %d\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
spaceman_chunk_zone_info_load_recent_chunks
removed potential orphan dstreamID record (id: %lld)\n
authapfs_valid_hash_type
%s:%d: %s reverting on error: %d\n
crypto_cache->type != CRYPTO_OBJ_TYPE_EP
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d: %s Failed to lookup purgeable drec (id %llu): error %d\n
file-id: %lld date-added:%lld flags:0x%x
%@src_fsroot_depth=%llu 
version:%u flags:%u current_offset: %llu current_ns_offset: %llu
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
omap_destroy
%s:%d: %s COW exempt file count underflow: %lld (delta %lld).  capping to zero.\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
purgatory.
%s:%d: %s lookup returned unexpected error while iterating: %d\n
Cannot parse timestamp '%s' using format \"%s\"\n
sha256
%s:%d: %s tx_enter() failed: %d\n
legacy_get_ek
%llu
%s:%d: %s Cannot open remapping dictionary from %s: unknown error\n
IOBlockStorageDevice
cst %llu hit zero retain count but still has ep related retain count (%u)\n
cst->ep_retain_count <= cst->hdr.retain_count
DELETE
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
Reference count underflowed for object %p!\n
dev=%s vers=%s 
** Sealing volume %ss%d: %llu hash records added
apfs-flags-lock
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
i40@?0q8Q16^v24^Q32
%s:%d: %s Cannot create a inode record for inode %lld - out of memory\n
%s:%d: Cannot get to the parent of %s\n
spaceman_free_extent_cache_remove
INSERT
%s:%d: %s Final sync/barrier failed: %d\n
%s\n
%@msg='%s' 
Cannot make snapshot in dry run mode
%s:%d: Unexpected sparse extent at the offset %lld in the data stream %lld\n
%s:%d: cannot get ino %llu ek %llu, %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%@tmp_blk=%llu 
%s:%d: stale clone mapping <%llu, %llu> had non-empty extended fields\n
%s:%d: %s Not enough room in the extent for %lld bytes at offset %lld in data stream %lld to read %lld bytes\n
fd_dev_close
%s:%d: %s encryption type %llx unsupported\n
%s:%d: %s reaper has tail with no head\n
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
spaceman_chunk_zone_info_list_remove
%@prepro_t=%llu 
%s:%d: Sealing volumes with block size: %u is not supported when producing root hash metadata\n
%s:%d: %s unexpected record type %u id %llu encountered\n
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
object-cache-flush-lock
%s:%d: %s tree_iterator_next failed: %s\n
tx_finish
%s:%d: The reaper for device %s failed: %s(%d)\n
%s:%d: %s omap tree sanity check failed: %d\n
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
obj_cache_remove
union
spaceman_upgrade_sm_version_0_to_1
%s%s %#x%s
 gen-count
 physical_size
%s:%d: %s failed to get integrity_meta of fs %llu, %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
capacity: leaves %llu / %llu => %.2f %% used\n
fs_is_content_protected(apfs)
nx_get_evict_mapping_tree
%s:%d: %s Cannot parse remapping dictionary from %s: unknown error\n
%s:%d: %s Coludn't remove dir stats key from (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
%s:%d: %s Failed to mark the dir-stats record for ino %llu as purgeable: error %d (%s)\n
%s:%d: %s failed to find host inode (id %llu) for purgeable rec lookup, falling back to ino %llu's atime\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
%@(%d:%d)
%s:%d: %s Failed filesystem tree preflight checks: %s(%d)\n
%s:%d: %s can't get <%llu, %llu> clone mapping, error %d\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s find_next_snap(%llu) returned %d\n
physical object dirty count underflow\n
%s:%d: %s Value too small:%u (group:%llu inum:%llu priv_id:%llu)\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
io_get_device_features
extent_remover_callback
%s:%d: ino %llu has no ekwk id\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
\"%s\"
%s:%d: failed to open img4 file: %s (%d)\n
sha384
%s:%d: %s failed to remove hash file info for id %llu @ logical offset %llu err %u\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
computing root hash for block size: %u\n
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
omap_cleanup
dev
spaceman_get_metazone_alloc_index
%s:%d: %s copied %llu fsroot tree records into new fsroot tree\n
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
Internal
full clone size
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n
%s:%d: %s Couldn't get existing fext tree, err %d\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
%s:%d: %s btree_get_extended failed - %d\n
%s:%d: %s Failed to remove purgeable record (record): %d (%s)\n
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: %s failed to look up dir-stats %llu for origin inode %llu: %s (%d)\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
Reference count overflowed for object %p!\n
Computed root hash: %s\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s Failed to remove purgeable record (ino %llu): error %d\n
%s:%d: %s Inserting snap_name failed, %d\n
%@features=0x%llx 
%s:%d: %s Cannot open remapping dictionary from %s: %s\n
%s:%d: %s failed to iterate fsroot tree for jobj %llu: %s (%d)\n
%s:%d: %s failed to %s dir-stats %llu as purgeable: %s (%d)\n
%s:%d: %s ino %llu is compressed and this volume does not support compressed purgeable files.\n
fs_write_stream
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
3288.52.1
%s:%d: %s bogus phase, %u\n
%s:%d: %s Failed to update inode : xid %llu, ino %llu, error = %d\n
%s:%d: %s failed to fetch the fext tree (error %d)\n
%s:%d: %s Failed to set purgeable start time for ino %lld: error %d (%s)\n
sealed, fext, req_tree != fs_root
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s doc-id tree sanity check failed: %d\n
%s:%d: Cannot save database header: %s (%d)\n
btree_seal_callback
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%@%s
child_remover_cb
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s Couldn't clone superblock, err %d\n
%s:%d: %s doc-id tree creation failed: %d\n
%s:%d: %s Invalid purgeable record type %u found on volume expecting type %u\n
%s/nx
parent:%lld private:%lld flags:0x%llx mode:%o uid/gid:%d/%d bsdflags:0x%x %s:%d cr8:mod:chg:acc %lld:%lld:%lld:%lld
 hash
%s:%d: %s failed to remove shadow dir-stats object (id %llu): %s (%d)\n
sha3_256
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s danger - crypto id %lld had refcnt %d\n
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
virtual
Removed INO_EXT_TYPE_FS_UUID for dir (id: %lld)\n
update_purgeable_record_time_and_flags
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
 atag:%lld
fs_tx_leave_ext
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%s%s
fsroot_tree_iterator
%s%s 0x%06x%s
%s:%d: %s failed to look up shadow dir-stats %llu: %s (%d)\n
%s:%d: failed to decode img4: %d\n
kind == NEW && refcnt = %d\n
ino_get_ekwk_
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s failed to update rightmost leaf field: %d\n
n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
%s:%d: %s failed to dereference range (%llu + %llu) of extended attribute %llu: %s(%d)\n
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%s%s 0x%08x%s
AppleAPFSVolume
%s:%d: %s Unexpected unwritten extent for offset %lld of data stream %lld in inode %lld\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
Cannot find inode record for inode %lld in sibling map record %lld: %s(%d)\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
,
exec
%s:%d: %s Lookup for key %llu failed in the remapping dictionary\n
 unexpected type %d @ %lld!
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
jobj_size_for_key_val
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
get_dir_stats_by_key
%s:%d: Sealing of encrypted volumes is not supported\n
%s:%d: Inode %lld has inline compressed data of type: %u\n
key_val_to_jobj
%s:%d: ** BOGUS FEXT FLAGS = 0x%02x (crypto_flags = 0x%llx)\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
spaceman_set_up_ip_reverse_mapping_tree
Using [-I] option without [-R]
(data: %llu, flags: 0x%x)
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
%@mv_t=%llu 
%s:%d: Failed to allocate %zu bytes for snapshot name\n
%s:%d: %s failed to serialize inode %lld: %s(%d)\n
fs_delete_inode_internal
nx-omap-lock
%@cloned_apps_blk=%llu 
%u
DirSize
F
merge_ino_purgeable_flags
%s/apfs
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: %s error modifying omap: %d\n
 inline
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
\\u0012
io_get_device_block_size
runtime_retains()
%s:%d: %s object cache initialization failed: %d\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
rolling-stats-lock
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s Unknown flags being used on purgeable record: %x. Truncating...\n
len:%lld phys:%lld crypto:%lld flags:%llx
%s:%d: %s Inserting snap_meta failed, %d\n
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s failed to compute root_hash - %d\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
\\u0013
%s:%d: locking id %llu, which is already locked by this thread\n
obj_checkpoint_done
%@purge_full_2=%llu 
%s:%d: %s cib %lld index %d should be %lld\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
%s:%d: Sealing volumes with block size: %u is not supported\n
%s:%d: %s unable to get fs snap meta tree: %d\n
group-id: %llu, private-id: %llu, file-id: %llu
%s:%d: unexpected payload type: %s\n
paddr
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s couldn't remove (group:%llu inum:%llu priv_id:%llu) err:%s\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld err %d\n
%s:%d: %s set apfs_fixup_flags to %#llx\n
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
%s:%d: %s key @ %p key.hdr.obj_id %lld val @ %p val.kind %d refcnt %d owning_obj_id 0x%llx\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
nx_reaper_next_record
suid
MODIFICATION
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
tmp-ino-clone-
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%d: %s Hit %d looking up first snapshot\n
nx_unblock_physical_range
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s tx xid %lld took %lld us to close\n
%@addcg_t=%llu 
apfs_mount_livefs
apfs_mark_inconsistent_
UNKNOWN TXN TYPE
%s%s %zd%s
hcp_get_class_ek_uncached
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
remove_dir_entry_ext
%s:%d: %s unable to get fs object 0x%llx: %d\n
Could not open metrics log file %s
fetch_precomputed_digest
%s:%d: %s dir-stats key %llu is busy even though we hold the inode lock\n
sha3_512_4k
%@freeQ_d=%lld 
%s
size
 cr/m/ch/atime
cst_cache
jdev_fext_read_data
START
follow
%s:%d: %s Creating key for lookup failed\n
<80
obj_delete_internal
auto
Cannot open digest database %s
 total_count
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: failed to load ekwk for ino %llu, id %llu, class %d, decode error\n
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
com.apple.fs.symlink
PhysExtent
match_jobj_expanded_type_to_tree_type
spaceman_trim_free_blocks
%@encoded_len=%zu 
%@max_stack=%zu 
clearing
cleanup_purgatory_dir
Invalid arguments: [-I] requires [-R] option
bt_insert
 %lld
%s:%d: %s ino %lld failed to remove purgatory entry: iflags 0x%llx internal_flags 0x%llx isdir: %d\n
nx_check
spaceman_set_bits_in_bm
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
omap_recent_sanity_callback
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
Timestamp specified as command line argument is ignored when remapping
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
 %llu
%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld (ret %d/%s)\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s failed to find valid checkpoint: %d\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
compute_digest
%s:%d: %s failed to leave tx, error %d\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: %s failed to write superblock to block %lld: %d\n
%@roincompat=0x%llx 
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
%s:%d: %s extentref tree %lld: %d\n
failed to insert fsroot tree entry: %s(%d)\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
 not
length
%s:%d: %s name is bad, name_len=%lu name[0] = %u\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
hcp_get_class_ek
find_highest_precomputed_digest_id
Removable
%s:%d: %s Couldn't get active extentref tree, err=%d\n
nx_mount_initiate_free_space_trims
%02X
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
%s%s %6lld%s
fetch_file_info_header
Found orphan dstreamID record (id: %lld), skipping...\n
jobj_merge_maybe_clamp_64
nx_check_omap
%s%s %lld%s
%s:%d: %s Shadow fs_root does not exist\n
add_entry_to_dir_stack
dir_stats_update_reconciliation
spaceman-ip-lock
type = %u, req_tree != fs_root\n
%s:%d: %s Attempted to %s range %llu+%llu but it isn't entirely there! (found gap at %llu, next range at %llu+%llu)\n
%s:%d: %s error %d removing purgatory entry %lld/%s for ino %lld\n
%s:%d: %s failed to delete prev doc-id tree, error %d\n
%s:%d: %s apfs_update_phys_range for satisfiable range failed on 0x%llx+%llu, error %d\n
update_hash_records_for_compressed_data
 spec-telemetry-flags
apfs_release_objects
exp_dir_stats_refcnt_merge
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: %s couldn't insert record err:%s\n
\\u0002
apfs_update_phys_range
%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu): %s\n
browse
%s:%d: %s Failed to find purgeable record (ino %llu) for flags merging: %d\n
val_size_for_jobj
%s:%d: %s Couldn't insert snapshot metadata, err %d\n
%s:%d: %s cab %d index %d should be %d\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s Found directory entry in directory %lld for directory inode %lld which has a sibling\n
Xattr
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
key_size_for_jobj
%s:%d: %s ino %lld file extent %lld:%lld extends beyond alloced_size %lld (fsize %lld). fixing it.\n
APFS_8K_OBJS
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
Relative Node ID: %llu\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
%@data_num_hardlnks=%llu 
dump_jobjs_for_id
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s Cannot mark space for %zu bytes at offset %lld in dstream %lld of inode %lld as writable: %s(%d)\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
len:%lld owning_obj_id:%lld refcnt: %d
%s:%d: Failed to remove sparse bytes attribute from ino %lld, but it was successfully got, errro %d\n
!apfs->apfs_readonly
fs_make_phys_range_writable
nx_reaper_add_ext
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
obj-mem-mgr-lock
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%@num_sr=%zu 
%lld (under obj-id: %lld / crypto-id: %lld)
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
%s:%d: %s failed to restore refcnt on dstream id %llu, err: %d\n
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
make_purgeable_drec_xfs_from_record
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
spaceman-dev-lock
Invalid arguments: [-S] requires [-V | -I] option
%s:%d: %s Skipping sibling map for inode %llu with single link count (id: %lld)\n
%s:%d: %s failed to init extended fields for dir-stats object on ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
res->xid %lld but xid is now %lld\n
invalid crypto id %llu
Conflicting options: [-V | -I] [-M]
%s:%d: %s failed to insert inode %llu: %s(%d)\n
spaceman_free_extent_cache_insert
\\u001f
%s:%d: %s failed to finish writing to obj-id %lld (pos %lld / new_size %lld)\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
\\u000e
%s:%d: %s failed to get reap list tail: %d\n
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
Attempting to reuse a non-candidate chunk zone info\n
file-id: %lld
get_dstream_id_refcnt
obj_mem_mgr_init
demomode
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
spaceman_clear_bits_in_bm
%s:%d: Cannot mount container on %s - %s(%d)\n
%s:%d: %s failed to fetch the integrity object (error %d)\n
%s:%d: %s failed to remove head_fext, ino %llu, laddr 0x%llx, error %d\n
delete_extentref_tree
apfs_clonegroup_remove_dir_stats_key
Invalid arguments: [-c] requires [-M] option
Hashed %lld bytes for dstream %lld\n
FileExtent
btree_node_check
%s:%d: %s Failed to find host inode (id %llu) for purgeable drec lookup, falling back to ino %llu\n
remove_purgeable_record
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s Cannot initiate iterator for overallocated ranges: %s(%d)\n
crypto_hash_insert
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s didn't find <%llu, %llu> clone mapping which was expected, not failing\n
%s:%d: %s apfs_update_phys_range failed, err = %d\n
apfs_clonegroup_inode_became_partial_clone
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
fd_dev_read_extended
failed to dump fsroot tree: %s(%d)\n
%s:%d: %s btree_node_insert failed: %d\n
zero_tail_of_last_block
apfs_clonegroup_lookup_locked
%s:%d: %s error getting cab %d @ %lld: %d\n
reserved metadata space underflow: %lld (%lld)\n
spaceman_sanity_check
%s:%d: %s Failed to create contiguous fsroot tree: (%llu + %llu) != %llu\n
authapfs_seal_break
createtmpcp
%s:%d: %s obj_create failed - %d\n
remove_extent_of_file
%s:%d: %s unable to get fs extentref tree: %d\n
Release count overflowed for object %p!\n
%@decloned=%llu 
%s:%d: Duplicate entry for data stream %lld\n
%s:%d: %s inode %llu was marked sparse but didn't have a sparse bytes extended field?\n
%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n
large_key_val_to_jobj
ino->rsrc_ekwk != ekwk
%@msu_purgble_clone_blk=%llu 
%s:%d: %s Cannot find inode record for inode %lld in sibling map record %lld: %s(%d)\n
failed to seal fsroot tree: %s(%d)\n
%s:%d: Unexpected AppleFSCompression extended attribute record for inode %lld\n
btree_node_compact
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: *** unknown obj type %d\n
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
 out-of-line data size
update
%s:%d: %s Failed to update jobj %llu while removing xattr %s with error: %d\n
%s:%d: %s failed to delete mapping, error: %d\n
nx_check_recent_sanity_omap
%s:%d: %s invalid object size: %d size_phys %d\n
strictatime
spaceman-lock
%@full_clones=%llu 
Set root tree oid to %lld and fext tree oid to %llu\n
Volume is already sealed - DANGER! This mode is not officially supported yet and can corrupt the volume.
 saf-dstats-key
** Sealing volume %ss%d...\n
%s:%d: cannot get on-disk ekwk %llu, %d\n
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
sha512_256
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
apfs_free_data_blocks_if_needed
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
nx_tx_wait_frozen
sha3_512
%s:%d: %s failed to get integrity_meta obj - %d\n
doc_id_tree_invalid_crypto
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s Trash unfinished tx xid=0x%llx\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
obj_checkpoint_check_for_unknown
%@time=%ld 
%s:%d: %s Failed to get next extent: %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
\"%s\":
btree_node_free_list_entry_validate
dst_paddr:%lld len:%lld
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
failed to allocate override hashes for dstream: %lld\n
update_size_tracking_no_gencount_bump
%s:%d: %s created doc-id tree, oid %llu\n
<BAD-KEY-LEN>
attr tag
%s:%d: *** Unknown file info type %llu\n
%s:%s
btree rightmost leaf field is set for physical tree!\n
btree_node_key_range_validate
%s:%d: %s invalid crypto object type %u\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
%s:%d: %s failed updating hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
%s (%s)
 full_clone_size
%s:%d: %s Volume inconsistency detected by %s:%u!\n
obj_read
btree_node_insert
%s:%d: %s Failed to update purgeable record (drec) time/flags (ino %llu): %d (%s)\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
set
%ss%d
%s:%d: ***: unknown obj type %d\n
exp-dir-stats
%s:%d: Duplicate record found for digest at offset %lld into data stream %lld\n
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s Failed to insert purgeable record (record): %d (%s)\n
SNAP_DELETE_TXN
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s fext_tree_remove returned %d\n
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
%s:%d: %s failed to attach graft to object cache: %d\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
%s:%d: %s couldn't get clonegroup tree err:%s\n
0x%llx
%s:%d: %s tx_leave failed: %d\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
%s:%d: %s Unexpected error searching (group:%llu priv_id:%llu): %s\n
 orig-sync-root-id
%s:%d: %s dir-stats %llu maintains purgeable rsrc size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d 
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
obj_modify
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
obj_checksum_verify
%s%s %s,%s
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s failed to remove sibling hard link entry for ino %lld under hardlink/sibling key %lld/%lld w/drec %lld:%s (ret %d)\n
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s failed to read file extent %llu (block %llu) of extended attribute %llu: %s(%d)\n
%lld
BSD Minor
%s:%d: Found incomplete data stream records after update starting with data stream %lld\n
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
spaceman_get_new_chunk_for_allocation_zone
%@%s:%d 
%@data_size_fclones=%llu 
%s:%d: %s could not alloc %zd bytes @ pos %lld for obj-id %lld (err %d)\n
%s:%d: unlocking id %llu, which is not locked\n
 data-len
 hash_size
Inode
Get count overflowed for object %p!\n
%s:%d: %s Couldn't lookup_ge (group:%llu inum:%llu priv_id:%llu): %s\n
%@disk_free_start=%llu 
get_val_from_dict
%s:%d: using 16k root hash\n
apfs-stream-id-lock
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s unable to get omap tree: %d\n
 conformance-nlink
%s:%d: Cannot hash file extent (dstream %lld, range [%llu:%llu) ) for new  filesystem tree: %s(%d)\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s failed to add initial cow-exempt-count xattr! err %d\n
%s:%d: %s failed to get newnode minkey: %d\n
decrement-dstream-id-for-deletion
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
Cannot find inode record for inode %lld: %s(%d)\n
failed to hash root node: %s(%d)\n
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
%s:%d: %s failed to update dstream id %lld err %d\n
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s fs_tx_enter failed: %s (%d)\n
btree_node_entry_update
%s:%d: %s Failed to lookup purgeable record for removal (ino %llu): error %d\n
%s:%d: %s failed to %s shadow dir-stats %llu as purgeable: %s (%d)\n
%s:%d: %s can't add dir %llu for recursive extent deletion\n
 parent-id
%s:%d: %s failed to extend existing extent %lld:%lld of inode %lld: %s(%d)\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
Invalid arguments: [-P] requires [-I] option
 sparse-bytes
PurgeableTombstone
image-format-read-only
obj_alloc
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
\\f
apfs_lock_id
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
apfs_clonegroup_update_purgeable_urgency
%s dstats-key: %llu
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
spaceman-free-lock
com.apple.system.fs.speculative_telemetry
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: %s couldn't get clonegroup tree: %s\n
%s:%d: Cannot create integrity object for volume %s: %s(%d)\n
apfs-incompat-features-lock
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
apfs-phys-lock-state-mutex
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
%s:%d: %s *** trim'ing free blocks returned: %d\n
spaceman_free_completed
apfs-integrity-meta-lock
modification
---UNKNOWN---
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s link count == %d for inum %lld?!\n
btree_node_copy
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
fs_tx_enter_internal
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
nx_dev_init
nx_tx_wait_closed
%s:%d: %s Failed to insert drec associated with purgatory_dir and ino %llu, error = %d\n
%s:%d: %s failed to delete ino %lld (%s) iflags 0x%llx err %d\n
%s:%d: %s error: fs_tx_leave_ext returned %d\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
%s:%d: %s failed to allocate temporary inode buffer\n
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: Cannot create temporary filesystem tree for volume %s: %s(%d)\n
save_file_info_record
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: %s Failed to copy supplemental tree (type %d): %d (%s)\n
apfs-dir-stats-id-lock
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
%s:%d: %s Deleted the shadow_fs_root tree %p\n
%s:%d: %s ino %llu is flagged to maintain dir-stats but has no dir-stats key\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
setup_demo_mode
nchildren
spaceman_sanitize_datazones
tx_unmount
%s%s %u%s
computed hash for block size %u is: %s\n
%s:%d: %s failed to%s update the <%llu, %llu> clone mapping, error %d\n
dir_stats_origin_can_be_moved
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s %s only collected %d crypto states for ino %llu (op %d, err %d)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%s:%d: %s unable to create snapshot tree: %d\n
remove_dir_stats_key_on_ino_and_clone_mapping
BSD Name
apfs_reap_extentref_blocks
cst->hdr.retain_count > 0
%d/%d/0o%o
%02hhx
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
%s:%d: %s found mapping tree with old subtype\n
%s:%d: %s spaceman chunks per cib is bad: %d\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
obj_cache_flush_prepare
%s:%d: %s failed to remove dir stats key from <%llu, %llu> clone mapping, error %d\n
%s:%d: %s overprovisioning volume can only mount r/o\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
spaceman_modify_bits
%@num_sb=%zu 
spaceman_fxc_update_length
<40
H
crypto state ep retain count %d is not valid (obj-id %lld, apfs %p)\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s Manually managed omaps don't support snapshots\n
DirStats
authapfs_select_root_hash
get_vol_crypto(apfs) == VOL_PFKEY
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
spaceman-czic-lock
Unknown xf value print format xf_type: %d\n
%s:%d: Cannot allocate %lld bytes for temporary buffer when processing extent %lld @ %lld of inode %lld\n
sha512
%s:%d: %s failed nx_check sanity: %d\n
obj_release
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
btree_node_insert_internal
\\u0016
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
obj_create_internal
%s attr-tag: 0x%llx
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
nx_metadata_range_add
%s:%d: Cannot overwrite an existing snapshot [%s]\n
%s%s %4d :: %s
  crypto-id
%@pmv_t=%llu 
update_jobj
  flags
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%d: %s Failed to remove purgatory_dir drec from fs_root tree: xid %llu, drec %llu, error = %d\n
jobj_refcnt_merge
omap_find_next_snapshot_xid
 type
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: %s couldn't insert cookie err:%s\n
spaceman_free_extent_cache_reset
id %llu not in crypto cache
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s:%d: unexpected payload data size: %lu != %lu\n
%s:%d: %s failed to get next physical extent, error %s(%d)\n
%s:%d: %s tx_finish returned %d\n
DATEADDED
spaceman-fxc-lock
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  child:%s hash:%s\n
com.apple.apfs.
obj_cache_flush_write
%@purge_from_data=%llu 
invalid temporary checkpoint option: %s
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
 %d:%.*s
%s:%d: %s unable to get spaceman free queue tree: %d\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
File Data Hash
dir_stats_moved
Purgeable
ef_oid:%llu sb_oid:%llu create_time:%llu inum:%llu ctime:%llu ef_type:0x%x flags:0x%x name:%u:%.*s
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
apfs_clonegroup_update_dir_stats_key
apfs-phys-ext-oid-lock
%s:%d: %s cannot assert cst %llu for bg access because we have reached asserted cst threshold\n
\\u0004
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
spaceman_chunk_zone_info_recent_decrement
%lld/%lld/%lld/%lld
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
fd_dev_write_extended
process_inode_record
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
check_stale_doc_id_index
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
 DELETED
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s:%d: %s Failed to remove purgeable record (drec): %d (%s)\n
lookup_and_remove_purgeable_record
%s:%d: Couldn't set sparse bytes extended attribute on ino %lld, error %d\n
%s:%d: don't know how to merge refcounts on objects of type %d\n
%s:%d: %s snap meta tree %lld: %d\n
hash_file_extent
filter_purgeable_flags_for_vol
%s:%d: %s failed to get object oid %lld: %d\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
%s:%d: Sealing volumes with fstree type: %u is not supported\n
%s:%d: %s ino %llu is flagged as dir-stats origin but has no dir-stats key\n
%s:%d: %s fs %llu is not formatted for sealing!\n
%s:%d: %s Failed to update purgatory_dir: xid %llu, ino %llu, error = %d\n
%s:%d: %s error %d while removing extents on %lld\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
cynfhvds:o:pH:F:t:TM:R:V:I:D:PU:u:SfrE:XxLam
Invalid arguments: [-m] requires [-u] option
doc_id_tree_destroy
%s:%d: %s The directory hierarchy rooted at ino %llu was modified - please retry.\n
%s:%d: %s Failed to create purgeable record (drec) for lookup (ino %llu): %d (%s)\n
MODKEY
%@vers=%s 
%s:%d: %s failed to find <%llu, %llu> clone mapping, error %d\n
mark
%s:%d: %s failed to init xfield %d for dir-stats %llu: %s (%d)\n
%s:%d: %s obj_modify of (%llu) failed - %d\n
???
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
%s:%d: Cannot delete old filesystem root tree of volume %s: %s(%d)\n
%s:%d: %s xattr %lld:%s err %d decrementing crypto state id %lld (xattr dstream id %lld)\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
spaceman_decrement_free_queue_count
%s:%d: %s Cannot fetch next entry in the filesystem tree: %s(%d)\n
Records breakdown: 
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
defwrite
invalid filesystem index (%ld) for %s
%s%s %llu%s
unknown
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
btree node: flags 0x%x %s%s%s%s%s%s LVL %d TOC %d/%d # %d/%d free %d %d %d tot %d\n
%s:%d: %s Couldn't rename snap %llx to %s\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
ino-io-lock
clear_invalid_fixups
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s failed to update <%llu, %llu> clone mapping, error %d\n
%s:%d: using 8k root hash\n
\\\"
%s:%d: %s Volume has unsupported purgeable record type: %u\n
%s:%d: %s unable to get doc-id tree: %d\n
%s:%d: %s Couldn't lookup_ge (group:%llu inum:0 priv_id:0): %s\n
%s:%d: wrlock == 0 failed %d\n
<20
%s:%d: %s spaceman cab count is bad: %d\n
virtual object dirty count underflow\n
%s:%d: %s unable to get snapshot tree: %d\n
%@data_size_hardlnks=%llu 
%s:%d: hash mismatch! expected: %s, actual: %s\n
btree_node_space_stats
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
%s:%d: %s object type 0x%x not reapable?: %d\n
obj_checkpoint_known
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
Snapshot name [%s] cannot be used because it's reserved
 signing-id
%s:%d: %s error updating chained key for calculating dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s tree creation failed: %d\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
we asked for %lld blocks but got zero (paddr %lld) from spaceman_alloc() and no error.\n
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: %s failed to set dir-stats key %llu on ino %llu: %s (%d)\n
com.apple.fs.cow-exempt-file-count
apfs-clonegroup-lock-mutex
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s Tree delete oid %llu threw %d\n
nx_checkpoint_traverse
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
File Attribution Tag
\\t
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
not handling the flushing tx!\n
 prev-size
failed to create fsroot tree: %s(%d)\n
clone_mapping_remove
isys
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
apfs-fext-tree-oid-lock
%s:%d: %s Cannot insert purgeable record with zero atime (ino %llu).\n
%s:%d: %s Couldn't remove extent at pbn %llu, err=%d\n
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
usage: %s [options] <volume_path>\n
com.apple.ResourceFork
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
apfs_clonegroup_unlock
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
%@dirstats=%llu 
%s:%d: %s cab %d cib count %d should be %d\n
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
current tx not closed/flushing?!\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
 pad1
remove_hash_file_info_record
nx_reaper_add_sub_object
obj_cache_remove_graft_persistent_ephemeral
%s%s %d/%d/0o%o%s
Cannot find inode %lld in the source tree: %s(%d)\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s ino %lld did not have a source-purge-id\n
nx_reaper_wait
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
 nlink
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s container block size too small for device block size (%d < %d)\n
%s:%d: %s failed to lookup file extent for data stream %llu: %s(%d)\n
unknown hash type: %s, (supported: sha256, sha512_256, sha384, sha512, sha3_256, sha3_384, sha3_512, sha3_256_4k, sha3_384_4k, sha3_512_4k)
size_tracking_untrack_inode
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
apfs_free_data_blocks
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
apfs_remap_records_fsroot
%s:%d: %s unable allocate space that should be there: %d\n
insert_purgeable_record
jobj_to_key_val
%s:%d: %s key.hdr.kind != NEW && numsnapshots == 0\n
_remove_extents_of_file_cb
%s:%d: %s failed to fix up checkpoint data: %d\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
btree_check_ext
can't have a negative refcnt on crypto state %llu refcnt %d\n
total_count
fext_tree_iterator
Expanded
%s:%d: %s X %d\n
descendants:%llu phys-size:%llu resource-fork-size:%llu gen-count:%llu flags:0x%x chained-key:%llu
%s:%d: %s Couldn't get existing pfkur tree, err %d\n
ro
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
clone_mapping_remove_locked
%s:%d: %s unsupported tree type, %d\n
Protocol Characteristics
%@xp_data=%lld 
com.apple.FinderInfo
%s:%d: object memory manager failed to create lock, error: %d\n
update_size_tracking
%@source_meta_size=%llu 
main
%s:%d: %s is not an APFS volume\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj.c
nx_metadata_range_optimize
%s:%d: An error occurred while checking if a snapshot with name [%s] is already present: %u %s\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu) : %s\n
rdonly
spaceman_ip_bm_block_free
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: Unsupported configuration - detected sparse region in data stream %lld between %lld and %lld\n
%s:%d: %s failed to tx enter, error %d\n
\\u0015
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
%s:%d: %s Failed to create purgeable record (drec) for time/flags modification (ino %llu): %d (%s)\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
FSRoot Tree NODES in detail: \n
level %d: %d nodes\n
physical size
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s failed to remove ext %lld:%lld for obj %lld (ret %d)\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
%s%s %lld)%s
%s:%d: Cannot copy file extent (dstream %lld, range [%llu:%llu) ) to new fext tree: %s(%d)\n
update_size_tracking_purgeable_size
%s:%d: %s added initial cow-exempt-count xattr!\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s failed to initialize free extent cache, error %d\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
spaceman_fxc_print_stats
level %d: %d nodes %.2f average descendents\n
%s:%d: %s Can't get tree: %d\n
%s:%d: %s set cloneinfo_id_epoch to %llu\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
Saved %d bytes of type %d (block size: %d) hash which starts with %x to %s\n
%s:%d: %s btree_node is null\n
jdev_fext_read_data() corrupts encrypted data
%s:%d: %s superblock container size %lld greater than device size %lld\n
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%@dev=%s result=%d 
Z
omap_sanity_check
_omap_snapshot_create
nx_tx_wait
spaceman_free_fs_deduct_block_counts
Invalid arguments: [-r] requires [-S | -s] option
Sealed fsroot tree has %llu records\n
%s:%d: %s Failed to fetch crypto for crypto_id %lld\n
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: %s checking the generation count was specified but the generation count of ino %llu is zero.\n
spaceman_check_allocation_status_internal
%s:%d: %s waiting for transaction to finish\n
%s:%d: Cannot mark volume %s(%lld) as changing: %s(%d)\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
%s:%d: %s failed to get data stream for extended attribute %llu: %s(%d)\n
%s_%d
apfs_update_cow_exempt_file_count
num children:%lld total size:%lld gen-count:%lld chained-key: %lld
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
%s:%d: Failed to create snapshot [%s] : %u - %s\n
%s:%d: %s iterate_jobjs failed with error %d\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
authapfs_validate_node_hash
ino_has_vnode(ino)
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
%s%s%llx
%s:%d: %s couldn't allocate memory for checkpoint map block\n
automounted
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
tx_enter_internal
unknown option: %s
IOService
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: can't get the device block size (%s). assuming 512\n
nx_check_reaper
apfs_clonegroup_full_clone_scan
%s:%d: %s Error: tx[%lld] failed to start: %d\n
%s:%d: %s Cannot parse remapping dictionary from %s: error information not available\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
%s:%d: %s Cannot find inode %lld in the fsroot tree: %s(%d)\n
%s%s %9s : %s
 file-size
%s:%d: %s failed to set up spaceman for demo mode: %d\n
committmpcp
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
APFS_BTREE_NODES
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: Not enough information to import digest at offset %lld of data stream %lld: expected at least %zd bytes, got %zd\n
attach_policy_to_crypto_state
ino-lock
%s:%d: %s failed to get ino %lld\n
tx_flush
private-id
%s:%d: Cannot insert range to deallocate (%lld+%lld) at offset %lld in data stream %lld - %s(%d)\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
spaceman_checkpoint_traverse
SiblingMap
%s:%d: failed to map img4 file (%lld) bytes: %s (%d)\n
%s:%d: %s Couldn't insert snap_meta_ext for snap_xid %llu, err %d\n
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
btree_delete
apfs_clonegroup_find_and_demote_last_full_clone
spaceman_chunk_zone_info_add
update_tree
%s:%d: Cannot find volume %s\n
ino_set_rage
%s:%d: %s failed to get ino %lld in dir %lld\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
%@ip_freeq_start=%llu 
failed to get next fsroot tree entry: %s(%d)\n
%s:%d: %s Failed to insert purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n
nx_mount
%s:%d: %s bad clonegroup_cookie_key_t, klen:%u vlen:%u group_id:%llu\n
%s:%d: Fatal: Free space is projected to be below the min free blocks for rootfs (%lli <= %u) after flush\n
 total written
%s:%d: %s Cannot dereference overallocated range (%lld+%lld): %s(%d)\n
sanity_check_alloced_blocks
 dir-gen-count
%s:%d: %s failed to get shadow dir-stats %llu for calculating dir-stats %llu (ino %llu): %s (%d); size tracking may go out of sync\n
get_purgeable_record_id_for_lookup
obj_checksum_verify_phys
flags: 0x%x, phys-size: %llu
omap_reap
%@total_t=%llu 
%s:%d: %s failed to clear purgatory dir nchildren %s(%d)
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/fscommon/purging.c
%s:%d: %s crypto_obj_insert of new crypto_id %lld should not have failed (ret %d)\n
%s:%d: %s cannot insert file extent record for extent of %lld bytes at offset %lld of data stream %lld in transaction %lld: %s(%d)\n
clone_fs
%s:%d: %s object type 0x%x not reapable: %d\n
Successfully validated hash %s\n
%s:%d: %s skipping extended attribute file extent: %lld\n
 embedded data size
Unknown hash type
<BAD-VAL-LEN>
\\u0003
%s:%d: %s did not find purgeable record for ino %lld (parent id %lld) (fsize %lld)\n
%s:%d: %s invalid ref count %d for non NULL zero ref tree\n
adjust_extent
jobj_validate_key_val
we asked for %lld blocks but got %lld (orig %lld, blks_this_allocation %lld)\n
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
\\u0007
md %d, off %u
remove_purgatory_entry
alloc_space_for_write_with_hint_and_spino
%s:%d: %s tx_leave failed with error: %d\n
<UNKNOWN-CLONEGROUP-TYPE>
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s:%d: %s parent is %lld name is %s\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: %s unable to allocate chunk zone info cache\n
com.apple.os.update-
bt_merge_up
%s:%d: %s failed to remove drec %lld:%s ino %lld ret %d\n
%s:%d: %s unable to get snap meta tree %lld: %d\n
ephemeral
  phys-block-num
empty 
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: DANGER! got the same extent for logical addr %lld twice!\n
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
userquota
com.apple.fs.altlink
CryptoState
protect
nx_tx_wait_open
Using %s digest algorithm\n
%s:%d: %s omap_destroy returned %d!\n
 info:%u %lld
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%d: %s Found corrupt record: %s\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
NO-NAME
update_dir_stats
io_get_num_device_blocks
%s:%d: %s Failed to remove (group:%llu inum:%llu priv_id:%llu): %s\n
spaceman_chunk_zone_info_compare
%d
DstreamID
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
\\n
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
_fs_add_xattr
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
  len
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
%s:%d: %s deleting extent %lld %lld with invalid owning_obj_id %lld while apfs_num_snapshots is 0, this will cause overallocation\n
fs_remove_snapshot_metadata
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
%s:%d: %s Error inserting cookie (group:%llu): %s\n
%@data_num_fclones=%llu 
 decmpfs magic
Hashed %lld bytes of plain text data for data stream %lld\n
%s:%d: %s Cannot fetch next overallocated entry: %s(%d)\n
asv_process_decmpfs_xattr
\\u0006
removal
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
authapfs_integrity_meta_create
\\u0017
nx_check_superblock
%s:%d: reaper thread is exiting, returning EBUSY\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
 <%llu/%llu>
object-lock
%s:%d: %s tx_finish() failed, %d\n
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s obj_modify failed - %d\n
%s:%d: %s failed to get fsys oid %lld: %d\n
not handling the current tx!\n
%@purge_full=%llu 
Found %lld overallocated data streams, maximum number of actively tracked uncompressed data streams with overallocations was %lld\n
logical addr
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: Cannot decompress chunk at offset %lld in data stream %lld: %s(%d)\n
%s:%d: %s Failed %s purgeability on directory %llu: %d (%s)\n
%s:%d: device initialization failed: %d\n
object-cache-list-lock
%s:%d: %s omap tree type 0x%x is bad\n
%@tgt_fsroot_depth=%llu 
dump_xf
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
invalid crypto id
apfs_clonegroup_validate_record_size
omap_snapshot_create
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s removing xattrs returned ENOENT for private-id %lld (ino %lld)\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s Couldn't create new extentref tree, err %d\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s:%d: %s failed to get reap list head: %d\n
spaceman-czic-scan-lock
Trying to update a namedstream inode %llx on volume %s\n
lookup_jobj_ext
%s:%d: %s trying to restore refcnt on dstream id %llu\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
Failed to escape special characters
raw_xattr_remover
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
X
\\u001d
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
 fs-uuid
Update
!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))
atime
apfs_create_doc_id_tree_if_needed
%s:%d: %s btree_node_insert_internal failed: %d\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
fs_rename_snapshot
%s:%d: %s omap xid %lld > spaceman xid %lld\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
%s:%d: Could not start a transaction for volume %s: %s(%d)\n
 dir_nlink
%s:%d: %s Cannot extract information for inode %lld: %s(%d)\n
%s:%d: %s tree_node_count failed for fsroot of fs %llu, %s(%d)\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
<UNKNOWN>
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
apfs-snap-delete-lock
bt_shift_or_split
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: %s failed to compare currently available space: error %d\n
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
hash_chunks
%s:%d: %s failed to initialize fsroot tree iterator: %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
fs_update_unwritten_extent_record
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
Remapping cannot be executed in dry run mode
apfs-rename-lock
apfs_sanity_check
%s:%d: %s btree check called with non-root btree node: %d\n
\\u001e
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
rw
<60
%s:%d: %s Cannot restore unwritten status of extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
%@findcg_t=%llu 
failed to create jobj: %llu - %u\n
 alloced-size
%s:%d: %s failed got get next fsroot tree entry: %s(%d)\n
DirRecord
btree_node_child_val
supplemental_tree_get
unable to mount NX container @ %s
ACCESS
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s oid (%llu) failed to set hash at index %d - %d\n
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
%llu, %llu
%s:%d: %s unable to get fs root tree: %d\n
spaceman_alloc_fxc_scan_wait
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
%@purge_all=%llu 
btree_iterate_nodes
_fd_dev_write
refcnt:%u persistent-class:0x%x
Conflicting options: [-V] [-I]
RefCntUpd
fd_dev_read_helper
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
Cannot remove sibling information for directory entry of inode %lld in directory %lld: %s(%d)\n
clone_mapping_update_flags
com.apple.system.Security
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
Making a snapshot [%s]:%s tagging as root\n
%s%s %s%s
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
apfs_clonegroup_lock
%s:%d: %s Found no other mapping. (group:%llu inum:%llu priv_id:%llu) count=%u found_inum=%u\n
%s:%d: %s Failed to update extended fields when %s APFS_PURGEABLE_MARK_CHILDREN on ino %llu: %d (%s)\n
%s:%d: %s tx_enter_frozen() failed: %d\n
%s:%d: %s Already partial! (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu)\n
asv_process_rsrc_xattr
(((ino->mode) & 0170000) == 0100000)
%s:%d: %s error getting next checkpoint map block address %d: %d\n
Could not initialize the NX container from %s
SnapName
%s:%d: %s Failed to create purgeable record (drec) for removal: %d (%s)\n
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
%s:%d: %s error starting move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s Unknown purgeable record type (%hhu)\n
%s:%d: %s Trying to delete space for extent %lld %lld which has invalid owning_obj_id %lld\n
%s:%d: %s failed to restore orig_fext, ino %llu, pbn 0x%llx, laddr 0x%llx, len %llu, crypto_id %llu, error %d\n
APFS_TREE_LOOKUP_ZONE
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
nx_corruption_detected_int
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
```
