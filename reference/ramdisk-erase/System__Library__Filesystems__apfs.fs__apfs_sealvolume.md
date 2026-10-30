# `/System/Library/Filesystems/apfs.fs/apfs_sealvolume`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 759,952 bytes.

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
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s invalid object size: %d size_phys %d\n
%s:%d: %s Checking for solo group returned error: %s\n
%s%s %6lld%s
com.apple.os.update-
%s:%d: %s failed to lookup file extent for data stream %llu: %s(%d)\n
%d/%d/0o%o
capacity: nodes  %llu / %llu => %.2f %% used\n
\\u0013
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
nx_reaper_add_sub_object
Using [-I] option without [-R]
IOService
isys
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
btree_seal_callback
fs_map_file_offset_ext
%s:%d: %s spaceman cab count is bad: %d\n
%s:%d: %s fs_tx_enter failed: %s (%d)\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s Failed to update purgatory_dir: xid %llu, ino %llu, error = %d\n
%s:%d: Couldn't set sparse bytes extended attribute on ino %lld, error %d\n
can't have a negative refcnt on crypto state %llu refcnt %d\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
dir_stats_move_origin
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s_%d
%s:%d: %s tree_node_count failed for fsroot of fs %llu, %s(%d)\n
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
.
\\u0010
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s Cannot extract information for inode %lld: %s(%d)\n
Unknown kind %d
bt_shift_or_split
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj.c
snap_xid:%llu
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s superblock container size %lld greater than device size %lld\n
Remapping cannot be executed in dry run mode
%s:%d: Cannot save database header: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
0
\\u0016
%s:%d: %s did not find purgeable record for ino %lld (parent id %lld) (fsize %lld)\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%s:%d: %s can't get <%llu, %llu> clone mapping, error %d\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
%s:%d: Sparse bytes removed from inode %lld internal flags: 0x%llx iflags 0x%llx, new_sparse_bytes %lld; name %s parent-id %lld), but it wasn't marked sparse.\n
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s omap tree sanity check failed: %d\n
nx_check_reaper
fetch_precomputed_digest
F
physical size
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s error searching snapshot tree: %d\n
spaceman_chunk_zone_info_compare
%s:%d: Cannot save metadata hash to %s: %s(%d)\n
found potential %s%sorphan dstreamID record %lld\n
%s:%d: %s error starting move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
%s:%d: %s Failed to find host inode (id %llu) for purgeable drec lookup, falling back to ino %llu\n
ds-id: %llu
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
%s:%d: failed to allocate %d dir stack entries (%zu bytes)\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: %s failed to update <%llu, %llu> clone mapping, error %d\n
ino %lld pos:len %lld:%lld fext %lld:%lld (%lld)\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld err %d\n
%s:%d: %s failed to get ino %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s%s %d,%s
,%s%s %#x,%s
%ss%d:%lld
%s:%d: %s tx_finish returned %d\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s Failed to get next extent: %d\n
make_purgeable_drec_xfs_from_record
iterate_expanded_purgeable_records
%s:%d: %s inode %llu was marked sparse but didn't have a sparse bytes extended field?\n
we asked for %lld blocks but got %lld (orig %lld, blks_this_allocation %lld)\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%@max_stack=%zu 
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
apfs_clonegroup_find_and_demote_last_full_clone
%s:%d: %s Final sync/barrier failed: %d\n
%@num_total_dirs=%zu 
cst_cache
%s:%d: %s omap snapshot count %d seems excessive\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
<BAD-CLONEGROUP_MAPPING-KEY-LEN>
validate_hashed_tree
 spec-telemetry-flags
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
cynfhvds:o:pH:F:t:TM:R:V:I:D:PU:u:SfrE:XxLam
where [options] are\n       -h             display usage\n       -v [-v]        increase verbosity\n       -d             increase APFS logging level from error to debug\n       -p             show sealer progress\n       -n             per
PurgeableTombstone
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s failed to get next physical extent, error %s(%d)\n
---UNKNOWN---
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
not handling the flushing tx!\n
%@vers=%s 
%s:%d: Fatal: Free space is projected to be below the min free blocks for rootfs (%lli <= %u) after flush\n
%s:%d: Database header is too small (%zu bytes)\n
%s:%d: Cannot find volume %s\n
%s:%d: %s failed to set the dir-gen-count xf field on the purgeable rec for ino %lld : err %d\n
exp-dir-stats
Removed INO_EXT_TYPE_FS_UUID for dir (id: %lld)\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
fd_dev_close
%s:%d: %s %s only collected %d crypto states for ino %llu (op %d, err %d)\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s Cannot parse remapping dictionary from %s: error information not available\n
%s:%d: %s Cannot find inode %lld in the fsroot tree: %s(%d)\n
%s:%d: Duplicate record found for digest at offset %lld into data stream %lld\n
__apfs_dec_parent_nlink
%s:%d: %s was NOT able to update/decrement crypto state %lld, err = %d\n
\"%s\":
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
%s:%d: %s Couldn't find name for snap_xid %llu\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
compute_digest
%s:%d: %s failed to init extended fields for dir-stats object on ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s failed to get omap tree for reaping: %d\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
 document-id
<%d
large_key_val_to_jobj
%@freeQ_d=%lld 
Could not initialize the NX container from %s
!(ino->iflags & (JI_RAW_ENCRYPTED))
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
dev
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
<100
%s:%d: %s Attempted to %s range %llu+%llu but it isn't entirely there! (found gap at %llu, next range at %llu+%llu)\n
tmp-ino-clone-
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
omap_cleanup
%s:%d: Cannot mark volume %s(%lld) as changing: %s(%d)\n
%02X
%d
%s:%d: %s tree creation failed: %d\n
nx_reaper_checkpoint_traverse
object-cache-list-lock
%s:%d: %s Couldn't lookup_ge (group:%llu inum:%llu priv_id:%llu): %s\n
spaceman_ip_block_alloc
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
%s:%d: %s full clone scan failed (group:%llu inum:%llu priv_id:%llu): %s\n
%@disk_free_start=%llu 
apfs-incompat-features-lock
version:%u flags:%u current_offset: %llu current_ns_offset: %llu
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
!(ino->iflags & JI_NAMEDSTREAM)
%s:%d: %s failed to allocate a new directory record for file id %llu (obj_id %llu): %d (%s)\n
authapfs_volume_seal
apfs-omap-lock
btree_node_child_val
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
hcp_get_class_ek_uncached
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%@data_num_fclones=%llu 
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
apfs_free_data_blocks_if_needed
id is zero\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%s:%d: %s Failed to lookup purgeable drec (id %llu): error %d\n
zero_tail_of_last_block
%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu) : %s\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
addition
%s:%d: %s failed to update dstream id %lld err %d\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
clone_fs
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
 alloced-size
apfs-fext-tree-oid-lock
%s:%d: %s Failed to fetch crypto for crypto_id %lld\n
jdev_fext_write_data() corrupts encrypted data
%s:%d: %s parent is %lld name is %s\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
invalid lock flags: 0x%x\n
  phys-block-num
failed to update inode record %lld: %s(%d)\n
dir_stats_origin_can_be_moved
CryptoState
sha3_512
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
\\u0019
jobj_refcnt_merge
%s%s %d%s
%s%s 0x%06x%s
, done %lld%% of the fs blocks
total_count
 dhash:%lld
MODVAL
%s:%d: %s %lld:%lld error: %d\n
spaceman-czic-lock
%s:%d: %s failed updating hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
%s:%d: %s tx xid %lld took %lld us to close\n
%s:%d: %s invalid crypto object type %u\n
0x%llx-0x%llx:%d
%s:%d: %s update of the purgatory dir failed! err %d xid %lld\n
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
%s:%d: %s failed to retain crypto-id %llu for ino %llu, %d\n
%s:%d: %s unable to get spaceman: %d\n
 REVERTED
Invalid arguments: [-r] requires [-S | -s] option
Found directory entry in directory %lld for directory inode %lld which has a sibling\n
%s:%d: %s failed to remove dir stats key from <%llu, %llu> clone mapping, error %d\n
%s:%d: Inode %lld has inline compressed data of type: %u\n
%s:%d: %s large key size (%u) on record (%llu) is too small\n
we asked for %lld blocks but got zero (paddr %lld) from spaceman_alloc() and no error.\n
resource fork size
%s:%d: %s key.hdr.kind != NEW && numsnapshots == 0\n
%s:%d: Found incomplete data stream records after update starting with data stream %lld\n
\"%s\"
sha3_512_4k
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
nx_check_recent_sanity_omap
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%s:%d: %s unexpected record type %u id %llu encountered\n
%s:%d: %s adjusting cow exempt count from %lld to %lld\n
apfs_sanity_check
\\u0018
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
%@%s
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s failed to delete ino %lld (%s) iflags 0x%llx err %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
apfs_clonegroup_lookup_locked
spaceman_chunk_zone_info_recent_decrement
%s:%d: %s reverting on error: %d\n
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
%s:%d: locking id %llu, which is already locked by this thread\n
DATEADDED
failed to create jobj: %llu - %u\n
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
%s:%d: %s Failed to estimate pfkur tree size for snapshots, err %d\n
 dstream
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s Failed %s purgeability on directory %llu: %d (%s)\n
%s:%d: Cannot create temporary filesystem tree for volume %s: %s(%d)\n
%s:%d: %s failed to get doc-id tree, error %d\n
union
%@data_ondisk_fclones=%llu 
removed potential orphan dstreamID record (id: %lld)\n
\\u000e
%s:%d: %s Failed to update_jobj(ino %llu) when %s is transitioning from pending-purgeable to purgeable: %d (%s)\n
%s:%d: %s failed to get reap list tail: %d\n
%s:%d: %s unable to get prev doc-id tree: %d\n
%@snap_t=%llu 
%s:%d: Inode %lld has both resource fork with data stream %lld and compressed data in extended attribute\n
%s:%d: %s Failed to create purgeable record (drec) for removal: %d (%s)\n
%s:%d: cannot get ino %llu ek %llu, %d\n
Reference count overflowed for object %p!\n
<UNKNOWN-CLONEGROUP-TYPE>
%s:%d: %s Timestamp set by B+I is %llu\n
apfs_update_cow_exempt_file_count
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
IOBlockStorageDevice
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
type:%u
create_empty_extentref_tree
%s:%d: %s obj_modify() failed: %d\n
 out-of-line data size
