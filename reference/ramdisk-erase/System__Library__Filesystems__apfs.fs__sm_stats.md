# `/System/Library/Filesystems/apfs.fs/sm_stats`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 415,776 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2000)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
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

## Strings (1,054)

```
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s unable to get spaceman: %d\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
%s:%d: %s omap xid %lld > spaceman xid %lld\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s tx_leave failed with error: %d\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
new address mismatch on redirty 0x%llx 0x%llx\n
%s:%d: %s error updating metadata ranges tree: %d\n
apfs-fext-tree-oid-lock
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
spaceman_chunk_zone_info_compare
nx_reaper_add_sub_object
Physical Interconnect Location
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: %s *** trim'ing free blocks returned: %d\n
spaceman_free
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s *** unknown expanded obj type %hhu\n
APFS_BTREE_NODES
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
<%d
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
nx_checkpoint_find_highest_xid
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: %s Tree delete oid %llu threw %d\n
obj_write_prepare
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
tx_unmount
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s unable to get fs snap meta tree: %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
apfs_sanity_check_tree_type
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
spaceman_ip_bm_block_alloc
apfs-pfkur-tree-oid-lock
apfs-global-lock
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
loadtmpcp
spaceman_trim_free_blocks
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: graft with invalid fs block size: %u\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
IOMedia
AppleAPFSVolume
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
groupquota
spaceman_chunk_zone_info_recent_increment
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
obj_cache_remove
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
Internal
%s:%d: %s tree_delete() failed: %d\n
live
bt_merge_nodes
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s free fragments length distribution\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s object cache bootstrap failed: %d\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
object-lock
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
<80
AppleAPFSSnapshot
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
spaceman_ip_bm_block_free
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
obj_get_async_read
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
spaceman-czic-lock
Attempting to reuse a non-candidate chunk zone info\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
%s:%d: %s xid %lld second sync/barrier failed: %d\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
smChunkIndexForDataZone
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
omap_destroy
%s:%d: %s First sync/barrier failed: %d\n
smChunksFull
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
btree_check_recent_sanity
nx_superblock_agrees_with_container_superblock
union
nx-volume_group-lock
smChunkFullnessFragDist
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
authapfs_integrity_meta_get_internal
IOService
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
Error %d failed to mount device %s
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
obj_release
obj_modify
nx-tree-node-compact-lock
<UNKNOWN>
level %d: %d nodes\n
  values: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
%s:%d: %s omap tree type 0x%x is bad\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
createtmpcp
btree rightmost leaf mismatch! (expected %lld found %lld)\n
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
%s/apfs
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
fd_dev_read_helper
jobj_validate_key_val
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
%s:%d: %s failed to find valid checkpoint: %d\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
committmpcp
%s:%d: %s Hit %d looking up first snapshot\n
bt_insert
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
apfs-snapmeta-oid-lock
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
btree_node_space_stats
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
suid
spaceman_fq_tree_insert
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: can't get features for device (%s)\n
spaceman_sanitize_datazones
spaceman_free_extent_cache_reset
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s container cleanly-unmounted flag set.\n
spaceman-czic-scan-lock
%s:%d: %s Final sync/barrier failed: %d\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
obj_checkpoint_known
%s:%d: %s tx xid %lld took %lld us to flush\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
%s:%d: %s unable to get fs extentref tree: %d\n
%s:%d: %s omap snapshot tree type 0x%x is bad\n
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
btree_node_key_range_validate
obj_cache_flush_prepare
%s:%d: %s Trash unfinished tx xid=0x%llx\n
verbose
btree_node_free_list_entry_validate
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
dev
%s:%d: can't get block count (%s)\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
apfs-incompat-features-lock
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
physical object dirty count underflow\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
%s=
authapfs_validate_node
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
jobj_release
%s:%d: %s container block size too small for device block size (%d < %d)\n
apfs-omap-lock
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s tx xid %lld took %lld us to close\n
nx_reaper_checkpoint_traverse
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
btree_node_entry_update
%s:%d: %s failed to get newnode minkey: %d\n
supplemental_tree_destroy
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
spaceman_get_metazone_alloc_index
apfs-doc-id-lock
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
tx_flush
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
dev_init
obj_checkpoint_done
spaceman_fq_tree_find_overlap
%s:%d: failed to open volume device %s: %s\n
Removable
nx_check
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
Cannot open output file
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
btree_node_reap
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s couldn't allocate memory for checkpoint map block\n
skipsanity
spaceman_fxc_tree_node_recycle_smallest
Chunk free fragments count distribution
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
supplemental_tree_get_descriptor
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
obj_delete_internal
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s failed to create reap list: %d\n
AppleAPFSMedia
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
owners
reserved metadata space underflow: %lld (%lld)\n
%ss%d
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s error getting mapping tree: %d\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
%s:%d: %s failed to get reap list head: %d\n
%s:%d: %s cib %lld chunk info count %d should be %lld\n
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
spaceman_fxc_print_stats
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
sealed, fext, req_tree != fs_root
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s invalid object size: %d size_phys %d\n
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
tx_leave
%s:%d: wrlock == 0 failed %d\n
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
apfs-stream-id-lock
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
key_val_to_jobj
%s:%d: %s unable to get snapshot tree: %d\n
DataZone ID %u history idx %llu frags %llu\n
spaceman_ip_block_alloc
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
perm
%s:%d: %s Error: tx[%lld] failed to start: %d\n
paddr
%s:%d: %s btree_node is null\n
apfs_free_data_blocks
%s:%d: %s omap check failed with error: %d\n
%s:%d: %s omap_destroy returned %d!\n
mount_apfs
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: %s error getting cab %d @ %lld: %d\n
apfs-clonegroup-lock-mutex
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
%s:%d: %s unable to get omap tree: %d\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
%s:%d: %s superblock failed sanity checks: %d\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
btree_node_child_id_update
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
not handling the current tx!\n
exec
%s:%d: %s unable to create chunk zone info cache lock: %d\n
MetaZone
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
nx_tx_wait_closed_prev_flushing
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
obj_mem_mgr_init
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
%s:%d: %s cab %d cib count %d should be %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
nx-global-extent-manipulation-lock
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
atime
Target Disk Mode
AppleAPFSContainer
%s:%d: device initialization failed: %d\n
protect
nx-omap-lock
%s:%d: %s doc-id tree sanity check failed: %d\n
%s:%d: %s object cache initialization failed: %d\n
obj_checkpoint_start
%s:%d: %s waiting for transaction to finish\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
apfs-global-snap-lock
fd_dev_read_extended
jobj_size_for_key_val
fullness %% |
apfs_checkpoint_traverse
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
Reference count overflowed for object %p!\n
spaceman_chunk_zone_info_list_remove
spaceman_unreserve
%s:%d: %s reap list object free list erroneously empty?\n
spaceman-dev-lock
<20
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s snap meta tree %lld: %d\n
apfs-dir-size-lock
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
Device Characteristics
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
match_jobj_expanded_type_to_tree_type
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s Invalid reap list free entry %d\n
spaceman_cib_sanity_check
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
authapfs_validate_node_hash
%s:%d: %s lookup_next_snapshot() returned %d\n
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
tx_checkpoint_space_check
[%3u, %3u) |
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
btree_node_insert
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
smFragCountMetaZoneDist
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s chunk %lld recent zone count overflow\n
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
apfs_reap_snapshots
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
empty chunks: %llu\n
apfs-im-cache-lock
btree_iterate_nodes
FULL
obj_destroy_complete
nx_metadata_range_optimize
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: %s spaceman chunk count is bad: %lld\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
APFS_TREE_LOOKUP_ZONE
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
omap_sanity_check
%s:%d: %s error modifying omap: %d\n
%ss%d:%lld
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
AppleAPFSContainerScheme
nx_corruption_detected_int
%s:%d: %s prev doc-id tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
IOMatchCategory
%s:%d: object memory manager failed to create lock, error: %d\n
auto
<40
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
rolling-stats-lock
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
make_large_jkey_header_from_jobj
%s=%llu\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
%s:%d: %s tx_finish() failed, %d\n
nx_metadata_fragmented_sanity_check
apfs-snap-delete-lock
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
spaceman_fxtp_add_child
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
length
%s:%d: %s found mapping tree with old subtype\n
:%llu
apfs-flags-lock
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
=%d
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s omap snapshot tree sanity check failed: %d\n
nx_reaper
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
%s:%d: %s chunk %lld recent zone count underflow\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: %s unable to get spaceman free queue tree: %d\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
obj_read
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
object-cache-flush-lock
%s:%d: %s Error %d, reinitializing\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
obj_alloc
spaceman_clear_bits_in_bm
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
[%3u, %3s) |
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
nx_tx_wait_frozen
tx_finish
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
lookup_jobj_ext
%s:%d: %s ***: expanded obj type found on unsupported volume\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d: %s bogus phase, %u\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: %s obj_modify() failed: %d\n
smFragSizeDist
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s spaceman chunks per cib is bad: %d\n
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
rw
%10llu,
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
level %d: %d nodes %.2f average descendents\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
spaceman-fxc-lock
%s:%d: %s failed to delete mapping, error: %d\n
%llu
DataZones highest frag count recent chunks
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: %s failed to fix up checkpoint data: %d\n
spaceman-space-usage-lock
smFragCountDist
fd_dev_write_extended
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s extentref tree %lld: %d\n
obj_checkpoint_check_for_unknown
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
APFS_INODES
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
nx_check_omap
obj_cache_remove_reverted_fs_objects
spaceman_allocation_init
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
userquota
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
smChunksEmpty
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
%s:%d: %s failed nx_check sanity: %d\n
       -l --live: container is live
spaceman_check_allocation_status_internal
apfs-rename-lock
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
jobj_allocate
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
Failed to collect spaceman stats %d
spaceman-free-lock
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
io_get_device_features
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
nx_check_recent_sanity_omap
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
APFS_4K_OBJS
%s:%d: %s spaceman free count is too large: %lld > %lld\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%5llu <= len    %5s | %8llu frags | %10.02f MiB \n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
       -o --outfile: file path
%s:%d: %s unable to get fs object 0x%llx: %d\n
spaceman_decrement_free_queue_count
btree_node_sanity_check
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
obj-mem-mgr-lock
spaceman_free_extent_cache_setup
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
tx_checkpoint_write
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: %s cab %d index %d should be %d\n
omap_recent_sanity_callback
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
%s:%d: %s reverting on error: %d\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
jobj_size_for_large_key_val
%s:%d: %s unable to get doc-id tree: %d\n
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
object-cache-reset-lock
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
usage: spacemanstats [ options ] [ <device_path> ]
%s:%d: %s unsupported tree type: %d\n
%s:%d: %s spaceman blocks per chunk is bad: %d\n
omap_reap
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
unexpected storagetype: 0x%x\n
spaceman_upgrade_sm_version_0_to_1
nx_tx_finish_wait
bt_remove_internal
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
invalid crypto index %d\n
%s:%d: %s failed to initialize free extent cache, error %d\n
outfile
%s:%d: %s unable to get snap meta tree %lld: %d\n
       -h --help
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
obj_cache_graft_attach
       -q --quiet
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
image-format-read-only
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
object-cache-lock
omap_cleanup
%s:%d: %s failed to set up spaceman for demo mode: %d\n
omap_find_next_snapshot_xid
spaceman_cab_sanity_check
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
tx_enter_internal
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
spaceman_modify_bits
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
nx_mount
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
tx-mgr-lock
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
<60
nx_check_superblock
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
tinyobjcache
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
BSD Minor
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
obj_checkpoint_get
%5llu <= len  < %5llu | %8llu frags | %10.02f MiB \n
gbitmap_reap
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
nx_tx_finish_wait_for_dirty_data
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
spaceman-lock
btree_node_child_val
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
%s:%d: %s unable to get fs root tree: %d\n
\t%16p %s\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
nx_check_reaper
spaceman_free_extent_cache_insert
nx_reaper_next_record
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
nx_tx_wait_closing
%s:%d: reaper thread is exiting, returning EBUSY\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
 
%s:%d: %s spaceman cab count is bad: %d\n
%s:%d: %s error updating snapshot tree: %d\n
ro
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: %s cib %lld index %d should be %lld\n
%s:%d: %s tx manager initialization failed: %d\n
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
spaceman_fxc_update_length
nx_reap_list_sanity_check
smChunkFragsForDataZone
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
%s:%d: %s failed to get omap tree for reaping: %d\n
automounted
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
spaceman_ip_freed
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
obj_checksum_verify
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
authapfs_valid_hash_type
%s:%d: *** Unknown file info type %llu\n
invalid tweak type %d\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
apfs_reap_extentref_blocks
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
not handling the flushing tx!\n
nx_reaper_obj_get
btree_node_check
apfs-phys-lock-state-mutex
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
nx_tx_wait_open
%s:%d: %s Failed to get next extent: %d\n
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
nx_tx_flush_busy
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
nx_checkpoint_load_data
object-cache-list-lock
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: unlock == 0 failed %d\n
spaceman_set_bits_in_bm
%s:%d: Invalid or unknown hash type: %d\n
btree_node_debug_stats
fd_dev_close
%s:%d: %s unable to get omap: %d\n
%s:%d: %s omap snapshot count %d seems excessive\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
nx_reaper_add_ext
nx_unblock_physical_range
_fd_dev_write
obj_cache_flush_write
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
FIXUP
smFragSizeMetaZoneDist
apfs-integrity-meta-lock
bt_shift_or_split
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
bt_update_last_leaf
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
demomode
spaceman_sanity_check
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%02hhx
capacity: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
,
%s:%d: %s waiting for available tx to open: xid %lld\n
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
obj_cache_remove_graft_persistent_ephemeral
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
<100
io_get_num_device_blocks
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: %s unable to allocate chunk zone info cache\n
spaceman_alloc
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
spaceman_fxc_update_smallest_with_successor
%s:%d: %s failed to get object oid %lld: %d\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
Reference count underflowed for object %p!\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: Container corruption detected by %s:%u!\n
browse
invalid lock flags: 0x%x\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
spaceman_chunk_zone_info_recent_decrement
hlo:qv
/dev/
nx_check_recent_sanity
%s:%d: %s btree check called with non-root btree node: %d\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
apfs-dir-stats-id-lock
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: %s failed to write superblock to block 0: %d\n
       -v --verbose
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
nx_get_evict_mapping_tree
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
%5llu == len    %5s | %8llu frags | %10.02f MiB \n
%10u,
jobj_validate_large_key_val
obj_checksum_verify_phys
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
spaceman_free_fs_deduct_block_counts
%s:%d: %s iter_next returned %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: *** Can't allocate unknown obj type %d\n
%s:%d: %s omap tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
spaceman_free_completed
io_get_device_block_size
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
Get count overflowed for object %p!\n
invalid unlock flags: 0x%x\n
btree_delete
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
BSD Major
nx_check_checkpoint_map_block
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
defwrite
nx_tx_wait
START
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
rdonly
spaceman_checkpoint_traverse
%s:%d: %s Tree iteration threw %d at cursor %llu\n
IOBlockStorageDevice
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
obj_create_internal
checkpoint
full chunks:  %llu\n
%s:%d: %s Fusion is not supported anymore\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
obj_delete_and_free_by_oid
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: *** unknown obj type %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: %s error searching snapshot tree: %d\n
nx_tx_wait_flush
btree_node_insert_internal
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s couldn't read superblock of size %d\n
%s:%d: %s error deleting empty snapshot tree: %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
%s:%d: %s unable to get prev doc-id tree: %d\n
virtual object dirty count underflow\n
capacity: leaves %llu / %llu => %.2f %% used\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
nx-resize-spaceman-lock
apfs_sanity_check
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: %s failed to attach graft to object cache: %d\n
nx_mount_initiate_free_space_trims
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
nx_tx_wait_closed
%s:%d: spaceman_stats took too more than %u seconds, aborting!\n
%s/apfs_data
%s:%d: failed to open container device %s: %s\n
large_key_val_to_jobj
Release count overflowed for object %p!\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
nx-txn-blocks-lock
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
spaceman_metazone_init
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
%s:%d: %s failed to get reap list tail: %d\n
dev_init_common
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
apfs_reap
%s/nx
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
ephemeral
virtual
Total
apfs-phys-ext-oid-lock
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
    keys: %9d %9d %9d %9d %9d %9d\n
APFS_8K_OBJS
nx_checkpoint_find_valid_checkpoint
Allocated %s object with OID %lld flags %llx type %x %d from\n
btree_check_ext
jfs_get_tree_in_snap
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s object type 0x%x not reapable?: %d\n
spaceman_trim_free_extent_callback
bt_lookup_copy_out
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
w
%s:%d: %s spaceman IP base address is bad: %lld\n
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s Can't get tree: %d\n
quarantine
%s:%d: %s bt_shift_or_split failed with error: %d\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
nx_metadata_range_add
spaceman_alloc_fxc_scan_wait
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
follow
make_jkey_from_jobj
tx_mgr_free_tx
type = %u, req_tree != fs_root\n
obj_init
nx_reaper_sanity_check
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
nx_dev_init
nx_checkpoint_traverse
%s:%d: %s removal of replaced free extent failed: %d\n
spaceman_alloc_iterate_chunks
%s:%d: %s failed to write checkpoint map block %lld: %d\n
spaceman_free_extent_cache_remove
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
spaceman_chunk_zone_info_cache_init
spaceman_set_up_ip_reverse_mapping_tree
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s reaper has tail with no head\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
current tx not closed/flushing?!\n
spaceman_free_extent_cache_search
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
help
spaceman_chunk_zone_info_add
spaceman_iterate_free_extents_internal
spaceman_freed
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
spaceman_fs_bounds_clear
btree_node_val_range_validate
quiet
spaceman-ip-lock
obj_cache_remove_new_fs_objects
%s:%d: %s xid %lld sync/barrier failed: %d\n
bt_merge_up
%s:%d: %s object type 0x%x not reapable: %d\n
spaceman_stats_free_extent_cb
Protocol Characteristics
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s failed to write superblock to block %lld: %d\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
btree_node_compact
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
```
