# `/usr/lib/libTiSerialFlasher.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 111,152 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1896)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libTiSerialFlasher.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (144)

```
strlen(name) <= sizeof(applicationFilename)
LockSectionA
HIBYTE(checksum) == inPacket[inPacketLen-1]
no entry from path!\n
Calibrating DCO...
sync[0] == 0x90
looking for mcu nub...
DCO calibration - brain damage
J33i platform found
fh != NULL
bytesRead == bytesToRead
offset <= 0xFFFF
/dev/cu.mcu-bsl0
IOKit: root name: %s\n
len <= 250
K66 platform found
IORegistryEntryFromPath failed
%255[^\r\n]%n%*[\r\n]
chunkIdx<NUMELS(chunks)
Total bytes to write: %d\n
got a calibration byte\n
J33i
IODeviceTree:/options
Error opening serial port %s - %s(%d).\n
Sending Application...\n
IODeviceTree:/arm-io/mcu0
Mass Erasing...
bytesRead == 1
MassErase
01.18
boot-args
Error calling ioctl(..., IOSSIOSPEED, ...) %s - %s(%d).\n
LeaveBslMode
J33
numWritten == sizeof(writeBuffer)
ValidatePacket
proto1
r
address <= 0xFFFF
### can't get matching dictionary\n
Leaving BSL mode...
IODeviceTree
Entered BSL mode successfully!\n
SendPassword
libTiSerialFlasher v%s\n
J42
Changing baud rate TO 38400...
Error setting tty attributes %s - %s(%d).\n
transferMSP430TXTFile
no entry in plane!\n
skip_mcu_reflash
J33 platform found
proto0
Error clearing O_NONBLOCK %s - %s(%d).\n
### can't open AppleTVIR: %d\n
ReleaseDtr
Using Application File: \"%s\"\n
Can't open file \"%s\" - Exiting.\n
Checking Chip ID...
expected version 0x%04X, but chip is version 0x%04X\n
SendData
Error waiting for drain - %s(%d).\n
Error setting TIOCEXCL on %s - %s(%d).\n
registerFilename
tmp != NULL
TiSerialFlasher not supported on this platform. Exiting.\n
/usr/standalone/firmware/TiSerialFlasher-03.10.txt
IOService:/
 
chunks[chunkIdx].data != NULL
checking firmware version of mcu...
/usr/standalone/firmware/TiSerialFlasher-02.09.txt
/usr/standalone/firmware/TiSerialFlasher-06.17.txt
IORegistryGetRootEntry failed
Error calling ioctl(..., IOSSIOSPEED, ...) - %s(%d).\n
final hardware
AssertRts
Unlocking...
WaitForAck
ChangeBaudRate
CheckBslVersion
nvram boot-args 2>/dev/null
bslMachineTaskStep
numBytes >= 0
bytesRead != 0
ReadMemory
bytesWritten == commandLen
TiSerialFlasher: skip_mcu_reflash boot-arg found! Exiting.\n
proto2
Finding serial port...
CalibrateDCO
LOBYTE(checksum) == inPacket[inPacketLen-2]
numBytes == 1
SendLoadPC
-> sendData:%d bytes at 0x%X\n
BslSerial.c
Error getting tty attributes %s - %s(%d).\n
### can't find AppleTVIR\n
AssertDtr
ReleaseRts
Checking BSL Version...
val == 0
ReleaseLines
SendMessage
Can't register Device Path: %s\n
Error setting read latency %s - %s(%d).\n
Assertion Failed at %s():%d \"%s\"\n
status == kStatusSuccess
bytesWritten != -1
EnterBslMode
IORegistryEntryGetName failed
rb
using %s\n
Port closed.\n
boot-args %[^\n]
J42 platform found
TiSerialFlasher_internal
K66
Entering BSL mode...
BlockingWrite
len < sizeof(data)
numRead != -1
numBytes != 0
readResponse[0] == 0x90
newPC <= 0xFFFF
entry found!\n
board-rev
WaitForData
IORegistryEntryGetProperty failed
Found skip_mcu_reflash boot-arg!
Error resetting tty attributes - %s(%d).\n
TiSerialFlasherIOCtrl
response[0] == 0x80
dataLength <= 250
Success!\n
got unrecognized trash\n
inPacket[0] == 0x80
not yet implemented - reflash suggested\n
status
/usr/standalone/firmware/TiSerialFlasher-01.32.txt
IOKit: boot-args: %s\n
### user client failed for %d, %d: %d\n
EstablishSync
CheckChipId
```
