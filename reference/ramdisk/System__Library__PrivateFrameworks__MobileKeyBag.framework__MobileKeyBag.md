# `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

From the upgrade restore ramdisk (141-29011-104.dmg). 353,328 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 30 (Size: 4120)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (13)

- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 2 protocols)

Classes: `MKBKeyStoreDevice`

Protocols: `KBXPCProtocol`, `NSObject`

## Strings (997)

```
MKBUnlockDeviceForACMRef
SE_unlock
%s\n
handle=%{public}d
AKS_unlock_verify
result=%{public}d
SE_enroll
completed
Unexpected AppleKeyStore error: %d\n
handle=%{public}d secretIsACM=%{public}d use_memento=%{public}d verify_only=%{public}d
MKBKeyStoreDevice
KBXPCProtocol
NSObject
getLockSateInfoforUser:WithReply:
loadKeybagForUserSession:withSessionID:withSecret:secretSize:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:withReply:
passcodeUnlockFailedWithReply:
removePersonaKeyForUserSession:withPersonaUUIDString:withVolumeUUIDString:
stashCommitwithUID:WithFlags:WithReply:
stopBackupSessionForVolume:withReply:
unloadKeybagForUserSession:withReply:
zone
createSyncBagForUserSession:withSessionUID:withReply:
getBackupkeyForVolume:andCryptoID:withError:
getDeviceLockState:needsExtended:withReply:
startBackupSessionForVolume:withReply:
backupUUIDForVolume:reply:
migrateFS
null
retainCount
setRemoteObjectInterface:
setSystemSecretBlob:reply:
getBackupkeyForVolume:andCryptoID:withReply:
SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:
T@\"NSString\",R,C
copySytemSecretBlob
isKeyRollingWithKeyStatus:
isKindOfClass:
migrationWithReply:
self
SeshatEnroll:secretIsACM:
_CreateMKBServerConnection
createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:
stashCreatewithSecret:secrestSize:withMode:withUID:WithFlags:reply:
stashDestroy
unloadSyncBagForUserSession:withSessionUID:
enableBackupForVolume:withSecret:secretIsACM:bagData:
bytes
length
loadSyncBagForUserSession:withSessionUID:withReply:
setVolumeToPersona:withPersonaString:withReply:
startBackupSessionForVolume:
verifySyncBagForUserSession:withSessionUID:withReply:
SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:
stashVerifywithUID:WithFlags:WithReply:
changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:
deleteKeybagForUserSession:withReply:
errorWithDomain:code:userInfo:
setSpacedRepetitionMode:reply:
release
passcodeUnlockSuccessWithReply:
SeshatDebug:
addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:
changeSystemSecretFromOldPasscode:ToNew:withOpaqueData:withParams:
forgottenPasscodeEventWithReply:
passcodeUnlockStart
setSpacedRepetitionMode:
forgottenPasscodeEvent
changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:
autorelease
getLockStateForUser:
initWithMachServiceName:options:
numberWithUnsignedLongLong:
verifySyncBagForUserSession:withSessionUID:
resume
stashDestroywithReply:
T@\"NSString\",?,R,C
changeSystemSecretfromOldSecret:oldSize:toNewSecret:newSize:opaqueData:withParams:reply:
code
disableBackupForVolume:
isKeyRollingInProgresswithreply:
loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:
stashCommit:WithFlags:
unloadSyncBagForUserSession:withSessionUID:withReply:
createKeybagForUserSession:withSessionUID:WithSecret:secretSize:withGracePeriod:withOpaqeStuff:withReply:
getFileHandleForData:
isMemberOfClass:
sharedService
unloadKeybagForUserSession:
disableBackupForVolume:reply:
passcodeUnlockFailed
removePersonaKeyForUserSession:withUID:withVolumeUUIDString:withReply:
passcodeUnlockStartWithReply:
removeSyncBagForUserSession:withSessionUID:withReply:
Event:
performSelector:
performSelector:withObject:withObject:
isProxy
T#,R
enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:
loadSyncBagForUserSession:withSessionUID:
setVolumeToPersona:withPersonaString:
getBytes:length:
SeshatDebugWithDebugMask:withReply:
backupUUIDForVolume:bagUUID:
hash
initWithFileDescriptor:closeOnDealloc:
respondsToSelector:
_xpcConnection
isEqual:
ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:
invalidate
passcodeUnlockSuccess
retain
stashVerifywithValidity:WithUID:WithFlags:
changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:
debugDescription
registerBackupBag:withSecret:secretSize:secretIsACM:reply:
SetSystemSecretBlob:
class
superclass
synchronousRemoteObjectProxyWithErrorHandler:
SeshatRecover:secretIsACM:
description
getPasscodeBlobWithReply:
registerOTABackup:withSecret:secretIsACM:
SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:
conformsToProtocol:
SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:
createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:
createSyncBagForUserSession:withSessionUID:
getDeviceLockStateForUser:extendedState:withLockStateInfo:
stashCreateWithSecret:withMode:withUID:WithFlags:
dataWithBytesNoCopy:length:freeWhenDone:
deleteKeybagForUserSession:
dictionaryWithObjects:forKeys:count:
getBackupBlobreply:
removeSyncBagForUserSession:withSessionUID:
stopBackupSessionForVolume:
TQ,R
interfaceWithProtocol:
performSelector:withObject:
v36@0:8@16i24@?28
v52@0:8@\"NSFileHandle\"16Q24i32I36I40@?<v@?@\"NSError\">44
v24@0:8@?<v@?i@\"NSError\">16
v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36B44i48B52@?<v@?@\"NSError\">56
i44@0:8@16@24@32I40
B16@0:8
v52@0:8@16Q24i32I36I40@?44
v48@0:8@\"NSFileHandle\"16Q24B32i36@?<v@?@\"NSError\">40
v32@0:8i16B20@?<v@?i@\"NSError\">24
i44@0:8@16@24B32^@36
@20@0:8i16
i48@0:8I16@20B28@32@40
i36@0:8I16@20@28
v48@0:8@16Q24B32i36@?40
v28@0:8I16@?<v@?@\"NSError\">20
v64@0:8@16Q24B32B36B40@44i52@?56
B24@0:8:16
v40@0:8@16@24@?32
v32@0:8I16I20@?<v@?@\"NSError\">24
i20@0:8i16
i28@0:8@16i24
@32@0:8:16@24
v40@0:8@16Q24@?32
v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSError\">44
v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?@\"NSError\">36
@24@0:8@16
v64@0:8@\"NSFileHandle\"16Q24B32B36B40@\"NSData\"44i52@?<v@?i@\"NSError\">56
B24@0:8@\"Protocol\"16
B24@0:8@16
@24@0:8:16
v24@0:8@?16
v80@0:8@16@24Q32@40Q48@56B64B68@?72
v68@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@\"NSData\"48I56@?<v@?@\"NSError\">60
v80@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@\"NSFileHandle\"40Q48@\"NSData\"56B64B68@?<v@?@\"NSError\">72
v20@0:8i16
v44@0:8@16I24@28@?36
v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSData\"@\"NSError\">44
i24@0:8@16
v64@0:8@16i24@28Q36i44@48@?56
i32@0:8@16@24
@\"NSString\"16@0:8
i24@0:8^i16
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
i32@0:8@16^@24
i48@0:8@16i24@28i36@40
v32@0:8i16B20@?24
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v40@0:8@\"NSData\"16Q24@?<v@?@\"NSData\"@\"NSError\">32
v28@0:8i16@?<v@?@\"NSError\">20
v36@0:8@\"NSDictionary\"16i24@?<v@?@\"NSError\">28
i20@0:8I16
@40@0:8@16Q24^@32
i56@0:8@16@24@32@40i48B52
^{_NSZone=}16@0:8
v32@0:8I16I20@?24
v28@0:8i16@?20
v44@0:8@16Q24B32@?36
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
i36@0:8@16i24I28I32
i24@0:8I16I20
i32@0:8^i16I24I28
v52@0:8@16@24Q32B40@?44
v24@0:8@?<v@?@\"NSError\">16
v28@0:8i16@?<v@?@\"NSDictionary\"@\"NSError\">20
v44@0:8@\"NSString\"16I24@\"NSString\"28@?<v@?@\"NSError\">36
i36@0:8@16@24B32
i16@0:8
i28@0:8@16B24
i48@0:8@16i24@28B36i40B44
@16@0:8
v68@0:8@16Q24@32Q40@48I56@?60
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24
v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?i@\"NSError\">36
i48@0:8@16B24B28B32@36i44
B24@0:8#16
v28@0:8I16@?20
v32@0:8I16I20@?<v@?i@\"NSError\">24
i32@0:8@16i24B28
#16@0:8
@40@0:8:16@24@32
Vv16@0:8
v64@0:8@16@24I32@36Q44B52@?56
v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36i44@\"NSData\"48@?<v@?@\"NSError\">56
v64@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44B52@?<v@?@\"NSError\">56
B32@0:8i16B20^i24
Q16@0:8
v32@0:8@16@?24
v64@0:8@16i24@28Q36B44i48B52@?56
__options_to_change_secret_params
com.apple.mobile.keybagd.db.file.extents.number
MKBUserSessionDisplayName
-[MKBKeyStoreDevice setSpacedRepetitionMode:]_block_invoke
effaceBlastableBytes
HealthPlistSetTime
keybags
result = %d (stash_mode:%d, uid:%d, flags:0x%x)
_MKBVerifyPasswordWithContext
error: unexpected encryption mode : %d
deCryptnextsession: session decrypt length:%d(expected: 32)
MKBUserSessionDisabled
addition of ld failed
APFSVolumePayloadGet len reveived to be %zd
HealthPlistSetFailed
Can't create dict
setNVRam
Can't create %s: %s
Can't encrypt: %d
OverrideMemento
wrapped key size too big (%u>%zu)
UMUserSessionRetrieveSecureBackupBlob
KBLoadSystemKeyBag
1
uuid_parse failed
-[MKBKeyStoreDevice getFileHandleForData:]
got error from remote proxy: %ld
-[MKBKeyStoreDevice backupUUIDForVolume:bagUUID:]_block_invoke_2
-[MKBKeyStoreDevice stashCommit:WithFlags:]_block_invoke_2
-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke_2
_DTIME
KBCleanupSystemKeyBag
KBSecureSaveObjectNoCrypto
aks_prederived_unlock_keybag() returned %d
MKBUserSessionName
MKBUserTypePermanent
Unable to open service: 0x%08x
sep measurement
extents = %s
UMCurrentSyncBubbleSessionID
MKBUserSessionShortName
-[MKBKeyStoreDevice migrateFS]_block_invoke_2
_DULD
validate_health_plist
Unable to decrypt: %d
Failed to validate keybag file: %d, %d
MKBDeviceGetGracePeriod
MKBGetDeviceConfigurations
write failed: %s\n
MKBDeviceModeMultiUser
Saving handle 0 with the magic handle
Retrieved keybag Cookie from AKS, setting in APFS volume
MKBBackupCopyBackupKeyUUID
MKBFileWriteEncrypted
MKBUserSessionRemovePersonaKeyForUser
Could not create stream for serialized data
-[MKBKeyStoreDevice backupUUIDForVolume:bagUUID:]_block_invoke
-[MKBKeyStoreDevice getDeviceLockStateForUser:extendedState:withLockStateInfo:]_block_invoke_2
_DVERS
version is of wrong type
Failed to get backup bag uuid from data: %x
corrupt key; blob size %lu, key size %u
sysctl(hw.osenvironment) -> %d
-[MKBKeyStoreDevice disableBackupForVolume:]_block_invoke_2
-[MKBKeyStoreDevice unloadKeybagForUserSession:]_block_invoke
_MKBWIPEID
MKBUserSessionFirstName
MKBUserSessionCachedLoginEndTime
UserSwitchTaskBundleID
data is of wrong type
Not cookie in this volume, attempting to write it
aks_set_keybag_for_volume_with_cookie_persona SUCCESS
failed to determine whether we are multi-user: 0x%x
crypto_id = 0x%016llx, extent_size = %llu, key class = %u
offset = %zu, keysize = %u, extent size = %llu
MKBUserSessionLastName
Could not get wrapped crypto key for inode %llu right now: %s
invalid ttr format
%s.writing
Error: %@
getting wrapped key from aks
no user bag found for UID %d
MKBUserSessionVolumeMounted
-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke_2
-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]
_DSEUN
KBSetCookie
Unable to load wipe info: %08x
MKBBackupOpen
MKBUserSessionFirstLoginEndTime
-[MKBKeyStoreDevice stashCreateWithSecret:withMode:withUID:WithFlags:]_block_invoke_2
-[MKBKeyStoreDevice forgottenPasscodeEvent]_block_invoke_2
MKBEventsRegister
Other
Can't create file to restore to (class: %d): %s
looking for ekwk, crypto_id 0x%016qx (%d of %u)
UMUserSessionConfigureLoginWindow
loaded bag handle %ld as session bag for %d, but got no session handle back: 0x%x
Could not open %s: %s
invalid timestamp
Can't create key
Failed to shrink %s to %lld: %s
seting APFSVolumeID For KeyBag 
-[MKBKeyStoreDevice isKeyRollingWithKeyStatus:]_block_invoke
WipeKeyUpdatePending
Failed to validate keybag file: %d
_MKBIV
MKBUserUnlockedSinceBoot
Failed to construct tweak key fixed data
v16@?0@\"NSError\"8
v20@?0i8@\"NSError\"12
invalid count
Failed to allocate Cookie malloc space
SBTransient
MKBForegroundUserSessionID
-[MKBKeyStoreDevice passcodeUnlockFailed]_block_invoke_2
_DTTR
Wipe Info ID is wrong: %d
failed to migrate skey, opts: %u
CCCryptorUpdate() failed:%d\n
key class %d
Failed to construct data key fixed data
extent = %llu bytes
/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
OpaqueStuff
single
Oh no! Can't save wipe ID
MKBKeyBagKeyStashEnableWithOpts
Prompted to SE enroll
FailedUnlockAttempts
cant add
could not rename %s to %s: %s
KBSecureSaveObjectWithCrypto
storeWipeIDInfo
MKBAssertionTimeout
/var
CCCCryptorFinal() failed:%d\n
Failed to get bag uuid
truncated key size: %zd
Failed to unlock in-kernel backup bag: 0x%08x
ftruncate() failed
cryptoId
got extent size %llu, keysize %d
MKBUserSessionQuotaSoftLimit
Port:%d has RECEIVERIGHT
health plist doesnt exist or wrong version, creating new one
MKBKeyBagKeyStashLoadWithOpts
setAPFSVolumeIDForKeyBag
-[MKBKeyStoreDevice createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:]_block_invoke
invalid fail indicator
plist data tests
Failed to get keybag persona Cookiefrom AKS:0x%x
KBSecureSaveObject
dbError
HealthPlistAddToData
%d
BackupKeyBagKeys
mount is with NO CPROTECT:0x%x on  (%s)
CameraOnLockScreen
v24@?0@\"NSDictionary\"8@\"NSError\"16
MKBKeyBagKeyStashDestroy
MementoBlobMaxUnlockAttempts
unlocked bag %d
found rewrapped key in MKB backup db
Failed to find UMUserSessionSwitchToLoginWindow in UM
Failed to unwrap dict blob with classF
com.apple.mobile.keybagd.user_started
IODeviceTree
aks_wrap_key error class: %d (%d) result: %d
UserSwitchTaskUUID
failed to get fds(1) with error:%s
KBMapDeviceBag
KBLoadLoadKeyBagFile
unlink failed: %s
%s: %s
aks_get_configuration result: %d\n
__MKBAssertionFinalize
Failed to find UMUserSessionSetSecureBackupBlob in UM
UMUserSessionDeleteSecureBackupBlob
result = %d
AKS can't create bag: %08x
MKBUserSessionLogoutStartTime
APFSIOC_GET_CRYPTO_IDS fail
-[MKBKeyStoreDevice changeSystemSecretFromOldPasscode:ToNew:withOpaqueData:withParams:]_block_invoke
-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke
-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke_2
-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]_block_invoke
 Empty Keybag returned from KBLoadLoadKeyBagFile
Got opaqueStuff from ondisk keybag
MementoBlobState
RemoteProfile
MKBBackupValidateKeyUUID
MKBUserSessionWrapSession
log_port_type
invalid ttr timestamp
Failed to resolve gAPFSVolumePayloadGet
%02x
backup key from db too large (%zu > %zu), ignoring
MKBUserSessionAuditor
cant create dict
MKBUserUnlockedSinceBoot for user(%d) fails with error(%d), returning 0
-[MKBKeyStoreDevice loadSyncBagForUserSession:withSessionUID:]_block_invoke
KBSaveUserBagHandle
no-effaceable-storage
Error from aks_backup_copy_current_bag_uuid: %d
copy_rewrapped_key_from_file
MKBUserSessionConfigureLoginWindow
-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]_block_invoke
got error from remote proxy(2): %ld
IOGeneralInterest
:/filesystems
hw.osenvironment
-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]_block_invoke
Deleted System KeyBag plist
RestoreFromBackup
found extent-based key_blob, size %zu
-[MKBKeyStoreDevice loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:]_block_invoke
time stamp is of wrong type
fileIV to wipeIV mismatch, no payload returned
sw
handleToUse_block_invoke
MKBFileWriteTranscrypt
MKBUserSessionRetrieveSecureBackupBlob
MKBUserSessionFirstLoginStartTime
MKBUserSessionLogoutEndTime
Could not get %s volume attributes (errno=%d)
MKBKeyBagKeyStashCommitWithOpts
BackupKey uuid mismatch
MKBOTABackupBagOpen
MKBDeviceModeSingleUser
-[MKBKeyStoreDevice passcodeUnlockSuccess]_block_invoke
%s%s/%s.kb
Attribute buffer too small. offset=%d, lenght=%u
Unable to load keybag with Crypto: %d
Can't create key data
MKBOTABackupBagCopyUUID
PointsOfInterest
Failed to construct data key
-[MKBKeyStoreDevice passcodeUnlockSuccess]_block_invoke_2
uld time stamp is of wrong type
IODeviceTree:/options
KBMapVolume
Failed to  obtain cookie from the volume with error %d
mount point (%s) does not support Data Protection
bag uuid mismatch (%s != %s)
MKBCopyCryptoIDKeysForFileDescriptor
MKBUserSessionSwitchToLoginWindow
APFSVolumePayloadSet failed with %d
manifest is of wrong type %lu
[%d] crypto_id = 0x%016llx, extent_size = %llu, key class = %u, bag uuid = %s
log_blob
MKBUserSessionUnloadSessionBags
MKBUserSessionGroupID
MKBUserSessionVolumeFSType
create_mutable_dict
AppleEffaceableStorage
nbytes = %zd, bytes_read = %zd
Failed to find UMUserSessionRetrieveSecureBackupBlob in UM
MKBUserSessionDeleteSecureBackupBlob
com.apple.mobile.keybagd.passcode_threshold
IsPermanentlyBlocked
got error from remote proxy: %@
Failed to allocate page aligned buffer
-[MKBKeyStoreDevice _CreateMKBServerConnection]
-[MKBKeyStoreDevice setVolumeToPersona:withPersonaString:]_block_invoke
countdown
dropping lock assertion for: handle:%d, type:%d, status:%d
CCCryptorUpdate() failed: %d\n
MKBUserSessionAPNSID
-[MKBKeyStoreDevice deleteKeybagForUserSession:]_block_invoke
-[MKBKeyStoreDevice createSyncBagForUserSession:withSessionUID:]_block_invoke
Can't store blastable bytes: %08x
failed to open_dprotected_np(%s): %s
found sparse extent (%d of %u)
Can't load blastable bytes: %08x
_DFAIL
ttr time stamp is of wrong type
systembag
entry overruns blob offset=%zu keysize=%u blob_size=%zu
Can't set key class to %d: %s
UMUserSessionListSyncMachServices
MKBUserSessionUnWrapSession
12A123
plist ttr tests
%s/%s
Status missing from response
com.apple.MobileKeyBag
Failed to dlopen UserManagement.framework
IsWipePending
Could not create %s: %s
Can't find EffaceableStorage kext!
version is invalid
failed to get data
invalid uld timestamp
Failed to get cstring from uuidString
Could not write to %s: %s
-[MKBKeyStoreDevice stashCreateWithSecret:withMode:withUID:WithFlags:]_block_invoke
-[MKBKeyStoreDevice stashVerifywithValidity:WithUID:WithFlags:]_block_invoke_2
HealthPlistSetTTR
_MKBPAYLOAD
ExtendedDeviceLockState
failed to get uuid for handle %d
found single-extent key_blob, size %zu
Failed to get multiuser_config flags from kernel with error:%d
MKBUserTypeKey
-[MKBKeyStoreDevice stashDestroy]_block_invoke
HealthPlistSetLockDate
-[MKBKeyStoreDevice migrateFS]_block_invoke
-[MKBKeyStoreDevice createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:]
failed to add interest notification
cant set version
KBUpdateKeyBag
MKBGetDeviceConfigurations failed to return a dictionary
UseMementoBlob
%s (%d):\n
CCCryptorFinal() failed: %d\n
no keybag in user bag plist
-[MKBKeyStoreDevice SeshatDebug:]_block_invoke
at capacity, forgetting oldest data entry
no time
change-secret failed %x
MKBAssertion
MKBUserSessionIsLoginSession
MKBUserSessionLibinfoHomeDir
failed to allocate memory for event callback
mkb events
addition of uld failed
trying to store invalid iv or secret
MKBBackupValidateKey
Unwrapped userland backup bag
_MKBDeviceSetGracePeriod
MKBUserSessionFileInfo
HealthPlistConsumeTTR
KBChangeSystemNonSeSecret
Saved new keybag for handle %d with result %d
Protection class changed from %d to %d
MKBKeyBagCopyUUID
existingKeyError
15A123
%s missing payload
Error prewarming SPSs: %d
Bag uuid mismatch, ignore
-[MKBKeyStoreDevice SeshatDebug:]_block_invoke_2
HealthPlistSetUnlockDate
no TTR entry
Failed to get keybag Cookie from AKS:0x%x
_MKBKeyBagKeyStashSetManifest
TimeMachine
backup key doesn't match current bag uuid!!
MKBUserTypeDeviceMode
Failed to parse to uuid_t
aks_unlock_bag() returned %d
Failed to find UMUserSessionListSyncMachServices in UM
Cannot find proper VolumeUUID String to remove personakey with volume unmap
Could not open the stream
Could not create object from stream
failed to copy health plist
ls
Failed to pread(%zu, %llu) from %s (%s)
PolicyUID
-[MKBKeyStoreDevice getLockStateForUser:]_block_invoke_2
Failed to resolve gAPFSVolumePayloadSet
DeviceHandle
remaining blob size too short offset=%zu blob_size=%zu
-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke
MKBDeviceUnlockedSinceBoot
device-recovery
-[MKBKeyStoreDevice passcodeUnlockStart]_block_invoke_2
kCommandSeshatUnlock -> %d
got error from remote proxy: %d
MKBAssertionKey
Failed to initialize crypto_buffer
MKBUserSessionOpaque
-[MKBKeyStoreDevice forgottenPasscodeEvent]_block_invoke
failed to copy block
cant allocate mem
storeBlastableBytes
ld time stamp is of wrong type
plist build tests
Can't create cryptor: %d
MKBUserSessionLoadKeybagForUser
key_class_f wrap Completed with size %d
Invalid Blob entry for wrap
Saving SystemBag with NO EFFACEABLE ROLL
IONVRAM-DELETE-PROPERTY
Unable to load keybag with No Crypto: %d
MKBBackupCreateFromFileDescriptors
key found in db doesn't match current backup bag!!
Failed to find UMUserSessionForegroundSession in UM
MKBUserSessionType
plist timestamp tests
Statfs failed due to:%s on  (%s)
SiriOnLockScreen
Failed to unwrap key (%p,%d) in class %d with keypair: 0x%08x
UMUserSessionIsLoginSession
MKBUserSessionRequiresPasscode
MKBUserSessionReqTotalUsers
com.apple.mobile.keybagd.xpc
HealthPlistSetVersion
Can't load secure keybag Object: %d
Can't load wipe info for ID:%08x
result = %d, (uid:%u, flags:0x%x)
MementoBlobSeSlot
addition of TTR failed
KBSaveSystemBagHandle
MementoBlobFailedAttempts
F_PUNCHHOLE failed on %s for range (%lld:%llu): %s
-[MKBKeyStoreDevice removeSyncBagForUserSession:withSessionUID:]_block_invoke
failed to validate newly created bag -- should never happen
bytes_read(%zd) not multiple of encryption block size
Failed to unload session keybags: 0x%x
MKBUserSessionQuotaLimit
_apfs_copy_wrapped_key_from_file
kCommandSeshatRecover -> %d
plist failure tests
failed to allocate handle
true
Can't serialize dictionary
v24@?0@\"NSData\"8@\"NSError\"16
-[MKBKeyStoreDevice getLockStateForUser:]_block_invoke
Could not save value:%08x
MKBFileReadTranscrypt
copy_rewrapped_key_from_existing_key
UMUserSessionSetSecureBackupBlob
TimeUntilUnblockedSinceReferenceDate
load_binary_dict
_apfs_get_all_crypto_ids
%s/%s.kb
-apfs_shared_datavolume
crypto_id mismatch (0x%016llx != 0x%016llx)
UMUserSessionForegroundSession
MKBUserSessionUUID
Could not create dictionary from stream
Unable to save wipe info: %08x
fileError
com.apple.mobile.usermanagerd.foregrounduser_changed
MKBDeviceModeKey
empty time
Unable to load %s
%s missing IV
extent count mismatch i=%d, count=%d, offset=%zu, key_blob_size=%zu
key is of wrong type
no
uuid_parse SUCCESS
StashBagValidOnDisk
StashStagedManifest
MKBKeyBagUnlock
HealthPlistTest
Could not get options entry from the device tree
bytes_read(%ld) < read_size(%ld), but effective_start(%lld) + read_size(%ld) <= file_size(%lld)\n
MKBCurrentSyncBubbleSessionID
-[MKBKeyStoreDevice passcodeUnlockFailed]_block_invoke
-[MKBKeyStoreDevice removePersonaKeyForUserSession:withPersonaUUIDString:withVolumeUUIDString:]_block_invoke
aksNotificationCB
_DDATA
APFSVolumePayloadSet
UMUserSessionLoadWithPasscode
MKBForegroundUserSession
MKBUserSessionLoginTimeStamp
MKBUserSessionVolumeUUID
create_dict
could not rename %s to %s: %s (%d)
System KeyBag plist still contains keys! Not xART based! Do not delete!
failed to fstat encryptedfd(%d): %s
Prewarming SPSs with %@
com.apple.mobile.keybagd.lock_status
MKBUserSessionForeground
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
-[MKBKeyStoreDevice passcodeUnlockStart]_block_invoke
fail indicator is of wrong type
Can't serialize object
MKBKeyBagKeyStashSupport
Failed to find UMCurrentSyncBubbleSessionID in UM
MKBUserSessionCreateTimeStamp
-[MKBKeyStoreDevice disableBackupForVolume:]_block_invoke
HealthPlistCopyOrCreateNew
Saving UserBag for uid %d with EFFACEABLE ROLL
unable to save bag %d
Can't allocate decryption buffer
Data to Wrap with length:%d
/System/Library/PrivateFrameworks/APFS.framework/APFS
corrupt blob size %zu, expected at least %zu
realloc failed
_DLD
:/defaults
Can't create crypt buffer
convertBinaryToObject
GracePeriod
MKBBackupCopyBackupBagUUIDForVolume
should_use_memento
MKBUserSessionTotalDataSize
Port:%d has DEADNAME
-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke
state
read() failed:%s\n
sessionblob length:%ld
MKBUserSessionAlternateUUID
AppleKeyStore
Can't create iv data
xts mode
FAILED to MKBUserTypeDeviceMode, EPERM
unexpected ld entry
plist lockdate tests
content-protect
dt = %d, bootarg = %d
got oversized key (%u > %zu) for crypto id 0x%016qx
KBSecureLoadObject
_MKBKeyBagCreateSystem does nothing, returning success
buffer size %zu not a multiple of %d\n
Failed to find UMUserSessionConfigureLoginWindow in UM
From EARLYSTART skip check switch between users
UserSessionManagedDevice
UserSwitchTaskPID
set-system failed %d
KBSecureLoadObjectWithCrypto
fa
result = %d, (handle:%d)
allocate_page_aligned_buffer
MKBUserSessionHomeDir
store_binary_dict_fd
-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke
invalid ld timestamp
create_string
kcreateKeybagForUserSession -> %d
plist unlock date tests
handle:%d, asserttype:%d, timeout:%llu, result:%d, ioret: 0x%x, ret:%d
failed to stat(%s): %s
extent_size mismatch (%llu != %llu)
verify_only_opt
found %d extent%s
open(%s) failed: %s
-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]_block_invoke
no version
aks_change_secret_epilogue() failed %x
first manifest
MKBUserSessionListSyncMachServices
MKBUserSessionEachUserSize
Can't create IV
MaxUnlockAttempts
Port:%d has SENDRIGHT
failed to find %s service
missing version
unexpected TTR entry
%s%s
Saving SystemBag with EFFACEABLE ROLL
<MKBAssertion %p [%p]> { AssertionType '%@' (%d), Assertion Retain: (%d)
failed to set bag handle %d as session bag for UID %d: 0x%x
PolicyIndex
UserSessionOther
userbag
Unable to fsync %s: %s
xts ans kdf2 mode
Failed to construct tweak key
MKBUserSessionQuotaUsed
MKBUserSessionTotalUsers
UserSwitchTaskReason
is_device_in_device_recovery_environment_block_invoke
_create_plist_with_version
APFSVolumePayloadGet failed with %d
Could not map %s volume (ret=%d)
%d: %s\n
MKBUserSessionID
DeviceNetworkBG
APFSVolumePayloadSet succeeded
_MKBKeyBagChangeSystemSecretOpts
UserVolumeAPFSConverted
-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]_block_invoke
-[MKBKeyStoreDevice startBackupSessionForVolume:]_block_invoke_2
-[MKBKeyStoreDevice loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:]
KBisxARTBasedKeyBag
validateSecureFile
MKBKeyBagKeyStashCreateWithOpts
VerifyOnly
got zero-length key for non-sparse crypto id
KBMapDeviceBag failed with error %d
Could not create stream from serialized data
-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]
MKBBackupCopyBackupBagUUIDForBag
Bag uuid mismatch
Failed to find UMUserSessionIsLoginSession in UM
Failed to get cstring from volumePath
-[MKBKeyStoreDevice SetSystemSecretBlob:]_block_invoke
/var/root/.mkb_seshat_health
-[MKBKeyStoreDevice copySytemSecretBlob]_block_invoke_2
Keybag %s doesn't actually contain keys
odd blob size %zu
Could not read %s: %s
Failed to delete System KeyBag plist: %s
Saving UserBag for uid %d with NO EFFACEABLE ROLL
MementoSupported
MKBFileCopyWrappedKey_OTA
Bad key passed in, does not validate
MKBUserTypeEphimeral
UserVolumeHFSPlus
load_binary_dict_from_buffer
data inconsistent
MKBKeyBagKeyStashPersistWithOpts
result = %d, (handle: %d)
Failed to pwrite(%lu, %llu) from %s
-[MKBKeyStoreDevice stopBackupSessionForVolume:]_block_invoke_2
KeyBagKeys
get_lock_state() -> 0x%x
Unable to load wipe info:%08x
kern.bootargs
MKBBackupValidateBackupKeyWithUUID
whoa, cryptoID does not match backup_key.inode: %llu vs %llu
MKBUserSessionSyncMachServices
-[MKBKeyStoreDevice stashVerifywithValidity:WithUID:WithFlags:]_block_invoke
bytes_read(%lu) != bytes_written(%lu)
%s/%s/%s.kb
unexpected uld entry
temp handle is invalid: %d
failed to open ondisk keybag, failing UpdateKeyBag
failed to close(%d): %s
Invalid assertion type
Buffer size %zu not multiple of %d\n
copy_rewrapped_key_from_db
MKBUserSessionLoadWithPasscode
e-apfs
Can't get crypto keys for inode %llu (fd %d): %s
MKBPrewarmSPS
false
UMUserSessionSwitchToLoginWindow
KBMapDeviceBag Success
MKBUserSessionSyncTasks
failed to write to pipe with error:%s
Failed to open APFS framework
Retrieved keybag persona Cookie from AKS, setting in APFS volume
BackOffDelay
MKBDeviceLockAssertion
Unknown trailer blob
Failed to deallocate page aligned buffer
failed to load bag for user %d: 0x%x
Successfully obtained the cookie for the volume with length:%zd
Can't create decryptor: %d
has_data_protection
MKBUnlockDeviceForACMRef
MKBUserSessionSetSecureBackupBlob
MKBUserSessionLanguage
got error from remote proxy for getPasscodeBlobWithReply: %ld
-[MKBKeyStoreDevice SetSystemSecretBlob:]_block_invoke_2
cant set time
two
params = %d
MKBUserSessionSetVolumeToPersona
UserSwitchTaskMachService
Out of Memory!!! Dying!...so...cold....
Port:%d has SENDONCERIGHT
LockDeviceNow
file size %lld bytes
cbc mode
cant get version
invalid version format
handle is of wrong type
__MKBBackupDecryptInPlace
invalid context %d %d
/private/var/
APFSVolumePayloadGet
Unable to finalize: %d
s
UserVolumeAPFSNative
-[MKBKeyStoreDevice stashCommit:WithFlags:]_block_invoke
-[MKBKeyStoreDevice verifySyncBagForUserSession:withSessionUID:]_block_invoke
boff
MKBBackupPread
file cannot be larger than backup
Could not get the backup key for crypto ID 0x%016qx (%d of %u, existing keys: %s, found1:%d, found2:%d, found3:%d)
Found target crypto_id
failed to key_class_f wrap by aks_wrap_key: 0x%x
MKBUserSessionDirty
MKBUserSessionSystemLoginSize
Result = %d
KBSaveKeyBag
MKBDeviceUnlockedSinceBoot fails with error(%d) for handle(%d) with AKS error(%d)
Failed to load in-kernel backup bag: 0x%08x
MobileKeyBagError
MKBUserSessionHasSyncBag
-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke_2
-[MKBKeyStoreDevice stopBackupSessionForVolume:]_block_invoke
pread() failed: %s\n
aks_backup_rewrap_key() failed: %d
Failed to unwrap key (%p,%d) in class %d with handle %d: 0x%08x
MKBDeviceSupportsEnhancedAPFS
loadWipeIDInfo
MKBKeyBagCleanupAfterMigration
MKBKeyBagHandle
_MKBKeyBagCreateSystem
disk
-[MKBKeyStoreDevice unloadSyncBagForUserSession:withSessionUID:]_block_invoke
failed to consume TTR entry
non-current version %d
welp, unable to persist old bag
Could not create string for value
KeyBagVersion
MKBFileCreateForRestore
_MKBBackupCheckKey
-[MKBKeyStoreDevice getDeviceLockStateForUser:extendedState:withLockStateInfo:]_block_invoke
MKBDeviceSetGracePeriod(acm:%d): To (%lld)AKS return Value is %d\n
}
-[MKBKeyStoreDevice Event:]_block_invoke
getNVRam
failed to fetch measurement\n
failed to allocate backup bag handle
Skipping enrollment
Data to Wrap is NULL
Updating VolumeUUID %@
MKBUserSessionPreviousLoggedinID
Port:%d has NORIGHTS
aks_set_keybag_for_volume_with_cookie_persona FAIL with 0x%x
MKBFileReadEncrypted
Can't save the bag: %d
yes
FAILED to MKBUserTypeDeviceMode, EINVAL
-[MKBKeyStoreDevice startBackupSessionForVolume:]_block_invoke
Failed to get backup bag uuid for volume: %x
Could not allocate buffer
-[MKBKeyStoreDevice isKeyRollingWithKeyStatus:]_block_invoke_2
failed to create notification port for AKS
unable to allocate
12A124
plist version tests
loadBlastableBytes
Manifest
Buffer size %zu not multiple of %zu\n
%s already exists
Failed to find UMUserSessionDeleteSecureBackupBlob in UM
MKBUserSessionLoginUser
Could not fstat %s: %s
efface failed: 0x%x
LastWipeKeyUpdateTimeStamp
changing non-SE passcode %s phase, (params:%d)
KeybagxART
pb
Failed to truncate %s to %lld
unexpected contents
KBLoadUserKeybag
%s missing wipeID
v8@?0
PolicyAuditToken
aks_set_keybag_for_volume_with_cookie FAIL with 0x%x
MKBUserSessionisTransient
MKBUserSessionCachedLoginStartTime
-[MKBKeyStoreDevice stashDestroy]_block_invoke_2
SkipSE
Couldn't allocate work buffer of %zu bytes\n
deallocate_page_aligned_buffer
odd blob size %zu, offset = %zu
Failed to find UMUserSessionLoadWithPasscode in UM
FailedPasscodeAttempts
-[MKBKeyStoreDevice copySytemSecretBlob]_block_invoke
Can't get volume uuid for fd %d: %s
looking for backup key for crypto_id 0x%016qx (%d of %u)
Invalid Blob entry for unwrap
create_array
mismatch
memento verifiers and acm context are unsupported
MKBUserSessionCloudLoginTimeStamp
MKBUserSessionVolumeDeviceNode
bad arguments
build is of wrong type
aks_set_keybag_for_volume_with_cookie SUCCESS
passcode and acm are mutually exclusive
MKBFileCopyWrappedKey
_get_userid_from_options
Can't set the system bag: %08x
com.apple.mobile.keybagd.user_changed
UserSwitchTaskName
fstat() failed:%s\n
```
