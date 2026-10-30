# `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

From the upgrade restore ramdisk (141-29011-104.dmg). 5,206,464 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 46 (Size: 6408)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (28)

- `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2 (compatibility version 1.0.0, current version 598.40.4)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit (compatibility version 302.0.0, current version 944.0.0)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/local/lib/libcurl.4.dylib (compatibility version 7.0.0, current version 9.0.0, weak)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages (compatibility version 1.0.8, current version 710.0.0, weak)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (84 classes, 8 protocols)

Classes: `AAS3DownloadRequest`, `AAS3DownloadSession`, `AEABackendXPC`, `BackendXPC`, `BaseDiskImageCreator`, `BlankDiskImageCreator`, `CryptoBackendXPC`, `DIAPFSPartition`, `DIAttachParams`, `DIAttachedDeviceInfo`, `DIBaseAgentDelegate`, `DIBaseAgentXPCHandler`, `DIBaseParams`, `DIBaseServiceDelegate`, `DIBaseXPCHandler`, `DIBlockDevice`, `DIChpassParams`, `DIClient2Controller_XPCHandler`, `DIClient2IODaemonXPCHandler`, `DICommonAttach`, `DIController2ClientDelegate`, `DIConvertParams`, `DICreateASIFParams`, `DICreateParams`, `DICreateRAWParams`, `DICreateUDSBParams`, `DIDataPartition`, `DIDeviceHandle`, `DIDiskArb`, `DIDiskArbEmulation`, `DIDiskImageBridge`, `DIDiskMountTracker`, `DIEncryptionChpass`, `DIEncryptionCreator`, `DIEncryptionFrontend`, `DIEncryptionUnlocker`, `DIError`, `DIHelpers`, `DIIOIterator`, `DIIOMedia`, `DIIOObject`, `DIImageHandle`, `DIImageInfoParams`, `DIKeyRetriever`, `DIOpenParams`, `DIResizeParams`, `DISLAFrontend`, `DIShadowChain`, `DIShadowNode`, `DIStackParams`, `DIStatFS`, `DIStatsParams`, `DITemporaryPassphrase`, `DIURL`, `DIUserDataParams`, `DIVerifyParams`, `DiskImageCreatorFromDevice`, `DiskImageCreatorFromFolder`, `DiskImageGraph`, `DiskImageGraphNode`, `DiskImageParamsASIF_XPC`, `DiskImageParamsLocked_XPC`, `DiskImageParamsPlugin_XPC`, `DiskImageParamsRAM_XPC`, `DiskImageParamsRaw_XPC`, `DiskImageParamsSparseBundle_XPC`, `DiskImageParamsUDIF_XPC`, `DiskImageParamsXPC`, `DiskImages2`, `FastFolderCopierWrapper`, `FileLocalXPC`, `KNOXBackendXPC`, `MKDIDevice`, `NSMutableDictionary`, `NSXPCConnection`, `NativeDiskImageGraphNode`, `PluginBackendXPC`, `PluginDiskImageGraphNode`, `QuarantineFileHandler`, `RamXPC`, `ReadSynchronizerBackendXPC`, `SerializedDiskImageGraph`, `SparseBundleBackendXPC`, `_TtC16FetchRestoreKeys16CryptoKitWrapper`

Protocols: `DIController2ClientProtocol`, `DIControllerProtocol`, `DIIOClientProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `PersistentBackend`

## Strings (4,034)

