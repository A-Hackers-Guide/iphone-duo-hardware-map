# `/System/Library/Filesystems/hfs.fs/fsck_hfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 323,968 bytes.

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
Nesting of folders has exceeded %d folders
journal_open
Journal read amount is 0, is that right?\n
\tvolume check failed with error %d \n
\tinvalid MDB drFilCnt \n
  S = Scan disk for bad blocks\n
 * * * cannot allocate memory * * *\n
Invalid file record length
%s:  Unknown journal endian magic number %#x from %s\n
getJournalTransaction
hfs_swap_BTNode: invalid forward link (0x%08X)\n
ERROR:  error output redirected to target volume for live verify.\n
a
                  CBTStat = 0x%04x CatStat = 0x%08x\n
hfs_swap_HFSPlusBTInternalNode: attr fork data #%d too big\n
System File: 
%s: invalid debug development argument.  Assuming zero\n
Can't stat %s\n
Reserved fields in the catalog record have incorrect data
Incorrect number of Access Control Lists
\t%s: Folder recordType mismatch for id=%u (found=%u)\n
\t%s - AllocateClearMemory failed to allocate %d bytes \n
\tcould not get embedded primary volume header at %qd, err %d \n
r
Invalid VBM start block
Invalid B-tree header
Invalid leaf record count
Bad Allocation File
\t%s: Error in replacing catalog record for id=%u\n
\t%s: No matching catalog record found for id=%u\n
ERROR: could not freeze volume (%s)\n
  E = exit on first major error\n
hfs_swap_BTNode: invalid node height (%d)\n
Embedded offset is %lld\n
Index key doesn't match first node key\n
Can't allocate memory for block list (%llu entries).\n
\tlinkCount=0 for dirinode=%u\n
\tFixBadLinkChainFirst: Attribute btree does not exists.\n
Expected (parent; node %u):\n
/
%s:  journal block size %u is not a multiple of fs block size %zu for %s\n
\n%s: UNEXPECTED INCONSISTENCY; RUN fsck_hfs MANUALLY.\n
hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n
\t\t\t<integer>%d</integer>\n
</plist>\n
Incorrect number of directory hard links
\t error %d - could not allocate %ld bytes of memory \n
hfs_swap_HFSPlusBTInternalNode: attr inline #%d too big\n
\tUnknown repair order found (type = %d)\n
MoveCatalogRecordByID
block %llu:\t
\tinvalid VHB modifyDate \n
\tinvalid VHB checkedDate \n
/dev/%s
RepairHardLinkChains:  calloc(%d, %zu) failed\n
\tinvalid first leaf node - calculated %d header %d \n
VolumeBitmapCheck.c
%s? [yn] 
  n = assume a no response \n
0
Missing file record for file thread
Invalid key for thread record
\tfirst link ID=%lu is > UINT32_MAX for dirinode=%u\n
Could not read journal from descriptor %d: %s
desktop
Overlapped node allocation
Internal files overlap (file %u)
RotateRight: InsertKeyRecord (left) returned false!\n
\tprivdir_valence=%u, calc_dirlinks=%u, calc_dirinode=%u\n
\tinvalid VHB encodingsBitmap, disk=0x%qx calculated=0x%qx \n
sysctlbyname failed, not auto-setting cache size\n
com.apple.FSKit
I can't understand this version of HFS Plus
Bad parent directory hierarchy (id = %u)
native endian
WriteFragmentedBlock: NULL bufs list!\n
hfs_swap_HFSBTInternalNode: catalog thread record #%d name too big\n
%s: Device block count was not initialized by user\n
%s: No matching extent record found in extents btree for fileID = %d (err=%d)\n
VolumeObjectIsValid
kern.progressmeterenable
Incorrect block count for file %s
Volume bitmap needs minor repair for orphaned blocks
\tinvalid VHB writeCount \n
\tIncorrect link reference number for filelink=%u (expected=%u, found=%u)\n
Journal checksum doesn't match:  orig %x != calc %x\n
\tinvalid wrapper MDB \n
Keys out of order
Directory name locked
%s(%d):  Wanted to read %zu, but only read %zd\n
dir_
Startup File
%s: Could not get catalog record for fileID %u\n
\tvolume type is HFS \n
\tvolume type is pure HFS+ \n
 
UUID
Device block size was not initialized\n
\tinvalid MDB drNmRtDirs \n
  e mode = emulate 'embedded' or 'desktop'\n
  r = rebuild catalog btree \n
  u = usage \n
