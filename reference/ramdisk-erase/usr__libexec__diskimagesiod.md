# `/usr/libexec/diskimagesiod`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,916,816 bytes.

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
DIEncryptionUnlocker
DISLAFrontend
RamXPC
DIIODaemonDelegate
DICreateRAWParams
DiskImageParamsXPC
DiskImageParamsLocked_XPC
NSXPCListenerDelegate
DIClient2IODaemonXPCHandler
DIIOMedia
DIError
DIKeyRetriever
DICreateUDSBParams
DiskImageParamsUDIF_XPC
DIStatsParams
FileLocalXPC
SerializedDiskImageGraph
DIShadowNode
DIIOClientDelegate
DIControllerProtocol
DIImageHandle
BackendXPC
DIURL
DIDeviceHandle
NSCoding
AAS3DownloadRequest
DIStatFS
DIClient2Controller_XPCHandler
PersistentBackend
DIBaseParams
DIBaseAgentDelegate
DICreateParams
DIDiskArbEmulation
DIAttachedDeviceInfo
DIEncryptionChpass
DIController2ClientDelegate
ReadSynchronizerBackendXPC
KNOXBackendXPC
DiskImageGraph
DIDiskMountTracker
DIDisappearedMountPointDelegate
DIChpassParams
DIDiskImageBridge
DIController2ClientProtocol
DITemporaryPassphrase
PluginBackendXPC
DIHelpers
DISpawnerProtocol
BackendConvenience
DIBlockDevice
DiskImageGraphNode
NSObject
DIAttachParams
DICreateASIFParams
DiskImageParamsRaw_XPC
DiskImageParamsRAM_XPC
QuarantineFileHandler
Private
DIVerifyParams
SparseBundleBackendXPC
DiskImages2
DIImageInfoParams
DIIOIterator
DIExtension
NativeDiskImageGraphNode
NSSecureCoding
DIEncryptionCreator
DIResizeParams
DIBaseAgentXPCHandler
DIShadowChain
DIIOObject
DIIODaemonProtocol
DIBaseServiceDelegate
AEABackendXPC
DIIOCacheDelete
DiskImageParamsPlugin_XPC
workaround
_TtC16FetchRestoreKeys16CryptoKitWrapper
AAS3DownloadSession
DIDiskArb
DIConvertParams
DIBaseXPCHandler
DIParams
CryptoBackendXPC
DiskImageParamsASIF_XPC
DIEncryptionFrontend
cpp_extension
DiskImageParamsSparseBundle_XPC
PluginDiskImageGraphNode
DIIOClientProtocol
DIUserDataParams
@56@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16r^v32Q40^@48
{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_des
@\"DIURL\"
{shared_ptr<crypto::header>=\"__ptr_\"^{header}\"__cntrl_\"^{__shared_weak_count}}
{shared_ptr<unsigned char>=*^{__shared_weak_count}}16@0:8
B16@0:8
B44@0:8r^v16I24^{?=Iq{fsid=[2i]}Q[1024c][2048c]I[32C]I[20C]}28^@36
@\"NSURL\"
@\"NSError\"
B48@0:8@16q24@32^@40
@32@0:8@16^v24
@28@0:8i16^@20
@24@0:8@?16
@24@0:8q16
@\"DiskImageParamsXPC\"
@48@0:8@16@24@32^@40
B40@0:8r^v16@24^@32
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}
^{?=Q*^{AAS3Context_impl}}16@0:8
B32@0:8@16@24
v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24
{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>={?=^{DiskImageInfo}}}28@0:8B16^@20
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8B16B20
@\"DIDiskArb\"
Ai
v32@0:8@\"DIEncryptionFrontend\"16@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">24
r^v16@0:8
B40@0:8@16@24^@32
v24@0:8B16B20
v32@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16
@\"NSURLSession\"
@\"NSDictionary\"
@40@0:8q16@24^@32
@\"NSProgress\"32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24
@\"NSString\"
v20@0:8B16
B40@0:8@16q24^@32
B24@0:8^@16
@56@0:8@16q24@32@40^@48
@36@0:8@16i24^@28
B24@0:8r^v16
@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}24
@28@0:8I16^@20
v24@0:8@?16
v24@0:8^{IONotificationPort=}16
i16@0:8
@\"DIStatFS\"
{shared_ptr<DiskImage>=^{DiskImage}^{__shared_weak_count}}60@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16Q32r^v40B48Q52
i24@0:8@16
I16@0:8
@\"NSArray\"
{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>={?=^{diskimage}
B40@0:8r^v16^v24^@32
@\"DIIOMedia\"
@\"DiskImageGraphNode\"
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}}16@0:8
@48@0:8r^v16Q24^v32^@40
@56@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24^Q40^@48
@32@0:8^{diskimage_open_params=^{diskimage_open_params_impl}}16r^v24
@32@0:8^v16r^v24
@24@0:8r^v16
Q32@0:8@16Q24
v16@0:8
Vv16@0:8
*
B40@0:8^B16^B24^@32
@\"DIClient2Controller_XPCHandler\"
@?16@0:8
i
v40@0:8@16@24@?32
@28@0:8@16B24
@\"NSMutableDictionary\"
B40@0:8@16^@24^@32
@32@0:8^v16^@24
i40@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16Q24q32
@\"DIShadowChain\"
{unique_ptr<udif::header, std::default_delete<udif::header>>=\"\"{?=\"__ptr_\"^{header}}}
@\"NSObject<OS_os_transaction>\"
v48@0:8@16@24@32@40
B36@0:8i16@20^@28
@24@0:8^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}16
v40@0:8@\"DIEncryptionCreator\"16@\"NSString\"24@?<v@?@\"DIEncryptionCreator\"@\"NSError\">32
@\"NSMutableData\"
B24@0:8Q16
B40@0:8^v16Q24^@32
B24@0:8:16
{shared_ptr<crypto::passphrase_header>=\"__ptr_\"^{passphrase_header}\"__cntrl_\"^{__shared_weak_count}}
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
#16@0:8
@40@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24
@16@0:8
@\"DIIOClientDelegate\"
v24@0:8Q16
^{_NSZone=}16@0:8
v24@0:8^{__DADisk=}16
B48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
@20@0:8I16
^v
^{__CFRunLoopSource=}
@32@0:8@16^@24
@32@0:8@16@24
B40@0:8q16@24^@32
{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"\"{?=\"__ptr_\"^{header}}}
@32@0:8#16@24
@28@0:8i16@20
v40@0:8@16q24@?32
v24@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16
v24@0:8^v16
B56@0:8@16^@24*32^Q40^@48
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}16@0:8
B48@0:8^v16*24Q32^@40
B28@0:8I16^@20
@36@0:8Q16B24^@28
@24@0:8^{DIRequestsStatsArray=[48{DIRequestStat=IIQQQQ}]I}16
v32@0:8@\"DIVerifyParams\"16@?<v@?@\"NSError\">24
@36@0:8@16i24Q28
@24@0:8Q16
@\"DIAttachParams\"
v40@0:8@16@24@32
@\"FileLocalXPC\"
@24@0:8@16
@24@0:8^@16
B24@0:8@\"Protocol\"16
B40@0:8@16I24I28^@32
@40@0:8@16^{__SecCertificate=}24^@32
@\"DIDiskMountTracker\"
B32@0:8q16^@24
B40@0:8r*16Q24^@32
B48@0:8@16*24Q32^@40
@32@0:8@16@?24
@24@0:8r*16
B40@0:8@16*24^@32
@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>={?=^{header}}}24
@\"NSMutableArray\"
v24@0:8@16
@\"NSTimer\"
Q
^{IONotificationPort=}16@0:8
AQ
@
@32@0:8q16@24
{unique_ptr<diskimage_uio::diskimage_open_params, std::default_delete<diskimage_uio::diskimage_open_params>>=\"\"{?=\"__ptr_\"^{diskimage_open_params}}}
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v24@0:8@\"NSCoder\"16
v24@0:8@?<v@?@\"NSError\">16
@\"NSString\"16@0:8
@24@0:8@\"NSCoder\"16
v20@0:8I16
@\"NSLock\"
B32@0:8Q16^@24
B32@0:8@16@?24
B44@0:8@16#24B32^@36
@24@0:8r^{?=Iq{fsid=[2i]}Q[1024c][2048c]I[32C]I[20C]}16
v24@0:8*16
{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<
@40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
{expected<std::shared_ptr<Backend>, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<std::shared_ptr<Backend>, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<std::s
@36@0:8@16B24^@28
@\"AAS3DownloadSession\"
@\"DIBaseParams\"
@\"NSObject<OS_dispatch_queue>\"
@\"NSObject<OS_dispatch_semaphore>\"
@28@0:8@16i24
B48@0:8i16r^{?=Iq{fsid=[2i]}Q[1024c][2048c]I[32C]I[20C]}20I28^v32^@40
@32@0:8r^v16^@24
B36@0:8@16B24^@28
v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}16
@28@0:8i16B20B24
@56@0:8@16@24@32@40^@48
Q16@0:8
i32@0:8^v16Q24
v24@0:8q16
v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSFileHandle\"@\"NSError\">24
@64@0:8@16Q24q32*40^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}48@56
@44@0:8@16^{?=Q*^{AAS3Context_impl}}24I32f36I40
B40@0:8*16@24^@32
B24@0:8@16
@\"DIClient2IODaemonXPCHandler\"
v24@0:8@?<v@?>16
{optional<iokit_utils::di_io_connect_t>=\"\"(?=\"__null_state_\"c\"__val_\"{di_io_connect_t=\"connect\"I})\"__engaged_\"B}
@\"DIDeviceHandle\"
v32@0:8@\"DIDeviceHandle\"16@?<v@?@\"NSError\">24
@\"BackendXPC\"
{shared_ptr<Backend>=\"__ptr_\"^{Backend}\"__cntrl_\"^{__shared_weak_count}}
@\"NSMutableURLRequest\"
B24@0:8#16
@\"NSObject<OS_dispatch_source>\"
v24@0:8^{__DASession=}16
B32@0:8^B16^@24
B40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
i40@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16^@32
@\"NSXPCListenerEndpoint\"
v24@0:8@?<v@?@\"DIDeviceHandle\"@\"NSError\">16
i44@0:8@16@24I32^@36
v24@0:8^{__CFRunLoopSource=}16
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16@0:8
B56@0:8@16@24@32@40^@48
B32@0:8@16^@24
f16@0:8
^{?=Q*^{AAS3Context_impl}}
@40@0:8r^v16@24^@32
v32@0:8@\"DIAttachParams\"16@?<v@?@\"NSError\">24
@32@0:8@16Q24
@\"NSMutableSet\"
@\"DIIODaemonDelegate\"
@?
v20@0:8f16
@\"DICreateParams\"
@40@0:8@16@24^@32
@52@0:8@16@24@32@40B48
I
v20@0:8i16
B48@0:8@16Q24q32^@40
B28@0:8i16^@20
@68@0:8@16@24@32@40@48@56B64
@20@0:8B16
@\"NSUUID\"
@\"DITemporaryPassphrase\"
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}
@\"NSNumber\"
@40@0:8@16Q24^@32
@36@0:8i16@20^@28
@48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
B48@0:8@16@24@32^@40
q
v32@0:8@16@?24
@\"NSData\"
@\"NSXPCConnection\"
B48@0:8r^{AuthData=^{AEAAuthData_impl}}16*24Q32^@40
^{IONotificationPort=}
^v16@0:8
@32@0:8r^v16@24
@24@0:8I16B20
@32@0:8:16@24
@40@0:8r^v16Q24^@32
@\"NSString\"24@0:8^@16
{expected<diskimage_uio::diskimage_open_params, std::error_code>=(storage<diskimage_uio::diskimage_open_params, std::error_code>=c{diskimage_open_params=^{diskimage_open_params_impl}}{error_code=i^{error_category}})B}16@0:8
{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16@0:8
@32@0:8Q16^@24
B
@24@0:8:16
@40@0:8:16@24@32
v40@0:8@16@?24@?32
{atomic<bool>=\"__a_\"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=\"__a_value\"AB}}
@\"NSXPCListener\"
@40@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16^@32
f
@56@0:8Q16q24*32^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}40@48
v32@0:8@16@24
B36@0:8B16q20^@28
q16@0:8
^v24@0:8^@16
B32@0:8r*16^@24
v40@0:8@\"DIEncryptionFrontend\"16q24@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">32
@32@0:8Q16@24
^{__DASession=}16@0:8
B64@0:8r*16Q24{function<bool (iokit_utils::di_io_obj_t)>={__value_func<bool (iokit_utils::di_io_obj_t)>=(type=[24C])^v}}32
B40@0:8Q16^v24^@32
*16@0:8
q40@0:8^v16Q24q32
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8^@16
v32@0:8@\"DIStatsParams\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
^{__CFRunLoopSource=}16@0:8
Q32@0:8@16^@24
Q24@0:8^@16
v32@0:8@\"DIAttachParams\"16@?<v@?@\"DIDeviceHandle\"@\"NSString\"@\"NSError\">24
B28@0:8B16^@20
{shared_ptr<unsigned char>=\"__ptr_\"*\"__cntrl_\"^{__shared_weak_count}}
v28@0:8@16B24
@\"<DIDisappearedMountPointDelegate>\"
^{__DASession=}
@60@0:8@16@24@32@40@48B56
Missing OIDC client ID in appinfo response
unmap_iterator_t di_asif::details::table::unmap(ContextASIF &, const unmap_extent_t *, size_t)
A controller XPC service attempted to connect to an existing device, but this daemon instance has no such device yet
Invalid format for shadow file
Failed to open crypto header
Write error: 
gcd::gcd_timer_source::gcd_timer_source(gcd_queue &, dispatch_time_t, uint64_t, uint64_t)
UDIF uncompressed read-only image
=
Malformed SLA LPic resource
mapped blocks of band 
Content-Type:
com.apple.diskimages.band_management
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
Missed an evictable slot
Key from the certificate is not exportable
-[DIIOClientDelegate addToRefCountWithReply:]
file of 
mountedOnURL
Cache is not supported when using pstack.
Diskimageuio: can't get file descriptor, backend doesn't exist
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Mount Point
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:172:22)]
downloadStreamPRead
The type option contains an invalid value for 
eject timeout
Constructing sb context
%@: %@
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
A mandatory argument is null in a DiskImages2 API call. Remember to check if init succeeded
di_plugin_image_t *PluginsManager::decode_plugin_image(const di_plugin_t &, const diskimage_decode_fn_t &, void *)
Can't lock entry
header read-only flags
metadata_flags_t
, errno=
-[DIClient2IODaemonXPCHandler createConnection]
blockSize
instanceID
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293
, errno 
Failed to parse key in KVS (zero size key).
Cannot stack images with different block sizes
getToken
checksum_type
could not create service iterator (end)
01234567
Cannot store an empty passphrase
 bytes are above the sparsebundle limit of 
Failed to create matching dictionary for device class 
v16@?0@\"NSTimer\"8
Key transcoding failed.
x-amz-
dataTaskWithRequest
header_flags
 - same 
Write zeros to unmap unaligned end region failed (err code
Decoding error.
-[DIIODaemonDelegate setupNewConnection:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hard
device with registry entry ID 0x
vector
Empty Bytes
None
[start: 
The image is encrypted with obsolete encoding version 1
Exception: %s
. Opening as root
file(
DIIOManager::~DIIOManager()
bool DIIOManager::fetchCacheStat(uint64_t &, uint64_t &)
Failed initializing RAM disk buffers
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp
Failed to get data from self signed certificate
%12.2f MB/s download speed\n
Failed to sign request\n
raw
device not found in registry
Unsupported block size for image format
com.apple.wkms.fcs-key-url
invalid field %u
-[DIAttachParams reOpenIfWritableWithError:]
Plugin 
asif_header
-[NativeDiskImageGraphNode deleteImage]
Disk image is terminated, skipping read
frk_set_device_identity_certificates
 instead
int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)
run_type
CFAutoRelease<CFDictionaryRef> udif::details::UDIF_base::get_resources() const
auto trim_data(const sg_vec::iterator &, const sg_vec::iterator &, size_t, const io_result_t &)::(anonymous class)::operator()(const auto &, const auto &, size_t) const [src:auto = sg_vec_ns::details::sg_vec_iterator, dst:auto = sg_vec_ns::
io_result_t DiskImage::Context::read(const sg_vec::iterator &, const sg_vec::iterator &)
User data is not supported in this image format
v32@?0@\"NSURL\"8Q16^B24
metadata
Disk image URL is too long
read only
rings_queue
segment_count_none = 0, segment_count_one = 1
Cannot save DiskImageGraph without specifying pstack URL
PKCS7 = 7
i
-[DIIODaemonDelegate reconnectAfterRespawnWithInstanceID:reply:]
Can't connect to driver
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Diskimageuio: single image given, but role is 
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
plugin://%@
The format specifier for 
Failed to create dispatch source for kqueue
Not enough space for metadata
, trimmed size
,
The argument index is invalid
read_only_cache = bit(0)
AEA
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
virtual int BackendSG::read(const sg_entry &)
+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]
-[DIDiskArbEmulation waitForDAMountWithExpectedCount:diskTracker:]
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
udzo
disk arbitration framework returned an error
Couldn't read sparseimage header
daw
header_size_512 = 512, header_size_4k = 4096
0b
fileMode
Bundle's lock file is closed
Ignoring truncate on block device
-[DIIODaemonDelegate resumeAttachAfterSLA:completionReply:confirmReply:]
wkms-dev.sd.apple.com
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c
;
emulateExternalDisk
Diskimageuio: get stackable uuid failed 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
crypto_op: can't initializae aes_cbc context
Cannot acquire 
public_key_crypto_algo_mode
diskimageuio: pre-write final error 
Diskimageuio: Failed to create resizer: 
Diskimageuio: backend isn't locked
Failed creating bands folder
 bytes)
-[DIDeviceHandle waitForQuietWithService:error:]
IOServiceMatched
UDIF read-only compressed image
The type option contains an invalid value for a string formatting argument
uniqueDevice
Failed to increase file size, pwrite returned 
Plugin struct size 
YES
Request failed with HTTP error: %lu %@: %@\n%@
band-size
Shadow underlying FS
Context setup failed.
s3Perform retry after %u ms
flags validator
 is incompatible with the framework, expected 
 - unmap_range: [
com.apple.diskimages.creator-uc
 doesn't exist
%@[ramsize=%llu]
fully
blocks_signature
intermediate-certs
The format string contains an invalid escape sequence
download
BackendSG: error allocating buffer
CacheURL
virtual int DiskImage::set_size(uint64_t)
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
 src size 
index
Encryption Method
Info.plist
Read-only image cannot be resized
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
vbuf validator
OK
Can't flush asif on map element close, backend barrier failed
Block device block size is larger than image block size
Size cannot exceed max ASIF size
Failed to get registry entry ID, ret %d
fstatfs failed with err code
encryption: header size mismatch
The value of the argument index exceeds its maximum value
com.apple.diskimages.band_unmap
shouldValidate
crypto
Key Size
Invalid path property (not UTF8)
shadowChain
Medium Type
static std::string FileDescriptorWrapper::handle_open_from_error_message(int, const std::string &, int, int)
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
Calling 
virtual int BackendSG::truncate(uint64_t)
+[DIAttachedDeviceInfo copyAllMountPoints]
Failed serializing user dictionary
maxRawUDIFRunSize
Convert AEA key from hex failed
Missing key in Knox response
size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)
fskit
commandSize
com.apple.diskimage.sparsebundle
UDIF: compressed runs should be <= 1MB
version_t
Invalid value for asif header field: %s
 = offset = 
com.apple.diskimage-test-plugin.raw
certificate
Backend barrier failed after dir offset changed, error 
ASIF: failed to write metadata
ASIF: missing internal metadata key
createErrorContextKey
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Failed during table 
-[DIIODaemonDelegate setupNewConnection:]_block_invoke
Diskimageuio: reopen backend to required mode 
Starting flush
&
, flags = 
static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
Compressed Length
Cannot find AmberDiskImagePluginCreate in libAmber
: 
Unsupported ASIF version 
-[DIDeviceHandle updateBSDNameWithBlockDevice:error:]
 [
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__hash_table:1892: lib
PUT
Cannot attach RAM disk as a read-only device
expected<int, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_file_descriptor() const
bundle-backingstore-version
Accept
Failed to add public key entry to auth table
Solid State
Default
Unaligned metadata entry size
field size too large
Failed to create kqueue
LaunchInstanceID
End of input while parsing format specifier precision
void SparseBundleBackend::write_info_plists()
Can't read for defrag
asif: chunk size is too small, too many dir indices
Crypto: can't read crypto header
 - map_range: [
GET
s3Perform
\\x{
 mode=
void di_hybrid_subscriber_t::cancel()
v32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
static void process_terminator::terminate()
saks-ac-prod.g.apple.com
invalid flags
No mapped file for band 
HTTP request failed with status code: %ld
len: 
Diskimageuio: Snapshot detected on top of cache
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
Evicting all bands for eject
Role
s3DownloadStreamOpen_urlsession
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr(image_format, std::shared_ptr<Backend> &, bool, const std::filesystem::path &, size_t)
 completely
) to type
Can't create data for plist deserialization
], cmd=
KVS dataBuffer allocation failure.
Non supported options in AAS3DownloadSession (ignored): proxy_headers %s
UDZO
-[DIUserDataParams retrieveWithError:]
Unmap done
Failed to read 
an integer
virtual di_coroutines::Task<void> CompressedBackend::run_futures()
Corrupted plist dictionary
+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke
Can't flush asif table, bitmap flush failed 
descriptor_special
int crypto::crypt_op::crypt_consecutive_vector::operator()()
-[DIIODaemonDelegate exitDaemon]
Failed to retrieve file info for index %u (status 0x%x)
void DIIOManager::drainDormantQueue()
) is unlocked
futimes failed on 
true
, band was written to
isCache
Can't read bitmap
TEXT
IV_TWEAK_SIZE_16 = 16
allocated: size change callback failed with 
could not create service iterator (begin)
IOBlockStorageDriver
--ram
Request failed
The precision option does not contain a value or an argument index
%@: %s
pluginParams
 auth entries
KEY_BITS_160 = 160, KEY_BITS_NONE = 0
 offset = 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
) is locked
Can't parse encryption entry: 
userData
Opened bundle's lock file with flags 0x
Failed opening mapped blocks file for 
backend write failed during locked flush of map element, error 
Cannot load libTestPlugin
readSynchronizer
void udif::details::UDIF_base::print_checksum_verification_status(const std::string &, const csum_any &, const details::checksum &) const
BZIP decompression failed, res=
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
AEA key retrieval failed
knox.sd.apple.com
Tag
More than one image in the stack has the provided tag, please specify UUID instead.
void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/crypto/crypto_format.cp
absolute_offset
X-Amz-Content-Sha256: %s
Reserved
Cannot create target image format with the block size of the source image
Failed converting CFNumber to longlong
Disk image is terminated, skipping unmap
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
-[DICreateParams onErrorCleanup]
Chunk Size
 but buffer is too small 
exclusive
crypto_format: cookie differs
ERROR: wrapped-key failed base64 decode
Udif: needs to read 
Awaitable completed in unexpected state
Couldn't upgrade lock entry
-[DIIODaemonDelegate attachToExistingDeviceWithParams:reply:]
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
plist
Unsupported ASIF, contains data beyond current header struct size
Invalid UDIF, run is not within block boundary
The disk image format is not supported by this OS
Failed to get plugin instance
+[DICreateParams eraseIfExistingWithURL:error:]
segment_count_t
fd block size retrieval failed (err code 
Passphrase cannot be empty
 is different than current mode 
/usr/lib/libAmber.dylib
url
Error: Not enough data read. expected: 
Diskimageuio: decryption key missing
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
Unsupported URL scheme
table entry map@
Missing parent node in graph.
ulfo
 for 
 logical: 
 io_start_offset: 
{:02x}{:02x}
The image is encrypted but has no passphrase auth entry
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433:
Failed writing sparsebundle info
version
Failed unlocking file with fd 
device with dev name 
Contains non-hexadecimal characters.
wrapped-key
Closing an unchanged 
secondaryKey
managed
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
Disk image is terminated, skipping future_unmap
bool DiskImageSparseBundle::try_unmap_band_extents_without_list(uint64_t, const extents_set_t &)
Retrying request after %.0f seconds %zu bytes at offset %llu
com.apple.DiskImages2.ErrorDomain
Failed to fetch stats from driver
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
knox-uat.sd.apple.com
virtual int Backend::write(const elements_t &)
static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
udsb
Diskimageuio: Invalid pstack element: 
 cannot be re-registered
Placed new 
void plugin_encode_buffer(void *, const char *, const void *, size_t)
Can't write UDIF resource part
virtual int CompressedBackend::read(const sg_entry &)
mountedFrom
Output of disk image conversion must be a file
is_locked
/dev/%s
int ExecutionEngineCommand<CommandQueue, MachPort>::execute_work(unsigned int, bool) [Container = CommandQueue, Port = MachPort]
bool DIIOManager::stashFileInformation(DIAttachParams *__strong)
Unexpected context construction by 
 err: 
Using automatic argument numbering in manual argument numbering mode
StandardCompressedBackend::pimpl::pimpl(algo_t)
Missing key in SAKS response
Metadata offset is invalid
which is larger than allowed 
Can't get key in cstring format
ASIF: can't set requested uuid
Cannot get subscriber from plugin
Can't read encryption table, error 
The format specifier contains malformed Unicode characters
void sparse_bundles::open_bands_t::remove(uint64_t)
https://%@/westgate/appinfo
CFUserNotificationReceiveResponse failed
attempting to authenticate with saks
bool di_asif::details::table_entry_data::validate() const
X-Amz-Security-Token: %s
Failed to write metadata
 closed
-[DIIOCacheDelete eraseOldCacheFiles]
startIO called more than once
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
Feature or image not supported by library
Invalid band size (
Unexpected unmap command received on read only image
AppleDiskImagesController
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
fetch_restore_keys_key_handling.m
-[AAS3DownloadSession syncRequests]
 
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::verify_backend() const
Can't connect to device
auto sparse_bundles::Band::get_mapped_blocks()::(anonymous class)::operator()() const
static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)
buffer[0]=[ptr=
-[DiskImageParamsXPC createDiskImageWithCache:shadowValidation:]
UDIF XML at 
 overrun events occurred in the plugin's ring!
sendEvent of type 
auto hdr_get_nr_blocks(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
Couldn't read asif's full header
Daemon no longer available
Request creation
Single element in pstack that isn't an image
Unexpected ASIF header length (
Failed to update asif header
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
 folder
clientID
sha1 too many bytes
CBCPADIV8 = 6
 size = 
-[DIIODaemonDelegate createShadowNodeWithBackend:fileIndex:error:]
Sparsebundles on SMB mounts are not supported on this system
Failed converting URL to UTF8
Corrupted plist
Background close of 
UDIFDiskImage: failed truncating image
, size=
void sparse_bundles::Band::ContextsList::clear()
Not valid SAKS metadata (no environment field)
-
public_key_padding_algo
NONE = 0
AAS3ContextSetFieldString
0B
outputFormat
knox-dev.sd.apple.com
Backend does not support file descriptor access
alternate form
virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)
Diskimageuio: is cache image failed 
, dirty=
Bitmapped Entries
Diskimageuio: Couldn't get diskimage: 
Failed to get instance ID from dormant device
ERROR: Shipping private key is NULL.
virtual io_result_t DiskImageUDIFRead<UDIFReader<locks::None>, DiskImageUDIF>::read(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &) [UDIF = UDIFReader<locks::None>, UDIFVariant = DiskImageUDIF]
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
ASIF block size isn't multiple of 512
Diskimageuio: Required read-write disk image (
ShadowChain: %@
The width option should not have a leading zero
Internal backend write() failed. ret=
Image has a read-only format, attach failed due to force RW flag
Diskimageuio: Can't create stackable image: 
Diskimageuio: get parent uuid failed 
bands
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
ULMO
System Entities
Failed placing new 
Num Tables
Backend barrier failed during bitmap allocator failures handling, error 
Transfer-Encoding:
bool sparse_bundles::open_bands_t::insert(uint64_t)
com.apple.diskimage-plugin.amber
Looking for existing bands
uid temporarily set to 
 auth entry
path
Driver returned error code 
LPic
shared
inode
v1/ac/decrypt
Failed to create DADisk during eject
The requested URL is an existing regular file
Couldn't lock entry
UDIF XML length 
virtual int FileLocalAsync::lock()
Backend: failed writing element in vector
New password
High Throughput Options
Band data is partial, reading 
tkn
Failed barrier after writing full dir
 not found in registry
slaText
devicePrivateKey
locale-specific form
di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke
Info.bckup
Error creating disk image params
-[DIBaseServiceDelegate init]
POST
s3HeaderAppendWithFormat
void udif::details::UDIF_base::generate_blocks(CFArrayRef)
ERROR: enc-request failed base64 decode
flush
Could not generate daw token - AppleConnect Failure
plugin
Read error: 
Duplicate shadow values for: %@
\\'
-[DIConvertParams shouldPerformInplaceSquash]
ASIF max chunk size in header exceeds the limit
saksKey
rdisk
int sparse_bundles::mapped_blocks_t::flush()
uid restored to 0 (res=
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
com.apple.knox.url
virtual int CommandDispatcherImpl::CommandDispatcherContextImpl::execute(Command &)
User-Agent
getErrorContextKey
auto FileLocalAsync::shared_state_t::init_unmap_zeros()::(anonymous class)::operator()() const
-[DiskImageGraph initWithBaseImageURL:tag:error:]
Compressed Offset
Remember password in my keychain?
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__memory/unique_ptr.h:
-[DIIODaemonDelegate finalizeSetupWithParams:service:connection:error:]
Content-Type
Integral value outside the range of the char type
Invalid size of saks response %lu
image_variant_type
std::unique_ptr<DiskImage> diskimage_uio::details::diskimage_open_params_impl::transfer_disk_image_ownership()
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
UDIFDiskImage: failed flush after user data write
File: Couldn't fetch status, error: 
Found a valid file for 
AAS3DownloadStream (NSURLSession)\n
Plugin initialization failed
Failed truncating plist
https://%@/v1/ac/decrypt
Could not stat shadow file
lock_backend
ASIF: Entry dirty bit is set when reading from disk
io_result_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
h
Compression Ratio
inputMountedFrom
set_euid_wrapper::set_euid_wrapper(uid_t)
The underlying file system doesn't support writable images with 
Failed initializing shared buffers
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
Diskimageuio: resolved disk image format 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
application/octet-stream
IOMedia device not found in registry iteration
Error decrypting data using public key, error code 
saks-ac-dev.g.apple.com
Diskimageuio: can't get Diskimage attribute, unknown header format
diskimageuio: pre-write first error 
Failed to initialize IO manager
void DIIOManager::setupDriver()
com.apple.diskimage-test-plugin.julio
SparseBundleBackend::SparseBundleBackend(int, bool, const shared_ptr<FileLocal> &, const shared_ptr<crypto::format> &)
(err 
Cannot lock bundle, ignoring: 
void boost::uuids::string_generator::throw_invalid() const
 (our euid is 
AWS4-HMAC-SHA256\n
Using compression 
disk image
/usr/local/bin/appleconnect
Bakcend not initialized for file
prng_algorithm_type
com.apple.diskimagespawner.xpc
The type does not fit in the mask
 buffer_size: 
com.apple.DiskImages2.TelemetryManager
Cleaning up!
passphrase
Shadow path %@ is not a valid file
Table flush failed during dir flush: 
Invalid instance ID format
Passphrase is too long
Not valid SAKS metadata (json format expected)
, allocated: 
Image key encoding failed with err code 
Agree Y/N? 
File descriptor 
handleRefCount
Failed to get path for shadow %zu
saks-ac-uat.g.apple.com
Diskimageuio: backend doesn't exist
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
Apple sparse image
ASIF meta header trailer isn't equal to zero
Destination folder URL must represent an existing folder.
virtual io_result_t sparse_bundles::Band::read(DiskImage::Context &, const sg_entry &)
oidc
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486:
RootDeviceEntryID
Reserved part isn't zeroed
is_writable
, Force closing.
Context creation failed.
virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()
-[DIIODaemonDelegate reopenStashedFilesWithUserClient:outBackends:error:]_block_invoke
ERROR: This archive does not contain a shipping key response.
The numeric value of the format specifier is too large
Cannot display SLA: no terminal or stderr to write to
Failed during ASIF extents enumeration.
Couldn't trim entry in write 
Asif header size unaligned
[
Checksum Value
Failed to read passphrase
https://%@/spaces/%@/files/%@/decryption-components
ssize_t plugin_decode_buffer(void *, const char *, void **)
Blocks header
(empty)
Does not contain an \"even number\" of hex digits.
No
internal metadata
[empty]
lzfse
virtual void DiskImageSparseBundle::on_eject()
Cannot increase size of a block device
no_match
-[DIStatFS initWithFileDescriptor:error:]
Invalid user data content
random generation failed with err code 
NO
The operation was cancelled by the user
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
Failed to create CFString for property key or value
PstackVersion
-[DIEncryptionFrontend storeInKeychainWithPassphrase:forceSystemKeychain:error:]
attempting to authenticate with kms
 error = 
IOBlockStorageDevice
BufferedWriteBackend doesn't support per io crypto
Diskimageuio: UDIF header changed while unlocked
v32@?0@\"NSMutableDictionary\"8Q16^B24
com.apple.diskimagesiod.ram
Failed to use the passphrase that was given
Opening mapped blocks for 
rawTestPlugin_t::~rawTestPlugin_t()
-[DIImageHandle resizeToSize:error:]
UDIF: Can't get resource array
Unexpected failure to get image info: 
Identity Info
Failed to create public key auth entry
Backend: failed reading element in vector
Device Characteristics
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
 in dir I/O, error 
disk
Mapped Sectors
-[DIConvertParams prepareConvertWithError:]
expected<image_format, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::query_image_format() const
-[DIVerifyParams verifyWithError:]
virtual int FileLocalAsync::disable_file_zero_padding() const
 ret: 
Failed to drain dormant I/O queue, status=
ERROR: shipping key enc-request failed base64 decode
hdid-pid
-[DIBaseAgentXPCHandler createConnection]
not a disk image
Error creating backendXPC
Failed to get canonical path for sandbox extension
Image does not have write permissions
Unexpected UDIF header length (
com.apple.diskimages_cache_update
int CommandDispatcherImpl::CommandDispatcherContextImpl::unmap(const Command &)
Failed to update crypto header
-[BackendXPC tryCreatingCryptoHeader]
Failed to find IO media entry for %@
ASIF: data entry - invalid reserved bits
Can't flush asif table, backend write failed
void SparseBundleBackend::read_info()
 doesn't exist, returning zeros
-[RamXPC createRamBackend]
Failed to subscribe to the plugin's IO ring
Destructing sb context
Can't load asif dir table
leaf-cert
eject
/System/Library/PrivateFrameworks/DiskImages2.framework
RAW
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_stackable_uuid() const
kern_return_t was 
Failed getting runloop source
IOServiceTerminate
bytes=
Start Offset
Plugin's ring resumed, ret code 
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
0123456789abcdefghijklmnopqrstuvwxyz
.xpc
Unsupported image stacking
wkms
sign
Disk image operation failed with error code %d
virtual int BackendSG::write(const sg_entry &)
 returned status 
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
, retrying
io_result_t di_asif::details::dir_base::move_realloc_chunk(ContextASIF &, char *, size_t, uint64_t)
ASIF meta header data is unaligned
Device is not a disk image
 existing bands
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
Root daemon connection denied
System keychain access is not allowed on this platform
band_ptr DiskImageSparseBundle::find_band_in_array(uint64_t)
uninit
size
unique_ptr<lock_free::bitmap_t> SparseBundleBackend::get_existing_bands() const
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Harde
could not create iterator (end)
Trying to read @ 
udifHeader
Backend barrier failed during dir flush, error 
algorithm_type
-bytes block size
-[DIAttachParams newAttachWithError:]
Resetting 
Invalid key size
com.apple.diskimagesiod.cachedelete
s3Sign
 rather than image
fchownat failed for 
oauth
ASIF Info
\\\\
ASIF: Header size is less than the min header size
Range: bytes=%llu-%llu
asif
com.apple.diskimages2
 extents
Flush failed after defrag, ignoring. Error 
Allocated after defrag: 
Cannot delete base image node.
Custom encryption entry header size exceeds max size
Compressed(
Unable to get matching services
Failed to start IO after SLA acceptance
creating session
com.apple.diskimages.file.crypto
numBlocks
 failed with 
, UID:GID(Name)=
Failed to set up image for resize
virtual int Ram::_write(const sg_entry &)
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
Udif: advanced buffer, needs to read 
v32@?0@\"DIShadowNode\"8Q16^B24
Apple Inc
CFUserNotificationCreate failed, error code %d
Failed to resize the image
The requested URL is an existing folder
shadowStats
Images Count
Plugin's async ring cancelled, ret code 
Not a pstack.
Diskimageuio: Couldn't lock backend 
ASIF header changed while unlocked
File size is less than the minimum header size
Can't read UDIF trailer
total_size
Writing 
+[DiskImageParamsXPC newWithURL:fileOpenFlags:error:]
ParentUUID
BSD Name
conversionMethod
Diskimageuio: required mode 
ReadOnlyBackend
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
static int FileDescriptorWrapper::open_file(const std::string &, int)
Failed to dup fd for file %u
Can't fulfill kernel's request. command: 
debug.didevice_queue_depth
IOStorageFeatures
lock
Failed to create backend for file %u
Stable UUID
-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]
]
Image
CyrptoKit is missing a required method.
iokit error
truncate error: 
failed to set euid to 
Master checksum
Failed to issue sandbox extension token for file
baseBackend
crypt_consecutive_vector: check errors_in read futures 
Using manual argument numbering in automatic argument numbering mode
std::string FileDescriptor::get_mounted_on_fs() const
Write zeros to unmap region failed (err code
???
 bytes, reading only 
Skipping band erase (in use)
metadata_read_only_flags
UDIF: compression algo is invalid
-[AAS3DownloadSession addRequest:]
The requested operation will delete the active node, please set another one first.
/s3/aws4_request,SignedHeaders=
UTF8
com.apple.wkms.fcs-response
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
band_ptr DiskImageSparseBundle::replace_oldest_band(Band *)
IOServiceOpen failed with status 0x
DES3_3KEY = 17, AES_KEY = 0x80000001
v28@?0Q8^{dispatch_mach_msg_s=}16i24
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:836: libc++ Harde
AWS4-HMAC-SHA256 Credential=
(err code %d)
Failed opening the sparsebundle as user 
Unmapping band 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
 on 
fetch_restore_keys_ephemeral
fetch_restore_key/%s OS/%@
static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)
pstack_header
uri
Failed to setup the plugin's IO ring
Disk image is terminated, skipping write
Failed to parse auth data blob.
inputStatFS
Failed creating CFData
 requested while there are only 
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
CACHE_DELETE_VOLUME
 with 
oauth-id-token:
ASIF: invalid dir index to header
fsync
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:429:
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
Opening band 
Starting unmap of 
int di_asif::details::dir::defrag_table(ContextASIF &, dir_idx_t)
Failed DA init
Unexpected image format from info: 
void diskimage_uio::details::diskimage_open_params_impl::lock_backend_if_required()
decryption-components
UDIF image of 
supportsBarrier
-r
, fd=
iv_tweak_size_t
Range
invalid uuid string
an unprepared device
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
Preferred Block Size
userDict cannot be nil or empty
UDIF: Can't create dictionary resource fork
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ H
URL
com.apple.wkms.auth-data
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
 is 
Nothing to defrag
Failed to allocate raw blob data
IORegistryEntryGetRegistryEntryID failed
IOServiceWaitQuiet error 0x%x
The format specifier should consume the input or end with a '}'
w
Invalid raw UDIF run size limit
Diskimageuio: No diskimage given
com.apple.diskimages.aio
crypto_format: blob length differs
bool DIIOManager::fetchRequestsStat(DIRequestsStatsArray *)
write
Diskimageuio: Single element in pstack that isn't an image
Invalid block size for image
PersistentAttach
outputParams
header_ignore_fields_t
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
dev
Malformed URL format
Failed creating 
prod
%12llu bytes downloaded (%.2f MB)\n
bytes=%llu-%llu
unknown
Mandatory callbacks in the plugin's image struct are missing
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)_block_invoke
writable
Error reading sectors for verify 
Password
image_format diskimage_uio::details::diskimage_impl::query_image_format() const
Bad pstack format, node with active UUID not found.
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
-[DIDiskMountTracker trackIfMyDisk:]
Backend creation failed for file %u: %s
table_entry_data::flags di_asif::details::table::get_next_extent(ContextASIF &, const interval_sectors &, interval_sectors &)
char *udif::header::write(char *)
B24@?0@\"NSURL\"8@\"NSError\"16
supportsPersistentAttach
udzo_max
!
Error creating crypto format
has_bitmap
Validation failed, input contains unexpected data.
fd
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682
overrideBlockSize
hit
enqueueRequest
lzma
IOHDIXHDDriveNub
a pointer
APPLECONNECT.APPLE.COM
Failed to encrypt data using public key from certificate
/dev/tty
Failed creating CFAutoRelease instance.
Failed to validate metadata 
UDIF images are currently not supported in diskimage_uio
 lock, errno 
application/json
+[AAS3DownloadSession completeRequest:data:response:error:]
Data
Skipping erase of 
Bearer openid-id-token-%@
First block of dir write failed with 
Failed writing first block of dir
Unknown checksum found
Disconnected during SLA prompt
Checksum Type
not 
missing DI_ATTACH_ENTITLEMENT on non macos platform
location
Failed to create disk image
-[DIUserDataParams encodeWithCoder:]
stat failed
full_fsync
Cannot find BSD name during respawn
-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]
 band contexts
Locked encrypted image
virtual int FileLocalAsync::_read(const sg_entry &)
void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
), reading from backup
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
 and property 
. returned 
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
Diskimageuio: query format failed 
Diskimageuio: get nr blocks failed 
, disk size: 
174350
crypto_op: can't initializae aes_xts context
 with errno: 
-[DIUserDataParams embedWithError:]
<
crypt_consecutive_vector: write check errors 
BZIP compression failed, res=
v16@?0@\"NSString\"8
Diskimageuio: can't get lock status 
Plugin image struct size 
-[DIShadowChain addShadowNodes:wrapReadOnly:error:]
map_element flush failed on creation
Failed to read crypto header for backend %zu: %s
no more attempts allowed
-o
Decompression failed
Invalid knox URL format. Expected: knox://host/download/space/digest
Legacy prepended-header UDIF image is not supported by this framework
 data: 
-[AAS3DownloadSession readToBuffer:size:atOffset:]
 to 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
Failed opening the file
Segmented UDIF images are not supported by this framework
forwardLogs
Asif header too large
UDIF: Can't find data key in dictionary
sg: buffer = 
cert-chain
Basic information about the IOMedia device is missing
UDSB
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = udif::header]
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
Extent 
v24@?0@\"DIDeviceHandle\"8@\"NSError\"16
File (fd 
attempting to authenticate with wkms
Failed writing full dir
int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
!Q
%@[%@]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669
virtual DiskImageSparseBundle::ContextSparseBundle::~ContextSparseBundle()
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
IsCache
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/Common/Threads.c
Cancel
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_write_iov_t]
ftruncate failed, errno: 
Unsupported public key algorithm.
\\n
)
Can't serialize property list
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc+
KVS data fetch failure.
%s (%@)
 bytes
ASIF: No data offset found (write)
Authentication Data creation failed.
Cannot find image with provided uuid.
-[DIIODaemonDelegate exitWithUnmount]
pthread_once
Failed opening the shadow/cache file(s) with RW access
infnanINFNAN
Diskimageuio: Raw header changed while unlocked
UDIF_header::UDIF_header(const std::shared_ptr<Backend> &)
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_t
int BufferedWriteBackend::reset_last_offset(const sg_entry &)
onDiskCache
ASIF: Content dirty bit is set when reading from disk
Can't load bitmap while setting range
Failed to read file for pstack parsing
static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)
InstanceID
Failed to find dormant device with instance ID
user data embedding failed
 was opened in the background, waiting for it to become available
v24@?0@\"NSDictionary\"8@\"NSError\"16
BufferedWriteBackend
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
com.apple.di_raw_test_plugin
Unable to get IOMedia preferred block size
The replacement field misses a terminating '}'
tr '\\r' '\\n' | fmt | ${PAGER:-more}
User declined SLA
STCK
pstack: unsupported node
Write header failed after dir offset changed, error 
Crypto: Unsupported encryption parameters
Unexpected error creating (unlocked) backend
Barrier failed before dir flush
table entry data@
Diskimageuio: Couldn't get locked status 
sparsebundle
void rawTestPlugin_t::subscriber_t::_resume()
%@ failed with error code %d
Too many mount arguments
DiskImageURL
-n
Can't load bitmap while flushing asif table 
' opened successfully with flags 
-t
virtual FileLocalAsync::~FileLocalAsync()
pending_requests
SLA text is empty
XPC connection failed
Key size isn't a multiple of 8
PKCS1 = 10, OEAP_SHA1 = 0x80000001
ulmo
fchmodat failed for 
-[DIBaseParams tryResolvePstackChain:]
ASIF: can't copy metadata to mutable copy
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
HTTP %u\n
Diskimageuio: image is locked
virtual int FileLocalAsync::truncate(uint64_t)
Cannot decode path
io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)
Overflow detected
https://%@
unmapped
Failed to serialize passphrase to crypto header
dirty = bit(0)
Invalid encryption method
Metadata corrupted 
io_result_inserter_t di_asif::details::table::read(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::data_entries_vectorizer_t::add_data_entry(const data_entry_t &)
device_OBSOLETE = 0, device = 1, partition = 2
static int FileDescriptorWrapper::open_from(int, const std::string &, int)
false
01
 elements returned 
void info::DiskImageInfoASIF::examine_mapped_extents(const DiskImageASIF &)
Couldn't trim entry in read 
Can't load bitmap from backend
 - different calculated: <
public key has an encoding issue or uses an unsupported algorithm
failed to enter SQE to the ring, ret code 
flock returned errno 
 io: 
-[DIIODaemonDelegate createShadowChainWithBackends:error:]
Accept: application/xml
Authorization: %s
NSURLSession read to buffer nbyte=%zx offset=%llx\n
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
Shadow
couldn't allocate space for entry 
Non supported options in AAS3DownloadSession (ignored): pinned_public_key %s
UDRO
Unregistering plugin 
mapped
-[DiskImageParamsXPC createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:]
Spawner failed to reopen file %u: %@
a floating-point
raw_header
static void sparse_bundles::Band::erase(const bundle_commons_t &, uint64_t)
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
%@[%@, %@]
applicationId
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
virtual int SparseBundleBackend::truncate(uint64_t)
nodes
bool ref::details::ctrl_blk<di_asif::details::table, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::table, tag_t = unsigned long long]
, but file size only 
void udif::details::UDIF_base::validate_runs()
read write
Couldn't open 
uint32_t FileDescriptor::fetch_physical_block_size() const
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocal
basic_string
offset
 while expecting 
KVS key value - parse failure.
ram
Not allowed more than one instance of 
' with flags 
unsigned long getCacheSize()
band_ptr sparse_bundles::band_ptr::replace_if_evictable(Band *)
Unmapped Entries
Sector Count
Invalid argument, please use one of the DICreateParams derived classes instead
public_key_crypto_algo
Request failed: %03ld %s
cache
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c
Diskimageuio: unsupported disk image type for get_backend
UDIF header changed while unlocked
Invalid field found in shadow file header: 
dispatch_source_create failed
key_derivation_prng_algorithm_t
io_result_t DiskImageSparseBundle::perform_io(ContextSparseBundle &, bool, const sg_entry &)
Legacy shadow file format is not supported by DiskImages2 framework
Replacement argument isn't a standard signed or unsigned integer type
Write zeros to unmap unaligned start region failed (err code
publicKey
auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:
Snapshot
-[DIIOCacheDelete setupNewConnection:]
Failed to stash files for persistent attach - ejecting
Base
wrap_key_crypto_algo
none = 0, crc28 = 1, crc32 = 2, dc42 = 3, md5 = 4, sha = 5, sha1 = 6, sha256 = 7, sha384 = 8, sha512 = 9, none_valid = 10
Final asif 
,Signature=
Failed to create DADisk during unmount
image-path
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
Band data doesn't exist, zeroing
attempting to authenticate with aea key
Cannot find IO object of class %@
Images
/
-[DiskImageParamsXPC allowOnDiskCacheWithSinkDiskImage:]
virtual FileDescriptorWrapper::~FileDescriptorWrapper()
virtual PurgeableFileBackend::~PurgeableFileBackend()
, truncating
Trimming: Written 
-[DIIOCacheDelete onPeriodicWithInfo:urgency:]
Corrupted encryption table, invalid offset/length in entry's descriptor
Cannot retrieve passphrase from user via TTY or GUI
invalid length
json
pkce
Failed to retrieve info
UDIF header doesn't contain a valid sector count, using runs upper value: 
v16@?0@\"NSError\"8
Range:
 size: 
Invalid pstack, Active stack contains a loop.
debug.didevice_cache_size_default
Daemon PID
%12u max requests in flight\n
-[DIBaseParams prepareImageWithXpcHandler:fileMode:error:]
Failed to get registry entry ID from dormant device
allowStoringInKeychain
IO error with sg: 
Diskimageuio: Unrecognized image format.
system error
Failed to update internal state after resize
device with class 
UDIF: Can't read UDIF trailer
://
precision
0x
-[DIConvertParams onConvertCompletionWithInError:outError:]
Crypto data block size: 
Max sector count is too large
IOBlockStorageDriver device not found in registry iteration
-[DIBaseXPCHandler installConnectionLostHandlers]_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:437:
virtual int DiskImageSparseBundle::flush(DiskImage::Context &, di_flush_mode)
Barrier failed after defrag table move, error 
 failed, error 
Image referenced in the pstack is unreachable.
Cannot edit crypto header that has more than 
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)
Not A Ninja/1.0
curl_easy_setopt failed\n
Background close of band at index 
Can't read encryption entry header, error 
Missing image path property
The argument index should end with a ':' or a '}'
di_plugin_image_t *verify_plugin_image(di_plugin_image_t *, CFErrorRef)
block_attributes
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
com.apple.diskimagesio_
Request timed out
Incorrect passphrase
Error with resolving knox url
deserializationError
Diskimageuio: images with constraints currently not supported
Failed adding matching notification
AAS3ContextCreate
ULFO
virtual io_result_t sparse_bundles::Band::write(DiskImage::Context &, const sg_entry &)
 trying to check permission after EACCES
Punch hole is not supported (err code 
int main(int, const char **)
com.apple.di_stackable.cache.flusher
static int SparseBundleBackend::open_bundle(const string &, int)
%@:%@
identityCertificates && [identityCertificates count] >= 1
-[AAS3DownloadRequest createAndResumeTask]
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Failed opening the image with RW access
Name
 io_size: 
ERROR: shipping key wrapped-key failed base64 decode
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
Encountered an irrecoverable I/O error, all future I/Os will be invalidated
IOService
high throughput
Error with decryption key size
knox
 is not supported
Total Bytes
debugLogsEnabled
ASIF: Can't defrag entries 
(unlocked)
ERROR: Response dictionary is missing required keys. Will fail
Cancelled
ddm
ActiveNode
identifier
dealloc_queue
\\u{
Yes
Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib 
 or exceeds size_t size 
com.apple.diskimagesiod
-[DIIODaemonDelegate reopenStashedFilesWithUserClient:outBackends:error:]
s3Perform failed (after retry), %s
system
shadow
Can't convert ASIF flag.
Found 
void boost::uuids::detail::sha1::process_byte(unsigned char)
Initialized bands array of size 
header_size_t
virtual int FileLocalAsync::flush(di_flush_mode)
unmanaged
bool DIIOManager::gatherFileMetadata(int, const char *, DIRespawnFileInfo *)
Registered plugin 
prng_key_bits_size_t
Can't take exclusive lock on entry
WARNING: this disk image contains a software license agreement that cannot be displayed as text. To read it, open the disk image in the Finder. Continuing accepts the license agreement without reading it.
(unrecognized error)
int sparse_bundles::Band::flush()
sparseimage format is not supported by DiskImages2 framework
Cannot find image with provided UUID.
int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)
CBC_IV8 = 5, XTS = 0x80000001
udro
 backend size 
BLX
-[DIShadowChain openWritable:createNonExisting:]_block_invoke
Failed to eject - cannot open device
zero-padding
Diskimageuio: locked backend 
Kernel returned error for complete command, command = 
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
%12u max attempts for a request\n
Invalid or missing image URL key
Image doesn't support resizing
RSA = 42
SLA prompt cancelled
virtual int DiskImageSparseBundle::set_size_impl(uint64_t)
bool ref::details::ctrl_blk<di_asif::details::map_element, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = di_asif::details::map_element, tag_t = unsigned long long]
UDZOMAX
v8@?0
strdup
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_unmap(const unmap_extent_t *, size_t, future_io_opts_t)
encKeys
Unable to convert data to vector.
DELETE
 length 
Zero padding cannot be disabled from this process (res=
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
!1
Error: failed to unwrap key. Error: %s\n
assetAttr
statInstanceID
A second controller XPC service attempted to create a new device
RO
Failed to set up image for info retreival
Couldn't read asif's header
KVS keyBuffer allocation failure.
crc32 {
/dev/%@
managed future err 
Missing key in KKMS response
RAW read-write image
 at index 
total_segments_t
void complete_function_uc(io_connect_t, const DIDeviceCommand &, unsigned int, int)
Disk image is terminated, skipping flush
Waiting for barrier to complete
remote mount
Invalid output format argument
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_write(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
ASIF meta header size exceeds its maximum
-[AAS3DownloadSession readToAsyncByteStream:size:atOffset:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ H
Re-enter new password: 
!\"
lw_future<batch_ctx_ns::batched_result<int>> DiskImage::Context::future_flush(di_flush_mode, future_io_opts_t)
 (error code 
com.apple.MobileAsset.AssetType
> %d %s\n
-[DIBaseAgentDelegate createListener]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406:
locally mounted from %@
 exceeds the maximum of 
diskimage_
main image
ZLIB = 0, LZFSE = 1, LZMA = 2, ZLIB_9 = 3, BZIP = 4
Band was evicted by another thread, retry erase process
Plugin's ring suspended, ret code 
Failed to find dormant device
Error during ASIF flush: 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:128:22)]
6.0
Format Description
CFAutoRelease<CFStringRef> udif::sla::extract_text_from_resource_array(CFArrayRef, std::optional<std::span<const UInt8>>, std::optional<int32_t>, CFStringEncoding)
End of input while parsing an argument index
Sparse bundle image
environment
int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)
Metadata contains unsupported field 
Failed to parse key in KVS (zero size data).
Invalid ASIF header size
entire_device
Bearer %@
Failed copying cache URL
Compression Info
virtual int Backend::read(const elements_t &)
snapshot
Failed locking the shadow file
Corrupted ASIF image.
1.0
 is clean, skipping flush
UDBZ
Is Cache
Resource name is too long to fit uint32_t
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c
AES-XTS
\\t
virtual int CompressedBackend::write(const sg_entry &)
Custom cache or shadow is not supported for pstack based images.
XPC connection interrupted
enc-request
Invalid public key: %s
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__expected/expected.h:
^{__CFDictionary=}20@?0i8^{__CFDictionary=}12
Size
Diskimageuio: Can't stack non asif formats. Got 
No WKMS key source available in AEA metadata
-[SparseBundleBackendXPC getCryptoHeaderBackend]
] 
DiskImages Framework
unique_lock::unlock: not locked
gcd_kqueue: kevent64 failed with ENOMEM
The URL encoded into the AEA authdata is missing or invalid.
US
curl_slist_append failed\n
/dev/disk
0123456789abcdef
Failed to read auth table
singleInstanceDaemon
Mandatory callbacks in the plugin's struct are missing
Size Info
ShadowURL
shadow-path
Failed to deserialize crypto format
Band was evicted by another thread (during retain attempt), retry erase process
 directly (without list)
 of type 
Backend is not mounted on APFS
virtual void ExecutionEngineCommand<CommandQueue, MachPort>::signal_terminate() [Container = CommandQueue, Port = MachPort]
Diskimageuio: backend is not a FileLocal
void DiskImage::do_terminate()
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
Crypto operation on data of 
AES_KEY = 0x80000001
, current is 
Content
int PluginsManager::register_plugin(const string &, di_plugin_t *)
Invalid size hex key %lu
void di_asif::details::table::set_entry_bitmap_range(ContextASIF &, data_entry_t &, const bits_range_t &, data_entry_t::flags, std::optional<data_entry_t::flags>)
crypto_format: Can't derive key 
invalid header: %s
Crypto couldn't read from inner backend @ 
9999
Dissented with status 0x%X, pid %d
hw.logicalcpu
Diskimageuio: Unsupported image format
token
Failed creating property list
virtual DiskImageSparseBundle::~DiskImageSparseBundle()_block_invoke
File too small.
Failed to add passphrase entry to auth table
Block size mismatch between crypto header and ASIF header
Can't flush asif on table close, backend barrier failed
Can't allocate mach port
Compressed Bytes
Failed opening folder for entries reading
diskimagesiod
Got error when trying to close 
malloc
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)
sig1_t
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)
-[FileLocalXPC replaceWithBackendXPC:]
iCloud
virtual int SparseBundleBackend::unlock_all()
value validator
Image contains crypto format but info class is missing EncryptionInfo
, res=
-[DIIODaemonDelegate setupExitDaemonWatchdog]_block_invoke
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
UUID
expected<uint64_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_nr_blocks() const
Diskimageuio: Nested stacking is not allowed.
Diskimageuio: path 
-[DIDeviceHandle dealloc]
Shadow backend %zu missing file descriptor
No backends provided for attach params creation
Replaced an empty slot
Unknown
BackendSG: truncating the inner backend failed, error = 
Failed to get Daemon PID
header_signature
plugin://%@/
ERROR: Failed to serialize request: %@ error: %@
 num_buffers: 
std::expected<CFAutoRelease<CFStringRef>, std::errc> udif::sla::extract_sla_text(const DiskImageUDIF &)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
Cannot decode file descriptor
void space_allocators::FixedSize::trim_largest(const size_changed_fn_t &)
user metadata
 failed wih error 
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
-[DICreateParams createDiskImageParamsWithError:]
Destination folder URL must be of 'file' scheme.
Can't read custom encryption entry header, error 
-[DIIOClientDelegate setupNewConnection:]_block_invoke
/sbin/mount
 option
Failed to write asif header, error 
special: 
regEntryID
addRequest
Failed to add symmetric key entry to auth table
In-place conversion maintains the encryption passphrase and method. It's not allowed to specify encryption arguments
%@%@.%@
 bits in the bitmap
io_result_t di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)
\n
Encryption Info
Failed to create XPC connection object
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = std::__bind<io_result_t (DiskImage::*)(DiskImage::Context &, const sg_entry &), DiskImage *, std::reference_wrapper<DiskImag
Cannot find registry entry ID 0x%llx
Failed to get parent registry entry, err code %d
'
IOServiceOpen failed
-[DIDiskArb onDiskDisappearedWithDisk:]
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/disk_im
void info::DiskImageInfoASIF::count_used_extents(const DiskImageASIF &)
-[DIDiskArb addDisappearedCallbackWithMountPoint:shadowMountPoints:delegate:]
Decryption key missing
com.apple.DiskImages2.ASIF.sparsity
udif::details::UDIF_base::UDIF_base(UDIF_header &&)
Can't convert data to property list
config_t
Cache
Failed to serialize symmetric key to crypto header
Master Checksum Info
bla
gcd::gcd_kqueue::gcd_kqueue(gcd_queue &, std::function<void (struct kevent64_s *, int)>)_block_invoke
oma-context
Barrier
Input underlying FS
uat
stable uuid
Couldn't convert CFStringRef to a proper std string
No pending SLA to confirm
 formatting argument
Unexpected backend replace request
std::vector<diskimage_uio::stack_image_node_ptr_t> create_stack_vector_from_single_fd(int, const std::filesystem::path &, bool)
SHA1_HMAC = 91, NONE = 0
bad flush type (
xpc error
void plugin_encode_fd(void *, const char *, int)
UDIF: Can't get types array from UDIF
Closing bands
Cannot attach RAM disk with a shadow or a cache file
set size failed
Sparse bundle ejected
-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]
source uuid
fsid
Authorization
lifs
 does not allow the 
 but buffer is full
Invalid UDIF format, contains intersected blocks
createTask
DaemonPID
Shadow block size is invalid (0)
Diskimageuio: Can't get image format
encryptionMethod
Error creating (unlocked) backend
Stackable image
fstatfs failed
suppressSsdFlags
Skipping erase of band 
: flush in destructor failed (
, err 
Unsupported value for crypto header field 
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
-[DIBaseParams openExistingImageWithFlags:error:]
uint64_t udif::details::UDIF_base::write_resources(CFDictionaryRef)
-[DICreateParams resizeWithDiskImage:blockCount:error:]
Failed barrier at start of dir flush, error
/dev/rdisk
Failed to erase mapped file of band 
diskimagesuio: future read invalid in read
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
 (band 0x
ASIF: table is not aligned to chunk size
index=
bool ref::details::ctrl_blk<CurrentReader, unsigned long long>::reset_val(tag_t, details::reset_val_option_set) [T = CurrentReader, tag_t = unsigned long long]
-[DIIODaemonDelegate onClientInvalidateWithConnection:]
 backend: 
, dest buffer_size 
wkms-uat.sd.apple.com
-[DIDiskArbEmulation ejectWithBSDName:error:]
virtual int BufferedWriteBackend::write(const sg_entry &)
CoreFoundation type mismatch: 
Failed to generate self signed certificate
0X
Internal backend read() failed. ret=
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = di_hybrid_subscriber_t]
Closed band at index 
DiskImageSparseBundle::ContextSparseBundle::ContextSparseBundle(DiskImageSparseBundle &)
 - 
-[DIIOCacheDelete setupSigtermHandler]_block_invoke
Failed to write SLA text to stdout
segment_num_none = 0, segment_num_one = 1
The symmteric key is wrong
r
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
flags_t
Invalid URL
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
, disk image is terminated
Background erase of 
openid,dsid,accountname
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
Failed to write metadata header
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
Couldn't upgrade lock entry 
Invalid value for UDIF header field: %s
-[FileLocalXPC sandboxExtensionTokenWithError:]
 status=
UDIF - max compressed run size: 
crypto_mode
CKIE
 crypto = 
\\r
ASIF: failed to deserialize metadata
Unable to create ioreg iterator
Failed to create DADisk during mount
inputURL
 was just created (truncated)
zlib
Persistent attach is not supported for this disk image type
get_next_capacity, allocator's max size reached
virtual int FileLocalAsync::_write(const sg_entry &)
image
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
Bad or missing key in SAKS response.
virtual DiskImageSparseBundle::~DiskImageSparseBundle()
Error opening ByteStream
> real: <
int di_asif::details::dir::handle_all_failures(ContextASIF &)
v16@?0Q8
a character
-[DIConvertParams copyUpdatedOutputURLWithError:]
di_plugin_image_t *PluginsManager::create_plugin_image(const di_plugin_t &, int, const CFDictionaryRef)
virtual int SparseBundleBackend::lock()
ASIF: can't read/allocate asif metadata
Trying to write @ 
-[DIIODaemonDelegate validateInstance]
The format string terminates at a '{'
IO handling of attached disk image
Cannot load libAmber
none
Missing payload URI in Knox response
-[DIEncryptionFrontend unlockWithPassphrase:error:]
set_euid_wrapper::~set_euid_wrapper()
auto DiskImageSparseBundle::void_stackable_identifier()::(anonymous class)::operator()() const
Can't register notification port
Failed to erase band 
Barrier failed after defrag, error 
Min Size Bytes
hw.memsize
Diskimageuio: bottom diskimage should have role image, but 
We're out of ctxs for async execute
virtual int DiskImageSparseBundle::unmap(DiskImage::Context &, const unmap_extent_t *, size_t)_block_invoke
trailer of a 
void sparse_bundles::mapped_blocks_t::map_range(uint64_t, uint64_t)
The disk image is corrupted
The requested URL is an existing non-sparsebundle folder
Sandbox extension token exceeds maximum size
bundle_handle
%s: 
Failed to replace passphrase entry in auth table
virtual size_t BZIPCompressedBackend::compress(const sg_entry &) const
Unexpected backend type for file
RW
Can't flush asif table, backend barrier failed
gcd_kqueue: kevent64 returned error 
V2 = 2
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Harde
, error 
-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]
-[DIResizeParams resizeWithError:]
Failed to open backend of crypto header
bitmap flag value invalid
 while expected is 
unexpected error
DiskImage::diskimage_extent_t DiskImage::const_extents_iterator_t::make_val() const
pthread_key_create
DiskImageConvert
Plugin version 
bool sparse_bundles::band_ptr::erase_if_unmapped(uint64_t)_block_invoke
Cannot find BSD name in IO media service
-[DIIOClientDelegate setupNewConnection:]
shadow file
Image info is not supported for the given image type
Flush failed - returning 
-[DIShadowChain topDiskImageNumBlocks]
Diskimages2 - ASIF - bad reserved bits 
Disk image is terminated, skipping ...
partition_num: 
set context
ID
a bool
 given
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692
 bytes is smaller than its trailer
Error reading file @ 
Failed during IO manager initialization
Cancelling mach ports...
Max Size Bytes
encryption_key_bits_size_t
int details::udif_verify::calculate_checksums(workqueue::workqueue &)_block_invoke
 changed before retain completed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
auto
flushing and closing 
Unexpected backend type for shadow file
header (
bool DIIOManager::requestGracefulShutdown()
bool DIIOManager::stashSingleFile(std::shared_ptr<Backend>, NSString *__strong, const char *, uint32_t)
1
Completed erase of band 
Attributes
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Flushing 
passphrase_header
^v8@?0
-[DIConvertParams prepareParamsForSquashWithError:]
Unmap error: 
PluginParams
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
 is not registered
+[BackendXPC newFileBackendWithURL:fileOpenFlags:error:]
Cannot find %@ entry
-[DIDiskMountTracker onDiskAppearedWithDiskName:isMountable:]
--oauth-grant-type
Could not parse OIDC token from AppleConnect output
Cannot find disk image with reg entry ID 0x%llx
crypto header contains invalid number of auth entries
AAS3DownloadStream (curl)\n
diParams
Diskimageuio: get block size failed 
This operation doesn't support pstack files
crypto_header
 dest 
void rawTestPlugin_t::subscriber_t::_cancel()
thread constructor failed
type: 
-[DIIODaemonDelegate unmountAll]
cmd
Attached disk image device info: BSD Name [%@], image URL [%@]
disk image kernel return
crypto_format: Can't decrypt wrapped key 
file_handle
int DiskImage::Context::unmap(const unmap_extent_t *, size_t)
-[DIDiskArbEmulation unmountWithMountPoint:error:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:425:
kern.aioprocmax
The specified image is a folder but not a sparsebundle
CFName
Is Encrypted
-[DIDiskArb unmountWithMountPoint:error:]
-C
Suspended
table flush failed during close: 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:113:22)]
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::set_path(const std::filesystem::path &, const diskimage_open_params::mode)
void di_hybrid_subscriber_t::suspend()
PluginName
Can't get send rights
BSDname
Could not generate OIDC token - AppleConnect Failure
xpcEndpoint
startIO called without a pending DiskImage
Image Format
Invalid path property (not a path or URL)
-[DIController2ClientDelegate attachCompletedWithHandle:reply:]
URL must have a file scheme
s3DownloadStreamOpen_curl
Failed to find keychain item using hashed key
Failed reading 
Couldn't write asif's header
user data retrieving failed
Num extents: 
 is now available
BackendNull
diskimage-bundle-type
-[DIIODaemonDelegate runIOmanager]
com.apple.DiskImages2
Type
expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_image_header(size_t)
 is incompatible with the framework, expected at least 
Can't write UDIF header
-[DIDiskMountTracker onDiskDescriptionChangedWithDiskName:isMounted:]
 updated from 
Updating 
Can't load table to get extents
useFormatMappingInfo
segment_num_t
Full dir write failed with 
void di_hybrid_subscriber_t::resume()
-[DIIOClientDelegate cancelSLAWithReason:reply:]
-[DIIODaemonDelegate wrapBackendWithEncryption:backendInfo:fileIndex:error:]
+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
Max Sector Count
virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)
-[DIIOClientDelegate confirmSLAAcceptedWithReply:]
Disk image is terminated, skipping future_flush
Looking for an evictable slot for 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633
bool sparse_bundles::mapped_blocks_t::load_file()
The argument index starts with an invalid character
+[DISLAFrontend(Private) redirectStdoutForDisplay]
 (band 
static autostart_task_t<process_entry_result_t> di_asif::details::table::write(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &)::process_write_entry::operator()(table &, ContextASIF &, table::data_entry_t &&, const sg_vec:
band 
encodedDict
Failed to read metadata 
Error writing file @ 
Runs
Size is not a multiple of block size
):
AppleDiskImageDevice
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
diskimage_uio::details::diskimage_impl::diskimage_impl(diskimage_open_params &&)
-I
int plugin_decode_fd(void *, const char *)
Can't flush asif on table flush, backend barrier failed
Raw header changed while unlocked
UDIF: Failed converting type array string (
-[DIIODaemonDelegate tryAttachWithParams:error:]
Failed to read passphrase from stdin
Failed to create resizer
 is not supported (err code 
mark purgeable failed on 
bzip2
trim largest: size change callback failed with 
diskimageuio: report err 
-[DIDiskArb waitForDAIdleWithError:]
Diskimageuio: ASIF header changed while unlocked
Unexpected response type: %@
 with ret 
ASIF: Block size isn't a multiple of 512
miss
disk image password
void SparseBundleBackend::write_primary_info_plist()
Couldn't open file with flags 
Cannot find image with provided tag.
wkms.sd.apple.com
ramTestPluginCreate
(locked)
-[DIIODaemonDelegate setupSigtermHandler]_block_invoke
-[DIStatFS logWithHeader:]
device size not found in registry
invalid file size for 
sandboxToken
Failed to reconstruct complete shadow chain during respawn
bool DIIOManager::sendFileToDriver(int, const char *, uint32_t, NSString *__strong, std::shared_ptr<Backend>, uint32_t)
Corrupted shadow file(s) chain
 opened and replaced at attempt 
readPassphraseFlags
File system is 
com.apple.wkms.url
The requested operation will delete all children of the provided node. use recursive removal to surpress this error.
CACHE_DELETE_AMOUNT
Cannot decode writable
get path failed
-[DIIODaemonDelegate validateConnection]
Invalid chunk size
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
: flush failed (
Root dir flush failed, error 
fstatfs failed with err code 
PKCS5_PBKDF2 = 103
Failed during data entry write in table write, error 
Invalid resource key
KEY_BITS_128 = 128, KEY_BITS_256 = 256
com.apple.mach_rcvd
Unmount already started, notifying controller to retry later
Failed to create crypto serializer
: [
Flushed 
Failed to add shadow nodes to chain
IO returned an error for command 
Unexpected passphrase header length (
Key is not 32 bytes size.
Dir Pointer Version
AEAHelper: Invalid file descriptor.
%s\n
Failed to open user client connection for file descriptor transport
The argument index value is too large for the number of arguments supplied
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
Key is not hexadecimal number.
BackendPlugin
Request failed: %03ld (error not set)
Resumed
backend
UDIF_header
Failed truncating 
 is closed, notifying waiters
 op_code: 
Unsupported disk image format
AmberDiskImagePluginCreate
Stack Info
Full Entries
Can't write table for defrag
-[DIIOCacheDelete registerPeriodicCallback]
%02x
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
, keeping file unlocked
Failed to create chiper data for public key auth
com.apple.diskimages.sla-prompt
Disk image is terminated, skipping flush of 
encryption
com.apple.diskimage-plugin.nbd
Failed to create graph from plist.
-[DIIODaemonDelegate tryReconnectToDormantDeviceWithInstanceID:error:]
Bands folder contains an out of range band (
tmp_convert
Not valid SAKS environment
Invalid plugin URL, plugin name is missing
Starting ASIF defrag, used size: 
Band 
Plugin bug: returned init failure without supplying the error
 (errno 
fstat failed
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ H
 bands flushed, calling 
Sector count is too large
Unsupported compressed run (
Zero padding disabled successfully on fd 
Unsupported key decryption algo
void DIIOManager::driverConnect(DIAttachParams *__strong, const DiskImage &)
Failed to evict band to make room for 
Couldn't exclusively lock entry 
PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_fo
Verify
Failed to mount filesystems
Disk image is terminated, skipping future_read
Validation failed for dictionary key %@.
Metadata
GUI SLA handling required
diskImageParams
Unexpected crypto header length (
, required decompression buffer size: 
Destroying File backend, but in-flight promises exist
ASIF
Disk image is terminated, skipping future_write
uuid
bool DIIOManager::checkForPendingSLA(io_connect_t)
s3HeaderAppend
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
}
sig2_t
std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)
curl_easy_init failed\n
(
Band size in sparse is zero
Cannot initialize pstack disk image without path.
AES = 0x80000001
Passphrases doesn't match
ASIF max_write size in header exceed the limit
 marked as purgeable
bytes, which is after end of ramdisk
Failed to create passphrase auth entry
-[DIBaseXPCHandler init]
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:152:22)]
encryption_mode
Couldn't lock entry 
unsigned char boost::algorithm::detail::hex_char_to_int(T) [T = char]
] = 
0
-[DIEncryptionChpass unlockWithPassphrase:error:]
-[DIIOCacheDelete eraseOldCacheFiles]_block_invoke
com.apple.diskimagesiod.spb
-[DIBaseXPCHandler completeCommandWithError:]
Data Fork
int di_asif::details::table::close()
FilePath
IOHDIXController
 read: 
NSURLSession read to stream nbyte=%zx offset=%llx\n
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603
Missing Expected AUTH DATA in AEA.
solid state
aaS3ContextClone
-[DIDiskArb waitForDAMountWithExpectedCount:diskTracker:]
Failed opening the shadow/cache file(s)
Failed creating sparsebundle folder
, 
com.apple.diskimagescontroller
BackendZero
Failed creating notification port
The fill option contains an invalid value
unmap
Diskimageuio: Only single cache is allowed
sparseHeader
Cannot stat 
Clone of plugin nodes is not supported.
Invalid header: %s
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ H
auth-data
key
virtual lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImageRaw::future_write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
Crypto couldn't write to inner backend @ 
BackendSG
s3StreamBaseInit
An argument index may not have a negative value
 / 
Read returned an error
Diskimageuio: Failed to create disk image: 
int di_asif::header::write_header(Backend &)
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
fileBackend
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const
/sbin/umount
+[DISLAFrontend(Private) displaySLAText:error:]
+[DIError errorWithDomain:code:description:verboseInfo:error:]
>
Parent UUID
encryption_key
Unsupported host for OIDC: %@
void rawTestPlugin_t::subscriber_t::_suspend()
Can't allocate ports array in driver
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
Close completed
Failed creating the image
User data contains reserved key(s)
none {
key_derivation_algorithm_t
Content-Length: %zd
Diskimageuio: Multiple images given but block size differ. 
Unexpected materialized_diskimage in create_diskimage_from_hdr
-[DIBaseServiceDelegate listener:shouldAcceptNewConnection:]
Registry entry ID mismatch between controller and daemon
keys/fetch
com.apple.internal.fetchrestorekeys
euqueueRequest timed out
device_command: 
can't get Diskimage attribute, unknown header format
is_aea: Error reading magic.
resource-fork
Failed to eject
Could not determine cache dir
 buffer_size = 
Terminating due to unrecoverable I/O error
X-Amz-Date: %s
virtual int FileLocalAsync::unlock_all()
^%@.*\\.%@$
void terminationCallback(void *, io_iterator_t)
int DiskImage::Context::flush(di_flush_mode)
%12.2f initial interval between retries (s)\n
Cannot change passphrase of unencrypted image
autoMount
virtual sparse_bundles::Band::~Band()
hybrid_queue
BuildVersion
 constant 
XPC connection invalidated
wrap_key_crypto_padding_algo
No room to add new auth entry
DIErrorVerboseInfo
Stack with cache as top image cannot be opened for writing.
typename boost::enable_if<boost::is_integral<typename hex_iterator_traits<OutputIterator>::value_type>, OutputIterator>::type boost::algorithm::detail::decode_one(InputIterator &, InputIterator, OutputIterator, EndPred) [InputIterator = std
The image was unlocked before setting userData
invalid bits range 
ASIF meta header is unaligned
Failed creating IO iterator, err code %d
:
flags
static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_handle_exceptions()
Failed to set up image for resize after creation
Can't write initial table data
 bytes image
 errno: 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
AES-CBC
-[DIDiskArb ejectWithBSDName:error:]
 block_size: 
Reading 
invalid value
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615
 header size 
Compression Type
Failed to store the passphrase in the keychain
ASIF: metadata header out of range
could not create iterator (begin)
+[DiskImageParamsXPC validateSupportedFormatWithBackendXPC:error:]
Physical block_size is 
Failed to read from certificate file 
Bit 
Backend barrier failed during allocator failures handling, error 
fetch_restore_keys self signed cert
vsnprintf
failed to open existing output file
pstack
Block size mismatch in DiskImageStackable
Mode for new files in bundle: 
Failed locking the image
ASIF meta header failed to read
IOMedia
not a valid DER-encoded X.509 certificate
version_1 = 1, version_2 = 2, version_3 = 3
Run interval: 
/s3/aws4_request\n
\\\"
Failed to serialize public key entry to crypto header
Requested write is out of range - offset 
corrupted image
-[DIIODaemonDelegate attachToNewDeviceWithParams:reply:]
v24@?0@\"NSFileHandle\"8@\"NSError\"16
 has size 
virtual int Ram::_read(const sg_entry &)
barrier
 bytes does not fit before the 
basename_r failed
-[DIIOCacheDelete setupExitTimer:]_block_invoke
s3StringBufferAppend
lw_future<batch_ctx_ns::batched_result<io_result_t>> DiskImage::Context::future_read(const sg_vec::iterator &, const sg_vec::iterator &, future_io_opts_t)
```
