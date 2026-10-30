# `/bin/mv`

From the upgrade restore ramdisk (141-29011-104.dmg). 53,872 bytes.

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
%s
%s not overwritten\n
fastcopy: open() failed (from): %s
malloc(%zu) failed
unlink %s
%s is not a directory
bin/mv
%s -> %s\n
%s: set flags (was: 0%07o)
/bin/cp
mv
%s %s %s: did not terminate normally
%s %s: waitpid
(y/n [n]) 
override %s%s%s/%s for %s? %s
%s: set owner/group (was: %lu/%lu)
-rf
%s %s: exec failed
%s %s: terminated with %d (non-zero) status
usage: mv [-f | -i | -n] [-hv] source target
unix2003
--
%s %s %s: exec failed
%s %s %s: terminated with %d (non-zero) status
 
cannot resolve %s: %s
fastcopy: read() failed: %s
%s: unable to move extended attributes and ACL from %s
-PRpv
%s %s: did not terminate normally
%s\n%s\n
       mv [-f | -i | -n] [-v] source ... directory
%s: destination pathname too long
not overwritten\n
fastcopy: open() failed (to): %s
fastcopy: write() failed: %s
%s: remove
rmdir %s
%s %s %s: waitpid
/bin/rm
fhinv
overwrite %s? %s
cannot rename a mount point
-PRp
mv: %s and %s are identical\n
rename %s to %s
%s: set mode (was: 0%03o)
%s: set times
%s: owner/group changed; clearing suid/sgid (mode was 0%03o)
```
