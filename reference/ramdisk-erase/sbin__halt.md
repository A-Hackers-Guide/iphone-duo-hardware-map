# `/sbin/halt`

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
IODeviceTree:/options
-N cannot be used with -n
???
halted by %s%s
reboot
true
failed to get device tree options node
lnNqubB:
option not supported: %c
IORegistryEntrySetCFProperty: %#x
auto-boot-halt-stage
1
2
usage: halt [-lNnq]\n
halt
rebooted by %s
usage: reboot [-lNnq]\n
-%c has no effect
auto-boot
false
assertion failure: \"v\" -> %llu
IOObjectRetain: %{mach.errno}d
```
