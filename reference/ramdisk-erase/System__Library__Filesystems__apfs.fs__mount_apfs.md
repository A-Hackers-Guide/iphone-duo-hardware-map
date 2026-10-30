# `/System/Library/Filesystems/apfs.fs/mount_apfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 72,896 bytes.

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
file %s is too large
XART
quarantine
createtmpcp
-E can only be specified with -P and -M
unknown group name '%s'
smac
unknown option '-%c'
missing operand for '-%c'
sparse disk image
update
:cCg:M:o:P:rRnSs:u:E:T:
pdi_nonce
image-path
CACHE
Unknown role: %s
ro
IOService
AppleAPFSVolume
missing argument
could not get file system representation from url
BASEBAND
brain
realpath [2] %s
/
DiskImageURL
cannot stat %s
OVERPROVISION
No volumes with role %s were found on disk %s
dev
apfs
rw
suid
follow
rdonly
skipsanity
loadtmpcp
UUID
/dev/
invalid auth environment '%s'
need non-empty files for -P and -M
RECOVERY
userquota
groupquota
strictatime
disk
rdisk
generic
invalid volume or device '%s'
cannot read %s into memory
VM
Failed to find a volume with role %s on disk %s, status: %x
union
IOHDIXHDDriveOutKernel
sparse bundle disk image
sparse-backend
cannot open %s
browse
automounted
tinyobjcache
committmpcp
conflicting crypto mount options
supplemental
mobile_asset
invalid cryptex type '%s'
unexpected argument
image-type
snapshot 
ROLE=
switch crypto context
volume could not be mounted
SYSTEM
UPDATE
SIDECAR
demomode
%s%s
cannot open backing store '%s' for '%s'
missing image path for '%s'
PREBOOT
HARDWARE
checkpoint
atime
owners
%sr%s
invalid user name '%s'
-T can only be specified with -P and -M
failed to allocate memory for %s
DATA
INTERNAL
statfs has failed, err %i
Unable to convert volume name
%s
AppleDiskImageDevice
cannot propagate backing store information to %s
%simplicitly mounted readonly
INSTALLER
BACKUP
ENTERPRISE
,
unrecognized option '%s'
USER
Volume type is not APFS
auto
exec
defwrite
perm
protect
need to specify both -P and -M or neither
[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset | smac>]] <volume | device> <directory>
IDIAGS
```
