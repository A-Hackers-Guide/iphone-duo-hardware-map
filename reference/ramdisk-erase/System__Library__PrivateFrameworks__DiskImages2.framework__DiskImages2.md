# `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 5,206,464 bytes.

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
%.*s: Ignoring, during shutdown
%.*s: Passphrase is correct
%.*s: Failed to open pager, writing directly to stdout
%.*s: %@
%.*s: Got error from last XPC command: %{public}@
%.*s: Not a sparseimage: %{public}s
%.*s: Failed creating queue
%.*s: Failed to copy %s (errno %d)
%.*s: <%lu> %{public}s
%.*s: Asking user permission to store the passphrase in the keychain
%.*s: Creating connection with %{public}@
%.*s: permissions for current path %s (uid %d): %c%c%c%c%c%c%c%c%c
%.*s: Convert in place failed, erasing %{private}@
%.*s: Failed to copy metadata of %s (errno %d)
%.*s: Background copy of %s to %s
%.*s: Decoding plugin instance
%.*s: Disk arbitration mount completed
%.*s: Failed to open top disk image node.
%.*s: Partition map updated
%.*s: File system resized
%.*s: Mount point %{private}@ disappeared
%.*s: Failed to generate device identity: %@
%.*s: Failed to connect to IO daemon for SLA handling
%.*s: Moving %{private}@ to %{private}@
%.*s: Appending to plugin node, skipping validation.
%.*s: Copying %s to %s, flags 0x%x
%.*s: Falling back to attach with di1
%.*s: Mount point %{private}@ disappeared (shadow's mount point)
%.*s: Keychain lookup returned %d
%.*s: Using %{private}@ as read-only
%.*s: Cannot open cache file %{private}@ with RW access, trying read-only
%.*s: Issuing new sandbox extension token for file %{private}@
%.*s: Using existing disk image params
%.*s: Reached an invalidation handler for the IO daemon connection
%.*s: Appeared Disk: %@
%.*s: Failed to create graph from plist: %@.
%.*s: Keeping RO mode for %{private}@
%.*s: Skipping %s
%.*s: IOServiceWaitQuiet timeout occurred, retrying.
[0x%08x](warning) %{public}s
%.*s: Looking for encrypted image passphrase in the %s keychain
%.*s: Unlocked using symmetric key
%.*s: Successfully retrieved WKMS shipping key
%.*s: Copied sandbox extension token from reopened backend (length=%zu)
%.*s: Creating connection to IO daemon clients listener
%.*s: IOServiceWaitQuiet done
%.*s: No matching item found in keychain
%.*s: Failed getting mounts list
%.*s: %{public}@ mounted successfully
%.*s: Failed to read passphrase from TTY
%.*s: Using an existing shadow file: %{private}@
%.*s: numBlocks queried for an empty shadowChain.
%.*s: Image %{private}@ re-opened with RW permissions
%.*s: APFS container and volume created
%.*s: DIDeviceHandle object is deallocating, invalidating connection
%.*s: %{private}@ unmounted successfully
%.*s: Successfully issued sandbox extension token for file %{private}s (token length: %zu bytes)
%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization
%.*s: I/O error at offset %lld iov_count %d errno %d
%.*s: MediaKit scan dict: %@
%.*s: Failed to dup stderr: %d
%.*s: Cache file %{private}@ opened with RW access
%.*s: Out of memory, failed to allocated %zu bytes for key %@
%.*s: File system is %{public}s
%.*s: Creation failed, erasing %{private}@
%.*s: Failed instantiating rawTestPlugin object: %s (code %d)
%.*s: Waiting for disk arbitration idle
%.*s: %{public}@ %{public}@
%.*s: %{public}s
%.*s: Erasing %{private}@
%.*s: Failed to find IOMedia entry for %@
%.*s: Creating %@
%.*s: Storing passphrase in the %s keychain
%.*s: Failed to open /dev/tty: %d, falling back to stderr
%.*s: Successfully retrieved WKMS non-shipping key
%.*s: Unmounting %{private}@
%.*s: Image file %{private}@ opened with flags %d
%.*s: Registry entry ID is 0, can't check %s property
%.*s: WARNING: Found %llu sectors with invalid flags (has_bitmap)
%.*s: Copying: %s -> %s
%.*s: Data partition resized
%.*s: Failed opening %{private}s, errno %d
%.*s: Registering DiskDisappearedCallback for %{private}@
%.*s: On disk cache path: %{public}@
%.*s: Missing parameters
%.*s: Not a pstack
%.*s: Input and output files are the same, using a temporary output file
%.*s: User data retrieving passed, %d value(s) found
%.*s: Failed to dup2 to stdout: %d
%.*s: Reached an interruption handler for the IO daemon connection
%.*s: A valid plist was given, but it has no pstack version key
%.*s: Not a UDIF: %{public}s, assuming RAW format
%.*s: Cannot open shadow chain %{private}@ with RW access: %{public}s, errno=%d
%.*s: Due to the conversion error, erasing the output file
%.*s: Mount Disk: %@
%.*s: Registering DiskDisappearedCallback for %{private}@ (shadow's mount point)
%.*s: Disk mount wait skipped (emulation mode)
%.*s: entry: %{public}@
%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported
%.*s: Copying: %s -> %s (%ld threads)
%.*s: Mounting %@ on %@
%.*s: Failed to delete %@: %@
%.*s: Failed to get UUID info of provided image.
%.*s: Keychain item requires ACL upgrade
%.*s: Failed creating semaphore
%.*s: Skipping invalid file type: %s
[0x%08x] %{public}s
%.*s: %@ ejected successfully
%.*s: Creating connection to %{public}@
%.*s: Stable UUID not found in provided image, Falling back to using Stackable UUID.
%.*s: entry with %{private}@
%.*s: Parent image is RAW, skipping shadow UUID validation on append.
%.*s: res_dict: %{public}@
%.*s: Creating %s plugin instance with params: %@
%.*s: Reached with diskURL=%{public}@
%.*s: Disk arbitration idle callback received
%.*s: Shadow file %{private}@ opened with RW access
%.*s: Failed to copy source disk image to temporary URL
%.*s: Failed during ASIF extents enumeration on offset: %llu
%.*s: Failed to dup stdout: %d
%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)
%.*s: Error checking %s property: %s
%.*s: Creating NSXPC listener on %{public}@
%.*s: Mountable Disk: %@
%.*s: Minimum data partition size is %lld blocks (estimation was %lld blocks)
%.*s: entry
%.*s: Disk image attached (with DI2) as %{public}@
%.*s: Received: %{public}@
%.*s: Failed to get block device for disk %@
%.*s: Validation exception: %{public}s
%.*s: Base image is raw format, using nil UUID.
%.*s: SLA detected, connecting to IO daemon for user acceptance
%.*s: Performing in-place squash optimization
%.*s: Block device class for %@: %@
%.*s: Allow parallel copy: Source=%d, Target=%d
%.*s: Skipping Class F protected file: %s
%.*s: Pager command failed with status %d, output may be incomplete
%.*s: Disk partitioning completed
%.*s: Error encoding user dictionary: %{public}@
%.*s: Passphrase found in keychain, unlocking the image
%.*s: %{public}s, errno=%d
%.*s: Mount error: %@
%.*s: Unlocked using public key
%.*s: Disk image resized to %llu bytes
%.*s: Failed to erase output URL
%.*s: MKMediaCreate failed with error %d (%d/%d)
%.*s: Failed initializing plugin: %{public}@
%.*s: Ejecting %@
%.*s: User data embedding passed
%.*s: On disk cache is not supported on embedded systems
%.*s: Received connection from pid %d with euid %d. Our euid is %d
%.*s: Failed to get info of newly created shadow/cache, will try to delete if an image was created.
%.*s: Cancelling copy (NSProgress cancel requested)
%.*s: XML_RSRC_FORK: %{public}@
%.*s: %{public}@ - %{public}@ %{public}@
%.*s: Failed to read pstack: %@.
%.*s: cancelSLA wait returned error: %{public}@
%.*s: Skipping content of folder %s
%.*s: BSD name: %{public}@
%.*s: Waiting for disk arbitration to finish mount
%.*s: %{public}@ error %{public}@
%.*s: Asking for passphrase using readpassphrase
%.*s: New disk image size is the same as previous
%.*s: XPC connection lost: %{public}@
%.*s: Shadow format validator exception: %{public}s
%.*s: Invalid key: %@
%.*s: %s
%.*s: Using an existing cache file %{private}@ with RO access
%.*s: isWritableFormat: %s
%.*s: Cancelling traverse (NSProgress cancel requested)
%.*s: Folder size: %llu
MKDIDevice
DIBaseParams
DIIOIterator
AppendPrivate
BlankDiskImageCreator
DIKeyRetriever
DIClient2Controller_XPCHandler
DiskImageParamsXPC
DiskImageParamsRAM_XPC
AEABackendXPC
PluginBackendXPC
DIImageInfoParams
DIDiskImageBridge
DIExtension
cpp_extension
DICreateRAWParams
DIHelpers
DIStackParams
DIOpenParams
_TtC16FetchRestoreKeys16CryptoKitWrapper
NSSecureCoding
DIEncryptionChpass
KNOXBackendXPC
NSXPCListenerDelegate
DITemporaryPassphrase
Append
DIResizeParams
DiskImageParamsRaw_XPC
ReadSynchronizerBackendXPC
InfoPrivate
DIBaseServiceDelegate
DIIOMedia
DIDataPartition
DI1
PluginDiskImageGraphNode
DIEncryptionUnlocker
RamXPC
DIAttachParams
workaround
DiskImageGraphNode
DIError
DIBaseXPCHandler
DiskImageParamsUDIF_XPC
DIIOClientProtocol
AAS3DownloadSession
DIDiskArbEmulation
DIEncryptionCreator
DIControllerProtocol
Info
DIBaseAgentDelegate
QuarantineFileHandler
DIAttachedDeviceInfo
DIEncryptionFrontend
DiskImageParamsSparseBundle_XPC
SparseBundleBackendXPC
DIClient2IODaemonXPCHandler
DICreateUDSBParams
DiskImageCreatorFromDevice
DIAPFSPartition
NSObject
DIChpassParams
DICommonAttach
DIShadowChain
DiskImageParamsLocked_XPC
BackendConvenience
DIConvertParams
DIDiskMountTracker
DiskImageGraph
Private
DIController2ClientDelegate
BackendXPC
CryptoBackendXPC
DIStatFS
DIIOObject
DIBaseAgentXPCHandler
DIShadowNode
DIController2ClientProtocol
FileLocalXPC
DICreateParams
BaseDiskImageCreator
DIDiskArb
DIUserDataParams
DIVerifyParams
DIParams
DIDeviceHandle
AAS3DownloadRequest
NativeDiskImageGraphNode
SerializedDiskImageGraph
NSCoding
PersistentBackend
DiskImageParamsPlugin_XPC
DiskImageParamsASIF_XPC
DIBlockDevice
DIURL
DISLAFrontend
DIStatsParams
DiskImages2
DICreateASIFParams
DIImageHandle
DiskImageCreatorFromFolder
FastFolderCopierWrapper
createListener
initWithURL:instanceId:error:
nilWithEnumValue:description:error:
TQ,N,V_readPassphraseFlags
copyNextObject
promptUserForSLAAcceptance:error:
_extraInfo
Tq,N,V_mountableDiskCount
addValue:forHTTPHeaderField:
isDeviceWithProperty:registryEntryID:predicate:
mountedFrom
startedOver
T@\"FileLocalXPC\",&,N,V_fileBackend
T@\"NSDictionary\",C,N,V_imageInfo
newUrl:
DI1URLWithData:error:
initWithFileDescriptor:
setTimeoutIntervalForRequest:
T@\"<DIDisappearedMountPointDelegate>\",W,N,V_delegate
T@\"DIStatFS\",&,N,V_inputStatFS
Tf,R,V_pauseInterval
_diskArb
inPlaceConversion
sandboxProfile
shadowChain
clearConnectionLostHandlers
T@\"NSString\",&,N,V_slaText
slaText
_imagesDictsArray
allowStoringInKeychain
keychainUnlockWithIsSystemKeychain:error:
setCreateParams:
setInvalidationHandler:
T@\"AAS3DownloadSession\",W,V_downloadSession
setDiskImageParamsXPC:
setInstanceID:
createGraphDictWithNode:
effectiveUserIdentifier
password
self
_pluginName
currentRunLoop
getAEAKeyWithHelper:keyBuffer:bufferSize:error:
initWithDIIOObject:
newDI2DevicesArrayWithError:
setBytesDownloaded:
stringWithUTF8String:
_imageInfo
setPassphrase:
tryResolvePstackChain:
buf
key
T@\"NSString\",C,N,V_certificate
TI,R,N,V_ioObj
arrayWithObject:
initWithUUIDBytes:
promptForAcceptance:
resizeWithDiskImage:blockCount:error:
TB,R,N,V_supportsBarrier
decodeBoolForKey:
ephemeralSessionConfiguration
getCertificateWithCertificatePath:error:
lastPathComponent
setIoMedia:
T@\"NSDictionary\",R,N,V_pluginParams
TB,N,V_suppressSsdFlags
appearedDiskCount
copyWithURL:outURLStr:maxLen:error:
isPrivileged
newFileBackendWithURL:fileOpenFlags:error:
setPassphrase:encryptionMethod:error:
setWithObjects:
_isCache
copyBlockDeviceWithError:
createInternalWithError:
initWithBytes:length:
retrieveInfoWithParams:error:
TB
_appearedDiskCount
createSinkDiskImage
setHandleRefCount:
setUseFormatMappingInfo:
_ioObj
applyMountPointsWithBSDName:error:
enumerateKeysAndObjectsUsingBlock:
newMountURLWithError:
setImageInfo:
createAndResumeTask
isKindOfClass:
setupNewConnection:
signalCommandCompletedWithXpcError:
suppressSsdFlags
T@\"NSMutableDictionary\",&,N,V_nodes
setCommandSize:
T@\"DIDiskMountTracker\",W,V_diskTracker
T@\"NSXPCConnection\",&,N,V_connection
_suppressSsdFlags
initWithFD:error:
inputMountedFrom
isDeviceSolidStateWithRegistryEntryID:
T@\"NSError\",&,N,V_operationError
setCachePolicy:
DI2_attachWithParams:BSDName:error:
_openParams
prepareImageWithXpcHandler:fileMode:encChpass:error:
setUUID:
validateWithDictionary:error:
T@\"NSString\",R,C
GUIPassphraseLabelUnlock
callbackReached
initWithOpenParams:lockableResources:
setArguments:
setOutputParams:
userDict
T@\"NSString\",C,N,V_volumeName
tag
addChild:withPendingUnitCount:
bytes
conformsToProtocol:
dupWithStderrHandle:reply:
formatImageWithCreateParams:error:
processIdentifier
_shadowMountedOnURLs
chpassWithError:
initWithBackendXPC:blockSize:
lockableResources
setPassphrase:encryptionMethod:
addPublicKeyEntryWithXpcHandler:error:
createShadowDiskImageWithBackend:numBlocks:sinkDiskImage:cache_only:stack_size:
newDIURLWithNSURL:
setClasses:forSelector:argumentIndex:ofReply:
setDaSession:
T@\"NSMutableData\",R,N,V_mutableSymmetricKey
_mountedDiskCount
appendOverlayWithURL:tag:error:
_fileMode
formatWithVolumeName:error:
initWithFileDescriptor:writable:locked:
isSparseFormat
singleInstanceDaemon
_streamBase
encodeBytes:length:forKey:
hasPrefix:
initWithDevice:error:
initWithURL:openMode:error:
keychainUnlockWithEncryptionUnlocker:reply:
resizeFileSystemToMinimumWithError:
resizeFileSystemWithNumBlocks:error:
initWithURL:openMode:
addToRefCountWithError:
encryptionUUID
init
removeRequest:
setHeader:
verifyWithParams:error:
T@\"DIURL\",R,N,V_URL
decryptKeyWithData:destKey:destKeySize:error:
enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:
getFileInfoWithError:
supportsBarrier
createDiskImageParamsWithError:
blockCount
fileMode
setAllowStoringInKeychain:
setNbyte:
streamBase
T@\"NSString\",R,C,N,V_instanceId
_parent
T{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}},R,N
UUIDString
_UIOOpenMode
initWithError:
localizedDescription
onConvertCompletionWithInError:outError:
T@\"NSObject<OS_dispatch_semaphore>\",R,V_requestsSem
WKMSShippingKeyWithURL:metadata:error:
_url
_useFormatMappingInfo
pluginHeader
reOpenIfWritableWithError:
verifyNodes:error:
Tq,N,V_mountedDiskCount
newDawTokenWithError:
outputFormat
replacePassWithXpcHandler:params:error:
closeConnection
cacheImage
createAndStoreInSystemKeychainWithCreator:account:error:
validateSquashFormats
_shouldValidate
initWithFormat:
createWithError:
prepareImageWithXpcHandler:fileMode:error:
setMountableDiskCount:
addShadowNodes:wrapReadOnly:error:
isWritableFormat
remoteProxy
setMetadata:
T@\"NSURL\",R,C,N,V_imageURL
anyObject
copyItemAtURL:toURL:error:
createNodesConnectivityWithNodesDict:error:
_graphDB
eraseIfExistingWithURL:error:
folderCopyXPCHandler
newAttachWithParams:error:
resizeDataPartitionWithError:
WKMSKeyWithAuthData:destKey:destKeySize:error:
getFileSystemMinimalBlocks:
newAttachWithCreateParams:error:
setSingleInstanceDaemon:
TAi,V_cancelled
Tq,N,V_fileMode
Tq,V_offset
_shadowChain
cancelSLAWithReason:reply:
inputStatFS
readToBuffer:size:atOffset:
validateAppendedImageWithURL:parentNode:isCache:error:
T@\"NSError\",C,N,V_deserializationError
_systemKeychainAccount
propertyListWithData:options:format:error:
setPassEntryToChange:
addBytesDownloaded:
copy
initWithDevName:
initWithExistingParams:error:
numberWithUnsignedLongLong:
setExportedInterface:
removeWithNode:recursive:error:
T@\"NSString\",R,C,N
T@\"NSString\",R,N
dateWithTimeIntervalSinceNow:
diskTracker
initWithURL:defaultFormat:error:
setEncryptionInfoOnly:
toDictionary
TI,R,V_maxRequests
initWithRegEntryID:autoMount:error:
newMountVolumeWithDiskArb:error:
setActiveNode:
unwrapEncryptionKeyWithWrappedKey:encapsulatedKey:privateKey:error:
T@\"NSURL\",R,C,N,V_URL
T@\"NSString\",&,N,V_tag
TB,N,V_useFormatMappingInfo
_URL
onDiskDescriptionChangedWithDiskName:isMounted:
passphrase
T@\"NSUUID\",C,N,V_parentUUID
TB,R,N
_GPTTypeID
askPermissionWithRememberPassword:error:
infoWithExtra:error:
isUnlocked
setExtraInfo:
unsignedIntegerValue
copyParentWithError:
initWithPluginName:params:
removeObjectForKey:
setEmulateExternalDisk:
_isPstack
_onDiskCache
addSymmetricKeyEntryWithError:
dataWithBytes:length:
isSparseBundleWithURL:
volumeBSDName
T@\"NSUUID\",R,C,N,V_encryptionUUID
appendWithURL:isCache:tag:numBlocks:setNewActive:error:
class
deleteImage
offset
setOffset:
setURL:
_mutableChildren
dupStderrWithError:
isQuarantined
keychainUnlockWithError:
listener
maxAttempts
T@\"DIBaseParams\",&,N,V_outputParams
ejectWithError:
activeInfoWithExtra:error:
nilWithUnexpected:verboseInfo:error:
TB,N,V_allowStoringInKeychain
addObject:
characterAtIndex:
setSemaphore:
updateSystemKeychainAttrWithDict:isStoring:error:
_delegate
_outputParams
_pstackURL
_sparseBundleBandSize
consoleAskForPassphraseWithUseStdin:usage:error:
initWithCapacity:
createWithXpcHandler:error:
isPlugin
newDIURLWithPluginName:params:
_uniqueDevice
componentsJoinedByString:
getImageInfoDictWithURL:error:
remoteObjectInterface
whitespaceAndNewlineCharacterSet
T@\"DIURL\",C,N,V_URL
T@\"NSURL\",R,N,V_fileUrl
initWithSize:
shadowURLs
tryCreatingCryptoHeader
port
_maxAttempts
_pluginParams
hasUnlockedBackend
waitForQuietWithService:error:
T@\"NSLock\",R,V_cacheLock
copyEntitiesList
description
displaySLAText:error:
hintFormat:
predicateWithBlock:
publicKey
forwardLogs
lockBackendsWithError:
metadata
relativePath
stringWithFormat:
initWithInputURL:outputURL:shadowURLs:error:
T*,V_buf
copyDiskImagesControllerWithError:
extraInfo
firstObject
mountedDiskCount
onDiskAppearedWithDiskName:isMountable:
setCopier:
T@\"NSString\",C,N,V_devBSDName
_volumeBSDName
addToRefCountWithReply:
failWithNoPstackError:
nbyte
setShouldValidate:
setSystemKeychainAccount:
xpcListenerEndpoint
_readPassphraseFlags
checkResourceIsReachableAndReturnError:
convertWithParams:reply:
createConnection
setBlockSize:error:
T@\"NSMutableArray\",R,N,V_nodes
_dataPartition
_persistentAttach
flags
mountableDiskCount
setAutoMount:
setBackendXPC:
setHTTPMethod:
T@\"DIShadowChain\",&,N,V_shadowChain
mountedOnURL
nilWithEnumValue:verboseInfo:error:
resizeToSize:error:
setObject:forKey:
T@\"NSMutableSet\",R,V_requests
cache
setMaxRawUDIFRunSize:
fillDI2InfoWithDevice:error:
getImageWithUUID:error:
materializeDiskImage
nilWithPOSIXCode:verboseInfo:error:
setInputStatFS:
addShadowURLs:error:
failWithUnexpected:error:
openEncryption
T@\"NSString\",?,R,C
_mountedOnURL
encodeInteger:forKey:
initWithURL:numBlocks:error:
passEntryToChange
pipe
unsignedLongLongValue
validateAndPopObjectForKey:className:isOptional:error:
T@\"NSString\",C,N,V_volumeBSDName
attributesOfItemAtPath:error:
containsValueForKey:
overrideBlockSize
removeAllObjects
setCacheImage:
T@\"DIBaseParams\",R,N,V_diParams
T@\"NSObject<OS_dispatch_semaphore>\",W,V_sem
_client2IOhandler
_requestsSem
fileURLWithPath:isDirectory:
getCryptoHeaderBackend
encodeWithCoder:
fileExistsAtPath:isDirectory:
keychainUnlockWithEncryptionUnlocker:error:
T@\"NSString\",R,C,N,V_mountedFrom
diskArbWithError:
diskImageAttach:BSDName:error:
initWithRegEntryID:
isCancelled
pauseInterval
requestSynchronousDataWithRequest:session:error:
T@\"NSDictionary\",&,N,V_metadata
_size
copyDescriptionWithBSDName:
initWithBytesNoCopy:length:freeWhenDone:
nonCacheNodes
pstackURL
_stream
getImageInfoWithExtra:error:
imagesDictsArray
initWithBackend:error:
operationError
substringFromIndex:
TB,V_autoMount
_cache
completeCommandWithError:
removeNodeWithTag:recursive:error:
setRemainingAttempts:
dealloc
T#,R
initWithGraphDB:error:
initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:
path
setFolderCopyXPCHandler:
urlSession
TB,V_encryptionInfoOnly
onErrorCleanup
setBackend:
setCancellationHandler:
setShouldValidateShadows:
T@\"NSProgress\",&,N,V_progress
dataWithContentsOfFile:
hasGUIaccess
toDI1ParamsWithError:
GraphNodeWithDictionary:workDir:error:
_overrideBlockSize
resizeDataPartitionWithPartitionUUID:partitionNumBlocks:error:
pid
setDiskTracker:
setTag:
T^{__MKMedia=},R,N,V_mediaRef
T{shared_ptr<unsigned char>=*^{__shared_weak_count}},R,N,V_key
client2IOhandler
customCacheURL
getChildren
TQ,R,N
_UUID
createAndStoreInSystemKeychainWithAccount:error:
setConnection:
setHTTPAdditionalHeaders:
setMutableChildren:
shouldValidate
T@\"NSMutableArray\",&,N,V_mutableChildren
T@\"DiskImageGraphNode\",&,N,V_activeNode
_fileBackend
_xpcError
initWithBase64EncodedString:options:
initWithEndpoint:
removeObject:
setDelegate:
JSONObjectWithData:options:error:
_parentUUID
initWithURL:tag:UUID:parentNode:metadata:isCache:
resizeWithParams:error:
setGraphDB:
TQ,N
fileBackend
performSelector:withObject:withObject:
requestsSem
systemKeychainAccount
validateBlockSizeSupport
TQ,N,V_sparseBundleBandSize
T^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v},V_stream
initWithURL:shadowURLs:error:
removeObjectAtIndex:
setShadowMountedOnURLs:
T@\"NSMutableArray\",&,N,V_imagesDictsArray
trackIfMyDisk:
T@\"NSURL\",R,C,N,V_shadowURL
_handleRefCount
TQ,R
_cacheBackendXPC
boolValue
decodeObjectOfClass:forKey:
initWithMachServiceName:
objectAtIndexedSubscript:
GUIPassphrasePromptCreate
_fileUrl
_passphrase
executeWithPath:arguments:error:
integerValue
numberWithInteger:
runMode:beforeDate:
setParentUUID:
_encryptionUUID
TQ,V_nbyte
addDecendantsToArray:
appendWithURL:isCache:tag:numBlocks:toNode:setNewActive:error:
encryptionMethod
initWithListenerEndpoint:
registerDiskTrackingCallbacksWithDiskTracker:
setPersistentAttach:
.cxx_destruct
GPTTypeID
numBlocksWithSizeStr:blockSize:
setRemoteProxy:
URLByDeletingLastPathComponent
_activeNode
_maxRequests
_xpcListenerEndpoint
T@\"NSMutableURLRequest\",&,V_urlRequest
T^v,R,N
lookupLegacyKeychainWithXpcHandler:error:
mediaContentUUID
pluginName
restoreStdout:
setImagesDictsArray:
setMyDisks:
setOnDiskCache:
isCache
Tq,R,N
_urlSession
getCFRunLoop
setValue:forKey:
xpcEndpoint
backend
T@\"NSString\",R,C,N,V_ramSizeStr
KKMSKeyWithURL:destKey:destKeySize:error:
T@\"NSString\",C,N,V_publicKey
_passEntryToChange
decodeObjectOfClasses:forKey:
outputParams
setSymmetricKey:
initWithPassphrase:
temporaryPassphrase
traverseSrcFolderWithProgress:error:
T@\"NSString\",R,N,V_pluginName
initWithMachServiceName:options:
T@\"NSData\",C,N
_cacheLock
defaultDiskImageAttach:BSDName:error:
failWithOSStatus:description:error:
length
setPassphrase:error:
T@\"NSNumber\",R,N,V_overrideBlockSize
_shadowURLs
_userDict
setUrlRequest:
createImageWithNumBlocks:error:
TB,N,V_cacheImage
TQ,N,V_regEntryID
appendOverlayWithURL:tag:numBlocks:error:
initWithBackendXPC:
ioMediaUUID
stream
TB,R
_cacheURL
_diskImageParamsXPC
folderSize
partitionDiskWithError:
reason
setStatus:
setupDefaults
TB,R,N,V_isPstack
_startedOver
invalidateAndCancel
readDataToEndOfFileAndReturnError:
setDataPartition:
statInstanceID
T@\"DIDataPartition\",&,N,V_dataPartition
TB,N,V_handleRefCount
encodeBool:forKey:
initWithFileDescriptor:closeOnDealloc:
newEntityDictWithIOMedia:mountPoints:
size
downloadSession
arrayWithObjects:count:
defaultCStringEncoding
initWithData:encoding:
setMountedDiskCount:
TQ,R,N,V_regEntryID
Tq,N,V_appearedDiskCount
copyRootBlockDeviceWithError:
respondsToSelector:
scheme
wrappedDataDictionaryWithCertWithPlainText:certificate:error:
T@\"NSNumber\",R,N,V_pid
_header
TQ,R,N,V_GPTTypeID
inputMountedOnURL
numFiles
setInterruptionHandler:
stringByAppendingString:
attachWithParams:handle:error:
initWithBSDName:numBlocks:blockSize:error:
objectAtIndex:
sandboxToken
shadowURL
Tq,N,V_outputFormat
URLByAppendingPathComponent:isDirectory:
_numBlocks
fileHandleForReading
nilWithDIException:prefix:error:
objectForKeyedSubscript:
encodeObject:forKey:
mutableSymmetricKey
remainingAttempts
setInputURL:
shadowStats
unlock
initWithBaseImageURL:tag:error:
T@\"NSString\",C,N,V_ioMediaUUID
T@\"DIClient2Controller_XPCHandler\",&,N,V_folderCopyXPCHandler
T^{?=Q*^{AAS3Context_impl}},R,V_streamBase
_mediaContentUUID
_mediaSize
recursiveInfoWithExtra:error:
shouldValidateShadows
_backend
_deviceHandle
setHTTPBody:
unlockWithXpcHandler:error:
validateObjWithKey:className:isOptional:error:
setSem:
bundleWithURL:
componentsWithURL:resolvingAgainstBaseURL:
convertWithParams:error:
getSerializerWithAuthTable:
initWithDevName:error:
setParent:
archivedDataWithRootObject:requiringSecureCoding:error:
regEntryID
CLIPassphrasePromptUnlock
readToAsyncByteStream:size:atOffset:
setIsCache:
substringToIndex:
isDiskImageWithURL:
processInfo
resizeWithError:
rootNode
unlockWithPassphrase:error:
setXpcEndpoint:
instanceID
prepareConvertWithError:
setPstackDict:
setSparseBundleBandSize:
volumeName
initWithString:
setForwardLogs:
_outputURL
array
countIOMediaObjectsWithError:
createImageWithSrcFolder:completionBlock:
initWithURL:key:
cacheLock
fillDI1InfoWithDevice:error:
requestsLock
_customCacheURL
myDisks
issueRespawnTokensWithError:
newOIDCSessionForHost:error:
validateSupportedFormatWithBackendXPC:error:
T@\"NSUUID\",&,N,V_UUID
_dispatchQueue
_urlRequest
lockWritableBackendsWithError:
mutableCopy
TQ,N,V_encryptionMethod
dispatchQueue
initWithDictionary:copyItems:
statsWithError:
T@\"NSArray\",&,N,V_handles
_mountedFrom
TB,N,V_startedOver
errorWithDomain:code:userInfo:
remoteObjectProxyWithErrorHandler:
validateFileWithURL:error:
_listener
T@\"DIURL\",C,N,V_inputURL
_volumeName
longLongValue
setCache:
stackableUUID
terminationStatus
TB,V_extraInfo
copyUpdatedOutputURLWithError:
dataTaskWithRequest:completionHandler:
listener:shouldAcceptNewConnection:
setAppearedDiskCount:
GUIPassphraseLabelCreate
T@\"DIShadowChain\",R,N,V_shadowChain
Tf,V_pauseInterval
mountedOnAPFS
xpcError
T@\"NSURL\",C,N,V_cacheURL
createBlankWithParams:error:
TB,N,V_singleInstanceDaemon
_myDisks
getFirstNonCacheAncestorWithNode:error:
isWritableFileAtPath:
semaphore
userInfo
T@\"DIClient2IODaemonXPCHandler\",&,N,V_client2IOhandler
errorWithPOSIXCode:verboseInfo:
T{shared_ptr<BaseFolderCopier>=^{BaseFolderCopier}^{__shared_weak_count}},N,V_copier
errorWithDomain:code:description:verboseInfo:error:
installConnectionLostHandlers
processName
errorWithEnumValue:verboseInfo:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_dispatchQueue
setFileMode:
supportsPersistentAttach
URLByStandardizingPath
boolValueForEntitlement:
loadPlistDictFromFileHandle:dict:error:
null
GUIAskForPassphraseWithEncryptionFrontend:usage:error:
sandboxExtensionTokenWithError:
url
failWithInError:outError:
ioClassName
mainImageSandboxToken
setDeserializationError:
startXPClistener
_statInstanceID
T@\"NSString\",R,C,N,V_mediaContentUUID
decodeBytesForKey:returnedLength:
initWithURL:isCache:
lastObject
pstackDict
urlRequest
useFormatMappingInfo
T@\"NSArray\",R,N
setCompletedUnitCount:
_conversionMethod
devBSDName
interfaceWithProtocol:
savePstackWithURL:error:
createImageWithSrcDevice:error:
_sem
cancelled
getImageWithTag:error:
setUserDict:
sem
changePasswordWithParams:error:
T@\"NSURL\",R,N,V_pstackURL
URLWithString:
_imageFormat
checkWithHasIcloudKeychain:error:
initForInplaceWithURL:error:
_cryptoHeader
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
progressWithTotalUnitCount:
appendWithURL:isCache:numBlocks:error:
certificate
initWithBaseImageURL:pstackURL:tag:error:
TB,V_callbackReached
_fileSystem
_ioMediaUUID
newACEndpointWithEnvironment:error:
newWithUnlockedBackendXPC:error:
setInputMountedOnURL:
T@\"NSString\",C,V_BSDName
retrieveStatsWithParams:reply:
setActiveNodeWithUUID:error:
T@\"NSArray\",C,N,V_shadowMountedOnURLs
initWithRegEntryID:xpcEndpoint:
findPartitionWithDeviceBSDName:error:
initWithDiskImage:lockableResources:
isPstack
setNumBlocks:
isEmpty
_certificate
mediaSize
setCacheBackendXPC:
S3KnoxResolveURL:key:keySize:error:
T@\"DITemporaryPassphrase\",R,N,V_temporaryPassphrase
failWithDIException:prefix:error:
registryEntryIDWithError:
setValue:forHTTPHeaderField:
_status
arrayWithCapacity:
dictionaryWithObjectsAndKeys:
T@\"NSUUID\",R,N,V_parentUUID
autoMount
createBackendWithFlags:
initWithURL:fileOpenFlags:
isEncryptedImageWithURL:error:
sessionWithConfiguration:
setDebugLogsEnabled:
T@\"DIURL\",C,N,V_outputURL
unregisterDiskTrackingCallbacks
T@\"NSURL\",R,N,V_filePath
TB,N,V_passphrase
_handles
_requests
initWithFileDescriptor:error:
lockBackendsWithWritableOnly:error:
Ti,V_status
_instanceID
_ramSizeStr
attachWithParams:reply:
checkExistingFileWithURL:isDirectory:error:
checkStackValidityWithError:
failWithPOSIXCode:verboseInfo:error:
newAttachWithError:
URLRelativeToPstackParentWithURL:
addDisappearedCallbackWithMountPoint:shadowMountPoints:delegate:
initWithIOObject:retain:
newIteratorWithOptions:error:
numBlocks
outputURL
setWithObject:
newOIDCTokenForHost:error:
serviceName
T@\"NSNumber\",R,N,V_blockSize
Ti,R,N
_remoteProxy
allObjects
initWithURL:
newDevicesArrayWithError:
pathExtension
requiresRootDaemon
mutableChildren
T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_semaphore
TQ,N,V_commandSize
cancelSLAWithReason:
connectWithError:
initWithURL:size:error:
postRequestWithURL:session:data:error:
reverseObjectEnumerator
T@\"NSURL\",R,C,N,V_cacheURL
cacheBackendXPC
diskImageDevice
T@\"NSNumber\",R,N,V_mediaSize
debugDescription
filteredArrayUsingPredicate:
stop
toDIShadowNode
TB,R,N,V_isCache
TQ,N,V_blockSize
compactAndEjectWithCreateParams:error:
filePath
waitUntilExit
UUID
fileExistsAtPath:
getCertificateWithPublicKey:error:
initWithIteratorNext:
setDI2PIDWithDevice:error:
setFilePath:
updatePartitionMapWithError:
handles
connection
initWithBSDName:error:
mountPoints
statWithError:
uniqueDevice
_operationError
TB,N,V_isPrivileged
_xpcEndpoint
convertPrivateKeyTox963WithPemPrivateKey:error:
convertWithCompletionBlock:
createImageWithSrcFolder:progress:createParams:convertParams:error:
initForInplaceWithExistingParams:error:
setFileSystem:
checkAuthEntriesWithHasPassphraseEntry:hasPublicKeyEntry:error:
T@\"NSMutableDictionary\",&,N,V_graphDB
TQ,N,V_numBlocks
TQ,R,N,V_blockSize
addRequest:
copyIOMediaWithError:
createDiskImageParamsXPC
initWithURL:fileOpenFlags:bandSize:
arrayWithArray:
initWithBackend:key:
ioObj
parentUUID
saveToPlistWithDictionary:URL:error:
setDevBSDName:
setHTTPMaximumConnectionsPerHost:
stringWithImageFormat:
_cacheImage
_commandSize
_pauseInterval
nilWithUnexpected:error:
setDownloadSession:
setProgress:
setSizeWithDiskImage:newSize:
updateNumBlocksWithFolderSize:numFiles:
containsObject:
_mutableSymmetricKey
_pid
initWithBackendXPC:header:
keysOfEntriesPassingTest:
setNodes:
validateAppendedImageWithInfo:error:
stringByAppendingPathComponent:
_regEntryID
nilWithOSStatus:verboseInfo:error:
_requestsLock
inputURL
resizeWithNumBlocks:error:
fileUrl
requestWithURL:
fileSystemRepresentation
getDescendants
launchedTaskWithExecutableURL:arguments:error:terminationHandler:
unlockImageWithOpenParams:
T@\"NSUUID\",R,C,N,V_statInstanceID
partitionDiskWithGPTTypeID:error:
setPublicKey:
T@\"NSString\",C,N,V_systemKeychainAccount
initWithDomain:code:userInfo:
jsonResponseWithRequest:session:error:
performSelector:
replaceWithBackendXPC:
requests
T@\"NSURL\",R,N
createRamBackend
T@\"DiskImageGraphNode\",&,N
handleRefCount
hasBaseImageCache
hash
initWithGraphDB:workDir:error:
newWithBackendXPC:error:
sendSynchronousRequest:returningResponse:error:
setHandles:
isProxy
TQ,N,V_fileSystem
_allowStoringInKeychain
ejectWithBSDName:error:
isEqualToString:
progress
unlockUsingSymmetricKeyWithError:
T{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}},N,V_backend
_callbackReached
_instanceId
_frameworkNum
absoluteURL
moveItemAtURL:toURL:error:
validateConnection
T@\"NSUUID\",R,N
T^{__DASession=},N,V_daSession
_filePath
_pstackDict
appendWithURL:tag:error:
createParams
deviceHandle
diParams
GUIAskForPassphraseWithEncryptionFrontend:usage:reply:
baseBackendXPC
fileDescriptor
generateAuthTableWithError:
nilWithPOSIXCode:description:error:
openExistingImageWithError:
waitForDAIdleWithError:
copyUnmatchedDiskImageWithRegEntryID:error:
nodes
_encryptionMethod
copier
copyWithDstFolder:progress:error:
decimalDigitCharacterSet
openMode
valueForEntitlement:
copyPropertyWithClass:key:
failWithUnexpected:verboseInfo:error:
newWithCryptoFormat:error:
Ti,R,N,V_UIOOpenMode
_imageURL
_inputStatFS
getRequestWithURL:error:
removeItemAtURL:error:
setVolumeName:
setXpcError:
URLByAppendingPathComponent:
dataWithPropertyList:format:options:error:
setConnectionMode
setPassword:
replacePassphrase:error:
_sandboxToken
delegate
initWithObjectsAndKeys:
relativeString
setExportedObject:
onDiskCache
onDiskDisappearedWithDisk:
persistentAttach
_bytesDownloaded
_nbyte
appendCacheWithURL:tag:error:
convertWithParams:completionBlock:
encodeInt64:forKey:
initWithURL:error:
readPassphraseFlags
T@\"NSMutableSet\",&,N,V_myDisks
setImageFormat:
copyDevicePathWithStatfs:
initWithPluginName:pluginParams:tag:UUID:parentNode:metadata:isCache:
replaceDiskImageWithUnlockedBackendXPC:error:
DI1_attachWithDictionary:BSDName:error:
initWithBackend:
insertObject:atIndex:
isMemberOfClass:
maxRawUDIFRunSize
setTemporaryPassphrase:
waitForDAMountWithExpectedCount:diskTracker:
activeShadowURL
T@\"NSUUID\",R,C,N
auth_table
logWithHeader:
T@\"NSBundle\",R
TB,N,V_emulateExternalDisk
UTF8String
_folderCopyXPCHandler
baseNode
findPartitionSchemeWithIOMedia:error:
frameworkNum
getRelativeIfContainedWithChildURL:parentURL:
initWithDictionary:workDir:error:
T@\"DiskImageGraphNode\",R,N
setCertificate:
_lockableResources
numberWithUnsignedInteger:
verifyWithError:
_connection
copyAllMountPoints
encryptionInfoOnly
initWithTag:UUID:parentNode:metadata:isCache:
TQ,V_size
_outputFormat
createEmptyImageWithError:
emulateExternalDisk
BSDName
T@\"BackendXPC\",R,N,V_baseBackendXPC
_inputMountedFrom
_isPrivileged
retrieveUserDataWithParams:error:
setTimeoutIntervalForResource:
setVolumeBSDName:
status
TQ,N,V_conversionMethod
activeNode
setDeviceHandle:
supportsSecureCoding
syncRequests
unlockUsingPublicKeyWithError:
TQ,N,V_maxRawUDIFRunSize
dataUsingEncoding:
dataWithJSONObject:options:error:
zone
T@\"NSDictionary\",&,N,V_userDict
bytesDownloaded
T@\"NSError\",&,N,V_xpcError
newEnvWithDictionary:error:
removeLastObject
lowercaseString
Tq,N,V_imageFormat
_diskTracker
copyDefaultLocalizedStringForDIErrorCode:
imageFormat
setBSDName:
sleepForTimeInterval:
set
errorWithDIException:prefix:error:
setBlockSize:
setSuppressSsdFlags:
T@,&,N,V_remoteProxy
appendWithURL:isCache:error:
errorWithUnexpected:verboseInfo:error:
managedAttachWithParams:handle:error:
savePstackWithError:
stringWithCString:encoding:
updateBSDNameWithBlockDevice:error:
_offset
_shadowURL
componentsSeparatedByString:
failWithEnumValue:description:error:
initFileURLWithPath:
initWithIOIterator:retain:
isEqual:
mediumType
initWithParams:
T@\"NSArray\",R,N,V_shadowStats
decodeIntegerForKey:
enterSandbox
imageURLFromDevice:error:
isDeviceHighThroughputWithRegistryEntryID:
prepareParamsWithError:
changePassWithXpcHandler:error:
T@\"NSArray\",R,N,V_shadowURLs
T^v,N,V_passEntryToChange
_downloadSession
shadowMountedOnURLs
waitForDeviceWithError:
initWithExistingParams:size:error:
ramSizeStr
setCacheURL:
validateDeserializationWithError:
GUIPassphrasePromptUnlock
_nodes
_temporaryPassphrase
domain
getOIDCClientIDForHost:error:
performSelector:withObject:
setXpcListenerEndpoint:
sharedSession
unlockUsingSaksWithError:
T@\"NSXPCListener\",&,N,V_listener
TB,R,N,V_autoMount
TQ,D,N
_encryptionInfoOnly
cacheDocument:
failWithPOSIXCode:description:error:
writeHexKeyToBuffer:hexKey:error:
code
dictionaryWithDictionary:
invalidate
stringByTrimmingCharactersInSet:
infoDictionary
instanceId
isFileURL
graphDB
openWritable:createNonExisting:
characterIsMember:
initWithClassName:error:
initWithInputURL:outputURL:error:
ioObjectWithClassName:iterateParent:error:
_semaphore
setListener:
T@\"NSMutableDictionary\",&,N,V_pstackDict
TAQ,V_bytesDownloaded
openExistingImageWithFlags:error:
_createParams
_emulateExternalDisk
_mountableDiskCount
_supportsBarrier
setCallbackReached:
embedWithError:
createDiskImageWithCache:shadowValidation:
imageURL
launchAndReturnError:
setUniqueDevice:
T@\"DiskImageParamsXPC\",&,N,V_diskImageParamsXPC
_BSDName
createAndStoreInSystemKeychainWithCreator:account:reply:
initWithUTF8String:
mediaRef
setOutputFormat:
writeToURL:options:error:
T@\"NSUUID\",C,N,V_instanceID
children
createEncryptionWithXPCHandler:error:
getBlockSizeFromStr:error:
newSessionWithError:
retain
TB,N,V_uniqueDevice
addShadowNodes:error:
getImageUUIDWithURL:allowMissingUUID:error:
_baseBackendXPC
URL
serviceListener
TB,N,V_persistentAttach
childrenInfoWithExtra:error:
setStandardOutput:
TB,N,V_shouldValidate
_deserializationError
attachCompletedWithHandle:reply:
diskImageParamsXPC
localizedStringForStatusCode:
newMKDIDeviceWithError:
setClient2IOhandler:
superclass
T@\"DIIOMedia\",&,N,V_ioMedia
getUUIDBytes:
hasDirectoryPath
initWithPluginName:pluginParams:pstackURL:tag:error:
setPauseInterval:
setStartedOver:
GUIVerifyPassphraseLabelCreate
_devBSDName
_maxRawUDIFRunSize
absoluteString
prepareParamsForSquashWithError:
shouldPerformInplaceSquash
T@\"NSString\",R,N,V_sandboxToken
T@\"NSLock\",R,V_requestsLock
_publicKey
_singleInstanceDaemon
count
embedUserDataWithParams:error:
GUIAskForPassphraseWithPassphraseUsage:error:
_shadowStats
allowOnDiskCacheWithSinkDiskImage:
decodeInt64ForKey:
initWithBaseImageURL:newPstackURL:tag:error:
newlineCharacterSet
redirectStdoutForDisplay
_blockSize
T@\"NSURL\",C,N,V_inputMountedOnURL
dataPartition
resume
shadowSandboxTokens
T@\"NSData\",&,V_cache
newWithURL:fileOpenFlags:error:
createDirectoryAtURL:withIntermediateDirectories:attributes:error:
initWithFormat:baseBackendXPC:
RAMdisk
Ti,R,N,V_blockSize
addPassphraseEntryWithXpcHandler:flags:usage:error:
allowParallelModeWithURL:outMode:error:
defaultManager
failWithOSStatus:verboseInfo:error:
T@\"NSXPCListenerEndpoint\",&,N,V_xpcEndpoint
_ioMedia
daSession
retrieveWithError:
setConversionMethod:
setRegEntryID:
setSlaText:
supportsPstack
CLIPassphrasePromptCreate
T@\"NSURLSession\",R,V_urlSession
frameworkBundle
TB,N
URLByAppendingPathExtension:
initWithIOObject:
newAEABackendThrowsWithBackendXPC:error:
progressWithTotalUnitCount:parent:pendingUnitCount:
mandatoryArgumentFailWithError:
fileHandleForReadingFromURL:error:
initWithCoder:
retainCount
setIsPrivileged:
backendXPC
imageInfo
initWithRegistryEntryID:error:
sparseBundleBandSize
T@\"DITemporaryPassphrase\",&,N,V_temporaryPassphrase
T@\"NSURL\",C,N,V_customCacheURL
numberWithBool:
getKnoxDecryptionComponentsWithURL:payloadURI:destKey:keySize:error:
getPublicKeyWithCertificate:error:
valueForKey:
T@\"BackendXPC\",&,N,V_cacheBackendXPC
cryptoHeader
openWithError:
setOperationError:
temporaryDirectory
ioMedia
_tag
addObjectsFromArray:
lock
lockAndMoveOpenParams
setOpenEncryption:
setOutputURL:
setStream:
_copier
T@\"NSURL\",R,V_url
cloneToURL:error:
confirmSLAAcceptedWithError:
initWithSession:size:atOffset:destinationBuffer:destinationStream:completionSemaphore:
toHeaderEncryptionMode:headerEncMode:error:
T*,N,V_buf
isMountCompleteWithExpectedCount:diskTracker:
popObjectForKey:
base64EncodedStringWithOptions:
TI,V_remainingAttempts
T@\"DIDeviceHandle\",&,N,V_deviceHandle
T@\"NSURL\",R,C,N,V_mountedOnURL
getImageUUIDStrWithIdentityInfo:stackableUUIDFallback:error:
initWithSrcFolder:parallelMode:auditToken:
T@\"DIDiskArb\",R,N,V_diskArb
_mediaRef
cacheURL
failWithPOSIXCode:error:
.cxx_construct
diskArb
_diParams
confirmSLAAcceptedWithReply:
removeNodeWithUUID:recursive:error:
statusCode
waitForDAMountWithError:
CLIVerifyPassphrasePromptCreate
initWithData:
setCancelled:
setIoMediaUUID:
setShadowChain:
T{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}},R,N
debugLogsEnabled
ensureDeviceIdentityWithError:
verifyWithParams:reply:
setFileBackend:
UIOOpenMode
_daSession
initWithServiceName:
mutableBytes
symmetricKey
dictionaryWithObjects:forKeys:count:
setActiveNodeWithTag:error:
T@\"NSXPCListenerEndpoint\",&,N,V_xpcListenerEndpoint
findVolumeBSDNameWithError:
updateStatFSWithError:
_progress
_remainingAttempts
initWithHandles:
initWithObjects:
setInputMountedFrom:
setBuf:
T@\"NSString\",C,N,V_inputMountedFrom
_key
conversionMethod
initWithGraphDB:pstackURL:error:
initWithPluginName:pluginParams:tag:error:
newDI1DevicesArrayWithError:
objectForKey:
T@\"BackendXPC\",&,N,V_backendXPC
_buf
copyDictNodesToFolder:dict:error:
setCustomCacheURL:
setObject:forKeyedSubscript:
setReadPassphraseFlags:
Tq,R,N,V_frameworkNum
_backendXPC
convertPrivateKeyToPEMWithX963PrivateKey:error:
countByEnumeratingWithState:objects:count:
updateDiskImageParamsWithFrontend:error:
T@\"NSString\",R,C,N,V_BSDName
_inputURL
completeRequest:data:response:error:
onDisappearedMountPoint
pluginParams
readDataUpToLength:error:
storeInKeychainWithPassphrase:forceSystemKeychain:error:
release
TB,R,N,V_isQuarantined
_autoMount
_inputMountedOnURL
_metadata
maxRequests
mountWithDeviceName:args:filesystem:mountURL:error:
_slaText
fileSystem
host
initWithURL:cachePolicy:timeoutInterval:
setSize:
dictionary
fileURLWithPath:relativeToURL:
initWithPstackURL:error:
initWithUUIDString:
parent
deserializationError
enumerateObjectsUsingBlock:
setEncryptionMethod:
setExecutableURL:
setRemoteObjectInterface:
topDiskImageNumBlocks
_isQuarantined
autorelease
blockSize
commandSize
fileURLWithPath:
TB,N,V_onDiskCache
_cancelled
getAEAKeyFromSAKSWithMetadata:key:error:
populateNodesDictsWithArray:workDir:nodesDict:error:
T@\"DICreateParams\",&,N,V_createParams
diskImageAttach:readOnly:autoMount:BSDName:error:
unarchivedObjectOfClasses:fromData:error:
unmountWithMountPoint:error:
TI,R,V_maxAttempts
failWithEnumValue:verboseInfo:error:
@32@0:8r^v16@24
v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}16
{shared_ptr<unsigned char>=\"__ptr_\"*\"__cntrl_\"^{__shared_weak_count}}
{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>={?=^{diskimage}
B48@0:8@16B24B28^@32^@40
@\"NSURLSession\"
B40@0:8r^v16@24^@32
@\"NSString\"24@0:8^@16
B24@0:8r^v16
{shared_ptr<unsigned char>=*^{__shared_weak_count}}16@0:8
v28@0:8@16B24
@\"NSError\"
@40@0:8q16@24^@32
B40@0:8^B16^B24^@32
v24@0:8Q16
@56@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24^Q40^@48
@28@0:8@16i24
@32@0:8Q16^@24
v32@0:8@16@24
@60@0:8@16@24@32@40@48B56
@68@0:8@16@24@32@40@48@56B64
v24@0:8^v16
v32@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16
Q16@0:8
@\"DITemporaryPassphrase\"
B40@0:8^v16Q24^@32
Q32@0:8@16Q24
@\"DIClient2IODaemonXPCHandler\"
v24@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16
v24@0:8^{__DASession=}16
@\"FileLocalXPC\"
v32@0:8r*16Q24
B32@0:8@16@24
v24@0:8@\"NSCoder\"16
v32@0:8@\"DIDeviceHandle\"16@?<v@?@\"NSError\">24
B48@0:8^v16*24Q32^@40
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8B16B20
Q24@0:8^@16
@\"DIDiskMountTracker\"
{shared_ptr<crypto::passphrase_header>=\"__ptr_\"^{passphrase_header}\"__cntrl_\"^{__shared_weak_count}}
@\"NSString\"16@0:8
@\"NSXPCListener\"
B48@0:8@16@24Q32^@40
v20@0:8B16
@\"DIBaseParams\"
i16@0:8
i32@0:8^v16Q24
@\"NSUUID\"
v24@0:8@?<v@?@\"NSError\">16
@20@0:8I16
B48@0:8r^{AuthData=^{AEAAuthData_impl}}16*24Q32^@40
r^v16@0:8
{unique_ptr<diskimage_uio::diskimage_open_params, std::default_delete<diskimage_uio::diskimage_open_params>>=\"\"{?=\"__ptr_\"^{diskimage_open_params}}}
@32@0:8q16@24
i
Q
@36@0:8@16B24^@28
@24@0:8r*16
@\"NSURL\"
@24@0:8@16
B40@0:8*16@24^@32
@\"DIDeviceHandle\"
{expected<std::shared_ptr<Backend>, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<std::shared_ptr<Backend>, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<std::s
@28@0:8i16^@20
B64@0:8r*16Q24{function<bool (iokit_utils::di_io_obj_t)>={__value_func<bool (iokit_utils::di_io_obj_t)>=(type=[24C])^v}}32
v24@0:8@?<v@?@\"DIDeviceHandle\"@\"NSError\">16
@56@0:8@16@24@32@40^@48
B48@0:8@16Q24q32^@40
@32@0:8@16@?24
{shared_ptr<crypto::header>=\"__ptr_\"^{header}\"__cntrl_\"^{__shared_weak_count}}
v32@0:8{shared_ptr<BaseFolderCopier>=^{BaseFolderCopier}^{__shared_weak_count}}16
B40@0:8@16@24^@32
@24@0:8q16
B32@0:8q16^@24
^v16@0:8
@
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
B56@0:8@16@24@32^@40^@48
@28@0:8I16^@20
I
*
B40@0:8Q16^v24^@32
@\"NSProgress\"
@32@0:8Q16@24
@32@0:8@16^@24
B44@0:8@16B24Q28^@36
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}
B28@0:8I16^@20
^{?=Q*^{AAS3Context_impl}}16@0:8
#16@0:8
{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"\"{?=\"__ptr_\"^{header}}}
@24@0:8I16B20
{shared_ptr<BaseFolderCopier>=^{BaseFolderCopier}^{__shared_weak_count}}16@0:8
B48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}}16@0:8
@\"DIShadowChain\"
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}
v32@0:8@\"DIAttachParams\"16@?<v@?@\"NSError\">24
B40@0:8@16q24^@32
^v24@0:8^@16
{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16@0:8
{shared_ptr<Backend>=\"__ptr_\"^{Backend}\"__cntrl_\"^{__shared_weak_count}}
@\"NSData\"
B40@0:8@16*24^@32
{shared_ptr<DiskImage>=^{DiskImage}^{__shared_weak_count}}60@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16Q32r^v40B48Q52
B40@0:8r*16Q24^@32
B40@0:8@16^B24^@32
i40@0:8^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16Q24q32
^{?=Q*^{AAS3Context_impl}}
@\"NSDictionary\"
B28@0:8i16^@20
B36@0:8B16q20^@28
B32@0:8r*16^@24
@24@0:8:16
B64@0:8@16B24@28Q36@44B52^@56
f
@44@0:8@16^{?=Q*^{AAS3Context_impl}}24I32f36I40
^{__DASession=}
@\"DIStatFS\"
B56@0:8@16@24@32@40^@48
B
@28@0:8@16B24
v40@0:8@16q24@?32
B56@0:8@16B24@28Q36B44^@48
{expected<diskimage_uio::diskimage_open_params, std::error_code>=(storage<diskimage_uio::diskimage_open_params, std::error_code>=c{diskimage_open_params=^{diskimage_open_params_impl}}{error_code=i^{error_category}})B}16@0:8
v20@0:8I16
@48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40
B48@0:8@16*24Q32^@40
^{__MKMedia=}
v24@0:8q16
@\"DIDataPartition\"
@\"NSMutableURLRequest\"
^{__DASession=}16@0:8
B48@0:8@16@24@32^@40
v20@0:8f16
B32@0:8@16^@24
v24@0:8^{__DADisk=}16
Vv16@0:8
@24@0:8Q16
@\"NSMutableData\"
v24@0:8B16B20
{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>={?=^{DiskImageInfo}}}28@0:8B16^@20
@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}24
@64@0:8@16Q24q32*40^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}48@56
@\"AAS3DownloadSession\"
@\"NSArray\"
@52@0:8@16@24@32@40B48
f16@0:8
v24@0:8@?16
B48@0:8@16q24@32^@40
AQ
v40@0:8@16@24@32
v20@0:8i16
@32@0:8#16@24
I16@0:8
@40@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16^@32
Ai
@40@0:8@16^{__SecCertificate=}24^@32
@24@0:8^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}16
{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_des
@40@0:8@16{shared_ptr<unsigned char>=*^{__shared_weak_count}}24
@\"NSLock\"
v32@0:8@\"DIVerifyParams\"16@?<v@?@\"NSError\">24
@32@0:8@16Q24
@\"DIDiskArb\"
B44@0:8@16#24B32^@36
@\"NSMutableArray\"
@24@0:8r^v16
@32@0:8^v16r^v24
@32@0:8:16@24
@32@0:8r^v16^@24
^{__MKMedia=}16@0:8
i24@0:8@16
@\"DIURL\"
v40@0:8@\"DIEncryptionCreator\"16@\"NSString\"24@?<v@?@\"DIEncryptionCreator\"@\"NSError\">32
q16@0:8
B32@0:8Q16^@24
@36@0:8@16B24^{?=[8I]}28
@\"NSString\"
@56@0:8@16q24@32@40^@48
v32@0:8@\"DIStatsParams\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8^@16
Q32@0:8@16^@24
{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<
@40@0:8:16@24@32
*16@0:8
v32@0:8Q16Q24
q
B24@0:8^@16
B16@0:8
@\"DiskImageParamsXPC\"
B56@0:8@16^@24*32^Q40^@48
v32@0:8@16@?24
B24@0:8#16
B44@0:8@16@24B32^@36
B40@0:8q16@24^@32
@40@0:8r^v16@24^@32
v48@0:8@16@24@32@40
v24@0:8@16
@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>={?=^{header}}}24
B24@0:8Q16
@\"BackendXPC\"
@56@0:8Q16q24*32^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}40@48
@32@0:8@16@24
@\"<DIDisappearedMountPointDelegate>\"
@\"NSMutableDictionary\"
B36@0:8@16B24^@28
@\"DIClient2Controller_XPCHandler\"
B40@0:8@16Q24^@32
v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24
@24@0:8^@16
B40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
@\"DICreateParams\"
@\"NSXPCConnection\"
^{AAAsyncByteStream_impl=^v^?^?^?^?^?^v}16@0:8
v32@0:8@\"DIEncryptionFrontend\"16@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">24
@16@0:8
@\"NSNumber\"
@40@0:8@16q24^@32
q40@0:8^v16Q24q32
@48@0:8@16@24@32^@40
B40@0:8@16^@24^@32
@28@0:8i16@20
v40@0:8@16@24@?32
^{_NSZone=}16@0:8
v24@0:8*16
@\"NSMutableSet\"
{unique_ptr<udif::header, std::default_delete<udif::header>>=\"\"{?=\"__ptr_\"^{header}}}
@28@0:8i16B20B24
@32@0:8@16^v24
@36@0:8Q16B24^@28
@36@0:8i16@20^@28
v40@0:8@\"DIEncryptionFrontend\"16q24@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">32
{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}16@0:8
@\"NSXPCListenerEndpoint\"
@32@0:8^{diskimage_open_params=^{diskimage_open_params_impl}}16r^v24
@40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32
B24@0:8:16
@24@0:8@?16
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v16@0:8
B28@0:8B16^@20
@36@0:8@16i24^@28
@\"DiskImageGraphNode\"
@40@0:8@16Q24^@32
B24@0:8@\"Protocol\"16
@36@0:8@16i24Q28
{shared_ptr<BaseFolderCopier>=\"__ptr_\"^{BaseFolderCopier}\"__cntrl_\"^{__shared_weak_count}}
B36@0:8i16@20^@28
@\"NSObject<OS_dispatch_semaphore>\"
@28@0:8B16^@20
@\"DIIOMedia\"
B32@0:8^B16^@24
@40@0:8@16@24^@32
B24@0:8@16
@\"NSProgress\"32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24
@24@0:8@\"NSCoder\"16
@\"NSObject<OS_dispatch_queue>\"
@44@0:8@16Q24i32^@36
{expected<void, std::error_code>=(constexpr_storage<void, std::error_code>=c{error_code=i^{error_category}})B}24@0:8^{diskimage_open_params=^{diskimage_open_params_impl}}16
-[DICreateParams onErrorCleanup]
Disk image is terminated, skipping read
-[DIVerifyParams verifyWithError:]
The format string terminates at a '{'
SLA prompt cancelled
XPC connection failed
Cannot find AmberDiskImagePluginCreate in libAmber
Full Entries
std::unique_ptr<FileLocal> SparseBundleBackend::read_info(const std::string &)
Failed to parse key in KVS (zero size key).
/dev/%@
Cannot find image with provided UUID.
private/var/db/dyld
Sandbox checked for 
Failed opening folder for entries reading
failed to enter SQE to the ring, ret code 
Agree Y/N? 
void di_hybrid_subscriber_t::resume()
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = pstack_header]
ASIF max_write size in header exceed the limit
Failed reading 
Skipping band erase (in use)
v24@?0@\"DIEncryptionCreator\"8@\"NSError\"16
YES
-[DIDiskMountTracker trackIfMyDisk:]
Failed opening the file
-[DIBaseXPCHandler init]
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_with_plugin(const std::string &, CFDictionaryRef, diskimage_open_params::mode)
com.apple.DiskImages2.TelemetryManager
com.apple.diskimage-plugin.nbd
UDZO
expected<size_t, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_block_size() const
.vol
set_euid_wrapper::set_euid_wrapper(uid_t)
void lw_future_managed_setter<batch_ctx_ns::batched_result<int>>::put() [T = batch_ctx_ns::batched_result<int>, ErrT = int, empty_value = 0]
Failed to allocate raw blob data
-[BaseDiskImageCreator createEmptyImageWithError:]
resource-fork
UDIF - max compressed run size: 
getErrorContextKey
Unsupported host for OIDC: %@
backend
Unmap done
stable uuid
type: 
Nothing to defrag
bool di_asif::details::table_entry_data::validate() const
header_signature
uid temporarily set to 
disk image kernel return
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
Attached disk image device info: BSD Name [%@], image URL [%@]
Blocks header
set_euid_wrapper::~set_euid_wrapper()
Authorization: %s
Not a pstack.
-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]
Diskimageuio: unsupported disk image type for get_backend
static di_plugin_image_t *rawTestPlugin_t::CreationError(const pluginException_t &, CFErrorRef *)
checksum_type
virtual int SparseBundleBackend::lock()
 bytes is smaller than its trailer
which is larger than allowed 
v32@?0@\"NSMutableDictionary\"8Q16^B24
Final asif 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hard
, res=
userData
-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]
Unsupported disk image format
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp
com.apple.DiskImages2
expected<bool, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::is_cache_image() const
fchownat failed for 
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/
-[DIDiskArbEmulation waitForDAMountWithExpectedCount:diskTracker:]
 ret: 
.
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Har
PKCS1 = 10, OEAP_SHA1 = 0x80000001
Non supported options in AAS3DownloadSession (ignored): proxy_pinned_public_key %s
&
ASIF: failed to write metadata
descriptor_special
Failed to create crypto serializer
auto diskimage_uio::details::diskimage_open_params_impl::create_diskimage_from_hdr()::(anonymous class)::operator()(const auto &) const [hdr:auto = raw_header]
bla
Couldn't convert CFStringRef to a proper std string
special: 
Compressed(
Failed to eject - cannot open device
readPassphraseFlags
Malformed URL format
Extent 
-[DIAPFSPartition formatWithVolumeName:error:]
Tag
Failed serializing user dictionary
-[DIStatFS initWithFileDescriptor:error:]
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162
 failed, error 
Block size mismatch in DiskImageStackable
 on 
Corrupted plist dictionary
ssize_t plugin_decode_buffer(void *, const char *, void **)
Cannot find disk image with reg entry ID 0x%llx
encryption_key_bits_size_t
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const
 logical: 
-[MKDIDevice updatePartitionMapWithError:]
Authorization
, allocated: 
AAS3DownloadStream (NSURLSession)\n
static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)
lzfse
0123456789abcdef
 errno: 
HTTP request failed with status code: %ld
invalid length
Backend barrier failed during bitmap allocator failures handling, error 
 requested while there are only 
Range:
Clone of plugin nodes is not supported.
Diskimageuio: multiple images given, but first role is image instead of shadow/cache/snapshot
virtual void DiskImageSparseBundle::on_eject()
Image cache flag does not match the requested operation.
band-size
Failed to unlock the encrypted image during open
-[DIClient2IODaemonXPCHandler cancelSLAWithReason:]
publicKey
Diskimageuio: Couldn't get diskimage: 
fetch_restore_keys_ephemeral
-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]
Mapped Sectors
\\n
, UID:GID(Name)=
!
diskimagesiod
KVS key value - parse failure.
RAW read-write image
Failed opening mapped blocks file for 
Metadata
Failed to set up image for resize
virtual void ParallelFolderCopier::copyFiles(progressFunc_t) const
Cannot get subscriber from plugin
AppleAPFSVolume
\\t
 length 
com.apple.diskimages_cache_update
void rawTestPlugin_t::subscriber_t::_suspend()
> real: <
Resetting 
s3Perform
pthread_once
int PluginsManager::register_plugin(const string &, di_plugin_t *)
knox-uat.sd.apple.com
virtual int BackendSG::write(const sg_entry &)
Failed to write asif header, error 
virtual int BackendSG::read(const sg_entry &)
-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]
 = offset = 
