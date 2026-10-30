# `/usr/lib/libpartition2_dynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 214,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 3872)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libpartition2_dynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (5 classes, 0 protocols)

Classes: `LPAPFSContainer`, `LPAPFSPhysicalStore`, `LPAPFSVolume`, `LPMedia`, `LPPartitionMedia`

## Strings (451)

```
%s : Failed to encode snapshot name %{private}s for some reason.
%s: path is a snapshot, but has no name: %{private}@
Cleaned up temporary mount point
%s : volume is missing a dev node somehow
%s: Error getting snapshot info for %@: %@
%s: No snapshot is tagged for boot and none match the naming scheme
%s: Volume is not mounted. Unable to set name\n
%s : You need to specify a volume name.
%s : Volume name is invalid
%s : Paired volume is not valid if role is not system.
Can not mount (%{private}s) because we could not create its mount folder (%{private}s).
%s called but %{private}@ is not mounted.
%s : Failed to delete snapshot: %{private}@, %d
%s : Waiting for snapshots to delete timed out
%s: Failed to unmount volume with error: %d
Volume is already mounted at %@, skipping re-mount
Unmount failed with EINVAL, will assume race. Ignoring error.
Unmounted %@ ( %{private}@ )
%s: Mount point is %{private}@\n
posix_spawn %s failed: %s
%s: Failed to get IOMedia objects
%s: No disk for %{private}@
%s: statfs failed: %d (%s)
%s: Failed to find primary media
%s : Failed to open media for snapshot delete: %d
%s: Failed to remount volume with error: %d
%s: Parent of disk backing %{private}@ is not an APFS volume
IOKit wait timed out, volume for media may be stale.
Failed to find media for %@
%s : IOIterator was still invalid after attempting %d times
%s : Container is somehow missing a BSD name.
%s : Container isn't a container?!
revert snapshot operation failed: %d %s
Could not reset metadata on %{private}s: %s
Deleting contents of %{private}s %s (result: %d).
Could not removefile(3) path %{private}s: %s
Failed to create partition media iterator.
%s : Paired volume must be in the same container
%s : going to delete apfs volume ( %@ )
%s : Need a valid new snapshot name.
Deleting contents of %{private}s...
pipe failed while preparing to execute %s: %s
Mounted %@ at %{private}@
Failed to unmount %@ **FORCING UNMOUNT** error: %d
%s : Error in reading attributes for directory entry %d
%s was stopped by signal %d
%s : Creating APFS volume %s with options: %@
%s: failed to get role. Error: %d
%s called on device with no dev node
Can not mount (%@) because mount returned %d.
%s : failed with posix error: %d
%s : fs_snapshot_list failed with error %d
%s: failed to get read-only status for %@\n
%s : Add volume failed with error: %d.
%s : Unable to get the iterator for entry.
%s : failed with unknown kern_return_t error: %d
waitpid failed for %s: %s
%s: No media found for path: %{private}@
Failed to unmount %@ retry: %s error: %d
Failed to clean up temporary mount point: %d
Was asked asked to unmount (%@) but is not mounted.
%s : Could not open device mount %{private}@.
%s: no filesystem for %@ (%d): %s
%s: Failed to obtain parent IOMedia for disk at path %{private}@
%s: Failed to set name for volume: %s\n
IOKit service wait timed out, volumes may be stale.
Couldn't create a temporary mount point %s
create snapshot operation failed: %d %s
%s: no IOMedia for %@ (device 0x%lx)
%s: Successfully set volume name to %{private}@\n
%s : failed to read value for property named: %@
Timed out waiting for: %@
%s : APFSVolumeCreateForMSU exists and we're creating a System volume. Preferring it to APFSVolumeCreate.
%s : Failed to get content type.
%s was terminated by signal %d
Failed to call APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ with errno %d\n
%s : Can not iterate over physical store services.
Can not mount (%s) because it does not appear to have a device node.
Volume is already mounted at %@, attempting to re-mount at %@
Mounted %@, Snapshot( %{private}@ ) at %{private}@
%s : failed with iokit error: %d
%s: Trying to determine mount point\n
%s: could not parse %s %{private}s: %{private}@
%s : Failed because target volume is not mounted
mount_apfs %@ returned %d, retrying (%d)
Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n
%s : Need a valid snapshot name.
%s : Could not open device is not mounted.
rename snapshot operation failed: %d %s
%s: Skipping unmount/remount of %@
%s : Could not set root from snapshot. Errno: %d
%s : Need a valid snapshot names.
%@
%s: could not look up snapshot by UUID: %d (%s)
%s: %@ isn't an APFS volume
%s: Not on a rooted snapshot disk, will return self: %{private}@
%s : Unable to get parent iterator
%s: failed to get journaled status for %@\n
%s : Requested system volume with sibling but the key is not supported.
%s : Unable to open mount point %{private}@: %d
@%@
/sbin/mount_apfs
-s
Solid State
-[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]
/private/xarts
LPAPFSSnapshotPropertyKeyMarkedForRoot
/dev/
%@: %@, UUID: %@
/mnt11
-o
no
q24@?0@\"NSDictionary\"8@\"NSDictionary\"16
AppleAPFSVolume
LPAPFSVolumeMountOptionNoBrowse
xART
iDiags
+[LPMedia liveMediaForSnapshotAtPath:]
Protocol Characteristics
/mnt8
/System/Volumes/Update
@
-n
EmbeddedDeviceTypeRoot
Vendor Name
deviceModel
GUID_partition_scheme
Content
/private/var/internal
/private/var/mobile
Hardware
-[LPAPFSPhysicalStore parent]
LPAPFSVolumeSnapshotMountPointKeyName
Data
failed
Medium Type
/mnt4
Backup
nobrowse
BSD Name
%@: %@
-[LPAPFSPhysicalStore role]
/private/var/wireless/baseband_data
i
IOProviderClass
LPAPFSVolumeMountOptionReadOnly
LPAPFSVolumeUnmountOptionSnapshotName
-[LPAPFSVolume role]
AppleAPFSMedia
+[LPMedia mediaForPath:snapshotName:]
UUID
IOParentMatch
41504653-0000-11AA-AA11-00306543ECAC
/mnt10
/private/var/hardware
Baseband Data
tmp-mount-
/mnt1
/private/var/logs
-[LPAPFSVolume eraseVolumeWithError:]
/var/mnt//tmp-mount-XXXXXX
-[LPAPFSVolume renameSnapshot:to:error:]
/dev/%@
-[LPAPFSVolume revertToSnapshot:options:error:]
69646961-6700-11AA-AA11-00306543ECAC
/private/var/
Update
SideCar
CaseSensitive
/var/mnt/
BSD Major
-restore
52637672-7900-11AA-AA11-00306543ECAC
/mnt3
LPAPFSVolumeRevertOptionSkipRemount
Recovery
Preboot
com.apple.os.update-
-[LPAPFSVolume snapshotInfoWithError:]
-[LPAPFSVolume createSnapshot:error:]
IORegistryEntryID
LPAPFSVolumeUnmountOptionAll
LPAPFSVolumeSnapshotMountPointKeyMountPoint
LPAPFSSnapshotPropertyKeyMarkedForRevert
yes
AppleAPFSSnapshot
v8@?0
EF57347C-0000-11AA-AA11-00306543ECAC
System
BSD Minor
/
Rotational
-[LPMedia isJournaled]
IOPropertyMatch
-[LPAPFSVolume deleteVolumeWithError:]
v12@?0I8
Baseband data
Whole
-[LPAPFSVolume snapshotMountPoints]
succeeded
FireWire Vendor Name
+[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]
%@s%d
Internal
v16@?0r^{?=iS@@}8
/dev/console
-[LPMedia wholeMediaForMedia]
Model Number
Physical Interconnect Location
Apple_partition_scheme
LPAPFSVolumeMountOptionSnapshotName
LPAPFSSnapshotPropertyKeyName
-[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]
Model
+[LPMedia _copyIOMediaForDiskWithPath:]
-[LPMedia(Private) getPropertyWithName:]
VolGroupUUID
/mnt6
q24@?0@8@16
%s\n
IOBlockStorageDevice
+[LPMedia snapshotNameForMediaForPath:]
FDisk_partition_scheme
s
/private/var/recovery/
User
VM
Enterprise data
/mnt5/tmp-mount-XXXXXX
com.apple.IOKit
kern.bootargs
-[LPAPFSContainer physicalStores]
LPAPFSVolumeMountOptionNoFirmlinks
LPAPFSVolumeUnmountOptionDoNotLock
Installer
_Bool iterateSafely(io_iterator_t, int, void (^__strong)(io_object_t), void (^__strong)(void))
IOMedia
Device Characteristics
-[LPMedia setName:withError:]
%@: %@, Mount: %@
-[LPAPFSVolume rootToSnapshot:error:]
+[LPAPFSContainer _containerWithPhysticalStoreRole:]
IOService
/private/var/vm
LPAPFSVolumeUnmountOptionForce
+[LPMedia allMedia]
rdonly
mount_apfs returned : %d
Mount failed
com.apple.MobileSoftwareUpdate
7C3457EF-0000-11AA-AA11-00306543ECAC
.XXXXXXXX
RoleValue
/mnt5
%.*s
libpartition2
-[LPMedia isReadOnly]
/mnt7
/mnt2
LPAPFSSnapshotPropertyKeyXID
Private
LPPartitionMedia
LPAPFSContainer
LPAPFSPhysicalStore
LPAPFSVolume
LPMedia
lastObject
mountAtTemporaryPathWithError:
name
stringByDeletingLastPathComponent
getPropertyWithName:
mediaForPath:
role
snapshotMountPoints
snapshotsWithError:
volumesWithRole:
T@\"NSDictionary\",R
_ioMedia
compare:
pairedVolume
waitForIOMediaWithDevNode:
boolValue
defaultVolumeNameGivenRole:
dictionaryWithObjects:forKeys:count:
mediaForPath:snapshotName:
primaryMedia
setIoMedia:
count
description
initWithBytes:length:encoding:
initWithFormat:arguments:
mediaForUUID:
mountPoint
objectForKeyedSubscript:
setName:withError:
arrayWithObjects:count:
hasSuffix:
init
substringFromIndex:
addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:
devNodePath
isEqual:
sortUsingComparator:
numberWithUnsignedLongLong:
recoveryVolume
snapshotNameForMediaForPath:
getCString:maxLength:encoding:
numberWithUnsignedShort:
parent
setRole:withError:
BSDName
initWithIOMediaObject:
mediaForPath:isSnapshot:
storageMedium
substringToIndex:
unmountWithError:
TI,R
addObject:
isMounted
liveMediaForSnapshotAtPath:
objectAtIndexedSubscript:
updateVolume
contentTypeToSubclassMap
errorWithDomain:code:userInfo:
hasEmbeddedDeviceTypeRoot
objectForKey:
sortedArrayUsingComparator:
componentsSeparatedByString:
container
enumerateRoleMetadataUsingBlock:
initialize
mountAtTemporaryPathWithOptions:error:
_copyLiveFilesystemIOMediaForRootedSnapshot
children
dictionaryWithDictionary:
intValue
isFilevaultEncrypted
mediaUUID
volumeGroupUUID
deleteSnapshots:waitForDeletionFor:error:
mediaForBSDNameOrDeviceNode:
objectAtIndex:
pairedVolumeWithRole:
removeAllObjects
isJournaled
length
_containerWithPhysticalStoreRole:
TB,R
TI,V_ioMedia
_createTemporaryMountPointWithError:
defaultMountPointGivenRole:
dictionary
isPrimaryMedia
physicalStores
numberWithInt:
containsString:
isWhole
caseInsensitiveCompare:
dictionaryWithCapacity:
mountAtPath:error:
rangeOfString:options:
volumesWithRole:group:
contentTypesForPartitionMedia
countByEnumeratingWithState:objects:count:
supportedContentTypes
vendorName
volumes
T@\"NSArray\",R
dealloc
_deviceCharacteristicStringForKey:
deviceModel
diagsContainer
hardwareVolume
isEmbeddedDeviceTypeRoot
mountAtPath:options:error:
stringWithCString:encoding:
hasPrefix:
prebootVolume
copy
fileSystemRepresentation
isEncrypted
revertToSnapshot:error:
snapshotInfoWithError:
stringWithUTF8String:
waitForBlockStorage
mountWithError:
stringByResolvingSymlinksInPath
arrayWithArray:
ioMedia
xARTVolume
IOMainPort
_matchVolumesWithRole:group:
isInternal
recoveryContainer
stringWithFormat:
deleteVolumeWithError:
VMVolume
roleMetadataForRole:
setObject:forKey:
setObject:forKeyedSubscript:
_copyIOMediaForDiskWithPath:
allAPFSContainers
isCaseSenstive
numberWithLongLong:
allMedia
getBoolPropertyWithName:
isReadOnly
rootToSnapshot:error:
unmountAllWithError:
content
_loadMountPointTableForMode:
getStringPropertyWithName:
renameSnapshot:to:error:
mediaOfCorrectTypeGivenIOMedia:
revertToSnapshot:options:error:
createSnapshot:error:
eraseVolumeWithError:
volumeWithRole:group:
wholeMediaForMedia
isEqualToString:
unmountWithOptions:error:
T@\"LPAPFSVolume\",R
UTF8String
_pathIsTemporaryMount:
arrayWithCapacity:
I
v24@0:8@16
@64@0:8@16i24B28q32q40@48^@56
v24@0:8@?16
B24@0:8^@16
B32@0:8@16^@24
@24@0:8^@16
B40@0:8@16@24^@32
v20@0:8I16
@16@0:8
@20@0:8i16
v16@0:8
v20@0:8i16
r^{?=iS@@}20@0:8i16
B28@0:8i16^@20
@32@0:8@16^@24
B40@0:8@16d24^@32
B24@0:8@16
@24@0:8@16
@32@0:8@16^B24
I24@0:8@16
I16@0:8
@20@0:8I16
@28@0:8i16@20
i16@0:8
B16@0:8
```
