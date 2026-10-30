# `/System/Library/Filesystems/apfs.fs/hfs_convert`

From the upgrade restore ramdisk (141-29011-104.dmg). 611,120 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2648)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (9)

- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit (compatibility version 302.0.0, current version 944.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
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

## Strings (1,820)

```
base64EncodedStringWithOptions:
UTF8String
dataWithBytes:length:
length
%s:%d: failed: cksum 0x%016llx, oid 0x%llx, type 0x%x/0x%x, size %d\n
--verbose: invalid argument: %s
%llu%s
Error %d freeing blocks for Catalog B-tree\n
%s:%d: %s Failed to find next smallest extent in length tree: %d\n
%s:%d: inserting bad phy ext @ %p : kind %d refcnt %d\n
apfs_is_volume_role_allowed
Unable to find LwVM extent for logical offset %lld
authapfs_integrity_meta_get_internal
Usage: apfs_hfs_convert [-D] [-e] [-v] [-s] [-S <path>] [-n] [-F n] [-M <mount_path>] [-o <option>] <device_path>\n
    %'llu bytes\n    %'llu free (%llu%%) before conversion\n
nx-tree-node-compact-lock
%s:%d: %s failed to initialize cib %d: %d\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with other entries\n
obj_delete_and_free_by_oid
parameters
    %'llu bytes allocated by HFS\n
spaceman_free_extent_cache_insert
levels: %d  keys: %lld  nodes: total %d  internal: %d (%.2f%%)  leaves: %d (%.2f%%)  usage: %.2f%% (%.2f%% %.2f%%)\n
7C3457EF-0000-11AA-AA11-00306543ECAC
ba=%lld 
du
%s:%d: %s Failing with error=%d\n
%s:%d: %s failed to restore orig_fext, ino %llu, pbn 0x%llx, laddr 0x%llx, len %llu, crypto_id %llu, error %d\n
PRECONVSTAT
%s:%d: %s oid %lld flags 0x%llx 0x%x refs 0x%llx taking too long to get reference!\n
\t%16p %s\n
%s:%d: %s oid 0x%llx (level %d): node's max key is not less than next sibling's entry in parent\n
  values: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s File extent too large (%llu > %llu): laddr %llu, paddr %llu\n
ino-io-lock
n_h=%lld 
%s:%d: %s spaceman checkpoint %s traverse failed: %d\n
%s:%d: %s chunk %lld recent zone count zero but still marked as current\n
defragment=no
61706673-7575-6964-00c0-766f6c756d00
%.24s: Entering a transaction for compaction\n
%s:%d: error: block size %d is not an even multiple of device block size %d\n
%s:%d: %s btree_node_key_update failed: %d\n
Object has no address: o %p oid %llu flags 0x%llx 0x%x paddr %llu naddr %llu\n
com.apple.hfs.dir-link
Journal is not empty!  Continuing (but not freeing journal).
%s:%d: %s large key size (%u) on record (%llu) is too small\n
sha3_256_4k
btree_iterate_nodes
%s:%d: %s Cannot find extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: Volume role 0x%x is not allowed for an unencrypted volume\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old location %d\n
Product Name
sf=%lld 
Error %d inserting hard link inode cnid=%u\n
%s:%d: %s FS will NOT be encrypted.\n
nx_reaper_wait returned an error: %d\n
%s:%d: %s Failed to delete supplemental tree (type %d): %d (%s)\n
%s:%d: %s Error: tx[%lld] failed to start: %d\n
kind == NEW && refcnt = %d\n
object-cache-flush-lock
61706673-7575-6964-0000-766f6c756d00
Product Revision Level
    uuid = %s\n
%s:%d: %s lookup_next_snapshot() returned %d\n
spaceman_upgrade_sm_version_0_to_1
61706673-7575-6964-0200-766f6c756d00
m
%s:%d: %s oid 0x%llx (level %d): table space length larger than available data space\n
spaceman_get_metazone_alloc_index
stats
postV
Cannot convert HFS volumes with directory hard links.\n
doc_id_tree_destroy
%s:%d: Sparse bytes removed from inode %lld internal flags: 0x%llx iflags 0x%llx, new_sparse_bytes %lld; name %s parent-id %lld), but it wasn't marked sparse.\n
%s:%d: %s unable to get fs object 0x%llx: %d\n
nx_reaper_obj_get
spaceman_trim_free_extent_callback
%s:%d: %s oid 0x%llx (level %d): val size greater than longest recorded for tree\n
icp_dec_ref
extent overlaps nx reserved space, fragmented %d
Error %d freeing blocks for journal info block\n
%s:%d: %s tx_enter_frozen() failed: %d\n
%s:%d: failed to write superblock to block 0: %d - %s\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/hfs_stream.c
%s:%d: %s oid 0x%llx (level %d): index %d val length %d longer than tree longest %d\n
owners
Cannot convert.
btree_node_reap
can't have a negative refcnt on crypto state %llu refcnt %d\n
%s:%d: %s file system %lld fs reserve block count %lld larger than global fs reserve block count %lld\n
%s:%d: %s failed to allocate block from internal pool: %d\n
%s:%d: %s expanded records are now supported\n
MKCFWriteMedia failed: %d
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error deleting mapping %d\n
spaceman_ip_freed
%s:%d: %s xid %lld checkpoint data block count is larger than expected: %d > %d\n
rmdir
sz=%lld 
%s:%d: %s failed to update allocate zone %llu: error %d\n
Journal info block length is unexpected (%u allocation blocks)
apfs-im-cache-lock
fs_get_inode_with_hint
%s:%d: %s failed inserting hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
attr tag
xml-report
/dev/rdisk%s
diskutil list
%s:%d: %s ino %llu is flagged to maintain dir-stats but has no dir-stats key\n
%s:%d: %s invalid zero len, paddr %llu\n
nx_tx_finish_wait_for_dirty_data
%s (%s)
fs_is_content_protected(apfs)
userquota
%s:%d: %s Failed to get fsys oid %lld - %s\n
\t\t<array>\n
not handling the current tx!\n
%s:%d: %s Would have attempted to create an entry with kind == NEW and refcnt == %d! (flags=0x%x, existing val len_and_kind=0x%llx owning_obj_id=%llu refcnt=%d)\n
%s:%d: %s ***: expanded obj type found on unsupported volume\n
spaceman_check_allocation_status_internal
    %'9u symlinks\n
%s:%d: %s oid 0x%llx (level %d): val entry overlaps with free space\n
Error %d getting record #%u of node %llu\n
hfs_find_free_blocks: found_start=%lld\n
bt_lookup_copy_out
nx_tx_flush_busy
%s:%d: %s tx xid %lld was closed for %lld us waiting to prepare to flush\n
%.24s: Updating the superblock\n
bt_update_last_leaf
fs_write_stream
spaceman_chunk_zone_info_recent_increment
logical_to_physical: error %d\n
%s:%d: %s Couldn't find snapshot metadata for xid %llu\n
physical object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
Invalid EA %s\n
tree_node_count for current fsroot tree failed \n
\t\t</array>\n
%.24s: Iterating over fsroot tree records\n
%s:%d: %s Trying to delete space for extent %lld %lld which has invalid owning_obj_id %lld\n
BSD Major
%.24s: Writing superblock\n
LwVM: media block size too small
%s:%d: %s error reaping object 0x%llx of type 0x%x: %d\n
case=insensitive
device fd
%s:%d: %s failed to serialize ino %lld into jval of size %u\n
modification
%s:%d: %s unknown expanded type (%hhu) on record (%u)\n
omap=btree
spaceman_fs_bounds_set
Error %d freeing blocks for Attributes B-tree\n
%7d  %8d  %6d\n
%s:%d: %s failed to serialize dir-stats %lld into jval of size %u\n
icp_new_crypto
Free extents (count = %d)\n
obj-id %llu type %u still has refcount %d\n
%s:%d: %s Attempted to %s range %llu+%llu but it isn't entirely there! (found gap at %llu, next range at %llu+%llu)\n
cannot migrate preboot in unified dev_t\n
%s:%d: %s unsupported tree type, %d\n
\t<dict>\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error unreserving space on non-dirty release: %d\n
%s:%d: hash mismatch! expected: %s, actual: %s\n
hfs_insert_object: could not set DREC_EXT_TYPE_SIBLING_ID (error %d)\n
%s:%d: %s failed to get reaper for checkpoint %s traverse: %d\n
is_APFS: error %d reading superblock\n
%s:%d: %s fext tree type 0x%x invalid, using physical btree instead\n
defragment=yes
%s:%d: Container corruption detected by %s:%u!\n
1
volumename
%s:%d: %s Trash unfinished pending tx, xid range = 0x%llx - 0x%llx\n
hfs_insert_extents
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj.c
%s:%d: %s Cannot make large jkey from unknown type %d (obj_id %llu)\n
%s:%d: %s failed to create reap list: %d\n
spaceman_chunk_zone_info_load_recent_chunks
    Limiting conversion to %ld seconds.  Use --watchdog=0 for no limit.\n
extent is freed more than once, or hfs has overlapping extents
%s:%d: %s %s tree: PATH TOO LONG: %d\n
%s:%d: %s failed to finish writing to obj-id %lld (pos %lld / new_size %lld)\n
Physical Interconnect Location
es=%lld\n
%s:%d: %s oid 0x%llx (level %d): couldn't allocate bitmap to check btree node space usage\n
capacity: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
hfs_convert_msg_number
%s:%d: %s removal of replaced free extent failed: %d\n
authapfs_integrity_meta_create
com.apple.FinderInfo
hfs_stream_create() failed: %d\n
spaceman_free_extent_cache_setup
apfs-snap-delete-lock
unhashed
%s:%d: %s %s: could not insert inode obj-id %lld (name: %s)\n
    -e    Estimate apfs metadata size.\n
Journal file is missing!
%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/lwvm.c
------------------
omap=physical
jobj_allocate
hfs_extents_iter_b() failed: %d\n
%s:%d: %s oid 0x%llx (level %d): tree says kv sizes are fixed, but leaf says kv size is variable\n
%s:%d: %s got err %d writing at pos %lld in obj-id %lld (blkcount %llu, len %zd)\n
%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n
%s:%d: %s lookup returned unexpected error while iterating: %d\n
%s:%d: %s xid %lld failed to write last checkpoint map block %lld: %d\n
eu=%lld 
failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
%u
total size
nx-omap-lock
obj_release
%s:%d: %s oid 0x%llx (level %d): invalid TOC[] pointer\n
%s:%d: %s failed to enter tx to update size tracking for ino %llu: %s (%d); size tracking may go out of sync\n
%s:%d: unknown expanded type (%hhu) on record (%u)\n
    %'llu bytes used by conversion\n
%.24s: Converting catalog B-tree\n
obj_cache_lock_by_state, invalid oc_lock_state %d\n
%s:%d: %s unable to create chunk zone info cache scan lock: %d\n
kern.osversion
%s:%d: %s failed to fetch the integrity object (error %d)\n
%s:%d: %s failed to fetch the pfkur tree (error %d)\n
%s:%d: %s failed to write checkpoint data block %lld: %d\n
Journal is not contiguous
hfs_insert_object: poison check failure\n
apfs_mount failed with error: %d\n
%s:%d: %s failed to get omap for checkpoint %s traverse: %d\n
%s:%d: %s error getting next checkpoint map block address %d: %d\n
r=%d 
Unable to start a new transaction due to error: %d\n
.journal
update-gpt
Opening %s read/write to trigger re-probe\n
Error %d updating apfs allocated blocks\n
capacity: leaves %llu / %llu => %.2f %% used\n
apfs_mount
%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n
get_vol_crypto(apfs) == VOL_PFKEY
%s:%d: *** Unknown file info type %llu\n
compactBtree
jfs_get_tree failed with error %d\n
%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n
%s:%d: %s Couldn't remove extent at pbn %llu, err=%d\n
/dev/disk
    Volume name: %s\n
    %'9u extent-based EA overflow records\n
apfs-phys-ext-oid-lock
btree rightmost leaf field is set for physical tree!\n
%s:%d: *** Can't release unknown obj type %d\n
%s:%d: %s failed to get fs[%d] oid %lld for checkpoint %s traverse: %d\n
          Print statistics and information about the converson to the given <path>.\n
          Preboot volume will be created and filled with the contents of the preboot directory.\n
unmount
%s:%d: %s Failed to update partially-covered node in length tree: %d\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says val size is variable\n
Size
postConvStats
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error freeing space %d\n
pi
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n
obj_write_prepare
sz_ssd=%lld 
%s:%d: %s reserved space underflow: %lld (+meta:%llu) < %lld\n
%s:%d: %s supplemental_tree_destroy(pfkur_tree) failed: %d (%s)\n
Container
%s:%d: %s xid %lld sync/barrier failed: %d\n
        %'9u class E\n
Content protection EA for cnid=%u is too short.  Conversion failed!\n
%s:%d: %s skip bad chunk info ci @ block %lld (cib %lld) ci_index 0x%x ci_addr 0x%llx (expect 0x%llx)\n
%s:%d: %s spaceman_free(%lld, %d) failed: %d\n
Unable to create watchdog timer!
hfs_bitmap_read_le failed with error %d\n
  inserting ID=%llu name=%.*s\n
%.24s: Waiting for reaper to finish\n
Journal size is inconsistent (file=0x%llx, jib=0x%llx)
Can't find inode number for iNode%d\n
insert_apfs_sibling_record: can't allocate sibling value\n
%.24s: Converting attributes B-tree\n
%s:%d: %s failed to delete fs snap metadata tree after fs creation failed: %d\n
61706673-7575-6964-0080-766f6c756d00
apfs-dir-stats-id-lock
%s:%d: %s %s: could not insert dir rec for obj-id %lld (name: %s)\n
make_large_jkey_header_from_jobj
obj_cache_remove
blocksize=
es
%.24s: Converting slice #%u\n
%s:%d: %s key size (%zu) on clone mapping (%llu) is too small\n
<integer>%d</integer>\n
%s:%d: %s completed cleaning snapshot %lld, om_snap_count %d om_most_recent_snap %lld\n
%s:%d: %s Found enough data to allocate outside the soft block-out range, re-enable soft block-out range\n
prl
spaceman_fxc_tree_node_recycle_smallest
fs_tx_leave_ext
Reserved space < reserved metadata: %llu < %llu\n
%s:%d: %s %s: could not remove inode obj-id %lld (name: %s)\n
%s:%d: %s fs extentref tree creation failed: %d\n
    %'llu bytes free (%llu%%)\n
spaceman_free_extent_cache_remove
%s:%d: %s Volume inconsistency detected by %s:%u!\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error getting mapping to write %d\n
insert_apfs_sibling_record: error %d inserting sibling map record (inode=%llu, link=%llu)\n
%s:%d: %s %s: could not update parent obj-id %lld on create of obj-id %lld (name: %s)\n
%s:%d: %s Warning: attempting to place unknown expanded type %hhu into fsroot.\n
com.apple.fs.altlink
Unable to read symlink offset=%llu length=%zu error=%d\n
 %02x
duplicate_jobj_op_to_shadow_fs_root
chunkSize   = %u (0x%x)\n
%s:%d: %s level %d node 0x%llx index %d: more levels than expected\n
%s:%d: %s xid %lld checkpoint data block count is not value tracked by cache: %d != %d\n
%.24s: Converting device at %s
%s:%d: %s %s overflowed on %s <%llu> %s %llu (delta: %lld)\n
overwriting backup LwVM header: wrote %zd expected %u
GPT
Error %d initializing stream for ID=%u\n
make_jkey_from_jobj
%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n
obj_cache_unlock_by_state, invalid oc_lock_state %d\n
spaceman_metazone_init
encrypted
%s:%d: %s obj_modify(fs %lld) failed: %d\n
%s:%d: %s value size (%zu) on purgeable tombstone (%llu) is too small\n
%s:%d: object cache bootstrap failed: %d - %s\n
Error %d freeing blocks for large extended attributes\n
%s:%d: %s Couldn't insert extent, err=%d\n
reading LwVM header
%s:%d: %s oid 0x%llx flags 0x%x type 0x%x error getting mapping to free %d\n
%s:%d: %s oid 0x%llx (level %d): key free list space larger than key space available\n
spaceman_free_fs_deduct_block_counts
hbf
%s:%d: %s oid 0x%llx (level %d): key free list entry len value too small\n
jdev_fext_write_data() corrupts encrypted data
n_d
%s:%d: %s expanded record found on unsupported volume\n
nx_tx_finish_wait
sz
_dev_flush:fsync(crypto_fd %d)
!apfs->apfs_readonly
%s:%d: tx_enter for initialization failed: %d - %s\n
%s:%d: %s *** failed to set rdev as an extended field of ino %lld (ret %d)\n
%s:%d: %s failed to get next physical extent, error %s(%d)\n
%s:%d: %s failed to delete fs root tree after fs creation failed: %d\n
obj_checkpoint_done
%s:%d: %s xid %lld error preparing to flush object cache: %d\n
v8@?0
i32@?0r^{HFSPlusCatalogKey=SI{HFSUniStr255=S[255S]}}8r^(HFSPlusCatalogRecord=s{HFSPlusCatalogFile=sSIIIIIII{HFSPlusBSDInfo=IICCS(?=III)}{FndrFileInfo=IIS{?=ss}s}{FndrOpaqueInfo=[16c]}II{HFSPlusForkData=QII[8{HFSPlusExtentDescriptor=II}]}{HF
%s:%d: spaceman initialization failed: %d - %s\n
tx_mgr_free_tx
3288.52.1
Physical Interconnect
cache_flush: Error %d from pwrite(fd=%s, size=0x%zx, offset=0x%llx), blk_count=%lld\n
%s:%d: %s Failed to create supplemental tree (type %d): %d\n
-------------------------
tx_enter_internal
%s:%d: %s waiting for available tx to open: xid %lld\n
Warning: dev_read_data called for addr=%lld, count=%zu\n
bitmap
apfs_is_volume_fsindex_allowed
could not load parent_id %lld to fixup its nchildren (dir-hardlink id %d)\n
%s:%d: %s oid 0x%llx (level %d): invalid vals[] pointer\n
\t</dict>\n
physical object dirty count underflow\n
%s:%d: object memory manager failed to create lock, error: %d\n
spaceman-ip-lock
fs_obj_create_name_checked
obj_cache_remove_reverted_fs_objects
eu
AppleAPFSContainerScheme
virtual object dirty count underflow\n
invalid slice: %s
%s\n
%s:%d: %s updating grandparent failed w/%d\n
%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n
%s:%d: %s overprovisioning volume can only mount r/o\n
Executing %s (version %s).
%s:%d: wrlock == 0 failed %d\n
spaceman_free_extent_cache_reset
bt_remove_internal
%s:%d: %s failed to upgrade spaceman from version 0 to 1: %d\n
%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n
nu
%s:%d: %s failed to update rightmost leaf field: %d\n
rdonly
close(crypto_fd)
%s:%d: %s bt_move_entries() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: %s size (%d) of FILE_INFO_TAG_EXT_TYPE_SIGNING_ID in attribution tag record with s_hash <%llu> <= 0 \n
sanity_check_alloced_blocks
nx_reaper_checkpoint_traverse
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error setting mapping for write %d\n
          Use the given path to mount APFS during conversion.\n
%.24s: Spaceman free queue count %llu\n
-C
%s:%d: %s apfs_update_phys_range failed, err = %d\n
object to be freed is on a list, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx list %p/%p\n
Error %d trying to overwrite alternate volume header\n
get_vol_crypto(apfs) == VOL_CPROTECTED
%s:%d: Why are we comparing a chunk to itself?\n
Error: dev_read_extended with flags 0x%x is not supported\n
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be free: %d\n
%.24s: Done\n
apfs-integrity-meta-lock
vmt
Error %d creating stream for B-tree (ID=%u)\n
%s:%d: %s minkey update traversal unexpectedly found the removed key in level 1 node; oid %llu subtype 0x%x level %d\n
!(ino->iflags & (JI_RAW_ENCRYPTED))
hash=
    --preboot=<preboot directory full path>\n
%s:%d: %s failed to leave tx, error %d\n
%s:%d: %s s_hash <%llu> finfo attribution tag value <%zu> is less than sizeof(j_file_attribution_tag_val_t) <%lu\n
BSD Minor
%s:%d: cp_os_version: unable to parse osversion `%s'\n
setup_demo_mode
jdev_fext_write_data
%s:%d: %s could not alloc %zd bytes @ pos %lld for obj-id %lld (err %d)\n
obj_cache_flush_write
        %'9u class 0\n
hfs_read() failed: %d\n
%s:%d: %s iter_next returned %d\n
%s:%d: %s cannot insert file extent record for extent of %lld bytes at offset %lld of data stream %lld in transaction %lld: %s(%d)\n
%s:%d: %s error removing coalesced extent from metadata ranges tree: %d\n
%s:%d: %s obj_modify() failed: %d\n
    --watchdog=<seconds>\n
mount_apfs exit status %d
%s:%d: %s level %d node 0x%llx: error getting index %d child oid: %d\n
%s:%d: %s unable to mount livefs as volume is restoring or mounted\n
Allocated %s object with OID %lld flags %llx type %x %d from\n
spaceman_alloc
%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond val space available\n
%s:%d: ***: unknown obj type %d\n
\t\t<key>%s</key>\n
%s:%d: %s Error: tx[%lld] failed to unclean superblock: %d\n
%s:%d: %s unable allocate space that should be there: %d\n
hfs_insert_object: could not initialize extended fields (error %d)\n
%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n
omap_expunge_oids_below_watermark
/sbin/mount_apfs
Offset
%s:%d: failed to get spaceman: %d\n
%s:%d: %s chunk %lld recent zone count overflow\n
apfs_update_phys_range
spaceman_alloc_fxc_scan_wait
btree_check_ext
POSTCONVSTAT
%s:%d: %s sfq %d error removing entry %lld %lld from free queue: %d\n
nx_reaper_add_sub_object
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error getting mapping to free %d\n
    apfs_encrypted = true
%s:%d: %s unable to create chunk zone info cache lock: %d\n
61706673-7575-6964-0240-766f6c756d00
          efi driver will be embedded in the nx superblock.\n
zero_tail_of_last_block
LwVM: media too large
%s:%d: %s error searching snapshot tree: %d\n
%s:%d: %s remove mapping (%lld, %lld) below watermark failed: %d\n
ca
reference
bad object type in flush list: oid %lld flags 0x%llx 0x%x\n
tu=%lld 
%s:%d: %s Invalid reap list free entry %d\n
fp
apfs_release_objects
%s:%d: %s oid 0x%llx (level %d): minkey not correct\n
%s:%d: %s Cannot start transaction with XID %lld: %s(%d)\n
%s:%d: %s %llu blocks are already reserved in container, Cannot reserve more than %llu blocks in the container\n
btree_node_copy
obj_cache_flush_prepare
m=%lld 
=%d
%s:%d: %s failed to delete doc-id tree, error %d\n
SYSTEM_GRAFT_4K_OBJS
START
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error writing: %d\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with free space\n
unified_devt disallowed for multiple volume conversion\n
%.24s: Creating empty apfs file system\n
btree_node_entry_update
crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n
key_val_to_jobj
%s:%d: %s Unexpected unwritten extent for offset %lld of data stream %lld in inode %lld\n
spaceman-space-usage-lock
Can't initialize catalog iterator!  (Error %d)\n
Out of memory
hfs_insert_object: could not serialize extended fields (error %d)\n
Warning: dev_write_data called for addr=%lld, count=%zu\n
verbose
dr
%s:%d: %s Failed to find smallest extent in paddr tree: %d\n
%s:%d: %s unable to reclaim just-freed val space on error path: %d\n
dirty object flush state inconsistent: oid %lld flags 0x%llx 0x%x fl %p\n
/var/tmp/
    %'9u inline EAs\n
spaceman_fs_bounds_clear
close(hfs[%u])
hfs_read(bitmap)
%s:%d: *** Can't allocate unknown obj type %d\n
    -S <path>\n
!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))
uid=
%s:%d: %s Bogus attempt to perform non-metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
%s:%d: %s xid %lld failed to write checkpoint superblock %lld: %d\n
skip-single-dirlinks
%s:%d: %s created doc-id tree, oid %llu\n
%s:%d: %s btree_node_insert_internal failed: %d\n
%s:%d: %s spaceman_alloc() FAILED, err: %d xid: %lld paddr: %lld blocks requested: %lld blocks allocated: %lld\n
%s:%d: *** unknown obj type %d\n
fs_update_unwritten_extent_record
    -n    Don't finalize conversion (dry run).  Volume remains HFS.\n
