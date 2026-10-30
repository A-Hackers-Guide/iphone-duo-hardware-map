# `/System/Library/Filesystems/hfs.fs/fsck_hfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 323,968 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2032)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/FSKit.framework/FSKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
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

## Strings (790)

```
hash: duplicate insert! (%d)\n
hfs_swap_HFSBTInternalNode: extents key #%d invalid length (%d)\n
\t%s - AllocateClearMemory failed to allocate %d bytes \n
\tinvalid first leaf node - calculated %d header %d \n
The volume name is %s
Missing directory record (id = %u)
Invalid volume free block count
\tIncorrect dirinode ID for dirlink=%u (expected=%u, found=%u)\n
CacheRead: CacheLookup failed %d [BUF_SPAN]\n
.journal_info_block
$File_ID_%d\n
SUCCESS
Journal was bad, stopped replaying\n
\t%s: parentID for id=%u do not match (fileKey=%u threadRecord=%u)\n
\tInvalid alternate volume header - error %d \n
Embedded offset is %lld\n
CAN'T CHECK FILE SYSTEM.
%s: invalid debug development argument.  Assuming zero\n
fsck_msg_number
Volume bitmap needs repair for under-allocation
Orphaned open unlinked file %s
\tillegal name is 0x
\tfirst link EA attrData is not NULL terminated for dirinode=%u\n
\tprivdir_valence=%u, calc_dirlinks=%u, calc_dirinode=%u\n
Extents Data attribute size %u is larger than HFSPlusAttrExtents size %u\n
\tBlock number %qd is not embedded alternate volume header \n
Journal checksum doesn't match:  orig %x != calc %x\n
\tinvalid VHB nextCatalogID \n
pread(%d, %p, %zu, %llu)
%d$@
%d %%
Limited repair mode, not all repairs available
B-tree node is split across extents (file id %u)
  PROJECT:
fsck_hfs: Use the -f option to force checking.\n
%s(%d):  index %u >= numRecords %u\n
  r = rebuild catalog btree \n
UNKNOWN
\tTransaction replay failed, returned %d\n
\tUsing cacheBlockSize=%uK cacheTotalBlock=%u cacheSize=%uK.\n
\tfirst link EA is not inline for dirinode=%u (found=0x%x)\n
UpdFolderCount:  ReplaceBTreeRecord failed (%d)\n
%c
ERROR: volume %s is mounted with write access. Re-run with (-l) to freeze volume.\n
\t\t\t<dict><key>%s</key> <string>%s</string></dict>\n
Look for missing items in %s directory.
%s: Tried to read JIB, got %zd\n
RotateRight: InsertKeyRecord (right) returned false!\n
(%ld, %qd)\n
\tcould not get embedded primary volume header at %qd, err %d \n
FixBadExtent
%s is not a character device\n
\t\t<key>%s</key> <integer>%u</integer>\n
Invalid volume header
Can't rebuilt attributes btree when there is no attributes file\n
Catalog BTree
\tvolume allocation block count %d device allocation block count %d \n
TrimFreeBlocks
INTERNAL ERROR: GOT TO reply()
%llu\n
\t\t</array>\n
%s: 
%s(line %d):  height %d != level %d\n
Requested attributes btree rebuild, but attributes file size is 0\n
%08x 
\tCould not recreate a missing directory (error %d)\n
%ld\n
Incorrect block count for file %s
Maximum nesting of folders and directory hard links reached
    curNodeNum = %u\n
hardLinkCheckBegin:  malloc(%zu) failed\n
hfs_swap_HFSBTInternalNode: catalog folder record #%d too big\n
Node %d's forward link is 0x%x; expected 0x%x\n    disk offset = 0x%llx, size = 0x%x\n
The volume %s could not be verified completely.
Checking catalog file.
I can't understand this version of HFS Plus
Incorrect block count for attribute %s of file %s
Record %d (offset 0x%04X):\n
IOMedia
journal_replay(%s) returned %d\n
Incorrect number of thread records
%s(%p, %p, %zu):  journal buffer wrap count = %d\n
\tinvalid VHB encodingsBitmap, disk=0x%qx calculated=0x%qx \n
fsckPrint
PROGRESS
Checking extended attributes file.
\t%s: fileID do not match (threadKey=%u fileRecord=%u), parentID=%u\n
%s %04x:  
GetJournalInfoBlock
Rebuilding extents overflow B-tree.
Incorrect flags for directory hard link ancestor (id = %u)
\tInvalid block size block_list_header\n
hfs_swap_HFSPlusBTInternalNode: attr inline #%d too big (attrSize=%u)\n
\t\"%s\": fixing mode from %07o to %07o\n
 
BSD Name
TrimFlush: nothing to flush\n
  x = XML output mode\n
 *****
directory
hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n
hfs_swap_HFSPlusBTInternalNode: attr fork data #%d too big\n
Unable to get journal file descriptor, journal flags = %#x\n
block %llu:\t
Invalid catalog record type
Wrapper catalog file location needs repair
getJournalTransaction
%u
BlockFindAll
\talternate VHB is at block %qd 0x%02qx \n
  S = Scan disk for bad blocks\n
Missing thread record for root dir
Incorrect folder count in a directory (id = %u)
\tLink reference num=%ld is invalid for inode=%u result=%d\n
error %d from cond wait\n
%s: Device block count was not initialized by user\n
Unknown attribute type %u\n
\tinvalid last leaf node - calculated %d header %d \n
update/reload mount for %s failed: %s\n
msg != NULL
%d\n
%s
%s(%d):  nodeNum %u > totalNodes %u\n
GetNode
Node %d's back link is 0x%x; expected 0x%x\n    disk offset = 0x%llx, size = 0x%x\n
\tinvalid VHB modifyDate \n
%s%s%s\n
Invalid file clump size
\tPrivate directory for dirlinks not found.  Stopping repairs.\n
%lu
\tcould not get volume block %d, err %d \n
Can't initialize disk cache\n
Got a non I/O error reading disk at offset %llu: %s\n
Invalid name for directory inode (id = %u)
hfs_swap_HFSBTInternalNode: catalog thread record #%d too big\n
--\n
\t\t\t<integer>%ld</integer>\n
Checking multi-linked files.
Detected a case-sensitive volume.
\tDetected when adding (%u,%u) to following traversal stack -\n
\tfilelink prime buckets do not match\n
\tinvalid wrapper MDB \n
/dev/%s
Invalid extent entry
DeleteRecord
\t%s: Error in deleting attribute record for id=%u\n
\tinvalid MDB drVolBkUp \n
doing update / reload mount for %s now\n
fsck_msg_type
BT map too short during repair
Invalid root directory count
Journal read amount is 0, is that right?\n
WriteFragmentedBlock: NULL bufs list!\n
%s%u
\tIncorrect record type for link=%u for inode=%u (expected=2, found=%u)\n
\tfilelink: fdType = 0x%08lx, fdCreator = 0x%08lx\n
\tcould not get primary MDB at block %qd, err %d \n
  n = assume a no response \n
/dev/fd/
VERIFY
\tcheck_loops: Allocation failed for visited list\n
\tduplicate name is 0x
\t\t\t<integer>%d</integer>\n
DAMAGEINFO
The volume %s could not be repaired after %d attempts.
Missing thread record (id = %u)
Bad information for symbolic link (file id %u)
\tvolume check failed with error %d \n
UUID
File/folder %s could not be repaired.
Keys out of order
Attributes BTree
(%c,\"%s\",%d)\n
Invalid key length
Incorrect flags for file inode (id = %u)
\t\tAnd we don't care\n
\tData out of range for block_list_header\n
hfs_swap_HFSPlusBTInternalNode: catalog key #%d too big\n
\tFixBadFlags (folder):  old = %#x, incorrect = %#x, correct = %#x\n
** %s (NO WRITE)\n
Invalid B-tree header
Invalid B-tree node size
Invalid Finder info for file hard link (id = %u)
\t%s: File thread recordType mismatch for id=%u (found=%u)\n
QUICKCHECK ONLY; FILESYSTEM CLEAN\n
fsck_msg_string
The volume %s was found corrupt and can not be repaired.
The volume %s was found corrupt and needs to be repaired.
Rebuilding catalog B-tree.
Invalid map node linkage
Reserved fields in the catalog record have incorrect data
%s(%d):  rv = %d\n
%s:  found %u blocks but needed %u\n
UpdFolderCount:  actual record type (%d) != FolderRecord\n
Startup File
|\n
\tinvalid MDB drCTClpSiz \n
** Root file system\n
Checking volume.
(catRecord.recordType == kHFSPlusFileRecord) || (catRecord.recordType == kHFSFileRecord)
%s: Could not get overflow extents record for fileID %u, fork %u, start block %u\n
%s: Error in copying disk blocks for fileID = %d (err=%d)\n
\tBlock %d is not an MDB or Volume Header \n
block %llu:\t*** NO MATCH ***\n
Volume bitmap needs minor repair for orphaned blocks
SRepair.c
hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d name too big\n
hfs_swap_HFSBTInternalNode: catalog key #%d offset too big (0x%04X)\n
\tCould not create lost+found directory \n
isHFSPlus == true
\tcould not get alternate volume header at %qd, err %d \n
usage: %s [-b [size] B [path] c [size] e [mode] ESdfglx m [mode] npqruy] special-device\n
Invalid BSD file type
\tfirst link ID=%u is < 16 for fileinode=%u\n
hfs_UNswap_BTNode: offsets %d and %d out of order (0x%04X, 0x%04X)\n
\tprimary MDB is at block %qd 0x%02qx \n
\tCheckExtRecord: id=%u %d:(%u,%u), maxBlocks=%u (startBlock > maxBlocks)\n
%s:  unable to load journal header from %s\n
GetCatalogRecord
\tinvalid alternate MDB at %qd result %d \n
hfs
\tinvalid tree depth - calculated %d header %d \n
\tinvalid VHB createDate \n
  g = GUI output mode\n
DeleteOffset
com.apple.system.hfs.firstlink
hash table full (%d entries) \n
%s: Cannot GetVolumeBlock: %d\n
\tinvalid MDB drCrDate \n
Invalid directory item count
\tinvalid VHB rsrcClumpSize (VH=%u, vcb=%u)\n
Can't get device block count (%s)\n
 * * * cannot allocate memory * * *\n
\n
hfs_swap_HFSPlusBTInternalNode: extents key #%d invalid length (%d)\n
external journal device name = `%s'\n
* * * cannot allocate memory * * *\n
volumename
Checking extents overflow file.
\tUpdFolderCount: first SearchBTreeRecord failed, parid = %u, result = %d\n
Repair Catalog File
Got %u errors, maxing out so stopping scan\n
hfs_UNswap_BTNode: invalid forward link (0x%08X)\n
DamagedFiles
\t%s - unknown volume type \n
\tinvalid MDB drNmRtDirs \n
** 
0
\tCache size should be greater than %uM and less than %luM\n
Symlink for file id %u has bad data length\n
.HFS+ Private Directory Data\r
%s: No matching extent record found in extents btree for fileID = %d (err=%d)\n
%s: No matching extent record found for fileID = %d\n
\tinvalid alternate VHB at %qd result %d \n
fsck_hfs: Invalid file descriptor path: %s
path
\tinvalid MDB drNmAlBlks \n
%s? no\n\n
desktop
Invalid number of allocation blocks
Loop in directory hierarchy
Master Directory Block needs minor repair
File record has hard link chain flag (id = %u)
%s(%d):  wrong kind of node\n
FixOrphanedFiles
Index key doesn't match first node key\n
\tinvalid MDB drSigWord \n
Checking Journaled HFS Plus volume.
Invalid directory record length
Incorrect flags for file hard link (id = %u)
hfs_swap_HFSPlusBTInternalNode: catalog file record #%d too big\n
\tinvalid VHB writeCount \n
Trimming unused blocks.
Invalid index link
1
BuildAttributeKey
\tVolumeObject flags = 0x%02X \n
Alternate MDB drXTFlSize = %llu, should be %llu\n
$Extents_Overflow_File\n
Improperly split node in file id %u, offset %u (extent #%d), Extent <%u, %u>\n
%s? yes\n\n
\t\t\t<string>%s</string>\n
\tTried to allocate %dK, minimum is %dK\n
%qd
\tError getting first link ID for inode=%u\n
hfs_swap_BTNode: invalid backward link (0x%08X)\n
hfs_swap_HFSBTInternalNode: catalog thread record #%d name too big\n
FAIL
Cannot create links to all corrupt files
i28@?0^v8i16*20
\t%s: Folder thread recordType mismatch for id=%u (found=%u)\n
. . .\n
\tinvalid VHB checkedDate \n
The volume %s cannot be verified when it is in use.
hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n
journalRead
\tData end out of range for block_list_header\n
%s: Could not replace catalog record for fileID %u\n
HasFolderCount flag needs to be set (id = %u)
%s: fsck_hfs completed at %s\n
\treplacement name is 0x
Unable to allocate %llu bytes for reading symlink
hash: overwriting data! (old:%u, new:%u)\n
..
%#x
parameters
Invalid file or directory ID found
Allocation File
\tFixBadFlags (parent folder):  old = %#x, incorrect = %#x, correct = %#x\n
UpdateExtentInAttributeBT
\tvolume headers disagree but there is confusion on which to use \n
Could not read journal from descriptor %d: %s
VolumeBitmapCheck.c
** %s\n
/r
\tfirst link ID=%lu is > UINT32_MAX for dirinode=%u\n
\tCache size should be multiple of cache block size (currently %uK)\n
\tinvalid MDB drFndrInfo \n
%s: unknown btree rebuild code `%c' (%#x)\n
Can't open %s: %s\n
Physical block size is not a power of 2\n
  %s\n
%s\n
\n%s: UNEXPECTED INCONSISTENCY; RUN fsck_hfs MANUALLY.\n
hfs_swap_HFSBTInternalNode: catalog file record #%d too big\n
\tsector size = %d 0x%02x \n
\tvolume headers disagree on extents file total blocks - primary %d alternate %d \n
ERROR:  error output redirected to target volume for live verify.\n
Invalid file record length
%s:  wanted %zd, got %zd\n
HardLinkCheckBegin: prime bucket allocation failed\n
\tinvalid VHB attributesFile.clumpSize \n
BTree rebuild requested but writing disabled\n
r
Invalid map node
Invalid extent file PEOF
ReadFrstate.debugLength != fragSize)\n
RepairHardLinkChains:  calloc(%d, %zu) failed\n
hfs_swap_HFSPlusBTInternalNode: attr key #%d offset too big (0x%04X)\n
\tinvalid MDB drVBMSt \n
\tinvalid MDB drClpSiz \n
\tIncorrect linkCount for inode=%u (expected=%u, found=%u)\n
hfs_UNswap_BTNode: offset #%d invalid  (0x%04X) (blockSize 0x%x numRecords %d)\n
%s: Device block size was not initialized by user\n
\tinvalid MDB drAlBlSt \n
</plist>\n
Previous ID in a hard link chain is incorrect (id = %u)
Next ID in a hard link chain is incorrect (id = %u)
hfs_swap_BTNode: offset #%d invalid  (0x%04X) (blockSize 0x%x numRecords %d)\n
\tFixBadLinkChainFirst: Attribute btree does not exists.\n
\t%s - repair failed for type 0x%02X %d \n
\tinvalid VHB nextAllocation \n
%s invalid block size %d\n
  d = output debugging info\n
Overlapped extent allocation (id = %u, %s)
Invalid root node number
hfs_UNswap_BTNode: invalid node height (%d)\n
lost+found
\tinvalid MDB drWrCnt \n
Cannot scan for bad blocks and ask for listed blocks to file mapping\n
%s: Error in updating extent record for fileID = %d (err=%d)\n
\t%s - volume header total allocation blocks is too small to be valid \n
Expected %d records in node, found %d\n
Repairing volume.
Invalid catalog record length
Disk full error
Invalid attribute record
\tlinkCount=0 for dirinode=%u\n
# DeviceRead: lseek(%qd) failed with %d\n
MoveCatalogRecordByID
Got a non I/O error reading disk at offset %llu:  %s\n
  p = just fix normal inconsistencies \n
Invalid allocation block start
Inline Attribute size %u is larger than maxsize %u\n
%s: Cannot find attribute record (err = %d)\n
(attrRecord->recordType == kHFSPlusAttrForkData) || (attrRecord->recordType == kHFSPlusAttrExtents)
\tInvalid primary volume header - error %d \n
\tinvalid MDB drAtrb \n
Trimmed %u allocation blocks.\n
b:B:c:dD:e:EfgJlm:npqrR:SuxXy
  q = quick check returns clean, dirty, or failure \n
Hard Link catalog entry %u has bad time %u (should be %u, or at least %u)\n
Extents Overflow BTree
\tvolume allocation block count %d \n
CheckAttributeRecord
$Catalog_File\n
Expected map node, got type %d\n
\tinvalid VHB totalBlocks \n
ERROR: could not freeze volume (%s)\n
\t%s: Error in replacing catalog record for id=%u\n
IVChk
Searching for key:\n
VolumeObjectIsValid
Node:\n
(bit % kBitsPerWord) == 0
%s is not a character device
Safe mode and single-user, setting memsize to a maximum of 2gbytes\n
\t\t<key>%s</key>\n
Verifying volume when it is mounted with write access.
Journal is empty\n
Fork Data attribute size %u is larger then HFSPlusAttrForkData size %u\n
$Attributes_File\n
\tCheckExtRecord: id=%u %d:(%u,%u), (startBlock == 0)\n
Exceeded maximum B-tree depth
CheckCatalogBTree
iNode
hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d too big\n
\tThread record:\n
%s: Incorrect BitMask found.\n
ERROR:  output redirected to target volume for live verify.\n
com.apple.FSKit
Incorrect flags for directory inode (id = %u)
FixIllegalNames
%s: Error finding attribute record (err=%d) for fileID = %d, attrname = %d\n
  E = exit on first major error\n
Incorrect number of directory hard links
S12@?0S8
a
\t%s: fileID=%u, thread.key.parentID=%u, record.fileID=%u\n
\tUnknown repair order found (type = %d)\n
\tprimary VHB is at block %qd 0x%02qx \n
\tcould not get alternate MDB \n
error %d getting path for id=%u\n
fsck_verbosity
Incorrect size for file %s
QUICKCHECK ONLY; NO HFS SIGNATURE FOUND\n
  e mode = emulate 'embedded' or 'desktop'\n
Invalid BTH length
Illegal name
Missing private directory for directory hard links
Invalid name for file inode (id = %u)
Orphaned file inode (id = %u)
hfs_swap_BTNode: invalid node height (%d)\n
fsck_hfs: fstat %s
(%d %%)\n
Look for links to corrupt files in %s directory.
File thread flag not set in file record
Incorrect size for attribute %s of file %s
Invalid Finder info for directory hard link (id = %u)
\tData size for block %d out of range for block_list_header\n
GetCatalogRecordByID
\tfirst link ID=%u is < 16 for dirinode=%u\n
\tDuplicate link=%u found in list for inode=%u\n
Unable to allocate hard link time repair order!
\tDoMinorRepair: Repair for type=%d failed (err=%d).\n
VolumeObjectIsHFSPlus() == true
%s: Could not replace overflow extents record for fileID %u, fork %u, start block %u\n
Non-empty journal:  start = %lld, end = %lld\n
%s: %s\n
\tinvalid primary VHB at %qd result %d \n
Improperly split node in file id %u, startBlock %u, index %d (offset %u), extent <%u, %u>\n
ERROR: input redirected from target volume for live verify.\n
ERROR: could not open %s to freeze the volume.\n
<plist version=\"1.0\">\n
\t<dict>\n
INFORMATION
hfs_swap_HFSBTInternalNode: catalog record #%d keyLength=%u expected=%u\n
Rechecking volume.
Checking volume information.
Checking non-journaled HFS Plus Volume.
%s:  Unknown journal endian magic number %#x from %s\n
I12@?0I8
UNKNOWN-DEV
\tIncorrect flag for link=%u for inode=%u (found=0x%x)\n
hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n
\tFile/Folder record:\n
%04x:  
\tInvalid embedded primary volume header at block %qd - error %d \n
%s: jnl: %s: open: bad jhdr size (%d) \n
0x%x
hfs_swap_HFSPlusBTInternalNode: catalog key #%d offset too big (0x%04X)\n
hfs_swap_HFSBTInternalNode: unrecognized catalog record type (0x%04X; record #%d)\n
AllocMinorRepairOrder
Unable to open block device %s: %s
Hard link record has data extents (id = %u)
/dev/rdisk
\tunknown volume type \n
  
\textentType=0x%x, startBlock=0x%x, blockCount=0x%x, attrName=%s\n
\tinvalid MDB drNxtCNID \n
Invalid key for thread record
Overlapped extent allocation (id = %d)
fsck_hfs: Volume is journaled.  No checking performed.\n
%s(%d):  other wrong kind of node\n
\tError getting link=%u for inode=%u\n
MoveExtent
$Allocation_Bitmap_File\n
\tinvalid MDB drLsMod \n
  b size = size of physical blocks (in bytes) for -B option\n
   
%02X 
\tinvalid MDB drVN \n
QUICKCHECK ONLY; FILESYSTEM DIRTY\n
\t\t<key>%s</key> <integer>%s</integer>\n
\t\t\t<integer>%llu</integer>\n
Invalid allocation block size
Journal needs to be replayed but volume is read-only
Symbolic link (file id %u) has bad length (is %u, should be %u)
%s(%d):  curNodeNum is 0\n
hfs_swap_HFSPlusBTInternalNode: extents key #%d offset too big (0x%04X)\n
%s: No matching catalog thread record found\n
Executing %s (version %s).
Overlapped node allocation
Volume header needs minor repair
Bad symbolic link is `%s'
%s/Library/Logs/fsck_hfs.log
ReleaseFragmentedBlock: NULL buf list!\n
RotateRight: RotateRecordRight returned false!\n
hfs_swap_HFSPlusBTInternalNode: attr inline #%d too big\n
Unknown File
    |
\tinvalid VHB dataClumpSize \n
CheckHardLinks:  calloc(1, %zu) failed\n
\tvolume type is pure HFS+ \n
\tinvalid VHB backupDate \n
fsck_hfs
hfs_UNswap_BTNode: invalid backward link (0x%08X)\n
%s: Bad extent for fileID %u in extent %u for startblock %u\n
fsck_hfs: Could not seek %d for dev: %s, errorno %d
** %s (NO WRITE ACCESS)\n
Checking multi-linked directories.
%s:  Invalid journal checksum from %s\n
%s(%d):  hdr has bad checksum, returning NULL\n
%s: Record found is not attribute fork data\n
\tinvalid VHB finderInfo \n
\n***** REBOOT NOW *****\n
\t\t\t<integer>%p</integer>\n
Invalid sibling link
Indirect node %d needs link count adjustment
\tFailed to allocate %uK for cache; trying %uK\n
%s: returning fsBTInvalidNodeErr\n
hfs_swap_BTNode: invalid record count (0x%04X)\n
Node %u:\n
\t%s: Folder recordType mismatch for id=%u (found=%u)\n
\tvolume type is embedded HFS+ \n
%02x
\tcould not get primary MDB \n
\tIncorrect link reference number for filelink=%u (expected=%u, found=%u)\n
hfs_UNswap_BTNode: invalid record count (0x%04X)\n
\tinvalid alternate wrapper MDB \n
Only read %zd bytes from journal (expected %zd)
AddExtentToOverlapList
Device block size was not initialized\n
  f = force fsck even if clean (preen only) \n
Invalid node height
\tinvalid primary MDB at %qd result %d \n
Records %d and %d (0-based); offsets 0x%04X and 0x%04X\n
Q16@?0Q8
%s(%d):  Wanted to read %zu, but only read %zd\n
UpdFolderCount: second SearchBTreeRecord failed (thread.parentID = %u, result = %d), just returning without complaint\n
\t%s: Unknown record type.\n
\tBlock number %qd is not embedded primary volume header \n
attrname != NULL
%s(%d):  offset is wrong\n
/
  B path = file containing physical block numbers to map to paths\n
fsck_messages.c
hfs_swap_HFSPlusBTInternalNode: catalog key #%d invalid length (%d)\n
\t%s: File recordType mismatch for id=%u (found=%u)\n
ERROR
Rebuilding extended attributes B-tree.
Orphaned file hard link (id = %u)
SearchTree
hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d too big\n
hfs_swap_HFSBTInternalNode: invalid record offset (0x%04X)\n
%s:  %u blocks free, but need %u; ignoring for now\n
Found (child; node %u):\n
\tinvalid VHB attributes \n
Scanning entire disk for bad blocks\n
Nesting of folders has exceeded %d folders
\n%s: fsck_hfs started at %s
hfs_UNswap_BTNode: invalid node kind (%d)\n
CheckFileExtents
Checking catalog hierarchy.
\nfsck_hfs started at %s
hfs_swap_HFSBTInternalNode: invalid record count (0x%04X)\n
\tinvalid device information for volume - total sectors = %qd sector size = %d \n
Can't stat %s\n
Incorrect number of extended attributes
hfs_swap_HFSBTInternalNode: catalog key #%d invalid length (%d)\n
System File: 
Extents:\n
Cannot allocate buffer for disk scan.\n
Physical block size cannot be greater than 16 KiB\n
Performing live verification.
%s:  journal block size %u < min block size %zu for %s\n
i32@?0q8^v16Q24
hfs_swap_BTNode: initial record at bad offset (0x%04X)\n
\t%s: Created thread record for id=%u (err=%u)\n
Scanning offset %lld\n
Can't stat root\n
Catalog file entry not found for extent
HFS wrapper volume needs repair
swapped endian
\tinvalid MDB drFilCnt \n
\tinvalid VHB signature \n
hfs_swap_HFSPlusBTInternalNode: catalog record #%d (0-based, offset 0x%lX) keyLength=%d expected=%lu\n
\ttotal sectors for volume = %qd 0x%02qx \n
The volume %s could not be repaired.
tried to read %zu for journal header buffer, got %zd
hfs_swap_HFSBTInternalNode: catalog key #%d too big\n
\treplacement name already exists \n
\t%s - volume header total allocation blocks is greater than device size \n
Trimming: startBlock=%10u, blockCount=%10u\n
Invalid length for file name
Invalid VBM start block
\tdirlink prime buckets do not match\n
id=%u
\tCheckHardLinks: found %u pre-Leopard file inodes.\n
Bogus Extents File
SearchExtentInAttributeBT
\r Pure HFS Plus
CONTINUE
kern.progressmeterenable
dir_
\tCheckHFS returned %d, fsmodified = %d\n
%s: missing special-device\n
The volume %s cannot be repaired when it is in use.
Invalid node type
Invalid volume directory count
Invalid first link in hard link chain (id = %u)
Can't get device block size (%s)\n
  c size = cache size (ex. 512m, 1g)\n
  l = live fsck (lock down and test-only)\n
Checking HFS volume.
Invalid parent for directory inode (id = %u)
%s: Cannot replace attribute record (err=%d)\n
hfs_swap_BTNode: invalid node kind (%d)\n
The volume %s could not be verified completely and can not be repaired.
Missing file record for file thread
Incorrect number of Access Control Lists
File has incorrect number of links (id = %u)
native endian
Offset %llu length %u:\n
Journal replay simulation succeeded\n
\t%s: fileCount = %u, fileThread = %u\n
\t%s: fileThreads = %u, filesWithThread = %u\n
Record %u (offset 0x%04X):\n
hfs_swap_HFSPlusBTInternalNode: unrecognized catalog record type (0x%04X; record #%d)\n
External Journal device\n
\t%s - could not get VHB/MDB at block %qd \n
com.apple.system.Security
CheckNodesFirstOffset
\tinvalid VHB extentsFile.clumpSize \n
Can't allocate memory for block list.\n
hw.memsize
Scanning offset %lld of %lld (%d%%)\n
  y = assume a yes response \n
Incorrect owner flags for directory hard link (id = %u)
\t error %d - could not allocate %ld bytes of memory \n
Invalid parent for file inode (id = %u)
Orphaned directory hard link (id = %u)
\tBlock %qd is not an MDB or Volume Header \n
Invalid volume file count
Bad parent directory hierarchy (id = %u)
RotateRight: InsertKeyRecord (left) returned false!\n
%s: Could not get catalog record for fileID %u\n
\tinvalid root node - calculated %d header %d \n
kern.progressmeter
%08X: 
\tfirst link EA attrData contains non-digit 0x%x for dirinode=%u\n
\"ROOT_OF_VOLUME%s\" (file id=%u)\n
Internal files overlap (file %u)
Invalid content in journal
Incorrect flags for directory hard link (id = %u)
\tIncorrect prevLinkID for link=%u for inode=%u (expected=%u, found=%u)\n
Bad Allocation File
\t%s - bad volume header - err %d \n
Can't allocate memory for block list (%llu entries).\n
Invalid node structure
BTIterateRecord
hfs_swap_HFSPlusBTInternalNode: fileID %u is not a system B-tree\n
CheckPhysicalMatch: Out of memory!\n
\tinvalid MDB drVSeqNum \n
\tinvalid MDB drXTClpSiz \n
sysctlbyname failed, not auto-setting cache size\n
During disk scan, did not get block size (%zd) read, got %zd instead.  Skipping rest of this block.\n
\t\t<key>%s</key> <string>%s</string>\n
\tdirlink: fdType = 0x%08lx, fdCreator = 0x%08lx\n
\tError getting first link ID for inode = %u (result=%d)\n
hfs_swap_HFSBTInternalNode: extents key #%d offset too big (0x%04X)\n
%s: Error in deleting record for %s for fileID %d, type = %d\n
\tCheckExtRecord: id=%u %d:(%u,%u), (blockCount != 0)\n
\tinvalid node size - calculated %d header %d \n
\tinvalid MDB drDirCnt \n
embedded
%ld
\t%s: No matching catalog record found for id=%u\n
\tvolume type is HFS \n
fsck_hfs: detonator_run (%s).\n
kern.safeboot
  u = usage \n
The volume %s appears to be OK.
Checking volume bitmap.
/var/log/fsck_hfs.log
volumeType is %d\n
Expected (parent; node %u):\n
%s? [yn] 
Can't dup fd for reading on %s: %s\n
REPAIR
Invalid file name
Directory name locked
CheckHFS
SVerify1.c
\tCheckExtRecord: id=%u %d:(%u,%u), (blockCount == 0)\n
File/folder %s may be damaged.
Invalid BSD User ID
\t
\t%s: dirCount = %u, dirThread = %u\n
hfs_swap_HFSBTInternalNode: fileID %u is not a system B-tree\n
%s: No matching catalog record found\n
CheckForClean
Invalid header node
Invalid thread record length
Orphaned directory inode (id = %u)
\t error %d - could not allocate file ID list \n
\tInvalid embedded alternate volume header at block %qd - error %d \n
\tinvalid VHB AlBlSt \n
TrimFlush: error %d\n
starting\n
Unused node is not erased (node = %u)
                  CBTStat = 0x%04x CatStat = 0x%08x\n
\tlink reference num=%lu is > UINT32_MAX for inode=%u\n
FixAttrSize
\tFixBadFlags (file):  old = %#x, incorrect = %#x, correct = %#x\n
\talternate MDB is at block %qd 0x%02qx \n
fstype
\tcould not get embedded alternate volume header at %qd, err %d \n
CompareXattrPrimeBuckets
file
\t</dict>\n
Invalid leaf record count
Bad hard link creation date
   Verify Status: VIStat = 0x%04x, ABTStat = 0x%04x EBTStat = 0x%04x\n
(extentInfo->attrname != NULL)
Header root node %u, calculated total nodes %u, tree depth %u, header node num %u\n
\tinvalid max key length - calculated %d header %d \n
Bad block at offset %lld\n
Invalid record count
Invalid catalog PEOF
%s:  Unknown journal header magic number %#x from %s\n
(bit % kBitsPerSegment) == 0
Can't stat %s: %s\n
%s:  journal block size %u is not a multiple of fs block size %zu for %s\n
hfs_swap_BTNode: offsets %d and %d out of order (0x%04X, 0x%04X)\n
\t%s: Deleted thread record for id=%d (err=%d)\n
RepairAttributesCheckABT
Incorrect permissions for private directory
Incorrect number of file hard links
journal_open
id = %u
%s: %ld is invalid mode argument\n
Invalid root file count
(%u,%u) 
hfs_UNswap_BTNode: initial record at bad offset (0x%04X)\n
forkType != kEAData
\ttotal sectors for embedded volume = %qd 0x%02qx \n
Extents File totalBlocks = %u, numABlks = %u\n
%s: Deleting attribute %s for fileID %d, type = %d\n
\tinvalid VHB blockSize \n
The volume was modified
hfs_swap_HFSPlusBTInternalNode: attr extents #%d too big\n
hfs_swap_BTNode: unrecognized attribute record type (%d)\n
\tvolume headers disagree on catalog file total blocks - primary %d alternate %d \n
\tCheckExtRecord: id=%u %d:(%u,%u), maxBlocks=%u (blockCount > (maxBlocks - startBlock))\n
%p\n
The volume %s was repaired successfully.
Invalid parent CName in thread record
hfs_swap_HFSPlusBTInternalNode: attr key #%d too big (%d)\n
Couldn't read node #%u\n
fsck_hfs completed at %s\n
CANNOT WRITE: BLK %ld\n
%s: Deleting extent overflow for fileID=%u, forkType=%u, startBlock=%u\n
\t%s: nodeName for id=%u do not match\n
\tinvalid total nodes - calculated %d header %d \n
\t\t<array>\n
\tPrivate directory for filelinks not found.  Stopping repairs.\n
hfs_swap_BTNode: invalid forward link (0x%08X)\n
\tinvalid primary wrapper MDB \n
\tinvalid free nodes - calculated %d header %d \n
Problem: b-tree key for \"HFS+ Private Data\" directory is out of order.\n
(It should be %s instead of %s)
\tCheckHardLinkList: list=NULL for inodeID = %u\n
hfs_swap_HFSPlusBTInternalNode: attr key #%d keyLength=%d attrNameLen=%d\n
%lli
Invalid index key
%d
\tinvalid VHB allocationFile.clumpSize \n
sysctl(%s) failed
  m arg = octal mode used when creating lost+found directory \n
```