static int FileDescriptorWrapper::open_file(const std::string &, int)
strdup
Cannot retrieve passphrase from user via TTY or GUI
-[DIConvertParams shouldPerformInplaceSquash]
UDZOMAX
udsb
unique_lock::unlock: not locked
-[PluginDiskImageGraphNode(Append) validateAppendedImageWithInfo:error:]
diskimage-bundle-type
int DiskImagePlugin::sync_enter_and_wait(io_rings_sqe_t *, Context &)
expected<std::shared_ptr<Backend>, diskimage_err> diskimage_uio::details::diskimage_impl::get_backend() const
Diskimageuio: Multiple images given, except for top or bottom, role should be cache/snapshot, but role given 
sign
The type option contains an invalid value for a string formatting argument
auto PluginsManager::register_plugin(const string &, di_plugin_t *)::(anonymous class)::operator()(di_plugin_t *) const
-[DIBaseXPCHandler completeCommandWithError:]
We're out of ctxs for async execute
ASIF: can't set requested uuid
File descriptor 
void SparseBundleBackend::write_primary_info_plist()
virtual int Backend::write(const elements_t &)
flags validator
Temporary Items
virtual size_t BZIPCompressedBackend::decompress(const sg_entry &, char *) const
Failed to check encryption status
Missing parent node in graph.
Integral value outside the range of the char type
Image info is not supported for the given image type
com.apple.wkms.auth-data
-[DIDiskArb waitForDAIdleWithError:]
-[FileLocalXPC sandboxExtensionTokenWithError:]
v32@?0@\"DiskImageGraphNode\"8Q16^B24
Diskimageuio: get parent uuid failed 
virtual int Backend::read(const elements_t &)
-[DIClient2IODaemonXPCHandler createConnection]_block_invoke
kern.aioprocmax
Backend barrier failed during allocator failures handling, error 
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1553: libc++ Har
-[DIDiskMountTracker onDiskAppearedWithDiskName:isMountable:]
shadow
Couldn't read asif's full header
Pstack corrupted, found a cache node without a non-cache ancestor.
Unsupported compressed run (
Failed to update crypto header
}
Only RAW, ASIF and UDSB formats are supported for new blank images
Failed placing new 
failed to set euid to 
raw
Couldn't upgrade lock entry 
Using automatic argument numbering in manual argument numbering mode
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
\\\"
, disk size: 
knox
total_segments_t
Unsupported value for crypto header field 
Couldn't open file with flags 
Context setup failed.
 but buffer is full