\t\t<key>%s</key> <integer>%u</integer>\n
Checking catalog hierarchy.
\tCheckExtRecord: id=%u %d:(%u,%u), maxBlocks=%u (startBlock > maxBlocks)\n
\tinvalid MDB drSigWord \n
%s(%d):  nodeNum %u > totalNodes %u\n
hfs_swap_HFSPlusBTInternalNode: catalog record #%d (0-based, offset 0x%lX) keyLength=%d expected=%lu\n
%s: No matching catalog record found\n
DamagedFiles
\tunknown volume type \n
%s: Cannot GetVolumeBlock: %d\n
hfs_swap_HFSPlusBTInternalNode: catalog key #%d invalid length (%d)\n
\tBlock number %qd is not embedded primary volume header \n
\tinvalid VHB attributes \n
b:B:c:dD:e:EfgJlm:npqrR:SuxXy
%lli
The volume %s cannot be verified when it is in use.
Invalid root node number
HasFolderCount flag needs to be set (id = %u)
Record %u (offset 0x%04X):\n
RepairAttributesCheckABT
  
BTree rebuild requested but writing disabled\n
ERROR: volume %s is mounted with write access. Re-run with (-l) to freeze volume.\n
Invalid allocation block start
Orphaned file inode (id = %u)
Offset %llu length %u:\n
%s: Cannot replace attribute record (err=%d)\n
\t\t\t<dict><key>%s</key> <string>%s</string></dict>\n
fstype
Invalid length for file name
Invalid header node
Bad information for symbolic link (file id %u)
\tData end out of range for block_list_header\n
error %d from cond wait\n
DeleteOffset
\tlink reference num=%lu is > UINT32_MAX for inode=%u\n
\tCould not recreate a missing directory (error %d)\n
/dev/rdisk
\t\t<key>%s</key> <string>%s</string>\n
Orphaned directory hard link (id = %u)
Q16@?0Q8
\tinvalid alternate VHB at %qd result %d \n
.journal_info_block
hfs_UNswap_BTNode: invalid forward link (0x%08X)\n
%s: Error in deleting record for %s for fileID %d, type = %d\n
CONTINUE
kern.progressmeter
\tprimary VHB is at block %qd 0x%02qx \n
\tinvalid VHB dataClumpSize \n
starting\n
Checking HFS volume.
GetNode
Requested attributes btree rebuild, but attributes file size is 0\n
Unknown attribute type %u\n
$Extents_Overflow_File\n
\t%s: fileID=%u, thread.key.parentID=%u, record.fileID=%u\n
\tfirst link EA attrData is not NULL terminated for dirinode=%u\n
\tcould not get primary MDB at block %qd, err %d \n
\tinvalid VHB signature \n
The volume %s cannot be repaired when it is in use.
Incorrect permissions for private directory
\tinvalid MDB drNxtCNID \n
\tinvalid VHB totalBlocks \n
%d\n
%s: Cannot find attribute record (err = %d)\n
\tvolume headers disagree on catalog file total blocks - primary %d alternate %d \n
\tinvalid MDB drFndrInfo \n
\tCheckHFS returned %d, fsmodified = %d\n
  c size = cache size (ex. 512m, 1g)\n
