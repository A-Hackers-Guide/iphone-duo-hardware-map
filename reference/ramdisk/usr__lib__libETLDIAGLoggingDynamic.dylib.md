# `/usr/lib/libETLDIAGLoggingDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 100,336 bytes.

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
Invalid event bit mask
Failed to configure message range
Unconfiguring Logging\n
Failed to get current event mask
Failed to get event range from DMC
_ETLDIAGLoggingLOGClear
Request GUID: Subsystem Command: %s\n
Warning: %s does not provide GUID\n
Response of GUID: Subsystem Command Code: %s (0x%x) \n
response 
Response of GUID: DIAG ID [%u]: %u\n
_ETLDIAGLoggingLOGSet
Configuring %u message ranges\n
Failed to clear log masks
 
Configuring log mask for equip ID %s(%u)\n
No event ranges found in DMC file
Response of GUID: Number of Files: %u\n
Failed to clear message masks
Failed to send to clear QTraces
Request GUID: Version: %u\n
Attempt %u\n
All subsystems returned empty GUID
ETLDIAGLoggingUnconfigure
:
_ETLDIAGLoggingMSGSet
Check range %u to %u\n
Failed to enable events
, maskBits (from BBFW): 
]
ETLDIAGLoggingConfigure
ETLDiagCreateGUIDDB request/response version mismatch: 
 [subsystem: 
basic_string
Failed to get event range from DMC file
Response of GUID: Response Count: %u\n
Response of GUID: Version: %u\n
Warning: QTraces are not found.\n
Failed to clear event masks
Response of GUID: GUID [%u]: %s\n
Configuring Logging\n
Failed to set message master switch
Failed to set event masks
_ETLDIAGLoggingMSGClear
Response of GUID: Delayed Response ID: %u\n
ETLDiagCreateGUIDDB failed with status: 
%s\n
request 
Received %u ranges\n
Warning: No message ranges found in DMC file\n
All subsystems returned empty DIAG ID
Response of GUID: OP Code: %u\n
Received more message ranges than expected
Logging configured successfully (maskID = %u)\n
\n
Failed to set log masks
Failed to send QTraces
_ETLDIAGLoggingEVTClear
Failed to configure logging (maskID = %u): %s\n
Failed to un-configure logging: %s\n
vector
No log equip ID found in DMC file
Message range %s, is incorrect\n
Get GUID try #%d\n
, 
Failed to get log mask from DMC
Range %u:\tIDs %u to %u\n
_ETLDIAGLoggingQTracesSet
Invalid event range: event range last (from DMC): 
ETLDIAGGetGUID
Logging un-configured successfully!\n
_ETLDIAGLoggingMSGSwitch
Response of GUID: Delayed Response Status: %u\n
_ETLDIAGLoggingEVTSet
Configuring %u Event Ranges\n
```
