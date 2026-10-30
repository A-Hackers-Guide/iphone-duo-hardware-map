# `/usr/bin/TiSerialFlasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 68,496 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1368)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (1)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (16)

```
       -d <devicePath> to override the serial device used for firmware upgrade
TiSerialFlasher success!
<%3d%%>
pqf:d:
TiSerialFlasher FAILED - Exiting with status %d\n
usage: TiSerialFlasher [options]
TiSerialFlasher v%s\n
01.18
libTiSerialFlasher.dylib
Error loading dynamic library \"%s\"!\n
       -q to quiet output
       -p to enable progress messages
Error finding lib function!
unrecognized non-option argument %s\n
TiSerialFlasher
       -f <filename> to supply a custom firmware image
```