cst %llu hit zero retain count but still has ep related retain count (%u)\n
Chunk  Part  Index
en_US.UTF-8
hfs_stream_dispose() failed: %d\n
%s:%d: %s failed to free allocated blocks, ino %llu, 0x%llx+%llu, error %d\n
Target Disk Mode
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
%s:%d: %s sfq %d entry %lld:%lld %lld - bad xid, current xid %lld\n
n_ea=%lld 
n_s
val_size_for_jobj
spaceman_chunk_zone_info_cache_init
exec
d100=%ld 
insert_jobj
jobj_type_from_possibly_large_key
update_sparse_bytes
Extents for slice #%d (count = %d)\n
\t\t<key>%s</key> <string>%s</string>\n
%s:%d: unlock == 0 failed %d\n
    -s    Force the APFS volume to be case-sensitive.\n
fcntl(crypto_fd,F_FULLFSYNC)
%s:%d: %s oid 0x%llx (level %d): invalid key offset\n
%s:%d: Failed to remove sparse bytes attribute from ino %lld, but it was successfully got, errro %d\n
%s:%d: Volume role %d is not allowed at fs index %d\n
%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n
dev_barrier: Error %d\n
%.24s: appears to be APFS.  Skipping conversion.\n
.HFS+ Private Directory Data\r
btree_node_child_id_update
%s:%d: Unknown subtype %d for file info object %lld\n
Requested forced secondary_fs_root but the tree is missing\n
path
unwritten=no
%s:%d: reaper initialization failed: %d - %s\n
61706673-7575-6964-0040-766f6c756d00
%s:%d: %s minkey update traversal unexpectedly found the key (%d) or a non-zero index (%d); oid %llu subtype 0x%x level %d\n
%s:%d: %s error adding child 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s failed to serialize file info with obj_id <%lld> into jval of size <%u>\n
addition
update_file_extent
ino_set_rage
%s:%d: %s Tree iteration threw %d at cursor %llu\n
  inserting ID=%llu EA=%s [%llu bytes] ea_id=%llu\n
