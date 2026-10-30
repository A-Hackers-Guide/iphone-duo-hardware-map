# `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,950,288 bytes.

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
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}16@0:8
v40@0:8@\"DIEncryptionFrontend\"16q24@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">32
@\"NSError\"
{expected<std::shared_ptr<Backend>, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<std::shared_ptr<Backend>, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<std::s
B24@0:8^@16
v24@0:8*16
@28@0:8i16^@20
@\"DIURL\"
{expected<diskimage_uio::diskimage_open_params, std::error_code>=(storage<diskimage_uio::diskimage_open_params, std::error_code>=c{diskimage_open_params=^{diskimage_open_params_impl}}{error_code=i^{error_category}})B}16@0:8
@40@0:8:16@24@32
i
B48@0:8r^{AuthData=^{AEAAuthData_impl}}16*24Q32^@40
{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>={?=^{DiskImageInfo}}}28@0:8B16^@20
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
B40@0:8@16^@24^@32
*
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}
@32@0:8q16@24
B32@0:8Q16^@24
v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}16
v32@0:8@\"DIDeviceHandle\"16@?<v@?@\"NSError\">24
B32@0:8@16@24
q16@0:8
@24@0:8r^v16
@40@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16^@32
B44@0:8@16#24B32^@36
@\"NSProgress\"32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24
Ai
@24@0:8r*16
B32@0:8@16^@24
v20@0:8i16
@32@0:8:16@24
v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24
@40@0:8@16@24^@32
B40@0:8Q16^v24^@32
@\"DIBaseParams\"
B40@0:8@16q24^@32
@\"BackendXPC\"
@\"NSNumber\"
@\"NSMutableData\"
{shared_ptr<unsigned char>=\"__ptr_\"*\"__cntrl_\"^{__shared_weak_count}}
B36@0:8i16@20^@28
{shared_ptr<crypto::header>=\"__ptr_\"^{header}\"__cntrl_\"^{__shared_weak_count}}
v32@0:8@\"DIEncryptionFrontend\"16@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">24
v40@0:8@\"DIEncryptionCreator\"16@\"NSString\"24@?<v@?@\"DIEncryptionCreator\"@\"NSError\">32
B28@0:8B16^@20
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}
v32@0:8@\"DIStatsParams\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
B24@0:8:16
v24@0:8@?<v@?@\"NSError\">16
v20@0:8B16
B24@0:8@16
@\"NSString\"
@32@0:8Q16^@24
@\"DiskImageGraphNode\"
@68@0:8@16@24@32@40@48@56B64
B40@0:8*16@24^@32
@36@0:8@16B24^@28
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@\"NSXPCListenerEndpoint\"
*16@0:8
v48@0:8@16@24@32@40
@32@0:8r^v16@24
B28@0:8I16^@20
B48@0:8@16q24@32^@40
B36@0:8B16q20^@28
{shared_ptr<DiskImage>=^{DiskImage}^{__shared_weak_count}}60@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16Q32r^v40B48Q52
@\"NSProgress\"
@48@0:8@16@24@32^@40
v40@0:8@16q24@?32
B24@0:8@\"Protocol\"16
v32@0:8@\"DIAttachParams\"16@?<v@?@\"DIDeviceHandle\"@\"NSString\"@\"NSError\">24
{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<
v24@0:8@?<v@?@\"DIDeviceHandle\"@\"NSError\">16
v20@0:8f16
B40@0:8q16@24^@32
@28@0:8@16B24
v16@0:8
v24@0:8q16
@40@0:8@16^{__SecCertificate=}24^@32
v24@0:8@?16
{shared_ptr<crypto::passphrase_header>=\"__ptr_\"^{passphrase_header}\"__cntrl_\"^{__shared_weak_count}}
@\"NSXPCConnection\"
B40@0:8@16*24^@32
@\"NSURL\"
B24@0:8#16
@\"DIConvertParams\"
@\"NSUUID\"
@24@0:8^@16
q40@0:8^v16Q24q32
B48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
v40@0:8@16@24@?32
@52@0:8@16@24@32@40B48
@20@0:8I16
v32@0:8@\"DIAttachParams\"16@?<v@?@\"NSError\">24
@\"DIClient2IODaemonXPCHandler\"
@32@0:8r^v16^@24
Q
@40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
@24@0:8@16
B
@32@0:8Q16@24
@32@0:8@16^v24
B32@0:8^v16^@24
@24@0:8@?16
@\"DIDeviceHandle\"
B16@0:8
I16@0:8
@\"NSObject<OS_dispatch_semaphore>\"
B48@0:8@16@24@32^@40
B40@0:8r*16Q24^@32
@\"NSMutableDictionary\"
B40@0:8^B16^B24^@32
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8^@16
@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}24
@28@0:8I16^@20
@24@0:8@\"NSCoder\"16
i16@0:8
@\"NSMutableSet\"
B32@0:8q16^@24
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}}16@0:8
@16@0:8
@\"DIVerifyParams\"
@32@0:8@16@24
q
@\"DIClient2Controller_XPCHandler\"
B64@0:8r*16Q24{function<bool (iokit_utils::di_io_obj_t)>={__value_func<bool (iokit_utils::di_io_obj_t)>=(type=[24C])^v}}32
@36@0:8@16i24Q28
@\"NSString\"16@0:8
@64@0:8@16Q24q32*40^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}48@56
^{_NSZone=}16@0:8
@\"DICreateParams\"
^v16@0:8
@40@0:8q16@24^@32
B24@0:8r^v16
@\"DiskImageParamsXPC\"
^{?=Q*^{AAS3Context_impl}}
@40@0:8@16Q24^@32
@\"DIShadowChain\"
{unique_ptr<udif::header, std::default_delete<udif::header>>=\"\"{?=\"__ptr_\"^{header}}}
v32@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16
{shared_ptr<Backend>=\"__ptr_\"^{Backend}\"__cntrl_\"^{__shared_weak_count}}
v32@0:8@\"DIVerifyParams\"16@?<v@?@\"NSError\">24
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8B16B20
#16@0:8
v24@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16
v24@0:8^v16
B32@0:8^B16^@24
C16@0:8
@44@0:8@16^{?=Q*^{AAS3Context_impl}}24I32f36I40
i24@0:8@16
@\"NSLock\"
B36@0:8@16B24^@28
@56@0:8@16q24@32@40^@48
i40@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16Q24q32
@\"NSURLSession\"
{shared_ptr<unsigned char>=*^{__shared_weak_count}}16@0:8
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16@0:8
@36@0:8i16@20^@28
@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>={?=^{header}}}24
{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"\"{?=\"__ptr_\"^{header}}}
@\"NSMutableArray\"
@28@0:8i16@20
@48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
@\"NSString\"24@0:8^@16
i32@0:8^v16Q24
{unique_ptr<diskimage_uio::diskimage_open_params, std::default_delete<diskimage_uio::diskimage_open_params>>=\"\"{?=\"__ptr_\"^{diskimage_open_params}}}
v32@0:8@16@?24
@\"NSArray\"
@\"NSXPCListener\"
r^v16@0:8
@24@0:8I16B20
@\"DIAttachParams\"
B40@0:8@16@24^@32
Q16@0:8
B32@0:8r*16^@24
B24@0:8Q16
@40@0:8r^v16@24^@32
B48@0:8@16@24^@32^@40
Q24@0:8^@16
v24@0:8Q16
@
@32@0:8#16@24
v24@0:8@16
Vv16@0:8
@\"NSDictionary\"
B48@0:8@16*24Q32^@40
B56@0:8@16^@24*32^Q40^@48
@56@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24^Q40^@48
@32@0:8@16Q24
@40@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24
f16@0:8
f
{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_des
@36@0:8@16i24^@28
B40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
AQ
B40@0:8*16^@24^@32
v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24
v32@0:8^v16^v24
@56@0:8Q16q24*32^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}40@48
^{?=Q*^{AAS3Context_impl}}16@0:8
B48@0:8@16Q24q32^@40
B28@0:8i16^@20
B40@0:8^v16Q24^@32
{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16@0:8
@56@0:8@16@24@32@40^@48
I
@32@0:8@16@?24
@\"DIController2IO_XPCHandlerRootCopier\"
@24@0:8Q16
v20@0:8I16
@\"AAS3DownloadSession\"
@\"DITemporaryPassphrase\"
@32@0:8^{diskimage_open_params=^{diskimage_open_params_impl}}16r^v24
B48@0:8@16*24^@32^@40
@24@0:8:16
{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>={?=^{diskimage}
@32@0:8^v16r^v24
Q32@0:8@16Q24
@\"FileLocalXPC\"
@60@0:8@16@24@32@40@48B56
@28@0:8i16B20B24
@32@0:8@16^@24
@\"NSObject<OS_dispatch_queue>\"
@\"NSMutableURLRequest\"
B40@0:8r^v16@24^@32
v24@0:8B16B20
@\"DIStatFS\"
@24@0:8q16
B48@0:8^v16*24Q32^@40
@28@0:8@16i24
@24@0:8^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}16
Q32@0:8@16^@24
B32@0:8^Q16^@24
@\"NSData\"
v24@0:8@\"NSCoder\"16
^v24@0:8^@16
/dev/tty
Failed creating bands folder
Can't flush asif table, bitmap flush failed 
int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)
virtual int FileLocalAsync::_write(const sg_entry &)
) is locked
ERROR: shipping key wrapped-key failed base64 decode
Cannot find BSD name in IO media service
The type option contains an invalid value for 
Sparse bundle image
No
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
-
Snapshot
 is clean, skipping flush
Backup GPT Table
Stable UUID
 is now available
maxRawUDIFRunSize
The requested URL is an existing regular file
 errno: 
virtual PurgeableFileBackend::~PurgeableFileBackend()
Invalid pstack, Active stack contains a loop.
Sector Count
dataTaskWithRequest
Failed to get canonical path for sandbox extension
crypto_mode
Failed opening mapped blocks file for 
None
Failed to read passphrase from stdin
inputMountedFrom
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
Could not stat shadow file
auto trim_data(const sg_vec::iterator &, const sg_vec::iterator &, size_t, const io_result_t &)::(anonymous class)::operator()(const auto &, const auto &, size_t) const [src:auto = sg_vec_ns::details::sg_vec_iterator, dst:auto = sg_vec_ns::
Maximum Transfer Sector Count
Raw header changed while unlocked
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
Cannot load libAmber
free = 0, full = 1, map_info = 2
an integer
-[DIResizeParams resizeWithError:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:429:
virtual int Ram::_write(const sg_entry &)
Couldn't parse scheme id
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Harde
Sparse bundle ejected
 with errno: 
Cannot create target image format with the block size of the source image
 read: 
virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)
Can't flush asif table, backend barrier failed
a pointer
Failed to add public key entry to auth table
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_handle_exceptions()
Requested write is out of range - offset 
fchownat failed for 
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
v24@?0@\"DIDeviceHandle\"8@\"NSError\"16
???
-[DIImageHandle resizeToSize:error:]
tkn
void plugin_encode_fd(void *, const char *, int)
pthread_once
snapshot
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)
+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
 completely
Diskimageuio: can't get Diskimage attribute, unknown header format
Info.plist
IV_TWEAK_SIZE_16 = 16
user data retrieving failed
ASIF header changed while unlocked
certificate
Cannot delete base image node.
image_format diskimage_uio::details::diskimage_impl::query_image_format() const
-[DIVerifyParams verifyWithError:]
stable uuid
com.apple.wkms.url
CFUserNotificationReceiveResponse failed
Failed to resize the image
+[DICreateParams eraseIfExistingWithURL:error:]
encryption_key_bits_size_t
Block size mismatch between crypto header and ASIF header
failed to set the destination image's size
UDIF: Failed converting type array string (
Failed to get parent registry entry, err code %d
Cancel
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603
device size not found in registry
Failed to get data from self signed certificate
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
Table flush failed during dir flush: 
Timeout waiting for a completion of an ongoing eject
dev
Stackable image
crypto_format: Can't decrypt wrapped key 
%s\n
Partitions
com.apple.diskimages.file.crypto
segment_count_t
Unmap error: 
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
] 
Data Runs
Couldn't get runs array from Media Kit
 length 
virtual int SparseBundleBackend::truncate(uint64_t)
virtual int SparseBundleBackend::lock()
Starting unmap of 
wrapped-key
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
Cannot convert this image in-place, as it contains unordered UDIF runs
io_result_inserter_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::data_entries_vectorizer_t::add_data_entry(const data_entry_t &)
Yes
attributes
not 
Couldn't lock entry 
]
virtual DiskImageSparseBundle::ContextSparseBundle::~ContextSparseBundle()
ASIF max chunk size in header exceeds the limit
' with flags 
Failed to parse auth data blob.
Primary GPT Header
s3Perform retry after %u ms
Failed to convert SLA text to C string
hw.memsize
Sector count is too large
Conversion started
 bytes is smaller than its trailer
 crypto = 
BSDname
Range: bytes=%llu-%llu
Diskimageuio: UDIF header changed while unlocked
Skipping erase of band 
getToken
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
Unsupported block size for image format
Block size mismatch between source (
pstack
Unexpected UDIF header length (
file of 
malloc
Unexpected materialized_diskimage in create_diskimage_from_hdr
PluginParams
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Single element in pstack that isn't an image
Diskimageuio: Couldn't get locked status 
 (errno 
 closed
Validation failed, input contains unexpected data.
\\\\
disk image
void sparse_bundles::Band::ContextsList::clear()
User data is not supported in this image format
-[DIClient2IODaemonXPCHandler cancelSLAWithReason:]
Can't read UDIF trailer
public_key_padding_algo
ERROR: wrapped-key failed base64 decode
uid temporarily set to 
header_flags
checksum_type
 returned status 
Looking for existing bands
sparsebundle
std::string FileDescriptor::get_mounted_on_fs() const
 
The fill option contains an invalid value
outputFormat
virtual int SparseBundleBackend::unlock_all()
Band was evicted by another thread, retry erase process
key
Destroying File backend, but in-flight promises exist
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = di_asif::header]
 bytes)
No mapped file for band 
auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:
band 
Can't read bitmap
Couldn't write asif's header
Diskimageuio: No diskimage given
 existing bands
-C
The requested operation will delete the active node, please set another one first.
Disk image verification failed
Data
Disk image is terminated, skipping unmap
diskimagesiod
Invalid ASIF header size
Invalid UDIF, run is not within block boundary
euqueueRequest timed out
virtual int Backend::read(const elements_t &)
high throughput
Can't load bitmap while setting range
ASIF: failed to deserialize metadata
bool sparse_bundles::mapped_blocks_t::load_file()
int DiskImage::Context::unmap(const unmap_extent_t *, size_t)
rawTestPlugin_t::~rawTestPlugin_t()
The replacement field misses a terminating '}'
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)_block_invoke
APPLECONNECT.APPLE.COM
Unexpected backend type for shadow file
static int FileDescriptorWrapper::open_from(int, const std::string &, int)
POST
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
Cannot decode file descriptor
ASIF: Content dirty bit is set when reading from disk
The requested operation will delete all children of the provided node. use recursive removal to surpress this error.
valid
aaS3ContextClone
passphrase_header
void di_hybrid_subscriber_t::suspend()
virtual int BackendSG::write(const sg_entry &)
applicationId
Destructing sb context
Barrier failed after defrag, error 
Failed creating 
diskimage-bundle-type
void udif::details::UDIF_base::print_checksum_verification_status(const std::string &, const csum_any &, const details::checksum &) const
-[DIDeviceHandle updateBSDNameWithBlockDevice:error:]
Request timed out
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
Band 
useFormatMappingInfo
Failed to create XPC connection object
 backend: 
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
-[DIController2IO_XPCHandlerAttach updateQuarantineFlagWithHandlerArray:flags:buffer:error:]
 bytes, reading only 
Failed placing new 
Cannot find disk image with reg entry ID 0x%llx
basename_r failed
 (error code 
oma-context
Encryption Method
Compression Info
, dirty=
attempting to authenticate with wkms
Can't write initial table data
gcd_kqueue: kevent64 returned error 
Final asif 
Disk image is terminated, skipping write
Failed converting URL to UTF8
Failed to create chiper data for public key auth
ASIF meta header trailer isn't equal to zero
crypto_op: can't initializae aes_cbc context
file
-[DIEncryptionFrontend unlockWithPassphrase:error:]
-[DIStatFS initWithFileDescriptor:error:]
Failed to update internal state after resize
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
nodes
\\r
flags validator
 is incompatible with the framework, expected at least 
-I
Opening band 
 auth entry
Can't read custom encryption entry header, error 
IOMedia
DiskImageConvert
udsb
Can't write UDIF resource part
key_derivation_prng_algorithm_t
Password
-[DIBaseXPCHandler installConnectionLostHandlers]_block_invoke
Failed reading 
fully
crc32 {
UDIF image of 
+[DIControllerServiceConnection tryAttachWithParams:clientConnection:slaXpcHandler:outError:]
Failed to replace passphrase entry in auth table
Reading 
fstatfs failed with err code 
wrap_key_crypto_padding_algo
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_fo
[empty]
shared
UDSB
Closing bands
virtual int Ram::_read(const sg_entry &)
Can't parse encryption entry: 
, but file size only 
disk image kernel return
, taking as mapped data
creating session
precision
Clone of plugin nodes is not supported.
Writable
Disk image is terminated, skipping read
1
virtual io_result_t DiskImageUDIFRead<UDIFReader<locks::None>, DiskImageUDIF>::read(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &) [UDIF = UDIFReader<locks::None>, UDIFVariant = DiskImageUDIF]
Image does not have write permissions
%@: %@
ASIF: Entry dirty bit is set when reading from disk
>
Cache is not supported when using pstack.
Diskimageuio: Couldn't lock backend 
Diskimageuio: Invalid pstack element: 
(unrecognized error)
AEA key retrieval failed
statInstanceID
Range:
The numeric value of the format specifier is too large
zero-padding
virtual lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImageRaw::future_write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
: [
Images Count
Conversion: unmap error 
sg: buffer = 
xpc error
iokit error
virtual io_result_t sparse_bundles::Band::write(DiskImage::Context &, const sg_entry &)
Band size in sparse is zero
read
:
 offset = 
MediaInfo::MediaInfo(DiskImage &)
Reserved
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)_block_invoke
bitmap flag value invalid
bla
Legacy prepended-header UDIF image is not supported by this framework
size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)
DI Verify Queue
Failed opening the shadow/cache file(s)
 to 
Unsupported ASIF version 
ddm
In-place conversion to this image format is not supported
fileMode
expected<uint64_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_nr_blocks() const
-[SparseBundleBackendXPC getCryptoHeaderBackend]
Couldn't parse scheme name
--oauth-grant-type
;
 rather than image
Unable to convert data to vector.
virtual int FileLocalAsync::disable_file_zero_padding() const
lifs
0b
com.apple.DiskImages2
Cannot acquire 
) is unlocked
 overrun events occurred in the plugin's ring!
expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_image_header(size_t)
virtual int CompressedBackend::write(const sg_entry &)
+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke
/s3/aws4_request,SignedHeaders=
-[DIUserDataParams embedWithError:]
void info::DiskImageInfoASIF::examine_mapped_extents(const DiskImageASIF &)
handleRefCount
Range
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
 elements returned 
Couldn't read sparseimage header
passphrase
IOBlockStorageDriver device not found in registry iteration
bytes=
Unexpected backend type for file
Block size mismatch in DiskImageStackable
Failed creating the image
wkms
Unknown
frk_set_device_identity_certificates
Udif: needs to read 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682
fileBackend
Terminating due to unrecoverable I/O error
Diskimageuio: Failed to create disk image: 
Band data doesn't exist, zeroing
saks-ac-uat.g.apple.com
device with registry entry ID 0x
Cannot find image with provided UUID.
ReadOnlyBackend
-[DIControllerServiceConnection dupWithStderrHandle:reply:]
/dev/rdisk
invalid uuid string
asif: chunk size is too small, too many dir indices
Failed to get registry entry ID, ret %d
forwardLogs
map_element flush failed on creation
generating for blkx 
 ret = 
%12llu bytes downloaded (%.2f MB)\n
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = std::__bind<io_result_t (DiskImage::*)(DiskImage::Context &, const sg_entry &), DiskImage *, std::reference_wrapper<DiskImag
DIErrorVerboseInfo
invalid length
UDIFDiskImage: failed flush after user data write
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615
UDIF: Can't find data key in dictionary
 (our euid is 
User declined SLA
Corrupted plist
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633
segment_count_none = 0, segment_count_one = 1
Validation failed for dictionary key %@.
public_key_crypto_algo_mode
Failed to read from certificate file 
 is incompatible with the framework, expected 
application/json
fstat failed
Error creating backendXPC
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
Failed truncating plist
):
Not a pstack.
algorithm_type
Udif: advanced buffer, needs to read 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
Authentication Data creation failed.
No WKMS key source available in AEA metadata
com.apple.diskimages.band_management
Diskimageuio: Can't get image format
userDict cannot be nil or empty
conversionMethod
fd
RO
Request creation
-[DIEncryptionChpass unlockWithPassphrase:error:]
Compressed(
 doesn't exist
AWS4-HMAC-SHA256 Credential=
Image has a read-only format, attach failed due to force RW flag
char *udif::details::plst::write(char *)
Failed truncating 
autoMount
writable
Placed new 
, res=
void sparse_bundles::open_bands_t::remove(uint64_t)
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:128:22)]
di_plugin_image_t *PluginsManager::decode_plugin_image(const di_plugin_t &, const diskimage_decode_fn_t &, void *)
io_result_t DiskImageSparseBundle::perform_io(ContextSparseBundle &, bool, const sg_entry &)
 directly (without list)
> real: <
, truncating
intermediate-certs
CKIE
, current is 
bytes=%llu-%llu
blockSize
 err: 
, band was written to
sparseHeader
Destination folder URL must represent an existing folder.
Compressed Length
disk image password
Couldn't lock entry
, required decompression buffer size: 
ASIF max_write size in header exceed the limit
version
v1/ac/decrypt
Key transcoding failed.
IOServiceOpen failed. error=0x%x
UDIF read-only compressed image
Error: Not enough data read. expected: 
Bearer %@
virtual DiskImageSparseBundle::~DiskImageSparseBundle()_block_invoke
thread constructor failed
 src size 
Failed creating CFAutoRelease instance.
Failed to find DiskImages2 controller, driver might not be installed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:836: libc++ Harde
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_fd(int, const std::filesystem::path &, bool)
public_key_crypto_algo
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:152:22)]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433:
write
num of runs 
Failed creating IO iterator, err code %d
Cannot decode writable
attempting to authenticate with saks
-[AAS3DownloadSession addRequest:]
uid restored to 0 (res=
Error during ASIF flush: 
prng_algorithm_type
bool sparse_bundles::open_bands_t::insert(uint64_t)
supportsPersistentAttach
Passphrase is too long
 (band 
Failed during ASIF extents enumeration.
void di_hybrid_subscriber_t::cancel()
clientID
-o
isCache
v32@?0@\"DIShadowNode\"8Q16^B24
Can't flush asif on table close, backend barrier failed
AAS3ContextCreate
-[DIConvertParams shouldPerformInplaceSquash]
Invalid raw UDIF run size limit
-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]
com.apple.diskimage-plugin.amber
plst: count = 
Failed to serialize public key entry to crypto header
Convert AEA key from hex failed
virtual int DiskImage::set_size(uint64_t)
KEY_BITS_128 = 128, KEY_BITS_256 = 256
Diskimageuio: query format failed 
encryption
asif_header
device_OBSOLETE = 0, device = 1, partition = 2
 not found in registry
, UID:GID(Name)=
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406:
entire_device
CFAutoRelease<CFDictionaryRef> udif::details::UDIF_base::get_resources() const
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
Could not determine cache dir
virtual void DiskImageSparseBundle::on_eject()
-[DIShadowChain openWritable:createNonExisting:]_block_invoke
udro
Invalid knox URL format. Expected: knox://host/download/space/digest
Unexpected context construction by 
UDIF XML at 
-[DIBaseParams prepareImageWithXpcHandler:fileMode:error:]
leaf-cert
allowStoringInKeychain
di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke
Couldn't trim entry in read 
mapped blocks of band 
/
Max Size Bytes
Unmapped Entries
Master Checksum Info
Could not parse OIDC token from AppleConnect output
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
dealloc_queue
fstatfs failed with err code
wrap_key_crypto_algo
The image was unlocked before setting userData
udzo_max
Plugin initialization failed
uat
-[RamXPC createRamBackend]
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
Disk image is terminated, skipping future_flush
Failed writing sparsebundle info
Images
virtual di_coroutines::Task<void> CompressedBackend::run_futures()
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib 
DiskImageUDIFWritable: aborting
ERROR: Response dictionary is missing required keys. Will fail
failed instantiating the diskimage object
-[DIUserDataParams encodeWithCoder:]
Failed to erase mapped file of band 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ H
://
fetch_restore_key/%s OS/%@
-[DIConvertParams onConvertCompletionWithInError:outError:]
UDIF: Can't create dictionary resource fork
 size = 
Bands folder contains an out of range band (
com.apple.knox.url
Attributes
RW
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)
Close completed
Max sector count is too large
 of type 
wkms-dev.sd.apple.com
Diskimageuio: required mode 
Data Fork
-[DIBaseAgentDelegate createListener]
Invalid block size for image
none = 0, crc28 = 1, crc32 = 2, dc42 = 3, md5 = 4, sha = 5, sha1 = 6, sha256 = 7, sha384 = 8, sha512 = 9, none_valid = 10
void DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::transform_i
Couldn't open file with flags 
rdisk
/dev/disk
bundle-backingstore-version
-[DIBaseParams openExistingImageWithFlags:error:]
Error creating crypto format
invalid value
!
File system is 
-[DiskImageParamsXPC allowOnDiskCacheWithSinkDiskImage:]
Failed during table 
trim largest: size change callback failed with 
invalid flags
Failed to create dispatch source for kqueue
BackendSG
Could not get media info
system
Resetting 
flags_t
https://%@
Non supported options in AAS3DownloadSession (ignored): pinned_public_key %s
Malformed URL format
virtual int DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::tran
int sparse_bundles::mapped_blocks_t::flush()
Contains non-hexadecimal characters.
com.apple.diskimagesiod.spb
UUID
gcd_kqueue: kevent64 failed with ENOMEM
Does not contain an \"even number\" of hex digits.
no more attempts allowed
expected<image_format, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::query_image_format() const
Diskimageuio: can't get lock status 
Missing payload URI in Knox response
Failed to update crypto header
Solid State
void space_allocators::FixedSize::trim_largest(const size_changed_fn_t &)
static int FileDescriptorWrapper::open_file(const std::string &, int)
Cannot find image with provided tag.
json
virtual int BackendSG::truncate(uint64_t)
uniqueDevice
daw
band_ptr DiskImageSparseBundle::replace_oldest_band(Band *)
 mode=
virtual FileDescriptorWrapper::~FileDescriptorWrapper()
Duplicate shadow values for: %@
Overflow detected
Cannot find IO object of class %@
 bytes
Failed to set up image for info retreival
void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)
/dev/%s
Failed to allocate raw blob data
Failed to store the passphrase in the keychain
Diskimageuio: image is locked
Failed to update asif header
-[DIConvertManager convertUserDataWithDiskImage:destination:]
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
Resumed
type: 
, size 
-[DICreateParams createDiskImageParamsWithError:]
uninit
 folder
