# `/sbin/fsck`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 70,992 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1792)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (67)

```
\n
Encountered ramdisk definition for location %s - will be created during mount.\n
Unknown pid %d\n
\n%s: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.\n
LABEL=
/
-%c flag requires a %s
Can't stat root
THE FOLLOWING FILE SYSTEM%s HAD AN %s\n\t
-%s%s%s%s%s%s%s
apfs
kqueue: could not create kqueue: %d\n
Can't stat %s\n
out of memory
S
%s (%s): EXITED WITH SIGNAL %d\n
q
Retrying (%d retries left)...\n
%c option?
ramdisk
f
warning: auto-boot is set to %s\n
, 
fsck: failed to copy boot container\n
BAD DISK NAME %s\n
kevent() failed to register: %d\n
%s is not a character device\n
%s in fstab more than once!\n
fsck: not booting main or diagnostic OS. Skipping fsck on OS container\n
number
auto-boot
%s (%s)%s
%s (%s) EXITED WITH SIGNAL %d\n
hfs
/r
IODeviceTree:/filesystems/fstab
p
/sbin
Filesystem cannot be checked \n
Encountered ramdisk definition. Do not stat\n
fsck: failed to get boot container\n
os_env_type
warning: 
l
fsck_%s
%s/fsck_%s
fork failed for %s \n
/dev/
%sfailed to get boot device - %s\n
UNEXPECTED INCONSISTENCY:
d
n
y
exfat
msdos
kevent: registered errors.
failed to get filesystem info\n
No need to check filesys for ramdisk, does not exist yet.\n
udf
fork
returning to single-user after filesystem check
Can't get filesystem checklist: %s\n
error attempting to exec %s\n
UUID=
fsck usage: fsck [-fdnypqL] [-l number]\n
dfpR:qnNyYl:L
fsck timed out. Can't stat %s\n
```
