# `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,950,288 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 41 (Size: 5528)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE, NlistOutofsyncWithDyldinfo
```

## Linked libraries (24)

- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/local/lib/libcurl.4.dylib (compatibility version 7.0.0, current version 9.0.0, weak)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit (compatibility version 302.0.0, current version 944.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
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
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authorization.extract-password</key>
	<true/>
	<key>com.apple.diskimages.creator-uc</key>
	<true/>
	<key>com.apple.private.amber.client</key>
	<true/>
	<key>com.apple.private.amfi.version-restriction</key>
	<integer>2</integer>
	<key>com.apple.private.apfs.no-padding</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.vfs.role-account-openfrom</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>DIDeviceCreatorUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.diskimagesiod.xpc</string>
		<string>com.apple.diskimagesiod.ram.xpc</string>
		<string>com.apple.securityd</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>hw.logicalcpu</string>
		<string>hw.memsize</string>
		<string>debug.didevice_queue_depth</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.DiskImagesKeychainGroup</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>
```

## Objective-C (75 classes, 9 protocols)

Classes: `AAS3DownloadRequest`, `AAS3DownloadSession`, `AEABackendXPC`, `BackendXPC`, `CryptoBackendXPC`, `DIAttachParams`, `DIBaseAgentDelegate`, `DIBaseAgentXPCHandler`, `DIBaseParams`, `DIBaseServiceDelegate`, `DIBaseXPCHandler`, `DIBlockDevice`, `DIChpassParams`, `DIClient2Controller_XPCHandler`, `DIClient2IODaemonXPCHandler`, `DIController2ClientDelegate`, `DIController2IO_XPCHandlerAttach`, `DIController2IO_XPCHandlerBase`, `DIController2IO_XPCHandlerStats`, `DIControllerServiceConnection`, `DIControllerServiceDelegate`, `DIConvertManager`, `DIConvertParams`, `DICreateASIFParams`, `DICreateParams`, `DICreateRAWParams`, `DICreateUDSBParams`, `DIDeviceHandle`, `DIDiskImageBridge`, `DIEncryptionChpass`, `DIEncryptionCreator`, `DIEncryptionFrontend`, `DIEncryptionUnlocker`, `DIError`, `DIHelpers`, `DIIOIterator`, `DIIOMedia`, `DIIOObject`, `DIImageHandle`, `DIImageInfoParams`, `DIKeyRetriever`, `DIResizeParams`, `DISLAFrontend`, `DIShadowChain`, `DIShadowNode`, `DIStatFS`, `DIStatsParams`, `DITemporaryPassphrase`, `DIURL`, `DIUserDataParams`, `DIVerifyManager`, `DIVerifyParams`, `DiskImageGraph`, `DiskImageGraphNode`, `DiskImageParamsASIF_XPC`, `DiskImageParamsLocked_XPC`, `DiskImageParamsPlugin_XPC`, `DiskImageParamsRAM_XPC`, `DiskImageParamsRaw_XPC`, `DiskImageParamsSparseBundle_XPC`, `DiskImageParamsUDIF_XPC`, `DiskImageParamsXPC`, `FileLocalXPC`, `KNOXBackendXPC`, `NSMutableDictionary`, `NSXPCConnection`, `NativeDiskImageGraphNode`, `PluginBackendXPC`, `PluginDiskImageGraphNode`, `QuarantineFileHandler`, `RamXPC`, `ReadSynchronizerBackendXPC`, `SerializedDiskImageGraph`, `SparseBundleBackendXPC`, `_TtC16FetchRestoreKeys16CryptoKitWrapper`

