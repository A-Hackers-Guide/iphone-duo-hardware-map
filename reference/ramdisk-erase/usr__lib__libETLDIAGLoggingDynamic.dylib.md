# `/usr/lib/libETLDIAGLoggingDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 100,336 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 1920)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libETLDIAGLoggingDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDMCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (75)

```
Failed to configure logging (maskID = %u): %s\n
Failed to un-configure logging: %s\n
No log equip ID found in DMC file
Range %u:\tIDs %u to %u\n
_ETLDIAGLoggingLOGClear
Request GUID: Subsystem Command: %s\n
Logging un-configured successfully!\n
Configuring %u Event Ranges\n
_ETLDIAGLoggingMSGSet
Request GUID: Version: %u\n
\n
Failed to set message master switch
, maskBits (from BBFW): 
Failed to get event range from DMC file
Failed to send QTraces
ETLDiagCreateGUIDDB request/response version mismatch: 
Attempt %u\n
Check range %u to %u\n
Failed to clear log masks
Warning: %s does not provide GUID\n
Response of GUID: GUID [%u]: %s\n
basic_string
ETLDIAGLoggingConfigure
_ETLDIAGLoggingLOGSet
Configuring log mask for equip ID %s(%u)\n
Failed to get log mask from DMC
Failed to set log masks
%s\n
Response of GUID: Delayed Response Status: %u\n
]
Unconfiguring Logging\n
Invalid event bit mask
No event ranges found in DMC file
Message range %s, is incorrect\n
Response of GUID: Response Count: %u\n
Failed to configure message range
Failed to clear message masks
_ETLDIAGLoggingEVTClear
Failed to send to clear QTraces
Received more message ranges than expected
Logging configured successfully (maskID = %u)\n
request 
All subsystems returned empty DIAG ID
ETLDIAGLoggingUnconfigure
_ETLDIAGLoggingQTracesSet
Failed to clear event masks
Response of GUID: Subsystem Command Code: %s (0x%x) \n
_ETLDIAGLoggingEVTSet
Failed to enable events
Failed to get event range from DMC
Response of GUID: Delayed Response ID: %u\n
ETLDiagCreateGUIDDB failed with status: 
:
Failed to get current event mask
 
Response of GUID: OP Code: %u\n
Response of GUID: Number of Files: %u\n
Response of GUID: DIAG ID [%u]: %u\n
Invalid event range: event range last (from DMC): 
Warning: No message ranges found in DMC file\n
_ETLDIAGLoggingMSGClear
ETLDIAGGetGUID
 [subsystem: 
Configuring Logging\n
_ETLDIAGLoggingMSGSwitch
Received %u ranges\n
Response of GUID: Version: %u\n
response 
All subsystems returned empty GUID
vector
Configuring %u message ranges\n
Get GUID try #%d\n
, 
Failed to set event masks
Warning: QTraces are not found.\n
```
