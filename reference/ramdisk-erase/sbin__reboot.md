# `/sbin/reboot`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 53,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1712)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (3)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (22)

```
true
false
failed to get device tree options node
IORegistryEntrySetCFProperty: %#x
1
-%c has no effect
reboot
IODeviceTree:/options
usage: halt [-lNnq]\n
usage: reboot [-lNnq]\n
???
2
halt
lnNqubB:
option not supported: %c
auto-boot
auto-boot-halt-stage
-N cannot be used with -n
halted by %s%s
rebooted by %s
assertion failure: \"v\" -> %llu
IOObjectRetain: %{mach.errno}d
```
