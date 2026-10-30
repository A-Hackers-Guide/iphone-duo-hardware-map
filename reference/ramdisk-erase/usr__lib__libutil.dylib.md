# `/usr/lib/libutil.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 77,840 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1976)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (28)

```
Warning, unable to start xartutil, waitpid error: %d
Warning, xartutil returned status %d
Warning, xartutil terminated by signal: %u
Warning, xartutil stopped by signal: %u
Warning, xartutil terminated abnormally, status 0x%x
Warning, init xartutil file actions error: %d
Warning, unable to start xartutil, spawn error: %d
 
%d%s%d%s%s%s
0123456789
--erase-disk
Invalid %s argument `%s'
,
%u
REEXEC_TO_MATCH_KERNEL
REEXEC_TO_MATCH_LP64NESS
/usr/sbin/xartutil
/var/run/%s.pid
%s=1
tz
error
disk
xartutil
/dev/null
v16@?0^v8
Missing %s argument
%lld%s%s%s
com.apple.tzlink
```
