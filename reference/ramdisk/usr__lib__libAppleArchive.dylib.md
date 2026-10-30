# `/usr/lib/libAppleArchive.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 851,616 bytes.

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
archive_id
DAT field is required
readdir on dataless directory: %s
importing full key
removeLeaveDirProc
workerDecodeAndApplyACL
extractStreamSendEntryToExtractThread
inserting CTM: %s
Cluster header decryption
data not locked
truncated DAT file
expected ref_count=1 for terminating thread
invalid ACL blob in manifest
invalid ACL qualifier type %c
setup header
read error
fork footer
error building regex
MutexInit
patch_write_controls
forceInPlaceControls
aaFileStreamRead
OArchiveFileStream didn't receive enough data before being destroyed\n
acl_set_permset_mask_np
ForceInPlace %d: excess_pages=%d/%d, converted bytes=%llu, %zu controls\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBuffers.c
controls_combo_enforce_copy_fork_boundary
entryDestroy
AAAFSCStreamOpen
stripAFSC
blob append
re-writing last block
lzma, preset 6 (alias: lzma)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAKeychain.c
aaReallocf
decoding lzma payload
AEAContextSetFieldBlob
extractThread
HMAC
Remove archive\n
in[%zu] is not NULL
LocalArrayPush
%12zu blocks per thread\n
getting DAT field
String table append
%12llu bytes to process\n
blob array init
ECC failed: %s
invalid compressed stream
chunkCreate
stat
stateLoadEntryBlob
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c
invalid image map JSON
retire segment
Async stream range timed out (FAIL): %zu bytes at %llu
Client selection callback reported an error
kAEA
%12u worker threads\n
  Expected SHA1: %s\n
Invalid AFSC data
opening output file: %s
invalid entry index %u
  async read stream: %s\n
Invalid representation
adding entry
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteStream.c
EOF reached
SharedArrayInit: pthread_cond_init failed\n
Sending task to worker
Invalid arguments
IMemStreamCreate failed
pending compressed fork
get node path
aeaInputStreamAuthenticatePadding
Closing paged file, input size: %llu B, output size: %llu B, bytes read: %llu B, bytes written: %llu B\n
invalid mapto path: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAInplace.c
processWithProgress
Filename is too long: %s
header payload too large
Fork missing header/footer
apfs_diskimage_map
aeaContainerRemovePadding
Invalid ECC algorithm
Second pass fixup failed: %s, compression_type=%d (expected %d), resource_fork_size=%u (expected %u)
YAA entry missing/invalid PAT field
\\E)
lock
acl_init
AEAKeychainGenerateItem
inserting segment range
Data append
invalid XAT blob
%12.0f MB/s\n
allocating buffer
hashing padding
LargeFile: Constructed %zu controls in %0.2f (s).\n
invalid entry final ref count %u: %s
PagedFileDump
offset
AAPathListMerge
Mach-O BE
arm64
%12llu blocks computed\n
Invalid hardness parameter
no nodePrev/Next: %zd
failed to join decoder thread
Invalid signing public key in context
Abort
entry defined multiple times in the same variant
invalid read blob request
getting entry path
dispatch_block_create
AATempFileStreamOpen
Invalid field
verifying data: %s
readlink: %s
invalid path
invalid header size
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAAuthData.c
ParallelCompressionAFSCCompress
write returned 0
loading and applying XAT
stateAllocClusters
bad page
afStreamClose
AEADecryptAndExtractChunkAsyncStreamOpen
encoding entry
AAAFSCGetMetadata
moving output page from cache to disk
invalid SRC/DST
no chunk info
%12u entries with YEC field\n
%12llu bytes in regular files DAT\n
unlocking context
ParallelCompressionAFSCStreamOpen failed: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAChunkAsyncStream.c
apply YEC (patch)
AATeeOutputStreamOpen
Prologue received: %zu B\n
callback cancel on non AEA container
%s%s/%s
Both file and temp file exist: %s
loading DIR entry
clearing file
loadChunkOffsets
PagedFileRetainIn
workerAlloc
Unsupported profile
closing AFSC stream
bad write mode
<<< range EOF\n
loading file XAT: %s
bad flags
verifyDirectoryStreamWriteBlob
Segment insertion
Input variants in patch: %u\n
update resource fork
blockPRead
pcRead failed
DIFF STREAM: I=%zu OPOS=%llu IPOS=%llu NDIFF=%llu NARCHIVE=%llu IDELTA=%lld\n
inProc read
non fork
>>> range %10llx %10llx\n
byte stream truncated write
AAHeaderGetFieldUInt
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAFSCStream.c
AAAssetBuilderCreate
AAAssetExtractorCreate
write
aaCompositeChunkAsyncStreamOpen
generating new main key
write failed
Writing chunk
aaEntryAttributesInitWithPath
inserting ACL: %s
insufficient out_capacity
Invalid block index
MemBufferFillFromBuffer
SemRelease failed
Scanning manifest\n
Multiple root nodes
invalid entry final fd
copy
invalid ACL entry tag %c
AAJSONInputStreamRead
%s
callback cancel
aaAssetExtractStreamSetParameterCallback
invalid linkname
invalid ACL flags 0x%llx
acl_get_flagset_np
decodeStreamReadBlob
rangeDataInsert
rawimg_get_digests
streamWorkerProc
nodeAlloc
Keychain support not available
looking up AFSC data: %s
hw.perflevel1.physicalcpu
creating dir: %s
malloc patch
rawimg_remove_fork_duplicates
AAAsyncByteStreamClose
DHERecipient_ECDHE_P256
closing stream
Extra bytes in patch (ignored)
invalid file header
no possible conversions
ChunkPipelineCreate
blob processing
decompression stream
Invalid scrypt parameters
negative offset
%12zu chunks in cache\n
AAConvertArchiveOutputStreamOpen
%12zu bytes allocated in DIR blob\n
no active entry or active thread
seek error
invalid ACL blob
workerCreateClusters
loading decmpfs
Opening paged file %s, %u pages in file, %u pages in cache, %u pages total, memory usage: %zu B\n
invalid decoder: %d
%i dangling reads
LZMA
applying XAT blob: %s
  compression: %s %zu MB\n
CompressionConsumerProc
Payload stream init
OECCStreamCreate
Fat GPU binary BE
invalid state
loading compressed segment
invalid stream type
invalid c_filesize
inserting blob placeholder
Scanning archive\n
derive segment encryption key
AAEntryXATBlobAppendEntry
 lbl=%s
malloc %u threads
querying AFSC metadata: %s
invalid YEC blob
send request
removing last segment
StringTableAppendTable
computing file digest: %s
MutexLock
lzbitmap
reading block payload
MASTERING_TOOLCHAIN_DIR
Segment decompression
Chunk write failed
importing private key
DSASign_ECDSA_P256
AEAEncryptInPlace
create temp file
tempStreamPRead
aaDecompressionStreamRead
  %u output pages stored, %llu bytes referenced\n
aaAssetDecodeStreamDone
AEAAuthDataCreateWithContext
DH callback returning invalid shared secret size
treeAdd
outProc write
ImagePatch: Static content hint failed.
aeaPaddedContainerSize
Segment processed: offset=%llu size=%zu\n
writing tool output
AAByteStreamSeek
- input %zu\n
process_output_block
Eerror getting blobs from header
cluster entry query
inserting SH1: %s
inserting SH3: %s
no free pages
%12zu bytes in chunks (%.2f MB)\n
Decrypted file: %s\n
invalid compressed buffer
some output bytes are missing or referenced more than once after archive expansion
create new header
stream not compatible
AAEntryXATBlobCreate
acl_set_tag_type
joinThread
MemBuffer write proc returned 0
Read out of range
SegmentStreamCreate
AAAssetBuilderSetParameter
mutex unlock
OBufferedStreamCreate
segment out of range
Stream pread
Reading decmpfs
largefile controls
Dynamically bound bundle file
reading from archive stream
out access out of range
extractStreamWriteHeader
Shared library stub for static linking only
 fork | %64s | algo |       size | compressed | V | C\n