UNKNOWN-DEV
hfs_swap_BTNode: unrecognized attribute record type (%d)\n
Checking volume information.
Incorrect number of file hard links
\t%s: Created thread record for id=%u (err=%u)\n
\ttotal sectors for embedded volume = %qd 0x%02qx \n
fsck_verbosity
\t\t\t<integer>%p</integer>\n
Invalid index link
ReleaseFragmentedBlock: NULL buf list!\n
%02x
\tCheckExtRecord: id=%u %d:(%u,%u), (startBlock == 0)\n
** 
(%d %%)\n
path
The volume %s was found corrupt and needs to be repaired.
com.apple.system.Security
CacheRead: CacheLookup failed %d [BUF_SPAN]\n
error %d getting path for id=%u\n
AddExtentToOverlapList
\tinvalid node size - calculated %d header %d \n
\tinvalid VHB attributesFile.clumpSize \n
update/reload mount for %s failed: %s\n
Invalid Finder info for directory hard link (id = %u)
%s: Could not get overflow extents record for fileID %u, fork %u, start block %u\n
FixOrphanedFiles
\tInvalid primary volume header - error %d \n
\t\t<key>%s</key>\n
\t\t<array>\n
Unable to allocate hard link time repair order!
\tDoMinorRepair: Repair for type=%d failed (err=%d).\n
\tThread record:\n
\tinvalid VHB AlBlSt \n
TrimFreeBlocks
Trimming: startBlock=%10u, blockCount=%10u\n
Limited repair mode, not all repairs available
Checking extended attributes file.
forkType != kEAData
\tFailed to allocate %uK for cache; trying %uK\n
hfs_swap_HFSPlusBTInternalNode: attr inline #%d too big (attrSize=%u)\n
..
\tcould not get alternate MDB \n
\r Pure HFS Plus
\tCheckExtRecord: id=%u %d:(%u,%u), maxBlocks=%u (blockCount > (maxBlocks - startBlock))\n
Record %d (offset 0x%04X):\n
%s
id=%u
SRepair.c
%s: No matching extent record found for fileID = %d\n
GetJournalInfoBlock
\tinvalid MDB drXTClpSiz \n
CAN'T CHECK FILE SYSTEM.
* * * cannot allocate memory * * *\n
%s: returning fsBTInvalidNodeErr\n
\tIncorrect flag for link=%u for inode=%u (found=0x%x)\n
hfs_swap_BTNode: invalid node kind (%d)\n
hfs_UNswap_BTNode: invalid record count (0x%04X)\n
\t%s: Error in deleting attribute record for id=%u\n
%s %04x:  
%s: Incorrect BitMask found.\n
fsck_hfs: Could not seek %d for dev: %s, errorno %d
   Verify Status: VIStat = 0x%04x, ABTStat = 0x%04x EBTStat = 0x%04x\n
hfs_swap_HFSPlusBTInternalNode: attr extents #%d too big\n
%s:  unable to load journal header from %s\n
%d
com.apple.system.hfs.firstlink
Performing live verification.
Invalid content in journal
Previous ID in a hard link chain is incorrect (id = %u)
%s(%d):  hdr has bad checksum, returning NULL\n
Unable to open block device %s: %s
\tinvalid MDB drNmAlBlks \n
fsck_hfs: Invalid file descriptor path: %s
fsck_msg_string
%s:  wanted %zd, got %zd\n
%s(%d):  rv = %d\n
\tFixBadFlags (parent folder):  old = %#x, incorrect = %#x, correct = %#x\n
%p\n
\tInvalid block size block_list_header\n
  PROJECT:
hfs_swap_HFSBTInternalNode: extents key #%d invalid length (%d)\n
ERROR: input redirected from target volume for live verify.\n
Look for links to corrupt files in %s directory.
Invalid key length
Records %d and %d (0-based); offsets 0x%04X and 0x%04X\n
QUICKCHECK ONLY; NO HFS SIGNATURE FOUND\n
SUCCESS
%s/Library/Logs/fsck_hfs.log
Extents Data attribute size %u is larger than HFSPlusAttrExtents size %u\n
\t%s: nodeName for id=%u do not match\n
  d = output debugging info\n
Rebuilding extended attributes B-tree.
Invalid extent entry
--\n
\tcould not get embedded alternate volume header at %qd, err %d \n
\tvolume headers disagree on extents file total blocks - primary %d alternate %d \n
hfs
msg != NULL
\tCould not create lost+found directory \n
    |
