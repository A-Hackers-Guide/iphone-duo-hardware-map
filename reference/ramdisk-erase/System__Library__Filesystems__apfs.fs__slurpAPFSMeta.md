# `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 342,208 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2032)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
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
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>
```

## Strings (781)

```
bt_merge_nodes
jobj_validate_key_val
object-cache-flush-lock
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: SETBIT for fsindex = %d \n
%s/Info.bckup
nx_check_superblock
%s:%d: cib %lld cib_chunk_info_count %d overflow\n
Requested forced secondary_fs_root but the tree is missing\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
Get count overflowed for object %p!\n
nx_checkpoint_find_valid_checkpoint
%s/Info.plist
%s:%d: %s omap_destroy returned %d!\n
bt_update_last_leaf
%s:%d: failed to read CAB %lld error=%d\n
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
%s:%d: %s found unexpected subtype 0x%x for object type 0x%x @ checkpoint descriptor block %d\n
%s:%d: %s failed to get reap list tail: %d\n
%s:%d: failed to write to image file fd #%d, error %d\n
update_progress
apfs-snapmeta-oid-lock
Release count overflowed for object %p!\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
%s:%d: %s xid %lld sanity check of recently-changed structures failed: %d\n
nx_metadata_range_add
detach_from_disk_image
open_output_disk_image
%s/nx
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
nx_checkpoint_find_highest_xid
%s:%d: %s Tree delete oid %llu threw %d\n
fd_dev_read_helper
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
nx_reaper_add_ext
<DIR>
GPTSPUD
apfs-fext-tree-oid-lock
IOMedia
jobj_validate_large_key_val
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
nx_reap_list_sanity_check
%s:%d: failed to write extents to sparse bundles, error %d\n
authapfs_validate_node
fd_dev_close
AppleAPFSContainer
%s:%d: %s checkpoint superblock %d @ %lld: failed sanity check: %d\n
%s:%d: %s Invalid reap list free entry %d\n
nx-tree-node-compact-lock
%s:%d:        up to two -o / -g / -r may be specified in order to output in both formats, or to have a backup copy\n
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
nx_reaper_checkpoint_traverse
%s:%d: Cannot allocate memory for fs_enc_sb_list[%d]
bt_shift_or_split
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
spawn_and_wait
%s:%d: wrlock == 0 failed %d\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s unable to get extentref tree %lld: %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
nx_reaper_sanity_check
%s:%d:   -O : <byte offset> (-G only) offset into the existing simple disk image to write to (one per '-G')\n
%s:%d: Detaching from disk image\n
%s:%d: Volume %s is already unlocked\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
%s%s
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
spaceman_unreserve
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
apfs-im-cache-lock
%s:%d: %s failed to move all entries: %d\n
%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n
spaceman-lock
%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n
START
%s:%d: Volume %s is marked as the main volume for decryption\n
%s:%d: block %llu in buf does not match APFS SB magic %c%c%c%c, fs %d, flags 0x%llx (UNENC: %c)\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
spaceman_free_extent_cache_search
dev_init
fd_dev_read_extended
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
can not delete an object w/a non-current xid %lld o == %p\n
%s:%d:   -t : the <disk> specified is a volume disk, slurp the entire volume\n
> create_sparse_bundle name=\"%s\" band-size=%llu size=%llu\n
io_get_device_features
jobj_size_for_key_val
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
obj_release
load_nx_and_oc
%s:%d:   fs %d, snapshot superblock at paddr %lld\n
%s:%d: %s failed to update allocate zone %llu: error %d\n
apfs-global-lock
%s:%d: %s error updating snapshot tree: %d\n
%s:%d: %s error searching spaceman free queue tree: %d\n
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
object-cache-list-lock
%s:%d: %s unable to get omap tree: %d\n
APFS_BTREE_NODES
Protocol Characteristics
obj_checksum_verify
%s:%d: %s couldn't read checkpoint data block %d @ %lld: %d\n
%s:%d: %s failed to load checkpoint data of type 0x%x:0x%x @ %lld\n
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
nx-txn-blocks-lock
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
%s:%d: failed to open container device %s: %s\n
%s:%d: %s error getting mapping tree: %d\n
jobj_size_for_large_key_val
obj_mem_mgr_init
nx_checkpoint_load_data
%s:%d: Failed to unlock volume %s with supplied passphrase error = %d\n
write_to_sparse_bundle
%s:%d: %s tree_delete() failed: %d\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
obj_delete_internal
%s:%d: failed to skip free extents\n
%s:%d: Failed to get Container BSD name\n
%s:%d: failed to unlock encrypted volumes filesystem (fsoid = %lld), error %d\n
Pre-change CKSUM: 
spaceman_fxtp_add_child
gbitmap_reap
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
spaceman-dev-lock
match_jobj_expanded_type_to_tree_type
%s:%d: too many disk image output copies requested (max is 2)\n
length
apfs-dir-stats-id-lock
disk
%s:%d: %s *** unknown expanded obj type %hhu\n
Attempting to reuse a non-candidate chunk zone info\n
%03llu
spaceman_free_completed
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
nx-resize-spaceman-lock
%s:%d: Done. Total of %lld blocks written\n
%s:%d: Failed to disable crypto io\n
%s:%d: failed obj_get on filesystem omap (fsoid = %lld, omapaddr = %lld), error %d\n
obj_get_async_read
%s:%d: %s superblock failed sanity checks: %d\n
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
nx-global-extent-manipulation-lock
skip_or_annotate_crypto_meta_extents
%s:%d: unlock == 0 failed %d\n
%s:%d: %s chunk %lld recent zone count overflow\n
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
main
%s:%d: disk image output '%s' cannot be created (errno %d)\n
UDIF
%s:%d: %s bt_shift_or_split failed with error: %d\n
obj_alloc
%s:%d: %s xid %lld checkpoint superblock index %d doesn't fit in blocks remaining: %d > %d\n
-layout
 