Diskimageuio: No diskimage given
Uninitialized Entries
 option
bytes=
No
Not valid SAKS environment
IOService
zlib
Unmapping band 
virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)
virtual int FileLocalAsync::truncate(uint64_t)
Calling 
 while expecting 
x-amz-
%02x
int sparse_bundles::mapped_blocks_t::flush()
Backend: failed reading element in vector
Not valid SAKS metadata (json format expected)
set size failed
device not found in registry
wrap_key_crypto_algo
version_t
Can't get key in cstring format
v32@?0@\"NSURL\"8Q16^B24
ReadOnlyBackend
-[SparseBundleBackendXPC getCryptoHeaderBackend]
unmanaged
AWS4-HMAC-SHA256 Credential=
hdid-pid
Diskimageuio: image is locked
Checksum Value
Failed to get plugin instance
+[DIAttachedDeviceInfo copyAllMountPoints]
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::validate_unlocked() const
flags_t
The width option should not have a leading zero
crypto_format: blob length differs
user data retrieving failed
Failed opening the image with RW access
iokit error
asif: chunk size is too small, too many dir indices
FSPersonalities
i
virtual int FileLocalAsync::lock()
-[AAS3DownloadSession initWithURL:streamBase:maxAttempts:pauseInterval:maxRequestsInFlight:]
algorithm_type
Failed to erase band 
+[DiskImageParamsXPC newWithUnlockedBackendXPC:error:]
tuple<int, size_t> DiskImageSparseBundle::flush_open_bands()_block_invoke
ASIF: No data offset found (write)
CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)
table entry map@
bands
metadata
Disk image is terminated, skipping write
, but file size only 
Failed to copy metadata of %s
-[MKDIDevice initWithBSDName:numBlocks:blockSize:error:]
crypto
bad flush type (
+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
.Trash
Failed copying %s
std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)
'
IOBlockStorageDriver
-[AAS3DownloadSession addRequest:]
Could not generate daw token - AppleConnect Failure
Invalid size hex key %lu
File size is less than the minimum header size
Invalid format for shadow file
%@[%@]
Compressed Offset
Failed to encrypt data using public key from certificate
band_ptr DiskImageSparseBundle::open_band(uint64_t, int)
Failed to store the passphrase in the keychain
attempting to authenticate with saks
inputMountedFrom
diskimageuio: pre-write final error 
char *udif::header::write(char *)
Run interval: 
 failed wih error 
