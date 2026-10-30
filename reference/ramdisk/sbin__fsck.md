# `/sbin/fsck`

From the upgrade restore ramdisk (141-29011-104.dmg). 70,992 bytes.

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
Retrying (%d retries left)...\n
dfpR:qnNyYl:L
warning: auto-boot is set to %s\n
UNEXPECTED INCONSISTENCY:
y
%s (%s) EXITED WITH SIGNAL %d\n
%sfailed to get boot device - %s\n
THE FOLLOWING FILE SYSTEM%s HAD AN %s\n\t
No need to check filesys for ramdisk, does not exist yet.\n
/sbin
kevent: registered errors.
Encountered ramdisk definition for location %s - will be created during mount.\n
n
\n%s: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.\n
apfs
hfs
-%c flag requires a %s
failed to get filesystem info\n
/dev/
number
%s (%s)%s
warning: 
p
f
l
error attempting to exec %s\n
exfat
fsck: failed to get boot container\n
fsck: failed to copy boot container\n
IODeviceTree:/filesystems/fstab
\n
Can't stat %s\n
os_env_type
S
UUID=
/
returning to single-user after filesystem check
d
%s in fstab more than once!\n
Can't get filesystem checklist: %s\n
fsck: not booting main or diagnostic OS. Skipping fsck on OS container\n
-%s%s%s%s%s%s%s
%s/fsck_%s
udf
Can't stat root
, 
ramdisk
out of memory
%c option?
auto-boot
%s (%s): EXITED WITH SIGNAL %d\n
fork failed for %s \n
LABEL=
fork
fsck_%s
Encountered ramdisk definition. Do not stat\n
fsck timed out. Can't stat %s\n
fsck usage: fsck [-fdnypqL] [-l number]\n
%s is not a character device\n
q
Filesystem cannot be checked \n
kqueue: could not create kqueue: %d\n
kevent() failed to register: %d\n
/r
BAD DISK NAME %s\n
Unknown pid %d\n
msdos
```
