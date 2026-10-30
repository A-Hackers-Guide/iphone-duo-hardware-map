# `/usr/libexec/diskimagesiod`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,916,816 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 43 (Size: 5808)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (26)

- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit (compatibility version 302.0.0, current version 944.0.0)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/local/lib/libcurl.4.dylib (compatibility version 7.0.0, current version 9.0.0, weak)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
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
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.diskimages.io-uc</key>
	<true/>
	<key>com.apple.diskimages.spawner</key>
	<true/>
	<key>com.apple.private.amber.client</key>
	<true/>
	<key>com.apple.private.apfs.no-padding</key>
	<true/>
	<key>com.apple.private.diskarbitrationd.access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceSystemPolicyAllFiles</string>
	</array>
	<key>com.apple.private.vfs.role-account-openfrom</key>
	<true/>
	<key>com.apple.private.vfs.role-account-unmount</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/usr/libexec/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>DIDeviceIOUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.DiskArbitration.diskarbitrationd</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>hw.logicalcpu</string>
		<string>hw.memsize</string>
		<string>debug.didevice_queue_depth</string>
		<string>debug.didevice_cache_size_default</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>
```

## Objective-C (75 classes, 11 protocols)

Classes: `AAS3DownloadRequest`, `AAS3DownloadSession`, `AEABackendXPC`, `BackendXPC`, `CryptoBackendXPC`, `DIAttachParams`, `DIAttachedDeviceInfo`, `DIBaseAgentDelegate`, `DIBaseAgentXPCHandler`, `DIBaseParams`, `DIBaseServiceDelegate`, `DIBaseXPCHandler`, `DIBlockDevice`, `DIChpassParams`, `DIClient2Controller_XPCHandler`, `DIClient2IODaemonXPCHandler`, `DIController2ClientDelegate`, `DIConvertParams`, `DICreateASIFParams`, `DICreateParams`, `DICreateRAWParams`, `DICreateUDSBParams`, `DIDeviceHandle`, `DIDiskArb`, `DIDiskArbEmulation`, `DIDiskImageBridge`, `DIDiskMountTracker`, `DIEncryptionChpass`, `DIEncryptionCreator`, `DIEncryptionFrontend`, `DIEncryptionUnlocker`, `DIError`, `DIHelpers`, `DIIOCacheDelete`, `DIIOClientDelegate`, `DIIODaemonDelegate`, `DIIOIterator`, `DIIOMedia`, `DIIOObject`, `DIImageHandle`, `DIImageInfoParams`, `DIKeyRetriever`, `DIResizeParams`, `DISLAFrontend`, `DIShadowChain`, `DIShadowNode`, `DIStatFS`, `DIStatsParams`, `DITemporaryPassphrase`, `DIURL`, `DIUserDataParams`, `DIVerifyParams`, `DiskImageGraph`, `DiskImageGraphNode`, `DiskImageParamsASIF_XPC`, `DiskImageParamsLocked_XPC`, `DiskImageParamsPlugin_XPC`, `DiskImageParamsRAM_XPC`, `DiskImageParamsRaw_XPC`, `DiskImageParamsSparseBundle_XPC`, `DiskImageParamsUDIF_XPC`, `DiskImageParamsXPC`, `FileLocalXPC`, `KNOXBackendXPC`, `NSMutableDictionary`, `NSXPCConnection`, `NativeDiskImageGraphNode`, `PluginBackendXPC`, `PluginDiskImageGraphNode`, `QuarantineFileHandler`, `RamXPC`, `ReadSynchronizerBackendXPC`, `SerializedDiskImageGraph`, `SparseBundleBackendXPC`, `_TtC16FetchRestoreKeys16CryptoKitWrapper`

Protocols: `DIController2ClientProtocol`, `DIControllerProtocol`, `DIDisappearedMountPointDelegate`, `DIIOClientProtocol`, `DIIODaemonProtocol`, `DISpawnerProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `PersistentBackend`

## Strings (4,104)