%s:%d: %s failed to enter tx - %s(%d)\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s Unexpected unwritten extent for offset %lld of data stream %lld in inode %lld\n
nx_corruption_detected_int
spaceman_alloc
dir_stats_set_purgeable_state
%s:%d: failed to decode img4: %d\n
sha512
%s:%d: %s fs_tx_leave failed for integrity_tree of fs %llu, %s(%d)\n
%s:%d: %s failed to load inode %lld ret %d on volume: %s\n
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
%s:%d: failed to open volume device %s: %s\n
%s:%d: %s failed inserting hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
duplicate_jobj_op_to_shadow_fs_root
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
tx_enter_internal
 physical_size
%s:%d: Cannot allocate memory to hold information about data stream for inode %lld\n
sha512_256
%s:%d: obj is NULL or not apfs object!\n
removal
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s failed to init xfield %d for dir-stats %llu: %s (%d)\n
%s:%d: failed to stat img4 file: %s (%d)\n
%s:%d: %s name is bad, name_len=%lu name[0] = %u\n
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
%s:%d: wrlock == 0 failed %d\n
%s:%d: %s error starting move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s Shadow fs_root does not exist\n
mark_doc_id_index_for_rebuild_if_needed
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s couldn't insert cookie err:%s\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
Internal
%s:%d: Unknown subtype %d for file info object %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
%@dirstats=%llu 
%s:%d: %s added initial cow-exempt-count xattr!\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
%s:%d: Unsupported offline AppleFSCompression extended attribute for inode %lld\n
authapfs_integrity_meta_get_internal
modification
%s:%d: %s Cannot find extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%@num_src=%llu num_dst=%llu 
num children:%lld total size:%lld gen-count:%lld chained-key: %lld
%s:%d: %s failed to get object oid %lld: %d\n
dump_jobjs_for_id
%s:%d: %s created doc-id tree, oid %llu\n
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%s:%d: %s spaceman_alloc() FAILED, err: %d xid: %lld paddr: %lld blocks requested: %lld blocks allocated: %lld\n
spaceman_modify_bits
%s:%d: Could not start a transaction for volume %s: %s(%d)\n
%s:%d: %s failed to read file extent %llu (block %llu) of extended attribute %llu: %s(%d)\n
%s:%d: %s Error looking up dstream id %llu: %d (%s)\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
nx_mount
%s:%d: Why are we comparing a chunk to itself?\n
nx_tx_finish_wait
%s:%d: %s could not get dir-stats %llu: %s (%d)\n
%s:%d: %s ino %lld failed to remove purgatory entry: iflags 0x%llx internal_flags 0x%llx isdir: %d\n
nx-volume_group-lock
%@num_sr=%zu 
Using %s digest algorithm\n
fs_rename_snapshot
obj_mem_mgr_init
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
create_plist_from_file
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
rolling-stats-lock
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: %s chunk %lld recent zone count overflow\n
 alloced_size
failed to get next fsroot tree entry: %s(%d)\n
%s:%d: %s couldn't remove the last clone mapping of private_id %llu, error %d\n
<BAD-VAL-LEN>
val_size_for_jobj
nx-omap-lock
group-id: %llu, type: %u
%s:%d: reaper thread is exiting, returning EBUSY\n
fixup_decmpfs_xattr
0x%llx
image-format-read-only
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
Cannot remove sibling information for directory entry of inode %lld in directory %lld: %s(%d)\n
\\u0003
len:%lld phys:%lld crypto:%lld flags:%llx
%s:%d: %s failed to remove extent for extent-id %lld @ logical offset %lld:%lld err %d\n
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
%s:%d: %s crypto_obj_insert of new crypto_id %lld should not have failed (ret %d)\n
%s:%d: %s failed to get reap list head: %d\n
%s%s %8lld%s
%s:%d: %s failed to create doc-id tree, error %d\n
%s:%d: %s Unsupported flags being used on purgeable record: %llx. Truncating...\n
get_purgeable_record_details
spaceman_free_fs_deduct_block_counts
%FT%T
failed to hash root node: %s(%d)\n
apfs-dir-stats-id-lock
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
lba %llu, len %hu, tweak %llu
%s:%d: %s got err %d writing at pos %lld in obj-id %lld (blkcount %llu, len %zd)\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
nx_tx_wait
Cannot open digest database %s
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
%s:%d: %s cab %d cib count %d should be %d\n
%s:%d: %s iter_next returned %d\n
%@ever_cloned=%llu 
BIRTH
%s%s %lld)%s
dump_xf
failed to dump fsroot tree: %s(%d)\n
%s:%d: %s couldn't get clonegroup tree err:%s\n
%s:%d: %s chunk %lld recent zone count underflow\n
Purgeable
spaceman_fxtp_add_child
%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n
%s:%d: %s skipping extended attribute file extent: %lld\n
capacity: leaves %llu / %llu => %.2f %% used\n
crypto state ep retain count %d is not valid (obj-id %lld, apfs %p)\n
jobj_size_for_large_key_val
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
%@purge_full=%llu 
clone_mapping_update_flags
FULL
%s:%d: %s failed to remove hash file info for id %llu @ logical offset %llu err %u\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
 atag:%lld
%s:%d: %s failed to get a new default crypto-id, ino %lld\n
%s:%d: %s unable to get omap tree: %d\n
%s:%d: %s failed got create jobj for id: %lld (type: %u)\n
dir_stats_get_flags
spaceman-space-usage-lock
Sealing fsroot tree with %llu records\n
/dev/r
  %4d: k:%5d:%-4d  v:%5d:%-4d  <<< ERROR: KEY/VALUE OUT OF BOUNDS >>>\n
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  child:%s\n
 dir-gen-count
Cannot sort extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
/dev/
apfs_unlock_id
%s:%d: %s unable to get omap %lld: %d\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
obj_get_async_read
fext_tree_iterator
process_xattr_record
%s:%d: %s Couldn't acquire lock on %llu-%llu, err=%d\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
 fs-uuid
update_tree
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
%s:%d: %s failed to remove ext %lld:%lld for obj %lld (ret %d)\n
apfs_clonegroup_full_clone_scan
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%@pure_cloned_apps_blk=%llu 
%@purge_from_data=%llu 
%@features=0x%llx 
%s
com.apple.fs.altlink
%s:%d: Cannot save information about digest at offset %lld into data stream %lld: %s (%d)\n
%s:%d: %s failed to find <%llu, %llu> clone mapping, error %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
update_purgeable_record_time_and_flags
%s:%d: %s X %d\n
ino %lld illogical file extent %lld:%lld != alloced_size %lld (fsize %lld)\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s couldn't get clonegroup tree: %s\n
DELETE 
%s:%d: %s started cleaning snapshots %lld-%lld\n
sha256
authapfs_validate_node_hash
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
rw
spaceman_sanity_check
%s:%d: %s iterating over fsroot tree records\n
%s:%d: %s Coludn't remove dir stats key from (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s Deleted the shadow_fs_root tree %p\n
new address mismatch on redirty 0x%llx 0x%llx\n
committmpcp
btree node: flags 0x%x %s%s%s%s%s%s LVL %d TOC %d/%d # %d/%d free %d %d %d tot %d\n
Protocol Characteristics
invalid unlock flags: 0x%x\n
spaceman_set_up_ip_reverse_mapping_tree
\n
 nchildren
<20
%s:%d: %s tx manager initialization failed: %d\n
%s:%d: %s unable to allocate chunk zone info cache\n
 type
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s invalid zero len, paddr %llu\n
%@src_fsroot_2nd_depth=%llu 
 nlink
\\u0014
obj_checksum_verify_phys
quarantine
%@findcg_t=%llu 
%s:%d: %s bt_move_entries %d failed: %d\n
jobj_allocate
obj_create_internal
\n---------------------------------------------------------------\n
DstreamID
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
spaceman-fxc-lock
%s:%d: DANGER! got the same extent for logical addr %lld twice!\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s Couldn't get existing pfkur tree, err %d\n
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
 
%u
%s:%d: %s failed to tx enter, error %d\n
update_dir_stats
invalid temporary checkpoint option: %s
 xf-size
logical addr
,%s%s %d,%s
SiblingMap
apfs-stream-id-lock
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
obj-mem-mgr-lock
spaceman_cib_sanity_check
%s:%d: %s Cannot parse remapping dictionary from %s: %s\n
capacity: all    %llu / %llu => %.2f %% used\n
%s attr-tag: 0x%llx
CHANGE
%s:%d: %s spaceman IP bm base address is bad: %lld\n
apfs_clonegroup_validate_record_size
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
%s:%d: *** unknown obj type %d\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
spaceman_fq_tree_find_overlap
%s:%d: %s copied %llu fsroot tree records into new fsroot tree\n
 prev-size
obj-id %llu type %u still has refcount %d\n
jobj_type_from_possibly_large_key
full clone size
%s:%d: %s bad clonegroup_key_t, size:%u\n
ro
suid
%@oc_hit=%llu 
asv_extract_hash_blob
key_val_to_jobj
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s waiting for available tx to open: xid %lld\n
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
\\u0002
nx_reaper_sanity_check
spaceman_chunk_zone_info_add
%s:%d: %s lookup_next_snapshot() returned %d\n
%s:%d: %s updating grandparent failed w/%d\n
tx_checkpoint_space_check
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
Target Disk Mode
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
Invalid arguments: [-I] requires [-R] option
 total written