volumeType is %d\n
\tinvalid MDB drWrCnt \n
\tinvalid VHB nextCatalogID \n
doing update / reload mount for %s now\n
hw.memsize
%s\n
hfs_swap_HFSBTInternalNode: extents key #%d offset too big (0x%04X)\n
Executing %s (version %s).
Rebuilding catalog B-tree.
Incorrect size for file %s
Maximum nesting of folders and directory hard links reached
Invalid Finder info for file hard link (id = %u)
%s: Record found is not attribute fork data\n
%s: fsck_hfs completed at %s\n
\treplacement name already exists \n
%s%s%s\n
\t\t\t<integer>%llu</integer>\n
Checking multi-linked directories.
Invalid catalog record type
%s(%d):  other wrong kind of node\n
Cannot scan for bad blocks and ask for listed blocks to file mapping\n
fsck_messages.c
Checking multi-linked files.
Invalid BSD User ID
IVChk
%s: %ld is invalid mode argument\n
Physical block size cannot be greater than 16 KiB\n
Wrapper catalog file location needs repair
Incorrect flags for file hard link (id = %u)
hfs_swap_HFSBTInternalNode: fileID %u is not a system B-tree\n
%s: Bad extent for fileID %u in extent %u for startblock %u\n
fsck_hfs: detonator_run (%s).\n
Got a non I/O error reading disk at offset %llu: %s\n
\treplacement name is 0x
hfs_swap_HFSPlusBTInternalNode: fileID %u is not a system B-tree\n
VolumeObjectIsHFSPlus() == true
(attrRecord->recordType == kHFSPlusAttrForkData) || (attrRecord->recordType == kHFSPlusAttrExtents)
Only read %zd bytes from journal (expected %zd)
Bad block at offset %lld\n
Invalid catalog PEOF
\n
FixIllegalNames
\tinvalid max key length - calculated %d header %d \n
Invalid parent for directory inode (id = %u)
hfs_swap_BTNode: invalid backward link (0x%08X)\n
\t%s: parentID for id=%u do not match (fileKey=%u threadRecord=%u)\n
\tinvalid device information for volume - total sectors = %qd sector size = %d \n
IOMedia
The volume %s was found corrupt and can not be repaired.
Next ID in a hard link chain is incorrect (id = %u)
\tError getting link=%u for inode=%u\n
Catalog BTree
MoveExtent
. . .\n
%04x:  
CheckForClean
embedded
  l = live fsck (lock down and test-only)\n