lock
diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>]
int copyfileWithClassFHandling(const char *, const char *, copyfile_state_t, copyfile_flags_t)
device with registry entry ID 0x
auth-data
supportsPersistentAttach
encryptionMethod
passphrase
%@ failed with error code %d
Diskimageuio: get nr blocks failed 
Starting flush
UDIF: Can't find data key in dictionary
wkms-dev.sd.apple.com
instanceID
Malformed ram URL, expected to be ram://<?? | ??b | ??k | ??m | ??g | ??t>
static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = std::move_iterator<std::__wrap_iter<diskimage_uio::diskimage_open_params_pair *>>]
ASIF: Content dirty bit is set when reading from disk
-[DiskImageCreatorFromFolder createImageWithSrcFolder:completionBlock:]_block_invoke_2
-[DIDataPartition resizeFileSystemToMinimumWithError:]
 for 
s3StreamBaseInit
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::open_and_resolve(const diskimage_open_params::mode, bool)
int rawTestPlugin_t::do_io(const IOV_OP &, ssize_t (*)(int, const struct iovec *, int, off_t)) [IOV_OP = io_rings_sqe_op_read_iov_t]
wkms
raw_header
key_derivation_algorithm_t
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410:
Can't write initial table data
, 
Updating 
B32@?0@\"NSString\"8@\"DiskImageGraphNode\"16^B24
rings_queue
Invalid schemes returned by MediaKit
locale-specific form
Unknown checksum found
Mode for new files in bundle: 
Missing payload URI in Knox response
Missing OIDC client ID in appinfo response
Image Format
UDIF images are currently not supported in diskimage_uio
map_element flush failed on creation
int plugin_decode_fd(void *, const char *)
{:02x}{:02x}
gcd_kqueue: kevent64 failed with ENOMEM
ramTestPluginCreate
expected<std::optional<uuid_t>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_parent_uuid() const
virtual int DiskImage::set_size(uint64_t)
could not create iterator (begin)
%s (%@)
ASIF meta header failed to read
Invalid partitions returned by MediaKit
true
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__format/formatter_out
\\u{
Invalid open mode specified
(err code %d)
NO
Failed unlocking file with fd 
autoMount
Unexpected backend type for file
Diskimageuio: backend doesn't exist
void diskimage_uio::details::async_execute_impl(io_rings_subscriber_t *) [di_subscriber_t = io_rings_di_subscriber_t]
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const
com.apple.diskimages2.fast_copy
fchmodat failed for 
+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
Size Info
Failed during table 
Cannot change passphrase of unencrypted image
0X
Failed to create diskimage_open_params
Missing image path property
attempting to authenticate with wkms
Udif: advanced buffer, needs to read 
numBlocks
pstack_header
cert-chain
void di_plugin_cq_event_callback(io_uhandle_t, void *, enum io_rings_event_type_t, struct io_rings_event_type_data_t *)
crypt_consecutive_vector: write check errors 
Disk image operation failed with error code %d
+[DICreateParams eraseIfExistingWithURL:error:]
ASIF: data entry - invalid reserved bits
.FBCLockFolder
> %d %s\n
-[DIBaseParams tryResolvePstackChain:]
Barrier failed after defrag, error 
-[MKDIDevice partitionDiskWithGPTTypeID:error:]
The format string contains an invalid escape sequence
Can't parse encryption entry: 
/Library/Caches/com.apple.xbs/B12752E6-52AB-4E21-B84A-D89217119754/TemporaryDirectory.M7lnho/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m
-[DIAttachParams isDeviceWithProperty:registryEntryID:predicate:]
.hotfiles.btree
Failed to copy %s
Couldn't open 
IOServiceWaitQuiet error 0x%x
B24@?0@\"DIShadowNode\"8@\"NSDictionary\"16
Size is not a multiple of block size
Can't load bitmap from backend
virtual int FileLocalAsync::unmap_range(uint64_t, uint64_t)
Images Count
slaText
Constructing sb context
entire_device
virtual int SparseBundleBackend::unlock_all()
enqueueRequest
/System/Library/PrivateFrameworks/DiskImages2.framework
plist
certificate
Can't connect to device
source uuid
 src size 
crypto_format: cookie differs
-[DIDeviceHandle dealloc]
AAS3ContextSetFieldString
vsnprintf
-[DIConvertParams prepareConvertWithError:]
Barrier failed before dir flush
Cannot get temporary directory
Custom encryption entry header size exceeds max size
StandardCompressedBackend::pimpl::pimpl(algo_t)
get path failed
Failed creating 
Failed creating sparsebundle folder
Unexpected UDIF header length (
udro
flush
int sparse_bundles::Band::flush()
void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5C
-[DIDiskArb unmountWithMountPoint:error:]
Failed to retrieve info
AEA
-[DIDiskArbEmulation unmountWithMountPoint:error:]
Decryption key missing
bzip2
Evicting all bands for eject
The format specifier should consume the input or end with a '}'
Daemon PID
system
Segmented UDIF images are not supported by this framework
Plugin's ring suspended, ret code 
IO error with sg: 
-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]
static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)
Image does not have write permissions
Failed creating CFData
IsCache
-[DIEncryptionChpass unlockWithPassphrase:error:]
diskimage_
-[DIConvertParams prepareParamsForSquashWithError:]
Bearer %@
 (band 0x
 bytes are above the sparsebundle limit of 
File: Couldn't fetch status, error: 
truncate error: 
Invalid size of saks response %lu
lock_backend
Failed to update asif header
s3DownloadStreamOpen_urlsession
UDIF: Can't get types array from UDIF
oidc
Missing key in SAKS response
Failed to find IO media entry for %@
udzo_max
Raw header changed while unlocked
auto hdr_get_block_size(const hdr_variant &)::(anonymous class)::operator()(const auto &) const [hdr:auto = std::monostate]
Source folder must be a path
UDIF: compression algo is invalid
v24@?0@\"DIEncryptionFrontend\"8@\"NSError\"16
token
hw.memsize
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc+
+[AAS3DownloadSession completeRequest:data:response:error:]
Failed to create DADisk during unmount
Destination folder URL must represent an existing folder.
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::initializer_list<rref_capture<diskimage_open_params_pair>>, uint32_t)
uint64_t space_allocators::FixedSize::allocate(const size_changed_fn_t &)
Failed creating the image
UDIF read-only compressed image
Close completed
CacheURL
UUID
+[DISLAFrontend(Private) displaySLAText:error:]
-[DIConvertParams onConvertCompletionWithInError:outError:]
 doesn't exist, returning zeros
