# `/usr/bin/TiSerialFlasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 68,496 bytes.

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
pqf:d:
       -q to quiet output
       -f <filename> to supply a custom firmware image
01.18
unrecognized non-option argument %s\n
libTiSerialFlasher.dylib
TiSerialFlasher
usage: TiSerialFlasher [options]
Error finding lib function!
<%3d%%>
Error loading dynamic library \"%s\"!\n
       -d <devicePath> to override the serial device used for firmware upgrade
TiSerialFlasher success!
TiSerialFlasher v%s\n
TiSerialFlasher FAILED - Exiting with status %d\n
       -p to enable progress messages
```