%s:%d: %s oid 0x%llx (level %d): node level should be %d\n
%s:%d: %s Bogus attempt to perform metadata reserved allocation %lld with insufficient reserve %lld (%lld)\n
supplemental_tree_create
tx_leave failed with error: %d\n
<60
%s:%d: %s Tree delete oid %llu threw %d\n
    -v    Enable verbose output.\n
Unable to create a new fs_root tree due to error: %d\n
%s:%d: %s oid 0x%llx (level %d): node says kv size is fixed, but tree says key size is variable\n
role=
Unable to insert symlink cnid=%llu error=%d\n
Error: dev_write_extended with flags 0x%x is not supported\n
%s fd=%d
%s:%d: %s unable to get object 0x%llx of type 0x%x: %d\n
Invalid inode filename: %.*s\n
HFS has too many files for unified dev_t conversion \n
apfs-fext-tree-oid-lock
<80
fsindex=
apfs-doc-id-lock
obj_destroy_complete
spaceman-czic-scan-lock
    -x\t   Changes standard output to contain statistics in XML format. All error messages and non statistics output is redirected to /var/log/hfs_convert.log\n
au
bt_merge_nodes
%s:%d: %s failed to destroy omap after fs creation failed: %d\n
%s:%d: %s failed to remove tail_fext, ino %llu, laddr 0x%llx, error %d\n
fs_is_phys_range_writable
nx_reaper_add_ext
union
Closing HFS fd=%d\n
btree_node_check
exp_dir_stats_refcnt_merge
%s:%d: %s can't get spaceman %d free queue tree %lld: %d\n
61706673-7575-6964-0001-766f6c756d00
%s:%d: %s attempt to free extent (0x%llx:0x%llx) which should not be freed: %d\n
%.24s: Unmounting APFS volumes\n
update_dir_stats_by_key_ext
num children
physical object new address mismatch: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx naddr 0x%llx 0x%llx\n
nx_tx_wait_open
true
%s:%d: %s existing file system (slot %d)\n
Invalid number of devices
%s:%d: %s oid 0x%llx (level %d): key %d compare error: %d\n
%s:%d: %s request to insert entry %d (%d) %d (%d) = (%d), max size is %d key %d, error %d\n
spaceman-dev-lock
%d %%
%s:%d: %s failed to checkpoint %s traverse test object 0x%llx of type 0x%x/0x%x: %d\n
%s:%d: %s failed to load the integrity object - %s(%d)\n
move_snapshot_to_purgatory
    %'9u crypto state records\n
doc_id_tree_invalid_crypto
extents_tree
%s:%d: %s fs omap initialization failed: %d\n
resource fork size
Writable
Device Characteristics
hexdump of file name that failed to convert:
lookup_jobj_ext
%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n
FAIL
\t\t<key>%s</key> <integer>%u</integer>\n
<dict><key>%s</key> <string>%s</string></dict>\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error destroying: %d\n
fs_rename_snapshot
hfs_convert_attributes_tree: unexpected record type (%u), skipping\n
%s:%d: %s snapmeta tree type 0x%x invalid, using physical btree instead\n
/var/tmp/RecoveryTemp/
Journal info block is not contiguous
Unmounting APFS conversion mount
dev_close:cache_flush
%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n
DELETE
%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n
hfs_find_free_blocks: wanted=%lld blocks (%llu bytes)\n
%s:%d: tx_leave for omap initialization failed: %d - %s\n
%s:%d: %s checkpoint area out of space: stable: %d %d - next %d %d available %d %d tx[%lld] %d %d\n
aa
slice %u: Bad volume name!  (Error %d)\n
%s:%d: %s unable to reclaim just-freed key space on error path: %d\n
%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n
insert_phys_extent
%s:%d: object memory manager initialized with feature flags: 0x%x, apfs_mem_max: %lld\n
nx_tx_wait_frozen
%s:%d: %s waited %lld us to open tx xid %lld (%s)\n
%s:%d: %s ***: expanded type seen on in-memory obj!\n
Error %d freeing blocks for volume bitmap\n
%02X 
update_size_tracking
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/obj.c
%s:%d: %s rapid-aged %llu inodes\n
Attempting to reuse a non-candidate chunk zone info\n
%s:%d: %s deletion threw %d for cursor %llu, oid %llu, oflags 0x%x\n
    -f    Force conversion if volume is dirty.\n
hfs_update_apfs_alloc
<plist version=\"1.0\">\n
d
%'ld max resident set size\n
fcntl(crypto_fd,F_BARRIERFSYNC)
<UNKNOWN>
spaceman_iterate_free_extents_internal
obj_modify returned an error: %d\n
automounted
spaceman_free_completed
can't transition from tx flags 0x%x to 0x%x (expected 0x%x)\n
%.24s: obj_id of current fsroot tree (%lld) and that of new fsroot tree (%lld)\n
nx_reaper
Content protection EA for cnid=%u is dirty.  Conversion failed!\n
%s:%d: %s oid 0x%llx (level %d): invalid val offset has non-zero length\n
jdev_fext_read_data
spaceman_init_cab
spaceman_modify_bits
force
ss=%lld 
Error %d freeing symlink cnid=%u\n
%s:%d: %s failed to enter tx, error %d\n
%s:%d: %s error searching spaceman free queue tree: %d\n
re-open/re-probe %s
%s:%d: %s Cannot allocate space for %zu bytes at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s failed to create fs: %d\n
image-format-read-only
aa=%lld 
* * * cannot allocate memory * * *\n
hfs_messages.c
%s:%d: %s Quota %llu is smaller than reserve %llu\n
          Conversion will abort after <seconds> seconds.  Default is 600 seconds for dry run, unlimited otherwise.\n
%s: Cannot determine sector size: %s\n
%s:%d: %s fs creation failed: %d ... cleaning up...\n
%s:%d: %s value size (%zu) on clone mapping (%llu) is too small\n
%s:%d: %s Shadow create_or_modify_jobj(jobj %p id %lld xid %lld op %d) failed with error %d\n
%s:%d: %s Container corruption detected by %s:%u!\n
  inserting inline EA: ID=%u EA=%s [%u bytes]\n