Protocols: `DIController2ClientProtocol`, `DIControllerProtocol`, `DIIOClientProtocol`, `DIIODaemonProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `PersistentBackend`

## Strings (3,723)

First 2,500 of 3,723.
```
Compressed(
overrideBlockSize
Starting ASIF defrag, used size: 
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocal
Invalid pstack, Active stack contains a loop.
CBC_IV8 = 5, XTS = 0x80000001
BackendSG
void boost::uuids::string_generator::throw_invalid() const
Cannot decode writable
Shadow block size is invalid (0)
static int FileDescriptorWrapper::open_from(int, const std::string &, int)
Key size isn't a multiple of 8
virtual int BackendSG::read(const sg_entry &)
https://%@
)
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:152:22)]
Cannot load libAmber
none
Initialized bands array of size 
Failed to get registry entry ID, ret %d
Skipping erase of band 
ASIF meta header size exceeds its maximum
Final asif 
Offset
;
Invalid header: %s
BZIP compression failed, res=
Destroying File backend, but in-flight promises exist
com.apple.diskimage-plugin.amber
virtual int Ram::_read(const sg_entry &)
Request failed: %03ld (error not set)
The argument index is invalid
\\x{
knox.sd.apple.com
Nothing to defrag
conversion failed
virtual int DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::tran
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
-[DiskImageParamsXPC createDiskImageWithCache:shadowValidation:]
UDIF: compressed runs should be <= 1MB
auto trim_data(const sg_vec::iterator &, const sg_vec::iterator &, size_t, const io_result_t &)::(anonymous class)::operator()(const auto &, const auto &, size_t) const [src:auto = sg_vec_ns::details::sg_vec_iterator, dst:auto = sg_vec_ns::
oma-context
SLA prompt cancelled
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638
AES_KEY = 0x80000001
: flush failed (
Failed to deserialize crypto format
 crypto = 
System keychain access is not allowed on this platform
 backend size 
Failed to update asif header
0X
Remember password in my keychain?
uid restored to 0 (res=
is_locked
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
leaf-cert
XPC connection failed
Diskimageuio: decryption key missing
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:836: libc++ Harde
-[DIConvertManager runWithError:]_block_invoke
An argument index may not have a negative value
-[DIVerifyManager runWithError:]
CFUserNotificationReceiveResponse failed
outputFormat
9999
Couldn't parse media block size in whole disk mode
IOServiceMatched
The argument index value is too large for the number of arguments supplied
mountedFrom
-[DIVerifyParams verifyWithError:]
Corrupted encryption table, invalid offset/length in entry's descriptor
598.40.4
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
 elements returned 
Corrupted shadow file(s) chain
header read-only flags
total_segments_t
bad flush type (
MediaKit returned unsupported block size
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
) is locked
+[DIControllerServiceConnection sendHandleToClient:clientConnection:outError:]_block_invoke
Non supported options in AAS3DownloadSession (ignored): pinned_public_key %s
Could not generate OIDC token - AppleConnect Failure
Write header failed after dir offset changed, error 
v24@?0@\"DIDeviceHandle\"8@\"NSError\"16
-[DIAttachParams newAttachWithError:]
Cannot create target image format with the block size of the source image
pkce
-[DICreateParams onErrorCleanup]
applicationId
system
aaS3ContextClone
Diskimageuio: Can't get image format
set context
%s (%@)
Background close of band at index 
failed to enter SQE to the ring, ret code 
Plugin initialization failed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406:
internal metadata
DES3_3KEY = 17, AES_KEY = 0x80000001
 with errno: 
%12u max requests in flight\n
Diskimageuio: Unsupported image format
Invalid band size (
encryption_key_bits_size_t
segment_num_t
Default
static void process_terminator::terminate()
Couldn't parse partition name or type
r
X-Amz-Security-Token: %s
snapshot
Failed creating 
The type does not fit in the mask
void diskimage_uio::details::diskimage_open_params_impl::lock_backend_if_required()
Evicting all bands for eject
-[DIBaseParams tryResolvePstackChain:]
Metadata contains unsupported field 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:816: libc++ H
key_derivation_algorithm_t
file of 
Max Sector Count
UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::UDIFWritable(const MediaInfo::logical_disk_entities_map &, std::shared_ptr<Backend>, Checksum &
fstatfs failed with err code
int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)
no more attempts allowed
Request failed
STCK
Diskimageuio: Raw header changed while unlocked
Failed opening mapped blocks file for 
bool DiskImageSparseBundle::try_unmap_band_extents_without_list(uint64_t, const extents_set_t &)
Disk image is terminated, skipping ...
-[DIBaseAgentXPCHandler createConnection]
Diskimageuio: backend is not a FileLocal
-[DIBaseServiceDelegate listener:shouldAcceptNewConnection:]
ASIF max chunk size in header exceeds the limit
Validation failed for dictionary key %@.
sign
Diskimageuio: single image given, but role is 
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
sparsebundle
allocated: size change callback failed with 
failed to set the destination image's size
device size not found in registry
partition size
IOServiceOpen failed. error=0x%x
ASIF header changed while unlocked
di_plugin_image_t *verify_plugin_image(di_plugin_image_t *, CFErrorRef)
Found a valid file for 
set_euid_wrapper::set_euid_wrapper(uid_t)
Couldn't lock entry 
-[AAS3DownloadSession readToAsyncByteStream:size:atOffset:]
The symmteric key is wrong
Block size mismatch between crypto header and ASIF header
Can't serialize property list
 is not supported
Failed to serialize symmetric key to crypto header
di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke
mark purgeable failed on 
Block Size
Mandatory callbacks in the plugin's struct are missing
ASIF: Can't defrag entries 
Can't flush asif on table close, backend barrier failed
virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)
read_only_cache = bit(0)
,Signature=
w
void udif::details::UDIF_base::validate_runs()
Ignoring truncate on block device
auto FileLocalAsync::shared_state_t::init_unmap_zeros()::(anonymous class)::operator()() const
Diskimageuio: required mode 
eject timeout
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::verify_backend() const
Invalid ASIF header size
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ H
+[DISLAFrontend(Private) redirectStdoutForDisplay]
fd
Barrier failed after defrag table move, error 
Backend barrier failed during allocator failures handling, error 
int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
Size Info
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
prng_key_bits_size_t
zero-padding
fileMode
Awaitable completed in unexpected state
 existing bands
Error reading sectors for verify 
Closing bands
Stack Info
ram
NO
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr(image_format, std::shared_ptr<Backend> &, bool, const std::filesystem::path &, size_t)
json
%@:%@
AAS3DownloadStream (curl)\n
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
virtual int SparseBundleBackend::lock()
Suspended
Unmap error: 
Failed to create chiper data for public key auth
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
The image is encrypted with obsolete encoding version 1
Feature or image not supported by library
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
udifHeader
ExecutionSchedulerSorted: work returned 
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
crypto_format: cookie differs
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
 extents
Encountered an irrecoverable I/O error, all future I/Os will be invalidated
int ExecutionSchedulerSortedConsecutiveIt<DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, lock
 bytes image
invalid flags
UDIF image of 
+[DIControllerServiceConnection tryAttachWithParams:clientConnection:slaXpcHandler:outError:]
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
-[DIController2IO_XPCHandlerAttach updateFileBackingInfoWithRootDeviceEntryID:error:]
IOServiceWaitQuiet error 0x%x
malloc
hw.memsize
expected<uint64_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_nr_blocks() const
com.apple.diskimages2
vsnprintf
Background close of 
Missing key in SAKS response
Placed new 
BZIP decompression failed, res=
-[DiskImageParamsXPC createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:]
 in dir I/O, error 
header_flags
virtual int FileLocalAsync::unlock_all()
0123456789abcdef
Failed to read passphrase from stdin
Failed during table 
true
application/json
Stackable image
ddm
CFName
Missing entitlement: %@
raw_header
Failed writing full dir
passphrase
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hard
ASIF: invalid dir index to header
rdisk
unknown
 err: 
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_handle_exceptions()
Diskimageuio: reopen backend to required mode 
v16@?0Q8
Retrying request after %.0f seconds %zu bytes at offset %llu
Unsupported compressed run (
The type option contains an invalid value for 
metadata
Unmapping band 
CyrptoKit is missing a required method.
Diskimageuio: Failed to create disk image: 
UDIFDiskImage: failed flush after user data write
BSD Name
sig2_t
intermediate-certs
IOStorageFeatures
entire_device
ftruncate failed, errno: 
Decoding error.
userDict cannot be nil or empty
int details::udif_verify::calculate_checksums(workqueue::workqueue &)_block_invoke
isCache
 auth entries
Unable to convert data to vector.
void di_hybrid_subscriber_t::suspend()
Data
false
diskImageParams
mountedOnURL
Failed to read 
Can't create data for plist deserialization
, taking as mapped data
01
Plugin struct size 
static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Images
BufferedWriteBackend
Disk image is terminated, skipping future_read
-[DICreateParams resizeWithDiskImage:blockCount:error:]
/dev/rdisk
AES-CBC
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
band 
The requested operation will delete all children of the provided node. use recursive removal to surpress this error.
void sparse_bundles::mapped_blocks_t::map_range(uint64_t, uint64_t)
Info.bckup
Failed to erase band 
Missing payload URI in Knox response
The requested URL is an existing regular file
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)_block_invoke
Error creating crypto format
table entry data@
:
bands
vbuf validator
Failed placing new 
/
euqueueRequest timed out
image
Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
 max =
 - same 
basic_string
Diskimageuio: Couldn't get diskimage: 
BackendSG: truncating the inner backend failed, error = 
com.apple.wkms.fcs-response
):
UDIF XML at 
Failed to find keychain item using hashed key
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
writable
Invalid argument, please use one of the DICreateParams derived classes instead
table_entry_data::flags di_asif::details::table::get_next_extent(ContextASIF &, const interval_sectors &, interval_sectors &)
Can't convert data to property list
fskit
Diskimageuio: is cache image failed 
Failed to set up image for info retreival
Looking for an evictable slot for 
-[DIController2IO_XPCHandlerBase setConnectionMode]
pthread_key_create
 bytes, reading only 
(err 
wrap_key_crypto_algo
an integer
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc+
run length
DELETE
Diskimageuio: image is locked
saks-ac-dev.g.apple.com
First block of dir write failed with 
int DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::transform_it
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615
Num Tables
Can't flush asif table, backend write failed
crypto_op: can't initializae aes_cbc context
File: Couldn't fetch status, error: 
frk_set_device_identity_certificates
Section Block Count
-[DIControllerServiceDelegate setupNewConnection:]_block_invoke
Using manual argument numbering in automatic argument numbering mode
Not valid SAKS environment
cache
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
Failed during data entry write in table write, error 
trim largest: size change callback failed with 
virtual int BackendSG::write(const sg_entry &)
 does not allow the 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
sparseHeader
Flush failed - returning 
readPassphraseFlags
ASIF: Entry dirty bit is set when reading from disk
UDIF: compression algo is invalid
int DiskImage::Context::flush(di_flush_mode)
 with 
failed to set euid to 
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
zlib
virtual int Backend::write(const elements_t &)
Cannot attach RAM disk as a read-only device
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
 (band 0x
Failed to get canonical path for sandbox extension
Plugin's ring suspended, ret code 
Failed truncating plist
Mapped Sectors
void space_allocators::FixedSize::trim_largest(const size_changed_fn_t &)
descriptor_special
PKCS1 = 10, OEAP_SHA1 = 0x80000001
createTask
ASIF: table is not aligned to chunk size
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
Failed to read metadata 
%@ failed with error code %d
std::string FileDescriptor::get_mounted_on_fs() const
Unregistering plugin 
Plugin's ring resumed, ret code 
Bad pstack format, node with active UUID not found.
wkms-dev.sd.apple.com
Cannot convert in-place with a shadow file
int DiskImage::Context::unmap(const unmap_extent_t *, size_t)
Can't convert ASIF flag.
-[NativeDiskImageGraphNode deleteImage]
Schemes
X-Amz-Date: %s
-[DIUserDataParams embedWithError:]
com.apple.diskimage-plugin.nbd
!
Disk image URL is too long
-[DIConvertParams prepareParamsForSquashWithError:]
Can't load asif dir table
0
0123456789abcdefghijklmnopqrstuvwxyz
Diskimageuio: Only single cache is allowed
Closing an unchanged 
!Q
-[FileLocalXPC replaceWithBackendXPC:]
resource-fork
dispatch_source_create failed
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
 io: 
v1/ac/decrypt
BSDname
Reserved part isn't zeroed
int di_asif::header::write_header(Backend &)
-[DIEncryptionFrontend storeInKeychainWithPassphrase:forceSystemKeychain:error:]
Context setup failed.
void udif::details::UDIF_base::generate_blocks(CFArrayRef)
UDIF: Failed converting type array string (
Unsupported image stacking
, retrying
 is not aligned to block size
-[DIControllerServiceConnection attachWithParams:reply:]_block_invoke
Decryption key missing
asif_header
segment_count_none = 0, segment_count_one = 1
Cannot find IO object of class %@
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)
media block count
/usr/lib/libAmber.dylib
version_t
forwardLogs
com.apple.DiskImages2.ErrorDomain
Couldn't lock entry
Closed band at index 
Not enough space for metadata
Failed unlocking file with fd 
diskimageuio: pre-write final error 
In-place conversion from this image format is not supported
The width option should not have a leading zero
hw.logicalcpu
Diskimages2 - ASIF - bad reserved bits 
UDIF: Can't find data key in dictionary
 (error code 
Cannot find %@ entry
random generation failed with err code 
 src size 
Failed to resize the image
image_format diskimage_uio::details::diskimage_impl::query_image_format() const
Background erase of 
, current is 
Range
Failed creating property list
Can't lock entry
void convert(DiskImage::const_extents_iterator_t, DiskImage::const_extents_iterator_t, DiskImage &, DiskImage &, const std::function<void (int64_t)> &, bool *)_block_invoke
\\n
Info.plist
header_signature
s3StreamBaseInit
The numeric value of the format specifier is too large
std::unique_ptr<DiskImage> diskimage_uio::details::diskimage_open_params_impl::transfer_disk_image_ownership()
 opened and replaced at attempt 
ASIF: data entry - invalid reserved bits
Stack with cache as top image cannot be opened for writing.
\\\"
band_ptr DiskImageSparseBundle::find_band_in_array(uint64_t)
 = offset = 
Invalid key size
File descriptor 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
The format string terminates at a '{'
Replaced an empty slot
oauth-id-token:
Backend barrier failed after dir offset changed, error 
DiskImageUDIFWritable: got a flush with error, aborting
auto hdr_get_nr_blocks(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
174350
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603
Could not stat shadow file
unmapped
ASIF: can't copy metadata to mutable copy
basename_r failed
Can't read custom encryption entry header, error 
wrapped-key
Failed to add public key entry to auth table
attempting to authenticate with saks
, Force closing.
fetch_restore_key/%s OS/%@
diParams
com.apple.knox.url
void convert(DiskImage::const_extents_iterator_t, DiskImage::const_extents_iterator_t, DiskImage &, DiskImage &, const std::function<void (int64_t)> &, bool *)
futimes failed on 
Compression Type
/System/Library/PrivateFrameworks/DiskImages2.framework
ASIF Info
Band data doesn't exist, zeroing
com.apple.diskimages.band_management
+[DiskImageParamsXPC newWithURL:fileOpenFlags:error:]
readSynchronizer
crypto_mode
Close completed
Can't read UDIF trailer
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
secondaryKey
fsync
read only
Invalid size of saks response %lu
boost::icl::interval_set<uint64_t> MediaInfo::process_mapped_data(uint64_t, uint64_t)
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
-r
sha1 too many bytes
Cannot edit crypto header that has more than 
com.apple.internal.fetchrestorekeys
outputParams
Write error: 
shadowStats
Dir Pointer Version
blkx
Invalid media block size
-[AAS3DownloadRequest createAndResumeTask]
, disk image is terminated
Failed to create disk image
-[FileLocalXPC sandboxExtensionTokenWithError:]
, keeping file unlocked
IOBlockStorageDriver
Failed to convert SLA text to C string
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
Failed writing sparsebundle info
Shadow path %@ is not a valid file
Error during ASIF flush: 
shared
Incorrect passphrase
Diskimageuio: get block size failed 
-
CFAutoRelease<CFDictionaryRef> udif::details::UDIF_base::get_resources() const
Content-Type
Write zeros to unmap unaligned end region failed (err code
remote mount
, error 
Media Block Size
Failed converting CFNumber to long
Using compression 
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
enqueueRequest
encryption
Unsupported key decryption algo
Record On Bits
Checksum Value
Cannot change passphrase of unencrypted image
Bands folder contains an out of range band (
Failed during ASIF extents enumeration.
 while expecting 
commandSize
void boost::uuids::detail::sha1::process_byte(unsigned char)
Invalid plugin URL, plugin name is missing
User data is not supported in this image format
Failed to allocate raw blob data
a pointer
https://%@/v1/ac/decrypt
PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0
-[DIConvertParams onConvertCompletionWithInError:outError:]
dev
Failed to write metadata header
int crypto::crypt_op::crypt_consecutive_vector::operator()()
free = 0, full = 1, map_info = 2
--oauth-grant-type
Extent 
Asif header too large
ASIF: Block size isn't a multiple of 512
Attributes
fchownat failed for 
OK
maxRawUDIFRunSize
Skipping band erase (in use)
Unexpected backend type for shadow file
Does not contain an \"even number\" of hex digits.
\\'
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = udif::header]
rawTestPlugin_t::~rawTestPlugin_t()
Image
fetch_restore_keys_key_handling.m
void SparseBundleBackend::write_primary_info_plist()
AAS3DownloadStream (NSURLSession)\n
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_read(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
-C
Failed creating the image
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
-[DIDeviceHandle waitForQuietWithService:error:]
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_write(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
Resetting 
Failed barrier after writing full dir
virtual FileDescriptorWrapper::~FileDescriptorWrapper()
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
-[DIConvertParams prepareConvertWithError:]
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
emulateExternalDisk
lock
Bakcend not initialized for file
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c
IOBlockStorageDevice
UDIFDiskImage: failed truncating image
BLX
lock_backend
UDSB
DiskImageConvert
Diskimageuio: get nr blocks failed 
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
, truncating
wkms
DIControllerServiceQueue
Identity Info
Read error: 
Cannot find disk image with reg entry ID 0x%llx
Failed reading 
invalid field %u
+[DISLAFrontend(Private) displaySLAText:error:]
Diskimageuio: Snapshot detected on top of cache
Plugin 
dirty = bit(0)
Failed opening the file
int di_asif::details::table::close()
assetAttr
Cannot find BSD name in IO media service
Error: Not enough data read. expected: 
, trimmed size
 
read
MediaInfo::MediaInfo(DiskImage &)
Couldn't exclusively lock entry 
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)_block_invoke
void rawTestPlugin_t::subscriber_t::_resume()
Cache
Type
Start Offset
header_ignore_fields_t
devicePrivateKey
managed
Non supported options in AAS3DownloadSession (ignored): proxy_headers %s
Diskimageuio: can't get lock status 
special: 
BufferedWriteBackend doesn't support per io crypto
Can't get geometry values from MediaKit
lifs
sendEvent of type 
Couldn't open file with flags 
suppressSsdFlags
backend
-[DIImageHandle resizeToSize:error:]
get path failed
pthread_once
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
int di_asif::details::dir::defrag_table(ContextASIF &, dir_idx_t)
-[DiskImageGraph initWithBaseImageURL:tag:error:]
] = 
(
com.apple.di_raw_test_plugin
 closed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__memory/unique_ptr.h:
Failed converting URL to UTF8
Image contains crypto format but info class is missing EncryptionInfo
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = std::__bind<io_result_t (DiskImage::*)(DiskImage::Context &, const sg_entry &), DiskImage *, std::reference_wrapper<DiskImag
XPC connection interrupted
, disk size: 
Full Entries
Metadata corrupted 
fstatfs failed
) and dest disk image (
virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()
Failed creating CFData
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
Diskimageuio: can't get Diskimage attribute, unknown header format
Invalid knox URL format. Expected: knox://host/download/space/digest
bitmap flag value invalid
YES
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
Starting flush
gcd::gcd_timer_source::gcd_timer_source(gcd_queue &, dispatch_time_t, uint64_t, uint64_t)
-[DIUserDataParams retrieveWithError:]
UDIF header changed while unlocked
crypto header contains invalid number of auth entries
keys/fetch
Cannot attach RAM disk with a shadow or a cache file
Failed to create XPC connection object
Image does not have write permissions
locally mounted from %@
-[DIShadowChain openWritable:createNonExisting:]_block_invoke
DI Conversion Queue
tmp_convert
v24@?0@\"NSDictionary\"8@\"NSError\"16
 is closed, notifying waiters
uat
Couldn't parse scheme id
Max Size Bytes
The image is encrypted but has no passphrase auth entry
Skipping erase of 
clientID
UDIF XML length 
UDIF: Can't get resource array
Crypto operation on data of 
+[AAS3DownloadSession completeRequest:data:response:error:]
vector
udzo
thread constructor failed
diskimagesuio: future read invalid in read
Can't read encryption table, error 
Error with decryption key size
int plugin_decode_fd(void *, const char *)
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)_block_invoke
virtual int Ram::_write(const sg_entry &)
Geometry
Primary GPT Table
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
Missed an evictable slot
AES-XTS
Plugin image struct size 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Harde
Barrier
solid state
Unable to get IOMedia preferred block size
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
enc-request
 bytes
application/octet-stream
exclusive
] 
com.apple.MobileAsset.AssetType
Partitions
%@[%@, %@]
UDIF read-only compressed image
UDIF uncompressed read-only image
ssize_t plugin_decode_buffer(void *, const char *, void **)
which is larger than allowed 
Error writing file @ 
-[DIController2IO_XPCHandlerAttach disconnectFromDriverWithError:]
%s: 
A mandatory argument is null in a DiskImages2 API call. Remember to check if init succeeded
Can't take exclusive lock on entry
Failed to replace passphrase entry in auth table
Diskimageuio: bottom diskimage should have role image, but 
fstat failed
com.apple.DiskImages2
Destination image format is unknown
 failed with 
 ret: 
Conversion: unmap error 
Cannot find image with provided uuid.
diskimage_uio::details::diskimage_impl::diskimage_impl(diskimage_open_params &&)
Couldn't upgrade lock entry 
Not allowed more than one instance of 
Invalid value for argument 'block-size'
Udif: needs to read 
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
unique_lock::unlock: not locked
Content-Type:
Disk image is terminated, skipping future_flush
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433:
' opened successfully with flags 
\\u{
Diskimageuio: Can't stack non asif formats. Got 
Failed to erase mapped file of band 
bla
Invalid value for UDIF header field: %s
diskimagesiod
virtual int FileLocalAsync::disable_file_zero_padding() const
flushing and closing 
int sparse_bundles::mapped_blocks_t::flush()
encryption_key
char *udif::details::plst::write(char *)
^v8@?0
void udif::details::UDIF_base::print_checksum_verification_status(const std::string &, const csum_any &, const details::checksum &) const
curl_easy_init failed\n
-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]
-t
Key is not hexadecimal number.
virtual int FileLocalAsync::_write(const sg_entry &)
Cannot initialize pstack disk image without path.
Failed to add symmetric key entry to auth table
Max sector count is too large
int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
ERROR: shipping key wrapped-key failed base64 decode
Invalid chunk size
Metadata offset is invalid
BackendNull
Transfer-Encoding:
Range:
creating session
IOBlockStorageDriver device not found in registry iteration
Cannot convert this image in-place, as it contains unordered UDIF runs
+[DIError errorWithDomain:code:description:verboseInfo:error:]
Length
Name
-[DIBaseXPCHandler completeCommandWithError:]
sparseimage format is not supported by DiskImages2 framework
Trying to write @ 
Completed erase of band 
Error creating disk image params
 checksum: 
bzip2
 - map_range: [
virtual int CompressedBackend::write(const sg_entry &)
Flushing 
download
Failed initializing RAM disk buffers
-[AAS3DownloadSession syncRequests]
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
The argument index should end with a ':' or a '}'
invalid uuid string
oauth
IOMedia
downloadStreamPRead
Failed to find IO media entry for %@
-[AAS3DownloadSession addRequest:]
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
inputURL
bool ref::details::ctrl_blk<di_asif::details::table, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::table, tag_t = unsigned long long]
 is now available
Unexpected materialized_diskimage in create_diskimage_from_hdr
Invalid field found in shadow file header: 
Failed to create resizer
udzo_max
knox-uat.sd.apple.com
Failed creating IO iterator, err code %d
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
encryption: header size mismatch
DIDevicePermissions calculateDevicePermissions(DIAttachParams *__strong, kDIInterconnectLocation)
xpcEndpoint
Cannot store an empty passphrase
missing DI_ATTACH_ENTITLEMENT on non macos platform
RSA = 42
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ H
Couldn't read sparseimage header
crypto
com.apple.diskimages.file.crypto
Diskimageuio: images with constraints currently not supported
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:128:22)]
, UID:GID(Name)=
Disk image is terminated, skipping flush of 
Key is not 32 bytes size.
Can't read bitmap
DiskImageUDIFWritable: Sink backend returned 
static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)
Physical block_size is 
> %d %s\n
Passphrases doesn't match
Failed opening the image with RW access
.xpc
Diskimageuio: unsupported disk image type for get_backend
attempting to authenticate with aea key
saksKey
DiskImageUDIFWritable: context backend returned 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_fo
plst
Cannot find image with provided UUID.
%@[%@]
-[DIBaseParams prepareImageWithXpcHandler:fileMode:error:]
Cannot stat 
shadow
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::set_path(const std::filesystem::path &, const diskimage_open_params::mode)
Updating 
 band contexts
-[DIController2ClientDelegate attachCompletedWithHandle:reply:]
Cleaning up!
Zero padding cannot be disabled from this process (res=
Trying to read @ 
partition offset
SHA1_HMAC = 91, NONE = 0
Raw header changed while unlocked
virtual io_result_t sparse_bundles::Band::write(DiskImage::Context &, const sg_entry &)
Invalid user data content
block_attributes
, but file size only 
Malformed URL format
Failed locking the image
Unexpected failure to get image info: 
Diskimageuio: path 
: 
encryption_mode
 of type 
Reading 
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
File (fd 
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const
User-Agent
a character
}
Not valid SAKS metadata (no environment field)
void plugin_encode_fd(void *, const char *, int)
com.apple.wkms.url
Metadata
Diskimageuio: UDIF header changed while unlocked
s3DownloadStreamOpen_curl
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c
ulfo
Diskimageuio: Nested stacking is not allowed.
Diskimageuio: can't get file descriptor, backend doesn't exist
void SparseBundleBackend::write_info_plists()
Unexpected ASIF header length (
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = di_asif::header]
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
iokit error
com.apple.diskimage-test-plugin.raw
 requested while there are only 
 doesn't exist, returning zeros
Tag
locale-specific form
Authorization
, errno 
Failed to serialize public key entry to crypto header
pstack: unsupported node
uri
fd block size retrieval failed (err code 
Unsupported ASIF, contains data beyond current header struct size
UDIF: Can't get types array from UDIF
Not a pstack.
]
int sparse_bundles::Band::flush()
diskimage_
invalid bits range 
Flush failed after defrag, ignoring. Error 
ASIF: failed to deserialize metadata
header_size_512 = 512, header_size_4k = 4096
getErrorContextKey
user data retrieving failed
. Opening as root
saks-ac-prod.g.apple.com
 completely
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
https
Invalid raw UDIF run size limit
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
Band data is partial, reading 
 bands flushed, calling 
shouldValidate
 failed, error 
public_key_padding_algo
 ret = 
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
Write zeros to unmap region failed (err code
End of input while parsing an argument index
No
-[DIStatFS initWithFileDescriptor:error:]
 doesn't exist
Table flush failed during dir flush: 
/s3/aws4_request\n
addRequest
crypto_header
void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)
void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/crypto/crypto_format.cp
POST
Cannot display SLA: no terminal or stderr to write to
!\"
 (band 
Destructing sb context
diskimageuio: pre-write first error 
 size = 
com.apple.diskimagesiod.ram
 is not registered
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
PKCS5_PBKDF2 = 103
 folder
The specified image is a folder but not a sparsebundle
Can't load table to get extents
Stable UUID
 / 
Bearer openid-id-token-%@
 directly (without list)
virtual int DiskImageSparseBundle::set_size_impl(uint64_t)
) to type
-[DIEncryptionFrontend unlockWithPassphrase:error:]
-[DIController2IO_XPCHandlerAttach createDeviceWithError:]
regEntryID
Passphrase is too long
is_aea: Error reading magic.
V2 = 2
a floating-point
Unsupported URL scheme
identifier
UDZOMAX
disk image
Bit 
bytes=
Failed to read auth table
band-size
Clone of plugin nodes is not supported.
Disk image is terminated, skipping flush
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
GUI SLA handling required
pstack_header
Diskimageuio: Couldn't lock backend 
wkms.sd.apple.com
Conversion: read error 
Failed to parse key in KVS (zero size data).
 [
Failed to open crypto header
asif
Can't connect to device
virtual int SparseBundleBackend::truncate(uint64_t)
 auth entry
 bytes is smaller than its trailer
uint32_t FileDescriptor::fetch_physical_block_size() const
Bitmapped Entries
failed to set the bundle's size
len: 
Accept
Couldn't create MediaKit subrange object
s3Sign
%12u max attempts for a request\n
expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_image_header(size_t)
: flush in destructor failed (
prod
-[DIDeviceHandle dealloc]
Passphrase cannot be empty
flush
\n
Diskimageuio: Couldn't get locked status 
knox-dev.sd.apple.com
Request failed with HTTP error: %lu %@: %@\n%@
NSURLSession read to buffer nbyte=%zx offset=%llx\n
Failed creating sparsebundle folder
tkn
1
disk image password
Zero padding disabled successfully on fd 
ERROR: enc-request failed base64 decode
Backup GPT Header
-[SparseBundleBackendXPC getCryptoHeaderBackend]
io_result_t di_asif::details::dir_base::move_realloc_chunk(ContextASIF &, char *, size_t, uint64_t)
BackendZero
supportsBarrier
Failed to set up image for resize after creation
virtual int BackendSG::truncate(uint64_t)
Flush failed. BackendSG = 
crypt_consecutive_vector: write check errors 
, fd=
Failed getting runloop source
APPLECONNECT.APPLE.COM
Block device block size is larger than image block size
(locked)
ERROR: Shipping private key is NULL.
dataTaskWithRequest
Could not get media info
/dev/tty
not 
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
Error with resolving knox url
Read returned an error
 for 
file
The fill option contains an invalid value
certificate
Range: bytes=%llu-%llu
Unsupported ASIF version 
End of input while parsing format specifier precision
+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
Failed to setup the plugin's IO ring
 while expected is 
raw
encryptionMethod
Can't load bitmap from backend
generating for blkx 
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
More than one image in the stack has the provided tag, please specify UUID instead.
Disk image is terminated, skipping write
 status: 
com.apple.diskimages.attach
X-Amz-Content-Sha256: %s
Failed opening the shadow/cache file(s)
Bundle's lock file is closed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682
Can't write UDIF header
ZLIB = 0, LZFSE = 1, LZMA = 2, ZLIB_9 = 3, BZIP = 4
blockSize
com.apple.diskimage.sparsebundle
ASIF block size isn't multiple of 512
stable uuid
DiskImage::diskimage_extent_t DiskImage::const_extents_iterator_t::make_val() const
Crypto: can't read crypto header
Image doesn't support resizing
 bytes are above the sparsebundle limit of 
UDIF: Can't read UDIF trailer
wrap_key_crypto_padding_algo
crypto_format: blob length differs
Verify
tr '\\r' '\\n' | fmt | ${PAGER:-more}
Corrupted ASIF image.
map_element flush failed on creation
Failed to create crypto serializer
UUID
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
di_plugin_image_t *PluginsManager::decode_plugin_image(const di_plugin_t &, const diskimage_decode_fn_t &, void *)
io_result_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
Unexpected image format from info: 
AEA key retrieval failed
%@[ramsize=%llu]
algorithm_type
Compression Ratio
Failed to set up image for resize
 updated from 
barrier
unsigned char boost::algorithm::detail::hex_char_to_int(T) [T = char]
IO error with sg: 
auto sparse_bundles::Band::get_mapped_blocks()::(anonymous class)::operator()() const
Opening mapped blocks for 
metadata_read_only_flags
plugin://%@
Failed to serialize passphrase to crypto header
 read: 
Master checksum
Unable to create ioreg iterator
Size
-[DIController2IO_XPCHandlerAttach launchIODaemonWithError:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
Invalid UDIF, run is not within block boundary
Error decrypting data using public key, error code 
In-place conversion maintains the encryption passphrase and method. It's not allowed to specify encryption arguments
Data Fork
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_t
com.apple.DiskImages2.TelemetryManager
virtual int DiskImageSparseBundle::flush(DiskImage::Context &, di_flush_mode)
 (our euid is 
static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Starting unmap of 
deserializationError
BackendPlugin
virtual io_result_t DiskImageUDIFRead<UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>, std::integral_constant<bool, false>>::read(DiskImage::Con
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
Flushed 
Failed to add passphrase entry to auth table
RW
Plugin version 
Unexpected error creating (unlocked) backend
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)
Cannot load libTestPlugin
Shadow underlying FS
 trying to check permission after EACCES
com.apple.diskimagesiod
blocks_signature
Yes
-[DIResizeParams resizeWithError:]
 but buffer is too small 
 block_size: 
 is 
Diskimageuio: Can't create stackable image: 
No mapped file for band 
encodedDict
char *udif::header::write(char *)
IV_TWEAK_SIZE_16 = 16
-o
Failed to open backend of crypto header
Disk image verification failed
-[DIConvertParams copyUpdatedOutputURLWithError:]
Diskimageuio: Unrecognized image format.
Could not parse OIDC token from AppleConnect output
v32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
KVS data fetch failure.
-[DIConvertParams shouldPerformInplaceSquash]
Couldn't convert CFStringRef to a proper std string
Cannot retrieve passphrase from user via TTY or GUI
Unexpected backend type for file
uuid
Not valid SAKS metadata (json format expected)
[empty]
managed future err 
 given
Parent UUID
Diskimageuio: Required read-write disk image (
void rawTestPlugin_t::subscriber_t::_cancel()
CKIE
-[DIBaseAgentDelegate createListener]
Failed to validate metadata 
Missing Expected AUTH DATA in AEA.
Failed to encrypt data using public key from certificate
Format Description
Failed serializing user dictionary
AmberDiskImagePluginCreate
plst: count = 
Empty Bytes
-[DIBaseXPCHandler installConnectionLostHandlers]_block_invoke
Plugin bug: returned init failure without supplying the error
void rawTestPlugin_t::subscriber_t::_suspend()
Sandbox extension token exceeds maximum size
%02x
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
Bearer %@
 mode=
DiskImageUDIFWritable: aborting
, errno=
Crypto: Unsupported encryption parameters
int BufferedWriteBackend::reset_last_offset(const sg_entry &)
virtual int BufferedWriteBackend::write(const sg_entry &)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Sparsebundles on SMB mounts are not supported on this system
Band was evicted by another thread, retry erase process
Resource name is too long to fit uint32_t
 offset = 
http
ParentUUID
bytes=%llu-%llu
Compressed Length
Opened bundle's lock file with flags 0x
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
Context creation failed.
Unsupported public key algorithm.
Crypto couldn't read from inner backend @ 
Sparse bundle image
Unexpected context construction by 
Barrier failed before dir flush
Failed to find DiskImages2 controller, driver might not be installed
int main(int, const char **)
config_t
Sections
 is different than current mode 
couldn't allocate space for entry 
metadata_flags_t
image_variant_type
AEA
Failed to read file for pstack parsing
Failed to quarantine device, error=0x%x
The format string contains an invalid escape sequence
Cannot find AmberDiskImagePluginCreate in libAmber
Backend barrier failed during dir flush, error 
crypt_consecutive_vector: check errors_in read futures 
path
We're out of ctxs for async execute
ASIF: missing internal metadata key
 or exceeds size_t size 
Origin
curl_slist_append failed\n
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
can't get Diskimage attribute, unknown header format
-[DIControllerServiceConnection checkAttachEntitlementWithError:]
Replacement argument isn't a standard signed or unsigned integer type
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
 returned status 
virtual int CompressedBackend::read(const sg_entry &)
Chunk Size
Can't load bitmap while setting range
format_type
Characteristics
 option
auto
 (errno 
Writing 
static void sparse_bundles::Band::erase(const bundle_commons_t &, uint64_t)
Unknown checksum found
, required decompression buffer size: 
Couldn't get runs array from Media Kit
unexpected error
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
static std::string FileDescriptorWrapper::handle_open_from_error_message(int, const std::string &, int, int)
 was just created (truncated)
ERROR: This archive does not contain a shipping key response.
Band was evicted by another thread (during retain attempt), retry erase process
Trimming: Written 
MBR
Primary GPT Header
virtual int Backend::read(const elements_t &)
 instead
di_plugin_image_t *PluginsManager::create_plugin_image(const di_plugin_t &, int, const CFDictionaryRef)
Missing key in KKMS response
fully
 bytes)
i
%s\n
Encryption Method
The argument index starts with an invalid character
Persistent attach is not supported for this disk image type
Diskimageuio: backend doesn't exist
environment
Failed creating CFAutoRelease instance.
Unaligned metadata entry size
s3Perform retry after %u ms
://
UDZO
xpc error
Locked encrypted image
crypto_op: can't initializae aes_xts context
Raw run size limit cannot be smaller than compressed run size limit
 while writing 
Key Size
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_unmap(const unmap_extent_t *, size_t, future_io_opts_t)
statInstanceID
fstatfs failed with err code 
virtual int FileLocalAsync::_read(const sg_entry &)
inputStatFS
Diskimageuio: get parent uuid failed 
Disk image is terminated, skipping future_unmap
Run interval: 
UDIF header doesn't contain a valid sector count, using runs upper value: 
fetch_restore_keys self signed cert
AWS4-HMAC-SHA256 Credential=
static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)
corrupted image
daw
Unknown
Error creating (unlocked) backend
-[RamXPC createRamBackend]
Got error when trying to close 
 exceeds the maximum of 
could not create iterator (begin)
New disk image
unique_ptr<lock_free::bitmap_t> SparseBundleBackend::get_existing_bands() const
ASIF meta header failed to read
In-place conversion to this image format is not supported
Backend: failed writing element in vector
Medium Type
, band was written to
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
 -> 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692
Root dir flush failed, error 
IOServiceClose failed. error=0x%x
Failed to create graph from plist.
io_result_t DiskImage::Context::read(const sg_vec::iterator &, const sg_vec::iterator &)
-[AAS3DownloadSession readToBuffer:size:atOffset:]
 constant 
Unexpected backend replace request
Failed to issue sandbox extension token for file
UDIF_header::UDIF_header(const std::shared_ptr<Backend> &)
fetch_restore_keys_ephemeral
Can't parse disk image with MediaKit. No partition scheme or partition scheme not supported by MediaKit
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Band 
auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:
static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Password
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
virtual int FileLocalAsync::truncate(uint64_t)
sg: 
User declined SLA
virtual size_t BZIPCompressedBackend::compress(const sg_entry &) const
(err code %d)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ H
Allocated after defrag: 
createErrorContextKey
onDiskCache
Failed creating bands folder
1.0
The URL encoded into the AEA authdata is missing or invalid.
Request timed out
infnanINFNAN
Opening band 
Conversion started
 rather than image
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
flags_t
Resumed
Failed to create kqueue
conversionMethod
Single element in pstack that isn't an image
Failed opening folder for entries reading
plist
checksum_type
Flush failed. Backend = 
Not A Ninja/1.0
none = 0, crc28 = 1, crc32 = 2, dc42 = 3, md5 = 4, sha = 5, sha1 = 6, sha256 = 7, sha384 = 8, sha512 = 9, none_valid = 10
size
int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)
static int SparseBundleBackend::open_bundle(const string &, int)
 failed wih error 
Device Characteristics
size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)
Failed to get data from self signed certificate
Can't create MediaKitRef
ULFO
-n
Error opening ByteStream
XPC connection invalidated
Corrupted plist
Unmapped Entries
Couldn't read asif's header
(empty)
Maximum Transfer Sector Count
The precision option does not contain a value or an argument index
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
RAW read-write image
void DiskImage::do_terminate()
UDRO
Can't load bitmap while flushing asif table 
Failed to increase file size, pwrite returned 
Calling 
v8@?0
-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]
Invalid encryption method
AEAHelper: Invalid file descriptor.
num of runs 
udro
virtual lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImageRaw::future_write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:437:
ASIF meta header trailer isn't equal to zero
Error reading file @ 
Master Checksum Info
RAW
No WKMS key source available in AEA metadata
UDIF: Can't create dictionary resource fork
Punch hole is not supported (err code 
PluginName
US
Can't get section values from dictionary
flags validator
 changed before retain completed
Failed to generate self signed certificate
Image info is not supported for the given image type
fchmodat failed for 
 errno: 
Error duplicating stderr
s3HeaderAppend
HTTP %u\n
Diskimageuio: Single element in pstack that isn't an image
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Harde
void DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::transform_i
KEY_BITS_160 = 160, KEY_BITS_NONE = 0
Failed to update crypto header
set size failed
Unsupported block size for image format
auth-data
s3StringBufferAppend
Checksum Type
Cancel
-[DIBaseXPCHandler createConnection]
virtual int SparseBundleBackend::unlock_all()
The requested URL is an existing folder
(unlocked)
AppleDiskImagesController
Sector Count
Is Cache
Duplicate shadow values for: %@
) is unlocked
The replacement field misses a terminating '}'
virtual FileLocalAsync::~FileLocalAsync()
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:113:22)]
Diskimageuio: Invalid pstack element: 
Unexpected unmap command received on read only image
The type option contains an invalid value for a string formatting argument
Cache is not supported when using pstack.
header (
device with registry entry ID 0x
. returned 
Runs
The operation was cancelled by the user
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
public_key_crypto_algo
 not found in registry
Output of disk image conversion must be a file
system error
Block size mismatch in DiskImageStackable
 to 
SLA text is empty
Internal backend read() failed. ret=
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
6.0
Terminating due to unrecoverable I/O error
Re-enter new password: 
The disk image is corrupted
Failed to get plugin instance
%@%@.%@
io_result_t di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
Conversion: write error 
Couldn't open 
-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]
Invalid value for asif header field: %s
fileBackend
Role
has_bitmap
s3HeaderAppendWithFormat
ramTestPluginCreate
Corrupted plist dictionary
set_euid_wrapper::~set_euid_wrapper()
com.apple.diskimages.band_unmap
key_derivation_prng_algorithm_t
-[DIConvertManager convertUserDataWithDiskImage:destination:]
PUT
Failed to read from certificate file 
CFUserNotificationCreate failed, error code %d
bool ref::details::ctrl_blk<di_asif::details::map_element, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::map_element, tag_t = unsigned long long]
 length 
disk arbitration framework returned an error
Size cannot exceed max ASIF size
attempting to authenticate with wkms
Couldn't upgrade lock entry
iCloud
+[BackendXPC newFileBackendWithURL:fileOpenFlags:error:]
Failed to get parent registry entry, err code %d
Failed to create public key auth entry
Failed to update internal state after resize
-[BackendXPC tryCreatingCryptoHeader]
File system is 
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
virtual DiskImageSparseBundle::~DiskImageSparseBundle()
virtual DiskImageSparseBundle::ContextSparseBundle::~ContextSparseBundle()
void info::DiskImageInfoASIF::examine_mapped_extents(const DiskImageASIF &)
ASIF: can't set requested uuid
high throughput
%@: %s
Legacy shadow file format is not supported by DiskImages2 framework
com.apple.wkms.auth-data
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
Is Encrypted
Failed opening the shadow/cache file(s) with RW access
0x
mapped
/usr/local/bin/appleconnect
Uninitialized Entries
status
precision
The value of the argument index exceeds its maximum value
Solid State
The requested URL is an existing non-sparsebundle folder
, allocated: 
Can't flush asif table, bitmap flush failed 
uint64_t udif::details::UDIF_base::write_resources(CFDictionaryRef)
+[DICreateParams eraseIfExistingWithURL:error:]
 has size 
Cannot delete base image node.
CBCPADIV8 = 6
prng_algorithm_type
 formatting argument
token
NONE = 0
Couldn't parse scheme name
KVS key value - parse failure.
supportsPersistentAttach
decryption-components
+[DiskImageParamsXPC validateSupportedFormatWithBackendXPC:error:]
 with ret 
 is clean, skipping flush
-[DIControllerServiceConnection dupWithStderrHandle:reply:]
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
Diskimageuio: resolved disk image format 
Mandatory callbacks in the plugin's image struct are missing
RootDeviceEntryID
PluginParams
Custom cache or shadow is not supported for pstack based images.
Cannot stack images with different block sizes
Missing key in Knox response
Can't flush asif on table flush, backend barrier failed
Can't write UDIF resource part
Couldn't parse 
failed instantiating the diskimage object
SparseBundleBackend::SparseBundleBackend(int, bool, const shared_ptr<FileLocal> &, const shared_ptr<crypto::format> &)
virtual io_result_t sparse_bundles::Band::read(DiskImage::Context &, const sg_entry &)
Missing OIDC client ID in appinfo response
Could not determine cache dir
 bytes does not fit before the 
Image key encoding failed with err code 
Failed to use the passphrase that was given
 at index 
Preferred Block Size
, size 
userData
Convert AEA key from hex failed
band_ptr DiskImageSparseBundle::replace_oldest_band(Band *)
[
virtual int FileLocalAsync::lock()
AES = 0x80000001
Invalid URL
v16@?0@\"NSString\"8
 is incompatible with the framework, expected at least 
Backup GPT Table
Create device call failed, error=0x%x
user data embedding failed
com.apple.DiskImages2.ASIF.sparsity
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293
Shadow
UDIF_header
Invalid resource key
attributes
Destination folder URL must be of 'file' scheme.
Key from the certificate is not exportable
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
/dev/disk
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
Failed locking the shadow file
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
encKeys
asif: chunk size is too small, too many dir indices
Cannot find image with provided tag.
Invalid size hex key %lu
is_writable
Couldn't read asif's full header
 - unmap_range: [
Apple Inc
AWS4-HMAC-SHA256\n
unmap_iterator_t di_asif::details::table::unmap(ContextASIF &, const unmap_extent_t *, size_t)
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
Failed to subscribe to the plugin's IO ring
 overrun events occurred in the plugin's ring!
run offset
section offset
Accept: application/xml
publicKey
Unmap done
kern_return_t was 
'
verify failed
 was opened in the background, waiting for it to become available
device not found in registry
Diskimageuio: Multiple images given but block size differ. 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Barrier failed after defrag, error 
run_type
>
void sparse_bundles::Band::ContextsList::clear()
Unexpected UDIF header length (
Images Count
Can't write initial table data
AppleDiskImageDevice
 on 
+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]
Can't get scheme values from dictionary
-[DIController2IO_XPCHandlerAttach updateQuarantineFlagWithHandlerArray:flags:buffer:error:]
NSURLSession read to stream nbyte=%zx offset=%llx\n
bool di_asif::details::table_entry_data::validate() const
could not create iterator (end)
&
Image referenced in the pstack is unreachable.
virtual di_coroutines::Task<void> CompressedBackend::run_futures()
instanceID
ASIF: Content dirty bit is set when reading from disk
Cannot acquire 
identityCertificates && [identityCertificates count] >= 1
Diskimageuio: backend isn't locked
wkms-uat.sd.apple.com
gcd_kqueue: kevent64 failed with ENOMEM
static int FileDescriptorWrapper::open_file(const std::string &, int)
virtual sparse_bundles::Band::~Band()
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)
: [
Constructing sb context
KVS keyBuffer allocation failure.
Disk image operation failed with error code %d
Unsupported disk image format
ReadOnlyBackend
dealloc_queue
typename boost::enable_if<boost::is_integral<typename hex_iterator_traits<OutputIterator>::value_type>, OutputIterator>::type boost::algorithm::detail::decode_one(InputIterator &, InputIterator, OutputIterator, EndPred) [InputIterator = std
01234567
failed to open existing output file
-[DIBaseXPCHandler init]
saks-ac-uat.g.apple.com
-[DIShadowChain addShadowNodes:wrapReadOnly:error:]
field size too large
> real: <
user metadata
x-amz-
sig1_t
\\\\
getToken
Segmented UDIF images are not supported by this framework
PKCS7 = 7
Content-Length: %zd
-[DICreateParams createDiskImageParamsWithError:]
table flush failed during close: 
Crypto data block size: 
slaText
Request creation
kern.aioprocmax
Overflow detected
partition_num: 
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)
void info::DiskImageInfoASIF::count_used_extents(const DiskImageASIF &)
UDBZ
Bad or missing key in SAKS response.
io_result_inserter_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::data_entries_vectorizer_t::add_data_entry(const data_entry_t &)
Failed converting CFNumber to longlong
{:02x}{:02x}
ASIF: Header size is less than the min header size
hybrid_queue
Timeout waiting for a completion of an ongoing eject
Reserved
Cannot decode file descriptor
 marked as purgeable
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
com.apple.diskimages.sla-prompt
ASIF: No data offset found (write)
ASIF max_write size in header exceed the limit
Total Bytes
Image Format
ulmo
expected<int, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_file_descriptor() const
Blocks header
bool sparse_bundles::mapped_blocks_t::load_file()
int PluginsManager::register_plugin(const string &, di_plugin_t *)
com.apple.diskimages.aio
 - different calculated: <
Compressed Bytes
public key has an encoding issue or uses an unsupported algorithm
 is incompatible with the framework, expected 
ASIF meta header is unaligned
value validator
trailer of a 
Couldn't parse media block size
%12llu bytes downloaded (%.2f MB)\n
, flags = 
Can't flush asif table, backend barrier failed
Failed truncating 
DiskImageSparseBundle::ContextSparseBundle::ContextSparseBundle(DiskImageSparseBundle &)
Invalid negative partition size of offset
Band size in sparse is zero
ASIF: failed to write metadata
/s3/aws4_request,SignedHeaders=
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
Couldn't trim entry in write 
crypto_format: Can't decrypt wrapped key 
Contains non-hexadecimal characters.
Couldn't get mapped sectors for [offset: 
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
, 
location
knox
Block size mismatch between source (
Cannot save DiskImageGraph without specifying pstack URL
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/disk_im
bool sparse_bundles::open_bands_t::insert(uint64_t)
-[DIAttachParams reOpenIfWritableWithError:]
source uuid
crc32 {
udsb
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
ActiveNode
invalid file size for 
Diskimageuio: No diskimage given
Cannot decode path
This operation doesn't support pstack files
bundle_handle
ULMO
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = di_hybrid_subscriber_t]
com.apple.diskimagesiod.spb
not a disk image
Base
disk image kernel return
] from MediaKit - errno 
https://%@/westgate/appinfo
void plugin_encode_buffer(void *, const char *, const void *, size_t)
IsCache
Include all
-I
No room to add new auth entry
invalid value
UDIF images are currently not supported in diskimage_uio
 lock, errno 
Disk image is terminated, skipping unmap
segment_count_t
 logical: 
<
Error creating backendXPC
segment_num_none = 0, segment_num_one = 1
void di_hybrid_subscriber_t::resume()
 buffer_size = 
Failed to read passphrase
Backend: failed reading element in vector
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
-[DIBaseServiceDelegate init]
com.apple.diskimages_cache_update
-[DIControllerServiceConnection init]
lzma
Failed to create passphrase auth entry
Failed to write asif header, error 
virtual io_result_t DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterato
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:429:
RO
Asif header size unaligned
Can't get key in cstring format
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Request failed: %03ld %s
a bool
The format specifier for 
Invalid public key: %s
Mode for new files in bundle: 
key
Can't load asif dir version
Unexpected crypto header length (
Can't read for defrag
Could not get mapping information
-[DIClient2IODaemonXPCHandler createConnection]
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__hash_table:1892: lib
Full dir write failed with 
none {
read write
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_flush(di_flush_mode, future_io_opts_t)
), reading from backup
virtual PurgeableFileBackend::~PurgeableFileBackend()
-[DIEncryptionChpass unlockWithPassphrase:error:]
void sparse_bundles::open_bands_t::remove(uint64_t)
virtual io_result_t DiskImageUDIFRead<UDIFReader<locks::None>, DiskImageUDIF>::read(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &) [UDIF = UDIFReader<locks::None>, UDIFVariant = DiskImageUDIF]
invalid length
singleInstanceDaemon
version
public_key_crypto_algo_mode
ERROR: wrapped-key failed base64 decode
-[DIUserDataParams encodeWithCoder:]
not a valid DER-encoded X.509 certificate
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
file(
The requested operation will delete the active node, please set another one first.
Partitions: 
v32@?0@\"DIDeviceHandle\"8@\"NSString\"16@\"NSError\"24
AAS3ContextCreate
 dest 
Looking for existing bands
v32@?0@\"NSURL\"8Q16^B24
iv_tweak_size_t
Using automatic argument numbering in manual argument numbering mode
Invalid format for shadow file
BackendSG: error allocating buffer
v16@?0@\"NSError\"8
, dirty=
pluginParams
Writable
useFormatMappingInfo
bool ref::details::ctrl_blk<CurrentReader, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = CurrentReader, tag_t = unsigned long long]
KEY_BITS_128 = 128, KEY_BITS_256 = 256
-[DIControllerServiceConnection cleanup]
curl_easy_setopt failed\n
shadowChain
io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c
Failed opening the sparsebundle as user 
Unsupported host for OIDC: %@
debugLogsEnabled
PstackVersion
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
None
\\t
Failed to create dispatch source for kqueue
Cannot get subscriber from plugin
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633
Apple sparse image
udif::details::UDIF_base::UDIF_base(UDIF_header &&)
/dev/%s
strdup
Compressed Offset
Integral value outside the range of the char type
Invalid output format argument
Can't flush asif on map element close, backend barrier failed
Backend is not mounted on APFS
Cannot increase size of a block device
Encryption Info
Diskimageuio: ASIF header changed while unlocked
virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
Failed to parse key in KVS (zero size key).
Input underlying FS
v32@?0@\"DIShadowNode\"8Q16^B24
Failed to parse auth data blob.
URL must have a file scheme
table entry map@
0B
Unexpected passphrase header length (
pstack
Registered plugin 
Legacy prepended-header UDIF image is not supported by this framework
void di_asif::details::table::set_entry_bitmap_range(ContextASIF &, data_entry_t &, const bits_range_t &, data_entry_t::flags, std::optional<data_entry_t::flags>)
udif::details::unique_buf UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::generate_blk(const interval_sectors &, struct block &, const descript
device_OBSOLETE = 0, device = 1, partition = 2
IOMedia device not found in registry iteration
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
baseBackend
com.apple.wkms.fcs-key-url
valid
s3Perform
Decompression failed
Requested write is out of range - offset 
openid,dsid,accountname
auto DiskImageSparseBundle::void_stackable_identifier()::(anonymous class)::operator()() const
type: 
flock returned errno 
 backend: 
Found 
virtual int FileLocalAsync::flush(di_flush_mode)
Can't read encryption entry header, error 
DI Verify Queue
Diskimageuio: locked backend 
Diskimageuio: query format failed 
virtual DiskImageSparseBundle::~DiskImageSparseBundle()_block_invoke
%12.2f initial interval between retries (s)\n
Cancelled
rings_queue
Invalid negative media block count
lzfse
-[DIStatFS logWithHeader:]
ShadowChain: %@
IOService
Error: failed to unwrap key. Error: %s\n
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
New password
attempting to authenticate with kms
User data contains reserved key(s)
Plugin's async ring cancelled, ret code 
, res=
invalid header: %s
alternate form
passphrase_header
 cannot be re-registered
plugin://%@/
Can't parse encryption entry: 
Min Size Bytes
expected<image_format, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::query_image_format() const
full_fsync
%12.2f MB/s download speed\n
The format specifier contains malformed Unicode characters
Internal backend write() failed. ret=
com.apple.diskimage-test-plugin.julio
plugin
Sparse bundle ejected
Destination folder URL must represent an existing folder.
 but buffer is full
Sector count is too large
BuildVersion
Disk image is terminated, skipping read
autoMount
DIErrorVerboseInfo
void SparseBundleBackend::read_info()
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486:
file_handle
ID
no_match
url
write
Failed barrier at start of dir flush, error
mapped blocks of band 
allowStoringInKeychain
inputMountedFrom
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
 is not supported (err code 
v32@?0@\"NSMutableDictionary\"8Q16^B24
get_next_capacity, allocator's max size reached
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
ERROR: shipping key enc-request failed base64 decode
Key transcoding failed.
\\r
Disk image is terminated, skipping future_write
stat failed
Cannot lock bundle, ignoring: 
+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
 header size 
s3DownloadStreamOpen_urlsession
Udif: advanced buffer, needs to read 
Could not generate daw token - AppleConnect Failure
uniqueDevice
-[DiskImageParamsXPC allowOnDiskCacheWithSinkDiskImage:]
 bits in the bitmap
io_result_t DiskImageSparseBundle::perform_io(ContextSparseBundle &, bool, const sg_entry &)
%@: %@
void di_hybrid_subscriber_t::cancel()
unmanaged
Failed to store the passphrase in the keychain
High Throughput Options
-[DIShadowChain topDiskImageNumBlocks]
Snapshot
File too small.
oidc
Can't write table for defrag
Backend barrier failed during bitmap allocator failures handling, error 
Unsupported value for crypto header field 
???
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:425:
truncate error: 
Invalid block size for image
virtual void DiskImageSparseBundle::on_eject()
Failed to mount filesystems
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_write_iov_t]
Validation failed, input contains unexpected data.
cert-chain
' with flags 
KVS dataBuffer allocation failure.
The format specifier should consume the input or end with a '}'
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
backend write failed during locked flush of map element, error 
gcd::gcd_kqueue::gcd_kqueue(gcd_queue &, std::function<void (struct kevent64_s *, int)>)_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ H
(unrecognized error)
numBlocks
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:172:22)]
Failed to retrieve info
uninit
gcd_kqueue: kevent64 returned error 
Write zeros to unmap unaligned start region failed (err code
Custom encryption entry header size exceeds max size
com.apple.di_stackable.cache.flusher
static autostart_task_t<process_entry_result_t> di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::process_write_entry::operator()(table &, ContextASIF &, table::data_entry_t &&, const sg_vec:
bytes, which is after end of ramdisk
FilePath
-[DIConvertManager runWithError:]
int di_asif::details::dir::handle_all_failures(ContextASIF &)
Failed writing first block of dir
crypto_format: Can't derive key 
CoreFoundation type mismatch: 
The disk image format is not supported by this OS
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669
nodes
ASIF: can't read/allocate asif metadata
 data: 
Diskimageuio: get stackable uuid failed 
Authentication Data creation failed.
Compression Info
Agree Y/N? 
File size is less than the minimum header size
Conversion: extents enumeration error 
Cannot find registry entry ID 0x%llx
Authorization: %s
StandardCompressedBackend::pimpl::pimpl(algo_t)
diskimageuio: report err 
, dest buffer_size 
Couldn't find partitions key
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
bundle-backingstore-version
HTTP request failed with status code: %ld
https://%@/spaces/%@/files/%@/decryption-components
Couldn't write asif's header
Read-only image cannot be resized
,
Diskimageuio: Failed to create resizer: 
Size is not a multiple of block size
diskimage-bundle-type
Failed to evict band to make room for 
int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)
header_size_t
Aborted by user
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_fd(int, const std::filesystem::path &, bool)
ERROR: Failed to serialize request: %@ error: %@
GET
ERROR: Response dictionary is missing required keys. Will fail
Failed to sign request\n
Image has a read-only format, attach failed due to force RW flag
URL
ASIF: metadata header out of range
Missing parent node in graph.
sg: buffer = 
-[DIDeviceHandle updateBSDNameWithBlockDevice:error:]
Unexpected response type: %@
Couldn't trim entry in read 
UDIF - max compressed run size: 
handleRefCount
AAS3ContextSetFieldString
ASIF
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)
version_1 = 1, version_2 = 2, version_3 = 3
0b
com.apple.diskimagescontroller
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_stackable_uuid() const
-[DIBaseParams openExistingImageWithFlags:error:]
ASIF meta header data is unaligned
Invalid UDIF format, contains intersected blocks
Data Runs
name: 
uid temporarily set to 
virtual int DiskImage::set_size(uint64_t)
CFAutoRelease<CFMutableArrayRef> UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::generate_blkx() [Checksum = ChecksumScheduler<checksum::CRC32,
Failed to write metadata
Crypto couldn't write to inner backend @ 
 - 
s3Perform failed (after retry), %s
The image was unlocked before setting userData
Failed to write SLA text to stdout
, err 
device with dev name 
-[DIClient2IODaemonXPCHandler cancelSLAWithReason:]
%.*s: Device created, attaching to the new device
%.*s: entry: %{public}@
%.*s: Looking for encrypted image passphrase in the %s keychain
%.*s: Disk image resized to %llu bytes
%.*s: Shadow format validator exception: %{public}s
%.*s: blocks array: %{public}@
%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported
%.*s: Error checking %s property: %s
%.*s: XPC connection lost: %{public}@
%.*s: Attaching to an existing device
%.*s: Failed initializing plugin: %{public}@
%.*s: Cannot open cache file %{private}@ with RW access, trying read-only
%.*s: Invalid key: %@
%.*s: Waiting for completion of an ongoing eject of %{private}@
%.*s: Erasing %{private}@
%.*s: Received connection from pid %d with euid %d. Our euid is %d
%.*s: Error encoding user dictionary: %{public}@
%.*s: SLA detected, connecting to IO daemon for user acceptance
%.*s: entry with %{private}@
%.*s: On disk cache is not supported on embedded systems
%.*s: entry
%.*s: Unlocked using public key
%.*s: Failed to dup stderr: %d
%.*s: <%lu> %{public}s
%.*s: fstat failed with errno %d
%.*s: Cleaned up folder copy connection
%.*s: Cannot open shadow chain %{private}@ with RW access: %{public}s, errno=%d
%.*s: %{public}s, errno=%d
%.*s: Not a UDIF: %{public}s, assuming RAW format
%.*s: Creation failed, erasing %{private}@
%.*s: Failed during ASIF extents enumeration on offset: %llu
%.*s: User data retrieving passed, %d value(s) found
%.*s: DIDeviceHandle object is deallocating, invalidating connection
%.*s: Keychain item requires ACL upgrade
%.*s: New disk image size is the same as previous
%.*s: Moving %{private}@ to %{private}@
%.*s: Failed opening %{private}s, errno %d
%.*s: Failed to delete %@: %@
%.*s: First connection attempt failed: %{public}@, retrying
%.*s: Controller path: %{public}@
%.*s: BSD name: %{public}@
%.*s: Creating connection to %{public}@
%.*s: Creating NSXPC listener on %{public}@
%.*s: Device will be marked as solid state
%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)
%.*s: Error calling back the client via XPC: %{public}@
%.*s: Due to the conversion error, erasing the output file
%.*s: Using an existing shadow file: %{private}@
%.*s: Setting oneshot XPC instance
%.*s: User data embedding passed
%.*s: Failed to dup stdout: %d
%.*s: Conversion completed, output file size: %llu bytes
%.*s: SLA detected, returning to client for acceptance
%.*s: Failed to open pager, writing directly to stdout
%.*s: isWritableFormat: %s
%.*s: res_dict: %{public}@
%.*s: Shadow file %{private}@ opened with RW access
%.*s: Attaching a quarantined image
%.*s: [Apple Internal] Creating an emulated external disk
%.*s: Received: %{public}@
%.*s: Reached an interruption handler for the IO daemon connection
%.*s: %{public}@ %{public}@
%.*s: Failed to generate device identity: %@
%.*s: Failed to read passphrase from TTY
%.*s: Entry ID of root block storage device: 0x%llx
%.*s: Device will be marked as high throughput
[0x%08x] %{public}s
%.*s: Passphrase found in keychain, unlocking the image
%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization
[0x%08x](warning) %{public}s
%.*s: Unlocked using symmetric key
%.*s: Performing in-place squash optimization
%.*s: Not a pstack
%.*s: numBlocks queried for an empty shadowChain.
%.*s: Failed instantiating rawTestPlugin object: %s (code %d)
%.*s: Client is entitled to attach disk images
%.*s: Passphrase is correct
%.*s: No matching item found in keychain
%.*s: Failed to erase output URL
%.*s: Creating %s plugin instance with params: %@
%.*s: Using existing disk image params
%.*s: Disk image file is not backed by local storage, root device entry ID will be the disk image device itself
%.*s: IOServiceWaitQuiet done
%.*s: File system is %{public}s
%.*s: Image %{private}@ re-opened with RW permissions
%.*s: Cancelling conversion (NSProgress cancel requested)
%.*s: DiskImages2 framework version: %s
%.*s: Registry entry ID is 0, can't check %s property
%.*s: Got error from last XPC command: %{public}@
%.*s: Successfully issued sandbox extension token for file %{private}s (token length: %zu bytes)
%.*s: %{public}s
%.*s: Keeping RO mode for %{private}@
%.*s: A valid plist was given, but it has no pstack version key
%.*s: Creating device with %llu blocks of %u bytes, instance ID %{public}@, ABI version %d
%.*s: Run loop aborted
%.*s: Keychain lookup returned %d
%.*s: Failed to open /dev/tty: %d, falling back to stderr
%.*s: Pager command failed with status %d, output may be incomplete
%.*s: Out of memory, failed to allocated %zu bytes for key %@
%.*s: cancelSLA wait returned error: %{public}@
%.*s: Converting user data
%.*s: Device will be marked as supporting persistent attach
%.*s: Successfully retrieved WKMS shipping key
%.*s: Not a sparseimage: %{public}s
%.*s: Verify passed
%.*s: Client reported error: %{public}@
%.*s: Failed to copy source disk image to temporary URL
%.*s: Image file %{private}@ opened with flags %d
%.*s: Validation exception: %{public}s
%.*s: Using %{private}@ as read-only
%.*s: XML_RSRC_FORK: %{public}@
%.*s: Connection attempt failed: %{public}@, retrying
%.*s: waitForSLACompletion returned error: %{public}@
%.*s: Failed to dup2 to stdout: %d
%.*s: %{public}@ - %{public}@ %{public}@
%.*s: On disk cache path: %{public}@
%.*s: Failed to open top disk image node.
%.*s: Missing parameters
%.*s: Failed creating queue
%.*s: Client acknowledged receiving the device handle
%.*s: Storing passphrase in the %s keychain
%.*s: %{public}@ error %{public}@
%.*s: Successfully retrieved WKMS non-shipping key
%.*s: WARNING: Found %llu sectors with invalid flags (has_bitmap)
%.*s: stderr duplicated
%.*s: Creating connection with %{public}@
%.*s: Using an existing cache file %{private}@ with RO access
%.*s: Converting to %{public}@
%.*s: Controller euid: %d
%.*s: Failed creating semaphore
%.*s: Cache file %{private}@ opened with RW access
%.*s: Creating connection to IO daemon clients listener
%.*s: Failed to get UUID info of provided image.
%.*s: %{public}@
%.*s: IOServiceWaitQuiet timeout occurred, retrying.
%.*s: Failed to connect to IO daemon for SLA handling
%.*s: Issuing new sandbox extension token for file %{private}@
%.*s: Asking user permission to store the passphrase in the keychain
%.*s: Copied sandbox extension token from reopened backend (length=%zu)
%.*s: Reached an invalidation handler for the IO daemon connection
%.*s: Failed to create graph from plist: %@.
%.*s: Closing IO service
%.*s: Got to XPC interruption handler
%.*s: I/O error at offset %lld iov_count %d errno %d
%.*s: Input and output files are the same, using a temporary output file
%.*s: %@
%.*s: Asking for passphrase using readpassphrase
%.*s: Device registry entry ID: 0x%llx
%.*s: Got to XPC invalidation handler
%.*s: Decoding plugin instance
dataUsingEncoding:
removeNodeWithUUID:recursive:error:
verifyNodes:error:
writeHexKeyToBuffer:hexKey:error:
T@\"NSUUID\",R,C,N
mandatoryArgumentFailWithError:
sessionWithConfiguration:
GUIVerifyPassphraseLabelCreate
TB,N
UUIDString
setOutputURL:
setPersistentAttach:
stackableUUID
T@\"NSArray\",R,N
_ramSizeStr
_regEntryID
_supportsBarrier
setCacheBackendXPC:
toDIShadowNode
ucConnection
urlRequest
TB,R,N
TQ,R,N,V_regEntryID
outputParams
semaphore
imageFormat
addShadowNodes:error:
currentConnection
setSymmetricKey:
TB,V_autoMount
_uniqueDevice
absoluteURL
cloneToURL:error:
copyPropertyWithClass:key:
ramSizeStr
setValue:forHTTPHeaderField:
getImageUUIDWithURL:allowMissingUUID:error:
hash
setCreateParams:
errorWithEnumValue:verboseInfo:
TB,N,V_handleRefCount
_publicKey
addBytesDownloaded:
copyBlockDeviceWithError:
errorWithDomain:code:userInfo:
initWithSize:
performSelector:
_temporaryPassphrase
filePath
resizeToSize:error:
resizeWithError:
resizeWithNumBlocks:error:
initWithParams:
auth_table
params
password
getChildren
TB,V_extraInfo
_convertParams
convertUserDataWithDiskImage:destination:
isMemberOfClass:
T@\"DIAttachParams\",R,N,V_attachParams
isDeviceHighThroughputWithRegistryEntryID:
setDiskImageParamsXPC:
T@\"NSLock\",R,V_cacheLock
_mountedFrom
chpassWithError:
initWithUTF8String:
isDeviceSolidStateWithRegistryEntryID:
nodes
_UUID
copyUnmatchedDiskImageWithRegEntryID:error:
moveItemAtURL:toURL:error:
setClient2IOhandler:
status
bundleWithURL:
newAEABackendThrowsWithBackendXPC:error:
pluginName
rootNode
setPublicKey:
TQ,N,V_regEntryID
createNodesConnectivityWithNodesDict:error:
setInvalidationHandler:
componentsSeparatedByString:
initWithDevName:error:
openMode
saveToPlistWithDictionary:URL:error:
T@\"NSArray\",&,N,V_handles
TB,N,V_uniqueDevice
_inputURL
deviceHandle
initWithDevName:
initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:
lastPathComponent
lockBackendsWithError:
T@\"DIConvertParams\",&,N,V_convertParams
T@\"NSDictionary\",R,N,V_pluginParams
arrayWithObject:
initWithURL:size:error:
setSizeWithDiskImage:newSize:
CLIPassphrasePromptUnlock
prepareImageWithXpcHandler:fileMode:error:
symmetricKey
initWithBackendXPC:
openExistingImageWithError:
savePstackWithError:
setFolderCopyXPCHandler:
T@\"NSString\",R,C,N,V_ramSizeStr
Ti,R,N
addValue:forHTTPHeaderField:
initWithUUIDString:
waitForSLACompletionWithReply:
Tq,R,N
containsValueForKey:
fileHandleForReadingFromURL:error:
copyDevicePathWithStatfs:
enterSandbox
ephemeralSessionConfiguration
initWithBaseImageURL:newPstackURL:tag:error:
parent
shouldValidate
stringWithFormat:
GraphNodeWithDictionary:workDir:error:
TQ,V_size
addRequest:
createAndStoreInSystemKeychainWithAccount:error:
createDeviceWithError:
imagesDictsArray
pauseInterval
removeObjectAtIndex:
lowercaseString
bytes
getUUIDBytes:
redirectStdoutForDisplay
setExportedInterface:
isQuarantined
RAMdisk
setTag:
_cacheBackendXPC
_cacheURL
copyIOMediaWithError:
TB,N,V_persistentAttach
certificate
failWithPOSIXCode:verboseInfo:error:
_mountedOnURL
_openParams
consoleAskForPassphraseWithUseStdin:usage:error:
conversionMethod
urlSession
createDiskImageParamsWithError:
T@\"NSUUID\",R,C,N,V_encryptionUUID
TB,N,V_cacheImage
Tf,V_pauseInterval
_isCache
_slaText
launchIODaemonWithError:
topDiskImageNumBlocks
T@\"NSString\",R,N,V_sandboxToken
remoteObjectInterface
setProgress:
unlockUsingSymmetricKeyWithError:
T@\"NSURL\",R,N,V_pstackURL
_bytesDownloaded
initWithGraphDB:pstackURL:error:
inputMountedFrom
readToAsyncByteStream:size:atOffset:
setHandles:
BSDName
keychainUnlockWithError:
setGraphDB:
TI,R,V_maxRequests
copyParentWithError:
validateObjWithKey:className:isOptional:error:
children
instanceID
nilWithUnexpected:error:
setOutputFormat:
setTimeoutIntervalForResource:
toDictionary
T@\"NSArray\",R,N,V_shadowStats
mountPoints
setExecutableURL:
.cxx_construct
initWithEndpoint:
lockAndMoveOpenParams
T@\"NSProgress\",&,N,V_progress
TB,V_encryptionInfoOnly
_passEntryToChange
allowOnDiskCacheWithSinkDiskImage:
lookupLegacyKeychainWithXpcHandler:error:
runWithError:
T@,&,N,V_remoteProxy
getPublicKeyWithCertificate:error:
remoteProxy
signalCommandCompletedWithXpcError:
terminationStatus
TI,V_remainingAttempts
URLWithString:
WKMSKeyWithAuthData:destKey:destKeySize:error:
setXpcListenerEndpoint:
domain
getInterconnectLocation
inputURL
requestsSem
T@\"NSMutableData\",R,N,V_mutableSymmetricKey
copyUpdatedOutputURLWithError:
initWithBase64EncodedString:options:
objectForKey:
T@\"BackendXPC\",&,N,V_cacheBackendXPC
_buf
setFileBackend:
failWithOSStatus:verboseInfo:error:
mountedOnAPFS
stringWithUTF8String:
T@\"DIClient2Controller_XPCHandler\",&,N,V_folderCopyXPCHandler
nilWithPOSIXCode:verboseInfo:error:
sendSynchronousRequest:returningResponse:error:
setImagesDictsArray:
GUIAskForPassphraseWithEncryptionFrontend:usage:error:
T{shared_ptr<unsigned char>=*^{__shared_weak_count}},R,N,V_key
_urlRequest
enumerateKeysAndObjectsUsingBlock:
suppressSsdFlags
_mutableSymmetricKey
T@\"NSXPCListenerEndpoint\",&,N,V_xpcEndpoint
encodeInteger:forKey:
insertObject:atIndex:
readPassphraseFlags
size
_offset
initWithDictionary:workDir:error:
isPstack
processName
substringToIndex:
tryResolvePstackChain:
T^v,R,N
_header
TI,R,N,V_ioObj
_shadowStats
class
decodeObjectOfClasses:forKey:
initWithURL:numBlocks:error:
nonCacheNodes
T@\"NSMutableArray\",R,N,V_nodes
_userDict
setEmulateExternalDisk:
setNbyte:
setValue:forKey:
GUIAskForPassphraseWithPassphraseUsage:error:
promptUserForSLAAcceptance:error:
T@\"NSData\",&,V_cache
TAQ,V_bytesDownloaded
TQ,N,V_blockSize
handleRefCount
initWithURL:
registryEntryIDWithError:
unlockWithPassphrase:error:
askPermissionWithRememberPassword:error:
completeCommandWithError:
copyDefaultLocalizedStringForDIErrorCode:
T@\"DIClient2IODaemonXPCHandler\",&,N,V_client2IOhandler
dictionaryWithObjects:forKeys:count:
GUIPassphrasePromptCreate
_outputURL
inPlaceConversion
setRemainingAttempts:
setStandardOutput:
synchronousRemoteObjectProxyWithErrorHandler:
containsObject:
T@\"NSMutableDictionary\",&,N,V_pstackDict
newWithURL:fileOpenFlags:error:
setClasses:forSelector:argumentIndex:ofReply:
statusCode
xpcEndpoint
_status
T@\"NSMutableSet\",R,V_requests
commandSize
errorWithUnexpected:verboseInfo:error:
verifyParams
S3KnoxResolveURL:key:keySize:error:
setXpcEndpoint:
isNewDevice
```