set
\\u0012
%s:%d: device initialization failed: %d\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
obj_cache_flush_prepare
createtmpcp
spaceman_free_extent_cache_setup
(((ino->mode) & 0170000) == 0100000)
%s:%d: don't know how to merge refcounts on objects of type %d\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
last_clone_cb
purgeable size
%s:%d: %s failed to compare currently available space: error %d\n
virtual object dirty count underflow\n
%s:%d: %s failed to iterate fsroot tree for jobj %llu: %s (%d)\n
jdev_fext_read_data
%s:%d: %s danger - crypto id %lld had refcnt %d\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
%s: Unknown xfield xf_type: %d\n
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
<40
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
nx_tx_wait_open
%s:%d: %s Skipping sibling id XF for directory entry %s (id: %lld) for inode with single link count (id: %lld)\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
 gen-count
%s:%d: %s failed to compute root_hash - %d\n
%lld:%lld
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
nx_tx_finish_wait_for_dirty_data
%@fl=%d
Failed to escape special characters
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: %s Failed to create purgeable record (drec): %d (%s)\n
%s:%d: %s unable to get omap snapshot tree: %d\n
nx_checkpoint_load_data
obj_modify
obj_delete_internal
dir_stats_moved
%s:%d: %s error finishing move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to initialize free extent cache, error %d\n
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
%@data_size_fclones=%llu 
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
invalid tweak type %d\n
%@decloned=%llu 
failed to seal fsroot tree: %s(%d)\n
%s:%d: ** BOGUS FEXT FLAGS = 0x%02x (crypto_flags = 0x%llx)\n
child_remover_cb
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s failed to increment crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
%s:%d: %s error getting mapping tree: %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
%@source_meta_size=%llu 
%s:%d: Sealing volumes with block size: %u is not supported\n
key_size_for_jobj
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
%s:%d: %s failed to leave tx, error %d\n
MODKEY
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s failed to add initial cow-exempt-count xattr! err %d\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
Release count overflowed for object %p!\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s ino %lld file extent %lld:%lld extends beyond alloced_size %lld (fsize %lld). fixing it.\n
apfs_lock_id
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
paddr
Trying to update a namedstream inode %llx on volume %s\n
nx_superblock_agrees_with_container_superblock
%s:%d: %s failed to remove <%llu, %llu> clone mapping, error %d\n
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
update_sparse_bytes
%s:%d: %s spaceman chunks per cib is bad: %d\n
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s Cannot create URL for %s\n
%s:%d: ***: unknown obj type %d\n
object-cache-lock
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
%s:%d: %s couldn't insert record type %u id %llu into new tree, error %d\n
failed to initialize fsroot tree iterator: %s(%d)\n
get_purgeable_record_id_for_lookup
 source-purge-id
FSRoot Tree Debug Output: \n
Failed to initialize hash override table: %s(%d)\n
SYSTEM_GRAFT_4K_OBJS
\\u0004
\\\"
%s:%d: %s Tree iteration threw %d at cursor %llu\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: Cannot insert file info object for offset %lld of dstream %lld into new filesystem tree: %s(%d)\n
clone_mapping_clear_flags
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s Inserting snap_name failed, %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
PhysExtent
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
make_jkey_from_jobj
refcnt:%d
spaceman_allocation_init
Found orphan dstreamID record (id: %lld), skipping...\n
length
%s:%d: %s failed to fetch sub-dir ino %lld\n
\t%16p %s\n
tx-mgr-lock
%s:%d: unlock == 0 failed %d\n
Removable
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s failed to find valid checkpoint: %d\n
%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n
%s:%d: %s failed to delete doc-id tree, error %d\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
 orig-sync-root-id
%s:%d: Cannot copy file extent (dstream %lld, range [%llu:%llu) ) to new fext tree: %s(%d)\n
%s:%d: %s Failed to get file ID from purgeable record key/val: error %d\n
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
%s:%d: %s Cannot open remapping dictionary from %s: %s\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
btree_node_val_range_validate
%llu, %llu
%s:%d: can't get features for device (%s)\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
_remove_extents_of_file_cb
%@ip_freeq_start=%llu 
%@pmv_t=%llu 
clone_mapping_remove
apfs-integrity-meta-lock
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
 hashed_len
%s: Invalid arguments os: %p xf: %p\n
%s:%d: %s failed to restore refcnt on dstream id %llu, err: %d\n
%s:%d: %s Couldn't create new extentref tree, err %d\n
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
obj_checkpoint_start
apfs-snap-delete-lock
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s Invalid purgeable record type %u found on volume expecting type %u\n
%s:%d: %s Failing with error=%d\n
INSERT
nx_reaper_add_ext
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
Invalid arguments: [-P] requires [-I] option
%llu
%s:%d: %s extentref tree %lld: %d\n
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
Cannot make snapshot in dry run mode
%s:%d: %s Cannot copy object %lld(%d) to new filesystem tree: %s(%d)\n
apfs_sanity_check_tree_type
cst->hdr.retain_count > 0
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
tx_leave
  len
set_cloneinfo_id_epoch
%s:%d: %s omap tree type 0x%x is bad\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
ephemeral
jobj_to_key_val
 %llu
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
apfs_clonegroup_update_purgeable_urgency
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
%s:%d: %s oid (%llu) unexpected oid at index %d - (%llu!=%llu)\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
spaceman_fs_bounds_clear
spaceman_fq_tree_insert
%s:%d: %s create_plist_from_file failed\n
Cannot serialize extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
spaceman_free_extent_cache_remove
update_jobj
nx_check_omap
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: %s fext_tree_update returned %d\n
ino
%s:%d: %s tx_finish() failed, %d\n
%@purge_from_user=%llu 
%@(%d:%d)
apfs_release_objects
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
ino->rsrc_ekwk != ekwk
%s:%d: %s error %d while removing extents on %lld\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
apfs_update_phys_range
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
remove_clone_mapping_if_last
%s:%d: %s apfs_update_phys_range failed, err = %d\n
%s:%d: %s Failed to remove snap_name record!\n
%s%s %lld/%lld/%lld/%lld%s
merge_ino_purgeable_flags
%s:%d: %s failed to get fsys oid %lld: %d\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
fs_write_stream
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s dstats-key: %llu
Invalid arguments: [-m] requires [-u] option
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s btree check called with non-root btree node: %d\n
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
spaceman_free
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: Cannot delete old fext tree of volume %s: %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
physical_size:%llu flags:0x%x
UNKNOWN TXN TYPE
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%@prepro_t=%llu 
invalid filesystem index (%ld) for %s
%s:%d: %s failed to remove shadow dir-stats object (id %llu): %s (%d)\n
 0x%06x:%u:%.*s
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s unable to get snapshot tree: %d\n
dereference
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
spaceman_trim_free_blocks
size
BSD Major
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
 unexpected type %d @ %lld!
 inline
authapfs_insert_root_hash
%s:%d: %s Couldn't copy pfkur tree into new object, err %d\n
%s:%d: %s failed to decrement crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
spaceman_freed
%s:%d: %s unsupported tree type: %d\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
spaceman_ip_bm_block_free
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s xid %lld second sync/barrier failed: %d\n
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s Cannot open remapping dictionary from %s: unknown error\n
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
\\u0007
%s:%d: %s Failed to copy supplemental tree (type %d): %d (%s)\n
%s:%d: %s The directory hierarchy rooted at ino %llu was modified - please retry.\n
%s:%d: %s Can't get tree: %d\n
%s:%d: %s Trying to delete space for extent %lld %lld which has invalid owning_obj_id %lld\n
START
%s:%d: Cannot allocate memory to track excessive space allocations in data stream %lld\n
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
loadtmpcp
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: %s failed to get data stream for extended attribute %llu: %s(%d)\n
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s Couldn't insert snap_meta_ext for snap_xid %llu, err %d\n
apfs_checkpoint_traverse
doc_id_tree_invalid_crypto
%s:%d: %s Failed to remove purgeable record (ino %llu): error %d\n
%s:%d: %s xattr %lld:%s err %d decrementing crypto state id %lld (xattr dstream id %lld)\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
%s:%d: %s couldn't get tree, err %d\n
demomode
spaceman_ip_bm_block_alloc
Unexpected extended attribute %s for inode %lld (flags 0x%x)\n
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: %s extended attribute %llu had an unexpected data stream id: %lld\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
nx_checkpoint_find_highest_xid
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
spaceman_upgrade_sm_version_0_to_1
%s:%d: %s stopped updating dir-stats due to chain being too long\n
hcp_get_class_ek
%s:%d: %s snap meta tree %lld: %d\n
%s:%d: %s object cache initialization failed: %d\n
%s:%d: %s Couldn't find lock for (group:%llu inum:%llu priv_id:%llu)\n
%s\n
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
file-id: %lld date-added:%lld flags:0x%x
nx_check
Encrypted
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
%s:%d: %s ino %llu is compressed and this volume does not support compressed purgeable files.\n
%s:%d: Cannot delete old filesystem root tree of volume %s: %s(%d)\n
 uncompressed size
 hash_size
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
defwrite
 internal_flags
%s:%d: stale clone mapping <%llu, %llu> had non-empty extended fields\n
crypto_obj_free
%s:%d: %s Failed to create purgeable record (drec) for time/flags modification (ino %llu): %d (%s)\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
main
%s:%d: %s apfs, filepath or new_fsroot_tree is null\n
update
curproc
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
spaceman_free_extent_cache_insert
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
\\u000f
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%s:%d: invalid object size: %d size_phys %d\n
 not
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
cleanup_purgatory_dir
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: WARNING WARNING WARNING!!! Invalid root hash: %s (expected: %s)\n
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
%@dev=%s result=%d 
%s:%d: %s Lookup for key %s failed in the remapping dictionary\n
 sparse-bytes
