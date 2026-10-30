# `/usr/lib/libTelephonyDebugDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 82,576 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2016)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libTelephonyDebugDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (21)

```
SystemTrace
, timeout 
/usr/bin/trace
-i
context->source
Telephony operation timeout at '%s', timeout %u\n
v8@?0
operation timeout at 
-l
basic_string
TelephonyBasebandWatchdogStartWithStackshot_block_invoke
%s%04u-%02u-%02u-%02u-%02u-%02u-systemtrace.raw
Watchdog fired: %s\n
trace
-e
-b
Telephony watchdog fired: %s\n
-d
Writing system trace at %s\n
%s: Telephony watchdog fired: %s\n
Telephony watchdog fired: %s\n
```
