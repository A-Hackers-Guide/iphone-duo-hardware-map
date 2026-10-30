# `/usr/lib/liblzma.5.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 204,192 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 17 (Size: 1392)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/liblzma.5.dylib (compatibility version 6.0.0, current version 6.3.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (34)

```
=
|
This filter cannot be used in the .xz format
 
Invalid filter chain ('lzma2' missing at the end?)
Unknown filter name
The sum of lc and lp must not exceed 4
0
Unexpected NULL pointer argument(s) to lzma_str_to_filters()
\n
Empty string is not allowed, try \"6\" if a default value is needed
Unsupported preset
The maximum number of filters is four
Options must be 'name=value' pairs separated with commas
Option value cannot be empty
Invalid multiplier suffix (KiB, MiB, or GiB)
:
=<
Invalid option value
,
0-9[e]
Filter name is missing
Value out of range
This option does not support any integer suffixes
UNKNOWN
Unsupported flags to lzma_str_to_filters()
>
Unsupported preset flag
Unknown option name
5.4.3
--
-
Memory allocation failed
Value is not a non-negative decimal integer
```