doc_id_tree_create
apfs_checkpoint_traverse
apfs-clonegroup-lock-mutex
obj_modify
%.24s:     Updating %'u symlinks\n
%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n
%s:%d: %s Failed to release reference to crypto ID %lld for data stream %lld: %s(%d)\n
%.24s: Wiping VM metadata and overwriting HFS alternate volume header\n
crypto_cache->type != CRYPTO_OBJ_TYPE_EP
Sections
purgeable rsrc size
%s:%d: %s tx xid %lld took %lld us to flush\n
Dmesngko:xvF:M:S:
%s:%d: %s block range %lld:%lld out of bounds %lld\n
%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n
jfs_get_tree_in_snap
msg != NULL
n_ea
apfs_reap_extentref_blocks
%s:%d: %s ***: expanded type seen on in-memory obj\n
FIXUP
obj_delete_internal
%s:%d: %s error getting mapping tree: %d\n
spaceman_chunk_zone_info_add
%s:%d: %s clone mapping <%llu, %llu>: failed to update attribution tag: %s (%d)\n
Failed to open file
%s:%d: device initialization failed: %d - %s\n
nx_corruption_detected_int
inodelayout
apfs-flags-lock
%s:%d: %s failed to initialize cab %d: %d\n
%s:%d: %s %lld:%lld error: %d\n
%sapfs_hfs_convert.%d
/dev/%s
cu=%lld 
%s:%d: %s Persistent allocation zone at slot %llu has invalid current boundaries\n
unknown
%s:%d: %s omap_destroy returned %d!\n
   
Reference count overflowed for object %p!\n
spaceman_chunk_zone_info_recent_decrement
%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: %s error getting cib %d bitmap %d @ %lld: %d\n
u=%lld
%s:%d: %s failed to get reap list object oid %lld: %d\n
%s:%d: %s failed to get omap snapshot tree for reaping: %d\n
estimate
%s:%d: %s oid 0x%llx (level %d): key free list entry overlaps with other free space\n
%s:%d: invalid object size: %d size_phys %d\n
        %'9u class B\n
%s hfs_to_phys(0x%llx, %d, %lld, %ld) failed
apfs-rename-lock
%s:%d: %s Couldn't rename snap %llx to %s\n
%s address %lld, size %lld is outside stream \"%s\", num_blocks %u, block_size %lld
spaceman_cib_sanity_check
com.apple.ResourceFork
%s:%d: %s integrity_meta object of fs %llu, oid invalid\n
n_s=%lld 
nx_tx_wait
\t\t<key>%s</key> <integer>%s</integer>\n
sf
%.24s: Unmounting the volume\n
%s:%d: %s Failed to delete covered node from length tree: %d\n
%s:%d: failed to insert large EA extent (cnid 0x%x, obj_id 0x%llx, loff 0x%llx). Ignoring the rest of the large EA extents.\n
%s:%d: %s level %d node 0x%llx: error MODIFYING index %d child 0x%llx flags 0x%x: %d\n
btree_node_key_range_validate
MODVAL
Include most
%s:%d: %s BT node sanity check failed for node type %u subtype %u oid %llu with mask 0x%x!\n
apfs_mark_inconsistent_
%s:%d: %s tx xid %lld took %lld us to prepare to flush\n
jobj_refcnt_merge
apfs_reap
btree_node_child_val
__apfs_dec_parent_nlink
%s:%d: %s failed to delete prev doc-id tree, error %d\n
%s:%d: %s failed to delete fs clonegroup tree after fs creation failed: %d\n
suid
Continuing.
%s:%d: %s level %d node 0x%llx: error getting index %d child 0x%llx flags 0x%x: %d\n
----------------------
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error freeing old space @ 0x%llx: %d\n
61706673-7575-6964-02c0-766f6c756d00
IOService
%s:%d: %s ino %lld file extent %lld:%lld extends beyond alloced_size %lld (fsize %lld). fixing it.\n
object-cache-list-lock
full clone size
prevent_synthetic_object_operation
MODKEY
nx-global-extent-manipulation-lock
%s:%d: %s failed to fetch the extentref tree (error %d)\n
hfsPrint
%s:%d: %s op %d error getting cib %d @ %lld: %d\n
hfs_convert_attributes_tree:hfs_btree_scan_b() failed: %d\n
%s:%d: %s btree_node_key_update() failed (%d) while trying to revert changes due to error: %d\n
ciphertext object @ %p can not be dirtied!! (flags: 0x%llx)\n
61706673-7575-6964-0300-766f6c756d00
fs
hbf=%lld\n
        %'9u class A\n
fssize=
.journal_info_block
<100
nx_format
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing space %d\n
recent zone chunk should have only ONE reference when being moved to the recent list!\n
%s:%d: %s refusing to upgrade spaceman! new_smp_size %u old_smp_size %u block_size %u\n
update_jobj
obj_checksum_verify
%s:%d: %s set cloneinfo_id_epoch to %llu\n
--feature-format: invalid argument %s
hfs_volume_init() failed for volume %u (error %d)\n
%s:%d: %s obj_modify failed - %d\n
%s:%d: %s error getting cib %d @ %lld: %d\n
spaceman_fq_tree_find_overlap
dev_close:_dev_flush
%s:%d: %s failed to read cib %d: %d\n
sha384
    -k\t   Change GPT GUID to Apple_KFS during conversion (relevant only for core storage).\n
apfs-omap-lock
%s:%d: %s spaceman fs reserve alloc count underflow: %lld (%lld)\n
xid %lld is not current xid
iterate_raw_jobjs_with_hint failed with error: %d\n
  values: %9s %9s %9s %9s %9s %9s\n
hfs_convert_verbosity
Error %d inserting records for cnid=%u, parent=%llu\n
Creating a normalization-sensitive volume
spaceman-free-lock
Conversion failed!  %s:%d slice=%d phase=%d location=%d error=%d%s\n
update
mount_apfs
hfs_update_root: unable to modify apfs_t\n
Error %d freeing blocks for Extents B-tree\n
%s:%d: %s failed to get doc-id tree, error %d\n
%s:%d: %s failed to clean up doc-id trees, error %d\n
%s:%d: %s freed != alloced (%llu freed, %llu alloced)\n
%s:%d: %s found bogus 0-length extent at lba %llu, ignoring\n
  inserting hard link inode ID=%u\n
hfs_insert_object: name grooming failed (error %d)\n
blocks_in_txn
tx_checkpoint_write
%s:%d: %s bogus phase, %u\n
curproc
%s:%d: %s failed to get spaceman oid %lld for checkpoint %s traverse: %d\n
nx-volume_group-lock
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x dirty object on the free list?!\n
conversion finish_finalize() failed: %d\n
totalChunks = %u\n
force-case-sensitive
n_f
_fs_add_xattr
%s:%d: %s nx reaper checkpoint %s traverse failed: %d\n
Content protection EA for cnid=%u is not inline!  Conversion failed!\n
%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n
ja=%lld 
length
crypto fd
APFS_BTREE_NODES
file
authapfs_validate_node
Attempt to open device by Volume Manager #%d failed, error %d during attempt to open the device\n
%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n
%s:%d: cannot change role of Backup volume\n
%s:%d: %s allocated unwritten file extents are now supported\n
%s:%d: %s failed to wait on reaper: %d\n
%s:%d: %s tx xid %lld took %lld us to close\n
Not an HFS volume? (signature 0x%04x)\n
apfs-stream-id-lock
nx_reaper_wait
ephemeral
%s:%d: %s xid %lld error preparing ephemeral object (oid 0x%llx type 0x%x/0x%x): %d\n
%s:%d: %s error adding btree 0x%llx type 0x%x to reap list: %d\n
%s:%d: %s mount for ramdisk\n
%s:%d: don't know how to merge refcounts on objects of expanded type %d\n
%s:%d: %s could not unwrap crypto-id %lld (err %d)\n
ro
sha3_384
Volume marked inconsistent!  %s\n
%s:%d: %s oid 0x%llx (level %d): val free list space larger than val space available\n
strictatime
61706673-7575-6964-01c0-766f6c756d00
%s:%d: %s xid %lld failed to write checkpoint data @ 0x%llx: %d\n
Can't get resource usage (error %d).\n
Reading journal info block
btree_delete
%s:%d: %s error deleting child 0x%llx type 0x%x: %d\n
fs_map_file_offset_ext
%s:%d: %s Cannot trim extent at offset %lld in inode %lld from %lld to %lld bytes: %s(%d)\n
%s:%d: %s failed to decrement crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
%s:%d: %s spaceman_free(%lld, %lld) failed: %d\n
%s:%d: %s oid 0x%llx (level %d): index %d key length %d longer than tree longest %d\n
%s:%d: %s oid 0x%llx (level %d): val free list head beyond end of node\n
%s:%d: cannot change role of xART volume\n
INSERT
LwVM: media too small
quarantine
%s:%d: %s file system %lld alloc block count is not zero: %lld/%lld\n
root
hfs_convert_msg_type
%s:%d: %s failed to get newnode minkey: %d\n
%s:%d: %s dstream id %llu refcnt %u (delta: %d) would overflow\n
nx-txn-blocks-lock
%s:%d: failed to set up sm allocation metadata: %d\n
%s:%d: %s op %d error getting cab %d @ %lld: %d\n
sealed, fext, req_tree != fs_root
nx_reaper_next_record
%s:%d: %s tried to get metazone alloc index for unknown type: %d\n
Bad EA Name %s\n
%s:%d: %s encryption type %llx unsupported\n
%s:%d: %s unsupported tree type: %d\n
    Offset      Length
failed to write superblock to block 0: %d - %s\n
spaceman_allocation_init
mt
nx_format failed\n
nx_conversion_complete() failed: %d\n
    %'7.3fs (%5.2f%%) system\n
%.24s: Creating a new fsroot tree\n
%.24s: Deleting old fsroot tree\n
flush phase checkpoint lengths (%d %d) don't match prepare phase (%d %d)\n
invalid offset (%llu) for last fext lookup\n
u
%s:%d: %s unable to get omap: %d\n
Journal info block is missing!
%s rd_fd=%d (%s) crypto_fd %d plain_fd %d, encrypted %d closed %d volume %llx
%s:%d: %s level %d node 0x%llx: error prefetching index %d child 0x%llx flags 0x%x: %d\n
%s:%d: apfs_get_extentref_tree(oid=%llu) returned %d\n
%s:%d: %s oid 0x%llx (level %d): minkey not in sync\n
removal
%s:%d: %s failed to get omap tree for reaping: %d\n
nx_tx_wait_flush
%s:%d: %s tx_enter() failed: %d\n
61706673-7575-6964-0140-766f6c756d00
spaceman_sanity_check
hfs_insert_object: failed to fix utf16 file name:\n
apfs_sanity_check_tree_type
/dev/
%s:%d: warning: fs block size too small for device block size (%d < %d)\n
%s:%d: %s error getting next checkpoint data block address %d: %d\n
%s:%d: %s oid 0x%llx: btree node count (%llu) doesn't match # nodes traversed (%u)\n
%s:%d: can't get features for device (%s)\n
    -o <nx_or_apfs_format_options>\n
