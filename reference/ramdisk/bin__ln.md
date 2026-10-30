# `/bin/ln`

From the upgrade restore ramdisk (141-29011-104.dmg). 52,976 bytes.

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

## Strings (15)

```
usage: link source_file target_file\n
FLPfhinsvw
warning: %s
link
%s and %s are the same directory entry
not replaced\n
%s\n%s\n
%s
%s/%s
%s %c> %s\n
usage: ln [-s [-F] | -L | -P] [-f | -i] [-hnv] source_file [target_file]
       ln [-s [-F] | -L | -P] [-f | -i] [-hnv] source_file ... target_dir
.
warning: %s inaccessible
replace %s? 
```