bxdiff5SetOut
calloc
invalid DAT path
AAEntryXATBlobGetEntry
seek to end of stream
workerLoadAndApplyXAT
BXDiff5 patch diff[%zu] payload: %zu B\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamCPIO.c
invalid cpio header
AAHeaderClone
bad fork size
invalid header
user cancelled
aeaOutputStreamWriterThreadProc
Writing chunk sizes
Archive identifier value mismatch when resuming
ARCHIVE STREAM: OPOS=%llu IPOS=%llu NDIFF=%llu NARCHIVE=%llu\n
Write chunk
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AATempStream.c
loading XAT blob
Invalid thread command
Non supported entry type %u
allocating reader
missing IDX field
flushOBuf
%12llu blocks\n
Invalid worker/block id
AAAsyncByteStreamProcess
match string is required for all rules
Invalid profile
removeStreamClose
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c
reading block
invalid auth_data blob
alloc blob
Invalid profile value: %s
Invalid KeySet string length: %zu
AAPathFilterCreate
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c
ThreadPipelineFlush
Segment write failed: offset=%llu size=%zu\n
AAHeaderGetFieldKey
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldACL.c
AEA_SCRYPT
Stream thread creation
%11.2f%% parity/data ratio\n
v8@?0
no chunks found
donor is not a regular file: %s
removing header field
invalid sizes
hlinkInsertEntry failed: %s
receiving blob data outside of entry
AAArchiveStreamWritePathList
Second pass fixup succeeded: %s
reading blob data
invalid resource fork
Cache size must be >= n_workers
XAT blob allocation
streamConsumerProc
threadPipelineConsumerThreadProc
SET range %10llx %10llx -- %8zu\n
acquireCachedBlock
workerCreate
a parent of path is not a directory: %s
seek dat stream
AAEntryMCOBlobInitWithFD
flushing obuf
allocating buffers
AAPathListNodeGetPath
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetBuilder.c
Segment decrypt
close stream
iterating to next blob
BXDiff5 patch headers: %zu B\n
no hash: %s
null
operation aborted
AEADecryptAndExtractAsyncStreamOpen
AAByteRangeSub
  Input data SHA1: %s\n
isize,osize too large
removing DAT field
AAEntryACLBlobRemoveEntry
writeOBuf
inserting DAT: %s
invalid AssetArchive DAT blob size
invalid match path: %s
no available chunk
sendHeader
acl_get_tag_type
invalid char %c %s
  %u total pages\n
