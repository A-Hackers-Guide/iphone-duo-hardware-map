# `/usr/lib/libETLDMCDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 268,048 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 2552)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/libETLDMCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libHDLCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libxml2.2.dylib (compatibility version 10.0.0, current version 10.9.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (186)

```
ETLLOGSetMask
Trying again\n
Bits %u too large\n
Failed to create instance\n
Merging views\n
1X
ETLMESSAGESetSubsystemRuntimeMasksWithRetry
): 
ETLDMCMerge
ETLMESSAGEParseSetAllSubsystemRunTimeMasksResponse
ETLQtraceSend
Audio
OTATypes
ETLLOGCreateSetMaskCommand
ETLQtraceClearSend
BOA
DSP
to 0x%x\n
transport cannot be NULL\n
ETLQtraceParseResponse
%c%d%s%s%s
0x%x
APPS
Error: Mask[%u]: 0x%x, and Received Mask[%u]: 0x%x\n
Partition Range to 0x%08X, max 0x%x\n
ETLMESSAGESetFlags
Status was %u\n
Failed to parse diag command header\n
Powerlog
STx
_ETLDMCAllocate
ETLDMCHandle
ETLLOGParseSetMaskResponse
Error: Received Mask bits upto %u bytes, but the actual payload has %u bytes.\n
ETLMESSAGESetAllSubsystemRunTimeMasks
Returned range 0x%x didn't match requested 0x%x\n
Failed to check payload length\n
Tput
Invald mask type %u\n
Failed to allocate Qtrace Masks\n
Displays
ISVConfig
Couldn't find root node children\n
LogCodes
Bits must be nonzero\n
Response subcommand %u mismatches expected %u\n
Failed to get DMC View for QTrace\n
UMTS
Setting enabled to 0x%x\n
Failed to add spec_count for clearing QTraces\n
VoLTE
RF
SNS
Logging
RSVD3
_
basic_string
ETLDMCViewLoadQTraces
ETLEVENTGetMask
Response has %u bytes, need %u\n
v8@?0
QTraces
[%02u:%02u:%02u:%06u] EVENT 0x%04x 
SUPL
Failed to create command frame\n
ETLEVENTParseSetGetMaskResponseInternal
Need %u bytes for mask of %u bits, only have %u\n
Parsing file\n
Failed to parse OTA Types\n
ETLLOGSetMaskWithRetry
RSVD2
WCDMA
Failed to add header (diag command/subsystem) for setting QTraces\n
Failed to add client id[%d]\n
None
_ETLDMCLoadViewFromFile
Display
Failed on ID %u\n
Total Clinet IDs: 
Message
The number of parsed QTrace (%u) is more than the number to allocate memory (%u)\n
ETLEVENTCreateSetMaskCommand
TDMA
_ETLDMCGetView
Found view %s\n
MessageLevels
GSM
Failed to open file, err = %s(%u)\n
Failed to parse QTraces\n
_ETLDMCParseQTraces
LBS
ETLMESSAGEGetSubsystemMasksWithRetry
\n
Displays View
Warning: QTrace Node is not valid XML Element Node!\n
Unknown
Response subcommand 0x%x mismatches expected 0x%x\n
Lite
Failed to parse Event ID\n
Failed to add action for clearing QTraces\n
Ranges: 
EquipID(
Merged
ETLQtraceBuildCommand
FullPacket
Failed to allocate merged QTrace Client Masks\n
Failed to add reserved for setting QTraces\n
Failed to add arg_count for clearing QTraces\n
_ETLDMCViewCopyMessageMasks
ETLEVENTSetMask
Packet length is (%u), source buffer length is (%u), LOG header size should be (%u), skipping.\n
Failed to parse Message Levels\n
ETLLOGClearAllMasksWithRetry
Error: Mask response mismatch\n
Default
Message View
Couldn't allocate memory for range %u\n
Failed to add arg_count for setting QTraces\n
ETLLOGParseLogRecord
Failed to convert string to number: %s\n
Clearing All Masks\n
Failed to set masks to 0x%x\n
Failed to get free space to the HDLC frame for QTrace clients\n
Verbose
EventIDs
Failed to add action for setting QTraces\n
Sleep
ThirdParty
Warning: QTrace Node is empty!\n
Failed to add spec_count for setting QTraces\n
Failed to add header (diag command/subsystem) for clearing QTraces\n
Logging View
  Clinet ID: 
_ETLDMCViewMergeQTraces
Failed to create XML parser context\n
QXDMProfessional
Set Mask for id %u, bits = %u (%u bytes)\n
ID mismatch. Requested %u, response %u\n
ETLMESSAGEParseSetSubsystemRunTimeMasksResponse
ETLMESSAGEParseSetFlagsResponse
Failed to add client mask[%d]\n
 to 
[%02u:%02u:%02u:%06u: %04x] LOG 0x%02x: 
Persistence
View
ETLMESSAGEFindMatchingResponse
Error Code: %d (0x%x)\n
, Mask: 0x
_ETLDMCViewCopyQTraces
Failed to allocate memory for clientIDMasks to copy\n
MessagesView
LoggingView
Couldn't find root node\n
Coex
QXDM
OEM
Sent:
ETLMESSAGEParseGetSubsystemIDRangesResponse
Failed to get expected subsystem code (0x%x) with actual value (0x%x)\n
GPS
SFT
_ETLDMCCreateFromFile
File size %lli is bigger than max 0x%x\n
DTV
TDS
Received:
Failed to find matching response\n
Setting masks of %u bits\n
%s%u
ETLLOGClearAllEnabledMasksWithRetry
Returned mask %u doesn't match requested %u\n
Failed to get expected subsystem command code (0x%x) with actual value (0x%x)\n
Failed to add reserved for clearing QTraces\n
Couldn't allocate memory for ranges and masks\n
ETLEVENTEnable
Failed to parse QTrace due to malformed format: %s\n
Invalid view %u\n
_ETLDMCLoadFromFile
Warning: response bits %u is less than request %u\n
ETLMESSAGEGetSubcommandTypeForMaskType
ETLMESSAGEParseGetSubsystemMasksResponse
Merged view
enable = %u\n
Done parsing file\n
Couldn't find sub root node\n
ETLQtraceClearBuildCommand
```
