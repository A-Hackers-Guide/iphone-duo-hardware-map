# `/usr/bin/orionmicroupdate`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 53,568 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1704)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleOrionMCUUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (20)

```
Could not find device AppleOrionMicro\n
Orion microcontroller unresponsive. Update may have failed.
Orion firmware successfully updated
error reading firmware from file %s\n
Could not open service: %s\n
Firmware update failed with result: %s\n
%s version %s\n
Firmware image is older than current firmware. Update aborted
Unable to send firmware to kernel. Update failed.
Could not find Orion microcontroller. Update failed.
IOClass
AppleOrionMCU
1.1
Firmware update failed due to invalid image
r
application file %s not found\n
AppleOrionMicro
usage: %s <image>\n
Firmware image is incorrect size. Update aborted.
Firmware update already in progress. Update aborted.
```