%s:%d: %s Cannot dereference overallocated range (%lld+%lld): %s(%d)\n
BSD Name
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
%s:%d: Failed to remove sparse bytes attribute from ino %lld, but it was successfully got, errro %d\n
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s failed to update dir-stats %llu: %s (%d)\n
assertion failed: %s
private-dir
%s:%d: %s failed to delete dir entry %lld:%s (file-id %lld) ret=%d\n
%s:%d: %s error: fs_tx_leave_ext returned %d\n
%s:%d: %s cab %d index %d should be %d\n
APFS_8K_OBJS
???
%s:%d: %s failed to enter tx to update size tracking for ino %llu: %s (%d); size tracking may go out of sync\n
=%d
btree_iterate_nodes returned non-zero: %d\n
dev_init_common
btree_node_key_range_validate
btree_node_free_list_entry_validate
%s%s %#x%s
%s:%d: Failed to lookup last digest in hash db: %s(%d)\n
Inode
apfs_reap_extentref_blocks
%s:%d: %s couldn't delete tree, err %d\n
%s:%d: %s failed nx_check sanity: %d\n
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
 bsd_flags
%s:%d: Cannot hash file extent (dstream %lld, range [%llu:%llu) ) for new  filesystem tree: %s(%d)\n
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
lookup_and_remove_purgeable_record
orphan_snap_check_iterator
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
spaceman_free_completed
 name-len
FSRoot Tree NODES in detail: \n
Cannot find inode record for inode %lld in sibling map record %lld: %s(%d)\n
%s:%d: %s Failed to insert purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n
%s:%d: %s didn't find <%llu, %llu> clone mapping which was expected, not failing\n
%@purge_all=%llu 
 parent-id
capacity: %9d %9d %9d %9d %9d %9d\n
%s:%d: ino %llu has no ekwk id\n
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
apfs_clonegroup_inode_became_partial_clone
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
update_dir_stats_by_key_ext
sha384
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
%s:%d: %s failed to clean up doc-id trees, error %d\n
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
fs_is_phys_range_writable
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
spaceman_trim_free_extent_callback
%lld
  crypto-id
 total_count
<80
attr tag
nx_reap_list_sanity_check
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
Timestamp specified as command line argument is ignored when remapping
%s:%d: %s Cannot fetch next overallocated entry: %s(%d)\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s Couldn't copy fext tree into new object, err %d\n
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
get_vol_crypto(apfs) == VOL_PFKEY
%s:%d: %s Failed to lookup purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n
update_file_extent
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
spaceman-dev-lock
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
%s:%d: can't get block count (%s)\n
%s:%d: %s inode %llu is already in purgatory\n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
%s%s %u%s
%s:%d: %s could not get dir-stats %llu to untrack ino %llu: %s (%d)\n
%s:%d: %s Failed to update purgeable flags on ino %llu (new flags %u):%d (%s)\n
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: Failed to create snapshot [%s] : %u - %s\n
update_size_tracking
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: %s btree_node_key_update failed: %d\n
%@num_sb=%zu 
 conformance-nlink
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s Cannot start transaction with XID %lld: %s(%d)\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
 dstats-key
%s:%d: %s failed to delete prev doc-id tree, error %d\n
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%@total_t=%llu 
%s:%d: DStream %lld has compressed size %zd bytes, we found %d extents\n
%s:%d: %s Not enough room in the extent for %lld bytes at offset %lld in data stream %lld to read %lld bytes\n
fd_dev_read_extended
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
%s:%s
 name
purgatory.
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
parent:%lld name:%d:%.*s
icp_dec_ref
%s:%d: unexpected payload type: %s\n
attach_policy_to_crypto_state
fext_collector
finalize_digest
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
btree_check_ext
filter_purgeable_flags_for_vol
%s:%d: %s encryption type %llx unsupported\n
%s:%d: %s deleting extent %lld %lld with invalid owning_obj_id %lld while apfs_num_snapshots is 0, this will cause overallocation\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
apfs-pfkur-tree-oid-lock
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
jdev_fext_read_data() corrupts encrypted data
%s:%d: %s object type 0x%x not reapable?: %d\n
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
unable to mount NX container @ %s
%s:%d: The reaper for device %s failed: %s(%d)\n
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
not handling the current tx!\n
NO-SIGNING-ID
%s:%d: %s fs_tx_enter failed for volume seal of fs %llu, %s(%d)\n
 date-added
unknown
%s:%d: %s failed to get shadow dir-stats %llu for calculating dir-stats %llu (ino %llu): %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to get doc-id tree key count, error %d\n
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
NO-NAME
supplemental_tree_destroy
invalid crypto id %llu
%s:%d: %s unable to get doc-id tree: %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
save_file_info_header
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
md %d, off %u
type = %u, req_tree != fs_root\n
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s unable to get fs extentref tree: %d\n
%s:%d: %s invalid ref count %d for non NULL zero ref tree\n
%s:%d: %s Cannot allocate space for %zu bytes at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
omap_recent_sanity_callback
%s:%d: %s First sync/barrier failed: %d\n
!((apfs)->apfs_main_apfs != ((void*)0))
\\b
%s:%d: %s did not find purgeable drec for file %lld (parent id %lld) (fsize %lld)\n
remove_hash_file_info_record
scalable_id_is_valid(apfs, id)
%s:%d: %s Lookup for key %llu failed in the remapping dictionary\n
apfs-clonegroup-lock-mutex
apfs_reap_snapshots
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
DELETE
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%@num_dirs=%zu 
Could not open metrics log file %s
%s:%d: Cannot create new filesystem tree for volume %s: %s(%d)\n
sha3_256
make_large_jkey_header_from_jobj
%s:%d: %s Found no other mapping. (group:%llu inum:%llu priv_id:%llu) count=%u found_inum=%u\n
%@cloned_apps_blk=%llu 
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
len:%lld phys:%lld flags:%llx
%s:%d: %s couldn't remove (group:%llu inum:%llu priv_id:%llu) err:%s\n
%s:%d: %s Already partial! (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu)\n
%@ip_freeq_curr=%llu 
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
file-size: %llu ds-id: %llu flags: 0x%x uid: %u
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%@ranges_to_move=%zu 
File Attribution Tag
adjust_extent
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
%s:%d: %s directory has an illegal sub-directory (dir: %lld ; sub-dir ino %lld)\n
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: Cannot save information about file extent (dstream %lld, range [%llu:%llu) ): %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: %s directory has an illegal hardlinked child (dir: %lld ; child ino %lld)\n
%s:%d: %s Tree delete oid %llu threw %d\n
%s:%d: %s overprovisioning volume can only mount r/o\n
%s:%d: %s can't add dir %llu for recursive extent deletion\n
apfs_reap
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: Failed to allocate %zu bytes for snapshot name\n
\"%llu\":
 file-size
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
clearing
%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s tx_enter() failed: %d\n
%s:%d: %s failed to fix up checkpoint data: %d\n
3288.52.1
%s:%d: failed to map img4 file (%lld) bytes: %s (%d)\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s Failed to set purgeable drec's dir gen-count: error %d\n
remove_dir_entry_ext
bt_update_last_leaf
add_entry_to_dir_stack
%s:%d: %s ***: expanded obj type found on unsupported volume\n
hash_file_extent
%s:%d: %s failed to initialize fsroot tree iterator: %s(%d)\n
get_dir_stats
mark
\\u0001
auto
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
Sealed fsroot tree has %llu records\n
remove_dir_stats_key_on_ino_and_clone_mapping
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
%s:%d: %s found mapping tree with old subtype\n
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
%s:%d: %s failed to%s update the <%llu, %llu> clone mapping, error %d\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%@incompat=0x%llx 
Removed dstream for compressed inode (id: %lld)\n
%s:%d: %s failed to insert root_hash of fs %llu,- %s(%d)\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
spaceman_checkpoint_traverse
dir_stats_move_regular_origin
%s:%d: %s failed to get integrity_meta obj - %d\n
  %4d: <<< ERROR: TOC ENTRY OUT OF BOUNDS >>>\n
%s:%d: %s cannot insert new ep %llu because the policy cache is full\n
\\u000b
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%@time=%llu 
%@full_clones=%llu 
xsys
%s:%d: Duplicate entry for data stream %lld\n
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  val:[[ %s ]]\n
%s:%d: %s Failed to update_jobj(ino %llu) after %s purgeability: %d (%s)\n
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
%s:%d: %s object type 0x%x not reapable: %d\n
i40@?0q8Q16^v24^Q32
%s:%d: failed to open img4 file: %s (%d)\n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
%s:%d: object memory manager failed to create lock, error: %d\n
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s fext_tree_iterate_fexts failed with %d\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
%s:%d: %s Cannot reset inode information for inode %lld: %s(%d)
io_get_device_block_size
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
dev=%s vers=%s 
Time is too far in the past
 cr/m/ch/atime
%s%s 0x%08x%s
bad pext.\n
Unknown hash type
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
%s:%d: %s cib %lld index %d should be %lld\n
Computed root hash: %s\n
 full_clone_size
cst->ep_retain_count <= cst->hdr.retain_count
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
%s:%d: %s error getting cab %d @ %lld: %d\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
Cannot read digest database %s header
CloneMap
apfs
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
  values: %9s %9s %9s %9s %9s %9s\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s Failed to update purgeable record (drec) time/flags (ino %llu): %d (%s)\n
com.apple.apfs.
apfs_clonegroup_unlock
%s:%d: Information about digest at offset %lld of data stream %lld does not match\n
%s:%d: Unexpected size of extended attribute record for inode %lld: expected %zd, got %d\n
%s:%d: %s fs_tx_enter returned %d\n
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
apfs_clonegroup_check_solo_group
spaceman_fxc_update_length
 atime:%llu file-id:%llu