First 2,500 of 4,104.
```
Destructing sb context
Unable to create ioreg iterator
 length 
Band size in sparse is zero
Found a valid file for 
(err 
Can't flush asif on table flush, backend barrier failed
(locked)
-[DIIODaemonDelegate tryAttachWithParams:error:]
UDIF header changed while unlocked
Data Fork
int plugin_decode_fd(void *, const char *)
Can't flush asif table, bitmap flush failed 
bad flush type (
Compressed Length
Format Description
DES3_3KEY = 17, AES_KEY = 0x80000001
 elements returned 
tmp_convert
Unsupported block size for image format
!
std::string FileDescriptor::get_mounted_on_fs() const
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_fo
mountedFrom
ASIF: missing internal metadata key
-[DIBaseServiceDelegate init]
Solid State
wkms-dev.sd.apple.com
\\\\
Mandatory callbacks in the plugin's struct are missing
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682
Diskimages2 - ASIF - bad reserved bits 
Failed to sign request\n
fsid
-[DIIOCacheDelete eraseOldCacheFiles]
-[DIIODaemonDelegate exitWithUnmount]
Role
Image
table_entry_data::flags di_asif::details::table::get_next_extent(ContextASIF &, const interval_sectors &, interval_sectors &)
Failed to parse key in KVS (zero size key).
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638
Failed to get registry entry ID, ret %d
virtual int BufferedWriteBackend::write(const sg_entry &)
token
header_signature
version
FilePath
v8@?0
, size=
UDIFDiskImage: failed flush after user data write
Can't convert data to property list
The requested operation will delete the active node, please set another one first.
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)
BZIP compression failed, res=
-[DIIODaemonDelegate attachToExistingDeviceWithParams:reply:]
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
RW
Failed barrier at start of dir flush, error
UDIF: Can't find data key in dictionary
-[DIIODaemonDelegate resumeAttachAfterSLA:completionReply:confirmReply:]
AWS4-HMAC-SHA256 Credential=
Skipping band erase (in use)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
Flushing 
Failed writing full dir
com.apple.mach_rcvd
HTTP %u\n
failed to open existing output file
int di_asif::details::table::close()
virtual int FileLocalAsync::_read(const sg_entry &)
Failed to eject - cannot open device
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Backend barrier failed during dir flush, error 
Failed to create DADisk during unmount
\\t
Raw header changed while unlocked
virtual int SparseBundleBackend::lock()
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)
, UID:GID(Name)=
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_t
-[DIIOCacheDelete registerPeriodicCallback]
Request failed: %03ld (error not set)
Failed to find keychain item using hashed key
PKCS7 = 7
shadowStats
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
 mode=
KEY_BITS_128 = 128, KEY_BITS_256 = 256
true
Legacy shadow file format is not supported by DiskImages2 framework
Failed to write metadata header
Authorization
-[DIEncryptionFrontend unlockWithPassphrase:error:]
Custom cache or shadow is not supported for pstack based images.
Unknown
-[DIShadowChain addShadowNodes:wrapReadOnly:error:]
prng_algorithm_type
%12u max attempts for a request\n
-[DIUserDataParams encodeWithCoder:]
writable
+[DiskImageParamsXPC validateSupportedFormatWithBackendXPC:error:]
 trying to check permission after EACCES
Cache is not supported when using pstack.
Disk image is terminated, skipping future_write
%@[%@]
 marked as purgeable
cmd
bool DIIOManager::fetchCacheStat(uint64_t &, uint64_t &)
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
backend
precision
ASIF header changed while unlocked
Diskimageuio: can't get file descriptor, backend doesn't exist
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
Backend does not support file descriptor access
Plugin version 
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)
Key is not 32 bytes size.
pluginParams
No room to add new auth entry
KVS dataBuffer allocation failure.
-[DICreateParams onErrorCleanup]
-[DIIODaemonDelegate validateConnection]
/dev/disk
Cleaning up!
Plugin's ring suspended, ret code 
Failed to reconstruct complete shadow chain during respawn
Dissented with status 0x%X, pid %d
Can't take exclusive lock on entry
Failed to create graph from plist.
inode
DiskImageConvert
key
 is incompatible with the framework, expected at least 
Unable to get IOMedia preferred block size
Info.plist
Suspended
 opened and replaced at attempt 
Cannot find IO object of class %@
Opening mapped blocks for 
+[BackendXPC newFileBackendWithURL:fileOpenFlags:error:]
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
knox.sd.apple.com
Can't write initial table data
Invalid instance ID format
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
ASIF
Backend barrier failed after dir offset changed, error 
PstackVersion
frk_set_device_identity_certificates
debug.didevice_queue_depth
virtual sparse_bundles::Band::~Band()
fetch_restore_keys_key_handling.m
Cannot store an empty passphrase
Diskimageuio: Raw header changed while unlocked
int PluginsManager::register_plugin(const string &, di_plugin_t *)
baseBackend
file of 
sg: buffer = 
YES
bool DIIOManager::stashSingleFile(std::shared_ptr<Backend>, NSString *__strong, const char *, uint32_t)
ERROR: shipping key wrapped-key failed base64 decode
virtual int DiskImageSparseBundle::flush(DiskImage::Context &, di_flush_mode)
Cannot find image with provided tag.
r
Diskimageuio: UDIF header changed while unlocked
AES-XTS
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
Image has a read-only format, attach failed due to force RW flag
Plugin image struct size 
io_result_t di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
IOMedia device not found in registry iteration
int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
Failed to generate self signed certificate
com.apple.diskimages.band_management
Background close of 
ASIF Info
AAS3ContextCreate
oidc
virtual lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImageRaw::future_write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
The argument index is invalid
com.apple.DiskImages2.TelemetryManager
Failed creating sparsebundle folder
getToken
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
CFAutoRelease<CFStringRef> udif::sla::extract_text_from_resource_array(CFArrayRef, std::optional<std::span<const UInt8>>, std::optional<int32_t>, CFStringEncoding)
unique_ptr<lock_free::bitmap_t> SparseBundleBackend::get_existing_bands() const
key_derivation_prng_algorithm_t
Can't load bitmap from backend
Failed to replace passphrase entry in auth table
Disk image operation failed with error code %d
, fd=
. returned 
Plugin initialization failed
Band was evicted by another thread (during retain attempt), retry erase process
LPic
Awaitable completed in unexpected state
Can't write UDIF header
Invalid public key: %s
Unexpected passphrase header length (
expected<uint64_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_nr_blocks() const
The requested URL is an existing non-sparsebundle folder
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ H
 src size 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:425:
com.apple.diskimage-plugin.nbd
-[SparseBundleBackendXPC getCryptoHeaderBackend]
Write zeros to unmap unaligned start region failed (err code
crypto
Failed to get instance ID from dormant device
Compressed Bytes
/System/Library/PrivateFrameworks/DiskImages2.framework
Diskimageuio: No diskimage given
block_attributes
total_segments_t
-[DIUserDataParams retrieveWithError:]
Info.bckup
dev
Default
com.apple.MobileAsset.AssetType
-[AAS3DownloadSession syncRequests]
set size failed
Failed barrier after writing full dir
Failed to create CFString for property key or value
IOServiceWaitQuiet error 0x%x
Block size mismatch in DiskImageStackable
auto sparse_bundles::Band::get_mapped_blocks()::(anonymous class)::operator()() const
Metadata corrupted 
File too small.
The fill option contains an invalid value
Failed placing new 
BackendPlugin
Write header failed after dir offset changed, error 
segment_count_none = 0, segment_count_one = 1
flock returned errno 
unknown
random generation failed with err code 
-[DIIOCacheDelete setupSigtermHandler]_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ H
bands
Failed to erase mapped file of band 
encryptionMethod
read_only_cache = bit(0)
managed
-[DIIODaemonDelegate unmountAll]
void terminationCallback(void *, io_iterator_t)
lzfse
+[DiskImageParamsXPC newWithURL:fileOpenFlags:error:]
ASIF: Entry dirty bit is set when reading from disk
-[DIClient2IODaemonXPCHandler createConnection]
main image
SLA prompt cancelled
blockSize
Snapshot
bool di_asif::details::table_entry_data::validate() const
 or exceeds size_t size 
A controller XPC service attempted to connect to an existing device, but this daemon instance has no such device yet
Non supported options in AAS3DownloadSession (ignored): pinned_public_key %s
An argument index may not have a negative value
Cannot decode writable
ASIF: Can't defrag entries 
IOServiceOpen failed with status 0x
void di_hybrid_subscriber_t::cancel()
The requested operation will delete all children of the provided node. use recursive removal to surpress this error.
Failed to add shadow nodes to chain
tr '\\r' '\\n' | fmt | ${PAGER:-more}
virtual di_coroutines::Task<void> CompressedBackend::run_futures()
Diskimageuio: image is locked
Band data doesn't exist, zeroing
sparseHeader
com.apple.diskimages.aio
The format specifier for 
Feature or image not supported by library
Uninitialized Entries
void di_hybrid_subscriber_t::suspend()
-[DIIOCacheDelete onPeriodicWithInfo:urgency:]
-[DIIODaemonDelegate finalizeSetupWithParams:service:connection:error:]
Sandbox extension token exceeds maximum size
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
Failed to retrieve file info for index %u (status 0x%x)
iCloud
virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
Unexpected response type: %@
 bytes image
Can't get key in cstring format
ParentUUID
[start: 
Failed unlocking file with fd 
v32@?0@\"NSMutableDictionary\"8Q16^B24
 completely
none {
Missing parent node in graph.
Crypto data block size: 
Unsupported public key algorithm.
lifs
The disk image is corrupted
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
APPLECONNECT.APPLE.COM
Failed to set up image for info retreival
Bit 
ASIF meta header size exceeds its maximum
[empty]
Can't get send rights
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
eject timeout
virtual io_result_t sparse_bundles::Band::write(DiskImage::Context &, const sg_entry &)
-[FileLocalXPC replaceWithBackendXPC:]
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
bool DIIOManager::sendFileToDriver(int, const char *, uint32_t, NSString *__strong, std::shared_ptr<Backend>, uint32_t)
-[DIDiskArb ejectWithBSDName:error:]
The format string terminates at a '{'
-[DIBaseXPCHandler createConnection]
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
-[DIBaseParams openExistingImageWithFlags:error:]
Flush failed after defrag, ignoring. Error 
int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)
IOBlockStorageDriver device not found in registry iteration
IOServiceMatched
unsigned long getCacheSize()
XPC connection invalidated
File: Couldn't fetch status, error: 
sig2_t
 io_start_offset: 
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c
0X
GUI SLA handling required
174350
Attributes
Failed during IO manager initialization
Failed to create DADisk during mount
Failed to create passphrase auth entry
 bits in the bitmap
-[DIBaseParams tryResolvePstackChain:]
Cache
Diskimageuio: decryption key missing
Metadata
Failed to drain dormant I/O queue, status=
KVS keyBuffer allocation failure.
no_match
Passphrase cannot be empty
Diskimageuio: Failed to create disk image: 
Updating 
 failed with 
uid temporarily set to 
readPassphraseFlags
 header size 
Can't write UDIF resource part
gcd::gcd_kqueue::gcd_kqueue(gcd_queue &, std::function<void (struct kevent64_s *, int)>)_block_invoke
Invalid field found in shadow file header: 
-[DICreateParams resizeWithDiskImage:blockCount:error:]
virtual int FileLocalAsync::unlock_all()
system
-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]
Failed to read 
Failed writing sparsebundle info
com.apple.diskimages.creator-uc
Diskimageuio: Invalid pstack element: 
fchmodat failed for 
Image does not have write permissions
Remember password in my keychain?
diskimage_uio::details::diskimage_impl::diskimage_impl(diskimage_open_params &&)
void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/crypto/crypto_format.cp
Failed copying cache URL
invalid flags
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
Invalid or missing image URL key
void diskimage_uio::details::diskimage_open_params_impl::lock_backend_if_required()
virtual io_result_t DiskImageUDIFRead<UDIFReader<locks::None>, DiskImageUDIF>::read(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &) [UDIF = UDIFReader<locks::None>, UDIFVariant = DiskImageUDIF]
Replaced an empty slot
Unmap done
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
UDIF_header
%12u max requests in flight\n
Barrier
Persistent attach is not supported for this disk image type
), reading from backup
Band was evicted by another thread, retry erase process
> real: <
fd block size retrieval failed (err code 
com.apple.diskimagesiod
Compression Type
raw
IOHDIXHDDriveNub
-[DIConvertParams prepareParamsForSquashWithError:]
useFormatMappingInfo
Cancelled
encryption: header size mismatch
Accept: application/xml
AAS3DownloadStream (NSURLSession)\n
Invalid path property (not UTF8)
STCK
Resetting 
Missing payload URI in Knox response
Resumed
Invalid format for shadow file
debug.didevice_cache_size_default
Failed to set up image for resize
LaunchInstanceID
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_read(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Harde
Could not stat shadow file
 logical: 
IO error with sg: 
(err code %d)
virtual DiskImageSparseBundle::ContextSparseBundle::~ContextSparseBundle()
url
IV_TWEAK_SIZE_16 = 16
cache
h
emulateExternalDisk
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
ramTestPluginCreate
segment_count_t
nodes
%02x
static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
 auth entries
zero-padding
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
publicKey
v24@?0@\"NSFileHandle\"8@\"NSError\"16
0123456789abcdef
set context
 - same 
static void sparse_bundles::Band::erase(const bundle_commons_t &, uint64_t)
Missed an evictable slot
Invalid encryption method
ActiveNode
AppleDiskImageDevice
UDRO
 option
Integral value outside the range of the char type
int details::udif_verify::calculate_checksums(workqueue::workqueue &)_block_invoke
BackendSG: truncating the inner backend failed, error = 
Content-Type:
 is different than current mode 
fully
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
Driver returned error code 
Failed to read auth table
singleInstanceDaemon
Failed opening the sparsebundle as user 
: flush in destructor failed (
invalid bits range 
lock_backend
KVS key value - parse failure.
stable uuid
virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()
an unprepared device
miss
pending_requests
Failed to set up image for resize after creation
curl_easy_setopt failed\n
Failed to write SLA text to stdout
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:172:22)]
%@[%@, %@]
UDBZ
virtual int Backend::write(const elements_t &)
Corrupted shadow file(s) chain
UDIF images are currently not supported in diskimage_uio
Error with resolving knox url
Images Count
Error opening ByteStream
virtual int CompressedBackend::write(const sg_entry &)
Cannot find AmberDiskImagePluginCreate in libAmber
Failed to create matching dictionary for device class 
gcd_kqueue: kevent64 returned error 
Destination folder URL must be of 'file' scheme.
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
BackendSG: error allocating buffer
solid state
Failed to create disk image
ReadOnlyBackend
Unexpected error creating (unlocked) backend
Flushed 
Waiting for barrier to complete
Replacement argument isn't a standard signed or unsigned integer type
Apple sparse image
-[DIIODaemonDelegate validateInstance]
The numeric value of the format specifier is too large
a pointer
Invalid band size (
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615
Corrupted ASIF image.
/usr/lib/libAmber.dylib
descriptor_special
Backend is not mounted on APFS
ERROR: enc-request failed base64 decode
Destination folder URL must represent an existing folder.
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
-[DIAttachParams reOpenIfWritableWithError:]
field size too large
algorithm_type
Mount Point
ERROR: Failed to serialize request: %@ error: %@
corrupted image
Failed creating 
virtual int DiskImage::set_size(uint64_t)
Failed to get parent registry entry, err code %d
oma-context
saks-ac-uat.g.apple.com
\\x{
instanceID
Name
com.apple.diskimages_cache_update
bool DiskImageSparseBundle::try_unmap_band_extents_without_list(uint64_t, const extents_set_t &)
Disk image URL is too long
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:113:22)]
Error creating backendXPC
overrideBlockSize
Num Tables
Sparse bundle image
mountedOnURL
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hard
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:836: libc++ Harde
-[DIIODaemonDelegate reopenStashedFilesWithUserClient:outBackends:error:]
encryption_key
The argument index should end with a ':' or a '}'
bool sparse_bundles::open_bands_t::insert(uint64_t)
uid restored to 0 (res=
Failed to create resizer
Duplicate shadow values for: %@
, required decompression buffer size: 
xpcEndpoint
Cannot find BSD name during respawn
virtual FileLocalAsync::~FileLocalAsync()
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc+
Diskimageuio: Can't stack non asif formats. Got 
di_plugin_image_t *PluginsManager::decode_plugin_image(const di_plugin_t &, const diskimage_decode_fn_t &, void *)
v32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
virtual int BackendSG::write(const sg_entry &)
(empty)
inputStatFS
Diskimageuio: Single element in pstack that isn't an image
Too many mount arguments
-[DIIODaemonDelegate onClientInvalidateWithConnection:]
0
DaemonPID
Failed during table 
Empty Bytes
Key transcoding failed.
Content-Length: %zd
void DIIOManager::driverConnect(DIAttachParams *__strong, const DiskImage &)
wkms
creating session
fstatfs failed
\\r
Unexpected backend type for file
Bundle's lock file is closed
Bad or missing key in SAKS response.
attempting to authenticate with kms
Extent 
ASIF block size isn't multiple of 512
auto trim_data(const sg_vec::iterator &, const sg_vec::iterator &, size_t, const io_result_t &)::(anonymous class)::operator()(const auto &, const auto &, size_t) const [src:auto = sg_vec_ns::details::sg_vec_iterator, dst:auto = sg_vec_ns::
 crypto = 
void DIIOManager::setupDriver()
X-Amz-Security-Token: %s
Band 
Invalid plugin URL, plugin name is missing
ASIF: Block size isn't a multiple of 512
assetAttr
Reserved
crypto_format: cookie differs
Failed to read passphrase from stdin
bitmap flag value invalid
shared
hybrid_queue
AES = 0x80000001
Failed to fetch stats from driver
enqueueRequest
Request failed
Encryption Method
Diskimageuio: can't get lock status 
We're out of ctxs for async execute
. Opening as root
Bearer openid-id-token-%@
Failed getting runloop source
/s3/aws4_request\n
-[AAS3DownloadRequest createAndResumeTask]
Convert AEA key from hex failed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603
Full Entries
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
InstanceID
 formatting argument
a floating-point
-[BackendXPC tryCreatingCryptoHeader]
Shadow backend %zu missing file descriptor
asif
-[DiskImageParamsXPC createDiskImageWithCache:shadowValidation:]
 requested while there are only 
ASIF max_write size in header exceed the limit
Invalid pstack, Active stack contains a loop.
crypto_mode
 while expecting 
get_next_capacity, allocator's max size reached
Attached disk image device info: BSD Name [%@], image URL [%@]
a bool
config_t
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
attempting to authenticate with saks
Can't parse encryption entry: 
-o
Using automatic argument numbering in manual argument numbering mode
Failed to resize the image
Unmapping band 
resource-fork
CFAutoRelease<CFDictionaryRef> udif::details::UDIF_base::get_resources() const
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
prng_key_bits_size_t
Failed to read passphrase
expected<int, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_file_descriptor() const
Image referenced in the pstack is unreachable.
virtual int BackendSG::truncate(uint64_t)
buffer[0]=[ptr=
image
allocated: size change callback failed with 
Failed to encrypt data using public key from certificate
Can't fulfill kernel's request. command: 
ERROR: This archive does not contain a shipping key response.
encKeys
type: 
 - different calculated: <
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_fd(int, const std::filesystem::path &, bool)
PKCS5_PBKDF2 = 103
CBC_IV8 = 5, XTS = 0x80000001
Encryption Info
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_stackable_uuid() const
Opening band 
Request creation
Missing OIDC client ID in appinfo response
UDIF image of 
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
\n
-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]
dealloc_queue
AAS3DownloadStream (curl)\n
 but buffer is full
di_plugin_image_t *verify_plugin_image(di_plugin_image_t *, CFErrorRef)
virtual FileDescriptorWrapper::~FileDescriptorWrapper()
-[FileLocalXPC sandboxExtensionTokenWithError:]
-[DIDiskMountTracker onDiskDescriptionChangedWithDiskName:isMounted:]
StandardCompressedBackend::pimpl::pimpl(algo_t)
Authentication Data creation failed.
readSynchronizer
/dev/%s
Backend creation failed for file %u: %s
s3Perform retry after %u ms
%12.2f initial interval between retries (s)\n
DiskImages Framework
The replacement field misses a terminating '}'
Couldn't open file with flags 
 is not supported (err code 
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
-[DIController2ClientDelegate attachCompletedWithHandle:reply:]
Block size mismatch between crypto header and ASIF header
an integer
 dest 
 given
Diskimageuio: Can't create stackable image: 
Read returned an error
CACHE_DELETE_AMOUNT
-[DIDiskArbEmulation ejectWithBSDName:error:]
Cannot create target image format with the block size of the source image
 is not registered
-[DIIOCacheDelete eraseOldCacheFiles]_block_invoke
Diskimageuio: Couldn't get locked status 
Could not parse OIDC token from AppleConnect output
crypt_consecutive_vector: write check errors 
Failed to allocate raw blob data
RSA = 42
fsync
01
com.apple.diskimage-test-plugin.julio
v32@?0@\"DIShadowNode\"8Q16^B24
Error during ASIF flush: 
 overrun events occurred in the plugin's ring!
static void process_terminator::terminate()
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
UDIF XML at 
Diskimageuio: unsupported disk image type for get_backend
startIO called without a pending DiskImage
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ H
Failed to serialize passphrase to crypto header
std::unique_ptr<DiskImage> diskimage_uio::details::diskimage_open_params_impl::transfer_disk_image_ownership()
+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)_block_invoke
Validation failed, input contains unexpected data.
static int FileDescriptorWrapper::open_from(int, const std::string &, int)
bytes, which is after end of ramdisk
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__memory/unique_ptr.h:
Max sector count is too large
get path failed
path
pthread_once
sign
Corrupted encryption table, invalid offset/length in entry's descriptor
] 
Transfer-Encoding:
Unexpected materialized_diskimage in create_diskimage_from_hdr
Failed truncating plist
shouldValidate
source uuid
--ram
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406:
Diskimageuio: Multiple images given but block size differ. 
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
, disk size: 
Failed locking the shadow file
io_result_inserter_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::data_entries_vectorizer_t::add_data_entry(const data_entry_t &)
 but buffer is too small 
Can't flush asif table, backend write failed
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
uniqueDevice
Disk image is terminated, skipping flush of 
ram
Base
Key size isn't a multiple of 8
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)
Cannot find %@ entry
Failed to find dormant device with instance ID
Content
int DiskImage::Context::flush(di_flush_mode)
Failed to update crypto header
A mandatory argument is null in a DiskImages2 API call. Remember to check if init succeeded
com.apple.DiskImages2.ASIF.sparsity
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
tkn
couldn't allocate space for entry 
, but file size only 
a character
Couldn't lock entry 
Failed to write asif header, error 
Can't load asif dir table
which is larger than allowed 
%@ failed with error code %d
 on 
Failed to read file for pstack parsing
Checksum Value
/dev/tty
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
, band was written to
asif_header
Asif header size unaligned
device with dev name 
PluginName
uri
--oauth-grant-type
int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
basic_string
supportsPersistentAttach
Unexpected image format from info: 
Can't convert ASIF flag.
-[DiskImageGraph initWithBaseImageURL:tag:error:]
sandboxToken
-[AAS3DownloadSession readToAsyncByteStream:size:atOffset:]
 with 
encryption
 at index 
v16@?0@\"NSError\"8
The underlying file system doesn't support writable images with 
Cannot attach RAM disk as a read-only device
crc32 {
ERROR: shipping key enc-request failed base64 decode
Decompression failed
void sparse_bundles::open_bands_t::remove(uint64_t)
IOStorageFeatures
sparseimage format is not supported by DiskImages2 framework
Read error: 
 is closed, notifying waiters
com.apple.DiskImages2.ErrorDomain
https://%@/spaces/%@/files/%@/decryption-components
 has size 
int crypto::crypt_op::crypt_consecutive_vector::operator()()
s3DownloadStreamOpen_curl
Cannot find image with provided uuid.
mapped blocks of band 
Failed to convert SLA text to C string
void info::DiskImageInfoASIF::examine_mapped_extents(const DiskImageASIF &)
Failed to increase file size, pwrite returned 
TEXT
Cannot display SLA: no terminal or stderr to write to
Invalid key size
diskimage_
int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)
Couldn't upgrade lock entry 
Failed to create DADisk during eject
Failed opening the shadow/cache file(s) with RW access
Bitmapped Entries
Barrier failed before dir flush
Failed to create chiper data for public key auth
vsnprintf
-[DIImageHandle resizeToSize:error:]
table entry data@
URL must have a file scheme
int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)
-[DIIODaemonDelegate wrapBackendWithEncryption:backendInfo:fileIndex:error:]
-[DIConvertParams onConvertCompletionWithInError:outError:]
auto hdr_get_nr_blocks(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
,
Constructing sb context
 - 
Compressed(
Band data is partial, reading 
UDIF_header::UDIF_header(const std::shared_ptr<Backend> &)
s3StringBufferAppend
Failed to use the passphrase that was given
flushing and closing 
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)_block_invoke
Not valid SAKS environment
encryption_key_bits_size_t
Background close of band at index 
:
https://%@/westgate/appinfo
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633
Max Size Bytes
Yes
+[DISLAFrontend(Private) redirectStdoutForDisplay]
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_handle_exceptions()
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
Failed creating bands folder
Unexpected unmap command received on read only image
Starting ASIF defrag, used size: 
Cannot find disk image with reg entry ID 0x%llx
, current is 
int ExecutionEngineCommand<CommandQueue, MachPort>::execute_work(unsigned int, bool) [Container = CommandQueue, Port = MachPort]
The argument index value is too large for the number of arguments supplied
Failed to store the passphrase in the keychain
Invalid output format argument
oauth
V2 = 2
com.apple.di_stackable.cache.flusher
Unknown checksum found
Invalid value for argument 'block-size'
application/json
strdup
Failed to eject
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
decryption-components
End of input while parsing an argument index
+[DISLAFrontend(Private) displaySLAText:error:]
barrier
read only
Size is not a multiple of block size
int di_asif::details::dir::handle_all_failures(ContextASIF &)
Bad pstack format, node with active UUID not found.
+[DIAttachedDeviceInfo copyAllMountPoints]
-[DIUserDataParams embedWithError:]
OK
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
 (errno 
Failed creating CFAutoRelease instance.
Flush failed - returning 
Looking for an evictable slot for 
Sector Count
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
 is now available
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
 directly (without list)
User data is not supported in this image format
virtual int Ram::_write(const sg_entry &)
shadow
 read: 
Can't flush asif table, backend barrier failed
Failed adding matching notification
AAS3ContextSetFieldString
 does not allow the 
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = udif::header]
Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib 
Invalid size hex key %lu
v24@?0@\"NSDictionary\"8@\"NSError\"16
Custom encryption entry header size exceeds max size
com.apple.wkms.auth-data
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
Diskimageuio: get parent uuid failed 
-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]
sg: 
Compressed Offset
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
diskimagesiod
bundle_handle
Crypto operation on data of 
s3Perform failed (after retry), %s
6.0
Zero padding disabled successfully on fd 
com.apple.diskimages.file.crypto
-r
Failed to issue sandbox extension token for file
internal metadata
bzip2
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::set_path(const std::filesystem::path &, const diskimage_open_params::mode)
file(
saks-ac-prod.g.apple.com
not a valid DER-encoded X.509 certificate
expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_image_header(size_t)
x-amz-
Backend: failed writing element in vector
com.apple.diskimage-plugin.amber
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ H
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
void udif::details::UDIF_base::print_checksum_verification_status(const std::string &, const csum_any &, const details::checksum &) const
lzma
ID
conversionMethod
Diskimageuio: path 
 bytes)
RAW read-write image
-[RamXPC createRamBackend]
device with registry entry ID 0x
saks-ac-dev.g.apple.com
Not A Ninja/1.0
Failed opening the image with RW access
PKCS1 = 10, OEAP_SHA1 = 0x80000001
com.apple.diskimagescontroller
public_key_crypto_algo_mode
passphrase_header
none
uat
oauth-id-token:
 with ret 
Error reading file @ 
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
Can't write table for defrag
Failed to start IO after SLA acceptance
Data
Full dir write failed with 
saksKey
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const
Clone of plugin nodes is not supported.
void sparse_bundles::Band::ContextsList::clear()
download
Barrier failed after defrag table move, error 
Failed to stash files for persistent attach - ejecting
Couldn't convert CFStringRef to a proper std string
Can't read custom encryption entry header, error 
Identity Info
Failed converting CFNumber to longlong
: flush failed (
Type
std::expected<CFAutoRelease<CFStringRef>, std::errc> udif::sla::extract_sla_text(const DiskImageUDIF &)
The format specifier should consume the input or end with a '}'
Failed to create crypto serializer
onDiskCache
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:152:22)]
startIO called more than once
DIIOManager::~DIIOManager()
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
Unsupported ASIF version 
Opened bundle's lock file with flags 0x
Master checksum
Backend barrier failed during allocator failures handling, error 
Cannot increase size of a block device
public_key_padding_algo
Registered plugin 
The requested URL is an existing regular file
public key has an encoding issue or uses an unsupported algorithm
Passphrases doesn't match
Diskimageuio: single image given, but role is 
 buffer_size = 
X-Amz-Date: %s
'
%s\n
No pending SLA to confirm
-[DIIODaemonDelegate createShadowChainWithBackends:error:]
Can't connect to driver
Start Offset
-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]
suppressSsdFlags
pstack_header
udzo_max
Could not determine cache dir
 bytes
Failed to evict band to make room for 
Read-only image cannot be resized
virtual PurgeableFileBackend::~PurgeableFileBackend()
Crypto couldn't read from inner backend @ 
Unmount already started, notifying controller to retry later
Metadata contains unsupported field 
Can't read UDIF trailer
) to type
Does not contain an \"even number\" of hex digits.
]
Write zeros to unmap unaligned end region failed (err code
v32@?0@\"NSURL\"8Q16^B24
typename boost::enable_if<boost::is_integral<typename hex_iterator_traits<OutputIterator>::value_type>, OutputIterator>::type boost::algorithm::detail::decode_one(InputIterator &, InputIterator, OutputIterator, EndPred) [InputIterator = std
CoreFoundation type mismatch: 
Failed to get Daemon PID
Image info is not supported for the given image type
Diskimageuio: backend is not a FileLocal
, dirty=
futimes failed on 
!Q
Corrupted plist
sha1 too many bytes
ASIF max chunk size in header exceeds the limit
Resource name is too long to fit uint32_t
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
No
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
Couldn't upgrade lock entry
Invalid URL
DiskImageURL
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_write(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
Invalid value for UDIF header field: %s
Starting unmap of 
void di_asif::details::table::set_entry_bitmap_range(ContextASIF &, data_entry_t &, const bits_range_t &, data_entry_t::flags, std::optional<data_entry_t::flags>)
could not create service iterator (begin)
End of input while parsing format specifier precision
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669
 is not supported
Failed to create public key auth entry
locally mounted from %@
fchownat failed for 
-[DiskImageParamsXPC allowOnDiskCacheWithSinkDiskImage:]
The type option contains an invalid value for a string formatting argument
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)
Tag
-[AAS3DownloadSession readToBuffer:size:atOffset:]
The precision option does not contain a value or an argument index
Failed to serialize public key entry to crypto header
Backend: failed reading element in vector
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:437:
lock
set_euid_wrapper::~set_euid_wrapper()
https://%@/v1/ac/decrypt
Cancelling mach ports...
Malformed URL format
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
Missing key in SAKS response
fileBackend
header_size_512 = 512, header_size_4k = 4096
 status=
Can't read encryption table, error 
UDZO
/sbin/umount
System Entities
Skipping erase of band 
Cannot decode path
Punch hole is not supported (err code 
crypto_format: blob length differs
 was just created (truncated)
-[AAS3DownloadSession addRequest:]
Diskimageuio: is cache image failed 
(unrecognized error)
Looking for existing bands
void complete_function_uc(io_connect_t, const DIDeviceCommand &, unsigned int, int)
https://%@
;
://
 rather than image
void SparseBundleBackend::write_primary_info_plist()
ASIF meta header data is unaligned
IsCache
BackendSG
Range: bytes=%llu-%llu
Request timed out
user data retrieving failed
UDSB
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_unmap(const unmap_extent_t *, size_t, future_io_opts_t)
Mode for new files in bundle: 
HTTP request failed with status code: %ld
dataTaskWithRequest
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
 to 
BLX
CFName
Using manual argument numbering in automatic argument numbering mode
Disk image is terminated, skipping future_read
identifier
Write zeros to unmap region failed (err code
-[DIIODaemonDelegate setupExitDaemonWatchdog]_block_invoke
Failed to create XPC connection object
IOBlockStorageDriver
POST
flags validator
-[DIDiskArb unmountWithMountPoint:error:]
Re-enter new password: 
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
secondaryKey
flags
vector
^v8@?0
dirty = bit(0)
%@%@.%@
: [
Unexpected crypto header length (
Got error when trying to close 
size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)
-[NativeDiskImageGraphNode deleteImage]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
UDIF read-only compressed image
key_derivation_algorithm_t
eject
plugin://%@/
-[DIIODaemonDelegate runIOmanager]
size
,Signature=
Invalid user data content
virtual void DiskImageSparseBundle::on_eject()
Failed to parse key in KVS (zero size data).
not 
udzo
, err 
ddm
crypto_format: Can't decrypt wrapped key 
-[DIIOClientDelegate confirmSLAAcceptedWithReply:]
Failed serializing user dictionary
void DiskImage::do_terminate()
auto DiskImageSparseBundle::void_stackable_identifier()::(anonymous class)::operator()() const
Couldn't exclusively lock entry 
ASIF meta header is unaligned
Stable UUID
\\\"
Segmented UDIF images are not supported by this framework
Failed to create dispatch source for kqueue
 closed
Unsupported key decryption algo
Request failed with HTTP error: %lu %@: %@\n%@
The type option contains an invalid value for 
 cannot be re-registered
truncate error: 
Bakcend not initialized for file
Terminating due to unrecoverable I/O error
Compression Info
Failed to read from certificate file 
-[DIConvertParams copyUpdatedOutputURLWithError:]
inputMountedFrom
Diskimageuio: Snapshot detected on top of cache
-[DIBaseServiceDelegate listener:shouldAcceptNewConnection:]
 block_size: 
Unsupported compressed run (
image_variant_type
Unable to convert data to vector.
crypt_consecutive_vector: check errors_in read futures 
mark purgeable failed on 
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
Cannot get subscriber from plugin
int main(int, const char **)
-[DIIOClientDelegate setupNewConnection:]
ulmo
WARNING: this disk image contains a software license agreement that cannot be displayed as text. To read it, open the disk image in the Finder. Continuing accepts the license agreement without reading it.
metadata_flags_t
Couldn't open 
IORegistryEntryGetRegistryEntryID failed
cert-chain
Failed to parse auth data blob.
%12llu bytes downloaded (%.2f MB)\n
AEAHelper: Invalid file descriptor.
virtual int FileLocalAsync::_write(const sg_entry &)
Contains non-hexadecimal characters.
Invalid header: %s
Closing an unchanged 
Couldn't lock entry
Failed to find IO media entry for %@
-[DIIODaemonDelegate attachToNewDeviceWithParams:reply:]
bool DIIOManager::gatherFileMetadata(int, const char *, DIRespawnFileInfo *)
Failed DA init
 size: 
Diskimageuio: Only single cache is allowed
could not create iterator (begin)
Unexpected context construction by 
-
int di_asif::header::write_header(Backend &)
Trying to write @ 
int CommandDispatcherImpl::CommandDispatcherContextImpl::unmap(const Command &)
table entry map@
The image is encrypted with obsolete encoding version 1
 changed before retain completed
ASIF: can't read/allocate asif metadata
rdisk
-bytes block size
raw_header
virtual int SparseBundleBackend::truncate(uint64_t)
Bearer %@
invalid length
checksum_type
More than one image in the stack has the provided tag, please specify UUID instead.
i
Apple Inc
virtual int Backend::read(const elements_t &)
(
 instead
Invalid size of saks response %lu
 op_code: 
index=
exclusive
Cannot find image with provided UUID.
Failed creating notification port
 num_buffers: 
)
Output of disk image conversion must be a file
Cannot stack images with different block sizes
DiskImage::diskimage_extent_t DiskImage::const_extents_iterator_t::make_val() const
device size not found in registry
s3StreamBaseInit
1
metadata_read_only_flags
run_type
Diskimageuio: resolved disk image format 
Cannot load libTestPlugin
IOService
, errno=
diskimageuio: pre-write first error 
Failed to create backend for file %u
com.apple.internal.fetchrestorekeys
Failed to serialize symmetric key to crypto header
-[DIIODaemonDelegate reconnectAfterRespawnWithInstanceID:reply:]
High Throughput Options
plist
auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:
unique_lock::unlock: not locked
Failed to get registry entry ID from dormant device
In-place conversion maintains the encryption passphrase and method. It's not allowed to specify encryption arguments
 io: 
Failed to setup the plugin's IO ring
snapshot
statInstanceID
CyrptoKit is missing a required method.
segment_num_none = 0, segment_num_one = 1
virtual int FileLocalAsync::flush(di_flush_mode)
-[DIResizeParams resizeWithError:]
Diskimageuio: Couldn't get diskimage: 
invalid uuid string
invalid value
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
First block of dir write failed with 
Invalid value for asif header field: %s
Unexpected ASIF header length (
Error creating crypto format
disk arbitration framework returned an error
encodedDict
Failed to get path for shadow %zu
Num extents: 
com.apple.wkms.fcs-key-url
Can't register notification port
virtual size_t BZIPCompressedBackend::compress(const sg_entry &) const
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
Unsupported disk image format
Image contains crypto format but info class is missing EncryptionInfo
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/disk_im
com.apple.diskimages.sla-prompt
disk image
bool DIIOManager::checkForPendingSLA(io_connect_t)
-[DIAttachParams newAttachWithError:]
image_format diskimage_uio::details::diskimage_impl::query_image_format() const
Failed creating CFData
Unsupported URL scheme
forwardLogs
Asif header too large
Invalid argument, please use one of the DICreateParams derived classes instead
ASIF meta header trailer isn't equal to zero
Crypto couldn't write to inner backend @ 
autoMount
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp
-[DIIOClientDelegate addToRefCountWithReply:]
-[DIConvertParams prepareConvertWithError:]
Failed opening folder for entries reading
-[DIShadowChain topDiskImageNumBlocks]
):
bla
Failed to retrieve info
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = di_asif::header]
fd
static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
, dest buffer_size 
com.apple.diskimagespawner.xpc
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
Diskimageuio: bottom diskimage should have role image, but 
Cannot load libAmber
Size cannot exceed max ASIF size
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692
Can't load asif dir version
virtual int FileLocalAsync::truncate(uint64_t)
-[DIIODaemonDelegate tryReconnectToDormantDeviceWithInstanceID:error:]
ASIF: invalid dir index to header
Table flush failed during dir flush: 
Physical block_size is 
The URL encoded into the AEA authdata is missing or invalid.
The format specifier contains malformed Unicode characters
-[DIBaseAgentDelegate createListener]
Password
Invalid block size for image
IOServiceTerminate
metadata
DiskImageSparseBundle::ContextSparseBundle::ContextSparseBundle(DiskImageSparseBundle &)
s3Sign
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = di_hybrid_subscriber_t]
Initialized bands array of size 
Medium Type
com.apple.diskimage.sparsebundle
Couldn't read sparseimage header
Unsupported ASIF, contains data beyond current header struct size
Unaligned metadata entry size
Cannot change passphrase of unencrypted image
w
json
%@: %@
Invalid resource key
Max Sector Count
bytes=%llu-%llu
XPC connection failed
No mapped file for band 
value validator
, retrying
void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)
\\u{
read
Reading 
-I
knox-dev.sd.apple.com
file_handle
Metadata offset is invalid
-[DIIOCacheDelete setupExitTimer:]_block_invoke
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
-n
io_result_t di_asif::details::dir_base::move_realloc_chunk(ContextASIF &, char *, size_t, uint64_t)
Context setup failed.
-[DIDeviceHandle updateBSDNameWithBlockDevice:error:]
iokit error
>
basename_r failed
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr(image_format, std::shared_ptr<Backend> &, bool, const std::filesystem::path &, size_t)
daw
Failed to open user client connection for file descriptor transport
-[DIBaseXPCHandler completeCommandWithError:]
void rawTestPlugin_t::subscriber_t::_resume()
Exception: %s
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = std::__bind<io_result_t (DiskImage::*)(DiskImage::Context &, const sg_entry &), DiskImage *, std::reference_wrapper<DiskImag
Sparsebundles on SMB mounts are not supported on this system
}
Failed to get data from self signed certificate
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:128:22)]
void plugin_encode_buffer(void *, const char *, const void *, size_t)
Failed to initialize IO manager
index
supportsBarrier
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
SparseBundleBackend::SparseBundleBackend(int, bool, const shared_ptr<FileLocal> &, const shared_ptr<crypto::format> &)
The requested URL is an existing folder
GET
None
dispatch_source_create failed
Mandatory callbacks in the plugin's image struct are missing
deserializationError
Failed to create kqueue
AES_KEY = 0x80000001
bundle-backingstore-version
application/octet-stream
The specified image is a folder but not a sparsebundle
could not create service iterator (end)
Image Format
UDIF uncompressed read-only image
This operation doesn't support pstack files
Zero padding cannot be disabled from this process (res=
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocal
diParams
-[DIStatFS initWithFileDescriptor:error:]
di_plugin_image_t *PluginsManager::create_plugin_image(const di_plugin_t &, int, const CFDictionaryRef)
int di_asif::details::dir::defrag_table(ContextASIF &, dir_idx_t)
UDIF: Can't read UDIF trailer
CACHE_DELETE_VOLUME
enc-request
Runs
 (band 
unmapped
udif::details::UDIF_base::UDIF_base(UDIF_header &&)
/dev/%@
User declined SLA
Found 
Daemon already has a device handle
Closing bands
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
US
Master Checksum Info
void rawTestPlugin_t::subscriber_t::_suspend()
UUID
UTF8
%@: %s
 / 
Failed to get canonical path for sandbox extension
ASIF: Content dirty bit is set when reading from disk
Ignoring truncate on block device
AWS4-HMAC-SHA256\n
ASIF: can't copy metadata to mutable copy
Failed to add symmetric key entry to auth table
Disk image is terminated, skipping future_unmap
Unregistering plugin 
AEA key retrieval failed
trim largest: size change callback failed with 
No backends provided for attach params creation
s3HeaderAppendWithFormat
allowStoringInKeychain
Input underlying FS
void udif::details::UDIF_base::validate_runs()
plugin://%@
Key Size
 band contexts
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
absolute_offset
0B
SLA text is empty
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
UDIF: compressed runs should be <= 1MB
 - map_range: [
Requested write is out of range - offset 
Failed to get plugin instance
Cannot decode file descriptor
static autostart_task_t<process_entry_result_t> di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::process_write_entry::operator()(table &, ContextASIF &, table::data_entry_t &&, const sg_vec:
System keychain access is not allowed on this platform
, 
fstat failed
+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]
unmanaged
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
mapped
-[DiskImageParamsXPC createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:]
Cannot find registry entry ID 0x%llx
+[DIError errorWithDomain:code:description:verboseInfo:error:]
Diskimageuio: can't get Diskimage attribute, unknown header format
hdid-pid
Diskimageuio: Unsupported image format
int sparse_bundles::Band::flush()
identityCertificates && [identityCertificates count] >= 1
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Failed to read crypto header for backend %zu: %s
aaS3ContextClone
-[DIBaseXPCHandler installConnectionLostHandlers]_block_invoke
 data: 
com.apple.diskimagesiod.spb
Failed to erase band 
Missing key in KKMS response
Stackable image
disk image password
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)
Chunk Size
has_bitmap
uint32_t FileDescriptor::fetch_physical_block_size() const
diskimageuio: pre-write final error 
KEY_BITS_160 = 160, KEY_BITS_NONE = 0
crypto_header
unmap_iterator_t di_asif::details::table::unmap(ContextASIF &, const unmap_extent_t *, size_t)
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
 was opened in the background, waiting for it to become available
virtual io_result_t sparse_bundles::Band::read(DiskImage::Context &, const sg_entry &)
 with errno: 
wkms-uat.sd.apple.com
NSURLSession read to stream nbyte=%zx offset=%llx\n
BackendZero
 failed wih error 
, errno 
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
iv_tweak_size_t
infnanINFNAN
virtual int SparseBundleBackend::unlock_all()
Dir Pointer Version
static int FileDescriptorWrapper::open_file(const std::string &, int)
%12.2f MB/s download speed\n
can't get Diskimage attribute, unknown header format
vbuf validator
Failed to deserialize crypto format
RootDeviceEntryID
Failed to add passphrase entry to auth table
maxRawUDIFRunSize
Invalid raw UDIF run size limit
band-size
Unmap error: 
BuildVersion
userData
\\n
header_ignore_fields_t
failed to enter SQE to the ring, ret code 
static std::string FileDescriptorWrapper::handle_open_from_error_message(int, const std::string &, int, int)
/
Unexpected failure to get image info: 
Plugin bug: returned init failure without supplying the error
 offset = 
Total Bytes
Checksum Type
false
Diskimageuio: get block size failed 
 is incompatible with the framework, expected 
No WKMS key source available in AEA metadata
Mapped Sectors
 ret: 
> %d %s\n
IOHDIXController
01234567
) is unlocked
fstatfs failed with err code 
, trimmed size
handleRefCount
v1/ac/decrypt
Failed to mount filesystems
%@:%@
BSD Name
ERROR: Response dictionary is missing required keys. Will fail
Failed to open crypto header
Legacy prepended-header UDIF image is not supported by this framework
, allocated: 
io_result_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
Couldn't read asif's full header
 bytes does not fit before the 
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
, disk image is terminated
rings_queue
Blocks header
int BufferedWriteBackend::reset_last_offset(const sg_entry &)
Cancel
-[DIBaseAgentXPCHandler createConnection]
Plugin 
Missing Expected AUTH DATA in AEA.
Request failed: %03ld %s
fskit
Udif: needs to read 
Shadow underlying FS
ASIF: No data offset found (write)
virtual int BackendSG::read(const sg_entry &)
com.apple.diskimagesiod.cachedelete
shadow file
Range:
device_command: 
v16@?0@\"NSString\"8
backend write failed during locked flush of map element, error 
 while expected is 
 (band 0x
Failed truncating 
len: 
Disconnected during SLA prompt
Diskimageuio: query format failed 
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
Background erase of 
-[DIBaseParams prepareImageWithXpcHandler:fileMode:error:]
 auth entry
-[DIShadowChain openWritable:createNonExisting:]_block_invoke
Can't load bitmap while setting range
void udif::details::UDIF_base::generate_blocks(CFArrayRef)
auto FileLocalAsync::shared_state_t::init_unmap_zeros()::(anonymous class)::operator()() const
BSDname
Size Info
virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)
void SparseBundleBackend::write_info_plists()
URL
%@[ramsize=%llu]
 in dir I/O, error 
entire_device
-[DIDeviceHandle waitForQuietWithService:error:]
hw.memsize
clientID
Failed locking the image
Run interval: 
Stack with cache as top image cannot be opened for writing.
Size
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
Shadow block size is invalid (0)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
Root daemon connection denied
leaf-cert
AmberDiskImagePluginCreate
 is 
diskimageuio: report err 
Trying to read @ 
Cannot find BSD name in IO media service
Failed to find dormant device
-[DIDiskArbEmulation waitForDAMountWithExpectedCount:diskTracker:]
Cannot retrieve passphrase from user via TTY or GUI
outputParams
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)_block_invoke
v24@?0@\"DIDeviceHandle\"8@\"NSError\"16
NO
Disk image is terminated, skipping unmap
Content-Type
Not valid SAKS metadata (json format expected)
 (error code 
-[DICreateParams createDiskImageParamsWithError:]
Can't lock entry
] = 
system error
Failed opening mapped blocks file for 
band_ptr DiskImageSparseBundle::replace_oldest_band(Band *)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293
Unexpected backend replace request
ULMO
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
udsb
unexpected error
ShadowChain: %@
Root dir flush failed, error 
 errno: 
createErrorContextKey
com.apple.di_raw_test_plugin
public_key_crypto_algo
s3HeaderAppend
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
Incorrect passphrase
Could not generate OIDC token - AppleConnect Failure
Missing key in Knox response
 bytes is smaller than its trailer
bool sparse_bundles::mapped_blocks_t::load_file()
PersistentAttach
Retrying request after %.0f seconds %zu bytes at offset %llu
0123456789abcdefghijklmnopqrstuvwxyz
set_euid_wrapper::set_euid_wrapper(uid_t)
-[DIIOCacheDelete setupNewConnection:]
KVS data fetch failure.
-[DIDiskArb waitForDAIdleWithError:]
.xpc
Udif: advanced buffer, needs to read 
Can't connect to device
disk
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c
Range
User-Agent
unmap
Images
ASIF: can't set requested uuid
[
Invalid UDIF, run is not within block boundary
/dev/rdisk
-[DIEncryptionFrontend storeInKeychainWithPassphrase:forceSystemKeychain:error:]
BZIP decompression failed, res=
Destroying File backend, but in-flight promises exist
RAW
Not valid SAKS metadata (no environment field)
Failed creating property list
+[DICreateParams eraseIfExistingWithURL:error:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__hash_table:1892: lib
Can't load table to get extents
-[DIDeviceHandle dealloc]
 
remote mount
Error: Not enough data read. expected: 
Diskimageuio: get nr blocks failed 
 failed, error 
Failed to find DiskImages2 controller, driver might not be installed
Could not generate daw token - AppleConnect Failure
Not allowed more than one instance of 
Can't create data for plist deserialization
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
unsigned char boost::algorithm::detail::hex_char_to_int(T) [T = char]
Parent UUID
Evicting all bands for eject
Unmapped Entries
trailer of a 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Compression Ratio
-[DIIODaemonDelegate setupSigtermHandler]_block_invoke
Error: failed to unwrap key. Error: %s\n
Locked encrypted image
Context creation failed.
bool ref::details::ctrl_blk<CurrentReader, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = CurrentReader, tag_t = unsigned long long]
AES-CBC
Preferred Block Size
New password
uninit
addRequest
user data embedding failed
-[DIEncryptionChpass unlockWithPassphrase:error:]
Cannot initialize pstack disk image without path.
Diskimageuio: Unrecognized image format.
Diskimageuio: get stackable uuid failed 
stat failed
 of type 
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
Internal backend read() failed. ret=
 backend size 
xpc error
diskImageParams
Failed to subscribe to the plugin's IO ring
CFUserNotificationReceiveResponse failed
plugin
void info::DiskImageInfoASIF::count_used_extents(const DiskImageASIF &)
Unable to get matching services
File system is 
wrap_key_crypto_padding_algo
Crypto: Unsupported encryption parameters
BufferedWriteBackend
Completed erase of band 
disk image kernel return
Registry entry ID mismatch between controller and daemon
9999
Invalid path property (not a path or URL)
kern.aioprocmax
XPC connection interrupted
 err: 
Couldn't read asif's header
Not enough space for metadata
File (fd 
void di_hybrid_subscriber_t::resume()
Min Size Bytes
shadow-path
openid,dsid,accountname
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
The width option should not have a leading zero
Failed initializing shared buffers
Failed opening the file
attempting to authenticate with wkms
Malformed SLA LPic resource
Key from the certificate is not exportable
Accept
Diskimageuio: images with constraints currently not supported
Overflow detected
uint64_t udif::details::UDIF_base::write_resources(CFDictionaryRef)
wrap_key_crypto_algo
Decoding error.
Image doesn't support resizing
Diskimageuio: locked backend 
Corrupted plist dictionary
Unexpected UDIF header length (
Unexpected backend type for shadow file
Can't read bitmap
, keeping file unlocked
, res=
Authorization: %s
ShadowURL
+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
Starting flush
Failed writing first block of dir
thread constructor failed
Is Encrypted
CacheURL
write
!\"
Diskimageuio: Couldn't lock backend 
Image key encoding failed with err code 
CBCPADIV8 = 6
crypto header contains invalid number of auth entries
pkce
Placed new 
Cannot acquire 
-[DIIODaemonDelegate reopenStashedFilesWithUserClient:outBackends:error:]_block_invoke
Spawner failed to reopen file %u: %@
s3DownloadStreamOpen_urlsession
Cannot lock bundle, ignoring: 
UDIFDiskImage: failed truncating image
UDIF: Failed converting type array string (
fstatfs failed with err code
SHA1_HMAC = 91, NONE = 0
crypto_op: can't initializae aes_cbc context
Crypto: can't read crypto header
BufferedWriteBackend doesn't support per io crypto
0b
io_result_t DiskImageSparseBundle::perform_io(ContextSparseBundle &, bool, const sg_entry &)
Disk image is terminated, skipping read
image-path
passphrase
 and property 
Daemon no longer available
wrapped-key
sparsebundle
version_t
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486:
inputURL
Shadow
hit
void DIIOManager::drainDormantQueue()
auto
version_1 = 1, version_2 = 2, version_3 = 3
devicePrivateKey
: 
environment
Error reading sectors for verify 
Final asif 
DELETE
%s: 
fetch_restore_key/%s OS/%@
Plugin struct size 
kern_return_t was 
CKIE
A second controller XPC service attempted to create a new device
\\'
Diskimageuio: backend doesn't exist
 bytes are above the sparsebundle limit of 
virtual int FileLocalAsync::disable_file_zero_padding() const
 lock, errno 
Single element in pstack that isn't an image
NONE = 0
-[DIClient2IODaemonXPCHandler cancelSLAWithReason:]
char *udif::header::write(char *)
virtual int Ram::_read(const sg_entry &)
Error decrypting data using public key, error code 
PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0
total_size
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
The format string contains an invalid escape sequence
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
 returned status 
com.apple.diskimages2
-[DIVerifyParams verifyWithError:]
header_flags
malloc
header_size_t
Plugin's ring resumed, ret code 
Cannot save DiskImageGraph without specifying pstack URL
CFUserNotificationCreate failed, error code %d
rawTestPlugin_t::~rawTestPlugin_t()
-[DIIOClientDelegate cancelSLAWithReason:reply:]
asif: chunk size is too small, too many dir indices
com.apple.wkms.fcs-response
Invalid knox URL format. Expected: knox://host/download/space/digest
Failed during ASIF extents enumeration.
static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
%s (%@)
{:02x}{:02x}
Diskimageuio: Can't get image format
getErrorContextKey
Error creating disk image params
isCache
table flush failed during close: 
Backend barrier failed during bitmap allocator failures handling, error 
header read-only flags
Disk image is terminated, skipping write
ERROR: Shipping private key is NULL.
Unsupported host for OIDC: %@
 doesn't exist, returning zeros
UDIF - max compressed run size: 
intermediate-certs
curl_easy_init failed\n
Skipping erase of 
<
Failed to read metadata 
void sparse_bundles::mapped_blocks_t::map_range(uint64_t, uint64_t)
missing DI_ATTACH_ENTITLEMENT on non macos platform
Couldn't write asif's header
^{__CFDictionary=}20@?0i8^{__CFDictionary=}12
Non supported options in AAS3DownloadSession (ignored): proxy_headers %s
-t
Cannot attach RAM disk with a shadow or a cache file
high throughput
certificate
File size is less than the minimum header size
user metadata
IO returned an error for command 
virtual void ExecutionEngineCommand<CommandQueue, MachPort>::signal_terminate() [Container = CommandQueue, Port = MachPort]
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
ASIF: data entry - invalid reserved bits
UDIF: Can't get types array from UDIF
 error = 
applicationId
curl_slist_append failed\n
shadowChain
Can't load bitmap while flushing asif table 
sig1_t
auth-data
&
void plugin_encode_fd(void *, const char *, int)
NSURLSession read to buffer nbyte=%zx offset=%llx\n
Can't read encryption entry header, error 
-[DIIODaemonDelegate exitDaemon]
managed future err 
Failed converting URL to UTF8
Close completed
locale-specific form
Diskimageuio: reopen backend to required mode 
AppleDiskImagesController
' with flags 
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_write_iov_t]
Stack Info
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c
userDict cannot be nil or empty
virtual DiskImageSparseBundle::~DiskImageSparseBundle()_block_invoke
downloadStreamPRead
The symmteric key is wrong
not a disk image
 updated from 
Couldn't trim entry in read 
Disk image is terminated, skipping ...
ulfo
Couldn't trim entry in write 
-[DIDiskArbEmulation unmountWithMountPoint:error:]
flags_t
segment_num_t
is_writable
IOBlockStorageDevice
1.0
B24@?0@\"NSURL\"8@\"NSError\"16
diskimagesuio: future read invalid in read
Decryption key missing
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
Barrier failed after defrag, error 
full_fsync
0x
com.apple.knox.url
v16@?0Q8
 size = 
^%@.*\\.%@$
X-Amz-Content-Sha256: %s
, Force closing.
) is locked
s3Perform
Key is not hexadecimal number.
debugLogsEnabled
-[DIIODaemonDelegate setupNewConnection:]
sendEvent of type 
Unsupported image stacking
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
no more attempts allowed
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
 existing bands
Can't serialize property list
Calling 
bytes=
-[DIDiskMountTracker trackIfMyDisk:]
com.apple.diskimages.band_unmap
Can't allocate mach port
PUT
attempting to authenticate with aea key
invalid header: %s
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke
-[DIIOClientDelegate setupNewConnection:]_block_invoke
bool DIIOManager::stashFileInformation(DIAttachParams *__strong)
-[DIConvertParams shouldPerformInplaceSquash]
Write error: 
Failed creating IO iterator, err code %d
-[DIIODaemonDelegate createShadowNodeWithBackend:fileIndex:error:]
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
Agree Y/N? 
 buffer_size: 
pstack: unsupported node
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
band_ptr DiskImageSparseBundle::find_band_in_array(uint64_t)
Failed to update asif header
Internal backend write() failed. ret=
BackendNull
Sector count is too large
Cannot delete base image node.
Cannot edit crypto header that has more than 
/sbin/mount
 bytes, reading only 
knox-uat.sd.apple.com
encryption_mode
ftruncate failed, errno: 
virtual int FileLocalAsync::lock()
com.apple.diskimagesio_
euqueueRequest timed out
outputFormat
Passphrase is too long
read write
 doesn't exist
void SparseBundleBackend::read_info()
Sparse bundle ejected
alternate form
device not found in registry
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
location
, flags = 
partition_num: 
Encountered an irrecoverable I/O error, all future I/Os will be invalidated
 = offset = 
regEntryID
Can't allocate ports array in driver
Verify
flush
 folder
Failed to validate metadata 
Using compression 
uuid
void rawTestPlugin_t::subscriber_t::_cancel()
header (
UDIF: Can't get resource array
AEA
void boost::uuids::detail::sha1::process_byte(unsigned char)
bool DIIOManager::fetchRequestsStat(DIRequestsStatsArray *)
???
The type does not fit in the mask
fileMode
Diskimageuio: backend isn't locked
Diskimageuio: required mode 
com.apple.diskimage-test-plugin.raw
Kernel returned error for complete command, command = 
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
wkms.sd.apple.com
Failed to update internal state after resize
Failed initializing RAM disk buffers
UDIF: compression algo is invalid
UDIF: Can't create dictionary resource fork
could not create iterator (end)
Failed opening the shadow/cache file(s)
is_locked
Validation failed for dictionary key %@.
offset
/s3/aws4_request,SignedHeaders=
static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)
, error 
udifHeader
ssize_t plugin_decode_buffer(void *, const char *, void **)
 for 
PluginParams
The value of the argument index exceeds its maximum value
Diskimageuio: Nested stacking is not allowed.
Basic information about the IOMedia device is missing
hw.logicalcpu
is_aea: Error reading magic.
UDZOMAX
com.apple.wkms.url
-[DIDiskArb onDiskDisappearedWithDisk:]
Failed to add public key entry to auth table
udro
void boost::uuids::string_generator::throw_invalid() const
Error with decryption key size
-C
Failed to open backend of crypto header
The argument index starts with an invalid character
diskimage-bundle-type
bool ref::details::ctrl_blk<di_asif::details::table, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::table, tag_t = unsigned long long]
ASIF: table is not aligned to chunk size
Invalid ASIF header size
io_result_t DiskImage::Context::read(const sg_vec::iterator &, const sg_vec::iterator &)
-[DIDiskArb addDisappearedCallbackWithMountPoint:shadowMountPoints:delegate:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433:
ASIF: metadata header out of range
File descriptor 
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::verify_backend() const
Failed creating the image
virtual DiskImageSparseBundle::~DiskImageSparseBundle()
com.apple.DiskImages2
 not found in registry
Disk image is terminated, skipping flush
Device Characteristics
 backend: 
virtual int DiskImageSparseBundle::set_size_impl(uint64_t)
ASIF: failed to deserialize metadata
slaText
prod
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
Plugin's async ring cancelled, ret code 
com.apple.diskimagesiod.ram
Failed during data entry write in table write, error 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
 exceeds the maximum of 
gcd::gcd_timer_source::gcd_timer_source(gcd_queue &, dispatch_time_t, uint64_t, uint64_t)
 is clean, skipping flush
ERROR: wrapped-key failed base64 decode
zlib
The operation was cancelled by the user
Block device block size is larger than image block size
Allocated after defrag: 
device with class 
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_flush(di_flush_mode, future_io_opts_t)
void space_allocators::FixedSize::trim_largest(const size_changed_fn_t &)
-[DIBaseXPCHandler init]
Is Cache
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
=
 - unmap_range: [
-[DIDiskArb waitForDAMountWithExpectedCount:diskTracker:]
Error creating (unlocked) backend
int sparse_bundles::mapped_blocks_t::flush()
IO handling of attached disk image
IOMedia
ASIF: failed to write metadata
pthread_key_create
Bands folder contains an out of range band (
The image is encrypted but has no passphrase auth entry
commandSize
Diskimageuio: ASIF header changed while unlocked
/usr/local/bin/appleconnect
ASIF: Header size is less than the min header size
Device is not a disk image
v28@?0Q8^{dispatch_mach_msg_s=}16i24
gcd_kqueue: kevent64 failed with ENOMEM
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
createTask
Daemon PID
Disk image is terminated, skipping future_flush
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:429:
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
special: 
Cannot stat 
crypto_format: Can't derive key 
The image was unlocked before setting userData
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Harde
map_element flush failed on creation
Trimming: Written 
Diskimageuio: Failed to create resizer: 
static int SparseBundleBackend::open_bundle(const string &, int)
numBlocks
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
virtual int CompressedBackend::read(const sg_entry &)
Closed band at index 
Can't flush asif on map element close, backend barrier failed
static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
Failed to write metadata
' opened successfully with flags 
-[DIDiskMountTracker onDiskAppearedWithDiskName:isMountable:]
virtual int CommandDispatcherImpl::CommandDispatcherContextImpl::execute(Command &)
Invalid chunk size
Diskimageuio: Required read-write disk image (
Reserved part isn't zeroed
User data contains reserved key(s)
Nothing to defrag
blocks_signature
none = 0, crc28 = 1, crc32 = 2, dc42 = 3, md5 = 4, sha = 5, sha1 = 6, sha256 = 7, sha384 = 8, sha512 = 9, none_valid = 10
 (our euid is 
Failed to dup fd for file %u
keys/fetch
invalid field %u
, truncating
+[AAS3DownloadSession completeRequest:data:response:error:]
RO
Failed reading 
knox
UDIF XML length 
crypto_op: can't initializae aes_xts context
Writing 
Shadow path %@ is not a valid file
bool DIIOManager::requestGracefulShutdown()
Invalid UDIF format, contains intersected blocks
UDIF header doesn't contain a valid sector count, using runs upper value: 
Not a pstack.
-[DIStatFS logWithHeader:]
Can't read for defrag
!1
 io_size: 
fetch_restore_keys_ephemeral
 extents
bool ref::details::ctrl_blk<di_asif::details::map_element, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::map_element, tag_t = unsigned long long]
Error writing file @ 
IOServiceOpen failed
fetch_restore_keys self signed cert
ZLIB = 0, LZFSE = 1, LZMA = 2, ZLIB_9 = 3, BZIP = 4
DIErrorVerboseInfo
The disk image format is not supported by this OS
Unsupported value for crypto header field 
 constant 
device_OBSOLETE = 0, device = 1, partition = 2
invalid file size for 
ULFO
Can't flush asif on table close, backend barrier failed
int DiskImage::Context::unmap(const unmap_extent_t *, size_t)
Missing image path property
pstack
 [
expected<image_format, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::query_image_format() const
failed to set euid to 
band 
v16@?0@\"NSTimer\"8
-[DIIODaemonDelegate setupNewConnection:]_block_invoke
 bands flushed, calling 
(unlocked)
ASIF meta header failed to read
], cmd=
%.*s: Received: %{public}@
%.*s: On disk cache path: %{public}@
%.*s: Graceful shutdown failed - falling back to normal shutdown
%.*s: Failed to add shadow nodes to chain: %{public}@
%.*s: IOServiceOpen returned %d
%.*s: Unmounting %{private}@
%.*s: SLA: unusable LPic resource
%.*s: Due to the conversion error, erasing the output file
%.*s: Failed to create graph from plist: %@.
%.*s: Using %{private}@ as read-only
%.*s: Successfully drained dormant I/O queue after daemon respawn
%.*s: Terminating cache delete instance due to SIGTERM
%.*s: Mount Disk: %@
%.*s: Graceful shutdown already initiated by SIGTERM - exiting immediately
%.*s: Failed creating unmount done semaphore
%.*s: Disabling reference counting
%.*s: Error encoding user dictionary: %{public}@
%.*s: Client confirmed SLA acceptance
%.*s: Retrieved %u files from kernel
%.*s: SLA: failed to decode %s resource ID %d with encoding 0x%x
%.*s: User data retrieving passed, %d value(s) found
%.*s: Appeared Disk: %@
%.*s: IOServiceWaitQuiet timeout occurred, retrying.
%.*s: XPC connection closed for a managed attach, # open connections left: %lu
%.*s: Waiting for disk arbitration to finish mount
%.*s: Asking for passphrase using readpassphrase
%.*s: Registry entry ID is 0, can't check %s property
%.*s: Received connection from pid %d with euid %d. Our euid is %d
%.*s: A new client has connected to the clients listener
%.*s: SLA resource has no text form, prompting with a warning instead
%.*s: fstat failed for fd %d: errno=%d
%.*s: Failed initializing plugin: %{public}@
%.*s: Shared buffer size: %-10d Read only:          %-6s Command size:  %ld
%.*s: Reached with diskURL=%{public}@
%.*s: %{public}s, errno=%d
%.*s: Reached an interruption handler for an attached client
%.*s: Exit already in progress
%.*s: I/O error at offset %lld iov_count %d errno %d
%.*s: On disk cache is not supported on embedded systems
%.*s: DIDeviceHandle object is deallocating, invalidating connection
%.*s: Forcing unmount of %{private}@ (%{public}@)
%.*s: SLA: non-numeric resource ID string, skipping
%.*s: Not a pstack
%.*s: Creating connection with %{public}@
%.*s: Mountable Disk: %@
%.*s: Reached an interruption handler for an attached controller service
%.*s: Creating connection to IO daemon clients listener
%.*s: Daemon successfully reconnected to dormant device
%.*s: fcntl(F_GETPATH) failed for %s: errno=%d
%.*s: Failed to generate device identity: %@
%.*s: Using an existing cache file %{private}@ with RO access
%.*s: Failed creating queue
%.*s: Cache delete periodic registered
%.*s: Reached an invalidation handler for an attached client
%.*s: Max IO size:        %-10d Num shared buffers: %-6d Extra buffers: %d
%.*s: Stashed encryption keys for %s (key=%u bytes, secondary=%u bytes)
%.*s: Mount error: %@
%.*s: Failed getting mounts list
%.*s: Failed to dup stdout: %d
%.*s: Successfully stashed %u files for daemon respawn
%.*s: User data embedding passed
%.*s: %{public}@ %{public}@
%.*s: entry, instance ID = %{public}@, registry entry ID = 0x%llx
%.*s: As we were launched without instance ID, rejecting the connection and killing the daemon.
%.*s: The rejected connection caused a daemon instance to wake up. Killing it
%.*s: Waiting for disk arbitration idle
%.*s: Decoding plugin instance
%.*s: Missing sandbox token for shadow file %lu
%.*s: Failed looking up %{public}@: %{public}@
%.*s: Unmount timeout occurred
%.*s: The connected client is not entitled to attach a disk image, rejecting
%.*s: Respawn with %zu shadow files detected - recreating shadow chain
%.*s: Found dormant device with registry entry ID: 0x%llx
%.*s: Failed with status %d
%.*s: Cannot open shadow chain %{private}@ with RW access: %{public}s, errno=%d
%.*s: Creating %s plugin instance with params: %@
%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported
%.*s: Failed to connect to IO daemon for SLA handling
%.*s: Missing parameters
%.*s: Failed during ASIF extents enumeration on offset: %llu
%.*s: Failed to find IOMedia entry for %@
%.*s: IO was not fully started, quitting immediately
%.*s: Failed to dup stderr: %d
%.*s: CacheDelete registration failed
%.*s: Unmanaged attach, ignoring XPC disconnection (# open connections left: %lu)
%.*s: Failed to open /dev/tty: %d, falling back to stderr
%.*s: Failed to copy source disk image to temporary URL
%.*s: Failed creating semaphore
%.*s: Image file %{private}@ opened with flags %d
%.*s: Connection to cache delete instance is not allowed, quitting
%.*s: Keeping RO mode for %{private}@
%.*s: Invalid key: %@
%.*s: Using existing disk image params
%.*s: <%lu> %{public}s
%.*s: Backend for %s does not support file descriptor access - cannot stash for respawn
%.*s: Reached an invalidation handler for the IO daemon connection
%.*s: SIGTERM: supportsPersistent = %d
%.*s: Device is already ejected, skipping unmount
%.*s: Reached an invalidation handler for an attached controller service
%.*s: IOAllocatePortsArrayCallMethod returned %d
%.*s: Image %{private}@ re-opened with RW permissions
%.*s: Failed to delete %@: %@
%.*s: Root daemon must be launched with an instance
%.*s: fetch failed
%.*s: IOConnectCallMethod returned %d
%.*s: Last access time expired for %{public}@ (%.2f days), removing
%.*s: Client cancelled SLA: %{public}@
%.*s: Successfully retrieved WKMS shipping key
%.*s: Successfully retrieved WKMS non-shipping key
%.*s: Erasing %{private}@
%.*s: Shadow file %{private}@ opened with RW access
%.*s: Could not determine cache dir
%.*s: %{public}@ mounted successfully
%.*s: Disk image resized to %llu bytes
%.*s: Cannot open cache file %{private}@ with RW access, trying read-only
%.*s: XPC connection disconnected during SLA wait, cancelling attach
%.*s: Successfully reconstructed crypto layer for encrypted backend %zu
%.*s: Failed to open pager, writing directly to stdout
%.*s: Failed instantiating rawTestPlugin object: %s (code %d)
%.*s: No sandbox extension token for file %u (%s) - cannot stash for respawn
%.*s: Disk mount wait skipped (emulation mode)
%.*s: Keychain lookup returned %d
%.*s: Creation failed, erasing %{private}@
%.*s: Can't allocate memory for shared buffers
%.*s: Failed to remove %{public}@: %{public}@
%.*s: Summary: removed %u files (%llu MB) out of %u files (%llu MB) of cache
%.*s: Daemon initialization failed. Quitting.
%.*s: %{public}s, status = %d
%.*s: Validation exception: %{public}s
%.*s: Unmount done
%.*s: Failed to read passphrase from TTY
%.*s: Using an existing shadow file: %{private}@
%.*s: Copied sandbox extension token from reopened backend (length=%zu)
%.*s: Terminating due to SIGTERM
%.*s: Unlocked using public key
%.*s: Failed to get UUID info of provided image.
%.*s: Got error from last XPC command: %{public}@
%.*s: Cache file %{private}@ opened with RW access
%.*s: fstatfs failed for fd %d: errno=%d
%.*s: Failed to get block device for disk %@
%.*s: Input and output files are the same, using a temporary output file
%.*s: Reached an interruption handler for the IO daemon connection
%.*s: Creating connection to %{public}@
%.*s: Connected client is entitled to attach a disk image
%.*s: No usable SLA text found in UDIF resources
%.*s: A valid plist was given, but it has no pstack version key
%.*s: XML_RSRC_FORK: %{public}@
%.*s: Shutting down cache delete instance
%.*s: Force unmount of %{private}@ failed with errno %d
%.*s: Keychain item requires ACL upgrade
%.*s: Failed to erase output URL
%.*s: %{public}@ error %{public}@
%.*s: Not a UDIF: %{public}s, assuming RAW format
%.*s: XPC error connecting to spawner: %@
%.*s: New disk image size is the same as previous
%.*s: numBlocks queried for an empty shadowChain.
%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization
%.*s: Out of memory, failed to allocated %zu bytes for key %@
%.*s: fcntl(F_GETPATH) failed for shadow file %zu: errno=%d
[0x%08x] %{public}s
%.*s: Ejecting %@
%.*s: # client connections at time of daemon termination: %lu
%.*s: Reached XPC invalidation/interruption before device initialization, quitting.
%.*s: %{public}@ - %{public}@ %{public}@
%.*s: %@
%.*s: %{public}s
%.*s: Closing IO user client
%.*s: Looking for encrypted image passphrase in the %s keychain
%.*s: Ignoring, during shutdown
%.*s: Passphrase found in keychain, unlocking the image
%.*s: Failed reading default cache size
%.*s: Dispatching DIIOManager
%.*s: %{private}@ unmounted successfully
%.*s: Reached periodic cache delete with urgency %d, volume: %{private}@
%.*s: IO daemon of %{public}@ is shutting down, stopping IO channels
%.*s: Failed for file %u (fd=%d) with status %d
%.*s: Performing in-place squash optimization
%.*s: Failed to extract encryption keys for file %u (%s)
%.*s: Too many shadow files - max %d supported
%.*s: Storing passphrase in the %s keychain
%.*s: Failed to dup2 to stdout: %d
%.*s: Issuing new sandbox extension token for file %{private}@
%.*s: %@ ejected successfully
%.*s: Exception reading/parsing crypto header for backend %zu: %s
%.*s: Asking user permission to store the passphrase in the keychain
%.*s: fcntl(F_GETFL) failed for fd %d: errno=%d
%.*s: Failed retrieving property for %{public}@: %{public}@
%.*s: Reached, keeping connection alive
%.*s: Exit daemon timeout (%d sec) expired
%.*s: Disk arbitration idle callback received
%.*s: Registering DiskDisappearedCallback for %{private}@
%.*s: res_dict: %{public}@
%.*s: Queue depth:        %-10u ABI version:        %d
%.*s: No matching item found in keychain
%.*s: Error checking %s property: %s
%.*s: Moving %{private}@ to %{private}@
%.*s: IO daemon euid: %d, pid: %d, isRAM: %d, IOpolicy process=%d thread=%d
%.*s: Got connection to an existing disk image, returning its handle
[0x%08x](warning) %{public}s
%.*s: Not a sparseimage: %{public}s
%.*s: Failed to open top disk image node.
%.*s: Successfully issued sandbox extension token for file %{private}s (token length: %zu bytes)
%.*s: IO daemon path: %{public}@
%.*s: Run loop aborted
%.*s: Shutdown is complete
%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)
%.*s: Skipping %{public}@ (last access time was %.2f days ago)
%.*s: Daemon failed to reconnect to dormant device: %{public}@
%.*s: CacheDelete is not supported, daemon was launched unexpectedly without an instance ID
%.*s: Mount point %{private}@ disappeared
%.*s: entry: %{public}@
%.*s: XPC connection lost: %{public}@
%.*s: WARNING: Found %llu sectors with invalid flags (has_bitmap)
%.*s: Invalid arguments specified
%.*s: BSD name: %{public}@
%.*s: # of active connections: %lu
%.*s: Exception occurred: %{public}@
%.*s: Passphrase is correct
%.*s: Pager command failed with status %d, output may be incomplete
%.*s: File system is %{public}s
%.*s: Failed to wrap backend %zu with encryption
%.*s: Registering DiskDisappearedCallback for %{private}@ (shadow's mount point)
%.*s: Shadow format validator exception: %{public}s
%.*s: Dormant device reconnection complete
%.*s: isWritableFormat: %s
%.*s: entry with %{private}@
%.*s: Retrieved %zu backends from kernel
%.*s: Mount point %{private}@ disappeared (shadow's mount point)
%.*s: Ignoring client reference counting request as a previous attach was performed without reference counting
%.*s: Disk arbitration mount completed
%.*s: cancelSLA wait returned error: %{public}@
%.*s: Failed opening %{private}s, errno %d
%.*s: IOServiceWaitQuiet done
%.*s: Encrypted backend %zu detected (%zu key bytes) - reconstructing crypto layer
%.*s: Creating NSXPC listener on %{public}@
%.*s: Reached termination callback, stopping the daemon.
%.*s: Instance ID: %{public}s
%.*s: Failed to get IOMedia during respawn
%.*s: Unlocked using symmetric key
%.*s: SLA detected, connecting to IO daemon for user acceptance
addRequest:
initWithEndpoint:
initWithURL:error:
isUnlocked
_persistentConnection
count
onDiskDisappearedWithDisk:
setPassEntryToChange:
_shouldValidate
TQ,N,V_regEntryID
initWithSession:size:atOffset:destinationBuffer:destinationStream:completionSemaphore:
initWithURL:key:
isKindOfClass:
readToBuffer:size:atOffset:
requiresRootDaemon
addDecendantsToArray:
arrayWithObjects:count:
getCertificateWithCertificatePath:error:
initWithGraphDB:error:
sendSynchronousRequest:returningResponse:error:
pid
URLWithString:
_cacheLock
errorWithDomain:code:userInfo:
initWithURL:fileOpenFlags:bandSize:
setHandleRefCount:
url
buf
copyDefaultLocalizedStringForDIErrorCode:
folderCopyXPCHandler
integerValue
isFileURL
nilWithDIException:prefix:error:
T@\"NSError\",C,N,V_deserializationError
T@\"NSNumber\",R,N,V_overrideBlockSize
TB,R,N,V_isRAM
_xpcError
isMemberOfClass:
runLoopSource
shadowURL
T@\"DiskImageGraphNode\",R,N
T@\"NSString\",&,N,V_tag
_tag
convertPrivateKeyTox963WithPemPrivateKey:error:
copyUnmatchedDiskImageWithRegEntryID:error:
regularExpressionWithPattern:options:error:
setInputMountedOnURL:
T@\"NSString\",R,N,V_pluginName
setDaSession:
synchronousRemoteObjectProxyWithErrorHandler:
setFileBackend:
completeRequest:data:response:error:
fillDI2InfoWithDevice:error:
popObjectForKey:
setDI2PIDWithDevice:error:
setSlaCompletionReply:
unsignedLongLongValue
Tq,N,V_fileMode
JSONObjectWithData:options:error:
T@\"DIClient2Controller_XPCHandler\",&,N,V_folderCopyXPCHandler
T@\"NSMutableSet\",&,N,V_myDisks
_isPrivileged
jsonResponseWithRequest:session:error:
T@\"NSString\",R,C,N,V_instanceId
CLIVerifyPassphrasePromptCreate
_shadowURLs
pstackURL
T@\"NSArray\",&,N,V_handles
_regEntryID
_url
finalizePostStartIO:waitForDevice:error:
initWithUnsignedShort:
waitUntilExit
_offset
_frameworkNum
initWithClassName:error:
inputMountedFrom
setSizeWithDiskImage:newSize:
T@\"DIURL\",R,N,V_URL
T^{__CFRunLoopSource=},N,V_runLoopSource
requestSynchronousDataWithRequest:session:error:
semaphore
supportsPersistentAttach
_fileBackend
_remoteProxy
baseNode
outputURL
setEncryptionInfoOnly:
setUUID:
Tf,R,V_pauseInterval
unlockWithXpcHandler:error:
mutableChildren
T@\"DITemporaryPassphrase\",R,N,V_temporaryPassphrase
readPassphraseFlags
T@\"DIDiskMountTracker\",W,V_diskTracker
_encryptionMethod
addSymmetricKeyEntryWithError:
auth_table
copyDictNodesToFolder:dict:error:
fileHandleForReadingFromURL:error:
initWithObjectsAndKeys:
initWithURL:size:error:
GUIPassphrasePromptCreate
T@\"<DIDisappearedMountPointDelegate>\",W,N,V_delegate
slaText
TQ,N,V_blockSize
T^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v},V_stream
class
copyUpdatedOutputURLWithError:
createShadowNodeWithBackend:fileIndex:error:
encodeInt64:forKey:
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
```