void rawTestPlugin_t::subscriber_t::_cancel()
Bit 
virtual int DiskImageSparseBundle::set_size_impl(uint64_t)
void udif::details::UDIF_base::validate_runs()
The type option contains an invalid value for a string formatting argument
encodedDict
Default
invalid file size for 
addRequest
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::set_path(const std::filesystem::path &, const diskimage_open_params::mode)
Can't flush asif table, backend write failed
UDIF: compression algo is invalid
Bad pstack format, node with active UUID not found.
AppleDiskImageDevice
static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
s3Sign
X-Amz-Security-Token: %s
virtual DiskImageSparseBundle::~DiskImageSparseBundle()
bool ref::details::ctrl_blk<di_asif::details::table, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::table, tag_t = unsigned long long]
 header size 
blocks_signature
 auth entries
s3Perform failed (after retry), %s
Key is not 32 bytes size.
name: 
%@[%@]
blkx
-[DIClient2IODaemonXPCHandler createConnection]
 failed with 
Missing parent node in graph.
Non supported options in AAS3DownloadSession (ignored): proxy_headers %s
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
com.apple.diskimage.sparsebundle
version_t
Context creation failed.
Can't get scheme values from dictionary
%02x
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_write_iov_t]
sha1 too many bytes
encryption: header size mismatch
int DiskImage::Context::flush(di_flush_mode)
AES-XTS
Decompression failed
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)
table_entry_data::flags di_asif::details::table::get_next_extent(ContextASIF &, const interval_sectors &, interval_sectors &)
void convert(DiskImage::const_extents_iterator_t, DiskImage::const_extents_iterator_t, DiskImage &, DiskImage &, const std::function<void (int64_t)> &, bool *)
-[AAS3DownloadRequest createAndResumeTask]
environment
full_fsync
void SparseBundleBackend::read_info()
RootDeviceEntryID
Failed converting CFNumber to longlong
-[DIConvertManager runWithError:]
0123456789abcdefghijklmnopqrstuvwxyz
singleInstanceDaemon
Diskimageuio: resolved disk image format 
rings_queue
int crypto::crypt_op::crypt_consecutive_vector::operator()()
Couldn't parse partition name or type
The argument index value is too large for the number of arguments supplied
Failed to create crypto serializer
%@: %s
stat failed
%@%@.%@
int di_asif::details::table::close()
Internal backend write() failed. ret=
Diskimageuio: unsupported disk image type for get_backend
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
int details::udif_verify::calculate_checksums(workqueue::workqueue &)_block_invoke
 changed before retain completed