%s:%d: %s link count == %d for inum %lld?!\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s failed to get ino %lld in dir %lld\n
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
btree_node_reap
%s:%d: %s Failed to insert purgeable record (record): %d (%s)\n
ino_phys_size_ext
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
retain_xdstream_crypto_states
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
userquota
spaceman_free_extent_cache_reset
update_purgeable_clone_tracking
%s:%d: Sealing of encrypted volumes is not supported\n
Compressed data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
Data stream %lld is overallocated: optimal size is %lld bytes, allocated %lld bytes\n
jobj_release
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
Snapshot name [%s] cannot be used because it's reserved
%s:%d: %s Skipping sibling map for inode %llu with single link count (id: %lld)\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s:%d: %s Couldn't insert extent, err=%d\n
fs_tx_enter_internal
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s (%s)
 kind
%s:%d: *** Can't release unknown obj type %d\n
res->xid %lld but xid is now %lld\n
get_unwrapped_ekwk_snap
apfs_mark_inconsistent_
jobj_size_for_key_val
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
nx_reaper
%@num_total_files=%zu 
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
%s:%d: %s Cannot open remapping dictionary from %s: error information not available\n
%s:%d: Length of the hashed region for digest at offset %lld of data stream %lld does not match: expected %d with block factor %d, got %d\n
flags:0x%x
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
nx-tree-node-compact-lock
%s:%d: Cannot create overallocated_ranges tree for volume %s: %s(%d)\n
%s%s %s,%s
Removed dstream for empty inode (id: %lld)\n
%s:%d: %s cp_corrupt_assert() failed: %s
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s failed to attach graft to object cache: %d\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
apfs_clonegroup_lock
bt_merge_nodes
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
%s:%d: %s Coludn't update dir stats key on (group:%llu inum:%llu priv_id:%llu): %s\n
apfs-global-lock
%s:%d: %s Failed to update extended fields when %s APFS_PURGEABLE_MARK_CHILDREN on ino %llu: %d (%s)\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
%s:%d: %s failed to serialize inode %lld: %s(%d)\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: %s xid %lld sync/barrier failed: %d\n
delta_from_dir_stats
insert_jobj
%s:%d: %s Invalid reap list free entry %d\n
%s:%d: %s failed to allocate record for skipped file extent: %lld\n
btree_node_debug_stats
fext_get_crypto_id
%s:%d: %s reap list object free list erroneously empty?\n
spaceman_get_metazone_alloc_index
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
FileInfo
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
get_vol_crypto(apfs) == VOL_CPROTECTED
alloc_space_for_write_with_hint_and_spino
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: An error occurred while checking if a snapshot with name [%s] is already present: %u %s\n
spaceman_fxc_tree_node_recycle_smallest
move_snapshot_to_purgatory
%s:%d: %s Couldn't get existing fext tree, err %d\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
%s:%d: %s failed to insert inode %llu: %s(%d)\n
\\f
remove_extent_of_file
jobj_validate_large_key_val
apfs_clonegroup_delete_inode
reserved metadata space underflow: %lld (%lld)\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
nx_mount_initiate_free_space_trims
%s:%d: Extent for %lld, %lld bytes at %lld points to block %lld\n
 hash
Cannot load extended fields for directory entry of inode %lld in directory %lld: %s(%d)\n
authapfs_select_root_hash
%s:%d: %s apfs_free_data_blocks_if_needed(%llu,%llu) failed: %d %s\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
ino_get_ekwk_
omap_snapshot_create
%s:%d: %s tx_leave failed: %d\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: %s Trash unfinished tx xid=0x%llx\n
Conflicting options: [-V | -I] [-M]
:
%s:%d: %s find_next_snap(%llu) returned %d\n
Skipping unexpected extented attribute %s for inode %lld\n
%s:%d: %s *** unknown expanded obj type %hhu\n
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
%s:%d: %s bad clonegroup_mapping_key_t, klen:%u vlen:%u group_id:%llu\n
private-id
%s:%d: %s fext_tree_remove returned %d\n
 <%llu/%llu>
%s:%d: %s Cannot trim extent at offset %lld in inode %lld from %lld to %lld bytes: %s(%d)\n
fs_update_unwritten_extent_record
%s:%d: %s Value too small:%u (group:%llu inum:%llu priv_id:%llu)\n
owners
%s:%d: Not enough information to import digest at offset %lld of data stream %lld: expected at least %zd bytes, got %zd\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
ino->ekwk == ekwk
%s:%d: %s stable checkpoint indices: desc %d data %d\n
physical object dirty count underflow\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
%s:%d: %s Found directory entry in directory %lld for directory inode %lld which has a sibling\n
SnapMetadata
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s failed to create reap list: %d\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
%s:%d: unexpected payload data size: %lu != %lu\n
PurgeableTomb
%s:%d: %s Fusion is not supported anymore\n
w:
Skipping sibling map for inode %lld with single link count (id: %lld)\n
nx_check_recent_sanity
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
 dir_nlink
** Sealing volume %ss%d...\n
com.apple.fs.cow-exempt-file-count
X
%s:%d: %s fext_ref_extent_key for fext %llu with crid %llu failed with %d\n
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
%@src_fsroot_2nd_nodes=%llu 
obj-id
Relative Node ID: %llu\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
cst %llu hit zero retain count but still has ep related retain count (%u)\n
%s:%d: Sealing volumes with block size: %u is not supported when producing root hash metadata\n
%s:%d: %s failed to remove the stale clone mapping <%llu , %llu>, error %d\n
com.apple.system.Security
0x%llx-dead
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s failed to %s shadow dir-stats %llu as purgeable: %s (%d)\n
%s:%d: %s obj_modify of integrity_meta failed - %d\n
supplemental_tree_get
%s%s %zd%s
apfs-phys-ext-oid-lock
\\u001a
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
remove_jobj
fs_remove_snapshot_metadata
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s Failed to remove (group:%llu inum:%llu priv_id:%llu): %s\n
omap_reap
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
ef_oid:%llu sb_oid:%llu create_time:%llu inum:%llu ctime:%llu ef_type:0x%x flags:0x%x name:%u:%.*s
extent_remover_callback
FSRoot Tree: %llu (keys: %llu, nodes: %llu)
%s:%d: %s dir-stats %llu maintains purgeable size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: Invalid or unknown hash type: %d\n
apfsuuid
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s Manually managed omaps don't support snapshots\n
%s:%d: Cannot find information about digest at offset %lld of data stream %lld - %s(%d)\n
Records breakdown: 
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s Failed to mark the dir-stats record for ino %llu as purgeable: error %d (%s)\n
type:%d
purgatory_cleaner_cb
Attempting to reuse a non-candidate chunk zone info\n
lookup_jobj_ext
%s:%d: %s mount for ramdisk\n
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
iterate_ino_crypto_state
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: %s failed to enter tx to %s dir-stats %llu as needing reconciliation: %s (%d); size tracking may go out of sync\n
asv_read_data_from_extent
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu): %s\n
bt_merge_up
%s:%d: %s oid (%llu) failed to set hash at index %d - %d\n
lookup_expanded_purgeable_record
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s Failed to estimate fext tree size for snapshots, err %d\n
nx_get_evict_mapping_tree
checkpoint
spaceman_metazone_init
v8@?0
%s:%d: Cannot delete old integrity object of volume %s: %s(%d)\n
Cannot find inode %lld in the source tree: %s(%d)\n
apfs-doc-id-lock
%s:%d: %s bogus phase, %u\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%@mv_t=%llu 
hash_chunks
\\u001c
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
trying to zero the superblock!\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
level %d: %d nodes %.2f average descendents\n
%s:%d: %s Aborting iterative purgeable record removal for id %llu because transaction is closing\n
%s:%d: %s failed to remove sibling hard link entry for ino %lld under hardlink/sibling key %lld/%lld w/drec %lld:%s (ret %d)\n
ino-io-lock
_fs_add_xattr
%s:%d: %s unable to get snap meta tree %lld: %d\n
object-cache-reset-lock
 uid/gid/mode
