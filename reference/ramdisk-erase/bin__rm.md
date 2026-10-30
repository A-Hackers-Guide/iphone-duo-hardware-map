# `/bin/rm`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 53,600 bytes.

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

## Strings (26)

```
remove %s? 
\"/\" may not be removed
%s\n%s\n
unlink
fflagstostr
 
 %s
 %d dirs
 and %d files
remove %d files
\".\" and \"..\" may not be removed
%s: %s
examine files in directory %s? 
%s: is a directory
%s
override %s%s%s/%s %s%sfor %s? 
recursively remove
 and 1 file
? 
usage: rm [-f | -i] [-dIPRrvWx] file ...
       unlink [--] file
dfiIPRrvWx
bin/rm
unix2003
fts_open
fts_read
```
