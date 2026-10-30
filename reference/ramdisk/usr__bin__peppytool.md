# `/usr/bin/peppytool`

From the upgrade restore ramdisk (141-29011-104.dmg). 72,048 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2528)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/PeppySystemState.framework/PeppySystemState (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MiniDisplay.framework/MiniDisplay (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.minidisplay.control</key>
	<true/>
	<key>com.apple.private.pss.control</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>ApplePeppyUserClient</string>
		<string>IOHIDLibUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (152)

```
Options:
    -r  --raw \"<cmd_code> <csv_w_bytes> <#r_bytes>\"  Write byte array and then read # of bytes for specified Peppy command.
LED Commands:
logging
info
    -u, --update_fw <path_to_file>                   Update Peppy firmware
                                                     -20    Firmware update failed
OOB Flag Values:
    clear                                            Clear the flag.
    off                                              Turn off trace and verbose logging.
l:m:c::u:t:s:r:o:fb:pg:q:ih
raw
Error: Invalid MD data size %lu\n
VersionInfo
ReadSensorSignal
InjectButton
Usage: peppytool [option] <command>\n
    -l, --led \"<index_mask> <color> <led_command> <ALS override>\"   LED commands
Error: %s\n
led
help
Sensor data: %s\n
MiniDisplay Element[%lu] X,Y Norm. Coords: %2.5f,%2.5f\n
SetPeppyLogging
                                                     -200   Can't find Peppy driver
    --force                                          Use with -u to force update
force
Error: MiniDisplay hardware not available, hwvers %lu\n
Current Peppy FW Version: %02x.%02x\n
set
Updating FW...
    -m, --md \"<2xNormalized LED> <57xNormalized MD RGB>\" Control LEDS+MiniDisplay.
    -s  --sensor \"<rsb_char_pattern> <#repeats>\"     Read sensor data #repeats times.
                                                     Bits 0,1 = plus, Bits 2,3 = minus, Bit 4,5 = Center.
Error: bad argument\n
ledcalibration-LEDc
clear
    -t  --touch <scan_command>                       Turn on or off touchpad scan.
    -p  --print_md                                   Print MiniDisplay info (hwVers, elementCount, coordinates.
                                                     Defaults to 0x7 (everything on).
    off                                              Turn LEDs off.
    <0.0 to 1.0>                                     Set LEDs to fraction of maximum brightness.
Warning: Bad MCU version info!\n
MiniDisplay HW Version: %lu\n
Error: Bad version info\n
                                                     -50    Bad firmware file path
    -g  --logging <log_command>                      Turn on trace or verbose logs, or turn logs off.
    -h, --help                                       Displays this help dialog and exit.
    0                                                White.
Touch Scan Commands:
v24@?0@\"NSObject\"8@\"NSError\"16
button
LED calibration data: %s\n
Raw command output: %s\n
                                                     The first bit of pair produces 1->0 edge, second bit produces 0->1 edge.
v20@?0B8@\"NSError\"12
off
Current Boot Mode: %d\n
trace
                                                     1      Empty file path argument
LED Colors:
    set                                              Set the flag.
Peppy FW Version: %02x.%02x\n
Finished updating FW
                                                     Argument is CSV bytes. For the structure, see rdar://problem/31442461
    -f  --fcrst_anim                                 Start the factory reset animation (red spinner). 
    1                                                Amber.
    off                                              Turn scan off.
    on                                               Turn scan on.
cal
update_fw
UNSET
SetPeppyTraceLogging
LEDProcessing
                                                     Data is 59 space delimited 0.0 to 1.0 normalized brightnesses.
    -c[csv_cal_bytes], --cal[=csv_cal_bytes]         Set LED calibration. Overwrite current calibration data, if any.
                                                     If called without data, read current LED calibration data.
Factory Reset Animation: %s\n
Peppy Interface Protocol Version: %d\n
                                                     Update error codes:
    -o  --oob <flag_value>                           Set or unset Out-Of-Box flag (no blink on boot).
sensor
OOB Flag state after command: %s\n
SUCCESS
    on                                               Turn LEDs on.
Logging Commands:
    verbose                                          Turn on verbose driver logging.
process
ReadSensorBaseline
RawWriteRead
                                                     Only key version 2 is supported (swap ordering of 16-bit values in a word).
    -q  --process <bitmask>                          Turn on or off LED processing. Argument is a 1 byte bitmask. 1 enables process, 0 disables.
                                                     Bit 0: Calibration, Bit 1: Gamma Correction, Bit 2: ALS autobrightness.
oob
SET
Peppy HW Version: %02x\n
verbose
                                                     -17    Can't open IOHIDDevice
    -b  --button <button_edge_mask>                  Inject a button edge for the specified buttons.
    -i  --info                                       Print FW version and other MCU info.
    trace                                            Turn on trace logging - endpoint logging for testing latency.
print_md
on
Error: Invalid LED data size %lu\n
ScanControl
ReadSensorRaw
MiniDisplay Element Count: %lu\n
md
touch
fcrst_anim
FAIL
Serial Number: %s\n
submitFrame:error:
normalizedXCoordForIndex:
normalizedYCoordForIndex:
setElementAtIndex:red:green:blue:
updateFirmwareFromPath:error:
objectAtIndexedSubscript:
addObject:
count
floatValue
objectAtIndex:
open
code
getOutOfBoxFlag:error:
getPropertyForKey:completion:
indexSet
setState:withColor:withRate:forIndices:completion:
addIndex:
appendBytes:length:
array
close
description
newFrame
setBrightness:withColor:forIndices:completion:
copy
elementCount
getBytes:length:
localizedDescription
setProperty:forKey:completion:
stringWithUTF8String:
UTF8String
copySerialNumber:error:
factoryResetAnimation:
length
setOutOfBoxFlag:error:
hwVersion
numberWithFloat:
numberWithUnsignedChar:
setLEDPlus:minus:
setOverrideBrightness:withColor:forIndices:completion:
sharedInstance
```
