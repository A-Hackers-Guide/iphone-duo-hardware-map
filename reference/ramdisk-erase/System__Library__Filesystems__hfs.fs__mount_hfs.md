# `/System/Library/Filesystems/hfs.fs/mount_hfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 72,672 bytes.

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
defwrite
perm
GetMasterBlock: Error %d opening %s\n
sparse-backend
cannot open backing store '%s' for '%s'
Re-key environment variable has 0 length
missing image path for '%s'
cannot propagate backing store information to %s
get_default_encoding
dev
rdonly
enable-remap-mode
follow
stat %s
enable-rolld-dev1
Non-data type reference for re-key environment check
suid
GetMasterBlock: Could not malloc %u bytes\n
unknown encoding: %s
auto
protect
realpath %s
/sbin/kextload
rdisk
automounted
%s/
invalid file mode: %s
encoding > -1 && encoding <= UINT_MAX
/System/Library/Filesystems/hfs.fs/Contents/Resources/Encodings/
Could not acquire IOMainPort for re-key environment check
%s%s
owners
GetMasterBlock: Error %d from read; amount=%ld, wanted=%u\n
IOService
unable to find: %s\n
groupquota
/dev/r%s
xu:g:m:e:o:wt:jc
DiskImageURL
Could not exec re-keying daemon %s
mount_hfs.c
unable to load: %s\n
/dev/disk
%s: Invalid tbuffer size %s\n
Failed to close GPT fd !\n
mount_hfs: error on mount(): error = %d.\n
Could not get options reference for re-key environment check
userquota
browse
quarantine
update
/usr/libexec/rolld
IODeviceTree:/options
ro
atime
GetMasterBlock: Error %d getting block size\n
/dev/rdisk0s1
/dev/
hfs
%sHFS_Mac%s.kext
true
rw
union
realpath(2) %s
AppleDiskImageDevice
could not get file system representation from url
disk
exec
unknown group id: %s
unknown user id: %s
usage: mount_hfs [-u user] [-g group] [-m mask] [-t tbuffer-size] [-j] [-c] [-o options] special-device filesystem-node\n
/.CFUserTextEncoding
```
