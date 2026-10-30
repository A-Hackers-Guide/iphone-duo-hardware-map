# `/sbin/mount`

From the upgrade restore ramdisk (141-29011-104.dmg). 113,200 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2936)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/FSKit.framework/FSKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.fskit.mount</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.fskit.mount</string>
	<key>com.apple.private.LiveFS.connection</key>
	<true/>
	<key>com.apple.private.bindfs-allow</key>
	<true/>
	<key>com.apple.private.iokit.system-nvram-allow</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.filesystems.fskitd</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>
```

## Strings (257)

```
localizedDescription
resourceWithURL:
setDispatch_group:
mountVolume:fileSystem:displayName:provider:domainError:on:how:options:
receiverForStandardIO:
volumeID
UTF8String
activateVolume:shortName:options:replyHandler:
containerID
count
deactivateVolume:shortName:options:replyHandler:
unloadResource:shortName:options:replyHandler:
uuid
URLWithString:
secureResourceWithURL:readonly:
addSubscriberForFileURL:withPublishingHandler:
fileURLWithPath:
proxyResourceForBSDName:isWritable:
resetOptionEnumeration
setProgress:
string
containsObject:
enumerateOptionsUsingBlock:
isEnabled
objectAtIndexedSubscript:
sharedInstance
boolValue
description
domain
formatResource:usingBundle:options:connection:replyHandler:
isEqualToString:
loadResource:shortName:options:synchronousReplyHandler:
probeResourceSync:usingBundle:replyHandler:
volumeName
addObjectsFromArray:
bundleForArguments:count:syntaxDictionary:errorHandler:
checkResource:usingBundle:options:connection:replyHandler:
getConnection
getProgressURLKey
showProgress
stringWithFormat:
stringWithUTF8String:
componentsJoinedByString:
componentsSeparatedByString:
initWithArray:
installedExtensionWithShortName:synchronous:replyHandler:
length
newClientForProvider:
objectForKeyedSubscript:
receiverWithDelegate:
UUID
attributes
bundleIdentifier
code
fs_containerIdentifier
%s: unknown special file or file system.
force
update
protect
Ramdisk fstab not in expected format.\n
%s: invalid special file or file system.
%s/%s.fs/%s/mount_%s
%s
too many mount arguments
Unexpected mount size %zu\n
journaled
noowners
warning: 
mount: successfully migrated Media Keys\n
%s is already mounted at %s.
Unable to invoke task
defwrite
Probing resource: %s
Mountpoints not available. Exiting.\n
Mounting tmpfs volume at %s\n
local
FSRequiresSecurityScopedPathURLResources
Command signaled: %d\n
%s is owned by the automounter.
/System/Library/Filesystems/apfs.fs/apfs_boot_util
strictatime
v24@?0@\"NSError\"8@\"NSString\"16
v16@?0@\"NSError\"8
v8@?0
%s 
/System/Library/Filesystems
usage: mount %s %s\n       mount %s\n       mount %s\n
noexec
FSSupportsPathURLs
%s:%d: Operation ended with error: %s
Final mount step cleanup ended with error: %s
/private/var/mobile
UMLCreatePrimaryUserLayout passed without error
/usr/sbin
/private/var
 %s
