# `/usr/lib/libETLSAHDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 73,152 bytes.

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
kETLSAHMSMHardwareIDRead
kETLSAHGetCommandsID
header, command, or responseLength is NULL\n
MAV Extension: Protocol version 2\n
MAV Extension Protocol version 4\n
failed creating command 0x%0x\n
ETLSAHCommandReceive failed in %s\n
Bad payload data when getting debug table\n
ETLSAHGetRecordEx64Bit
not enough data received\n
kETLSAHReturnProtocolError
ETLSAHGetDebugRecordCount
header is NULL\n
unexpected command type\n
ETLSAHCommandExecuteDataCreate
ETLSAHCommandCreateMaverickConfigResponse
ETLSAHGetDebugTable
ETLSAHModeComplete
ETLSAHModeCommand
ETLSAHModeMaverick
kETLSAHSwitchToDMSSDLOAD
command response ID doesn't match, expected %u but received %u\n
Couldn't insert transport data into ring buffer when getting debug table\n
ETLSAHCommandCreateSwitchMode
kETLSAHGetDDRCalData
ETLSAHGetDebugRecordCount64Bit
Didn't receive expected number of bytes when getting debug table\n
Read failed. success = %u, read %u of %llu\n
ETLSAHCommandExecuteParseResponse
invalid arguments.  buffer = %p, chip id = %p\n
ETLSAHModePending
ETLSAHCommandExecute
buffer capacity too small\n
ETLSAHCommandExecuteCreate
_ETLSAHCommandExpectType
ETLSAHCommandSend failed in %s\n
Read failed. success = %u, read %u of %u\n
ETLSAHCommandParseMaverickSendHashesQuery
Sahara Protocol version 4\n
Sahara Protocol version 1\n
kETLSAHReturnSuccess
kETLSAHReturnError
kETLSAHReturnMemoryError
kETLSAHReturnIOError
ETLSAHModeMemoryDebug
kETLSAHSerialNumberRead
ETLSAHCommandReceive
ETLSAHCommandCreateMemoryRead failed in %s\n
kETLSAHSwitchToStreamingDLOAD
failed parsing command response\n
Sahara Protocol version 3\n
ETLSAHCommandParseMaverickRootManifestQuery
Expected type %u, got %u:\n
%s: no records requested\n
ETLSAHGetDebugTable64Bit
Protocol version 2\n
not enough room in buffer for data\n
kETLSAHReturnInternalError
kETLSAHNoOperation
Command of type %u, length %u has invalid length\n
failed receiving command response packet\n
ETLSAHCommandParseChipID
MAV Extension Protocol version 3\n
failed sending command\n
unexpected data size.  expected %zu received %zu\n
Unknown
ETLSAHGetRecordEx
```