unified
%s:%d: %s reap list object free list erroneously empty?\n
spaceman_info failed with error: %d\n
%s:%d: %s btree_node_insert() failed (%d) while trying to revert changes due to error: %d\n
%s:%d: cannot change role of SideCar volume\n
apfsuuid
Get count overflowed for object %p!\n
%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n
password=
i32@?0r^v8r^v16^B24
Error %d inserting extent: id=%llu, logical_offset=%llu\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error preparing for write: %d\n
%s:%d: %s attempt to free block(s) outside of internal pool: 0x%llx:0x%llx\n
%s:%d: %s fs_update_snap_metadata() returned %d\n
%.24s: Estimated %'llu bytes of metadata\n
%s:%d: %s oid 0x%llx (level %d): root node has a parent 0x%llx (level %d)\n
jobj_validate_large_key_val
%s:%d: %s failed to compare currently available space: error %d\n
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n
%s:%d: %s fs %lld alloc count underflow: %lld (%lld)\n
capacity: all    %llu / %llu => %.2f %% used\n
raw_init
w
        %'9u class F\n
paddr
%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n
%s:%d: %s error deleting empty snapshot tree: %d\n
tx_checkpoint_desc_zero
%s:%d: %s failed to get fsys oid %lld: %d\n
groupquota
%s:%d: %s xid %lld checkpoint descriptor count is larger than expected: %d > %d\n
--watchdog: invalid argument: %s
lwvm_physical_to_logical
apfs-incompat-features-lock
jobj_size_for_key_val
%s:%d: %s sfq %d count underflow %lld - %lld\n
%s:%d: Invalid or unknown hash type: %d\n
apfs_create_doc_id_tree_if_needed
    keys: %9d %9d %9d %9d %9d %9d\n
%s:%d: %s failed to remove head_fext, ino %llu, laddr 0x%llx, error %d\n
%s:%d: %s invalid ref count %d for non NULL zero ref tree\n
xid
%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n
%s:%d: %s Trash unfinished tx xid=0x%llx\n
MKMediaCreateWithFileDescriptor: error %d\n
LwVM: media block size too large
PROGRESS
=
unable to get the volume's fsroot tree due to error: %d\n
%s:%d: %s failed to delete fs fext tree after fs creation failed: %d\n
obj_read
bt_merge_up
%s:%d: %s oid 0x%llx (level %d): key free list entry points to itself\n
perm
%s:%d: rdlock == 0 failed %d\n
%s:%d: %s sfq %d error inserting shortened entry %lld %lld into free queue: %d\n
ino_has_vnode(ino)
conformance
%s:%d: %s invalid object size: %d size_phys %d\n
%s:%d: %s oid 0x%llx (level %d): val free list entry starts beyond val space available\n
raw != NULL
Medium Type
%s:%d: %s failed to update dir-stats %llu: %s (%d)\n
mark_doc_id_index_for_rebuild_if_needed
%s:%d: %s fs[%d] checkpoint %s traverse failed: %d\n
%s:%d: %s oid 0x%llx (level %d): key location not within key space\n
%s:%d: %s Clearing persistent allocation zone at slot %llu\n
current tx not closed/flushing?!\n
No partition map found
%s:%d: %s unable to get snapshot tree: %d\n
No GPT partition map found
%s:%d: %s oid 0x%llx (level %d): leaf node has non-zero level\n
%s hfs_off=%lld hfs_len=%lld vol_size=%lld
%s:%d: %s btree_node_insert failed: %d\n
%s:%d: failed to serialize drec %lld/%s into jval of size %u\n
ps=%lld 
%s:%d: %s oid 0x%llx (level %d): non-leaf node has no children?\n
we asked for %lld blocks but got zero (paddr %lld) from spaceman_alloc() and no error.\n
%s:%d: %s could not update purgeable rsrc size for dir-stats %llu: %s (%d)\n
%s:%d: %s unable to get object 0x%llx: %d\n
fstype
unknown feature-format: %s\n
%.24s: Converting extents B-tree\n
%s:%d: %s oid 0x%llx (level %d): minkey compare error: %d\n
    keys: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s freeing 0x%llx:%lld, but %lld bits are already clear.  Double free?\n
feature-format
%s:%d: %s failed to move all entries: %d\n
%s:%d: %s oid 0x%llx (level %d): invalid child oid: 0x%llx\n
disk
key_size_for_jobj
%s:%d: %s error updating snapshot tree: %d\n
    %'9u hard link inodes\n
jobj_size_for_large_key_val
%s:%d: object cache initialization failed: %d - %s\n
not handling the flushing tx!\n
%s:%d: %s tx xid %lld took %lld us to sync and write superblock\n
com.apple.system.cprotect
can't produce fake mount path
%s:%d: %s Cannot mark space for %zu bytes at offset %lld in dstream %lld of inode %lld as writable: %s(%d)\n
%s:%d: %s could not update clone size for dir-stats %llu: %s (%d)\n
%s:%d: %s obj_create failed - %d\n
allocate_keylocker_space
hfs_free_metadata: hfs_free_extent returned error %d for freeing blocks of alternate volume header\n
%02hhx
n_h
Removed LwVM keylocker
update_dir_stats
%s:%d: %s removing reverted fs objects for fs %lld: %lld - %lld\n
raw_hfs_to_phys
ID
capacity: %9d %9d %9d %9d %9d %9d\n
alloc_space_for_write_with_hint_and_spino
%s:%d: %s sfq %d error validating extent %lld %lld: %d\n
%s:%d: %s failed to remove first, error %d\n
%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n
%s:%d: %s level %d node 0x%llx: error getting index %d child flags 0x%x: %d\n
pwrite: offset=0x%llx size=0x%x\n
Content protection EA for cnid=%u is incorrect version (%u).  Conversion failed!\n
%s:%d: %s fs snapshot metadata tree creation failed: %d\n
spaceman_freed
          Preboot volume will be blessed with the boot efi driver.\n
bootefi
hfs_insert_inode: invalid record type (%u)\n
%.24s: Number of current fsroot tree nodes %lld\n
%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n
%s:%d: %s deleting extent %lld %lld with invalid owning_obj_id %lld while apfs_num_snapshots is 0, this will cause overallocation\n
uuid_from_role
orphan_snap_check_iterator
<integer>%ld</integer>\n
%s:%d: %s extentref tree type 0x%x invalid, using physical btree instead\n
spaceman_allocated
crypto_hash_insert
preV=%s 
ss
%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n
hfs_to_apfs: hfs_offset=%lld, phys_offset=%lld is outside the APFS space
%s:%d: %s oid 0x%llx (level %d): key count larger than TOC space\n
%s:%d: Couldn't set sparse bytes extended attribute on ino %lld, error %d\n
%s:%d: %s *** unknown expanded obj type %hhu\n
%s
btree rightmost leaf mismatch! (expected %lld found %lld)\n
sealed=yes
waitpid(mount_apfs) failed (pid=%d, errno=%d)
Volume not cleanly unmounted and not journaled!  %s\n
%s:%d: %s oid 0x%llx (level %d): can't get child: 0x%llx\n
auto
        %'9u class C\n
%s:%d: %s expanded obj type %hhu found on unsupported volume\n
%s:%d: %s clonegroup tree creation failed: %s\n
UNKNOWN TXN TYPE
Direct Mode
%s:%d: %s range 0x%llx:%lld overlaps with recently-freed range 0x%llx:%lld\n
n_f=%lld 
%s:%d: %s Failed to get pfkur tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: cannot change role of system-unique volume\n
tx_enter failed: %d\n
%s:%d: %s btree_node is null\n
%s:%d: %s tx_leave failed: %d\n
invalid crypto id
    --bootefi=<boot efi driver directory full path>\n
hfs_catalog_iter_b() failed: %d\n
%s:%d: %s ino %lld no extent covering dstream alloced_size %lld (fsize %lld) pos/len %lld:%lld\n
%s:%d: %s value size (%zu) on purgeable record (%llu) is too small\n
Error %d freeing blocks for journal\n
spaceman_fxc_update_smallest_with_successor
%s:%d: %s error updating metadata ranges tree: %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x can't modify object before read completes\n
nx_tx_wait_closed
n_lf
Error %d inserting physical extent: id=%llu, logical_offset=%llu\n
%s:%d: %s failed to create doc-id tree, error %d\n
%s:%d: %s Cannot restore unwritten status of extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n
%s:%d: %s unreserving %lld blocks for reverted fs objects\n
new address mismatch on redirty 0x%llx 0x%llx\n
%s:%d: %s error getting cab %d @ %lld: %d\n
    Fixed size: %llu (0x%llx) bytes\n
supplemental_tree_get_descriptor
omap_sanity_check
obj_checksum_verify_phys
%s:%d: %s this volume requires valid UUID option specified\n
apfs_is_volume_uuid_allowed
com.apple.apfs.
    %'llu bytes freed by conversion\n
%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n
journal
Invalid HFSPlus version (%u)\n
apfs_sanity_check
no-name
jobj_to_key_val
mount_apfs didn't exit?
slice %u: Can't find volume name.  (Error %d)\n
%s:%d: %s Preventing %s of objects to synthetic folder (id %lld, parent %lld)\n
%s:%d: %s was NOT able to update/decrement crypto state %lld, err = %d\n
%s:%d: %s error unreserving space, %lld blocks: %d\n
61706673-7575-6964-0010-766f6c756d00
%s:%d: %s file system %lld fs reserve alloc count %lld larger than global fs reserve alloc count %lld\n
close(plain_fd)
%s:%d: %s ***: expanded obj type %d found on unsupported volume\n
fs_make_hole_range_writable
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object missing paddr!\n
    -g\t   Change GPT GUID to APFS at end of conversion (relevant only for raw hfs volumes, and hfs volumes inside core storage).\n
        %'9u class D\n