0X
plist
table entry map@
-[DIControllerServiceDelegate setupNewConnection:]_block_invoke
Verify
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
baseBackend
v32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
virtual int CompressedBackend::read(const sg_entry &)
Diskimageuio: decryption key missing
Info.bckup
Opening mapped blocks for 
dirty = bit(0)
DiskImage::diskimage_extent_t DiskImage::const_extents_iterator_t::make_val() const
IOMedia device not found in registry iteration
std::unique_ptr<DiskImage> diskimage_uio::details::diskimage_open_params_impl::transfer_disk_image_ownership()
auto sparse_bundles::Band::get_mapped_blocks()::(anonymous class)::operator()() const
Invalid user data content
debugLogsEnabled
UDIF: Can't get resource array
Compressed Bytes
STCK
udifHeader
RSA = 42
int main(int, const char **)
)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
bands
Reserved part isn't zeroed
crypto_header
ASIF meta header data is unaligned
virtual io_result_t DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterato
enqueueRequest
encryption_mode
Read error: 
Aborted by user
Corrupted encryption table, invalid offset/length in entry's descriptor
YES
Read-only image cannot be resized
ASIF Info
The type does not fit in the mask
-t
Failed to write metadata
 data: 
Crypto operation on data of 
 - unmap_range: [
%@[%@, %@]
Transfer-Encoding:
The format string contains an invalid escape sequence
Replacement argument isn't a standard signed or unsigned integer type
Can't convert ASIF flag.
The operation was cancelled by the user
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
Unsupported URL scheme
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
 io: 
Diskimageuio: is cache image failed 
 cannot be re-registered
uuid
IsCache
Failed to parse key in KVS (zero size data).
-[DIUserDataParams retrieveWithError:]
-[DIAttachParams newAttachWithError:]
Plugin 
Dir Pointer Version
flush
CFName
void diskimage_uio::details::diskimage_open_params_impl::lock_backend_if_required()
bool di_asif::details::table_entry_data::validate() const
No room to add new auth entry
Characteristics
disk arbitration framework returned an error
IOStorageFeatures
Flush failed - returning 
' opened successfully with flags 
i
ERROR: Failed to serialize request: %@ error: %@
Invalid chunk size
Agree Y/N? 
Invalid key size
tr '\\r' '\\n' | fmt | ${PAGER:-more}
oidc
-[DiskImageParamsXPC createDiskImageWithCache:shadowValidation:]
Failed to validate metadata 
metadata_flags_t
 buffer_size = 
not a valid DER-encoded X.509 certificate
 band contexts
Backend barrier failed during dir flush, error 
Backend barrier failed after dir offset changed, error 
Error duplicating stderr
w
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)
, error 
void plugin_encode_buffer(void *, const char *, const void *, size_t)
random generation failed with err code 
New disk image
public key has an encoding issue or uses an unsupported algorithm
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
, Force closing.
vsnprintf
RAW
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr(image_format, std::shared_ptr<Backend> &, bool, const std::filesystem::path &, size_t)
 trying to check permission after EACCES
