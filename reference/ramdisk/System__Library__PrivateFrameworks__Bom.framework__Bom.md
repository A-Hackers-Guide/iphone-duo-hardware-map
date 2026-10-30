# `/System/Library/PrivateFrameworks/Bom.framework/Bom`

From the upgrade restore ramdisk (141-29011-104.dmg). 706,912 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2528)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/Bom.framework/Bom (compatibility version 2.0.0, current version 195.0.0)`
- `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression (compatibility version 1.0.0, current version 182.40.4)`
- `/usr/lib/libParallelCompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libarchive.2.dylib (compatibility version 9.0.0, current version 9.2.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,391)

```
Applied xattr com.apple.provenance to %s
Set mtime [%ld.%ld] and atime [%ld.%ld] on %s
fromObj: %s
copy_resources: %s
 discover_resource_attributes: %s
 defer_apple_doubles: %s
Entry created from redirect path %s
destination_path: %s
destination_staging_path: %s
Copy successful
fatal error: %s
Swallowing error
Pushing entry onto the pre-empt stack
Unsequestering __MACOSX entry
Opened segmented file at %s
Applied xattr %s to %s
Applied ACL to %s
Source entry skipped\n
options: %@
copy_extended_attributes: %s
 capture_extended_attributes: %s
Opened data archive from file descriptor
Injecting AppleDouble between segmented files
Synthesized resource fork from %s
Hardlinked %s to %s
copy_acls: %s
Set %s%s%s
%s conflicts with %s
kept old: %s
Retrieving entry from the pre-empt stack
Opened AppleArchive from CFReadStream
Synthesizing AppleDouble replay entry
Synthesizing AppleDouble replay entry from extra AppleDouble entry
Read 0 bytes from deterministic source.
 use_apple_double_suffix: %s
Created file at %s
rename old: %s
 %s
 convert_extra_apple_doubles: %s
Open resource fork at %s
Opened FTS from %s
Ignored AppleDouble
Synthesizing AppleDouble entry
%s [%s]
Filesystem Conflict: The source entry is a Directory but the destination entry is not.
Creating source entry from FTS entry
Consuming AppleDouble entry
Sequestering AppleDouble from %s
Enabled filesystem compression for %s
Set deny bom with destination
 discover_extended_attributes: %s
 discover_acls: %s
Redirected to %s
Deferring AppleDouble entry
Appending suffix %s to %s
Read 0 bytes from non-deterministic source.
Starting copy
Copying source entry to destination set
Source entry retry?\n
destination options: %@
Unlinked %s
Conflicting symlink unlinked
Set enumeration bom with destination
 capture_resource_attributes: %s
 capture_acls: %s
 replay_apple_doubles: %s
 ignore_apple_doubles: %s
fatal file error: %s %d (%s) [%s]
Opened archive from CFReadStream
Synthesizing resource fork entry
Filtering the mode for %s from %s to %s
AppleDouble merge not supported on this filesystem. Unlinking %s
Client cancelled\n
file error: %s %d (%s) [%d]
Retrieving entry from the source
Retrieving entry from the sequester stack
Synthesized AppleDouble from %s
Read %llu total bytes from the source.
Set destination redirect callback
 reorder_extra_files: %s
Consuming __MACOSX directory entry
Merged AppleDouble %s to %s
Source exhausted
source options: %@
Sequestering __MACOSX entry
Changed file flags on %s from %u to %u
Opened data archive from CFReadStream
FTS exhausted
Changed file flags again on %s from %u to %u
Client cancelled
Client skipped source entry
Copy complete but a file error occurred
file error: %s %d (%s) [%u]
Opened AppleArchive from %s
Conflicting symlink followed
rename new: %s
Synthesizing replay AppleDouble from %s to %s
Applied xattr com.apple.rootless to %s
Copy state prepared
toObj: %s
Filesystem Conflict: The source entry is not a Directory but the destination entry is.
 unsequester_apple_doubles: %s
Source path: %s
Could not create FTS entry. Calling error handler
Synthesizing parent entry from FTS root entry
Synthesizing replay symlink entry
kept new: %s
Skipping %s
Retrieving entry from the replay stacks
Marking segmented file entry
Synthesized replay directory from %s
Source entry claims to be compressed but there is no com.apple.decmpfs extended attribute. Assuming zero-length file.
Copying %lu bytes to %s
Opened archive from file descriptor
Opened data archive from %s
Consuming root entry
Consuming extra AppleDouble entry
 synthesize_apple_doubles: %s
Synthesizing replay symlink from %s
 merge_acls: %s
Synthesizing replay directory entry
entry_path: [%s] %s
Retrieving the next source entry
 sequester_apple_doubles: %s
Using an enumeration bom
Created symlink %s -> %s
Skipping copying com.apple.decmpfs until finalization
Set passphrase callback
Set allow bom with destination
Pushing root entry onto the pre-empt stack
Opened archive from %s
Transmogrified symlink: %s to %s
Opened AppleArchive from file descriptor
Source entry copied to destination set\n
Created directory %s
euid: %u egid: %u
Set enumeration bom with source
Could not allocate FTS agent object: %s
BOMCopierDataAnalyzerReset
node_populate_children_traditional
Could not retrieve the entry access time
parse_entry_pkzip_local_header
kBOMCopierSourceOptionReplayDirectoriesKey must be a CFBooleanRef
Could not consume the symlink entry
%s is too large (%luu) to hold a symlink target
Could not read %ld from data decoder
Could not create BOMCopierSourceEntry for replay directory
Unknown BOMCopierSourceEntry
chflags(\"%s\", %u) => %d\n
End of archive
Could not parse CPIO ASCII entry
Could not write to %s: %s
/.BC.T_XXXXXX
can't compute checksum for %s
BOMCopierSourceEntryFree
Could not read from the underlying origin
Could not set the group ID for the directory entry
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/data_archive/data_archive.c
Could not push the extra directory entry onto the replay stack
Could create a regular file entry
verifier: can't make page
Could not read the potential version value
name is NULL
Could not copy metadata from the source entry to its replay apple double
/tmp/.BCDE.%u.T_XXXXXX
Could not AFSC compress %ld bytes: %ld\n
Could not create empty root node
createAppleArchive
symlink
Could not allocate buffer %u: %s
/.BC.D_XXXXXX
BOMCopierSourceEntryNewFromAppleArchive
populate_pkzip_entry
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Storage/BOMStorage.c
Could not parse local header extra field
Could not allocate %ld bytes for name buffer: %s\n
The client did not provide an index bom to use for checksum validation
kBOMCopierSourceOptionDiscoverQuarantine must be a CFBooleanRef
Could not close AFSC stream for %s: %s
%s/%.2s/%.2s/%.2s/%s
arm
Unknown data format: %d
kBOMCopierDestinationOptionUseDefaultDirectoryPermissions must be a CFBooleanRef
Could not create empty ACL for %s: %s
Entry is not a regular file
Invalid bytes to read
Could not create root path tree node
pkzip read seek error: %s
Could not populate source entry from AppleArchive
verify_copier_options
data_stack_push
Could not retrieve extended attribute name for index %u
Could not basename %s: %s\n
fsync
async read thread terminating\n
fts_agent_free
indexbom
./%s/%s
======\nTotal free bytes: %u\n
    Bid: '%s' (%lu bytes)
Could not set POSIX ustar user name attribute
Could not set entry type
BOMCopierSourceSetErrorHandler
kBOMCopierSourceAllowAccessFailuresKey must be a CFBooleanRef
%s: conflict replacing %s with %s
Cannot convert kBOMCopierOptionKeepBinariesPatternKey from options dictionary into UTF8 encoded C string
Intel 80x86
ARM64_32
Could not push child %s of %s onto the stack\n
Could not allocate read buffer: %s\n
Could not create child node for %s\n
D
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopier2.c
BOMBomVerifyBom: bom is NULL.\n
     
./__MACOSX
Could not create empty replay symlink stack
kBOMCopierDestinationOptionEnforceDestinationEncapsulationKey must be a CFBooleanRef
Could not create symlink at %s: %s
kBOMCopierOptionCloneFiles requires the destination to be a filesystem
 i # records: %d\n
Unknown entry type
write_data_libarchive
     leaf   : %d (%d)\n
check_cpio_header
Could not asprintf kept path: %s\n
Out of memory.
Could not read encrypted data
make_path
..
Could not adjust entry path
lzfse
kBOMCopierDestinationOptionApplyProvenanceKey must be a CFDataRef
extra file
Could not resolve path for %s: %s\n
kBOMCopierOptionApplyIndexBomOwnershipKey must be a CFBooleanRef
seek_buffer_size is 0
Improperly formatted field
%d is out of range for kept file balance limit
Could not initialize decompression\n
filesystem object has an invalid type: 0x%X\nCannot dearchive.\n
\tdest:\t%p\n
NUMERICS
Could not parse the regular file
%s is not a directory in the sandbox bom\n
Unsupported flag
readlink(\"%s\", %p, %zu) => %zd\n
Could not consume the source entry
entry_uid
Could not parse the POSIX ustar prefix field
Could not read AppleArchive header: %d
Could not read %ld bytes from source: %s\n
%s\t%d/%d\n
Tree '%s' has an unknown version: 0x%X\n
Could not set POSIX ustar group name attribute
PKZip central directory header
pkzip central directory file comment
Could not constructed adjusted AppleDouble path: %s
Could not get volume state for %s: %s
kBOMCopierDestinationOptionPreserveAppleFSCompression must be a CFBooleanRef
calloc: %s\n
parse_entry_cpio_header_decode
setStaticContent
copy_file_entry_to_destinations
 [BOM]\n
kBOMCopierOptionKeepBinariesListKey is not a CFStringRef
can't convert fallback arch #%d from fallback archs listinto UTF8 encoded C string
Could not get bulk attributes for %s: %s\n
%s%s
entry_size: %lld vs %lld
BOMStorageCopyFromBlockRange: !bid
\ttype:\t%s\n
 i # pages  : %d (%d)\n
Could not enable cpio skip trailer %s
Could not allocate destination name: %s
I was expecting %s not %s
i386
Could not allocate SHA1 context: %s
fstat(%d, %p) => %d\n
Could not inflateEnd: %d
kBOMCopierDestinationOptionAppleFSCompressionType must be a CFNumberRef
F_SINGLE_WRITER 
resolve_filesystem_conflict
kBOMCopierOptionUseHFSPlusCompressionKey must be a CFBooleanRef
Open cancelled
Could not set cpio header attribute
Could not set archive filter: %s
TMPDIR
Cannot get the real path for %s: %s
Could not convert quarantine source path string to C string
injectAppleDoubleBetweenSegmentedFiles
Could not push the extra symlink entry onto the replay stack
Could not set the mode for the regular file entry
Could not write archive entry: %s (%d)
Invalid source_path
Invalid version for POSIX ustar archive
skipbom
Could not allocate empty match record list: %s
discoverSegmentedFiles
BOMCopierDestinationEntryWrite
Could not allocate zero buffer: %s
kBOMCopierDestinationOptionUseAppleFSCompression must be a CFBooleanRef
The legacy engine does not support AppleArchive
Could not parse AppleArchive ACL blob: %d
BOMStorageCopyRangeFromBlockRange: block extends past end of storage
ppc604e
Could not set PKZip ZIP64 end of central directory locator attribute
Could not duplicate %s: %s
setStaticContent is only for filesystem destinations
data_archive_read_entry
copy_entry_metadata
com.apple.provenance
Cannot create parent directory for %s
Could not resolve architecture info for %s
BOMCopierDataAnalyzerUpdate
Could not allocate CRC_32 context: %s
armv7em
Could not get the next source entry
BOMCopierDestinationSetDenyBom
Could not convert kBOMCopierDestinationOptionSegmentFileSizeKey to kCFNumberLongLongType
Could not unlink %s: %s
Could not construct insert entry path: %s\n
Origin %u does not support filesystem cloning
read/write [dirty]
m68030
decompress_streamed_data
PKZip ZIP64 end of central directory locator read
discoverCompressionAttributes
Could not create BOMCopierSourceEntry from FTS entry
Could not copy entry path from the source entry to its replay directory
replay AppleDouble
copy_entry_to_destinations
initialCPIOInode
entry_type: %s vs %s
Could not parse PKZip entry
Could not push the synthetic replay AppleDouble
Could not rename staged %s to %s: %s
copyQuarantine
Could not open %s: %s
Could create a directory entry
extra directory
veo 1
SIMPLE
readdir_r(%s, %s, %s) => %d\n
Size64
pkzip set compression (0,1) error: %s
fts_agent_new
Should not reach here, either
/..namedfork/rsrc
unknown
Could not construct path from %s and %s: %s\n
Symlink object has an invalid version: 0x%X\nCannot dearchive.\n
Could not push current FTS node onto the stack
Could not parse the tar uid field
Could not allocate copy state: %s
hardlink
write_data_filesystem
File object has an invalid version: 0x%X\nCannot dearchive.\n
Could not push parent entry onto the preempty stack
B
If the source is a filesystem, the fromObj argument cannot be nil
rename: %s\n
Storage: open %s (%u blocks)\n
read(%d, %p, %zu) => %zd\n
directory_path is NULL\n
Minimum amount necessary for CPIO name is unavailable
Could not set PKZip ZIP64 end of central directory record attribute
Could not set conflict resolver
bzip2
fsync: %s\n
PKZip extra data
kBOMCopierDestinationOptionCloneFilesKey must be a CFBooleanRef
kBOMCopierDestinationOptionSetSingleWriterKey must be a CFBooleanRef
populate_aa_header_xattr
BOMFREELISTIMPLEMENTATION
0x%02x%02x%02x%02x \"%s\" (%lu bytes)\n
PKZip extra field
Could not push AppleDouble onto the replay stack
Could not merge %s to %s: %s
set_timestamps
BOMCopierCountFilesInArchive: maximum path length exceeded: %ld
kBOMCopierOptionExtractPKZipKey is not a CFBooleanRef
\titerationCount:\t%d\n
Could not set deny bom for destination
Could not close node directory
kBOMCopierSourceOptionSegmentFileSizeKey must be a CFNumberRef
Could not rename kept %s to %s: %s
DITTO2
kBOMCopierOptionSegmentLargeFilesKey is not a CFBooleanRef
Could not allocate SHA224 digest: %s
path is not a UTF8 string
Could not parse the PKZip data descriptor
Invalid BOMCopier\n
ppc7450
Could not construct lookup path for skip bom from %s
kBOMCopierDestinationKeptFileBalanceLimitKey must be a CFNumberRef
Invalid modification_time
kBOMCopierOptionPersistRestrictedFlagsKey must be a CFBooleanRef
useAppleFSCompression
Could not make the kept file directory %s: %s
BOMCopierSourceEntryGetExtendedAttributeCount
\tsource:\t%p\n
arm v7f
chflags
kBOMCopierOptionOutputFileDescriptorKey must be a CFNumberRef
async write thread asked to finish\n
Could not extract PKZip local header from entry
Could not duplicate entry path %s: %s
Could not set AppleArchive path
Could not write the central directory for
Could not get dirname of %s: %s\n
fstatfs(%d, %p) => %d\n
Could not set BOMCopierSource error handler
BOM_CRC32_TYPE
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopierSourceEntry.c
listxattr(\"%s\", \"%s\", %zu, %d) => %zd\n
The destination type has already been assigned to %d
Could not construct target path for %s and %s: %s
kBOMCopierOptionVerifyFileDataPerIndexBomKey is not a CFBooleanRef
Could not allocate xattr value: %s
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Storage/BOMStream.c
Empty stack
Could not close AppleArchive compression stream: %d\n
Could not retrieve actual path for source entry
Cannot get the real path for source '%s'
Could not duplicate file descriptor %s: %s
BOMCopierSourceEntryRead
read_from_origin
sparc
link
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Common/BOMSystemCmds.c
Could not fstat %s: %s
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Common/BOMCRC32.c
Invalid PKZip central directory header signature: %04x
Could not mktemp %s: %s
kBOMCopierOptionKeepBinariesKey is not a CFBooleanRef
readdir_r
can't stat %s: %s\n
can't read %s. skipping...\n
Could not parse the POSIX ustar group name field
Invalid CPIO magic: %lld
PRESERVECOMPRESSION
Cannot specify toObj or kBOMCopierOptionOutputFileDescriptorKey with kBOMCopierOptionOutputCFWriteStreamKey
Could not allocate SHA1 digest: %s
Could not read next data_archive entry: %s
Could not remove saved ACL from %s: %s
SHA224 is not supported
Unsupported AppleArchive compression algorithm
segmentLargeFiles
PKZip archives can only be extracted to filesystem destinations
%s: stream invalid; admin range is outside file\n
CPIO format entry is missing %s attribute
arm64_32
%s is not a directory\n
BOMCopierDataAnalyzerGetDigest
Could not update CRC_32 context: %s
%d 
Could not inflate: %d
Invalid central directory signature
Could not push the synthetic post-order symlink
Could not set F_SETSTATICCONTENT for %s: %s
Could not get name for xattr %u
Invalid data size
Could not retrieve ACL for %s: %s
Invalid passphrase callback
extractDataArchive
BOMCopierDestinationSetDataWrittenCallback
Could not set xattr %s on %s: %s
enforceDestinationLocation
unreadable directory
%s.dittoKeptBinary.%d.%lu
Cannot specify fromObj or kBOMCopierOptionInputFileDescriptorKey with kBOMCopierOptionInputCFReadStreamKey
entry_access_time
    ToC: %u entries (%u bytes)\n
0x%02x%02x%02x%02x (%lu bytes)\n
m88k
/
Could not create empty replay AppleDouble stack
Could not duplicate path %s: %s
Could not allocate MD5 digest: %s
Could not set source redirect callback
async compression enabled for %d\n
fts_agent_open
can't get hardlink data\n
%s\t
Could not read %ld bytes from decoder
deferAppleDoubles
Invalid data_archive
pkzip ZIP64 end of central directory record
synthesize_resource_fork
__MACOSX
BOMCopierDestinationNew
cpio
Could not create AppleArchive encoder\n
Could not set provenance xattr %s: %s
rmdir
Could not create data read stream
maximum path length exceeded: %ld
strlcat(%p, %s, %lu) >= %lu)
BOMCopierDataAnalyzerFinalize
kBOMCopierOptionCreateAppleArchiveKey must be a CFBooleanRef
Could not get destination path
Could not allocate FTS child
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/data_archive/data_archive_decoder.c
Could not parse the tar gid field
Could not consume padding %llu
next_libarchive_entry
Could not get ACL for %s: %s\n
y
nonatomicCopy
Could not read from source entry\n
read called on write-only buffer!\n
Could not parse the CPIO name
?
Could not set archive format: %s
BOMCopierDestinationGetCopyOperation
BOMCopierSourceEntryGetQuarantine
   toc size : %d\n
Could not allocate data stack object: %s
Unable to allocate BOM buffer pool gBOMAsyncBufferSize=%lu gBOMAsyncBufferCount=%u!\n
Invalid key
Could not change file flags on %s from %u to %u: %s. Calling error handler
entry_type
veo
close(%d) => %d\n
kBOMCopierOptionVerifyFileDataPerIndexBomKey must be a CFStringRef
Could not set PKZip end of central directory record attribute
setDataProtectionClass
BOMCopierSourceEntryNewFromResourceFork
Could not constructed entry rsrc path: %s
BOMCOPIER_LOGGING
data_archive_decoder_read_data
enforceDestinationEncapsulation
Cannot convert kBOMCopierOptionEncryptionKey from options dictionary into UTF8 encoded C string
BOMCopierSourceEntryNewFromFSObject
SHA1 is not supported
PowerPC 601
mktemp(\"%s\") => \"%s\"\n
r
TODO: parse extra field
BOMCopierDestinationSetChecksumBom
kBOMCopierDestinationOptionEnforceDestinationLocationKey must be a CFBooleanRef
C
BOMCopierSourceEntryNewFromLibarchive
Could not allocate new_extended_attribute_list: %s
arm64e.x1
synthesize_filesystem_stuff
path_tree_node_create
Could not archive file data (%ld bytes): %s\n
mktemp
kBOMCopierOptionArchitectureArrayKey must be a CFArrayRef
Unrecognized extra field header ID: 0x%04x %d %d
quarantineFilePath
follow
kBOMCopierOptionApplyProvenanceKey must be a CFDataRef
\taddr = %u\n\tsize = %u\n
Could not parse the PKZip ZIP64 end of central directory record
synthesize_replay_symlink
Could not create AppleArchive byte stream at %s\n
BOMCopierDestinationSetInit
Could not allocate error state: %s\n
BOMCopierSourceEntryGetDevice
SPARC
parse_regular_file
Invalid entry
1
kBOMCopierDestinationKeptFileListKey must be a CFStringRef
keptFileBalanceLimit
Could not readlink %s: %s\n
seek_from_origin
    Bid: 0x%08x (%u) '%s' (%lu bytes)
useEnumerationBom
BOMCopierDestinationCreateEntry
Could not skip remaning source entry data\n
verifier: page->next != next->bid
wb
This entry has global extended metadata
kBOMCopierSourceOptionReplaySymlinksKey must be a CFBooleanRef
kBOMCopierDestinationOptionAppleFSCompressionFlags must be a CFNumberRef
Couldn't read pkzip signature.
Could not parse the PKZip file name
The copier source is not configured to use an enumeration bom
kBOMCopierSourceOptionExtractAppleArchiveKey must be a CFReadStreamRef
Could not populate sequester stack
Could not retrieve CRC32 from data analyzer
i486SX
PowerPC 970
parse_entry_pkzip_extra_field_zip64
Could not create data_archive object
Could not basename %s: %s
kBOMCopierOptionUseFilesystemCacheKey is not a CFBooleanRef
Could not allocate xattr name: %s
PowerPC cpusubtype %u
Invalid file descriptor
com.apple.ResourceFork
can't write %s to keepBinariesList: %s
Invalid archive
Could not close FTS agent: %s\n
kBOMCopierOptionCloneFilesKey is not a CFBooleanRef
PKZip local header
parse_entry_pkzip_extra_field_infozip_unix_v1
Could not create archive
lzbitmap
Could not verify copier options
ppc750
The source entry is an unreadable directory
%s/./%s
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopierMatchRecord.c
Invalid data archive entry
getcwd
BOMBomInsertFSObject failed while getting data for '%s' (parentPathID=%u pathID=%u bid=%u)
Could not retrieve the entry modification time
Previous split file path is NULL
Could not create path key for %u %s\n
lz4
useDefaultDirectoryPermissions
Could not write encoded AppleArchive XAT buffer to the destination
kBOMCopierOptionArchitectureArrayKey is not a CFArrayRef
Unresolved path component too large: %ld\n
Could not create BOMCopierSourceEntry from %d
entry_mode: %s vs %s
Invalid FTS agent
SHA384 is not supported
ARM64EX1
lchown
com.apple.rootless
Could not get size for rootless attribute %s: %s
kBOMCopierOptionSkipCPIORootKey is not a CFBooleanRef
pentpro
Could not read next signature
readonly
pkzip data descriptor
Could not set source for read stream: %d
zlib
The source entry is a circular directory
is_root
F_NOCACHE 
Architecture info has an invalid version: 0x%X\nCannot dearchive.\n
arm xscale
injectAppleDouble requires creating a CPIO
Could not write next segment archive entry: %s\n
Could not allocate %lld bytes for parse buffer: %s
i860
The extra buffer is not empty
Could not convert passphrase string to C string
adjust_filesystem_entry_path
outputStream
Cannot compile \"%s\" as a regular expression pattern
Could not allocate blob list: %s
ARM
async write thread terminated. Draining FIFO...
Unrecognize tar type flag value: %c
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/FSObject/BOMFSOTypeInfo.c
write
rmdir(\"%s\") => %d\n
Could not parse the POSIX ustar padding field
Could not mkdir %s: %s
skipCPIORoot
update_data_analyzer
Could not parse the client options
PKZip file comment
Invalid read handler
%s is not a Tree\n
Could not copy metadata from the source entry to its replay directory
Could not set AppleArchive mode
kBOMCopierOptionExtractCPIOKey is not a CFBooleanRef
can't read from %s\n
pentium4
Could not get last path component
Could not seek to beginning of matching slice\n
Could not read %s
Item %d from architecture list is not a CFString
Could not allocate BOMCopierArchRecord: %s
Could not get AppleArchive inode: %d
\tsourceOffset:\t%lld\n
.
createCPIO
BOMCopierSourceEntryClone
Could not read %ld bytes from file descriptor: %s
open
access(\"%s\", %d) => %d\n
The agent has not opened a path to traverse
gzip
async read thread starting\n
Tree: %s\n
Could not parse the PKZip entry
pkzip extra field InfoZIP UNIX v3
Could not create insert entry path
Could not read parse AppleArchive XAT blob: %d
Could not allocate empty BOMCopierDestination
kBOMCopierOptionKeepBinariesKey must be a CFBooleanRef
I do not support contiguous files
kBOMCopierDestinationOptionUseFilesystemCacheKey must be a CFBooleanRef
Invalid num_bytes
Could not set name attribute
%s: Not a directory
Could not statfs %s: %s\n
kBOMCopierOptionInputCFReadStreamKey must be a CFReadStream
can't set path info for %s.\n
kBOMCopierSourceOptionAppleDoubleCaptureExtendedAttributesKey must be a CFBooleanRef
Could not set mode for entry %s
parse_entry_pkzip_zip64_end_of_central_directory_locator
keepBinaries
entry_symlink_target
BOMCopierDestinationSetAllowBom
kBOMCopierDestinationOptionOutputToNowhereKey must be a CFBooleanRef
kBOMCopierOptionZlibCompressionLevel is not a CFNumberRef
entry_name
parse_entry_cpio_padding
Could not open AppleArchive byte stream from file descriptor
can't stat %s (%s)\n
parse_entry_posix_ustar_extended_metadata
Could not skip source entry
kBOMCopierDestinationKeepFilePatternKey must be a CFStringRef
kBOMCopierOptionPreserveHFSPlusCompressionKey is not a CFBooleanRef
kBOMCopierOptionEncryptionKey is not a CFStringRef
missing tree page
data_stack_free
kBOMCopierSourceOptionUseEnumerationBomKey must be a CFBooleanRef
setSingleWriter
%s is too large: %ld
Could not getxattr size for %s: %s
removexattr
data_stack_pop
Could not create BOMCopierDataAnalyzer
The entry path is empty
kBOMCopierOptionEnforceDestinationEncapsulationKey is not a CFBooleanRef
Can't open trace file
     branch : %d (%d)\n
parse_entry_cpio_header
data_archive_open_fd
Could not inflateInit2: %d\n
BOMCopierPrepareMatchContext
invalid key segment: '%s'\n
kBOMCopierOptionCompressAppleArchiveKey must be a CFStringRef
kBOMCopierOptionSetStaticContentKey must be a CFBooleanRef
filesystem object has an invalid version: 0x%X\nCannot dearchive.\n
arm v6
Could not consume %lld bytes of padding
Could not create set entry name for %s
Could not strdup %s: %s
Could not write zeroes to the archive for seeking
%llu\t
(%lu bytes) (NULL)\n
appleDoublesCaptureACLs
kBOMCopierDestinationBalanceKeptFilesKey must be a CFBooleanRef
other_entry
%s\t%o\t%d/%d\t%llu\t%u%s%s%s
\toriginalSourceSize:\t%lld\n
kBOMCopierOptionArchitectureFallbackKey must be a CFDictionaryRef
can't read from %s: %s\n
Could not allocate new FTS node: %s
Could not open directory %s: %s
central header
populate_aa_header
Could not set ACL on %s: %s
kBOMCopierOptionCreateAppleArchiveKey is not a CFBooleanRef
Could not decode AppleArchive XAT data blob
cloneFiles
Could not set AppleArchive symlink path
Could not make the kept file subdirectory %s: %s
Could not getattrlist %s: %s\n
Could not get symlink target from Libarchive entry\n
No method enabled
Invalid value
get_next_entry
error
persistRootless
Could not drain the FTS state\n
_maskWithBom failed while getting data for '%s' (parentPathID=%u pathID=%u bid=%u)
Could not retrieve AppleArchive XAT entry sizes: %d
internal btree error
.%s
Could not create resource fork at %s: %s
parse_entry_posix_ustar_header_decode
Could not allocate discovery buffer: %s\n
dense
kBOMCopierSourceOptionSequesterAppleDoublesKey must be a CFBooleanRef
unsequesterAppleDoubles
Could not asprintf the entry_path: %s
entry_path
parse_apple_archive_blobs
parse_entry_pkzip_extra_field
Could not allocate destination list: %s
Could not update length for CRC_32 POSIX context: %s
armv7s
Could not parse the PKZip file comment
parse_entry_pkzip_digital_signature
kBOMCopierSourceOptionReorderExtraEntriesKey must be a CFBooleanRef
getxattr(\"%s\", \"%s\", %p, %zu, %u, %d) => %zd\n
Could not set adjusted path %s: %s
keptFileList
Could not clone source entry to %s: %s
kBOMCopierOptionDestinationOptionsDictionaryKey is not a CFDictionaryRef
BOMStorageCopyRangeFromBlockRange: 32-bit overflow with block address+size
Could not set timestamps on destination entry
Cannot convert indexbom from options dictionary into UTF8 encoded C string
Could not create BOMCopierSourceEntry for regular file
BOMStorageCopyRangeFromBlockRange: bad block address
lseek(%d, %lld, %d) => %lld\n
close_stack
directory_get_next_child
Could not convert the kept file balance limit to kCFNumberSInt32Type
Could not copy xattr %u
%06s%06ho%06ho%06ho%06ho%06ho%06ho%06ho%011o%06ho%011llo
PowerPC 7400
arm v7em
kBOMCopierOptionSkipCPIOTerminatorKey must be a CFBooleanRef
applyBomOwnership
useHFSPlusCompression
kBOMCopierOptionCloneFiles requires the source to be a filesystem
Could not allocate %ld bytes for kBOMCopierOptionIndexBomKey
Could not close compressor stream: %s
keepFilePattern
kBOMCopierSourceOptionDiscoverBinaries must be a CFBooleanRef
next_data_archive_entry
create_entry_libarchive
Could not set AppleArchive size
file %s is corrupt: slice for %s extends beyond length of file. (%lu > %lld)\n
preserveAppleFSCompression
Could not enumerate %s: %s
Could not parse the Mach-O architectures to copy
populate_posix_ustar_entry
PowerPC 750
kBOMCopierOptionIndexBomKey must be a CFStringRef
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Common/BOMFile.c
Could not allocate %ld bytes for PKZip ZIP64 central directory locator: %s
applySourcePermissions
BOMStorageCopyFromBlock: !storage
Node %u:\n
Checksum mismatch for %s: %d vs %d
BOMCopierDestinationEntryGetType
Could not allocate attribute buffer: %s
Could not chown %s to %d:%d: %s
parse_apple_archive_xat_blob
\"%s\" (%lu bytes)\n
setxattr
CFNumberCreate: %s\n
Could not open the origin
source entry has no actual path
Could not initialize BOMCopierDataAnalyzer
Could not close AppleArchive decoder: %d\n
kBOMCopierSourceOptionExcludeRootDirectoryKey must be a CFBooleanRef
com.apple.decmpfs
kBOMCopierOptionInputFileDescriptorKey is not a CFNumberRef
Could not capture extended attributes
entry_name is too long
resolve_path
passphrase
Could not get status time for entry %s
kBOMCopierDestinationOptionSymlinkTreatmentKey is not a CFStringRef
create_entry_filesystem
Could not realpath %s %d: %s\n
%s has an unknown version: 0x%X\n
arm v4t
Could not fstatat %s: %s
kBOMCopierOptionRemoveExecutablePermissionsKey is not a CFBooleanRef
entry_size
kBOMCopierOptionSetSingleWriterKey must be a CFBooleanRef
yes
Could not disable __MACOSX support\n
Could not archive_write_open_filename %s: %s\n
Could not lookup %s in checksum bom
Could not create directory at %s: %s
kBOMCopierOptionInputCFReadStreamKey is not a CFReadStreamRef
CFDataCreate: %s\n
pkzip ZIP64 end of central directory locator
Could not set PKZip compression level %s: %s (%d)
kBOMCopierOptionCopyResourcesKey is not a CFBooleanRef
entry_gid: %d vs %d
m68k
 i data size: %zd\n
Could not advance to the magic offset
Could not duplicate entry path: %s
Could not convert kept_file_directory string to C string
Could not get xattr name for index %d
Could not create fatal message: %s\n
%s: stream invalid; toc range is outside file\n
name '%s' is > %d\n
TRAILER!!!
populate_aa_header_acl
kBOMCopierOptionSetSingleWriterKey is not a CFBooleanRef
read
utimes
._
Could not dirname %s: %s
Timed out waiting for the read stream to open
Not enough fields
Could not create empty parent node
Could not read directory
Could not skip the ZIP64 central dir locator.
kBOMCopierSourceOptionSkipRootDirectoryKey must be a CFBooleanRef
DeleteOnFree
Could not unsequester AppleDouble file
removeSetuidPermissions
Could not construct atomic template path from %s and %s: %s
%lu
kBOMCopierOptionUseFilesystemCacheKey must be a CFBooleanRef
Could not create empty bom\n
kBOMCopierSourceOptionReplayAppleDoublesKey must be a CFBooleanRef
hfsPlusCompressionOptions
Could not get AppleArchive nlink: %d
Could not allocate node
Could not construct path to resolve: %s %s %ld\n
stat
CRC32 POSIX is not supported
BOMCOPIER_LOG_OPTION_RESULTS
No input file descriptor\n
Could not get source entry modification time
Could not initialize BOM CRC32 state
path_tree_node_push
ppc970
kBOMCopierOptionSkipBomKey must be a CFStringRef
kBOMCopierOptionSkipCPIORootKey must be a CFBooleanRef
PKZip data descriptor
libarchiveFilter
unable to reserve block %d.\n
BOMCopierDestinationEntrySeek
Could not get size for xattr %u
armv7k
num_bytes is 0
Could not convert the format number to kCFNumberSInt32Type
Cannot thin the index bom
pkzip local header
Invalid PKZip archive digital signature signature: %04x
compress
Could not allocate parent path buffer: %s\n
synthesize_replay_directory
Could not allocate %ld bytes for skip buffer: %s\n
Minimum amount necessary for CPIO header is unavailable
file
ppc603e
data_archive_open
appleDoublesCaptureExtendedAttributes
push_preempt_stack
async read thread finished file\n
parent directory %s does not exist\n
kBOMCopierOptionKeepBinariesListKey must be a CFStringRef
Bytes don't match
name
PKZip file name
PKZip archive extra data
enableAtomicCopies
Could not seek forward in the origin
ppc603
Invalid rewind buffer
Invalid bytes to rewind
Could not reset POSIX ustar name attribute
Could not extract PKZip central directory header from entry
Could not apply retention policy
Cannot write the terminator for the CPIO archive
/.
Could not retrieve path from fso\n
Could not create byte stream
copier_source->aa_decoder is NULL
kBOMCopierDestinationOptionCreateArchiveKey must be a CFBooleanRef
%lu\t
BOMStreamReadAddress: bad buffer type!\n
Big Endian
CFDictionaryCreateMutable: %s\n
Could not set timestamp
Could not allocate empty BOMCopierSource
Could not copy metadata from the source entry to its directory doppleganger
Could not compile regular expression from %s: %s
persistRestrictedFlags
Couldn't read pkzip local header
Could not resolve the path: %s
synthesize_inject_apple_double
<memory>
Could not allocate SHA224 context: %s
Could not duplicate node path
replayQuarantineFromPath
libarchiveFormat
Could not get source entry status time
Could not resolve family architecture info for %s
Unknown deprecated compression option
index %d is out of range
zipFileEncryptionKey
Item %d from architecture list could not converted to a UTF8 string
waiting for async write thread to finish...
appleDoublesCaptureResourceAttributes
replaySymlinks
%d
BOMCopierDestinationEntryGetPath
Timed out waiting for the write stream to open
Could not check for a tar POSIX header
vm_allocate failed
Could not create AppleArchive header
Could not create AppleArchive XAT blob
finalize_entry_filesystem
        %s (%u entries)\n
Unknown data entry type
%p {%d}
**** WARNING **** Can't compile pattern: %s\n
fts_read: %s\n
entry_status_time
decrypt_data
Could not create parent path
compressAppleArchive
kBOMCopierOptionOutputFileDescriptorKey is not a CFNumberRef
can't read arch #%d from archs list
btree cache is deadlocked
can't read path of size %d: %s\n
passphrase_callback
Not enough data remaining (%ld) for %s (%ld)
init_pkzip_cipher
%lu + %p - %p > %d
BOMBomNewFromDirectory_parallel
add_sequester_entry_block_invoke
allowAccessFailures
x86_64h
Could not set EoA entry type
source_entry
BOMStorageCopyFromBlock: !bid
kBOMCopierOptionSegmentLargeFilesKey must be a CFBooleanRef
seek_filesystem
kBOMCopierOptionSourceIsAppSandboxed is not a CFBooleanRef
arm v7m
Could not create parent element: %s\n
data_archive_decoder_set_stream
Minimum amount necessary for POSIX ustar header is unavailable
Invalid PKZip archive extra signature: %04x
kBOMCopierSourceOptionReplayExtraAppleDoubleEntriesKey must be a CFBooleanRef
BOMCopierDestinationSetFinalizationCallback
Could not allocate provenance data buffer
Could not encode ACL
kBOMCopierDestinationOptionOutputFileDescriptorKey must be a CFBooleanRef
%s is not a regular file
setSingleWriter is only for filesystem destinations
Could not create BOMCopierSourceEntry for type %d
Could not allocate MD5 context: %s
arm v7k
setxattr(\"%s\", \"%s\", %p, %zu, %u, %d) => %d\n
    %s\n
BOMBomVerifyBom: count is wrong.\n
Could not set extended timestamp
Could not inflateInit2: %d
Could not enable read support for all filter types
Could not get next FTS agent entry: %s
If the destination is a filesystem, the toObj argument cannot be nil
%d/%d
Could not duplicate child name: %s
Could not set POSIX ustar header attribute
Could not match the binary
xscale
Could not create source options
character device
Invalid arch_record
entry_path is too long
_BOMCopyStepCopy
data_archive_decoder_read_entry
Could not open the archive %d for reading: %s
Could not write to AppleArchive: %u
Could not parse AppleArchive payload blobs
Large sizes: %d entr%s\n
Could not create error path: %s
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Bom/BOMFSEnumerator.c
Could not set AppleArchive uid
Could not allocate copy buffer of %ld bytes: %s\n
lseek: %s\n
armv8
Could not parse the tar version field
verifyFileDataPerIndexBom
populate_pkzip_entry_central_directory_header
filter_next_source_entry
kBOMCopierDestinationOptionCreateAppleArchiveKey must be a CFBooleanRef
utimes(\"%s\") => %d\n
kBOMCopierOptionEncryptionKey must be a CFStringRef
Could not allocate %ld bytes for PKZip central directory header: %s
check_filesystem_conflict
Could not push synthetic AppleDouble entry
Could not parse the options dictionary
Could not create error message: %s\n
Implementation
kBOMCopierOptionKeepBinariesDirKey must be a CFStringRef
pkzip extra field ZIP64
Could not allocate target buffer %lu: %s
Could not create platform toolbox\n
Could not create archive object
Could not create destination entry
Could not prepare binary matching context
size is 0
populate_source_entry_from_apple_archive
BOMStorageCopyFromBlockRange: !storage
Can't allocate data for free list
populate_read_buffer
discoverQuarantine
PowerPC 64-bit
Could not create parse copier options
kBOMCopierOptionKeepParentKey must be a CFBooleanRef
kBOMCopierDestinationOptionSetStaticContentKey must be a CFBooleanRef
Could not get AppleArchive size: %d
Invalid PKZip local header signature: %04x
Could not set ZIP64
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/data_archive/fts_agent.c
can't archive %s. skipping...\n
can't get arch info for '%s'
Could not rewind remaining data: %d
kBOMCopierSourceOptionEnforceArchiveEntryPermissionsKey must be a CFBooleanRef
Could not setattrlist timestamps for %s: %s
Could not chmod %s: %s
BOMCopierSourceEntryNewFromPath
copier_source->archive is NULL
%s.tv_sec: %ld vs %ld
Could not get path for redirected source entry
Paths
Could not archive fso for %s\n
Could not unlink placeholder at %s: %s
acl_text_size is NULL
Could not get AppleArchive uid: %d
armv7f
%s is too long\n
%d is out of range for Zlib compression
Invalid fso
kBOMCopierOptionPreserveRestrictedFlagsKey is not a CFBooleanRef
fallbackForSubtype
Could not skip remaining AppleArchive file data
useFilesystemCache
keepBinariesList
message_digest is NULL
Architecture Independent
POSIX ustar group name
synthesize_apple_double
posix
Missing symlink target for %s
sequesterResources is only for PKZip archives
<unknown>
Could not create CFNumber from %d
keptFileDirectory
The source entry is unknown
copy_binary_entry_to_destinations
kBOMCopierOptionCopyACLsKey must be a CFBooleanRef
Could not close nodes on the stack
Could not get the global queue\n
Invalid magic for POSIX ustar archive
unlink
cpio header
w
%s is empty: Unrecognized archive format
kBOMCopierDestinationPreserveRestrictedFlags must be a CFBooleanRef
Could not create regular file at %s: %s
Could not initialize BOM CRC32 state\n
Could not allocate %ld bytes for PKZip ZIP64 central directory header: %s
kBOMCopierDestinationOptionLibarchiveFormatKey must be a CFNumberRef
kBOMCopierDestinationOptionZlibCompressionLevel must be a CFNumberRef
Could not set F_SINGLE_WRITER for %s: %s
kBOMCopierOptionKeepBinariesPatternKey is not a CFStringRef
Invalid data_archive_entry
.afpDeleted
The extra buffer is not large enough
Could not allocate attribute buffer: %s\n
Could not reset pkzip entry size
Could not allocate %ld bytes for path_size
Invalid other_entry
arm v5
Could not set the passphrase callback\n
Could create a post order symlink entry
kBOMCopierDestinationOptionApplySourcePermissionsKey must be a CFBooleanRef
\tbuffer:\t%p\n
kBOMCopierOptionApplyIndexBomOwnershipKey is not a CFBooleanRef
Could not duplicate path for redirected source entry
sequesterAppleDoubles
destination_entry->archive is NULL
BOMCopierCopySourceEntryToDestinationSet
Could not read %s %lu: %s
destination path ('%s') too long [%lu >= %lu]!
cpio read error: %s
Could not allocate buffer: %s
Could not drain the final FTS state: %s\n
enforceArchiveEntryPermissions
verifier: next->prev != page->bid
Could not allocate SHA384 context: %s
little
copyfile(\"%s\", \"%s\")\n
The agent is exhausted
end of archive
kBOMCopierOptionSourceOptionsDictionaryKey is not a CFDictionaryRef
i486
copier_source is NULL
Could not match the source binary
Oct  3 2026
\tdestOffset:\t%lld\n
stat(\"%s\", %p) => %d\n
path is too long
PKZip signature
The BOMCopierSource does not have an open FTS agent
chmod
   data size: %zd\n
Invalid buffer
keepBinariesDir
Could not allocate space for Apple Double filename.
bad file format
BOMCopierSourceEntryGetHardlinkCount
Could not allocate %ld bytes for path
init_data_analyzer
\tnumSteps:\t%d\n
BomInfo
Could not parse the tar linkname field
Could not open AppleArchive decompression stream at %s
Could not path for source entry of %s\n
PowerPC 603ev
getxattr
Could not append AA_FIELD_DAT to AppleArchive header: %d
Invalid entry_parent
hppa
next_apple_archive_entry
Concatenated path too large: %s %s %ld\n
prepare_copy_state
kBOMCopierOptionInputFileDescriptorKey must be a CFNumberRef
Could not set path info for %s\n
Invalid data archive
Could not add passphrase: %s\n
Could not open the archive %s for reading: %s
Could not mode for source entry of %s\n
kBOMCopierOptionCopyACLsKey is not a CFBooleanRef
create_node
Could not parse the PKZip digital signature
kBOMCopierSourceOptionDiscoverACLs must be a CFBooleanRef
child_name is NULL
copyResources
tree is read-only\n
Could not set checksum bom for destination
kBOMCopierOptionArchitectureArrayKey is empty
segmentFileSize
Could not set AppleArchive gid
BOMCopierSourceSetEnumerationBom
BOMCopierDestinationFinalizeEntry
%s/%c%c/%c%c/%c%c/%s
BOMCopierSourceEntryNewFromDataArchive
LEGACY
POSIX ustar extended metadata string length %lu does not match expected size %lu
Could not allocate path to resolve\n
any
The password appears to be invalid and the client did not provide a callback for retrieving a new PKZip encryption key
name %s already exists!\n
 %02x
%02x
Motorola 88K
BOMCopier
Could not get entry for hardlink node\n
   bt size  : %d\n
Could not set allow bom for destination
Unrecognized uid size: %d
Could not parse the PKZip Info-ZIP UNIX v3
Could not copy metadata from the symlink entry to its replay symlink
copier_destination is NULL
Could not finalize data analyzer
Could not set the mode for the directory entry
kBOMCopierOptionUseHFSPlusCompressionKey is not a CFBooleanRef
POSIX ustar extended metadata
Could not prepare archive source
symlinkTreatment
entry_uid: %d vs %d
Could not get entry path for source entry
Could not make the parent_path %s
Could not allocate copy target list: %s
finalize_entry_apple_archive
source path ('%s') too long [%lu >= %lu]!
Could not stat %s: %s
match_binary
ies
fdesc
Intel Pentium 4
Could not set BOMCopierSource passphrase callback
fts_agent_read
Could not open AppleArchive byte stream at %s
Could not construct filesystem destinations
can't open %s for reading: %s\n
Could not close AppleArchive decompression stream: %d\n
Could not allocate %ld bytes for passphrase_size
synthesize_replay_apple_double
BOMCopierDestinationEntryGetMatchRecordCount
mmap: %s\n
fsync(%d) => %d\n
can't set new path value\n
size
Could not read %ld bytes from data_archive: %s
x86_64
kBOMCopierOptionSourceIsAppSandboxed must be a CFBooleanRef
Invalid decoder?
read_data_direct
can't access symlink for %s
lseek
access
kBOMCopierDestinationOptionRemoveSetuidPermissionsKey must be a CFBooleanRef
\n
Intel Pentium
parse_entry_pkzip_extra_field_ntfs
Could not statfs %s: %s
kBOMCopierSourceOptionDiscoverResourceAttribute must be a CFBooleanRef
kBOMCopierOptionIndexBomKey is not a CFStringRef
Invalid entry_name
no
Could not convert ACL to text for %s: %s
sequester_apple_double
zero_buffer is NULL
SkipTerminator is only used for CPIO archives
Invalid compare_handler
POSIX ustar format entry is missing %s attribute
Unknown free list manager. Aborting
Could not open the archive_read_open2 for reading: %s
Could not set appended entry path for AppleDouble file
compressCPIO
data_archive_read_data
node_populate_children_bulk
Actual name length doesn't match expected value\n
pkzip end of central directory record
Could not copy quarantined directory path.
Could not finalize AppleArchive entry
Could not create hardlink %s to %s: %s
Could not finish the HFS FinishStreamCompressorQueue error (%d)
entry_resolved_path
Could not create parent from FTS entry
kBOMCopierDestinationKeptFileDirectoryKey must be a CFStringRef
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/FSObject/BOMFSOArchInfo.c
Step %d:\n
Device object has an invalid version: 0x%X\nCannot dearchive.\n
kBOMCopierOptionInitialCPIOInodeRootKey must be a CFNumberRef
Cannot convert %u to replay entry
Could not copy attribute value for index %d: %s\n
Could not get current working directory: %s\n
Invalid seek_amount
Could not get field type from AppleArchive header index %u: %d
Unknown archive format
Could not get the root fso for the enumeration bom
CFReadStream is not open
can't set file data\n
Could not read additional %ld bytes onto read buffer: %s\n
Could not seek to the end of %s: %s
seek_apple_archive
Missing entry_path
Intel 80586
kBOMCopierOptionCopyQuarantineKey must be a CFStringRef
Could not read next decoder entry
write_data_apple_archive
Unsupported format: %d
PowerPC 603
Could not lookup %s in sandbox bom\n
Could not decode CPIO header
i20@?0r*8B16
Could not create last path component
post order directory
Could not convert kBOMCopierOptionIndexBomKey to UTF8 C string
data_archive_set_passphrase_callback
initialInode
kBOMCopierOptionHFSPlusCompressionOptionsDictionaryKey is not a CFDictionaryRef
BOMStorageCopyToBlockRange: length extends beyond block size
v8@?0
kBOMCopierDestinationOptionSetDataProtectionClassKey must be a CFStringRef
Could not duplicate %s: %s\n
entry_parent
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopierDataAnalyzer.c
dense+trace
pkzip extra field extended timestamp
Could not close archive %s\n
statfs(\"%s\", %p) => %d\n
Could not create ParallelCompression AFSC stream for %s: %s
Can't find . in bom file
Could not access %s: %s\n
parse_entry_pkzip_extra_field_infozip_unix_v3
crossDevices
Motorola 68040
seek_libarchive
check_tar_posix_header
Could not create AppleArchive compression stream\n
BOMCopierSourceEntryCopyExtendedAttribute
ARM64E
Could not release node stack
parse_entry_pkzip
kBOMCopierSourceOptionReplayQuarantineFromPath must be a CFBooleanRef
Could not finalize filesystem entry
The agent has already opened a path to traverse
   i branch : %d (%d)\n
padding amount %lld is larger than buffer %lld
next_enumeration_bom_entry
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopierDestination.c
[not an array]\n
Invalid format entry
Unknown GP_CRC_TYPE: %s\n
DALLAS: string_length = %lu\n
synthesizeAppleDoubles
Cannot convert kBOMCopierOptionKeepBinariesListKey from options dictionary into UTF8 encoded C string
Attempting to destroy a non-empty FIFO!
%d\t%d\t%s\n
BOMCopierSourceEntryNewFromFTSENT
%s: stream invalid; overflow of admin offset+size\n
BOMStorageCopyRangeFromBlockRange: reading from free block
PowerPC 604e
%ld bytes remaining after parsing %s extra field
BOMCopierMatchBinary
_BOMCopyStepCopyToEndOfSource
Can't allocate free list
Could not open FTS agent: %s\n
Invalid data source
Could not BZ2_bzDecompress: %d\n
rename(\"%s\", \"%s\") => %d\n
Invalid path
xtra
VIndex
unknown stream type: %d\n
Could not chmod relay directory %s to %s: %s
kBOMCopierSourceOptionDisableLexicographicSortKey must be a CFBooleanRef
Could not convert kBOMCopierDestinationOptionInitialInodeKey to kCFNumberLongLongType
kBOMCopierOptionSetDataProtectionClassKey must be a CFStringRef
BOMCopierSourceEntryGetInode
%s/
wstream
vm_copy failed
\tcopier:\t%p\n
Could not reallocate new children list\n
Could not read %lu bytes from non-deterministic source
Could not resolve %s
Invalid FTS entry
size + position are out of range
close
PowerPC 604
parse_entry_pkzip_end_of_central_directory_record
whiteout
Filename('%s') too long [%lu >= %lu]!
armv7m
finalize_data_analyzer
libarchiveReadBlockSize
Could not create BOMCopierSource from %s: %s
kBOMCopierOptionCreateCPIOKey is not a CFBooleanRef
Could not get symlink target from fso\n
Could not seek to the end of the source entry\n
can't get temp file.\n
   fl size  : %d\n
CompressionTypes must be a CFNumberRef
Could not create empty hardlink table\n
vm_deallocate failed
ProjectToPathTree
The client did not provide an index bom to use for enumeration
Could not set NTFS extra field
keepParent
seek_buffer is NULL
Could not seek %ld bytes to beginning of new slice
Could not allocate %ld bytes for cpio_header: %s
BOMCopierDestinationEntrySkipped
Could not write encoded AppleArchive ACL buffer to the destination
kBOMCopierOptionKeepParentKey is not a CFBooleanRef
   # blocks : %d\n
Could not populate the read buffer
Could not allocate %ld bytes: %s
Could not dirname_r %s: %s
Could not create BOMCopierDestination
kBOMCopierOptionCompressCPIOKey must be a CFBooleanRef or CFStringRef
Could not create BOMFSObject for %s\n
chdir: %s\n
 i key size : %zd\n
Could not update data analyzer
lzma
kBOMCopierOptionSkipCPIOTerminatorKey is not a CFBooleanRef
Could not allocate unresolved prefix\n
Could not parse the PKZip local header
Could not allocate zlib stream: %s
kBOMCopierSourceOptionCrossDevicesKey must be a CFBooleanRef
.BCD.T_XXXXXX
%s/%s.dittoKeptBinary.%d.%lu
Could not read %lu bytes from source
munmap
Could not lchmod %s %s to %s: %s
kBOMCopierOptionSymlinkTreatmentKey must be a CFStringRef
I expect path to be NULL for nowhere destinations
none
BOM_ASYNC
Could not skip the end of the central directory record.
NULL error
Could not parse the PKZip ZIP64 extra block
PKZip end of central directory read
Could not duplicate fso_path %s: %s\n
Could not listxattr %s: %s
ProjectTagTable
Could not create empty data format entry
Could not parse the PKZip NTFS extra field
Could not write fat header\n
Could not skip the digital signature.
closedir(%s) => %d\n
Could not retrieve entry path for AppleDouble entry
ppc603ev
write(%d, %p, %zu) => %zd\n
Could not allocate libarchive buffer: %s
Could not set the entry path
Could not allocate empty destination entry: %s
Unexpected post order entry type: %u
Invalid data
Intel Pentium II Model 5
Could not request password from client
Could not readlinkat %s: %s
Could not parse the POSIX ustar devminor field
kBOMCopierSourceOptionExtractDataArchiveKey must be a CFBooleanRef
Could not archive_write_open2 %s: %s\n
replay directory
kBOMCopierOptionNonAtomicCopyKey is not a CFBooleanRef
Compression is only used for CPIO archives
bad stream!\n
hardlink group #%d: (%d links)\n
Could not allocate %ld bytes for name buffer: %s
populate_cpio_entry
ppc64
%d/%d\t
Intel 80486SX
Could not copy from %s to %s: %s
Could not create BOMCopierSource
injectAppleDouble requires segment large files
Invalid flags
Could not create empty parent stack\n
Could not sequester AppleDouble entry
Could not write zeroes to AppleArchive: %u
Corresponding fallback entry for item %d from architecture list is not a CFArray
%s is missing %s
Could not set insert entry path
Could not populate AppleArchive header
enableLogging
can't set path info for %s. skipping...\n
Could not get AppleArchive mode: %d
arm v6m
lstat
Invalid read size
kBOMCopierSourceOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef
Could not set gid for entry %s
kBOMCopierOptionPersistRootlessExtendedAttributesKey is not a CFBooleanRef
Could not get path from AppleArchive: %d
BOMStorageCopyFromBlockRange(storage=%p, bid=%u, location=%u, length=%u, data=%p) failed!
appleDoubleMergeACLs
kBOMCopierOptionOutputCFWriteStreamKey is not a CFWriteStreamRef
Could not constructed resolved rsrc path: %s
%d\t
Motorola 68030
kBOMCopierOptionPreserveHFSPlusCompressionKey must be a CFBooleanRef
read_streamed_data
Unsupported data protection class
The copier source is not BOMCopierSourceIndexBom
discoverExtendedAttributes
%s resolves outside of %s
Could not retrieve modification time
Could not finalize destination entry\n
BOMTree iterator cannot cache keys. This is a fatal error (BOMStorageCopyFromBlock returned an error).\n
Invalid data buffer handle
bom_path is NULL\n
kBOMCopierSourceOptionAppleDoubleCaptureResourceAttributesKey must be a CFBooleanRef
Could not get basename of %s: %s\n
Invalid header
Motorola 68K
pentIIm5
Could not create path value for %u %u\n
Could not enable read support for all format types
extractPKZip
Invalid cloned
write: %s\n
Could not allocate %ld bytes for kept file directory
memory
realloc: %s\n
PackageTagTable
data_archive_open_custom
Unknown compression type
BOMStorageCopyFromBlock: bid > storage->blocks
kBOMCopierSourceOptionSynthesizeResourceForksKey must be a CFBooleanRef
output2Nowhere
Incorrect pkzip signature
pentIIm3
mkdir(\"%s\", %d) => %d\n
Could not allocate zlib stream: %s\n
copyExtendedAttributes
fstat: %s\n
write called on read-only buffer!\n
MD5 is not supported
cpio entry name
replayExtraAppleDoubles
Could not set the path for the post order symlink entry
parse_copier_destination_options
%o\t
data_archive_decoder_rewind_data
Could not set rootless xattr %s: %s
Couldn't read PKZip signature
BOMCopierSourceEntrySkip
No passphrase callback
The BOMCopierSource does not have an index bom enumerator
balanceKeptFiles
Cannot create CPIO file at %s
Could not get AppleArchive data size: %d
%s\t%o\t%d/%d\n
closedir
Could not set entry name
Could not F_NOCACHE %s: %s\n
%s%06ho%06ho%06ho%06ho%06ho%06ho%06ho%011o%06ho%011llo
Could not parse the tar name field
local header
kBOMCopierSourceOptionIgnoreAppleDoubles must be a CFBooleanRef
Could not get symlink target path: %d
Could not get %s attribute
CRC32 is not supported
armv6
fts_agent_close
parse_entry_posix_ustar
Could not make_path %s: %s
Could not convert ACL text: %s
0x%02x%02x%02x%02x (NULL) (%lu bytes)\n
_copyFilesFromBomToBomInOrder failed while getting data (pid=%u bid=%u)
kBOMCopierSourceOptionAppleDoubleCaptureACLsKey must be a CFBooleanRef
add_sequester_entry
Could not set uid for entry %s
construct_filesystem_destination
copyACLs
persistRootlessEAs
kBOMCopierOptionRemoveSetuidPermissionsKey is not a CFBooleanRef
Could not set modification time for entry %s
Could not resolve filesystem conflict
CFReadStream is not open: %u
  %s\n
mmap
kBOMCopierOptionExtractCPIOKey must be a CFBooleanRef
Could not allocate %ld for read buffer: %s
BOMCopierSourceNew
pkzip set compression (1,1) error: %s
pkzip read span error: %s
Could not read pkzip data descriptor: %s
capture_extended_attributes
realpath
<Tree %d>
Could not set linkname attribute
Could not create AppleArchive byte stream from file descriptor\n
Could not construct destination path from %s: %s
Could not read %ld bytes from source
   key size : %zd\n
Could not create data decoder
synthesizeResourceForks
discoverACLs
next_source_entry
Could not verify the copier options
BOMTree in invalid state - nextNode is NULL!\n
arch
lang
Could not get match record at index %d\n
Cannot open file %s for writing: %s
armv4t
Could not allocate empty _BOMCopierError\n
PKZip archive digital signature
destination_set is NULL
Couldn't read next signature
async read thread finished file (errno=%d)\n
CLEVER
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Bom/BOMBom.c
pkzip extra field NTFS
kBOMCopierDestinationOptionSkipCPIOTerminatorKey must be a CFBooleanRef
Could not lstat resource path for %s: %s
kBOMCopierOptionExtractPKZipKey must be a CFBooleanRef
BOMCopierSourceSetPassphraseCallback
  
Could not get the next entry
   # records: %d\n
kBOMCopierSourceOptionLibarchiveReadBlockSize must be a CFNumberRef
kBOMCopierSourceOptionKeepParent must be a CFBooleanRef
Could not realpath %s: %s
createPKZip
Could not allocate BOMCopierDataAnalyzer: %s
The source type has already been assigned to %d
Could not create BOMHardLinkTable
AppleFSCompressionType
directory cycles
Could not duplicate %s
Improperly formatted input, too many fields
mmap(%p, %zu, %d, %d, %d, %lld) => %p\n
Could not parse the POSIX ustar uname field
PKZip ZIP64 end of central directory read
sourceIsAppSandboxed
BOMCopierSourceEntryGetExtendedAttributeSize
%s is not a BOMStorage file\n
Could not open allow bom at %s
Could not allocate %ld bytes for suffix_size
Could not set the data for the regular file entry
Error reading from CFReadStream
com.apple.FinderInfo
value is NULL
populate_pkzip_entry_local_header
fcntl(%d, %d, %p) => %d\n
Could not set entry file comment
Could not read initial ciphertext: %s
Could not stat the archive %s: %s
BOMCopierDestinationEntryGetMatchType
kBOMCopierDestinationKeepBinariesKey must be a CFBooleanRef
Could not write %ld bytes to destination
kBOMCopierOptionInitialCPIOInodeRootKey is not a CFNumberRef
Could not find a PKZip signature
starting-inode
Could not allocate extended attribute list: %s
Could not allocate SHA384 digest: %s
Could not create AppleArchive decoder
Could not convert enumeration_bom_path string to C string
PKZip local header format entry is missing %s attribute
stream maximum size exceeded: %lu > %lu
Read cancelled
match_record is NULL
Could not update CRC_32 POSIX context: %s
_BOMCopyStepBuffer
%s/._%s
Could not create a BOMPKZip object
BOMCopierSourceEntryGetACL
kBOMCopierOptionRemoveSetuidPermissionsKey must be a CFBooleanRef
xcpt
data_archive_entry_set_format_entry
can't read fallback arch #%d from fallback archs list
reallocf: %s\n
match_context is NULL
read: %s\n
Could not BZ2_bzDecompressInit: %d\n
Could not decode AppleArchive ACL data blob
arm64e
Could not open regular file at %s: %s
ARM64
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Common/BOMBufferManager.c
open(\"%s\", %d, %d) => %d\n
mknod(\"%s\", %d, %d) => %d\n
parse_entry_pkzip_zip64_end_of_central_directory_record
  %s
Could not set kBOMCopierSourceEntryDeleteOnFree option
outputFD
Could not lstat %s: %s
HLIndex
BOMStorageCopyRangeFromBlockRange: length extends beyond block size
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Bom/BOMBomEnumerator.c
hppa7100LC
Could not create node stack
Could not push the synthetic replay directory onto the replay stack
Could not check for a destination conflict for %s
Could not symlink %s to %s: %s
Could not update BOM CRC32 state\n
Invalid PKZip data descriptor signature: %04x
extractAppleArchive
auto
Could not skip the ZIP64 central dir record.
Could not finalize CRC_32 POSIX context: %s
BOMCopierCopyWithOptions2
Could not initialize the PKZip cipher
Could not create BOMCopierSourceEntry for replay AppleDouble file
Size %d: %d entr%s\n
kBOMCopierOptionEnforceDestinationEncapsulationKey must be a CFBooleanRef
Could not parse extended timestamp
kBOMCopierSourceOptionDeferAppleDoublesKey must be a CFBooleanRef
Could not allocate destination parent: %s
Could not get source entry access time
/tmp.XXXXXX
PowerPC
Invalid read buffer
require_minimum_amount
parse_entry_pkzip_data_descriptor
Could not parse central directory header extra field
Item %d from fallback list is not a CFString
parse_entry_pkzip_central_directory_header
internal
Unsupported BOMCopierSourceEntryType: %s
index is out of range
PowerPC 603e
waiting for async read thread to finish...
Could not write AppleArchive header
Empty field in summary
data_stack_new
Unknown value for kBOMCopierOptionSymlinkTreatmentKey
socket
Could not create ACL file path: %s\n
Could not get ACL from source entry
%s\t%d/%d\t%lld\t%05u\t%s\n
Could not set the passphrase callback: %s
data_size is 0
(null)
kBOMCopierOptionCopyResourcesKey must be a CFBooleanRef
Could not allocate read buffer: %s
prepare_archive_source
Could not construct resolved path from %s + %s: %s\n
Could not set finalization callback
kBOMCopierOptionCopyQuarantineKey must be a CFBooleanRef
Could not close FTS agent
No output file descriptor\n
entry_modification_time
Could not allocate CRC_32 POSIX context: %s
Could not archive_write_open_fd %s: %s\n
PowerPC 7450
POSIX ustar header
Could not parse the tar checksum field
replay symlink
Could not create data source
BOMCopierSourceNext
Could not apply AppleArchive ACL blob to %s: %d\n
BOMStorageCopyRangeFromBlockRange: bad block (bid > storage->blocks)
No flag is set.
_BOMCopyStepSeekToEndOfSource
Could not determine kernel version\n
Intel family %u model %u
skipTerminator
Could not get xattr size for index %d: %s
applyIndexBomOwnership
SkipRoot is only used for CPIO archives
applyProvenance is only applicable when extracting from archives
%s PKZip archive
mknod
Could not push synthetic resource fork entry
regular file
kBOMCopierOptionSequesterResourcesKey is not a CFBooleanRef
Unsupported entry type: %u
ppc
PowerPC 970 64-bit
Could not set PKZip central directory header attribute
getattrlist
%s
archs
zlibCompressionLevel
keepParent is only for archives
fstat
kBOMCopierOptionNonAtomicCopyKey must be a CFBooleanRef
pkzip central directory header
Unknown NTFS tag value: %u
Could not create BOMCopierSourceEntry from redirect path %s
Could not synthesize replay symlink
cpio seek error: %s
Could not retrieve item %d from architecture list
%ld does not match %ld\n
\t
Could not parse the tar type flag field
appleDoubleSuffix
Could not get parent path
kBOMCopierOptionArchitectureFallbackKey is not a CFDictionaryRef
(%lu bytes for %d entr%s)\n
        %s Value 
munmap(%p, %zd) => %d\n
Could not set entry range
inputStream
skipRootDirectory
Could not read AppleArchive blob data
removexattr(\"%s\", \"%s\", %d) => %d\n
_maskWithPatternList failed while getting data for '%s' (parentPathID=%u pathID=%u bid=%u)
Cannot convert kBOMCopierOptionKeepBinariesDirKey from options dictionary into UTF8 encoded C string
Item %d from fallback list could not converted to a UTF8 string
buffer overflow!
zip
Could not read from FTS agent: %s\n
Could not set entry path for replay AppleDouble file
Unknown format type
ppc7400
veo2
kBOMCopierSourceOptionExtractAppleArchiveKey must be a CFNumberRef
Cannot open BOM at '%s'
Error message is NULL\n
skip-trailer
Could not get arch record for index %d
 [Metabom]\n
arm v7
<storage>
replayAppleDoubles
Could not free archive: %s\n
_BOMCopyStepZero
data_stack_count
Could not read ciphertext: %s
Cannot create PKZip file at %s
false
kBOMCopierOptionApplySourcePermissionsKey must be a CFBooleanRef
Invalid data stack
Could not resolve %s: %s\n
Unable to open the symlink %s: %s\n
BOMStorageCopyFromBlockRange: !data
malloc: %s\n
done\n
child_allocate
Could not set entry size
Could not skip remaining libarchive file data
%s%08x:
pkzip extra field InfoZIP UNIX v1
Could not write the fat header to the destination entry
Could not realpath parent %s: %s
Could not allocate kept file subdirectory path: %s
%s.tv_nsec: %ld vs %ld (%ld margin)
i686
Could not allocate %ld bytes for value: %s\n
Could not create empty replay directory stack
createArchive
Could not allocate regular expression
Unknown source entry type: %d
CFWriteStream is not open: %u
The password provided for the encrypted PKZip archive appears to be invalid
Could not populate read buffer for %s
Could not parse the POSIX ustar extended metadata
Could not set read stream for decoder: %d
Could not synthesize replay directory
Could not allocate encoded buffer: %s
Could not create resource fork entry for %s
<cputype %d, subtype %d>
arm64 v8
I'm expecting the end of central directory record.
Could not get AppleArchive blob: %d
kBOMCopierOptionCopyExtendedAttributesKey must be a CFBooleanRef
kBOMCopierDestinationOptionSegmentFileSizeKey must be a CFNumberRef
BOMCopierDestinationSetRelease
%s\t%o\t%d/%d\t%lld\t%05u\t%s\n
.nfs
Could not open child %s: %s
Could not set entry range\n
BOMCopierDestinationEntryGetTotalWritten
Could not write %ld bytes to destination: %s\n
Could not faccess %s: %s
Could not read the potential magic value
decompress_data
copier_source->data_archive is NULL
Could not reconstruct destination path: %s
__
1.2.12
Could not construct resolve path from %s and %s: %s
CFReadStream
Could not pop FTS node off the stack
Could not basename_r %s: %s
pentium
Storage:\n
Could not allocate %ld bytes for PKZip data descriptor: %s
consume_padding
named pipe
veo 2
POSIX ustar extended metadata string length %lu is larger than TAR record size %lu
kBOMCopierDestinationPersistRestrictedFlags must be a CFBooleanRef
Cannot convert skipbom from options dictionary into UTF8 encoded C string
The legacy engine does not support the nowhere destination
statfs
parse_copier_source_options
Could not dirname %s: %s\n
BOM_ASYNC_DEBUG
fcntl
Could not resolve %s: %s
Could not parse the tar mtime field
TODO: parse .ZIP file comment
Can't copy directory %s into a file %s.
Could not create set AppleDouble target for replay AppleDouble file
%s/%lu
Could not clone %s to %s: %s
armv7
Could not parse POSIX ustar entry
Could not get rootless attribute for xattr %s: %s
Could not unlock AFSC file: %d\n
\"%s\"\t
openFor
Could not create empty node
kBOMCopierSourceOptionAppleDoubleSuffix must be a CFStringRef
Could not add child %s to %s
populate_sequester_stack
BOMCopierDestinationSetConflictResolver
unlink(\"%s\") => %d\n
conflict_resolver
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Common/BOMPatternList.c
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/BOMCopierSource.c
BOMCopierDestinationEntryGetMatchRecord
Could not allocate fatal message: %s\n
PathTagTable
Could not create source entry for %s\n
Could not allocate I/O buffer: %s
Could not set AppleArchive type
Couldn't extract junk data
open_origin
veo1
parse_copier_options
path
extractLibarchive
Could not set the user ID for the directory entry
create_entry_apple_archive
Invalid access_time
async write thread starting\n
can't archive %s\n
kBOMCopierDestinationOptionPersistRootlessExtendedAttribute must be a CFBooleanRef
opendir(\"%s\") => %s\n
tar linkname
Could not convert AppleDouble suffix string to C string
Could not allocate %ld bytes for BOMCopierSourceEntry: %s
Unable to create write stream.
openFor(\"%s\", %d, %d, \"%s\") => %d\n
TODO: parse ZIP64 extensible data
Could not create AppleDouble injection entry
extra regular file
archs array is empty
Could not push parent FTS node onto the stack
Intel x86-64
Intel 80486
%p {%llu, %d, \"%s\"}
[%s:%u] %s\n
Could not lookup count for hardlink origin\n
Could not allocate %ld bytes for PKZip local header: %s\n
%s/%s
Could not finalize BOM CRC32 state
Could not read the potential binary magic value
zero_buffer_size is 0
Could not get AppleArchive device: %d
SHA256 is not supported
arm v8
realpath(\"%s\", \"%s\") => \"%s\"\n
Could not parse the PKZip extended-timestamp extra block
decrypt_streamed_data
Could not copy metadata from the symlink entry to its regular file doppleganger
Could not create empty sequester stack
dude offset is wack
kBOMCopierOptionEnforceDestinationLocationKey is not a CFBooleanRef
BOMCopierSourceEntryNewFromFTSAgent
can't open %s: %s\n
Could not allocate FTS child: %s
Could not get storage block for fso\n
Could not open FTS agent
Could not set cpio starting inode %s: %s
CFWriteStream is not open
Could not preallocate regular file at %s for %llu: %s
Could not re-apply saved ACL to %s: %s
Could not open the underlying origin
Could not read: %s
next_filesystem_entry
Could not get access time for entry %s
kBOMCopierDestinationOptionPerformAtomicCopies must be a CFBooleanRef
Directory object has an invalid version: 0x%X\nCannot dearchive.\n
/tmp/.BCSE.%u.T_XXXXXX
Could not read %lld bytes from archive for seeking
kBOMCopierOptionExtractAppleArchiveKey must be a CFBooleanRef
_computeVariantSizes(bom=%p, blockSize=%u): catcnt(%d) > catmax(%d)!
Could not create enumerator for the enumeration bom
Could not convert the read block size number to kCFNumberSInt64Type
push_replay_stack
Could not read %lu bytes from data_archive: %u
Could not realpath %s: %s\n
readlink
Could not set data written callback
Could not check for a cpio header
path and options are NULL
kBOMCopierSourceOptionPassphraseKey must be a CFStringRef
disableLexicographicSort
chmod(\"%s\", %d) => %d\n
com.apple.BOMCopier
archive has encrypted entries
source_entry is NULL
Could not regexec %s: %s\n
sourceOptions
kBOMCopierOptionSetStaticContentKey is not a CFBooleanRef
entry_gid
\tsize:\t%lld\n
Invalid data buffer size pointer
Could not sort the children
reorderExtraEntries
A
Could not allocate bzip2 stream: %s\n
kBOMCopierOptionCreatePKZipKey is not a CFBooleanRef
directory with cycles
Could not retrieve AppleArchive XAT entry: %d
Intel 860
Invalid PKZip end of central directory record signature: %04x
Could not copyfile %s to %s: %s
stream invalid; root page is outside of address range\n
%s is not a file\n
Could not stat %s: %s\n
kBOMCopierSourceOptionUnsequesterAppleDoublesKey must be a CFBooleanRef
kBOMCopierSourceOptionDiscoverCompressionAttributes must be a CFBooleanRef
io_buffer_size is 0
Could not set AppleArchive modification time
-------------------
Could not parse the POSIX ustar devmajor field
kBOMCopierDestinationOptionInitialInodeKey must be a CFNumberRef
removeExecutablePermissions
%p
kBOMCopierOptionPreserveRestrictedFlagsKey must be a CFBooleanRef
async write thread terminating\n
%s\t%o\t%d/%d\t%d\n
Could not allocate SHA256 context: %s
Could not allocate SHA512 digest: %s
kBOMCopierOptionCreateCPIOKey must be a CFBooleanRef
kBOMCopierOptionZlibCompressionLevel must be a CFNumberRef
Could not convert the zlib compression level to kCFNumberSInt32Type
Could not append AA_FIELD_ACL to AppleArchive header: %d
Add\t\t%#zx\n
BOMCopierSourceEntryGetExtendedAttributeName
data_analyzer is NULL
symlink(\"%s\", \"%s\") => %d\n
Could not create set entry parent for %s
./%s
source entry is not a fat file
Could not create ACL from text [%s]: %s
Unknown digest_type: %d
_BOMCopySpecification %p:\n
Large sizes:\n\t
rb
Could not set the path for the regular file entry
apply_retention_policy
Invalid PKZip ZIP64 end of central directory record signature: %04x
Intel Pentium II Model 3
Invalid data buffer
%d\t%s\n
kBOMCopierOptionSymlinkTreatmentKey is not a CFStringRef
Could not parse the PKZip Info-ZIP extra block for UNIX
Could not set ctime
Could not append %u entry to AppleArchive XAT blob: %d
%s: %s vs %s
Could not get AppleArchive gid: %d
        %s   Key 
Intel Pentium Pro
Invalid decoder
Could not add sequester entry for %s
Could not create node path for %s and %s\n
unsequester_apple_double
Could not set zlib compression level %s: %s
Invalid filesystem_entry
enumeration_bom is NULL
kBOMCopierDestinationOptionLibarchiveFilterKey must be a CFNumberRef
Could not allocate %ld bytes for pattern
destinationOptions
kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey is not a CFBooleanRef
Could not get actual path
arm v7s
Could not create number for %lld
can't unarchive %s. skipping...\n
BOMStorageCopyToBlockRange: internal consistency error
(%lu bytes)\n
dstPath is NULL
read/write
getcwd(%p, %zu) => \"%s\"\n
Could not set enumeration bom for source
Should not reach here
Could not asprintf resource path for %s: %s
BOMCopierSourceEntryGetArchRecord
readdir
Could not synthesize filesystem stuff
Remove\t\t%#zx\n
kBOMCopierOptionOutputNowhereKey must be a CFBooleanRef
async write thread finished file (errno=%d)\n
verifier: first leaf has prev value
Could not set the saved entry path
Could not close AppleArchive byte stream: %d\n
BOMCopierReleaseMatchContext
BOMCopierSourceEntrySeek
is_root: %s vs %s
capture_acl
Could not F_NOCACHE: %s
   adm size : %d\n
 [Package]\n
Format entry callback failed
Could not allocate bom_cpu_type_list
file '%s' is an unknown file type\n
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Storage/BOMTree.c
Client did not register password request callback
Could not read archive header: ARCHIVE_FATAL: %s
Could not get modification time for entry %s
Could not create rsrc path for %s: %s
async read thread asked to finish\n
%s exists on a different device from its target
%s:
kBOMCopierOptionSequesterResourcesKey must be a CFBooleanRef
path_tree_node_add_child
%s: stream invalid; overflow of toc offset+size\n
kBOMCopierOptionOutputCFWriteStreamKey must be a CFWriteStream
Could not allocate %ld bytes for POSIX ustar header: %s
Could not read minimal data for auto-detection: %s\n
Could not set destination redirect callback
00
BOMCopierDataAnalyzerNew
Intel x86-64h Haswell
lstat(\"%s\", %p) => %d\n
CompressionTypes
can't unlink %s\n
%s/%s%s
Could not created adjusted path for %s: %s
Could not push root node %s onto the stack\n
Could not construct destination path from %s and %s: %s
Could not lstat %s: %s\n
rename
Could not encode extended attributes
Not a central directory signature
parse_apple_archive_acl_blob
kBOMCopierSourceOptionExtractLibarchiveKey must be a CFBooleanRef
Could not write %ld bytes: %s\n
Could not parse NFTS extra field
Could not copy file entry to destination entry list
BOMCopierSourceEntryNew
Could not populate the children
Could not create custom AppleArchive byte stream at %s\n
Could not set status time for entry %s
Invalid source_entry
070707
arm64
readdir(%s) => %s\n
Could not re-allocate the entry list: %s\n
%s and %s are identical.\n
Decryption passphrase appears to be incorrect
Could not create FTS agent
Could not create set path entry for %s
Could not read archive header: %d: %s
BOMCopierDestinationEntryWriteFatHeader
Could not mktemp %s and %s: %s
Could not update BOM CRC32 state
Could not get arch record at index %d\n
No files for
%u\t
Unsupported format entry type: %d
\ttotalDestinationSize:\t%lld\n
open: %s\n
Close cancelled
   i leaf   : %d (%d)\n
Client did not provide passphrase
discoverBinaries
Could not convert kBOMCopierSourceOptionSegmentFileSizeKey to kCFNumberLongLongType
Could not capture access control list
ppc970-64
kBOMCopierOptionCompressDeprecatedKey must be a CFStringRef
%s\n
BOMBomVerifyBom: leaves do not verify.\n
Could not parse the POSIX ustar magic field
Could not set PKZip local header attribute
End of decoder
BOMCopierSourceSetRedirectCallback
Could not chmod %s %s to %s: %s
ppc604
parse_entry_pkzip_archive_extra_data
kBOMCopierOptionCrossDevicesKey is not a CFBooleanRef
BOMStorageCopyRangeFromBlockRange: !stream
file %s is not a bom file\n
Could not allocate last path component buffer: %s\n
Could not constructed entry rsrc name: %s
kBOMCopierOptionCloneFiles must be a CFBooleanRef
Cannot specify a fromObj with kBOMCopierOptionInputFileDescriptorKey
        
.ZIP file comment
ignoreAppleDoubles
kBOMCopierDestinationOptionRemoveExecutablePermissionsKey must be a CFBooleanRef
Could not append AA_FIELD_XAT to AppleArchive header: %d
Little Endian
chdir
Could not set the path for the directory entry
compression-level
kBOMCopierDestinationOptionCompressAppleArchiveKey must be a CFStringRef
skipCPIOTerminator
Could not discover resource fork
F_SETSTATICCONTENT 
directory
kBOMCopierOptionPersistRestrictedFlagsKey is not a CFBooleanRef
true
fstatfs
Could not duplicate key %s: %s\n
Could not create empty archive entry
Could not get AppleArchive modification timespec: %d
Could not open deny bom at %s
kBOMCopierOptionEnforceDestinationLocationKey must be a CFBooleanRef
kBOMCopierOptionPersistRootlessExtendedAttributesKey must be a CFBooleanRef
kBOMCopierSourceOptionDiscoverExtendedAttributes must be a CFBooleanRef
kBOMCopierSourceOptionDiscoverSegmentedFilesKey must be a CFBooleanRef
Could not create set sequester path entry for %s
Unknown AppleArchive field type: %u
Could not finalize CRC_32 context: %s
kBOMCopierOptionEnableLogging must be a CFBooleanRef
Could not decode POSIX ustar header
consume_source_entry
verifier: can't read page
Could not allocate SHA512 context: %s
can't convert arch #%d from archs listinto UTF8 encoded C string
Could not open the archive %d for custom reading: %s
%lld
Could not close AppleArchive encoder: %d\n
applyProvenance
key too long\n
m68040
stat: %s\n
data_archive_open_source
kBOMCopierOptionKeepBinariesDirKey is not a CFStringRef
extractCPIO
Could not open symlink %s
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/data_archive/data_archive_entry.c
kBOMCopierSourceOptionApplyBomOwnershipKey must be a CFBooleanRef
Could not create sequester path for %s: %s
BOMCopierDestinationSetRedirectCallback
post-order directory
Could not lchown %s to %d:%d: %s
mmap failed
i586
Could not allocate child list: %s
Could not parse the PKZip ZIP64 end of central directory locator
kBOMCopierDestinationOptionOutputCFWriteStreamKey must be a CFBooleanRef
can't write to keepBinariesList: %s
/tmp
SHA512 is not supported
Could not parse the tar size field
buffer is NULL
Cannot specify a toObj with kBOMCopierOptionOutputFileDescriptorKey
mkdir
getattrlist(\"%s\", %p, %p, %zu, %lu) => %d\n
discoverResourceAttribute
kBOMCopierDestinationOptionAppleDoubleMergeACLsKey must be a CFBooleanRef
Could not allocate buffer for value: %s\n
No password was provided and the client did not provide a callback for retrieving the PKZip encryption key
Could not parse the tar mode field
Could not free FTS agent
%d\t%s -> %d\t%d\n
entry_mode
com.apple.Bom
block device
armv6m
Could not create FTS agent: %s\n
parse_entry_pkzip_extra_field_extended_timestamp
inputFD
pkzip spanning doesn't match: %s
chdir(\"%s\") => %d\n
Could not create destination options
Could not allocate stack node: %s
POSIX ustar user name
extra symlink
Could not rmdir %s: %s
Cannot seek beyond the end of entry data
   # pages  : %d (%d)\n
Could not parse the CPIO header
get_volume_state
preserveHFSPlusCompression
kBOMCopierOptionApplySourcePermissionsKey is not a CFBooleanRef
armv5
link(\"%s\", \"%s\") => %d\n
kBOMCopierSourceOptionUseFilesystemCacheKey must be a CFBooleanRef
Could not synthesize the AppleDouble file
AppleFSCompressionFlags
Could not lseek in the destination %d:%lu: %s
WARNING: file appears to be a corrupt Metabom! (found %04x expected %04x or %04x)\n
%s/bomfreelist.trace.%d.%d.txt
/Library/Caches/com.apple.xbs/C6748B3C-87F0-4BBF-B6B7-4DD7691D0297/TemporaryDirectory.crewDc/Sources/Bom/Copier/data_archive/data_stack.c
Could not convert the input file descriptor number to kCFNumberSInt32Type
kBOMCopierOptionCopyExtendedAttributesKey is not a CFBooleanRef
keepBinariesPattern
%s and %s are identical (not copied).
Could not allocate %d bytes: %s
Could not allocate space for Apple Double files.
Could not lseek: %s
kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef
Cannot specify a toObj with kBOMCopierOptionOutputNowhereKey
extra
Invalid archive_entry
Could not get field key from AppleArchive header index %u: %u
node_sort_children
boms are identical.\n
HP-PA 7100LC
Could not allocate padding buffer: %s
fat_header_size is NULL
kBOMCopierOptionApplyProvenanceKey has an invalid size
Could create AppleArchive ACL blob from %s: %s
Could not create empty BOMCopierSource options
kBOMCopierOptionSkipBomKey is not a CFStringRef
Cannot enable on-the-fly decompression
Invalid aa_decoder
Could not finalize BOM CRC32 state\n
preserveRestrictedFlags
Could not mkstemp %s: %s\n
bad value for block table count\n
data is NULL
BOMCopierSourceSetAllowBom
The options dictionary is not a CFDictionary
Could not create empty preempt stack
missing path parameter
kBOMCopierOptionExtractAppleArchiveKey is not a CFBooleanRef
NULL error->error_message
munmap failed
applyProvenance is only for extracting from archives
BOMCopier: Inconsistency while preflighting copy\n
Could not create the entry
destination_entry is NULL
BOMCopierCountFilesInArchive: missing path
sequesterResources
Unknown source entry type
big
chown(\"%s\", %d, %d) => %d\n
!mac-ext
Could not push source entry onto the preempty stack
HP-PA
Exceed byte stream when parsing extra field
excludeRootDirectory
Could not set access time for entry %s
Couldn't read pkzip central header
Could not allocate SHA256 digest: %s
Could not set PKZip data descriptor attribute
kBOMCopierSourceOptionExtractAppleArchiveKey must be a CFBooleanRef
Could not create BOMCopierSourceEntry from %s
Could not replay AppleDouble file
Could not retrieve item %d from fallback list
Invalid status_time
listxattr
opendir
Vendor specific extensions (POSIX.1-1988)
BOMCopierDestinationGetCopyResult
BOMCopierSourceEntryCheckAccess
BOMTree iterator cannot cache keys. This is a fatal error (!it->key).\n
Could not create extra byte stream
replayDirectories
pkzip seek error: %s
stat error for '%s'\n
kBOMCopierOptionKeepBinariesPatternKey must be a CFStringRef
can't set hardlink index\n
Could not create dispatch group\n
Could not set format entry
Could not inflate: %d\n
Invalid entry_path
Could not read %lu bytes from %s
Can't create FSO for %s
ppc601
```
