# `/System/Library/Filesystems/apfs.fs/fsck_apfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 579,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2080)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/FSKit.framework/FSKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`

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

## Strings (2,003)

```
       -D            scavenge disk\n
(oid 0x%llx) %s: using old subtype (0x%x, expected 0x%x)\n
failed to validate %s object, retrying as %s\n
speculative download xattr (id %llu): unknown flags: %x\n
Space Verification failed.
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode kek%s\n
%s (id %llu): invalid bsd_flags (0x%x)\n
%s (id %llu): expected physical block number for extent at offset %lld\n
error writing object: %s\n
ersb_recovery_extents_count == 0, but ersb_recovery_length is non-zero (%llu)\n
obj-id: ??? type: ???\n
enabling overallocation repairs because -o was passed; this may cause data loss\n
encrypt
%s (id %llu): number of sparse bytes (%llu) is larger than alloced_size (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list entry (%u, %u)\n
%s (id %llu): invalid parent_id (%llu)\n
performed too many chained-key iterations (current id %llu); aborting dir-stats repairs\n
can't unmark purgeable (file_id %llu) for cross checks\n
%s/nx
%-20s%-15s\n
ERROR
fsroot tree is invalid.
omap (oid 0x%llx): invalid om_tree_type (0x%x)\n
Cache average %s time:
could not insert extent with range (%llu + %llu) for physical extent repair: %s\n
repair_overlapped_extents: update target pext 0x%llx\n
omap entry (oid 0x%llx): invalid ok_xid (0x%llx)\n
%s (%llu+%llu): entry %u with size %u brings total size %u beyond object size %u\n
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
nx_xp_data_index (%u) puts the checkpoint data outside of its range\n
spaceman cib count %u is inconsistent with chunk count %llu and chunks per cib %u\n
%s (id %llu): unknown flags: (0x%02x / known flags are: 0x%02x)\n
%s (id %llu): xf %u/%u: %s: invalid dstream\n
need to clear bsd flags (0x%x) in inode (object-id %llu)\n
file info: attribution tag (hash %llu): physical size does not match expected value (%llu)\n
%s (id %llu): Unexpected hash size (%u != %u)\n
clone mapping (private_id %llu, file_id %llu): unknown flags (0x%x / known flags are: 0x%x)\n
dir stats
Unknown type %d
integrity_meta: (0x%llx:0x%llx): unknown hash type (%u)\n
%s (id %llu): xf %u/%u: %s: found in an unsupported volume\n
INO_EXT_TYPE_RDEV
\t\t<array>\n
Invalid disk file-descriptor passed\n
failed to get inode (id %llu) dstream: %s\n
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on directory without INODE_MARK_CHILD_PURGEABLE flag\n
phys extent
%s:%d: failed to open container device %s: %s\n
clone mapping
failed to search for clone mapping (private_id %llu,  file_id %llu): %s (%d)\n
omap snapshot: invalid oms_pad (0x%x)\n
physical extent
zero type/id
cannot find checkpoint area because container superblock is too damaged\n
NX jumpstart record range is invalid: 0x%llx+%llu\n
Fix btree: bt_node_count (%llu)? 
not a leaf
error (%d) looking up spaceman IP block address at index %u\n
Corrupt
%s (id %llu): xf %u/%u: %s: invalid x_type (%u)\n
need to clear flags (0x%llx) in inode (object-id %llu)\n
Expanded
Space Verification: failed to insert paddr (%llu) error : %s\n
detected invalid fsroot tree nodes (& thus data loss), pruning the nodes to make the system usable\n
inode (id %llu) has a stale dir_stats (id %llu)\n
gbitmap_blk
overallocation
Checking the fragmented metadata trees.
** 
failed to insert snap_name entry: %s\n
%s (id %llu): xf %u/%u: %s: found nlink x-field but volume has dir-nlink in core-inode\n
%s (id %llu): invalid key length (%u), given name_len (%u)\n
%s (id %llu): extent crypto flag set on unencrypted volume\n
object (oid 0x%llx): o_xid invalid, o_xid %llu is greater than nx_next_xid: %llu\n
Internal
\tactual hash:   %s\n
Failed to unwrap encrypted volume keybag using the provided password: %s\n
inode (jobj_id %llu): unable to add repair for unexpected xfield: %s\n
SUCCESS
apfs object (oid 0x%llx): cpflags (%u) should be 0\n
found invalid fsroot btree node key id (%llu)\n
repair_overlapped_extents: failed to copy paddr 0x%llx to paddr 0x%llx, block_count 0x%llx: %s\n
omap (oid 0x%llx): invalid om_pending_revert_max (0x%llx), given om_flags (0x%x)\n
omap entry (oid 0x%llx): invalid tweak type (%u) given ov_flags (0x%x)\n
error starting transaction: %s\n
Checking the APFS volume superblock.
failed to read spaceman cab %u at address 0x%llx\n
Fix apfs_next_doc_id(oid 0x%llx, xid 0x%llx)? 
object (oid 0x%llx): unable to add omap repair: %s\n
found file extent gap (id %llu) at logical address %llu (expected %llu)\n
%s (id %llu): invalid internal_flags (0x%llx) given unassigned default_crypto_id\n
descendants
can't add purgeable size for dir-stats: %s (%d)\n
media keybag
_fd_dev_write
can't add attribution tag for clonegroup: %s (%d)\n
IOService
%s (id %llu): Logical address %llu of data hash not a multiple of the hash chunk size (%u)\n
object (oid 0x%llx): Unable to mark nx checkpoint desc range (0x%llx + %u) allocated for space verification\n
Spaceman Repair: failed to allocate memory for the bitmap block\n
failed to initialize the omap snap tree: %s\n
sfqe_key : (paddr 0x%llx, xid 0x%llx) : invalid xid\n
apfs superblock at index %u: apfs_pfkur_tree_type is invalid: 0x%x\n
inode (id %llu): found unexpected security xattr\n
container omap
reaper list entry (index (%u) list oid (0x%llx)) : is not valid as per flags(0x%x)\n
repair_overlapped_extents: unable to free space for target_paddr 0x%llx block_count 0x%llx: %s\n
failed to lookup doc-id %u error : %s\n
%s (id %llu): invalid file_id (%llu) (%s)\n
pad1: 0x%x \n
Requested cache size: %s (%uk blocks * %ukB)\n
Cache %s time:
alloced_size of dstream (object-id %llu) does not match minimum found size (%llu)\n
NX checkpoint desc range is invalid: 0x%llx+0x%x\n
gen-count: %u nchildren: %d \n
0
       -T            tree node repair\n
found invalid directory record object (id %llu)\n
cpm_count is 0\n
\t\t<key>%s</key> <integer>%u</integer>\n
Failed to allocate memory for cab\n
%s (%llu+%llu): oti_ke_blob_cksum (0x%llx) is invalid for blob\n
encrypted
omap entry (oid 0x%llx): invalid crypto key index (%u) given ov_flags (0x%x)\n
Snapshot (0x%llx): apfs_integrity_meta_oid is invalid\n
%s (id %llu): invalid pad1 (0x%hx)\n
%s (id %llu): xf %u/%u: %s: sparse_bytes set even though inode is not sparse\n
found dir-stats object (id %llu; flags 0x%x) with bad chained key (%llu/%llu)\n
checkpoint<->%s mismatch on nx_xp_desc_blocks: %d %d\n
unable to iterate snap fsroot tree for tree node repairs: %s\n
xattr record too small (%u)\n
Fix %s (0x%llx+%llu) bitmap address (0x%llx)? 
Checking the extent ref tree.
clone mapping (private_id %llu, file_id %llu): compressed physical size (%llu) != inode (id %llu) compressed physical size (%llu)\n
clone mapping (private_id %llu, file_id %llu): dir stats key (%llu) != inode (id %llu) dir stats key (%llu)\n
Unset unknown flags? (0x%llx) 
Container superblock is invalid.
kek group
%s (%llu+%llu): failed to allocate memory\n
block 0 superblock
Set missing flags? 
|\n
hash validation: invalid node hash for node %llu (hash type: %u, hash size: %u, root oid: %llu, seal xid: %llu, broken xid: %llu)\n
failed to insert dir-stats entry %llu into the repair tree\n
need to make file extent with missing crypto state (id %llu) at logical address %llu+%llu sparse\n
failed to sparse VEK extents for resource fork of inode (%llu): %s\n
Fix spaceman free queue tree sfq_count (oid 0x%llx)? 
Spaceman Repair: Cannot modify more than a block's worth of bitmap\n
\t\t[%4llu - %4llu) [%4s] = %d\n
Device Characteristics
Set
encryption rolling recovery data extends past recovery length, oid 0x%llx, ersb_recovery_length %llu, accumulated length %llu\n
error iterating trees during free queue tree repair: %s\n
REQUIRE_func
Fix internal flags (0x%llx)? 
origin_id (%llu) of dir-stats object (id %llu) is not as expected (%llu)\n
failed to allocate memory to find dir-stats %llu\n
er_state->ersb_version is %d, should be at most %d\n
INO_EXT_TYPE_UNRAW_SIZE
uncompressed-size: 0x%llx \n
apfs superblock at index %u: apfs_total_blocks_freed (%llu) should not be greater than apfs_total_blocks_alloced (%llu)\n
last reap list object 0x%llx doesn't match tail 0x%llx\n
container %s is mounted.\n
%s (id %llu): xf %u/%u: %s: invalid doc_id (%u), less than MIN_DOC_ID (%u)\n
%s (id %llu): class %u file references per-file crypto_id (%llu) but is missing INODE_PROT_CLASS_EXPLICIT\n
failed to cross check purgeable inode: %d (%s)\n
found orphan/invalid purgeable record (file_id %llu, atime %llu)\n
get_fext_tree() called on unsealed volume\n
fv_get_blob_state
omap (oid 0x%llx): invalid om_pending_revert_min (0x%llx), given om_flags (0x%x)\n
found dir-stats object (id %llu) that is both shadow and calculating\n
sm: sm_free_count (%llu) is not valid (%llu)\n
omap
error (%d) getting cab %u @ %lld\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unexpected btn_btree.bt_fixed.bt_flags (0x%x)\n
%s (id %llu): invalid value length (%u)\n
iOS encryption rolling state object: (version %u) current_state unset, yet non-zero current_id (%llu)
nx_spaceman_oid is invalid\n
INO_EXT_TYPE_DELTA_TREE_OID
%s (id %llu): found attribution tag on a volume that doesn't support them\n
sec
failed to register the purgeable tree in the fsck memory storage\n
btree node
failed to allocate memory for repair\n
Fix crypto_id (%llu)? 
Fix apfs_num_directories(oid 0x%llx, xid 0x%llx)? 
 embedded data size: %d\n
ersb_total_blk_to_encrypt (%llu) exceeds bm_bit_count (%llu)\n
(oid 0x%llx) %s: invalid encryption type ov_flags (0x%x)\n
found spaceman free queue tree entry (0x%llx, xid %llu) which overlaps with existing range\n
directory valence check: directory (oid 0x%llx): nlink (%d) does not match subdirectory count (%d)\n
Space Allocation: failed to allocate memory\n
%s (id %llu): invalid full clone size (%llu) for hash (%llu)\n
bitmap store: address %llu is beyond maximum allowed %llu\n
purgeable record (atime %llu, file_id %llu) is different than inode atime (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: validate_loc_ctx_alloc failed for btn_nkeys (%u)\n
error allocating encryption rolling recovery data buffer, ersb_recovery_length %llu\n
failed to init fsroot tree for file lookup in purgatory directory\n
1
Could not open error file: %s\n
%s (id %llu): failed to register dir-stats (%llu) purgeable_size: %d\n
sm_fs_reserve_alloc_count is not valid (expected %llu, actual %llu)\n
failed to update clone mapping (private_id %llu,  file_id %llu) with compressed clone size: %s (%d)\n
xf: xf_used_data (%u) is larger than expected (%u)\n
CryptoState
fstype
failed to initialize the doc-id tree: %s\n
%s (%llu+%llu): number of keys %u does not match number of entries found %u\n
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) must not be greater than apfs_fs_quota_block_count (%llu)\n
nx_xp_data_len (%u) is larger than nx_xp_data_blocks (%u)\n
category
volume metadata
Object map is invalid.
File extent tree is invalid.
clone mapping (private_id %llu, file_id %llu): failed to update dir stats %llu: %s (%d)\n
refcnt (%u) of dstream id object (id %llu) is less than expected (%u)\n
omap (oid 0x%llx): invalid om_most_recent_snap (0x%llx), given om_flags (0x%x)\n
Fix om_snap_count (oid 0x%llx)? 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x)\n
spaceman IP bitmap blocks field is %u, but sum of ranges is %llu\n
can't add dir stats key for clone mapping: %s (%d)\n
Fix apfs_num_other_fsobjects(oid 0x%llx, xid 0x%llx)? 
%s (id %llu): xf %u/%u: %s: extended field at offset %u+%u extends beyond xf_used_data (%u)\n
Could not initialize omap tree (oid 0x%llx): %s\n
file info: found orphan attribution tag with hash (%llu)\n
%s (id %llu): invalid dir_nlink (%d)\n
sparse bytes overflow (current %llu, update %llu)\n
Remove entry with invalid blob? 
fp=%d fl=%d repairs=%d time=%ld iter=%d\n
Set internal_flags to 0x%llx? 
iOS encryption rolling state object: xattr invalid storage type, flags (%hu)\n
file info: inode (jobj_id 0x%llx) has unexpected attribution tag with hash (%llu)\n
omap snapshot: oms_oid should be unused but has value (0x%llx)\n
%s (%llu+%llu): block range isn't a valid keybag, skipping checks\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list entry (%u, %u)\n
%s (id %llu): invalid parent_id (%llu) for root directory\n
%s (id %llu): sparse bytes mismatch for a file in the purgatory\n
Remove entry with invalid blob range? 
File key rolling tree is invalid.
failed to allocate memory for the bitmap block\n
fsckPrintXML
xf: xf_num_exts (%u) extended fields do not fit in the given xf_used_data (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key (%u, %u)\n
zero type
repair_overlapped_extents: unable to update fext 0x%llx 0x%llx for fs_oid 0x%llx: %s\n
error (%s) failed to populate free queue trees \n
error copying on-disk free queue tree into reordered tree in memory: %s\n
--------
succeeded.
cpm_map[%d].cpm_type object type (0x%x) is invalid!\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btn_btree.bt_fixed.bt_key_size (%u) and btn_btree.bt_fixed.bt_val_size (%u)\n
Status
%s (id %llu): invalid gen_count (%llu)\n
inode (id %llu): finder info internal flag is unexpectedly set\n
object (oid 0x%llx): o_subtype invalid, o_subtype 0x%x should be 0x%x\n
could not look up cpm_map[%d].cpm_paddr (%llu) in checkpoint data area\n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/platform/platform.c
miss
speculative download xattr (id %llu): unknown purge reason: %u\n
nx_uuid is NULL\n
SiblingLink
%s%llu.%.*s %cB%s
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys enable%s\n
xp_map->cpm_map[%d].cpm_size is 0\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btn_level (%u)\n
invalid ersb_flags (0x%llx), exactly one of ERSB_FLAG_ENCRYPTING and ERSB_FLAG_DECRYPTING bits must be set\n
failed to run predicate callback on inode (oid 0x%llx) for lookup in directory: %s\n
failed to allocate memory to add an xfield\n
object (oid 0x%llx): Unable to mark spaceman ip bitmap range (0x%llx + %u) allocated for space verification\n
(void *)m->msg == (void *)fmt
_bind_unmanaged_vek
(oid 0x%llx) %s: should be encrypted (ov_flags 0x%x)\n
(oid 0x%llx) %s: invalid o_oid (0x%llx)\n
%s xfield of dir-stats object (id %llu) does not match expected value (%llu)\n
NX blocked out range is invalid: 0x%llx+%llu\n
error (%d) reading spaceman IP bitmap block at index %u, addr 0x%llx\n
found spaceman free queue tree entry (0x%llx+%llu, xid %llu) which overlaps with existing range (0x%llx+%llu)\n
IP
Fix apfs_num_snapshots(oid 0x%llx, xid 0x%llx)? 
Invalid disk file-descriptor path\n
found orphan %s (id %llu, size %llu)\n
Insert missing %s objects? 
checkpoint %d (xid %llu) superblock disagrees with block 0\n
snap_meta_ext: (0x%llx:0x%llx): invalid xid (0x%llx)\n
%s (id %llu): invalid private_id (%llu)\n
failed to insert node at segment (%llu) error : %s\n
iOS encryption rolling state object: (version %u) lite rolling has invalid current_state (%u)\n
y
failed to traverse doc-id tree : %s\n
%s (%llu+%llu): oti_ke_blob_len (%u) is too large\n
er_state magic number is %d, should be %d\n
spaceman chunk %llu wrong number of blocks: %u, expected %u\n
Truncate alloced_size to block size? 
com.apple.fs.cow-exempt-file-count
shadow dir-stats object (id %llu) unexpectedly marked as having origin-id\n
%s (%llu+%llu): entry %u has blob size == 0\n
speculative download xattr (id %llu): invalid flags: 0x%x\n
no snap_meta entry found for snap_name entry with xid %llu and name %.*s\n
apfs superblock at index %u: apfs_pfkur_tree_oid is invalid.\n
Failed to get keybag entry with tag %d for volume %s\n
%s: could not iterate reaper for omap space verification\n
bitmap store: reached limit of %llu B-tree nodes\n
failed to cross check purgeable record: %d (%s)\n
Volume %s has revert_to_xid set, skipping the fsroot tree.\n
       -q            quick check if the superblock and checkpoint superblock are valid.\n
%s (id %llu): xf %u/%u: %s: found nlink field even though inode is not a directory\n
%s (id %llu): invalid dstream.default_crypto_id (%llu)\n
clonegroup (group id %llu, private_id %llu, file id %llu): private_id is invalid\n
free_overlapped_range: unable to free space for source_paddr 0x%llx block_count 0x%llx (leak): %s\n
clone mapping (private_id %llu, file_id %llu): attribution tag (%llu) != inode (id %llu) attribution tag (%llu)\n
%s (id %llu): invalid internal_flags (0x%llx) given volume readonly compatible features (0x%llx)\n
failed to initialize the pfkur tree: %s\n
Fix ci_free_count (%u)? 
Fragmented metadata trees are invalid.
spaceman ip bitmap block xid is invalid: %llu > %llu\n
AppleAPFSMedia
file info: orphan attribution tag with hash (%llu)\n
dev_read
cpm_flags has invalid flags set: 0x%x\n
DREC_EXT_TYPE_DIR_GEN_COUNT
uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %.*s\n
fsck_msg_string
failed to get cib for chunk index %llu: %s\n
Could not read nx_reaper_list object (oid (0x%llx)): %s\n
The volume %s cannot be repaired when it is in use.
file-id: %6lld flags: %d date-added: %lld name-len: %d name: %.*s\n
clone mapping (private_id %llu, file_id %llu): invalid file_id\n
Volume superblock is invalid.
found dstream (id %llu) with missing crypto state object (id %llu)\n
extended attribute (id %llu, name %.*s) is orphan\n
speculative download xattr (id %llu): pristine time (%llu) is greater than current time (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: key (%u) compare error: %d\n
alloced_size (%llu) of dstream (id %llu, object-id %llu) does not match minimum found size (%llu)\n
%s (id %llu): xf %u/%u: %s: invalid shadow_key (%llu)\n
could not remove extent at %llu for physical extent repair: %s\n
oms: 
reaper list entry (index (%u) list oid (0x%llx)) : entry is not referenced\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_key (expected %u, actual %u)\n
%s BTNODE_LEAF flags? 
obsolete spaceman tier2 fields should be empty but they aren't\n
fd_dev_read_extended
nx_flags (0x%llx) has an unknown flag set \n
spaceman datazone zone id is zero but other fields are initialized\n
spaceman struct ranges %u+%u and %u+%u overlap\n
object (oid 0x%llx): Unable to mark omap entry for omap space verification \n
(oid 0x%llx) %s: should not be encrypted (ov_flags 0x%x)\n
DIR_STATS_EXT_TYPE_SHADOW_KEY
inode with file-id %llu has doc-id %u but doc-id is already in use\n
The volume %s with UUID %s could not be verified completely.
found multiple clonegroup records for file_id %llu\n
unexpected: space verification data structure not initialized
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) is greater than spaceman reserve block count (%llu) for a guaranteed-minimum space FS\n
Failed to allocate memory\n
%s (id %llu): xf %u/%u: %s: found zero rdev on char/block device (mode %u)\n
nx_newest_mounted_version is less than expected: %s\n
ersb_snap_xid (%llu) is greater than or equal to container next xid (%llu)\n
crypto state
expanded directory stats
logical addr: %lld  phys-block-num: %lld  crypto-id: %lld  len: %lld  flags: %x\n
container %s is mounted. repairs in a mounted container is not supported yet.\n
found unexpected crypto state object (id %llu, refcnt %u)\n
%s (%llu+%llu): entry %u has blob size %u > maximum blob size %u\n
INO_EXT_TYPE_DOCUMENT_ID
option -X is specified but FSKit is not present, ignoring\n
%s (id %llu): xf %u/%u: %s: SAF dir-stats key found on non origin ino (%llu)\n
%s (id %llu): xf %u/%u: %s: uuid is NULL\n
%s (%llu+%llu): number of entries %u exceeds object capacity %lu\n
NX keybag data range is invalid: 0x%llx+%llu\n
unable to mark allocated blocks for volume oid %llu\n
Volume object map space verification failed.
%d$@
found orphan file extent (id %llu) at logical address %llu\n
error iterating fsroot tree during dstream repair: %s\n
failed to remove node at segment (%llu) error : %s\n
mismatch between extentref entry reference count (0) and calculated fsroot entry reference count (%d) for extent (%llu + %llu)\n
nx_fusion_mt_oid should be invalid but isn't\n
Fix default_crypto_id (%llu)? 
SAF descendants
encryption rolling gbitmap tree is invalid\n
Remove entry with null UUID? 
efi_jumpstart
%s: can't create path to container\n
%s (id %llu): failed to update dstream (%llu)\n
unable to get dir-stats key of inode (id %llu) to repair dir-stats chained key: %s\n
Unable to perform deferred repairs without full space verification\n
unable to init fsroot tree for dstream repair\n
%s (id %llu): invalid inum (%llu)\n
failed to allocate memory for dir-stats lookup\n
error iterating fsroot tree for file lookup in directory: %s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s icloud recovery key%s\n
w
%s (id %llu): dstream xf does not exist, despite existence of sparse bytes xf\n
NX checkpoint data range is invalid: 0x%llx+0x%x\n
clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n
%s: fsck_apfs completed at %s\n
failed to remove INODE_PROT_CLASS_UPGRADE_ROLLIP flag for inode (%llu): %s\n
file info: attribution tag (hash %llu) skipping clone size repair: full clone size %llu > %llu\n
%s (id %llu): invalid state.key_os_version (%u)\n
expanded key (id %llu) on incompatible volume\n
??? (id %llu): invalid key length (%u)\n
mismatch between extentref entry reference count (%d) and calculated fsroot entry reference count (0) for extent (%llu + %llu)\n
%d%d-%d
Spaceman free queue tree of type [%d] is invalid\n
       -d            print extra debugging information\n
/dev/
%s (id %llu): invalid type (0%o)\n
apfs superblock at index %u: apfs_revert_to_xid is %llu, but sblock oid is invalid\n
detected chained-key loop involving dir-stats %llu\n
Look for missing items in %s directory.
Round %s ov_size (oid 0x%llx) to block size? 
iOS encryption rolling state object: xattr record too small (%zu)\n
nx_xp_desc_index (%u) is larger than nx_xp_desc_blocks (%u)\n
unable to init iterators for free queue tree repair: %s\n
Too many warnings of this type generated; suppressing subsequent ones.\n
aborting jobj validations for current fsck pass - trying to repair fsroot tree with invalid nodes\n
%s (id %llu): xf %u/%u: %s: invalid name (%.*s), given name_len (%u)\n
unable to load dir-stats %llu to retrieve attributes: %s\n
. . .\n
a
Volume %s is incompletely restored, skipping the fsroot tree.\n
%s (id %llu): invalid nlink (%d)\n
%s (id %llu): invalid dir-stats flags (0x%x) on volume without attribution tags\n
found orphan omap mapping (oid %llu xid %llu)\n
%s (id %llu): xf %u/%u: %s: directory nlink value %lld is greater than nchildren (%d)\n
found %s file extent object (id %llu) at logical address %llu\n
%s (id %llu): signing id does not exist\n
checkpoint map o_xid (0x%llx) doesn't match checkpoint superblock o_xid (0x%llx)\n
can't allocate memory to insert a new clone mapping value\n
repair_overlapped_extents: encryption is rolling for fs_oid 0x%llx\n
\nTotal blocks marked by fsck: %llu\n
Checking the file extent tree.
Could not initialize gbitmap tree (oid 0x%llx): %s\n
checksum block size is invalid, checksum_block_size enum: %llu\n
INO_EXT_TYPE_DSTREAM
file-id: %6lld flags: %d date-added: %lld hash: 0x%x name-len: %d name: %.*s\n
apfs superblock at index %u: apfs_fext_tree_type is invalid: %u\n
Set INODE_PROT_CLASS_EXPLICIT? 
failed to mark cached doc-id tree record %d as verified error : %s\n
Fix the keybag size? 
Repairing volume.
spaceman ip bm range (%llu, %llu) overlaps with spaceman ip range (%llu, %llu)\n
file info
%s (id %llu): Invalid hash at offset %llu\n
sealed volume fsroot corruptions cannot be repaired and will automatically be skipped\n
device_is_mounted(%s) failed with error: %s\n
file extent length %llu does not fit inside %u bits, refusing to repair\n
%s (id %llu): invalid name_len (%u), given value length (%u)\n
sm
fd_dev_write_extended
invalid checksum block size, enum: %llu\n
Total blocks allocated by spaceman: %llu\n\n
BSD Name
%s (id %llu): invalid nchildren (%d)\n
inode (id %llu): security xattr internal flag is unexpectedly set\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 2%s\n
purgeable inode (id %llu) is missing a purgeable record\n
sm : free queue tree has sfq_count (%llu) greater than available block count (%llu)\n
(oid 0x%llx) %s: invalid object address (0x%llx)\n
inode (id %llu): need to set internal_flags 0x%llx\n
checkpoint<->%s mismatch on nx_xp_data_blocks: %d %d\n
pfk_val : object (oid 0x%llx): unknown version (%u)\n
failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) flags: 0x%x repair: %s\n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/platform/platform_lib.c
unable to init fsroot tree to enqueue dir-stats repairs\n
REPAIR
\texpected hash: %s\n
failed to search for clone mapping (private_id %llu,  file_id %llu) to update compressed clone size: %s (%d)\n
invalid
%s (id %llu): dstream.alloced_size (%llu) is not a multiple of the block size (%u)\n
no valid checkpoint found\n
checkpoint %d (xid %llu) superblock is invalid\n
error (%d) looking up spaceman IP block address at index %llu\n
%s%s%llx
%s (id %llu): uncompressed_size/rdev/dir_nlink union field is set (%llu) but inode flags and mode do not indicate it should (flags: 0x%llx, mode %u)\n
apfs_root: 
Rechecking volume.
failed to initialize the fext tree: %s\n
AppleAPFSContainerScheme
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_node_size (%u), given mt_node_size (%u)\n
integrity_meta: (0x%llx:0x%llx): invalid root hash offset (%u+%u) > %u\n
refcnt of crypto state object (id %llu) is %s than expected (%u)\n
recovery extent #%llu: checksums at offset %llu, length %llu exceed ersb_recovery_length %llu\n
Checking the NX evict mapping tree.
apfs superblock at index %u: apfs_extentref_tree_oid is invalid.\n
apfs_next_obj_id is not valid (expected %llu, actual %llu)\n
error updating snap_meta entry: %s\n
resource fork size
Space manager free queue trees are invalid.
Encryption key structures are invalid.
%s (id %llu): found dstream with unassigned default_crypto_id\n
inode (id %llu): unknown compression type: %u\n
parameters
reap list object 0x%llx first index %u larger than max index %u\n
reap list tail 0x%llx is not last reap list object, next 0x%llx\n
failed to read object (oid (0x%llx)) being reaped from disk \n
Fix object (oid 0x%llx) subtype? 
 *****
missing crypto state object (id %llu) referenced by %u file extents / dstreams\n
data_hash: object (oid 0x%llx): Invalid length at offset %llu\n
%s (id %llu): xf %u/%u: %s: invalid SAF dir_stats_key (%llu)\n
gbitmap: 
File/folder %s may be damaged.
ersb_recovery_length (%llu) exceeds recovery length limit (%llu), some checks will be disabled\n
sibling link
reached invalid tree node limit %llu for fs_oid %llu\n
msec
object (oid 0x%llx): o_oid invalid\n
/..namedfork/rsrc
spaceman free count is too large: %llu > %llu\n
OTI
fsck_msg_number
%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh, Unexpected short PDK len%s\n
snap_meta_ext: (0x%llx:0x%llx): sme_uuid is NULL\n
%s (%llu+%llu): entry %u has size %u > maximum size %u\n
NX checkpoint data blocks field is %u, but sum of ranges is %llu\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list offset %u\n
PURGEABLE_EXT_TYPE_DIR_GEN_COUNT
%s (id %llu): failed to register attribution tag: %d\n
%s (id %llu): extent crypto flag missing on encrypted volume\n
%s: %llu orphan mappings found\n
snapshot fsroot / file key rolling / doc-id / clone group tree corruptions are not repaired; they'll go away once the snapshot is deleted\n
val size is too small, actual: %u, minimum: %u\n
Fix apfs_next_obj_id(oid 0x%llx, xid 0x%llx)? 
shadow dir-stats object (id %llu) unexpectedly has origin-id\n
(oid 0x%llx) %s: invalid ov_flags (0x%x), crypto key index set for unencrypted object\n
btn
origin_id of dir-stats object (id %llu) does not match expected value (%llu)\n
nx_xp_desc_next (%u) is larger than the # of nx_xp_desc_blocks (%u)\n
checkpoint %d (xid %llu) failed consistency check\n
error (%d) writing spaceman IP bitmap %d @ %lld\n
object (oid 0x%llx): o_cksum (0x%llx) is invalid for object\n
apfs superblock at index %u: apfs_unmount_time (%llu) is greater than current time (%llu)\n
fv_create_pdk
found a snapshot in the purgatory (xid %llu) with no corresponding omap entry\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list length (%u), given total value length (%u)\n
snapshot metadata
%s:%spid:%d,%s:%s%s%s%s%s%u:%s personal recovery key%s\n
%s (id %llu): unknown flags (0x%x / known flags are: 0x%x)\n
%s (id %llu): extent crypto flag set on sparse extent\n
cpm_map[%d].cpm_fs_oid (%llu) is less than minimum oid (%u)!\n
SnapMetadata
repair_overlapped_extents: unable to remove source pext 0x%llx for fs_oid 0x%llx (pext leak): %s\n
%s (id %llu): uncompressed size is set (%llu) but has-uncompressed-size flag is not set (flags: 0x%llx)\n
Invalidate spaceman ip bm free list at index at index %u? 
%s (id %llu): invalid dstream\n
Fix object (oid 0x%llx) omap flags? 
error iterating snapshot tree: %s\n
evict mapping range is invalid: (0x%llx+%llu --> 0x%llx+%llu)\n
volume
dir_stats (id %llu) already has a registered origin (id %llu), but we found another one (id %llu)\n
Failed to fix %s\n
spaceman chunk %llu wrong free count: %u, expected %u\n
clone mapping (private_id %llu, file_id %llu): physical size (%llu) != inode (id %llu) physical size (%llu)\n
failed to initialize the snap meta tree: %s\n
Fix btree: bt_longest_key (%u)? 
clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect attribution tag (%llu)\n
purgatory.
verification/reading of the nx_reaper object failed\n
SiblingMap
num children: %lld total size: %lld gen-count: %lld\n
refcnt (%u) of crypto state object (id %llu) is greater than expected (%u)\n
Allocated (%llu) MB for cached btrees in %u blocks, limit is (%llu) MB\n
fsck_apfs completed at %s\n
container has been mounted by APFS version %s, which is newer than %s\n
resource fork size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
found unexpected %s xfield associated with inode (object-id %llu)\n
Trimming unused blocks.
inode
       -s            print space verification summary\n
Failed to get password for encrypted volume from provided file descriptor: %s\n
xf: xf total size (%u) is larger than UINT16_MAX\n
%s (%llu+%llu): %s records entry %u contains invalid range %llu+%llu\n
btree node (oid (0%llx)) being reaped is hashed\n
unable to enqueue tree node insertion repairs: %s\n
inode (id %llu): dataless bsd_flag is set, but compression bsd_flag is not\n
iOS encryption rolling state object: current_offset (%llu) too large\n
PROGRESS
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null KEK, file radar%s\n
%s (id %llu): xf %u/%u: %s: found on a non class F file\n
live repair of a volume in mounted container %s is not supported yet.\n
spaceman blocks per chunk %u is inconsistent with block size %u\n
%s xfield of inode object (id %llu) does not match expected value (%llu)\n
nx_xp_desc_len (%u) is less than 2\n
Spaceman internal pool fragmented metadata tree is invalid\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid cpm_size or ov_size (%u), given btn_btree.bt_fixed.bt_node_size (%u)\n
 out-of-line data size: %lld (under obj-id: %lld / crypto-id: %lld)\n
Disabling fsck cross checks of %s tree\n
%s (%llu+%llu): entry %u has invalid padding\n
(oid 0x%llx) %s: _xp_lookup_obj(0x%llx): %s\n
failed to repair inode nlink (id %llu): %s\n
 type: %u hash: 0x%llx total_count: %llu physical_size: %llu flags: 0x%x\n
could not open %s to freeze the volume: %s\n
spaceman datazone invalid previous boundary index (%hu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s user uuid unexpectedly match new kek uuid%s\n
%s (id %llu): unknown flags: (0x%x / known flags are: 0x%x)\n
clonegroup (group id %llu, private_id %llu, file id %llu): invalid value length (%u)\n
clone group mapping record missing for (group_id %llu, private_id %llu, file_id %llu)\n
spaceman
%s: %s%s
doc id
apfs_extentref: 
%s (id %llu): Logical address %llu of file extent not a multiple of the block size (%u)\n
object (oid 0x%llx): Unable to mark the omap entry of the apfs_snap_meta_ext_oid in use for omap space verification\n
       -o            repair overallocations; please do not run an older fsck_apfs on newer systems with this option\n
??? (id %llu): invalid key type (%u)\n
failed to init the dir stats repair tree\n
tried to remove %s object but it wasn't there!\n
The volume name is %s
\t\t\t<dict><key>%s</key> <string>%s</string></dict>\n
extent ref tree
spaceman ip bm block count is bad: %d\n
found fext (id %llu) with missing crypto state object (id %llu)\n
com.apple.fs.graft-jobj-id-base
DAMAGEINFO
spaceman cab count %u is inconsistent with cib count %u and cibs per cab %u\n
could not allocate array of %u entries for tracking omap objects in reap list; skipping subsequent ones\n
(oid 0x%llx) %s: found a bit flip in the header\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u), given btn_flags (0x%x)\n
found solo clonegroup inode: (group_id %llu, private_id %llu, file_id %llu)\n
repair_overlapped_extents: unable to insert target pext 0x%llx for fs_oid 0x%llx: %s\n
 type: %u\n
Allocate new doc-id %u for file-id %llu? 
sealed volume hash records
dir_nlink of inode object (id %llu) does not match expected value (%d)\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
failed to allocate memory to read the container superblock\n
dstream id
unable to lookup latest snap xid: %s\n
Fix overlapped extents? 
DirRecord
apfs superblock at index %u: apfs_fs_flags has conflicting encryption flags 0x%llx\n
Fix inode_val: internal_flags (0x%llx)? 
%s (id %llu): Found data hash on unsealed volume\n
reap list expected %u objects, but got last reap list object with %u more objects left\n
flags of dir-stats object (id %llu) does not match expected value (0x%x)\n
encryption rolling recovery block with data size 0, oid 0x%llx, nx_block_size %u, recovery length %llu\n
Enabling idle sleep, %s\n
clone group mapping record exists for (group_id %llu, private_id %llu, file_id %llu), but no inode refers to it\n
Checking volume %s.
apfs superblock at index %u: apfs_doc_id_tree_type is invalid: %u\n
%s (id %llu): invalid length (%u), given state.key_len (%u)\n
encountered more than %u omap objects in reap list; skipping subsequent ones\n
Xattr
snap_meta_ext: object (oid 0x%llx): no record for snapshot (xid 0x%llx)\n
%s (id %llu): invalid nonzero crypto_id (%llu) on unencrypted volume\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u\n
%s (%llu+%llu): UUID %s of entry %u (tag %u) does not reference any volume\n
compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n
%s (id %llu): invalid type (%u)\n
clonegroup (group id %llu, private_id %llu, file id %llu): invalid physical_size (%llu)\n
iOS encryption rolling state object: current_xattr is unterminated\n
could not open %s to prevent reclaims: %s\n
found file extent (id %llu) at logical address %llu beyond the end of the dstream %llu\n
%s (id %llu): invalid pad2 (0x%x)\n
%s (id %llu): xf %u/%u: %s: found attribution tag on a volume that doesn't support them\n
Purgeable
Clear uncompressed size? 
object (oid 0x%llx): Unable to mark nx checkpoint data range (0x%llx + %u) allocated for space verification\n
sib-map: %lld\n
sm_fs_reserve_block_count is not valid (expected %llu, actual %llu)\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in free queue tree lies in the internal pool\n
compression xattr (id %llu): compression magic is unknown: 0x%x\n
iOS encryption rolling state object: cannot determine absence of ierso xattr\n
file (id %llu) isn't purgeable but its matching clonegroup record flags (0x%x) suggest it is\n
clonegroup-cookie
purgeable rsrc size
%s (%llu+%llu): version cannot be 0\n
physical size of dir-stats object (id %llu) does not match expected value (%llu)\n
iOS encryption rolling state object: cannot get ierso xattr\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given btn_flags (0x%x)\n
ersb_recovery_extents_count is non-zero (%llu), but ersb_recovery_list_oid == 0\n
DIR_STATS_EXT_TYPE_PURGEABLE_SIZE
apfs superblock at index %u: apfs_prev_doc_id_tree_oid is set (%llu), despite apfs_doc_id_index_flags (0x%x)\n
directory valence check: directory (oid 0x%llx): nchildren (%d) does not match drec count (%d)\n
other
can't remove orphan clone mapping (private_id %llu, file_id %llu): %s (%d)\n
Fix sme_snap_xid (xid 0x%llx)? 
%s (id %llu): xf %u/%u: %s: invalid attribution hash (%llu)\n
Could not iterate omap tree to read reaper objects (oid 0x%llx): %s\n
Deferred repairs skipped.
The volume %s with UUID %s was found to be corrupt and cannot be repaired.
a leaf
obj-id: %8lld type: %-11s\n
Performing deferred repairs.
%s%s%s\n
container %s is mounted with write access.\n
%s (id %llu): xf %u/%u: %s: invalid sibling_id (%llu)\n
nx_sb->nx_o.o_oid != OID_NX_SUPERBLOCK, %llu\n
the EFI jumpstart record magic number is invalid: 0x%x\n
refcnt %d len %lld owning_obj_id %lld\n
 revision: %u key len: %u
%s (id %llu): xf %u/%u: %s: failed to register dstream for crypto state tracking: %d\n
\t%-32s %.2lf [usec]\n
(oid 0x%llx) %s: found a bit flip at index 0x%x\n
failed to sparse VEK extents for inode (%llu): %s\n
apfs superblock at index %u: apfs reserve alloc count (%llu) is greater than spaceman reserve alloc count (%llu) for a guaranteed-minimum space FS\n
apfs superblock at index %u: apfs_vol_uuid is NULL\n
apfs superblock at index %u: apfs_fs_flags (0x%llx) PFK bit inconsistent with apfs_incompatible_features (0x%llx) PFK bit\n
refcnt (%u) of crypto state object (id %llu) is less than expected (%u)\n
malloc(%u)\n
n
apfs superblock at index %u: apfs_sec_root_tree_oid is invalid\n
inode (id %llu): compression type is dataless, but the dataless bsd_flag is not set\n
failed to add doc-id tree repair record, doc-id %u : %s\n
reaper head (0x%llx) and tail (0x%llx) should be both valid or both invalid\n
\t%-14s: %s\n
\t\t\t<integer>%d</integer>\n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/aeskeywrap.c
Conflicting options: [ -y ] option cannot be run with the [ -n | -l ] options\n
%s (id %llu): invalid key on expanded-records volume\n
unable to allocate memory to repair dir-stats chained key\n
overallocation detected on %s device: (0x%llx+%llu) bitmap address (0x%llx)\n
Fix apfs_clonegroup_next_id(oid 0x%llx, xid 0x%llx)? 
Remove orphan entry? 
found xattr (id %llu, name %.*s) with missing crypto state\n
%s (id %llu): xf %u/%u: %s: directory nlink value is invalid (%llu)\n
The volume %s was formatted by %s and last modified by %s.
failed to initialize the clone group tree: %s\n
a root
repair_overlapped_extents: unable to init extentref tree for fs_oid 0x%llx\n
spaceman fs_reserve_alloc_count %llu is greater than sm_fs_reserve_block_count %llu\n
error (%d) getting cib %u @ %lld\n
       -W            treat warnings as errors\n
unable to access %s: %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unexpected btn_flags (0x%x)\n
Skipping clonegroup cross-check since INVALID flag is set\n
PurgeableTombstone
repair_overlapped_extents: unable to target update target pext 0x%llx for fs_oid 0x%llx (refcnt leak): %s\n
   
%s (id %llu): file_id (%llu) and name (%.*s) mismatch for root directory\n
invalid extent address range (0x%llx+%llu)\n
(oid 0x%llx) %s: object is %s but should be %s\n
%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n
\t</dict>\n
spaceman chunk %llu free count %u > block count %u\n
verification/reading of the nx_reaper object failed: %s\n
unexpected key (%u) / val (%u) size in evict mapping tree\n
found orphan clone group mapping: (group_id %llu, private_id %llu, file_id %llu)\n
apfs object (oid 0x%llx): crypto major version (%u) is not CP_CURRENT (%u)\n
unable to get fsroot tree to repair missing crypto state\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_key_count (overflow)\n
Fix btree: bt_key_count (%llu)? 
ersb_flags (0x%llx) has ERSB_FLAG_PAUSED on but checksum count is non-zero (%u)\n
key size (%u)/val size (%u) is invalid\n
Fix apfs_fs_alloc_count(oid 0x%llx, xid 0x%llx)? 
       -E <path>     write warning/error information to <path>; Use \"-\" for stdout\n
%s: couldn't find APFS container\n
com.apple.apfs.
%s (id %llu): no rdev xf on char/block device (mode %u)\n
\t\t</array>\n
could not retrieve er_state_phys_t\n
Keybag size is too large\n
an origin and 
repair_overlapped_extents: unable to load fext 0x%llx 0x%llx for fs_oid 0x%llx: %s\n
apfs_num_directories is not valid (expected %llu, actual %llu)\n
BSD Minor
 descendants: %llu phys_size: %llu resource_fork_size: %llu gen_count: %llu chained_key: %llu flags: 0x%x\n
INFORMATION
\t<dict>\n
Fix apfs_doc_id_fixup_cursor? 
apfs superblock at index %u: unknown clone group tree flags: 0x%x\n
failed to register the dstream tree in the fsck memory storage\n
invalid EFI jumpstart record number of extents: %d\n
repair_overlapped_extents: update fext 0x%llx 0x%llx\n
apfs superblock at index %u: apfs_extentref_tree_type is invalid: 0x%x\n
Decryption
%d %%
QUICKCHECK ONLY; FILESYSTEM DIRTY
failed to add doc-id repair (deletion), doc-id %u : %s\n
com.apple.system.Security
%s (id %llu): zero rdev on char/block device (mode %u)\n
%s (id %llu): invalid dstream_id (%llu)\n
unable to flush deferred repairs: %s\n
chained key of dir-stats object (id %llu) does not match expected value (%llu)\n
%s:%d: can't get features for device (%s)\n
nx_max_file_systems (%u) is invalid\n
%s (id %llu): invalid internal_flags (0x%llx), (dir-stats SAF but not dir-stats maintained)\n
%s (id %llu): invalid hash (0x%x, expected 0x%x) of name (%.*s)\n
%s (id %llu): failed to register file info (hash %llu): %d\n
Fix object (oid 0x%llx) encryption? 
no valid checkpoint\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space (%u, %u), given btn_flags (0x%x)\n
INO_EXT_TYPE_CLONEGROUP_ID
 extentref_tree_oid: %lld sblock_oid: %lld change_time: %llu create_time: %llu\n
Restarting tree validation in case more minkey errors exist...\n
INO_EXT_TYPE_SNAP_XID
apfs superblock at index %u: apfs_fs_flags (0x%llx) inconsistent with apfs_incompatible_features secondary fsroot bit (0x%llx)\n
apfs superblock at index %u: apfs_volname[0] == 0\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n
_unlock_result
fd_dev_close
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list offset %u\n
%ld\n
spaceman block size %u doesn't match NX superblock block size %u\n
found clone mapping in an unsupported volume format\n
unable to init fsroot tree to enque purgeable repairs\n
DirStats
apfs superblock at index %u: apfs_doc_id_fixup_cursor is set (%llu), despite apfs_doc_id_index_flags (0x%x)\n
user
unable to load inode (oid 0x%llx) for file lookup in purgatory directory: %s\n
spaceman struct range %u+%u lies outside the struct itself (size %u)\n
%s (%llu+%llu): UUID %s of entry %u (tag %u) is not the container UUID %s\n
%s/apfs
%02x
vek group
error (%d) writing cib %u @ %lld\n
found orphan dir-stats object (id %llu)\n
ersb_recovery_extents_count is %llu, extent descriptor size is %zu, expected descriptors length is %llu > ersb_recovery_length %llu\n
PreventUserIdleDisplaySleep
Fix apfs_num_files(oid 0x%llx, xid 0x%llx)? 
clone group tree (id %llu): invalid cookie val length (%u)\n
can't add clone size for dir-stats: %s (%d)\n
pfk_val : object (oid 0x%llx): unknown flags (%u)\n
logical addr: %lld  phys-block-num: %lld  len: %lld  flags: %x\n
nrl
need to insert spaceman free queue tree entry (0x%llx+%llu, xid %llu) to replace existing overlapping ranges\n
%s (id %llu): invalid default_protection_class (%u)\n
found shadow key (%llu) on non-calculating dir-stats object (id %llu)\n
dev_read(%llu, 1): %s\n
Checking the file key rolling tree.
Checking the encryption key structures.
       -y            always repair (answer \"yes\" to questions)\n
%s (id %llu): xf %u/%u: %s: invalid name (%s)\n
found an orphan purgeable record (atime %llu, file_id %llu)\n
invalid gbitmap block oid 0x%llx\n
compression xattr (id %llu): internal flags are invalid (0x%x)\n
iOS encryption rolling state object: (version %u) timestamps unordered: start_time (%llu) <= end_time (%llu) <= current_time (%llu)\n
/var/log/fsck_apfs.log
%s: 
%s (id %llu): attribution tag xf exists, despite internal_flags (0x%llx)\n
failed to initialize the spaceman free queue tree %d: %s\n
checkpoint %d fsck_obj_phys failed\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x), given mt_btflags\n
encryption rolling recovery block offset mismatch, oid 0x%llx, expected %llu, actual %llu\n
spaceman datazone unknown zone id (%hu)\n
hash validation: invalid node %llu (root %llu)\n
block count
found shadow dir-stats object (id %llu) with origin (id %llu)\n
found xattr dstream (id %llu, name %.*s) that references a missing crypto state\n
file_id %llu (group_id %llu, private_id %llu) has different clonegroup group_id (%llu)\n
%s:%d: %s failed (E%d)\n
io_get_device_block_size
Volume %s is encrypted and crypto I/O failed/was skipped, skipping the fsroot tree.\n
failed to initialize the prev doc-id tree: %s\n
non-multikey volume
ersb_total_blk_to_encrypt (%llu) exceeds device block count (%llu)\n
recovery extent #%llu: fext_laddr (0x%llx) exceeds nx_block_count (%llu), fs_bsize %u\n
repair_overlapped_extents: unable to remove target pext 0x%llx for fs_oid 0x%llx (pext leak): %s\n
 private_id: %llu, file_id: %llu\n
found unexpected EFI jumpstart record\n
Invalid object type/subtype (type : %u) (subtype : %u)\n
om: om_snap_count (%u) is not equal to the number of snapshots found (%llu)\n
%s (id %llu): xf %u/%u: %s: extended field type is no longer used\n
reaper list entry (index (%u) list oid (0x%llx)) : index not less than nrl_max (%u)\n
no snap_name entry found for snap_meta entry with xid %llu and name %.*s\n
file info: attribution tag (hash %llu): total count does not match expected value (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_level (expected %u, actual %u)\n
overallocation detected in internal pool: (0x%llx+%llu) bitmap address (0x%llx)\n
failed to allocate memory for device path\n
directory record
Checking the snapshot metadata.
om
Checking snapshot %ld of %ld (%s, transaction ID %ld)
SAF descendants (%llu) of dir-stats object (id %llu) is greater than expected (0)\n
can't add purgeable resource fork size for dir-stats: %s (%d)\n
\tCache %s histogram:\n
unable to find inode (id %llu): %d (%s)\n
reap list object 0x%llx record count %u larger than max %u\n
integrity_meta: (0x%llx:0x%llx): unexpected flags (0x%x) for xid (%llu)\n
Conflicting options: [ -s ] option cannot be run with the [ -q ] option\n
Set ov_size (oid 0x%llx) to the block size? 
Remove invalid flags (0x%02x)? 
skipping dir stats clone sizes repair because the computed clone size is negative\n
purgeable resource fork size xfield of dir-stats object (id %llu) exists unexpectedly\n
nr
multiKeyEncryption
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid value (%u, %u)\n
       -F            force checking of encrypted volumes\n
checkpoint<->%s mismatch on uuid\n
failed to iterate the spaceman free queue tree: %s\n
dir-stats object (id %llu): %s overflow\n
.%llu
fsck_apfs completed at %s
found orphan/invalid xattr (id %llu, name %.*s)\n
spaceman ip bitmap %u at index %u was on the free list\n
com.apple.FSKit
%s (id %llu): invalid parent_id (%llu) for private directory\n
%s (id %llu): dstream.size (%llu) is greater than dstream.alloced_size (%llu)\n
performed too many chained-key iterations (current id %llu); can't mark the entire chain as needing reconciliation\n
cpm_map[%d].cpm_oid object type is invalid!\n
%s BTNODE_LEAF flag? 
error (%d) getting cib %d bitmap %d @ %lld\n
Fix btn_level (%u)? 
spaceman cib out of order: %u, expected %u\n
fv_kek_global_policy_eval
missing dir-stats object (id %llu) referenced by %s%llu files / directories\n
%s (%llu+%llu): entry %u has 'unknown' tag type\n
verification/reading of the omap object failed: %s\n
failed to look up checkpoint block address: %s\n
Main
apfs superblock at index %u: apfs_fs_alloc_count (%llu) is greater than container wide allocated count (%llu)\n
%llu
omap entry (oid 0x%llx): invalid ov_range (0x%llx+%llu)\n
checkpoint<->%s mismatch on nx_block_count: %lld %lld\n
Invalid
spaceman ip block count is bad: %lld\n
dir-stats object (id %llu) is purgeable, but its origin isn't\n
spaceman ip bitmap %u at index %u was referenced by a previous entry in sm_ip_bitmap \n
unable to init omap_snap tree iterator for snapshot repair: %s\n
unable to fix overlaps in candidate tree: %s\n
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield even though the file is marked as purgeable\n
Mark volume for doc-id tree building on next mount? 
snap_meta_ext: (0x%llx:0x%llx): unknown flags (%u)\n
can't find new dir-stats key for inode (id %llu): error %d\n
inode (id %llu): dataless bsd_flag is set, but the compression xattr is missing\n
 file_id: %llu dstream_id: %llu\n
apfs superblock at index %u: apfs_formatted_by.timestamp (%llu) is greater than current time (%llu)\n
resource fork size (%llu) of dir-stats object (id %llu) exists unexpectedly\n
iOS encryption rolling state object: size (%u), version (%u) does not match expected size (%zu)\n
iOS encryption rolling state object: non-iOS content protected volume unexpectedly has ierso\n
extended attribute
disabling overallocation repairs by default; use -o to override\n
omap entry (oid 0x%llx): invalid crypto key index (%u) on %s\n
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on file without INODE_WANTS_TO_BE_PURGEABLE flag\n
Fix apfs_num_symlinks(oid 0x%llx, xid 0x%llx)? 
\t\t<key>%s</key>\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in ip free queue tree does not lie in the internal pool\n
%s:%d: Zero'ing excess data to %s: paddr %lld, completed %lld, remaining %zu\n
%s (id %llu): invalid state.minor_version (%u)\n
clone mapping (private_id %llu, file_id %llu): invalid physical_size (%llu)\n
dir-stats descendants
Checking the object map.
* * * cannot allocate memory * * *\n
spaceman IP bitmap range is invalid: 0x%llx+0x%x\n
INO_EXT_TYPE_PURGEABLE_FLAGS
Space Verification: failed to lookup paddr (%llu) : error %s\n
apfs superblock at index %u: apfs_root_tree_oid is invalid.\n
       -b <num>      set default cache block size to <num> KiB\n
%s (id %llu): invalid internal_flags (0x%llx), (dir-stats origin but not dir-stats maintained)\n
%s (%llu+%llu): size is too large\n
(oid 0x%llx) %s: invalid ov_flags (0x%x)\n
Fix object (oid 0x%llx) checksum? 
failed to initialize the omap tree: %s\n
fs root tree
file
apfs superblock at index %u: apfs_fs_flags (0x%llx) indicates sealed volume is not fully unencrypted\n
blockcopy: unable to read paddr 0x%llx block_count 0x%llx: %s\n
failed to add PFKUR entry for inode (%llu): %s\n
apfs_sb: object (oid 0x%llx): apfs_snap_meta_ext_oid invalid\n
apfs_num_symlinks is not valid (expected %llu, actual %llu)\n
fv_encode_vek_blob
failed to register the file info tree in the fsck memory storage\n
omap (oid 0x%llx): invalid om_snap_count (%u), given om_flags (0x%x)\n
purgeable
The volume was modified
/dev/r%ss%d
Encryption
descendants (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
%s (id %llu): invalid name_len (%u)\n
%s (id %llu): present on sealed volume\n
%s (id %llu): Logical address %llu not a multiple of the block size (%u)\n
repair_overlapped_extents: remove target pext 0x%llx\n
Snapshot is invalid.
%s (id %llu): invalid owning_obj_id (%llu) for update extent\n
checkpoint %d (xid %llu) checkpoint map is invalid\n
apfs superblock at index %u: apfs_doc_id_fixup_cursor (%llu) is greater than or equal to apfs_next_obj_id (%llu)\n
%s (id %llu): invalid state.cpflags (%u)\n
Encrypted
failed to insert doc-id tree repair for doc-id %u, file-id %llu : %s\n
reaper list entry (index (%u) list oid (0x%llx)) : invalid flags (0x%x) set\n
nx_omap_oid is invalid\n
INO_EXT_TYPE_FINDER_INFO
Most recent checkpoint is invalid.
tried to remove snap_name entry but it's not there!\n
omap entry (oid 0x%llx): invalid ov_size (%u)\n
up
inode (id %llu): Resource Fork xattr is missing or empty for compressed file\n
AppleAPFSContainer
Update the parent's minkey? 
failed to init fsroot tree to mark dir-stats chain as inconsistent\n
purgeable tombstone
repair_overlapped_extents: allocate space for block_count 0x%llx\n
Fix apfs_volname(oid 0x%llx, xid 0x%llx)? 
could not cache physical extent repair at %llu error: %s\n
dev_init
com.apple.fs.graft-vol-uuid
%s (id %llu): owning_obj_id is 0\n
reap list expected %u objects, but haven't seen last reap list object yet\n
blockcopy: unable to write paddr 0x%llx block_count 0x%llx: %s\n
Disabling idle sleep, %s\n
file info: failed to allocate memory\n
bt
Checking the EFI jumpstart record.
%s (id %llu): invalid sibling_id (%llu)\n
Round down logical address (%llu) to block size? 
nx_xp_desc_blocks (%u) is less than 8\n
repair_overlapped_extents: insert target pext 0x%llx\n
volumename
%d\n
apfs superblock at index %u: apfs_modified_by[%d].id (%.*s) is not NULL terminated.\n
mismatch between extentref entry reference count (%d) and calculated fsroot entry reference count (%d) for extent (%llu + %llu)\n
error aborting transaction: %s\n
File/folder %s could not be repaired.
_INO_EXT_TYPE_VOLNAME
apfs superblock at index %u: apfs_omap_oid is invalid.\n
no snap_meta entry found for snap_name entry with name %.*s\n
unable to setup snapshot tree iteration: %s\n
nx_superblock magic number invalid: 0x%X\n
apfs_num_snapshots is not valid (expected %llu, actual %llu)\n
%s (id %llu): Invalid type (0x%x)\n
%s (%llu+%llu): entry %u has size %u > remaining size %u (keybag size %u)\n
(oid 0x%llx) %s: found zeroed-out block\n
file info: attribution tag (hash %llu): full clone size does not match expected value (%llu)\n
compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n
IOBlockStorageDevice
\nSpace allocation summary:\n\n
       -X            report progress to FSKit\n
omap snapshot: invalid key (0x%llx)\n
%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than CLONEGROUP_ID_MIN (%u)\n
found shadow dir-stats object (id %llu) but did not find its calculating dir-stats (%llu)\n
orphan omap mapping found for oid %llu\n
Could not initialize APFS-specific messages\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n
%s (id %llu): invalid xfields\n
failed to enqueue purgeable record (file id %llu, atime %llu) for remove\n
invalid sblock_oid (%llu)\n
found invalid object (type %u, id %llu)\n
found orphan crypto state object (id %llu, refcnt %u)\n
unable to get the file ids of dstream_id %llu\n
nx_fusion_wbc should be empty but isn't\n
unable to initialize fsroot tree iterator for file lookup in directory: %s\n
Fix sm_fs_reserve_alloc_count? 
apfs superblock at index %u: apfs_sec_root_tree_type is invalid\n
Fix apfs_doc_id_tree_type? 
need to increment crypto state object (id %llu) refcount (%u)\n
fd_dev_read_helper
Spaceman internal pool bitmap fragmented metadata tree is invalid\n
:%d
AppleAPFSVolume
less
Could not iterate extentref tree to read reaper objects(oid 0x%llx): %s\n
failed to allocate memory for snapshot repair\n
ersb_flags (0x%llx) has ERSB_FLAG_PAUSED on but ersb_recovery_extents_count is non-zero (%llu)\n
sec fs root tree
 atime: %llu file_id: %llu file_size: %llu dstream_id: %llu flags: 0x%x owning_uid: %u\n
integrity_meta: (0x%llx:0x%llx): unknown flags (0x%x)\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %lu\n
gbitmap
failed to update %s object: %s\n
%s (id %llu): xf %u/%u: %s: invalid doc_id index\n
inode (id %llu): unable to add repair to unmark purgeable: %d (%s)\n
nx_xp_data_blocks (%u) is less than 8\n
UNKNOWN
Could not initialize snap meta tree (oid 0x%llx): %s\n
clonegroup_tree: 
underallocation detected on %s device: (0x%llx+%llu) bitmap address (0x%llx)\n
found clone group tree in invalid volume format\n
dev_init_common
\t\t\t<integer>%p</integer>\n
option -f is not implemented, ignoring\n
verification/reading of the spaceman object failed: %s\n
checkpoint<->%s mismatch on nx_xp_desc_base: %lld %lld\n
sib-id: %lld parent-id: %lld name: %.*s\n
Running FSCK
msg != NULL
spaceman cab out of order: %u, expected %u\n
can't add orphan clone mapping (private_id %llu, file_id %llu) to the fsck repairs: %s (%d)\n
The volume %s with UUID %s was found to be corrupt and needs to be repaired.
IOMedia
nx_incompatible_features has unsupported flags: (0x%llX)\n
ersb_progress (%llu) exceeds ersb_total_blk_to_encrypt (%llu)\n
error (%d) writing cib\n
Invalid volume index passed\n
option -Z is deprecated, ignoring\n
Fix snapshot meta name_len (%u) from snap name entry? 
%s (id %llu): invalid dstream.default_crypto_id (%llu) on unencrypted volume, given apfs_fs_flags (0x%llx)\n
invalid btree node address range (0x%llx+%llu)\n
resource fork size of dir-stats object (id %llu) does not match expected value (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u), given mt_val_size (%u)\n
INO_EXT_TYPE_FS_UUID
path
failed to allocate memory for fsck_state\n
btree node (oid (0%llx)) being reaped has invalid val_len (%u) at index (%d) \n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x)\n
  
refcnt: %d \n
cpm_count (%u) is larger than the max that this block size can accommodate (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_node_count (overflow)\n
fsck_messages.c
failed to read spaceman cib %u at address 0x%llx\n
%s%llu%-*.*s %cB%s
%s (id %llu): xf %u/%u: %s: invalid extended field size %u, max %u\n
hw.memsize
\t%-32s %u\n
(%c,\"%s\",%d)\n
apfs superblock at index %u: apfs_snap_meta_tree_type is invalid: 0x%x\n
doc-id tree: record exists for doc-id %u, file-id %llu but no inode references this doc-id\n
the checkpoint superblock has a lower o_xid (%lld) than the %s (%lld)\n
Tree node repair failed.
volume omap (fs_oid 0x%llx)
INO_EXT_TYPE_STRICT_CLASS_F
\t\t\t<integer>%llu</integer>\n
need to insert missing clone mapping (private_id %llu, file_id %llu)\n
need to insert key at id (%llu) to repair invalid internal node\n
failed to update allocation counts: %s\n
%s (id %llu): Bad phys_block_num + len (%llu + %llu) for physical file extent record\n
%s (id %llu): invalid chained_key (%llu)\n
%s (id %llu): purgeable resource fork size (%llu) is larger than resource fork size (%llu)\n
file info: attribution tag (hash %llu) with invalid jobj_id (%llu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep managed vek cannot have flag_no_ephdm%s\n
unable to allocate memory to repair missing crypto state\n
nchildren of inode object (id %llu) does not match expected value (%d)\n
file info: found orphan data hash (id %llu) at logical address %llu\n
cpm_flags has an unknown flag set 0x%x\n
checksum_count (%u) exceeds max checksums (%u)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s institutional recovery key%s\n
bitmap was not entirely unset, stopping allocation\n
object (oid (0%llx)) being reaped : Invalid tree subtype (%u)\n
failed to remove inode (oid 0x%llx) xfield (type %u): %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u), given total value length (%u) (%d %d %d = %d)\n
Checking deleted snapshot residual state.
%s (id %llu): invalid state.key_len (%u)\n
Fix btree: bt_longest_val (%u)? 
unexpected on-disk range 0x%llx+%llu xid %llu and in-memory range 0x%llx+%llu xid %llu while repairing free queue tree\n
file data
%s: error %d from IORegistryEntryGetParentEntry\n
Missing required option: [ -D ] option requires the [ -T ] option\n
purgeable size xfield of dir-stats object (id %llu) exists unexpectedly\n
failed to register the phys extent tree in the fsck memory storage\n
repair_overlapped_extents: free space for target_paddr 0x%llx block_count 0x%llx\n
Verifying volume object map space.
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid implicit stash%s\n
unable to init fsroot tree iterator for dstream repair: %s\n
%s (id %llu): attribution tag xf does not exist, despite internal_flags (0x%llx)\n
Remove orphan/invalid %s objects? 
found orphan dstream id object (id %llu)\n
refcnt of dstream id object (id %llu) less than expected\n
nx_reaper_oid (%llu) is less than minimum OID (%d)\n
nx_newest_mounted_version is greater than expected: %s\n
DREC_EXT_TYPE_SIBLING_ID
file info: attribution tag (hash %llu) skipping clone size repair because the computed clone size is negative\n
failed to initialize the fsroot tree: %s\n
iOS encryption rolling state object: (version %u) invalid policy (%u)\n
Clear unexpected flags? 
 * * * cannot allocate memory * * *\n
spaceman cab %u address 0x%llx is not in the internal pool\n
%s (id %llu): xf %u/%u: %s: found rdev x-field even though inode is not a char/block device\n
snap_meta_ext
down
could not retrieve erb, oid 0x%llx\n
Checking the fsroot tree.
userfs_data_cryptor
clone group tree (id %llu): invalid key length (%u)\n
cib: ci_free_count (%u) is not valid (%llu) (ci_addr 0x%llx)\n
directory
fsckPrintGUI
spaceman ip bitmap %u at index %u is not invalidated on the free list\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode vek%s\n
alloced_size (%llu) of dstream (id %llu) does not match calculated size (%llu)\n
%s (id %llu): invalid internal_flags (0x%llx), given type (0%o)\n
%s (id %llu): xf %u/%u: %s: failed to register dstream: %d\n
ersb_recovery_extents_count == 0, but ersb_recovery_list_oid is non-zero (0x%llx)\n
apfs_clonegroup_next_id is not valid (expected %llu, actual %llu)\n
%s (id %llu): invalid sparse extent with nonzero crypto_id (%llu)\n
clone mapping (private_id %llu, file_id %llu): invalid private_id\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btree node is %s\n
(%d %%)\n
com.apple.FinderInfo
.DocumentRevisions-V100
failed to validate object with crypto key index (%u), retrying with (%u)\n
failed to allocate dir-stack memory for lookup in directory\n
%s: error %d from IORegistryEntryCreateCFProperties\n
cib
found file extent gap (id %llu) at logical address %llu+%llu\n
-----------
failed!
found an orphan clone mapping (private_id %llu, file_id %llu)\n
%s (id %llu): xf %u/%u: %s: invalid dir_stats_key (%llu)\n
%s (%llu+%llu): %s records entry %u contains invalid keybag\n
%s%s
clone group tree: unknown type (%u)\n
failed to register the dir stats tree in the fsck memory storage\n
apfs
Fix apfs_modified_by[%d].id(oid 0x%llx, xid 0x%llx)? 
need to update inode (object-id %llu) sparse bytes with (%llu)\n
tried to remove oid %llu from the omap but it wasn't there\n
failed to look up dstream id object (id %llu): %s\n
%s (id %llu): directory nlink value %d is greater than nchildren (%d)\n
physical_size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given btn_btree.bt_fixed.bt_flags (0x%x)\n
spaceman datazone duplicate zone id (%hu) for allocation zones at indices (%hu, %hu)\n
dstream (id %llu) does not have an associated dstream id object\n
evict_mapping_tree: 
The volume %s with UUID %s appears to be OK.
failed to look up resource fork for inode (%llu): %s\n
%s (id %llu): invalid state.major_version (%u)\n
\n
error updating omap entry: %s\n
failed to remove dir stats (id %llu) %s xfield: %s (%d)
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space (%u, %u)\n
    |
\t\t<key>%s</key> <integer>%s</integer>\n
integrity_meta: failed to copy object (0x%llx:0x%llx)\n
clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n
refcnt %d\n
Fix apfs_formatted_by.id(oid 0x%llx, xid 0x%llx)? 
Node counts:
cab
       -l            live fsck (lock down for verify-only)\n
%s (id %llu): invalid atime (0)\n
Any
file (id %llu) purgeable_flags (0x%x) disagree with its matching clonegroup record flags (0x%x)\n
inum: %8lld version: %u flags: %u current_offset: %8llu current_ns_offset: %8llu\n
file info: attribution tag (hash %llu): physical size (%llu) does not match computed size (%llu)\n
 type: %u logical addr: %lld\n
file info: found more than one attribution tag with matching computed hash, invalid entry (hash %llu)\n
%s (id %llu): Unknown type (0x%x)\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
file extent
Space manager is invalid.
apfs superblock at index %u: apfs_fext_tree_oid is invalid.\n
object (oid 0x%llx): Unable to mark omap entry in use for omap space verification \n
Limited repair mode, not all repairs available
spaceman sm_ip_bm_free_next index %u does not lie in ip bm range\n
dir-stats object (id %llu) is SAF, but its origin isn't\n
%s (%llu+%llu): unknown version %u\n, skipping checks\n
error (%d) looking up spaceman IP bitmap block %u\n
failed to insert purgeable (file_id %llu): %s (%d)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_val (expected %u, actual %u)\n
ersb_recovery_extents_count is non-zero (%llu), but ersb_recovery_length == 0\n
%s (id %llu): invalid dstream.default_crypto_id (%llu) on encrypted volume\n
iOS encryption rolling state object: xattr payload (%hu) does not match record size (%zu)\n
%s:%d: can't get the device block size (%s). assuming 512\n
clonegroup records of (private_id %llu) count (%u) != dstream_id refcount (%u)\n
Restarting after deferred repairs...\n
%s %llu/%llu repairs of this type in total.\n
Invalid file descriptor passed\n
need to set flags (0x%llx) in inode (object-id %llu)\n
The volume %s with UUID %s was found to have minor issues that can be repaired.
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_val (%u), given btn_btree.bt_fixed.bt_val_size (%u)\n
failed to init fsroot tree for lookup in directory\n
unexpected key (%u) / val (%u) size in extent list tree\n
inode (id %llu): failed to enqueue to the repairs\n
%s (id %llu): xf %u/%u: %s: found attribution tag on an inode with unsupported flags\n
unable to iterate fsroot tree (xid %llu) for tree node repairs: %s\n
subdir count overflow (%d)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n
equal to
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s %s unlock %s (%d)%s\n
error: 
%s (id %llu): xf %u/%u: %s: failed to register dir-stats (%llu) origin: %d\n
failed to lookup %s object: %s\n
:
can't repair inode (id %llu) with dir stats (id %llu)\n
%s/apfs_data
nx_xp_desc_len (%u) is larger than nx_xp_desc_blocks (%u)\n
repair_overlapped_extents: unable to init fsroot for fs_oid 0x%llx\n
 name: '%.*s' name_len: %u snap_xid: %lld\n
Clear
Fix the number of bytes? 
xp_map->cpm_map[%d].cpm_size (%u) is not a multiple of nx_block_size (%u)\n
underallocation detected in internal pool: (0x%llx+%llu) bitmap address (0x%llx)\n
skipping dir stats clone sizes repair because the clone mapping repairs were aborted\n
inode with file-id %llu has doc-id %u but doc-id tree record is missing or points to another inode\n
Fix corrupt container superblock? 
volume-index
%s (id %llu): invalid physical size (%llu) for hash (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: index %u is %s maxkey (should be less than)\n
0x%08x
Try running fsck against the entire APFS container instead of a volume\n
Mark volume for doc-id tree cleanup on next mount? 
unable to init snap_meta tree iterator for snapshot repair: %s\n
failed to write apfs superblock : %s\n
%s (id %llu): owning_obj_id is '%s'\n
purgeable size xfield is missing from dir-stats object (id %llu)\n
nx_ephemeral_info %d: invalid info (0x%llx)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: can't compare key (%u) with key (%u)\n
unknown obj type (%u) to add xfields\n
unable to load inode (oid 0x%llx) for lookup in purgatory directory: %s\n
%s (id %llu): invalid internal_flags (0x%llx), inconsistent protection class\n
%s (%s)
(oid 0x%llx) %s: invalid o_type (0x%x, expected 0x%x)\n
spaceman fs_reserve_block_count %llu is greater than nx_block_count %llu\n
bitmap was not entirely set, stopping deallocation\n
       -x            print output in XML\n
unable to add tree repair at key at id %llu : %s\n
orphan/invalid physical extent (%llu)\n
missing upgrade-rolling entry for inode (%llu), version (%d)\n
integrity_meta: (0x%llx:0x%llx): invalid version\n
unencrypted
Executing %s (version %s).
pfk_val : object (oid 0x%llx): invalid current_offset (%llu)\n
found non-shadow dir-stats object (id %llu) that has calculating dir-stats\n
index %u key
DirSize
error %d from cond wait\n
AKS_FV_service
%s (id %llu): unable to remove dstream of inode %llu\n
error updating omap_snap entry: %s\n
found clone mapping in a volume with initialized clonegroup tree\n
The volume %s cannot be verified when it is in use.
could not sync and freeze volume: %s\n
apfs superblock at index %u: apfs_fs_flags (0x%llx) previously sealed bit inconsistent with apfs_incompatible_features (0x%llx) / apfs_integrity_meta_oid (%llu) / apfs_fext_tree_oid (%llu)\n
dir-stats object (id %llu) unexpectedly unmarked as having origin-id\n
cpm_map[%d].cpm_subtype has nonzero storage type (0x%x)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list, btn_val_free_list, or btn_free_space: %s\n
unable to iterate tree for tree node repairs: %s\n
%s:%d: CCCryptorCreateWithMode failed (E%d)\n
INO_EXT_TYPE_DIR_STATS_KEY
FileInfo
nx_next_oid (%llu) is less than the minimum (%u)\n
checkpoint %d obj->o_type is invalid: (0x%x)\n
clonegroup
repair_overlapped_extents: remove source pext 0x%llx\n
UNKNOWN-DEV
apfs superblock at index %u: apfs_doc_id_index_flags has unrecognized flags (0x%x)\n
can't add attribution tag for clone mapping: %s (%d)\n
Conflicting options: [ -T ] option cannot be run with the [ -n | -q ] options\n
 %s tree (%llu)%s
fsck cache stats:\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_key_count (expected %llu, actual %llu)\n
CLONE_MAPPING_EXT_DIR_STATS_KEY
Set missing flag? 
purgeable size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
%s (%llu+%llu): failed to get keybag data: %s\n
nx_read_only_compatible_features has unsupported flags: (0x%llX)\n
fsckPrintString
%s (id %llu): xf %u/%u: %s: found rdev x-field but volume has rdev in core-inode\n
cpm_map[%d].cpm_type storage type (0x%x) != OBJ_EPHEMERAL\n
bm_bit_count %llu is not an integer multiple of container block count %llu\n
no omap_snap tree entry found for snap_meta entry with xid %llu\n
%s (id %llu): com.apple.ResourceFork is expected to be stream based\n
inode (id %llu): has the compression bsdflag, but doesn't have the compression xattr\n
iOS encryption rolling state object: ierso version (%u) unrecognized\n
INO_EXT_TYPE_ORIG_SYNC_ROOT_ID
apfs_num_files is not valid (expected %llu, actual %llu)\n
com.apple.fs.graft-jobj-id-len
reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
object oid %llu/xid %llu/type 0x%x/subtype 0x%x: unable to mark range %llu+%llu allocated for space verification: %s\n
extent_list: 
inode (id %llu): need to clear internal_flags 0x%llx\n
no file key rolling entry found for inode object (%llu)\n
Missing required option: [ -l ] option requires the [ -n ] or [ -q ] option\n
Clear uncompressed size/rdev/dir_nlink? 
purgeable resource fork size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
%s (%llu+%llu): number of bytes %u does not match sum of all entries %u\n
pl=%d:%d 
spaceman datazone current boundaries (%llu -> %llu) is not a valid address range on disk\n
Checking the snapshot metadata tree.
wr=%d wl=%d
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unknown blob type %i%s\n
Failed to close password file descriptor: %s\n
file info: clone size overflow for hash (%llu)\n
Space Verification: failed to remove paddr (%llu) error : %s\n
unexpected spaceman struct size %u != %u\n
unable to init physical extent tree iterator for repairs: %s\n
OTI keybag
Update %s objects? 
nx_xp_data_next (%u) is larger than the # of nx_xp_data_blocks (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: index %u is %s index %u (should be less than)\n
found file extent overlap (id %llu) at logical address %llu (expected %llu)\n
Fix object (oid 0x%llx) header bit flip? 
%s:%d: can't get solidstate for device (%s)\n
0x%llx-dead
reaper list entry (index (%u) list oid (0x%llx)) : cycle detected\n
doc-id tree record exists for doc-id %u, but no inode references this doc-id\n
IOMatchCategory
fsckPrint
clonegroup (group id %llu, private_id %llu, file id %llu): unknown flags (0x%x / known flags are: 0x%x)
fsck_apfs is out of memory - some cross checks are skipped\n
%s: error %d from IORegistryEntryGetLocationInPlane\n
cmp_map[%d].cpm_subtype object type (0x%x) is invalid!\n
\t\t\t<integer>%ld</integer>\n
 (
dev_read_finish
dev=%s vers=%s default_ans=%s result=%d 
successful
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u
repair_overlapped_extents: unable to update source pext 0x%llx for fs_oid 0x%llx (refcnt leak): %s\n
reaper list entry (index (%u) list oid (0x%llx)) : invalid nrle_fs_oid (0x%llx)\n
failed to repair inode sparse bytes (id %llu): %s\n
\t\t<key>%s</key> <string>%s</string>\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n
%s (%llu+%llu): entry %u has invalid blob\n
found orphan/unexpected crypto state object (id %llu)\n
NX checkpoint data area fragmented metadata tree is invalid\n
Checking the checkpoint with transaction ID %ld.
Encryption Rolling data structures are invalid.
too many parent chain lookups during missing dir-stats repairs\n
%s (id %llu): xf %u/%u: %s: unable to remove dstream of non-regular inode\n
(oid 0x%llx) %s: %s(%llu, %u): %s\n
can't allocate memory to insert a new clonegroup value\n
apfs superblock at index %u: apfs_fs_flags has an unknown flag set 0x%llx\n
%s (id %llu): Length %llu of file extent not a multiple of the block size (%u)\n
unable to init fsroot tree: %s\n
main
failed to look up crypto state object (id %llu): %s\n
om: om_most_recent_snap (%llu) is not equal to the largest snapshot xid (%llu)\n
hit
Device does not contain a valid APFS container.\n
directory stats
<plist version=\"1.0\">\n
       -n            verify only (answer \"no\" to questions)\n
dir-stats object (id %llu) is purgeable, but it doesn't track purgeable size\n
checkpoint<->%s mismatch on nx_xp_data_base: %lld %lld\n
device %s failed to open with error: %s\n
%s:%d: can't get block count (%s)\n
number of files in clonegroup (%u) != dstream reference count (%u)\n
usec
failed to allocate memory for snapshot validation\n
invalid gbitmap block oid 0x%llx for key 0x%llx\n
%llu\n
Fix spaceman free queue tree sfq_oldest_xid (oid 0x%llx)? 
Failed to allocate memory for keybag\n
found orphan dstream id object (id %llu, refcnt %u)\n
%s:%d: lib_get_file_vault_services failed (E%d)\n
Fix inode_val: parent_id (%llu)? 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: parent doesn't have enough space to update the minkey\n
%s (id %llu): xf %u/%u: %s: inode is expected to be an SAF dir-stats origin\n
com.apple.decmpfs
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: missing btn_flags (expected 0x%x, actual 0x%x)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys disable%s\n
omap snapshot: invalid oms_flags (0x%x)\n
com.apple.fs.altlink
%s (id %llu): invalid flags: (0x%02x)\n
0x%016llx
greater
Removable
CloneMap
spaceman struct is versioned but version is 0\n
dir-stats object (id %llu) unexpectedly marked as having origin-id\n
spaceman ip bitmap block address is invalid: %hu > %u\n
reaper needs more cowbell, flags 0x%x\n
nx_fusion_wbc_oid should be invalid but isn't\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid node hash\n
error (%d) writing bitmap @ %lld\n
%s (id %llu): xf %u/%u: %s: invalid hash: (0)\n
image-format-read-only
%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n
error iterating trees during snapshot repair: %s\n
%s (id %llu): xf %u/%u: %s: unable to add repair for unexpected xfield: %s\n
dir-stats (id %llu) is missing\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list length (%u), given total key length (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u)\n
Could not initialize extentref tree (oid 0x%llx): %s\n
could not retrieve gbitmap from er_state_phys_t\n
invalid kind (expected %u, actual %u) for extent (%llu + %llu)\n
object (oid 0x%llx): o_type invalid, o_type 0x%x should be 0x%x\n
INO_EXT_TYPE_FILE_DATA
INO_EXT_TYPE_SPARSE_BYTES
integrity_meta: (0x%llx:0x%llx): invalid root hash\n
unknown
failed to look up checkpoint block address %d: %s\n
CLONE_MAPPING_EXT_TYPE_ATTR_TAG
Checking the container superblock.
clone mapping (private_id %llu, file_id %llu) is orphan\n
Fix om_most_recent_snap (oid 0x%llx)? 
INO_EXT_TYPE_ATTRIBUTION_TAG
container %s is mounted with write access; please re-run with -l.\n
%s (id %llu): file extent record present on sealed volume\n
warning: 
spaceman sm_ip_bm_free_head %u and sm_ip_bm_free_tail %u do not point to a valid list\n
clone mapping (private_id %llu, file_id %llu) is missing\n
%s (id %llu): physical size (%llu) is less than full clone size (%llu) for hash (%llu)\n
failed to allocate memory for the extentref tree\n
apfs superblock at index %u: apfs_fs_alloc_count (%llu) must not be greater than apfs_fs_quota_block_count (%llu)\n
clone group tree: invalid key length (%u)\n
</plist>\n
spaceman cibs per cab %u is inconsistent with block size %u\n
apfs_num_other_fsobjects is not valid (expected %llu, actual %llu)\n
%s (%llu+%llu): entry %u has invalid blob range %llu+%llu\n
Protocol Characteristics
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_nkeys (%u), given btn_flags (0x%x)\n
b:cCdE:fFglnMopqr:sSWxXyZTD
container
%s:%d: failed to open volume device %s: %s\n
pfkur_key : object (oid 0x%llx): invalid oid (0x%llx)\n
decrypt
 [reconstructed]
speculative download xattr (id %llu): shouldn't be stream based\n
unable to open the volume for repairs: %s\n
%04x:  
unable to init snap_meta tree for snapshot repair\n
omap (oid 0x%llx): invalid om_snapshot_tree_type (0x%x)\n
%s (id %llu): xf %u/%u: %s: found nlink field but volume doesn't support it\n
cpm
inode (id %llu): dataless bsd_flag is set, but the compression type is different: 0x%x\n
descendants of dir-stats object (id %llu) does not match expected value (%llu)\n
file key rolling
\n%s: fsck_apfs started at %s
invalid extent (%llu + %llu) with reference count (0)\n
com.apple.system.apfs.ierso
apfs superblock at index %u: apfs_revert_to_xid (%llu) should be less than nx_next_xid (%llu)\n
Fix apfs_fs_reserve_block_count(oid 0x%llx, xid 0x%llx)? 
clone mapping (private_id %llu, file_id %llu): purgeable status is different than inode (id %llu) purgeable status\n
       -C            force a sync prior to freezing for live fsck\n
%s (id %llu): dir-stats key xf does not exist, despite internal_flags (0x%llx)\n
(oid 0x%llx) %s: could not repair object to match checksum: too many bit flip candidates (%d)\n
checkpoint %d (xid %llu) fsck_obj_phys failed\n
missing clone group record for file_id %llu (private_id %llu, group_id %llu)\n
failed to allocate memory for file lookup in purgatory directory\n
INO_EXT_TYPE_SPEC_TELEM_FLAGS
fsck may bail out with overallocation - could not mark space allocated in fsck's version of the bitmap (%lld + %lld)\n
%s (id %llu): invalid flags (0x%x), given name (<%.*s> ; name_len %d)\n
failed to insert %s object: %s\n
%s xfield of dir-stats object (id %llu) exists unexpectedly\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode blob%s\n
com.apple.system.fs.speculative_telemetry
DstreamID
%02x 
apfs superblock at index %u: apfs_modified_by[%d].timestamp (%llu) is greater than current time (%llu)\n
)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n
Delete snap_meta entries? 
failed to register the dir stats repair tree in the fsck memory storage\n
Target Disk Mode
failed
failed to remove snap_name entry: %s\n
Fix apfs_fs_index(oid 0x%llx, xid 0x%llx)? 
found orphan/invalid clone mapping (private_id %llu, file_id %llu)\n
BSD Major
omap (oid 0x%llx): invalid om_snapshot_tree_oid (0x%llx), given om_flags (0x%x)\n
%s (id %llu): invalid key length (%u)\n
%s (id %llu): found dir-stats object (chained-key %llu) that is unexpectedly being moved\n
PURGEABLE_EXT_TYPE_START_TIME
%d failures and %d warnings issued; failing execution as requested.\n
%s (id %llu): invalid zero crypto_id on encrypted volume\n
failed to init fsroot tree to repair dir-stats chained key\n
cpm_map[%d].cpm_paddr (%llu) + cpm_size (%u) is not in the checkpoint data area\n
xattr value length (%u) does not match record size (%u)\n
error (%s) failed to get cib for chunk index %llu \n
Remove entry with invalid keybag? 
set missing flag? (0x%x) 
recovery extent #%llu: invalid fext_pbn (0x%llx)\n
apfs_fs_reserve_block_count brings total reserve block count beyond the container block count (max %llu, actual %llu)\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_level (%u), given btree node is %s\n
%s (id %llu): xf %u/%u: %s: unknown x_type (%u)\n
%s (id %llu): signing id hash (%llu) for signing id (%s) with length (%zu) does not match attribution tag hash (%llu)\n
Remove entry with invalid range? 
Fix sm_fs_reserve_block_count? 
Fix snapshot meta name (%.*s) from snap name entry? 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u), given total key length (%u)\n
%s (id %llu): invalid name_len (%u), given key length (%u)\n
reaper list entry (index (%u) list oid (0x%llx)) : entry is both occupied and free!\n
inode (id %llu): can't add internal flags repair: %d (%s)\n
invalid range: 0x%llx+%llu\n
aks
       -g            print output in form suitable for automatic parsing\n
unable to init omap_snap tree for snapshot repair\n
unable to insert tree node at key id %llu for repairs : %s\n
clone group tree: mapping group_id (%llu) is invalid\n
(oid 0x%llx) %s: invalid o_xid (0x%llx)\n
object (oid 0x%llx): Unable to mark spaceman ip range (0x%llx + %llu) allocated for space verification\n
fv_decrypt_vek
clonegroup (group id %llu, private_id %llu, file id %llu): inum is invalid\n
error iterating physical extent tree: %s\n
nx
can't cross check inode (id %llu) with its corresponding clonegroup record: %d (%s)\n
Verifying allocated space.
clone size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
NX evict mapping tree is invalid.
Reached max number of fsck passes during repair\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u, expected %u\n
Could not iterate gbitmap tree to read reaper objects (oid 0x%llx): %s\n
apfs superblock at index %u: apfs_fs_quota_block_count (%llu) should not be greater than nx_block_count (%llu) for an FS with quota\n
AppleAPFSSnapshot
failed to register the crypto tree in the fsck memory storage\n
data_hash: object (oid 0x%llx): Missing hash at offset %llu (found %llu)\n
file info: attribution tag with invalid hash (%llu)\n
nx_ephemeral_info 0: invalid version (%u), should be: (%d)\n
com.apple.ResourceFork
could not lookup extent at %llu for physical extent repair: %s\n
Missing required option: [ -S ] option requires the [ -n ] option\n
%s (%llu+%llu): number of bytes %u exceeds object size %u\n
speculative download xattr (id %llu): found outside of an SAF dir stats hierarchy\n
apfs superblock at index %u: APFS_FEATURE_EXTENDED_VEK_CLASSES set on non-HCP volume (apfs_features: 0x%llx)\n
%llu 
%s (id %llu): unknown flags (0x%hx / known flags are: 0x%hx)\n
can't add dir stats key for clonegroup: %s (%d)\n
reap list object 0x%llx last index %u larger than max index %u\n
missing/invalid physical extent (%llu + %llu) with refcnt %d\n
cpm_o.o_oid (0x%llx) doesn't match the physical address (0x%llx)\n
spaceman sm_ip_bm_block_count %u is too large\n
%s (id %llu): invalid flags (0x%x)\n
failed to allocate memory for bitmap store\n
apfs superblock at index %u: apfs_modified_by[%d].last_xid (0x%llx) is greater than nx_next_xid (0x%llx)\n
apfs superblock at index %u: apfs_doc_id_index_xid (%llu) is greater than or equal to container nx_next_xid (%llu)\n
physical size
Cache %s count:
directory valence check: directory (oid 0x%llx): orphan directory record\n
_enable_user_kek
dstream (id %llu) is older than the current dstream (id %llu)\n
file info: attribution tag (hash %llu): full clone size (%llu) does not match computed size (%llu)\n
orphan omap mappings found for oid range %llu --> %llu\n
The volume %s with UUID %s could not be repaired.
the EFI jumpstart entry has length %u but occupies %llu blocks of size %u\n
encryption rolling
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 1%s\n
Round %s length (%llu) to block size? 
recovery extent #%llu: invalid prange (0x%llx+%llu), dev_bsize %u\n
Fix sm_free_count (%llu)? 
%s (id %llu): unknown kind (%u)\n
Spaceman free queue tree of type [%s] has sfq_oldest_xid (%llu) greater than the oldest xid in the free tree (%llu)\n
%s (id %llu): unknown internal_flags (0x%llx / known flags are: 0x%llx)\n
Checking if the parent's minkey can be updated...\n
vers: %u.%u flags: %#x class: %c os: 
spaceman IP range is invalid: 0x%llx+0x%llx\n
file info: computed size overflow for hash (%llu)\n
QUICKCHECK ONLY; FILESYSTEM CLEAN
failed to initialize the clone-group tree: %s\n
VERIFY
(void *)fmt == (void *)m->msg
com.apple.fs.firmlink
skipping dir stats clone sizes repair: present clone size %llu > %llu\n
Look for links to corrupt files in %s directory.
%s (id %llu): invalid internal_flags (0x%llx) given apfs_fs_flags (0x%llx) PFK bit\n
need to set bsd flags (0x%x) in inode (object-id %llu)\n
Document ID tree is invalid.
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid btn_flags (0x%x)\n
obj-id: %8lld type: ???\n
Extent ref tree is invalid.
object (oid 0x%llx): Unable to mark the omap entry of the apfs_sb at index (%u) in use for omap space verification\n
%s (id %llu): invalid crypto_id (%llu)\n
unable to allocate space to walk dir-stats parent chain\n
FAIL
%s (id %llu): invalid flag: (0x%02x)\n
,
%s (%llu+%llu): block range isn't a valid keybag, aborting\n
reap list object (oid 0x%llx) expected %u entries, found %u\n
compression xattr (id %llu): size is too small, actual: %u, minimum: %lu\n
private_id (%llu) has multiple clonegroup ids (%llu, %llu)\n
failed to register the doc id tree in the fsck memory storage\n
unknown keybag
spaceman cab %u wrong number of cibs: %u, expected %u\n
apfs superblock at index %u: apfs_root_tree_type is invalid: 0x%x\n
apfs superblock at index %u: apfs_sec_root_tree_oid (%llu) set on incompatible volume\n
apfs superblock at index %u: apfs_formatted_by.id (%.*s) is not NULL terminated.\n
cloned dstream (id %llu, object-ids %s) is being truncated\n
unable to load drec (oid 0x%llx) for file lookup in directory\n: %s\n
%s (id %llu): invalid xdata_len (%u), given flags (0x%x)\n
data_hash: object (oid 0x%llx): Found unexpected hash at offset %llu (expected length %llu)\n
om: invalid om_snap_count (overflow)\n
unable to init snap_meta tree for extentref_tree_oid lookup: %s\n
unable to allocate memory for tree repairs\n
Overlapping object: (oid : 0x%llx) (type : %u) (subtype : %u), (%llu + %llu)\n
clone size xfield is missing from dir-stats object (id %llu)\n
volume keybag
error (%d) looking up spaceman IP bitmap block at index %u\n
(oid 0x%llx) %s: invalid o_cksum (0x%llx)\n
Fix object (oid 0x%llx) bit flip? 
Checking the space manager.
apfs superblock at index %u: apfs_readonly_compatible_features has unsupported flags: (0x%llX)\n
file info: attribution tag (hash %llu): total count (%llu) does not match computed count (%llu)\n
error (%d) writing cib during deallocation\n
%s (id %llu): invalid name (%.*s), given name_len (%u)\n
purgeable resource fork size xfield is missing from dir-stats object (id %llu)\n
no snap_meta tree entry found for omap_snap entry with xid %llu\n
clone mapping (private_id %llu, file_id %llu): invalid xfields\n
INO_EXT_TYPE_SAF_DIR_STATS_KEY
DIR_STATS_EXT_TYPE_PURGEABLE_RSRC_SIZE
error iterating omap tree for repair: %s\n
(oid 0x%llx) %s: _omap_lookup_obj(0x%llx, 0x%llx): %s\n
underallocation
IOStorage
number of files in the clone mapping (%u) != dstream reference count (%u)\n
(oid 0x%llx) %s: invalid object size (0x%x)\n
failed to initialize tree for container repairs\n
Failed to get keybag : %s\n
spaceman chunk %llu bitmap address 0x%llx is not in the internal pool\n
%s: can't get BSD name of container\n
%s (id %llu): invalid hash (0)\n
apfs superblock at index %u: apfs_last_mod_time (%llu) is greater than current time (%llu)\n
purgeable size
found file extent overlap (id %llu) with next extent / end of dstream at logical address %llu+%llu\n
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
more than %d inodes tracked as rolling, disabling pfkur tracking repairs\n
failed to allocate memory for lookup in directory\n
apfs superblock at index %u: apfs_features has unrecognized features (0x%llX)\n
failed to traverse prev doc-id tree : %s\n
INO_EXT_TYPE_SOURCE_PURGE_ID
3288.52.1
%s (id %llu): file_id (%llu) and name (%.*s) mismatch for private directory\n
failed to initialize the extentref tree: %s\n
%s: not a valid disk name/path\n
purgeable resource forks are maintained on dir-stats object (id %llu) but not purgeable data forks\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space.len (%u), given toc_entry_size (%u) and btn_flags (0x%x)\n
\t\t\t<string>%s</string>\n
option -p is not implemented, ignoring\n
failed to allocate memory to mark dir-stats chain as inconsistent\n
drec count overflow (%d)\n
spaceman datazone previous boundaries (%llu -> %llu) is not a valid address range on disk\n
spaceman chunk %llu xid is invalid: %llu > %llu\n
error (%d) looking up spaceman IP block %llu\n
Fix object (oid 0x%llx) encryption and omap flags? 
pfk_val : object (oid 0x%llx): invalid current_ns_offset (%llu)\n
apfs superblock at index %u: apfs_volname (%.*s) is not NULL terminated.\n
%s (id %llu): invalid snap_xid (%llu)\n
purgeable resource forks are maintained on dir-stats object (id %llu) but not rsrc forks\n
_cmd_stash_kek
checkpoint<->%s mismatch on nx_block_size: %d %d\n
failed to allocate dir-stack memory for lookup in directory: %s; results may be incomplete\n
%s (id %llu): doc_id xf does not exist, despite bsd_flags (0x%x)\n
       -r <num>      read password for encrypted external volume from file descriptor <num>\n
disk
SAF descendants (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
OTI blob
(oid 0x%llx) %s: invalid ov_flags (0x%x), tweak type set for unencrypted object\n
Skipped
failed to remove %s object (id %llu): %s\n
fsck_apfs
Clear volume inconsistent bit? 
error (%d) getting cib bitmap %d @ %lld\n
%s (id %llu): invalid sblock_oid (%llu)\n
recovery extent #%llu: invalid ersb_flags (0x%llx), ERSB_FLAG_CID_IS_TWEAK is set but fext_cid == 0\n
apfs superblock at index %u: apfs_incompatible_features has unsupported flags: (0x%llX)\n
aborting purgeable cross checks - out of memory\n
failed to remove %s object: %s\n
SnapName
sm_ip
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_key (%u), given btn_btree.bt_fixed.bt_key_size (%u)\n
 extentref_Tree_type: %u flags: %u name: '%.*s' name_len: %u\n
%s (%llu+%llu): UUID of entry %u is null\n
(oid 0x%llx) %s: object is encrypted with crypto key index (%u)but omap says it's encrypted with crypto key index (%u)\n
insert missing directory record object (parent_id %llu, file_id %llu)\n
file extents
Can't read/write encrypted data to/from block 0!
reap list object 0x%llx max record count %u different than expected %lu\n
repair_overlapped_extents: unable to load pext 0x%llx for fs_oid 0x%llx: %s\n
failed to register the clone mapping tree in the fsck memory storage\n
file info: computed count overflow for hash (%llu)\n
%s (id %llu): invalid state.key_revision (%u)\n
nx_newest_mounted_version should not start with a 0: %s\n
clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect dir-stats key (%llu)\n
repair_overlapped_extents: copy paddr 0x%llx to paddr 0x%llx, block_count 0x%llx\n
failed to populate cached doc-id tree : %s\n
sealed volume hash records (id %llu, size %llu) do not match size of dstream (%llu)\n
%s (id %llu): invalid value length (%u), given name_len (%u)\n
failed to get fsroot tree for jobj type %d: %s\n
The container %s appears to be OK.
DIR_STATS_EXT_TYPE_CLONE_SIZE
inode with file-id %llu has doc-id %u but doc-id tree record has file-id %llu\n
unable to load inode (id %llu) to repair dir-stats chained key: %s\n
key size is too small, actual: %u, minimum: %u\n
failed to allocate memory for snapshot tracking\n
get_pfkur_tree() called on non-pfk volume\n
root_device
fsck_msg_type
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in free queue tree is not a valid address range on disk\n
clone group tree: invalid cookie key length (%u)\n
nx_fs_oid (%llu) at index (%d) is less than minimum OID (%d)\n
failed to finish pending reads from the bitmap iterator: %d (%s)
spaceman sm_ip_bm_free_tail %u does not point to the last index on the free list %u\n
dump_bytes_internal
unable to remove tree node at key id %llu for repairs : %s\n
omap (oid 0x%llx): invalid om_flags (0x%x)\n
(oid 0x%llx) %s: invalid crypto key index (%u) given obj_subtype\n
INO_EXT_TYPE_PREV_FSIZE
ersb_version is %d, unsupported\n
object (oid 0x%llx): Unable to mark omap entry in usefor omap space verification \n
reap list object 0x%llx free index %u larger than max index %u\n
failed to lookup extentref tree oid at snap_xid %llu : %s\n
can't add clone mapping (private_id %llu, file_id %llu) for repairs: %s (%d)\n
(oid 0x%llx) %s: invalid o_xid (0x%llx, expected 0x%llx)\n
omap mapping
iOS encryption rolling state object: failed to allocate ierso\n
NX media keylocker data range is invalid: 0x%llx+%llu\n
repair_overlapped_extents: unable to allocate space for block_count 0x%llx: %s\n
fv_rewrap_kek
unable to add tree node repair at key id %llu : %s\n
failed to find node at segment (%llu) : error %s\n
nx_ephemeral_info 0: invalid structures per fs (%u), should be: (%d)\n
failed to initialize tree for volume repairs\n
apfs superblock at index %u: apfs_formatted_by.last_xid (0x%llx) is greater than nx_next_xid (0x%llx)\n
INO_EXT_TYPE_NAME
FILE_INFO_TAG_EXT_TYPE_SIGNING_ID
%-20s%-15llu\n
EFI jumpstart record is invalid.
spaceman chunk %llu disk address out of order: 0x%llx, expected 0x%llx\n
apfs superblock at index %u: apfs_next_doc_id (%u) should not be less than MIN_DOC_ID (%d)\n
inode with file-id %llu has doc-id %u but doc-id tree record is missing\n
nlink: %d \n
Spaceman free queue tree of type [%s] has sfq_count (%llu) mismatch with cumulative counts in the tree (%llu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek and unmanaged vek device protection mismatch vek:%x, kek:%x%s\n
       -S            skip iteration of snapshots, although no repairs can be made.\n
Clear invalid flag? 
%s (id %llu): fext tree record present on non-sealed volume\n
(oid 0x%llx) %s: malloc(%u)\n
(oid 0x%llx) %s: object is %s but omap says it's %s\n
xattr size (%u) does not match expected size (%lu)\n
failed to register the prev phys extent tree in the fsck memory storage\n
The container %s could not be verified completely.
unexpected end of iteration while repairing free queue tree\n
failed to enable crypto I/O mode for container %s: %s\n
%s (id %llu): invalid length (%u), given xdata_len (%u)\n
%s (id %llu): invalid file_id (%llu)\n
Fix the number of keys? 
Fix object (oid 0x%llx) flags? 
(oid 0x%llx) %s: invalid crypto key index (%u), expected (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unable to repair minkey\n
Overlap repair pass...\n
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) is greater than the container block count (%llu)\n
Conflicting options: [ -o ] option cannot be run with the [ -n | -q ] options\n
dstream
unable to access the tree repairs structure: %s\n
pfkur_tree_key : object (oid 0x%llx): pfkur tree record present on non-pfkur volume\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given mt_key_size (%u)\n
repair_overlapped_extents: load fext 0x%llx 0x%llx\n
%03llu
failed to get fsroot tree to find expanded dir-stats %llu: %s\n
spaceman ip bm list has a loop\n
failed to insert clone mapping (private_id %llu,  file_id %llu, flags 0x%x): %s (%d)\n
?
private-id: %lld parent-id: %lld cr/mtime: %lld/%lld \n
flags: 0x%x data-len: %d name: %.*s\n
spaceman block count %llu doesn't match NX superblock block count %llu\n
Spaceman IP free queue tree has sfq_count (%llu) greater than IP block count (%llu)\n
invalid doc-id record, file-id is 0 for doc-id %u\n
NX checkpoint desc blocks field is %u, but sum of ranges is %llu\n
spaceman ip bitmap block at index [%u] is neither on the sm_ip_bitmap[] nor on the free list\n
%s (id %llu): invalid state.persistent_class (%u)\n
YES\n
Fix xf_used_data? 
failed to initialize the secondary fsroot tree: %s\n
%s BTNODE_ROOT flag? 
Clone group tree is invalid.
Physical Interconnect Location
failed to construct drec key (dir_id %llu, file_name %s)\n
Inode
spaceman chunk %llu free count %u of unallocated bitmap != block count %u\n
found cloned xattr dstream (id %llu, object-ids %s)\n
Remove invalid flag (0x%02x)? 
tmp-ino-clone-
speculative download xattr (id %llu): unknown version: %u\n
nx_ephemeral_info 0: invalid minimum block count per structure (%u), should be less than: (%d)\n
could not get the current executable path of %s\n
invalid zero-length extent (id %llu) at logical address %llu\n
The volume %s with UUID %s was repaired successfully.
unable to initialize iterator for snapshot validation: %s\n
invalid EFI jumpstart record file length: %d\n
\nfsck_apfs started at %s
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n
need to mark dir-stats %llu as needing reconciliation, due to an issue with dir-stats %llu\n
iOS encryption rolling state object: xattr payload (%hu) is too small\n
iOS encryption rolling state object: epoch unordered: current_id (%llu) <= epoch (%llu) < apfs_next_obj_id (%llu) <= MAX_JOBJ_ID (%llu)\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
%s (id %llu): invalid name (%.*s)\n
fsck_verbosity
%s (%llu+%llu): %s records entry %u does not contain a range (size %u)\n
apfs superblock at index %u: apfs_magic invalid: %d\n
%s%llu %cB%s
omap entry (oid 0x%llx): invalid ov_flags (0x%x)\n
%s (id %llu): ID larger than MAX_JOBJ_ID (%llu)\n
found orphan directory record object (id %llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_nkeys (%u), given btn_table_space.len (%u) and toc_entry_size (%u)\n
spaceman chunk count %llu is inconsistent with block count %llu and blocks per chunk %u\n
spaceman free count %llu does not match sum of free counts %llu\n
_cmd_handle_vek
       -c            enable cache statistics\n
/dev/fd/
file info: attribution tag (hash %llu) skipping clone size repair because the clone mapping repairs were aborted\n
object (oid 0x%llx): o_xid invalid, o_xid is 0\n
Checking the document ID tree.
Checking the clone group tree.
spaceman chunks per cib %u is inconsistent with block size %u\n
unknown spaceman struct version %u > %u\n
nx_features has unsupported flags: (0x%llX)\n
nx_xp_data_len (%u) is less than 2\n
found EFI jumpstart record of unknown version %d (max known: %d)\n
less than
PhysExtent
missing encryption rolling recovery data, actual length %llu, ersb_recovery_length %llu\n
apfs_fs_index (%d) is not valid (%d)\n
om: 
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
INO_EXT_TYPE_CONFORMANCE_NLINK
Checking the space manager free queue trees.
spaceman cib %u wrong number of chunks: %u, expected %u\n
apfs_next_doc_id is not valid (expected %u, actual %u)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n
orphan/invalid physical extent (%llu) at snapshot %llu\n
iOS encryption rolling state object: (version %u) full rolling has unrecognized current_state (%u)\n
fv_decode_kek_blob_opts
clone size
unable to initialize omap tree iterator for repair: %s\n
clone mapping (private_id %llu, file_id %llu): failed to update attribution tag %llu: %s (%d)\n
spaceman IP blocks field is %llu, but sum of ranges is %llu\n
%s (%llu+%llu): failed to put keybag: %s\n
failed to search purgeable record (file id %llu) in the fsck_apfs tree: %d (%s)\n
greater than
failed to register the clonegroup trees in the fsck memory storage\n
%s (id %llu): failed to register dir-stats (%llu) descendant: %d\n
clone group tree: cookie group_id (%llu) or cookie_group_id (%llu) is invalid\n
Could not iterate snap meta tree to read reaper objects (oid 0x%llx): %s\n
FileExtent
%s\n
unable to enqueue tree node prune repairs: %s\n
error iterating fsroot tree (xid %llu) for tree node repairs: %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u)\n
unable to init fsroot tree iterator: %s\n
error (%d) getting spaceman IP bitmap block %u @ %lld\n
%s (id %llu): invalid dstream.default_crypto_id (%llu) on encrypted volume, given apfs_fs_flags (0x%llx)\n
def-prot-class: %d \n
crypto
apfs_snap_meta: 
speculative download xattr (id %llu): size is too small, actual: %u, minimum: %lu\n
missing/invalid physical extent (%llu + %llu) with refcnt %d at snapshot %llu\n
%p\n
%s (id %llu): length is 0\n
repair_overlapped_extents: unable to find volume for fs_oid 0x%llx\n
%s (id %llu): Bad phys_block_num + len (%llu) for physical extent record\n
error ending transaction: %s\n
nx_block_count is %llu, while device block count is %llu\n
repair_overlapped_extents: update source pext 0x%llx\n
Could not initialize message output\n
%s (id %llu): invalid xattr_obj_id (%llu)\n
clonegroup (group id %llu, private_id %llu, file id %llu): invalid xfields\n
failed to read container superblock\n
dir stats repairs
failed to allocate memory for insertion of dir-stats\n
error updating the reap list: %s\n
Fix unassigned default_crypto_id? 
com.apple.fs.symlink
\ndir-stats %llu (has dir-stats? %d)%s:\nflags: 0x%x\nchained-key: %llu (computed: %llu)\norigin-id: %llu (computed: %llu)\nshadow-key: %llu (exists? %d)\ndescendants: %llu (computed: %llu)\nSAF descendants: %llu\ndir-stats descendants: %ll
inode (id %llu) needs to untrack from dir-stats\n
(oid 0x%llx) %s: dev_write(%llu, %u): %s\n
mount_apfs
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
Set bsd_flags to 0x%x? 
io_get_device_features
invalid ersb_flags (0x%llx), ERSB_FLAG_CID_IS_TWEAK is set but ersb_fext_cid == 0\n
CLONEGROUP_EXT_TYPE_ATTRIBUTION_TAG
omap has %llu snaphots but snap meta tree has %llu\n
apfs superblock at index %u: incompatible features set (apfs_readonly_compatible_features: (0x%llX), apfs_incompatible_features: (0x%llX))\n
 chained-key: %lld\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null VEK, file radar%s\n
refcnt (%u) of dstream id object (id %llu) is greater than expected (%u)\n
Fix object (oid 0x%llx) crypto key index? 
Fix crypto_id? 
Applied
blockcopy: unable to allocate memory for buffer_size 0x%zx.\n
need to update default_crypto_id (%llu) of dstream (object-id %llu) with missing crypto state\n
nx_block_size of %u is invalid\n
Space Verification: failed to allocate memory for the bitmap block\n
free_overlapped_range: free space for source_paddr 0x%llx block_count 0x%llx\n
apfs superblock at index %u: apfs_integrity_meta_oid is invalid.\n
usage: fsck_apfs [ [-q | -n | -y] [-r num] [-l] [-s] [-W] [-S] [-o] [-b num] [-c] [-C] [-d]\n\t\t[-E path] [-F | -M] [-g | -x] [-X] [-T [-D]] ] device\n
omap entry (oid 0x%llx): invalid ov_paddr + ov_size (%llu + %u)\n
(oid 0x%llx) %s: object is encrypted with crypto key index (%u) but should be encrypted with crypto key index (%u)\n
%s (id %llu): xf %u/%u: %s: doc_id exists (%u), despite bsd_flags (0x%x)\n
sibling map
snap_meta_ext: (0x%llx:0x%llx): unknown version (%u)\n
%s (id %llu): invalid hdr.obj_id\n
checkpoint<->%s mismatch on fusion uuid\n
failed to init fsroot tree for file lookup in directory\n
Truncate size to alloced size? 
%s (%llu+%llu): invalid padding\n
dev_read_async
(oid 0x%llx) %s: invalid o_subtype (0x%x, expected 0x%x)\n
nx_xp_data_index (%u) is is larger than nx_xp_data_blocks (%u)\n
Delete omap_snap entries? 
verification/reading of the EFI jumpstart record failed\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: minkey is %s index 0 (should be equal)\n
%s (id %llu): invalid parent_id (%llu) for regular directory\n
could not freeze volume: %s\n
inode (id %llu): finder info internal flag is missing\n
xp_sb->nx_xp_desc_index (%d) doesn't match index block (%d)\n
failed to insert cached doc-id record, doc-id %u,file-id %llu : %s\n
clone size xfield of dir-stats object (id %llu) exists unexpectedly\n
NO\n
er_state
orphan
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_node_count (expected %llu, actual %llu)\n
snapshot name
%s
??? (id ???): invalid key length (%u)\n
failed to look up dir-stats object (id %llu): %s\n
Deferred repairs failed.
found invalid dir-stats object (id %llu)\n
not a root
Snapshot metadata tree is invalid.
apfs_fs_alloc_count is not valid (expected %llu, actual %llu)\n
prev phys extent
CLONEGROUP_EXT_TYPE_DIR_STATS_KEY
unlock
_create_kek_data
%s (id %llu): xf %u/%u: %s: found unexpected dstream associated with non-regular file\n
container keybag
extent
spaceman cib %u address 0x%llx is not in the internal pool\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : key out of order (last paddr 0x%llx, last xid 0x%llx)\n
.
Could not lookup cached extent_ref_tree information at snap xid (0x%llx): %s\n
apfs_sec_root: 
(oid 0x%llx) %s: object read was finished already\n
%s/Library/Logs/fsck_apfs.log
       -M            skip checks which require encrypted volumes to be unlocked\n
io_get_num_device_blocks
%s (id %llu): invalid extentref_tree_type (0x%x)\n
clonegroup (group id %llu, private_id %llu, file id %llu): can't register for cross checks: %d (%s)\n
NX checkpoint descriptor area fragmented metadata tree is invalid\n
```