Hashed %lld bytes for dstream %lld\n
%s:%d: %s Found purgeable record with file ID 0!\n
automounted
spaceman_alloc_fxc_scan_wait
%s:%d: Got highest hashed dstream id: %llu\n
btree_node_sanity_check
FIXUP
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
\\u0006
\\n
apfs-phys-lock-state-mutex
purgeable rsrc size
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
object-cache-flush-lock
save_file_info_record
((&crypto_cache->free_list)->tqh_first == ((void*)0))
%s:%d: %s tree_remove(%llu) failed\n
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
tx_finish
skipsanity
process_inode_record
Freeing %llu overallocated dstream ranges\n
btree_node_compact
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu): %s\n
%@xp_data=%lld 
spaceman_free_extent_cache_search
fs_delete_inode_internal
%s:%d: %s failed to free allocated blocks, ino %llu, 0x%llx+%llu, error %d\n
%s:%d: %s Failed to remove snap_meta record!\n
Saved %d bytes of type %d (block size: %d) hash which starts with %x to %s\n
dir_stats_update_reconciliation
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
%s:%d: %s failed to fetch the extentref tree (error %d)\n
%@tgt_fsroot_depth=%llu 
Invalid arguments: [-S] requires [-V | -I] option
%s:%d: %s directory sizing aborted (dir: %lld)\n
apfs_lock_phys_range first_pbn 0, last_pbn 0x%llx\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%02hhx
btree_node_space_stats
sanity_check_alloced_blocks
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%@num_sh=%zu 
apfs_free_data_blocks
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
nx_tx_wait_flush
raw_xattr_remover
%s:%d: %s tx_leave failed with error: %d\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
size_tracking_untrack_inode
child_size_calculator_cb
%s:%d: %s unable to get spaceman free queue tree: %d\n
get_val_from_dict
%s:%d: %s failed to decrement crypto state = %llu, err %d\n
omap_destroy
authapfs_valid_hash_type
%s:%d: %s Invalid residency reason %d ino %llu\n
jfs_get_tree_in_snap
nlink
apfs_clonegroup_remove_dir_stats_key
fetch_file_info_header
RefCntUpd
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
Crypto cache num asserted crypto states (%u) surpassed the limit (%u)\n
%s:%d: %s Failed to set purgeable start time for ino %lld: error %d (%s)\n
nx_metadata_range_optimize
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
Cannot find inode record for inode %lld: %s(%d)\n
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
Z
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld (ret %d/%s)\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%@msu_purgble_clone_blk=%llu 
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s failed to enter tx, error %d\n
%s:%d: %s btree_node is null\n
%s:%d: %s get_cp_class_for_crypto_id failed (crypto id %llu, error %d)\n
%s:%d: %s Failed to update jobj %llu while removing xattr %s with error: %d\n
check_stale_doc_id_index
%s:%d: %s couldn't allocate memory for checkpoint map block\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s%s %s%s
bt_insert
%s:%d: %s failed to find host inode (id %llu) for purgeable rec lookup, falling back to ino %llu's atime\n
%s/apfs
%s:%d: %s failed to restore orig_fext, ino %llu, pbn 0x%llx, laddr 0x%llx, len %llu, crypto_id %llu, error %d\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
nx_tx_flush_busy
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: %s failed with err %d while getting the cow-exempt-file-count xattr on the root dir\n
remove_purgeable_record
%s:%d: %s Failed to release reference to crypto ID %lld for data stream %lld: %s(%d)\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
RR_HOLE
apfs_sealvolume
failed to allocate override hashes for dstream: %lld\n
btree_delete
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
%s:%d: %s error modifying omap: %d\n
browse
spaceman_chunk_zone_info_list_remove
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
authapfs_integrity_meta_create
btree_node_insert_internal
%s:%d: %s removing xattrs returned ENOENT for private-id %lld (ino %lld)\n
APFS_BTREE_NODES
%s%s %lld (under obj-id: %lld / crypto-id: %lld)%s
init_dir_stats_xfields
SnapName
    keys: %9d %9d %9d %9d %9d %9d\n
nchildren
move_inode_to_purgatory_ext
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
spaceman_check_allocation_status_internal
%s:%d: Cannot allocate %lld bytes for data buffer when processing data stream %lld\n
SiblingLink
%s:%d: Cannot get index of the volume %s\n
cst->ep_retain_count > 0
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s failed to dereference range (%llu + %llu) of extended attribute %llu: %s(%d)\n
update_dir_stats_key_on_ino_and_clone_mapping
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s%s%s%sCKI %d CG %d %lld:%d
Conflicting options: [-S] [-s]
 total read
%s:%d: Inode %lld is missing its resource fork\n
sha3_256_4k
%s:%d: %s Failed to remove purgeable record for ino %llu (parent id %llu, internal_flags %#llx) iteratively (err %d).\n
reference
%s%s%llx
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%@addcg_t=%llu 
subtype
%s:%d: %s failed to delete mapping, error: %d\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
%s:%d: %s container cleanly-unmounted flag set.\n
obj_cache_remove_new_fs_objects
obj_write_prepare
%s:%d: failed to move ino %lld from dir %lld to purgatory : %d\n
<UNKNOWN>
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s tree_iterator_next failed: %s\n
%s:%d: %s error finishing move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
fs_make_phys_range_writable
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
spaceman-lock
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: Cannot extract the expected hash from file %s: %s(%d)
preflight_tree
AppleAPFSVolume
%s:%d: %s failed to create snapshot: %d\n
 sibling-id
%s:%d: %s Volume has unsupported purgeable record type: %u\n
%s:%d: %s remove_purgatory_entry failed on %s for file-id %lld err %d\n
%@data_num_hardlnks=%llu 
 pad1
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: %s failed to write superblock to block 0: %d\n
%s:%d: %s omap snapshot tree sanity check failed: %d\n
** Sealing volume %ss%d: %llu hash records added
%s:%d 
%s:%d: %s obj_modify of (%llu) failed - %d\n
 offset
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
descendants:%llu phys-size:%llu resource-fork-size:%llu gen-count:%llu flags:0x%x chained-key:%llu
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%s:%d: %s xf_set error %d for type %u id %llu\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s failed to remove head_fext, ino %llu, laddr 0x%llx, error %d\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
%@encoded_len=%zu 
%s:%d: Cannot allocate %lld bytes for temporary buffer when processing extent %lld @ %lld of inode %lld\n
%s:%d: %s COW exempt file count underflow: %lld (delta %lld).  capping to zero.\n
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
apfs_clonegroup_remove_locked
%s:%d: %s Cannot initiate iterator for overallocated ranges: %s(%d)\n
DirRecord
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/fscommon/purging.c
%s:%d: %s apfs_update_phys_range for satisfiable range failed on 0x%llx+%llu, error %d\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
%s:%d: Database header not found\n
Expanded
%s:%d: %s failed to allocate temporary block memory\n
%s:%d: %s failed to set up spaceman for demo mode: %d\n
copy_kv_to_new_tree
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
Unknown xf value print format xf_type: %d\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
Skipping sibling link for inode with single link count (id: %lld)\n
ino_set_rage
e:
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
xid
 %d:%.*s
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
Found %u potential orphan dstream id records\n
apfs-rename-lock
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s failed to remove extents iteratively\n
%s:%d: %s error updating chained key for calculating dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
 unraw-size
marking
 %u:%.*s
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
%s:%d: %s Cannot initiate a walk of the filesystem tree: %s(%d)\n
level %d: %d nodes\n
total size
%s:%d: %s Failed to lookup purgeable record for removal (ino %llu): error %d\n
nx_checkpoint_find_valid_checkpoint
tinyobjcache
%s:%d: %s waiting for transaction to finish\n
%@data_ondisk_hardlnks=%llu 
%s:%d: Cannot create integrity object for volume %s: %s(%d)\n
 signing-id-hash
obj_checkpoint_known
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
file-id
btree_node_entry_update
  values: %9d %9d %9d %9d %9d %9d\n
exec
%s:%d: %s failed to remove tail_fext, ino %llu, laddr 0x%llx, error %d\n
%s:%d: %s Couldn't update other (group:%llu inum:%llu priv_id:%llu): %s\n
follow
unable to mount APFS volume @ %s [%ld]
Physical Interconnect Location
fs_destroy_shadow_fs_root_tree
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
%s:%d: %s Unexpected error searching (group:%llu priv_id:%llu): %s\n
%@tgt_fsroot_nodes=%llu 
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
descendants
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
%s/apfs_data
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
%s:%d: %s unable to get omap: %d\n
group-id: %llu, private-id: %llu, file-id: %llu
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
btree_node_copy
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
nx_metadata_range_add
%s:%d: %s unable to create snapshot tree: %d\n
%s:%d: %s ino %lld did not have a source-purge-id\n
Requested forced secondary_fs_root but the tree is missing\n
can not lock id zero\n
%s:%d: %s could not unwrap crypto-id %lld (err %d)\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s Cannot fetch next entry in the filesystem tree: %s(%d)\n
%s:%d: %s Would have attempted to create an entry with kind == NEW and refcnt == %d! (flags=0x%x, existing val len_and_kind=0x%llx owning_obj_id=%llu refcnt=%d)\n
%s:%d: %s Failed to update inode : xid %llu, ino %llu, error = %d\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
find_highest_precomputed_digest_id
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n
%s:%d: %s failed to finish writing to obj-id %lld (pos %lld / new_size %lld)\n
%@data_size_hardlnks=%llu 
%lld (under obj-id: %lld / crypto-id: %lld)
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
fd_dev_write_extended
%s:%d: %s ***: expanded type seen on in-memory obj\n
APFS_4K_OBJS
%@oc_miss=%llu 
%s:%d: %s dir-stats key %llu is busy even though we hold the inode lock\n
%s:%d: Cannot allocate mempry to track state of inode %lld with compressed flag set\n
%s:%d: %s btree_node_insert_internal failed: %d\n
%@roincompat=0x%llx 
com.apple.decmpfs
%s:%d: %s Hit %d looking up first snapshot\n
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
%@%s:%d 
num children
%s:%d: %s obj_modify failed - %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: %s trying to restore refcnt on dstream id %llu\n
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
update_hash_records_for_compressed_data
%s:%d: %s dir-stats %llu maintains purgeable rsrc size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n
invalid crypto id
tmp-ino-
spaceman_set_bits_in_bm
File Data Hash
Hashed %lld bytes of plain text data for data stream %lld\n
supplemental_tree_copy
%s:%d: %s failed to re-insert ext %lld:%lld for obj %lld (ret %d)\n
nx-resize-spaceman-lock
obj_destroy_complete
unknown option: %s
 embedded data size
failed to insert fsroot tree entry: %s(%d)\n
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s could not alloc %zd bytes @ pos %lld for obj-id %lld (err %d)\n
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
recursively_remove_extents_of_dir
%s:%d: Sealing volumes with fstree type: %u is not supported\n
get_dir_stats_by_key
doc_id_tree_destroy
%s:%d: %s failed to remove drec %lld:%s ino %lld ret %d\n
fs_remove_xattr_with_nstream_inode
 signing-id
\\r
%s:%d: %s BUG BUG BUG: ino %lld non-contiguous extents! prev_fext %lld:%lld (%lld) and orig_fext %lld:%lld (%lld)\n
%s:%d: %s Found corrupt record: %s\n
decrement-dstream-id-for-deletion
sha3_384_4k
spaceman_chunk_zone_info_cache_init
nx_tx_wait_closed_prev_flushing
exp_dir_stats_refcnt_merge
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
nx_unblock_physical_range
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
_omap_snapshot_create
spaceman_sanitize_datazones
%s:%d: %s error getting next checkpoint map block address %d: %d\n
%@tmp_cloned_blk=%llu 
(data: %llu, flags: 0x%x)
Skipping sibling id XF for directory entry %s (id: %lld) for inode with single link count (id: %lld)\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
obj_cache_remove_reverted_fs_objects
tx_flush
(data: %s, flags: 0x%x)
%s:%d: %s oid (%llu) failed to compute hash - %d\n
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
Invalid arguments: [-c] requires [-M] option
Time is more then 30 days in the future
%s:%d: %s did not find purgeable drec for dir %lld (parent id %lld) (fsize %lld)\n
clean_up_doc_id_trees_if_needed
Volume is already sealed - DANGER! This mode is not officially supported yet and can corrupt the volume.
%s:%d: %s failed got get next fsroot tree entry: %s(%d)\n
strictatime
 def-prot-class
%s:%d: %s is not an APFS volume\n
set_ino_purgeable_state
 %lld
refcnt:%u persistent-class:0x%x
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
%s:%d: Cannot create new fext tree for volume %s: %s(%d)\n
obj_cache_flush_write
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
%s:%d: %s Couldn't clone superblock, err %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
Set root tree oid to %lld and fext tree oid to %llu\n
%s:%d: %s Cannot create read stream for %s\n
H
%s:%d: %s cannot assert cst %llu for bg access because we have reached asserted cst threshold\n
invalid offset (%llu) for last fext lookup\n
SNAP_DELETE_TXN
APFS_INODES
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
empty 
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%@msu_shared_clone_blk=%llu 
%s:%d: Found incomplete inode records after update starting with inode %lld\n
FileExtent
%s:%d: %s oid (%llu) failed to get child %d - %d\n
no-name
delete_extentref_tree
%s:%d: %s error updating metadata ranges tree: %d\n
update_size_tracking_purgeable_size
obj_delete_and_free_by_oid
atime
supplemental_tree_get_descriptor
Device Characteristics
fs_tx_leave_ext
%s:%d: %s remapping xml is empty\n
%s:%d: %s Cannot parse remapping dictionary from %s: unknown error\n
%s:%d: %s rapid-aged %llu inodes\n
dst_paddr:%lld len:%lld
%s:%d: %s Couldn't remove extent at pbn %llu, err=%d\n
flags: 0x%x, phys-size: %llu
DirSize
authapfs_validate_node
%s:%d: %s doc-id tree creation failed: %d\n
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
perm
%s%s
New
hashed:%u hashsz:%u
%s:%d: %s Cannot update extent at offset %lld in inode %lld: %s(%d)\n
%s:%d: %s Skipping sibling link for inode with single link count (id: %lld)\n
(data: %#llx, flags: %#x)
%s:%d: %s dir-stats %llu maintains clone size but failed to get the xfield: %s (%d); size tracking may go out of sync\n
spaceman_fxc_update_smallest_with_successor
%s:%d: cannot get ino %llu ekwk %d\n
nx_checkpoint_traverse
protect
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: %s checking the generation count was specified but the generation count of ino %llu is zero.\n
lookup_purgeable_drec_as_record
ino-lock
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
jdev_fext_write_data
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
spaceman-czic-scan-lock
 compression type
\\u0017
%s:%d: %s unable to read cib %lld @ %lld: %d\n
obj_checkpoint_done
spaceman_alloc_iterate_chunks
ENCRYPTED 
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
MODIFICATION
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s Failed to create purgeable record (drec) for lookup (ino %llu): %d (%s)\n
%s:%d: Cannot overwrite an existing snapshot [%s]\n
Update
%s:%d: %s Error inserting cookie (group:%llu): %s\n
%@disk_free_curr=%llu 
%s:%d: Invalid expected root hash: %s (expected size: %d)\n
%s:%d: %s failed to extend existing extent %lld:%lld of inode %lld: %s(%d)\n
%s:%d: %s tx_enter_frozen() failed: %d\n
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
nx_check_superblock
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
nx_check_checkpoint_map_block
%@tmp_blk=%llu 
bt_remove_internal
com.apple.system.fs.speculative_telemetry
%s:%d: %s couldn't insert record err:%s\n
btree_check_ext returned non-zero: %d\n
decrement_dstream_id_for_deletion
apfs_mount
%s:%d: %s Couldn't get active extentref tree, err=%d\n
legacy_get_ek
%s:%d: %s fs_update_snap_metadata() returned %d\n
%s:%d: %s unable to get fs snap meta tree: %d\n
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s superblock failed sanity checks: %d\n
apfs_remap_records_fsroot
%s:%d: %s Cannot find inode record for inode %lld in sibling map record %lld: %s(%d)\n
\\t
com.apple.fs.symlink
Skipped %u orphan dstream id records\n
usage: %s [options] <volume_path>\n
%s:%d: %s Cannot remove purgeable record with zero atime (ino %llu).\n
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
spaceman_decrement_free_queue_count
Invalid
%s:%d: %s unsupported tree type, %d\n
%s:%d: %s Volume inconsistency detected by %s:%u!\n
nx_dev_init
%s:%d: %s error unreserving space, %lld blocks: %d\n
obj_cache_remove
obj_read
tx_mgr_free_tx
%s:%d: %s failed to set dir-stats key %llu on ino %llu: %s (%d)\n
%s:%d: %s set cloneinfo_id_epoch to %llu\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
kind == NEW && refcnt = %d\n
L
\\u0005
clear_invalid_fixups
%s:%d: %s omap xid %lld > spaceman xid %lld\n
 rdev
%ss%d
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
obj_release
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
asv_empty_purgatory
%s:%d: %s Failed to insert drec associated with purgatory_dir and ino %llu, error = %d\n
%s%s %llu%s
clear
sha3_384
  %4d: k:%5d:%-4d  v:%5d:%-4d  key:[[ %s ]]  child:%s hash:%s\n
prevent_synthetic_object_operation
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s%s %lld%s
%s:%d: %s Failed filesystem tree preflight checks: %s(%d)\n
fs_make_hole_range_writable
%s:%d: %s Cannot mark space for %zu bytes at offset %lld in dstream %lld of inode %lld as writable: %s(%d)\n
nx-txn-blocks-lock
 DELETED
groupquota
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: Sparse bytes removed from inode %lld that didn't have an extended field.\n
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
file-id: %lld
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
nx_metadata_fragmented_sanity_check
obj_checkpoint_get
%@msg='%s' 
\\u001f
%s:%d: failed to load ekwk for ino %llu, id %llu, class %d, decode error\n
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
%s:%d: %s spaceman chunk count is bad: %lld\n
virtual
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: %s omap_destroy returned %d!\n
!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))
%s:%d: %s Cannot restore unwritten status of extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
  flags
