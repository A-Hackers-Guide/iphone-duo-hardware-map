# `/usr/bin/update_mcdp29xx`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 98,592 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1792)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (3)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOAVDeviceUserClient</string>
		<string>IODPDeviceUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (152)

```
  Installed
UpdateMode
Normal Mode
Commanding Install...
A2
waiting for device...
Update successful
  Successfully opened %s
App
app update failed
IODPDevice
DPCD FW Rev: %u.%03u (%s)
  New Mode: %s (0x%02x)
  Error Installing image!
Requesting Device Mode: %s (0x%02x)
total time: %.2f seconds.
Unable to fstat plist at %s
%s
Installed
Requesting %s...
app_version_minor
Unable to chdir to %s
Warning: attempted to read %u bytes, fread returned %lu
32-KByte Update Mode
None
Requesting 
Error reading from device: %s (0x%08x)
A4
Unable to malloc
failed to put device into reset
Error writing to device address 0x%08x offset 0x%08x: %s (0x%08x)
Install
Eight-Byte Update Protocol
AppleMCDP29XXGPIO
Unable to load Madea ISP
Unable to load Madea App
Madea is present
Opening package file: %s
Updated
Data
Error with restore process, resetting to retry attempt #%d...
  %u bytes written
min_hw_rev_minor
lfch
Error leaving update mode
Loading ISP driver from %s
ISP driver loaded successfully.
/usr/standalone/firmware/MCDP29XX/
Data End
Requesting %s Again...
Reset
alert
notice
debug
factory
/usr/local/standalone/firmware/MCDP29XX-factory/
Error entering update mode
rb
Commanding Restart...
Can't create device update session
Updating firmware...
Current FW versions do not match what was programmed.
Madea HW revision below minimum supported. Must update manually.
Unknown Mode
  Validated
Device Mode: %s (0x%02x)
Reading firmware versions for type %d from %s
%s: %s (0x%08x)
%08zx:
Unable to Enter %s...
No plist at %s
driver_version_major
Could not create CFData
unknown error
app_version_major
A3
Updating Madea application firmware from %s
pHDMIf
versions.plist
Final Status: %s (0x%02x)
IORegistryEntrySetCFProperty failed %08x
Unable to open plist at %s
/usr/local/standalone/firmware/MCDP29XX/
failed to bring madea out of reset
DPCD HW Rev: %u.%u (%s)
usage: update_mcdp29xx [-c] [firmware bundle path]\n       update_mcdp29xx -f [firmware bundle path]\n       update_mcdp29xx -l [firmware bundle path]\n Update Madea firmware from a firmware bundle. The firmware bundle path may be optionall
Current Device Mode: %s%s (0x%02x)
Initial Device Status: %s (0x%02x)
emerg
info
Writing Data from File...
Validated
Validate
min_hw_rev_major
BranchIEEEOUI
Writing Data from Memory...
Busy
dpfu: 
ISP
Download
A1
%s:
Initial Device Mode: %s (0x%02x)
Updated DPCD FW Rev: %u.%03u (%s)
Idle
Device already in %s
IOServicePublish
crit
app
IROM
FW on disk and Madea do not match!
Eight-Byte Update Mode
  Current Status in this Mode: %s (0x%02x)
Single-Byte Update Protocol
%s not found
firmware update completed successfully.
  Error writing data after %u successful bytes
Sending Host Command: %s (0x%02x)
Commanding Validate...
Unable to read plist at %s
Could not create CFDictionary
timed out
warning
check
DPFUSession
Successfully wrote %u total bytes
  Restarted in mode: %s (0x%02x)
 %02x
Madea did not re-appear
Unable to read device info
DPFUSessionInstallFilePayload( %s )
Single-Byte Update Mode
  Download Ready
Unknown
Commanding Download...
BranchDeviceID
error
local
Firmware is up to date.
  Error opening file: %s
Ready
32-KByte Update Protocol
%s: 
driver_version_minor
A0
driver update failed
help
Could not find device
isp
Error
  Device Status: %s (0x%02x)
Restart
```
