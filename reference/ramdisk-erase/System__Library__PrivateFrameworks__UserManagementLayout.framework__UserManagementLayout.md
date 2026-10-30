# `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 255,424 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3536)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 3 protocols)

Classes: `UMAppleKeyStoreProvider`, `UMFilesystemProvider`, `UMLManager`, `UMLProviderSideEffects`, `UMLSideEffects`, `UMLUser`, `UMLUserManifest`

Protocols: `NSObject`, `UMAppleKeyStoreProviding`, `UMFilesystemProviding`

## Strings (739)

```
MAXUSERSIZE
SYNCENT
MKBUserTypeKey
%@/System/Library/Templates/User/
nodev
MKBUserSessionVolumeDeviceNode
BLOB
MKBUserSessionFileInfo
MKBUserSessionRequiresPasscode
LRUBLOB
MKBUserSessionShortName
MKBUserSessionLanguage
MKBUserSessionisPrimary
device-recovery
IOService
BSD Name
Data
MKBUserSessionNeedsMount
USESSTYPE
en_US
MKBUserSessionisAdminKey
User
MKBUserSessionGroupID
sideeffect
Unexpected composed log message.
MKBUserSessionLoginTimeStamp
AppleAPFSContainer
MKBUserSessionAPNSID
MKBUserSessionCachedLoginStartTime
com.apple.UserManagementLayout
UserVolumeAPFSNative
DEVICECONFIG
NUMENT
UserManifestVersion
userlayout
%@/mobile
TRUE
MKBUserSessionCreateTimeStamp
MKBUserSessionFirstLoginStartTime
%@.writing
BOOTEDUSER
DEVICENETWORKBG
MKBUserSessionID
i32@?0i8i12@\"NSString\"16@\"NSString\"24
MKBUserSessionHomeDir
MKBUserSessionFirstLoginEndTime
APNSID
LOGINCHECKIN
MKBUserSessionUUID
MKBUserSessionLoginUser
MKBUserSessionDirty
/keybags/usersession.kb
nosuid
FALSE
/keybags
UserSessionOther
default
MKBUserSessionForeground
RoleValue
Encrypted
MKBUserSessionKeybagOpaqueData
MKBUserSessionVolumeFSType
MKBUserSessionDisplayName
-o
MKBUserSessionCachedLoginEndTime
legacy
MAXUSER
MKBUserSessionLibinfoHomeDir
MKBUserSessionVolumeUUID
SYNCBLOB
LRUENT
MKBUserSessionFirstName
MKBUserSessionLastName
MKBUserSessionName
hw.osenvironment
v8@?0
MKBUserSessionAlternateUUID
2457711A-523C-4604-B75A-F48A571D5036
UUID
vfs.generic.ctlbyfsid
MKBUserSessionDisabled
MKBUserSessionHasSyncBag
MKBUserSessionOpaque
mobile
/var/mobile
/sbin/mount_apfs
AppleAPFSVolume
MKBUserSessionAuditor
UMUUIDHelper
UMLProviderSideEffects
UMLSideEffects
UMLUserManifest
Private
UMSerializationHelper
UMAppleKeyStoreProviding
UMFilesystemProvider
UMFilesystemProviding
NSObject
UMLManager
UMLUser
UMAppleKeyStoreProvider
_isPrimaryUser
_userLanguauge
dictionary
respondsToSelector:
setUserSessionType:
Ti,N,V_version
_deviceConfig
dataWithContentsOfFile:options:error:
firstName
fsVolumeType
mountUserDataVolumeOnSystemDataAt:withACMCredential:withError:
numberWithUnsignedInteger:
unlockIdentity:passcode:isACMCredential:error:
verifyIdentityPasswordInSession:passcode:isACMCredential:error:
_dataValue
version
T@\"NSString\",C,N,V_volumeUUID
fixupPath:withMode:toUser:group:error:
setIsAuditor:
T@\"NSString\",C,N,V_fsVolumeType
TB,N,V_isLoginUser
_networkBG
cachedLoginStart
debugDescription
firstLoginEnd
removeAnUser:fromUserManifest:saveToPath:
superclass
T@\"NSMutableArray\",C,N,V_users
sizeOfFileWithDescriptor:error:
TQ,R
mountUserDataVolumeOnSystemDataAt:withSecret:withError:
setAlternateDSID:
setDiskNode:
setOpaqueData:
setGid:
setGracePeriod:
_creationDate
chmodPath:withMode:error:
Tq,N,V_apnsIDStart
_libInfoPath
initWithUUIDString:
userUUID
isLoginUser
code
createPrimaryUserOnSharedDataVolumePath:withError:
users
_fileInfoPath
_isAdminUser
unlockIdentityInSession:passcode:isACMCredential:error:
T@\"NSMutableArray\",C,N,V_syncUserList
TB,N,V_isPrimaryUser
_alternateDSID
_isLoginUser
createPrimaryUserLayoutWithOnUserVolumePath:fromSystemVolumePath:withError:
loadManifestFromSharedDataVolumePath:
setMaxUsers:
T@\"NSData\",&,N,V_dataValue
isAuditor
setFirstName:
T@\"NSString\",C,N,V_alternateDSID
_apnsID
_generation
objectForKey:
setIsPrimaryUser:
setLastBootedUser:
setLoginuiCheck:
T@\"NSDate\",C,N,V_firstLoginStart
loadIdentity:intoSession:error:
TB,N,V_hasSyncBag
numberWithLongLong:
replaceObjectAtIndex:withObject:
setUserLanguauge:
sharedManager
clonePath:toPath:error:handler:
conformsToProtocol:
username
T@\"NSString\",C,N,V_userLanguauge
TB,N,V_isForeground
Ti,N,V_userSessionType
isEqualToString:
retain
setLastLoginEnd:
setVolumeUUID:
Ti,N,V_loginuiCheck
Ti,N,V_networkBG
_gracePeriod
_homeDirPath
_loginuiCheck
_cachedLoginStart
lastName
setCreationDate:
T@\"NSString\",C,N,V_username
_maxUsers
_userType
makePath:mode:error:
firstLoginStart
loginIdentity:intoSession:passcode:isACMCredential:error:
setLibInfoPath:
countByEnumeratingWithState:objects:count:
T@\"NSDate\",C,N,V_firstLoginEnd
uid
Tq,N,V_apnsID
_diskNode
atomicallyWriteData:toPath:error:
T@\"NSString\",C,N,V_libInfoPath
gid
UUID
hasSyncBag
numberWithInt:
setIsDirty:
_isDirty
apnsIDStart
dataWithBytes:length:
dataWithPropertyList:format:options:error:
manifestFromData:
openFileForAppendingAtPath:error:
setSyncUserList:
Tq,N,V_maxUserSize
_firstName
dataValue
setApnsID:
setNeedsMount:
setApnsIDStart:
UUIDString
_opaqueData
diskNode
mutableCopy
setCachedLoginEnd:
updatePrimaryUser:onSharedDataVolumePath:withDiskNode:withVolumeuuid:withVolumeName:withError:
_cachedLoginEnd
T@\"NSData\",C,N,V_opaqueData
_isDisabledUser
T@\"NSString\",?,R,C
TI,N,V_version
_filesystem
count
setIsDisabledUser:
_lastBootedUser
UTF8String
addNewUser:toUserManifest:saveToPath:
domain
readUserFromManifest:forUserUid:withError:
setValue:forKey:
T@\"NSString\",C,N,V_homeDirPath
TQ,N,V_generation
_maxUserSize
fileExistsAtPath:isDirectory:
_hasSyncBag
_username
errorWithDomain:code:userInfo:
fileInfoPath
length
mapVolume:toSession:withPersona:error:
isPrimaryUser
isValidClassTypeinDictionary:withKey:withType:
_se
closeFileWithDescriptor:
dataWithContentsOfFile:error:
lastLoginStart
T@\"NSString\",C,N,V_fileInfoPath
_firstLoginEnd
removePath:error:
setUserType:
unsignedIntValue
unsignedLongLongValue
T#,R
Ti,N,V_maxUsers
TB,N,V_ignoreIdentityMethods
TB,N,V_needsMount
_keybagOpaqueData
deletePersonaWithUUID:fromSession:error:
networkBG
syncUserList
setMaxUserSize:
addPersonaWithUUID:toSession:passcode:error:
createUserLayoutForUserwithUserID:withAKSSetup:onUserVolumePath:fromSystemVolumePath:withError:
deviceConfig
T@\"NSString\",C,N,V_firstName
T@\"NSDate\",C,N,V_creationDate
setIsAdminUser:
_userSessionType
dataUnwrappingDataWithDeviceClassF:error:
mountSystemDataVolumeAt:withError:
setHasSyncBag:
T@\"NSDate\",C,N,V_cachedLoginStart
T@\"NSData\",R,N
Ti,N,V_uid
_apnsIDStart
autorelease
bytes
dataWithData:
isMemberOfClass:
removeObject:
TB,N
dataWrappingDataWithDeviceClassF:error:
propertyListWithData:options:format:error:
refreshPrimaryUserOnSharedDataVolumePath:withBootstrapToken:withError:
setLastLoginStart:
keybagOpaqueDataOnSharedDataVolumePath:withError:
userInfo
T@\"NSString\",C,N,V_userUUID
_lastName
_manifest
dataUsingEncoding:
gracePeriod
lastLoginEnd
saveManifest:toPath:
setDataValue:
setUid:
Ti,N,V_gid
_lastLoginEnd
inDeviceRecoveryEnvironment
isAdminUser
setIgnoreIdentityMethods:
setIsForeground:
setUserUUID:
isEqual:
setLruList:
userManifestDictionary
volumeUUID
release
Ti,N,V_lastBootedUser
_uid
init
loginuiCheck
stringWithString:
writeToFileWithDescriptor:string:error:
Ti,N,V_gracePeriod
T@\"NSMutableArray\",C,N,V_lruList
.cxx_destruct
apnsID
isForeground
setDeviceConfig:
unmountUserDataVolumeOnSystemDataAt:withError:
_userUUID
hash
setKeybagOpaqueData:
stringWithUTF8String:
userLanguauge
T@\"NSData\",C,N,V_keybagOpaqueData
_lruList
lastBootedUser
performSelector:
defaultManager
deleteIdentity:error:
isIdentityLoadedIntoSession:
stringWithCString:encoding:
cachedLoginEnd
createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:isACMCredential:error:
needsMount
setUsers:
setWithArray:
unloadIdentityFromSession:error:
T@\"NSString\",R,C
class
performSelector:withObject:
setLastName:
userType
isProxy
T@\"NSString\",C,N,V_diskNode
lruList
T@\"NSString\",C,N,V_lastName
keybagOpaqueData
setFirstLoginStart:
setGeneration:
setObject:forKeyedSubscript:
performSelector:withObject:withObject:
removeFileAtPath:error:
renameFileFromPath:toPath:error:
setNetworkBG:
unmountSystemDataVolumeAt:withError:
TB,N,V_isDirty
_needsMount
appendString:
zone
numberWithBool:
_isForeground
_syncUserList
setFileInfoPath:
T@\"NSString\",C,N,V_displayName
TB,N,V_isDisabledUser
setVersion:
userSessionType
TB,N,V_isAuditor
_users
changeSecretrForIdentityWithUUID:oldPasscode:newPasscode:existingSession:isACMCredential:error:
mountVolumeAtPath:fromDevice:forUserUID:userGID:withMode:withError:
setCachedLoginStart:
dateWithTimeIntervalSince1970:
ignoreIdentityMethods
setFsVolumeType:
userFromManifestDictionary:
homeDirPath
intValue
isDisabledUser
isDirty
Ti,N,V_deviceConfig
_gid
_ignoreIdentityMethods
addObject:
description
TB,N,V_isAdminUser
_aks
_firstLoginStart
_volumeUUID
boolValue
bootstrapVolumeWithMountPoint:user:error:
displayName
setIsLoginUser:
_lastLoginStart
_isAuditor
chownPath:toUser:group:error:
libInfoPath
longLongValue
maxUserSize
opaqueData
T@\"NSDate\",C,N,V_cachedLoginEnd
setHomeDirPath:
_version
primaryUserOnSharedDataVolumePath:withError:
retainCount
self
setFirstLoginEnd:
setUsername:
setDisplayName:
_fsVolumeType
creationDate
maxUsers
objectForKeyedSubscript:
unMountVolumeAt:withError:
unmapVolume:error:
isKindOfClass:
T@\"NSDate\",C,N,V_lastLoginStart
T@\"NSDate\",C,N,V_lastLoginEnd
alternateDSID
readUserManifestOnSharedDataVolumePath:withError:
stringWithFormat:
updateUser:inManifest:withDiskNode:volumeUUID:volumeName:withSharedDataVolumePath:withError:
generation
T@\"NSString\",C,N,V_userType
_displayName
i
B52@0:8@16@24I32I36S40^@44
@\"NSData\"
v20@0:8B16
@\"NSObject<UMFilesystemProviding>\"
Q16@0:8
B24@0:8@\"Protocol\"16
q16@0:8
B36@0:8@\"NSString\"16I24^@28
@16@0:8
v16@0:8
i16@0:8
v24@0:8@16
B40@0:8I16@\"NSData\"20B28^@32
B44@0:8@\"NSUUID\"16I24@\"NSData\"28^@36
@\"NSObject<UMAppleKeyStoreProviding>\"
B48@0:8@16@24^@32@?40
B36@0:8@\"NSString\"16S24^@28
@24@0:8@16
B56@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36B44^@48
@\"NSString\"16@0:8
B40@0:8@16@24^@32
@\"NSDate\"
B40@0:8@16@24#32
B40@0:8I16@20B28^@32
B56@0:8@\"NSUUID\"16@\"NSData\"24@\"NSData\"32I40B44^@48
B24@0:8@16
B40@0:8@\"NSData\"16@\"NSString\"24^@32
B40@0:8@\"NSString\"16@\"NSString\"24^@32
B44@0:8@\"NSString\"16S24I28I32^@36
q
@\"NSMutableArray\"
B44@0:8@16I24@28^@36
B16@0:8
v24@0:8Q16
@\"NSString\"
B40@0:8@16@24@32
I16@0:8
I
B24@0:8#16
v20@0:8i16
q28@0:8i16^@20
B56@0:8@16@24@32I40B44^@48
B44@0:8@\"NSString\"16I24@\"NSUUID\"28^@36
B36@0:8@16S24^@28
B32@0:8@16@24
B20@0:8I16
B48@0:8@16I24@28B36^@40
B32@0:8@\"NSString\"16^@24
B32@0:8@\"NSString\"16^B24
v24@0:8q16
B32@0:8@16^@24
^{_NSZone=}16@0:8
i32@0:8@16^@24
@\"UMLUserManifest\"
B32@0:8@\"NSUUID\"16^@24
B32@0:8@16^B24
B44@0:8@16S24I28I32^@36
@\"NSData\"32@0:8@\"NSString\"16^@24
B40@0:8@\"NSString\"16I24I28^@32
B72@0:8@16@24@32@40@48@56^@64
B36@0:8i16@\"NSString\"20^@28
Q
@36@0:8@16I24^@28
@32@0:8@16^@24
B24@0:8:16
B36@0:8i16@20^@28
B64@0:8@16@24@32@40@48^@56
@\"UMLSideEffects\"
v20@0:8I16
B
@24@0:8:16
@40@0:8:16@24@32
Vv16@0:8
i32@0:8@\"NSString\"16^@24
B36@0:8@16I24^@28
B56@0:8@16@24I32@36B44^@48
@\"NSData\"32@0:8@\"NSData\"16^@24
B48@0:8@\"NSUUID\"16I24@\"NSData\"28B36^@40
B40@0:8@16I24I28^@32
B48@0:8@\"NSString\"16@\"NSString\"24^@32@?<i@?ii@\"NSString\"@\"NSString\">40
B48@0:8i16B20@24@32^@40
B28@0:8I16^@20
B36@0:8@\"NSUUID\"16I24^@28
#16@0:8
@32@0:8:16@24
AKSVolumeUnmap(%{public}@) failed: %{public}@
Added the user to the manifest and updated the manifest to Disk
Invalid Parameters, returning error
No primary user in the manifest
Removed file: %{pubilc}@
removefile(\"%{public}@\", REMOVEFILE_RECURSIVE) failed: %{darwin.errno}d
Failed to map the UDV with error, unload identity, bailing..
501 AKS Identity is not loaded, returning success
Unable to force unmap UDV at given location
could not find user with error:%@
Skipping AKS setup
Failed to create user manifest path, bailing...
Failed to atomically write %{public}@: fsync(%d) failed: %{darwin.errno}d
Removed path \"%{public}@\"
Failed to find Primary USER volume
getmntfsid failed with error:%d
Failed to parse user UUID, bailing..
Failed to parse user homedir path, skipping..
Failed to unwrap data: data is too large: %lu
AKSIdentityUnlockSession(%u) failed: %{public}@
Unlocked AKS identity %u
Failed to atomically write %{public}@: Failed to atomically swap writing file: %{darwin.errno}d, then failed to rename file: %{darwin.errno}d
Unable to force UnMount SDV at given location
Manifest Write Successful
BootDevice is %@
Failed to parse user uid, bailing..
Found Existing User Uid:%d
Failed to allocate buffer to read OSEnvironment value. Assuming running in normal mode
Failed to atomically write %{public}@: open_dprotected_np(%{public}@) failed: %{darwin.errno}d
Warning: failed to create write barrier when writing %{public}@: fcntl(%d, F_BARRIERFSYNC) failed: %{darwin.errno}d
Failed to lchown path %{public}@ to %d/%d: %{darwin.errno}d
Failed to chmod path %{public}@ to %o: %{darwin.errno}d
While removing path, lchflags(\"%{public}s\") failed: %{darwin.errno}d
Unable to locate UDV on the booted container
unable to scan IORegistry
Failed to parse user name, bailing..
Failing to delete 501 after load failure
No user uuidstring on the user manifest on the given SDV Path
failed to unload the AKS identity
Found DiskNode: %@ within the Boot Container
no APFS containers found
Failed to parse user type, bailing..
Failed to parse user first name, bailing..
While removing path, removefile_state_get(REMOVEFILE_STATE_ERRNO) failed: %{darwin.errno}d
Failed to find SDV
Unmapped volume %{public}@ from AKS session
Created AKS identity: %{public}@
aks_get_system(%u) failed: 0x%x
AKSIdentityUnload(%u) failed: %{public}@
While removing path, failed to unlink \"%{public}s\" after removing UF_IMMUTABLE: %{darwin.errno}d
Failed to load bootstrap user with the token, bailing
unmounted UDV on error path
copyfile: Error: could not chown %{public}@
verified AKS identity in session %u
AKSIdentityLoginWithACMCred(%@, %u) failed: %{public}@
Added persona %{public}@ to AKS session %u
removefile(\"%{public}@\", REMOVEFILE_RECURSIVE) failed with ENOENT, ignoring...
Failed to mount the volume with error %d
Failed to set chown  on volume mounts directory %{public}@
Found SystemData Volume:%s isEncrypted:%s
newUser.apnsID:%lld
AKSIdentityChangePasscode(%@, %u) failed: %{public}@
Calling aks_verify_password_with_acm for user:%d
Failed to load user manifest: Failed to read user manifest file from disk
Cannot wait for pid: %s
newUser.userType:%@
Failed to parse user libinfo path, bailing..
Copyfile from %{public}@ to %{public}@ stopped at handler request
newUser.gid:%d
Failed to parse dictionary plist from data: plist is not a dictionary
Copyfile from %{public}@ to %{public}@ failed: %{darwin.errno}d
No manifest on the SDV Path
Failed to login with identity UDV with error, bailing
updated the User and the on disk manifest
Failing to unload 501 OTI after failure to set Primary
Failed to convert array into binary plist: %@
Unlocked AKS identity in session %u
Failed to atomically write %{public}@: unlink(%{public}@) failed: %{darwin.errno}d
Failed to create path %{pubilc}@: mkpath_np failed: %{darwin.errno}d
Adding and Saving the manifest
bootstrap user LOADED
Failed to load user AKSIdfentity with error, bailing
Failed to parse dictionary plist from data: %{public}@
AKSIdentityLoad(%@, %u) failed: %{public}@
AKSIdentityUnlockSessionWithACMCred(%u) failed: %{public}@
No primary user manifest on the SDV Path
Failed to delete primary user Identity, bailing
Copying Starting from %@ to %@
Successfully copied contents from %{public}@ to %{public}@
Updating the user with User Vol properties
Failed to AKSVolumeBootstrapFS(%{public}@, %d): %{public}@
AKSIdentityLogin(%@, %u) failed: %{public}@
Failed to atomically write %{public}@: write(%d, <data>, %lu) only wrote %ld bytes
While removing path, unset UF_IMMUTABLE on \"%{public}s\"
Invalid parameter, no system or user path
Failed to copy contents from %{public}@ to %{public}@
Failed to get manifest data with bailing...
Volume is UnEncrypted
AKS Identity for session %u not loaded
AKSIdentityAddPersona(%u, ..., %{public}@,) failed: %{public}@
Failed to set permissions on volume mounts directory %{public}@
Running in DeviceRecoveryEnvironment\n
Unable to determine OS environment: %d:(%s)\n
Found Primary User Volume:%s  isEncrypted:%s
Failed to parse user alternateDSID, skipping..
Failed to parse user last name, bailing..
Failed to parse user manifest: manifest data is invalid
Failing to set Primary, return error
Failed to set aks bootstrap
Replacing Existing User with new content
APFSContainerGetBootDevice failed with %d, bailing..
sysctl_fsid failed with error:%d
newUser.uid:%d
newUser.userUUID:%@
Ignored bootstrap mountpoint %{public}@ to AKS identity session
updating the user home dir mount volume details
failed to unmount UDV on error path
Running in OS environment: %s
Volume is Encrypted
Warning while atomically writing %{public}@: close(%d) failed: %{darwin.errno}d
VALID primary user with UUID
501 AKS Identity already not loaded, failure
Invalid manifest user, could not get the dictionary
Failed to parse user display name, bailing..
Failed to wrap data: data is too large: %lu
Changed passcode of AKS identity: %{public}@
Ignored unmapping volume %{public}@ from AKS identity
removefile_state_set(REMOVEFILE_STATE_ERROR_CONTEXT) failed: %{darwin.errno}d
While removing path, lstat(\"%{public}s\") failed: %{darwin.errno}d
Primary user Identity Refreshed, load the identity to set Primary
Created ManifestDir Path 
Writing to the FileSytem Manifest
Warning while atomically writing %{public}@: unlink(%{public}@) failed: %{darwin.errno}d
Failing to delete 501 OTI after failure to set Primary
Failed to mount the UDV with error, unload identity, bailing..
Out of Memory!!! could not allocate dict, exiting....
newUser.alternateDSID:%@
Failed to parse array plist from data: %{public}@
AKS Identity for session %u loaded
Invalid user uuid string on the user manifest on the given SDV Path
Unable to force unmap UDV with error %@
UMD: Found keybag Blob
UMLUser-Not existing type or invalid type
Failed to convert dictionary into binary plist: %{public}@
Failed to unwrap data: aks_unwrap_key failed: %{mach.errno}d
Logged AKS identity %@ into session %u
AKSVolumeMap(%{public}@, %u, %{public}@) failed: %{public}@
Successful setting of ownershup of file:%{public}@ with uid:%d
Creating Bag Dir as it doesnot exit
failed to write to FS with error %@
Failed to determine size of buffer to read OSEnvironment value(%s). Assuming running in normal mode
Failed to load Primary UID after recreating, bailing
Unloaded AKS identity from session %u
Failed to generate user dictionary to save in the manifest, returning error
501 AKS Identity already loaded, failure
Now AKSVolumeBootstrapFS with uid:%d
Forced unmount of VARMOBILE failed with %s
Container: %@, volumeDiskNode:%@
Deleted AKS identity %{public}@
AKSIdentityDeletePersona(%u, %{public}@) failed: %{public}@
Ignored mapping volume %{public}@ to AKS identity session %u (persona: %{public}@)
While removing path, failed to remove path \"%{public}s\": %{darwin.errno}d
user with no opaqueData
Failed to unwrap data: aks_unwrap_key failed: kAKSReturnDecodeError
Failed to atomically write %{public}@: Failed to atomically swap writing file: %{darwin.errno}d
Primary user Identity unloaded
failed to unload the Bootstrap idenitity in the end
unable to fetch IORegistry properties
Failed to parse dictionary plist from data: plist is not an array
aks_unlock_device(-%u) failed: %{mach.errno}d
Calling aks_verify_password for user:%d
aks_verify_password(-%u) failed: %{mach.errno}d
Deleted persona %{public}@ from AKS session %u
Read data from file %@
removefile_state_set(REMOVEFILE_STATE_ERROR_CALLBACK) failed: %{darwin.errno}d
While removing path, ignoring missing file \"%{public}s\"
Primary user Identity DELETED
Set Primary on new 501 OTI, all parts successful
AKSIdentityDelete(%@) failed: %{public}@
Failed to get data with contents of file %{public}@: %{public}@
Did not remove file %{public}@: file did not exist
User manifest version does not exist or is wrong type
Primary user manifest exists on the SDV Path
Failed to unload primary user Identity, bailing
Unable to recreate Primary user Identity with bootstrap user
Failed to create manifest for the User, returning error..
Unable to mount SDV at given location
aks_lock_device after check failed with Error:%d
COPYFILE_FINISH: Changing %{public}@ to uidgid:%d
Successfully set aks bootstrap
Failed to load user manifest: Failed to parse user manifest
Adding the user to UserArray
Loaded AKS identity %@ into session %u
Failed to atomically write %{public}@: write(%d, <data>, %lu) failed: %{darwin.errno}d
Atomically wrote data to file %{public}@
Failed to remove all files for path \"%{public}@\": %{darwin.errno}d
Failed to add or write the manifest, returning error
Primary user Identity not Present, continue with the creation of the Identity
No uuid available for the Primary user
bootstrap user Unlaoded 
Failing to unload 501 OTI after successful setting of Primary
Failed to remove file %{public}@: unlink failed: %{darwin.errno}d
NOT in DRE with error:%@
 Skipping the diskNode:%@ as its not in the Boot Container
Unable to spawn %s
Failed to parse user gid, bailing..
Failed to parse user APNSID, skipping..
Failed to get data with contents of file %{public}@: %{darwin.errno}d
Failed to wrap data: aks_wrap_key failed: %{mach.errno}d
AKSIdentityCreate(%@, %u) failed: %{public}@
Mapped volume %{public}@ to AKS session %u (persona: %{public}@)
```