nx_metadata_range_add
bad option '%s'
ca=%lld 
%.24s: Done converting slice #%u\n
%s:%d: %s Failed to get next extent: %d\n
%s:%d: %s Couldn't acquire lock on %llu-%llu, err=%d\n
Journal header magic or endian is wrong (magic=0x%08x, endian=0x%08x)
%s:%d: %s failed updating hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n
%s:%d: %s clonegroups enabled for this volume\n
MKCFBuildPartition failed: %d
%s:%d: %s sm_fs_reserve_alloc_count underflow, sm_fs_reserve_alloc_count %lld, new fs_reserve_block_count %lld, old fs_reserve_block_count %lld alloc_count %lld\n
%s:%d: %s fs fext tree creation failed: %d\n
%s:%d: %s key.hdr.kind != NEW && numsnapshots == 0\n
nx_reaper_sanity_check
%s:%d: %s Error reinitializing free extent cache: %d\n
apfs-pfkur-tree-oid-lock
%s:%d: %s oid 0x%llx (level %d): key free list head beyond key space available\n
apfs_free_data_blocks
IOBlockStorageDevice
%s:%d: tx manager initialization failed: %d - %s\n
i24@?0r^v8r^v16
%s:%d: %s failed to init extended fields on purgeable %llu from blob\n
xid = %lld, curr_xid = %lld
Deleting old fsroot tree returned error: %d\n
%s:%d: %s fext_tree_update returned %d\n
%s:%d: %s failed to extend existing extent %lld:%lld of inode %lld: %s(%d)\n
vol_index equals -1, but hfs_offset is not VM_FREE_SPACE_MARKER or VM_USED_SPACE_MARKER
%ss%d
physical size
hfs_update_root: unable to get APFS root directory\n
%s:%d: %s Failed to unwrap metadata crypto state: %d\n
%s:%d: %s failed to increment crypto state refcnt, ino %llu, crypto_id %llu, error %d\n
gbitmap_reap
    %'9u files\n
btree_node_debug_stats
follow
%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n
%s:%d: obj is NULL or not apfs object!\n
%s:%d: %s spaceman_free failed for LBA %llx, size %llu : %d %s\n
%s:%d: %s failed to get object oid %lld: %d\n
INFORMATION
UNKNOWN
non-physical object on physical object dirty list: oid %lld flags 0x%llx 0x%x\n
spaceman_cab_sanity_check
Type
%s:%d: %s Hit %d looking up first snapshot\n
%s:%d: %s remove_jobj(old-snap-name) returned %d\n
vol_index == 0
%ss%d:%lld
MKCFCreateMedia failed: %d
hfs_free_metadata: hfs_free_extent returned error %d for volume header\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n
omap_destroy
%s:%d: %s bt_shift_or_split failed with error: %d\n
find_free_blocks_in_free_extents: found_start=%lld\n
ino %lld illogical file extent %lld:%lld != alloced_size %lld (fsize %lld)\n
%s:%d: %s object type 0x%x not reapable?: %d\n
%s:%d: error: device is not writable!\n
Release count overflowed for object %p!\n
%s:%d: %s remove mapping (%lld, %lld) failed: %d\n
failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d, %s\n
level %d: %d nodes %.2f average descendents\n
%s:%d: %s failed to get reap list head: %d\n
%s:%d: %s Space outside soft block-out range seems fragmented (requested %llu, but could alloc only %llu), disable soft block-out range\n
tx_leave failed: %d\n
ea=%lld 
%s:%d: %s omap checkpoint traverse (op %d) failed: %d\n
%s:%d: %s %s: could not remove dir rec for obj-id %lld (name: %s)\n
%s:%d: can't get solidstate for device (%s)\n
%s:%d: %s oid 0x%llx (level %d): val free list entry extends beyond val space available\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - has refs\n
sha512
tx_finish
journal_info_block
%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n
d=%ld 
%s:%d: %s oid 0x%llx (level %d): key free list entry starts beyond key space available\n
%s:%d: %s cannot insert new ep %llu because the policy cache is full\n
%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n
descendants
%s:%d: %s Inserting snap_name failed, %d\n
%s%s%llx
i32@?0r^{HFSPlusExtentKey=SCCII}8r^{HFSPlusExtentDescriptor=II}16^B24
jobj_validate_key_val
Schemes
apfs_unlock_id
rolling-stats-lock
%s:%d: %s oid 0x%llx (level %d): keys out of order: %d\n
atime
%s:%d: %s Error mapping freed IP block range 0x%llx:0x%llx to index: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/hfs_dev_io.c
%s:%d: %s failed to init extended fields on clone mapping <%llu/%llu> from blob\n
%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n
rw
%s:%d: %s op %d failed to free internal pool block %lld: %d\n
capacity: %9s %9s %9s %9s %9s %9s\n
%s:%d: %s ***: expanded obj type %d (obj_id %llu) found on unsupported volume\n
%s:%d: %s key size (%zu) on purgeable record (%llu) is too small\n
%s:%d: %s IP free queue tree is too large: %lld nodes (limit %d) xid %lld\n
%s:%d: Volume role 0x%x is not supported
omap_cleanup
spaceman_get_new_chunk_for_allocation_zone
%s:%d: %s op %d failed to create bitmap object %lld: %d\n
%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n
virtual object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
spaceman_chunk_zone_info_list_remove
unable to get matching service
fsroot_iterator
%s:%d: %s error getting oid for child %d of 0x%llx: %d\n
%s:%d: %s failed to insert fext in fext_tree: %d\n
trying to zero the superblock!\n
%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n
dry-run
Rotation Rate
%s:%d: %s UUID %s is not allowed, error %d\n
%s:%d: %s unable to create/store metadata crypto (%d)\n
case=sensitive
61706673-7575-6964-0002-766f6c756d00
spaceman_free
Content protection key for cnid=%u is too long (%u).  Trying to repair.\n
fs_make_phys_range_writable
%s:%d: metadata space calculation failed: %d - %s\n
%s:%d: %s Quota %llu is smaller than what's currently allocated and reserved %llu\n
cu
Error %d freeing extent [start=%lu, count=%lu]\n
tx_finish failed with error: %d\n
%s:%d: %s supplemental_tree_destroy(fext_tree) failed: %d (%s)\n
%s:%d: %s Unknown NEW persistent ephemeral object found: oid 0x%llx type 0x%x/0x%x\n
doc_id_tree_insert() failed: %d\n
Removed APFS keylocker
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/nx/jobj_snap.c
rs
    %'lld bytes used by APFS\n
__OSINSTALL_ENVIRONMENT
virtual object not prepared before dirtying: oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x xid 0x%llx 0x%llx 0x%llx\n
%.24s: Flushing transactions\n
spaceman-fxc-lock
jdev_fext_read_data() corrupts encrypted data
%s:%d: %s value size (%zu) on unknown record (%llu) is too small\n
Could not open volume %s
Error %d converting name (%s) to UTF-16\n
authapfs_seal_break
Reading journal header
  inserting extent id=%llu, logical=%llu, physical=%llu, length=%llu\n
type = %u, req_tree != fs_root\n
%s:%d: %s oid 0x%llx (level %d): val free list entries total space exceeds free list space\n
%s:%d: %s xid %lld error getting first checkpoint map block address %d: %d\n
fixed
</plist>\n
AppleEffaceableStorage
Symlink too large (cnid=%u, size=%llu)\n
%s:%d: %s Failed to find successor node in length tree: %d\n
%s:%d: %s key size (%zu) on expanded record (%llu) is too small\n
%s:%d: %s failed to init extended fields on dir-stats %llu from blob\n
%s:%d: %s invalid reap_id (%llu), must be smaller than nr_next_reap_id (%llu)\n
spaceman_checkpoint_traverse
%s:%d: %s failed to check if doc-id index is stale (error %d)\n
    -F n  Slice #n (0-based) should be fixed size.\n
bt_insert
61706673-7575-6964-0008-766f6c756d00
%s:%d: %s op %d failed to allocate block from internal pool: %d\n
sha512_256
mount-path
apfs_newfs failed\n
,
Journal is not empty!  Cannot convert.
%s:%d: %s oid 0x%llx (level %d): val location extends beyond val space\n
%s:%d: %s failed to write checkpoint map block %lld: %d\n
fsreserve=
%s:%d: %s wrong object at 0x%llx - wanted oid 0x%llx type 0x%x:0x%x xid %lld - got oid 0x%llx type 0x%x:0x%x xid %lld\n
    Conversion took %ld seconds\n
insert_apfs_sibling_record: error %d inserting sibling record (inode=%llu, link=%llu)\n
fs_destroy_shadow_fs_root_tree
assertion failed: %s
          Format options passed through to nx_format and apfs_newfs.\n
!((apfs)->apfs_main_apfs != ((void*)0))
Trying to update a namedstream inode %llx on volume %s\n
%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n
APFS_TREE_LOOKUP_ZONE
sha3_512_4k
cprotect EA disallowed with unified devt\n
%s:%d: %s oid 0x%llx (level %d): key size greater than longest recorded for tree\n
invalid crypto id %llu
%s:%d: %s fext_ref_extent_key for fext %llu with crid %llu failed with %d\n
%s:%d: %s danger - crypto id %lld had refcnt %d\n
tx_leave
btree_node_insert_internal
%s:%d: failed to init extended fields on drec %lld from blob.\n
%s:%d: %s xid %lld second sync/barrier failed: %d\n
ea
capacity: nodes  %llu / %llu => %.2f %% used\n
object-lock
spaceman_fxc_update_length
%s:%d: %s BUG BUG BUG: ino %lld non-contiguous extents! prev_fext %lld:%lld (%lld) and orig_fext %lld:%lld (%lld)\n
defwrite
is_APFS: expected %zu bytes, got %zd\n
%s malloc(%ld) failed, io_size %ld io_offset %lld, bytes_per_sector %d
Logical  Physical  Length
Error %d inserting crypto_state for inode=%u.  Conversion failed!\n
%s:%d: %s oid 0x%llx (level %d): val free list entry beyond end of node\n
%s:%d: Volume role 0x%x is not supported in container\n
SNAP_DELETE_TXN
n_le
%s:%d: %s clone mapping is enabled for this volume\n
omap_reap
%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n
Writing journal info block
%.24s: Invoking omap_expunge_oids_below_watermark\n
%s:%d: %s oid 0x%llx (level %d): key free list entry extends beyond key space available\n
hfs_convert
hfs_free_metadata: hfs_to_apfs returned error %d for volume header address mapping\n
cp_os_version
%s:%d: %s xid %lld error flushing objects from the cache: %d\n
au=%lld 
unable to insert EA (%llu, %s, %llu); error=%d\n
/usr/sbin/ioreg -l
%s:%d: %s fixing DIR_STATS_IS_SHADOW flag for dir-stats %llu\n
sha3_256
authapfs_valid_hash_type
tx_flush
sha3_384_4k
%s:%d: %s oid 0x%llx (level %d): invalid table space offset\n
spaceman_set_bits_in_bm
%s:%d: %s Error %d, reinitializing\n
vol_write: Error %d from pwrite(fd=%d, offset=0x%llx, size=0x%zx)\n
apfs_free_data_blocks_if_needed
%.24s: Gathering pre-conversion statistics\n
%s:%d: %s failed to get omap %lld: %d\n
Can't set block size to %u (not a multiple of %u)\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld\n
obj-mem-mgr-lock
%s:%d: %s failed to serialize purgeable %llu into jval of size %u\n
total_count
Reference count underflowed for object %p!\n
%s:%d: %s apfs_free_data_blocks_if_needed(%llu,%llu) failed: %d %s\n
spaceman_init_cib
pil
Could not remove LwVM keylocker
%s:%d: %s no space for a new file system (slot %d, max %d)\n
%s:%d: %s failed to get reap list tail: %d\n
%d$@
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list for cleaning: %d\n
61706673-7575-6964-0180-766f6c756d00
/dev/r%s
unknown fd
%s:%d: %s invalid crypto object type %u\n
apfs-phys-lock-state-mutex
%s:%d: %s old reserve was %lld, num_blocks %lld. blocks_in_txn_counter %lld num_active_txns=%d\n
untitled
%s:%d: %s fs private dir creation failed: %d\n
<integer>%p</integer>\n
nx_check_superblock
%s:%d: %s oid 0x%llx (level %d): tree says key size is fixed, but node says kv size is variable\n
%s:%d: unlocking id %llu, which is not locked\n
ta
%s:%d: reaper thread is exiting, returning EBUSY\n
Volume is not journaled!
Ignoring block or character device (cnid=%u)\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x paddr 0x%llx error verifying checksum\n
hfs_init: %s\n
%s:%d: %s attribution tags are supported on this volume\n
%s:%d: failed to finish first transaction: %d - %s\n
invalid unlock flags: 0x%x\n
%s:%d: %s free extent %lld:%lld appears to span container metadata and should not be free: %d\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/hfs_vol.c
Content protection EA for cnid=%u is incorrect version (%u).  Try to repair\n
invalid tweak type %d\n
Conversion is taking too long!
    --efi=<efi driver file name>\n