Operation ended with error: %s
Failed access check for %s with issue %s\n
e-apfs
mount: missing data volume
File system named %s unable to mount
FSKit unavailable
%s: %s
, sealed
Failed to copy user template: %s (%ld).\n
waitpid failed: %d (%s)\n
mount: data volume missing, but not required in env: %u\n
, %s
with quotas
quarantine
invalid fstype
Operation did not add any volumes
/
unknown special file or file system %s.
Contents/Resources
)
invoke_tool_from_fskit_block_invoke_14
statfs %s
FSSupportsBlockResources
Command output:\n%s\n
os_env_type
apfs
File system named %s not found
Filesystem %s supports neither Block Device nor PathURL resources nor ServerURL resources.
Mounting tmpfs volume at tmp location %s\n
posix_spawn_file_actions_addclose output_pipe[0] failed: %d (%s)\n
posix_spawn_file_actions_adddup2 output_pipe[1] failed: %d (%s)\n
Executing command: 
Copying %s -> %s\n
found multiple data volumes\n
mount: failed to migrate Media Keys, error = %x\n
Internal error, operation type %d unrecognized\n
invoke_tool_from_fskit_block_invoke_10
r
noauto
mount: encountered ramdisk\n
You must specify a filesystem type with -t.
getmntinfo
/Library/Filesystems
mount
Default mount %s is not available. Using backup %s.\n
%s has unknown file system type.
%s failed with %d
nodev
FSSupportsServerURLs
v24@?0@\"NSArray\"8@\"NSError\"16
@?<v@?>16@?0@\"NSProgress\"8
net
mount: failed to setup tmpfs mount
nobrowse
failed to allocate memory for arguments
%s,%s
ramdisk
waitpid
%s on %s (%s
async
synchronous
SUDO_UID
Initial mount to %s failed with %d\n
template=
failed to get filesystem info\n
fork
Argument count %d not equal to expected count %d
n
Failed to copy contents from %s to %s with error: %s\n
/sbin/mount_tmpfs
fgetln failed: %d (%s)\n
Creating %s/\n
%sfailed to lookup data volume - %s\n
%d
rw
Final mount step ended with error: %s
/.b/8/
/private/system_data/
fclose failed: %d (%s)\n
only one -t option may be specified.
realpath %s
special mount_point
,
%zu
/sbin/umount
url
, mounted by 
[-adfFrkuvw] [-t external_type]
operation exiting with error %s
posix_spawn_file_actions_init failed: %d (%s)\n
%sfailed to get boot device - %s\n
union
failed to mount data volume on darwinOS.
apfs_boot_util exec failed
NFS exported
automounted
Error %s parsing '%s'
rdonly
Loading resource: %s
v24@?0@\"NSUUID\"8@\"NSError\"16
Failed to create pipe for command output: %d (%s)\n
%s: invalid file system.
mkdir %s
2
Module %s is disabled!\n
fsck
-f
IODeviceTree:/filesystems/fstab
-P flag requires a valid mount phase number
file system %s too long.
exec: mount_%s
nosuid
newfs
q
posix_spawn_file_actions_addclose output_pipe[1] failed: %d (%s)\n
-o
asynchronous
sync
noatime
root data
Filesystem %s does not support operation %s
FSSupportsGenericURLResources
No mnt_opts provided to mount preflight.\n
posix_spawn failed: %d (%s)\n
[-dfrkuvw] special | mount_point
read-only
v24@?0@\"FSProbeResult\"8@\"NSError\"16
com.apple.filesystems.UserFS.FileProvider
Failed to find executable: %s \n
fdopen failed: %d (%s)\n
[-dfFrkuvw] [-o options] [-t external_type]
fskit
Failed mount preflight. Exiting.\n
calloc failed: %d (%s)\n
mount: can't get filesystem checklist
/sbin
nofollow
nonfs
o
Final mount to %s failed with %d\n
headfFko:rwt:uvP:
Found a ramdisk entry\n
exec %s for %s
v40@?0@\"NSString\"8@\"NSString\"16Q24^B32
%@/%@
size=
IODeviceTree:/filesystems
%s/mount_%s
ro
Filesystem %s doesn't support Block Device or PathURL resources, can't preform format/check task.
Unexpected size string: %s\n
Command failed: %d\n
Retrying (%d retries left)...\n
mount: found boot container: %s, data volume: %s env: %u\n
nfs
special file or file system %s too long.
v24@?0@\"FSModuleIdentity\"8@\"NSError\"16
Failed to unmount %s (errno %d).\n
-s
Failed to execute command %s\n
%s:error:%@
```
