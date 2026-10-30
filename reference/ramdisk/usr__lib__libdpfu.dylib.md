# `/usr/lib/libdpfu.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 93,312 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1880)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libdpfu.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (64)

```
Unknown Mode
Unable to Enter %s...
  Download Ready
dpfu: 
UpdateMode
Eight-Byte Update Mode
Ready
Final Status: %s (0x%02x)
32-KByte Update Protocol
  Error opening file: %s
Error
Requesting %s...
  Successfully opened %s
Requesting %s Again...
Data End
Error reading from device: %s (0x%08x)
Successfully wrote %u total bytes
  Validated
Commanding Restart...
Normal Mode
32-KByte Update Mode
Current Device Mode: %s%s (0x%02x)
Initial Device Status: %s (0x%02x)
Validate
Warning: attempted to read %u bytes, fread returned %lu
  Error writing data after %u successful bytes
Installed
Commanding Validate...
  Installed
Initial Device Mode: %s (0x%02x)
Writing Data from File...
Validated
None
Install
DPFUSessionInstallFilePayload( %s )
DPFUSession
Error writing to device address 0x%08x offset 0x%08x: %s (0x%08x)
Commanding Download...
Data
  New Mode: %s (0x%02x)
Device already in %s
  %u bytes written
Commanding Install...
Writing Data from Memory...
  Current Status in this Mode: %s (0x%02x)
Restart
Updated
  Device Status: %s (0x%02x)
Eight-Byte Update Protocol
Opening package file: %s
rb
Single-Byte Update Mode
Sending Host Command: %s (0x%02x)
Download
Device Mode: %s (0x%02x)
  Restarted in mode: %s (0x%02x)
Single-Byte Update Protocol
Idle
Unknown
  Error Installing image!
Requesting Device Mode: %s (0x%02x)
Can't create device update session
Busy
Requesting 
```
