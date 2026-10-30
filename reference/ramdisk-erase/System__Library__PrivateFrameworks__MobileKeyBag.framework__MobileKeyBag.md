# `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 353,328 bytes.

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
WipeKeyUpdatePending
StashBagValidOnDisk
RemoteProfile
extent_size mismatch (%llu != %llu)
Error from aks_backup_copy_current_bag_uuid: %d
odd blob size %zu
plist data tests
plist unlock date tests
KeyBagKeys
IODeviceTree:/options
Failed to get keybag persona Cookiefrom AKS:0x%x
looking for backup key for crypto_id 0x%016qx (%d of %u)
deCryptnextsession: session decrypt length:%d(expected: 32)
MKBFileWriteTranscrypt
existingKeyError
com.apple.mobile.keybagd.user_changed
_DSEUN
KeyBagVersion
MKBKeyBagKeyStashDestroy
MKBCopyCryptoIDKeysForFileDescriptor
Failed to find UMUserSessionRetrieveSecureBackupBlob in UM
UserVolumeAPFSNative
v24@?0@\"NSDictionary\"8@\"NSError\"16
-[MKBKeyStoreDevice stashCreateWithSecret:withMode:withUID:WithFlags:]_block_invoke
storeBlastableBytes
result = %d, (handle: %d)
MKBDeviceLockAssertion
MKBUserSessionRetrieveSecureBackupBlob
MKBUserSessionCloudLoginTimeStamp
MKBUserTypeEphimeral
kcreateKeybagForUserSession -> %d
%s%s/%s.kb
KBSecureLoadObjectWithCrypto
failed to open_dprotected_np(%s): %s
-[MKBKeyStoreDevice unloadKeybagForUserSession:]_block_invoke
HealthPlistSetLockDate
no version
build is of wrong type
failed to allocate backup bag handle
Failed to get multiuser_config flags from kernel with error:%d
%02x
plist lockdate tests
KBSaveSystemBagHandle
Can't create key
sep measurement
MKBUserSessionConfigureLoginWindow
loadBlastableBytes
%s/%s.kb
has_data_protection
fa
Invalid assertion type
buffer size %zu not a multiple of %d\n
MKBUserSessionGroupID
-[MKBKeyStoreDevice disableBackupForVolume:]_block_invoke_2
copy_rewrapped_key_from_existing_key
Can't create %s: %s
OverrideMemento
%s already exists
Error: %@
version is invalid
unexpected ld entry
aks_set_keybag_for_volume_with_cookie SUCCESS
corrupt blob size %zu, expected at least %zu
open(%s) failed: %s
extent = %llu bytes
UserVolumeHFSPlus
KBSaveUserBagHandle
failed to migrate skey, opts: %u
MKBKeyBagKeyStashLoadWithOpts
MKBCurrentSyncBubbleSessionID
MKBUserSessionLoadKeybagForUser
no keybag in user bag plist
Unable to load wipe info:%08x
Bag uuid mismatch
store_binary_dict_fd
-[MKBKeyStoreDevice getDeviceLockStateForUser:extendedState:withLockStateInfo:]_block_invoke
key is of wrong type
_MKBVerifyPasswordWithContext
SkipSE
Unknown trailer blob
Keybag %s doesn't actually contain keys
LastWipeKeyUpdateTimeStamp
setNVRam
ls
MKBBackupCopyBackupKeyUUID
efface failed: 0x%x
result = %d, (handle:%d)
MementoBlobFailedAttempts
MKBUserSessionCreateTimeStamp
MKBUserSessionVolumeMounted
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
-[MKBKeyStoreDevice stashCommit:WithFlags:]_block_invoke
Can't store blastable bytes: %08x
Saving UserBag for uid %d with EFFACEABLE ROLL
MKBDeviceSupportsEnhancedAPFS
PointsOfInterest
CCCryptorUpdate() failed:%d\n
Can't get volume uuid for fd %d: %s
-[MKBKeyStoreDevice stashDestroy]_block_invoke
MKBEventsRegister
fileIV to wipeIV mismatch, no payload returned
Failed to get bag uuid
deallocate_page_aligned_buffer
false
invalid ld timestamp
_MKBIV
failed to fetch measurement\n
CameraOnLockScreen
From EARLYSTART skip check switch between users
failed to copy health plist
aks_set_keybag_for_volume_with_cookie_persona FAIL with 0x%x
_MKBPAYLOAD
aks_prederived_unlock_keybag() returned %d
aks_unlock_bag() returned %d
params = %d
found single-extent key_blob, size %zu
failed to load bag for user %d: 0x%x
unexpected contents
aks_set_keybag_for_volume_with_cookie FAIL with 0x%x
got zero-length key for non-sparse crypto id
MKBUserSessionName
UserVolumeAPFSConverted
_apfs_copy_wrapped_key_from_file
-[MKBKeyStoreDevice _CreateMKBServerConnection]
-[MKBKeyStoreDevice stashCreateWithSecret:withMode:withUID:WithFlags:]_block_invoke_2
HealthPlistTest
pb
found rewrapped key in MKB backup db
Failed to truncate %s to %lld
UMUserSessionForegroundSession
Port:%d has RECEIVERIGHT
bad arguments
unexpected uld entry
s
-[MKBKeyStoreDevice passcodeUnlockFailed]_block_invoke
-[MKBKeyStoreDevice setVolumeToPersona:withPersonaString:]_block_invoke
OpaqueStuff
cant create dict
ld time stamp is of wrong type
Oh no! Can't save wipe ID
state
<MKBAssertion %p [%p]> { AssertionType '%@' (%d), Assertion Retain: (%d)
CCCryptorFinal() failed: %d\n
Can't set key class to %d: %s
boff
Failed to allocate page aligned buffer
MobileKeyBagError
cryptoId
bytes_read(%lu) != bytes_written(%lu)
MKBUserSessionHomeDir
MKBUserSessionEachUserSize
MKBDeviceModeKey
HealthPlistSetUnlockDate
/System/Library/PrivateFrameworks/APFS.framework/APFS
Can't create key data
truncated key size: %zd
uuid_parse SUCCESS
load_binary_dict_from_buffer
-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke_2
failed to create notification port for AKS
failed to open ondisk keybag, failing UpdateKeyBag
Failed to resolve gAPFSVolumePayloadGet
KeybagxART
Unable to finalize: %d
handle:%d, asserttype:%d, timeout:%llu, result:%d, ioret: 0x%x, ret:%d
backup key doesn't match current bag uuid!!
MKBUserSessionReqTotalUsers
ttr time stamp is of wrong type
Failed to delete System KeyBag plist: %s
Successfully obtained the cookie for the volume with length:%zd
%s: %s
Found target crypto_id
key_class_f wrap Completed with size %d
MKBUserSessionAuditor
Could not create object from stream
found %d extent%s
Could not create stream for serialized data
-[MKBKeyStoreDevice getFileHandleForData:]
-[MKBKeyStoreDevice backupUUIDForVolume:bagUUID:]_block_invoke
invalid uld timestamp
storeWipeIDInfo
failed to stat(%s): %s
MKBUserSessionForeground
HealthPlistCopyOrCreateNew
data inconsistent
fstat() failed:%s\n
Can't get crypto keys for inode %llu (fd %d): %s
Buffer size %zu not multiple of %d\n
MKBUserSessionSetVolumeToPersona
-[MKBKeyStoreDevice forgottenPasscodeEvent]_block_invoke_2
no TTR entry
log_blob
CCCCryptorFinal() failed:%d\n
copy_rewrapped_key_from_file
-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]_block_invoke
HealthPlistAddToData
MKBDeviceUnlockedSinceBoot
MKBFileReadEncrypted
failed to fstat encryptedfd(%d): %s
Skipping enrollment
failed to set bag handle %d as session bag for UID %d: 0x%x
MKBUserSessionQuotaSoftLimit
Port:%d has NORIGHTS
_DVERS
1
Unable to save wipe info: %08x
should_use_memento
UMUserSessionLoadWithPasscode
Cannot find proper VolumeUUID String to remove personakey with volume unmap
MKBUserSessionLogoutStartTime
MKBUserSessionSystemLoginSize
MKBBackupCopyBackupBagUUIDForBag
read() failed:%s\n
v24@?0@\"NSData\"8@\"NSError\"16
got error from remote proxy(2): %ld
welp, unable to persist old bag
MKBKeyBagKeyStashSupport
Failed to get cstring from volumePath
-[MKBKeyStoreDevice forgottenPasscodeEvent]_block_invoke
IOGeneralInterest
15A123
MKBUserSessionRemovePersonaKeyForUser
MKBUserSessionQuotaLimit
-[MKBKeyStoreDevice isKeyRollingWithKeyStatus:]_block_invoke
set-system failed %d
MKBFileCopyWrappedKey_OTA
KBMapDeviceBag failed with error %d
Could not create %s: %s
-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]
-[MKBKeyStoreDevice createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:]
/private/var/
content-protect
could not rename %s to %s: %s
Can't create crypt buffer
MementoBlobSeSlot
%d: %s\n
IsWipePending
FailedPasscodeAttempts
Could not map %s volume (ret=%d)
seting APFSVolumeID For KeyBag 
failed to key_class_f wrap by aks_wrap_key: 0x%x
log_port_type
fail indicator is of wrong type
MKBBackupOpen
failed to get uuid for handle %d
handleToUse_block_invoke
_MKBKeyBagCreateSystem
-[MKBKeyStoreDevice copySytemSecretBlob]_block_invoke
-[MKBKeyStoreDevice passcodeUnlockStart]_block_invoke
-[MKBKeyStoreDevice getDeviceLockStateForUser:extendedState:withLockStateInfo:]_block_invoke_2
MKBFileCopyWrappedKey
Failed to unwrap key (%p,%d) in class %d with keypair: 0x%08x
MKBUserSessionFirstLoginStartTime
MKBUserSessionLogoutEndTime
v20@?0i8@\"NSError\"12
_DULD
Can't allocate decryption buffer
MementoBlobState
/var
MKBBackupValidateKeyUUID
_get_userid_from_options
getting wrapped key from aks
Failed to dlopen UserManagement.framework
no time
KBMapDeviceBag
Unable to load keybag with Crypto: %d
result = %d (stash_mode:%d, uid:%d, flags:0x%x)
aks_wrap_key error class: %d (%d) result: %d
MKBUserTypeDeviceMode
FailedUnlockAttempts
Could not allocate buffer
cant add
Attribute buffer too small. offset=%d, lenght=%u
MKBBackupCopyBackupBagUUIDForVolume
Failed to construct tweak key
UMUserSessionConfigureLoginWindow
loaded bag handle %ld as session bag for %d, but got no session handle back: 0x%x
kCommandSeshatUnlock -> %d
-[MKBKeyStoreDevice removePersonaKeyForUserSession:withPersonaUUIDString:withVolumeUUIDString:]_block_invoke
uld time stamp is of wrong type
MKBPrewarmSPS
PolicyAuditToken
invalid context %d %d
failed to close(%d): %s
 Empty Keybag returned from KBLoadLoadKeyBagFile
