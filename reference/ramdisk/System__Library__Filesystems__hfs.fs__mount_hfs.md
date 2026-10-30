# `/System/Library/Filesystems/hfs.fs/mount_hfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 72,672 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1840)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

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

## Strings (72)

```
userquota
dev
/dev/r%s
unknown group id: %s
invalid file mode: %s
exec
defwrite
quarantine
GetMasterBlock: Error %d getting block size\n
%s/
xu:g:m:e:o:wt:jc
owners
mount_hfs: error on mount(): error = %d.\n
unknown encoding: %s
/.CFUserTextEncoding
unable to load: %s\n
Failed to close GPT fd !\n
rdisk
auto
GetMasterBlock: Could not malloc %u bytes\n
%s: Invalid tbuffer size %s\n
/dev/
unknown user id: %s
true
rw
union
AppleDiskImageDevice
sparse-backend
cannot propagate backing store information to %s
GetMasterBlock: Error %d from read; amount=%ld, wanted=%u\n
/sbin/kextload
Non-data type reference for re-key environment check
Re-key environment variable has 0 length
DiskImageURL
mount_hfs.c
/dev/rdisk0s1
cannot open backing store '%s' for '%s'
missing image path for '%s'
Could not acquire IOMainPort for re-key environment check
realpath(2) %s
realpath %s
IOService
get_default_encoding
atime
protect
enable-rolld-dev1
enable-remap-mode
suid
perm
update
disk
/System/Library/Filesystems/hfs.fs/Contents/Resources/Encodings/
rdonly
browse
stat %s
encoding > -1 && encoding <= UINT_MAX
IODeviceTree:/options
Could not get options reference for re-key environment check
automounted
GetMasterBlock: Error %d opening %s\n
hfs
/usr/libexec/rolld
Could not exec re-keying daemon %s
usage: mount_hfs [-u user] [-g group] [-m mask] [-t tbuffer-size] [-j] [-c] [-o options] special-device filesystem-node\n
%sHFS_Mac%s.kext
unable to find: %s\n
groupquota
ro
follow
/dev/disk
could not get file system representation from url
%s%s
```
