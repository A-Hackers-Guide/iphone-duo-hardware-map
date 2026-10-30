# `/System/Library/Filesystems/apfs.fs/newfs_apfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 508,592 bytes.

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
	<key>com.apple.apfs.expandedrecords</key>
	<true/>
	<key>com.apple.private.apfs.xart</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.system-async-io</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleAPFSUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (1,321)

```
%s:%d: %s Enabling temporary checkpoints starting with xid %lld.\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
61706673-7575-6964-0040-766f6c756d00
%s:%d: %s omap checkpoint %s traverse failed: %d\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s chunk %lld recent zone count underflow\n
rolling-stats-lock
%s:%d: wrlock == 0 failed %d\n
uid=%s
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s Encrypted volume is not allowed with special role = 0X%x\n
paddr
%s:%d: %s sanity checking all container state... please be patient.\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
duplicate_jobj_op_to_shadow_fs_root
apfs_sanity_check
obj_modify
sha512
%s:%d: %s ino %llu is flagged to maintain dir-stats but has no dir-stats key\n
%s:%d: %s cib %lld chunk info %d xid %lld > cib xid %lld\n
%s:%d: reaper thread is exiting, returning EBUSY\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s omap entry %lld:%lld beyond deletion entry @ xid %lld\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%s:%d: %s fs snap meta tree sanity check failed: %d\n
%s:%d: %s trim distribution 1:%lld 2+:%lld 4+:%lld 16+:%lld 64+:%lld 256+:%lld\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s spaceman IP free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s unable to read cab %d @ %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
APFS_TREE_LOOKUP_ZONE
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s %s: could not remove dir rec for obj-id %lld (name: %s)\n
%s:%d: %s allocated unwritten file extents are now supported\n
%s:%d: %s unable to get omap %lld: %d\n
nx_checkpoint_traverse
%s:%d: %s clonegroups enabled for this volume\n
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
BSD Major
%s:%d: %s initializing cache w/hash_size %u and cache size %u\n
%s:%d: %s nx_unblock_physical_range failed with error: %d\n
%s:%d: %s invalid object size: %d size_phys %d\n
<60
nx_reaper_obj_get
%s:%d: error: device is not writable!\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
spaceman_allocated
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
nx_check_superblock
obj_delete_and_free_by_oid
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
%s%llu.%.*s %cB%s
object-cache-reset-lock
obj_cache_flush_write
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
dev_init
supplemental_tree_destroy
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
jobj_merge_maybe_clamp_64
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
%s:%d: %s omap tree entries out of order: oid %lld < %lld\n
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
%s:%d: %s object type 0x%x not reapable?: %d\n
physical size
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s chunk %lld recent zone count overflow\n
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
-c requires -x as well
nx_reaper_wait
%s:%d: %s tx_enter() failed: %d\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
nx_format
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
%s:%d: can't get block count (%s)\n
%s:%d: %s skipping check of fs[%d] oid %lld fs root tree because it's encrypted\n
%s:%d: %s prev doc-id tree sanity check failed: %d\n
modification
apfs-dir-size-lock
%s:%d: reaper initialization failed: %d - %s\n
%s/nx
apfs-fext-tree-oid-lock
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
spaceman_ip_block_alloc
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
apfs-pfkur-tree-oid-lock
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
DELETE
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: tx_enter for initialization failed: %d - %s\n
omap=ephemeral
insert_jobj
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
nx_tx_wait_closed
authapfs_integrity_meta_get_internal
Could not set uuid from role 0x%x, error %s
btree_node_debug_stats
%s:%d: failed load container metadata ranges (overlap?): %d\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
61706673-7575-6964-01c0-766f6c756d00
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
61706673-7575-6964-0010-766f6c756d00
Internal
%s:%d: %s %s tree: PATH TOO LONG: %d\n
Removable
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
tx_flush
fd_dev_read_helper
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
spaceman_free_extent_cache_search
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
apfs
cst %llu hit zero retain count but still has ep related retain count (%u)\n
assertion failed: %s
missing operand for '-%c'
%sName:[%s] Class:[%s]
%s:%d: %s spaceman IP free block count is wrong %lld != %lld\n
capacity: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
spaceman_metazone_init
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
spaceman_free_extent_cache_setup
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
%s:%d: %s failed to allocate bitmap block from IP bitmap pool: %d\n
uuid_from_role
%s:%d: %s fs snap meta tree xid %lld > spaceman xid %lld\n
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
%s:%d: %s failed to update rightmost leaf field: %d\n
rdisk
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
%s:%d: %s cib %lld xid %lld > spaceman xid %lld\n
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
%s:%d: %s spaceman chunks per cib is bad: %d\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
obj_init
%s:%d: %s obj_create failed - %d\n
AppleAPFSVolume
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
bt_insert
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
IOBlockStorageDevice
%s:%d: %s fragmented checkpoint area failed sanity check: %d\n
obj_checkpoint_get
another file system
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
%s:%d: %s failed to update dir-stats %llu: %s (%d)\n
fd_dev_close
61706673-7575-6964-0002-766f6c756d00
%s:%d: %s spaceman free queue count %lld doesn't match count in the free queue: %lld\n
nx_check_reaper
%s:%d: %s iter_next returned %d\n
%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
RR_HOLE
apfs-incompat-features-lock
%s:%d: %s failed to update allocate zone %llu: error %d\n
%s:%d: tx_leave for omap initialization failed: %d - %s\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
spaceman_ip_freed
tx_unmount
%s:%d: %s spaceman IP bitmap block count is too low: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
%s:%d: %s failed to get mapping tree, error: %d\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
apfs-im-cache-lock
spaceman_alloc_fxc_scan_wait
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
cannot nest APFS containers
%s:%d: %s spaceman IP bitmap block %d index %d out of range\n
SYSTEM_GRAFT_4K_OBJS
%s:%d: %s error deleting empty snapshot tree: %d\n
uid=
%s:%d: %s spaceman IP bitmap has too many free blocks %lld > %lld\n
%s:%d: %s unable to get fs extentref tree: %d\n
%s:%d: %s unable to get fs snap meta tree: %d\n
removal
%s:%d: %s omap_destroy returned %d!\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
obj_checksum_verify_phys
ino-lock
large_key_val_to_jobj
%s:%d: %s Attempt to load temporary checkpoint found unexpected data (0x%02x @ %d), checkpoint descriptor block %d @ %lld\n
fd_dev_write_extended
supplemental_tree_get_descriptor
%s:%d: %s Can't get tree: %d\n
nx-txn-blocks-lock
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
new address mismatch on redirty 0x%llx 0x%llx\n
%s:%d: %s First sync/barrier failed: %d\n
apfs_is_volume_role_allowed
%s:%d: %s failed to write cib %d: %d\n
%s:%d: %s failed to read cab %d: %d\n
case=insensitive
password=
MODKEY
%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n
spaceman_sanitize_datazones
spaceman_chunk_zone_info_recent_decrement
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s container block size too small for device block size (%d < %d)\n
%s:%d: %s unable to get spaceman IP free queue tree: %d\n
%s:%d: %s fs root tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
0
jobj_size_for_key_val
%s:%d: %s checkpoint xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
obj_checkpoint_start
obj_checkpoint_check_for_unknown
%s:%d: %s omap snapshot count %d seems excessive\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
%s:%d: %s failed to find valid checkpoint: %d\n
ephemeral
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
61706673-7575-6964-0180-766f6c756d00
%s:%d: %s omap snapshot tree xid %lld > spaceman xid %lld\n
apfs-omap-lock
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: creation of fragmented metadata physical extent list tree(s) failed: %d - %s\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
omap_sanity_check
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
nx_metadata_fragmented_sanity_check
nx_unblock_physical_range
FIXUP
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
%s:%d: %s failed to initialize cab %d: %d\n
tx_finish
%s:%d: %s unable to get snap meta tree %lld: %d\n
sealed, fext, req_tree != fs_root
obj_cache_remove_graft_persistent_ephemeral
spaceman_unreserve
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
object-cache-lock
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
%s:%d: %s waiting for transaction to finish\n
defragment=no
nx-omap-lock
%s:%d: Volume role 0x%x is not supported
image-format-read-only
spaceman_init_cib
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
root
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
authapfs_validate_node
fsindex=
%s:%d: %s FS will NOT have extended vek protection classes\n
%s:%d: %s unable to create chunk zone info cache lock: %d\n
%s:%d: %s validation failed for checkpoint at index %d: %d\n
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s Err: unable to fetch properties\n
%s:%d: %s spaceman IP bitmap unable to get bitmap block %d @ %lld: %d\n
%s:%d: %s updating grandparent failed w/%d\n
obj_read
sha3_384
%s retry %d/30
maxfs=
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
%s:%d: failed to get spaceman: %d\n
spaceman_free
btree_iterate_nodes
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
apfs-stream-id-lock
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: object cache initialization failed: %d - %s\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
spaceman_clear_bits_in_bm
<80
nx_reaper_checkpoint_traverse
bt_update_last_leaf
%s:%d: %s failed to initialize free extent cache, error %d\n
spaceman_chunk_zone_info_list_remove
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
sha3_384_4k
%s:%d: %s spaceman IP block count is bad: %lld\n
%s:%d: %s error getting IP block index for cib %lld ci %d bm addr %lld\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
sealed=yes
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: %s failed to allocate buffer for checkpoint superblock\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s obj_modify failed - %d\n
%s:%d: %s snap meta tree %lld: %d\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s error getting IP block index for spaceman IP free queue tree entry %lld:%lld %lld\n
blocks_in_txn
INSERT
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s extentref tree type 0x%x invalid, using physical btree instead\n
%s:%d: %s checkpoint descriptor length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: failed to set up sm allocation metadata: %d\n
tx_checkpoint_space_check
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
authapfs_integrity_meta_create
,
%s:%d: %s failed to create reap list: %d\n
%s:%d: %s spaceman IP bitmap free next %d, value %d invalid\n
fsreserve=
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
%s:%d: %s failed to delete fs clonegroup tree after fs creation failed: %d\n
apfs-integrity-meta-lock
%s:%d: %s failed to fix up checkpoint data: %d\n
%s:%d: %s checkpoint search: largest xid %lld, best xid %lld @ %d\n
newfs_apfs
61706673-7575-6964-0004-766f6c756d00
%s:%d: %s Failed to get fsys oid %lld - %s\n
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
nx_dev_init
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
%s:%d: %s tx xid %lld took %lld us to flush\n
hash=
btree rightmost leaf mismatch! (expected %lld found %lld)\n
spaceman_get_metazone_alloc_index
%s:%d: %s cib %lld chunk info %d block count %d should be %d\n
%s:%d: %s btree_node is null\n
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s checkpoint: largest xid %lld, given checkpoint xid %lld @ %d\n
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
tx_leave
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
an APFS configuration
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
gbitmap_reap
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
fsreserve=%s
unexpected argument
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
io_get_device_features
%s:%d: %s loading older checkpoint, checkpoint xid %lld, superblock xid %lld\n
%s:%d: failed to write superblock to block 0: %d - %s\n
omap_cleanup
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
%s:%d: error: block size %d is not an even multiple of device block size %d\n
obj_cache_flush_prepare
Can't create an encrypted volume with special role 0x%x
%s:%d: %s spaceman IP bitmap next array free count is wrong, %lld != %d\n
%s:%d: %s failed to get reap list tail: %d\n
%ss%d
%s:%d: %s unable to allocate chunk zone info cache\n
%s:%d: %s checkpoint descriptor index %d out of range [0...%d]\n
%s:%d: %s checkpoint descriptor block %d superblock failed sanity checks: %d\n
%s:%d: %s failed to set up sm allocation metadata: %d\n
blocksize=%s
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: cannot change role of xART volume\n
apfs-flags-lock
apfs-snap-delete-lock
%s:%d: %s bogus phase, %u\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s cib %lld index %d should be %lld\n
%s:%d: %s cib %lld chunk %d unable to get bitmap block @ %lld: %d\n
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
BSD Minor
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
Yes
61706673-7575-6964-0001-766f6c756d00
nx_metadata_range_optimize
%s:%d: %s failed to delete mapping, error: %d\n
%s:%d: %s fs root tree creation failed: %d\n
apfs_is_volume_uuid_allowed
%s:%d: %s *** trim'ing free blocks returned: %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: %s invalid reap_id (%llu), must be smaller than nr_next_reap_id (%llu)\n
%s:%d: %s fs snapshot metadata tree creation failed: %d\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s reaper needs more cowbell, flags 0x%x\n
nx_metadata_range_add
fs_obj_create_name_checked
resource fork size
btree_node_child_val
%s:%d: %s checkpoint data length is bad.  Container cleanly-unmounted flag ignored\n
%s:%d: %s failed nx_check sanity: %d\n
%s:%d: %s spaceman chunk info block %lld addr %lld not within IP block range\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
%s:%d: %s expanded record found on unsupported volume\n
spaceman_alloc
spaceman_fs_bounds_set
%s:%d: %s tx xid %lld took %lld us to close\n
dev_init_common
%s:%d: %s large key size (%u) on record (%llu) is too small\n
bt_lookup_copy_out
AppleAPFSContainer
level %d: %d nodes %.2f average descendents\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
role=%s
61706673-7575-6964-02c0-766f6c756d00
.
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
nx_reap_list_sanity_check
spaceman_ip_bm_block_free
%s:%d: %s spaceman free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s omap tree xid %lld > spaceman xid %lld\n
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
%s:%d: %s failed to delete fs root tree after fs creation failed: %d\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
%s:%d: Volume role 0x%x is not supported in container\n
invalid unlock flags: 0x%x\n
omap_reap
%s:%d: %s Trash unfinished tx xid=0x%llx\n
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
sha3_256
%s:%d: %s spaceman free count %lld doesn't match free count in chunks %lld\n
obj_checkpoint_done
%s:%d: %s %lld blocks trimmed in %lld extents (%lld us/trim, %lld trims/s)\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
61706673-7575-6964-0300-766f6c756d00
%s:%d: %s spaceman free count is too large: %lld > %lld\n
nx_reaper_sanity_check
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
%s:%d: spaceman initialization failed: %d - %s\n
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
spaceman_checkpoint_traverse
61706673-7575-6964-00c0-766f6c756d00
61706673-7575-6964-0200-766f6c756d00
%s:%d: %s spaceman IP bitmap block count per tx is too small: %d\n
%s:%d: %s cib %lld chunk info %d free count %d > chunk block count %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
btree_delete
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s sm_fs_reserve_alloc_count underflow, sm_fs_reserve_alloc_count %lld, new fs_reserve_block_count %lld, old fs_reserve_block_count %lld alloc_count %lld\n
%s:%d: %s spaceman IP free queue tree sanity check failed: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
bt_remove_internal
spaceman_fxc_print_stats
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
nx_tx_flush_busy
%s:%d: %s spaceman IP bitmap free head %d out of range\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
btree_node_child_id_update
spaceman-free-lock
%s:%d: %s extentref tree %lld: %d\n
%s:%d: %s clone mapping is enabled for this volume\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
apfs-rename-lock
%s:%d: %s failed to write cab %d: %d\n
%s:%d: %s spaceman blocks per chunk is bad: %d\n
%s:%d: %s omap check failed for omap %lld: %d\n
%s:%d: %s failed to initialize cib %d: %d\n
%s:%d: %s last reap list object 0x%llx doesn't match tail 0x%llx\n
%s:%d: %s spaceman_unset_block_out_range failed with error %u\n
btree_node_val_range_validate
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
unable to format volume inside %s
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
jobj_to_large_key_val
object-cache-list-lock
%s:%d: unlock == 0 failed %d\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
jobj_refcnt_merge
obj_create_internal
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
tx_mgr_free_tx
bad pext.\n
not allowed to create volume with role %hu
%s:%d: %s error getting IP block index for spaceman chunk info block %lld addr %lld\n
%s:%d: %s omap tree sanity check failed: %d\n
%s:%d: %s tx_leave failed with error: %d\n
disk
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
spaceman_set_bits_in_bm
spaceman-czic-lock
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
volname=%s
failed to get media from %s
failed to allocate memory for entitlements blob
APFS_8K_OBJS
%s:%d: %s clonegroup tree creation failed: %s\n
apfs-dir-stats-id-lock
spaceman_decrement_free_queue_count
spaceman_free_fs_deduct_block_counts
%s:%d: %s spaceman IP free queue tree entries out of order: xid %lld < %lld\n
%s:%d: %s unable to get prev doc-id tree: %d\n
%s:%d: %s unable to get omap tree: %d\n
omap_find_next_snapshot_xid
spaceman_iterate_free_extents_internal
%s:%d: %s Final sync/barrier failed: %d\n
_fd_dev_write
AppleAPFSMedia
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s failed to compare currently available space: error %d\n
%s:%d: %s stopped updating dir-stats due to chain being too long\n
%s:%d: %s couldn't allocate memory for checkpoint map block\n
obj_write_prepare
%ss%d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld range is bad\n
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
nx_reaper_add_sub_object
__apfs_dec_parent_nlink
%s:%d: cannot change role of system-unique volume\n
total size
%s:%d: %s cab %d cib count %d should be %d\n
%s:%d: %s doc-id tree sanity check failed: %d\n
APFS_4K_OBJS
spaceman_chunk_zone_info_cache_init
%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
apfs-phys-lock-state-mutex
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%s:%d: %s Quota %llu is smaller than reserve %llu\n
spaceman-dev-lock
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
nx_checkpoint_find_valid_checkpoint
%s:%d: cannot change role of SideCar volume\n
match_jobj_expanded_type_to_tree_type
btree_node_insert_internal
apfs-doc-id-lock
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
nx-resize-spaceman-lock
btree_node_entry_update
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
sha3_512
%s:%d: %s cib %lld cib_chunk_info_count %d invalid\n
%s:%d: %s reloading after unclean unmount, checkpoint xid %lld, superblock xid %lld\n
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
tx-mgr-lock
%03llu
%s:%d: %s *** unknown expanded obj type %hhu\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
spaceman_init_cab
%s:%d: %s failed to write checkpoint map block %lld: %d\n
nx_tx_wait_flush
%s:%d: %s cab %d @ %lld cab_cib_count %d invalid\n
%s:%d: %s fs root tree xid %lld > spaceman xid %lld\n
jobj_validate_key_val
private-dir
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d: %s reap list object 0x%llx max record count %u not expected value %u\n
%s:%d: %s tx_leave failed: %d\n
%s:%d: Unknown subtype %d for file info object %lld\n
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
spaceman_free_extent_cache_remove
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
omap_recent_sanity_callback
%s:%d: Volume role %d is not allowed at fs index %d\n
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
spaceman_free_extent_cache_reset
%s:%d: %s failed to get omap %lld: %d\n
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
mount_apfs
%s:%d: %s reaper check failed with error: %d\n
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
spaceman_fxc_update_length
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s unable to get spaceman: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
tx_checkpoint_desc_zero
unable to reformat volume %s
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
=%d
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: device initialization failed: %d - %s\n
%s:%d: %s reap list object free list erroneously empty?\n
 ???
com.apple.private.apfs.xart
61706673-7575-6964-0240-766f6c756d00
%s:%d: %s spaceman IP bitmap free list corrupted, too long, count %lld\n
%s:%d: %s FS will NOT be encrypted.\n
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s couldn't read superblock of size %d\n
unable to format %s
%s:%d: %s unable to get omap snapshot tree: %d\n
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
btree_node_reap
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s spaceman free count %lld doesn't match free count in bitmap %lld\n
nx_check_recent_sanity
btree_check_recent_sanity
%s:%d: %s tx manager initialization failed: %d\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
%s:%d: %s Tree delete oid %llu threw %d\n
encrypted
apfsuuid
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
authapfs_valid_hash_type
gid=
%s:%d: %s spaceman cib count is bad: %d\n
%s:%d: %s container cleanly-unmounted flag set.\n
%s:%d: omap initialization failed: %d - %s\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
%s:%d: %s failed to get reap list object oid %lld: %d\n
... 
%s:%d: %s spaceman IP free queue count is too large: %lld > %lld\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%s:%d: graft with invalid fs block size: %u\n
%s:%d: invalid object size: %d size_phys %d\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%d: %s reap list object 0x%llx record count %d larger than max %d\n
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s attribution tags are supported on this volume\n
apfs_checkpoint_traverse
%s:%d: tx checkpoint descriptor area initialization failed: %d - %s\n
%s:%d: %s obj_modify() failed: %d\n
sha256
volname=
%s:%d: %s btree check called with non-root btree node: %d\n
nx_reaper
spaceman_chunk_zone_info_load_recent_chunks
%s:%d: device initialization failed: %d\n
    keys: %9d %9d %9d %9d %9d %9d\n
jfs_get_tree_in_snap
update_dir_stats_by_key_ext
unrecognized option '%s'
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
%s:%d: %s Failed to get next extent: %d\n
spaceman_sanity_check
%s:%d: tx manager initialization failed: %d - %s\n
spaceman_set_up_ip_reverse_mapping_tree
supplemental_tree_create
%s:%d: %s unable to get omap: %d\n
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
apfs_newfs
%s:%d: %s failed to move all entries: %d\n
spaceman_fq_tree_insert
not handling the current tx!\n
%s:%d: %s %s: could not insert inode obj-id %lld (name: %s)\n
unexpected storagetype: 0x%x\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s spaceman IP bitmap free list corrupted, too short, count %lld\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
total_count
spaceman_allocation_init
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
nx_reaper_next_record
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
%s:%d: %s %llu blocks are already reserved in container, Cannot reserve more than %llu blocks in the container\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
%s:%d: %s unable to read cib %lld @ %lld: %d\n
%s%llu %cB%s
spaceman_free_extent_cache_insert
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
nx_tx_wait
spaceman_upgrade_sm_version_0_to_1
Get count overflowed for object %p!\n
some non-applicable container options were ignored
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
Target Disk Mode
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
%s:%d: %s spaceman IP bitmap tx multiplier is too small: %d\n
%s:%d: %s spaceman free queue count is too large: %lld > %lld\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
capacity: all    %llu / %llu => %.2f %% used\n
%s:%d: %s object type 0x%x not reapable: %d\n
%s:%d: %s failed to delete fs fext tree after fs creation failed: %d\n
%s:%d: %s prev doc-id tree xid %lld > spaceman xid %lld\n
exp-dir-stats
%s:%d: %s Error reinitializing free extent cache: %d\n
%s:%d: %s Unknown object loaded from checkpoint: oid 0x%llx type 0x%x/0x%x\n
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
%s:%d: %s unable allocate space that should be there: %d\n
bt_shift_or_split
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
unwritten
61706673-7575-6964-0008-766f6c756d00
%s:%d: %s spaceman cibs per cab is bad: %d\n
%s:%d: %s spaceman free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
unable to open %s
%s:%d: %s spaceman IP free queue count %lld doesn't match count in the free queue: %lld\n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
%s:%d: %s bad overprovisioning volume configuration: reserve %lld quota %lld\n
%s:%d: don't know how to merge refcounts on objects of type %d\n
obj_get_async_read
blocksize=
%s:%d: %s cab %d index %d should be %d\n
%s:%d: %s omap tree entries out of order: oid %lld xid %lld <= lastxid %lld\n
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
prevent_synthetic_object_operation
apfs-global-lock
%s:%d: %s error getting cib %d @ %lld: %d\n
%s:%d: %s omap xid %lld > spaceman xid %lld\n
%s:%d: %s Making temporary checkpoint %lld permanent (start %lld).\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
%s:%d: %s cib %lld ci %d free count %d doesn't match free bits in bitmap block %lld\n
<%d
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
apfs-global-snap-lock
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
%s:%d: %s xid %lld second sync/barrier failed: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
%s:%d: %s fs creation failed: %d ... cleaning up...\n
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
nx_mount
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
spaceman_fs_bounds_clear
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
conformance
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
%s:%d: %s this volume requires valid UUID option specified\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
spaceman-space-usage-lock
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
nx_get_evict_mapping_tree
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
ino-io-lock
num children
%s:%d: %s error modifying omap: %d\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
%s:%d: %s found mapping tree with old subtype\n
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
descendants
MODVAL
spaceman_cab_sanity_check
missing argument
nx-tree-node-compact-lock
%s:%d: %s checkpoint xid %lld failed to get spaceman: %d\n
invalid lock flags: 0x%x\n
nx_tx_finish_wait
%s:%d: %s spaceman IP bitmap block %d xid %lld > spaceman xid %lld\n
%s:%d: %s no space for a new file system (slot %d, max %d)\n
%s:%d: %s tx_enter_frozen() failed: %d\n
obj-mem-mgr-lock
current tx not closed/flushing?!\n
%s
unwritten=no
spaceman-fxc-lock
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
obj_destroy_complete
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s/apfs_data
%s (%s)
%s:%d: %s omap entry %lld:%lld addr %lld size %d is bad\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
exp_dir_stats_refcnt_merge
%s:%d: %s Error %d, reinitializing\n
nx_tx_wait_closed_prev_flushing
apfs_free_data_blocks
%s:%d: %s failed to enter tx to update size tracking for ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: %s failed to set up spaceman for demo mode: %d\n
spaceman-ip-lock
%s:%d: %s No temporary checkpoint start xid!  Aborting!\n
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
START
Device Characteristics
obj_cache_remove_new_fs_objects
%s:%d: %s %s: could not insert dir rec for obj-id %lld (name: %s)\n
%s:%d: %s fs private dir creation failed: %d\n
apfs-snapmeta-oid-lock
spaceman_trim_free_blocks
spaceman_trim_free_extent_callback
%s:%d: %s Error: tx[%lld] failed to start: %d\n
io_get_num_device_blocks
gid=%s
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
io_get_device_block_size
3288.52.1
:b:ieo:q:r:s:v:wACDWEG:PR:S:U:Txcam
defragment=yes
61706673-7575-6964-0000-766f6c756d00
%s:%d: %s fs extentref tree xid %lld > spaceman xid %lld\n
%s:%d: %s omap entry %lld:%lld size %d seems excessive\n
addition
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
%s:%d: %s spaceman free queue tree entry %lld:%lld %lld addr is bad\n
nx_reaper_add_ext
%s:%d: %s fext tree type 0x%x invalid, using physical btree instead\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
%s:%d: %s lookup_next_snapshot() returned %d\n
update_size_tracking
%s:%d: %s Fusion is not supported anymore\n
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
%s:%d: %s failed to delete fs extentref tree after fs creation failed: %d\n
jobj_validate_large_key_val
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
%s:%d: %s unsupported nx_readonly_compatible_features (0x%llx): mount r/o\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
spaceman_free_completed
AppleAPFSContainerScheme
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
%s:%d: %s waiting for available tx to open: xid %lld\n
sha384
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
IOMedia
Reference count overflowed for object %p!\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s failed to zero checkpoint descriptor block %d @ %lld: %d\n
omap=btree
%s:%d: %s spaceman IP free queue tree entry %lld:%lld xid larger than spaceman xid %lld\n
clone size
!((apfs)->apfs_main_apfs != ((void*)0))
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
obj_checkpoint_known
some non-applicable volume options were ignored
IOService
failed to create CFData from entitlements blob
%s%llu%-*.*s %cB%s
%s:%d: cannot change role of Backup volume\n
%s:%d: %s fs root dir creation failed: %d\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
invalid tweak type %d\n
<UNKNOWN>
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
%s:%d: %s unable to create/store metadata crypto (%d)\n
btree_node_copy
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
 (
remove_jobj
bt_merge_up
%s:%d: %s object cache bootstrap failed: %d\n
61706673-7575-6964-0020-766f6c756d00
<40
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
nx-volume_group-lock
omap_destroy
%s:%d: %s omap entry %lld:%lld unknown flags are set: 0x%x\n
%s:%d: %s omap entry %lld:%lld marks deletion of object with no earlier mappings\n
SNAP_DELETE_TXN
apfs_reap_extentref_blocks
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
spaceman_chunk_zone_info_recent_increment
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
%s:%d: %s unsupported tree type: %d\n
%s is already a synthesized APFS device
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s checkpoint descriptor block %d is not a valid superblock\n
%s:%d: %s removal of replaced free extent failed: %d\n
%s:%d: %s omap tree type 0x%x is bad\n
%s:%d: %s X %d\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
%s:%d: %s btree_node_key_update failed: %d\n
%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n
update_dir_stats
%s:%d: %s error unreserving space, %lld blocks: %d\n
%s:%d: %s Failed to create supplemental tree (type %d): %d\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
btree_node_sanity_check
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%s:%d: %s spaceman free queue tree entries out of order: addr %lld < %lld\n
%s:%d: %s fext_tree_remove returned %d\n
can't have a negative refcnt on crypto state %llu refcnt %d\n
failed to create CFDictionary from entitlements XML
%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n
%s:%d: %s unable to get snapshot tree: %d\n
fd_dev_read_extended
%s:%d: %s unable to get fs root tree: %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s ***: expanded type seen on in-memory obj\n
spaceman-czic-scan-lock
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
spaceman_fq_tree_find_overlap
%s:%d: %s unable to get doc-id tree: %d\n
%s:%d: %s omap entry %lld:%lld xid > spaceman xid %lld\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
%s:%d: %s fs omap initialization failed: %d\n
btree_node_free_list_entry_validate
apfs-phys-ext-oid-lock
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: %s spaceman chunk count is bad: %lld\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
61706673-7575-6964-0140-766f6c756d00
nx_check_recent_sanity_omap
%s:%d: %s omap snapshot count %d doesn't match snapshot tree record count %lld\n
update_jobj
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
%02hhx
%s:%d: %s spaceman free queue tree iteration aborted with error %d\n
jobj_to_key_val
%s:%d: Volume role 0x%x is not allowed for an unencrypted volume\n
%s:%d: %s stable checkpoint indices: desc %d data %d\n
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld addr is bad\n
%s:%d: %s failed to get reap list head: %d\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
%s:%d: %s Invalid reap list free entry %d\n
%s:%d: ***: unknown obj type %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
nx_tx_wait_frozen
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
Trying to update a namedstream inode %llx on volume %s\n
%s:%d: %s UUID %s is not allowed, error %d\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
nx_checkpoint_load_data
spaceman_alloc_iterate_chunks
nx_tx_wait_closing
authapfs_validate_node_hash
purgeable size
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s xid %lld sync/barrier failed: %d\n
%s:%d: %s spaceman IP bm base address is bad: %lld\n
%s:%d: %s Could not set fs bounds for guarantee %lld and quota %lld: %d\n
%s:%d: %s failed to delete fs snap metadata tree after fs creation failed: %d\n
%s:%d: %s bt_shift_or_split failed with error: %d\n
apfs_reap_snapshots
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
%s:%d: object memory manager failed to create lock, error: %d\n
sha3_512_4k
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
object-cache-flush-lock
%s:%d: Container corruption detected by %s:%u!\n
conflicting '-A' and '-C' options
%s > %s : %s
%s:%d: %s cib %lld chunk info count %d should be %lld\n
dir-stats
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
tx_enter_internal
[-o options] [-b block-size] [[-s volume-size] | [-r volume-reserve] [-q volume-quota]] [-v volume-name] [-i | -e] [-U uid] [-G gid] [-E [-S passphrase | -W (empty password) ]] [-A | -C] [-R role] [-D] [-w] [-x] [-T] [-c] [-a] device
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s Hit %d looking up first snapshot\n
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
-m requires -c as well
61706673-7575-6964-0280-766f6c756d00
%s:%d: %s omap snapshot tree type 0x%x is bad\n
%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
btree_check_ext
btree_node_key_range_validate
nx_check_checkpoint_map_block
obj_cache_remove_reverted_fs_objects
%s:%d: %s omap check failed with error: %d\n
%s:%d: %s fs extentref tree sanity check failed: %d\n
spaceman_fxc_update_smallest_with_successor
obj_mem_mgr_init
%s:%d: %s error getting mapping tree: %d\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
spaceman_create
%s/apfs
nx_check_omap
%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: can't get features for device (%s)\n
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s failed to allocate block from internal pool: %d\n
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
%s is an APFS volume
%s:%d: %s unable to get spaceman free queue tree: %d\n
%s:%d: %s %s: could not remove inode obj-id %lld (name: %s)\n
jobj_allocate
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: failed to finish first transaction: %d - %s\n
%s:%d: %s existing file system (slot %d)\n
obj_cache_remove
container not published on %s
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: %s error updating metadata ranges tree: %d\n
%s:%d: object cache bootstrap failed: %d - %s\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
%s:%d: failed to open container device %s: %s\n
%s:%d: %s omap snapshot tree sanity check failed: %d\n
jobj_size_for_large_key_val
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s failed to read cib %d: %d\n
%s:%d: %s spaceman block size %d doesn't match nx superblock block size %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
nx_checkpoint_find_highest_xid
apfs-clonegroup-lock-mutex
%sr%s
spaceman_check_allocation_status_internal
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
%s:%d: failed to open volume device %s: %s\n
val_size_for_jobj
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
spaceman_chunk_zone_info_add
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
Reserved space < reserved metadata: %llu < %llu\n
fstree=btree
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
%s:%d: %s reverting on error: %d\n
%s:%d: %s checkpoint superblock index %d doesn't match index block was found at: %d\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
entitlement was not expected CFBoolean type
%s:%d: checkpoint<->container superblock mismatch on uuid\n
%s:%d: %s spaceman IP base address is bad: %lld\n
attr tag
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s failed to get omap tree for reaping: %d\n
%s:%d: %s scan took %lld.%06lld s, trims took %lld.%06lld s\n
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
not handling the flushing tx!\n
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
%s:%d: %s superblock failed sanity checks: %d\n
%s:%d: %s object cache initialization failed: %d\n
nx_mount_initiate_free_space_trims
%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n
%s:%d: %s failed to create fs: %d\n
%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
nx_tx_wait_open
btree_node_check
UNKNOWN TXN TYPE
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
%s:%d: %s storage is untrusted. Container cleanly-unmounted flag ignored\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
Physical Interconnect Location
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
%s:%d: %s spaceman cab count is bad: %d\n
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
jobj_type_from_possibly_large_key
%s:%d: %s Volume role 0x%x already exists in container uuid %s\n
%s:%d: *** Can't allocate unknown obj type %d\n
curproc
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
%s:%d: %s spaceman IP free queue tree iteration aborted with error %d\n
fssize=
%s:%d: %s spaceman IP bitmap block count is too large: %d\n
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: %s error getting end block index for spaceman IP free queue tree entry %lld:%lld %lld\n
/dev/
FULL
nx-global-extent-manipulation-lock
%s:%d: %s *** failed to set rdev as an extended field of ino %lld (ret %d)\n
bt_merge_nodes
length
%s:%d: %s block size %d is not an even multiple of device block size %d\n
capacity: leaves %llu / %llu => %.2f %% used\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
%s:%d: %s failed to wait on reaper: %d\n
%s:%d: %s failed to scan checkpoint descriptor area for largest xid: %d\n
obj_cache_graft_attach
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
obj_release
spaceman-lock
%llu%s
%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n
%s:%d: metadata space calculation failed: %d - %s\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
spaceman_freed
%s is hosting %s
unable to reformat %s
APFS_INODES
IOMatchCategory
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
key_val_to_jobj
%s:%d: %s Couldn't reopen transaction to clean up: %d\n
%s%s
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%s:%d: warning: fs block size too small for device block size (%d < %d)\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%s:%d: %s snapmeta tree type 0x%x invalid, using physical btree instead\n
%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
obj_checksum_verify
wipefs
%s:%d: %s reap list tail 0x%llx is not last reap list object, next 0x%llx\n
key_size_for_jobj
%s:%d: %s unable to get reaper: %d\n
%s:%d: %s doc-id tree xid %lld > spaceman xid %lld\n
type = %u, req_tree != fs_root\n
spaceman_cib_sanity_check
case=sensitive
fsquota=
%s:%d: %s spaceman IP free queue tree entry %lld:%lld %lld end addr is bad\n
%s:%d: %s reaper has tail with no head\n
%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
Release count overflowed for object %p!\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
%s:%d: %s fs extentref tree creation failed: %d\n
nx_check
%s:%d: %s spaceman IP bm block count is bad: %d\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
%ss%d:%lld
%s:%d: %s data for checkpoint at index %d couldn't be loaded: %d\n
 (%s)
61706673-7575-6964-0100-766f6c756d00
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
%s:%d: %s failed to destroy omap after fs creation failed: %d\n
spaceman_fxtp_add_child
%s:%d: conflicting mount options: is_system_graft but not is_graft\n
virtual object dirty count underflow\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
invalid value for '-%c'
61706673-7575-6964-0080-766f6c756d00
<20
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
btree_node_compact
unknown option '-%c'
failed to get container scheme from %s
spaceman_fxc_tree_node_recycle_smallest
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: %s failed to attach graft to object cache: %d\n
object-lock
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
level %d: %d nodes\n
  values: %9s %9s %9s %9s %9s %9s\n
Protocol Characteristics
%s:%d: warning: fs block size too small (%d < %d)\n
obj_alloc
fsquota=%s
quota must be larger than reserve
%s:%d: %s fs tree type 0x%x invalid, using virtual btree instead\n
make_large_jkey_header_from_jobj
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
sha3_256_4k
omap=physical
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
%s:%d: %s failed to get object oid %lld: %d\n
btree_node_insert
nx_superblock_agrees_with_container_superblock
%s:%d: %s Quota %llu is smaller than what's currently allocated and reserved %llu\n
%s:%d: %s spaceman block count %lld doesn't match nx superblock block count %lld\n
%s:%d: %s cib %lld chunk info %d addr %lld should be %lld\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
tx_checkpoint_write
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
lookup_jobj_ext
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
failed to copy entitlements blob
%s:%d: %s %s: could not update parent obj-id %lld on create of obj-id %lld (name: %s)\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
fs_tx_enter_internal
nx_tx_finish_wait_for_dirty_data
failed to get entitlements blob size
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s cib %lld ci %d bm addr %lld not within IP block range\n
<100
%s:%d: *** unknown obj type %d\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s cab %d xid %lld > spaceman xid %lld\n
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s btree_node_insert failed: %d\n
role=
%s:%d: %s failed to write superblock to block 0: %d\n
%s:%d: %s Attempting to load from temporary checkpoint (start xid %lld).\n
%s:%d: %s Couldn't load checkpoint from cleanly-unmounted state.  Falling back to descriptor scan.\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
\t%16p %s\n
invalid crypto index %d\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
fssize=%s
APFS_BTREE_NODES
fs_tx_leave_ext
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
apfs_reap
spaceman_chunk_zone_info_compare
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%d: %s tx_finish() failed, %d\n
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
)
%s:%d: %s expanded records are now supported\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s error getting cab %d @ %lld: %d\n
%s:%d: %s failed to write superblock to block %lld: %d\n
  values: %9d %9d %9d %9d %9d %9d\n
empty_password
password=%s
untitled
physical object dirty count underflow\n
make_jkey_from_jobj
purgeable rsrc size
apfs_sanity_check_tree_type
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n
spaceman_ip_bm_block_alloc
%s:%d: Invalid or unknown hash type: %d\n
%s:%d: %s fs fext tree creation failed: %d\n
%s:%d: %s fext_tree_update returned %d\n
full clone size
%s is not an APFS container
Attempting to reuse a non-candidate chunk zone info\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
obj_delete_internal
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s spaceman free queue tree sanity check failed: %d\n
btree_node_space_stats
capacity: nodes  %llu / %llu => %.2f %% used\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
virtual
spaceman_modify_bits
apfs_is_volume_fsindex_allowed
%s:%d: *** Unknown file info type %llu\n
Reference count underflowed for object %p!\n
sha512_256
No
%s:%d: %s spaceman IP bitmap block count is bad: %d\n
jobj_release
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
nx_corruption_detected_int
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: %s btree_node_insert_internal failed: %d\n
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
```
