# `/usr/lib/libParallelCompression.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 596,640 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2136)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libParallelCompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/liblzma.5.dylib (compatibility version 6.0.0, current version 6.3.0)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,274)

```
fcntl
No database provided
decoding compressed block %zu
%12lld 1:1 patches cache updates\n
%12zu entries selected\n
truncated write: %s
extractWriteToThread
ForceInPlace %d: excess_pages=%d/%d, converted bytes=%llu, %zu controls\n
preallocation %llu/%llu B took %0.2f seconds (# of calls=%i)
File a radar to increase obuf_capacity, sz=%zu
BXPatch4
rawimg_get_digests
enumerateTree_rec
SegmentStreamSimulate
getBXDiffControls
Invalid AFSC data
couldn't read enough header bytes from compressed file
unable to locate path in merged array
invalid reverse index for OUT
reserveDiffSegmentVector
Label PREPARE: %s\n
missing GID field: %s
writing data to ECC stream
loadDirectoryProc
Prepare
tempStreamPWrite
PagedFile: moving page from file[%u] to cache[%u]\n
com.apple.ParallelCompression
Create chunk pipeline
No database in set matches alias %s
no variants
cluster id out of range
extra bytes written after EOF has been sent
ForkOutputStreamPWrite
PagedFileCreate
%s stream: %llu bytes -> %llu bytes\n
writing entry header twice
RS65537\n
too many tasks
Number of written bytes and expected output size do not match
encode DAT field
rawimg_force_in_place
getStreamSHA1Digest
bad stream position
Generating patches for %zu entries on %d threads %s\n
DirectoryPatch
  Output: %s\n
OSHA1StreamCreate
NOP received
,s=%llu
%s must be an existing regular file
Broken pipeline
obtain AFSC data: %s
insertBLOBField
encoding directory entry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Utils.c
missing UID field: %s
transcodeOThreadPayloadProc
%12lld combo patches created\n
None
%s\n
bxdiff5CreateComboControls
BXPatchFile
%12llu redundant bytes in same data files\n
SH1
pushControls
Invalid compression type request %d
Can't write DAT-based field and DAT itself at the same time
Writing DAT blobs to database\n
bad index
ILowMemoryDecoderStreamCreateWithBuffer
writing entry data YDK
BTM
removeEntryProc
unlocking chdir_mutex failed: %s
CompressionWorkerDataCreate
hlink_path
lzma
a,b,t options are invalid in read mode
Missing some HLO fields in manifest
SemRelease
,0x%08x
static content hint failed
Writing resource fork header
allocating ACL blob
%12zu B final BOM size\n
storing vindex block
%12llu patch size\n
EYP
  truncate archive payload: %s\n
invalid compression type %d
ThreadPoolRunWorker
dumpStringArray
in memory allocation for PagedFile
Incompatible page size
getting string from includePaths
looking up parent path failed
creating combo controls requires 2 or more unique inputs
extractBlobProc
includeList
acl_set_permset_mask_np
transcodeOThreadBeginProc
waiting for O thread
%12zu non resolved entries\n
  In-place: %s\n
reading file header
extractClonesEnd
Block %zu loaded and decoded in cache\n
SLC
Invalid request type
NoExclude
%12zu entries with XAT blob\n
offloadToFile
aaReallocf
ImageDiff\n
RawImageDiff
ArchiveTreeInsert
merging string tables
ParallelCompressionFileRead
reading contents: %s
copyFileSegment
inserting string
bxdiff5CreatePatchBackend
ThreadPipelineFlush
ImagePatch: Patch not created with in place. No bound on needed excess space.
Attr not fixed: %s
BXDiffMatchesCreate
Invalid entry path
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPipeline.c
unexpected DAT blob
aaSequentialDecompressionIStreamOpen
  diff level: default (%d)\n
Search failed
OFileStreamGetPos
MemGateDestroy
invalid storage type in YAA header: 0x%02x, key=%s
ChunkPipelineDestroy
path_blob
serializing YAF entry
ARCHIVE entry with XAT/ACL: %s\n
ParallelArchiveSort
encode MTM field
[%7d] DIR mkdir: %s\n
storing extra fields data
yaa_decodeHeader
Payload too large: %zu B received / %llu B expected
pthread_attr_set_qos_class_np
dir/path too long: %s
SimStreamClose
Retry limit reached: %s
stream write
writing entry data
mode: r\n
ctrl[%zu]: moving %llu bytes from diff to lit (minFree=%d, ndiff=%llu)\n
creating YAA writer
open failed (%d): %s
getErrorContextKey
Input file digest and patch digest do not match
invalid length
creating AFSC stream: %s
[%d] processing entry %s\n
StringTableAppendTable
Worker: encode block %5lld: %7llu => %7llu\n
RunWorker
no overlapping segment found
Final labels (all entries)\n
%s rules: %zu total entries match\n
ParallelCompressionAFSCStreamOpen
computing file digest
Invalid ECC algorithm
CTM
Invalid output digest
%12lld entries extracted\n
DEV field is not set for a block/char special entry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACacheStream.c
bxdiff5SetOut
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
OArchiveFileStream didn't receive enough data before being destroyed\n
writing to digest stream
decodeEntryACL
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelCompression/File.c
allocating buffers
ParallelCompressionAFSCGetMetadata
writerReceiveData: ZERO (end of stream)\n
loadDirectory
Data
variant too large
write DAT 0x00, w=%zu: %s
addBlob
Write chunk
opening read request from database
[%7d] HLINK (legacy) deferred: %s\n
Invalid ECC magic
PagedFileRetainOut
CFStringGetCStringPtr returned 0
convertEnd
bad fork
%12lld cache updates FAILED\n
 labels=
archiveTreePackNodes
concatPath
%12lld entries valid\n
read: %llu B\n
  ECC variant: 
KEEP WITH FIXUP: %s\n
%12zu in the output, and not in any inputs\n
aaFileStreamPWrite
reading block header
aborting current receiving thread
Could not identify compressed stream format
Worker data allocation
retain output chunk
fsync
allocate XAT blob
Warning: ACL field verification is not implemented\n
bxdiffEncodeBuffer
Before applying control
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ISparseArchiveStream.c
invalid archive ID
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c
yaa_setEntryACL
No 1:1 patch %zu in cache: %s\n
LZMA
Patch matching entry %u\n
invalid output size/decoder error: block=%lld, inSize=%lld, outSize=%lld, expectedOutSize=%lld
unsupported qualifier length
invalid ACE qualifier type in ACL blob: %c
invalid cache directory: %s
entry is missing IDX field: %s
pcWrite
ImagePatch: Patching with excess space <= %d bytes.\n
ParallelCompressionEncode
allocating state buffers
writing raw header
invalid new node index
OBufferedStreamCreate
%12llu initial available blocks\n
%12zu LINK\n
invalid output PAGE
IFileStreamSetPos
EOF reached
 fork | %64s | algo |       size | compressed | V | C\n
Missing some HLC fields in manifest
ERR
BlobBufferIncreaseCapacity
SHA1 inconsistency (patching): %s
Stored patch: %s\n
  Metadata: %llu bytes\n  Controls: %llu bytes\n
MutexLock
sorting string table
OEncoderStreamDestroy
InSituStreamPWrite
Parsing YAA header
AATempFileStreamOpenWithDirectory
ARCHIVE new directory uid=%u gid=%u mode=0%04o flags=0x%08x parent_gid=%u: %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c
yaa_writeRawEntryHeader
invalid patch, output after buffer
%12zu in the output, and in all inputs\n
type=%c
realignment failed
input data is missing
encode PAT field
getting node path
patch is not a valid 1:1 BXDIFF50
update resource fork
%12zu B written for blocks table\n
YAF
rawimg_set_fork_types
ThreadPoolSync
rawimg_check_memory
too little variants
invalid inDir
SharedArrayPush: pthread_cond_signal failed\n
DirectoryPatch: %llu errors after processing the archive payload
loadFileSegment
stringTableReserve
%12lld entries compared -> modified\n
REMOVE archive, links, firmlinks, remove rule: %s\n
rawimg_save_to_stream
- input %zu\n
%s (with errors)\n
parsing profile: %s
invalid compression algorithm in mode: %s
invalid inKey
%12u block size\n
reading page
aaFileStreamWrite
cacheFlush
merge_controls
storing encoded extra fields
SharedArrayPush: pthread_mutex_lock failed\n
truncate temp file
PagedFileRetainAndWriteOut
%12lld bytes received in regular files\n
failed to join encoder thread
writing stream magic
invalid mode
OECCStreamWrite
cacheData
pos out of range
input is missing or invalid
generateBOM
overflow in offset,size
patchCacheOpenFromURL
SimStream: pages: %i file, %i written, %i free, %i excess (%iK)\n
encode CKS field
read archive payload
fstat
writing data to database request
payload segment: %llu [%llu]\n
SharedArrayPop
aaFileStreamRead err=%zd buf=%p n=%zu
%12lld buffers exchanged\n
storing XAT blob contents
convert_block_controls
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBuffers.c
entry path too long
open: %s
Created 1:1 controls %zu: %s\n
getFreeCachePos
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBasicStreams.c
[%7d] HLINK/CLONE deferred: %s\n
seek file decoder
block %zu: compressed:%llu..%llu raw:%llu..%llu\n
copy, no compression
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelCompression/Streams.c
MemBuffer write proc returned 0
%12lld bytes hashed\n
no fork extents
encoding metadata entry
SharedArrayEnqueue failed
indexBeginProc
extra data: %s
%12llu entries extracted\n
invalid patch, input after buffer
flushCache
pthread_join
decoder failed
%12llu INVALID BLOCKS\n
CFArrayGetValueAtIndex(%ld) returned 0
write DAT, w=%zu: %s
[%s] 
OECCStreamCreate
    comboPatch set, comboPatchSize=%zu (%zu MB)\n
SemAquire failed
MemBufferFlushToBuffer
truncated stream header
Patch application
[%d] Entry processing thread starting\n
%zu entries in hlinks cluster %zu\n
%12llu final free blocks\n
zlib, level 5 (alias: zlib)
ParallelArchiveDBRequestOpenForWriting
getting SHA1 digest: %s
  worker threads: %d\n
Warning: couldn't set F_NOCACHE\n
comboPatch is not NULL
creating mem buffer
decoding ACE
ArchiveTreeMergeAndDestroy
mergeDiffSegmentVectors
Input variants in patch: %u\n
createHLinks
entry is not labelled REMOVE and matches REMOVE rule: %s
InSituStreamClose
write: %s
thread didn't consume data
Invalid patch cache URL (NULL)
index=%zu
invalid ACE perms: 0x%016llx
segment out of range
SharedBufferFillFromStream
aaFileStreamPRead err=%zd buf=%p n=%zu off=%llu
Warning: F_NOCACHE failed: %s\n
Invalid iBlock received
decoding bzip2 payload
virtual fork
Loaded 1:1 patch %zu from cache: %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Extract.c
Invalid profile code: %c
Output buffer too small, %zu B required, %zu B provided
%s variant <%s> | %llu bytes | %zu extents | %zu forks (%llu/%llu) | digest=%s\n
getting entry path
enumerateTree %s
extra header field is too large for processing thread buffer
BXDiff5 patch allocated: %zu B\n
Input doesn't match any of the expected patch inputs
createVIndex
%12llu hard link entries\n
aaFileStreamGetFD
close
BXDiff5 patch capacity: %zu B\n
reading from archive stream
AADecompressionInputStreamOpen
MemBufferIncreaseSize
PagedFile: moving page from cache[%u] to file[%u]\n
missing CKS field: %s
MappedBufferCreateWithFilename
invalid thread_id stored in entry
encode CLC field
missing combo controls
lzraven
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c
MemGateInit
Allocating deferred entry
building full link path: %s
%12llu patched files disk usage\n
 path=%s\n
Missing write limit %llu
Closing file patch cache in directory: %s\n
in digest mismatch in patch
Warning: couldn't set F_NOCACHE on paged file\n
MutexUnlock
entry is labelled PATCH + REMOVE: %s
invalid cache POS
%zu clusters in main hlinks tree\n
noExcludeList
yaa_encodeHeader
%12u entries in index\n
seek error
setting attributes: %s
inode index is too large
manifest doesn't provide MOD for entry %s
invalid blockSize in input stream
Updated combo patch to cache: %s\n
create diff payload stream
initBestMatchFromHashes
invalid entry
ParallelArchiveDBReadRequestOpenWithSet
digest
DirectoryDiff:\n
running worker
inserting IDX
writeHeader
Moving %s to %s (2nd attempt)
[%7d] %s SPECIAL: %s\n
bad header
lzma, preset 6 (alias: lzma)
appendPayload
alloc first block
raw data size: %llu B\n
invalid ACE type in ACL blob: %c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffWithCache.c
seeking compressed stream
SharedArrayPop: pthread_mutex_lock failed\n
PagedFileReadAndReleaseIn
init available_threads
no
path_tree
Total time %.2fs, %.2f MB/s (%s)\n
chunk out of bounds
SemAcquire
parsing archive
fsetxattr resource fork
ImagePatch: No variant found
Block %zu evicted from cache\n
%12zu in the output, and in some but not all inputs\n
bxdiff5CreateInPatch
missing PAT field
Could not reduce minFree to %d, something is wrong
invalid inPatch,inPatchSize
ImagePatch: Digest match. Output reconstructed.\n
Warning: XAT field verification is not implemented\n
ARCHIVE directory with different attributes: %s\n
com.apple.decmpfs
create DAT buffer
/.WXXXXXX
ParallelArchiveRead failed
%s%s/%s
pcWrite failed
allocating XAT blob
block is too large: %zu B
file < written
controls_append_copy_forks
writing entry header
comboControls is not NULL
%12u worker threads\n
reallocf
skip dataless: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c
Writing chunk sizes
patch_read_variants
GetLargeFileControls
%12lld entries removed\n
installFile
%12lld combo patches cache hits\n
writing page
readdir on dataless directory: %s
Payload compression
is
aaCacheStreamClose
Release bufferReady, buffer size: %zu\n
lseek failed and pos < s->pos
RawImageGetPatchInfo
Label MAIN: %s\n
%12zu PATCH\n
create input stream
pthread_setspecific
Truncated read n=%zd pos=%llu read=%u fd=%d
  Expected SHA1: %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c
MASTERING_TOOLCHAIN_DIR
invalid I=%zu
    0x%06x diagnostic code\n
bad fork flags
%12llu entries in subtree\n
- output\n
qsufsort32
rename: %s
[%7d] HLINK (legacy) %s -> %s\n
aaCacheStreamOpen
invalid decoder: %d
hard link resolved to a larger index: %s -> %s
v8@?0
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/SharedBuffer.c
input patch is missing or invalid
Invalid uncompressed chunk size
Second pass fixup succeeded: %s
No-op patch matching, writing input\n
outputStreamProc
storing ACL blob contents
threadPoolWorkerThreadProc
yaa_decodeHeaderInfo
stream read
PCompressFilter
building full path from includePaths
ThreadPoolDestroy failed
A LoadDirectory thread reported an error
SharedArrayInit
too many excess pages
Created 1:1 patch %zu: %s\n
unable to load input page
lzvn
some output bytes are missing or referenced more than once after archive expansion
override attributes
%12zu blocks per thread\n
01234567
patch_write_stream
add_fork
OFileEncoderStreamCreateWithFD
ARCHIVE root directory: .\n
NoRemove
data missing
unexpected XAT blob
Thread allocation
Dropping copy fork with %llu bytes, needed=%llu bytesx\n
no digest info
fixOpsForInPlace
bxdiff5Free
internal header buffer is too small
File too small for AFSC
YEC
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c
yaa_setEntryAttributes
%11.2f%% parity/data ratio\n
entry is labelled PATCH + ARCHIVE: %s
Generating diff list, %zu entries\n
FLG
invalid output file SHA1 digest %s: %s
bad chunk order
IGNORE excluded directory with type change: %s\n
entry is labelled REMOVE and matches INCLUDE rule: %s
file not empty
BXDiff5 patch archive payload: %zu B\n
Full replacement patch\n
createBomInfo
writing entry data BLOBS
cacheWrite
malloc %u threads
computePatches
aaIntervalInputStreamOpen
fsetxattr resource fork header
ParallelCompressionAFSCFixupMetadataEx
pcRead failed
rawimg_load_chunks_from_stream
Literal
stat failed: %s\n
missing out
%12llu entries failed to extract\n
ImagePatch: Static content hint failed.
unsupported decoder in file header: %c
Initial labels (regular files / symbolic links)\n
flush cache
expected ref_count=1 for terminating thread
BXDiff5 backend, out: %zu B, diff: %zu B, lit: %zu B, ctrl: %zu B\n
RawImagePatchInternal
ImagePatch: Digest match. Copy input to output.\n
Decompressing the file: %s\n
entry_id=%u parent_id=%u %s\n
 uid=%u gid=%u mode=0%04o flags=0x%02x duz=%llu size=%llu link=%zu
encode TYP field
setattrlist error %d: %s
invalid qualifier type: %d
createErrorContextKey
/System/Library/Filesystems/apfs.fs/Contents/Resources
writing tool output
create expandDir thread
aaFileStreamRead
aaSimStreamOpen
get entry segment
bxdiff5Alloc
could not move input page in cache
remapping nodes
allocating YAF buffer
inserting YDK
OBufferedStream creation
Warning: ACL tag type is not ALLOW/DENY (ignoring entry): %d\n
fileRequestPRead
Input archive compression: %s %llum\n
OFileStreamCreateWithFD
KEEP: %s\n
string table sorting
pthread_mutex_lock
length
ERROR
loadManifest
sendEOF
tree has a first root, but no last root
chdir+bind failed: %s/%s
control_reader_create
YDK payload is too large
invalid entry index
%s
encode INO field
creating file stream: %s
Loaded combo patch from cache: %s\n
write after EOF
<%02x>
compression_decode_buffer
Warning: F_SETSTATICCONTENT failed with error %d: %s\n
writing header
IMemStreamCreate
generic controls
ThreadPipelineCreate
ThreadPipelineRunWorker
SKIPPED
Data fixed with ECC (diag 0x%08x): %s
invalid offset=%llu, size=%llu in file %s
getFileDigests
bad map
zero_coder_encode
inserting YEC
ctrl[%zu]: ndiff=%llu nlit=%llu\n
ForceInPlace: %zu controls. Dropped %llu bytes to stay within budget.\n
too many variants
fsetxattr decmpfs
threadPipelineConsumerThreadProc
patchCacheUpdate
Comparison fields: %s\n
encode EYP field
Decompression
missing DEV field: %s
controls_create_with_variants
consumer proc reported an error
aaByteStreamReadExpected
entry is labelled KEEP + REMOVE: %s
aaByteStreamPReadExpected
bad variant
could not determine parent directory: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Sort.c
reading aggregated entries
write entry data: %s
reading archive tree: %s
a parent of path is not a directory: %s
    comboControls is NULL\n
Total time %.2fs, %.2f MB/s\n
Invalid input file: 'odc' or 'newc' raw cpio archive expected: %s
SegmentStreamPWrite
remapping tree nodes
append expandDirRange output to main tree
reading block payload failed
jsonPushValue
invalid entryType
BXDiff5 patch total size: %zu B\n
checkAndFixBlob
nDB is not expected to be 0\n
pc_array_compress
bad image size
mergeContents
fileSessionCreate
invalid cache url: %s
parsing YAF blob
bad seek
aaCacheStreamTruncate
end of stream\n
%12lld combo patches cache lookups\n
invalid inDir length
InSituStreamPRead
Final truncate
GetLargeFileControlsWithStreams
could not find unique input
Thread creation
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/PatchCache.c
hw.physicalcpu
ChunkPipelineCreate
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOCompressedStreams.c
w
  %u free pages in cache\n
invalid YAA header
HLIndex
Indexing failed
fork chunks
ARCHIVE patch is larger: %s\n
createThread
read failed (%d): %s
SharedArrayPop: pthread_mutex_unlock failed\n
statfs failed: %s\n
ArchiveTreePrune
malloc holes failed
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/StringTable.c
invalid ACE flags: 0x%016llx
Pipeline failed: using in-thread compression
writing block payload
%12lld bytes not stored in clones\n
ParallelArchiveECCGenerateCommon
Include
create input path
decoding block payload failed
%d HLINK(%d) ino=%llu size=%llu -- %s = %s\n
%12zu directories\n
PagedFile: input page %u removed from storage\n
sort string table
file + excess != written + free
uncompressed_size
sending failure info
invalid header, TYP must be set
TMPDIR
Thread %d processing '%s', size=%zu, header=%zu, capacity=%zu\n
invalid temp_dir: %s
Truncated block header (%lld/16 bytes read)
%12lld bytes received\n
fail to init buffer
encode MOD field
IDecoderStreamCreate
%12llu initial blocks\n
can't connect to database to get YDA YDK
07070100000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000b00000000TRAILER!!!
cachePageEvict
SharedArrayInit: malloc failed\n
YDA
extra header data size doesn't match expected value
Decoder: %s\n
reading uncompressed block %zu
creating decoder failed
Storing path
ParallelArchiveReadMetadata
invalid linkSize
ArchiveTree append
archiveTreeAppend
, %s
No-op patch matching, do nothing\n
inserting YDA
invalid segment size: %llu
  override mode for regular files: 0%o\n
aaSegmentStreamOpen
false
writing metadata entry blob
Storing slink path
%s rule [%s] prefix match: %s\n
updating depth field
archiveTreeSort
join expandDir thread
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ArchiveDatabase.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteStream.c
failed to start decoder thread
decoded/read ratio: %.2f\n
setThreadErrorContext
fstat: %s
aaCalloc
getProfile
BufferDecoderRead
WARNING: firmlink directory is not empty: %s\n
AATempFileStreamOpen
invalid segment order
Removing xattr
ThreadPoolGetWorker failed
hlinks
max level reached
compressed fork
%12llu data size\n
inserting XAT xname: %s
Thread reported an error
Total size %zu MB\n
setEntryXAT
Invalid index in ino table
getting next worker
write entry XAT
openEntryTemp
Worker: decode block %5lld: %7llu => %7llu\n
> %s %zu\n
reading gzip header data
acl_get_flagset_np
  %u input pages stored, %llu bytes referenced\n
building full path: %s
 LargeFile: Using %zu M for hashing.\n LargeFile: Using %zu M for fingerprints.\n LargeFile: Parsed %zu M in %0.2f (s). Added %zu/%zu fingerprints.\n
full entry path is too long
AATempStreamOpenWithDirectory
chunk error
Input retained
writing block header
setEntryAttributes
lzfse
offload to file
input page is not stored
Couldn't convert to requested compression type
store XAT and ACL blobs in entry
[%7d] inserted: %s\n
resize blob buffer
ParallelArchiveCombine
no segment found
directoryPatchEnd
Flush chunk pipeline
ParallelArchiveWriteDirContents
write
out is not NULL
write DAT blob: %s
getPatchMaxMemory
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Write.c
No patch in cache: %s\n
bad write mode
Extracting all entries not in subtree: %s\n
encode HLC field
write extra fields data
archiveTreeCreate
/usr/standalone/update
corrupted stream header
increasing XAT buffer capacity: %s
%zu/%zu unique inputs: %s\n
Updated 1:1 patch %zu to cache: %s\n
fork_realign
no cache
mem buffer creation
bomBeginProc
bad chunk info
too much data
archiveTreeUpdateNodeDepth
    inPatch set, inPatchSize=%zu (%zu MB)\n
resolving output fields
Inconsistent HLC fields in manifest
malloc patch
ILowMemoryDecoderStreamCreate
%12zu sockets\n
InSituStreamSimulate
Loaded input file %zu: %s\n
ParallelArchiveRead
no chunks found
YDA payload is too large
Created combo patch: %s\n
%s: 
encode FLG field
output page is not stored
inControls[%zu] is not NULL
extractThreadProc
aaSegmentStreamProcess
fchflags UF_COMPRESSED
CacheStream: read ops %zu/%zu, write ops %zu/%zu\n
%12u input archives\n
resizeStream
Cache miss after PENDING timeout: %s\n
ForkOutputStreamWrite
aaForkInputStreamOpen
could not locate the apfs diskimage map tool
XAT/ACL blob is not empty
processDeferredEntries
%12lld 1:1 patches created\n
unable to load output page
inserting new root name string
MemBufferFillFromBuffer failed
acl_create_entry
PagedFileDestroy
BXDiff5WithIndividualPatches
ISparseArchiveStreamRead
ParallelCompressionIStreamCreate
MemBufferFillFromBuffer n is too large: %zu
read diff payload
create session: %s
Updated labels after patch generation\n
  %s:\n
loadFileContents: %s
symlink %s -> %s
store entryEnd
image size mismatch
Multiple HLO = 0 entries for same cluster
full replacement
 rules=
ARCHIVE different files, not in patch range for AFSC-compressed files: %s\n
ACL blob [%zu] stored for %s\n
realign_fork
Errors in archive: %u
searchThreadMain
Error decompressing file
MemBufferIncreaseCapacity out
directoryPatchPayload
mmap file segment
Too much fork padding: %zu
clear XAT: %s
%12llu initial free blocks\n
unsupported entry type '%c'
archiveTreeUpdateChilds
pos not reached
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/CheckAndFix.c
convertBlob
invalid type for default field %s
invalid ACL blob
increasing blob capacity failed
ImagePatch: Digest match. Output already correct.\n
invalid segments in archive
inserting root dir
%11.0f%% cache hits\n
pthread_attr_setstacksize
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/SharedArray.h
invalid op in BLOB PAYLOAD
reserveBlobPayload
PatchCache update not expected
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c
reading block
Invalid ECC header
transcodeIThreadProc
errors during manifest scan
PC_APFS_DISKIMAGE_MAP
output data is missing
Archive stream init
Missing call to RunWorker before GetWorker
vindex
MemGateFree
load_variants
areFilesEqual
%02x
loadBlock
invalid session URL: %s (invalid alias chars)
  skip archive payload: %s\n
Compressed archive payload (gzip, bzip2, xz)\n
writing header before all required fields are updated
Write
NoInclude
storing ACL
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AATempStream.c
SemInit
Updated 1:1 patch to cache: %s\n
parseAPFSJSON
unexpected ACL blob
  min patch size: %llu B\n
merging contents
acl_set_tag_type
BXDiffWithCache
archiveTreeFromArchiveBlobProc
[%7d] DIR deferred: %s\n
zlib
lz4
compressor thread
bad chunk
MTM
not implemented
mutex unlock
no storage available for output page
Could not identify payload format
building fast path controls
pc_array_init
update DIDIFF10 header
tempStreamPRead
allocate ACL blob
Archive read
getFileSegmentSHA1DigestFD
archiveTreeFromIndexBeginProc
ThreadPoolRunWorker failed
rawimg_query_forks
initOps
getFilesystemBlockSize
createSearchThread
Writing resource map
getFileDiskUsage
lstat %s
acl_init
writing data
getDefaultNThreads
bad interval
copyStream
inFlightQueueRetire
store AUX in depth
Invalid temp dir path: %s
%12llu bytes read\n
writerReleaseSem
no free pages in file
/
attr
cloning file: %s
  - %s\n
Patch can't be applied in-place
ARCHIVE STREAM: OPOS=%llu IPOS=%llu NDIFF=%llu NARCHIVE=%llu\n
compressionWorkerProc
  input directory: %s\n
removeLeaveDirProc
%12u entries in archive tree\n
path too long: %s/%s
 V%zu[
createPatch
MOD
  ignore EPERM: %s\n
getFileSegmentSHA1Digest
Processing deferred entries
entry is labelled REMOVE and matches EXCLUDE rule: %s
r
BXDiff5Data: n=%zu, nUnique=%zu\n
BXPatch5StreamWithFlags
%12lld entries invalid\n
DST is not empty
  - Variants:   %d\n  - Flags:      %llx\n  - # controls: %llu\n  - Patch size: %llu bytes\n    - Metadata: %llu bytes\n    - Controls: %llu bytes\n
processing DAT end
decoded: %llu B\n
  patch threads: %d\n
%12zu not in the output\n
invalid prefix length
%12llu same data entries\n
encode SLC field
Loaded output file: %s\n
Reading entry
preallocating %llu B
true
create archive encoder
%12zu REMOVE\n
PAT
inputPageData
Parity buffer out of range
%12llu final patch size\n
buffer is not empty
Generated patches (%.1f s)\n
SIZ
yaa_decodeHeaderField
PagedFileDump
%12llu bytes in archive\n
bad page
/XXXXXXXX
changing pos
%12zu hard link clusters\n
MemBufferDecreaseSize n is too large: %zu
(memoryLimit %llu MB)
acl_get_qualifier
waiting for an available worker
bad page index
invalid input index
calloc
hlink_cluster_tree
cache size: %zu B (%d blocks)\n
decoding zlib payload
processDATEnd
looking up parent node
archiveTreeAppendTree
Invalid resource fork size request: %u
read: %s
missing MOD field: %s
Truncated read n=%zd pos=%llu read=%llu %s
resolving hard link %s -> %s
ParallelArchiveWriterCreate
aaForkOutputStreamOpen
  %u output pages stored, %llu bytes referenced\n
file not open
Invalid patch header
checkAndFixThreadProc
creating session for: %s
XAT blob [%zu] stored for %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/../ParallelCompression/../Common/SharedArray.h
dir doesn't exist, or is invalid: %s
invalid image map JSON
MemBufferIncreaseSize n is too large: %zu
too little excess
compressed stream detected : try compression_tool
%12lld max entries in flight\n
reading data segment
parsing index
%12zu B written for blocks\n
generatePatch
*** %s\n
Stream close error
verifyDirEndEntry
%12zu entries reported an error\n
archiveTreeReserve
%12.0f MB/s\n
MemBufferDecreaseSize
[%7d] HLINK %s -> %s\n
vindex_tree
cachePageReadFromDisk
FAIL
no possible conversions
Output
MemGateAllocateRequest
invalid SRC/DST
outputPageData
controls_combo_enforce_copy_fork_boundary
storing bom_info block
loadDirectoryThreadProc
writing block
pthread_mutex_init
allocate_page
  Input %zu: %s\n
reading magic
Truncated stream
mismatch in number of tree pages: i_page=%zu n_pages=%zu
Block %zu loaded in cache\n
Waiting for PENDING patch (%llu s): %s\n
could not move output page in cache
  Patch: %s\n
BXPatch5FileWithFlags
IGNORE excluded directory: %s\n
invalid state
%12llu archive payload size\n
invalid nameSize
temp stream open
invalid new index
No output_file given
Truncated write n=%zd pos=%llu read=%u fd=%d
invalid offset=%llu in file %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ArchiveDatabasePlugins/ArchiveDatabaseFilePlugin.c
pthread_create
processStream
ImagePatch\n  Input:        %s\n  Output:       %s\n  Patch:        %s\n  CryptexCache: %s\n  StaticContent: %s\n
allocating shared buffer
IGNORE excluded entry present in output: %s\n
SH2
allocation
outPath is not a directory: %s
pc_array_append
setEntryXAT: %s
manifest doesn't provide SIZ for entry %s
encode SH1 field
preallocation failed
expand directory
add_control
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/VerifyDir.c
  skip attributes: %s\n
    comboPatch is NULL\n
(stream based)
copy
computing buffer digest
transcoding
%12zu hard links\n
PagedFile: moving page from file[%u] to file[%u]\n
aaByteStreamWriteExpected
%12lld bytes not stored in holes\n
ParallelCompressionAFSCFixupMetadata failed: %s (aft=%d afr=%u)
%12zu block count\n
Label DATA: %s\n
%12lld entries missing\n
lzma_stream_decoder
fork header
invalid size increase
ECC65537CheckAndFix
inconsistency in nRefs == 0
  Compression: %s\n
building diff controls
WriteAlignedChunkProc
com.apple.ResourceFork
setEntryACL: %s
gettimeofday
verifyDirThreadProc
archiveTreeFromArchiveEndProc
OArchiveFileStreamCreate
ParallelCompressionFileSeek
%12llu fixed bytes\n
Rules from %s to %s (priority): %s\n
file:
CFArrayGetValueAtIndex(%d) returned 0
increasing string table capacity
StringTableSort
MemBufferCreate
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/LargeFile.c
MemGateReserve
creating resolve thread
stat: %s
BlobBufferStore
Invalid compression type %u
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelCompression/Filter.c
checkAndFixBeginEntry
ParallelCompressionFileOpen
MemBufferFlushToOStream
.%08x
First pass fixup failed: %s, compression_type=%d (expected %d), resource_fork_size=%u (expected %u)
inProc read
aaCompressionOutputStreamWrite
extents overlapping
truncated read
apfs_scan_diskimage
aborting entry
filePatchCacheOpen failed
SharedArrayPush
ParallelArchiveWriteEntryHeader
Missing decmpfs xattr
creating pipeline
corrupted file
ParallelArchiveExtractSubtree
OFileStreamCreateWithFilename
File too large for AFSC
creating workBuffer
%d ino=%llu size=%llu -- %s\n
Storing link path
GID
Missing resource fork xattr
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPool.c
writing entry data YEC
truncated block payload
rawimg_verify
create output link path
PagedFile: storing oldest cache[%u] to file\n
moving page from disk to cache
StringTableCreate
CHAR
reserveExtraFields
write failed
yaa_decodeACE
ImageDiff: Removed non-unique input variant <%s>.\n
pcRead
ParallelArchiveDBSetDestroy
SharedArrayPush: stack is full\n
Reading input file failed
acl_set_qualifier
Created 1:1 patch: %s\n
inconsistency in inPage/outPage indices
Error 0x%08x\n
invalid dir: %s
OArchiveFileStreamCreate: %s
invalid in,inSize
Dropping %llu bytes at %llu, needed=%llu bytes, type %s\n
AFT
.\n
Exceeding write limit %llu: nbyte=%llu
invalid entry type: %s
BXDiff5 patch diff[%zu] payload: %zu B\n
flushToResourceFork
patchCacheLookup
%12u unique entries\n
 ops=
current PagedFile state
Writing decmpfs
Truncated lit stream
pthread_get_qos_class_np
 (C)
opening input file: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/WriteDirContents.c
filePatchCacheLookup
%s.json
writeToThread
ARCHIVE differing types: %s\n
%12lld 1:1 patches cache hits\n
skip mounted dir: %s
looking up AFSC data: %s
  Output data SHA1: %s\n
%12lld entries compared -> verified\n
invalid header
INO
SharedArrayPop: pthread_cond_wait failed\n
alloc writer buffer
empty controls
string too long for StringTable
Invalid output digest after patch application
Truncated block header (%lld/16 bytes written)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/BXPatchFile.c
noIncludeList
manifest doesn't provide GID for entry %s
  MSU mode: yes\n
inconsistency in nRefs != 0
creating archive decoder stream
Size64
bad duplicate
*full replacement*
write DIDIFF10 header
%s \"%s\"
%12lld entries in archive\n
couldn't locate entry [%d] in queue
writing metadata entry
invalid ACE type
bxdiff5CreateComboPatch
    comboControls set, nControls=%zu, inPlace=%d (%zu MB)\n
 (MSU)
Unsupported patch format
%12llu diff payload size\n
Invalid path length for subtree: %s\n
extractSubtreeBegin
Output copy failed\n
[%7d] SLINK: %s -> %s\n
BomInfo
stream read failed
loadManifestProc
%s/%c%c%c/%s
bad extent pos
ARCHIVE directory with XAT/ACL: %s\n
sendFailureEntry
%12lld raw archive\n
increasing archive tree storage
retiring entry from in-flight state
[%7d] processing deferred Dir: %s\n
size64_tree
bad algo
ARCHIVE differing symlink: %s\n
storing node depth in AUX
archiveTreeSortStringTable
[%7d] set attributes: %s\n
Invalid ECC block size
%12zu entries\n
acl_get_permset_mask_np
Warnings:0x%08x
readdir_r
bxdiff5CreateFullReplacementBackend
writing metadata
write error
invalid patch size
DirectoryPatch:\n
insertUINTField
Output fields: %s\n
XAT blob size mismatch
Invalid patch size
Can't allocate header/footer
Patching failed %s
manifest doesn't provide UID for entry %s
yaa_encodeACE
bxdiff5SetInPatch
.XXXXXX
missing MTM field: %s
invalid cache pos
no chunk info
bxdiffFastPathControls
Destroying state with non-empty in-flight queue
callback signaled abort
Invalid out segment in patch
IDecoderStreamThreadProc
%12zu segments to read in archive\n
destroying session
  update cache: %s\n
bad image
seek archive decoder
Invalid profile value: %s
DAT
inserting root entry
volumes
non-directory entry not found in any archive
fileRequestCloseAndGetKey
processing DAT begin
Data not fixed with ECC (diag 0x%08x): %s
IMemStreamCreate failed
process_input
cachePageGet
create YAA writer
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/FilePatchCache.c
writing dir entry
write entry header: %s
expandDirRange
MemBufferIncreaseCapacity in
connecting to database
Threads reported errors
rawimg_create_with_file
out digest mismatch in patch
YDK
output file stream was not closed
no digests found
SharedBufferAbort
ParallelCompressionAFSCGetMetadataFD
some input bytes are still mapped after diff expansion
Request creation
unsupported entry type %d
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Combine.c
renameIfNotExist
listxattr failed: %s
stream not compatible
size
IMagicStreamCreate
ImagePatch: Preallocation failed.
locateBlock
acl_get_tag_type
mutex init
currentReadBufferEmpty
Extracting subtree: %s\n
%12lld bytes not stored in same data files\n
Too many bytes received
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/MSUArchive.c
After input pages retained, %u free pages\n
encode CTM field
fileRequestOpenForWriting
hashing output file
%12zu B written for TOC\n
too many entries in tree
encoding ACE
createThreadErrorContext
Stream write failed: %s
SharedArrayPop failed
isize,osize too large
unexpected output buffer size
Manifest fields: %s\n
pruning entries: %s (%d)
readProcessData
reading from tool pipe
Invalid patch header contents
ARCHIVE different files, attributes differ: %s\n
write entry ACL
File patch cache dir name is too long: %s
skip dataless dir: %s
worker proc reported an error
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c
creating compressed stream
bxdiff5CreateInControls
[%7d] FILE writing %s%s: %s\n
empty tree creation
flushing cache pos
Archive stream applied
Final FULLSYNC
Invalid header
in[%zu] access out of range
invalid file header
%12zu FIRMLINK\n
encode UID field
InSituStream: pages: %i file, %i written, %i remapped, %i free, %i excess (%iK)\n
reading manifest
generating entry header
    in is NULL\n
Truncated block payload (%lld/%llu bytes written)
ParallelArchiveCheckAndFix
Input archive is already sorted\n
inconsistent N
PagedFile: moving page from cache[%u] to cache[%u]\n
%12lld cache lookups FAILED\n
stream not compatible\n
concatExtractPathEx
ParallelArchiveSearch
Missing bytes in patch
ISparseArchiveStreamCreate
finalizing database write
diff list file
joinThread
creating internal buffer
%12llu archived files disk usage\n
%12llu same data clusters\n
patching file %s
mkostemp
INSERTED
invalid outKey
ThreadPipelineDestroy failed
manifest doesn't provide SH1 for entry %s
reading from diff stream
truncated stream
empty segment vector
truncated data: %s
AAByteStreamClose
ImageDiff: Constructed %zd combo controls.\n
%12llu compressed archive size\n%12llu raw archive size\n%12.3f compression ratio\n
segment_decode_to_buffer
BLOCK
decoding lzma payload
%12zu entries in BOM\n
resizing stream
PagedFile: storing cached input page to file\n
offset
%12lld deferred directories\n
%12zu blocks allocated\n
MemBufferFillFromBuffer
ARCHIVE one input is too small: %s\n
Rules from %s to %s (no-xxx): %s\n
Fork missing header/footer
ParallelArchiveExtractClones
calloc controls
Merged %zu inputs and 1 output\n
pcWrite EOF failed
invalid option in mode: %s (%c requires an arg)
Invalid block index
bad variant size
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/DirectoryDiff.c
%12zu regular files\n
aaByteStreamPWriteExpected
checkAndFixEndEntry
too many YAF fields
BXPatch5InPlace
jsonPushLabel
not enough bytes received
IDecoderStreamDestroy
tree_ptr
ECC buffer overflow
memory leak
ARCHIVE included directory: %s\n
invalid XAT entry key %zu
could not get a free pos from cache
files
    out set, outSize=%zu, outSHA1=
creating archive file stream
Control stream init
open %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/GenerateBOM.c
waiting for I thread
SIZE MISMATCH
StringTableAppend
parseProfile
writing entry data YDA
filename: %s\n
CompressionConsumerProc
ArchiveTreeCreateFromIndex
IFileStreamCreateWithFilename
Writing chunk
Encoder: %s\n
BZ2_bzDecompressInit
too many entries
init entry_ready
DATA_EXTRACTED
MemBufferFlushToBuffer n is too large: %zu
SharedArrayPush: pthread_mutex_unlock failed\n
SharedArrayEnqueue
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ArchiveTree.c
reading from control stream S=%lld
Regular file is missing DAT blob: %s
processPatchThreadProc
could not resolve qualifier (type %d): %s
SharedBufferFlushToStream
Path too long: %s
Error compressing file
bad # of allocation requests
%12zu ARCHIVE\n
???
input controls already present
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/BXPatch5.c
storeCachePos
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ExtractClones.c
  output manifest: %s\n
aaFileStreamPWrite err=%zd buf=%p n=%zu off=%llu
OFileStreamWrite
Missing call to GetWorker before RunWorker
Invalid cache size
aaCacheStreamPRead
ParallelArchiveECCFixCommon:\n
new size out of range: %zu
AAByteStreamSeek
invalid block size
Can't shrink resource fork: %s (current %u, target %u)
flushing shared buffer
mismatch in hlink entry count
lzbitmap
pthread_attr_init
Second pass fixup failed: %s, compression_type=%d (expected %d), resource_fork_size=%u (expected %u)
ECCGenerateThreadProc
rawimg_init_algorithm
ARCHIVE entry with invalid cluster mapping: %s\n
bad controls
inserting root node
Truncate on compressed stream failed
read
opening file: %s
In-place patch matching entry %u\n
  archive block size: %zu B\n
  override mode for directories: 0%o\n
node has a first child, but no last child
lseek
Diff stream init
[%7d] end: %s\n
archive read failed
VIndex
IGNORE excluded entry not present in output: %s\n
XAT
SharedArrayInit: pthread_mutex_init failed\n
vacating page in file
inPatch[%zu] is not NULL
aaCompressionOutputStreamClose
delta
Invalid entry state
fork footer
unique
aaCacheStreamSeek
ParallelArchiveECCGenerateCommon:\n
%5zu | %s | %4d | %10llu | %10llu | %d | %d\n
seek temp file
%zu controls in patch (%zu B allocated)\n
ThreadPipelineDestroy
invalid header in input stream
extra bytes found in file
loading profile: %d
Unsupported file type: %d
malloc
encode XAT field
read patch header
%s read
writing archive metadata twice
invalid character in mode: %s ('%c')
loading directory %s
reading from input stream
%12lld entries stored\n
resolveSameThreadProc
PRC
yaa_encodeHeaderField
%12llu entries in input archive\n
aaFileStreamPRead
%d (old=%d) ino=%llu size=%llu -- %s\n
BufferDecoderInit
DirectoryDiff
XAT value is too long to be stored in YAA archive (%zd B): %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACompressionStream.c
no free pages
compression
Digest stream init
%12llu clone clusters\n
Loaded 1:1 patch from cache: %s\n
invalid archive entry, PAT/TYP missing
Invalid entry, no TYP field
Acquire bufferEmpty\n
bad fork compressed
transcodeOThreadProc
setxattr: %s
LZRAVEN
ParallelArchiveECCVerifyCommon
Missing patchFilename
AFR
write DAT blob
io_set_nocache
control sequence broken
ParallelArchiveDBCloneWithSet
calloc ipos
duplicate fork
Generating %s directory patch\n
reading from control stream
ThreadPipelineGetWorker
Storing entry path
storing XAT
os
Reading input file magic failed
%12lld header size\n
  %s: %s\n
0123456789abcdef
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Search.c
getting worker from pipeline
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c
ECC generation failed
AUTO MKDIR new directory uid=%u gid=%u mode=0%04o parent_gid=%u: %s\n
%12zu symbolic links\n
compressed content
    inControls is NULL\n
Invalid block header payload=0x%llx raw=0x%llx block=0x%llx\n
  %llu B, %d entries\n
writeMetadata
creating database write request
storeFileContents
Missing HLO field
copy preserved
reading link: %s
reading block header at offset %llu
serializing fields
patchFilename is not a regular file: %s
getComboControlsFromMergedDiffSegmentVectors
Invalid compression type %u in decmpfs xattr
convertBegin
aaMalloc
PagedFileRetainIn
PagedFile: storing cached output page to file\n
invalid path: %s
extractInsertEntry: %s
Compressing the file: %s\n
writerReceiveData: %zu\n
fixOpsForHardLinkClusters
resolving ACE qualifier: %s
- %s\n
Not a regular file: %s
Moving %s to %s (1st attempt)
Closing paged file, input size: %llu B, output size: %llu B, bytes read: %llu B, bytes written: %llu B\n
Unsupported file type: %07o (%s)
pc_array_indirect_sort
mknod %s
manifest doesn't provide DUZ for regular file %s
%12u ECC parity size per block\n
fileSessionClone
Running %u threads to expand %u nodes (%u per thread)\n
get temp dir
ThreadPoolGetWorker
generating parity block %llu\n
[%d] terminating\n
aaFileStreamWrite err=%zd buf=%p n=%zu
storing blob data
excludeList
SegmentStreamCreate
OK
processing failed for entry %zd\n
temp file write
cacheRead
dispatch_block_create
lstat after readdir failed (errno=%d): %s
archiveTreeRemapNodes
[%7d] FIFO: %s\n
fileRequestWrite
Extra bytes in patch (ignored)
Invalid in segment in patch
OEncoderStreamCreate
Input buffer size mismatch: expected %llu B, got %llu B
%12lld entries added\n
FIRMLINK directory: %s\n
open archived file: %s
missing LNK field: %s
read failed
%12lld entries fixed\n
bad chunk position
%12zu ECC buffer size\n
Post-processing ctrl for in-place patching, %u pages\n
Destroying state with non-empty deferred queue
expanding archive tree range
encode DEV field
slink %s -> %s
Attr fixed: %s
invalid aliasCapacity
SharedArrayInit: pthread_cond_init failed\n
ArchiveTreeCreateFromDirectory
PROCESS_ON_RETIRE
Failed to set dir attributes
parsing gzip header
%s rule [%s] exact match: %s\n
Main
inPath == outPath is not supported
invalid patch header
invalid out,outSize
clusterLookup
Updating entry state
null
ParallelArchiveOLDWriterCreate
Input
loadFileContentsEx
sysctlbyname
Thread shutdown
too many blocks
  patch file: %s\n
create archive payload stream
processEntryThreadProc
acl_set_file: %s
SRC is empty
%12lld combo patches cache updates\n
resize stream
parent node was not processed first
unexpected read call
invalid option in mode: %s (was '%c')
creating directory tree
Invalid patch length
loading manifest %s
%12llu redundant bytes in clones\n
yaa_setEntryXAT
invalid JSON state
getxattr
patch has been truncated, can't expand archive payload
copy failed: %s to %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c
Stream write failed
Truncated ECC buffer
%12llu fixed bits\n
  compression: %s\n
close: %s
blocks: %zu\n
%s_tmp_XXXXXX
HLC
ArchiveTreeCreateWithRootEntry
ParallelCompressionAFSCStreamWrite failed with status %d
creating compression stream %s
Reading chunk
Invalid YEC blob size
read error: %zd
Release bufferEmpty\n
error: read more bytes than requested: %zd (requested %zu)
setEntryAttributes: %s
reading block header failed
clearEntryXAT
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c
apfs_diskimage_map
ParallelCompressionOStreamCreate
PagedFileReleaseIn
BXDiff5 patch control payload: %zu B\n
%12lld entries in manifest\n
compression_stream_init
Invalid compression algorithm
inFlightQueueInsert
rawimg_create_with_path
%12zu IGNORE\n
processDATBegin
processDATPayload
mkdir %s
moving input page from cache to disk
ParallelCompressionAFSCCompress
n threads: %d\n
SimStreamSimulate
%12zu entries with ACL blob\n
fileRequestClose
init buffer
invalid char %c %s
Loaded directory: %s (%.1fs)\n
PagedFile: vacating file pos\n
ImageDiff: Processed copy forks: %zd controls\n
in[%zu] is not NULL
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c
ParallelArchiveVerifyDir
patch file
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/BlobBuffer.c
markFilesMatchingPrefixArray
Invalid resource fork xattr
missing FLG field: %s
running transcoder I thread
seek to patch beginning
forceInPlaceControls
BXDiff5 patch archive payload size: %zu B\n
fullReplacementBXPatch5
threadPipelineWorkerThreadProc
reading payload failed
LINK: %s\n
%12llu clone entries\n
create output stream
moving output page from cache to disk
update parent depth
%12lld diff payload size\n
computing patch: %s
truncated entry payload: %llu B missing
%12lld entries compared\n
ParallelArchiveDBSetCreate
copy header extra fields
aaFileStreamFlush
-- thread %d:\n
Paths
remap_page
bad fork size
invalid segment offset: %llu
PATCH different files: %s\n
Payload stream init
%12llu final available blocks\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/PagedFile.c
updating tree depth
aaDecompressionStreamRead
Truncated control stream
%12zu resolved entries\n
expandDirRangeThreadProc
LargeFile: Constructed %zu controls in %0.2f (s).\n
process_output_block
aaCacheStreamPWrite
mutex lock
SharedBufferCreate
bom_info
missing SIZ field: %s
name
Truncated add stream
invalid valueType in field
acl_add_flag_np
invalid reverse index for IN
ParallelArchiveDBRequestOpenForReading
  cache URL: %s\n
%12u entries merged from %s\n
CLC
pc_array_compact
allocating blob buffer
fork_write_index
archiveTreeUpdateDepth
IFileStreamRead
ParallelArchiveExtract
BXDIFF_MATCHES_PROFILE
readining from database
Unknown patch cache URL: %s
rawimg_remove_fork_duplicates
checkAndFixPayload
truncated stream payload
%12zu entries in archive payload\n
encode PRC field
    inPatch is NULL\n
  diff level: %d\n
Remove
hw.perflevel1.physicalcpu
encode
computing file digests: %s
  soft memory limit: %llu MB\n
filePatchCacheUpdate
sorting tree
Truncated decmpfs xattr
reading compressed block %zu
invalid extra field key: %s
bxdiff5SetIn
mkstemp
inFlightQueueStoreEntryEnd
setEntryAttributes failed
blob store
ECCFixThreadProc
MemBufferIncreaseCapacity
data not locked
snprintf
ArchiveTreeCreateFromArchive
ParallelCompressionAFSCStreamOpen failed: %s
allocating buffer
non fork
%12u archive stream switches\n
%12lld bytes stored in regular files\n
decoding compression payload
Min free pages reached: %d\n
File is too large to be patched in place
AAFileStreamOpenWithFD
WRITING
inoTable allocation
invalid input PAGE
string table creation
largefile controls
Flush on underlying stream failed
MemBuffer is not allocated
tempStreamTruncate
nRefs inconsistency
SharedArrayDequeue
archive tree creation
expandDir
OArchiveFileStreamWrite
reading from payload stream
[%7d] SOCKET: %s\n
moving thread data to main state
patch_apply
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Convert.c
r,c=2
getting full path: %s
ctrl_reader_create
getting new entry path
%12zu character special entries\n
yes
OArchiveFileStreamDestroyEx
Blocksize: %llu\n
inFlightQueueStoreBlobs
creating index file stream
fingerprint_consumer
Invalid ECC variant: %u
full path too long
File patch cache path is not a directory: %s
ParallelArchiveSort:\n  input archive: %s\n
getting disk usage: %s
initFilterState
mkfifo %s
creating ECC context to get YEC
%12lld entries selected\n
inserting XAT xsize: %s
yaa_decodeACL
fileRequestRead
Opening paged file %s, %u pages in file, %u pages in cache, %u pages total, memory usage: %zu B\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiff5.c
BZ2_bzDecompress error %d\n
inserting path to entries: %s (%s)
%12lld 1:1 patches cache lookups\n
Key capacity is too low, %d bytes needed
set output attributes
invalid block header
Rules from %s to %s (include not in output): %s\n
checkOps
invalid input for ArchiveTreeInsert
mode should specify either 'w' or 'r': %s
Only one default database is allowed
creating output file: %s
markFilesMatchingPrefix failed
path too long
io_set_nocache %s
OEncoderStreamWrite
insertion failed in string table
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c
getcwd failed: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection.c
encode SH2 field
,o=%llu
invalid session URL: %s (invalid engine chars)
ACL
currentWriteBufferFull
invalid pos
out access out of range
truncated read: %s
storeBlock
array too large
SemRelease failed
extractSubtreeData
Truncated block payload (%lld/%llu bytes read)
Invalid arguments
opendir %s
chdir failed: %s
unsupported entry type
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/ExtractSubtree.c
%s: generating %s -> %s\n
writing data segment
invalid size=%llu
MutexDestroy
MemBufferTransmit
creating diff match lookup object
AAMemoryInputStreamOpen
UID
SHA256 hash collision: %s
PagedFile: assigning cache[%u] to new output page %u\n
AACompressionOutputStreamOpen
socket failed: %s
chunks too large
manifest doesn't provide FLG for entry %s
encode GID field
extractEndProc
mode: w\n
ARCHIVE different files, not in patch range: %s\n
concatPath failed: %s
%i dangling reads
  %u free pages in file\n
cloning file, falling back to copy, failed: %s
patch_read_header
%12zu KEEP\n
encode ERR field
filePatchCacheOpen
Expanding resource fork
 LargeFile: Block = %5u, %5u K cache, %6zu controls\n
rawimg_digest_worker
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/BXPatch4.c
building archive tree
inserting new node
AAByteStreamPRead
Free pages after diff controls: %u\n
Invalid decmpfs xattr
%12zu hard link entries\n
Invalid manifest, HLO without HLC
cache lookup failed (ignored): %s
    inControls set, nControls=%zu, inPlace=%d (%zu MB)\n
verifyDirBeginEntry
%s/%s
setEntryACL
ThreadPoolDestroy
reading node segment
entry is not labelled: %s
TYP
Diff
EXTRACTED
pending compressed fork
invalid path
Invalid blockSize: %u
OFileStreamSetPos
write to stream failed: %s
Reading decmpfs
loading archive tree
createTree
locateBlock failed
lstat
lzma_code error %d\n
File comparison failed: %s vs %s
ParallelArchiveConvert
block decompression failed
parsing YAF metadata field
invalid key size: %zu
%12llu final blocks\n
Unsupported file type [%c] %s
opening archive file: %s
pthread_key_create
removexattr failed for name=%s: %s
lseek failed
digest mismatch
invalid hard link index
%12zu invalid entries\n
%12llu redundant bytes in hard links\n
ForkOutputStreamClose
writing EOF
%12zu FIFO\n
copy fork not found
ftruncate
%12lld bytes stored\n
extractPayloadProc
resolveFields
locking chdir_mutex failed: %s
failed to join decoder thread
copy fork
transmitting entry payload
    in set, inSize=%zu, inSHA1=
Exclude
encode header field
writing data to temp file
  override UID: %u\n
non unique
Input digest failed
ParallelArchiveECCFixCommon
%12llu bytes in regular files (%.2f %cB)\n
AAByteStreamTruncate
Loaded 1:1 controls from patch %zu: %s\n
c option is invalid in write mode
Storing symlink path
%12zu block special entries\n
Not a directory: %s
  override GID: %u\n
patch_write_metadata
segment=%zu offset=%llu size=%llu\n
write error: %s
bxdiffControlsWithMatches
DIFF STREAM: I=%zu OPOS=%llu IPOS=%llu NDIFF=%llu NARCHIVE=%llu IDELTA=%lld\n
[%7d] CLONE %s -> %s\n
hlink_tree
joining resolve thread
encode BTM field
malloc ACE
Output fields:         %s\n
  output directory: %s\n
AAJSONInputStreamOpen
invalid user ACL callback return value
metadata entry was not written
block size: %zu B\n
starting task
encode ACL field
CKS
inserting tree node
collecting YAF buffer
rawimg_create_with_stream
extractClonesBegin
convertPayload
readlink returned an empty string: %s
truncated write: %zd/%zu
aaByteStreamSimulate
Raw cpio/yaa archive payload\n
reading archive header
processing DAT payload
algorithm: %s\n
ParallelArchiveOLDWriterAddEntry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/DirectoryPatch.c
  skip diff payload: %s\n
pthread_once
io_preallocate
size inconsistency: diff + archive != out
ParallelCompressionAFSCStreamWrite
Pipeline failed
reading block payload
%12lld entries processed\n
BXDiff5 patch headers: %zu B\n
Allowed output fields: %s\n
%llu entries failed to extract
ARCHIVE full replacement: %s\n
load patch: %s
link path not found: %s -> %s
cached input page does not have a file position
io_hint_static_content
bad flags
invalid patch, input before buffer
markFilesMatchingPrefix
cloning %s to %s
archiveTreeFromArchivePayloadProc
update node depth
%12zu B in state blob storage\n
truncated header
  input manifest %d: %s\n
aaInSituStreamOpen
cache update failed (ignored): %s
create output path
archiveTreeFindPath
Invalid entry state [%d] %s: %s
n > %d not supported
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/Read.c
%12lld raw archive size\n
ParallelCompressionAFSCStreamClose
reserving extra fields
too many controls
bxdiff5ReadInControlsFromInPatch
patch_write_controls
loadFileContents
stat failed: %s
    - %s stream: %llu bytes\n
Input fields:          %s\n
path too long in header
invalid patch payload size
Warning: extra bytes in patch (ignored)\n
Diff stream applied
truncated block header
encode SIZ field
storing depth in AUX
looking up cluster
rawimg_compact
ARCHIVE_NOREMOVE symlink attribute changes only: %s\n
KEEP dir: %s\n
patchCacheOpenFromURL: %s (continue without cache)
%12zu entries in diff payload\n
file type is not supported (st_mode=0%o): %s
AAFileStreamOpenWithPath
rawimg_add_fork
aaCompressionOutputStreamFlush
storing link
%zu failed entries reported
writing PENDING in cache entry failed
    out is NULL\n
inFlightQueueOverrideAttributes
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c
ParallelArchiveDBSessionCreate
REMOVE contents of removed directory: %s\n
SharedBuffer invalid capacity: %zu
segment_add
outProc write
invalid args
Loaded manifest:  %s (%.1fs)\n
  input directory %d: %s\n
invalid fields storage type
inPath is not a directory: %s
patch_verify_header
failed to start encoder thread
too many elements
  Input data SHA1: %s\n
Invalid ECC buffer size
applyRules
DirectoryPatch: %llu errors after processing the diff payload
[%7d] retiring %s: %s\n
storing base block
fingerprint_worker
%12zu AUTO MKDIR\n
movePage
extents
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c
truncated write
OBufferedStreamWrite
ParallelCompressionGetCompressedSize
cache too big
ARCHIVE include: %s\n
LNK
fileRequestOpenForReading
Reading DAT blobs from database\n
combo delta
directoryPatchBegin
Decoding YAA header
ARCHIVE differing types directory: %s\n
encode LNK field
Invalid number of inputs: %zu
extractBeginProc
merging archive tree: %s
OMemStreamCreate
ILowMemoryDecoderStreamRead
ctrl_reader_get
OEncoderStreamThreadProc
%12llu fixed blocks\n
  %u total pages\n
merging trees
reading chunk
processFileHeader
%12zu B written for header\n
allocating extraFields
%12u entries selected\n
AAJSONInputStreamRead
writing metadata entry header
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelArchive/YAACommon.c
ParallelArchiveWriteEntryData
too many bytes received
%12lld bytes not stored in hard links\n
bad extent size
MutexInit
include path doesn't exist, or is not a directory: %s
out size mismatch in patch
Reading chunk sizes
entry expected to be a directory: %s
DEV
invalid ACE qualifier type
[%7d] begin: %s\n
invalid blob size: %llu
Invalid session URL: %s (unknown engine)
Opening file patch cache in directory: %s\n
Invalid chunk size
Acquire bufferReady\n
invalid XAT entry size
Invalid file: %s
patch_write
invalid prune operation: more than one node at depth %u
F_PUNCHHOLE failed
writing output
storing page
hlink %s -> %s
SegmentStreamPRead
missing controls for input %zu
retrieving AFSC metadata: %s
invalid block ID in write thread %lld
encoder failed
writing patch to disk
segment=%zu offset=%llu size=<to EOF>\n
0707070000000000000000000000000000000000010000000000000000000001300000000000TRAILER!!!
%12llu hard link clusters\n
AFSC compression failed: %s
ThreadPoolCreate
invalid argument for '%c' in mode: %s
verification failed: %s
pending requests
seekTo
Input doesn't match any of the expected patch inputs (in-place)
GetBXDiffMaxMemoryUsage
missing hard link target entry: %s
invalid variant %u
creating encoder failed
bad extent
Invalid patch
reading archive
writing chunk
Allocating deferred stack
running transcoder O thread
SemDestroy
[0x%08x] %{public}s
[0x%08x](warning) %{public}s
```
