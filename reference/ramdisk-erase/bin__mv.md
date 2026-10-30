# `/bin/mv`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 53,872 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1448)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (1)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (49)

```
%s: set times
%s %s: waitpid
%s: destination pathname too long
%s not overwritten\n
override %s%s%s/%s for %s? %s
%s -> %s\n
malloc(%zu) failed
fastcopy: write() failed: %s
%s %s: did not terminate normally
       mv [-f | -i | -n] [-v] source ... directory
unix2003
mv: %s and %s are identical\n
fastcopy: open() failed (from): %s
%s: owner/group changed; clearing suid/sgid (mode was 0%03o)
%s: set flags (was: 0%07o)
fastcopy: open() failed (to): %s
%s: remove
rmdir %s
%s %s: exec failed
%s %s: terminated with %d (non-zero) status
fhinv
%s is not a directory
cannot rename a mount point
rename %s to %s
%s: unable to move extended attributes and ACL from %s
%s: set mode (was: 0%03o)
unlink %s
-PRpv
%s
(y/n [n]) 
--
%s %s %s: terminated with %d (non-zero) status
/bin/rm
-rf
%s\n%s\n
usage: mv [-f | -i | -n] [-hv] source target
bin/mv
not overwritten\n
%s: set owner/group (was: %lu/%lu)
/bin/cp
-PRp
%s %s %s: did not terminate normally
%s %s %s: exec failed
overwrite %s? %s
cannot resolve %s: %s
fastcopy: read() failed: %s
mv
%s %s %s: waitpid
 
```
