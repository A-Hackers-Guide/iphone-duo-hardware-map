# `/usr/bin/update_mcdp29xx`

From the upgrade restore ramdisk (141-29011-104.dmg). 98,592 bytes.

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
ISP driver loaded successfully.
%s: %s (0x%08x)
Unable to chdir to %s
Updating firmware...
usage: update_mcdp29xx [-c] [firmware bundle path]\n       update_mcdp29xx -f [firmware bundle path]\n       update_mcdp29xx -l [firmware bundle path]\n Update Madea firmware from a firmware bundle. The firmware bundle path may be optionall
Unknown Mode
Busy
Data
Requesting Device Mode: %s (0x%02x)
error
Error entering update mode
Single-Byte Update Mode
app_version_minor
IORegistryEntrySetCFProperty failed %08x
waiting for device...
Initial Device Status: %s (0x%02x)
  Current Status in this Mode: %s (0x%02x)
Validate
A1
Could not create CFDictionary
IOServicePublish
emerg
factory
32-KByte Update Mode
Download
unknown error
Updated DPCD FW Rev: %u.%03u (%s)
Opening package file: %s
Error reading from device: %s (0x%08x)
Requesting %s...
Commanding Validate...
Current FW versions do not match what was programmed.
rb
Writing Data from File...
Unable to Enter %s...
  Device Status: %s (0x%02x)
Install
Reset
Error leaving update mode
Normal Mode
dpfu: 
min_hw_rev_major
Could not find device
DPCD FW Rev: %u.%03u (%s)
Validated
  Restarted in mode: %s (0x%02x)
Single-Byte Update Protocol
info
  Validated
A3
debug
help
versions.plist
Eight-Byte Update Mode
Final Status: %s (0x%02x)
32-KByte Update Protocol
IROM
total time: %.2f seconds.
/usr/standalone/firmware/MCDP29XX/
lfch
Writing Data from Memory...
Idle
Requesting 
Could not create CFData
BranchIEEEOUI
timed out
FW on disk and Madea do not match!
Madea did not re-appear
Device already in %s
A0
app update failed
check
  Successfully opened %s
alert
crit
Current Device Mode: %s%s (0x%02x)
driver_version_major
firmware update completed successfully.
%s: 
notice
Madea HW revision below minimum supported. Must update manually.
Successfully wrote %u total bytes
Commanding Restart...
local
Error writing to device address 0x%08x offset 0x%08x: %s (0x%08x)
AppleMCDP29XXGPIO
  Error opening file: %s
Eight-Byte Update Protocol
min_hw_rev_minor
Unable to fstat plist at %s
DPCD HW Rev: %u.%u (%s)
App
pHDMIf
Unable to load Madea App
Madea is present
Update successful
DPFUSessionInstallFilePayload( %s )
Warning: attempted to read %u bytes, fread returned %lu
Unknown
  %u bytes written
No plist at %s
app
A2
Updating Madea application firmware from %s
Unable to read plist at %s
Commanding Download...
Reading firmware versions for type %d from %s
UpdateMode
IODPDevice
failed to put device into reset
Updated
 %02x
failed to bring madea out of reset
Error
Restart
Device Mode: %s (0x%02x)
Loading ISP driver from %s
Unable to open plist at %s
Can't create device update session
Firmware is up to date.
Initial Device Mode: %s (0x%02x)
Data End
driver update failed
Unable to malloc
warning
  Error writing data after %u successful bytes
Installed
None
  Download Ready
  Error Installing image!
%08zx:
%s:
isp
Ready
  New Mode: %s (0x%02x)
Requesting %s Again...
Commanding Install...
driver_version_minor
BranchDeviceID
Unable to load Madea ISP
Error with restore process, resetting to retry attempt #%d...
Sending Host Command: %s (0x%02x)
  Installed
app_version_major
%s not found
%s
/usr/local/standalone/firmware/MCDP29XX-factory/
/usr/local/standalone/firmware/MCDP29XX/
Unable to read device info
DPFUSession
ISP
A4
```