Port:%d has DEADNAME
Can't create cryptor: %d
KBSecureSaveObject
addition of uld failed
Not cookie in this volume, attempting to write it
result = %d
BackupKey uuid mismatch
__MKBAssertionFinalize
key class %d
at capacity, forgetting oldest data entry
health plist doesnt exist or wrong version, creating new one
Result = %d
Can't serialize object
System KeyBag plist still contains keys! Not xART based! Do not delete!
MKBFileWriteEncrypted
MKBUserSessionListSyncMachServices
MKBUserSessionQuotaUsed
addition of ld failed
APFSVolumePayloadSet
failed to validate newly created bag -- should never happen
RestoreFromBackup
verify_only_opt
device-recovery
-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke_2
kCommandSeshatRecover -> %d
sysctl(hw.osenvironment) -> %d
-[MKBKeyStoreDevice getLockStateForUser:]_block_invoke
-[MKBKeyStoreDevice createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:]_block_invoke
-[MKBKeyStoreDevice loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:]_block_invoke
mkb events
temp handle is invalid: %d
MKBUserSessionDisabled
-[MKBKeyStoreDevice changeSystemSecretFromOldPasscode:ToNew:withOpaqueData:withParams:]_block_invoke
-[MKBKeyStoreDevice passcodeUnlockSuccess]_block_invoke_2
unable to save bag %d
Can't load secure keybag Object: %d
MaxUnlockAttempts
Can't set the system bag: %08x
Port:%d has SENDRIGHT
cant get version
Wipe Info ID is wrong: %d
Buffer size %zu not multiple of %zu\n
_MKBKeyBagCreateSystem does nothing, returning success
aks_backup_rewrap_key() failed: %d
TimeUntilUnblockedSinceReferenceDate
-[MKBKeyStoreDevice startBackupSessionForVolume:]_block_invoke_2
two
Unable to load keybag with No Crypto: %d
%s missing IV
GracePeriod
remaining blob size too short offset=%zu blob_size=%zu
FAILED to MKBUserTypeDeviceMode, EPERM
MKBForegroundUserSessionID
v16@?0@\"NSError\"8
setAPFSVolumeIDForKeyBag
MKBUserTypeKey
-[MKBKeyStoreDevice SeshatDebug:]_block_invoke_2
aksNotificationCB
/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
uuid_parse failed
cant set version
Manifest
Failed to find UMCurrentSyncBubbleSessionID in UM
PolicyIndex
userbag
_MKBWIPEID
-apfs_shared_datavolume
MKBOTABackupBagOpen
dropping lock assertion for: handle:%d, type:%d, status:%d
nbytes = %zd, bytes_read = %zd
-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke
trying to store invalid iv or secret
passcode and acm are mutually exclusive
Could not get options entry from the device tree
e-apfs
Unable to load wipe info: %08x
UMUserSessionDeleteSecureBackupBlob
MKBUserSessionType
_DTIME
Can't create dict
APFSVolumePayloadGet len reveived to be %zd
}
Saving UserBag for uid %d with NO EFFACEABLE ROLL
_MKBKeyBagChangeSystemSecretOpts
looking for ekwk, crypto_id 0x%016qx (%d of %u)
cbc mode
HealthPlistSetFailed
:/defaults
aks_set_keybag_for_volume_with_cookie_persona SUCCESS
KBSaveKeyBag
Failed to load in-kernel backup bag: 0x%08x
UserSessionOther
Port:%d has SENDONCERIGHT
-[MKBKeyStoreDevice stopBackupSessionForVolume:]_block_invoke
%s missing wipeID
Failed to find UMUserSessionLoadWithPasscode in UM
UserSessionManagedDevice
MKBUserTypePermanent
-[MKBKeyStoreDevice passcodeUnlockSuccess]_block_invoke
-[MKBKeyStoreDevice unloadSyncBagForUserSession:withSessionUID:]_block_invoke
-[MKBKeyStoreDevice removeSyncBagForUserSession:withSessionUID:]_block_invoke
-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]_block_invoke
cant allocate mem
Could not create string for value
Failed to resolve gAPFSVolumePayloadSet
crypto_id mismatch (0x%016llx != 0x%016llx)
UseMementoBlob
SiriOnLockScreen
Can't load blastable bytes: %08x
%s/%s
aks_get_configuration result: %d\n
MKBUserSessionFirstLoginEndTime
MKBUserSessionTotalUsers
Could not open %s: %s
APFSIOC_GET_CRYPTO_IDS fail
-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke
UMUserSessionSetSecureBackupBlob
_apfs_get_all_crypto_ids
-[MKBKeyStoreDevice Event:]_block_invoke
-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]
failed to get data
invalid timestamp
KBUpdateKeyBag
mount point (%s) does not support Data Protection
found sparse extent (%d of %u)
DeviceNetworkBG
IsPermanentlyBlocked
got error from remote proxy: %@
/var/root/.mkb_seshat_health
Deleted System KeyBag plist
MKBKeyBagCopyUUID
CCCryptorUpdate() failed: %d\n
failed to get fds(1) with error:%s
-[MKBKeyStoreDevice loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:]
Failed to validate keybag file: %d
Failed to construct data key
MKBUserSessionDeleteSecureBackupBlob
MKBUserSessionSyncTasks
MKBUserSessionHasSyncBag
Unwrapped userland backup bag
%s/%s/%s.kb
true
create_dict
com.apple.MobileKeyBag
no
invalid fail indicator
Could not get %s volume attributes (errno=%d)
Can't encrypt: %d
MKBDeviceGetGracePeriod
Prompted to SE enroll
-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]_block_invoke
unable to allocate
Saving handle 0 with the magic handle
MKBBackupPread
%s (%d):\n
offset = %zu, keysize = %u, extent size = %llu
UMUserSessionListSyncMachServices
com.apple.mobile.keybagd.passcode_threshold
MKBUserSessionDisplayName
got oversized key (%u > %zu) for crypto id 0x%016qx
got extent size %llu, keysize %d
invalid count
plist timestamp tests
get_lock_state() -> 0x%x
MKBUserSessionLoginUser
empty time
Unable to load %s
bag uuid mismatch (%s != %s)
MKBUnlockDeviceForACMRef
-[MKBKeyStoreDevice SetSystemSecretBlob:]_block_invoke_2
invalid version format
Got opaqueStuff from ondisk keybag
Can't create decryptor: %d
validateSecureFile
Can't load wipe info for ID:%08x
StashStagedManifest
Failed to find UMUserSessionSwitchToLoginWindow in UM
MKBForegroundUserSession
backup key from db too large (%zu > %zu), ignoring
AppleEffaceableStorage
cant set time
KBSecureLoadObject
yes
MKBUserSessionUUID
UserSwitchTaskPID
-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]_block_invoke
SBTransient
Prewarming SPSs with %@
%s missing payload
plist ttr tests
KBCleanupSystemKeyBag
no-effaceable-storage
Retrieved keybag Cookie from AKS, setting in APFS volume
Failed to  obtain cookie from the volume with error %d
ftruncate() failed
whoa, cryptoID does not match backup_key.inode: %llu vs %llu
loadWipeIDInfo
single
result = %d, (uid:%u, flags:0x%x)
MKBUserSessionSwitchToLoginWindow
MKBUserSessionUnloadSessionBags
MKBUserSessionOpaque
Unable to decrypt: %d
_MKBKeyBagKeyStashSetManifest
Can't serialize dictionary
manifest is of wrong type %lu
failed to determine whether we are multi-user: 0x%x
Failed to initialize crypto_buffer
Failed to find UMUserSessionListSyncMachServices in UM
Invalid Blob entry for wrap
-[MKBKeyStoreDevice SetSystemSecretBlob:]_block_invoke
-[MKBKeyStoreDevice passcodeUnlockStart]_block_invoke_2
change-secret failed %x
Failed to get keybag Cookie from AKS:0x%x
BackOffDelay
UMCurrentSyncBubbleSessionID
MKBUserSessionLanguage
-[MKBKeyStoreDevice stashCommit:WithFlags:]_block_invoke_2
Can't create file to restore to (class: %d): %s
Failed to deallocate page aligned buffer
convertBinaryToObject
MKBKeyBagKeyStashEnableWithOpts
MKBKeyBagKeyStashPersistWithOpts
failed to allocate handle
corrupt key; blob size %lu, key size %u
-[MKBKeyStoreDevice stashVerifywithValidity:WithUID:WithFlags:]_block_invoke
Statfs failed due to:%s on  (%s)
sessionblob length:%ld
Could not create dictionary from stream
-[MKBKeyStoreDevice createSyncBagForUserSession:withSessionUID:]_block_invoke
MKBGetDeviceConfigurations failed to return a dictionary
crypto_id = 0x%016llx, extent_size = %llu, key class = %u
Failed to pwrite(%lu, %llu) from %s
Failed to get cstring from uuidString
MKBDeviceModeSingleUser
Could not create stream from serialized data
-[MKBKeyStoreDevice passcodeUnlockFailed]_block_invoke_2
-[MKBKeyStoreDevice SeshatDebug:]_block_invoke
%s%s
xts mode
MKBUserSessionLoginTimeStamp
AppleKeyStore
Protection class changed from %d to %d
UserSwitchTaskUUID
MKBUserSessionVolumeUUID
-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke
-[MKBKeyStoreDevice stashDestroy]_block_invoke_2
_DFAIL
HealthPlistSetTTR
validate_health_plist
copy_rewrapped_key_from_db
Failed to pread(%zu, %llu) from %s (%s)
Invalid Blob entry for unwrap
MKBUserSessionFirstName
MKBUserSessionRequiresPasscode
plist build tests
BackupKeyBagKeys
MKBUserSessionSetSecureBackupBlob
UMUserSessionIsLoginSession
KBMapDeviceBag Success
MKBUserSessionVolumeFSType
Could not open the stream
create_mutable_dict
Can't find EffaceableStorage kext!
invalid ttr format
aks_change_secret_epilogue() failed %x
Bad key passed in, does not validate
MKBUserSessionAPNSID
Out of Memory!!! Dying!...so...cold....
-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke
-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke_2
plist version tests
MKBDeviceSetGracePeriod(acm:%d): To (%lld)AKS return Value is %d\n
MKBAssertion
MKBUserSessionFileInfo
-[MKBKeyStoreDevice deleteKeybagForUserSession:]_block_invoke
version is of wrong type
KBLoadLoadKeyBagFile
MKBKeyBagKeyStashCreateWithOpts
memento verifiers and acm context are unsupported
com.apple.mobile.keybagd.xpc
-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke_2
-[MKBKeyStoreDevice verifySyncBagForUserSession:withSessionUID:]_block_invoke
addition of TTR failed
Can't create iv data
KBSecureSaveObjectNoCrypto
MementoBlobMaxUnlockAttempts
TimeMachine
xts ans kdf2 mode
MKBUserSessionCachedLoginEndTime
MKBOTABackupBagCopyUUID
__MKBBackupDecryptInPlace
Failed to shrink %s to %lld: %s
Failed to parse to uuid_t
MKBUserSessionAlternateUUID
MKBUserSessionLastName
realloc failed
got error from remote proxy: %ld
DeviceHandle
unlocked bag %d
Can't save the bag: %d
hw.osenvironment
-[MKBKeyStoreDevice copySytemSecretBlob]_block_invoke_2
changing non-SE passcode %s phase, (params:%d)
kern.bootargs
Could not get the backup key for crypto ID 0x%016qx (%d of %u, existing keys: %s, found1:%d, found2:%d, found3:%d)
-[MKBKeyStoreDevice stashVerifywithValidity:WithUID:WithFlags:]_block_invoke_2
v8@?0
Failed to unlock in-kernel backup bag: 0x%08x
Couldn't allocate work buffer of %zu bytes\n
extents = %s
could not rename %s to %s: %s (%d)
ExtendedDeviceLockState
MKBGetDeviceConfigurations
MKBKeyBagKeyStashCommitWithOpts
bytes_read(%ld) < read_size(%ld), but effective_start(%lld) + read_size(%ld) <= file_size(%lld)\n
com.apple.mobile.keybagd.lock_status
MKBDeviceModeMultiUser
KBisxARTBasedKeyBag
getNVRam
file cannot be larger than backup
-[MKBKeyStoreDevice disableBackupForVolume:]_block_invoke
effaceBlastableBytes
mismatch
odd blob size %zu, offset = %zu
Failed to find UMUserSessionConfigureLoginWindow in UM
Updating VolumeUUID %@
MKBUserSessionDirty
UserSwitchTaskReason
-[MKBKeyStoreDevice migrateFS]_block_invoke
IONVRAM-DELETE-PROPERTY
dt = %d, bootarg = %d
extent count mismatch i=%d, count=%d, offset=%zu, key_blob_size=%zu
wrapped key size too big (%u>%zu)
got error from remote proxy: %d
failed to allocate memory for event callback
failed to copy block
plist failure tests
%d
Failed to allocate Cookie malloc space
dbError
Failed to find UMUserSessionForegroundSession in UM
time stamp is of wrong type
APFSVolumePayloadGet
countdown
Failed to get backup bag uuid for volume: %x
MKBBackupValidateBackupKeyWithUUID
MKBBackupValidateKey
bytes_read(%zd) not multiple of encryption block size
create_string
Unable to fsync %s: %s
unlink failed: %s
Retrieved keybag persona Cookie from AKS, setting in APFS volume
APFSVolumePayloadGet failed with %d
%s.writing
MKBUserSessionLoadWithPasscode
Failed to find UMUserSessionIsLoginSession in UM
got error from remote proxy for getPasscodeBlobWithReply: %ld
MKBBackupCreateFromFileDescriptors
F_PUNCHHOLE failed on %s for range (%lld:%llu): %s
MKBUserSessionIsLoginSession
MKBUserSessionUnWrapSession
MKBUserSessionPreviousLoggedinID
-[MKBKeyStoreDevice setSpacedRepetitionMode:]_block_invoke
failed to find %s service
HealthPlistSetVersion
_create_plist_with_version
error: unexpected encryption mode : %d
Could not write to %s: %s
Could not read %s: %s
-[MKBKeyStoreDevice loadSyncBagForUserSession:withSessionUID:]_block_invoke
non-current version %d
KBChangeSystemNonSeSecret
AKS can't create bag: %08x
Failed to construct data key fixed data
UMUserSessionSwitchToLoginWindow
MKBUserSessionWrapSession
MKBUserSessionLibinfoHomeDir
create_array
Saving SystemBag with NO EFFACEABLE ROLL
Failed to open APFS framework
MementoSupported
MKBFileCreateForRestore
Error prewarming SPSs: %d
__options_to_change_secret_params
MKBKeyBagHandle
Data to Wrap with length:%d
APFSVolumePayloadSet succeeded
_MKBBackupCheckKey
disk
MKBUserSessionShortName
MKBUserSessionSyncMachServices
is_device_in_device_recovery_environment_block_invoke
12A123
Could not save value:%08x
mount is with NO CPROTECT:0x%x on  (%s)
UserSwitchTaskMachService
load_binary_dict
-[MKBKeyStoreDevice startBackupSessionForVolume:]_block_invoke
_DDATA
Saving SystemBag with EFFACEABLE ROLL
MKBAssertionTimeout
handle is of wrong type
failed to write to pipe with error:%s
_DTTR
invalid ttr timestamp
IODeviceTree
Other
_MKBDeviceSetGracePeriod
Failed to construct tweak key fixed data
FAILED to MKBUserTypeDeviceMode, EINVAL
UserSwitchTaskName
MKBUserUnlockedSinceBoot
found extent-based key_blob, size %zu
MKBUserSessionCachedLoginStartTime
UserSwitchTaskBundleID
-[MKBKeyStoreDevice stopBackupSessionForVolume:]_block_invoke_2
-[MKBKeyStoreDevice isKeyRollingWithKeyStatus:]_block_invoke_2
_DLD
keybags
APFSVolumePayloadSet failed with %d
Can't create IV
MKBKeyBagCleanupAfterMigration
MKBAssertionKey
Failed to get backup bag uuid from data: %x
Data to Wrap is NULL
unexpected TTR entry
Unable to open service: 0x%08x
failed to consume TTR entry
KBLoadUserKeybag
KBMapVolume
Status missing from response
MKBFileReadTranscrypt
Failed to find UMUserSessionDeleteSecureBackupBlob in UM
MKBUserSessionVolumeDeviceNode
HealthPlistSetTime
12A124
:/filesystems
key found in db doesn't match current backup bag!!
com.apple.mobile.keybagd.user_started
MKBUserSessionTotalDataSize
Could not get wrapped crypto key for inode %llu right now: %s
HealthPlistConsumeTTR
data is of wrong type
KBLoadSystemKeyBag
Saved new keybag for handle %d with result %d
KBSetCookie
first manifest
entry overruns blob offset=%zu keysize=%u blob_size=%zu
Bag uuid mismatch, ignore
Failed to find UMUserSessionSetSecureBackupBlob in UM
no user bag found for UID %d
Failed to unload session keybags: 0x%x
-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]_block_invoke
systembag
KBSecureSaveObjectWithCrypto
LockDeviceNow
MKBDeviceUnlockedSinceBoot fails with error(%d) for handle(%d) with AKS error(%d)
write failed: %s\n
Could not fstat %s: %s
missing version
file size %lld bytes
-[MKBKeyStoreDevice getLockStateForUser:]_block_invoke_2
Failed to validate keybag file: %d, %d
pread() failed: %s\n
VerifyOnly
fileError
com.apple.mobile.usermanagerd.foregrounduser_changed
MKBUserSessionID
failed to add interest notification
MKBUserUnlockedSinceBoot for user(%d) fails with error(%d), returning 0
[%d] crypto_id = 0x%016llx, extent_size = %llu, key class = %u, bag uuid = %s
Failed to unwrap dict blob with classF
PolicyUID
MKBUserSessionisTransient
-[MKBKeyStoreDevice migrateFS]_block_invoke_2
sw
Failed to unwrap key (%p,%d) in class %d with handle %d: 0x%08x
MKBKeyBagUnlock
allocate_page_aligned_buffer
com.apple.mobile.keybagd.db.file.extents.number
UMUserSessionRetrieveSecureBackupBlob
-[MKBKeyStoreDevice backupUUIDForVolume:bagUUID:]_block_invoke_2
handle=%{public}d
result=%{public}d
SE_enroll
completed
Unexpected AppleKeyStore error: %d\n
%s\n
handle=%{public}d secretIsACM=%{public}d use_memento=%{public}d verify_only=%{public}d
MKBUnlockDeviceForACMRef
AKS_unlock_verify
SE_unlock
KBXPCProtocol
NSObject
MKBKeyStoreDevice
stashCommit:WithFlags:
isProxy
SeshatDebug:
getPasscodeBlobWithReply:
passcodeUnlockSuccessWithReply:
forgottenPasscodeEvent
passcodeUnlockFailed
superclass
synchronousRemoteObjectProxyWithErrorHandler:
SeshatEnroll:secretIsACM:
backupUUIDForVolume:bagUUID:
passcodeUnlockFailedWithReply:
registerOTABackup:withSecret:secretIsACM:
retain
setSpacedRepetitionMode:reply:
SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:
getDeviceLockState:needsExtended:withReply:
removeSyncBagForUserSession:withSessionUID:withReply:
createKeybagForUserSession:withSessionUID:WithSecret:secretSize:withGracePeriod:withOpaqeStuff:withReply:
loadKeybagForUserSession:withSessionID:withSecret:secretSize:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:withReply:
passcodeUnlockStartWithReply:
stashDestroy
stopBackupSessionForVolume:
unloadKeybagForUserSession:withReply:
ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:
addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:
changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:
getBackupBlobreply:
loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:
SetSystemSecretBlob:
description
unloadSyncBagForUserSession:withSessionUID:withReply:
SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:
SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:
TQ,R
changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:
removeSyncBagForUserSession:withSessionUID:
startBackupSessionForVolume:withReply:
registerBackupBag:withSecret:secretSize:secretIsACM:reply:
_xpcConnection
enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:
initWithFileDescriptor:closeOnDealloc:
setVolumeToPersona:withPersonaString:withReply:
stashCreateWithSecret:withMode:withUID:WithFlags:
SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:
bytes
changeSystemSecretFromOldPasscode:ToNew:withOpaqueData:withParams:
changeSystemSecretfromOldSecret:oldSize:toNewSecret:newSize:opaqueData:withParams:reply:
disableBackupForVolume:reply:
getDeviceLockStateForUser:extendedState:withLockStateInfo:
respondsToSelector:
setSystemSecretBlob:reply:
createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:
deleteKeybagForUserSession:
getLockSateInfoforUser:WithReply:
invalidate
T@\"NSString\",R,C
stopBackupSessionForVolume:withReply:
unloadSyncBagForUserSession:withSessionUID:
backupUUIDForVolume:reply:
isKindOfClass:
verifySyncBagForUserSession:withSessionUID:withReply:
deleteKeybagForUserSession:withReply:
getBackupkeyForVolume:andCryptoID:withError:
length
migrateFS
performSelector:withObject:
retainCount
self
setVolumeToPersona:withPersonaString:
release
autorelease
class
enableBackupForVolume:withSecret:secretIsACM:bagData:
removePersonaKeyForUserSession:withUID:withVolumeUUIDString:withReply:
disableBackupForVolume:
loadSyncBagForUserSession:withSessionUID:
verifySyncBagForUserSession:withSessionUID:
getBytes:length:
resume
setSpacedRepetitionMode:
null
performSelector:
removePersonaKeyForUserSession:withPersonaUUIDString:withVolumeUUIDString:
errorWithDomain:code:userInfo:
zone
getFileHandleForData:
getLockStateForUser:
isKeyRollingWithKeyStatus:
migrationWithReply:
passcodeUnlockStart
sharedService
stashVerifywithUID:WithFlags:WithReply:
_CreateMKBServerConnection
dataWithBytesNoCopy:length:freeWhenDone:
hash
isKeyRollingInProgresswithreply:
code
createSyncBagForUserSession:withSessionUID:withReply:
interfaceWithProtocol:
isMemberOfClass:
loadSyncBagForUserSession:withSessionUID:withReply:
performSelector:withObject:withObject:
Event:
changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:
getBackupkeyForVolume:andCryptoID:withReply:
conformsToProtocol:
createSyncBagForUserSession:withSessionUID:
copySytemSecretBlob
debugDescription
forgottenPasscodeEventWithReply:
stashDestroywithReply:
stashVerifywithValidity:WithUID:WithFlags:
unloadKeybagForUserSession:
SeshatDebugWithDebugMask:withReply:
createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:
passcodeUnlockSuccess
stashCommitwithUID:WithFlags:WithReply:
T#,R
numberWithUnsignedLongLong:
setRemoteObjectInterface:
stashCreatewithSecret:secrestSize:withMode:withUID:WithFlags:reply:
SeshatRecover:secretIsACM:
dictionaryWithObjects:forKeys:count:
initWithMachServiceName:options:
T@\"NSString\",?,R,C
isEqual:
startBackupSessionForVolume:
Q16@0:8
@\"NSString\"16@0:8
v52@0:8@16Q24i32I36I40@?44
v24@0:8@?<v@?@\"NSError\">16
v32@0:8i16B20@?<v@?i@\"NSError\">24
v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSData\"@\"NSError\">44
i44@0:8@16@24@32I40
i56@0:8@16@24@32@40i48B52
i24@0:8@16
i36@0:8I16@20@28
v64@0:8@\"NSFileHandle\"16Q24B32B36B40@\"NSData\"44i52@?<v@?i@\"NSError\">56
Vv16@0:8
^{_NSZone=}16@0:8
v64@0:8@16Q24B32B36B40@44i52@?56
v32@0:8I16I20@?<v@?i@\"NSError\">24
B32@0:8i16B20^i24
i48@0:8@16B24B28B32@36i44
v44@0:8@16I24@28@?36
@24@0:8:16
v24@0:8@?16
v32@0:8i16B20@?24
B24@0:8@16
v52@0:8@16@24Q32B40@?44
v80@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@\"NSFileHandle\"40Q48@\"NSData\"56B64B68@?<v@?@\"NSError\">72
v64@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44B52@?<v@?@\"NSError\">56
i48@0:8@16i24@28i36@40
@16@0:8
v80@0:8@16@24Q32@40Q48@56B64B68@?72
v28@0:8I16@?<v@?@\"NSError\">20
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
@40@0:8@16Q24^@32
i16@0:8
i24@0:8I16I20
i20@0:8i16
#16@0:8
@40@0:8:16@24@32
v32@0:8@16@?24
v44@0:8@16Q24B32@?36
v64@0:8@16i24@28Q36i44@48@?56
v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSError\">44
@24@0:8@16
i36@0:8@16i24I28I32
B24@0:8#16
v28@0:8I16@?20
v48@0:8@\"NSFileHandle\"16Q24B32i36@?<v@?@\"NSError\">40
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?i@\"NSError\">36
v68@0:8@16Q24@32Q40@48I56@?60
v68@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@\"NSData\"48I56@?<v@?@\"NSError\">60
v32@0:8I16I20@?<v@?@\"NSError\">24
v36@0:8@\"NSDictionary\"16i24@?<v@?@\"NSError\">28
i44@0:8@16@24B32^@36
i32@0:8^i16I24I28
i28@0:8@16i24
v24@0:8@?<v@?i@\"NSError\">16
@32@0:8:16@24
B24@0:8@\"Protocol\"16
v48@0:8@16Q24B32i36@?40
v28@0:8i16@?20
v64@0:8@16@24I32@36Q44B52@?56
i32@0:8@16^@24
@20@0:8i16
v64@0:8@16i24@28Q36B44i48B52@?56
v20@0:8i16
v40@0:8@\"NSData\"16Q24@?<v@?@\"NSData\"@\"NSError\">32
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24
v28@0:8i16@?<v@?@\"NSError\">20
v44@0:8@\"NSString\"16I24@\"NSString\"28@?<v@?@\"NSError\">36
i32@0:8@16@24
v40@0:8@16Q24@?32
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36B44i48B52@?<v@?@\"NSError\">56
i20@0:8I16
i32@0:8@16i24B28
i24@0:8^i16
i28@0:8@16B24
i48@0:8@16i24@28B36i40B44
B24@0:8:16
v32@0:8I16I20@?24
v40@0:8@16@24@?32
v52@0:8@\"NSFileHandle\"16Q24i32I36I40@?<v@?@\"NSError\">44
v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36i44@\"NSData\"48@?<v@?@\"NSError\">56
v36@0:8@16i24@?28
i36@0:8@16@24B32
i48@0:8I16@20B28@32@40
v28@0:8i16@?<v@?@\"NSDictionary\"@\"NSError\">20
v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?@\"NSError\">36
B16@0:8
```