%s:%d: failed to get snapmeta tree for (fsoid = %lld, fsextentreftreeoid = %lld), error = %d\n
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s Tree iteration threw %d at cursor %llu\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
object-cache-reset-lock
%s:%d: %s couldn't read checkpoint descriptor map block %d @ %lld: %d\n
%s:%d: %s unable to get spaceman: %d\n
apfs_sanity_check
%s:%d: failed to read CIB %lld error=%d\n
omap_cleanup
%s:%d: %s error deleting empty snapshot tree: %d\n
AppleAPFSContainerScheme
%sr%s
spaceman_check_allocation_status_internal
apfs_checkpoint_traverse
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
\t%16p %s\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
%s:%d: %s found unexpected object type 0x%x @ checkpoint descriptor block %d\n
supplemental_tree_get_descriptor
%s:%d:   -T : same as -t, but treat the volume as the main fs (decrypt entire container according to its encryption first)\n
destroy_output_sparse_bundle
paddr
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
btree_node_compact
%s:%d: %s Can't get tree: %d\n
%s:%d: %s btree_node_key_update failed: %d\n
io_get_device_block_size
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: *** Unknown file info type %llu\n
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
Apple_APFS
%s:%d: failed tree_get on filesystem omap (fsoid = %lld, omapaddr = %lld, omaptreepaddr = %lld), error %d\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
ephemeral
obj_init
%s:%d: %s extentref tree %lld: %d\n
spawn_and_redirect_output
%s:%d: cib %lld ci_index %x ci_block_count %d overflow\n
Device Characteristics
%s:%d: *** Can't release unknown obj type %d\n
obj_cache_remove
%s:%d: %s couldn't allocate memory for checkpoint map block\n
%s:%d:   both stdout output and output dir for sparse bundle defined\n
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
spaceman_freed
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
%s:%d: %s unable to get fs object 0x%llx: %d\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
%s:%d: %s superblock container size %lld greater than device size %lld\n
%s:%d: disk image output '%s' doesn't exist or error accessing it (errno %d)\n
authapfs_valid_hash_type
%s:%d: pipe failed while preparing to execute %s: %s\n
obj_checksum_verify_phys
IOBlockStorageDevice
mount_apfs
virtual
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d:   -o : <output directory> where metadata sparsebundle will be created\n
%s:%d: waitpid(%s) failed (pid=%d, errno=%d)\n
reserved metadata space underflow: %lld (%lld)\n
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
spaceman_fq_tree_insert
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
%s:%d: failed to create path to create sparsebundle, error = %d\n
handle_snapshot_extentref_extents
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
spaceman-fxc-lock
spaceman_fxc_update_smallest_with_successor
%s:%d: %s warning: best valid checkpoint xid %lld is less than max free queue oldest xid %lld seen in checkpoint %lld\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
%s:%d:   -v : the <disk> specified is a volume disk, slurp its metadata only\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
obj-mem-mgr-lock
%s:%d: object memory manager failed to create lock, error: %d\n
%s:%d: failed to %s snapshot extentref extents for (fsoid = %lld)\n
wait_for_spawned_process
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s failed to update rightmost leaf field: %d\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d:   Preparing to image %s\n
spaceman_free_extent_cache_reset
%s:%d: %s failed to get reap list head: %d\n
%ss%d:%lld
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
%s:%d: %s unsupported tree type: %d\n
/
-type
invalid unlock flags: 0x%x\n
%s:%d: %s unsupported nx_incompatible_features (0x%llx): unable to mount\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
-nomount
spaceman_chunk_zone_info_load_recent_chunks
apfs_reap_snapshots
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
spaceman_free
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
nx_dev_init
%s:%d: %s superblock block size %d not an even multiple of device block size %d\n
%s:%d:        if <output directory> is not specified /var/tmp is used instead\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
apfs_reap
multiKeyEncryption
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
nx_check_checkpoint_map_block
%s:%d: Removing incomplete sparse bundle under '%s' at index %d\n
attach
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s snap meta tree %lld: %d\n
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
nx_reaper_obj_get
%s:%d: Note that fs %d is File Vault encrypted but no password was given\n
create_output_disk_image
spaceman_fq_tree_find_overlap
large_key_val_to_jobj
%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n
%s:%d: %s xid %lld checkpoint superblock index %d doesn't match index block was found at: %d\n
%s:%d: tree_iterator_next returned error = %d\n
%s:%d: %s omap check failed with error: %d\n
btree_node_child_val
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
%s:%d: failed to write to band file %llx, error %d\n
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
apfs-rename-lock
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
%s:%d: Volume lock failed for %s (error %d)\n
apfs_reap_extentref_blocks
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
spaceman-space-usage-lock
obj_cache_remove_new_fs_objects
%s:%d: %s found unexpected xid %lld @ checkpoint descriptor block %d\n
supplemental_tree_destroy
%s:%d:   -d : container <disk> node to slurp metadata from\n
handle_data_extents
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
\nClearing bits of encryption info (mask: 0x%llx) and setting bit indicating SB is non-encrypted (0x%llx) at byte offset %ld in address %lld\n
%s:%d: %s check of oid:xid %lld:%lld  size %d paddr 0x%llx flags 0x%x failed: %d\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child: %d\n
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
BSD Minor
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
%s:%d: failed to clear extentref extents for (fsoid = %lld, fsextentreftreeoid = %lld)\n
%s:%d: %s node 0x%llx (level %d): error getting index %d key/val: %d\n
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: Skipping fs %d slurp, not requested by user\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
spaceman_free_fs_deduct_block_counts
object-lock
%s:%d: Crypto IO enable failed (error %d)\n
clear_free_extents
%s:%d: %s unable to get omap: %d\n
apfs-phys-ext-oid-lock
apfs-omap-lock
apfs-integrity-meta-lock
%s:%d: %s Hit %d looking up first snapshot\n
rdisk
spaceman_iterate_free_extents_internal
%s:%d: %s invalid checksum for object type 0x%x @ checkpoint descriptor block %d @ 0x%llx\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
%s:%d: %s couldn't allocate memory for superblock of size %d\n
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s/%s-%d.sparsebundle
%s:%d: Attaching to disk image\n
%s:%d: tree_iterator_init returned error = %d\n
%s:%d: %s  Overwriting SB blocks of fs %d to remove decryption info\n
spaceman_chunk_zone_info_list_remove
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
obj_modify
<UNKNOWN>
%s:%d: block %llu detected as APSB, clearing all crypto-flags and setting the un-encrypted flag\n
handle_extentref_extents
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
IOMatchCategory
%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
%s:%d: object cache bootstrap failed: %d\n
W
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
%s:%d: %s unable to get snap meta tree %lld: %d\n
%s:%d: *** unknown obj type %d\n
%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n
%s:%d:   -U : the password for some encrypted volumes is unknown, so copy their blocks as-is (macOS-only option)\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
)
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s Error %d, reinitializing\n
spaceman_fxc_update_length
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
APFS_4K_OBJS
spaceman_fs_bounds_clear
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
omap_sanity_check
Removable
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
new address mismatch on redirty 0x%llx 0x%llx\n
extract_container_bsdname
spaceman_free_extent_cache_remove
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%s:%d: Creating the disk image '%s'. Please be patient, this could take a long time.\n
%s%02x
%s:%d: fs %d, live superblock at paddr %lld\n
authapfs_validate_node_hash
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
according to
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s chunk %lld recent zone count underflow\n
spaceman_alloc_iterate_chunks
obj_destroy_complete
%s:%d: Failed to get IOService object associated with %s for dev %s\n
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
obj_cache_remove_reverted_fs_objects
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
.
%s%llu %cB%s
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: failed to open volume device %s: %s\n
Physical Interconnect Location
%s:%d:   -s : write output to stdout\n
%s/token
spaceman_modify_bits
%s:%d: *** Can't allocate unknown obj type %d\n
invalid lock flags: 0x%x\n
%s:%d: sparsebundle output folder %s must exist and be a folder (errno %d)\n
Internal
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
%s:%d:   -p : password for encrypted volume (macOS-only option and valid only when one of -v, -t or -T is specified)\n
/var/tmp
 (
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s%llu.%.*s %cB%s
btree_delete
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
%s:%d: %s failed to get object oid %lld: %d\n
%s:%d: failed to remove meta extents (fsoid = %lld, omapaddr = %lld, omaptreepaddr = %lld), error %d\n
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s Fusion is not supported anymore\n
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
obj_checkpoint_get
%s:%d: Failed to dev init for volume %s error: %d\n
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
type = %u, req_tree != fs_root\n
%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n
%s:%d: disk node %s does not exist \n
%s:%d: Failed to locate attached APFS container\n
APFS_TREE_LOOKUP_ZONE
Reference count underflowed for object %p!\n
FIXUP
%s/bands/%llx
%s:%d: failed to find latest spaceman, error = %d\n
spaceman_get_metazone_alloc_index
%s:%d: %s unable to read cab %d @ %lld: %d\n
io_get_num_device_blocks
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
%ss%d
spaceman_free_extent_cache_insert
%s:%d: %s bogus phase, %u\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
%s:%d: can't get block count (%s)\n
%s:%d: %s %lld:%lld error: %d\n
%s:%d: %s unable to get object 0x%llx: %d\n
%s:%d: failed to %s extentref extents for (fsoid = %lld, fsextentreftreeoid = %lld)\n
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s unable to get fs[%d] oid %lld, %d\n
bt_merge_up
image-format-read-only
%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n
%s:%d: Passphrase given but no volume set (-v, -t or -T)\n
%s:%d: fsctl(APFSIOC_IS_VOL_LOCKED, %s) failed, error = %d\n
jobj_release
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
r
btree_iterate_nodes
%s:%d: can't get the device block size (%s). assuming 512\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
spaceman_trim_free_extent_callback
invalid crypto index %d\n
%s:%d: %s probe of external device... skipping recent sanity checks.\n
%s:%d: Why are we comparing a chunk to itself?\n
%s:%d: %s unable to get omap %lld: %d\n
%s:%d: %s bt_move_entries %d failed: %d\n
APFS_8K_OBJS
get_free_extents_info_from_spaceman
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
unexpected storagetype: 0x%x\n
%s:%d: checkpoint<->container superblock mismatch on uuid\n
%s:%d: %s failed to get omap %lld: %d\n
btree_node_entry_update
btree_node_free_list_entry_validate
bt_lookup_copy_out
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
spaceman-free-lock
spaceman_sanity_check
%s:%d: device initialization failed: %d\n
apfs-snap-delete-lock
spaceman_ip_bm_block_free
spaceman_set_bits_in_bm
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
destroy_output_disk_image
%s/bands
APFS
%s:%d: failed to get extentref tree for (fsoid = %lld, fsextentreftreeoid = %lld), error = %d\n
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
%s:%d: Open '%s' failed: errno %d\n
%s:%d: %s unable to get omap snapshot tree: %d\n
%s
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
key_val_to_jobj
%s:%d: failed to skip data extents\n
%s:%d: Disk for container is '%s'\n
%s:%d: %s error getting cib %d @ %lld: %d\n
apfs_sanity_check_tree_type
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
spaceman-ip-lock
%s:%d:   no disk set as source\n
%s:%d: Failed to get IOService object associated with %s dev\n
Post-change CKSUM:
%s:%d: %s  Entire container imaging %s fs %d\n\n
%s:%d: %s unable to read cib %lld @ %lld: %d\n
AppleAPFSSnapshot
%s:%d: %s object type 0x%x not reapable: %d\n
%s:%d: %s error modifying omap: %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
/dev/%ss%d
apfs-doc-id-lock
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: failed to annotate encrypted meta extents, error %d\n
%s:%d: Removing incomplete disk image '%s' at index %d\n
%s:%d: failed obj_get on filesystem (fsoid = %lld), error %d\n
%s:%d: failed to get extents for (fsoid = %lld, fsextentreftreeoid = %lld)\n
spaceman_chunk_zone_info_recent_increment
%s:%d: %s unable to get snapshot tree: %d\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
%s:%d: %s invalid object size: %d size_phys %d\n
nx_superblock_agrees_with_container_superblock
%s:%d: too many sparsebundle output copies requested (max is 2)\n
%s:%d: failed to create slurper context\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
make_jkey_from_jobj
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
apfs-global-snap-lock
btree_node_key_range_validate
fd_dev_write_extended
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
%s:%d: %s sanity checking all recently-changed container state... please be patient.\n
%s:%d: fs %d is FV but no password was given. Since '-U' was set, it will be copied as-is and a password will be required for it to be accessible\n
using the decryption info from
AppleAPFSMedia
apfs-phys-lock-state-mutex
%s:%d: %s xid %lld failed to fix up checkpoint data: %d\n
%s:%d: '-t', '-T' or '-v' should be set right after disk argument pass with '-d' option \n
destroy_slurper_context
%s:%d: %s  %sriting the remaining un-encrypted blocks\n\n
%s:%d: %s didn't exit?
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
spaceman_set_up_ip_reverse_mapping_tree
spaceman_decrement_free_queue_count
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
%s:%d: Failed to get base_offset from '%s'\n
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
%s:%d: %s Container corruption detected by %s:%u!\n
%s:%d: Invalid free count for non allocated chunk %u != %u\n
%s:%d: %s container block size too small for device block size (%d < %d)\n
apfs-clonegroup-lock-mutex
spaceman_cib_sanity_check
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
%s:%d: failed to get free extent info from spaceman, error = %d\n
apfs-flags-lock
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
%s:%d: %s unable allocate space that should be there: %d\n
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
nx-volume_group-lock
%s:%d: failed to annotate encrypted meta extents (fsoid = %lld, omapaddr = %lld, omaptreepaddr = %lld), error %d\n
SYSTEM_GRAFT_4K_OBJS
clear
spaceman_ip_block_alloc
%s:%d: failed to init extended fields on drec %lld from blob.\n
lookup_jobj_ext
detach
%s:%d: Internal error: failed memory allocation\n
> write_band bundle=\"%s\" band_num=%llu offset=%lld size=%llu\n
/dev/
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
spaceman_alloc
%s:%d: %s reap list object free list erroneously empty?\n
Launching 'hdiutil' failed %d, or creation of '%s' failed %d\n
> data binary %lld\n
%02hhx
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
btree_node_insert
APFS_INODES
BSD Name
spaceman_checkpoint_traverse
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
%s:%d: %s xid %lld validation failed for checkpoint at index %d: %d\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
_fd_dev_write
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s block size %d is not an even multiple of device block size %d\n
%s:%d: %s checkpoint mapping (%d,%d) extends beyond checkpoint data range: %d,%d\n
%s:%d: Get parent object failed (error %d)\n
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<dict>\n\t<key>CFBundleInfoDictionaryVersion</key>\n\t<string>6
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
btree_check_recent_sanity
btree_node_val_range_validate
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
%s:%d: %s obj_modify() failed: %d\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
%s:%d: failed to seek/write to image file fd #%d, error %d\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
%s:%d: %s omap check failed for omap %lld: %d\n
nx_check_recent_sanity_omap
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
spaceman_clear_bits_in_bm
usage
-fs
set-decrypt
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
obj_create_internal
%s:%d: Either '-G' was not set, or multiple '-O' defined\n
%s:%d: Shrinking the container to the exact size (%lld)\n
%s:%d: %s Error reinitializing free extent cache: %d\n
%s/apfs
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
obj_checkpoint_start
rolling-stats-lock
%s:%d: %s xid %lld failed to get spaceman: %d\n
%s:%d: %s failed to create reap list: %d\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
btree_node_sanity_check
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
%s:%d: %s couldn't read superblock of size %d\n
create_slurper_context
apfs-incompat-features-lock
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
nx_corruption_detected_int
%s:%d: can't get features for device (%s)\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
jfs_get_tree_in_snap
spaceman_ip_freed
%s:%d: volume %s does not belong to the same container %s\n
%s:%d: Invalid arguments:\n
hdiutil
%s:%d: Failed to get IO registry entry for given device path %s\n
create
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
%llu
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
spaceman_cab_sanity_check
make_large_jkey_header_from_jobj
%s:%d: %s failed to get reap list object oid %lld: %d\n
%s:%d: Failed to launch '%s %s %s' (error %d)\n
/dev/r%s
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
sealed, fext, req_tree != fs_root
obj_checkpoint_known
%s:%d: %s couldn't read checkpoint descriptor block %d @ %lld: %d\n
%s:%d: %s xid %lld at index %d failed to load checkpoint metadata ranges (overlap?): %d\n
> update_progress progress=%d current_blocks=%llu total_blocks=%llu\n
\n
apfs-dir-size-lock
%s:%d: %s lookup_next_snapshot() returned %d\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
obj_delete_and_free_by_oid
invalid tweak type %d\n
%s:%d: %s couldn't read checkpoint descriptor block %d @ 0x%llx: %d\n
btree_node_reap
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s error getting cab %d @ %lld: %d\n
omap_recent_sanity_callback
%s:%d: %s spawn error %d\n
%s:%d: %s node 0x%llx (level %d) index %d: more levels than expected\n
bt_remove_internal
spaceman_ip_bm_block_alloc
skip_fs_meta_blocks
%s:%d: Invalid or unknown hash type: %d\n
btree rightmost leaf mismatch! (expected %lld found %lld)\n
omap_destroy
%s:%d: %s failed to get omap tree for reaping: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
/usr/bin/hdiutil
spaceman_chunk_zone_info_compare
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s unexpected checkpoint map entry address: 0x%llx, expected 0x%llx\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
nx-omap-lock
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
omap_reap
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
spaceman_alloc_fxc_scan_wait
obj_read
%s:%d: %s xid %lld failed to load spaceman metadata ranges (overlap?): %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
apfs-pfkur-tree-oid-lock
btree rightmost leaf field is set for physical tree!\n
%s:%d: %s reverting on error: %d\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
nx_reaper_add_sub_object
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
Target Disk Mode
%s:%d: failed to read (block #%lld, len #%lld), error %d\n
write_extents_to_output
write_bitmaps_extents
Overw
%s:%d: %s iter_next returned %d\n
%lld
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
apfs_free_data_blocks
%s:%d: failed to load nx layer and object cache, error = %d\n
%s:%d: failed to write metadata to sparsebundle, error %d\n
container_find_and_unlock_encrypted_volumes
w
bt_insert
dev_init_common
%s:%d: failed to open band file %llx, error %d\n
%s:%d: %s  %sriting the blocks of fs %d using its decryption info\n\n
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n
%s:%d: Failed to create password data reference for %s\n
-size
handle_fs_data_extents
authapfs_integrity_meta_get_internal
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
IOService
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
%s:%d:   -g : <dmg sparse image> output the slurped data to the specified simple disk image\n
%s:%d:   -r : <raw dev> output the slurped data to the raw device representing a container\n
%s:%d: Resizing container down to %lld failed %d\n
apfs-stream-id-lock
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
%s:%d: %s node 0x%llx (level %d): error getting index %d child oid: %d\n
btree_node_insert_internal
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: Usage: %s -d <disk> [-m <apfs mount path>] [-o <output directory>]\n
%s/apfs_data
omap_find_next_snapshot_xid
object-cache-lock
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
%s:%d: %s xid %lld data for checkpoint at index %d couldn't be loaded: %d\n
spaceman_chunk_zone_info_add
%s:%d: %s Failed to get next extent: %d\n
BSD Major
AppleAPFSVolume
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
spaceman_chunk_zone_info_recent_decrement
%s:%d: %s removal of replaced free extent failed: %d\n
jobj_allocate
%s:%d: invalid object size: %d size_phys %d\n
spaceman_fxc_tree_node_recycle_smallest
nx_check_recent_sanity
btree_node_child_id_update
nx_checkpoint_traverse
%s:%d:   -G : <dmg sparse image> output the slurped data to an existing simple disk image\n
%s:%d: offset '%s' is not a number!\n
%s%llu%-*.*s %cB%s
%s:%d: Container corruption detected by %s:%u!\n
%s:%d: failed to read BITMAP %lld error=%d\n
Reference count overflowed for object %p!\n
%s:%d:        if -s is specified, only a single -o may be used\n
d:o:g:G:O:svtTUp:
```