, trimmed size
 bits in the bitmap
Failed to find DiskImages2 controller, driver might not be installed
AppleDiskImageDevice
Diskimageuio: Couldn't lock backend 
zero = 0x00000000ul, raw = 0x00000001ul, ignore = 0x00000002ul, comment = 0x7FFFFFFEul, adc_old = 0x80000000ul, first_plugin = 0x80000001ul, kencode = 0x80000001ul, dartrle = 0x80000002ul, dartlzh = 0x80000003ul, adc = 0x80000004ul, zlib = 
Failed to evict band to make room for 
-[AAS3DownloadSession enqueueRequestWithSize:atOffset:destinationBuffer:destinationStream:completionSemaphore:]
/sbin/mount
UDIFDiskImage: failed truncating image
/System/Library/Filesystems/apfs.fs
false
Couldn't lock entry
Couldn't exclusively lock entry 
void sparse_bundles::mapped_blocks_t::unmap_interval(uint64_t, uint64_t)
std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const
std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)
dealloc_queue
SHA1_HMAC = 91, NONE = 0
) is locked
dispatch_source_create failed
encryption
ID
Failed to create chiper data for public key auth
Default
GET
static expected<diskimage, diskimage_err> diskimage_uio::diskimage::create(std::vector<diskimage_open_params_pair> &&, uint32_t)
End of input while parsing format specifier precision
Failed to read 
Failed to parse key in KVS (zero size data).
di_plugin_t *amberPluginCreate(uint64_t)_block_invoke
-[DIUserDataParams retrieveWithError:]
Failed to open backend of crypto header
Diskimageuio: Can't create stackable image: 
Schemes
0x
wrap_key_crypto_padding_algo
virtual di_coroutines::Task<void> crypto_format_backend::run_futures()
ddm
v24@?0@\"NSDictionary\"8@\"NSError\"16
Cannot create target image format with the block size of the source image
RootDeviceEntryID
UDBZ
Diskimageuio: images with constraints currently not supported
AES_KEY = 0x80000001
%s: 
Error creating disk image params
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Har
Total Bytes
crypto_format: Can't decrypt wrapped key 
Locked encrypted image
Flushed 
pstack
DiskImageSparseBundle::DiskImageSparseBundle(const shared_ptr<SparseBundleBackend> &, size_t)
 is closed, notifying waiters
