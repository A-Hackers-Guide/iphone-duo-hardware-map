# `/System/Library/Filesystems/tmpfs.fs/mount_tmpfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 69,184 bytes.

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
atime
owners
quarantine
io:en:s:h
Desired memsize %lld too large - defaulting to %lld bytes\n
Unsuccessful mount
ro
suid
follow
tmpfs
tmpfs kext not loaded (searched for %s file system)
hw.memsize
browse
/sbin/kextload
usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] [special] <directory>
error parsing mount options
invalid value for '-%c': %s\n
/System/Library/Extensions/tmpfs.kext
userquota
groupquota
union
perm
unexpected special device: %s\n
rw
auto
dev
could not load kernel extension, return code %d\n
automounted
exec
rdonly
protect
update
Could not get the hw memory size, errno = %d (%s)\n
defwrite
```
