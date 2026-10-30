# `/usr/lib/libpartition2_dynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 214,544 bytes.

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
/private/var/hardware
System
@%@
UUID
-[LPAPFSVolume renameSnapshot:to:error:]
BSD Name
IOService
/private/var/wireless/baseband_data
CaseSensitive
BSD Minor
deviceModel
EF57347C-0000-11AA-AA11-00306543ECAC
User
iDiags
-[LPAPFSVolume snapshotMountPoints]
/dev/
Vendor Name
%@: %@, UUID: %@
-[LPMedia(Private) getPropertyWithName:]
LPAPFSVolumeRevertOptionSkipRemount
/private/var/internal
-[LPAPFSVolume role]
/var/mnt/
Rotational
%@: %@, Mount: %@
s
IORegistryEntryID
7C3457EF-0000-11AA-AA11-00306543ECAC
no
/
v8@?0
IOMedia
/private/var/logs
AppleAPFSMedia
FDisk_partition_scheme
RoleValue
LPAPFSSnapshotPropertyKeyXID
Recovery
nobrowse
Preboot
Baseband data
Baseband Data
Medium Type
GUID_partition_scheme
/private/var/recovery/
%s\n
EmbeddedDeviceTypeRoot
-[LPMedia isReadOnly]
+[LPMedia _copyIOMediaForDiskWithPath:]
+[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]
LPAPFSVolumeUnmountOptionSnapshotName
xART
rdonly
_Bool iterateSafely(io_iterator_t, int, void (^__strong)(io_object_t), void (^__strong)(void))
succeeded
Protocol Characteristics
LPAPFSVolumeUnmountOptionForce
LPAPFSVolumeUnmountOptionAll
-[LPAPFSPhysicalStore parent]
/private/var/
LPAPFSSnapshotPropertyKeyMarkedForRevert
yes
AppleAPFSSnapshot
IOProviderClass
AppleAPFSVolume
LPAPFSVolumeMountOptionSnapshotName
VM
tmp-mount-
52637672-7900-11AA-AA11-00306543ECAC
Internal
/mnt5
-[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]
Device Characteristics
LPAPFSSnapshotPropertyKeyName
/var/mnt//tmp-mount-XXXXXX
-restore
+[LPMedia allMedia]
BSD Major
com.apple.os.update-
Whole
+[LPAPFSContainer _containerWithPhysticalStoreRole:]
-[LPAPFSContainer physicalStores]
v16@?0r^{?=iS@@}8
-[LPMedia setName:withError:]
Model
Solid State
v12@?0I8
SideCar
-o
q24@?0@8@16
-[LPAPFSVolume rootToSnapshot:error:]
/mnt11
LPAPFSVolumeUnmountOptionDoNotLock
/mnt5/tmp-mount-XXXXXX
/sbin/mount_apfs
+[LPMedia snapshotNameForMediaForPath:]
VolGroupUUID
i
/mnt4
LPAPFSSnapshotPropertyKeyMarkedForRoot
.XXXXXXXX
%@: %@
Apple_partition_scheme
/mnt10
@
failed
Backup
-[LPAPFSVolume eraseVolumeWithError:]
Mount failed
IOBlockStorageDevice
69646961-6700-11AA-AA11-00306543ECAC
/mnt7
/private/var/vm
/private/var/mobile
Enterprise data
-[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]
-[LPAPFSPhysicalStore role]
/mnt1
Installer
Update
-s
kern.bootargs
/dev/console
%@s%d
/mnt6
/System/Volumes/Update
LPAPFSVolumeMountOptionReadOnly
LPAPFSVolumeMountOptionNoBrowse
-n
mount_apfs returned : %d
+[LPMedia mediaForPath:snapshotName:]
/mnt2
com.apple.IOKit
-[LPAPFSVolume createSnapshot:error:]
-[LPAPFSVolume revertToSnapshot:options:error:]
q24@?0@\"NSDictionary\"8@\"NSDictionary\"16
-[LPMedia wholeMediaForMedia]
IOPropertyMatch
41504653-0000-11AA-AA11-00306543ECAC
/mnt8
LPAPFSVolumeSnapshotMountPointKeyMountPoint
libpartition2
Model Number
-[LPMedia isJournaled]
LPAPFSVolumeMountOptionNoFirmlinks
Content
/mnt3
/dev/%@
IOParentMatch
LPAPFSVolumeSnapshotMountPointKeyName
-[LPAPFSVolume deleteVolumeWithError:]
-[LPAPFSVolume snapshotInfoWithError:]
FireWire Vendor Name
com.apple.MobileSoftwareUpdate
Physical Interconnect Location
Data
Hardware
%.*s
+[LPMedia liveMediaForSnapshotAtPath:]
/private/xarts
LPAPFSPhysicalStore
LPAPFSVolume
LPMedia
Private
LPPartitionMedia
LPAPFSContainer
intValue
isEncrypted
snapshotsWithError:
unmountAllWithError:
dealloc
allAPFSContainers
isFilevaultEncrypted
mediaForPath:snapshotName:
mountAtTemporaryPathWithOptions:error:
supportedContentTypes
isWhole
arrayWithArray:
componentsSeparatedByString:
hasEmbeddedDeviceTypeRoot
parent
substringFromIndex:
addObject:
description
lastObject
pairedVolume
rootToSnapshot:error:
setRole:withError:
storageMedium
T@\"NSDictionary\",R
ioMedia
getPropertyWithName:
objectForKey:
stringWithUTF8String:
liveMediaForSnapshotAtPath:
name
numberWithUnsignedLongLong:
numberWithUnsignedShort:
children
_createTemporaryMountPointWithError:
objectAtIndexedSubscript:
unmountWithOptions:error:
wholeMediaForMedia
hardwareVolume
objectForKeyedSubscript:
xARTVolume
initialize
mountAtPath:options:error:
mountAtTemporaryPathWithError:
UTF8String
fileSystemRepresentation
initWithBytes:length:encoding:
mediaForBSDNameOrDeviceNode:
objectAtIndex:
addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:
contentTypesForPartitionMedia
copy
deleteVolumeWithError:
devNodePath
isCaseSenstive
_containerWithPhysticalStoreRole:
volumeGroupUUID
deleteSnapshots:waitForDeletionFor:error:
deviceModel
dictionary
isEmbeddedDeviceTypeRoot
mediaUUID
snapshotNameForMediaForPath:
numberWithInt:
_copyLiveFilesystemIOMediaForRootedSnapshot
content
container
isJournaled
isMounted
updateVolume
T@\"LPAPFSVolume\",R
TI,R
arrayWithObjects:count:
renameSnapshot:to:error:
unmountWithError:
revertToSnapshot:options:error:
boolValue
countByEnumeratingWithState:objects:count:
volumesWithRole:group:
waitForIOMediaWithDevNode:
IOMainPort
mediaOfCorrectTypeGivenIOMedia:
count
volumeWithRole:group:
T@\"NSArray\",R
defaultMountPointGivenRole:
getBoolPropertyWithName:
getStringPropertyWithName:
isInternal
recoveryVolume
removeAllObjects
revertToSnapshot:error:
snapshotMountPoints
stringByResolvingSymlinksInPath
_deviceCharacteristicStringForKey:
arrayWithCapacity:
diagsContainer
isPrimaryMedia
VMVolume
_ioMedia
_matchVolumesWithRole:group:
enumerateRoleMetadataUsingBlock:
initWithFormat:arguments:
initWithIOMediaObject:
mountPoint
role
setName:withError:
createSnapshot:error:
dictionaryWithDictionary:
isEqualToString:
mediaForPath:
snapshotInfoWithError:
sortedArrayUsingComparator:
stringWithCString:encoding:
volumesWithRole:
_copyIOMediaForDiskWithPath:
compare:
dictionaryWithObjects:forKeys:count:
hasSuffix:
recoveryContainer
dictionaryWithCapacity:
physicalStores
stringWithFormat:
volumes
allMedia
init
mediaForUUID:
mountAtPath:error:
waitForBlockStorage
containsString:
_pathIsTemporaryMount:
caseInsensitiveCompare:
eraseVolumeWithError:
isEqual:
isReadOnly
roleMetadataForRole:
BSDName
TB,R
TI,V_ioMedia
_loadMountPointTableForMode:
hasPrefix:
length
numberWithLongLong:
rangeOfString:options:
errorWithDomain:code:userInfo:
setObject:forKeyedSubscript:
stringByDeletingLastPathComponent
substringToIndex:
mountWithError:
contentTypeToSubclassMap
defaultVolumeNameGivenRole:
mediaForPath:isSnapshot:
prebootVolume
setObject:forKey:
sortUsingComparator:
getCString:maxLength:encoding:
pairedVolumeWithRole:
primaryMedia
setIoMedia:
vendorName
@64@0:8@16i24B28q32q40@48^@56
v24@0:8@?16
B24@0:8^@16
B32@0:8@16^@24
B24@0:8@16
@28@0:8i16@20
i16@0:8
B28@0:8i16^@20
B16@0:8
@32@0:8@16^@24
B40@0:8@16@24^@32
B40@0:8@16d24^@32
@24@0:8@16
v20@0:8i16
@24@0:8^@16
@20@0:8I16
v20@0:8I16
I
v16@0:8
r^{?=iS@@}20@0:8i16
@32@0:8@16^B24
I24@0:8@16
I16@0:8
v24@0:8@16
@16@0:8
@20@0:8i16
%s : Failed to get content type.
Couldn't create a temporary mount point %s
Cleaned up temporary mount point
Can not mount (%@) because mount returned %d.
%s : Unable to get the iterator for entry.
%s: No media found for path: %{private}@
%s: Failed to find primary media
%s : Paired volume is not valid if role is not system.
Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n
%s: Volume is not mounted. Unable to set name\n
mount_apfs %@ returned %d, retrying (%d)
Failed to unmount %@ **FORCING UNMOUNT** error: %d
Failed to unmount %@ retry: %s error: %d
%s : failed with unknown kern_return_t error: %d
%s : Could not open device mount %{private}@.
%s was stopped by signal %d
posix_spawn %s failed: %s
pipe failed while preparing to execute %s: %s
%s : Container isn't a container?!
Failed to clean up temporary mount point: %d
%s : fs_snapshot_list failed with error %d
%s: Failed to unmount volume with error: %d
%s : Could not set root from snapshot. Errno: %d
%s: path is a snapshot, but has no name: %{private}@
%s: %@ isn't an APFS volume
%s : Unable to get parent iterator
%s : Need a valid snapshot names.
Failed to call APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ with errno %d\n
%s : Container is somehow missing a BSD name.
%s : Paired volume must be in the same container
Can not mount (%s) because it does not appear to have a device node.
%s : Failed to encode snapshot name %{private}s for some reason.
%s : Could not open device is not mounted.
%s: Failed to remount volume with error: %d
%s : APFSVolumeCreateForMSU exists and we're creating a System volume. Preferring it to APFSVolumeCreate.
Can not mount (%{private}s) because we could not create its mount folder (%{private}s).
%s : failed with posix error: %d
%s : Failed to open media for snapshot delete: %d
%s: No snapshot is tagged for boot and none match the naming scheme
%s: Failed to obtain parent IOMedia for disk at path %{private}@
%s: failed to get read-only status for %@\n
IOKit wait timed out, volume for media may be stale.
%s called on device with no dev node
Was asked asked to unmount (%@) but is not mounted.
Deleting contents of %{private}s...
%s: no filesystem for %@ (%d): %s
%s: Error getting snapshot info for %@: %@
%s: Successfully set volume name to %{private}@\n
%s : Creating APFS volume %s with options: %@
%s : Failed because target volume is not mounted
rename snapshot operation failed: %d %s
%s: Trying to determine mount point\n
%s : Requested system volume with sibling but the key is not supported.
%s : volume is missing a dev node somehow
%s called but %{private}@ is not mounted.
%s: No disk for %{private}@
IOKit service wait timed out, volumes may be stale.
Failed to create partition media iterator.
Volume is already mounted at %@, skipping re-mount
%s : going to delete apfs volume ( %@ )
%s : Waiting for snapshots to delete timed out
Deleting contents of %{private}s %s (result: %d).
Could not removefile(3) path %{private}s: %s
%s: Parent of disk backing %{private}@ is not an APFS volume
%s: failed to get journaled status for %@\n
Failed to find media for %@
%s : Unable to open mount point %{private}@: %d
%s : Failed to delete snapshot: %{private}@, %d
revert snapshot operation failed: %d %s
%s: Mount point is %{private}@\n
waitpid failed for %s: %s
%s: Failed to get IOMedia objects
%s: no IOMedia for %@ (device 0x%lx)
%s: Failed to set name for volume: %s\n
%s : Add volume failed with error: %d.
Volume is already mounted at %@, attempting to re-mount at %@
%s : Need a valid snapshot name.
%s : Need a valid new snapshot name.
%s: Not on a rooted snapshot disk, will return self: %{private}@
%s : IOIterator was still invalid after attempting %d times
create snapshot operation failed: %d %s
%s : Volume name is invalid
%s : Can not iterate over physical store services.
%s: failed to get role. Error: %d
%s : failed with iokit error: %d
%s : Error in reading attributes for directory entry %d
%s: Skipping unmount/remount of %@
Could not reset metadata on %{private}s: %s
Mounted %@, Snapshot( %{private}@ ) at %{private}@
Unmount failed with EINVAL, will assume race. Ignoring error.
Unmounted %@ ( %{private}@ )
%s was terminated by signal %d
%@
%s: could not parse %s %{private}s: %{private}@
%s: statfs failed: %d (%s)
%s : failed to read value for property named: %@
%s: could not look up snapshot by UUID: %d (%s)
Timed out waiting for: %@
Mounted %@ at %{private}@
%s : You need to specify a volume name.
```