io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = io_result_t (&)(const sg_entry &)]
invalid header: %s
Disk image URL is too long
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697
Error during ASIF flush: 
Failed creating MediaKit device refcon
CBC_IV8 = 5, XTS = 0x80000001
flattened = bit(0), raw_image = bit(1), internet_enable = bit(2)
Failed to add symmetric key entry to auth table
not a valid DER-encoded X.509 certificate
Diskimageuio: Nested stacking is not allowed.
Cannot open filesystems bundle
nil params specified
daw
useFormatMappingInfo
io_result_t DiskImage::Context::write(const sg_vec::iterator &, const sg_vec::iterator &)
 elements returned 
creating session
Diskimageuio: after reopening backend to read-write, it's no longer encrypted
(unrecognized error)
/AppleInternal/Library/BuildRoots/4~CatQugDmjpkP6bW2lpQHtTOWCRHdb0UbQx9vEnk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp
Can't lock entry
] 
Failed to serialize symmetric key to crypto header
UDIF uncompressed read-only image
diskimage_uio::expected<di_plugin_t *, diskimage_uio::diskimage_err> PluginsManager::get_plugin_ptr(const std::string &, bool)
header read-only flags
 buffer_size = 
fd block size retrieval failed (err code 
/AppleInternal/System/Library/libtest_plugin_shared_object.dylib
-[DIEncryptionFrontend askPermissionWithRememberPassword:error:]
emulateExternalDisk
suppressSsdFlags
High Throughput Options
None
Cannot decode writable
Can't write table for defrag
saks-ac-dev.g.apple.com
int DiskImage::Context::flush(di_flush_mode)
 - 
V2 = 2
ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/app/utils.c
 - unmap_range: [
File (fd 
-[AAS3DownloadRequest createAndResumeTask]
SLA text is empty
Missing key in KKMS response
-[DIBaseXPCHandler createConnection]
Max Size Bytes
Band was evicted by another thread (during retain attempt), retry erase process
intermediate-certs
+[DIError errorWithDomain:code:description:verboseInfo:error:]
encryption_mode
Cannot initialize pstack disk image without path.
expected<void, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::resolve_disk_after_crypto_ctx(std::optional<crypto_internal::keys> &&)
Got error when trying to close 
AEAHelper: Invalid file descriptor.
mapped blocks of band 
```