Partitions
%s:%d: %s oid 0x%llx (level %d): freespace %u larger than nodespace %u\n
unexpected storagetype: 0x%x\n
spaceman_decrement_free_queue_count
%s:%d: %s reverting on error: %d\n
%s:%d: %s omap checkpoint %s traverse failed: %d\n
nx_tx_wait_closed_prev_flushing
%s:%d: %s oid 0x%llx (level %d): free space extends beyond end of node\n
%s:%d: %s oid 0x%llx (level %d): val free list entry overlaps with other free space\n
%s:%d: %s Volume role 0x%x already exists in container uuid %s\n
legacy_get_ek
\t\t\t<key>%s</key> 
%s:%d: %s Shadow fs_root does not exist\n
    Preparing encryption: offset=%llu (0x%llx)\n
omap_expunge_oids_below_watermark returned an error: %d\n
%s:%d: %s oid 0x%llx (level %d): key free list entries total space exceeds free list space\n
obj_get_async_read
volname=
spaceman_fq_tree_insert
%s:%d: %s xid %lld error getting next checkpoint superblock address %d: %d\n
%.24s: Copied %llu fsroot tree records into new fsroot tree\n
%s:%d: %s not enough space to enter transaction\n
hfs_vol_read: Error %d from pread(fd=%d, aligned_size=0x%zx, aligned_offset=0x%llx\n
object-cache-reset-lock
%s:%d: %s reap list expected %u objects, but got last reap list object with %u more objects left\n
%s:%d: %s failed to get next internal pool reverse mapping, error %s(%d)\n
%s:%d: %s sfq %d processing xid %lld blocked by temporary checkpoints %lld\n
%s:%d: %s Final sync/barrier failed: %d\n
jobj_to_large_key_val
sha256
p=%lu 
%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n
%s:%d: %s failed to delete fs extentref tree after fs creation failed: %d\n
61706673-7575-6964-0020-766f6c756d00
61706673-7575-6964-0280-766f6c756d00
%s:%d: %s Failed to set bits for allocation %lld:%lld: %d\n
%s:%d: %s fs reserved space underflow: %lld (%lld)\n
%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n
%s unaligned pread(%d, 0x%llx, %ld, %lld) failed, io_size %ld io_offset %lld, bytes_per_sector %d
%s:%d: %s Cannot update extent at offset %lld in inode %lld: %s(%d)\n
APFS_INODES
io_get_device_features
%s:%d: %s failed to write cib %d: %d\n
dirents
tx_finish() returned %d, tx still active?\n
%s:%d: %s failed to initialize free extent cache, error %d\n
%s:%d: tx checkpoint descriptor area initialization failed: %d - %s\n
nx_tx_wait_closing
-S: %s
fl
%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n
%.24s: apfs_hfs_convert (%s)\n
APFSIOC_SET_CONV_CTX
Error %d trying to overwrite metadata at offset %lld length %lld\n
%s:%d: %s stopped updating dir-stats due to chain being too long\n
fs_insert_fext_record
obj_cache_remove_new_fs_objects
obj %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refs 0x%llx is not ephemeral\n
hfs_vol_read: Error %d from pread(fd=%d, size=0x%zx, offset=0x%llx\n
%s:%d: %s failed to get a new default crypto-id, ino %lld\n
  inserting extent-based EA: ID=%u EA=%s [%llu logical; %llu physical]\n
%s:%d: %s level %d node 0x%llx: error ON WAIT getting index %d child 0x%llx flags 0x%x: %d\n
%s:%d: %s waiting for transaction to finish\n
%s:%d: Unable to insert record into new fsroot tree\n
%s:%d: %s failed to fetch the fext tree (error %d)\n
APFS_8K_OBJS
%s:%d: failed load container metadata ranges (overlap?): %d\n
physical object on dirty list not dirty: oid %lld flags 0x%llx 0x%x\n
spaceman-czic-lock
After scanning %d Volume Managers, none was able to open the device\n
bad pext.\n
%s:%d: %s Encrypted volume is not allowed with special role = 0X%x\n
%s:%d: %s fs tree type 0x%x invalid, using virtual btree instead\n
browse
0
Removable
<40
obj_mem_mgr_init
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary index\n
unwritten
bad transition tx flags 0x%x to 0x%x (expected 0x%x)\n
sha3_512
d100
Error %d from optimize_btree\n
apfs_mount_livefs
obj_checkpoint_known
reserved metadata space underflow: %lld (%lld)\n
cst->ep_retain_count <= cst->hdr.retain_count
%s:%d: %s Fusion is not supported anymore\n
omap_find_next_snapshot_xid
61706673-7575-6964-0100-766f6c756d00
Protocol Characteristics
tu
%s:%d: %s failed to get doc-id tree key count, error %d\n
dev_read: offset=0x%llx size=0x%zx(%s)\n
fext %lld (pos %lld len %lld flags %x can not have crypto-id -1\n
%s:%d: %s failed to lookup pos %lld in obj-id %lld err %d\n
%s:%d: %s oid 0x%llx (level %d): table space length smaller than minimum\n
%s:%d: %s Couldn't create extentref tree for demo mode: %d\n
%s:%d: creation of fragmented metadata physical extent list tree(s) failed: %d - %s\n
%s:%d: %s danger: oid %lld type 0x%x/0x%x flags 0x%llx 0x%x xid %lld refs 0x%llx - is dirty\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error allocating new location %d\n
raw.c
    -M <mount_path>\n
%s:%d: %s invalid relative OID: %llu < root OID: %llu\n
%s:%d: %s oid 0x%llx (level %d): can't get child %d oid: %d\n
level %d: %d nodes\n
%s:%d: failed to init extended fields on inode %lld from blob (xfret %d).\n
%s:%d: %s Failed to get supplemental tree (type %d, oid %llu): %d (%s)\n
supplemental_tree_destroy
set_cloneinfo_id_epoch
%s:%d: %s failed to write superblock to block 0: %d\n
%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n
    %'llu bytes used by HFS\n
%.24s: Checking for directory hard links\n
spaceman_free_extent_cache_search
vol_write: Error %d from pwrite(fd=%d, aligned_offset=0x%llx, aligned_size=0x%zx)\n
%s:%d: %s failed to zero checkpoint descriptor block %d @ %lld: %d\n
\n %04x 
%s:%d: %s oid 0x%llx (level %d): key count larger than gross key space\n
%s:%d: locking id %llu, which is already locked by this thread\n
prevConvStats
nx_checkpoint_traverse
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error deleting old mapping %d\n
%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error deleting mapping %d\n
%s:%d: failed to init extended fields on attribution tag record with objid <%lld> from blob due to error <%d> %s\n
non-virtual object on virtual object dirty list: oid %lld flags 0x%llx 0x%x\n
hfs_insert_object: hfs_utf16_t_utf8 failed (error %d)\n
((&crypto_cache->free_list)->tqh_first == ((void*)0))
fext_get_crypto_id
%s:%d: %s EALREADY; rooted from snap, apfs %p\n
%s:%d: %s fs root dir creation failed: %d\n
supplemental_tree_get
%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n
%s:%d: %s Failed to find smallest extent %d in length tree: %d\n
btree_node_val_range_validate
fs_tx_enter_internal
clean_up_doc_id_trees_if_needed
ps
dev_write: offset=0x%llx size=0x%zx(%s)\n
%s:%d: %s Inserting snap_meta failed, %d\n
%s:%d: Sparse bytes removed from inode %lld that didn't have an extended field.\n
%s:%d: %s Skipping metazone_init() as backing store is sparse\n
spaceman-lock
%s/apfs
%s:%d: %s btree check called with non-root btree node: %d\n
%s:%d: %s failed to enter tx - %s(%d)\n
%s:%d: %s integrity protection will be disabled (from xid: %llu)\n
    %'9u folders\n
clear_invalid_fixups
com.apple.system.fs.speculative_telemetry
APFS_4K_OBJS
spaceman_chunk_zone_info_compare
Journal location is inconsistent (file=0x%llx, jib=0x%llx)
virtual
<%d
%s:%d: %s cannot translate key-val (%llu) into valid jobj\n
dereference
%s:%d: %s value size (%zu) on dir stats (%llu) is too small\n
clone size
obj_alloc
%s:%d: %s error modifying omap: %d\n
spaceman_unreserve
authapfs_validate_node_hash
watchdog
%.24s: Spaceman free queue count %llu and xid is %llu\n
overwriting backup LwVM header
btree_node_free_list_entry_validate
%s:%d: %s failed to serialize clone mapping <%llu/%llu> into jval of size %u\n
cache_flush: offset=0x%llx size=0x%zx(%s)\n
␀␀␀␀HFS+ Private Data
%s:%d: %s unable to allocate chunk zone info cache\n
%s:%d: %s chunk %lld recent zone count underflow\n
%s spaceman_free failed, line %u, apfs_offset %lld apfs_length %lld xid %lld apfs_block_size %u
nx-resize-spaceman-lock
<string>%s</string>\n
%s:%d: ** BOGUS FEXT FLAGS = 0x%02x (crypto_flags = 0x%llx)\n
61706673-7575-6964-0004-766f6c756d00
ft
APFS filesystem block size is set to %u\n
btree_node_space_stats
%s:%d: %s oid 0x%llx (level %d): free space offset too large\n
/tmp/hfs_convert.log
fstree=btree
%s:%d: %s find_next_snap(%llu) returned %d\n
Journal flags are unexpected (0x%x)
%.24s: Number of new fsroot tree nodes %lld\n
obj_init
%.24s: Creating APFS container\n
Could not remove APFS keylocker
%.24s: Finding inode files for slice %u\n
%s:%d: %s set apfs_fixup_flags to %#llx\n
%s:%d: %s could not update purgeable size for dir-stats %llu: %s (%d)\n
IOMedia
empty_password
fs=%d fp=%d fl=%d 
reopening %s
%.24s: Freeing HFS metadata\n
apfs-global-snap-lock
jobj_release
check_stale_doc_id_index
%s:%d: %s FS will NOT have extended vek protection classes\n
%s:%d: %s unable to get test object 0x%llx of type 0x%x/0x%x for checkpoint %s traverse: %d\n
%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n
    %'9u extent-based EAs\n
rdisk
gid=
spaceman_clear_bits_in_bm
    -D    Convert all former and current directory hard links to files/aliases. \n
MKCFReadMedia: error %d
Error %d reading B-tree offset=%llu length=%zu\n
%s:%d: %s tree_delete() failed: %d\n
r
dev_barrier after writing JIB
btree_node_compact
%s:%d: %s fs root tree creation failed: %d\n
MKMediaCreateWithFileDescriptor failed: %d
%s:%d: %s Persistent allocation zone at slot %llu has invalid previous boundary %llu\n
%s:%d: %s failed to allocate bitmap block from IP bitmap pool: %d\n
failed to init btree for iteration \n
spaceman_fxtp_add_child
apfs_reap_snapshots
bt_shift_or_split
%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n
purgeable size
match_jobj_expanded_type_to_tree_type
%s:%d: %s found free extent (0x%llx:0x%llx) which should not be free!: %d\n
%s:%d: %s First sync/barrier failed: %d\n
hfs_insert_large_EA_extent: logical_offset %llu apfs_length %lld\n
%s:%d: %s Couldn't get active extentref tree, err=%d\n
%.24s: Overwriting backup LwVM header.\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x bad dirty xid: 0x%llx\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/hfs_convert.c
%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n
%s:%d: warning: fs block size too small (%d < %d)\n
Number of free blocks %lld and number of current fsroot nodes %lld. There isnt enough free space to continue..\n
remove_jobj
%s:%d: %s Could not set fs bounds for guarantee %lld and quota %lld: %d\n
** 
can not delete an object w/a non-current xid %lld o == %p\n
unified_devt disallowed with directory hardlinks \n
apfs-dir-size-lock
    keys: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
Retain existing content
%s:%d: %s key @ %p key.hdr.obj_id %lld val @ %p val.kind %d refcnt %d owning_obj_id 0x%llx\n
spaceman_ip_bm_block_free
directory hardlinks disallowed on unified_devt\n
you can't change a key here!  (ekey %p eklen %d; key %p klen %d; n %p bt %p)\n
spaceman_sanitize_datazones
%s:%d: %s extent at lba %llu len %llu couldn't be freed: %d\n
oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x object not prepared before dirtying\n
%s:%d: %s Couldn't reopen transaction to clean up: %d\n
%s:%d: %s failed to load inode %lld ret %d on volume: %s\n
apfs_lock_id
btree_node_sanity_check
%5d  %4d  %5d\n
nx_metadata_range_optimize
key/val sizes:  tree max k:%d v:%d  max k:%d v:%d  avg k:%llu v:%llu\n
spaceman_set_up_ip_reverse_mapping_tree
%s:%d: %s gettin' low on space: ttype %s num_blocks %lld blocks_in_txn %lld free_blocks %lld xid %lld\n
directory
preV
Unknown record type: 0x%x\n
%s:%d: %s Could not find data to allocate outside the soft block-out range, disable soft block-out range\n
p
    Freeing journal (offset=0x%llx, size=0x%llx)\n
vol_write: Error %d from pread(fd=%d, aligned_offset=0x%llx, aligned_size=0x%zx)\n
%s:%d: %s oid 0x%llx (level %d): key entry overlaps with other entries\n
ino
conversion_init() failed: %d\n
tx-mgr-lock
preboot
%s:%d: spaceman_get() failed: %d\n
CTRL-C received, conversion failed
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n
com.apple.fs.symlink
Error %d freeing blocks for Hot Files B-tree\n
%s:%d: %s oid 0x%llx (level %d): invalid keys[] pointer\n
apfs-global-lock
obj_create_internal
apfs-snapmeta-oid-lock
%s:%d: %s oid 0x%llx (level %d): node level greater than root level %d\n
%s:%d: %s oid 0x%llx (level %d): val location not within val space\n
%s:%d: %s Failed to get fext tree w/oid %llu (modify_xid %llu): %d (%s)\n
%s:%d: %s error adding omap 0x%llx type 0x%x to reap list: %d\n
spaceman_ip_bm_block_alloc
spaceman_ip_block_alloc
dr=%d\n
Error %d from spaceman_info\n
Journal info block location is inconsistent (header=0x%llx, file=0x%llx)
%s:%d: %s failed to modify the apfs_t before reaping (error %d).\n
%s:%d: %s Can't get tree: %d\n
Found record in directory hard link private directory: (name=%s, record type=%u)\n
%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n
%s:%d: %s reap list expected %u objects, but haven't seen last reap list object yet\n
 * * * cannot allocate memory * * *\n
%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n
%.24s: Performing btree compaction\n
pn
%s:%d: %s oid 0x%llx (level %d): can't get key %d: %d\n
%s:%d: %s tree_remove(%llu) failed\n
%sr%s
%s:%d: %s failed: cksum 0x%016llx, oid 0x%llx, o_xid 0x%llx, o_type 0x%x, o_subtype 0x%x, size %d\n
ta=%lld 
%s pread(%d, 0x%llx, %ld, %lld) failed
hfs_convert_msg_string
dev_read: Error %d from pread(fd=%d, size=0x%zx, offset=%llx\n
%s:%d: %s crypto_obj_insert of new crypto_id %lld should not have failed (ret %d)\n
%s:%d: %s X %d\n
%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n
ja
apfs_create_doc_id_tree_if_needed() failed: %d\n
hot_files
apfs_newfs
Error %d initializing wrapped crypto state (cnid=%u)\n
%s:%d: %s Invalid reap list entry nrl_entries[%d].nrle_next = %d\n
encrypt
_dev_flush:fsync(plain_fd %d)
nodesize: %d  dataspace: %d  key size: %d  val size: %d  max keys: node %d leaf %d  avg keys: node %d leaf %d\n
%s:%d: don't know how to merge refcounts on objects of file info type %llu\n
%ss1s%u
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x non-virtual object missing paddr!\n
%s: Cannot determine device features: %s\n
%s:%d: %s doc-id tree creation failed: %d\n
ino %lld pos:len %lld:%lld fext %lld:%lld (%lld)\n
%s:%d: %s failed to mark doc-id index for rebuild, error %d\n
jobj_merge_maybe_clamp_64
invalid crypto index %d\n
%s:%d: %s unable to find free IP block or to free pending free IP blocks\n
\nConversion took %ld seconds\n
n_d=%lld 
Invalid HFSX version (%u)\n
we asked for %lld blocks but got %lld (orig %lld, blks_this_allocation %lld)\n
dir-stats
exp-dir-stats
hfs_find_inodes: hfs_utf16_to_utf8 failed (error %d)\n
  values: %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n
omap=ephemeral
%s:%d: %s tx_finish() failed, %d\n
%s:%d: %s xid %lld failed to write block 0 superblock: %d\n
 (%s)
After scanning %d Volume Managers, none found applicable\n
/Library/Caches/com.apple.xbs/913BFFDF-E590-49D6-85F8-42EB80AAF337/TemporaryDirectory.vZXWuT/Sources/apfs_executables/hfs/hfs_btree.c
    %'7.3fs (%5.2f%%) user\n
ino-lock
%s:%d: %s failed to get next extent in metadata fragmented extent list tree, error %s(%d)\n
%.24s: Finishing transaction\n
%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n
%s:%d: %s tree_iter_init() returned %d\n
%s:%d: %s apfs_update_phys_range for satisfiable range failed on 0x%llx+%llu, error %d\n
n_lf=%lld 
ru
jfs_get_tree() failed: %d\n
%s:%d: %s object type 0x%x not reapable: %d\n
dev
btree_node_insert
FULL
crypto_obj_free
%s:%d: don't know how to merge refcounts on objects of type %d\n
%s:%d: %s oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x error destroying: %d\n
deleted object @ %p can not be dirtied!! (flags: 0x%llx)\n
fsquota=
Error %d from iterate_vm_metadata\n
Invalid extent_ref tree
%s%s\n
%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n
Internal
%s:%d: %s oid 0x%llx (level %d): key location extends beyond key space\n
%s:%d: omap initialization failed: %d - %s\n
%s%s
<20
RR_HOLE
obj_checkpoint_start
postV=%s 
    %'9u hard links\n
%s:%d: %s oid 0x%llx (level %d): key count larger than possible\n
apfs_lock_phys_range first_pbn 0, last_pbn 0x%llx\n
\t\t\t<integer>%d</integer>\n
%s:%d: %s oid %lld flags 0x%llx 0x%x type 0x%x/0x%x xid %lld (cur xid %lld) error allocating space to write %d; blkcount %d (o_size_phys %d) paddr %lld\n
%s:%d: %s failed to read cab %d: %d\n
purgatory.
%s:%d: cnid 0x%x / obj_id 0x%llx is not a valid inode. ignoring orphaned file extents.\n
catalog_tree
apfs
can not lock id zero\n
%10llx  %10llx\n
spaceman_create
n_le=%lld 
.hotfiles.btree
tx_unmount
%s: Cannot determine number of sectors: %s\n
%s: Cannot open device: %s\n
ba
private-dir
fs_insert_snapshot_metadata
fs_lookup_snapshot_metadata_by_xid
%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n
%s:%d: %s bt_move_entries %d failed: %d\n
%s:%d: %s started cleaning snapshots %lld-%lld\n
tx_checkpoint_space_check
Failed to alloc cache buffer\n
%s:%d: %s oid 0x%llx: btree key count (%llu) doesn't match # leaf entries (%u)\n
%s:%d: %s fext_tree_remove returned %d\n
%s:%d: %s Failed to fetch crypto for crypto_id %lld\n
large_key_val_to_jobj
nx_reap_list_sanity_check
invalid lock flags: 0x%x\n
protect
hfs_insert_large_EA_extent: spaceman_alloc alloc'd %lld blocks at paddr %llu\n
%s:%d: %s bad overprovisioning volume configuration: reserve %lld quota %lld\n
%s:%d: %s clone mapping <%llu, %llu>: failed to update dir-stats key: %s (%d)\n
%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n
%s:%d: %s key size (%zu) on purgeable tombstone (%llu) is too small\n
maxfs=
%s:%d: %s failed to write cab %d: %d\n
%s:%d: %s Deleted the shadow_fs_root tree %p\n
%s:%d: %s failed to allocate temporary block memory\n
spaceman_alloc_iterate_chunks
mkdir for fake mount
object-cache-lock
```
