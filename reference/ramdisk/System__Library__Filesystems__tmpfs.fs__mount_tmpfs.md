# `/System/Library/Filesystems/tmpfs.fs/mount_tmpfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 69,184 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1336)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (2)

- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (34)

```
ro
automounted
owners
error parsing mount options
Could not get the hw memory size, errno = %d (%s)\n
follow
browse
defwrite
atime
perm
io:en:s:h
invalid value for '-%c': %s\n
unexpected special device: %s\n
rw
could not load kernel extension, return code %d\n
/System/Library/Extensions/tmpfs.kext
dev
rdonly
update
usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] [special] <directory>
groupquota
auto
tmpfs kext not loaded (searched for %s file system)
hw.memsize
Desired memsize %lld too large - defaulting to %lld bytes\n
/sbin/kextload
suid
union
quarantine
protect
tmpfs
userquota
exec
Unsuccessful mount
```
