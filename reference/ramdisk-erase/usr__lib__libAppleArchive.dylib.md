# `/usr/lib/libAppleArchive.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 851,616 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2208)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/usr/lib/liblzma.5.dylib (compatibility version 6.0.0, current version 6.3.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,924)

First 2,500 of 2,924.
```
Dropping %llu bytes at %llu, needed=%llu bytes, type %s\n
invalid type %d, expected HASH
Segment key derivation failed
fullReplacementBXPatch5
Archive identifier size mismatch when resuming
AACustomByteStreamOpen
invalid header size
$)
yes
getFileDiskUsage
 LargeFile: Block = %5u, %5u K cache, %6zu controls\n
AAEntryXATBlobRemoveEntry
ECC65537CheckAndFix
acl_set_permset_mask_np
getSegmentFile
creating fs object: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAChunkOutputStream.c
ctrl_reader_get
invalid sizes in manifest
Invalid ECC algorithm
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAUtils.c
invalid pax header
runWorker
aaAssetDecodeStreamSetParameterPtr
creating new worker
importing public key
archive stream read error (header)
ImagePatch: Patch not created with in place. No bound on needed excess space.
append YOQ
\\E/)
Invalid archive stream
pc_array_compress
inserting YEC: %s
Truncated block payload (%lld/%llu bytes read)
treeSub
Invalid arguments
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetDecompressionStream.c
accumulating blob data
MutexUnlock
AEADEncrypt_None_MAC256_KEY256
aaCacheStreamPRead
close
 ACL
empty controls
storing deferred entry
inserting path in table
header payload too large
copy
,0x%08x
out access out of range
Segment %u: dequeue\n
aaSequentialDecompressionIStreamOpen
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/PagedFile.c
(^\\Q
%12llu differences ignored\n
AEADDecrypt_AESCTR_MAC256_KEY640
MemBufferIncreaseCapacity
read
entryDestroy
extractStreamEntryEnd
invalid type %d, expected BLOB
%s\n
Async stream reported errors
new size out of range: %zu
Name out of range
compute patch
writing header blob
/XXXXXXXX
rawimg_create_with_stream
Cluster header received: %zu B\n
invalid image map JSON
Thread creation
String table insert
Eerror getting blobs from header
aeaCryptoInit
parsing profile: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBasicStreams.c
loadDecmpfsXattr
PagedFile: moving page from file[%u] to cache[%u]\n
initializing ACL field from path
invalid stream
invalid header magic
extractor stream
streamConsumerProc
bad image
inserting DEV: %s
reading magic bytes\n
creating encryption context
AAByteStreamTruncate
callback cancel
MemBufferFillFromBuffer n is too large: %zu
invalid compression algo
ParallelCompressionAFSCGetMetadataFD
starting blob
AAHeaderGetFieldTimespec
creating YEC field
fetching ranges
BXDiff5 patch diff[%zu] payload: %zu B\n
decode stream reported errors
write blob to stream
ThreadPoolGetWorker
fork chunks
processPadding
copy fork
Stored remaining range is not a subset of initial range
Invalid segment offset: %llu, size: %zu
aaEntryXATBlobApplyToFD
invalid ACL entry tag %c
insertion failed in string table
allocating blob buffer
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c
Total size %zu MB\n
enqueue chunk write
invalid read blob request
aaByteStreamSimulate
invalid offset=%llu, size=%llu for fd
%12zu chunk size (B)\n
AAPathListNodeNext
extractThreadFailEntry
Relocatable object file
invalid resource fork for type
invalid cache pos
operation aborted
Loading segment
uncompressed_size
creating extract stream
inserting GID: %s
graisPRead
creating worker pool
AAPathListNodeGetPath
 CTM
getting blob field
extract cluster entry failed: %s
aeaContainerReencrypt
AARangeInputStreamOpen
readdir on dataless directory: %s
AAExtractArchiveOutputStreamSetQuarantine
removexattr failed for name=%s
Patch matching entry %u\n
writing container headers
apply YEC (extract)
ace_check_entry
calloc ipos
 (0x%x %i %i %u %llu %llu %u)
%12llu B file size\n
compressed stream detected : try compression_tool
Decoder: %s\n
AAByteRangeCreate
Invalid item type %d
setting attributes
createFilesystemObject
qualifier too long
afscStreamOpen
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAsyncStream.c
AAArchiveStreamProcess
Input doesn't match any of the expected patch inputs
AAMemoryOutputStreamCloseWithSize
reading header magic
could not get a free pos from cache
sendEOF
creating internal buffer
expected ref_count=1 for terminating thread
Encoding failed
inserting UID: %s
storing patch: %s
A file composed of other Mach-Os
Warning: couldn't set F_NOCACHE on paged file\n
workerAlloc
adding item to the keychain: %d
Invalid input header
aaInPlaceStreamSeek
invalid XAT blob in manifest
cluster has pending entries %d/%llu
AAEntryACLBlobGetEntry
ARCHIVE (too small for patching): %s\n
lzbitmap
Padding received: %zu B\n
Invalid segment size in root header: %u
streamThreadProc
callback signaled abort
streamPWrite
pushSegmentData failed
%12u directories\n
SharedArrayPush: stack is full\n
create access control
reading magic
AAHeaderSetFieldHash
alloc stream
PagedFile: moving page from cache[%u] to cache[%u]\n
invalid blob reference
file can't be fixed: %s
decompression failed
writing stream magic
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c
Segment decryption
extents
invalid archive
AATempStreamOpen
aeaOutputStreamWriterThreadProc
lstat: %s
truncated entry when header encoded
add HLC field
writing DAT bytes
aaAssetExtractorStoreCheckpoint
ThreadPipelineCreate
removeStreamWriteHeader
User cancelled operation
processing manifest
inserting IDX,IDZ fields
%5zu | %s | %4d | %10llu | %10llu | %d | %d\n
realign_fork
mem buffer creation
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetExtractStream.c
LZMA
Context can't be modified
corrupted padding
inserting SH1: %s
truncated read: %s
unlock
lstat after readdir failed (errno=%d): %s
Abort requested
AAHeaderGetFieldString
SemRelease
fcntl F_SETPROTECTIONCLASS
  In-place: %s\n
requested compression type requests inline storage
  %u free pages in cache\n
loading profile: %d
AEAContextSetFieldCallback
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/../Common/SharedArray.h
?
signing prologue digest
Segment compression failed
aeaContainerAppendSegment
Path too long: %s
creating YEC context
aaSegmentStreamProcess
invalid temp_dir: %s
invalid work dir: %s
StringTableAppend
Invalid public key size
Missing bytes in patch
AA entry missing/invalid PAT field
reading prologue
control_reader_create
SIZE MISMATCH
comboControls is not NULL
too many excess pages
computePatchesWorkerProc
aaFileStreamRead err=%zd buf=%p n=%zu
user cancelled in progress callback
xhdr %s: %s\n
PagedFile: moving page from cache[%u] to file[%u]\n
generating last cluster random MAC
segment_add
listxattr
moving input page from cache to disk
lstat %s
ForkOutputStreamPWrite
invalid PAT: %s
aaEntryXATBlobInitWithFD failed: %s
invalid YEC variant: %u
%12.2f encoding time (s)\n
invalid header state
open checkpoint path: %s
rename: %s
Chunk has already been written
creating file stream
in memory allocation for PagedFile
Invalid checksum mode
FAIL
Stream pread
Context creation
normalize
encoding entry
entry not found, or not a regular file
no digest info
RunWorker
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/BXPatch5.c
Extract archive\n
inserting FLI: %s
invalid ACE flags: 0x%016llx
rawimg_create_with_path
load container
AAChunkAsyncStream\n
generic controls
reading thread command, %zd
Min free pages reached: %d\n
istream read error
PagedFileReleaseIn
initializing YEC field from path
writing block header
generate random bytes
%i dangling reads
loadAndDecodeHeader_Ustar
writing page
Invalid encryption parameters
OArchiveFileStreamDestroyEx
lseek failed and pos < s->pos
process hlinks
extractStreamProcessDirs
init header
loading file contents: %s
  raw size: %llu B\n
aeaKeychainCreateAttributes
lzma_stream_decoder
streamWriteChunkData
invalid index in HLC/CLC/SLC cluster
mkdir failed: %s
max level reached
Invalid segment id\n
reading blob
entryCreate
Object archive BE
jsonPushLabel
decryptAsyncClose
(
inserting blob placeholder
message callback cancelled operations
creating workBuffer
aaHeaderAppendEntryAttributes
AAHeaderAssign
REMOVE (not in output): %s\n
(^
updating chunks
GetRange
mutex unlock
inserting LNK: %s
LNK blob
storeCachePos
getFreeCachePos
seekTo
invalid in,inSize
truncated read resource fork
xhdr value parsing
bytes remaining in obuf
SharedArrayPush: pthread_mutex_unlock failed\n
buffer full
ParallelCompressionAFSCGetMetadata
streamProc
creating symlink: %s
Error 0x%08x\n
GetLargeFileControlsWithStreams
building diff controls
no more writes possible
BXDIFF_MATCHES_PROFILE
<<< range %10llx %10llx\n
  manifest: %s\n
cloning file, falling back to copy, failed: %s
PagedFileDump
reading page
writing tool output
MemBufferDecreaseSize
can't generate a field from DAT, and keep DAT at the same time
resize stream
AEAContextCreateWithProfile
stateScanArchive
allocating final blob
internal streams
invalid signature size
AEAEncryptionOutputStreamCloseAndUpdateContext
received too many bytes %llu/%llu
writing output
no PAT field in header
loading XAT blob
addSegment
pthread_mutex_lock
applyYEC
Invalid tmp dir: %s
ctrl[%zu]: ndiff=%llu nlit=%llu\n
aaCompressionOutputStreamClose
invalid auth_data key
ctrl_reader_create
Invalid ECC buffer size
readdir_r
file stream already opened
Companion file with only debug sections
rawimg_init_algorithm
Main key derivation failed (%d)
archive stream write error (header)
aaReallocf
forceInPlaceControls
append MTM
invalid path
AAVerifyDirectoryArchiveOutputStreamOpen
SharedArrayInit: pthread_cond_init failed\n
largefile controls
fsync
Invalid segment index
SharedArrayPop
set PAT
bad input size
Password is too short
AEAD can't operate in-place
init buffer
Invalid signing public key in context
AADecodeArchiveInputStreamOpen
AAAFSCStreamOpen
read resource fork chunk
Invalid checksum mode for decrypt to file, at least 256 bits are required
AEAAuthDataCreate
ForceInPlace: %zu controls. Dropped %llu bytes to stay within budget.\n
qsufsort32
invalid compression type %d
append AFR
no overlapping segment found
aaFileStreamWrite err=%zd buf=%p n=%zu
mkostemp
afscStreamWrite
null
PagedFileRetainIn
Invalid compression type request %d
entry found in extract stream
Worker thread creation
Worker alloc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetExtractor.c
Chunk write failed
Refill buffer failed
rangeDataInsert
AAFieldKeySetInsertKey
Total time %.2fs, %.2f MB/s (%s)\n
pos not reached
ImageDiff: Constructed %zd combo controls.\n
truncated header
finalize resource fork
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection.c
%12llu requests processed\n
bad controls
async stream alloc
MemBufferFillFromBuffer failed
%12zu chunk size\n
generate random field
invalid header size: %llu
Mach-O
worker reported errors
Input retained
stateShouldCreateFileInCluster
AAFieldKeySetInsertKeySet
Directory expansion
reading file header
.XXXXXX
lockedStateReserveChunks
storing archive id: %s
Decode archive\n
Flush on underlying stream failed
threadPoolWorkerThreadProc
rawimg_set_fork_types
bad page
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAArchiveFileStream.c
bad chunk position
aeaDeriveMainKeyNew
Reading chunk data failed
append AFT
Invalid decoder state
AACompressionOutputStreamOpenExisting
unlockState
Blocksize: %llu\n
verifyDirectoryStreamClose
Invalid ECC variant: %u
istream read
Writing chunk data failed
entryMessage
Non supported entry type %u
Invalid magic bytes
generating random salt
MutexLock
aaFileStreamGetFD
byte stream read error
send request
.AssetExtractCheckpoint
ScryptDerive_KEY256
aeaInputStreamAuthenticatePadding
cacheRead
  - Variants:   %d\n  - Flags:      %llx\n  - # controls: %llu\n  - Patch size: %llu bytes\n    - Metadata: %llu bytes\n    - Controls: %llu bytes\n
not enough bytes received
chunkAsyncGetRange
pthread_join
 fork | %64s | algo |       size | compressed | V | C\n
bad extent pos
%12llu bytes in regular files DAT\n
Stream processing cancelled
areFilesEqual
updating YEC field
scanning manifest
Invalid temp dir path: %s
DSAVerify_ECDSA_P256
ImagePatch: Patching with excess space <= %d bytes.\n
extractThreadProc
prepare decmpfs header
  %u input pages stored, %llu bytes referenced\n
Main key derivation
missing IDX field
ECC applied 0x%08x: %s
HLC field found, not supported: %s
*** %s\n
no free pages in file
refill buffer
preallocating %llu B
decrypting signature
flushing chunks to stream
invalid ._ entry
entry defined multiple times in the same variant
storeFileContents %s
fstat failed
Caller cancelled
Segment %u: cached\n
invalid ACL entry type %c
invalid state
Segment decrypt
reading payload failed
  Output data SHA1: %s\n
convertStreamEndBlob
BXDiff5 patch total size: %zu B\n
extractStreamClose
invalid resource fork
getting entry path
ParallelCompressionAFSCCompress
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Utils.c
iterating to next non-empty blob
storeRemainingRange
String insertion failed
stateAggregateEntries
ARCHIVE (full replacement): %s\n
HMAC verification
clearing extended attributes
AAFileStreamOpenWithFD
get temp dir
stream read failed
unsupported parameter
expected match type PREFIX for MAPTO rule
match string is required for all rules
SharedBufferWrite
ImagePatch: Digest match. Copy input to output.\n
Invalid decmpfs xattr
%12zu bytes in chunks (%.2f MB)\n
storing new offsets
dat archive invalid
StringTableAppendTable
in[%zu] access out of range
creating shared command buffer
FIXUP (hard linked): %s\n
getting next worker
invalid input PAGE
Final FULLFSYNC
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiff5.c
BXDiff5 patch allocated: %zu B\n
is
bad image size
stream process
Segment %u: %zu B processed\n
importing full key
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACacheStream.c
AARemoveArchiveOutputStreamOpen
extractStreamWriteBlob
computing file hashes: %s
bad duplicate
Cluster header encryption key derivation
apfs_scan_diskimage
%12llu common, OK\n
Invalid worker_id
update resource fork
invalid directory: %s
write DAT
inserting DAT: %s
Truncated block header (%lld/16 bytes read)
CCKDFParametersCreateHkdf
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/SharedBuffer.c
aeaContainerLoadSegment
blockPRead
extractStreamSendEntryToRetireThread
blob too large
pushPaddingRange
    inControls set, nControls=%zu, inPlace=%d (%zu MB)\n
loading segment: %u
get field blob failed
invalid compression type
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEASequentialDecryptionStream.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAEncryptionStream.c
%12zu blocks per thread\n
dir/path too long: %s
aaEntryXATBlobInitWithFD
invalid ACL perms 0x%llx
aaEntryACLBlobApplyToFD
%12u requests\n
AEADecryptInPlace
 GID
patch_write_metadata
%12u segments in cache\n
loading file attributes: %s
truncated stream payload
inconsistency in nRefs == 0
path too long
Invalid hardness parameter
store remaining range
create
derivating secondary key
pending compressed fork
invalid XAT blob size
inserting path component in table
append FLI
no TYP
Output
DH callback
statfs failed: %s\n
aaEntryHashesInitWithFD
invalid entry final fd
invalid thread ID %d
%11.2f%% parity/data ratio\n
Hole fill
sending entry to retire thread
invalid blockSize in input stream
Reading chunk
fremovexattr
PagedFileReadAndReleaseIn
rawimg_verify
workerProc
%s
Archive path list\n
ImagePatch: Digest match. Output reconstructed.\n
stream not compatible
invalid blob sizes
Invalid thread command
DH callback returning invalid shared secret size
aaCacheStreamPWrite
Segment %u: stored in cache\n
AAPathListCreateWithPath
symlink %s
inserting BTM: %s
AAHeaderSetFieldUInt
invalid XAT index %u
cacheFlush
reading data segment
invalid xhdr entry
Fixed VM shared library file
AATeeOutputStreamOpen
aaFileStreamPWrite
storeChunkOffsets
PagedFileDestroy
expected valid YOQ field
in-place patching failed
extract stream reported errors
Dynamic link editor
%12llu blocks\n
rangeDataRemove
invalid mapto path: %s
isDirEmpty
removing header field
decryptAsyncProcess
nodeAlloc
copyStream
generating padding
temp stream
InSituStreamClose
aaEntryAttributesApplyToPath
Fat binary
AAAssetBuilderAddVariantArchive
threadPipelineConsumerThreadProc
setThreadErrorContext
dir name too long
AATempFileStreamOpenWithDirectory
invalid file sizes
ThreadPoolDestroy
RS65537\n
stateRetireRanges
    comboPatch set, comboPatchSize=%zu (%zu MB)\n
futimes
%12u blocks in cache\n
PagedFile: storing cached input page to file\n
load and decrypt last segment
Patch can't be applied in-place
aaCompositeChunkAsyncStreamOpen
MemBuffer write proc returned 0
getting archive identifier
write XAT
DST is not empty
encoding root header
Computing patches...\n
encode entry
storeDecmpfsXattr
extents overlapping
rawimg_load_chunks_from_stream
retrieving AFSC metadata: %s
no active entry or active thread
variant too large
Invalid uncompressed chunk size
concatExtractPathEx
workerCreateClusters
AAAssetBuilderGenerate
offset
Invalid hole size
inserting INO: %s
AAHeaderSetFieldString
acl_get_qualifier
AEAAuthDataGetEntry
a parent of path is not a directory: %s
patching failed: %s
createErrorContextKey
    comboControls set, nControls=%zu, inPlace=%d (%zu MB)\n
AAEntryXATBlobGetEntry
Demand paged executable file
read error: %zd
flushBuf
RNG failed
too little excess
storing compressed segment
fchflags UF_COMPRESSED
truncate to final size: %s
loadAndDecodeHeader_Cpio
Setting directories attributes (%s)\n
%12u entries with ACL field\n
%12zu chunks in cache\n
reading state
AATempStreamOpenWithDirectory
invalid blob segment
AAEntryXATBlobCreate
collector stream
truncated file
rawimg_add_fork
pcRead failed
reading from control stream S=%lld
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOCompressedStreams.c
corrupted stream
SET range %10llx %10llx -- %8zu\n
preallocation %llu/%llu B took %0.2f seconds (# of calls=%i)
RandomAccessDecompressStreamGetBlock
encrypt signature
Chunk still has holes
aaCompressionOutputStreamFlush
Final truncate
bad fork size
lzraven
Segment %u processed, offset=%jd, payload=%u, raw=%u\n
RawImagePatchInternal
invalid range
Patch %s\n
getComboControlsFromMergedDiffSegmentVectors
unsupported compression type: %d
Segment payload size mismatch
Invalid return type
InSituStreamPWrite
YAA entry missing/invalid PAT field
AAHeaderGetFieldUInt
encoderStreamWriteBlob
No-op patch matching, writing input\n
bad output size
setupContext
inserting SH2: %s
invalid ACE perms: 0x%016llx
Last block decompression
AAAsyncByteStreamProcessAllRanges
Scanning target directory failed: %s
reading from control stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAContextValidate.c
aaEntryACLBlobInitWithPath
creating XAT field
  checksum: %s\n
invalid file header
Segment write failed: offset=%llu size=%zu\n
fork footer
decryptAsyncGetRange
bad seek
Reading decmpfs
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAInPlaceStream.c
copy cluster header
entry already linked
stripAFSC
pc_array_append
blob size mismatch
scrypt
ECC generation failed
flushing buffer
%12llu B block size\n
inconsistency in nRefs != 0
closing AFSC stream
finishing blob
io_set_nocache
controls_create_with_variants
'H' LNK not a regular file: %s
write failed %zd
reading header
missing LNK
Filename is too long: %s
%12u symbolic links\n
AAHeaderGetFieldHash
clear header
Invalid segment sizes: payload=%u raw=%u
%12llu entries in archive\n
invalid size=%llu for fd
stateUpdateChunks
missing out
entry processing
Invalid output digest after patch application
processPrologue
getProfile
HMACInit_SHA256
Missing decmpfs xattr
loading file ACL: %s
exactly one output, and 0 or more inputs expected
encoderStreamWriteHeader
invalid nlink
AEAAuthDataRemoveEntry
derivating segment key
aaCacheStreamTruncate
AppleEncryptedArchive
opendir failed with errno=%d: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAExtractArchiveOutputStream.c
allocating header
aaCreateArchString
invalid AssetArchive DAT blob size
sending dat magic
creating dir: %s
Src check %c %s\n
%12llu final patch size\n
write blob
reading from input stream
OArchiveFileStreamCreate
patch doesn't allow in-place
finalizeResourceFork
loading last block
set YOP
invalid entry index %u
removing last segment
SharedArrayPush: pthread_cond_signal failed\n
Segment insertion
AEAKeychainRemoveItem
MemBufferIncreaseSize
    %zu active chunks\n
%12u entries with YEC field\n
AEADecryptAndExtractChunk
%s \"%s\"
SegmentStreamCreate
Hole creation
retire segment
computing file digests
increaseCapacity
%12s %s\n
write state
running worker
InSituStreamSimulate
PagedFileCreate
aeaOutputStreamWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c
chunkAppendHole
stateCollectorStreamWriteHeader
flush output buffer failed
digest
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c
get blob location
writing EOF
invalid path for name match: %s
no nodePrev/Next: %zd
process range
extractThread
processFileHeader
bxdiff5CreatePatchBackend
bad page index
too many hard links or inconsistent nlink/ino data in archive
DAT
Thread shutdown
invalid block ID in write thread %lld
read error
none
Invalid patch size
user error
invalid 'H' PAT
entry creation
init ops
aaByteStreamPReadExpected
Write failed
reading chunk
deriving signing public key
GetLargeFileControls
removing item from keychain: %d
hashing padding
linkpath
aaFileStreamPRead err=%zd buf=%p n=%zu off=%llu
NOP received
treeRebalance: %zd
F_PUNCHHOLE failed
some output bytes are missing or referenced more than once after archive expansion
processEntry
ftruncate
hw.physicalcpu
Extraction failed: %s
size inconsistency: diff + archive != out
read resource fork
%12zu symbolic links\n
realloc_keys failed
donor is not a regular file: %s
alloc XAT entry
read state
invalid rule type: %u
Signing
AEADecryptToFileChunk
updating label
arm64_32
Invalid stream type
decodeStreamLoadHeader
invalid size
bxdiff5SetOut
stateCreate
dirInsertEntry failed: %s
rawimg_compact
no chunk info
pc_array_indirect_sort
no
couldn't read enough header bytes from compressed file
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBuffers.c
  Metadata: %llu bytes\n  Controls: %llu bytes\n
invalid raw size
computing segment checksum
ImagePatch: Preallocation failed.
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFileAsyncStream.c
Client context callback returned an error
retireEntryRange
truncated node path
disable AFSC by clearing UF_COMPRESSED
flushOBuf
inserting padding range
end of stream cancel
Invalid segment size in cluster header
loading entry blob
 [%s, %s, %s]
ParallelCompressionAFSCStreamWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AATempStream.c
AAChunkOutputStreamOpen
arm64
resizeResourceFork
truncated: %s
compile regex (err=%i, msg=%s)
SharedArrayInit: pthread_mutex_init failed\n
decoder failed
write failed
convertStreamToNextNonEmptyBlob
in[%zu] is not NULL
aaEntryHashesInitWithPath
size
Invalid profile: %u
writing data to temp file
Creating hard links / clones\n
Not a directory: %s/%s
volumes
DIFFER  %s (%s)\n
(stream based)
aaSimStreamOpen
SharedBufferFlushToStream
invalid header in state
add_control
creating state
<target dir>
stat failed: %s\n
AAHeaderSetFieldFlag
x86_64h
reading from tool pipe
pos out of range
inserting SH3: %s
%12llu fixed bits\n
%12llu bytes processed in chunks (%.2f MB)\n
skip dataless: %s
invalid extractor state (blobs)
aeaContextUnlock
get AFSC attributes
stateCreateEntries
no IDX
writing data
invalid compressed buffer
encoderStreamClose
parsing entry header
append to ibuf
decompressing block
Async stream returning EOF, but we still have ranges in flight
AACustomArchiveStreamOpen
inProc read
  ECC variant: 
ThreadPipelineFlush
no valid DAT entry for cluster %d/%llu
clusterInit
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACompressionStream.c
AAFileStreamOpenWithPath
Client processing callback reported an error
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtract.c
cachePageGet
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAPathList.c
stateCollectorStreamWriteBlob
decoding compression payload
SharedArrayInit: malloc failed\n
    - %s stream: %llu bytes\n
stateScanManifest
append_field
realloc_fields failed
setup header
re-writing last block
digesting prologue
Stream thread creation
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFile.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/StringTable.c
malloc %u threads
iterating to next blob
workerDeferEntry
afscStreamCloseWithState
invalid request
flushToResourceFork
invalid AssetArchive stream (missing manifest)
invalid input index
streamEnqueueWriteChunkToStream
open
invalid payload size
subArchiveCreate
creating AFSC stream: %s
mutex init
%12llu data bytes written\n
Abort
end entry
inserting CTM: %s
stateStreamEntryBlob
writeOBuf
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/LargeFile.c
corrupted archive header
resizing resource fork
invalid state when resizing resource fork
writeProc
AAAsyncByteStreamGetRange
io_set_nocache %s
Input buffer size mismatch: expected %llu B, got %llu B
File too small for AFSC
 SH5
attributes from header
Invalid number of inputs: %zu
BXDiff5 patch archive payload: %zu B\n
loading dir entry
searching item in keychain: %d
  Input data SHA1: %s\n
Write to stream
streamCheckAndWriteChunksToStream
string table append
read blob from archive
GPU program
Closing paged file, input size: %llu B, output size: %llu B, bytes read: %llu B, bytes written: %llu B\n
dispatch_block_create
append UID
applying ACL blob: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStream.c
Corrupted stream
verifyDirectoryStreamWriteBlob
Invalid segment bounds
AAMemoryInputStreamOpen
Invalid profile value: %s
tempStreamTruncate
YAA device entry has no DEV field: %s
Invalid cluster header size
CheckAndFix: %s
Key generation
Invalid state
finishing entry
aaEntryXATBlobInitWithPath
size mismatch: %s
reading segment data
Segment encryption failed
serializing state
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAInplace.c
aaForkOutputStreamOpen
creating directories
process dirs
cluster entry query
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAArchiveStream.c
compression
decrypting segment
archive stream write error (blob)
Digest stream init
nlink mismatch
clearing UF_COMPRESSED
Can't allocate header/footer
invalid AssetArchive, extra blobs
invalid DAT blob
Invalid segments per cluster count in root header: %u
AEADecryptionDirectRandomAccessInputStreamOpen
IMemStreamCreate failed
- input %zu\n
%12zu entries selected\n
bad map
invalid AEA stream
removing DAT field
Scanning archive\n
opening file
RNG
%12zu block count\n
IFileStreamCreateWithFD
lockedStateReserveActiveChunks
write returned 0
SemTimedAcquire
PagedFileRetainOut
processSegment
CCDeriveKey
Write
createThread
Second pass fixup succeeded: %s
AEAContextCreateWithEncryptedStream
realloc_keys
Free pages after diff controls: %u\n
aaByteStreamWriteExpected
Parity buffer out of range
Invalid entry: no TYP field
AAJSONInputStreamRead
  %u free pages in file\n
ECDHE_P256_Recipient invalid sizes
0123456789abcdef
AEAContextGetFieldUInt
treeDelete: %zd
Invalid entry missing TYP field (skipped)
append MOD
update_field_sizes failed
gname
obuf full
flush cache
workerAllocBuffers
truncate temp file
Unsupported signature mode
%12u entries\n
alloc ACL entry
mmap file segment
 XAT
aeaContextCreateWithPrologue
chunkWriteToStream
dataless dir error: %s
update_field_sizes
%s variant <%s> | %llu bytes | %zu extents | %zu forks (%llu/%llu) | digest=%s\n
InSituStreamPRead
Invalid dir: %s
stateInitOps
invalid input path
Invalid container offset
reading padding
invalid imbalance: %d
reading from payload stream
acl_create_entry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEARandomAccessDecryptionStream.c
compressed fork
InSituStream: pages: %i file, %i written, %i remapped, %i free, %i excess (%iK)\n
Invalid worker id
Root header encryption
    inPatch is NULL\n
SharedArrayEnqueue
open %s
controls_combo_enforce_copy_fork_boundary
chunkWriteData
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARangeInputStream.c
%12u workers\n
PagedFile: moving page from file[%u] to file[%u]\n
OBufferedStreamWrite
truncated write: %s
 AFT
getxattr failed for name=%s
AADecompressionRandomAccessInputStreamOpen
AAChunkAsyncStreamOpen
pushControls
Invalid KeySet string length: %zu
aaFileStreamFlush
store padding
/System/Library/Filesystems/apfs.fs/Contents/Resources
inserting XAT: %s
mapping decode stream progress
DIFF STREAM: I=%zu OPOS=%llu IPOS=%llu NDIFF=%llu NARCHIVE=%llu IDELTA=%lld\n
remaining.tmp
invalid HASH subtype: %d
chunkCount
%s%s/%s
aaAssetDecodeStreamDone
RawImageDiff
workerApplyAttr
pushSegmentRange
Invalid password/salt
Invalid signing private key in context
aaEntryAttributesInitWithPath
depth loop
sending command
Insufficient buffer capacity
Invalid compression type %u in decmpfs xattr
%12zu regular files\n
Capacity increase
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldACL.c
COPY: %s\n
Segment data failed verification
AEA_SCRYPT
aaCheckAndFixWithPath
x86_64
moving output page from cache to disk
lockState
createThreadErrorContext
- output\n
Header creation
Worker: encode block %5lld: %7llu => %7llu\n
Fat binary BE
truncated stream header
copy, no compression
%s stream: %llu bytes -> %llu bytes\n
resizeStream
inserting AFR: %s
AAHeaderRemoveField
writing data blob
DHERecipient_ECDHE_P256
Invalid resource fork size request: %u
deriving fields from header
Invalid prologue
chunkAppendData
inserting TYP: %s
unlock container
unsupported parameter key
SharedBufferAbort
%12u worker threads\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetDecryptionStream.c
entry size mismatch
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAEncodeArchiveOutputStream.c
AFSC stream close
Control stream init
Container size limit reached
creating DecryptAsyncStream
invalid dir entry
AAAssetExtractorDestroy
AAFieldKeySetCreate
ADDED   %s\n
Invalid patch header
truncate failed
%12zu other entries\n
writing archive
Truncated block header (%lld/16 bytes written)
StringTableCreate
tmp
invalid ACL index %u
Prologue received: %zu B\n
bad donor for: %s
Invalid stream magic
aaAssetExtractorCreateCommon
looking up AFSC data: %s
Invalid segment state
Invalid data size
aeaOutputStreamRunThreads
bad header
get a valid chunk from cache
flushing obuf
Invalid AEA container (auth_data_size)
XAT blob allocation
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c
Reading chunk sizes
openProc
invalid YEC blob
LocalArrayPush
write
Warning: extra bytes in patch (ignored)\n
Diff stream applied
Missing resource fork xattr
ParallelCompressionAFSCFixupMetadataEx
vacating page in file
decryption stream
ThreadPipelineRunWorker
unique
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARandomAccessDecodeAndExtract.c
writing data segment
Truncated decmpfs xattr
zlib, level 5 (alias: zlib)
truncated state
OECCStreamCreate
%12llu fixed blocks\n
streamReadChunkData
Segment %u: in queue for processing\n
allocating mem buffer
reading file data for ECC
header processing
file stream
Mach-O 64-bit
%12llu segment bytes in cache\n
DecodeAndExtract\n
write header
Opening paged file %s, %u pages in file, %u pages in cache, %u pages total, memory usage: %zu B\n
AEAEncryptionOutputStreamOpen
patch_read_header
reading block payload failed
Invalid payload
fchmod
extractThreadSendCommand
inserting MOD: %s
AAHeaderSetFieldTimespec
Input
image size mismatch
pcWrite
cacheWrite
realignment failed
seek error
invalid input dir: %s
    out set, outSize=%zu, outSHA1=
???
SharedBufferCreate
BXDiffMatchesCreate
inserting header field
invalid fd
workerDecodeAndApplyACL
missing PAT field
getting attributes from header
bad fork flags
%12llu entries in %llu same data clusters (SLC)\n
getting worker from pipeline
deriving signature encryption key
capturing non-empty blobs
    in is NULL\n
invalid linkname
%s (N=%u)
bad variant size
AEAContextGetFieldBlob
PC_APFS_DISKIMAGE_MAP
invalid match path: %s
AEADEncrypt_AESCTR_MAC256_KEY640
SemAcquire
invalid path %s/%s
applying XAT: %s
%12llu removed\n
data missing
Flush chunk pipeline
AEADecryptToFileChunkAsyncStreamOpen
invalid padding state
workerLoadAndApplyXAT
DAT size not received yet
YAA link entry has no LNK field: %s
decoding bzip2 payload
Invalid AFSC data
 FLG
failed to create clone: %s
invalid key
invalid resource fork size
  Patch: %s\n
invalid field index %u
AAEntryXATBlobAppendEntry
main
Object archive
Payload stream init
aaAssetDecompressionStreamOpenWithState
inserting MCO: %s
aaFileStreamPWrite err=%zd buf=%p n=%zu off=%llu
invalid uncompressed size
loading state
ParallelCompressionEncode
BXDiff5 backend, out: %zu B, diff: %zu B, lit: %zu B, ctrl: %zu B\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamTar.c
read: %s
prepareFilter
signing prologue
assigning labels
%12u entries in archive\n
Invalid checksum in root header: %u
%12llu entries in directory\n
AAPathFilterAddRule
virtual fork
encodeYOPEntry
invalid ACL blob in manifest
 %c
setUFCompressedBit
add range
Invalid op
Invalid representation
Name too long: %s
clusterEntryUpdateDAT
stateLoadEntryHeader
Archive unlock
SharedArrayPop failed
invalid cpio header
read data
aaAssetDecodeStreamOpen
loading segment
invalid length
Fixed data using ECC: %s
threads reported errors
pending %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPool.c
consumer proc reported an error
adding entry
increase PathList capacity
get block data
PagedFileRetainAndWriteOut
ThreadPoolSync
inserting segment range
PRead
os
AARandomAccessDecodeAndExtract
hard link: %s
AAHeaderGetFieldBlob
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldXAT.c
%12llu entries skipped\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/BlobBuffer.c
byte stream write error
workerCreateEntries
aaEntryYECBlobInitWithFD
Unsupported profile
isize,osize too large
MemBufferDecreaseSize n is too large: %zu
aaAssetDecryptionStreamOpen
Fat binary 64-bit BE
aaByteStreamPWriteExpected
buffer offset not aligned to holes
io_preallocate
    comboPatch is NULL\n
ThreadPoolCreate
creating pipeline
reading block payload
NULL stream
creating combo controls requires 2 or more unique inputs
invalid segment sizes
applying XAT
rawimg_force_in_place
bxdiff5Free
cluster init
link %s ->%s
unexpected read call
PCompressFilter
BlobBufferIncreaseCapacity
Invalid compression type %u
<<< range EOF\n
hw.perflevel1.physicalcpu
cacheData
Input doesn't match any of the expected patch inputs (in-place)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/SharedArray.h
truncated stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldYFP.c
computing hashes: %s
AAHeaderClone
invalid JSON state
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAsyncByteStream.c
AAByteStreamPReadAsync barrier
Invalid block header payload=0x%llx raw=0x%llx block=0x%llx\n
AACompressionOutputStreamOpen
ImageDiff\n
bxdiffEncodeBuffer
Stream write failed
inconsistency in inPage/outPage indices
Client post-unlock callback returned an error
invalid auth_data index %u
 AFR
tempStreamPRead
verifyDirectoryStreamWriteHeader
writing to digest stream
decrypt stream reported errors
append PRC
aaFileStreamPRead
rawimg_save_to_stream
\\E)
alloc holes
SimStreamSimulate
decrypting segment data
Can't shrink resource fork: %s (current %u, target %u)
bxdiff5CreateInControls
aaCacheStreamOpen
decoding block payload failed
generating random padding
chunkAsyncProcess
missing combo controls
gid
.dmg
StringTableSort
truncating sub asset
AAEntryMCOBlobInitWithFD
run worker
data already written
invalid output size/decoder error: block=%lld, inSize=%lld, outSize=%lld, expectedOutSize=%lld
compressed content
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c
get XAT
invalid entry final ref count %u: %s
clearXATFD
stateScanVariants
Cache size must be >= n_workers
%12u entries with XAT field\n
AAAFSCStreamOpen failed: %s
update file attributes
%12.2f MB/s\n
invalid compression_type: %d
blob byte count mismatch
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c
ECDHE_P256_Sender invalid sizes
Output copy failed\n
No segments to remove
MemBufferFlushToOStream
SemRelease failed
sending command payload
comboPatch is not NULL
Invalid magic
ImagePatch: No variant found
aeaContainerRemoveLastSegment
fstat
write DAT file
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c
generating random encryption key
Invalid profile
Writing decmpfs
mapping patch file
 PRC
Path resolving outside target dir: %s/%s
ARCHIVE (different type/missing in some inputs): %s\n
OFileStreamWrite
invalid char %c %s
Blob segment out of range, key=%s
%s.json
Multi-thread read
%12zu bytes allocated in DIR blob\n
sending blob
lzfse
AEAKeychainGenerateItem
Truncated stream
copy file: %s
Too many segments
verifying data: %s
MASTERING_TOOLCHAIN_DIR
AAByteStreamPReadAsync
LZRAVEN
manifest read
loading entry header
ChunkInputStream\n
patch_write_controls
%12llu common, not matching\n
filter prepare
sending blob data
array too large
deriving segment key
notifySegmentAvailable
randomAccessWorkerProc
AAFieldKeySetCreateWithString
LocalArrayEnqueue
Invalid scrypt parameters
aaCacheStreamSeek
OECCStreamWrite
getTempSegmentFilename
creating hard links, clones
no LNK
false
Streaming data setup
AEAEncryptInPlace
no PAT
importing pub key
ParallelArchiveECCVerifyCommon
ParallelCompressionAFSCStreamWrite failed with status %d
no input dir
decryptToFileAsyncClose
storing offsets
PagedFile: storing cached output page to file\n
fields
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEACommon.c
loading AFSC stream state
Invalid out segment in patch
currentReadBufferEmpty
opening output file: %s
File is too large to be patched in place
bad variant
inControls[%zu] is not NULL
archive_id
invalid chunk
compression_decode_buffer
Context setup callback returned an error
add SLC field
setFieldBlob
Invalid path, doesn't exist: %s/%s
hlinkInsertEntry failed: %s
unexpected blob key: received %s, expecting %s
decodeStreamReadBlob
convertStreamWriteHeader
EOF reached
string too long for StringTable
ParallelArchiveECCFixCommon
missing TYP
creating directory: %s
/XXXXXX
Async stream receiving an unknown segment
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAAuthData.c
Signature verification
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAArchiveStreamProcess.c
fork_write_index
TMPDIR
invalid patch: %s
mergeDiffSegmentVectors
Creating files (flags=0x%08x)\n
decrypting segment %u
Archive stream init
ForkOutputStreamWrite
no cache
SharedBufferFillFromStream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPipeline.c
creating shared data buffer
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAFSCStream.c
flushCache
could not move output page in cache
treeAdd: %zd
fchown
set dir attributes failed: %s
aaHeaderBlobArrayInitWithHeader
Fat binary 64-bit
reading block header
ForkOutputStreamClose
  Input %zu: %s\n
allocating worker buf
pushRange
Destination file exists and size doesn't match: %s
loading cluster header
MemBufferIncreaseCapacity out
invalid decoder: %d
invalid blob size
inserting CKS: %s
Truncated block payload (%lld/%llu bytes written)
create item data
block already consumed
SegmentStreamSimulate
loadThread
computing YEC blob: %s
resourceForkHeaderSize
Cryptor creation
IDecoderStreamCreate
SharedArrayEnqueue failed
AEAContextSetFieldUInt
murmur64
r
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADirectRandomAccessDecryptionStream.c
string table creation
Remove archive\n
too many blob bytes received
corrupted resource fork
MappedBufferCreateWithFD
writing chunk
store blob
aaHeaderInitWithEncodedData
alloc auth_data entry
AAPathFilterApply
File too large for AFSC
load_variants
path
digest mismatch
blob segment mismatch
HKDFDerive
running task
Padding generation and hashing failed
Invalid field
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c
open decoder stream
AAJSONInputStreamOpen
stateGetEntryData
applying XAT blob: %s
invalid XAT index
aaEntryMCOStringCreateWithPath
%12u messages\n
stream not compatible\n
copy failed %lld
retireThreadEnqueue
invalid blob state
%12llu data size\n
truncated write
ImageDiff: Removed non-unique input variant <%s>.\n
LargeFile: Constructed %zu controls in %0.2f (s).\n
blob resize
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAContext.c
stateSetDirsAttributes
acl_init
AAEntryACLBlobRemoveEntry
not implemented
aaAssetExtractStreamSetParameterPtr
create new header
AAEntryXATBlobSetEntry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c
SharedArrayPop: pthread_mutex_lock failed\n
Create chunk pipeline
AAEntryYECBlobCreate
pcWrite EOF failed
Header has already been sent
AEAEncryptionOutputStreamOpenExisting
treeRotateLeft %zd
AEADecryptToFileAsyncStreamOpen
could not resolve qualifier (type %c): %s
aaInPlaceStreamOpen
BXDiff5 patch headers: %zu B\n
alloc blob failed
parse stored header
Invalid archive: segment size mismatch
add_fork
Decompression
computing file digest: %s
 UID
String table creation
not enough capacity to store HASH
%12llu entries in %llu clone clusters (CLC)\n
Full replacement patch\n
%12llu bytes read from clients\n
loadRemainingRange
  path checking: %s\n
decodeStreamReadData
Invalid block_id, or no workers available
com.apple.ResourceFork
stateGenerateArchive
write YEC
After input pages retained, %u free pages\n
header init
invalid SRC/DST
inserting first cluster header range
inserting next cluster header range
    0x%06x diagnostic code\n
 MOD
entry too large to defer
initializing blob array
archive stream read error (blob)
rangeInputStreamRead
Dst fixup %c%s %s\n
pthread_attr_setstacksize
invalid c_namesize
creating worker thread
Invalid segment size
aeaInputStreamLoadSegment
In-place patch matching entry %u\n
Invalid ECC header
close: %s
verifying signature
extractStreamSendEntryToExtractThread
x86
  container size: %llu B\n
AADecompressionInputStreamOpen
create extract stream
io_hint_static_content
decodeStreamHLCFromINO
no fork extents
%12llu errors reported\n
closing stream
copyFileWithAttributes
AEAContextGenerateFieldBlob
calloc
 pat=%s
blob alloc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARandomAccessByteStreamProcess.c
sequentialReaderProc
too many cluster entries
invalid state on destroy
attribute data is too large name=%s
 lbl=%s
HMAC derivation
mutex failed
AAPathListCreateWithDirectoryContents
invalid file size
insufficient out_capacity
Segment load
BXPatch5StreamWithFlags
reading block header failed
directory path too long
writing cluster header
reserve buffers
BXDiff5WithIndividualPatches
reading from archive stream
Invalid item type
invalid block header
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACompositeChunkAsyncStream.c
OArchiveFileStreamWrite
Threads reported errors
AEAContextSetFieldBlob
loading and applying XAT
bad fork compressed
.tmp_decrypt
BXDiff5Data: n=%zu, nUnique=%zu\n
    comboControls is NULL\n
mkfifo %s
mkdtemp
stateAssignLabels
Can't init MCO
Fork missing header/footer
startStreaming
)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAVerifyDirectoryArchiveOutputStream.c
AAByteStreamSeek
%zu controls in patch (%zu B allocated)\n
invalid file descriptor
Copy %c %s\n
derive segment encryption key
invalid path: %s
aaArchiveFileOutputStreamCloseAndReturnFD
allocating reader
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c
AEAContextDecryptAttributes
fsetxattr decmpfs
Blob encoding failed
deriving container offsets
afStreamClose
workerUpdateDir
writerProc
AEAContextGetContainerSizeUpperBound
%s/%08x
Missing IDX,IDZ from archive decoder
%12u regular files\n
invalid match type: %u
data not locked
too many bytes received
AAByteStreamProcess
setting internal attributes
missing reference entry in cluster
Invalid path (subpath normalization failed): %s/%s
could not determine entry type: %s
memoryOutputStreamWrite
--> chunk %10llx %10llx -- %8zu\n
applying ATTR: %s
update global header
expand obuf
%12llu blocks computed\n
*full replacement*
MemBufferFillFromBuffer
 SH3
append BTM
Warning: ACL tag type is not ALLOW/DENY (ignoring entry): %d\n
LocalArrayDequeue
afStreamWrite
streamPRead
error: read more bytes than requested: %zd (requested %zu)
aaInPlaceStreamClose
BXDiff5 patch capacity: %zu B\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldYEC.c
%12.0f MB/s\n
store decmpfs xattr
subSegment
Invalid padding_alignment
WriteAlignedChunkProc
AAChunkInputStreamOpen
truncated read
rawimg_get_digests
AAAssetExtractorWrite
fail to init buffer
aeaContainerFinish
invalid buffer
aaParseFatFile
AAAsyncByteStreamProcess
could not move input page in cache
Invalid ECC block size
Can't reopen %s for writing
offload to file
flushing cache pos
no possible conversions
First pass fixup failed: %s, compression_type=%d (expected %d), resource_fork_size=%u (expected %u)
invalid field subtype: %d
uname
clearing file
decompressing to regular data file
CompressionConsumerProc
kAEA
patch doesn't match source file: %s
file not empty
inconsistent blob key
compute patches
BXDiff5
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEACrypto.c
user cancelled
invalid context
Hole append
retireThreadEnqueue failed
unable to load input page
afStreamCloseWithState
patch_read_variants
aeaContainerRemovePadding
enumerateTree_rec
Invalid header field type
read resource fork header
verifySegmentProc
ThreadPipelineDestroy failed
invalid type %d, expected UINT
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetGenerate.c
aaFileStreamRead
LocalArrayPop
closeWithStateProc
loading compressed segment
reallocating block blob
aeaInputStreamDecryptSegment
Truncated ECC buffer
alloc
stream not in-place compatible\n
extract entry failed: %s
workerDecodeAndApplyXAT
MCO creation failed
inserting YFP: %s
invalid variant %u
convertStreamEndEntry
Multiple root nodes
invalid tar archive
aggregating entries
LocalArrayInit
blob array init
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetBuilder.c
SimStream: pages: %i file, %i written, %i free, %i excess (%iK)\n
removeLeaveDirProc
bxdiff5CreateComboControls
Segment %u: not needed\n
%12zu regular files in same content clusters\n
expandDirThreadProc
Segment received: %zu B\n
treeAdd
treeRebalance
    inControls is NULL\n
inserting PRC: %s
invalid qualifier type: %d
bad chunk
cachePageEvict
deriving cluster header key
invalid stream type
Warning: F_NOCACHE failed: %s\n
blockWriter
getting DAT field
bad chunk info
Encryption
pthread_mutex_unlock
%12llu segment bytes to download\n
setting entry attributes: %s
aaArchiveFileOutputStreamOpenAt
SegmentStreamPWrite
seek
acquireCachedBlock
treeRotateRight %zd
IDecoderStreamThreadProc
invalid out,outSize
allocating clusters
Magic received: %zu B\n
Invalid context
aaAssetExtractorCreateWithCheckpoint
, %s
append CTM
cached input page does not have a file position
add CLC field
parseAPFSJSON
aaEntryYFPBlobInitWithPath
aaCopyFile
true
Async stream range timed out (FAIL): %zu bytes at %llu
%12llu blocks in file\n
 FLI
non unique
computing file digests: %s
realloc_fields
Worker buffer allocation
authenticating padding
invalid header blob size
Diff
AFSC compression failed: %s
MutexInit
invalid entry final state %d: %s
create copy: %s
error building regex
Truncated segment
SharedArrayPush: pthread_mutex_lock failed\n
aeaContainerCreateNew
creating compression stream %s
v8@?0
missing IDZ field
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAHeader.c
AAAssetBuilderCreate
decoder stream
finishing container
write after EOF
<-- chunk %10llx %10llx -- %8zu\n
buf_capacity is too small
Invalid entry path
loading decmpfs xattr
ECC failed: %s
blob not found
loading chunk offsets
%12llu B data size\n
outProc write
Entry failed: %s
Cluster header encryption
Couldn't convert to requested compression type
bxdiff5CreateComboPatch
bxdiffFastPathControls
realloc blob
aaEntryXATBlobInitWithEncodedData
lstat
Invalid offset received: %jd\n
Scanning target directory: %s\n
ILowMemoryDecoderStreamCreateWithBuffer
lock
errors reported
generate archive
ARCHIVE (not a regular file): %s\n
reading block
aeaPaddedContainerSize
out is not NULL
AASharedBufferPipeOpen
set UF_COMPRESSED
loading manifests / scanning directories
Stream seek
Async stream range timed out (retry): %zu bytes at %llu
patch_verify_header
BXDiff5 patch control payload: %zu B\n
process_output_block
scanning archive
SemInit failed
sending DAT blob
GPU support functions
aaDecompressionStreamRead
no variants
AEAAuthDataSetEntry
aeaDeriveMainKeyExisting
Invalid archive, too many clusters
ACL blob allocation
SemInit
Final FULLSYNC
 SH2
retire failed entry
BlobBufferStore
header size mismatch: stored %u, got %llu
readlink: %s
re-encrypting container
removing padding
SharedBuffer invalid capacity: %zu
fingerprint_worker
invalid raw stream
invalid 'H' LNK
extra data received for blob %s: received %llu, expecting %llu
AEADecryptAsyncStreamOpen
CacheStream: read ops %zu/%zu, write ops %zu/%zu\n
invalid offset=%llu for fd
Invalid data write, no matching hole
  target directory: %s\n
stateAppendEntry
AAAFSCSetMetadata
no digests found
Warning: container truncate failed
/
invalid reference entry: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldMCO.c
AAAsyncByteStreamClose
importing private key
Sending task to worker
workerReserve
Invalid EOF record header
ECCFixThreadProc
obtain AFSC data: %s
All entries:\n
reading current metadata
Truncate on compressed stream failed
sequentialWriterProc
write to stream failed: %s
BXDiff5 patch archive payload size: %zu B\n
aaEntryACLBlobInitWithEncodedData
SH2,IDX,IDZ,SIZ
reserveDiffSegmentVector
getStreamSHA1Digest
AAMemoryOutputStreamOpen
File a radar to increase obuf_capacity, sz=%zu
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c
Prologue size mismatch
skip dataless dir: %s
uid
chunks too large
lseek failed
streamGetChunk
 BTM
aaInPlaceStreamCancel
Invalid auth data size: %zu
Fat GPU binary BE
Fat GPU binary
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c
%12zu directories\n
invalid ACL flags 0x%llx
Scanning archive for variant %zu...\n
PagedFile: storing oldest cache[%u] to file\n
Encoder: %s\n
reading gzip header data
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c
opening file: %s
remap_page
Tree normalization
bad stream position
file + excess != written + free
%12u block size\n
applying ACL
appendPathListWorkerProc
blockGetFromCache
%12llu archive bytes\n
entry not found, or not a regular file: %s
loadChunkOffsets
invalid attribute size
copyFileSegment
encoding magic
%12zu allocated chunks\n
creating diff match lookup object
workerCreateDirs
unsupported entry type
invalid path: %s/%s
ParallelCompressionGetCompressedSize
OFileStreamCreateWithFilename
Stream close error
retrieving digest from header
AAEntryACLBlobSetEntry
decompression stream
invalid private key size
streamWorkerProc
Literal
ForceInPlace %d: excess_pages=%d/%d, converted bytes=%llu, %zu controls\n
Write chunk
fsetxattr resource fork header
SRC is empty
ImagePatch: Static content hint failed.
Writing chunk
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAChunkAsyncStream.c
AATempFileStreamOpen
loading ACL blob
invalid cache POS
movePage
moving page from disk to cache
\\E$)
aeaOutputStreamWorkerThreadProc
OBufferedStreamCreate
worker proc reported an error
getDefaultNThreads
 lnk=%s
bad index
inserting ACL: %s
bad write mode
Warnings:0x%08x
patch_write
retireThreadDequeue
dat decoder stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c
no available chunk
getFileSegmentSHA1DigestFD
Remove %c %s\n
building fast path controls
String table append
Encode archive\n
IDecoderStreamDestroy
Invalid root header
workerSetDirAttributes
truncated entry when encoder destroyed
aaForkInputStreamOpen
aeaInputStreamUnlockCluster
%12llu entries removed\n
joinThread
>>> range %10llx %10llx\n
invalid output dir: %s
extract entry attributes from header
com.apple.ParallelCompression
hashing file: %s
aeaOutputStreamRunCurrentWorker
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamCPIO.c
getBXDiffControls
aaEntryAttributesInitWithFD
invalid decmpfs xattr size
Diff stream init
Chunk creation
get ACL
SharedArrayPush
bad interval
get attributes
Generating asset...\n
blob reserve
aaByteStreamReadExpected
bad extent size
AAArchiveStreamWritePathList
ChunkPipelineDestroy
unsupported entry type %c: %s
PagedFile: input page %u removed from storage\n
Invalid profile code: %c
getErrorContextKey
string too long
No more data
too many elements
blob processing
invalid key set: %s
invalid 'D' PAT
not implemented yet
invalid ACL qualifier type %c
calloc controls
decoding lzma payload
Expanding resource fork
chunkCreate
%12u segments to download\n
subArchiveReset
mapto string is required for MAPTO rule
Invalid compression algorithm in context
string table
patch path: %s
write data
AAByteRangeClone
file < written
invalid dir: %s
blockReader
Invalid state, file already open
streamClose
creating decrypt stream
inserting SH5: %s
initializing XAT field from path
 MTM
invalid newc encoding for hard links
AAByteStreamProcess reported an error
AAEntryACLBlobApplyToPath
string table sort
OK
segment checksum verification
invalid type %d, expected STRING
seek dat stream
Invalid worker/block id
aaMalloc
    %zu chunks\n
preallocation failed
stateLoadEntryBlob
%s/0x%08zx
  %u total pages\n
SharedArrayDequeue
threadPipelineWorkerThreadProc
Writing chunk sizes
invalid c_filesize
Checksum verification failed, data corrupted
control sequence broken
decrypting cluster header
Padding was not removed
derivating RHEK
clusterInsertEntry
Preloaded executable file
ParallelArchiveECCFixCommon:\n
getFileSegmentSHA1Digest
Invalid segment index: %u
AAHeaderCreate
invalid archive stream
Bad stream
%u entries failed to extract
invalid reverse index for IN
bxdiff5SetIn
lzma, preset 6 (alias: lzma)
Mach-O BE
acquire segment in cache
nRefs inconsistency
YEC blob allocation
fsetxattr resource fork
segment_decode_to_buffer
String table merge
decodeStreamReadHeader
prepare non zlib header
PagedFile: vacating file pos\n
BYE chunk %8zu evicted\n
convert_block_controls
invalid auth_data index
Warning: F_NOCACHE failed with error %d: %s\n
fstat: %s
stream cancelled
Invalid sizes in root header
loading file XAT: %s
Data append
Segment count/size mismatch
creating header
initFilterState
corrupted file data, ECC failed 0x%08x: %s
dirInsertEntry
acl_get_flagset_np
write patch payload
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/../AppleArchive/../Common/SharedArray.h
aeaContainerCreateExisting
initBestMatchFromHashes
Pipeline failed: using in-thread compression
AAConvertArchiveOutputStreamOpen
Thread allocation
CompressionWorkerDataCreate
too many writes pending
AEAD invalid sizes
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAKeychain.c
pthread_setspecific
Payload compression
AAExtractArchiveOutputStreamOpen
invalid ACL entry
AAAFSCGetMetadata
invalid/missing decmpfs
could not locate the apfs diskimage map tool
blob append
Invalid KDF parameters
Padding authentication
  Expected SHA1: %s\n
unlocking AEA
%12zu regular files in hard link clusters\n
blob field size too large
pc_array_compact
IMemStreamCreate
copy failed: %s to %s
reading DAT file
AEADecryptAndExtractChunkAsyncStreamOpen
stateAllocClusters
getTempDir
no SIZ: %s
Client selection callback reported an error
SemAquire failed
open failed: %s
send header
%12zu entries in output\n
YEC blob
AAAFSCStreamOpenWithState
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAGenericRandomAccessInputStream.c
%12llu entries in %llu hard link clusters (HLC)\n
Invalid segment sizes
ACL blob
client callback cancel
processMagic
pcRead
AAByteRangeSub
reading from diff stream
Incompatible page size
writeHeaderProc
String too long: %zu
writing block payload
AAByteStreamPRead
some input bytes are still mapped after diff expansion
%12llu bytes read from upstream\n
not a regular file: %s
Verifying file: %s\n
append GID
acl_add_flag_np
Writing resource map
Unsupported entry type (extract): %c\n
SegmentStreamPRead
%02x
Invalid/missing directory: %s
stateComputePatches
resource fork resize failed
kSecUseDataProtectionKeychain
AA entry missing TYP field
inputPageData
snprintf
Some segments failed to process
creating entries
inserting DUZ: %s
aaCompressionOutputStreamWrite
zlib
aeaContainerParamsInitWithProfile
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteRange.c
Signing callback
Too many bytes received
    out is NULL\n
Before applying control
ChunkPipelineCreate
%s read
ARCHIVE (smaller than patch): %s\n
%12.2f x compression ratio (%s)\n
invalid reverse index for OUT
Name too long
Mach-O 64-bit BE
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c
decoding zlib payload
aaAssetExtractStreamOpen
patch_write_stream
%12llu bytes in archive (uncompressed)\n
Too many arches
invalid output PAGE
aaAssetDecryptionStreamOpenWithState
stateCreateClusters
afscStreamClose
getting entry full path
append to buf
MemBufferIncreaseCapacity in
Segment write
IFileStreamCreateWithFilename
rawimg_digest_worker
initializing header from path
allocate_page
ARCHIVE (empty in some inputs): %s\n
rawimg_check_memory
Invalid signature size
File exists but is not a regular file: %s
verifySegment
byte stream truncated write
querying AFSC metadata: %s
sha256
looking up header
aaEntryYECBlobInitWithPath
AAEntryYECBlobApplyToPath
removing DAT
invalid state %d
compressionWorkerProc
increasing blob capacity failed
MemBufferCreate
create temp file
    in set, inSize=%zu, inSHA1=
AAEncodeArchiveOutputStreamOpen
pc_array_init
RNG lookup
inserting FLG: %s
Core file
resourceForkSize
alloc buffer
read chunk
OSHA1StreamCreate
failed to create hard link: %s
aaSegmentStreamOpen
%s/%s
aeaContainerParamsInitWithMagic
updateFileAttributes
AAPathListMerge
Post-processing ctrl for in-place patching, %u pages\n
reading blob data
AAMagicInputStreamOpen
invalid node index
Invalid compression algorithm
missing PAT
invalid ACL blob size
Creating directories\n
aaAsyncByteStreamIsCancelled
aaCalloc
too many inputs/outputs
AEAStreamSign
temp file write
%12llu bytes in archive\n
invalid type %d, expected TIMESPEC
acl_get_permset_mask_np
pcWrite failed
AAEntryXATBlobApplyToPath
close stream
Warning: couldn't set F_NOCACHE\n
fixup failed: %s
seek temp file
bad algo
1 0x%x %u
Invalid non metadata entry missing PAT field (skipped)
bxdiff5CreateInPatch
opendir failed: %s
inserting MTM: %s
input page is not stored
no storage available for output page
aaIntervalInputStreamOpen
com.apple.decmpfs
setting directories attributes
entry failed
aaAssetExtractStreamOpenWithState
\t<%s>\n
open AFSC stream
Readers reported errors
alloc blob
pAEA
Container size mismatch
Missing call to GetWorker before RunWorker
pthread_key_create
aaAsyncByteStreamAlloc
creating shared buffer
output page is not stored
invalid header
mapto string is not allowed for non MAPTO rules
Segment checksum failed
computing file digest
AEAKeychainStoreItem
currentWriteBufferFull
convertStreamWriteBlob
stream read error
aeaChecksum
SharedArrayPop: pthread_cond_wait failed\n
MemBufferTransmit
apply YEC (copy)
rawimg_create_with_file
Invalid field size
mkdir: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldKeys.c
treeDeleteRangeWithPoint
BlockDecryptionStreamPRead
Truncated write n=%zd pos=%llu read=%u fd=%d
end entry failed
mtime
XAT blob
arm64e
Worker data allocation
rawimg_remove_fork_duplicates
AAAssetBuilderSetParameter
Invalid container size
fcntl
Client progress callback reported an error
Archive identifier value mismatch when resuming
invalid final AFSC stream state, received %zu/%zu bytes
AAGenericRandomAccessInputStreamOpen
apfs_diskimage_map
Invalid directory: %s
BXPatch5FileWithFlags
generating new main key
pthread_attr_set_qos_class_np
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c
inserting PAT: %s
invalid XAT entry key %zu
lz4
writing back last segment data
AEAKeychainLoadItem
mutex lock
Invalid padding size
invalid ACL blob
extractStreamProcessHLinks
 siz=%llu yec=%zu
Too much fork padding: %zu
Invalid encryption data size
%12llu INVALID BLOCKS\n
Stream write failed: %s
static content hint failed
no IDZ
sendMessage
duplicate fork
decodeStreamRefillBuffer
AAAssetBuilderGetParameter
aeaContainerParamsInitWithRootHeader
workerCreate
apply YEC (patch)
  Compression: %s\n
creating retire thread
aaPReadExpected
initializing YFP field from path
/)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAsyncByteStreamProcessAllRanges.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAConvertArchiveOutputStream.c
header copy
Dynamically bound bundle file
aaFileStreamWrite
```
