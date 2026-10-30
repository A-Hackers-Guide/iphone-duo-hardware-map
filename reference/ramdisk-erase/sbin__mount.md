# `/sbin/mount`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 113,200 bytes.

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
Operation ended with error: %s
Final mount step ended with error: %s
/private/system_data/
Initial mount to %s failed with %d\n
UMLCreatePrimaryUserLayout passed without error
%s: %s
statfs %s
%s on %s (%s
Filesystem %s supports neither Block Device nor PathURL resources nor ServerURL resources.
SUDO_UID
FSSupportsPathURLs
%s has unknown file system type.
too many mount arguments
root data
n
v40@?0@\"NSString\"8@\"NSString\"16Q24^B32
Mounting tmpfs volume at tmp location %s\n
posix_spawn_file_actions_addclose output_pipe[1] failed: %d (%s)\n
failed to get filesystem info\n
mount: failed to setup tmpfs mount
/private/var
File system named %s unable to mount
invoke_tool_from_fskit_block_invoke_14
/sbin/mount_tmpfs
Failed to execute command %s\n
fclose failed: %d (%s)\n
Retrying (%d retries left)...\n
mount: can't get filesystem checklist
%d
usage: mount %s %s\n       mount %s\n       mount %s\n
invoke_tool_from_fskit_block_invoke_10
/private/var/mobile
Ramdisk fstab not in expected format.\n
Unexpected mount size %zu\n
IODeviceTree:/filesystems
mount: missing data volume
%s: unknown special file or file system.
%s: invalid file system.
posix_spawn_file_actions_adddup2 output_pipe[1] failed: %d (%s)\n
special file or file system %s too long.
%s: invalid special file or file system.
unknown special file or file system %s.
realpath %s
FSKit unavailable
%s failed with %d
sync
Argument count %d not equal to expected count %d
ro
Failed to unmount %s (errno %d).\n
Unexpected size string: %s\n
nonfs
, mounted by 
automounted
q
%@/%@
file system %s too long.
update
%s
special mount_point
asynchronous
mount
v24@?0@\"NSUUID\"8@\"NSError\"16
Mounting tmpfs volume at %s\n
Failed access check for %s with issue %s\n
mount: successfully migrated Media Keys\n
failed to allocate memory for arguments
Error %s parsing '%s'
v24@?0@\"NSError\"8@\"NSString\"16
Loading resource: %s
operation exiting with error %s
%s/mount_%s
nodev
noatime
quarantine
Final mount step cleanup ended with error: %s
posix_spawn_file_actions_init failed: %d (%s)\n
e-apfs
)
strictatime
Module %s is disabled!\n
@?<v@?>16@?0@\"NSProgress\"8
com.apple.filesystems.UserFS.FileProvider
size=
Creating %s/\n
%s,%s
with quotas
rdonly
rw
Mountpoints not available. Exiting.\n
Failed to copy user template: %s (%ld).\n
Executing command: 
waitpid failed: %d (%s)\n
headfFko:rwt:uvP:
mount: data volume missing, but not required in env: %u\n
FSSupportsGenericURLResources
posix_spawn failed: %d (%s)\n
noauto
apfs
exec: mount_%s
exec %s for %s
noexec
journaled
Filesystem %s does not support operation %s
FSSupportsBlockResources
Failed to create pipe for command output: %d (%s)\n
found multiple data volumes\n
/sbin
/usr/sbin
nobrowse
waitpid
%s:%d: Operation ended with error: %s
r
Command output:\n%s\n
ramdisk
force
%s/%s.fs/%s/mount_%s
, %s
async
/
No mnt_opts provided to mount preflight.\n
calloc failed: %d (%s)\n
IODeviceTree:/filesystems/fstab
v24@?0@\"FSModuleIdentity\"8@\"NSError\"16
Internal error, operation type %d unrecognized\n
Copying %s -> %s\n
url
[-dfFrkuvw] [-o options] [-t external_type]
[-adfFrkuvw] [-t external_type]
NFS exported
local
posix_spawn_file_actions_addclose output_pipe[0] failed: %d (%s)\n
Command signaled: %d\n
net
%s is owned by the automounter.
%zu
%s 
mount: encountered ramdisk\n
You must specify a filesystem type with -t.
2
newfs
v8@?0
nfs
mount: failed to migrate Media Keys, error = %x\n
Contents/Resources
, sealed
/System/Library/Filesystems/apfs.fs/apfs_boot_util
synchronous
fsck
Unable to invoke task
 %s
fork
mount: found boot container: %s, data volume: %s env: %u\n
o
Default mount %s is not available. Using backup %s.\n
template=
fdopen failed: %d (%s)\n
-f
nofollow
read-only
,
v16@?0@\"NSError\"8
Operation did not add any volumes
Found a ramdisk entry\n
/System/Library/Filesystems
protect
File system named %s not found
[-dfrkuvw] special | mount_point
FSRequiresSecurityScopedPathURLResources
Filesystem %s doesn't support Block Device or PathURL resources, can't preform format/check task.
v24@?0@\"NSArray\"8@\"NSError\"16
fgetln failed: %d (%s)\n
mkdir %s
Failed mount preflight. Exiting.\n
-s
%sfailed to lookup data volume - %s\n
only one -t option may be specified.
/Library/Filesystems
defwrite
noowners
invalid fstype
FSSupportsServerURLs
Failed to copy contents from %s to %s with error: %s\n
Failed to find executable: %s \n
/sbin/umount
-o
Probing resource: %s
os_env_type
getmntinfo
Final mount to %s failed with %d\n
-P flag requires a valid mount phase number
failed to mount data volume on darwinOS.
%s is already mounted at %s.
nosuid
Command failed: %d\n
%sfailed to get boot device - %s\n
warning: 
v24@?0@\"FSProbeResult\"8@\"NSError\"16
/.b/8/
union
apfs_boot_util exec failed
fskit
%s:error:%@
URLWithString:
checkResource:usingBundle:options:connection:replyHandler:
count
initWithArray:
localizedDescription
receiverForStandardIO:
unloadResource:shortName:options:replyHandler:
volumeID
bundleIdentifier
description
newClientForProvider:
probeResourceSync:usingBundle:replyHandler:
setProgress:
showProgress
fileURLWithPath:
addObjectsFromArray:
attributes
boolValue
domain
objectAtIndexedSubscript:
objectForKeyedSubscript:
stringWithFormat:
containsObject:
secureResourceWithURL:readonly:
UUID
activateVolume:shortName:options:replyHandler:
code
deactivateVolume:shortName:options:replyHandler:
isEqualToString:
loadResource:shortName:options:synchronousReplyHandler:
getProgressURLKey
length
mountVolume:fileSystem:displayName:provider:domainError:on:how:options:
string
uuid
volumeName
UTF8String
bundleForArguments:count:syntaxDictionary:errorHandler:
containerID
formatResource:usingBundle:options:connection:replyHandler:
getConnection
receiverWithDelegate:
resourceWithURL:
setDispatch_group:
addSubscriberForFileURL:withPublishingHandler:
componentsJoinedByString:
componentsSeparatedByString:
enumerateOptionsUsingBlock:
installedExtensionWithShortName:synchronous:replyHandler:
proxyResourceForBSDName:isWritable:
resetOptionEnumeration
sharedInstance
fs_containerIdentifier
isEnabled
stringWithUTF8String:
```
