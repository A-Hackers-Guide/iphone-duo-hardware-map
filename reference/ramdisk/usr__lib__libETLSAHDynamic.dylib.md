# `/usr/lib/libETLSAHDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 73,152 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 1624)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/libETLSAHDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDLOADDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (67)

```
kETLSAHReturnInternalError
kETLSAHReturnIOError
kETLSAHNoOperation
kETLSAHSwitchToDMSSDLOAD
Expected type %u, got %u:\n
Unknown
ETLSAHCommandReceive
failed parsing command response\n
not enough room in buffer for data\n
ETLSAHCommandParseMaverickSendHashesQuery
Sahara Protocol version 3\n
Protocol version 2\n
ETLSAHCommandCreateMaverickConfigResponse
command response ID doesn't match, expected %u but received %u\n
kETLSAHGetCommandsID
Didn't receive expected number of bytes when getting debug table\n
header is NULL\n
_ETLSAHCommandExpectType
ETLSAHModePending
ETLSAHCommandCreateMemoryRead failed in %s\n
Bad payload data when getting debug table\n
ETLSAHCommandExecuteDataCreate
Read failed. success = %u, read %u of %llu\n
unexpected command type\n
MAV Extension: Protocol version 2\n
kETLSAHReturnSuccess
ETLSAHGetDebugRecordCount
ETLSAHGetDebugRecordCount64Bit
ETLSAHGetDebugTable64Bit
kETLSAHReturnMemoryError
Command of type %u, length %u has invalid length\n
failed sending command\n
ETLSAHModeComplete
ETLSAHModeCommand
ETLSAHCommandSend failed in %s\n
not enough data received\n
MAV Extension Protocol version 3\n
kETLSAHSwitchToStreamingDLOAD
failed receiving command response packet\n
invalid arguments.  buffer = %p, chip id = %p\n
unexpected data size.  expected %zu received %zu\n
ETLSAHModeMemoryDebug
failed creating command 0x%0x\n
ETLSAHCommandCreateSwitchMode
Sahara Protocol version 1\n
header, command, or responseLength is NULL\n
kETLSAHGetDDRCalData
ETLSAHCommandExecute
%s: no records requested\n
Read failed. success = %u, read %u of %u\n
ETLSAHCommandExecuteParseResponse
ETLSAHCommandParseMaverickRootManifestQuery
kETLSAHSerialNumberRead
kETLSAHMSMHardwareIDRead
ETLSAHCommandReceive failed in %s\n
Couldn't insert transport data into ring buffer when getting debug table\n
ETLSAHGetRecordEx
ETLSAHCommandParseChipID
ETLSAHModeMaverick
ETLSAHCommandExecuteCreate
ETLSAHGetDebugTable
ETLSAHGetRecordEx64Bit
buffer capacity too small\n
Sahara Protocol version 4\n
kETLSAHReturnProtocolError
MAV Extension Protocol version 4\n
kETLSAHReturnError
```