\tCache size should be greater than %uM and less than %luM\n
\tError getting first link ID for inode = %u (result=%d)\n
hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d too big\n
SearchExtentInAttributeBT
\tVolumeObject flags = 0x%02X \n
Alternate MDB drXTFlSize = %llu, should be %llu\n
INFORMATION
Orphaned open unlinked file %s
\tfirst link ID=%u is < 16 for dirinode=%u\n
\tCheckHardLinks: found %u pre-Leopard file inodes.\n
\tFixBadFlags (folder):  old = %#x, incorrect = %#x, correct = %#x\n
\t%s: Folder thread recordType mismatch for id=%u (found=%u)\n
\tBlock number %qd is not embedded alternate volume header \n
\t%s - could not get VHB/MDB at block %qd \n
\t%s - bad volume header - err %d \n
Improperly split node in file id %u, offset %u (extent #%d), Extent <%u, %u>\n
\t%s: fileCount = %u, fileThread = %u\n
\tfirst link ID=%u is < 16 for fileinode=%u\n
hfs_swap_HFSPlusBTInternalNode: attr key #%d keyLength=%d attrNameLen=%d\n
hfs_swap_HFSBTInternalNode: catalog key #%d invalid length (%d)\n
hfs_swap_HFSBTInternalNode: unrecognized catalog record type (0x%04X; record #%d)\n
%s? yes\n\n
Can't initialize disk cache\n
  b size = size of physical blocks (in bytes) for -B option\n
CheckFileExtents
  B path = file containing physical block numbers to map to paths\n
PROGRESS
UNKNOWN
The volume %s could not be repaired after %d attempts.
Checking non-journaled HFS Plus Volume.
\tTransaction replay failed, returned %d\n
hfs_swap_HFSBTInternalNode: catalog key #%d too big\n
(catRecord.recordType == kHFSPlusFileRecord) || (catRecord.recordType == kHFSFileRecord)
%s: Could not replace catalog record for fileID %u\n
File/folder %s may be damaged.
Incorrect size for attribute %s of file %s
Incorrect flags for directory inode (id = %u)
Invalid name for directory inode (id = %u)
%s:  Unknown journal header magic number %#x from %s\n
/var/log/fsck_hfs.log
0x%x
GetCatalogRecord
%c
\tinvalid tree depth - calculated %d header %d \n
Invalid directory item count
Unused node is not erased (node = %u)
swapped endian
RotateRight: RotateRecordRight returned false!\n
\t%s: File thread recordType mismatch for id=%u (found=%u)\n
\talternate MDB is at block %qd 0x%02qx \n
Invalid sibling link
Loop in directory hierarchy
(bit % kBitsPerSegment) == 0
hfs_swap_HFSPlusBTInternalNode: catalog key #%d offset too big (0x%04X)\n
# DeviceRead: lseek(%qd) failed with %d\n
journal_replay(%s) returned %d\n
The volume %s could not be repaired.
hfs_swap_BTNode: invalid record count (0x%04X)\n
hfs_swap_HFSBTInternalNode: invalid record count (0x%04X)\n
\t%s: Deleted thread record for id=%d (err=%d)\n
\tinvalid primary MDB at %qd result %d \n
sysctl(%s) failed
During disk scan, did not get block size (%zd) read, got %zd instead.  Skipping rest of this block.\n
   
Missing thread record (id = %u)
%s: 
\n***** REBOOT NOW *****\n
Invalid file or directory ID found
Journal was bad, stopped replaying\n
I12@?0I8
\tFile/Folder record:\n
AllocMinorRepairOrder
CheckAttributeRecord
BSD Name
(bit % kBitsPerWord) == 0
%08X: 
Checking volume.
\tdirlink prime buckets do not match\n
hfs_UNswap_BTNode: offset #%d invalid  (0x%04X) (blockSize 0x%x numRecords %d)\n
CANNOT WRITE: BLK %ld\n
Attributes BTree
$Attributes_File\n
fsck_msg_type
%qd
\tIncorrect prevLinkID for link=%u for inode=%u (expected=%u, found=%u)\n
hfs_UNswap_BTNode: invalid node kind (%d)\n
\tInvalid embedded alternate volume header at block %qd - error %d \n
block %llu:\t*** NO MATCH ***\n
Invalid node type
Invalid volume header
Incorrect flags for directory hard link ancestor (id = %u)
DeleteRecord
\tCheckHardLinkList: list=NULL for inodeID = %u\n
\tcould not get alternate volume header at %qd, err %d \n
Node %d's forward link is 0x%x; expected 0x%x\n    disk offset = 0x%llx, size = 0x%x\n
Scanning offset %lld of %lld (%d%%)\n
ERROR: could not open %s to freeze the volume.\n
Look for missing items in %s directory.
Verifying volume when it is mounted with write access.
CheckCatalogBTree
\tfirst link EA attrData contains non-digit 0x%x for dirinode=%u\n
hfs_swap_HFSBTInternalNode: catalog file record #%d too big\n
Invalid node height
Missing directory record (id = %u)
Invalid root file count
Incorrect folder count in a directory (id = %u)
Node %u:\n
hfs_swap_HFSPlusBTInternalNode: extents key #%d invalid length (%d)\n
fsck_msg_number
Orphaned directory inode (id = %u)
\tUsing cacheBlockSize=%uK cacheTotalBlock=%u cacheSize=%uK.\n
\tDetected when adding (%u,%u) to following traversal stack -\n
hfs_UNswap_BTNode: initial record at bad offset (0x%04X)\n
\tsector size = %d 0x%02x \n
%s(%d):  index %u >= numRecords %u\n
\t%s: dirCount = %u, dirThread = %u\n
Header root node %u, calculated total nodes %u, tree depth %u, header node num %u\n
Overlapped extent allocation (id = %d)
hfs_swap_HFSPlusBTInternalNode: catalog file record #%d too big\n
\tinvalid MDB drCrDate \n
external journal device name = `%s'\n
The volume %s was repaired successfully.
Missing private directory for directory hard links
fsck_hfs: Use the -f option to force checking.\n
%u
\tDuplicate link=%u found in list for inode=%u\n
** %s\n
/dev/fd/
The volume %s appears to be OK.
The volume name is %s
Improperly split node in file id %u, startBlock %u, index %d (offset %u), extent <%u, %u>\n
%s is not a character device
Invalid index key
Invalid file name
Invalid file clump size
B-tree node is split across extents (file id %u)
CheckPhysicalMatch: Out of memory!\n
\tinvalid VHB allocationFile.clumpSize \n
ReadFrstate.debugLength != fragSize)\n
hfs_swap_HFSPlusBTInternalNode: attr key #%d offset too big (0x%04X)\n
\t%s - repair failed for type 0x%02X %d \n
%s: Deleting extent overflow for fileID=%u, forkType=%u, startBlock=%u\n
\tinvalid primary wrapper MDB \n
Invalid map node linkage
Symlink for file id %u has bad data length\n
Hard Link catalog entry %u has bad time %u (should be %u, or at least %u)\n
  q = quick check returns clean, dirty, or failure \n
  y = assume a yes response \n
Checking catalog file.
Invalid map node
Invalid root directory count
\tData out of range for block_list_header\n
hfs_swap_HFSBTInternalNode: catalog record #%d keyLength=%u expected=%u\n
\tinvalid MDB drAlBlSt \n
\tinvalid MDB drVolBkUp \n
fsck_hfs: fstat %s
  f = force fsck even if clean (preen only) \n
  %s\n
Bad symbolic link is `%s'
Non-empty journal:  start = %lld, end = %lld\n
hfs_swap_HFSBTInternalNode: invalid record offset (0x%04X)\n
\tcould not get volume block %d, err %d \n
Invalid number of allocation blocks
Incorrect number of thread records
Invalid first link in hard link chain (id = %u)
fsck_hfs
Expected map node, got type %d\n
\tinvalid MDB drClpSiz \n
%s invalid block size %d\n
Checking Journaled HFS Plus volume.
hash table full (%d entries) \n
hfs_swap_HFSPlusBTInternalNode: extents key #%d offset too big (0x%04X)\n
hfs_swap_HFSBTInternalNode: catalog folder record #%d too big\n
UpdFolderCount:  ReplaceBTreeRecord failed (%d)\n
\tinvalid VHB createDate \n
Can't stat root\n
directory
Invalid volume free block count
UpdFolderCount: second SearchBTreeRecord failed (thread.parentID = %u, result = %d), just returning without complaint\n
UpdateExtentInAttributeBT
File/folder %s could not be repaired.
BT map too short during repair
%s: jnl: %s: open: bad jhdr size (%d) \n
%s: Tried to read JIB, got %zd\n
Can't stat %s: %s\n
Invalid B-tree node size
INTERNAL ERROR: GOT TO reply()
%ld\n
parameters
%d %%
Rebuilding extents overflow B-tree.
%s:  %u blocks free, but need %u; ignoring for now\n
\tBlock %qd is not an MDB or Volume Header \n
\tinvalid VHB nextAllocation \n
  m arg = octal mode used when creating lost+found directory \n
fsckPrint
FAIL
Invalid catalog record length
Orphaned file hard link (id = %u)
Got a non I/O error reading disk at offset %llu:  %s\n
  p = just fix normal inconsistencies \n
volumename
\t</dict>\n
Repairing volume.
The volume %s could not be verified completely and can not be repaired.
Cannot create links to all corrupt files
%s(%d):  curNodeNum is 0\n
SearchTree
i28@?0^v8i16*20
\tIncorrect linkCount for inode=%u (expected=%u, found=%u)\n
%08x 
%02X 
%s is not a character device\n
Volume header needs minor repair
hfs_swap_BTNode: offsets %d and %d out of order (0x%04X, 0x%04X)\n
hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d too big\n
Repair Catalog File
\tinvalid MDB drDirCnt \n
Node:\n
Checking volume bitmap.
Invalid record count
Disk full error
\t%s: fileThreads = %u, filesWithThread = %u\n
\tinvalid alternate MDB at %qd result %d \n
\tinvalid last leaf node - calculated %d header %d \n
%s: unknown btree rebuild code `%c' (%#x)\n
Detected a case-sensitive volume.
Incorrect flags for directory hard link (id = %u)
Journal needs to be replayed but volume is read-only
journalRead
Trimmed %u allocation blocks.\n
Trimming unused blocks.
Invalid BTH length
Catalog file entry not found for extent
Volume bitmap needs repair for under-allocation
Invalid parent for file inode (id = %u)
%s:  Invalid journal checksum from %s\n
%s(%d):  wrong kind of node\n
.HFS+ Private Directory Data\r
BlockFindAll
\tduplicate name is 0x
\tvolume type is embedded HFS+ \n
Scanning offset %lld\n
\t<dict>\n
(It should be %s instead of %s)
hfs_swap_HFSPlusBTInternalNode: unrecognized catalog record type (0x%04X; record #%d)\n
%s: Device block size was not initialized by user\n
$Allocation_Bitmap_File\n
\t\t<key>%s</key> <integer>%s</integer>\n
Illegal name
1
External Journal device\n
\tvolume allocation block count %d \n
Problem: b-tree key for \"HFS+ Private Data\" directory is out of order.\n
Physical block size is not a power of 2\n
Invalid parent CName in thread record
Invalid extent file PEOF
File thread flag not set in file record
Incorrect owner flags for directory hard link (id = %u)
Hard link record has data extents (id = %u)
%#x
\textentType=0x%x, startBlock=0x%x, blockCount=0x%x, attrName=%s\n
\tinvalid MDB drLsMod \n
Invalid volume file count
Bad hard link creation date
fsck_hfs completed at %s\n
hfs_UNswap_BTNode: offsets %d and %d out of order (0x%04X, 0x%04X)\n
%lu
BuildAttributeKey
\tinvalid free nodes - calculated %d header %d \n
%s: missing special-device\n
\tdirlink: fdType = 0x%08lx, fdCreator = 0x%08lx\n
hash: overwriting data! (old:%u, new:%u)\n
hfs_swap_BTNode: initial record at bad offset (0x%04X)\n
\tUpdFolderCount: first SearchBTreeRecord failed, parid = %u, result = %d\n
\tinvalid MDB drAtrb \n
TrimFlush: error %d\n
Can't open %s: %s\n
(%c,\"%s\",%d)\n
\tLink reference num=%ld is invalid for inode=%u result=%d\n
%s: Error in updating extent record for fileID = %d (err=%d)\n
%s: Deleting attribute %s for fileID %d, type = %d\n
Can't dup fd for reading on %s: %s\n
  x = XML output mode\n
<plist version=\"1.0\">\n
\t\t\t<integer>%ld</integer>\n
The volume was modified
HardLinkCheckBegin: prime bucket allocation failed\n
\tFixBadFlags (file):  old = %#x, incorrect = %#x, correct = %#x\n
\tinvalid VHB finderInfo \n
QUICKCHECK ONLY; FILESYSTEM CLEAN\n
Master Directory Block needs minor repair
\tPrivate directory for dirlinks not found.  Stopping repairs.\n
hash: duplicate insert! (%d)\n
\t\tAnd we don't care\n
tried to read %zu for journal header buffer, got %zd
%s%u
Bogus Extents File
Can't allocate memory for block list.\n
Invalid allocation block size
\tIncorrect record type for link=%u for inode=%u (expected=2, found=%u)\n
\tCheckExtRecord: id=%u %d:(%u,%u), (blockCount != 0)\n
** %s (NO WRITE ACCESS)\n
File record has hard link chain flag (id = %u)
File has incorrect number of links (id = %u)
iNode
Journal is empty\n
\tfilelink: fdType = 0x%08lx, fdCreator = 0x%08lx\n
Can't rebuilt attributes btree when there is no attributes file\n
\t%s: fileID do not match (threadKey=%u fileRecord=%u), parentID=%u\n
\tprimary MDB is at block %qd 0x%02qx \n
$Catalog_File\n
Invalid BSD file type
\tIncorrect dirinode ID for dirlink=%u (expected=%u, found=%u)\n
(%u,%u) 
Allocation File
** %s (NO WRITE)\n
Invalid directory record length
HFS wrapper volume needs repair
%s(line %d):  height %d != level %d\n
Inline Attribute size %u is larger than maxsize %u\n
%s: Error in copying disk blocks for fileID = %d (err=%d)\n
%s: Error finding attribute record (err=%d) for fileID = %d, attrname = %d\n
CompareXattrPrimeBuckets
\"ROOT_OF_VOLUME%s\" (file id=%u)\n
%llu\n
\tPrivate directory for filelinks not found.  Stopping repairs.\n
\n%s: fsck_hfs started at %s
\tTried to allocate %dK, minimum is %dK\n
\t
hfs_swap_HFSPlusBTInternalNode: catalog key #%d too big\n
\tinvalid MDB drVSeqNum \n
\tinvalid MDB drCTClpSiz \n
TrimFlush: nothing to flush\n
Journal replay simulation succeeded\n
    curNodeNum = %u\n
hfs_swap_HFSBTInternalNode: catalog thread record #%d too big\n
Found (child; node %u):\n
Scanning entire disk for bad blocks\n
VERIFY
Invalid thread record length
Indirect node %d needs link count adjustment
hardLinkCheckBegin:  malloc(%zu) failed\n
Unknown File
(extentInfo->attrname != NULL)
\tInvalid embedded primary volume header at block %qd - error %d \n
%d$@
REPAIR
Checking extents overflow file.
CheckHardLinks:  calloc(1, %zu) failed\n
\t%s: File recordType mismatch for id=%u (found=%u)\n
\tinvalid MDB drVBMSt \n
\tinvalid VHB blockSize \n
ERROR:  output redirected to target volume for live verify.\n
Safe mode and single-user, setting memsize to a maximum of 2gbytes\n
/r
 *****
CheckHFS
fsck_hfs: Volume is journaled.  No checking performed.\n
Unable to allocate %llu bytes for reading symlink
\tError getting first link ID for inode=%u\n
FixBadExtent
%s: Could not replace overflow extents record for fileID %u, fork %u, start block %u\n
%s: No matching catalog thread record found\n
|\n
\tillegal name is 0x
Extents Overflow BTree
\t%s - unknown volume type \n
\tinvalid VHB backupDate \n
Cannot allocate buffer for disk scan.\n
Can't get device block count (%s)\n
\nfsck_hfs started at %s
\tCache size should be multiple of cache block size (currently %uK)\n
id = %u
hfs_UNswap_BTNode: invalid node height (%d)\n
hfs_swap_HFSBTInternalNode: catalog key #%d offset too big (0x%04X)\n
Couldn't read node #%u\n
\tBlock %d is not an MDB or Volume Header \n
\talternate VHB is at block %qd 0x%02qx \n
Fork Data attribute size %u is larger then HFSPlusAttrForkData size %u\n
Expected %d records in node, found %d\n
\tinvalid MDB drVN \n
Invalid node structure
Invalid name for file inode (id = %u)
attrname != NULL
Invalid attribute record
RotateRight: InsertKeyRecord (right) returned false!\n
%s:  found %u blocks but needed %u\n
QUICKCHECK ONLY; FILESYSTEM DIRTY\n
Can't get device block size (%s)\n
Incorrect number of extended attributes
S12@?0S8
lost+found
(%ld, %qd)\n
\tcould not get primary MDB \n
\t%s - volume header total allocation blocks is too small to be valid \n
\tinvalid VHB extentsFile.clumpSize \n
Overlapped extent allocation (id = %u, %s)
BTIterateRecord
hfs_swap_BTNode: offset #%d invalid  (0x%04X) (blockSize 0x%x numRecords %d)\n
UpdFolderCount:  actual record type (%d) != FolderRecord\n
\t\"%s\": fixing mode from %07o to %07o\n
\tinvalid alternate wrapper MDB \n
Unable to get journal file descriptor, journal flags = %#x\n
usage: %s [-b [size] B [path] c [size] e [mode] ESdfglx m [mode] npqruy] special-device\n
\tfilelink prime buckets do not match\n
hfs_swap_HFSPlusBTInternalNode: attr key #%d too big (%d)\n
file
ERROR
Invalid volume directory count
Symbolic link (file id %u) has bad length (is %u, should be %u)
%s:  journal block size %u < min block size %zu for %s\n
\t error %d - could not allocate file ID list \n
hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n
\tInvalid alternate volume header - error %d \n
\t%s - volume header total allocation blocks is greater than device size \n
Node %d's back link is 0x%x; expected 0x%x\n    disk offset = 0x%llx, size = 0x%x\n
%s? no\n\n
\t\t</array>\n
\tinvalid root node - calculated %d header %d \n
\tcheck_loops: Allocation failed for visited list\n
\tvolume headers disagree but there is confusion on which to use \n
Extents File totalBlocks = %u, numABlks = %u\n
Extents:\n
$File_ID_%d\n
DAMAGEINFO
hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n
isHFSPlus == true
\ttotal sectors for volume = %qd 0x%02qx \n
SVerify1.c
** Root file system\n
Incorrect block count for attribute %s of file %s
%s(%p, %p, %zu):  journal buffer wrap count = %d\n
\tData size for block %d out of range for block_list_header\n
%s: %s\n
\tfirst link EA is not inline for dirinode=%u (found=0x%x)\n
FixAttrSize
%ld
\t%s: Unknown record type.\n
\tvolume allocation block count %d device allocation block count %d \n
Got %u errors, maxing out so stopping scan\n
  g = GUI output mode\n
CheckNodesFirstOffset
\tinvalid total nodes - calculated %d header %d \n
kern.safeboot
Rechecking volume.
Missing thread record for root dir
Incorrect flags for file inode (id = %u)
hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d name too big\n
\t\t\t<string>%s</string>\n
GetCatalogRecordByID
hfs_UNswap_BTNode: invalid backward link (0x%08X)\n
%s(%d):  offset is wrong\n
The volume %s could not be verified completely.
Exceeded maximum B-tree depth
pread(%d, %p, %zu, %llu)
i32@?0q8^v16Q24
Searching for key:\n
\tinvalid primary VHB at %qd result %d \n
\tCheckExtRecord: id=%u %d:(%u,%u), (blockCount == 0)\n
\tinvalid VHB rsrcClumpSize (VH=%u, vcb=%u)\n
```
