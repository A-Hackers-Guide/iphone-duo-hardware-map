# `/sbin/halt`

From the upgrade restore ramdisk (141-29011-104.dmg). 53,680 bytes.

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
IORegistryEntrySetCFProperty: %#x
auto-boot-halt-stage
halt
lnNqubB:
-%c has no effect
???
auto-boot
true
halted by %s%s
rebooted by %s
false
1
2
usage: halt [-lNnq]\n
IODeviceTree:/options
failed to get device tree options node
usage: reboot [-lNnq]\n
-N cannot be used with -n
reboot
option not supported: %c
assertion failure: \"v\" -> %llu
IOObjectRetain: %{mach.errno}d
```
