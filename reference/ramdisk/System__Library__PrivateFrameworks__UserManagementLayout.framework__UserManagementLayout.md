# `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout`

From the upgrade restore ramdisk (141-29011-104.dmg). 255,424 bytes.

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
@\"NSString\"
B72@0:8@16@24@32@40@48@56^@64
@\"NSObject<UMAppleKeyStoreProviding>\"
@\"NSString\"16@0:8
B40@0:8@16@24^@32
B44@0:8@\"NSString\"16S24I28I32^@36
@\"NSData\"
@24@0:8:16
B32@0:8@16^B24
B40@0:8@16I24I28^@32
v24@0:8Q16
v24@0:8@16
i
B40@0:8@16@24@32
B52@0:8@16@24I32I36S40^@44
B40@0:8I16@20B28^@32
@32@0:8:16@24
B24@0:8:16
Q16@0:8
q28@0:8i16^@20
B44@0:8@16S24I28I32^@36
v20@0:8I16
B56@0:8@16@24I32@36B44^@48
B20@0:8I16
B16@0:8
B32@0:8@\"NSUUID\"16^@24
@\"NSObject<UMFilesystemProviding>\"
B32@0:8@\"NSString\"16^B24
B48@0:8@\"NSString\"16@\"NSString\"24^@32@?<i@?ii@\"NSString\"@\"NSString\">40
@24@0:8@16
B48@0:8@16I24@28B36^@40
B56@0:8@\"NSUUID\"16@\"NSData\"24@\"NSData\"32I40B44^@48
B44@0:8@\"NSString\"16I24@\"NSUUID\"28^@36
v16@0:8
Vv16@0:8
q
@\"UMLSideEffects\"
B48@0:8i16B20@24@32^@40
B24@0:8@16
i32@0:8@\"NSString\"16^@24
q16@0:8
B32@0:8@16@24
@\"NSDate\"
B48@0:8@16@24^@32@?40
I
@32@0:8@16^@24
B
@16@0:8
Q
@36@0:8@16I24^@28
B40@0:8@16@24#32
B40@0:8I16@\"NSData\"20B28^@32
#16@0:8
B36@0:8i16@20^@28
B40@0:8@\"NSString\"16I24I28^@32
v24@0:8q16
B64@0:8@16@24@32@40@48^@56
B32@0:8@16^@24
B36@0:8@\"NSString\"16I24^@28
i32@0:8@16^@24
B36@0:8@16S24^@28
B56@0:8@16@24@32I40B44^@48
B36@0:8@\"NSUUID\"16I24^@28
B48@0:8@\"NSUUID\"16I24@\"NSData\"28B36^@40
@\"UMLUserManifest\"
B40@0:8@\"NSString\"16@\"NSString\"24^@32
B36@0:8@\"NSString\"16S24^@28
v20@0:8B16
@\"NSData\"32@0:8@\"NSString\"16^@24
@\"NSMutableArray\"
I16@0:8
B56@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36B44^@48
B40@0:8@\"NSData\"16@\"NSString\"24^@32
B36@0:8i16@\"NSString\"20^@28
B28@0:8I16^@20
B44@0:8@16I24@28^@36
@\"NSData\"32@0:8@\"NSData\"16^@24
B24@0:8#16
B24@0:8@\"Protocol\"16
v20@0:8i16
B36@0:8@16I24^@28
B44@0:8@\"NSUUID\"16I24@\"NSData\"28^@36
B32@0:8@\"NSString\"16^@24
@40@0:8:16@24@32
^{_NSZone=}16@0:8
i16@0:8
Set Primary on new 501 OTI, all parts successful
Successful setting of ownershup of file:%{public}@ with uid:%d
Failed to determine size of buffer to read OSEnvironment value(%s). Assuming running in normal mode
Ignored bootstrap mountpoint %{public}@ to AKS identity session
Unlocked AKS identity in session %u
Calling aks_verify_password_with_acm for user:%d
Removed file: %{pubilc}@
Unable to force UnMount SDV at given location
501 AKS Identity already loaded, failure
unmounted UDV on error path
Failed to set aks bootstrap
No uuid available for the Primary user
Failed to atomically write %{public}@: write(%d, <data>, %lu) failed: %{darwin.errno}d
Added the user to the manifest and updated the manifest to Disk
Failed to load user AKSIdfentity with error, bailing
Failed to mount the UDV with error, unload identity, bailing..
could not find user with error:%@
unable to scan IORegistry
Volume is UnEncrypted
Ignored mapping volume %{public}@ to AKS identity session %u (persona: %{public}@)
Ignored unmapping volume %{public}@ from AKS identity
Warning: failed to create write barrier when writing %{public}@: fcntl(%d, F_BARRIERFSYNC) failed: %{darwin.errno}d
UMD: Found keybag Blob
Cannot wait for pid: %s
AKSVolumeMap(%{public}@, %u, %{public}@) failed: %{public}@
Skipping AKS setup
Failed to load user manifest: Failed to parse user manifest
Running in OS environment: %s
newUser.userUUID:%@
newUser.userType:%@
Failed to unwrap data: aks_unwrap_key failed: kAKSReturnDecodeError
Failed to convert array into binary plist: %@
removefile_state_set(REMOVEFILE_STATE_ERROR_CONTEXT) failed: %{darwin.errno}d
While removing path, unset UF_IMMUTABLE on \"%{public}s\"
copyfile: Error: could not chown %{public}@
Found Existing User Uid:%d
Unable to spawn %s
Warning while atomically writing %{public}@: close(%d) failed: %{darwin.errno}d
Failed to lchown path %{public}@ to %d/%d: %{darwin.errno}d
COPYFILE_FINISH: Changing %{public}@ to uidgid:%d
sysctl_fsid failed with error:%d
Failed to parse user homedir path, skipping..
AKSVolumeUnmap(%{public}@) failed: %{public}@
Failed to get data with contents of file %{public}@: %{darwin.errno}d
Warning while atomically writing %{public}@: unlink(%{public}@) failed: %{darwin.errno}d
failed to unload the Bootstrap idenitity in the end
NOT in DRE with error:%@
Copying Starting from %@ to %@
Unloaded AKS identity from session %u
verified AKS identity in session %u
Failed to atomically write %{public}@: Failed to atomically swap writing file: %{darwin.errno}d
updating the user home dir mount volume details
Invalid Parameters, returning error
Failed to copy contents from %{public}@ to %{public}@
Successfully copied contents from %{public}@ to %{public}@
Failed to load user manifest: Failed to read user manifest file from disk
Failed to parse dictionary plist from data: plist is not an array
Changed passcode of AKS identity: %{public}@
removefile(\"%{public}@\", REMOVEFILE_RECURSIVE) failed: %{darwin.errno}d
While removing path, failed to remove path \"%{public}s\": %{darwin.errno}d
Failed to set chown  on volume mounts directory %{public}@
Volume is Encrypted
no APFS containers found
UMLUser-Not existing type or invalid type
AKSIdentityDelete(%@) failed: %{public}@
aks_verify_password(-%u) failed: %{mach.errno}d
Failed to atomically write %{public}@: open_dprotected_np(%{public}@) failed: %{darwin.errno}d
Failed to map the UDV with error, unload identity, bailing..
Replacing Existing User with new content
Failed to get manifest data with bailing...
Failed to allocate buffer to read OSEnvironment value. Assuming running in normal mode
newUser.uid:%d
aks_get_system(%u) failed: 0x%x
Failed to parse array plist from data: %{public}@
Deleted AKS identity %{public}@
While removing path, lstat(\"%{public}s\") failed: %{darwin.errno}d
Failed to login with identity UDV with error, bailing
Failed to create user manifest path, bailing...
Found Primary User Volume:%s  isEncrypted:%s
Failed to parse user gid, bailing..
Failed to wrap data: data is too large: %lu
AKSIdentityUnlockSession(%u) failed: %{public}@
Invalid manifest user, could not get the dictionary
Failed to mount the volume with error %d
Failed to parse user type, bailing..
Failed to parse user first name, bailing..
Failed to convert dictionary into binary plist: %{public}@
AKSIdentityDeletePersona(%u, %{public}@) failed: %{public}@
Failed to generate user dictionary to save in the manifest, returning error
Unable to mount SDV at given location
Adding the user to UserArray
failed to write to FS with error %@
 Skipping the diskNode:%@ as its not in the Boot Container
aks_unlock_device(-%u) failed: %{mach.errno}d
Copyfile from %{public}@ to %{public}@ stopped at handler request
No user uuidstring on the user manifest on the given SDV Path
501 AKS Identity already not loaded, failure
Failed to parse user APNSID, skipping..
Failed to parse user UUID, bailing..
Created AKS identity: %{public}@
Calling aks_verify_password for user:%d
Atomically wrote data to file %{public}@
Failed to remove file %{public}@: unlink failed: %{darwin.errno}d
While removing path, lchflags(\"%{public}s\") failed: %{darwin.errno}d
Out of Memory!!! could not allocate dict, exiting....
newUser.apnsID:%lld
Unable to recreate Primary user Identity with bootstrap user
Failed to delete primary user Identity, bailing
newUser.gid:%d
AKS Identity for session %u loaded
Loaded AKS identity %@ into session %u
Mapped volume %{public}@ to AKS session %u (persona: %{public}@)
removefile(\"%{public}@\", REMOVEFILE_RECURSIVE) failed with ENOENT, ignoring...
Adding and Saving the manifest
Failing to set Primary, return error
Failing to delete 501 OTI after failure to set Primary
bootstrap user Unlaoded 
Failed to AKSVolumeBootstrapFS(%{public}@, %d): %{public}@
Failed to get data with contents of file %{public}@: %{public}@
removefile_state_set(REMOVEFILE_STATE_ERROR_CALLBACK) failed: %{darwin.errno}d
Invalid user uuid string on the user manifest on the given SDV Path
failed to unload the AKS identity
Unable to force unmap UDV at given location
Invalid parameter, no system or user path
Updating the user with User Vol properties
Primary user Identity unloaded
Failing to unload 501 OTI after successful setting of Primary
Unmapped volume %{public}@ from AKS session
Failed to atomically write %{public}@: fsync(%d) failed: %{darwin.errno}d
AKSIdentityLogin(%@, %u) failed: %{public}@
Logged AKS identity %@ into session %u
User manifest version does not exist or is wrong type
No manifest on the SDV Path
Failed to atomically write %{public}@: Failed to atomically swap writing file: %{darwin.errno}d, then failed to rename file: %{darwin.errno}d
Failed to add or write the manifest, returning error
Now AKSVolumeBootstrapFS with uid:%d
Creating Bag Dir as it doesnot exit
Failed to set permissions on volume mounts directory %{public}@
Running in DeviceRecoveryEnvironment\n
BootDevice is %@
getmntfsid failed with error:%d
Failed to chmod path %{public}@ to %o: %{darwin.errno}d
updated the User and the on disk manifest
Manifest Write Successful
Failed to parse user last name, bailing..
Failed to atomically write %{public}@: write(%d, <data>, %lu) only wrote %ld bytes
While removing path, failed to unlink \"%{public}s\" after removing UF_IMMUTABLE: %{darwin.errno}d
Failed to create manifest for the User, returning error..
Failed to unload primary user Identity, bailing
Primary user Identity not Present, continue with the creation of the Identity
Primary user Identity DELETED
Failed to parse user display name, bailing..
AKSIdentityAddPersona(%u, ..., %{public}@,) failed: %{public}@
Added persona %{public}@ to AKS session %u
Unable to locate UDV on the booted container
aks_lock_device after check failed with Error:%d
Failed to parse user uid, bailing..
AKSIdentityLoad(%@, %u) failed: %{public}@
Copyfile from %{public}@ to %{public}@ failed: %{darwin.errno}d
While removing path, removefile_state_get(REMOVEFILE_STATE_ERRNO) failed: %{darwin.errno}d
While removing path, ignoring missing file \"%{public}s\"
Failed to find Primary USER volume
Failed to parse user alternateDSID, skipping..
AKSIdentityLoginWithACMCred(%@, %u) failed: %{public}@
Failed to parse user libinfo path, bailing..
Read data from file %@
Removed path \"%{public}@\"
Primary user Identity Refreshed, load the identity to set Primary
No primary user in the manifest
Created ManifestDir Path 
Writing to the FileSytem Manifest
unable to fetch IORegistry properties
AKSIdentityUnload(%u) failed: %{public}@
Failed to wrap data: aks_wrap_key failed: %{mach.errno}d
Deleted persona %{public}@ from AKS session %u
Failing to unload 501 OTI after failure to set Primary
Unable to determine OS environment: %d:(%s)\n
Found SystemData Volume:%s isEncrypted:%s
Failed to find SDV
Found DiskNode: %@ within the Boot Container
Failed to unwrap data: data is too large: %lu
Did not remove file %{public}@: file did not exist
Failed to remove all files for path \"%{public}@\": %{darwin.errno}d
No primary user manifest on the SDV Path
Forced unmount of VARMOBILE failed with %s
newUser.alternateDSID:%@
Failed to parse user name, bailing..
AKSIdentityUnlockSessionWithACMCred(%u) failed: %{public}@
bootstrap user LOADED
Failed to load Primary UID after recreating, bailing
user with no opaqueData
Container: %@, volumeDiskNode:%@
Unlocked AKS identity %u
Failed to atomically write %{public}@: unlink(%{public}@) failed: %{darwin.errno}d
Failed to create path %{pubilc}@: mkpath_np failed: %{darwin.errno}d
VALID primary user with UUID
Failing to delete 501 after load failure
failed to unmount UDV on error path
Unable to force unmap UDV with error %@
APFSContainerGetBootDevice failed with %d, bailing..
AKSIdentityCreate(%@, %u) failed: %{public}@
Failed to parse dictionary plist from data: %{public}@
Failed to parse dictionary plist from data: plist is not a dictionary
AKSIdentityChangePasscode(%@, %u) failed: %{public}@
Failed to load bootstrap user with the token, bailing
501 AKS Identity is not loaded, returning success
Successfully set aks bootstrap
Failed to unwrap data: aks_unwrap_key failed: %{mach.errno}d
AKS Identity for session %u not loaded
Failed to parse user manifest: manifest data is invalid
Primary user manifest exists on the SDV Path
MKBUserSessionDisplayName
MKBUserSessionVolumeDeviceNode
-o
nosuid
MKBUserSessionGroupID
sideeffect
%@.writing
2457711A-523C-4604-B75A-F48A571D5036
FALSE
MKBUserSessionFirstLoginEndTime
MKBUserSessionRequiresPasscode
device-recovery
MKBUserSessionDisabled
MKBUserSessionKeybagOpaqueData
MKBUserSessionCachedLoginEndTime
MKBUserSessionVolumeFSType
SYNCBLOB
MKBUserSessionLibinfoHomeDir
MKBUserSessionLoginUser
DEVICECONFIG
APNSID
SYNCENT
mobile
MKBUserSessionLoginTimeStamp
UUID
MKBUserSessionCreateTimeStamp
MKBUserSessionDirty
MKBUserSessionVolumeUUID
v8@?0
legacy
DEVICENETWORKBG
MKBUserTypeKey
MKBUserSessionFirstLoginStartTime
USESSTYPE
MKBUserSessionisPrimary
MAXUSERSIZE
BOOTEDUSER
MKBUserSessionID
MKBUserSessionShortName
MKBUserSessionLastName
/keybags/usersession.kb
BSD Name
vfs.generic.ctlbyfsid
NUMENT
BLOB
en_US
%@/mobile
/sbin/mount_apfs
IOService
MKBUserSessionNeedsMount
MKBUserSessionHasSyncBag
Unexpected composed log message.
default
MKBUserSessionLanguage
%@/System/Library/Templates/User/
MKBUserSessionAuditor
MKBUserSessionOpaque
LOGINCHECKIN
UserSessionOther
MKBUserSessionForeground
Encrypted
UserVolumeAPFSNative
AppleAPFSContainer
MKBUserSessionHomeDir
MKBUserSessionisAdminKey
/keybags
UserManifestVersion
MKBUserSessionFirstName
MKBUserSessionName
nodev
User
MKBUserSessionAPNSID
i32@?0i8i12@\"NSString\"16@\"NSString\"24
userlayout
com.apple.UserManagementLayout
MAXUSER
LRUENT
Data
RoleValue
MKBUserSessionFileInfo
MKBUserSessionAlternateUUID
hw.osenvironment
TRUE
LRUBLOB
MKBUserSessionUUID
/var/mobile
AppleAPFSVolume
MKBUserSessionCachedLoginStartTime
UMAppleKeyStoreProviding
UMUUIDHelper
UMFilesystemProvider
UMFilesystemProviding
UMLUserManifest
UMLManager
UMLUser
UMSerializationHelper
UMAppleKeyStoreProvider
UMLProviderSideEffects
UMLSideEffects
NSObject
Private
T@\"NSString\",C,N,V_fsVolumeType
setIsAdminUser:
_hasSyncBag
dataWithBytes:length:
lastLoginEnd
needsMount
readUserFromManifest:forUserUid:withError:
_syncUserList
dataWithContentsOfFile:error:
setFirstLoginStart:
setUserUUID:
T@\"NSMutableArray\",C,N,V_lruList
setLibInfoPath:
deletePersonaWithUUID:fromSession:error:
manifestFromData:
setIsAuditor:
volumeUUID
_keybagOpaqueData
code
isPrimaryUser
setLastBootedUser:
lruList
_loginuiCheck
_maxUsers
_userType
defaultManager
setHomeDirPath:
Ti,N,V_lastBootedUser
numberWithInt:
setNetworkBG:
_firstLoginStart
gid
Ti,N,V_deviceConfig
lastLoginStart
setFsVolumeType:
T@\"NSString\",C,N,V_username
UUID
removeAnUser:fromUserManifest:saveToPath:
setUserType:
_dataValue
_fsVolumeType
_libInfoPath
_volumeUUID
dictionary
loginIdentity:intoSession:passcode:isACMCredential:error:
_firstName
loginuiCheck
_gid
T@\"NSString\",C,N,V_lastName
class
homeDirPath
removeFileAtPath:error:
userInfo
apnsIDStart
fsVolumeType
generation
lastBootedUser
setLastName:
T#,R
_se
TB,N,V_isAdminUser
_homeDirPath
isLoginUser
performSelector:withObject:withObject:
setLoginuiCheck:
setSyncUserList:
TB,N,V_isPrimaryUser
closeFileWithDescriptor:
isAuditor
opaqueData
unloadIdentityFromSession:error:
sizeOfFileWithDescriptor:error:
addPersonaWithUUID:toSession:passcode:error:
hash
mountVolumeAtPath:fromDevice:forUserUID:userGID:withMode:withError:
stringWithString:
unmountSystemDataVolumeAt:withError:
unsignedIntValue
T@\"NSString\",C,N,V_userType
userSessionType
TB,N,V_isAuditor
_fileInfoPath
bootstrapVolumeWithMountPoint:user:error:
createPrimaryUserLayoutWithOnUserVolumePath:fromSystemVolumePath:withError:
lastName
maxUsers
firstLoginStart
T@\"NSData\",C,N,V_keybagOpaqueData
_version
appendString:
keybagOpaqueData
setLastLoginEnd:
setVersion:
setIsLoginUser:
_isAuditor
objectForKey:
T@\"NSData\",C,N,V_opaqueData
clonePath:toPath:error:handler:
setHasSyncBag:
superclass
unmountUserDataVolumeOnSystemDataAt:withError:
zone
T@\"NSString\",C,N,V_volumeUUID
UUIDString
atomicallyWriteData:toPath:error:
debugDescription
init
isDisabledUser
setDiskNode:
setGeneration:
setApnsIDStart:
setUid:
TB,N,V_isLoginUser
dataUsingEncoding:
initWithUUIDString:
length
stringWithCString:encoding:
username
refreshPrimaryUserOnSharedDataVolumePath:withBootstrapToken:withError:
unsignedLongLongValue
_cachedLoginEnd
T@\"NSString\",C,N,V_homeDirPath
T@\"NSString\",C,N,V_diskNode
setGracePeriod:
Ti,N,V_userSessionType
_username
apnsID
saveManifest:toPath:
T@\"NSDate\",C,N,V_lastLoginEnd
setIsDirty:
setKeybagOpaqueData:
setValue:forKey:
unlockIdentityInSession:passcode:isACMCredential:error:
userType
_isDisabledUser
boolValue
bytes
libInfoPath
setAlternateDSID:
setVolumeUUID:
userManifestDictionary
alternateDSID
countByEnumeratingWithState:objects:count:
createUserLayoutForUserwithUserID:withAKSSetup:onUserVolumePath:fromSystemVolumePath:withError:
displayName
domain
isProxy
Tq,N,V_maxUserSize
_displayName
numberWithBool:
TB,N,V_isDisabledUser
_alternateDSID
_userSessionType
diskNode
firstName
makePath:mode:error:
T@\"NSDate\",C,N,V_lastLoginStart
T@\"NSDate\",C,N,V_cachedLoginStart
_lastName
keybagOpaqueDataOnSharedDataVolumePath:withError:
setCreationDate:
T@\"NSDate\",C,N,V_firstLoginStart
Ti,N,V_gid
_filesystem
_isDirty
_isLoginUser
_userUUID
T@\"NSData\",&,N,V_dataValue
_gracePeriod
_userLanguauge
fileExistsAtPath:isDirectory:
setFirstName:
setObject:forKeyedSubscript:
userFromManifestDictionary:
userUUID
autorelease
readUserManifestOnSharedDataVolumePath:withError:
self
setUsers:
_cachedLoginStart
_diskNode
deviceConfig
gracePeriod
intValue
setFirstLoginEnd:
unlockIdentity:passcode:isACMCredential:error:
T@\"NSString\",R,C
release
uid
description
fileInfoPath
updatePrimaryUser:onSharedDataVolumePath:withDiskNode:withVolumeuuid:withVolumeName:withError:
Tq,N,V_apnsID
_manifest
setCachedLoginEnd:
Ti,N,V_maxUsers
T@\"NSDate\",C,N,V_creationDate
chownPath:toUser:group:error:
openFileForAppendingAtPath:error:
retainCount
setOpaqueData:
isDirty
T@\"NSString\",C,N,V_libInfoPath
T@\"NSMutableArray\",C,N,V_syncUserList
removeObject:
replaceObjectAtIndex:withObject:
_lastBootedUser
isKindOfClass:
Tq,N,V_apnsIDStart
TB,N,V_isDirty
addNewUser:toUserManifest:saveToPath:
isForeground
mountSystemDataVolumeAt:withError:
removePath:error:
_isPrimaryUser
isIdentityLoadedIntoSession:
setUserLanguauge:
T@\"NSDate\",C,N,V_cachedLoginEnd
TB,N,V_hasSyncBag
TB,N,V_needsMount
hasSyncBag
isEqualToString:
numberWithUnsignedInteger:
setIgnoreIdentityMethods:
setGid:
version
T@\"NSString\",C,N,V_firstName
_apnsIDStart
dataWithPropertyList:format:options:error:
loadManifestFromSharedDataVolumePath:
performSelector:
setApnsID:
TB,N,V_isForeground
TQ,N,V_generation
_firstLoginEnd
mutableCopy
unmapVolume:error:
TI,N,V_version
_generation
TB,N,V_ignoreIdentityMethods
_aks
_networkBG
chmodPath:withMode:error:
createPrimaryUserOnSharedDataVolumePath:withError:
creationDate
loadIdentity:intoSession:error:
Ti,N,V_networkBG
count
createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:isACMCredential:error:
dataUnwrappingDataWithDeviceClassF:error:
dataValue
isAdminUser
sharedManager
TB,N
cachedLoginEnd
fixupPath:withMode:toUser:group:error:
setDeviceConfig:
updateUser:inManifest:withDiskNode:volumeUUID:volumeName:withSharedDataVolumePath:withError:
writeToFileWithDescriptor:string:error:
T@\"NSMutableArray\",C,N,V_users
T@\"NSString\",C,N,V_userLanguauge
errorWithDomain:code:userInfo:
ignoreIdentityMethods
T@\"NSString\",C,N,V_fileInfoPath
Ti,N,V_gracePeriod
_lastLoginEnd
cachedLoginStart
isValidClassTypeinDictionary:withKey:withType:
objectForKeyedSubscript:
_apnsID
addObject:
conformsToProtocol:
mapVolume:toSession:withPersona:error:
Ti,N,V_uid
_opaqueData
dateWithTimeIntervalSince1970:
isEqual:
primaryUserOnSharedDataVolumePath:withError:
T@\"NSString\",C,N,V_alternateDSID
T@\"NSString\",C,N,V_userUUID
verifyIdentityPasswordInSession:passcode:isACMCredential:error:
dataWithContentsOfFile:options:error:
mountUserDataVolumeOnSystemDataAt:withSecret:withError:
renameFileFromPath:toPath:error:
setLruList:
setUserSessionType:
_lastLoginStart
Ti,N,V_version
firstLoginEnd
mountUserDataVolumeOnSystemDataAt:withACMCredential:withError:
propertyListWithData:options:format:error:
maxUserSize
stringWithUTF8String:
unMountVolumeAt:withError:
setIsDisabledUser:
setIsPrimaryUser:
setDisplayName:
_isForeground
_maxUserSize
dataWrappingDataWithDeviceClassF:error:
isMemberOfClass:
longLongValue
performSelector:withObject:
setDataValue:
T@\"NSString\",C,N,V_displayName
setFileInfoPath:
setIsForeground:
syncUserList
.cxx_destruct
T@\"NSDate\",C,N,V_firstLoginEnd
Ti,N,V_loginuiCheck
networkBG
setLastLoginStart:
T@\"NSString\",?,R,C
TQ,R
_deviceConfig
dataWithData:
setNeedsMount:
setUsername:
users
_creationDate
_ignoreIdentityMethods
_isAdminUser
_lruList
_users
changeSecretrForIdentityWithUUID:oldPasscode:newPasscode:existingSession:isACMCredential:error:
deleteIdentity:error:
respondsToSelector:
UTF8String
_uid
numberWithLongLong:
retain
setWithArray:
stringWithFormat:
userLanguauge
T@\"NSData\",R,N
inDeviceRecoveryEnvironment
setMaxUsers:
_needsMount
setCachedLoginStart:
setMaxUserSize:
```