First 2,500 of 4,034.
```
Invalid or missing image URL key
Stack with cache as top image cannot be opened for writing.
locally mounted from %@
Failed to create DADisk during unmount
-[DIDiskArbEmulation ejectWithBSDName:error:]
Failed to read passphrase from stdin
%s (%@)
0X
01
-[DIBaseAgentDelegate createListener]
pstack_header
Backend barrier failed during allocator failures handling, error 
 size = 
set size failed
Output of disk image conversion must be a file
UDIF header changed while unlocked
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
Persistent attach is not supported for this disk image type
void info::DiskImageInfoASIF::examine_mapped_extents(const DiskImageASIF &)
The format specifier for 
com.apple.DiskImages2.TelemetryManager
), reading from backup
Failed to open backend of crypto header
identifier
Crypto: Unsupported encryption parameters
IOHDIXController
encodedDict
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
Error during ASIF flush: 
virtual int BufferedWriteBackend::write(const sg_entry &)
Unexpected failure to get image info: 
BufferedWriteBackend doesn't support per io crypto
AppleDiskImagesController
Failed writing first block of dir
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:437:
 auth entries
static int SparseBundleBackend::open_bundle(const string &, int)
system
instanceID
Key is not hexadecimal number.
not a disk image
Content
Image Format
solid state
X-Amz-Security-Token: %s
virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)
bands
Failed creating property list
pstack: unsupported node
v8@?0
Encryption Info
header_size_t
virtual void ParallelFolderCopier::copyFiles(progressFunc_t) const_block_invoke
+[DICreateParams eraseIfExistingWithURL:error:]
Can't read bitmap
 existing bands
/usr/lib/libAmber.dylib
Failed to add symmetric key entry to auth table
Content-Type
auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:
-[DiskImageCreatorFromFolder createImageWithSrcFolder:progress:createParams:convertParams:error:]
virtual PurgeableFileBackend::~PurgeableFileBackend()
Plugin 
Dissented with status 0x%X, pid %d
Missing key in SAKS response
Unsupported block size for image format
barrier
.Trash
com.apple.diskimage-test-plugin.raw
knox-dev.sd.apple.com
XPC connection interrupted
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)
, fd=
/sbin/mount
UUID
saks-ac-dev.g.apple.com
download
Failed to get registry entry ID, ret %d
lifs
-[DIBaseXPCHandler init]
Invalid value for UDIF header field: %s
Disk image is terminated, skipping ...
Authentication Data creation failed.
%s\n
diskimage_uio::details::diskimage_impl::diskimage_impl(diskimage_open_params &&)
Cleaning up!
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293
vsnprintf
Content-Length: %zd
url
YES
Stack already contains an image with the same stable UUID.
CKIE
could not create iterator (end)
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
+[DIError errorWithDomain:code:description:verboseInfo:error:]
decryption-components
com.apple.diskimages.sla-prompt
Diskimageuio: after reopening backend to read-write, it's no longer encrypted
UDIFDiskImage: failed flush after user data write
HTTP %u\n
 but buffer is full
Input underlying FS
GUI SLA handling required
Unaligned metadata entry size
, disk size: 
BackendPlugin
Failed to write metadata header
invalid field %u
managed future err 
metadata
supportsPersistentAttach
Invalid encryption method
virtual DiskImageSparseBundle::~DiskImageSparseBundle()
Compressed(
com.apple.diskimages.band_management
Images
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:152:22)]
Failed to create disk image
Geometry
Cannot change passphrase of unencrypted image
The width option should not have a leading zero
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ H
Diskimageuio: can't set passphrase, can't get encrypted status 
DIErrorVerboseInfo
uat
-[DIConvertParams onConvertCompletionWithInError:outError:]
UDIF uncompressed read-only image
ASIF: can't copy metadata to mutable copy
com.apple.DiskImages2.ASIF.sparsity
Failed to create crypto serializer
raw_header
expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_image_header(size_t)
Couldn't lock entry 
ftruncate failed, errno: 
AAS3DownloadStream (curl)\n
fstatfs failed
Diskimageuio: Unrecognized image format.
required_mode
Failed to erase band 
static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)
virtual DiskImageSparseBundle::ContextSparseBundle::~ContextSparseBundle()
table flush failed during close: 
IOServiceWaitQuiet error 0x%x
%12llu bytes downloaded (%.2f MB)\n
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
handleRefCount
Can only append ASIF formatted images to pstack.
Opening mapped blocks for 
shadow-path
debugLogsEnabled
Cannot attach RAM disk as a read-only device
Unsupported image stacking
X-Amz-Date: %s
Failed DA init
Full dir write failed with 
 failed with errno 
 bytes image
+[DICommonAttach diskImageAttach:readOnly:autoMount:BSDName:error:]
,Signature=
a floating-point
segment_count_none = 0, segment_count_one = 1
The disk image format is not supported by this OS
Could not parse OIDC token from AppleConnect output
Image doesn't support resizing
void di_hybrid_subscriber_t::suspend()
Diskimageuio: Can't create stackable image: 
Error reading sectors for verify 
Can't flush asif table, backend barrier failed
secondaryKey
Crypto operation on data of 
key_derivation_prng_algorithm_t
Source folder real path is invalid
 cannot be re-registered
fskit
Plugin bug: returned init failure without supplying the error
Failed to create graph from plist.
com.apple.internal.fetchrestorekeys
DiskImageURL
Failed to retrieve info
 is not registered
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
Failed to allocate raw blob data
Request failed: %03ld (error not set)
InstanceID
sign
-[DIBaseParams openExistingImageWithFlags:error:]
metadata_flags_t
-[BaseDiskImageCreator createEmptyImageWithError:]
Unsupported compressed run (
BackendSG: truncating the inner backend failed, error = 
9999
high throughput
Couldn't write asif's header
ERROR: enc-request failed base64 decode
crypto_op: can't initializae aes_xts context
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_handle_exceptions()
Diskimageuio: Only single cache is allowed
path
Error reported from fts_read
iv_tweak_size_t
SmallVector unable to grow. Requested capacity (
Block device block size is larger than image block size
bundle_handle
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
virtual size_t BZIPCompressedBackend::compress(const sg_entry &) const
IOBlockStorageDriver
AES-XTS
expected<uint64_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_nr_blocks() const
Diskimages2 - ASIF - bad reserved bits 
-[MKDIDevice updatePartitionMapWithError:]
has_bitmap
Couldn't upgrade lock entry 
Invalid UDIF, run is not within block boundary
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__hash_table:1892: lib
fsync
Corrupted plist dictionary
Accept
UDSB
private/tmp
Failed to find the data partition
No room to add new auth entry
file(
AAS3ContextSetFieldString
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
Invalid block size for image
Cannot create target image format with the block size of the source image
an integer
no more attempts allowed
creating session
clientID
void info::DiskImageInfoASIF::count_used_extents(const DiskImageASIF &)
static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Can't read custom encryption entry header, error 
;
fileBackend
Can't connect to device
Max Size Bytes
ShadowChain: %@
-[FastFolderCopierWrapper traverseSrcFolderWithProgress:error:]_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
sparsebundle
int di_asif::details::dir::handle_all_failures(ContextASIF &)
Legacy shadow file format is not supported by DiskImages2 framework
could not create iterator (begin)
%12.2f initial interval between retries (s)\n
ASIF: Entry dirty bit is set when reading from disk
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
Unexpected backend type for shadow file
KEY_BITS_128 = 128, KEY_BITS_256 = 256
Invalid raw UDIF run size limit
disk arbitration framework returned an error
DiskImage::diskimage_extent_t DiskImage::const_extents_iterator_t::make_val() const
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:425:
GUID
The precision option does not contain a value or an argument index
prng_key_bits_size_t
void udif::details::UDIF_base::validate_runs()
BZIP decompression failed, res=
set context
%12u max requests in flight\n
segment_count_t
Couldn't read asif's header
Zero padding disabled successfully on fd 
Updating 
1.0
 backend size 
-[DIAPFSPartition newMountVolumeWithDiskArb:error:]
01234567
UDIF: Can't get resource array
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = std::__bind<io_result_t (DiskImage::*)(DiskImage::Context &, const sg_entry &), DiskImage *, std::reference_wrapper<DiskImag
virtual lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImageRaw::future_write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
The value of the argument index exceeds its maximum value
Failed opening mapped blocks file for 
Write zeros to unmap region failed (err code
Crypto data block size: 
com.apple.diskimages_cache_update
Failed creating the image
Single element in pstack that isn't an image
Uninitialized Entries
Barrier failed after defrag table move, error 
virtual void ParallelFolderCopier::copyFiles(progressFunc_t) const
void rawTestPlugin_t::subscriber_t::_suspend()
Agree Y/N? 
UDRO
Is Encrypted
-[MKDIDevice resizeDataPartitionWithPartitionUUID:partitionNumBlocks:error:]
precision
IV_TWEAK_SIZE_16 = 16
image
disk image
, disk image is terminated
bytes=%llu-%llu
Invalid path property (not UTF8)
CoreFoundation type mismatch: 
-[DIConvertParams shouldPerformInplaceSquash]
bytes, which is after end of ramdisk
GET
Cannot load libAmber
Device is not a disk image
stat failed
Diskimageuio: Can't get image format
The numeric value of the format specifier is too large
band-size
%@[ramsize=%llu]
-[FastFolderCopierWrapper copyWithDstFolder:progress:error:]_block_invoke
Couldn't open 
Failed to write metadata
Retrying request after %.0f seconds %zu bytes at offset %llu
\\\\
/dev/%@
-[DIEncryptionChpass unlockWithPassphrase:error:]
can't get Diskimage attribute, unknown header format
Diskimageuio: backend doesn't exist
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
) to type
Validation failed for dictionary key %@.
public_key_crypto_algo_mode
blocks_signature
Cannot stat 
%s: 
cert-chain
Passphrase cannot be empty
%@%@.%@
sparseHeader
Default
-[DiskImageParamsXPC createDiskImageWithCache:shadowValidation:]
readPassphraseFlags
sendEvent of type 
virtual int Ram::_read(const sg_entry &)
s3Perform
XPC connection invalidated
int sparse_bundles::mapped_blocks_t::flush()
sparseimage
FilePath
Failed initializing RAM disk buffers
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
ASIF: table is not aligned to chunk size
fetch_restore_keys self signed cert
public key has an encoding issue or uses an unsupported algorithm
leaf-cert
Sparsebundles on SMB mounts are not supported on this system
tmp_convert
read write
Diskimageuio: resolved disk image format 
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
ShadowURL
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
Cannot attach RAM disk with a shadow or a cache file
' with flags 
-[AAS3DownloadSession readToAsyncByteStream:size:atOffset:]
Failed to create public key auth entry
zlib
/dev/rdisk
s3StreamBaseInit
Unexpected crypto header length (
Closing bands
true
The image is encrypted with obsolete encoding version 1
The disk image is corrupted
invalid bits range 
/System/Library/PrivateFrameworks/DiskImages2.framework
POST
DES3_3KEY = 17, AES_KEY = 0x80000001
bitmap flag value invalid
entire_device
v32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
uid temporarily set to 
slaText
-[DIStatFS initWithFileDescriptor:error:]
xpc error
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_path(const std::filesystem::path &, bool)
Invalid field found in shadow file header: 
BackendZero
std::unique_ptr<DiskImage> diskimage_uio::details::diskimage_open_params_impl::transfer_disk_image_ownership()
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
Unmapping band 
Failed to initialize folder copier
IOMedia device not found in registry iteration
com.apple.diskimage-plugin.nbd
invalid value
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Harde
Failed to increase file size, pwrite returned 
Stack Info
Failed to unlock the encrypted image
Children
ULFO
 exceeds the maximum of 
 for 
fetch_restore_keys_ephemeral
ERROR: wrapped-key failed base64 decode
com.apple.diskimagescontroller
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<diskimage_uio::diskimage_open_params_pair *>]
Extent 
uninit
pthread_key_create
Size
Checksum Type
Range
auto hdr_get_nr_blocks(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
' opened successfully with flags 
unique_ptr<lock_free::bitmap_t> SparseBundleBackend::get_existing_bands() const
token
-[RamXPC createRamBackend]
plugin://%@
expected<image_format, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::query_image_format() const
ASIF: data entry - invalid reserved bits
SHA1_HMAC = 91, NONE = 0
Failed creating CFData
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c
void plugin_encode_fd(void *, const char *, int)
mapped
Cannot find the data partition
CFAutoRelease<CFDictionaryRef> udif::details::UDIF_base::get_resources() const
Only file URLs are supported by DIOpenParams
Passphrases doesn't match
 requested while there are only 
bool sparse_bundles::open_bands_t::insert(uint64_t)
flags validator
Destroying File backend, but in-flight promises exist
a bool
algorithm_type
void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/crypto/crypto_format.cp
virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)
Failed to get parent registry entry, err code %d
Cannot increase size of a block device
Disk image URL is too long
Compression Ratio
Attach with legacy DiskImages framework is not supported on embedded platforms
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
 instead
-[DIAPFSPartition formatWithVolumeName:error:]
fd block size retrieval failed (err code 
Stackable image
Cannot find BSD name in IO media service
Non supported options in AAS3DownloadSession (ignored): proxy_headers %s
,
Invalid key size
trim largest: size change callback failed with 
00000000-0000-0000-0000-000000000000
Punch hole is not supported (err code 
Diskimageuio: Invalid pstack element: 
getErrorContextKey
Backend: failed writing element in vector
Mount Point
none
Unmap error: 
BackendSG: error allocating buffer
Start Offset
.fseventsd
.vol
 was just created (truncated)
 read: 
Starting flush
total_segments_t
7C3457EF-0000-11AA-AA11-00306543ECAC
virtual int FileLocalAsync::truncate(uint64_t)
Diskimageuio: Required read-write disk image (
MediaKit write error
Failed to evict band to make room for 
bool di_asif::details::table_entry_data::validate() const
flushing and closing 
bool ref::details::ctrl_blk<CurrentReader, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = CurrentReader, tag_t = unsigned long long]
Cannot initialize pstack disk image without path.
ASIF meta header is unaligned
a pointer
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
Failed to store the passphrase in the keychain
Disk image is terminated, skipping flush
table entry map@
Run interval: 
static std::string FileDescriptorWrapper::handle_open_from_error_message(int, const std::string &, int, int)
, errno=
NSURLSession read to stream nbyte=%zx offset=%llx\n
Passphrase is too long
type: 
static int FileDescriptorWrapper::open_from(int, const std::string &, int)
strdup
Basic information about the IOMedia device is missing
The requested operation will delete all children of the provided node. use recursive removal to surpress this error.
 to 
Unexpected ASIF header length (
ASIF: metadata header out of range
int di_asif::header::write_header(Backend &)
uint64_t udif::details::UDIF_base::write_resources(CFDictionaryRef)
com.apple.wkms.auth-data
Invalid path property (not a path or URL)
-[DIBaseXPCHandler createConnection]
Sparse bundle ejected
io_result_t di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
End of input while parsing format specifier precision
sig2_t
special: 
BackendSG
Unknown
virtual int DiskImageSparseBundle::flush(DiskImage::Context &, di_flush_mode)
 in dir I/O, error 
com.apple.wkms.fcs-key-url
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)_block_invoke
get path failed
IOBlockStorageDriver device not found in registry iteration
com.apple.diskimage.sparsebundle
Unsupported host for OIDC: %@
Asif header too large
The format specifier should consume the input or end with a '}'
AWS4-HMAC-SHA256\n
Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib 
maxRawUDIFRunSize
 is different than current mode 
lzfse
encryption_key
'
Images Count
BSDname
Cannot decode path
 lock, errno 
) is larger than maximum value for size type (
Content-Type:
disk image password
Not valid SAKS environment
dealloc_queue
-[DIBaseXPCHandler installConnectionLostHandlers]_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
Compressed Bytes
Image contains crypto format but info class is missing EncryptionInfo
Flushed 
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:113:22)]
Cannot edit crypto header that has more than 
.Trashes
, dirty=
key
NO
outputFormat
raw
Diskimageuio: Couldn't lock backend 
Invalid sections returned by MediaKit
nil URL specified
Diskimageuio: No diskimage given
ASIF: can't set requested uuid
Failed to eject
virtual FileLocalAsync::~FileLocalAsync()
random generation failed with err code 
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
] 
Failed during ASIF extents enumeration.
Unmapped Entries
int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)
Closing an unchanged 
, errno 
 marked as purgeable
<
system error
Bit 
UDIF - max compressed run size: 
s3DownloadStreamOpen_urlsession
IOHDIXHDDriveNub
CBCPADIV8 = 6
Invalid resource key
virtual int SparseBundleBackend::unlock_all()
 was opened in the background, waiting for it to become available
virtual FileDescriptorWrapper::~FileDescriptorWrapper()
Bad pstack format, node with active UUID not found.
Unexpected passphrase header length (
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const
Found a valid file for 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
):
ASIF: failed to write metadata
Error: Not enough data read. expected: 
encryptionMethod
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486:
version_1 = 1, version_2 = 2, version_3 = 3
Context setup failed.
 is now available
Backend is not mounted on APFS
 folder
 but buffer is too small 
ASIF: invalid dir index to header
Does not contain an \"even number\" of hex digits.
-[AAS3DownloadSession syncRequests]
not a valid DER-encoded X.509 certificate
Error creating backendXPC
 bytes are above the sparsebundle limit of 
int di_asif::details::table::close()
Plugin struct size 
Mandatory callbacks in the plugin's struct are missing
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
-[DIBaseXPCHandler completeCommandWithError:]
plugin_name
Can't write initial table data
Failed to access folder: %@
TCC permission denied for path %s
Failed to create dispatch source for kqueue
com.apple.DiskImages2.ErrorDomain
, but file size only 
UUID validation failed for appended image.
The requested operation will delete the active node, please set another one first.
SLA prompt cancelled
Can't load bitmap while setting range
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)
 not found in registry
disk image kernel return
fetch_restore_keys_key_handling.m
/dev
UDIF: Can't find data key in dictionary
createErrorContextKey
STCK
a character
virtual io_result_t sparse_bundles::Band::write(DiskImage::Context &, const sg_entry &)
%@ failed with error code %d
Full Entries
bool DiskImageSparseBundle::try_unmap_band_extents_without_list(uint64_t, const extents_set_t &)
source uuid
stable uuid
.hotfiles.btree
Failed to allocate refcon
basename_r failed
void boost::uuids::string_generator::throw_invalid() const
+[DICommonAttach DI2_attachWithParams:BSDName:error:]
-[AAS3DownloadSession addRequest:]
user data embedding failed
Cannot store an empty passphrase
shouldValidate
AES_KEY = 0x80000001
DiskImageSparseBundle::ContextSparseBundle::ContextSparseBundle(DiskImageSparseBundle &)
File (fd 
di_plugin_image_t *verify_plugin_image(di_plugin_image_t *, CFErrorRef)
/dev/disk
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
asif
FSPersonalities
 failed wih error 
+[DiskImageParamsXPC validateSupportedFormatWithBackendXPC:error:]
Nothing to defrag
Failed to start folder traversal
Resetting 
> %d %s\n
invalid length
+[DiskImageGraph(InfoPrivate) getImageUUIDWithURL:allowMissingUUID:error:]
read_only_cache = bit(0)
 option
Bakcend not initialized for file
Band data is partial, reading 
full_fsync
private/var/db/dyld
Failed to copy %s
Crypto: can't read crypto header
Error with decryption key size
regEntryID
(unrecognized error)
alternate form
, required decompression buffer size: 
BZIP compression failed, res=
oidc
Failed to find IO media entry for %@
shadow
Disk image is terminated, skipping unmap
Failed to encrypt data using public key from certificate
+[DIAttachedDeviceInfo copyAllMountPoints]
Failed converting URL to UTF8
Failed to read metadata 
int copyfileWithClassFHandling(const char *, const char *, copyfile_state_t, copyfile_flags_t)
PKCS1 = 10, OEAP_SHA1 = 0x80000001
: [
Using automatic argument numbering in manual argument numbering mode
wkms-dev.sd.apple.com
shadowChain
-[DIBaseServiceDelegate listener:shouldAcceptNewConnection:]
int details::udif_verify::calculate_checksums(workqueue::workqueue &)_block_invoke
Close completed
Unable to create ioreg iterator
bzip2
User data contains reserved key(s)
, UID:GID(Name)=
-[DIUserDataParams retrieveWithError:]
Cancel
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
Can't flush asif on table flush, backend barrier failed
Failed barrier at start of dir flush, error
User-Agent
Failed to create DADisk during eject
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
No
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)
1
https://%@
-[DIAttachParams reOpenIfWritableWithError:]
 err: 
Diskimageuio: get stackable uuid failed 
Source folder must be a path
Disk image is terminated, skipping flush of 
Plugin image struct size 
failed to open existing output file
-[DICreateParams onErrorCleanup]
-[DIDiskMountTracker onDiskAppearedWithDiskName:isMountable:]
0x
auto sparse_bundles::Band::get_mapped_blocks()::(anonymous class)::operator()() const
w
Failed to deserialize crypto format
dirty = bit(0)
Diskimageuio: get parent uuid failed 
URL
Shadow path %@ is not a valid file
Min Size Bytes
Copy aborted by user
Band was evicted by another thread (during retain attempt), retry erase process
virtual int SparseBundleBackend::truncate(uint64_t)
device with dev name 
No WKMS key source available in AEA metadata
Could not stat shadow file
Type
PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0
Master checksum
SmallVector capacity unable to grow. Already at maximum size 
wrapped-key
plist
Custom encryption entry header size exceeds max size
Diskimageuio: Raw header changed while unlocked
Image cache flag does not match the requested operation.
Band was evicted by another thread, retry erase process
auth-data
Invalid plugin URL, plugin name is missing
com.apple.diskimages.aio
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
Cannot decode writable
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
Unsupported key decryption algo
int crypto::crypt_op::crypt_consecutive_vector::operator()()
encryption_key_bits_size_t
Can't flush asif on map element close, backend barrier failed
crypto header contains invalid number of auth entries
Failed creating bands folder
diskimage-bundle-type
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
PstackVersion
void di_asif::details::table::set_entry_bitmap_range(ContextASIF &, data_entry_t &, const bits_range_t &, data_entry_t::flags, std::optional<data_entry_t::flags>)
Max sector count is too large
Couldn't upgrade lock entry
UDIF: Can't create dictionary resource fork
Unable to get IOMedia preferred block size
Failed to get plugin instance
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(diskimage_open_params &&)
Failed opening the file
fully
Overflow detected
Failed to create XPC connection object
!
 failed, error 
couldn't allocate space for entry 
Failed unlocking file with fd 
Unexpected context construction by 
crypt_consecutive_vector: check errors_in read futures 
Starting unmap of 
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
numBlocks
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp
Can't write UDIF resource part
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ H
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/Temp
Resumed
write
V2 = 2
iokit error
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
-[DIVerifyParams verifyWithError:]
Evicting all bands for eject
sig1_t
dataTaskWithRequest
-[DIDiskArb ejectWithBSDName:error:]
Missing parent node in graph.
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406:
 - 
\\'
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
UDIF: Failed converting type array string (
fstatfs failed with err code 
IOService
malloc
ParentUUID
Failed to create disk image with shadow/cache
ulfo
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = di_asif::header]
Root dir flush failed, error 
s3StringBufferAppend
dev
Invalid size of saks response %lu
Plugin's ring suspended, ret code 
Failed to update internal state after resize
 does not allow the 
sg: buffer = 
IOMedia
Failed to check encryption status
Error creating (unlocked) backend
Disk image is terminated, skipping future_unmap
Failed serializing user dictionary
attempting to authenticate with wkms
config_t
Device Characteristics
Diskimageuio: UDIF header changed while unlocked
virtual DiskImageSparseBundle::~DiskImageSparseBundle()_block_invoke
Range:
Failed locking the shadow file
-[DIBaseServiceDelegate init]
void rawTestPlugin_t::subscriber_t::_cancel()
Couldn't trim entry in write 
Validation failed, input contains unexpected data.
-[NativeDiskImageGraphNode(Append) validateAppendedImageWithInfo:error:]
hw.logicalcpu
virtual int FileLocalAsync::unlock_all()
Cannot find image with provided uuid.
s3Sign
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_unmap(const unmap_extent_t *, size_t, future_io_opts_t)
static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
BLX
v16@?0@\"NSString\"8
-[SparseBundleBackendXPC getCryptoHeaderBackend]
UDBZ
unknown
Feature or image not supported by library
unsigned char boost::algorithm::detail::hex_char_to_int(T) [T = char]
crypto_format: cookie differs
void sparse_bundles::Band::ContextsList::clear()
\n
UDIF XML length 
di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke
Info.plist
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
 is 
v32@?0@\"NSURL\"8Q16^B24
, retrying
IO error with sg: 
Cannot get partition size
Cannot find the APFS volume
Non supported options in AAS3DownloadSession (ignored): pinned_public_key %s
Cannot find registry entry ID 0x%llx
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
Disk image is terminated, skipping write
Pstack corrupted, found a cache node without a non-cache ancestor.
 is not supported
UDIFDiskImage: failed truncating image
^v8@?0
Volumes
/System/Library/Filesystems/apfs.fs
Failed resizing the APFS container
Replaced an empty slot
 while expecting 
Key Size
BufferedWriteBackend
(err 
Bundle's lock file is closed
Error: failed to unwrap key. Error: %s\n
+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke
uri
PKCS7 = 7
-
 on 
Missing OIDC client ID in appinfo response
Failed to create chiper data for public key auth
field size too large
Table flush failed during dir flush: 
com.apple.DiskImages2
devicePrivateKey
Failed to open crypto header
Cannot display SLA: no terminal or stderr to write to
+[DISLAFrontend(Private) displaySLAText:error:]
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
Background close of band at index 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615
Failed truncating 
BackendNull
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_write_iov_t]
Max Sector Count
.FBCIndex
CFName
Completed erase of band 
Sandbox checked for 
 closed
Cannot stack images with different block sizes
Cannot load libTestPlugin
Shadow block size is invalid (0)
Couldn't open file with flags 
Failed to update asif header
] = 
 bytes
Diskimageuio: image is locked
(locked)
ASIF: failed to deserialize metadata
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
void sparse_bundles::mapped_blocks_t::map_range(uint64_t, uint64_t)
%@: %s
Data
diskimageuio: report err 
File descriptor 
Re-enter new password: 
virtual int CompressedBackend::write(const sg_entry &)
apfs
mountedOnURL
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
Got error when trying to close 
ASIF meta header failed to read
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
DiskImageConvert
writable
ASIF meta header data is unaligned
) is locked
 io: 
segment_num_none = 0, segment_num_one = 1
Clone of plugin nodes is not supported.
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::initializer_list<rref_capture<diskimage_open_params_pair>>, uint32_t)
Can't load table to get extents
Not a pstack.
The image is encrypted but has no passphrase auth entry
backend
 doesn't exist
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr(image_format, std::shared_ptr<Backend> &, bool, const std::filesystem::path &, size_t)
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
bla
auto DiskImageSparseBundle::void_stackable_identifier()::(anonymous class)::operator()() const
Failed to convert SLA text to C string
Suspended
 directly (without list)
Can't load bitmap from backend
s3Perform failed (after retry), %s
IOStorageFeatures
basic_string
Error creating disk image params
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:172:22)]
void rawTestPlugin_t::subscriber_t::_resume()
Can't load asif dir version
Bearer %@
not 
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hard
ASIF: missing internal metadata key
ddm
 is incompatible with the framework, expected at least 
Failed to read passphrase
 failed with 
Bands folder contains an out of range band (
Placed new 
Writable
Image
v32@?0@\"NSMutableDictionary\"8Q16^B24
application/octet-stream
--oauth-grant-type
Compression Info
Locked encrypted image
virtual int FileLocalAsync::disable_file_zero_padding() const
 updated from 
://
Image info is not supported for the given image type
 doesn't exist, returning zeros
void udif::details::UDIF_base::print_checksum_verification_status(const std::string &, const csum_any &, const details::checksum &) const
bool sparse_bundles::mapped_blocks_t::load_file()
CacheURL
v24@?0@\"DIDeviceHandle\"8@\"NSError\"16
v24@?0@\"NSDictionary\"8@\"NSError\"16
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
Unsupported ASIF version 
+[AAS3DownloadSession completeRequest:data:response:error:]
Verify
Failed to add public key entry to auth table
Error with resolving knox url
-[DIConvertParams copyUpdatedOutputURLWithError:]
table entry data@
uuid
partition_num: 
file of 
Failed to resize the image
crypt_consecutive_vector: write check errors 
.DS_Store
An argument index may not have a negative value
UDIF: Can't read UDIF trailer
kern.aioprocmax
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)_block_invoke
unmap_iterator_t di_asif::details::table::unmap(ContextASIF &, const unmap_extent_t *, size_t)
prng_algorithm_type
CFUserNotificationReceiveResponse failed
Failed to serialize public key entry to crypto header
Unsupported disk image format
Apple sparse image
 data: 
io_result_inserter_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::data_entries_vectorizer_t::add_data_entry(const data_entry_t &)
 constant 
public_key_padding_algo
File too small.
: flush failed (
set_euid_wrapper::~set_euid_wrapper()
Metadata
Failed opening the image with RW access
Diskimageuio: can't get Diskimage attribute, unknown header format
Backend barrier failed during bitmap allocator failures handling, error 
owners
>
daw
certificate
Can't write table for defrag
 elements returned 
Fit Map to Container
Error writing file @ 
-[AAS3DownloadRequest createAndResumeTask]
Unexpected backend replace request
This operation doesn't support pstack files
The requested URL is an existing regular file
PluginParams
IOBlockStorageDevice
Empty Bytes
Mismatch between the device's and partition's block size
 band contexts
virtual int CompressedBackend::read(const sg_entry &)
s3HeaderAppend
Allocated after defrag: 
Read-only image cannot be resized
Invalid schemes returned by MediaKit
CBC_IV8 = 5, XTS = 0x80000001
gcd_kqueue: kevent64 failed with ENOMEM
intermediate-certs
Password
https://%@/spaces/%@/files/%@/decryption-components
file_handle
Looking for existing bands
aaS3ContextClone
)
Read error: 
Segmented UDIF images are not supported by this framework
fd
Diskimageuio: can't get file descriptor, backend doesn't exist
allocated: size change callback failed with 
\\n
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
-[DIDiskArbEmulation unmountWithMountPoint:error:]
Compressed Length
int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
diskimageuio: pre-write first error 
 - same 
[empty]
com.apple.MobileAsset.AssetType
Failed to eject - cannot open device
application/json
Backend: failed reading element in vector
Missing payload URI in Knox response
udsb
 given
Failed creating sparsebundle folder
Too many mount arguments
Library/Caches/TemporaryItems
char *udif::header::write(char *)
 or exceeds size_t size 
 is closed, notifying waiters
plugin
Include most
Missing key in KKMS response
In-place conversion maintains the encryption passphrase and method. It's not allowed to specify encryption arguments
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_flush(di_flush_mode, future_io_opts_t)
Sector Count
virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()
DaemonPID
-[DICreateParams createDiskImageParamsWithError:]
async_fd
Barrier failed after defrag, error 
UDIF XML at 
AmberDiskImagePluginCreate
-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]
getToken
emulateExternalDisk
-[DICreateParams resizeWithDiskImage:blockCount:error:]
Chunk Size
Couldn't read sparseimage header
Can't write UDIF header
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682
{:02x}{:02x}
The argument index starts with an invalid character
int sparse_bundles::Band::flush()
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)_block_invoke
crypto_op: can't initializae aes_cbc context
Metadata offset is invalid
Can't convert data to property list
 - map_range: [
Decompression failed
Error reading file @ 
enqueueRequest
-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]
ASIF Info
The argument index value is too large for the number of arguments supplied
Decoding error.
lock
Not A Ninja/1.0
Failed to set up image for info retreival
Unexpected materialized_diskimage in create_diskimage_from_hdr
-[DIDiskArb waitForDAMountWithExpectedCount:diskTracker:]
%@[%@]
Read returned an error
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
run_type
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
oma-context
Cache
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)
ASIF: Header size is less than the min header size
Failure during source folder traversal in %s
UDIF: Can't get types array from UDIF
static int FileDescriptorWrapper::open_file(const std::string &, int)
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)
io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)
Sector count is too large
\\u{
Integral value outside the range of the char type
Can't parse encryption entry: 
virtual int Backend::read(const elements_t &)
Unexpected response type: %@
Write error: 
Metadata corrupted 
Using manual argument numbering in automatic argument numbering mode
The type option contains an invalid value for 
Background erase of 
Using compression 
virtual int FileLocalAsync::_read(const sg_entry &)
uid restored to 0 (res=
AAS3ContextCreate
Size cannot exceed max ASIF size
ASIF header changed while unlocked
Disk image is terminated, skipping future_read
End of input while parsing an argument index
0123456789abcdef
More than one image in the stack has the provided tag, please specify UUID instead.
CFUserNotificationCreate failed, error code %d
(
Cache is not supported when using pstack.
-[DIClient2IODaemonXPCHandler createConnection]
Diskimageuio: path 
File system is 
 dest 
\\x{
mark purgeable failed on 
gcd::gcd_timer_source::gcd_timer_source(gcd_queue &, dispatch_time_t, uint64_t, uint64_t)
-[BackendXPC tryCreatingCryptoHeader]
-[DIConvertParams prepareConvertWithError:]
-[DIImageHandle resizeToSize:error:]
virtual int DiskImageSparseBundle::set_size_impl(uint64_t)
/sbin/%@
Internal backend read() failed. ret=
Unregistering plugin 
Could not generate OIDC token - AppleConnect Failure
Diskimageuio: is cache image failed 
corrupted image
zero-padding
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
Request failed with HTTP error: %lu %@: %@\n%@
URL must have a file scheme
auto
Starting ASIF defrag, used size: 
crypto_format: blob length differs
UDIF header doesn't contain a valid sector count, using runs upper value: 
void sparse_bundles::open_bands_t::remove(uint64_t)
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_read(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
0b
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
Skipping erase of 
plugin://%@/
Encountered an irrecoverable I/O error, all future I/Os will be invalidated
static autostart_task_t<process_entry_result_t> di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::process_write_entry::operator()(table &, ContextASIF &, table::data_entry_t &&, const sg_vec:
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/disk_im
void BaseFolderCopier::traverseSrcFolder()
Failed opening folder for entries reading
RAW
Unexpected image format from info: 
.Spotlight-V100
-[MKDIDevice initWithBSDName:numBlocks:blockSize:error:]
Skipping band erase (in use)
virtual int BackendSG::truncate(uint64_t)
-[DIUserDataParams embedWithError:]
nodes
band_ptr DiskImageSparseBundle::replace_oldest_band(Band *)
Partitions
The requested URL is an existing folder
None
Provided image has no UUID info.
Solid State
 returned status 
The type does not fit in the mask
Size is not a multiple of block size
overrideBlockSize
ULMO
static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Failed barrier after writing full dir
, 
Authorization: %s
Diskimageuio: can't set passphrase, image not encrypted after reopen
file-read-data
KVS keyBuffer allocation failure.
-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]
UDZO
asif: chunk size is too small, too many dir indices
The format string terminates at a '{'
saksKey
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)
Failed to create kqueue
Failed to add passphrase entry to auth table
Band size in sparse is zero
Terminating due to unrecoverable I/O error
Reserved part isn't zeroed
Failed to create diskimage_open_params
Awaitable completed in unexpected state
Plugin's async ring cancelled, ret code 
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::set_path(const std::filesystem::path &, const diskimage_open_params::mode)
eject timeout
Plugin initialization failed
len: 
]
Diskimageuio: Can't stack non asif formats. Got 
Closed band at index 
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_t
System keychain access is not allowed on this platform
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
ReadOnlyBackend
cache
ASIF meta header trailer isn't equal to zero
com.apple.di_stackable.cache.flusher
Failed to parse key in KVS (zero size data).
%@: %@
inputMountedFrom
!\"
udro
RSA = 42
Failed to copy metadata of %s
Destination folder URL must be of 'file' scheme.
The symmteric key is wrong
commandSize
UDIF: compressed runs should be <= 1MB
Cannot lock bundle, ignoring: 
Failed to use the passphrase that was given
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
Couldn't trim entry in read 
 [
onDiskCache
AEAHelper: Invalid file descriptor.
unmanaged
-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]
rdisk
Cannot find image with provided tag.
attempting to authenticate with saks
-[FileLocalXPC replaceWithBackendXPC:]
Barrier
 rather than image
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
Failed converting CFNumber to longlong
UDIF image of 
vector
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
infnanINFNAN
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
Reading 
/s3/aws4_request,SignedHeaders=
com.apple.diskimages2.fast_copy
+[DiskImageGraph(InfoPrivate) getImageUUIDStrWithIdentityInfo:stackableUUIDFallback:error:]
suppressSsdFlags
Diskimageuio: unsupported disk image type for get_backend
Sparse bundle image
UDIF_header
 while expected is 
curl_easy_setopt failed\n
-[DIStatFS logWithHeader:]
Image key encoding failed with err code 
table_entry_data::flags di_asif::details::table::get_next_extent(ContextASIF &, const interval_sectors &, interval_sectors &)
Backend barrier failed after dir offset changed, error 
Can't get key in cstring format
BSD Name
-C
Transfer-Encoding:
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = udif::header]
virtual void SerialFolderCopier::copyFiles(progressFunc_t) const
segment_num_t
Malformed URL format
Apple Inc
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
virtual int Backend::write(const elements_t &)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
\\t
The type option contains an invalid value for a string formatting argument
-[DiskImageGraph initWithBaseImageURL:tag:error:]
High Throughput Options
Invalid value for argument 'block-size'
crypto_hdr
checksum_type
s3Perform retry after %u ms
/dev/tty
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_stackable_uuid() const
0
KVS data fetch failure.
-[DIResizeParams resizeWithError:]
virtual void DiskImageSparseBundle::on_eject()
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603
Cannot save DiskImageGraph without specifying pstack URL
sha1 too many bytes
File not owned by current user (%d): %s
Failed truncating plist
header (
Write header failed after dir offset changed, error 
void SparseBundleBackend::read_info()
Request timed out
Mandatory callbacks in the plugin's image struct are missing
-[DIEncryptionFrontend unlockWithPassphrase:error:]
Can't serialize property list
%@[%@, %@]
NONE = 0
v16@?0@\"NSError\"8
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<diskimage_uio::diskimage_open_params_pair *>]
Cancelled
Cannot get temporary directory
Key is not 32 bytes size.
Invalid knox URL format. Expected: knox://host/download/space/digest
is_aea: Error reading magic.
void di_hybrid_subscriber_t::resume()
rings_queue
Append of existing image with custom size is not supported.
Trying to write @ 
 bytes)
Corrupted shadow file(s) chain
attempting to authenticate with kms
Stable UUID
We're out of ctxs for async execute
flock returned errno 
Invalid chunk size
Cannot delete base image node.
user data retrieving failed
Not valid SAKS metadata (json format expected)
expected<int, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_file_descriptor() const
ERROR: Failed to serialize request: %@ error: %@
Custom cache or shadow is not supported for pstack based images.
 (error code 
 crypto = 
v32@?0@\"DiskImageGraphNode\"8Q16^B24
Flush failed after defrag, ignoring. Error 
.xpc
Udif: needs to read 
Failed opening the shadow/cache file(s) with RW access
Final asif 
Can't convert ASIF flag.
The format specifier contains malformed Unicode characters
Attributes
dispatch_source_create failed
OK
Failed creating MediaKit device refcon
X-Amz-Content-Sha256: %s
frk_set_device_identity_certificates
-r
Corrupted ASIF image.
-[DIDiskArb unmountWithMountPoint:error:]
hybrid_queue
Failed to setup the plugin's IO ring
Looking for an evictable slot for 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Missed an evictable slot
Invalid pstack, Active stack contains a loop.
Failed to read file for pstack parsing
Shadow underlying FS
Udif: advanced buffer, needs to read 
 backend: 
Invalid output format argument
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
createTask
-[FastFolderCopierWrapper initWithSrcFolder:parallelMode:auditToken:]
Crypto couldn't read from inner backend @ 
DELETE
ASIF
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = di_hybrid_subscriber_t]
user metadata
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Failed to read pstack.
Unsupported value for crypto header field 
&
inputStatFS
thread constructor failed
Internal backend write() failed. ret=
wkms.sd.apple.com
Error creating crypto format
Data Fork
static void process_terminator::terminate()
which is larger than allowed 
udif::details::UDIF_base::UDIF_base(UDIF_header &&)
uint32_t FileDescriptor::fetch_physical_block_size() const
device size not found in registry
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc+
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
uniqueDevice
Failed to read 
com.apple.diskimage-test-plugin.julio
diskImageParams
 with ret 
-[DIDiskArb onDiskDisappearedWithDisk:]
udzo_max
ASIF block size isn't multiple of 512
 ret: 
s3DownloadStreamOpen_curl
-[DIBaseAgentXPCHandler createConnection]
-[DIAttachParams newAttachWithError:]
 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633
Can't lock entry
: flush in destructor failed (
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
Failed to get data from self signed certificate
Plugin version 
 overrun events occurred in the plugin's ring!
Invalid argument, please use one of the DICreateParams derived classes instead
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::verify_backend() const
auto trim_data(const sg_vec::iterator &, const sg_vec::iterator &, size_t, const io_result_t &)::(anonymous class)::operator()(const auto &, const auto &, size_t) const [src:auto = sg_vec_ns::details::sg_vec_iterator, dst:auto = sg_vec_ns::
 bytes does not fit before the 
SparseBundleBackend::SparseBundleBackend(int, bool, const shared_ptr<FileLocal> &, const shared_ptr<crypto::format> &)
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
Diskimageuio: Couldn't get locked status 
Not enough space for metadata
 has size 
descriptor_special
-[DIDiskArbEmulation waitForDAMountWithExpectedCount:diskTracker:]
publicKey
Diskimageuio: reopen backend to required mode 
Diskimageuio: Couldn't get diskimage: 
Couldn't read asif's full header
virtual int DiskImage::set_size(uint64_t)
Can't read encryption table, error 
managed
Block size mismatch between crypto header and ASIF header
secondary_key
ASIF: No data offset found (write)
static void sparse_bundles::Band::erase(const bundle_commons_t &, uint64_t)
 is incompatible with the framework, expected 
Cannot find %@ entry
/dev/%s
Failed to erase mapped file of band 
Zero padding cannot be disabled from this process (res=
Cannot find AmberDiskImagePluginCreate in libAmber
ulmo
The replacement field misses a terminating '}'
kern_return_t was 
Failed to create DADisk during mount
Failed to serialize passphrase to crypto header
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
Invalid public key: %s
Failed to set up image for resize after creation
Flushing 
encryption: header size mismatch
fchmodat failed for 
Opened bundle's lock file with flags 0x
CyrptoKit is missing a required method.
Found 
header read-only flags
-n
Raw header changed while unlocked
Failed to write asif header, error 
outputParams
Failed to find DiskImages2 controller, driver might not be installed
ASIF: Can't defrag entries 
header_flags
 formatting argument
sparseimage format is not supported by DiskImages2 framework
Runs
 at index 
ERROR: shipping key wrapped-key failed base64 decode
Failed to set up image for resize
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
Can't load bitmap while flushing asif table 
Can't flush asif table, backend write failed
none {
Physical block_size is 
Failed locking the image
Master Checksum Info
gcd_kqueue: kevent64 returned error 
+[DISLAFrontend(Private) redirectStdoutForDisplay]
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
, flags = 
version
virtual int BackendSG::write(const sg_entry &)
-[DIDiskArb addDisappearedCallbackWithMountPoint:shadowMountPoints:delegate:]
-[DIBaseParams tryResolvePstackChain:]
read only
Blocks header
 bits in the bitmap
US
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
Total Bytes
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
std::string FileDescriptor::get_mounted_on_fs() const
-[DIShadowChain openWritable:createNonExisting:]_block_invoke
attempting to authenticate with aea key
Failed to get canonical path for sandbox extension
Diskimageuio: images with constraints currently not supported
 opened and replaced at attempt 
APPLECONNECT.APPLE.COM
Duplicate shadow values for: %@
false
set_euid_wrapper::set_euid_wrapper(uid_t)
Couldn't lock entry
Cannot find image with provided UUID.
create_stack_vector_from_single_path called with an empty path
+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
+[DiskImageParamsXPC newWithURL:fileOpenFlags:error:]
backend write failed during locked flush of map element, error 
The argument index is invalid
, error 
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
!1
, dest buffer_size 
Crypto couldn't write to inner backend @ 
-[DIDeviceHandle waitForQuietWithService:error:]
-[NativeDiskImageGraphNode deleteImage]
Failed to read auth table
udzo
crypto_format: Can't derive key 
band_ptr DiskImageSparseBundle::find_band_in_array(uint64_t)
FSFormatExecutable
Diskimageuio: Failed to create resizer: 
UDIF images are currently not supported in diskimage_uio
Initialized bands array of size 
}
 offset = 
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
com.apple.diskimages.band_unmap
Can't flush asif on table close, backend barrier failed
, res=
StandardCompressedBackend::pimpl::pimpl(algo_t)
futimes failed on 
wkms-uat.sd.apple.com
, truncating
Invalid URL
File size is less than the minimum header size
Encryption Method
Block size mismatch in DiskImageStackable
fstatfs failed with err code
File: Couldn't fetch status, error: 
NSURLSession read to buffer nbyte=%zx offset=%llx\n
Preferred Block Size
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
The specified image is a folder but not a sparsebundle
Failed creating 
. Opening as root
Request failed
Not valid SAKS metadata (no environment field)
Image has a read-only format, attach failed due to force RW flag
Cannot find disk image with reg entry ID 0x%llx
snapshot
Disk image is terminated, skipping future_flush
Failed during table 
Can't load asif dir table
Mode for new files in bundle: 
Cannot get subscriber from plugin
crypto_mode
void DiskImage::do_terminate()
header_signature
crypto
 of type 
-[DIOpenParams unlockImageWithOpenParams:]
public_key_crypto_algo
allowStoringInKeychain
174350
Invalid minimum data partition size
Invalid band size (
shadowStats
Failed creating IO iterator, err code %d
PUT
RW
Destination folder URL must represent an existing folder.
-[DIShadowChain addShadowNodes:wrapReadOnly:error:]
blockSize
Cannot find IO object of class %@
Constructing sb context
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:429:
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
%@:%@
int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)
Name
Can't read encryption entry header, error 
conversionMethod
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ H
RootDeviceEntryID
value validator
-[DIDiskMountTracker trackIfMyDisk:]
Diskimageuio: can't get lock status 
-[DIDataPartition resizeFileSystemToMinimumWithError:]
Unable to convert data to vector.
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
, band was written to
Snapshot
AppleAPFSVolume
inputURL
Band 
io_result_t di_asif::details::dir_base::move_realloc_chunk(ContextASIF &, char *, size_t, uint64_t)
Minimum container size must be non-zero
 is not supported (err code 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Harde
int di_asif::details::dir::defrag_table(ContextASIF &, dir_idx_t)
Ignoring truncate on block device
-[AAS3DownloadSession readToBuffer:size:atOffset:]
%12u max attempts for a request\n
Medium Type
Key size isn't a multiple of 8
auto FileLocalAsync::shared_state_t::init_unmap_zeros()::(anonymous class)::operator()() const
downloadStreamPRead
knox.sd.apple.com
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
Decryption key missing
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
The image was unlocked before setting userData
UDIF read-only compressed image
Only RAW, ASIF and UDSB formats are supported for new blank images
Invalid header: %s
v1/ac/decrypt
-[DIDiskArb waitForDAIdleWithError:]
Diskimageuio: required mode 
Unsupported ASIF, contains data beyond current header struct size
 header size 
Unsupported URL scheme
Key from the certificate is not exportable
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c
Convert AEA key from hex failed
unexpected error
ASIF max_write size in header exceed the limit
trailer of a 
curl_easy_init failed\n
diParams
image_variant_type
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
(empty)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638
, trimmed size
Error opening ByteStream
UDIF_header::UDIF_header(const std::shared_ptr<Backend> &)
Failed to generate self signed certificate
The operation was cancelled by the user
Flush failed - returning 
\\\"
typename boost::enable_if<boost::is_integral<typename hex_iterator_traits<OutputIterator>::value_type>, OutputIterator>::type boost::algorithm::detail::decode_one(InputIterator &, InputIterator, OutputIterator, EndPred) [InputIterator = std
%02x
assetAttr
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669
Failed copying %s
AEA
com.apple.diskimage-plugin.amber
Diskimageuio: ASIF header changed while unlocked
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:836: libc++ Harde
passphrase_header
Invalid size hex key %lu
-[DiskImageParamsXPC allowOnDiskCacheWithSinkDiskImage:]
void udif::details::UDIF_base::generate_blocks(CFArrayRef)
Failed to read from certificate file 
io_result_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
Failed to cleanup folder traversal
passphrase
com.apple.di_raw_test_plugin
RAW read-write image
resource-fork
 (errno 
!Q
size
ERROR: Shipping private key is NULL.
AEA key retrieval failed
Could not determine cache dir
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
Diskimageuio: Multiple images given but block size differ. 
Temporary Items
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
Cannot open filesystems bundle
prod
ID
flush
void SparseBundleBackend::write_primary_info_plist()
void SparseBundleBackend::write_info_plists()
Invalid format for shadow file
MediaKit error during partitioning
Unknown checksum found
userData
Sparse images are not supported by DI2
sg: 
Daemon PID
Diskimageuio: backend is not a FileLocal
 extents
.FBCLockFolder
Write zeros to unmap unaligned start region failed (err code
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_write(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
asif_header
ASIF max chunk size in header exceeds the limit
statInstanceID
tkn
 = offset = 
Failed getting runloop source
System Entities
knox-uat.sd.apple.com
Can't flush asif table, bitmap flush failed 
crc32 {
Failed reading 
ERROR: shipping key enc-request failed base64 decode
Is Cache
, allocated: 
 - different calculated: <
Background close of 
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
Calling 
x-amz-
-[PluginDiskImageGraphNode(Append) validateAppendedImageWithInfo:error:]
.
Band data doesn't exist, zeroing
Diskimageuio: backend isn't locked
ASIF: can't read/allocate asif metadata
Failed to sign request\n
ramTestPluginCreate
Failed to get Daemon PID
Failed to create passphrase auth entry
MediaKit read error
Unsupported public key algorithm.
Schemes
UDIF: compression algo is invalid
Failed to write SLA text to stdout
Barrier failed before dir flush
0123456789abcdefghijklmnopqrstuvwxyz
Write zeros to unmap unaligned end region failed (err code
fetch_restore_key/%s OS/%@
Identity Info
vbuf validator
 bands flushed, calling 
private/var/vm
applicationId
saks-ac-prod.g.apple.com
Unexpected backend type for file
, Force closing.
di_plugin_image_t *PluginsManager::create_plugin_image(const di_plugin_t &, int, const CFDictionaryRef)
The format string contains an invalid escape sequence
json
 / 
Request creation
identityCertificates && [identityCertificates count] >= 1
device not found in registry
bool ref::details::ctrl_blk<di_asif::details::table, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::table, tag_t = unsigned long long]
Asif header size unaligned
invalid uuid string
\\r
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_after_crypto_ctx(std::optional<crypto_internal::keys> &&)
 (band 
, current is 
Failed writing sparsebundle info
virtual int SparseBundleBackend::lock()
Disk image is terminated, skipping future_write
singleInstanceDaemon
int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)
Yes
Shadow
v32@?0@\"DIShadowNode\"8Q16^B24
Disk image is terminated, skipping read
Failed to find partition scheme
+[DICommonAttach DI1_attachWithDictionary:BSDName:error:]
Range: bytes=%llu-%llu
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocal
s3HeaderAppendWithFormat
The requested URL is an existing non-sparsebundle folder
Diskimageuio: couldn't resolve image while setting passphrase 
Bad or missing key in SAKS response.
 length 
crypto_header
Diskimageuio: query format failed 
lzma
ASIF: Block size isn't a multiple of 512
Base
pluginParams
disk
Failed during data entry write in table write, error 
 with 
. returned 
Cannot acquire 
wkms
pstack
Diskimageuio: Nested stacking is not allowed.
Failed placing new 
private/var/db/BootCache.playlist
diskimageuio: pre-write final error 
band 
Can't read UDIF trailer
invalid file size for 
fileMode
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
 completely
nobrowse
 auth entry
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433:
Failed to validate metadata 
no_match
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_fd(int, const std::filesystem::path &, bool)
virtual int FileLocalAsync::_write(const sg_entry &)
readSynchronizer
-t
flags_t
RO
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__memory/unique_ptr.h:
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/
Can't take exclusive lock on entry
AES = 0x80000001
> real: <
 (our euid is 
IOServiceMatched
 is clean, skipping flush
KVS key value - parse failure.
ASIF meta header size exceeds its maximum
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
com.apple.knox.url
Skipping erase of band 
 buffer_size = 
Sections
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c
Registered plugin 
Missing key in Knox response
Diskimageuio: decryption key missing
io_result_t DiskImage::Context::read(const sg_vec::iterator &, const sg_vec::iterator &)
First block of dir write failed with 
ASIF: Content dirty bit is set when reading from disk
void space_allocators::FixedSize::trim_largest(const size_changed_fn_t &)
 trying to check permission after EACCES
image-path
AES-CBC
int DiskImage::Context::unmap(const unmap_extent_t *, size_t)
Failed creating MediaKit object
) is unlocked
Unexpected UDIF header length (
Num Tables
shared
keys/fetch
oauth
Diskimageuio: locked backend 
-[MKDIDevice partitionDiskWithGPTTypeID:error:]
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
Dir Pointer Version
AWS4-HMAC-SHA256 Credential=
Image Info
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
Diskimageuio: get block size failed 
crypto_format: Can't decrypt wrapped key 
metadata_read_only_flags
Invalid UDIF format, contains intersected blocks
Failed to serialize symmetric key to crypto header
https://%@/v1/ac/decrypt
fstat failed
Size Info
Error decrypting data using public key, error code 
The argument index should end with a ':' or a '}'
 with errno: 
???
isCache
Failed to issue sandbox extension token for file
Cleanup At Startup
int BufferedWriteBackend::reset_last_offset(const sg_entry &)
AAS3DownloadStream (NSURLSession)\n
/usr/local/bin/appleconnect
Unmap done
Invalid user data content
cores
Key transcoding failed.
 (band 0x
nil params specified
curl_slist_append failed\n
hdid-pid
ssize_t plugin_decode_buffer(void *, const char *, void **)
void boost::uuids::detail::sha1::process_byte(unsigned char)
euqueueRequest timed out
Diskimageuio: Snapshot detected on top of cache
enc_keys
Failed to create resizer
Can't create data for plist deserialization
Contains non-hexadecimal characters.
virtual int FileLocalAsync::lock()
Diskimageuio: Unsupported image format
Diskimageuio: get nr blocks failed 
rawTestPlugin_t::~rawTestPlugin_t()
User declined SLA
Couldn't convert CFStringRef to a proper std string
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ H
i
Diskimageuio: Failed to create disk image: 
PKCS5_PBKDF2 = 103
UDZOMAX
-[DIEncryptionFrontend storeInKeychainWithPassphrase:forceSystemKeychain:error:]
Compression Type
error
0B
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
BuildVersion
userDict cannot be nil or empty
pkce
Format Description
virtual int Ram::_write(const sg_entry &)
bundle-backingstore-version
-[DIDeviceHandle updateBSDNameWithBlockDevice:error:]
+[DICommonAttach diskImageAttach:BSDName:error:]
ActiveNode
Sandbox extension token exceeds maximum size
ZLIB = 0, LZFSE = 1, LZMA = 2, ZLIB_9 = 3, BZIP = 4
virtual int FileLocalAsync::flush(di_flush_mode)
-[DIShadowChain topDiskImageNumBlocks]
mountedFrom
APFS
ERROR: This archive does not contain a shipping key response.
get_next_capacity, allocator's max size reached
com.apple.diskimages2
Info.bckup
Accept: application/xml
com.apple.wkms.fcs-response
Tag
A mandatory argument is null in a DiskImages2 API call. Remember to check if init succeeded
encryption
Image does not have write permissions
Checksum Value
hw.memsize
locale-specific form
Diskimageuio: single image given, but role is 
bool ref::details::ctrl_blk<di_asif::details::map_element, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::map_element, tag_t = unsigned long long]
KEY_BITS_160 = 160, KEY_BITS_NONE = 0
unmapped
Invalid partitions returned by MediaKit
 - unmap_range: [
header_ignore_fields_t
Missing image path property
Failed to update crypto header
image_format diskimage_uio::details::diskimage_impl::query_image_format() const
IOPartitionScheme
int PluginsManager::register_plugin(const string &, di_plugin_t *)
+[DiskImageCreatorFromFolder allowParallelModeWithURL:outMode:error:]
fts_set failed
Missing Expected AUTH DATA in AEA.
6.0
-[DiskImageCreatorFromFolder createImageWithSrcFolder:completionBlock:]_block_invoke
Role
Image referenced in the pstack is unreachable.
knox
com.apple.diskimages.file.crypto
internal metadata
mapped blocks of band 
Writing 
Trying to read @ 
addRequest
IsCache
-I
supportsBarrier
-[DIConvertParams prepareParamsForSquashWithError:]
useFormatMappingInfo
Diskimageuio: bottom diskimage should have role image, but 
: 
-[DiskImageGraph(AppendPrivate) appendWithURL:isCache:tag:numBlocks:toNode:setNewActive:error:]
r
SLA text is empty
read
Corrupted encryption table, invalid offset/length in entry's descriptor
Not allowed more than one instance of 
bad flush type (
Invalid open mode specified
oauth-id-token:
crypto_fd
Destructing sb context
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_fo
The fill option contains an invalid value
%12.2f MB/s download speed\n
/s3/aws4_request\n
Unexpected error creating (unlocked) backend
is_locked
size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)
version_t
.VolumeIcon
-o
Legacy prepended-header UDIF image is not supported by this framework
is_writable
Reserved
private/var/folders
No mapped file for band 
failed to set euid to 
forwardLogs
-[DIDiskMountTracker onDiskDescriptionChangedWithDiskName:isMounted:]
User data is not supported in this image format
openid,dsid,accountname
unique_lock::unlock: not locked
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
 logical: 
Failed opening the shadow/cache file(s)
-[DiskImageCreatorFromFolder createImageWithSrcFolder:completionBlock:]_block_invoke_2
-v
truncate error: 
HTTP request failed with status code: %ld
udifHeader
Invalid ASIF header size
xpcEndpoint
Metadata contains unsupported field 
Invalid value for asif header field: %s
diskimagesiod
Failed to subscribe to the plugin's IO ring
Unexpected unmap command received on read only image
Failed to get minimum APFS container size
failed to enter SQE to the ring, ret code 
Failed to replace passphrase entry in auth table
saks-ac-uat.g.apple.com
AppleDiskImageDevice
diskimagesuio: future read invalid in read
:
, keeping file unlocked
Failed opening the sparsebundle as user 
 bytes, reading only 
remote mount
wrap_key_crypto_padding_algo
Backend barrier failed during dir flush, error 
Failed to parse auth data blob.
void plugin_encode_buffer(void *, const char *, const void *, size_t)
-[DIBaseParams prepareImageWithXpcHandler:fileMode:error:]
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
Compressed Offset
device_OBSOLETE = 0, device = 1, partition = 2
virtual io_result_t sparse_bundles::Band::read(DiskImage::Context &, const sg_entry &)
 errno: 
/sbin/umount
Remember password in my keychain?
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
Resource name is too long to fit uint32_t
device with registry entry ID 0x
diskimage_
encKeys
Replacement argument isn't a standard signed or unsigned integer type
 src size 
com.apple.wkms.url
 mode=
New password
location
missing DI_ATTACH_ENTITLEMENT on non macos platform
header_size_512 = 512, header_size_4k = 4096
void BaseFolderCopier::print_permissions(uid_t, mode_t, char *)
DiskImages Framework
Incorrect passphrase
lock_backend
deserializationError
Failed writing full dir
Could not generate daw token - AppleConnect Failure
environment
 block_size: 
Couldn't exclusively lock entry 
Failed to parse key in KVS (zero size key).
DiskImageCreatorFromFolder
PluginName
Mapped Sectors
Can't read for defrag
 bytes is smaller than its trailer
(err code %d)
 changed before retain completed
bytes=
tr '\\r' '\\n' | fmt | ${PAGER:-more}
-[DIController2ClientDelegate attachCompletedWithHandle:reply:]
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:128:22)]
v16@?0Q8
Failed to unlock the encrypted image during open
Request failed: %03ld %s
Disk image operation failed with error code %d
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
Provided image has no identity info.
int DiskImage::Context::flush(di_flush_mode)
, err 
invalid header: %s
The URL encoded into the AEA authdata is missing or invalid.
virtual io_result_t DiskImageUDIFRead<UDIFReader<locks::None>, DiskImageUDIF>::read(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &) [UDIF = UDIFReader<locks::None>, UDIFVariant = DiskImageUDIF]
void diskimage_uio::details::diskimage_open_params_impl::lock_backend_if_required()
none = 0, crc28 = 1, crc32 = 2, dc42 = 3, md5 = 4, sha = 5, sha1 = 6, sha256 = 7, sha384 = 8, sha512 = 9, none_valid = 10
Opening band 
Failed creating CFAutoRelease instance.
XPC connection failed
int plugin_decode_fd(void *, const char *)
virtual int BackendSG::read(const sg_entry &)
fchownat failed for 
Attached disk image device info: BSD Name [%@], image URL [%@]
pthread_once
Cannot retrieve passphrase from user via TTY or GUI
map_element flush failed on creation
Direct Mode
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
Failed to find keychain item using hashed key
Authorization
-[DIClient2IODaemonXPCHandler cancelSLAWithReason:]
Parent UUID
gcd::gcd_kqueue::gcd_kqueue(gcd_queue &, std::function<void (struct kevent64_s *, int)>)_block_invoke
+[BackendXPC newFileBackendWithURL:fileOpenFlags:error:]
Error in new image's UUID.
void di_hybrid_subscriber_t::cancel()
key_derivation_algorithm_t
virtual sparse_bundles::Band::~Band()
-[FileLocalXPC sandboxExtensionTokenWithError:]
current_mode
Bitmapped Entries
static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)
enc-request
/
iCloud
https://%@/westgate/appinfo
autoMount
Plugin's ring resumed, ret code 
io_result_t DiskImageSparseBundle::perform_io(ContextSparseBundle &, bool, const sg_entry &)
block_attributes
(unlocked)
Network Trash Folder
ERROR: Response dictionary is missing required keys. Will fail
-[DIUserDataParams encodeWithCoder:]
invalid flags
Requested write is out of range - offset 
virtual di_coroutines::Task<void> CompressedBackend::run_futures()
KVS dataBuffer allocation failure.
Bearer openid-id-token-%@
ram
Context creation failed.
encryption_mode
di_plugin_image_t *PluginsManager::decode_plugin_image(const di_plugin_t &, const diskimage_decode_fn_t &, void *)
Failed to mount filesystems
[
Trimming: Written 
exclusive
+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]
-[DiskImageParamsXPC createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:]
Cannot decode file descriptor
baseBackend
Diskimageuio: Single element in pstack that isn't an image
wrap_key_crypto_algo
Corrupted plist
-[DIDeviceHandle dealloc]
%.*s: %{public}@ mounted successfully
%.*s: Failed to read passphrase from TTY
%.*s: Keeping RO mode for %{private}@
%.*s: Mount point %{private}@ disappeared (shadow's mount point)
%.*s: Pager command failed with status %d, output may be incomplete
%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported
%.*s: WARNING: Found %llu sectors with invalid flags (has_bitmap)
%.*s: Cancelling copy (NSProgress cancel requested)
%.*s: Minimum data partition size is %lld blocks (estimation was %lld blocks)
%.*s: Using an existing shadow file: %{private}@
%.*s: Base image is raw format, using nil UUID.
%.*s: Skipping content of folder %s
%.*s: Failed getting mounts list
%.*s: Unlocked using public key
%.*s: Got error from last XPC command: %{public}@
%.*s: Issuing new sandbox extension token for file %{private}@
%.*s: Creating connection to IO daemon clients listener
%.*s: Copying: %s -> %s (%ld threads)
%.*s: Reached an invalidation handler for the IO daemon connection
%.*s: Appeared Disk: %@
%.*s: Skipping %s
[0x%08x] %{public}s
%.*s: Waiting for disk arbitration idle
%.*s: Asking for passphrase using readpassphrase
%.*s: Unlocked using symmetric key
%.*s: Not a sparseimage: %{public}s
%.*s: cancelSLA wait returned error: %{public}@
%.*s: Creation failed, erasing %{private}@
%.*s: Failed during ASIF extents enumeration on offset: %llu
%.*s: Failed to erase output URL
%.*s: Received connection from pid %d with euid %d. Our euid is %d
%.*s: Unmounting %{private}@
%.*s: Successfully retrieved WKMS non-shipping key
%.*s: Cache file %{private}@ opened with RW access
%.*s: Image %{private}@ re-opened with RW permissions
%.*s: SLA detected, connecting to IO daemon for user acceptance
%.*s: Mountable Disk: %@
%.*s: File system is %{public}s
%.*s: Input and output files are the same, using a temporary output file
%.*s: Mount point %{private}@ disappeared
%.*s: Waiting for disk arbitration to finish mount
%.*s: Failed to open /dev/tty: %d, falling back to stderr
%.*s: %@
%.*s: BSD name: %{public}@
%.*s: Disk image attached (with DI2) as %{public}@
%.*s: Performing in-place squash optimization
%.*s: Moving %{private}@ to %{private}@
%.*s: Ignoring, during shutdown
%.*s: Passphrase found in keychain, unlocking the image
%.*s: Disk arbitration idle callback received
%.*s: Keychain lookup returned %d
%.*s: Failed to generate device identity: %@
%.*s: Invalid key: %@
%.*s: entry with %{private}@
%.*s: permissions for current path %s (uid %d): %c%c%c%c%c%c%c%c%c
%.*s: entry
%.*s: Failed creating semaphore
%.*s: Not a UDIF: %{public}s, assuming RAW format
%.*s: Failed to get info of newly created shadow/cache, will try to delete if an image was created.
%.*s: Failed initializing plugin: %{public}@
%.*s: Disk image resized to %llu bytes
%.*s: On disk cache is not supported on embedded systems
%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization
%.*s: Creating %@
%.*s: IOServiceWaitQuiet timeout occurred, retrying.
%.*s: Decoding plugin instance
%.*s: Failed to dup stdout: %d
%.*s: Appending to plugin node, skipping validation.
%.*s: Failed opening %{private}s, errno %d
%.*s: Registering DiskDisappearedCallback for %{private}@ (shadow's mount point)
%.*s: Shadow file %{private}@ opened with RW access
%.*s: No matching item found in keychain
%.*s: Received: %{public}@
%.*s: Cancelling traverse (NSProgress cancel requested)
%.*s: Background copy of %s to %s
%.*s: Failed to read pstack: %@.
%.*s: Using an existing cache file %{private}@ with RO access
%.*s: On disk cache path: %{public}@
%.*s: %{public}s, errno=%d
%.*s: Failed creating queue
%.*s: Disk partitioning completed
%.*s: res_dict: %{public}@
%.*s: Failed to dup2 to stdout: %d
%.*s: Disk mount wait skipped (emulation mode)
%.*s: Keychain item requires ACL upgrade
%.*s: Out of memory, failed to allocated %zu bytes for key %@
%.*s: IOServiceWaitQuiet done
%.*s: A valid plist was given, but it has no pstack version key
%.*s: User data retrieving passed, %d value(s) found
%.*s: Successfully retrieved WKMS shipping key
%.*s: Using existing disk image params
%.*s: Stable UUID not found in provided image, Falling back to using Stackable UUID.
%.*s: Erasing %{private}@
%.*s: Falling back to attach with di1
[0x%08x](warning) %{public}s
%.*s: Mount error: %@
%.*s: isWritableFormat: %s
%.*s: Failed to copy source disk image to temporary URL
%.*s: DIDeviceHandle object is deallocating, invalidating connection
%.*s: Creating %s plugin instance with params: %@
%.*s: Creating connection with %{public}@
%.*s: %{public}s
%.*s: Failed to connect to IO daemon for SLA handling
%.*s: MediaKit scan dict: %@
%.*s: XML_RSRC_FORK: %{public}@
%.*s: entry: %{public}@
%.*s: %{private}@ unmounted successfully
%.*s: Error encoding user dictionary: %{public}@
%.*s: Failed to open pager, writing directly to stdout
%.*s: Error checking %s property: %s
%.*s: Failed instantiating rawTestPlugin object: %s (code %d)
%.*s: Allow parallel copy: Source=%d, Target=%d
%.*s: %s
%.*s: Failed to delete %@: %@
%.*s: %{public}@ %{public}@
%.*s: Storing passphrase in the %s keychain
%.*s: Validation exception: %{public}s
%.*s: Registry entry ID is 0, can't check %s property
%.*s: Mount Disk: %@
%.*s: Failed to find IOMedia entry for %@
%.*s: MKMediaCreate failed with error %d (%d/%d)
%.*s: Failed to create graph from plist: %@.
%.*s: Image file %{private}@ opened with flags %d
%.*s: Reached an interruption handler for the IO daemon connection
%.*s: Parent image is RAW, skipping shadow UUID validation on append.
%.*s: Failed to copy metadata of %s (errno %d)
%.*s: Failed to dup stderr: %d
%.*s: New disk image size is the same as previous
%.*s: XPC connection lost: %{public}@
%.*s: Failed to open top disk image node.
%.*s: Not a pstack
%.*s: Partition map updated
%.*s: Reached with diskURL=%{public}@
%.*s: %{public}@ error %{public}@
%.*s: Using %{private}@ as read-only
%.*s: Shadow format validator exception: %{public}s
%.*s: Cannot open shadow chain %{private}@ with RW access: %{public}s, errno=%d
%.*s: I/O error at offset %lld iov_count %d errno %d
%.*s: Copying: %s -> %s
%.*s: <%lu> %{public}s
%.*s: Data partition resized
%.*s: Asking user permission to store the passphrase in the keychain
%.*s: Successfully issued sandbox extension token for file %{private}s (token length: %zu bytes)
%.*s: Copied sandbox extension token from reopened backend (length=%zu)
%.*s: Block device class for %@: %@
%.*s: File system resized
%.*s: numBlocks queried for an empty shadowChain.
%.*s: Creating NSXPC listener on %{public}@
%.*s: Failed to get block device for disk %@
%.*s: Convert in place failed, erasing %{private}@
%.*s: Folder size: %llu
%.*s: Copying %s to %s, flags 0x%x
%.*s: Failed to copy %s (errno %d)
%.*s: Mounting %@ on %@
%.*s: Disk arbitration mount completed
%.*s: Looking for encrypted image passphrase in the %s keychain
%.*s: Creating connection to %{public}@
%.*s: Skipping invalid file type: %s
%.*s: APFS container and volume created
%.*s: Registering DiskDisappearedCallback for %{private}@
%.*s: Failed to get UUID info of provided image.
%.*s: User data embedding passed
%.*s: %{public}@ - %{public}@ %{public}@
%.*s: Due to the conversion error, erasing the output file
%.*s: Ejecting %@
%.*s: %@ ejected successfully
%.*s: Cannot open cache file %{private}@ with RW access, trying read-only
%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)
%.*s: Missing parameters
%.*s: Skipping Class F protected file: %s
%.*s: Passphrase is correct
DIIOMedia
DICreateASIFParams
DIStackParams
NSXPCListenerDelegate
DIHelpers
Append
BaseDiskImageCreator
MKDIDevice
DISLAFrontend
DIVerifyParams
CryptoBackendXPC
DIDiskMountTracker
KNOXBackendXPC
DiskImages2
DiskImageCreatorFromDevice
DIDataPartition
DIOpenParams
DIDeviceHandle
RamXPC
DIEncryptionFrontend
DIEncryptionCreator
Private
DICreateUDSBParams
BlankDiskImageCreator
AAS3DownloadRequest
DIAttachedDeviceInfo
DIDiskArb
NativeDiskImageGraphNode
PluginDiskImageGraphNode
SerializedDiskImageGraph
DIShadowChain
DIDiskImageBridge
workaround
DIError
DIControllerProtocol
DIIOIterator
DIChpassParams
DIShadowNode
DiskImageParamsUDIF_XPC
SparseBundleBackendXPC
AEABackendXPC
BackendConvenience
DIAttachParams
DICreateRAWParams
DIImageHandle
DIExtension
DIEncryptionUnlocker
DIConvertParams
DIIOClientProtocol
DICommonAttach
AAS3DownloadSession
NSCoding
DIResizeParams
DIClient2Controller_XPCHandler
DIUserDataParams
NSSecureCoding
NSObject
DIClient2IODaemonXPCHandler
DIIOObject
DIBlockDevice
DIURL
DITemporaryPassphrase
DIController2ClientDelegate
DiskImageParamsXPC
BackendXPC
Info
DIBaseServiceDelegate
QuarantineFileHandler
FastFolderCopierWrapper
DI1
FileLocalXPC
DiskImageGraph
DIStatsParams
DIKeyRetriever
DiskImageParamsSparseBundle_XPC
DiskImageParamsASIF_XPC
DIBaseAgentDelegate
DiskImageCreatorFromFolder
DIController2ClientProtocol
DiskImageParamsRAM_XPC
AppendPrivate
DIAPFSPartition
_TtC16FetchRestoreKeys16CryptoKitWrapper
DIDiskArbEmulation
DIBaseAgentXPCHandler
DiskImageParamsRaw_XPC
DiskImageParamsPlugin_XPC
DIParams
InfoPrivate
DICreateParams
DIImageInfoParams
DiskImageGraphNode
cpp_extension
DIEncryptionChpass
DIBaseXPCHandler
PersistentBackend
DiskImageParamsLocked_XPC
PluginBackendXPC
DIStatFS
ReadSynchronizerBackendXPC
DIBaseParams
enumerateObjectsUsingBlock:
_offset
DI1_attachWithDictionary:BSDName:error:
Ti,R,N,V_UIOOpenMode
initWithBase64EncodedString:options:
setMountedDiskCount:
T@\"NSData\",C,N
addBytesDownloaded:
initWithURL:openMode:error:
T@\"BackendXPC\",R,N,V_baseBackendXPC
URLByDeletingLastPathComponent
getDescendants
setWithObject:
_semaphore
WKMSShippingKeyWithURL:metadata:error:
_xpcEndpoint
unlock
updateStatFSWithError:
T@\"NSObject<OS_dispatch_semaphore>\",R,V_requestsSem
decryptKeyWithData:destKey:destKeySize:error:
lookupLegacyKeychainWithXpcHandler:error:
setNumBlocks:
setReadPassphraseFlags:
waitUntilExit
T@\"DiskImageGraphNode\",R,N
_requests
T@\"<DIDisappearedMountPointDelegate>\",W,N,V_delegate
autorelease
fileDescriptor
initWithDictionary:workDir:error:
initWithURL:fileOpenFlags:bandSize:
managedAttachWithParams:handle:error:
pluginName
stringByTrimmingCharactersInSet:
T@\"NSLock\",R,V_requestsLock
T@\"NSArray\",&,N,V_handles
_UUID
ephemeralSessionConfiguration
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
getFirstNonCacheAncestorWithNode:error:
TB,R,N,V_isCache
_allowStoringInKeychain
deserializationError
numBlocks
openWithError:
T@\"NSString\",R,N,V_sandboxToken
T@\"DIStatFS\",&,N,V_inputStatFS
T@\"NSNumber\",R,N,V_overrideBlockSize
Tq,N,V_appearedDiskCount
_fileMode
copyUpdatedOutputURLWithError:
host
launchedTaskWithExecutableURL:arguments:error:terminationHandler:
RAMdisk
sandboxExtensionTokenWithError:
TQ,N,V_blockSize
_cacheLock
_mountedDiskCount
nilWithPOSIXCode:description:error:
resizeFileSystemToMinimumWithError:
self
T@\"NSURLSession\",R,V_urlSession
T@\"NSUUID\",R,N,V_parentUUID
_filePath
_isPrivileged
_pstackDict
copy
executeWithPath:arguments:error:
logWithHeader:
_diskImageParamsXPC
attachWithParams:reply:
initWithGraphDB:workDir:error:
keychainUnlockWithEncryptionUnlocker:reply:
longLongValue
newACEndpointWithEnvironment:error:
registerDiskTrackingCallbacksWithDiskTracker:
verifyWithError:
TB,N,V_emulateExternalDisk
_nodes
initWithURL:openMode:
T^{?=Q*^{AAS3Context_impl}},R,V_streamBase
_autoMount
countIOMediaObjectsWithError:
initWithBackendXPC:header:
newEntityDictWithIOMedia:mountPoints:
createEncryptionWithXPCHandler:error:
errorWithDomain:code:description:verboseInfo:error:
isKindOfClass:
effectiveUserIdentifier
newEnvWithDictionary:error:
pstackURL
setImageInfo:
initWithString:
T@\"NSBundle\",R
T@\"NSMutableDictionary\",&,N,V_graphDB
```
