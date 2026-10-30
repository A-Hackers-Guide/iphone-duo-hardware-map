# `/System/Library/Filesystems/apfs.fs/mount_apfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 72,896 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2000)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
</dict>
</plist>
```

## Strings (110)

```
strictatime
IOService
pdi_nonce
unknown option '-%c'
cannot open %s
DATA
BASEBAND
No volumes with role %s were found on disk %s
union
AppleDiskImageDevice
XART
IDIAGS
perm
update
demomode
loadtmpcp
%s
could not get file system representation from url
cannot propagate backing store information to %s
[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset | smac>]] <volume | device> <directory>
USER
RECOVERY
VM
INTERNAL
mobile_asset
smac
IOHDIXHDDriveOutKernel
cannot open backing store '%s' for '%s'
volume could not be mounted
INSTALLER
Failed to find a volume with role %s on disk %s, status: %x
dev
file %s is too large
disk
rdisk
generic
supplemental
switch crypto context
DiskImageURL
userquota
invalid volume or device '%s'
image-type
image-path
sparse-backend
browse
automounted
defwrite
atime
:cCg:M:o:P:rRnSs:u:E:T:
missing argument
realpath [2] %s
snapshot 
PREBOOT
SIDECAR
Unknown role: %s
Unable to convert volume name
%sr%s
invalid cryptex type '%s'
need to specify both -P and -M or neither
rw
auto
quarantine
/dev/
brain
need non-empty files for -P and -M
sparse disk image
owners
skipsanity
committmpcp
%s%s
-T can only be specified with -P and -M
cannot stat %s
ROLE=
,
exec
follow
unknown group name '%s'
conflicting crypto mount options
/
%simplicitly mounted readonly
BACKUP
UPDATE
groupquota
AppleAPFSVolume
cannot read %s into memory
statfs has failed, err %i
suid
tinyobjcache
unrecognized option '%s'
invalid auth environment '%s'
unexpected argument
-E can only be specified with -P and -M
ro
protect
createtmpcp
failed to allocate memory for %s
missing operand for '-%c'
missing image path for '%s'
OVERPROVISION
checkpoint
rdonly
UUID
invalid user name '%s'
SYSTEM
ENTERPRISE
sparse bundle disk image
apfs
HARDWARE
CACHE
Volume type is not APFS
```
