# `/usr/lib/libdpfu.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 93,312 bytes.

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
  Error Installing image!
Device Mode: %s (0x%02x)
Requesting Device Mode: %s (0x%02x)
Initial Device Mode: %s (0x%02x)
Commanding Download...
  Download Ready
Commanding Restart...
Writing Data from Memory...
None
Validated
Sending Host Command: %s (0x%02x)
Successfully wrote %u total bytes
Eight-Byte Update Protocol
Writing Data from File...
Error
Restart
Installed
Initial Device Status: %s (0x%02x)
Unable to Enter %s...
Device already in %s
Download
Single-Byte Update Protocol
Can't create device update session
  Error writing data after %u successful bytes
Ready
  Current Status in this Mode: %s (0x%02x)
Commanding Install...
Validate
  Restarted in mode: %s (0x%02x)
Opening package file: %s
  New Mode: %s (0x%02x)
Data
32-KByte Update Protocol
  Installed
Updated
UpdateMode
Unknown Mode
Idle
Data End
Requesting %s...
DPFUSession
Requesting 
Eight-Byte Update Mode
32-KByte Update Mode
Unknown
Error writing to device address 0x%08x offset 0x%08x: %s (0x%08x)
Current Device Mode: %s%s (0x%02x)
Requesting %s Again...
  Device Status: %s (0x%02x)
DPFUSessionInstallFilePayload( %s )
rb
  Error opening file: %s
Normal Mode
  %u bytes written
  Validated
  Successfully opened %s
dpfu: 
Warning: attempted to read %u bytes, fread returned %lu
Single-Byte Update Mode
Busy
Error reading from device: %s (0x%08x)
Install
Final Status: %s (0x%02x)
Commanding Validate...
```
