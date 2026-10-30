# `/usr/bin/peppytool`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 72,048 bytes.

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
submitFrame:error:
elementCount
getOutOfBoxFlag:error:
stringWithUTF8String:
UTF8String
addIndex:
floatValue
setBrightness:withColor:forIndices:completion:
setState:withColor:withRate:forIndices:completion:
updateFirmwareFromPath:error:
count
setOverrideBrightness:withColor:forIndices:completion:
addObject:
appendBytes:length:
close
indexSet
localizedDescription
normalizedXCoordForIndex:
normalizedYCoordForIndex:
numberWithFloat:
array
code
copySerialNumber:error:
hwVersion
objectAtIndex:
setLEDPlus:minus:
setOutOfBoxFlag:error:
setProperty:forKey:completion:
objectAtIndexedSubscript:
description
factoryResetAnimation:
getBytes:length:
getPropertyForKey:completion:
length
setElementAtIndex:red:green:blue:
sharedInstance
copy
newFrame
numberWithUnsignedChar:
open
Error: %s\n
Error: Invalid MD data size %lu\n
MiniDisplay Element[%lu] X,Y Norm. Coords: %2.5f,%2.5f\n
Peppy HW Version: %02x\n
LEDProcessing
    <0.0 to 1.0>                                     Set LEDs to fraction of maximum brightness.
    off                                              Turn scan off.
    on                                               Turn scan on.
off
logging
Error: Bad version info\n
SetPeppyTraceLogging
                                                     Bits 0,1 = plus, Bits 2,3 = minus, Bit 4,5 = Center.
                                                     Defaults to 0x7 (everything on).
    -i  --info                                       Print FW version and other MCU info.
LED Colors:
Error: Invalid LED data size %lu\n
set
Finished updating FW
    -m, --md \"<2xNormalized LED> <57xNormalized MD RGB>\" Control LEDS+MiniDisplay.
    1                                                Amber.
Logging Commands:
VersionInfo
Current Peppy FW Version: %02x.%02x\n
Sensor data: %s\n
Raw command output: %s\n
InjectButton
                                                     Data is 59 space delimited 0.0 to 1.0 normalized brightnesses.
    clear                                            Clear the flag.
SUCCESS
MiniDisplay Element Count: %lu\n
verbose
Usage: peppytool [option] <command>\n
Options:
                                                     Only key version 2 is supported (swap ordering of 16-bit values in a word).
Touch Scan Commands:
l:m:c::u:t:s:r:o:fb:pg:q:ih
v20@?0B8@\"NSError\"12
force
md
update_fw
oob
UNSET
    trace                                            Turn on trace logging - endpoint logging for testing latency.
    -c[csv_cal_bytes], --cal[=csv_cal_bytes]         Set LED calibration. Overwrite current calibration data, if any.
    set                                              Set the flag.
    verbose                                          Turn on verbose driver logging.
LED calibration data: %s\n
v24@?0@\"NSObject\"8@\"NSError\"16
clear
Peppy Interface Protocol Version: %d\n
trace
                                                     The first bit of pair produces 1->0 edge, second bit produces 0->1 edge.
Error: bad argument\n
Warning: Bad MCU version info!\n
Peppy FW Version: %02x.%02x\n
SetPeppyLogging
    -u, --update_fw <path_to_file>                   Update Peppy firmware
                                                     1      Empty file path argument
    -h, --help                                       Displays this help dialog and exit.
    off                                              Turn LEDs off.
fcrst_anim
raw
print_md
ScanControl
Current Boot Mode: %d\n
Updating FW...
    -l, --led \"<index_mask> <color> <led_command> <ALS override>\"   LED commands
                                                     If called without data, read current LED calibration data.
led
cal
sensor
help
info
on
                                                     -17    Can't open IOHIDDevice
                                                     -50    Bad firmware file path
ledcalibration-LEDc
FAIL
                                                     Argument is CSV bytes. For the structure, see rdar://problem/31442461
                                                     Update error codes:
    -r  --raw \"<cmd_code> <csv_w_bytes> <#r_bytes>\"  Write byte array and then read # of bytes for specified Peppy command.
    -o  --oob <flag_value>                           Set or unset Out-Of-Box flag (no blink on boot).
    -q  --process <bitmask>                          Turn on or off LED processing. Argument is a 1 byte bitmask. 1 enables process, 0 disables.
    on                                               Turn LEDs on.
Error: MiniDisplay hardware not available, hwvers %lu\n
ReadSensorRaw
RawWriteRead
OOB Flag state after command: %s\n
SET
                                                     -20    Firmware update failed
    --force                                          Use with -u to force update
    -b  --button <button_edge_mask>                  Inject a button edge for the specified buttons.
touch
button
ReadSensorBaseline
    -t  --touch <scan_command>                       Turn on or off touchpad scan.
    -p  --print_md                                   Print MiniDisplay info (hwVers, elementCount, coordinates.
    -g  --logging <log_command>                      Turn on trace or verbose logs, or turn logs off.
OOB Flag Values:
Factory Reset Animation: %s\n
MiniDisplay HW Version: %lu\n
                                                     -200   Can't find Peppy driver
    -s  --sensor \"<rsb_char_pattern> <#repeats>\"     Read sensor data #repeats times.
LED Commands:
    off                                              Turn off trace and verbose logging.
process
ReadSensorSignal
Serial Number: %s\n
    -f  --fcrst_anim                                 Start the factory reset animation (red spinner). 
                                                     Bit 0: Calibration, Bit 1: Gamma Correction, Bit 2: ALS autobrightness.
    0                                                White.
```