computing root hash for block size: %u\n
%s:%d: %s ino %llu is flagged to maintain dir-stats but has no dir-stats key\n
%s:%d: Unexpected AppleFSCompression extended attribute record for inode %lld\n
<BAD-KEY-LEN>
%s/nx
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
%s:%d: %s failed to allocate temporary inode buffer\n
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
apfs_clonegroup_insert_cookie
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
%s%s %d/%d/0o%o%s
%s:%d: %s expanded record found on unsupported volume\n
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
lookup_purgeable_drec
%s:%d: %s Failed to remove purgeable record (drec): %d (%s)\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
Successfully validated hash %s\n
%s:%d: %s failed to get fsroot tree of fs %llu, %s(%d)\n
R
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld\n
%s:%d: %s ino %lld no extent covering dstream alloced_size %lld (fsize %lld) pos/len %lld:%lld\n
spaceman_unreserve
apfs_create_doc_id_tree_if_needed
btree_node_insert
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
%s:%d: %s bad clonegroup_cookie_key_t, klen:%u vlen:%u group_id:%llu\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
Making a snapshot [%s]:%s tagging as root\n
%s:%d: %s failed to seal integrity_tree of fs %llu, %s(%d)\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
\\u0011
obj_cache_remove_graft_persistent_ephemeral
ACCESS
%s:%d: %s Creating key for lookup failed\n
apfs-dir-size-lock
%s:%d: %s Cannot insert purgeable record with zero atime (ino %llu).\n
%s:%d: %s omap check failed with error: %d\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
%s:%d: %s Cannot find inode record for inode %lld: %s(%d)\n
%s:%d: %s fs %llu is not formatted for sealing!\n
\\u001b
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
,
fsroot_tree_iterator
icp_new_crypto
obj_checkpoint_check_for_unknown
nx_tx_wait_frozen
%s:%d: Cannot get the fext tree of volume %s: %s(%d)\n
fs_insert_fext_record
nx_reaper_wait
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%zd
%s:%d: %s Cannot create a inode record for inode %lld - out of memory\n
%s:%d: %s Failed to create contiguous fsroot tree: (%llu + %llu) != %llu\n
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
 default-crypto-id
spaceman_fxc_print_stats
<60
%s:%d: %s spaceman free count is too large: %lld > %lld\n
tx_checkpoint_write
%s%s %-11s%s
dev_init
%s:%d: %s set apfs_fixup_flags to %#llx\n
match_jobj_expanded_type_to_tree_type
%s:%d: %s unable to get fs root tree: %d\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s Couldn't lookup_ge (group:%llu inum:0 priv_id:0): %s\n
%@purge_full_2=%llu 
%s%s %#llx%s
kind:%d
insert_phys_extent
nx-global-extent-manipulation-lock
%s:%d: %s Did not find date-added/change/birth/mod/access time in the xml dictionary, remapper will perform no modifications\n
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
%s:%d: %s Failed to remove purgatory_dir drec from fs_root tree: xid %llu, drec %llu, error = %d\n
%s:%d: %s key @ %p key.hdr.obj_id %lld val @ %p val.kind %d refcnt %d owning_obj_id 0x%llx\n
spaceman_ip_freed
%s:%d: %s failed to look up dir-stats %llu for origin inode %llu: %s (%d)\n
%s:%d: %s not enough space to enter transaction\n
%s:%d: %s invalid reap_id (%llu), must be smaller than nr_next_reap_id (%llu)\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
 purgeable-flags