, errno 
Compression Type
An argument index may not have a negative value
-[DIConvertManager runWithError:]_block_invoke
/System/Library/PrivateFrameworks/DiskImages2.framework
attempting to authenticate with kms
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
ASIF: Block size isn't a multiple of 512
trailer of a 
partition_num: 
udzo
 given
Crypto data block size: 
Metadata
-[AAS3DownloadSession readToAsyncByteStream:size:atOffset:]
<
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
Backup GPT Header
 option
SLA prompt cancelled
 was opened in the background, waiting for it to become available
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
Can't write table for defrag
virtual int BackendSG::read(const sg_entry &)
BZIP compression failed, res=
allocated: size change callback failed with 
virtual int BufferedWriteBackend::write(const sg_entry &)
fetch_restore_keys_ephemeral
Disk image is terminated, skipping future_read
Asif header size unaligned
File descriptor 
fetch_restore_keys_key_handling.m
KVS data fetch failure.
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c
Can't lock entry
Unaligned metadata entry size
 failed, error 
resource-fork
Diskimageuio: Unrecognized image format.
(err 
UDIF_header
Failed to read file for pstack parsing
NSURLSession read to buffer nbyte=%zx offset=%llx\n
Evicting all bands for eject
encKeys
Cannot increase size of a block device
Type
(unlocked)
CBC_IV8 = 5, XTS = 0x80000001
US
Couldn't parse media block size
managed future err 
0
Failed to set up image for resize
We're out of ctxs for async execute
 at index 
unique_lock::unlock: not locked
Plugin's ring resumed, ret code 
Invalid value for asif header field: %s
Failed locking the shadow file
virtual int DiskImageSparseBundle::flush(DiskImage::Context &, di_flush_mode)
Image referenced in the pstack is unreachable.
Cannot save DiskImageGraph without specifying pstack URL
Cannot edit crypto header that has more than 
MBR
ulfo
Full dir write failed with 
Diskimages2 - ASIF - bad reserved bits 
UDIF XML length 
ERROR: shipping key enc-request failed base64 decode
corrupted image
RAW read-write image
Error with resolving knox url
Primary GPT Table
NO
Diskimageuio: Required read-write disk image (
failed to set euid to 
virtual io_result_t sparse_bundles::Band::read(DiskImage::Context &, const sg_entry &)
prng_key_bits_size_t
v24@?0@\"NSDictionary\"8@\"NSError\"16
 formatting argument
+[DISLAFrontend(Private) redirectStdoutForDisplay]
Error opening ByteStream
virtual int FileLocalAsync::truncate(uint64_t)
int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
Checksum Type
Closing an unchanged 
%@[ramsize=%llu]
Can't load asif dir version
!\"
A mandatory argument is null in a DiskImages2 API call. Remember to check if init succeeded
backend
void di_asif::details::table::set_entry_bitmap_range(ContextASIF &, data_entry_t &, const bits_range_t &, data_entry_t::flags, std::optional<data_entry_t::flags>)
Unsupported ASIF, contains data beyond current header struct size
Length
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Plugin image struct size 
virtual int FileLocalAsync::_read(const sg_entry &)
IOServiceMatched
 with 
Disk image operation failed with error code %d
plugin
Metadata corrupted 
UDIF - max compressed run size: 
Passphrases doesn't match
 requested while there are only 
Unsupported key decryption algo
The image is encrypted with obsolete encoding version 1
Can't serialize property list
infnanINFNAN
Unexpected passphrase header length (
saks-ac-dev.g.apple.com
knox-uat.sd.apple.com
This operation doesn't support pstack files
GET
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
cache
Failed creating sparsebundle folder
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)_block_invoke
application/octet-stream
pkce
Couldn't read asif's header
field size too large
UDIF: Can't get types array from UDIF
iv_tweak_size_t
 [
plst
band-size
Include all
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
End of input while parsing an argument index
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:113:22)]
Background erase of 
Cache
Destination folder URL must be of 'file' scheme.
Input underlying FS
raw_header
ASIF: Can't defrag entries 
int BufferedWriteBackend::reset_last_offset(const sg_entry &)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c
vector
com.apple.DiskImages2.TelemetryManager
Bad or missing key in SAKS response.
Image
special: 
virtual int FileLocalAsync::unlock_all()
(
Starting ASIF defrag, used size: 
Invalid UDIF format, contains intersected blocks
crypt_consecutive_vector: write check errors 
Mandatory callbacks in the plugin's image struct are missing
mapped
Failed serializing user dictionary
 backend size 
Diskimageuio: path 
ParentUUID
fsync
-[DIControllerServiceConnection init]
-[DIBaseXPCHandler init]
-[FileLocalXPC sandboxExtensionTokenWithError:]
bool ref::details::ctrl_blk<CurrentReader, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = CurrentReader, tag_t = unsigned long long]
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
> %d %s\n
-n
File too small.
basic_string
can't get Diskimage attribute, unknown header format
Opened bundle's lock file with flags 0x
Num Tables
Full Entries
io_result_t di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
config_t
void boost::uuids::string_generator::throw_invalid() const
Unexpected backend replace request
Apple sparse image
, retrying
Failed to write asif header, error 
,
Geometry
-[DIController2IO_XPCHandlerBase setConnectionMode]
Diskimageuio: Failed to create resizer: 
Invalid value for UDIF header field: %s
run offset
Diskimageuio: single image given, but role is 
v32@?0@\"NSURL\"8Q16^B24
virtual int FileLocalAsync::flush(di_flush_mode)
+[AAS3DownloadSession completeRequest:data:response:error:]
XPC connection interrupted
, disk image is terminated
wkms-uat.sd.apple.com
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
static autostart_task_t<process_entry_result_t> di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::process_write_entry::operator()(table &, ContextASIF &, table::data_entry_t &&, const sg_vec:
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
com.apple.diskimages_cache_update
The argument index is invalid
-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]
-[DIBaseXPCHandler createConnection]
regEntryID
mark purgeable failed on 
Failed to read passphrase
ramTestPluginCreate
-[DIBaseServiceDelegate init]
Couldn't read asif's full header
ASIF block size isn't multiple of 512
UDIF: compressed runs should be <= 1MB
Failed during data entry write in table write, error 
UDIF_header::UDIF_header(const std::shared_ptr<Backend> &)
MediaKit returned unsupported block size
-[DIControllerServiceConnection checkAttachEntitlementWithError:]
true
Failed to read 
ftruncate failed, errno: 
Failed to quarantine device, error=0x%x
Failed to use the passphrase that was given
com.apple.diskimage-plugin.nbd
Failed to erase band 
-[DIController2ClientDelegate attachCompletedWithHandle:reply:]
%@:%@
block_attributes
Write error: 
-[DIControllerServiceConnection cleanup]
Is Encrypted
Mandatory callbacks in the plugin's struct are missing
unique_ptr<lock_free::bitmap_t> SparseBundleBackend::get_existing_bands() const
Metadata contains unsupported field 
. returned 
Plugin version 
-[DIShadowChain addShadowNodes:wrapReadOnly:error:]
IOService
could not create iterator (begin)
Content-Length: %zd
Cannot change passphrase of unencrypted image
tmp_convert
Constructing sb context
Error reading file @ 
 failed wih error 
emulateExternalDisk
Failed to generate self signed certificate
-[DIEncryptionFrontend storeInKeychainWithPassphrase:forceSystemKeychain:error:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692
file(
set_euid_wrapper::~set_euid_wrapper()
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Cannot attach RAM disk with a shadow or a cache file
Disk image URL is too long
com.apple.di_stackable.cache.flusher
flushing and closing 
Bitmapped Entries
inputStatFS
Feature or image not supported by library
IOBlockStorageDriver
Name
-[DIBaseAgentXPCHandler createConnection]
Not valid SAKS metadata (no environment field)
oauth-id-token:
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
Cannot get subscriber from plugin
static int SparseBundleBackend::open_bundle(const string &, int)
invalid bits range 
PKCS5_PBKDF2 = 103
Cannot store an empty passphrase
Is Cache
, errno=
, fd=
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
void SparseBundleBackend::write_primary_info_plist()
kern_return_t was 
onDiskCache
int PluginsManager::register_plugin(const string &, di_plugin_t *)
fd block size retrieval failed (err code 
ulmo
Not valid SAKS metadata (json format expected)
BLX
Failed to find IO media entry for %@
Crypto couldn't write to inner backend @ 
set size failed
header_ignore_fields_t
: flush in destructor failed (
UDIFDiskImage: failed truncating image
 - different calculated: <
Image key encoding failed with err code 
The value of the argument index exceeds its maximum value
knox-dev.sd.apple.com
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
verify failed
%s: 
virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)
ASIF: can't copy metadata to mutable copy
diskimageuio: pre-write first error 
auto
 is not registered
-[DIController2IO_XPCHandlerAttach disconnectFromDriverWithError:]
Compression Ratio
shouldValidate
Diskimageuio: can't get file descriptor, backend doesn't exist
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__hash_table:1892: lib
UDIF header doesn't contain a valid sector count, using runs upper value: 
X-Amz-Content-Sha256: %s
UDIF header changed while unlocked
Background close of 
 in dir I/O, error 
The argument index starts with an invalid character
virtual FileLocalAsync::~FileLocalAsync()
Physical block_size is 
virtual sparse_bundles::Band::~Band()
void rawTestPlugin_t::subscriber_t::_resume()
-[DIBaseServiceDelegate listener:shouldAcceptNewConnection:]
void info::DiskImageInfoASIF::count_used_extents(const DiskImageASIF &)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Partitions: 
Remember password in my keychain?
commandSize
v32@?0@\"NSMutableDictionary\"8Q16^B24
crypto_format: cookie differs
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
ASIF: failed to write metadata
static std::string FileDescriptorWrapper::handle_open_from_error_message(int, const std::string &, int, int)
Failed to increase file size, pwrite returned 
IOServiceWaitQuiet error 0x%x
solid state
/usr/lib/libAmber.dylib
 bits in the bitmap
boost::icl::interval_set<uint64_t> MediaInfo::process_mapped_data(uint64_t, uint64_t)
Not A Ninja/1.0
strdup
Runs
size
Unexpected image format from info: 
Missing OIDC client ID in appinfo response
int DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, locks::Std, boost::iterators::transform_it
Size
Using automatic argument numbering in manual argument numbering mode
\\t
 logical: 
read write
Diskimageuio: Couldn't get diskimage: 
Failed opening folder for entries reading
Encountered an irrecoverable I/O error, all future I/Os will be invalidated
gcd::gcd_kqueue::gcd_kqueue(gcd_queue &, std::function<void (struct kevent64_s *, int)>)_block_invoke
Couldn't open 
Ignoring truncate on block device
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
Not valid SAKS environment
BackendPlugin
, allocated: 
UDIF: Can't read UDIF trailer
di_plugin_image_t *PluginsManager::create_plugin_image(const di_plugin_t &, int, const CFDictionaryRef)
Content-Type
Master checksum
Role
get_next_capacity, allocator's max size reached
 but buffer is too small 
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_stackable_uuid() const
Bakcend not initialized for file
+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
curl_easy_setopt failed\n
unexpected error
 ret: 
FilePath
enc-request
The format specifier should consume the input or end with a '}'
com.apple.diskimages.sla-prompt
Completed erase of band 
http
device not found in registry
Failed to mount filesystems
Diskimageuio: ASIF header changed while unlocked
 on 
Replaced an empty slot
Error reading sectors for verify 
File size is less than the minimum header size
 doesn't exist, returning zeros
deserializationError
Couldn't get mapped sectors for [offset: 
Failed to open crypto header
Crypto: Unsupported encryption parameters
%s (%@)
lock_backend
File: Couldn't fetch status, error: 
+[DISLAFrontend(Private) displaySLAText:error:]
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/disk_im
 bytes are above the sparsebundle limit of 
Shadow block size is invalid (0)
+[DIControllerServiceConnection sendHandleToClient:clientConnection:outError:]_block_invoke
%12.2f initial interval between retries (s)\n
Format Description
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486:
Registered plugin 
 = offset = 
ssize_t plugin_decode_buffer(void *, const char *, void **)
pluginParams
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638
diskimageuio: pre-write final error 
1.0
identityCertificates && [identityCertificates count] >= 1
locale-specific form
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_read(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
failed to enter SQE to the ring, ret code 
Bundle's lock file is closed
/usr/local/bin/appleconnect
Can't write UDIF header
value validator
Request failed: %03ld (error not set)
Passphrase cannot be empty
Corrupted plist dictionary
bundle_handle
Image info is not supported for the given image type
Custom cache or shadow is not supported for pstack based images.
Diskimageuio: get stackable uuid failed 
Can't create data for plist deserialization
Record On Bits
s3Perform
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
mountedFrom
Invalid size hex key %lu
-[DIConvertParams prepareParamsForSquashWithError:]
path
Failed to get plugin instance
unmapped
 bytes does not fit before the 
bad flush type (
Invalid negative media block count
DELETE
vbuf validator
&
Disk image is terminated, skipping ...
Preferred Block Size
BufferedWriteBackend
https
Failed to create passphrase auth entry
Failed to serialize symmetric key to crypto header
AEAHelper: Invalid file descriptor.
readSynchronizer
image_variant_type
, dest buffer_size 
Couldn't parse media block size in whole disk mode
-[DIConvertParams copyUpdatedOutputURLWithError:]
Diskimageuio: Only single cache is allowed
Disk image is terminated, skipping flush of 
table flush failed during close: 
barrier
createErrorContextKey
com.apple.diskimages2
band_ptr DiskImageSparseBundle::find_band_in_array(uint64_t)
Can't get section values from dictionary
segment_num_none = 0, segment_num_one = 1
cert-chain
Failed converting CFNumber to long
ram
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ H
segment_num_t
int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)
'
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
The width option should not have a leading zero
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
Context setup failed.
Can't convert data to property list
Accept: application/xml
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_flush(di_flush_mode, future_io_opts_t)
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = di_hybrid_subscriber_t]
system error
Unexpected crypto header length (
Conversion: read error 
-[NativeDiskImageGraphNode deleteImage]
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc+
Error creating (unlocked) backend
-[BackendXPC tryCreatingCryptoHeader]
-[DIDeviceHandle waitForQuietWithService:error:]
[
File (fd 
Error: failed to unwrap key. Error: %s\n
 -> 
Create device call failed, error=0x%x
Size Info
{:02x}{:02x}
The symmteric key is wrong
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::verify_backend() const
location
Failed barrier at start of dir flush, error
 is closed, notifying waiters
XPC connection invalidated
ASIF: metadata header out of range
auto FileLocalAsync::shared_state_t::init_unmap_zeros()::(anonymous class)::operator()() const
, trimmed size
Diskimageuio: reopen backend to required mode 
com.apple.diskimagesiod.ram
readPassphraseFlags
shadowStats
sig1_t
io_result_t DiskImage::Context::read(const sg_vec::iterator &, const sg_vec::iterator &)
set context
-[AAS3DownloadSession syncRequests]
getErrorContextKey
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
Diskimageuio: get nr blocks failed 
OK
Backend: failed writing element in vector
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:172:22)]
ULFO
user data embedding failed
crypto header contains invalid number of auth entries
IOServiceClose failed. error=0x%x
NSURLSession read to stream nbyte=%zx offset=%llx\n
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
void rawTestPlugin_t::subscriber_t::_suspend()
DIDevicePermissions calculateDevicePermissions(DIAttachParams *__strong, kDIInterconnectLocation)
s3HeaderAppendWithFormat
Request failed: %03ld %s
Size cannot exceed max ASIF size
BuildVersion
s3HeaderAppend
Diskimageuio: Can't create stackable image: 
token
numBlocks
file_handle
ASIF: can't read/allocate asif metadata
get path failed
Tag
Section Block Count
Key Size
a floating-point
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
udif::details::unique_buf UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::generate_blk(const interval_sectors &, struct block &, const descript
Failed to create graph from plist.
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
header_signature
Write header failed after dir offset changed, error 
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
static void process_terminator::terminate()
Incorrect passphrase
read only
Diskimageuio: backend doesn't exist
eject timeout
Failed to read metadata 
Destination image format is unknown
The URL encoded into the AEA authdata is missing or invalid.
Image doesn't support resizing
Couldn't upgrade lock entry
Failed to open backend of crypto header
Unsupported value for crypto header field 
 was just created (truncated)
com.apple.DiskImages2.ASIF.sparsity
unmap_iterator_t di_asif::details::table::unmap(ContextASIF &, const unmap_extent_t *, size_t)
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
DiskImageUDIFWritable: context backend returned 
Failed creating property list
version_1 = 1, version_2 = 2, version_3 = 3
(locked)
header_size_512 = 512, header_size_4k = 4096
Flush failed. Backend = 
Couldn't find partitions key
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__memory/unique_ptr.h:
Cannot attach RAM disk as a read-only device
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
Failed unlocking file with fd 
User-Agent
High Throughput Options
 bands flushed, calling 
Failed writing first block of dir
assetAttr
ZLIB = 0, LZFSE = 1, LZMA = 2, ZLIB_9 = 3, BZIP = 4
Unexpected failure to get image info: 
V2 = 2
 is not aligned to block size
com.apple.diskimagesiod
Unregistering plugin 
https://%@/spaces/%@/files/%@/decryption-components
overrideBlockSize
Cannot load libTestPlugin
com.apple.diskimages.band_unmap
Key from the certificate is not exportable
Custom encryption entry header size exceeds max size
void sparse_bundles::mapped_blocks_t::map_range(uint64_t, uint64_t)
Content-Type:
Failed to add passphrase entry to auth table
void di_hybrid_subscriber_t::resume()
fetch_restore_keys self signed cert
partition offset
Size is not a multiple of block size
auto hdr_get_nr_blocks(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
sparseimage format is not supported by DiskImages2 framework
io_result_t di_asif::details::dir_base::move_realloc_chunk(ContextASIF &, char *, size_t, uint64_t)
ASIF meta header is unaligned
Cannot stat 
UDZO
Image Format
com.apple.DiskImages2.ErrorDomain
image
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
Backend barrier failed during bitmap allocator failures handling, error 
static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)
identifier
%@ failed with error code %d
pthread_key_create
), reading from backup
uint32_t FileDescriptor::fetch_physical_block_size() const
ASIF: table is not aligned to chunk size
which is larger than allowed 
Can't read encryption table, error 
Disk image is terminated, skipping flush
UDIF images are currently not supported in diskimage_uio
Unsupported image stacking
Sections
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
oauth
+[DiskImageParamsXPC newWithURL:fileOpenFlags:error:]
url
Unsupported compressed run (
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = udif::header]
Cancelled
KVS key value - parse failure.
The requested URL is an existing folder
device with dev name 
Trying to read @ 
ActiveNode
UDRO
Internal backend read() failed. ret=
Parent UUID
prod
, flags = 
Write zeros to unmap region failed (err code
CFUserNotificationCreate failed, error code %d
+[DiskImageParamsXPC validateSupportedFormatWithBackendXPC:error:]
Can't read for defrag
exclusive
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
Cannot find image with provided uuid.
sig2_t
Invalid media block size
pstack: unsupported node
End of input while parsing format specifier precision
alternate form
inputURL
Can't flush asif on table flush, backend barrier failed
Metadata offset is invalid
virtual int FileLocalAsync::lock()
PKCS7 = 7
IOBlockStorageDevice
 block_size: 
, 
keys/fetch
-[DIStatFS logWithHeader:]
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
Failed creating CFData
ERROR: enc-request failed base64 decode
Cannot stack images with different block sizes
shadowChain
Failed to evict band to make room for 
Failed barrier after writing full dir
KVS dataBuffer allocation failure.
Medium Type
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
publicKey
len: 
crypt_consecutive_vector: check errors_in read futures 
Invalid public key: %s
download
Failed writing full dir
Backend is not mounted on APFS
CoreFoundation type mismatch: 
-[DIController2IO_XPCHandlerAttach launchIODaemonWithError:]
invalid header: %s
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Harde
Barrier failed before dir flush
Couldn't convert CFStringRef to a proper std string
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:437:
table entry data@
none {
Cannot find registry entry ID 0x%llx
Encryption Info
-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]
truncate error: 
Legacy shadow file format is not supported by DiskImages2 framework
Invalid header: %s
sg: 
saksKey
Raw run size limit cannot be smaller than compressed run size limit
raw
-[DIVerifyManager runWithError:]
BZIP decompression failed, res=
Sandbox extension token exceeds maximum size
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
diParams
int di_asif::header::write_header(Backend &)
Decryption key missing
Failed opening the file
header_size_t
Found a valid file for 
Media Block Size
-[DIAttachParams reOpenIfWritableWithError:]
(err code %d)
ASIF: invalid dir index to header
AES-CBC
is_aea: Error reading magic.
Shadow path %@ is not a valid file
Stack Info
KEY_BITS_160 = 160, KEY_BITS_NONE = 0
Failed locking the image
has_bitmap
shadow
Invalid size of saks response %lu
outputParams
backend write failed during locked flush of map element, error 
s3StringBufferAppend
 - same 
Failed opening the image with RW access
none
User data contains reserved key(s)
Conversion: write error 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
io_result_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
Can't load bitmap from backend
ID
The disk image format is not supported by this OS
com.apple.diskimages.aio
Couldn't exclusively lock entry 
metadata_read_only_flags
AEA
More than one image in the stack has the provided tag, please specify UUID instead.
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
] from MediaKit - errno 
Updating 
Authorization
-[DiskImageParamsXPC createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:]
Unexpected unmap command received on read only image
ASIF meta header size exceeds its maximum
01234567
BackendNull
Base
Could not generate OIDC token - AppleConnect Failure
Unexpected error creating (unlocked) backend
Stack with cache as top image cannot be opened for writing.
partition size
%12.2f MB/s download speed\n
StandardCompressedBackend::pimpl::pimpl(algo_t)
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
total_segments_t
Not allowed more than one instance of 
Can't create MediaKitRef
-[DIController2IO_XPCHandlerAttach createDeviceWithError:]
Min Size Bytes
System keychain access is not allowed on this platform
SLA text is empty
knox
virtual io_result_t DiskImageUDIFRead<UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>, std::integral_constant<bool, false>>::read(DiskImage::Con
char *udif::header::write(char *)
v8@?0
Mode for new files in bundle: 
Could not generate daw token - AppleConnect Failure
-[DIShadowChain topDiskImageNumBlocks]
 with ret 
 while writing 
crypto_format: Can't derive key 
] = 
lzfse
com.apple.diskimage-test-plugin.julio
: 
Write zeros to unmap unaligned start region failed (err code
auth-data
DiskImageSparseBundle::ContextSparseBundle::ContextSparseBundle(DiskImageSparseBundle &)
crypto_format: blob length differs
9999
598.40.4
Diskimageuio: Unsupported image format
Can't flush asif on map element close, backend barrier failed
key_derivation_algorithm_t
Diskimageuio: Snapshot detected on top of cache
DiskImageUDIFWritable: Sink backend returned 
Error writing file @ 
Request failed with HTTP error: %lu %@: %@\n%@
The format specifier for 
remote mount
Uninitialized Entries
conversion failed
DES3_3KEY = 17, AES_KEY = 0x80000001
BackendSG: truncating the inner backend failed, error = 
status
Failed getting runloop source
Trimming: Written 
Diskimageuio: get parent uuid failed 
com.apple.internal.fetchrestorekeys
x-amz-
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
ULMO
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Sparsebundles on SMB mounts are not supported on this system
Mapped Sectors
Invalid value for argument 'block-size'
Initialized bands array of size 
ExecutionSchedulerSorted: work returned 
Unable to create ioreg iterator
crypto
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
Flush failed. BackendSG = 
 - map_range: [
Offset
Invalid URL
false
The requested URL is an existing non-sparsebundle folder
Couldn't trim entry in write 
fchmodat failed for 
void DiskImage::do_terminate()
Resource name is too long to fit uint32_t
Can't get key in cstring format
virtual size_t BZIPCompressedBackend::compress(const sg_entry &) const
saks-ac-prod.g.apple.com
encryptionMethod
PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0
com.apple.diskimagescontroller
r
The image is encrypted but has no passphrase auth entry
Plugin struct size 
https://%@/westgate/appinfo
 (band 0x
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
metadata
Missing key in KKMS response
Failed to retrieve info
Shadow underlying FS
Conversion: extents enumeration error 
-[DIDeviceHandle dealloc]
invalid field %u
The format specifier contains malformed Unicode characters
\\u{
Flushing 
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
ERROR: This archive does not contain a shipping key response.
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
openid,dsid,accountname
Flush failed after defrag, ignoring. Error 
CFAutoRelease<CFMutableArrayRef> UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::generate_blkx() [Checksum = ChecksumScheduler<checksum::CRC32,
BackendZero
SHA1_HMAC = 91, NONE = 0
no_match
\\'
suppressSsdFlags
failed to open existing output file
not a disk image
is_writable
header read-only flags
/s3/aws4_request\n
bool ref::details::ctrl_blk<di_asif::details::map_element, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::map_element, tag_t = unsigned long long]
Failed to create kqueue
-[DIController2IO_XPCHandlerAttach updateFileBackingInfoWithRootDeviceEntryID:error:]
01
Diskimageuio: Single element in pstack that isn't an image
https://%@/v1/ac/decrypt
+[BackendXPC newFileBackendWithURL:fileOpenFlags:error:]
PstackVersion
v32@?0@\"DIDeviceHandle\"8@\"NSString\"16@\"NSError\"24
Failed to add symmetric key entry to auth table
-[DIBaseXPCHandler completeCommandWithError:]
 exceeds the maximum of 
 while expected is 
Failed to parse key in KVS (zero size key).
Using compression 
Key is not hexadecimal number.
Read returned an error
 is not supported
 but buffer is full
Shadow
Allocated after defrag: 
Device Characteristics
-[DIConvertParams prepareConvertWithError:]
Found 
Band was evicted by another thread (during retain attempt), retry erase process
ASIF meta header failed to read
Invalid resource key
futimes failed on 
s3DownloadStreamOpen_curl
-[AAS3DownloadSession readToBuffer:size:atOffset:]
Corrupted shadow file(s) chain
Unexpected response type: %@
-[DICreateParams onErrorCleanup]
Couldn't create MediaKit subrange object
unmanaged
X-Amz-Date: %s
 checksum: 
Diskimageuio: locked backend 
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
Diskimageuio: backend is not a FileLocal
In-place conversion from this image format is not supported
Request failed
174350
Diskimageuio: images with constraints currently not supported
 is different than current mode 
devicePrivateKey
SparseBundleBackend::SparseBundleBackend(int, bool, const shared_ptr<FileLocal> &, const shared_ptr<crypto::format> &)
secondaryKey
Write zeros to unmap unaligned end region failed (err code
a bool
Couldn't parse 
Can't load bitmap while flushing asif table 
Unable to get IOMedia preferred block size
Start Offset
Block device block size is larger than image block size
BackendSG: error allocating buffer
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:425:
Unsupported host for OIDC: %@
Failed to deserialize crypto format
Disk image is terminated, skipping future_unmap
missing DI_ATTACH_ENTITLEMENT on non macos platform
Cannot find AmberDiskImagePluginCreate in libAmber
Invalid argument, please use one of the DICreateParams derived classes instead
run_type
Unsupported public key algorithm.
BufferedWriteBackend doesn't support per io crypto
 while expecting 
Invalid output format argument
expected<int, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_file_descriptor() const
KVS keyBuffer allocation failure.
: flush failed (
Bearer openid-id-token-%@
kern.aioprocmax
int plugin_decode_fd(void *, const char *)
ASIF: data entry - invalid reserved bits
Punch hole is not supported (err code 
Plugin's ring suspended, ret code 
Cannot display SLA: no terminal or stderr to write to
Unsupported disk image format
source uuid
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:816: libc++ H
curl_easy_init failed\n
Band data is partial, reading 
int ExecutionSchedulerSortedConsecutiveIt<DiskImageUDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, ExecutionSchedulerSortedConsecutiveIt<dummy_context, lock
Backend: failed reading element in vector
Cannot lock bundle, ignoring: 
int sparse_bundles::Band::flush()
Error creating disk image params
PluginName
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ H
-[DIControllerServiceConnection attachWithParams:reply:]_block_invoke
lzma
Unmapping band 
couldn't allocate space for entry 
int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)
internal metadata
Diskimageuio: get block size failed 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669
DiskImageUDIFWritable: got a flush with error, aborting
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
The precision option does not contain a value or an argument index
v16@?0@\"NSString\"8
Skipping band erase (in use)
user metadata
Could not get mapping information
Calling 
knox.sd.apple.com
 extents
supportsBarrier
v16@?0Q8
Can't read encryption entry header, error 
downloadStreamPRead
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
Checksum Value
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ H
encryption_key
, keeping file unlocked
Cannot initialize pstack disk image without path.
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
!Q
XPC connection failed
Unmap done
uint64_t udif::details::UDIF_base::write_resources(CFDictionaryRef)
managed
Diskimageuio: Nested stacking is not allowed.
Suspended
Background close of band at index 
UDZOMAX
Cannot convert in-place with a shadow file
 does not allow the 
failed to set the bundle's size
diskImageParams
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Diskimageuio: backend isn't locked
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
Accept
UDIF uncompressed read-only image
Cleaning up!
-[DICreateParams resizeWithDiskImage:blockCount:error:]
 bytes image
void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/crypto/crypto_format.cp
\\\"
ASIF: No data offset found (write)
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
Re-enter new password: 
read_only_cache = bit(0)
diskimageuio: report err 
Persistent attach is not supported for this disk image type
wkms.sd.apple.com
Backend barrier failed during allocator failures handling, error 
UDIFWritable<ChecksumScheduler<checksum::CRC32, ExecSchedulerItBinder::ExecutionSchedulerSortedConsecutiveItTransform, locks::Std>, locks::Std>::UDIFWritable(const MediaInfo::logical_disk_entities_map &, std::shared_ptr<Backend>, Checksum &
AES_KEY = 0x80000001
createTask
Using manual argument numbering in automatic argument numbering mode
void SparseBundleBackend::write_info_plists()
-[DIBaseParams tryResolvePstackChain:]
format_type
Identity Info
The argument index should end with a ':' or a '}'
unknown
URL
Failed initializing RAM disk buffers
udif::details::UDIF_base::UDIF_base(UDIF_header &&)
Failed to encrypt data using public key from certificate
io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)
 or exceeds size_t size 
Zero padding cannot be disabled from this process (res=
CBCPADIV8 = 6
Image contains crypto format but info class is missing EncryptionInfo
diskimage_
Failed to setup the plugin's IO ring
AAS3DownloadStream (NSURLSession)\n
%12u max requests in flight\n
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_unmap(const unmap_extent_t *, size_t, future_io_opts_t)
com.apple.diskimage-test-plugin.raw
Missed an evictable slot
bzip2
asif
Nothing to defrag
plugin://%@
Can't get geometry values from MediaKit
Block Size
Missing entitlement: %@
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
run length
zlib
Corrupted ASIF image.
Got error when trying to close 
Chunk Size
Barrier failed after defrag table move, error 
Decoding error.
v16@?0@\"NSError\"8
0B
^v8@?0
ShadowChain: %@
Error decrypting data using public key, error code 
Invalid field found in shadow file header: 
-[FileLocalXPC replaceWithBackendXPC:]
Invalid plugin URL, plugin name is missing
Can't load table to get extents
DI Conversion Queue
Apple Inc
crypto_op: can't initializae aes_xts context
New password
com.apple.di_raw_test_plugin
Looking for an evictable slot for 
Crypto couldn't read from inner backend @ 
DIControllerServiceQueue
Diskimageuio: bottom diskimage should have role image, but 
set_euid_wrapper::set_euid_wrapper(uid_t)
pstack_header
HTTP request failed with status code: %ld
 constant 
sendEvent of type 
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
Segmented UDIF images are not supported by this framework
, err 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp
Failed to create disk image
Can't load asif dir table
 is not supported (err code 
Trying to write @ 
UDBZ
ASIF
 has size 
BSD Name
Failed to read auth table
uri
Missing key in SAKS response
The specified image is a folder but not a sparsebundle
CyrptoKit is missing a required method.
Writing 
Locked encrypted image
bool DiskImageSparseBundle::try_unmap_band_extents_without_list(uint64_t, const extents_set_t &)
}
Invalid band size (
attempting to authenticate with aea key
 marked as purgeable
Flushed 
curl_slist_append failed\n
decryption-components
Missing key in Knox response
Blocks header
Error with decryption key size
dispatch_source_create failed
Failed to subscribe to the plugin's IO ring
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
descriptor_special
slaText
HTTP %u\n
a character
 is 
Missing Expected AUTH DATA in AEA.
iCloud
locally mounted from %@
di_plugin_image_t *verify_plugin_image(di_plugin_image_t *, CFErrorRef)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hard
Unknown checksum found
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_t
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
Failed to write metadata header
6.0
instanceID
The format string terminates at a '{'
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
. Opening as root
Can't parse disk image with MediaKit. No partition scheme or partition scheme not supported by MediaKit
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
First block of dir write failed with 
void udif::details::UDIF_base::generate_blocks(CFArrayRef)
static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)
PUT
Output of disk image conversion must be a file
is_locked
 - 
AWS4-HMAC-SHA256\n
hw.logicalcpu
Starting flush
com.apple.wkms.fcs-key-url
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
(empty)
%12u max attempts for a request\n
Failed opening the shadow/cache file(s) with RW access
Couldn't upgrade lock entry 
typename boost::enable_if<boost::is_integral<typename hex_iterator_traits<OutputIterator>::value_type>, OutputIterator>::type boost::algorithm::detail::decode_one(InputIterator &, InputIterator, OutputIterator, EndPred) [InputIterator = std
In-place conversion maintains the encryption passphrase and method. It's not allowed to specify encryption arguments
virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()
AAS3DownloadStream (curl)\n
virtual int Backend::write(const elements_t &)
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_write(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
lock
Asif header too large
-r
Failed to set up image for resize after creation
flock returned errno 
com.apple.wkms.fcs-response
Failed to find keychain item using hashed key
Origin
 / 
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
void boost::uuids::detail::sha1::process_byte(unsigned char)
gcd::gcd_timer_source::gcd_timer_source(gcd_queue &, dispatch_time_t, uint64_t, uint64_t)
Failed to create public key auth entry
.xpc
static void sparse_bundles::Band::erase(const bundle_commons_t &, uint64_t)
Cannot decode path
\\n
IO error with sg: 
Diskimageuio: Can't stack non asif formats. Got 
Skipping erase of 
com.apple.MobileAsset.AssetType
fstatfs failed
Can't connect to device
Invalid format for shadow file
auto DiskImageSparseBundle::void_stackable_identifier()::(anonymous class)::operator()() const
Not enough space for metadata
 max =
Run interval: 
Crypto: can't read crypto header
AAS3ContextSetFieldString
unsigned char boost::algorithm::detail::hex_char_to_int(T) [T = char]
0123456789abcdef
xpcEndpoint
\n
sign
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocal
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const
 lock, errno 
 status: 
0x
Plugin's async ring cancelled, ret code 
Barrier
 updated from 
Integral value outside the range of the char type
GUI SLA handling required
diskimage_uio::details::diskimage_impl::diskimage_impl(diskimage_open_params &&)
userData
Diskimageuio: Raw header changed while unlocked
URL must have a file scheme
Can't take exclusive lock on entry
The disk image is corrupted
, disk size: 
ASIF: missing internal metadata key
bytes, which is after end of ramdisk
com.apple.wkms.auth-data
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293
int di_asif::details::dir::handle_all_failures(ContextASIF &)
Failed to sign request\n
Failed to write SLA text to stdout
Unexpected ASIF header length (
Failed to create resizer
static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
AmberDiskImagePluginCreate
Failed opening the sparsebundle as user 
ASIF: Header size is less than the min header size
 for 
Authorization: %s
Empty Bytes
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
Invalid encryption method
Cannot find %@ entry
 dest 
Extent 
media block count
Disk image is terminated, skipping future_write
) to type
Zero padding disabled successfully on fd 
hybrid_queue
\\x{
Cannot retrieve passphrase from user via TTY or GUI
 opened and replaced at attempt 
Closed band at index 
Max Sector Count
int di_asif::details::dir::defrag_table(ContextASIF &, dir_idx_t)
header (
ERROR: Shipping private key is NULL.
Plugin bug: returned init failure without supplying the error
) and dest disk image (
Schemes
Compressed Offset
Total Bytes
Diskimageuio: Multiple images given but block size differ. 
Root dir flush failed, error 
Key size isn't a multiple of 8
PKCS1 = 10, OEAP_SHA1 = 0x80000001
section offset
s3DownloadStreamOpen_urlsession
Awaitable completed in unexpected state
 instead
AES = 0x80000001
mountedOnURL
Failed to issue sandbox extension token for file
void convert(DiskImage::const_extents_iterator_t, DiskImage::const_extents_iterator_t, DiskImage &, DiskImage &, const std::function<void (int64_t)> &, bool *)_block_invoke
plugin://%@/
could not create iterator (end)
AppleDiskImagesController
-[DiskImageGraph initWithBaseImageURL:tag:error:]
com.apple.diskimages.attach
Retrying request after %.0f seconds %zu bytes at offset %llu
fskit
Failed to serialize passphrase to crypto header
+[DIError errorWithDomain:code:description:verboseInfo:error:]
NONE = 0
Invalid negative partition size of offset
s3StreamBaseInit
,Signature=
ASIF: can't set requested uuid
diskimagesuio: future read invalid in read
%.*s: Passphrase is correct
%.*s: Failed to open top disk image node.
%.*s: Reached an invalidation handler for the IO daemon connection
%.*s: Unlocked using symmetric key
%.*s: Disk image resized to %llu bytes
%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)
%.*s: Copied sandbox extension token from reopened backend (length=%zu)
%.*s: DiskImages2 framework version: %s
%.*s: File system is %{public}s
%.*s: Erasing %{private}@
%.*s: Verify passed
%.*s: Passphrase found in keychain, unlocking the image
%.*s: Registry entry ID is 0, can't check %s property
%.*s: entry with %{private}@
%.*s: waitForSLACompletion returned error: %{public}@
%.*s: Got to XPC interruption handler
[0x%08x](warning) %{public}s
%.*s: Keeping RO mode for %{private}@
%.*s: %{public}@ error %{public}@
%.*s: DIDeviceHandle object is deallocating, invalidating connection
%.*s: isWritableFormat: %s
%.*s: %{public}@ %{public}@
%.*s: XPC connection lost: %{public}@
%.*s: Successfully retrieved WKMS non-shipping key
%.*s: Attaching to an existing device
%.*s: Device will be marked as solid state
%.*s: BSD name: %{public}@
%.*s: Out of memory, failed to allocated %zu bytes for key %@
%.*s: Failed to create graph from plist: %@.
%.*s: Failed to copy source disk image to temporary URL
%.*s: Using an existing shadow file: %{private}@
%.*s: res_dict: %{public}@
%.*s: Device created, attaching to the new device
%.*s: Asking for passphrase using readpassphrase
%.*s: Failed to read passphrase from TTY
%.*s: Looking for encrypted image passphrase in the %s keychain
%.*s: Failed to dup stdout: %d
%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported
%.*s: Cannot open cache file %{private}@ with RW access, trying read-only
%.*s: Failed during ASIF extents enumeration on offset: %llu
%.*s: Conversion completed, output file size: %llu bytes
%.*s: Creating device with %llu blocks of %u bytes, instance ID %{public}@, ABI version %d
%.*s: Image %{private}@ re-opened with RW permissions
%.*s: Shadow format validator exception: %{public}s
%.*s: Issuing new sandbox extension token for file %{private}@
%.*s: Failed opening %{private}s, errno %d
%.*s: Device registry entry ID: 0x%llx
%.*s: IOServiceWaitQuiet timeout occurred, retrying.
%.*s: Asking user permission to store the passphrase in the keychain
%.*s: Decoding plugin instance
%.*s: Error calling back the client via XPC: %{public}@
%.*s: Failed creating semaphore
%.*s: Closing IO service
%.*s: Entry ID of root block storage device: 0x%llx
%.*s: First connection attempt failed: %{public}@, retrying
%.*s: Connection attempt failed: %{public}@, retrying
%.*s: Cannot open shadow chain %{private}@ with RW access: %{public}s, errno=%d
%.*s: Image file %{private}@ opened with flags %d
%.*s: blocks array: %{public}@
%.*s: Device will be marked as supporting persistent attach
%.*s: Failed creating queue
%.*s: Got to XPC invalidation handler
%.*s: User data retrieving passed, %d value(s) found
%.*s: Storing passphrase in the %s keychain
%.*s: Failed to connect to IO daemon for SLA handling
%.*s: Successfully retrieved WKMS shipping key
%.*s: Cache file %{private}@ opened with RW access
%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization
%.*s: Successfully issued sandbox extension token for file %{private}s (token length: %zu bytes)
%.*s: %{public}s
%.*s: XML_RSRC_FORK: %{public}@
%.*s: A valid plist was given, but it has no pstack version key
%.*s: Converting user data
%.*s: Client reported error: %{public}@
%.*s: Failed to open /dev/tty: %d, falling back to stderr
%.*s: Input and output files are the same, using a temporary output file
%.*s: Validation exception: %{public}s
%.*s: Received connection from pid %d with euid %d. Our euid is %d
%.*s: Cancelling conversion (NSProgress cancel requested)
%.*s: Waiting for completion of an ongoing eject of %{private}@
%.*s: Client is entitled to attach disk images
%.*s: Error encoding user dictionary: %{public}@
%.*s: On disk cache is not supported on embedded systems
%.*s: Shadow file %{private}@ opened with RW access
%.*s: Reached an interruption handler for the IO daemon connection
%.*s: Disk image file is not backed by local storage, root device entry ID will be the disk image device itself
%.*s: Attaching a quarantined image
%.*s: [Apple Internal] Creating an emulated external disk
%.*s: fstat failed with errno %d
%.*s: User data embedding passed
%.*s: Pager command failed with status %d, output may be incomplete
%.*s: Creating connection to %{public}@
%.*s: On disk cache path: %{public}@
%.*s: Controller euid: %d
%.*s: Run loop aborted
%.*s: entry: %{public}@
%.*s: Keychain item requires ACL upgrade
%.*s: Failed to dup stderr: %d
%.*s: SLA detected, connecting to IO daemon for user acceptance
%.*s: Failed initializing plugin: %{public}@
%.*s: numBlocks queried for an empty shadowChain.
%.*s: Setting oneshot XPC instance
%.*s: SLA detected, returning to client for acceptance
%.*s: Creating %s plugin instance with params: %@
%.*s: Received: %{public}@
%.*s: Missing parameters
%.*s: WARNING: Found %llu sectors with invalid flags (has_bitmap)
%.*s: Not a UDIF: %{public}s, assuming RAW format
%.*s: Converting to %{public}@
%.*s: Controller path: %{public}@
%.*s: IOServiceWaitQuiet done
%.*s: Failed to open pager, writing directly to stdout
%.*s: %{public}@
[0x%08x] %{public}s
%.*s: Performing in-place squash optimization
%.*s: Due to the conversion error, erasing the output file
%.*s: Not a sparseimage: %{public}s
%.*s: %{public}@ - %{public}@ %{public}@
%.*s: Not a pstack
%.*s: entry
%.*s: Got error from last XPC command: %{public}@
%.*s: Using existing disk image params
%.*s: Cleaned up folder copy connection
%.*s: No matching item found in keychain
%.*s: Moving %{private}@ to %{private}@
%.*s: cancelSLA wait returned error: %{public}@
%.*s: Client acknowledged receiving the device handle
%.*s: Failed to dup2 to stdout: %d
%.*s: Failed to erase output URL
%.*s: %@
%.*s: Using %{private}@ as read-only
%.*s: Failed to delete %@: %@
%.*s: stderr duplicated
%.*s: New disk image size is the same as previous
%.*s: I/O error at offset %lld iov_count %d errno %d
%.*s: Creation failed, erasing %{private}@
%.*s: Invalid key: %@
%.*s: %{public}s, errno=%d
%.*s: Error checking %s property: %s
%.*s: Creating connection with %{public}@
%.*s: Failed instantiating rawTestPlugin object: %s (code %d)
%.*s: Failed to get UUID info of provided image.
%.*s: Device will be marked as high throughput
%.*s: Keychain lookup returned %d
%.*s: Unlocked using public key
%.*s: Using an existing cache file %{private}@ with RO access
%.*s: Creating NSXPC listener on %{public}@
%.*s: Creating connection to IO daemon clients listener
%.*s: <%lu> %{public}s
%.*s: Failed to generate device identity: %@
T@,&,N,V_remoteProxy
_nbyte
copyParentWithError:
removeObjectAtIndex:
retainCount
updateQuarantineFlagWithHandlerArray:flags:buffer:error:
createDiskImageParamsWithError:
T@\"NSNumber\",R,N,V_overrideBlockSize
addToRefCountWithError:
replaceDiskImageWithUnlockedBackendXPC:error:
self
setCacheBackendXPC:
verifyNodes:error:
askPermissionWithRememberPassword:error:
isDeviceWithProperty:registryEntryID:predicate:
UTF8String
initWithPluginName:pluginParams:pstackURL:tag:error:
objectForKeyedSubscript:
reverseObjectEnumerator
terminationStatus
T@\"NSMutableArray\",R,N,V_nodes
decodeObjectOfClass:forKey:
dictionary
frameworkBundle
_outputURL
setInputMountedFrom:
_commandSize
_parentUUID
allowOnDiskCacheWithSinkDiskImage:
keychainUnlockWithIsSystemKeychain:error:
backend
initWithFormat:
TB,N,V_singleInstanceDaemon
_isCache
pipe
initWithParams:
arrayWithObject:
getDescendants
initWithCapacity:
initWithGraphDB:workDir:error:
regEntryID
setUniqueDevice:
setWithObject:
T@\"NSString\",C,N,V_inputMountedFrom
```
