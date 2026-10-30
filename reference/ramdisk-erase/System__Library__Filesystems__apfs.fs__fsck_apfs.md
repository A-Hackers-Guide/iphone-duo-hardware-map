# `/System/Library/Filesystems/apfs.fs/fsck_apfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 579,136 bytes.

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
file info: attribution tag (hash %llu) skipping clone size repair because the computed clone size is negative\n
\t\t\t<integer>%llu</integer>\n
file info: attribution tag (hash %llu) skipping clone size repair: full clone size %llu > %llu\n
%s (id %llu): attribution tag xf does not exist, despite internal_flags (0x%llx)\n
(oid 0x%llx) %s: invalid o_oid (0x%llx)\n
need to clear bsd flags (0x%x) in inode (object-id %llu)\n
chained key of dir-stats object (id %llu) does not match expected value (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list, btn_val_free_list, or btn_free_space: %s\n
fstype
orphan omap mapping found for oid %llu\n
unable to initialize fsroot tree iterator for file lookup in directory: %s\n
Fix btree: bt_longest_key (%u)? 
missing encryption rolling recovery data, actual length %llu, ersb_recovery_length %llu\n
INO_EXT_TYPE_DSTREAM
spaceman chunk %llu free count %u > block count %u\n
found a snapshot in the purgatory (xid %llu) with no corresponding omap entry\n
need to set bsd flags (0x%x) in inode (object-id %llu)\n
checkpoint %d (xid %llu) superblock is invalid\n
Deferred repairs failed.
%s (id %llu): invalid file_id (%llu) (%s)\n
skipping dir stats clone sizes repair: present clone size %llu > %llu\n
reap list expected %u objects, but haven't seen last reap list object yet\n
repair_overlapped_extents: insert target pext 0x%llx\n
Deferred repairs skipped.
%s (id %llu): xf %u/%u: %s: invalid doc_id (%u), less than MIN_DOC_ID (%u)\n
origin_id (%llu) of dir-stats object (id %llu) is not as expected (%llu)\n
%s (%llu+%llu): entry %u has blob size == 0\n
Checking the encryption key structures.
/dev/r%ss%d
%s: not a valid disk name/path\n
.%llu
       -x            print output in XML\n
%s (id %llu): invalid owning_obj_id (%llu) for update extent\n
efi_jumpstart
spaceman fs_reserve_block_count %llu is greater than nx_block_count %llu\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep managed vek cannot have flag_no_ephdm%s\n
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield even though the file is marked as purgeable\n
performed too many chained-key iterations (current id %llu); aborting dir-stats repairs\n
omap entry (oid 0x%llx): invalid ov_range (0x%llx+%llu)\n
btree node
block 0 superblock
index %u key
%s (id %llu): xf %u/%u: %s: invalid sibling_id (%llu)\n
OTI
sm
sm_ip
unable to open the volume for repairs: %s\n
Most recent checkpoint is invalid.
xattr size (%u) does not match expected size (%lu)\n
PreventUserIdleDisplaySleep
failed to lookup %s object: %s\n
%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n
nx_ephemeral_info %d: invalid info (0x%llx)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_key_count (overflow)\n
file-id: %6lld flags: %d date-added: %lld hash: 0x%x name-len: %d name: %.*s\n
Fix apfs_fs_reserve_block_count(oid 0x%llx, xid 0x%llx)? 
%s (id %llu): uncompressed_size/rdev/dir_nlink union field is set (%llu) but inode flags and mode do not indicate it should (flags: 0x%llx, mode %u)\n
apfs superblock at index %u: apfs_vol_uuid is NULL\n
alloced_size (%llu) of dstream (id %llu) does not match calculated size (%llu)\n
unable to get the file ids of dstream_id %llu\n
failed to allocate memory for snapshot repair\n
iOS encryption rolling state object: xattr payload (%hu) is too small\n
NX checkpoint descriptor area fragmented metadata tree is invalid\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_val (expected %u, actual %u)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null KEK, file radar%s\n
/dev/
omap snapshot: invalid oms_pad (0x%x)\n
iOS encryption rolling state object: (version %u) lite rolling has invalid current_state (%u)\n
sib-map: %lld\n
/..namedfork/rsrc
spaceman ip bitmap %u at index %u is not invalidated on the free list\n
??? (id %llu): invalid key type (%u)\n
phys extent
0x%016llx
\t\t<key>%s</key> <string>%s</string>\n
apfs superblock at index %u: apfs_formatted_by.timestamp (%llu) is greater than current time (%llu)\n
failed to initialize the doc-id tree: %s\n
(oid 0x%llx) %s: invalid ov_flags (0x%x), crypto key index set for unencrypted object\n
Spaceman IP free queue tree has sfq_count (%llu) greater than IP block count (%llu)\n
spaceman chunk %llu wrong free count: %u, expected %u\n
%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: index %u is %s index %u (should be less than)\n
%s (id %llu): invalid file_id (%llu)\n
dir_stats (id %llu) already has a registered origin (id %llu), but we found another one (id %llu)\n
nx_features has unsupported flags: (0x%llX)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_level (%u), given btree node is %s\n
apfs_fs_index (%d) is not valid (%d)\n
om: invalid om_snap_count (overflow)\n
%s (id %llu): invalid flags (0x%x), given name (<%.*s> ; name_len %d)\n
%s (id %llu): Invalid hash at offset %llu\n
\t%-14s: %s\n
Xattr
failed to search for clone mapping (private_id %llu,  file_id %llu) to update compressed clone size: %s (%d)\n
unable to add tree node repair at key id %llu : %s\n
clone size xfield of dir-stats object (id %llu) exists unexpectedly\n
mismatch between extentref entry reference count (%d) and calculated fsroot entry reference count (0) for extent (%llu + %llu)\n
?
option -Z is deprecated, ignoring\n
found orphan file extent (id %llu) at logical address %llu\n
|\n
PhysExtent
fsroot tree is invalid.
failed to allocate memory for fsck_state\n
no snap_meta tree entry found for omap_snap entry with xid %llu\n
found shadow key (%llu) on non-calculating dir-stats object (id %llu)\n
Remove entry with null UUID? 
gbitmap_blk
%s xfield of dir-stats object (id %llu) does not match expected value (%llu)\n
file info: attribution tag (hash %llu): physical size (%llu) does not match computed size (%llu)\n
??? (id %llu): invalid key length (%u)\n
failed to initialize the fsroot tree: %s\n
Clear
spaceman cib count %u is inconsistent with chunk count %llu and chunks per cib %u\n
Invalid volume index passed\n
bt
crypto state
could not open %s to prevent reclaims: %s\n
reap list expected %u objects, but got last reap list object with %u more objects left\n
spaceman chunk count %llu is inconsistent with block count %llu and blocks per chunk %u\n
%s (id %llu): xf %u/%u: %s: found on a non class F file\n
resource fork size (%llu) of dir-stats object (id %llu) exists unexpectedly\n
failed to register the clonegroup trees in the fsck memory storage\n
 type: %u logical addr: %lld\n
found cloned xattr dstream (id %llu, object-ids %s)\n
down
inode (id %llu): failed to enqueue to the repairs\n
The volume %s with UUID %s appears to be OK.
failed to enable crypto I/O mode for container %s: %s\n
dir stats repairs
inode (id %llu): dataless bsd_flag is set, but the compression xattr is missing\n
nx_fusion_mt_oid should be invalid but isn't\n
failed to allocate memory for file lookup in purgatory directory\n
refcnt: %d \n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u\n
nchildren of inode object (id %llu) does not match expected value (%d)\n
clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect dir-stats key (%llu)\n
could not retrieve gbitmap from er_state_phys_t\n
Failed to get keybag : %s\n
error iterating physical extent tree: %s\n
apfs superblock at index %u: apfs_revert_to_xid is %llu, but sblock oid is invalid\n
%s/nx
private_id (%llu) has multiple clonegroup ids (%llu, %llu)\n
0
failed to update clone mapping (private_id %llu,  file_id %llu) with compressed clone size: %s (%d)\n
failed to insert clone mapping (private_id %llu,  file_id %llu, flags 0x%x): %s (%d)\n
clonegroup (group id %llu, private_id %llu, file id %llu): unknown flags (0x%x / known flags are: 0x%x)
failed to allocate memory for snapshot tracking\n
fsck_apfs
Invalid disk file-descriptor path\n
%s (%s)
main
disabling overallocation repairs by default; use -o to override\n
       -D            scavenge disk\n
The volume %s with UUID %s could not be repaired.
iOS encryption rolling state object: failed to allocate ierso\n
hash validation: invalid node %llu (root %llu)\n
zero type
sec
nrl
resource fork size of dir-stats object (id %llu) does not match expected value (%llu)\n
failed to sparse VEK extents for resource fork of inode (%llu): %s\n
unable to access %s: %s\n
%s (id %llu): extent crypto flag missing on encrypted volume\n
purgeable size xfield is missing from dir-stats object (id %llu)\n
Fix apfs_num_snapshots(oid 0x%llx, xid 0x%llx)? 
Invalid file descriptor passed\n
Failed to close password file descriptor: %s\n
ersb_recovery_extents_count is %llu, extent descriptor size is %zu, expected descriptors length is %llu > ersb_recovery_length %llu\n
n
\t\t[%4llu - %4llu) [%4s] = %d\n
sec fs root tree
spaceman chunk %llu free count %u of unallocated bitmap != block count %u\n
%s (id %llu): invalid value length (%u), given name_len (%u)\n
%s (id %llu): invalid dir-stats flags (0x%x) on volume without attribution tags\n
dir stats
unable to init physical extent tree iterator for repairs: %s\n
\t<dict>\n
%s (id %llu): Bad phys_block_num + len (%llu + %llu) for physical file extent record\n
Overlap repair pass...\n
apfs superblock at index %u: apfs_integrity_meta_oid is invalid.\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u, max %u\n
detected invalid fsroot tree nodes (& thus data loss), pruning the nodes to make the system usable\n
Document ID tree is invalid.
IOMatchCategory
%s (id %llu): unknown flags (0x%x / known flags are: 0x%x)\n
Could not iterate extentref tree to read reaper objects(oid 0x%llx): %s\n
checkpoint map o_xid (0x%llx) doesn't match checkpoint superblock o_xid (0x%llx)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btn_btree.bt_fixed.bt_key_size (%u) and btn_btree.bt_fixed.bt_val_size (%u)\n
apfs superblock at index %u: apfs_prev_doc_id_tree_oid is set (%llu), despite apfs_doc_id_index_flags (0x%x)\n
failed to iterate the spaceman free queue tree: %s\n
spaceman IP range is invalid: 0x%llx+0x%llx\n
Node counts:
Cache %s time:
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: index %u is %s maxkey (should be less than)\n
physical extent
failed to remove node at segment (%llu) error : %s\n
INO_EXT_TYPE_PURGEABLE_FLAGS
/var/log/fsck_apfs.log
found file extent gap (id %llu) at logical address %llu (expected %llu)\n
%s (id %llu): invalid nonzero crypto_id (%llu) on unencrypted volume\n
INO_EXT_TYPE_ORIG_SYNC_ROOT_ID
found invalid dir-stats object (id %llu)\n
nx_xp_data_index (%u) puts the checkpoint data outside of its range\n
spaceman struct range %u+%u lies outside the struct itself (size %u)\n
com.apple.fs.cow-exempt-file-count
could not lookup extent at %llu for physical extent repair: %s\n
directory valence check: directory (oid 0x%llx): orphan directory record\n
</plist>\n
%s (id %llu): invalid nchildren (%d)\n
can't add purgeable size for dir-stats: %s (%d)\n
found orphan/invalid purgeable record (file_id %llu, atime %llu)\n
flags: 0x%x data-len: %d name: %.*s\n
dstream
(oid 0x%llx) %s: object read was finished already\n
category
Extent ref tree is invalid.
%s (id %llu): com.apple.ResourceFork is expected to be stream based\n
file info: found orphan attribution tag with hash (%llu)\n
iOS encryption rolling state object: non-iOS content protected volume unexpectedly has ierso\n
need to insert spaceman free queue tree entry (0x%llx+%llu, xid %llu) to replace existing overlapping ranges\n
refcnt of dstream id object (id %llu) less than expected\n
io_get_device_block_size
a root
sm_fs_reserve_block_count is not valid (expected %llu, actual %llu)\n
clone mapping
%s %llu/%llu repairs of this type in total.\n
%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than CLONEGROUP_ID_MIN (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unexpected btn_btree.bt_fixed.bt_flags (0x%x)\n
Fix sm_fs_reserve_block_count? 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n
b:cCdE:fFglnMopqr:sSWxXyZTD
%s (id %llu): sparse bytes mismatch for a file in the purgatory\n
(oid 0x%llx) %s: object is encrypted with crypto key index (%u) but should be encrypted with crypto key index (%u)\n
inode (id %llu): Resource Fork xattr is missing or empty for compressed file\n
\t\t<key>%s</key>\n
apfs_next_obj_id is not valid (expected %llu, actual %llu)\n
%s (id %llu): invalid parent_id (%llu) for regular directory\n
INO_EXT_TYPE_DIR_STATS_KEY
 (
reap list object 0x%llx max record count %u different than expected %lu\n
%s (id %llu): invalid state.key_len (%u)\n
%s (%llu+%llu): block range isn't a valid keybag, aborting\n
NX checkpoint data area fragmented metadata tree is invalid\n
fsck_messages.c
failed to get fsroot tree to find expanded dir-stats %llu: %s\n
spaceman ip bm list has a loop\n
iOS encryption rolling state object: xattr invalid storage type, flags (%hu)\n
NX keybag data range is invalid: 0x%llx+%llu\n
       -S            skip iteration of snapshots, although no repairs can be made.\n
(oid 0x%llx) %s: invalid o_type (0x%x, expected 0x%x)\n
(oid 0x%llx) %s: using old subtype (0x%x, expected 0x%x)\n
prev phys extent
nx_ephemeral_info 0: invalid version (%u), should be: (%d)\n
File key rolling tree is invalid.
failed to read spaceman cib %u at address 0x%llx\n
Fix apfs_next_obj_id(oid 0x%llx, xid 0x%llx)? 
apfs_num_directories is not valid (expected %llu, actual %llu)\n
need to clear flags (0x%llx) in inode (object-id %llu)\n
The volume was modified
pfk_val : object (oid 0x%llx): unknown version (%u)\n
Fix object (oid 0x%llx) crypto key index? 
%s (id %llu): dstream xf does not exist, despite existence of sparse bytes xf\n
resource fork size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
INO_EXT_TYPE_SNAP_XID
Spaceman Repair: failed to allocate memory for the bitmap block\n
unable to init omap_snap tree for snapshot repair\n
Insert missing %s objects? 
Fix snapshot meta name_len (%u) from snap name entry? 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 1%s\n
%s (id %llu): invalid internal_flags (0x%llx), (dir-stats SAF but not dir-stats maintained)\n
found shadow dir-stats object (id %llu) but did not find its calculating dir-stats (%llu)\n
reaper list entry (index (%u) list oid (0x%llx)) : cycle detected\n
spaceman cib out of order: %u, expected %u\n
reaper list entry (index (%u) list oid (0x%llx)) : index not less than nrl_max (%u)\n
invalid EFI jumpstart record file length: %d\n
Fix btn_level (%u)? 
can't add attribution tag for clone mapping: %s (%d)\n
file info
unable to iterate snap fsroot tree for tree node repairs: %s\n
unable to enqueue tree node insertion repairs: %s\n
%s (%llu+%llu): UUID %s of entry %u (tag %u) is not the container UUID %s\n
snap_meta_ext
FILE_INFO_TAG_EXT_TYPE_SIGNING_ID
 type: %u hash: 0x%llx total_count: %llu physical_size: %llu flags: 0x%x\n
omap snapshot: invalid oms_flags (0x%x)\n
error starting transaction: %s\n
Fix snapshot meta name (%.*s) from snap name entry? 
failed to init fsroot tree for lookup in directory\n
 atime: %llu file_id: %llu file_size: %llu dstream_id: %llu flags: 0x%x owning_uid: %u\n
directory
failed to initialize tree for volume repairs\n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/platform/platform_lib.c
omap (oid 0x%llx): invalid om_pending_revert_max (0x%llx), given om_flags (0x%x)\n
Could not lookup cached extent_ref_tree information at snap xid (0x%llx): %s\n
clonegroup (group id %llu, private_id %llu, file id %llu): inum is invalid\n
%s (%llu+%llu): entry %u has blob size %u > maximum blob size %u\n
dir-stats object (id %llu): %s overflow\n
Skipping clonegroup cross-check since INVALID flag is set\n
failed to mark cached doc-id tree record %d as verified error : %s\n
Requested cache size: %s (%uk blocks * %ukB)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n
can't add dir stats key for clone mapping: %s (%d)\n
sparse bytes overflow (current %llu, update %llu)\n
missing crypto state object (id %llu) referenced by %u file extents / dstreams\n
doc-id tree record exists for doc-id %u, but no inode references this doc-id\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list length (%u), given total key length (%u)\n
%s (id %llu): failed to register dir-stats (%llu) descendant: %d\n
recovery extent #%llu: invalid prange (0x%llx+%llu), dev_bsize %u\n
Fix sme_snap_xid (xid 0x%llx)? 
container keybag
%d %%
INO_EXT_TYPE_SAF_DIR_STATS_KEY
unable to load inode (id %llu) to repair dir-stats chained key: %s\n
found orphan/unexpected crypto state object (id %llu)\n
The volume %s cannot be verified when it is in use.
could not look up cpm_map[%d].cpm_paddr (%llu) in checkpoint data area\n
Failed to allocate memory for keybag\n
%s (id %llu): Bad phys_block_num + len (%llu) for physical extent record\n
cpm_count is 0\n
(oid 0x%llx) %s: dev_write(%llu, %u): %s\n
error (%d) reading spaceman IP bitmap block at index %u, addr 0x%llx\n
/dev/fd/
tried to remove snap_name entry but it's not there!\n
%s (id %llu): invalid inum (%llu)\n
can't add clone size for dir-stats: %s (%d)\n
clone mapping (private_id %llu, file_id %llu) is orphan\n
%s (id %llu): fext tree record present on non-sealed volume\n
inode (id %llu): can't add internal flags repair: %d (%s)\n
physical size of dir-stats object (id %llu) does not match expected value (%llu)\n
Space Verification: failed to lookup paddr (%llu) : error %s\n
PROGRESS
integrity_meta: (0x%llx:0x%llx): invalid root hash offset (%u+%u) > %u\n
Fix apfs_clonegroup_next_id(oid 0x%llx, xid 0x%llx)? 
Fix crypto_id? 
clone group tree (id %llu): invalid key length (%u)\n
less
dir-stats (id %llu) is missing\n
nx_flags (0x%llx) has an unknown flag set \n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/aeskeywrap.c
can't add clone mapping (private_id %llu, file_id %llu) for repairs: %s (%d)\n
%s (id %llu): xf %u/%u: %s: invalid dstream\n
speculative download xattr (id %llu): found outside of an SAF dir stats hierarchy\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_node_size (%u), given mt_node_size (%u)\n
spaceman IP bitmap blocks field is %u, but sum of ranges is %llu\n
Try running fsck against the entire APFS container instead of a volume\n
%s (id %llu): xf %u/%u: %s: failed to register dir-stats (%llu) origin: %d\n
bitmap store: address %llu is beyond maximum allowed %llu\n
(oid 0x%llx) %s: invalid object size (0x%x)\n
(oid 0x%llx) %s: object is encrypted with crypto key index (%u)but omap says it's encrypted with crypto key index (%u)\n
inode with file-id %llu has doc-id %u but doc-id tree record is missing\n
orphan/invalid physical extent (%llu)\n
get_fext_tree() called on unsealed volume\n
AppleAPFSContainerScheme
failed to add PFKUR entry for inode (%llu): %s\n
val size is too small, actual: %u, minimum: %u\n
spaceman free count is too large: %llu > %llu\n
found clone group tree in invalid volume format\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %u
invalid sblock_oid (%llu)\n
nx_xp_data_len (%u) is less than 2\n
failed to allocate memory for device path\n
error (%d) writing cib\n
%s (id %llu): invalid dstream.default_crypto_id (%llu)\n
%s (id %llu): invalid sparse extent with nonzero crypto_id (%llu)\n
\n
Fix object (oid 0x%llx) bit flip? 
unable to setup snapshot tree iteration: %s\n
Snapshot is invalid.
container %s is mounted.\n
clonegroup (group id %llu, private_id %llu, file id %llu): private_id is invalid\n
file info: computed count overflow for hash (%llu)\n
dev_read_async
failed to validate object with crypto key index (%u), retrying with (%u)\n
(oid 0x%llx) %s: object is %s but should be %s\n
failed to initialize the extentref tree: %s\n
spaceman cab %u wrong number of cibs: %u, expected %u\n
found unexpected EFI jumpstart record\n
data_hash: object (oid 0x%llx): Found unexpected hash at offset %llu (expected length %llu)\n
Fix inode_val: internal_flags (0x%llx)? 
Fix unassigned default_crypto_id? 
%s (id %llu): doc_id xf does not exist, despite bsd_flags (0x%x)\n
need to set flags (0x%llx) in inode (object-id %llu)\n
the checkpoint superblock has a lower o_xid (%lld) than the %s (%lld)\n
apfs_num_files is not valid (expected %llu, actual %llu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode blob%s\n
can't add orphan clone mapping (private_id %llu, file_id %llu) to the fsck repairs: %s (%d)\n
fsck may bail out with overallocation - could not mark space allocated in fsck's version of the bitmap (%lld + %lld)\n
container
%llu
could not insert extent with range (%llu + %llu) for physical extent repair: %s\n
apfs superblock at index %u: apfs_omap_oid is invalid.\n
user
found file extent (id %llu) at logical address %llu beyond the end of the dstream %llu\n
** 
Remove entry with invalid blob? 
iOS encryption rolling state object: xattr record too small (%zu)\n
file info: failed to allocate memory\n
Device Characteristics
unable to init fsroot tree: %s\n
repair_overlapped_extents: unable to target update target pext 0x%llx for fs_oid 0x%llx (refcnt leak): %s\n
clone mapping (private_id %llu, file_id %llu): invalid physical_size (%llu)\n
reap list object 0x%llx record count %u larger than max %u\n
Executing %s (version %s).
CloneMap
(%d %%)\n
apfs superblock at index %u: apfs_doc_id_fixup_cursor (%llu) is greater than or equal to apfs_next_obj_id (%llu)\n
resource fork size
(oid 0x%llx) %s: found zeroed-out block\n
\texpected hash: %s\n
%d failures and %d warnings issued; failing execution as requested.\n
apfs superblock at index %u: apfs_next_doc_id (%u) should not be less than MIN_DOC_ID (%d)\n
unable to init fsroot tree iterator: %s\n
error iterating trees during free queue tree repair: %s\n
apfs superblock at index %u: apfs reserve alloc count (%llu) is greater than spaceman reserve alloc count (%llu) for a guaranteed-minimum space FS\n
failed to get cib for chunk index %llu: %s\n
Remove invalid flag (0x%02x)? 
shadow dir-stats object (id %llu) unexpectedly has origin-id\n
failed to init fsroot tree to mark dir-stats chain as inconsistent\n
snapshot name
VERIFY
dir-stats object (id %llu) unexpectedly unmarked as having origin-id\n
spaceman ip bitmap block at index [%u] is neither on the sm_ip_bitmap[] nor on the free list\n
clone group tree: unknown type (%u)\n
%s (id %llu): xf %u/%u: %s: found attribution tag on an inode with unsupported flags\n
inode (id %llu): compression type is dataless, but the dataless bsd_flag is not set\n
sibling map
warning: 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n
%s (id %llu): invalid dstream.default_crypto_id (%llu) on unencrypted volume, given apfs_fs_flags (0x%llx)\n
found orphan dstream id object (id %llu)\n
Spaceman free queue tree of type [%s] has sfq_count (%llu) mismatch with cumulative counts in the tree (%llu)\n
Fix apfs_num_files(oid 0x%llx, xid 0x%llx)? 
usage: fsck_apfs [ [-q | -n | -y] [-r num] [-l] [-s] [-W] [-S] [-o] [-b num] [-c] [-C] [-d]\n\t\t[-E path] [-F | -M] [-g | -x] [-X] [-T [-D]] ] device\n
failed to enqueue purgeable record (file id %llu, atime %llu) for remove\n
apfs_extentref: 
failed to run predicate callback on inode (oid 0x%llx) for lookup in directory: %s\n
volume metadata
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 2%s\n
The volume %s was formatted by %s and last modified by %s.
xp_sb->nx_xp_desc_index (%d) doesn't match index block (%d)\n
integrity_meta: (0x%llx:0x%llx): unknown hash type (%u)\n
aborting jobj validations for current fsck pass - trying to repair fsroot tree with invalid nodes\n
%s (id %llu): xf %u/%u: %s: unable to remove dstream of non-regular inode\n
%s (id %llu): invalid hash (0)\n
iOS encryption rolling state object: current_offset (%llu) too large\n
container %s is mounted. repairs in a mounted container is not supported yet.\n
apfs superblock at index %u: apfs_extentref_tree_type is invalid: 0x%x\n
media keybag
found orphan directory record object (id %llu)\n
live repair of a volume in mounted container %s is not supported yet.\n
Reached max number of fsck passes during repair\n
apfs superblock at index %u: apfs_volname[0] == 0\n
%s (id %llu): present on sealed volume\n
btn
(oid 0x%llx) %s: could not repair object to match checksum: too many bit flip candidates (%d)\n
failed to look up checkpoint block address %d: %s\n
failed to allocate memory for the bitmap block\n
Space manager is invalid.
Space Allocation: failed to allocate memory\n
Fix inode_val: parent_id (%llu)? 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unexpected btn_flags (0x%x)\n
Fix btree: bt_node_count (%llu)? 
       -C            force a sync prior to freezing for live fsck\n
Could not initialize omap tree (oid 0x%llx): %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u), given total key length (%u)\n
extent ref tree
%s (id %llu): xf %u/%u: %s: failed to register dstream: %d\n
Update %s objects? 
checkpoint %d (xid %llu) fsck_obj_phys failed\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid node hash\n
ersb_progress (%llu) exceeds ersb_total_blk_to_encrypt (%llu)\n
repair_overlapped_extents: remove source pext 0x%llx\n
Conflicting options: [ -y ] option cannot be run with the [ -n | -l ] options\n
%s (id %llu): invalid dstream_id (%llu)\n
%s (%llu+%llu): number of entries %u exceeds object capacity %lu\n
iOS encryption rolling state object: (version %u) current_state unset, yet non-zero current_id (%llu)
Checking the space manager free queue trees.
spaceman blocks per chunk %u is inconsistent with block size %u\n
       -r <num>      read password for encrypted external volume from file descriptor <num>\n
purgeable size xfield of dir-stats object (id %llu) exists unexpectedly\n
performed too many chained-key iterations (current id %llu); can't mark the entire chain as needing reconciliation\n
reaper list entry (index (%u) list oid (0x%llx)) : invalid flags (0x%x) set\n
nx_block_count is %llu, while device block count is %llu\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid implicit stash%s\n
com.apple.fs.graft-vol-uuid
fsck cache stats:\n
cpm_map[%d].cpm_subtype has nonzero storage type (0x%x)\n
CryptoState
AppleAPFSSnapshot
unable to mark allocated blocks for volume oid %llu\n
omap (oid 0x%llx): invalid om_snap_count (%u), given om_flags (0x%x)\n
%s (id %llu): xf %u/%u: %s: extended field at offset %u+%u extends beyond xf_used_data (%u)\n
extent
Set missing flags? 
snap_meta_ext: (0x%llx:0x%llx): unknown version (%u)\n
dir-stats object (id %llu) is SAF, but its origin isn't\n
cannot find checkpoint area because container superblock is too damaged\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space (%u, %u), given btn_flags (0x%x)\n
expanded directory stats
%s (id %llu): invalid pad2 (0x%x)\n
Could not initialize extentref tree (oid 0x%llx): %s\n
object (oid 0x%llx): o_xid invalid, o_xid %llu is greater than nx_next_xid: %llu\n
INO_EXT_TYPE_CLONEGROUP_ID
repair_overlapped_extents: free space for target_paddr 0x%llx block_count 0x%llx\n
:%d
unknown spaceman struct version %u > %u\n
io_get_device_features
Spaceman internal pool bitmap fragmented metadata tree is invalid\n
file-id: %6lld flags: %d date-added: %lld name-len: %d name: %.*s\n
 extentref_tree_oid: %lld sblock_oid: %lld change_time: %llu create_time: %llu\n
spaceman ip bm block count is bad: %d\n
error (%d) writing bitmap @ %lld\n
(oid 0x%llx) %s: invalid crypto key index (%u) given obj_subtype\n
the EFI jumpstart entry has length %u but occupies %llu blocks of size %u\n
error (%d) looking up spaceman IP bitmap block at index %u\n
Invalidate spaceman ip bm free list at index at index %u? 
fv_encode_vek_blob
error (%d) getting cib %u @ %lld\n
Failed to unwrap encrypted volume keybag using the provided password: %s\n
Mark volume for doc-id tree cleanup on next mount? 
failed to allocate memory for dir-stats lookup\n
dev_read
spaceman free count %llu does not match sum of free counts %llu\n
can't find new dir-stats key for inode (id %llu): error %d\n
failed to read container superblock\n
missing clone group record for file_id %llu (private_id %llu, group_id %llu)\n
Checking deleted snapshot residual state.
refcnt (%u) of dstream id object (id %llu) is greater than expected (%u)\n
%s (id %llu): xf %u/%u: %s: doc_id exists (%u), despite bsd_flags (0x%x)\n
nx_xp_desc_len (%u) is larger than nx_xp_desc_blocks (%u)\n
%s (%llu+%llu): number of bytes %u exceeds object size %u\n
  
invalid gbitmap block oid 0x%llx for key 0x%llx\n
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on directory without INODE_MARK_CHILD_PURGEABLE flag\n
error (%d) getting cab %u @ %lld\n
%s (id %llu): xf %u/%u: %s: unable to add repair for unexpected xfield: %s\n
%s (id %llu): Logical address %llu not a multiple of the block size (%u)\n
error updating omap entry: %s\n
inode (id %llu): dataless bsd_flag is set, but compression bsd_flag is not\n
BSD Minor
FileInfo
can't add attribution tag for clonegroup: %s (%d)\n
 * * * cannot allocate memory * * *\n
wr=%d wl=%d
fv_rewrap_kek
%s: can't create path to container\n
Checking the space manager.
clone mapping (private_id %llu, file_id %llu): physical size (%llu) != inode (id %llu) physical size (%llu)\n
%s: error %d from IORegistryEntryGetParentEntry\n
failed to register the dstream tree in the fsck memory storage\n
Allocated (%llu) MB for cached btrees in %u blocks, limit is (%llu) MB\n
(oid 0x%llx) %s: invalid encryption type ov_flags (0x%x)\n
failed to allocate memory to add an xfield\n
fsck_msg_number
%s xfield of dir-stats object (id %llu) exists unexpectedly\n
Expanded
error: 
INFORMATION
unable to init snap_meta tree iterator for snapshot repair: %s\n
found invalid directory record object (id %llu)\n
nx_xp_desc_next (%u) is larger than the # of nx_xp_desc_blocks (%u)\n
error (%d) looking up spaceman IP block address at index %u\n
failed to remove snap_name entry: %s\n
Allocate new doc-id %u for file-id %llu? 
nx_block_size of %u is invalid\n
Status
Fix spaceman free queue tree sfq_oldest_xid (oid 0x%llx)? 
Keybag size is too large\n
invalid doc-id record, file-id is 0 for doc-id %u\n
file extents
inode (id %llu): has the compression bsdflag, but doesn't have the compression xattr\n
tried to remove %s object but it wasn't there!\n
       -l            live fsck (lock down for verify-only)\n
disk
iOS encryption rolling state object: (version %u) timestamps unordered: start_time (%llu) <= end_time (%llu) <= current_time (%llu)\n
DIR_STATS_EXT_TYPE_PURGEABLE_SIZE
Tree node repair failed.
Fix apfs_modified_by[%d].id(oid 0x%llx, xid 0x%llx)? 
Fix apfs_num_directories(oid 0x%llx, xid 0x%llx)? 
found xattr dstream (id %llu, name %.*s) that references a missing crypto state\n
%s:%d: can't get the device block size (%s). assuming 512\n
cpm_o.o_oid (0x%llx) doesn't match the physical address (0x%llx)\n
\t%-32s %.2lf [usec]\n
failed to update %s object: %s\n
nx_spaceman_oid is invalid\n
%s BTNODE_LEAF flag? 
er_state->ersb_version is %d, should be at most %d\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in free queue tree is not a valid address range on disk\n
unable to insert tree node at key id %llu for repairs : %s\n
%s (id %llu): invalid key length (%u), given name_len (%u)\n
%s:%d: Hit an error flushing the cache, %d dev_name = %s\n
INO_EXT_TYPE_ATTRIBUTION_TAG
fs root tree
obsolete spaceman tier2 fields should be empty but they aren't\n
apfs superblock at index %u: apfs_sec_root_tree_oid is invalid\n
omap entry (oid 0x%llx): invalid crypto key index (%u) given ov_flags (0x%x)\n
btree node (oid (0%llx)) being reaped has invalid val_len (%u) at index (%d) \n
checkpoint %d (xid %llu) superblock disagrees with block 0\n
BSD Name
failed to traverse prev doc-id tree : %s\n
clone mapping (private_id %llu, file_id %llu): invalid private_id\n
 embedded data size: %d\n
apfs superblock at index %u: apfs_volname (%.*s) is not NULL terminated.\n
com.apple.system.fs.speculative_telemetry
failed to repair inode nlink (id %llu): %s\n
Total blocks allocated by spaceman: %llu\n\n
       -W            treat warnings as errors\n
%s (id %llu): invalid chained_key (%llu)\n
iOS encryption rolling state object: (version %u) invalid policy (%u)\n
omap
dir_nlink of inode object (id %llu) does not match expected value (%d)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u), given btn_flags (0x%x)\n
nx_read_only_compatible_features has unsupported flags: (0x%llX)\n
       -q            quick check if the superblock and checkpoint superblock are valid.\n
The container %s could not be verified completely.
_fd_dev_write
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list entry (%u, %u)\n
other
Checking the APFS volume superblock.
clone mapping (private_id %llu, file_id %llu): compressed physical size (%llu) != inode (id %llu) compressed physical size (%llu)\n
unable to init fsroot tree for dstream repair\n
file (id %llu) purgeable_flags (0x%x) disagree with its matching clonegroup record flags (0x%x)\n
Failed to fix %s\n
    |
userfs_data_cryptor
file info: orphan attribution tag with hash (%llu)\n
unable to add tree repair at key at id %llu : %s\n
clone size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
iOS encryption rolling state object: size (%u), version (%u) does not match expected size (%zu)\n
INO_EXT_TYPE_UNRAW_SIZE
%s (id %llu): Logical address %llu of file extent not a multiple of the block size (%u)\n
snapshot fsroot / file key rolling / doc-id / clone group tree corruptions are not repaired; they'll go away once the snapshot is deleted\n
unable to allocate memory for tree repairs\n
Protocol Characteristics
pfk_val : object (oid 0x%llx): invalid current_offset (%llu)\n
PurgeableTombstone
com.apple.system.Security
IOService
(oid 0x%llx) %s: should be encrypted (ov_flags 0x%x)\n
repair_overlapped_extents: unable to update fext 0x%llx 0x%llx for fs_oid 0x%llx: %s\n
%-20s%-15llu\n
fsckPrint
unexpected spaceman struct size %u != %u\n
clone mapping (private_id %llu, file_id %llu): purgeable status is different than inode (id %llu) purgeable status\n
bitmap was not entirely set, stopping deallocation\n
found orphan omap mapping (oid %llu xid %llu)\n
alloced_size of dstream (object-id %llu) does not match minimum found size (%llu)\n
DIR_STATS_EXT_TYPE_SHADOW_KEY
%s:%d: Zero'ing excess data to %s: paddr %lld, completed %lld, remaining %zu\n
failed to init the dir stats repair tree\n
image-format-read-only
overallocation detected in internal pool: (0x%llx+%llu) bitmap address (0x%llx)\n
%llu\n
Remove orphan entry? 
found an orphan purgeable record (atime %llu, file_id %llu)\n
file info: attribution tag with invalid hash (%llu)\n
file key rolling
verification/reading of the EFI jumpstart record failed\n
can't allocate memory to insert a new clonegroup value\n
Checking the document ID tree.
object (oid 0x%llx): Unable to mark spaceman ip range (0x%llx + %llu) allocated for space verification\n
%s: 
FAIL
file extent length %llu does not fit inside %u bits, refusing to repair\n
underallocation
no omap_snap tree entry found for snap_meta entry with xid %llu\n
\ndir-stats %llu (has dir-stats? %d)%s:\nflags: 0x%x\nchained-key: %llu (computed: %llu)\norigin-id: %llu (computed: %llu)\nshadow-key: %llu (exists? %d)\ndescendants: %llu (computed: %llu)\nSAF descendants: %llu\ndir-stats descendants: %ll
volume keybag
(oid 0x%llx) %s: invalid o_cksum (0x%llx)\n
xp_map->cpm_map[%d].cpm_size (%u) is not a multiple of nx_block_size (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x)\n
<plist version=\"1.0\">\n
data_hash: object (oid 0x%llx): Invalid length at offset %llu\n
file info: attribution tag (hash %llu): full clone size does not match expected value (%llu)\n
clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n
%s (id %llu): invalid hdr.obj_id\n
directory valence check: directory (oid 0x%llx): nlink (%d) does not match subdirectory count (%d)\n
spaceman datazone current boundaries (%llu -> %llu) is not a valid address range on disk\n
failed to initialize the pfkur tree: %s\n
no valid checkpoint found\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: can't compare key (%u) with key (%u)\n
repair_overlapped_extents: unable to load fext 0x%llx 0x%llx for fs_oid 0x%llx: %s\n
checkpoint<->%s mismatch on nx_xp_desc_blocks: %d %d\n
pfk_val : object (oid 0x%llx): invalid current_ns_offset (%llu)\n
obj-id: %8lld type: %-11s\n
fsck_verbosity
\t\t\t<integer>%p</integer>\n
alloced_size (%llu) of dstream (id %llu, object-id %llu) does not match minimum found size (%llu)\n
%s (id %llu): signing id does not exist\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: validate_loc_ctx_alloc failed for btn_nkeys (%u)\n
skipping dir stats clone sizes repair because the clone mapping repairs were aborted\n
clone size
%s (%llu+%llu): %s records entry %u contains invalid range %llu+%llu\n
UNKNOWN
Fix apfs_num_other_fsobjects(oid 0x%llx, xid 0x%llx)? 
AppleAPFSMedia
checkpoint<->%s mismatch on nx_block_size: %d %d\n
apfs superblock at index %u: apfs_extentref_tree_oid is invalid.\n
too many parent chain lookups during missing dir-stats repairs\n
failed to initialize the fext tree: %s\n
%s:%d: failed to open volume device %s: %s\n
io_get_num_device_blocks
%s (id %llu): xf %u/%u: %s: found rdev x-field even though inode is not a char/block device\n
%s (id %llu): invalid physical size (%llu) for hash (%llu)\n
purgeable size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
failed to register the purgeable tree in the fsck memory storage\n
repair_overlapped_extents: unable to update source pext 0x%llx for fs_oid 0x%llx (refcnt leak): %s\n
Fix corrupt container superblock? 
error iterating trees during snapshot repair: %s\n
NX checkpoint data range is invalid: 0x%llx+0x%x\n
%s: couldn't find APFS container\n
%s (id %llu): invalid value length (%u)\n
DirStats
1
%s (id %llu): found dir-stats object (chained-key %llu) that is unexpectedly being moved\n
Overlapping object: (oid : 0x%llx) (type : %u) (subtype : %u), (%llu + %llu)\n
found clone mapping in an unsupported volume format\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_node_count (expected %llu, actual %llu)\n
vers: %u.%u flags: %#x class: %c os: 
%d\n
%s (id %llu): invalid hash (0x%x, expected 0x%x) of name (%.*s)\n
%s:%d: can't get features for device (%s)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given btn_btree.bt_fixed.bt_flags (0x%x)\n
can't cross check inode (id %llu) with its corresponding clonegroup record: %d (%s)\n
invalid ersb_flags (0x%llx), exactly one of ERSB_FLAG_ENCRYPTING and ERSB_FLAG_DECRYPTING bits must be set\n
invalid checksum block size, enum: %llu\n
INO_EXT_TYPE_NAME
could not open %s to freeze the volume: %s\n
found non-shadow dir-stats object (id %llu) that has calculating dir-stats\n
checkpoint %d fsck_obj_phys failed\n
found EFI jumpstart record of unknown version %d (max known: %d)\n
spaceman
file
clone mapping (private_id %llu, file_id %llu): dir stats key (%llu) != inode (id %llu) dir stats key (%llu)\n
%s (%llu+%llu): entry %u has invalid blob range %llu+%llu\n
nx
could not get the current executable path of %s\n
enabling overallocation repairs because -o was passed; this may cause data loss\n
w
%s (%llu+%llu): oti_ke_blob_len (%u) is too large\n
repair_overlapped_extents: failed to copy paddr 0x%llx to paddr 0x%llx, block_count 0x%llx: %s\n
sfqe_key : (paddr 0x%llx, xid 0x%llx) : invalid xid\n
no snap_name entry found for snap_meta entry with xid %llu and name %.*s\n
dev_init_common
found spaceman free queue tree entry (0x%llx+%llu, xid %llu) which overlaps with existing range (0x%llx+%llu)\n
_cmd_stash_kek
com.apple.fs.graft-jobj-id-len
checkpoint<->%s mismatch on fusion uuid\n
a leaf
free_overlapped_range: free space for source_paddr 0x%llx block_count 0x%llx\n
need to mark dir-stats %llu as needing reconciliation, due to an issue with dir-stats %llu\n
Target Disk Mode
Missing required option: [ -D ] option requires the [ -T ] option\n
SAF descendants (%llu) of dir-stats object (id %llu) is greater than expected (0)\n
apfs_sec_root: 
%s/apfs
overallocation
Fix apfs_doc_id_tree_type? 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s user uuid unexpectedly match new kek uuid%s\n
%s (id %llu): uncompressed size is set (%llu) but has-uncompressed-size flag is not set (flags: 0x%llx)\n
%s (id %llu): signing id hash (%llu) for signing id (%s) with length (%zu) does not match attribution tag hash (%llu)\n
%s: %llu orphan mappings found\n
mismatch between extentref entry reference count (0) and calculated fsroot entry reference count (%d) for extent (%llu + %llu)\n
cpm_map[%d].cpm_paddr (%llu) + cpm_size (%u) is not in the checkpoint data area\n
nx_superblock magic number invalid: 0x%X\n
failed to cross check purgeable inode: %d (%s)\n
drec count overflow (%d)\n
IOMedia
%s (id %llu): attribution tag xf exists, despite internal_flags (0x%llx)\n
INO_EXT_TYPE_RDEV
apfs superblock at index %u: apfs_fs_flags (0x%llx) previously sealed bit inconsistent with apfs_incompatible_features (0x%llx) / apfs_integrity_meta_oid (%llu) / apfs_fext_tree_oid (%llu)\n
%s (id %llu): Length %llu of file extent not a multiple of the block size (%u)\n
need to insert missing clone mapping (private_id %llu, file_id %llu)\n
Remove orphan/invalid %s objects? 
file info: attribution tag (hash %llu): physical size does not match expected value (%llu)\n
       -n            verify only (answer \"no\" to questions)\n
error writing object: %s\n
The volume %s with UUID %s was found to be corrupt and cannot be repaired.
mount_apfs
blockcopy: unable to read paddr 0x%llx block_count 0x%llx: %s\n
object (oid 0x%llx): Unable to mark nx checkpoint desc range (0x%llx + %u) allocated for space verification\n
device %s failed to open with error: %s\n
   
data_hash: object (oid 0x%llx): Missing hash at offset %llu (found %llu)\n
%s (id %llu): xf %u/%u: %s: invalid doc_id index\n
%s (id %llu): failed to register attribution tag: %d\n
%s (id %llu): invalid full clone size (%llu) for hash (%llu)\n
 [reconstructed]
iOS encryption rolling state object: current_xattr is unterminated\n
Volume %s is incompletely restored, skipping the fsroot tree.\n
apfs superblock at index %u: apfs_pfkur_tree_oid is invalid.\n
%s (id %llu): file extent record present on sealed volume\n
unable to init fsroot tree to enque purgeable repairs\n
cmp_map[%d].cpm_subtype object type (0x%x) is invalid!\n
CLONE_MAPPING_EXT_TYPE_ATTR_TAG
Invalid object type/subtype (type : %u) (subtype : %u)\n
--------
container has been mounted by APFS version %s, which is newer than %s\n
Clear volume inconsistent bit? 
failed to search for clone mapping (private_id %llu,  file_id %llu): %s (%d)\n
Delete snap_meta entries? 
%s (id %llu): invalid xdata_len (%u), given flags (0x%x)\n
mismatch between extentref entry reference count (%d) and calculated fsroot entry reference count (%d) for extent (%llu + %llu)\n
checksum block size is invalid, checksum_block_size enum: %llu\n
apfs superblock at index %u: APFS_FEATURE_EXTENDED_VEK_CLASSES set on non-HCP volume (apfs_features: 0x%llx)\n
apfs superblock at index %u: apfs_fs_flags (0x%llx) PFK bit inconsistent with apfs_incompatible_features (0x%llx) PFK bit\n
error (%d) getting cib %d bitmap %d @ %lld\n
an origin and 
Could not iterate snap meta tree to read reaper objects (oid 0x%llx): %s\n
failed to finish pending reads from the bitmap iterator: %d (%s)
-----------
%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on file without INODE_WANTS_TO_BE_PURGEABLE flag\n
checkpoint<->%s mismatch on nx_xp_data_base: %lld %lld\n
encryption rolling
%s (id %llu): invalid internal_flags (0x%llx) given unassigned default_crypto_id\n
root_device
spaceman datazone invalid previous boundary index (%hu)\n
%s (id %llu): Found data hash on unsealed volume\n
Fix object (oid 0x%llx) checksum? 
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in ip free queue tree does not lie in the internal pool\n
%s (%llu+%llu): entry %u has invalid blob\n
Checking volume %s.
INO_EXT_TYPE_SPARSE_BYTES
apfs_num_other_fsobjects is not valid (expected %llu, actual %llu)\n
Conflicting options: [ -s ] option cannot be run with the [ -q ] option\n
%s:%d: CCCryptorCreateWithMode failed (E%d)\n
fsckPrintGUI
%s (id %llu): xf %u/%u: %s: unknown x_type (%u)\n
\t%-32s %u\n
zero type/id
failed to initialize the omap snap tree: %s\n
dev_read(%llu, 1): %s\n
checksum_count (%u) exceeds max checksums (%u)\n
%s (id %llu): found dstream with unassigned default_crypto_id\n
The container %s appears to be OK.
cpm_map[%d].cpm_type storage type (0x%x) != OBJ_EPHEMERAL\n
overallocation detected on %s device: (0x%llx+%llu) bitmap address (0x%llx)\n
%s (id %llu): xf %u/%u: %s: invalid x_type (%u)\n
Disabling fsck cross checks of %s tree\n
need to update inode (object-id %llu) sparse bytes with (%llu)\n
failed to lookup doc-id %u error : %s\n
file info: clone size overflow for hash (%llu)\n
error iterating fsroot tree (xid %llu) for tree node repairs: %s\n
%s (id %llu): xf %u/%u: %s: found attribution tag on a volume that doesn't support them\n
verification/reading of the spaceman object failed: %s\n
Physical Interconnect Location
%s BTNODE_LEAF flags? 
Inode
%04x:  
repair_overlapped_extents: unable to insert target pext 0x%llx for fs_oid 0x%llx: %s\n
Checking the extent ref tree.
a
 descendants: %llu phys_size: %llu resource_fork_size: %llu gen_count: %llu chained_key: %llu flags: 0x%x\n
_enable_user_kek
%s (id %llu): invalid state.major_version (%u)\n
found spaceman free queue tree entry (0x%llx, xid %llu) which overlaps with existing range\n
%d%d-%d
apfs superblock at index %u: apfs_features has unrecognized features (0x%llX)\n
failed to register the file info tree in the fsck memory storage\n
%s (%llu+%llu): unknown version %u\n, skipping checks\n
(oid 0x%llx) %s: invalid o_subtype (0x%x, expected 0x%x)\n
failed to initialize the omap tree: %s\n
file info: attribution tag (hash %llu): full clone size (%llu) does not match computed size (%llu)\n
%s (id %llu): xf %u/%u: %s: invalid name (%.*s), given name_len (%u)\n
 file_id: %llu dstream_id: %llu\n
fsck_msg_type
apfs superblock at index %u: apfs_doc_id_index_flags has unrecognized flags (0x%x)\n
found file extent overlap (id %llu) at logical address %llu (expected %llu)\n
 %s tree (%llu)%s
missing upgrade-rolling entry for inode (%llu), version (%d)\n
ersb_recovery_length (%llu) exceeds recovery length limit (%llu), some checks will be disabled\n
       -T            tree node repair\n
%s: can't get BSD name of container\n
purgeable size
%s: could not iterate reaper for omap space verification\n
reap list object 0x%llx last index %u larger than max index %u\n
found invalid object (type %u, id %llu)\n
nx_fusion_wbc_oid should be invalid but isn't\n
apfs superblock at index %u: apfs_fext_tree_type is invalid: %u\n
can't allocate memory to insert a new clone mapping value\n
       -d            print extra debugging information\n
up
Fix default_crypto_id (%llu)? 
%s (id %llu): failed to register dir-stats (%llu) purgeable_size: %d\n
apfs superblock at index %u: apfs_modified_by[%d].last_xid (0x%llx) is greater than nx_next_xid (0x%llx)\n
xf: xf_used_data (%u) is larger than expected (%u)\n
usec
invalid kind (expected %u, actual %u) for extent (%llu + %llu)\n
dstream (id %llu) does not have an associated dstream id object\n
,
purgeable
checkpoint<->%s mismatch on uuid\n
nx_incompatible_features has unsupported flags: (0x%llX)\n
unable to init iterators for free queue tree repair: %s\n
nlink: %d \n
file info: attribution tag (hash %llu) skipping clone size repair because the clone mapping repairs were aborted\n
%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_node_count (overflow)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: key (%u) compare error: %d\n
repair_overlapped_extents: unable to free space for target_paddr 0x%llx block_count 0x%llx: %s\n
Checking the snapshot metadata.
%s%s%s\n
       -o            repair overallocations; please do not run an older fsck_apfs on newer systems with this option\n
       -E <path>     write warning/error information to <path>; Use \"-\" for stdout\n
%s (id %llu): invalid zero crypto_id on encrypted volume\n
purgeable rsrc size
could not sync and freeze volume: %s\n
spaceman IP bitmap range is invalid: 0x%llx+0x%x\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek and unmanaged vek device protection mismatch vek:%x, kek:%x%s\n
found orphan %s (id %llu, size %llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_key (%u), given btn_btree.bt_fixed.bt_key_size (%u)\n
dev=%s vers=%s default_ans=%s result=%d 
spaceman datazone zone id is zero but other fields are initialized\n
spaceman chunk %llu disk address out of order: 0x%llx, expected 0x%llx\n
object (oid 0x%llx): Unable to mark the omap entry of the apfs_sb at index (%u) in use for omap space verification\n
%s%llu%-*.*s %cB%s
failed to insert cached doc-id record, doc-id %u,file-id %llu : %s\n
cpm_map[%d].cpm_fs_oid (%llu) is less than minimum oid (%u)!\n
obj-id: %8lld type: ???\n
\t\t<array>\n
purgeable resource forks are maintained on dir-stats object (id %llu) but not rsrc forks\n
doc id
speculative download xattr (id %llu): invalid flags: 0x%x\n
INO_EXT_TYPE_DOCUMENT_ID
0x%llx-dead
reap list tail 0x%llx is not last reap list object, next 0x%llx\n
nx_ephemeral_info 0: invalid structures per fs (%u), should be: (%d)\n
0x%08x
failed to traverse doc-id tree : %s\n
dir-stats object (id %llu) is purgeable, but it doesn't track purgeable size\n
aborting purgeable cross checks - out of memory\n
failed to remove %s object: %s\n
Checking the clone group tree.
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode kek%s\n
Invalid disk file-descriptor passed\n
%s (id %llu): invalid nlink (%d)\n
%s (id %llu): xf %u/%u: %s: invalid name (%s)\n
%s (id %llu): found attribution tag on a volume that doesn't support them\n
inode (id %llu): unknown compression type: %u\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_val (%u), given btn_btree.bt_fixed.bt_val_size (%u)\n
failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) flags: 0x%x repair: %s\n
fd_dev_read_helper
cpm_count (%u) is larger than the max that this block size can accommodate (%u)\n
* * * cannot allocate memory * * *\n
 *****
spaceman sm_ip_bm_free_tail %u does not point to the last index on the free list %u\n
crypto
%s (id %llu): xf %u/%u: %s: found unexpected dstream associated with non-regular file\n
ERROR
Too many warnings of this type generated; suppressing subsequent ones.\n
\t\t<key>%s</key> <integer>%s</integer>\n
%s (id %llu): unknown kind (%u)\n
%s (id %llu): invalid internal_flags (0x%llx), (dir-stats origin but not dir-stats maintained)\n
%s (id %llu): xf %u/%u: %s: SAF dir-stats key found on non origin ino (%llu)\n
%s (id %llu): number of sparse bytes (%llu) is larger than alloced_size (%llu)\n
%s (id %llu): extent crypto flag set on unencrypted volume\n
cpm
spaceman chunks per cib %u is inconsistent with block size %u\n
apfs superblock at index %u: unknown clone group tree flags: 0x%x\n
failed to allocate memory to find dir-stats %llu\n
%s: %s%s
Checking the snapshot metadata tree.
Device does not contain a valid APFS container.\n
pfkur_tree_key : object (oid 0x%llx): pfkur tree record present on non-pfkur volume\n
%ld\n
%s (id %llu): invalid flag: (0x%02x)\n
failed to initialize the clone-group tree: %s\n
Conflicting options: [ -o ] option cannot be run with the [ -n | -q ] options\n
com.apple.ResourceFork
(oid 0x%llx) %s: should not be encrypted (ov_flags 0x%x)\n
inode (id %llu): found unexpected security xattr\n
BSD Major
blockcopy: unable to write paddr 0x%llx block_count 0x%llx: %s\n
failed to look up checkpoint block address: %s\n
DIR_STATS_EXT_TYPE_PURGEABLE_RSRC_SIZE
failed to add doc-id tree repair record, doc-id %u : %s\n
%s (id %llu): invalid bsd_flags (0x%x)\n
SAF descendants
Rechecking volume.
The volume name is %s
dev_init
failed to sparse VEK extents for inode (%llu): %s\n
object (oid 0x%llx): Unable to mark nx checkpoint data range (0x%llx + %u) allocated for space verification\n
error copying on-disk free queue tree into reordered tree in memory: %s\n
failed to register the crypto tree in the fsck memory storage\n
com.apple.fs.symlink
clone group tree (id %llu): invalid cookie val length (%u)\n
unable to allocate memory to repair dir-stats chained key\n
unable to init fsroot tree to enqueue dir-stats repairs\n
extent_list: 
nx_next_oid (%llu) is less than the minimum (%u)\n
refcnt (%u) of crypto state object (id %llu) is less than expected (%u)\n
descendants (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
directory record
omap entry (oid 0x%llx): invalid ov_size (%u)\n
could not freeze volume: %s\n
\tCache %s histogram:\n
apfs superblock at index %u: apfs_doc_id_fixup_cursor is set (%llu), despite apfs_doc_id_index_flags (0x%x)\n
%s (id %llu): class %u file references per-file crypto_id (%llu) but is missing INODE_PROT_CLASS_EXPLICIT\n
Round down logical address (%llu) to block size? 
inode (id %llu): security xattr internal flag is unexpectedly set\n
error ending transaction: %s\n
%02x
error (%s) failed to get cib for chunk index %llu \n
pl=%d:%d 
unable to iterate tree for tree node repairs: %s\n
failed to remove inode (oid 0x%llx) xfield (type %u): %s\n
blockcopy: unable to allocate memory for buffer_size 0x%zx.\n
option -X is specified but FSKit is not present, ignoring\n
error (%d) looking up spaceman IP bitmap block %u\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid btn_flags (0x%x)\n
 private_id: %llu, file_id: %llu\n
Fix apfs_fs_alloc_count(oid 0x%llx, xid 0x%llx)? 
com.apple.FSKit
inode with file-id %llu has doc-id %u but doc-id tree record has file-id %llu\n
sealed volume fsroot corruptions cannot be repaired and will automatically be skipped\n
Clear unexpected flags? 
apfs superblock at index %u: apfs_fs_quota_block_count (%llu) should not be greater than nx_block_count (%llu) for an FS with quota\n
physical size
invalid extent (%llu + %llu) with reference count (0)\n
reap list object (oid 0x%llx) expected %u entries, found %u\n
equal to
recovery extent #%llu: invalid fext_pbn (0x%llx)\n
apfs superblock at index %u: apfs_fs_alloc_count (%llu) is greater than container wide allocated count (%llu)\n
failed to allocate memory for repair\n
%s (id %llu): invalid key length (%u)\n
SUCCESS
spaceman block size %u doesn't match NX superblock block size %u\n
sm_fs_reserve_alloc_count is not valid (expected %llu, actual %llu)\n
found orphan/invalid xattr (id %llu, name %.*s)\n
File/folder %s may be damaged.
nx_xp_data_len (%u) is larger than nx_xp_data_blocks (%u)\n
SnapMetadata
%s (%llu+%llu): failed to put keybag: %s\n
NX jumpstart record range is invalid: 0x%llx+%llu\n
Enabling idle sleep, %s\n
spaceman ip bitmap block address is invalid: %hu > %u\n
clone group tree: invalid key length (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_key_free_list offset %u\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u), given total value length (%u) (%d %d %d = %d)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x)\n
spaceman sm_ip_bm_free_head %u and sm_ip_bm_free_tail %u do not point to a valid list\n
apfs superblock at index %u: apfs_incompatible_features has unsupported flags: (0x%llX)\n
spaceman cab count %u is inconsistent with cib count %u and cibs per cab %u\n
spaceman ip bitmap %u at index %u was on the free list\n
%s (id %llu): Logical address %llu of data hash not a multiple of the hash chunk size (%u)\n
(oid 0x%llx) %s: _omap_lookup_obj(0x%llx, 0x%llx): %s\n
%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n
CLONE_MAPPING_EXT_DIR_STATS_KEY
Space Verification failed.
can't remove orphan clone mapping (private_id %llu, file_id %llu): %s (%d)\n
decrypt
om
compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n
file (id %llu) isn't purgeable but its matching clonegroup record flags (0x%x) suggest it is\n
NX evict mapping tree is invalid.
failed to initialize tree for container repairs\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null VEK, file radar%s\n
unknown
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u)\n
fsckPrintString
Remove entry with invalid range? 
%s (%llu+%llu): failed to get keybag data: %s\n
Spaceman free queue tree of type [%d] is invalid\n
IP
spaceman cib %u address 0x%llx is not in the internal pool\n
apfs superblock at index %u: apfs_doc_id_index_xid (%llu) is greater than or equal to container nx_next_xid (%llu)\n
gbitmap
greater than
clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n
%s%llu %cB%s
       -F            force checking of encrypted volumes\n
Set missing flag? 
%s (id %llu): purgeable resource fork size (%llu) is larger than resource fork size (%llu)\n
nx_newest_mounted_version should not start with a 0: %s\n
fv_create_pdk
%s (id %llu): expected physical block number for extent at offset %lld\n
ersb_recovery_extents_count == 0, but ersb_recovery_list_oid is non-zero (0x%llx)\n
Could not initialize APFS-specific messages\n
failed
option -f is not implemented, ignoring\n
%s (id %llu): invalid parent_id (%llu) for root directory\n
com.apple.fs.altlink
%s (id %llu): file_id (%llu) and name (%.*s) mismatch for private directory\n
Update the parent's minkey? 
INO_EXT_TYPE_CONFORMANCE_NLINK
unable to load dir-stats %llu to retrieve attributes: %s\n
purgeable record (atime %llu, file_id %llu) is different than inode atime (%llu)\n
reaper list entry (index (%u) list oid (0x%llx)) : invalid nrle_fs_oid (0x%llx)\n
ersb_flags (0x%llx) has ERSB_FLAG_PAUSED on but ersb_recovery_extents_count is non-zero (%llu)\n
Checking the EFI jumpstart record.
clonegroup (group id %llu, private_id %llu, file id %llu): can't register for cross checks: %d (%s)\n
reaper list entry (index (%u) list oid (0x%llx)) : is not valid as per flags(0x%x)\n
nx_uuid is NULL\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_level (expected %u, actual %u)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys disable%s\n
found dir-stats object (id %llu) that is both shadow and calculating\n
Removable
extended attribute
repair_overlapped_extents: unable to load pext 0x%llx for fs_oid 0x%llx: %s\n
 revision: %u key len: %u
apfs object (oid 0x%llx): cpflags (%u) should be 0\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n
unable to init snap_meta tree for extentref_tree_oid lookup: %s\n
Fix object (oid 0x%llx) subtype? 
encryption rolling recovery block with data size 0, oid 0x%llx, nx_block_size %u, recovery length %llu\n
failed to allocate dir-stack memory for lookup in directory\n
uncompressed-size: 0x%llx \n
Object map is invalid.
\t\t\t<dict><key>%s</key> <string>%s</string></dict>\n
object (oid 0x%llx): Unable to mark the omap entry of the apfs_snap_meta_ext_oid in use for omap space verification\n
%s (id %llu): xf %u/%u: %s: invalid shadow_key (%llu)\n
nx_newest_mounted_version is less than expected: %s\n
checkpoint<->%s mismatch on nx_xp_data_blocks: %d %d\n
Fix apfs_formatted_by.id(oid 0x%llx, xid 0x%llx)? 
apfs superblock at index %u: apfs_formatted_by.last_xid (0x%llx) is greater than nx_next_xid (0x%llx)\n
unable to iterate fsroot tree (xid %llu) for tree node repairs: %s\n
Clear uncompressed size/rdev/dir_nlink? 
failed to look up dir-stats object (id %llu): %s\n
inode (id %llu): finder info internal flag is unexpectedly set\n
Restarting tree validation in case more minkey errors exist...\n
Round %s ov_size (oid 0x%llx) to block size? 
failed to find node at segment (%llu) : error %s\n
Remove entry with invalid keybag? 
error aborting transaction: %s\n
The volume %s with UUID %s could not be verified completely.
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key order: minkey is %s index 0 (should be equal)\n
ersb_recovery_extents_count is non-zero (%llu), but ersb_recovery_list_oid == 0\n
%s (%llu+%llu): entry %u has invalid padding\n
Space Verification: failed to insert paddr (%llu) error : %s\n
purgeable resource fork size xfield is missing from dir-stats object (id %llu)\n
Fix the number of keys? 
QUICKCHECK ONLY; FILESYSTEM CLEAN
file data
apfs_sb: object (oid 0x%llx): apfs_snap_meta_ext_oid invalid\n
om: om_snap_count (%u) is not equal to the number of snapshots found (%llu)\n
non-multikey volume
file info: attribution tag (hash %llu) with invalid jobj_id (%llu)\n
SiblingLink
%s (id %llu): directory nlink value %d is greater than nchildren (%d)\n
%s (id %llu): invalid internal_flags (0x%llx), given type (0%o)\n
%s (id %llu): invalid gen_count (%llu)\n
The volume %s with UUID %s was found to be corrupt and needs to be repaired.
kek group
Could not initialize snap meta tree (oid 0x%llx): %s\n
inode (id %llu): dataless bsd_flag is set, but the compression type is different: 0x%x\n
cpm_map[%d].cpm_type object type (0x%x) is invalid!\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btree node is %s\n
_INO_EXT_TYPE_VOLNAME
Conflicting options: [ -T ] option cannot be run with the [ -n | -q ] options\n
error (%d) getting spaceman IP bitmap block %u @ %lld\n
refcnt %d\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : key out of order (last paddr 0x%llx, last xid 0x%llx)\n
apfs
file extent
Volume %s has revert_to_xid set, skipping the fsroot tree.\n
reap list object 0x%llx free index %u larger than max index %u\n
com.apple.fs.graft-jobj-id-base
need to increment crypto state object (id %llu) refcount (%u)\n
Missing required option: [ -l ] option requires the [ -n ] or [ -q ] option\n
speculative download xattr (id %llu): pristine time (%llu) is greater than current time (%llu)\n
nx_xp_data_index (%u) is is larger than nx_xp_data_blocks (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list length (%u), given total value length (%u)\n
Fix spaceman free queue tree sfq_count (oid 0x%llx)? 
apfs superblock at index %u: apfs_snap_meta_tree_type is invalid: 0x%x\n
found xattr (id %llu, name %.*s) with missing crypto state\n
volume omap (fs_oid 0x%llx)
failed to validate %s object, retrying as %s\n
%s (id %llu): xf %u/%u: %s: failed to register dstream for crypto state tracking: %d\n
Truncate size to alloced size? 
%s (id %llu): invalid xattr_obj_id (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_longest_key (expected %u, actual %u)\n
set missing flag? (0x%x) 
no snap_meta entry found for snap_name entry with name %.*s\n
spaceman cab %u address 0x%llx is not in the internal pool\n
Fix overlapped extents? 
invalid zero-length extent (id %llu) at logical address %llu\n
Could not read nx_reaper_list object (oid (0x%llx)): %s\n
cib
file_id %llu (group_id %llu, private_id %llu) has different clonegroup group_id (%llu)\n
Corrupt
%s (id %llu): invalid type (0%o)\n
xf: xf_num_exts (%u) extended fields do not fit in the given xf_used_data (%u)\n
%s (id %llu): xf %u/%u: %s: found zero rdev on char/block device (mode %u)\n
failed to repair inode sparse bytes (id %llu): %s\n
no file key rolling entry found for inode object (%llu)\n
File/folder %s could not be repaired.
spaceman datazone previous boundaries (%llu -> %llu) is not a valid address range on disk\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys enable%s\n
%s (id %llu): invalid parent_id (%llu)\n
%s (id %llu): invalid state.minor_version (%u)\n
Fragmented metadata trees are invalid.
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n
failed to cross check purgeable record: %d (%s)\n
failed to insert snap_name entry: %s\n
Fix btree: bt_key_count (%llu)? 
key size (%u)/val size (%u) is invalid\n
Verifying volume object map space.
y
(oid 0x%llx) %s: invalid ov_flags (0x%x)\n
DREC_EXT_TYPE_DIR_GEN_COUNT
spaceman IP blocks field is %llu, but sum of ranges is %llu\n
Restarting after deferred repairs...\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s institutional recovery key%s\n
clone mapping (private_id %llu, file_id %llu): failed to update attribution tag %llu: %s (%d)\n
refcnt (%u) of crypto state object (id %llu) is greater than expected (%u)\n
Repairing volume.
found an orphan clone mapping (private_id %llu, file_id %llu)\n
cib: ci_free_count (%u) is not valid (%llu) (ci_addr 0x%llx)\n
pad1: 0x%x \n
Disabling idle sleep, %s\n
xf: xf total size (%u) is larger than UINT16_MAX\n
OTI keybag
clone group mapping record missing for (group_id %llu, private_id %llu, file_id %llu)\n
Volume object map space verification failed.
\t</dict>\n
file info: inode (jobj_id 0x%llx) has unexpected attribution tag with hash (%llu)\n
inode (jobj_id %llu): unable to add repair for unexpected xfield: %s\n
%s (id %llu): ID larger than MAX_JOBJ_ID (%llu)\n
Unable to perform deferred repairs without full space verification\n
%s (id %llu): invalid xfields\n
%s (id %llu): invalid length (%u), given xdata_len (%u)\n
(oid 0x%llx) %s: found a bit flip at index 0x%x\n
directory valence check: directory (oid 0x%llx): nchildren (%d) does not match drec count (%d)\n
cpm_map[%d].cpm_oid object type is invalid!\n
%s (%llu+%llu): UUID of entry %u is null\n
%s/apfs_data
found multiple clonegroup records for file_id %llu\n
Could not initialize message output\n
       -y            always repair (answer \"yes\" to questions)\n
       -c            enable cache statistics\n
failed to insert purgeable (file_id %llu): %s (%d)\n
PURGEABLE_EXT_TYPE_START_TIME
apfs superblock at index %u: apfs_revert_to_xid (%llu) should be less than nx_next_xid (%llu)\n
Set bsd_flags to 0x%x? 
NX checkpoint desc range is invalid: 0x%llx+0x%x\n
YES\n
apfs superblock at index %u: apfs_pfkur_tree_type is invalid: 0x%x\n
Fix om_most_recent_snap (oid 0x%llx)? 
Fix object (oid 0x%llx) header bit flip? 
inode
error (%d) looking up spaceman IP block address at index %llu\n
Delete omap_snap entries? 
could not cache physical extent repair at %llu error: %s\n
NX checkpoint data blocks field is %u, but sum of ranges is %llu\n
error updating omap_snap entry: %s\n
snap_meta_ext: (0x%llx:0x%llx): invalid xid (0x%llx)\n
%s (id %llu): xf %u/%u: %s: invalid SAF dir_stats_key (%llu)\n
unlock
%s:%d: can't get block count (%s)\n
evict mapping range is invalid: (0x%llx+%llu --> 0x%llx+%llu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s personal recovery key%s\n
error (%d) writing cib %u @ %lld\n
clone group tree: mapping group_id (%llu) is invalid\n
clone mapping (private_id %llu, file_id %llu): invalid file_id\n
failed to initialize the spaceman free queue tree %d: %s\n
%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n
object (oid 0x%llx): o_oid invalid\n
Fix ci_free_count (%u)? 
spaceman chunk %llu bitmap address 0x%llx is not in the internal pool\n
Volume superblock is invalid.
integrity_meta: (0x%llx:0x%llx): invalid version\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unknown blob type %i%s\n
_unlock_result
speculative download xattr (id %llu): shouldn't be stream based\n
Encryption Rolling data structures are invalid.
integrity_meta: failed to copy object (0x%llx:0x%llx)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s icloud recovery key%s\n
purgeable resource forks are maintained on dir-stats object (id %llu) but not purgeable data forks\n
Limited repair mode, not all repairs available
xattr value length (%u) does not match record size (%u)\n
Checking the checkpoint with transaction ID %ld.
%s (id %llu): invalid parent_id (%llu) for private directory\n
Fix object (oid 0x%llx) omap flags? 
orphan/invalid physical extent (%llu) at snapshot %llu\n
CLONEGROUP_EXT_TYPE_DIR_STATS_KEY
       -g            print output in form suitable for automatic parsing\n
no valid checkpoint\n
repair_overlapped_extents: allocate space for block_count 0x%llx\n
%-20s%-15s\n
fsck_apfs completed at %s
subdir count overflow (%d)\n
iOS encryption rolling state object: cannot get ierso xattr\n
Fix the keybag size? 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_flags (0x%x), given mt_btflags\n
error iterating omap tree for repair: %s\n
object (oid 0x%llx): o_cksum (0x%llx) is invalid for object\n
fsck_apfs completed at %s\n
3288.52.1
file info: found more than one attribution tag with matching computed hash, invalid entry (hash %llu)\n
%s (id %llu): invalid snap_xid (%llu)\n
%s (id %llu): invalid state.key_revision (%u)\n
found dir-stats object (id %llu; flags 0x%x) with bad chained key (%llu/%llu)\n
unable to flush deferred repairs: %s\n
repair_overlapped_extents: encryption is rolling for fs_oid 0x%llx\n
unexpected: space verification data structure not initialized
%s (id %llu): failed to register file info (hash %llu): %d\n
 name: '%.*s' name_len: %u snap_xid: %lld\n
apfs superblock at index %u: apfs_root_tree_oid is invalid.\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n
encrypt
reaper completed ID 0x%llx not less than next reap ID 0x%llx\n
unable to load drec (oid 0x%llx) for file lookup in directory\n: %s\n
container %s is mounted with write access; please re-run with -l.\n
fp=%d fl=%d repairs=%d time=%ld iter=%d\n
failed to read spaceman cab %u at address 0x%llx\n
Can't read/write encrypted data to/from block 0!
%s (id %llu): invalid atime (0)\n
%s (%llu+%llu): %s records entry %u does not contain a range (size %u)\n
iOS encryption rolling state object: epoch unordered: current_id (%llu) <= epoch (%llu) < apfs_next_obj_id (%llu) <= MAX_JOBJ_ID (%llu)\n
. . .\n
 extentref_Tree_type: %u flags: %u name: '%.*s' name_len: %u\n
doc-id tree: record exists for doc-id %u, file-id %llu but no inode references this doc-id\n
%s (%llu+%llu): UUID %s of entry %u (tag %u) does not reference any volume\n
origin_id of dir-stats object (id %llu) does not match expected value (%llu)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n
%s (id %llu): owning_obj_id is '%s'\n
speculative download xattr (id %llu): unknown flags: %x\n
nx_xp_desc_len (%u) is less than 2\n
apfs superblock at index %u: apfs_doc_id_tree_type is invalid: %u\n
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/platform/platform.c
_cmd_handle_vek
Mark volume for doc-id tree building on next mount? 
%s (%llu+%llu): entry %u with size %u brings total size %u beyond object size %u\n
fsck_apfs is out of memory - some cross checks are skipped\n
Encryption key structures are invalid.
The volume %s with UUID %s was repaired successfully.
%s (id %llu): invalid dstream\n
speculative download xattr (id %llu): unknown purge reason: %u\n
verification/reading of the nx_reaper object failed: %s\n
clonegroup-cookie
invalid btree node address range (0x%llx+%llu)\n
Spaceman internal pool fragmented metadata tree is invalid\n
%s: error %d from IORegistryEntryGetLocationInPlane\n
refcnt (%u) of dstream id object (id %llu) is less than expected (%u)\n
apfs_snap_meta: 
Checking the container superblock.
unable to allocate memory to repair missing crypto state\n
Set ov_size (oid 0x%llx) to the block size? 
SnapName
Decryption
snap_meta_ext: (0x%llx:0x%llx): sme_uuid is NULL\n
INO_EXT_TYPE_FS_UUID
encountered more than %u omap objects in reap list; skipping subsequent ones\n
%s/Library/Logs/fsck_apfs.log
snap_meta_ext: object (oid 0x%llx): no record for snapshot (xid 0x%llx)\n
ersb_version is %d, unsupported\n
dstream id
%s (id %llu): xf %u/%u: %s: inode is expected to be an SAF dir-stats origin\n
flags of dir-stats object (id %llu) does not match expected value (0x%x)\n
Clear uncompressed size? 
%s (id %llu): xf %u/%u: %s: invalid attribution hash (%llu)\n
clone size xfield is missing from dir-stats object (id %llu)\n
%s xfield of inode object (id %llu) does not match expected value (%llu)\n
%s (id %llu): invalid private_id (%llu)\n
Set INODE_PROT_CLASS_EXPLICIT? 
INO_EXT_TYPE_SPEC_TELEM_FLAGS
DirSize
invalid range: 0x%llx+%llu\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s %s unlock %s (%d)%s\n
speculative download xattr (id %llu): size is too small, actual: %u, minimum: %lu\n
checkpoint<->%s mismatch on nx_xp_desc_base: %lld %lld\n
\nTotal blocks marked by fsck: %llu\n
%02x 
nx_xp_desc_blocks (%u) is less than 8\n
nx_reaper_oid (%llu) is less than minimum OID (%d)\n
underallocation detected in internal pool: (0x%llx+%llu) bitmap address (0x%llx)\n
NO\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh, Unexpected short PDK len%s\n
omap entry (oid 0x%llx): invalid crypto key index (%u) on %s\n
found invalid fsroot btree node key id (%llu)\n
xattr record too small (%u)\n
aks
volume-index
compression xattr (id %llu): internal flags are invalid (0x%x)\n
er_state magic number is %d, should be %d\n
apfs superblock at index %u: apfs_sec_root_tree_type is invalid\n
omap snapshot: oms_oid should be unused but has value (0x%llx)\n
found file extent overlap (id %llu) with next extent / end of dstream at logical address %llu+%llu\n
more than %d inodes tracked as rolling, disabling pfkur tracking repairs\n
failed to remove %s object (id %llu): %s\n
nx_fusion_wbc should be empty but isn't\n
could not retrieve erb, oid 0x%llx\n
spaceman ip bitmap %u at index %u was referenced by a previous entry in sm_ip_bitmap \n
apfs_fs_alloc_count is not valid (expected %llu, actual %llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_flags (0x%x), given btn_level (%u)\n
Fix %s (0x%llx+%llu) bitmap address (0x%llx)? 
unable to lookup latest snap xid: %s\n
fsckPrintXML
found orphan crypto state object (id %llu, refcnt %u)\n
%llu 
encrypted
IOBlockStorageDevice
repair_overlapped_extents: copy paddr 0x%llx to paddr 0x%llx, block_count 0x%llx\n
%s (%llu+%llu): entry %u has size %u > maximum size %u\n
object (oid 0x%llx): o_xid invalid, o_xid is 0\n
recovery extent #%llu: invalid ersb_flags (0x%llx), ERSB_FLAG_CID_IS_TWEAK is set but fext_cid == 0\n
spaceman cib %u wrong number of chunks: %u, expected %u\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u, expected %u\n
could not remove extent at %llu for physical extent repair: %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_nkeys (%u), given btn_table_space.len (%u) and toc_entry_size (%u)\n
refcnt %d len %lld owning_obj_id %lld\n
spaceman datazone unknown zone id (%hu)\n
AppleAPFSVolume
failed to init fsroot tree to repair dir-stats chained key\n
(oid 0x%llx) %s: object is %s but omap says it's %s\n
repair_overlapped_extents: unable to remove source pext 0x%llx for fs_oid 0x%llx (pext leak): %s\n
apfs superblock at index %u: apfs_magic invalid: %d\n
apfs_num_symlinks is not valid (expected %llu, actual %llu)\n
%s (id %llu): xf %u/%u: %s: directory nlink value is invalid (%llu)\n
%s (id %llu): owning_obj_id is 0\n
Truncate alloced_size to block size? 
clonegroup (group id %llu, private_id %llu, file id %llu): invalid xfields\n
error iterating fsroot tree for file lookup in directory: %s\n
detected chained-key loop involving dir-stats %llu\n
EFI jumpstart record is invalid.
found orphan dstream id object (id %llu, refcnt %u)\n
%s (id %llu): invalid type (%u)\n
greater
Internal
       -X            report progress to FSKit\n
%s (id %llu): invalid state.cpflags (%u)\n
Checking the fragmented metadata trees.
.DocumentRevisions-V100
%s (id %llu): unknown flags: (0x%x / known flags are: 0x%x)\n
error allocating encryption rolling recovery data buffer, ersb_recovery_length %llu\n
\t\t<key>%s</key> <integer>%u</integer>\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode vek%s\n
error (%d) writing cib during deallocation\n
failed to allocate memory for snapshot validation\n
failed to write apfs superblock : %s\n
omap (oid 0x%llx): invalid om_most_recent_snap (0x%llx), given om_flags (0x%x)\n
clone group tree: cookie group_id (%llu) or cookie_group_id (%llu) is invalid\n
failed to register the prev phys extent tree in the fsck memory storage\n
%s (%llu+%llu): entry %u has size %u > remaining size %u (keybag size %u)\n
insert missing directory record object (parent_id %llu, file_id %llu)\n
unable to get dir-stats key of inode (id %llu) to repair dir-stats chained key: %s\n
Trimming unused blocks.
Container superblock is invalid.
clone group tree: invalid cookie key length (%u)\n
found shadow dir-stats object (id %llu) with origin (id %llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_free_space (%u, %u)\n
can't add dir stats key for clonegroup: %s (%d)\n
ersb_recovery_extents_count == 0, but ersb_recovery_length is non-zero (%llu)\n
error %d from cond wait\n
unable to initialize iterator for snapshot validation: %s\n
ersb_total_blk_to_encrypt (%llu) exceeds device block count (%llu)\n
INO_EXT_TYPE_FILE_DATA
sm: sm_free_count (%llu) is not valid (%llu)\n
omap (oid 0x%llx): invalid om_snapshot_tree_type (0x%x)\n
clone mapping (private_id %llu, file_id %llu): unknown flags (0x%x / known flags are: 0x%x)\n
%s (%llu+%llu): block range isn't a valid keybag, skipping checks\n
iOS encryption rolling state object: cannot determine absence of ierso xattr\n
clonegroup
.
ersb_recovery_extents_count is non-zero (%llu), but ersb_recovery_length == 0\n
%s (id %llu): xf %u/%u: %s: extended field type is no longer used\n
dir-stats object (id %llu) is purgeable, but its origin isn't\n
unexpected end of iteration while repairing free queue tree\n
Failed to allocate memory\n
failed to read object (oid (0x%llx)) being reaped from disk \n
clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect attribution tag (%llu)\n
%s (id %llu): unknown flags: (0x%02x / known flags are: 0x%02x)\n
nx_sb->nx_o.o_oid != OID_NX_SUPERBLOCK, %llu\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list offset %u\n
(void *)m->msg == (void *)fmt
failed to insert %s object: %s\n
sm : free queue tree has sfq_count (%llu) greater than available block count (%llu)\n
device_is_mounted(%s) failed with error: %s\n
error (%d) getting cib bitmap %d @ %lld\n
Failed to get keybag entry with tag %d for volume %s\n
unable to get fsroot tree to repair missing crypto state\n
error iterating fsroot tree during dstream repair: %s\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space.len (%u), given toc_entry_size (%u) and btn_flags (0x%x)\n
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) is greater than spaceman reserve block count (%llu) for a guaranteed-minimum space FS\n
Cache average %s time:
encryption rolling recovery block offset mismatch, oid 0x%llx, expected %llu, actual %llu\n
failed to init fsroot tree for file lookup in directory\n
underallocation detected on %s device: (0x%llx+%llu) bitmap address (0x%llx)\n
successful
The volume %s cannot be repaired when it is in use.
Checking the object map.
omap entry (oid 0x%llx): invalid ov_flags (0x%x)\n
purgeable resource fork size xfield of dir-stats object (id %llu) exists unexpectedly\n
missing/invalid physical extent (%llu + %llu) with refcnt %d\n
unable to load inode (oid 0x%llx) for lookup in purgatory directory: %s\n
Any
_create_kek_data
unable to enqueue tree node prune repairs: %s\n
%s (id %llu): invalid length (%u), given state.key_len (%u)\n
%s (id %llu): extent crypto flag set on sparse extent\n
 out-of-line data size: %lld (under obj-id: %lld / crypto-id: %lld)\n
apfs superblock at index %u: apfs_fs_flags has conflicting encryption flags 0x%llx\n
Encryption
%s (id %llu): invalid name (%.*s)\n
object (oid 0x%llx): o_type invalid, o_type 0x%x should be 0x%x\n
Checking the NX evict mapping tree.
Fix apfs_num_symlinks(oid 0x%llx, xid 0x%llx)? 
failed to initialize the prev doc-id tree: %s\n
failed to look up resource fork for inode (%llu): %s\n
unable to remove tree node at key id %llu for repairs : %s\n
object (oid (0%llx)) being reaped : Invalid tree subtype (%u)\n
pfkur_key : object (oid 0x%llx): invalid oid (0x%llx)\n
cloned dstream (id %llu, object-ids %s) is being truncated\n
Unset unknown flags? (0x%llx) 
er_state
nx_ephemeral_info 0: invalid minimum block count per structure (%u), should be less than: (%d)\n
apfs superblock at index %u: apfs_fs_flags (0x%llx) indicates sealed volume is not fully unencrypted\n
Could not iterate omap tree to read reaper objects (oid 0x%llx): %s\n
UNKNOWN-DEV
object (oid 0x%llx): Unable to mark omap entry for omap space verification \n
omap snapshot: invalid key (0x%llx)\n
Unknown type %d
Skipped
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: missing btn_flags (expected 0x%x, actual 0x%x)\n
       -M            skip checks which require encrypted volumes to be unlocked\n
Clear invalid flag? 
can't repair inode (id %llu) with dir stats (id %llu)\n
unable to initialize omap tree iterator for repair: %s\n
Main
%s
Checking snapshot %ld of %ld (%s, transaction ID %ld)
%s (id %llu): invalid dir_nlink (%d)\n
Remove entry with invalid blob range? 
Could not open error file: %s\n
reached invalid tree node limit %llu for fs_oid %llu\n
compression xattr (id %llu): compression magic is unknown: 0x%x\n
inode (id %llu): need to clear internal_flags 0x%llx\n
 chained-key: %lld\n
found dstream (id %llu) with missing crypto state object (id %llu)\n
unable to init fsroot tree iterator for dstream repair: %s\n
reaper list entry (index (%u) list oid (0x%llx)) : entry is not referenced\n
nx_newest_mounted_version is greater than expected: %s\n
checkpoint<->%s mismatch on nx_block_count: %lld %lld\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid value (%u, %u)\n
Verifying allocated space.
omap (oid 0x%llx): invalid om_flags (0x%x)\n
reap list object 0x%llx first index %u larger than max index %u\n
path
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) is greater than the container block count (%llu)\n
unexpected on-disk range 0x%llx+%llu xid %llu and in-memory range 0x%llx+%llu xid %llu while repairing free queue tree\n
succeeded.
AKS_FV_service
tmp-ino-clone-
reaper needs more cowbell, flags 0x%x\n
apfs superblock at index %u: apfs_modified_by[%d].timestamp (%llu) is greater than current time (%llu)\n
spaceman ip block count is bad: %lld\n
Applied
NX checkpoint desc blocks field is %u, but sum of ranges is %llu\n
container %s is mounted with write access.\n
apfs superblock at index %u: apfs_fs_reserve_block_count (%llu) must not be greater than apfs_fs_quota_block_count (%llu)\n
clone mapping (private_id %llu, file_id %llu): invalid xfields\n
Checking the file key rolling tree.
(void *)fmt == (void *)m->msg
last reap list object 0x%llx doesn't match tail 0x%llx\n
Purgeable
apfs superblock at index %u: apfs_fext_tree_oid is invalid.\n
purgatory.
NX media keylocker data range is invalid: 0x%llx+%llu\n
found fext (id %llu) with missing crypto state object (id %llu)\n
%s (%llu+%llu): number of keys %u does not match number of entries found %u\n
Missing required option: [ -S ] option requires the [ -n ] option\n
%s (id %llu): xf %u/%u: %s: found nlink field even though inode is not a directory\n
bitmap store: reached limit of %llu B-tree nodes\n
%s (id %llu): invalid name_len (%u)\n
%s (id %llu): invalid crypto_id (%llu)\n
%s BTNODE_ROOT flag? 
sib-id: %lld parent-id: %lld name: %.*s\n
Snapshot (0x%llx): apfs_integrity_meta_oid is invalid\n
bm_bit_count %llu is not an integer multiple of container block count %llu\n
\nfsck_apfs started at %s
%s (id %llu): unknown internal_flags (0x%llx / known flags are: 0x%llx)\n
%s (id %llu): Unknown type (0x%x)\n
failed to get fsroot tree for jobj type %d: %s\n
failed to allocate memory to mark dir-stats chain as inconsistent\n
omap mapping
repair_overlapped_extents: unable to allocate space for block_count 0x%llx: %s\n
\nSpace allocation summary:\n\n
spaceman fs_reserve_alloc_count %llu is greater than sm_fs_reserve_block_count %llu\n
unencrypted
Fix sm_fs_reserve_alloc_count? 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n
omap entry (oid 0x%llx): invalid ok_xid (0x%llx)\n
descendants
malloc(%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nwarning: btn: invalid cpm_size or ov_size (%u), given btn_btree.bt_fixed.bt_node_size (%u)\n
object oid %llu/xid %llu/type 0x%x/subtype 0x%x: unable to mark range %llu+%llu allocated for space verification: %s\n
failed to insert doc-id tree repair for doc-id %u, file-id %llu : %s\n
%s (id %llu): invalid internal_flags (0x%llx), inconsistent protection class\n
sibling link
File extent tree is invalid.
%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n
container omap
Fix the number of bytes? 
need to make file extent with missing crypto state (id %llu) at logical address %llu+%llu sparse\n
object (oid 0x%llx): Unable to mark spaceman ip bitmap range (0x%llx + %u) allocated for space verification\n
%s (id %llu): no rdev xf on char/block device (mode %u)\n
invalid gbitmap block oid 0x%llx\n
not a leaf
private-id: %lld parent-id: %lld cr/mtime: %lld/%lld \n
%s (id %llu): invalid key on expanded-records volume\n
nx_xp_data_blocks (%u) is less than 8\n
integrity_meta: (0x%llx:0x%llx): invalid root hash\n
apfs superblock at index %u: apfs_fs_flags (0x%llx) inconsistent with apfs_incompatible_features secondary fsroot bit (0x%llx)\n
apfs superblock at index %u: apfs_formatted_by.id (%.*s) is not NULL terminated.\n
%s (id %llu): invalid flags: (0x%02x)\n
object (oid 0x%llx): Unable to mark omap entry in use for omap space verification \n
failed to initialize the secondary fsroot tree: %s\n
DIR_STATS_EXT_TYPE_CLONE_SIZE
%s (id %llu): invalid name_len (%u), given value length (%u)\n
%s (id %llu): xf %u/%u: %s: directory nlink value %lld is greater than nchildren (%d)\n
%s (id %llu): unable to remove dstream of inode %llu\n
orphan
fd_dev_write_extended
obj-id: ??? type: ???\n
%s (id %llu): invalid extentref_tree_type (0x%x)\n
unable to allocate space to walk dir-stats parent chain\n
unable to find inode (id %llu): %d (%s)\n
nx_max_file_systems (%u) is invalid\n
parameters
Fix apfs_doc_id_fixup_cursor? 
failed to look up dstream id object (id %llu): %s\n
Set internal_flags to 0x%llx? 
directory stats
failed to add doc-id repair (deletion), doc-id %u : %s\n
gbitmap: 
failed to register the doc id tree in the fsck memory storage\n
%s:%d: can't get solidstate for device (%s)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid key (%u, %u)\n
free_overlapped_range: unable to free space for source_paddr 0x%llx block_count 0x%llx (leak): %s\n
gen-count: %u nchildren: %d \n
failed to lookup extentref tree oid at snap_xid %llu : %s\n
apfs superblock at index %u: apfs_sec_root_tree_oid (%llu) set on incompatible volume\n
apfs_next_doc_id is not valid (expected %u, actual %u)\n
failed to register the clone mapping tree in the fsck memory storage\n
%s (id %llu): length is 0\n
%s (id %llu): dstream.size (%llu) is greater than dstream.alloced_size (%llu)\n
physical_size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
dev_read_finish
failed to allocate memory to read the container superblock\n
could not retrieve er_state_phys_t\n
:
failed to get inode (id %llu) dstream: %s\n
%s%s
spaceman chunk %llu xid is invalid: %llu > %llu\n
omap entry (oid 0x%llx): invalid tweak type (%u) given ov_flags (0x%x)\n
hit
the EFI jumpstart record magic number is invalid: 0x%x\n
%s (id %llu): invalid state.persistent_class (%u)\n
found orphan dir-stats object (id %llu)\n
sealed volume hash records
%s (%llu+%llu): failed to allocate memory\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_val_size (%u), given mt_val_size (%u)\n
msg != NULL
spaceman chunk %llu wrong number of blocks: %u, expected %u\n
inode with file-id %llu has doc-id %u but doc-id is already in use\n
clone mapping (private_id %llu, file_id %llu) is missing\n
failed to search purgeable record (file id %llu) in the fsck_apfs tree: %d (%s)\n
cpm_flags has an unknown flag set 0x%x\n
 type: %u\n
number of files in the clone mapping (%u) != dstream reference count (%u)\n
Fix object (oid 0x%llx) flags? 
apfs_num_snapshots is not valid (expected %llu, actual %llu)\n
)
       -s            print space verification summary\n
%s (id %llu): failed to update dstream (%llu)\n
SiblingMap
apfs superblock at index %u: incompatible features set (apfs_readonly_compatible_features: (0x%llX), apfs_incompatible_features: (0x%llX))\n
failed to register the dir stats repair tree in the fsck memory storage\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_table_space (%u, %u)\n
%s (id %llu): invalid state.key_os_version (%u)\n
%s (id %llu): xf %u/%u: %s: invalid extended field size %u for type %u, expected %lu\n
clonegroup_tree: 
(oid 0x%llx) %s: invalid o_xid (0x%llx, expected 0x%llx)\n
found unexpected %s xfield associated with inode (object-id %llu)\n
QUICKCHECK ONLY; FILESYSTEM DIRTY
INO_EXT_TYPE_SOURCE_PURGE_ID
Space Verification: failed to remove paddr (%llu) error : %s\n
failed to populate cached doc-id tree : %s\n
omap (oid 0x%llx): invalid om_pending_revert_min (0x%llx), given om_flags (0x%x)\n
inode (id %llu) has a stale dir_stats (id %llu)\n
%s (%llu+%llu): invalid padding\n
logical addr: %lld  phys-block-num: %lld  crypto-id: %lld  len: %lld  flags: %x\n
volumename
omap has %llu snaphots but snap meta tree has %llu\n
Fix internal flags (0x%llx)? 
Cache %s count:
btree node (oid (0%llx)) being reaped is hashed\n
com.apple.system.apfs.ierso
%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n
apfs superblock at index %u: apfs_readonly_compatible_features has unsupported flags: (0x%llX)\n
Failed to get password for encrypted volume from provided file descriptor: %s\n
\t\t\t<string>%s</string>\n
%p\n
spaceman ip bm range (%llu, %llu) overlaps with spaceman ip range (%llu, %llu)\n
Fix apfs_fs_index(oid 0x%llx, xid 0x%llx)? 
%s:%d: failed to open container device %s: %s\n
Checking if the parent's minkey can be updated...\n
recovery extent #%llu: fext_laddr (0x%llx) exceeds nx_block_count (%llu), fs_bsize %u\n
%s (id %llu): dstream.alloced_size (%llu) is not a multiple of the block size (%u)\n
expanded key (id %llu) on incompatible volume\n
inode (id %llu): need to set internal_flags 0x%llx\n
multiKeyEncryption
%s\n
error updating the reap list: %s\n
%s (id %llu): invalid internal_flags (0x%llx) given volume readonly compatible features (0x%llx)\n
(oid 0x%llx) %s: %s(%llu, %u): %s\n
descendants of dir-stats object (id %llu) does not match expected value (%llu)\n
verification/reading of the omap object failed: %s\n
%s (id %llu): xf %u/%u: %s: found rdev x-field but volume has rdev in core-inode\n
inode (id %llu): unable to add repair to unmark purgeable: %d (%s)\n
(oid 0x%llx) %s: found a bit flip in the header\n
fsck_msg_string
found %s file extent object (id %llu) at logical address %llu\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_nkeys (%u), given btn_flags (0x%x)\n
vek group
%s (%llu+%llu): size is too large\n
hash validation: invalid node hash for node %llu (hash type: %u, hash size: %u, root oid: %llu, seal xid: %llu, broken xid: %llu)\n
fv_decrypt_vek
inode with file-id %llu has doc-id %u but doc-id tree record is missing or points to another inode\n
iOS encryption rolling state object: xattr payload (%hu) does not match record size (%zu)\n
DREC_EXT_TYPE_SIBLING_ID
Failed to allocate memory for cab\n
%s (id %llu): xf %u/%u: %s: invalid dir_stats_key (%llu)\n
PURGEABLE_EXT_TYPE_DIR_GEN_COUNT
unexpected key (%u) / val (%u) size in extent list tree\n
spaceman sm_ip_bm_free_next index %u does not lie in ip bm range\n
omap (oid 0x%llx): invalid om_snapshot_tree_oid (0x%llx), given om_flags (0x%x)\n
%s (id %llu): invalid sblock_oid (%llu)\n
failed to insert dir-stats entry %llu into the repair tree\n
IOStorage
%s:%d: lib_get_file_vault_services failed (E%d)\n
encryption rolling recovery data extends past recovery length, oid 0x%llx, ersb_recovery_length %llu, accumulated length %llu\n
repair_overlapped_extents: update fext 0x%llx 0x%llx\n
       -b <num>      set default cache block size to <num> KiB\n
could not allocate array of %u entries for tracking omap objects in reap list; skipping subsequent ones\n
unknown obj type (%u) to add xfields\n
apfs superblock at index %u: apfs_unmount_time (%llu) is greater than current time (%llu)\n
%s:%d: %s failed (E%d)\n
hw.memsize
orphan omap mappings found for oid range %llu --> %llu\n
failed to allocate memory for bitmap store\n
inum: %8lld version: %u flags: %u current_offset: %8llu current_ns_offset: %8llu\n
integrity_meta: (0x%llx:0x%llx): unexpected flags (0x%x) for xid (%llu)\n
Remove invalid flags (0x%02x)? 
missing dir-stats object (id %llu) referenced by %s%llu files / directories\n
object (oid 0x%llx): Unable to mark omap entry in usefor omap space verification \n
xp_map->cpm_map[%d].cpm_size is 0\n
DAMAGEINFO
\tactual hash:   %s\n
apfs_clonegroup_next_id is not valid (expected %llu, actual %llu)\n
dump_bytes_internal
failed to update allocation counts: %s\n
com.apple.decmpfs
Invalid
num children: %lld total size: %lld gen-count: %lld\n
spaceman datazone duplicate zone id (%hu) for allocation zones at indices (%hu, %hu)\n
spaceman struct ranges %u+%u and %u+%u overlap\n
dir-stats descendants
inode (id %llu) needs to untrack from dir-stats\n
failed to remove INODE_PROT_CLASS_UPGRADE_ROLLIP flag for inode (%llu): %s\n
fv_decode_kek_blob_opts
Fix om_snap_count (oid 0x%llx)? 
com.apple.fs.firmlink
reaper head (0x%llx) and tail (0x%llx) should be both valid or both invalid\n
clonegroup (group id %llu, private_id %llu, file id %llu): invalid physical_size (%llu)\n
speculative download xattr (id %llu): unknown version: %u\n
recovery extent #%llu: checksums at offset %llu, length %llu exceed ersb_recovery_length %llu\n
failed to allocate memory for the extentref tree\n
(oid 0x%llx) %s: invalid o_xid (0x%llx)\n
com.apple.apfs.
failed to register the phys extent tree in the fsck memory storage\n
pfk_val : object (oid 0x%llx): unknown flags (%u)\n
failed to init fsroot tree for file lookup in purgatory directory\n
failed to look up crypto state object (id %llu): %s\n
%s (id %llu): xf %u/%u: %s: found nlink x-field but volume has dir-nlink in core-inode\n
%s (id %llu): invalid flags (0x%x)\n
Fix object (oid 0x%llx) encryption? 
invalid EFI jumpstart record number of extents: %d\n
spaceman cibs per cab %u is inconsistent with block size %u\n
Spaceman Repair: Cannot modify more than a block's worth of bitmap\n
unable to init snap_meta tree for snapshot repair\n
%s (id %llu): xf %u/%u: %s: found nlink field but volume doesn't support it\n
%s (id %llu): Invalid type (0x%x)\n
can't unmark purgeable (file_id %llu) for cross checks\n
iOS encryption rolling state object: ierso version (%u) unrecognized\n
spaceman block count %llu doesn't match NX superblock block count %llu\n
apfs superblock at index %u: apfs_total_blocks_freed (%llu) should not be greater than apfs_total_blocks_alloced (%llu)\n
need to insert key at id (%llu) to repair invalid internal node\n
clone group mapping record exists for (group_id %llu, private_id %llu, file_id %llu), but no inode refers to it\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: parent doesn't have enough space to update the minkey\n
apfs object (oid 0x%llx): crypto major version (%u) is not CP_CURRENT (%u)\n
??? (id ???): invalid key length (%u)\n
Could not initialize gbitmap tree (oid 0x%llx): %s\n
Round %s length (%llu) to block size? 
dir-stats object (id %llu) unexpectedly marked as having origin-id\n
get_pfkur_tree() called on non-pfk volume\n
INO_EXT_TYPE_FINDER_INFO
%s: fsck_apfs completed at %s\n
apfs superblock at index %u: apfs_modified_by[%d].id (%.*s) is not NULL terminated.\n
%s (id %llu): invalid dstream.default_crypto_id (%llu) on encrypted volume\n
ersb_flags (0x%llx) has ERSB_FLAG_PAUSED on but checksum count is non-zero (%u)\n
clonegroup (group id %llu, private_id %llu, file id %llu): invalid value length (%u)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_val_free_list entry (%u, %u)\n
found orphan clone group mapping: (group_id %llu, private_id %llu, file_id %llu)\n
def-prot-class: %d \n
%s (id %llu): zero rdev on char/block device (mode %u)\n
failed to insert node at segment (%llu) error : %s\n
%s (%llu+%llu): %s records entry %u contains invalid keybag\n
failed to initialize the snap meta tree: %s\n
block count
volume
option -p is not implemented, ignoring\n
Fix crypto_id (%llu)? 
nx_omap_oid is invalid\n
unable to load inode (oid 0x%llx) for file lookup in purgatory directory: %s\n
CLONEGROUP_EXT_TYPE_ATTRIBUTION_TAG
integrity_meta: (0x%llx:0x%llx): unknown flags (0x%x)\n
%s%s%llx
error (%d) looking up spaceman IP block %llu\n
oms: 
found orphan/invalid clone mapping (private_id %llu, file_id %llu)\n
The volume %s with UUID %s was found to have minor issues that can be repaired.
encryption rolling gbitmap tree is invalid\n
\n%s: fsck_apfs started at %s
Volume %s is encrypted and crypto I/O failed/was skipped, skipping the fsroot tree.\n
%s (id %llu): invalid internal_flags (0x%llx) given apfs_fs_flags (0x%llx) PFK bit\n
%s (id %llu): invalid dstream.default_crypto_id (%llu) on encrypted volume, given apfs_fs_flags (0x%llx)\n
%s (id %llu): dir-stats key xf does not exist, despite internal_flags (0x%llx)\n
DirRecord
%d$@
found unexpected crypto state object (id %llu, refcnt %u)\n
verification/reading of the nx_reaper object failed\n
ersb_snap_xid (%llu) is greater than or equal to container next xid (%llu)\n
failed to allocate dir-stack memory for lookup in directory: %s; results may be incomplete\n
file info: found orphan data hash (id %llu) at logical address %llu\n
%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n
apfs_fs_reserve_block_count brings total reserve block count beyond the container block count (max %llu, actual %llu)\n
bitmap was not entirely unset, stopping allocation\n
file info: computed size overflow for hash (%llu)\n
unable to fix overlaps in candidate tree: %s\n
miss
%s (%llu+%llu): version cannot be 0\n
unable to access the tree repairs structure: %s\n
(%c,\"%s\",%d)\n
%s: error %d from IORegistryEntryCreateCFProperties\n
failed to allocate memory for insertion of dir-stats\n
(oid 0x%llx) %s: malloc(%u)\n
Look for links to corrupt files in %s directory.
repair_overlapped_extents: unable to init fsroot for fs_oid 0x%llx\n
spaceman cab out of order: %u, expected %u\n
fv_kek_global_policy_eval
%s (id %llu): physical size (%llu) is less than full clone size (%llu) for hash (%llu)\n
SAF descendants (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
skipping dir stats clone sizes repair because the computed clone size is negative\n
Fix btree: bt_longest_val (%u)? 
number of files in clonegroup (%u) != dstream reference count (%u)\n
INO_EXT_TYPE_DELTA_TREE_OID
unable to init omap_snap tree iterator for snapshot repair: %s\n
%s (id %llu): xf %u/%u: %s: sparse_bytes set even though inode is not sparse\n
unknown keybag
spaceman struct is versioned but version is 0\n
extended attribute (id %llu, name %.*s) is orphan\n
found file extent gap (id %llu) at logical address %llu+%llu\n
repair_overlapped_extents: update source pext 0x%llx\n
repair_overlapped_extents: remove target pext 0x%llx\n
%s (id %llu): file_id (%llu) and name (%.*s) mismatch for root directory\n
tried to remove oid %llu from the omap but it wasn't there\n
Space Verification: failed to allocate memory for the bitmap block\n
Fix apfs_next_doc_id(oid 0x%llx, xid 0x%llx)? 
%03llu
error updating snap_meta entry: %s\n
Set
Snapshot metadata tree is invalid.
apfs superblock at index %u: apfs_root_tree_type is invalid: 0x%x\n
apfs superblock at index %u: apfs_last_mod_time (%llu) is greater than current time (%llu)\n
apfs superblock at index %u: apfs_fs_flags has an unknown flag set 0x%llx\n
less than
NX blocked out range is invalid: 0x%llx+%llu\n
INO_EXT_TYPE_STRICT_CLASS_F
failed to construct drec key (dir_id %llu, file_name %s)\n
\t\t\t<integer>%d</integer>\n
Spaceman free queue tree of type [%s] has sfq_oldest_xid (%llu) greater than the oldest xid in the free tree (%llu)\n
Fix apfs_volname(oid 0x%llx, xid 0x%llx)? 
_bind_unmanaged_vek
clone mapping (private_id %llu, file_id %llu): attribution tag (%llu) != inode (id %llu) attribution tag (%llu)\n
om: om_most_recent_snap (%llu) is not equal to the largest snapshot xid (%llu)\n
%s (id %llu): invalid default_protection_class (%u)\n
%s (id %llu): Unexpected hash size (%u != %u)\n
(oid 0x%llx) %s: _xp_lookup_obj(0x%llx): %s\n
inode (id %llu): finder info internal flag is missing\n
checkpoint %d (xid %llu) checkpoint map is invalid\n
unexpected key (%u) / val (%u) size in evict mapping tree\n
sealed volume hash records (id %llu, size %llu) do not match size of dstream (%llu)\n
%s (id %llu): xf %u/%u: %s: uuid is NULL\n
(oid 0x%llx) %s: invalid object address (0x%llx)\n
compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n
spaceman sm_ip_bm_block_count %u is too large\n
REQUIRE_func
purgeable resource fork size (%llu) of dir-stats object (id %llu) is %s than expected (%llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given btn_flags (0x%x)\n
Checking the file extent tree.
fv_get_blob_state
file info: attribution tag (hash %llu): total count does not match expected value (%llu)\n
nx_xp_data_next (%u) is larger than the # of nx_xp_data_blocks (%u)\n
(oid 0x%llx) %s: invalid ov_flags (0x%x), tweak type set for unencrypted object\n
ersb_total_blk_to_encrypt (%llu) exceeds bm_bit_count (%llu)\n
snapshot metadata
Running FSCK
found solo clonegroup inode: (group_id %llu, private_id %llu, file_id %llu)\n
key size is too small, actual: %u, minimum: %u\n
fd_dev_read_extended
repair_overlapped_extents: unable to find volume for fs_oid 0x%llx\n
repair_overlapped_extents: load fext 0x%llx 0x%llx\n
clonegroup records of (private_id %llu) count (%u) != dstream_id refcount (%u)\n
file info: attribution tag (hash %llu): total count (%llu) does not match computed count (%llu)\n
invalid
purgeable inode (id %llu) is missing a purgeable record\n
no snap_meta entry found for snap_name entry with xid %llu and name %.*s\n
nx_fs_oid (%llu) at index (%d) is less than minimum OID (%d)\n
error iterating snapshot tree: %s\n
Performing deferred repairs.
Clone group tree is invalid.
failed!
%s (id %llu): invalid pad1 (0x%hx)\n
%s (%llu+%llu): number of bytes %u does not match sum of all entries %u\n
invalid ersb_flags (0x%llx), ERSB_FLAG_CID_IS_TWEAK is set but ersb_fext_cid == 0\n
%s (id %llu): xf %u/%u: %s: invalid hash: (0)\n
evict_mapping_tree: 
missing/invalid physical extent (%llu + %llu) with refcnt %d at snapshot %llu\n
fd_dev_close
Space manager free queue trees are invalid.
snap_meta_ext: (0x%llx:0x%llx): unknown flags (%u)\n
failed to register the dir stats tree in the fsck memory storage\n
not a root
repair_overlapped_extents: unable to remove target pext 0x%llx for fs_oid 0x%llx (pext leak): %s\n
shadow dir-stats object (id %llu) unexpectedly marked as having origin-id\n
failed to remove dir stats (id %llu) %s xfield: %s (%d)
%s%llu.%.*s %cB%s
found clone mapping in a volume with initialized clonegroup tree\n
invalid extent address range (0x%llx+%llu)\n
sfqe_entry : (range 0x%llx+0x%llx, xid 0x%llx) : Range in free queue tree lies in the internal pool\n
%s (id %llu): unknown flags (0x%hx / known flags are: 0x%hx)\n
%s (%llu+%llu): entry %u has 'unknown' tag type\n
OTI blob
object (oid 0x%llx): o_subtype invalid, o_subtype 0x%x should be 0x%x\n
INO_EXT_TYPE_PREV_FSIZE
\t\t\t<integer>%ld</integer>\n
failed to allocate memory for lookup in directory\n
(oid 0x%llx) %s: invalid crypto key index (%u), expected (%u)\n
refcnt of crypto state object (id %llu) is %s than expected (%u)\n
checkpoint %d obj->o_type is invalid: (0x%x)\n
FileExtent
uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %.*s\n
om: 
Fix object (oid 0x%llx) encryption and omap flags? 
compression xattr (id %llu): size is too small, actual: %u, minimum: %lu\n
Look for missing items in %s directory.
error (%s) failed to populate free queue trees \n
apfs superblock at index %u: apfs_fs_alloc_count (%llu) must not be greater than apfs_fs_quota_block_count (%llu)\n
%s (id %llu): invalid name_len (%u), given key length (%u)\n
can't add purgeable resource fork size for dir-stats: %s (%d)\n
dstream (id %llu) is older than the current dstream (id %llu)\n
reaper list entry (index (%u) list oid (0x%llx)) : entry is both occupied and free!\n
Could not iterate gbitmap tree to read reaper objects (oid 0x%llx): %s\n
%s (%llu+%llu): oti_ke_blob_cksum (0x%llx) is invalid for blob\n
omap entry (oid 0x%llx): invalid ov_paddr + ov_size (%llu + %u)\n
purgeable tombstone
REPAIR
apfs_root: 
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_fixed.bt_key_size (%u), given mt_key_size (%u)\n
logical addr: %lld  phys-block-num: %lld  len: %lld  flags: %x\n
com.apple.FinderInfo
Encrypted
nr
spaceman ip bitmap block xid is invalid: %llu > %llu\n
iOS encryption rolling state object: (version %u) full rolling has unrecognized current_state (%u)\n
clone mapping (private_id %llu, file_id %llu): failed to update dir stats %llu: %s (%d)\n
nx_xp_desc_index (%u) is larger than nx_xp_desc_blocks (%u)\n
repair_overlapped_extents: unable to init extentref tree for fs_oid 0x%llx\n
Fix sm_free_count (%llu)? 
\t\t</array>\n
Fix xf_used_data? 
%s (id %llu): invalid sibling_id (%llu)\n
msec
object (oid 0x%llx): unable to add omap repair: %s\n
cab
failed to initialize the clone group tree: %s\n
DstreamID
repair_overlapped_extents: update target pext 0x%llx\n
%s (id %llu): xf %u/%u: %s: found in an unsupported volume\n
checkpoint %d (xid %llu) failed consistency check\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid btn_btree.bt_key_count (expected %llu, actual %llu)\n
btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: unable to repair minkey\n
%s (id %llu): invalid name (%.*s), given name_len (%u)\n
omap (oid 0x%llx): invalid om_tree_type (0x%x)\n
need to update default_crypto_id (%llu) of dstream (object-id %llu) with missing crypto state\n
%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n
Checking the fsroot tree.
error (%d) writing spaceman IP bitmap %d @ %lld\n
AppleAPFSContainer
cpm_flags has invalid flags set: 0x%x\n
```
