# `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 137,616 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2144)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression (compatibility version 1.0.0, current version 182.40.4)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/liblzma.5.dylib (compatibility version 6.0.0, current version 6.3.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (212)

```
%s:%d: Error: value for %@ is not a number, assuming %d\n
Synchronous
/System/Library/PrivateFrameworks/AppleFSCompression.framework
IO
emitCurBuffer
%s:%d: fileOffset=%llu is too big: %s\n
%s:%d: validate(%s): %s\n
%s:%d: Error: file type of %s is out of range\n
MH_DSYM
%s:%d: Error: value %@ for %@ could not be parsed\n
running %s task after finish
%s:%d: %p %p %p %p %p %p %p %p %p %p: Error: setting compressor error to %d (%s)\n
decompressIfNecessary_block_invoke_3
%s:%d: Error: unknown compression scheme %llu\n
%s:%d: write %s: %s\n
%s:%d: Error: compression ratio needs to be between 1 and 100\n
%s:%d: pread(%s): %s\n
SkipMachOFileTypes
numChunks <= UINT32_MAX
%s:%d: %s: fgetxattr: %s\n
%s:%d: %s: position=%lld is too big\n
%s:%d: %s: workbuffer allocation failed\n
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Libraries/CompressData/CompressData.c
%s:%d: Error: invalid kAFSCDispatchQueuePriority value %d\n
ioqueue
Flags
%s:%d: Error: StreamCompressor %p path: %s
%s:%d: fstat %s: %s\n
%s:%d: %s: readRscData: (%llu, %zu), returned size [%lu]\n
%s:%d: Error: type %d out of range\n
%s:%d: Error: size of %s EA is too small (%zd < %zu)\n
%s:%d: Error: size of %s EA is too big (%zd)\n
DispatchQueuePriority
Key 'RuleType' was not a string while evaluating compression rule at index %llu\n
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/ChunkCompression.cpp
%s:%d: %s: expected size %u, found %llu\n
%s:%d: add overflow: offset %llu, totalSize %llu\n
%s:%d: invalid offset: %llu\n
%s:%d: Error: SkipMachOFileTypes value at index %lu is not a number or string\n
MH_OBJECT
%s:%d: chunk %u produced %lld of %lld expected bytes\n
%s:%d: setrlimit(RLIMIT_NOFILE.rlim_cur = %lld): %s\n
%s:%d: sysctl: %s\n
read request from %d: %s
%s:%d: stat /: %s\n
%s:%d: fchmod %s: %s\n
MH_CORE
%s:%d: open '%s': %s\n
%s:%d: FinishStreamCompressorQueue: %s\n
A path match key had a value that was not a string, while evaluating compression rule at index %llu\n
incorrectly released
%s:%d: %p %p %p %p %p %p %p %p %p %p: Error: wrote %llu bytes but expected %llu bytes\n
%s:%d: fstatfs %s: %s\n
Failed to apply system rules.\n
%s:%d: Error: StreamCompressor %p stack: %@
%s:%d: dup %s: %s\n
%s:%d: fcntl %s: %s\n
%s:%d: open %s (%s): %s\n
%s:%d: Error: failed to write %zu bytes to %s(%d) at %llu: %s\n
%s:%d: %s: invalid zlib header\n
%s:%d: getrlimit(RLIMIT_NOFILE): %s\n
MH_DYLINKER
None of the keys 'RuleType', 'Flags', or 'InverseFlags' were found while evaluating compression rule at index %llu\n
/dev/afsc_type5
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/pathUtils.c
%s:%d: Error: returning errno %d (%s) from DrainStreamCompressorQueue\n
CompressionTypes
CompressionLevel
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/StreamCompressor.cpp
%s:%d: %s: readRscData: (%llu, %zu), returned error [%d]
v32@?0Q8Q16r^{?=QQQ}24
unknown request type from %d: %lld\n
%s:%d: open(%s): %s\n
%s:%d: stat %s: %s\n
MH_DYLIB
AFSCThrottledIO
IgnoreXattrErrors
%s:%d: Error: StreamCompressor %p %s. PLEASE FILE A BUG AGAINST AppleFSCompression/X
%s:%d: %s: resource fork offsets are out of order (offsets[1] (%u) <= offsets[0] (%u)) \n
%s:%d: allocation of %zu bytes failed\n
PathExactlyEqualsString
%s:%d: Error: freed StreamCompressor for %s without closing data fd\n
%s:%d: Error: unknown compressor %d\n
%s:%d: Error: could not use desired max fds of %d, using %llu instead\n
send response to %d: %s
%s:%d: statfs %s: %s\n
fd
%s:%d: Error: invalid %@ value %@, assuming %d\n
MH_FVMLIB
MH_PRELOAD
Exclude
stats
%s:%d: open resource fork %s: %s\n
%s:%d: %s: readRscData: (0, 0), returned error [%d]
MH_BUNDLE
i24@?0r^v8Q16
%s:%d: Error: SkipMachOFileTypes value is not an array\n
*
%s:%d: Error: shouldn't use compressor type %d since it is a single chunk compressor, using %d instead\n
scheduling %s task after compression finished
%s:%d: Error: freed StreamCompressor for %s without closing rsrc fd\n
i8@?0
borrowed buffer queue
%s:%d: Error: invalid item '%@' at index %ld in SkipMachOFileTypes dictionary\n
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Libraries/CompressionQueue/CompressionQueue.c
SystemCompressionRules
Invalid value found for key 'RuleType' while evaluating compression rule at index %llu\n
%s:%d: %s: unknown compression scheme %llu\n
%s:%d: %s: allocating buffer of size %u failed\n
%s:%d: getattrlist %s: %s\n
%s:%d: Error: decompressing %s changed its data!\n
failed to convert string\n
%p 
%s:%d: %s: fgetxattr(%llu,%zu) returned %zu\n
%s:%d: Error: Unknown compression scheme encountered for file '%s'\n
MH_DYLIB_STUB
AllowStoringDataInXattr
ForceAsynchronous
scheduling %s task after finish
%s:%d: getrlimit: %s\n
v8@?0
%s:%d: read %s: %s\n
MH_KEXT_BUNDLE
%s:%d: Error: value for %@ is not a string or number\n
Failed to apply user rules.\n
Rule at index %llu was not a dictionary\n
%s:%d: Error: freed StreamCompressor for %s that is still has a curBuffer\n
double-closed
%s:%d: Error: Uncompressed size for path '%s' as reported by stat did not match size in disk header!\n
Key 'InverseFlags' was not a number while evaluating compression rule at index %llu\n
magic numbers have been clobbered (0x%08x 0x%08x)
allocating buffer of size %zu failed
%s:%d: Error: freed StreamCompressor for %s that is still locked\n
%s:%d: %s: resource fork is too small (actual size: %llu < expected min size: %llu) header: (attr_size %u, compression_type %u, uncompressed_size %llu)\n
%s:%d: %s: attempting to read chunk %u from file with %u chunks\n
%s:%d: %s: vecTotal=%lld is too big for compression algorithm 0x%x\n
%s:%d: open %s: %s\n
%s:%d: Error: the first mach header of %s is not in the first %zu bytes, assuming we need to skip it\n
AllowLargeResourceForks
%s:%d: %s: allocating buffer of size %llu failed for compression algorithm 0x%x\n
%s:%d: Error: size of %s EA changed\n
%s:%d: lchmod %s (%s): %s\n
CompressionRules
StreamCompressor.cpp
bufSz == uncmpSize + 1
%s:%d: fgetxattr %s: %s\n
%s:%d: %s: expected chunk count %u, found %u\n
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/ThrottlingAllocator.c
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/StreamCompressorQueue.c
%s:%d: %p %p %p %p %p %p %p %p %p %p: Error: setting queue error to %d (%s)\n
%s:%d: Error: value for %@ is not a boolean, using default value (%s)\n
SkipMachOOverridePaths
RuleType
%s:%d: Error: StreamCompressor %p queue: %s
finalized before it was finished
%s:%d: setBsdflags %s: %s\n
Include
PathContainsString
ChunkCompression.cpp
%s:%d: %s: decmpfs xattr size (%u) should be greater than decmpfs disk header size (%zu)\n
/
MaxCompressionPercentage
plist
%s:%d: futimes %s (fd %d): %s\n
com.apple.decmpfs
%s:%d: %s: fgetxattr(%llu,%zu): %s\n
%s:%d: Error: _InitCompressionRules failed (malformed plist?)\n
%s:%d: fchmod %s (fd %d): %s\n
com.apple.ResourceFork
%s:%d: %s: decode failed for compression algorithm 0x%x\n
AFSC_MAX_FDS
%s:%d: Error: using max fds override of %d\n
PathEndsWithString
InverseFlags
Key 'Flags' was not a number while evaluating compression rule at index %llu\n
String to match against not found while evaluating compression rule at index %llu\n
%s:%d: Error: freed StreamCompressor for %s that is still has a compressionBuffer\n
written to after it was closed
%s:%d: Error: wrote %llu bytes to file of size %llu\n
MH_EXECUTE
PathBeginsWithString
IOManager
%s:%d: ftruncate %s: %s\n
v24@?0^v8@?<v@?>16
%s:%d: lstat %s: %s\n
%s:%d: Error: Compressed file at path '%s' had incorrect magic in disk header\n
%s
true
decompression
afsc open: %s
/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/commonUtilsUser.c
%s:%d: Error: storing data in xattr not allowed\n
CompressedFile
%s:%d: %s: unknown chunking scheme %llu\n
%s:%d: Error: Type %d compressed file at path '%s' did not have a resource fork\n
false
finalized before it was closed
%s:%d: Error: invalid close flag %d\n
%s:%d: fsetxattr %s: %s\n
%s:%d: Error: chunk %d of %s decompressed to %u, expected %u\n
%s:%d: Error: processFileData %s: %s\n
%s:%d: decompress: %s\n
%s:%d: WriteToStreamCompressor(%s): %s\n
compression
running %s task after compression finished
%s:%d: write: %s\n
curBuffer
..namedfork/rsrc
%s:%d: %s: invalid resource map\n
%s:%d: %s: decmpSize=%zu is too big\n
%s:%d: getxattr(%s): %s\n
%s:%d: unsetBsdflags %s: %s\n
```