(
bad header
AEAContextDecryptAttributes
invalid chunk size
SegmentStreamPWrite
aaSegmentStreamOpen
Archive stream applied
Parity buffer out of range
write to stream failed: %s
File exists but is not a regular file: %s
%02x
inserting FLI: %s
ctrl[%zu]: ndiff=%llu nlit=%llu\n
aeaContainerCreateNew
preallocating %llu B
AEAContextSetFieldCallback
sending blob
Fat binary
Mach-O 64-bit
no fork extents
convertStreamBeginBlob
  Metadata: %llu bytes\n  Controls: %llu bytes\n
computing hashes: %s
inserting PRC: %s
loadDecmpfsXattr
pc_array_append
invalid offset=%llu for fd
Missing decmpfs xattr
dir doesn't exist, or is invalid: %s
convertStreamEndEntry
tmp
flushing ibuf
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACompressionStream.c
ILowMemoryDecoderStreamRead
StringTableSort
io_hint_static_content
end entry
ARCHIVE (too small for patching): %s\n
AACompressionOutputStreamOpenExisting
no storage available for output page
bad fork flags
Total size %zu MB\n
unlocking AEA
%12u segments to process\n
true
CCKDFParametersCreateHkdf
aaInPlaceStreamOpen
.XXXXXX
close: %s
PagedFileRetainAndWriteOut
bad index
%12llu entries in directory\n
decoding bzip2 payload
  Output data SHA1: %s\n
arm64_32
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEASequentialDecryptionStream.c
ImagePatch: Digest match. Output reconstructed.\n
generating last cluster random MAC
deriving fields from header
extractThreadFailEntry
acl_get_qualifier
PATCH: %s\n
aaParseFatFile
read error: %zd
unlock container
AAMemoryOutputStreamCloseWithSize
BlobBufferIncreaseCapacity
AEAContextCreateWithProfile
bxdiffControlsWithMatches
generate archive
PagedFileReleaseIn
creating XAT field
Invalid ECC block size
copy fork not found
reading thread command, %zd
Worker buffer allocation
creating YEC field
archive stream write error (blob)
starting blob
invalid archive stream
looking up header
ace_check_entry
Main key derivation failed (%d)
file < written
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c
CompressionWorkerDataCreate
currentWriteBufferFull
invalid newc encoding for hard links
invalid compression type
reading from control stream S=%lld
    inPatch set, inPatchSize=%zu (%zu MB)\n
String overflow
ImagePatch: Preallocation failed.
SIZE MISMATCH
opening parent directory
pcWrite failed
Dropping copy fork with %llu bytes, needed=%llu bytesx\n
invalid patch: %s
Invalid root header
chunkWriteData
loadRemainingRange
invalid XAT blob in manifest
allocating worker buf
PCompressFilter
Warning: F_NOCACHE failed with error %d: %s\n
 MTM
ImageDiff: Constructed %zd combo controls.\n
ImageDiff: Processed copy forks: %zd controls\n
%12zu other entries\n
store padding
%12llu requests processed\n
missing TYP
pending %s\n
os
could not resume from saved checkpoint
NOP received
Invalid checksum mode
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFile.c
convertStreamEndBlob
get ACL
threads reported errors
write patch payload
pthread_mutex_init
cachePageEvict
AAByteRangeAdd
invalid variant %u
fstat
set UF_COMPRESSED
getting worker from pipeline
aeaContextUnlock
set dir attributes failed: %s
update_field_sizes
decodeStreamLoadHeader
Archive unlock
treeSub
aaSegmentStreamProcess
append_field
%s/0x%08zx
aaFileStreamWrite err=%zd buf=%p n=%zu
unsupported parameter key
volumes
invalid digest size
IFileStreamCreateWithFD
alloc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAPathList.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAExtractArchiveOutputStream.c
A file composed of other Mach-Os
lzfse
creating worker thread
prepare decmpfs header
reading current metadata
aaIntervalInputStreamOpen
clearXATFD
blob reserve
Worker: decode block %5lld: %7llu => %7llu\n
fcntl F_SETPROTECTIONCLASS
derivating RHEK
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c
%12llu bytes processed in chunks (%.2f MB)\n
Destination file exists and size doesn't match: %s
patch_read_variants
Name too long: %s
blob not found
aaAssetExtractStreamOpenWithState
SegmentStreamPRead
streamCheckAndWriteChunksToStream
Extract archive\n
PagedFile: moving page from file[%u] to cache[%u]\n
dat decoder stream
aaArchiveFileOutputStreamCloseAndReturnFD
no input dir
byte stream write error
invalid AEA prologue
extract entry failed: %s
invalid ACL perms 0x%llx
Invalid iBlock received
archive stream write error (header)
 PRC
Segment %u: not needed\n
decrypt stream reported errors
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToStream.c
parseProfile
%12zu regular files in hard link clusters\n
setting entry attributes: %s
pc_array_init
<target dir>
AARangeInputStreamOpen
init active chunks
%12zu regular files in clone clusters\n
Creating files (flags=0x%08x)\n
istream read error
storeCachePos
aeaRootHeaderInit
AAByteStreamClose
setThreadErrorContext
isDirEmpty
%12zu regular files\n
can't resize resource fork %u to %u
PagedFile: storing cached input page to file\n
cacheData
ScryptDerive_KEY256
adding item to the keychain: %d
Invalid decmpfs xattr
open AFSC stream
PagedFile: storing cached output page to file\n
too little excess
encoding magic
stat failed: %s\n
stateShouldCreateFileInCluster
AEADEncrypt_None_MAC256_KEY256
comboPatch is not NULL
%12u segments in archive\n
AARandomAccessDecodeAndExtract
 (0x%x %i %i %u %llu %llu %u)
compile regex (err=%i, msg=%s)
ForkOutputStreamWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetExtractStream.c
 siz=%llu yec=%zu
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARandomAccessDecompressionStream.c
vacating page in file
ThreadPoolDestroy
bad output size
%12llu bytes read from clients\n
Can't reopen %s for writing
offload to file
clear header
%12.2f MB/s\n
HMACInit_SHA256
allocating blob buffer
deriving signing public key
chunkAppendHole
AAPathListCreateWithDirectoryContents
aaHeaderInitWithEncodedData
append MTM
encode entry
Missing bytes in patch
ForkOutputStreamClose
invalid output dir: %s
non unique
applying XAT: %s
realloc_fields failed
reading file data for ECC
resource fork resize failed
inserting YFP: %s
Header creation
Truncated block payload (%lld/%llu bytes written)
bad seek
SharedArrayPush: pthread_mutex_lock failed\n
loading padding
MemBufferFlushToOStream
IFileStreamRead
writing updated prologue
Invalid compression type request %d
--> chunk %10llx %10llx -- %8zu\n
loading file ACL: %s
inserting MTM: %s
aaEntryXATBlobInitWithFD failed: %s
%12.2f decoding time (s)\n
Preloaded executable file
dat archive invalid
aaCacheStreamPRead
creating AFSC stream: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAConvertArchiveOutputStream.c
Context creation
Stream write failed
Final truncate
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetDecodeStream.c
reading payload
AAGenericRandomAccessInputStreamOpen
aaMalloc
Full replacement patch\n
OFileStreamWrite
BXDiff5 backend, out: %zu B, diff: %zu B, lit: %zu B, ctrl: %zu B\n
Invalid segment index: %u
Setting directories attributes (%s)\n
Invalid path, doesn't exist: %s/%s
invalid ACL entry type %c
Invalid worker id
computing buffer digest
Input buffer size mismatch: expected %llu B, got %llu B
threadPipelineWorkerThreadProc
BXDiff5 patch total size: %zu B\n
loading chunk offsets
deriving container offsets
AEADecryptInPlace
inserting AFR: %s
invalid ACL index %u
nRefs inconsistency
bad chunk position
add range
%s.json
SharedArrayInit: malloc failed\n
OArchiveFileStreamDestroyEx
- output\n
inserting UID: %s
hw.physicalcpu
stateCreateDirs
CCDeriveKey
Invalid encryption data size
ECCFixThreadProc
com.apple.ResourceFork
Invalid auth data size: %zu
Invalid segment offset: %llu, size: %zu
%12u symbolic links\n
finalize resource fork
0123456789abcdef
    comboPatch set, comboPatchSize=%zu (%zu MB)\n
invalid reverse index for OUT
temp stream open
create item data
Threads reported errors
ParallelCompressionAFSCStreamClose
ParallelCompressionAFSCFixupMetadataEx
convertStreamWriteHeader
Async stream reported errors
%12llu B file size\n
getStreamSHA1Digest
Literal
Writing decmpfs
offloadToFile
bytes remaining in obuf
treeRotateLeft %zd
MemBufferIncreaseSize
empty controls
invalid AEA stream
Invalid node: %llu
no valid DAT entry for cluster %d/%llu
retireThreadDequeue
write header
AEADecryptAsyncStreamOpen
Worker: encode block %5lld: %7llu => %7llu\n
(^\\Q
progress_proc
merge_controls
Pipeline failed: using in-thread compression
loadAndDecodeHeader_Ustar
opening file
encrypt signature
BZ2_bzDecompressInit
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c
MemBufferIncreaseCapacity
copy cluster header
%12llu bytes in archive\n
AAFieldKeySetCreateWithString
truncated node path
Invalid op
AEADecryptionRandomAccessInputStreamOpen
Blocksize: %llu\n
aaCacheStreamPWrite
file stream already opened
pthread_once
SegmentStreamSimulate
writing archive
pcWrite EOF failed
invalid signature size
ECDHE_P256_Recipient invalid sizes
load container
AAMemoryOutputStreamOpen
updateFromHeader
  Output: %s\n
SRC is empty
user cancelled in progress callback
ctrl_reader_create
Reading chunk data failed
hard link: %s
Invalid dir: %s
Warning: couldn't set F_NOCACHE on paged file\n
authenticating padding
Input digest failed
mkstemp
iterating to next non-empty blob
  Input %zu: %s\n
generate random field
extractToDirAsyncClose
Encode archive\n
inserting YEC: %s
loadAndDecodeHeader_Cpio
%12zu symbolic links\n
stateGetEntryData
Invalid path (subpath normalization failed): %s/%s
attribute data is too large name=%s
acl_get_permset_mask_np
Refill buffer failed
invalid state %d
Segment key derivation failed
applyYEC
Warnings:0x%08x
bxdiffEncodeBuffer
unexpected read call
PagedFileRetainOut
no cache
aaAssetExtractorStoreCheckpoint
Invalid segment state
decoder stream
cacheWrite
symlink
append AFT
write XAT
1 0x%x %u
AEADecryptAndExtractChunk
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetExtractor.c
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACacheStream.c
SharedArrayPop failed
truncate to final size: %s
inserting GID: %s
uid
storeDecmpfsXattr
HKDFDerive
aaCacheStreamOpen
generating random padding
writing cluster header
ForkOutputStreamPWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldYFP.c
Input doesn't match any of the expected patch inputs (in-place)
reading block header failed
invalid extractor state (blobs)
fetching Mach-O information: %s
AAEntryACLBlobCreate
Object archive BE
afscStreamWrite
getting next worker
clearing extended attributes
decodeStreamReadHeader
loading decmpfs xattr
read resource fork chunk
aeaContainerParamsInitWithRootHeader
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiff5.c
digest mismatch
zlib, level 5 (alias: zlib)
blob size mismatch
invalid out,outSize
InSituStreamPWrite
aaHeaderInitWithPath
inserting SH5: %s
acl_set_fd
bad duplicate
creating workBuffer
retrieving AFSC metadata: %s
    comboControls is NULL\n
Archive identifier size mismatch when resuming
single pass
applying ATTR: %s
aaEntryACLBlobApplyToFD
expected match type PREFIX for MAPTO rule
archive stream read error (blob)
buffer offset not aligned to holes
Could not identify compressed stream format
reading block payload failed
decryptToFileAsyncClose
initializing blob array
PagedFile: moving page from cache[%u] to cache[%u]\n
%12u entries with XAT field\n
writing DAT bytes
decoding block payload failed
SemAquire failed
Removing xattr
bad image
mkostemp
rangeDataGetRange
removing DAT
ParallelArchiveECCFixCommon
invalid chunk index
mem buffer creation
io_set_nocache
pushSegmentData
read data
chunkCount
capturing non-empty blobs
AEADecryptToStreamChunk
%12llu errors reported\n
workerUpdateDir
AAChunkAsyncStreamOpen
loading ACL blob
threadPoolWorkerThreadProc
getting entry full path
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEACommon.c
invalid XAT entry key %zu
ARCHIVE (smaller than patch): %s\n
computing YEC blob: %s
fork header
AAAssetBuilderGetParameter
patch_write
streamEnqueueWriteChunkToStream
initializing YEC field from path
DSAVerify_ECDSA_P256
aaInSituStreamOpen
processFileHeader
invalid node index
SharedArrayPush
ImagePatch: No variant found
Stream read
concatExtractPathEx
Worker thread creation
workerAllocBuffers
unsupported parameter
user callback returned an error
storing patch: %s
encoderStreamWriteBlob
Signature verification
SharedBufferWrite
applying ACL: %s
aaFileStreamRead err=%zd buf=%p n=%zu
decryptAsyncProcess
AAPathFilterAddRule
pAEA
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c
fsetxattr resource fork
unsupported entry type
retireThreadEnqueue
AAHeaderRemoveField
computing file digests
applyEntryAttributes failed: %s
no IDX
XAT blob
Invalid decoder state
MCO creation failed
write data
invalid state when resizing resource fork
AAChunkOutputStreamOpen
invalid file sizes
initializing header from path
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c
cluster has pending entries %d/%llu
extract thread BEGIN failed
ARCHIVE (different type/missing in some inputs): %s\n
writing page
Invalid block header payload=0x%llx raw=0x%llx block=0x%llx\n
Segment load
Some segments failed to process
Invalid number of inputs: %zu
compression type mismatch
(^
filter prepare
%s read
invalid XAT index %u
DH callback
(stream based)
control sequence broken
 BTM
AFSC compression failed: %s
DecodeAndExtract\n
clusterFree
x86_64h
truncated stream payload
Multi-thread read
BXDIFF_MATCHES_PROFILE
finishing entry
Segment %u: in queue for processing\n
workerSetDirAttributes
image size mismatch
treeAdd: %zd
Warning: extra bytes in patch (ignored)\n
removeStreamWriteHeader
streamPRead
apply YEC (copy)
Computing patches...\n
reading header magic
closeWithStateProc
ThreadPipelineRunWorker
%12llu bytes read from upstream\n
create copy: %s
aaFileStreamFlush
stream read failed
Invalid callback size return value
ParallelCompressionAFSCStreamOpen
Bad stream
retire failed entry
YAA link entry has no LNK field: %s
calloc ipos
too many variants
patch_read_header
stream not compatible\n
OMemStreamCreate
getErrorContextKey
workerDecodeAndApplyXAT
dir name too long
realloc_blob failed
encode
setting internal attributes
AAHeaderCreate
invalid blob reference
truncated entry when encoder destroyed
acquire segment in cache
invalid DAT blob
Segment compression failed
not enough bytes received
First pass fixup failed: %s, compression_type=%d (expected %d), resource_fork_size=%u (expected %u)
creating diff match lookup object
invalid compression_type: %d
PagedFileCreate
Patch can't be applied in-place
lzma_stream_decoder
Missing call to GetWorker before RunWorker
creating padding hash state
aaEntryAttributesApplyToPath
blob field size too large
reading header
aeaInputStreamClose
MappedBufferCreateWithFD
consumer proc reported an error
Client context callback returned an error
FIXUP (hard linked): %s\n
PagedFileDestroy
lzvn
aeaInputStreamLoadSegment
addSegment
Invalid container size
obtain AFSC data: %s
rename: %s
getFileSegmentSHA1DigestFD
apply YEC (extract)
aaForkInputStreamOpen
treeDeleteRangeWithPoint
ImagePatch\n  Input:        %s\n  Output:       %s\n  Patch:        %s\n  CryptexCache: %s\n  StaticContent: %s\n
SharedBufferCreate
FAIL
Invalid header field type
%12u segments to download\n
Name too long
extents overlapping
processSegment
%12llu differences ignored\n
control_reader_create
SimStream: pages: %i file, %i written, %i free, %i excess (%iK)\n
bxdiff5SetIn
invalid worker index
 [%s, %s, %s]
aeaKeychainCreateAttributes
Client progress callback reported an error
applying XAT
Abort requested
ECC applied 0x%08x: %s
storeFileContents %s
parsing entry header
aaEntryMCOStringCreateWithPath
get blob location
Diff stream applied
invalid header size: %llu
Fat binary 64-bit BE
aaFileStreamPWrite
sendMessage
AA entry missing/invalid PAT field
Cluster header encryption
Invalid resource fork size request: %u
lstat
reallocf
extents
BYE chunk %8zu evicted\n
  %u free pages in cache\n
ECC65537CheckAndFix
MemBufferIncreaseSize n is too large: %zu
Path too long: %s/%s
array too large
Segment received: %zu B\n
Invalid profile: %u
Stream processing cancelled
bad controls
encoding root header
invalid extract state
append YOQ
invalid stream type (0x%02x 0x%02x 0x%02x 0x%02x)
%s/%s
currentReadBufferEmpty
invalid file descriptor
readdir_r
setting attributes from header
AAByteStreamPReadAsync
aeaInputStreamUnlockCluster
%12llu fixed blocks\n
BXDiff5 patch archive payload: %zu B\n
storing archive id: %s
String insertion failed
unexpected blob key: received %s, expecting %s
%12u blocks in cache\n
ThreadPoolCreate
rawimg_add_fork
parseAPFSJSON
rawimg_force_in_place
aaEntryHashesInitWithFD
MemBufferFillFromBuffer n is too large: %zu
rangeInputStreamRead
creating compression stream %s
opening file: %s
Not a directory: %s
invalid path: %s/%s
clusterInsertEntry failed: %s
AAHeaderGetFieldType
parsing gzip header
Invalid segments per cluster count in root header: %u
invalid input dir: %s
Error 0x%08x\n
ACL blob
%12u entries in archive\n
AACustomByteStreamOpen
aaSequentialDecompressionIStreamOpen
creating shared buffer
remap_page
Invalid field size
entryMessage
%12llu bytes in archive (uncompressed)\n
storeChunkOffsets
SharedArrayDequeue
Invalid patch size
write after EOF
entry failed
blockGetFromCache
  In-place: %s\n
extractStreamEntryEnd
AAHeaderSetFieldString
bad fork
scrypt
verifySegment
Too many segments
allocating clusters
aaEntryXATBlobInitWithPath
getxattr failed for name=%s
Free pages after diff controls: %u\n
AEADDecrypt_None_MAC256_KEY256
invalid type %d, expected STRING
write DAT
corrupted stream header
invalid reverse index for IN
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOBasicStreams.c
aaFileStreamGetFD
open decoder stream
Scanning archive for variant %zu...\n
decoding compression payload
SharedArrayEnqueue
retain output chunk
bad chunk
aaAssetDecodeStreamSetParameterPtr
aaAssetDecodeStreamOpen
invalid auth_data key
creating symlink: %s
fcntl
AAHeaderGetFieldTimespec
loading entry blob
chunk out of bounds
processEntry
File a radar to increase obuf_capacity, sz=%zu
/XXXXXXXX
truncated remaining range file
invalid type %d, expected HASH
After input pages retained, %u free pages\n
bad extent
%12s %s\n
streamPWrite
invalid state on destroy
append FLI
aggregating entries
stateAggregateEntries
invalid/missing decmpfs
treeDelete: %zd
ParallelCompressionGetCompressedSize
writing padding
.tmp_decrypt
setupContext
temp file write
linkpath
invalid header in input stream
lstat after readdir failed (errno=%d): %s
extractStreamProcessDirs
could not resolve qualifier (type %c): %s
exactly one output, and 0 or more inputs expected
Main key derivation
Invalid compression algorithm
Invalid temp dir path: %s
%12u requests\n
AAByteRangeCreate
Blob encoding failed
depth loop
bad donor for: %s
no entry in thread
Invalid EOF record header
AADecompressionRandomAccessInputStreamOpen
file + excess != written + free
reading data segment
DAT size not received yet
invalid output size/decoder error: block=%lld, inSize=%lld, outSize=%lld, expectedOutSize=%lld
(\\Q
getTempSegmentFilename
AAEntryACLBlobAppendEntry
.dmg
fullReplacementBXPatch5
Invalid ECC magic
 SH2
%s stream: %llu bytes -> %llu bytes\n
stateCreateEntries
fields
%12.2f time (s)\n
RawImagePatchInternal
inControls[%zu] is not NULL
AAByteStreamProcess reported an error
remaining
uname
%12zu entries in output\n
Invalid checksum mode for decrypt to file, at least 256 bits are required
decrypting cluster
AEAEncryptionOutputStreamCloseAndUpdateContext
patch_apply
aaForkOutputStreamOpen
Invalid blockSize: %u
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c
fstat failed
Context setup callback returned an error
aaAssetDecryptionStreamOpenWithState
  target directory: %s\n
file can't be re-compressed: %s
flushCache
ThreadPoolRunWorker
Segment payload size mismatch
StringTableAppend
AA entry missing TYP field
reading magic
processing manifest
Generating asset...\n
PC_APFS_DISKIMAGE_MAP
loading AFSC stream state
yes
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/StringTable.c
Object archive
aaAssetDecodeStreamOpenWithState
Invalid AEA container (auth_data_size)
verifyDirectoryStreamClose
not implemented
load_variants
Creating directories\n
AADecodeArchiveInputStreamOpen
%12u workers\n
AAFieldKeySetInsertKey
verifyDirectoryStreamWriteHeader
invalid path %s/%s
computing file hashes: %s
alloc XAT entry
DAT,YEC,UID,GID,FLG,AFT,AFR
blob alloc
clearing UF_COMPRESSED
Invalid encrypted stream
Running stream threads
serializing state
segment_decode_to_buffer
main
graisPRead
invalid context
invalid offset=%llu, size=%llu for fd
createThreadErrorContext
could not determine entry type: %s
append PRC
inputPageData
AARandomAccessByteStreamProcess
decoding zlib payload
Invalid segment id\n
write ACL
pushPaddingRange
convert_block_controls
inserting INO: %s
alloc buf
ECC generation failed
getFilesystemBlockSize
inserting MCO: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c
mapping decode stream progress
append AFR
too many elements
Invalid item type %d
writeHeaderProc
get XAT
scanning manifest
no TYP
processSequential
setting attributes
  path checking: %s\n
rawimg_create_with_stream
cluster_id out of range
sub_asset
writing EOF
MemBufferDecreaseSize
close
bxdiff5CreatePatchBackend
alloc ACL entry
loadAndDecodeHeader_AA
Invalid shared secret size
Cluster header encryption key derivation
aaByteStreamPWriteExpected
Sending task to worker failed
Too many bytes received
pushControls
Hole creation
aaCreateArchString
decompressToData
malloc
reading from input stream
getFileDiskUsage
variant too large
Pipeline failed
finishing blob
aaEntryYFPBlobInitWithPath
%s/%08x
extractStreamSendEntryToRetireThread
reading page
workerDataAlloc
deriving segment key
com.apple.decmpfs
error: read more bytes than requested: %zd (requested %zu)
static content hint failed
chunk error
invalid field index %u
AATempFileStreamOpenWithDirectory
Magic received: %zu B\n
AAPathFilterApply
*full replacement*
File too large for AFSC
preallocation failed
initializing ACL blob: %s
GPU support functions
clearUFCompressedBit
<-- EOF\n
accumulating blob data
create dir failed: %s
invalid 'H' PAT
send entry to thread
inserting SH2: %s
%s-%zd.dmg
setUFCompressedBit
Segment count/size mismatch
aeaChecksum
reading segment data
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetDecompressionStream.c
streamProc
sending header
Missing field in new header
Invalid padding size
too many tasks
lockState
SharedArrayInit
SharedArrayPush: pthread_cond_signal failed\n
treeRebalance
Invalid item type
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAContextValidate.c
enumerateTree_rec
initFilterState
Couldn't convert to requested compression type
 FLG
 YEC
Header has already been sent
sending DAT blob
Readers reported errors
%12llu entries skipped\n
Segment %u: stored in cache\n
increase PathList capacity
update_field_sizes failed
aaEntryXATBlobInitWithFD
aaEntryACLBlobInitWithEncodedData
AAEntryACLBlobSetEntry
SH2,IDX,IDZ,SIZ,YEC
lz4
reading block header
OArchiveFileStreamCreate
 AFR
seek
%s (N=%u)
x86
alloc stream
write state
ILowMemoryDecoderStreamCreate
lseek failed
attributes from header
bxdiff5CreateComboControls
truncated read resource fork
could not locate the apfs diskimage map tool
aaArchiveFileOutputStreamOpenAtWithState
blob resize
readerProc
pushSegmentRange
aeaInputStreamDecryptSegment
increasing string table capacity
Caller cancelled
too many controls
rawimg_save_to_stream
Input retained
RS65537\n
Unsupported entry type (extract): %c\n
invalid type %d, expected TIMESPEC
invalid pax header
qualifier too long
Worker data allocation
open: %s
buf_capacity is too small
MemBufferCreate
setxattr
Segment data failed verification
invalid match type: %u
aeaCryptoInit
invalid range
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
loading file attributes: %s
storing entry in worker blob
Name out of range
Can't allocate header/footer
write checkpoint
AEAAuthDataGetEntry
mapto string is required for MAPTO rule
importing public key
x86_64
pc_array_compress
MemBufferDecreaseSize n is too large: %zu
pthread_mutex_lock
Write to stream
stateScanArchive
inserting TYP: %s
stateAssignLabels
OK
pthread_get_qos_class_np
get block data
decrypting segment %u
kSecUseDataProtectionKeychain
pthread_attr_set_qos_class_np
aaInPlaceStreamCancel
bxdiff5Free
decode stream reported errors
decodeStreamHLCFromINO
pc_array_compact
appendPathListWorkerProc
no
Write
SharedBuffer invalid capacity: %zu
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARemoveArchiveOutputStream.c
istream read
input is missing or invalid
Scanning target directory failed: %s
BXDiff5 patch allocated: %zu B\n
reading blob
aaEntryXATBlobInitWithEncodedData
ARCHIVE (empty in some inputs): %s\n
%12zu entries selected\n
invalid tar archive
invalid qualifier type: %d
generating shared secret
computing file digest
Signing callback
inserting FLG: %s
string too long
/XXXXXX
IDX,IDZ,SIZ
Mach-O 64-bit BE
Invalid archive: segment size mismatch
entry too large to defer
sending command payload
Too much fork padding: %zu
Invalid magic bytes
generate random bytes
reading prologue
extractStreamClose
invalid thread ID %d
invalid uncompressed size
invalid compression type: %d
%12zu chunk size (B)\n
getDefaultNThreads
statfs failed: %s\n
in[%zu] access out of range
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAContext.c
unexpected blob data received: %llu B
writing stream magic
copy, no compression
AAByteStreamTruncate
String too long: %zu
no LNK
entry not found, or not a regular file: %s
RandomAccessDecryptionStreamGetBlock
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/BlobBuffer.c
 lnk=%s
resourceForkSize
MemBufferTransmit
invalid raw stream
get attributes
invalid dir entry
missing LNK field
CheckAndFix: %s
reading from control stream
aaSimStreamOpen
SharedArrayEnqueue failed
%12llu ranges requested\n
mkdir: %s
acl_create_entry
aaEntryYECBlobInitWithPath
OBufferedStreamWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/../Common/SharedArray.h
loading file contents: %s
Can't init MCO
get temp dir
prepare zlib header
unexpected output buffer size
F_PUNCHHOLE failed
getFileSegmentSHA1Digest
BXDiff5 patch control payload: %zu B\n
 pat=%s
string table
LocalArrayInit
Invalid cluster header size
hashing file: %s
AAAssetExtractorDestroy
SharedArrayPop: pthread_cond_wait failed\n
fingerprint_consumer
notifySegmentAvailable
inserting BTM: %s
decompressing to regular data file
  ECC variant: 
storeFileContents
expected valid YOQ field
Prologue size mismatch
bxdiffFastPathControls
signing prologue digest
invalid path: %s
ImagePatch: Digest match. Output already correct.\n
Container size mismatch
    0x%06x diagnostic code\n
truncated read
comboControls is not NULL
creating decrypt stream
Segment %u: dequeue\n
fchmod
end entry failed
aaEntryACLBlobInitWithFD
encoderStreamWriteHeader
writing data blob
LocalArrayEnqueue
invalid blockSize in input stream
no file stream
bxdiff5CreateFullReplacementBackend
gid
aaFileStreamPWrite err=%zd buf=%p n=%zu off=%llu
common constructor
ChunkInputStream\n
pthread_attr_init
aaEntryAttributesApplyToFD
extractThreadSendCommand
invalid resource fork size
path too long
inserting path in table
clusterInit
stateCollectorStreamWriteHeader
Decoder: %s\n
%12llu common, OK\n
Signing
aeaContainerAppendSegment
<-- chunk %10llx %10llx -- %8zu\n
missing PAT
Mach-O
aaAsyncByteStreamIsCancelled
AEADEncrypt_AESCTR_MAC256_KEY640
unlock
skip dataless: %s
too many hard links or inconsistent nlink/ino data in archive
GPU program
Invalid segment index
sending dat magic
???
AEAContextGetFieldBlob
BXDiff5 patch archive payload size: %zu B\n
Segment file name too long
subSegment
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAArchiveFileStream.c
update file attributes
Encoding failed
workerLoadAndApplyACL
inserting DEV: %s
getTempDir
BXPatch5InPlace
ThreadPipelineCreate
Entry failed: %s
Missing call to RunWorker before GetWorker
invalid header in state
AEAContextGetFieldUInt
errors reported
invalid blob size
murmur64
processStream
Truncated segment
%12.2f percent usage\n
store blob
createErrorContextKey
creating retire thread
process dirs
add SLC field
header processing
writing back last segment data
Diff stream init
BXDiff5Data: n=%zu, nUnique=%zu\n
invalid input index
invalid type %d, expected BLOB
write chunk
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAChunkInputStream.c
creating DecryptAsyncStream
truncated stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAEncodeArchiveOutputStream.c
Could not reduce minFree to %d, something is wrong
decrypting segment
missing combo controls
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAChunkOutputStream.c
getBXDiffControls
Flush on underlying stream failed
getFreeCachePos
Segment write
no segment found
LZRAVEN
%12u segments in cache\n
%12llu B block size\n
Segment decryption
ParallelCompressionAFSCStreamWrite
aaAssetExtractStreamOpen
mapping patch file
aeaContextCreateWithPrologue
not implemented yet
opening file RW: %s
computing segment checksum
in-place patching failed
    in is NULL\n
add_control
process_input
mtime
aaFileStreamPRead
Invalid stream magic
invalid index
StringTableCreate
derivating cluster key
PagedFile: moving page from file[%u] to file[%u]\n
invalid compression algo
Stream close error
reading state
Directory expansion
AEADDecrypt_AESCTR_MAC256_KEY640
is
Not a directory: %s/%s
resizeResourceFork
RandomAccessDecompressStreamGetBlock
In-place patch matching entry %u\n
Invalid output digest
decoder failed
Fixed VM shared library file
Invalid segment size in cluster header
GetLargeFileControls
segment checksum verification
aaCompressionOutputStreamClose
rangeDataRemove
Invalid prologue
%12llu data bytes written\n
invalid XAT key
invalid resource fork for type
%12llu blocks in file\n
pushRange
reading from tool pipe
load and decrypt last segment
%12zu allocated chunks\n
loading last block
write: %s
get a valid chunk from cache
ImageDiff\n
inserting PAT: %s
invalid cache POS
AAAFSCStreamOpen failed: %s
SharedBufferFillFromStream
Warning: F_NOCACHE failed: %s\n
aaFileStreamPRead err=%zd buf=%p n=%zu off=%llu
Last block decompression
generating random encryption key
SharedArrayInit: pthread_mutex_init failed\n
create attributes
,0x%08x
Extraction failed: %s
get AFSC attributes
extractStreamProcessHLinks
Dynamically bound shared library
rawimg_query_forks
size
AppleEncryptedArchive
decrypting segment data
Final FULLSYNC
getting archive identifier
reserveDiffSegmentVector
afscStreamClose
blob segment mismatch
RNG failed
message callback cancelled operations
xhdr %s: %s\n
arm64e
unsupported compression type: %d
inconsistency in nRefs != 0
PagedFile: input page %u removed from storage\n
removing padding
ILowMemoryDecoderStreamCreateWithBuffer
reading chunk
write failed %zd
inserting SIZ: %s
AAAFSCStreamOpenWithState
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEARandomAccessDecryptionStream.c
invalid output PAGE
output page is not stored
%12llu entries in %llu clone clusters (CLC)\n
RunWorker
Cryptor creation
treeRebalance: %zd
qsufsort32
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFileAsyncStream.c
 LargeFile: Block = %5u, %5u K cache, %6zu controls\n
applying ACL
  checksum: %s\n
AEAAuthDataAppendEntry
Invalid compression type %u
Dst fixup %c%s %s\n
GetLargeFileControlsWithStreams
writerProc
symlink %s
append MOD
decryption stream
Truncated block header (%lld/16 bytes read)
HMAC verification
com.apple.ParallelCompression
invalid in,inSize
pushSegmentData failed
%12u entries\n
AAHeaderGetFieldHash
aeaOutputStreamWorkerThreadProc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAContainer.c
ThreadPipelineGetWorker
storeRemainingRange
AAEntryXATBlobRemoveEntry
aaStrdup
AATempStreamOpen
empty segment vector
%12llu entries removed\n
byte stream read error
computing file digests: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAGenericRandomAccessInputStream.c
could not move output page in cache
pcRead
Invalid args
Truncated stream
sendEOF
fork_realign
ThreadPipelineDestroy failed
processClusterHeader
AEAKeychainLoadItem
ImagePatch: Patching with excess space <= %d bytes.\n
Root header encryption
increaseCapacity
invalid cache pos
Invalid size received: %zu\n
AAVerifyDirectoryArchiveOutputStreamOpen
Invalid stream type
reading DAT file
Invalid archive stream
received too many bytes %llu/%llu
write DAT file
missing LNK
futimes
jsonPushValue
DST is not empty
rawimg_load_chunks_from_stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/BXPatch5.c
Invalid ECC header
areFilesEqual
invalid buffer
read blob from archive
MemBufferFillFromBuffer failed
writing chunk
AACompressionOutputStreamOpen
Tree normalization
inserting AFT: %s
invalid rule type: %u
generating random salt
  - Variants:   %d\n  - Flags:      %llx\n  - # controls: %llu\n  - Patch size: %llu bytes\n    - Metadata: %llu bytes\n    - Controls: %llu bytes\n
  %u free pages in file\n
cacheFlush
Write failed
%12u ECC parity size per block\n
ChunkPipelineDestroy
input controls already present
Fat GPU binary
ThreadPipelineDestroy
patch_verify_header
Path too long: %s
Invalid hole size
creating shared data buffer
failed to create clone: %s
extra data received for blob %s: received %llu, expecting %llu
flushIBuf
Checksum verification failed, data corrupted
aeaInputStreamRead
%12u block size\n
fsetxattr resource fork header
aaFileStreamWrite
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPool.c
%s \"%s\"
IDecoderStreamCreate
aaAssetExtractStreamSetParameterPtr
allocating header
PagedFileReadAndReleaseIn
AEAAuthDataSetEntry
Segment checksum failed
memoryOutputStreamWrite
aeaContainerFinish
NULL stream
InSituStreamClose
decodeStreamReadData
running task
invalid request
Writing resource fork header
    inControls is NULL\n
AAEntryXATBlobApplyToPath
stateComputePatches
unable to load input page
creating combo controls requires 2 or more unique inputs
AEAContextGetContainerSizeUpperBound
Fat binary BE
virtual fork
invalid field subtype: %d
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAssetGenerate.c
All entries:\n
size mismatch: %s
rawimg_create_with_path
zlib
Invalid ECC variant: %u
aaInPlaceStreamSeek
Stored remaining range is not a subset of initial range
manifest read
stateCreateClusters
extractStreamWriteBlob
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/LargeFile.c
cacheRead
AEAEncryptionOutputStreamOpen
%12llu data size\n
reserve buffers
patching failed: %s
Invalid payload
ImageDiff: Removed non-unique input variant <%s>.\n
callback signaled abort
blockReader
loading segment: %u
invalid HASH subtype: %d
LNK blob
compute patch
allocating mem buffer
invalid XAT index
fsync
aaAsyncByteStreamAlloc
initializing YFP field from path
truncated state
aaInPlaceStreamClose
AAByteStreamProcess
Fixed data using ECC: %s
AAEntryYECBlobCreate
client callback cancel
inconsistency in nRefs == 0
bad algo
Streaming data setup
invalid length
workerDeferEntry
invalid entry final state %d: %s
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtract.c
removeEntryProc
file not empty
Verifying file: %s\n
AEAContextCreateWithEncryptedStream
invalid segment sizes
invalid directory: %s
realloc_keys failed
Segment %u skipped, offset=%jd, payload=%u, raw=%u\n
processMagic
async stream alloc
set PAT
flushing chunks to stream
processPadding
reading file header
Password is too short
no SIZ: %s
BXDiff5
flushing buffer
runWorker
OK      %s\n
updating YEC field
String table creation
invalid key
invalid ACE flags: 0x%016llx
Client post-unlock callback returned an error
compressed stream detected : try compression_tool
%12llu INVALID BLOCKS\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ThreadPipeline.c
compressed content
AASharedBufferPipeOpen
Async stream returning EOF, but we still have ranges in flight
aaCacheStreamTruncate
worker reported errors
invalid XAT blob size
invalid ACL blob size
invalid YEC variant: %u
SharedArrayPush: pthread_mutex_unlock failed\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/ErrorCorrection.c
process range
dirInsertEntry
parsing profile: %s
Stream write failed: %s
creating encryption context
flush buf
generating padding
write blob to stream
Copy %c %s\n
resizeStream
flushBuf
aaByteStreamReadExpected
open checkpoint path: %s
unlocking next cluster
AAArchiveStreamProcess
write resource fork
invalid dir: %s
 FLI
stream read error
loading block
Input
pc_array_indirect_sort
creating worker pool
aaAssetExtractorCreateWithCheckpoint
Invalid archive
SemRelease
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAAsyncByteStreamProcessAllRanges.c
extract stream reported errors
realloc blob
Invalid entry path
too much data
read failed
fchflags UF_COMPRESSED
stat: %s
String table insert
creating shared command buffer
truncated header
AAHeaderSetFieldBlob
%s variant <%s> | %llu bytes | %zu extents | %zu forks (%llu/%llu) | digest=%s\n
Padding received: %zu B\n
/System/Library/Filesystems/apfs.fs/Contents/Resources
ParallelArchiveECCVerifyCommon
loading profile: %d
entry processing
retireEntryRange
aaEntryXATBlobApplyToFD
chunkWriteToStream
read chunk
input page is not stored
sending blob data
aaAssetDecompressionStreamOpen
append to ibuf
invalid chunk
Async stream receiving an unknown segment
pcWrite
invalid attribute size
bad map
prepareFilter
aaCacheStreamClose
decrypting cluster header
ParallelCompressionAFSCStreamWrite failed with status %d
creating YEC context
create access control
Can't shrink resource fork: %s (current %u, target %u)
<<< range %10llx %10llx\n
creating entries
invalid fd
missing reference entry in cluster
pread failed
writing data
BXPatch5StreamWithFlags
Archive stream init
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c
getting header blob field
truncating sub asset
Invalid state
invalid imbalance: %d
init_blob_with_magic
%12u messages\n
Invalid public key size
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtractAsyncStream.c
aaCheckAndFixWithPath
encodeEntry
Invalid compression type %u in decmpfs xattr
open failed: %s
 ACL
AAByteStreamPReadAsync barrier
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEAEncryptionStream.c
deriving signature encryption key
SharedArrayPop: pthread_mutex_lock failed\n
aaAssetDecompressionStreamOpenWithState
 MOD
Hole append
add CLC field
signing prologue
%12zu ECC buffer size\n
fsetxattr decmpfs
truncated write: %s
copy file: %s
can't generate a field from DAT, and keep DAT at the same time
AEAContextGenerateFieldBlob
AEADecryptionDirectRandomAccessInputStreamOpen
creating new worker
ftruncate
bad input size
User cancelled operation
workerApplyAttr
read resource fork header
reallocating block blob
reading payload failed
clusterEntryUpdateDAT
AAEntryXATBlobSetEntry
Thread creation
aeaContainerReencrypt
%12zu block count\n
Key generation
streamReadChunkData
openProc
cached input page does not have a file position
moving page from disk to cache
Incompatible page size
updating new header field
block already consumed
AFSC stream close
SharedBufferAbort
fixup failed: %s
bad fork compressed
Output copy failed\n
Flush chunk pipeline
truncate temp file
getSegmentFile
creating the ECC stream
inserting next cluster header range
Warning: F_SETSTATICCONTENT failed with error %d: %s\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADirectRandomAccessDecryptionStream.c
Context can't be modified
HLC field found, not supported: %s
allocating final blob
invalid private key size
ParallelCompressionAFSCGetMetadata
tempStreamPWrite
getFieldBlob
extract cluster entry failed: %s
AAHeaderSetFieldTimespec
Truncated block header (%lld/16 bytes written)
Padding generation and hashing failed
OSHA1StreamCreate
opendir failed with errno=%d: %s
aaEntryYECBlobInitWithFD
Decode archive\n
compute patches
AAMagicInputStreamOpen
inserting XAT: %s
BXDiff5 patch capacity: %zu B\n
building fast path controls
missing PAT field
invalid input PAGE
AACustomArchiveStreamOpen
AEAAuthDataRemoveEntry
Invalid compression algorithm key in root header: %u
Invalid segment size in root header: %u
Hole fill
blob too large
bad chunk info
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAVerifyDirectoryArchiveOutputStream.c
randomAccessWorkerProc
OArchiveFileStreamWrite
stateRetireRanges
inserting LNK: %s
Invalid/non-supported archive stream
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c
writeProc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEACrypto.c
cache too big
aeaContainerRemoveLastSegment
pthread_mutex_unlock
bxdiff5CreateInControls
verifySegmentProc
sha256
re-encrypting container
invalid raw size
AAHeaderSetFieldFlag
inserting XAT entry
movePage
dat decompression stream
invalid input path
building diff controls
hlinkInsertEntry
No-op patch matching, writing input\n
Invalid resource fork xattr
outputPageData
DerivePublicFromPrivate_ECP256
WriteAlignedChunkProc
flushToResourceFork
 SH5
too many excess pages
flushing cache pos
unlockState
buffer full
Expanding resource fork
file stream
AAExtractArchiveOutputStreamSetQuarantine
no IDZ
rawimg_digest_worker
processPrologue
%12llu removed\n
    comboControls set, nControls=%zu, inPlace=%d (%zu MB)\n
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelPatch/PagedFile.c
Invalid segment bounds
Input doesn't match any of the expected patch inputs
user error
cloning file, falling back to copy, failed: %s
stateAppendEntry
SH2,IDX,IDZ,SIZ
finalizeResourceFork
aaCalloc
Invalid magic
invalid variant
entry size mismatch
invalid payload size
aaEntryACLBlobInitWithPath
Warning: ACL tag type is not ALLOW/DENY (ignoring entry): %d\n
string table append
snprintf
Invalid segment sizes
ImagePatch: Digest match. Copy input to output.\n
sysctlbyname
append FLG
encodeYOPEntry
send worker message
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c
SimStreamSimulate
Container size is too large to allow padding
.AssetExtractCheckpoint
writing block header
aeaOutputStreamWrite
 GID
concatSourcePath
AAFieldKeySetCreate
ECC buffer overflow
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAInPlaceStream.c
stateScanVariants
decompression failed
decryptAsyncClose
parse stored header
Before applying control
copy header size
Cluster header received: %zu B\n
blob byte count mismatch
invalid archive
writing output
SharedBufferFlushToStream
lseek failed and pos < s->pos
update global header
patch path: %s
initializing XAT field from path
end of stream cancel
writing block payload
r
afStreamWrite
%s\n
aaCompressionOutputStreamWrite
rawimg_init_algorithm
invalid header blob size
no more writes possible
invalid auth_data index %u
Invalid encryption parameters
Truncated ECC buffer
truncated read: %s
stateFetchRanges
invalid header state
invalid sizes in manifest
archive stream read error (header)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAByteRange.c
io_preallocate
out is not NULL
aaAssetDecryptionStreamOpen
segment already in cache
AAJSONInputStreamOpen
\\E$)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AACompositeChunkAsyncStream.c
writing container headers
MappedBuffer fstat
Too many arches
Invalid password/salt
Total time %.2fs, %.2f MB/s (%s)\n
not a regular file: %s
Capacity increase
prepare non zlib header
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/SharedArray.h
Decompression
chunkAsyncGetRange
String table merge
AAHeaderSetFieldHash
Invalid entry: no TYP field
writing data segment
creating internal buffer
 SH3
Chunk creation
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldXAT.c
aeaOutputStreamRunCurrentWorker
no PAT field in header
AATempStreamOpenWithDirectory
storing deferred entry
?
resourceForkHeaderSize
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAArchiveStream.c
createThread
    in set, inSize=%zu, inSHA1=
Missing IDX,IDZ from archive decoder
io_set_nocache %s
some input bytes are still mapped after diff expansion
Warning: container truncate failed
Invalid entry missing TYP field (skipped)
missing out
generic controls
invalid blob sizes
stat failed: %s
lzma
loading cluster header
AEAKeychainHasItem
streamWriteChunkData
extractStreamProcessClusters
failed to create hard link: %s
invalid field index
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAFieldYEC.c
no digest info
%12llu entries\n
reading padding
IDecoderStreamThreadProc
creating directory: %s
retireThreadProc
dirInsertEntry failed: %s
data already written
Encoder: %s\n
aeaDeriveMainKeyNew
Invalid KDF parameters
SemAcquire
append to buf
  manifest: %s\n
Invalid checksum in root header: %u
updateLabel
abort from callback
%12.2f encoding time (s)\n
store decmpfs xattr
Invalid stream compression key
digest
%12u entries with ACL field\n
REMOVED %s\n
compression_stream_init
invalid I=%zu
Chunk has already been written
loading dir entry
truncated entry when header encoded
Invalid context
Invalid signature
copyFileWithAttributes
realloc_keys
cluster init
refill buffer
unable to load output page
inserting first cluster header range
mkdir failed: %s
Encryption
aeaContainerLoadSegment
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARandomAccessDecodeAndExtract.c
workerCreateEntries
invalid 'D' PAT
init ops
nlink mismatch
Diff
%12llu final patch size\n
aaEntryAttributesInitWithFD
invalid entry data
dataless dir error: %s
realloc_fields
append BTM
initializing ACL field from path
stream cancelled
invalid compression type %d
invalid ACL entry
writing to digest stream
    - %s stream: %llu bytes\n
invalid size
Warning: couldn't set F_NOCACHE\n
Payload compression
YAA device entry has no DEV field: %s
lzraven
Invalid out segment in patch
BXDiff5WithIndividualPatches
patch doesn't allow in-place
Chunk still has holes
aaCompressionOutputStreamFlush
run worker
creating header
too many inputs/outputs
Final FULLFSYNC
mergeDiffSegmentVectors
entry creation
inconsistent blob key
Archive path list\n
updateFileAttributes
corrupted resource fork
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAsyncStream.c
afStreamCloseWithState
failed to start decoder thread
Missing resource fork xattr
convertStreamToNextNonEmptyBlob
%12llu archive bytes\n
invalid ._ entry
computePatchesWorkerProc
File too small for AFSC
mutex lock
store remaining range
creating directories
PagedFile: vacating file pos\n
read: %s
TMPDIR
read resource fork
AAFieldKeySetClone
String table sorting
flush output buffer failed
getComboControlsFromMergedDiffSegmentVectors
create
invalid nlink
ECDHE_P256_Sender invalid sizes
AEADecryptionInputStreamOpen
sequentialWriterProc
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/IOCompressedStreams.c
invalid size=%llu for fd
controls_append_copy_forks
invalid blob segment
AAByteRangeClone
aaCopyFile
header copy
corrupted archive header
initializing crypto params
AAMemoryInputStreamOpen
retiring ranges
lockedStateReserveChunks
read
MemBufferIncreaseCapacity out
stream not in-place compatible\n
blockWriter
Segment %u: %zu B processed\n
acl_set_qualifier
bad variant
invalid block ID in write thread %lld
AEAEncryptionOutputStreamOpenExisting
ImagePatch: Patch not created with in place. No bound on needed excess space.
AARemoveArchiveOutputStreamOpen
Invalid padding_alignment
chunkAsyncProcess
invalid c_namesize
remaining.tmp
missing IDZ field
internal streams
deriving cluster header key
increasing blob capacity failed
Broken pipeline
stateStreamEntryBlob
max level reached
aeaDeriveMainKeyExisting
Patch matching entry %u\n
append UID
AADecompressionInputStreamOpen
Invalid chunk size
AAExtractArchiveOutputStreamOpen
sending command
disable AFSC by clearing UF_COMPRESSED
AAFileStreamOpenWithFD
obuf full
aaAssetExtractorCreateCommon
TODO(%c) %c %s\n
streamClose
invalid key set: %s
corrupted file data, ECC failed 0x%08x: %s
COPY: %s\n
invalid stream
CacheStream: read ops %zu/%zu, write ops %zu/%zu\n
DAT
Relocatable object file
decryptAsyncGetRange
Invalid segment size
AAAssetBuilderAddVariantArchive
invalid padding state
loading and applying ACL
aaPReadExpected
Companion file with only debug sections
PRead
AAHeaderAssign
flush cache
current PagedFile state
bad variant size
lstat %s
compressionWorkerProc
Invalid signing private key in context
Truncated read n=%zd pos=%llu read=%u fd=%d
worker proc reported an error
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Utils.c
entry already linked
alloc holes
AEAKeychainRemoveItem
BXDiffMatchesCreate
too many writes pending
streamThreadProc
copyStream
initBestMatchFromHashes
Src check %c %s\n
patch_write_stream
writing data to temp file
could not find unique input
setting directories attributes
%12llu fixed bytes\n
pos not reached
invalid xhdr entry
aaEntryYECBlobInitWithEncodedData
x86_64 kexts
invalid temp_dir: %s
AAAFSCSetMetadata
PagedFile: assigning cache[%u] to new output page %u\n
set YOP
Invalid output digest after patch application
bad page index
AAHeaderGetFieldBlob
ACL entry size out of range
BlobBufferStore
copy failed %lld
acl_add_flag_np
Writing to ostream failed
Invalid compression algorithm in context
ADDED   %s\n
invalid block size
Truncated write n=%zd pos=%llu read=%u fd=%d
scanning archive
couldn't determine worker_id
could not move input page in cache
Invalid state, file already open
Segment verified: offset=%llu size=%zu\n
%12.2f x compression ratio (%s)\n
bad extent size
seekTo
Temp file exists but is not a regular file: %s
inserting CKS: %s
AAFileStreamOpenWithPath
bad extent pos
AAAsyncByteStreamProcessAllRanges
    out set, outSize=%zu, outSHA1=
 LargeFile: Using %zu M for hashing.\n LargeFile: Using %zu M for fingerprints.\n LargeFile: Parsed %zu M in %0.2f (s). Added %zu/%zu fingerprints.\n
%u entries failed to extract
Post-processing ctrl for in-place patching, %u pages\n
Demand paged executable file
cachePageGet
Invalid patch header
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AARandomAccessByteStreamProcess.c
data missing
applyEntryAttributes
read state
digesting prologue
aaByteStreamSimulate
AAChunkInputStreamOpen
file not open
rawimg_create_with_file
append GID
ctrl[%zu]: moving %llu bytes from diff to lit (minFree=%d, ndiff=%llu)\n
rawimg_verify
string table creation
Invalid sizes in root header
Reading chunk
Thread shutdown
no digests found
workerProc
Truncated block payload (%lld/%llu bytes read)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchive/AAPathFilter.c
malloc holes failed
reserving chunks
 AFT
writeBlobProc
Hash collision detected: %s != %s
AEAD can't operate in-place
Dropping %llu bytes at %llu, needed=%llu bytes, type %s\n
insertion failed in string table
GetRange
 %c
ARCHIVE (not a regular file): %s\n
No more data
rawimg_compact
%12llu entries in %llu same data clusters (SLC)\n
Extract %c %s\n
 UID
AAEntryACLBlobApplyToPath
length
derivating segment key
pthread_attr_setstacksize
resizing stream
    inControls set, nControls=%zu, inPlace=%d (%zu MB)\n
AAEntryACLBlobGetEntry
write blob
ThreadPoolGetWorker
cachePageReadFromDisk
workerCreateDirs
reading magic bytes\n
Invalid block_id, or no workers available
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/ParallelCompression/Filter.c
corrupted stream
    %zu active chunks\n
```
