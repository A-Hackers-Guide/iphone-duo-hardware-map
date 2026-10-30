# `/usr/local/bin/configdarwinbootargs`

From the upgrade restore ramdisk (141-29011-104.dmg). 54,096 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1632)
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

## Strings (80)

```
ls
%s value length is %lu, expected length of at least %lu\n
Retrieved current boot-args : %s\n
Setting new boot-args to : %s\n
asprintf failed with %d\n
Device tree reports device name as %s\n
usage: configdarwinbootags [OPTIONS]\n
Failed to read key %s with error: %s\n
personalized-boot-args
%s value is of type %lu, expected  CFData (%lu)\n
Previous script version run on this system was %d, continuing with this script (version %d)\n
debug=
Current debug value (0x%lx) doesn't match any previous defaults that need to be updated, skipping\n
Unable to retrieve hw.product\n
%s must be run as root, invoked under UID %d\n
last-boot-args-script-vers
DEV board detected setting debug boot-arg to 0x%x\n
debug=0x%x
Appending new boot_arg (%s) to existing (%s) would exceed boot-arg length (%d)\n
IOService:/
Failed to look up root registry entry\n
Existing value for key %s is type %lu, attempting to set with type %lu\n
NVRAM is not supported on this system\n
CFDataCreate failed\n
Error creating CFString for key %s\n
 %s
hw.product
Failed to get root name of device from device tree\n
   -s log to os_log instead of stdout/stderr\n
Failed to update %s variable with error %s\n
Device product (%s) matches exempt product type, setting debug boot-arg to 0x%x\n
 
IODeviceTree:/options
stress-rack
%s NVRAM key found, skipping boot-arg reconfig check\n
%s value is of type %lu, expected  CFString (%lu)\n
serial=
 debug=0x%x
CFStringCreateWithCString failed\n
   -l check for liveon config (iOS only)\n
No %s NVRAM key found on system, proceeding\n
boot-args
Failed to snprintf new debug boot-arg with %d\n
IOService
No existing %s boot-arg to remove.\n
boot-arg reconfiguration complete!
Retrieved hw.product: %s\n
DEV
No %s NVRAM key found on system, proceeding\n
%s value is of type %lu, expected  CFString (%lu)
NVRAM is not supported on this system
Setting new boot-args to : %s\n
boot-arg reconfiguration complete!\n
Error creating CFString for key %s
Unable to retrieve hw.product
DEV board detected setting debug boot-arg to 0x%x\n
Device tree reports device name as %s\n
Existing value for key %s is type %lu, attempting to set with type %lu
usage: configdarwinbootags [OPTIONS]
   -l check for liveon config (iOS only)
%s value length is %lu, expected length of at least %lu
asprintf failed with %d
Failed to snprintf new debug boot-arg with %d
Previous script version run on this system was %d, continuing with this script (version %d)\n
Retrieved current boot-args : %s\n
Failed to update %s variable with error %s
No existing %s boot-arg to remove.\n
%s value is of type %lu, expected  CFData (%lu)
Failed to look up root registry entry
   -s log to os_log instead of stdout/stderr
%s must be run as root, invoked under UID %d
Retrieved hw.product: %s\n
Failed to read key %s with error: %s
%s NVRAM key found, skipping boot-arg reconfig check\n
Current debug value (0x%lx) doesn't match any previous defaults that need to be updated, skipping\n
Failed to get root name of device from device tree
CFStringCreateWithCString failed
CFDataCreate failed
Device product (%s) matches exempt product type, setting debug boot-arg to 0x%x\n
Appending new boot_arg (%s) to existing (%s) would exceed boot-arg length (%d)
```
