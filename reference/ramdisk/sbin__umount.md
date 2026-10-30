# `/sbin/umount`

From the upgrade restore ramdisk (141-29011-104.dmg). 53,888 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1632)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (25)

```
nfs
getmntinfo
pthread_cond_timeout failed; continuing with unmount
%s: not currently mounted
sysctlnametomib(%s)
usage: %s\n       %s\n
/dev/
AaFfh:t:v
only one -t option may be specified.
vfs.generic.noremotehang
Can't get filesystem checklist: %s\n
realpath(%s)
stat(%s)
ftp://
sysctl vfs.generic.noremotehang
%s: not a directory or special device
unmount(%s)
://
vfs.generic.ctlbyfsid
attempting to unmount %s by fsid\n
%s unmount from %s\n
umount(%s): %s -- try 'diskutil unmount'\n
umount [-fv] [-t fstypelist] special | node
umount -a[fv] [-h host] [-t fstypelist]
invalid fstype
```