apfs-snapmeta-oid-lock
btree_node_check
\\u0015
%s:%d: %s failed to fetch the fext tree (error %d)\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s object cache bootstrap failed: %d\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
\\u001d
parent:%lld private:%lld flags:0x%llx mode:%o uid/gid:%d/%d bsdflags:0x%x %s:%d cr8:mod:chg:acc %lld:%lld:%lld:%lld
%s:%d: %s Inserting snap_meta failed, %d\n
%s:%d: %s failed to find uncompressed size for indoe %llu\n
\\u001e
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
Dead
%s:%d: %s failed to enter transaction to clear purgatory dir nchildren %s(%d)
fs_get_inode_with_hint
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
%s:%d: %s error adding snapshot: %d\n
DirStats
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
clone size
%s:%d: using 16k root hash\n
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s Failed to find purgeable record (ino %llu) for flags merging: %d\n
fs_is_content_protected(apfs)
APFS_TREE_LOOKUP_ZONE
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
%lld/%lld/%lld/%lld
%s:%d: %s stopped purgatory dir cleanup after %d loops\n
<BAD-CLONEGROUP-KEY-LEN>
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
%s:%d: %s cannot insert file extent record for extent of %lld bytes at offset %lld of data stream %lld in transaction %lld: %s(%d)\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s failed to look up shadow dir-stats %llu: %s (%d)\n
gbitmap_reap
jobj_merge_maybe_clamp_64
%s:%d: %s couldn't allocate memory for superblock of size %d\n
spaceman_iterate_free_extents_internal
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
%s:%d: %s doc-id tree sanity check failed: %d\n
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: Unsupported configuration - detected sparse region in data stream %lld between %lld and %lld\n
failed to create fsroot tree: %s(%d)\n
%s:%d: %s %s flags 0x%x for clone mapping <%llu, %llu> failed: %s (%d)\n
com.apple.FinderInfo
 info:%u %lld
%@num_files=%zu 
asv_process_decmpfs_xattr
_fd_dev_write
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
runtime_retains()
%s:%d: %s spaceman IP base address is bad: %lld\n
apfs_clonegroup_update_dir_stats_key
jdump file not specified [-D], skipping extended jdump
%s:%d: Cannot get to the parent of %s\n
doc_id_tree_create
sealed, fext, req_tree != fs_root
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: %s Unknown flags being used on purgeable record: %x. Truncating...\n
insert_purgeable_record
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
obj_alloc
 clonegroup-id
apfs-flags-lock
%s:%d: %s Unsupported flags being used on purgeable drec: %llx. Truncating...\n
fd_dev_read_helper
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s reaper has tail with no head\n
w
Conflicting options: [-V] [-I]
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s extended attribute %llu has an unexpected compression type: %u\n
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
crypto_hash_insert
ino->rsrc_ekwk == cur_ekwk
object-lock
SAVED 
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
Get count overflowed for object %p!\n
%s:%d: unlocking id %llu, which is not locked\n
%s:%d: %s decrement dstream id returned ENOENT for private-id %lld (ino %lld)\n
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
unknown hash type: %s, (supported: sha256, sha512_256, sha384, sha512, sha3_256, sha3_384, sha3_512, sha3_256_4k, sha3_384_4k, sha3_512_4k)
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
%@src_fsroot_nodes=%llu 
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
apfs_mount_livefs
setup_demo_mode
%s:%d: %s spaceman cibs per cab is bad: %d\n
spaceman_cab_sanity_check
%s:%d: Database header has wrong version/size: expected %u/%zu, got %u/%zu\n
flags:%u total-count:%llu physical-size:%llu full-clone-size:%llu
current tx not closed/flushing?!\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
btree_iterate_nodes
AppleAPFSContainerScheme
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
%s:%d: %s container block size too small for device block size (%d < %d)\n
invalid crypto index %d\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
%s%s %9s : %s
authapfs_seal_break
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
bt_lookup_copy_out
id:%lld %s %s
jobj_to_large_key_val
%@num_sc=%zu 
compressed 
\\\\
%s:%d: %s Unknown purgeable record type (%hhu)\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
NOHEAD 
%s:%d: using 8k root hash\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
btree_check_recent_sanity
crypto_cache->type != CRYPTO_OBJ_TYPE_EP
remove_purgatory_entry
dir-stats
unexpected storagetype: 0x%x\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
io_get_num_device_blocks
NONAME
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
%s:%d: %s Error: tx[%lld] failed to start: %d\n
 data-len
asv_mount_container
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
%s:%d: %s Failed to update extended fields when %s WANTS_TO_BE_PURGEABLE on ino %llu: %d (%s)\n
obj_cache_graft_attach
Found %lld overallocated data streams, maximum number of actively tracked uncompressed data streams with overallocations was %lld\n
%s%s %4d :: %s
Unknown type %d
%s:%d: cannot get on-disk ekwk %llu, %d\n
spaceman-free-lock
%s:%d: Cannot get the filesystem tree of volume %s: %s(%d)\n
insert_prev_inode
refcnt
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
Cannot parse timestamp '%s' using format \"%s\"\n
%@max_mem=%llu 
sib-id
%s:%d: Cannot decompress chunk at offset %lld in data stream %lld: %s(%d)\n
%s:%d: %s Couldn't insert snapshot metadata, err %d\n
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
Reference count underflowed for object %p!\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
_remove_purgeable_record_cb
IOMedia
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
%@num_cg=%zu 
unmark
%s:%d: %s failed to clear purgatory dir nchildren %s(%d)
%s:%d: Duplicate entry for inode %lld\n
 (%s%s %lld;%s
 strict-class-f
%s:%d: %s ino %llu is being moved but we don't know how to account for it (from_dir %llu/%llu, to_dir %llu/%llu); size tracking may go out of sync\n
Xattr
%s:%d: %s btree_get_extended failed - %d\n
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
nx_tx_wait_closing
    keys: %9s %9s %9s %9s %9s %9s\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
obj_checksum_verify
failed to find override hash for %lld: %s(%d)\n
%s:%d: %s failed to remove dir-stats object (id %llu): %s (%d)\n
%s:%d: %s failed to get integrity_meta of fs %llu, %s(%d)\n
%s:%d: %s failed to remove first, error %d\n
%s:%d: %s error %d removing purgatory entry %lld/%s for ino %lld\n
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
obj_init
 flags
Found orphan fext record (offset:%lld, id: %lld), skipping...\n
%s:%d: Cannot mount container on %s - %s(%d)\n
%s:%d: unexpected payload type length : %d\n
apfs-im-cache-lock
id %llu not in crypto cache
io_get_device_features
%s:%d: %s prev doc-id tree sanity check failed: %d\n
%s:%d: %s error updating chained key for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
!apfs->apfs_readonly
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
%s:%d: %s Bad blob in (group:%llu inum:%llu priv_id:%llu): %s\n
%s:%d: Cannot fetch database header: %s (%d)\n
%s:%d: Cannot insert range to deallocate (%lld+%lld) at offset %lld in data stream %lld - %s(%d)\n
btree_node_child_id_update
omap_find_next_snapshot_xid
Any
get_dstream_id_refcnt
!ino_is_class_v(apfs, ino)
%s:%d: %s Couldn't rename snap %llx to %s\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
tx_unmount
%s:%d: %s iterate_jobjs failed with error %d\n
jobj_validate_key_val
%s:%d: %s failed to fetch the integrity object (error %d)\n
ino_has_vnode(ino)
ino_get_ekwk_uncached
ino_get_ekwk_id
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
apfs-global-snap-lock
rdonly
spaceman_chunk_zone_info_recent_increment
BSD Minor
apfs_clonegroup_update_locked
update_size_tracking_no_gencount_bump
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
flags 0x%x%s%s oid %lld
%s:%d: Unexpected sparse extent at the offset %lld in the data stream %lld\n
asv_save_compressed_inode_num
flags
com.apple.ResourceFork
%s:%d: graft with invalid fs block size: %u\n
spaceman_clear_bits_in_bm
clone_mapping_remove_locked
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
fs_insert_snapshot_metadata
%@time=%ld 
total written
%s:%d: %s Cannot read %lld bytes at physical block %lld which corresponds to offset %lld of data stream %lld: %s(%d)\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%@src_fsroot_depth=%llu 
%s:%d: %s failed to set dir stats key for <%llu, %llu> clone mapping, error %d\n
%s:%d: %s Purgeable start time (%llu) is unsupported on purgeable drecs.\n
%s:%d: failed to open container device %s: %s\n
orig-file-id: %lld
%@mnt_t=%llu 
asv_process_rsrc_xattr
%s:%d: %s obj_create failed - %d\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
blocks_in_txn
nx_reaper_obj_get
%s:%d: %s Failed to set purgeable rec's dir gen-count: error %d\n
%s:%d: %s Failed to remove purgeable record (record): %d (%s)\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
spaceman-ip-lock
Could not allocate memory
 decmpfs magic
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
%s:%d: %s tx xid %lld took %lld us to flush\n
%s:%d: %s ino %llu is flagged as dir-stats origin but has no dir-stats key\n
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
nx_tx_wait_closed
%@xp_desc=%lld 
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s failed to %s dir-stats %llu as purgeable: %s (%d)\n
len:%lld owning_obj_id:%lld refcnt: %d
%s:%d: unknown expanded type (%hhu) on record (%u)\n
nx_reaper_next_record
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
omap_sanity_check
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
populate_time_from_dict
%s:%d: %s Failed to remove existing purgeable record (ino %llu): %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
 saf-dstats-key
computed hash for block size %u is: %s\n
%s:%d: %s Failed to insert purgeable record (drec): %d (%s)\n
```
