# `/usr/lib/libTiSerialFlasher.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 111,152 bytes.

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
LeaveBslMode
Error waiting for drain - %s(%d).\n
BlockingWrite
chunks[chunkIdx].data != NULL
numBytes == 1
tmp != NULL
numRead != -1
TiSerialFlasher not supported on this platform. Exiting.\n
board-rev
proto1
rb
Sending Application...\n
got unrecognized trash\n
MassErase
SendMessage
IODeviceTree
TiSerialFlasher_internal
IORegistryEntryGetName failed
Error setting TIOCEXCL on %s - %s(%d).\n
/dev/cu.mcu-bsl0
nvram boot-args 2>/dev/null
IORegistryEntryFromPath failed
AssertDtr
status == kStatusSuccess
using %s\n
Entered BSL mode successfully!\n
Unlocking...
/usr/standalone/firmware/TiSerialFlasher-03.10.txt
final hardware
-> sendData:%d bytes at 0x%X\n
ValidatePacket
/usr/standalone/firmware/TiSerialFlasher-06.17.txt
registerFilename
EnterBslMode
CalibrateDCO
IOKit: root name: %s\n
Success!\n
got a calibration byte\n
numBytes >= 0
inPacket[0] == 0x80
Total bytes to write: %d\n
Using Application File: \"%s\"\n
SendPassword
status
J42 platform found
len <= 250
J33i platform found
Error calling ioctl(..., IOSSIOSPEED, ...) - %s(%d).\n
Assertion Failed at %s():%d \"%s\"\n
numWritten == sizeof(writeBuffer)
DCO calibration - brain damage
BslSerial.c
address <= 0xFFFF
### can't find AppleTVIR\n
### can't open AppleTVIR: %d\n
Mass Erasing...
ReadMemory
checking firmware version of mcu...
ReleaseDtr
SendData
bytesWritten == commandLen
/usr/standalone/firmware/TiSerialFlasher-02.09.txt
proto0
IORegistryEntryGetProperty failed
Error setting read latency %s - %s(%d).\n
fh != NULL
response[0] == 0x80
J33
IOKit: boot-args: %s\n
strlen(name) <= sizeof(applicationFilename)
numBytes != 0
bytesRead != 0
SendLoadPC
HIBYTE(checksum) == inPacket[inPacketLen-1]
no entry in plane!\n
### user client failed for %d, %d: %d\n
LOBYTE(checksum) == inPacket[inPacketLen-2]
libTiSerialFlasher v%s\n
bytesRead == bytesToRead
01.18
 
Error opening serial port %s - %s(%d).\n
Error getting tty attributes %s - %s(%d).\n
TiSerialFlasherIOCtrl
Error resetting tty attributes - %s(%d).\n
Port closed.\n
ReleaseLines
not yet implemented - reflash suggested\n
chunkIdx<NUMELS(chunks)
len < sizeof(data)
Error clearing O_NONBLOCK %s - %s(%d).\n
Error setting tty attributes %s - %s(%d).\n
AssertRts
bslMachineTaskStep
no entry from path!\n
K66 platform found
Checking BSL Version...
looking for mcu nub...
skip_mcu_reflash
Checking Chip ID...
CheckChipId
J33i
IORegistryGetRootEntry failed
Entering BSL mode...
EstablishSync
IOService:/
bytesWritten != -1
Can't open file \"%s\" - Exiting.\n
ReleaseRts
transferMSP430TXTFile
WaitForData
ChangeBaudRate
Changing baud rate TO 38400...
offset <= 0xFFFF
LockSectionA
expected version 0x%04X, but chip is version 0x%04X\n
/usr/standalone/firmware/TiSerialFlasher-01.32.txt
Error calling ioctl(..., IOSSIOSPEED, ...) %s - %s(%d).\n
%255[^\r\n]%n%*[\r\n]
sync[0] == 0x90
WaitForAck
dataLength <= 250
Can't register Device Path: %s\n
J42
boot-args
### can't get matching dictionary\n
entry found!\n
TiSerialFlasher: skip_mcu_reflash boot-arg found! Exiting.\n
proto2
K66
val == 0
readResponse[0] == 0x90
CheckBslVersion
IODeviceTree:/arm-io/mcu0
J33 platform found
Finding serial port...
bytesRead == 1
newPC <= 0xFFFF
boot-args %[^\n]
Found skip_mcu_reflash boot-arg!
r
IODeviceTree:/options
Leaving BSL mode...
Calibrating DCO...
```
