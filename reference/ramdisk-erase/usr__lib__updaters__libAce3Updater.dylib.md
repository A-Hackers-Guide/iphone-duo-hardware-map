# `/usr/lib/updaters/libAce3Updater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 373,424 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3344)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/updaters/libAce3Updater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (6 classes, 0 protocols)

Classes: `Ace3UpdateController`, `Ace3UpdaterInstance`, `NSDictionary`, `SoCUpdaterHelper`, `UARPSoCUpdaterController`, `UARPSoCUpdaterInstance`

## Strings (876)

```
Ace in boot mode: Can't be updated!\n
UARP Restore: Failed to tx uarp message
- MetaData length is %u
%@: Firmware staging failed. Status: 0x%08x (%s), Reason: 0x%08x (%s)
UARPSoCUpdaterFirmwareTssRequest
-[UARPSoCUpdaterController offerFirmwareDataWithDictionary:]
%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>
libusbcupdate-update-all-aces
WARNING: Unexpected tag for offered Dynamic Asset
UARP Restore (Asset Solicitation): %s: No Asset Metadata
UARPSoCUpdaterLayer4ApplePropertyUpdate
%s: options = %@
Unknown Accessory
com.apple.uarp.embedded
HPM in ADFU, yet boot-nonce found to be all 0s, blocking SFWi attempt
Finished AC
Workaround: setting digest list length to 0 because we aren't doing personalization
UARP Restore: Failed to process rx uarp message
Unknown Payload
Mismatch Data Offset
HPM in ADFU in OTA Stage 1\n
Ace never enterred mode 0x%x\n
Finished DL\n
Buffer size = 0! 
fAssetGetBytesAtOffset2
Couldn't get number value\n
Found no matching device tree nodes\n
SocLiveNonce
-[UARPSoCUpdaterInstance initUARPWithFirmware:]
%s: error subclass needs to override this method
Skipping updatable check due to bootarg\n
CoreUARPRestoreAssetApplyStatus
UARP Restore Layer 3: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
No MetaData
In Progress
Version Discovery Request
Endpoint Bulk Information Response Ack
ProductionMode
UpdaterRef
CRPV=0x%llX [16b]\n
%s: NULL pBuffer
Finished init Restore UARP Query Info
%@: _forceLocalSigning = %d
Writing NVRAM variable %s to {0x%02x,0x%02x,0x%02x,0x%02x,0x%02x,0x%02x}\n
SecurityMode
Corrupt SuperBinary
Downstream Endpoint Reachable
Found no matching services
WARNING: HPM in ADFU in Unknown Mode and force_dfu not set\n
get_mode failed in get pers param status=0x%x\n
fAssetProcessingNotificationAck called\n
%s.%u.payload
%@%d
%s Update Finished For Unit (LUN:%d,RouterID:%hhu)
QueryInterface returned 0x%08x\n
Performing ramdisk, ADFU detected\n
fAssetReady
UarpRestoreLayer3FirmwareStageStatusQueueHandler
Unknown Downstream Endpoint
downstream
Invalid UART RID 0x%x for SPI RID 0x%x\n
libusbcupdate-prevent-downgrades
Forcing retimer at RID%u into DFU due to failure to get exclusive access, status=0x%X\n
Failed SFWi on RID %d with 'Flash Busy' error - check SPI flash seating\n
Asset Corrupt
Endpoint Discovery Response
Board ID: %@
-[UARPSoCUpdaterInstance initWithRouterID:helper:options:]
Personalization Failure
Received some payload data
UARP Restore: %s: fLayer3FirmwareStageProgress is NULL
BootedOS
%s: error subclass needs to override this property
Invalid TLV
Invalid Data Transfer Notification
Unsupported Asset Tag
Downstream Endpoint Unreachable Ack
verify_only set! Should not be attempting to flash!\n
Staged Firmware Version Greater than Asset
Staging FW in personalization backend\n
UART HPM interface is NULL for RID %d\n
Final params, after accounting for any endianness quirks:\n
Error creating backend: 0x%x\n
Downstream Endpoint Message
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetSetPayloadIndex failed with status: %u
%s: Failed to init Restore UARP Query Info.
UARPSoCUpdaterLayer4UARPPropertyUpdate
Unsupported Message Type
Asset Available Notification
Skipping firmware update due to version number check
apBORD=0x%X, apChip=0x%X\n
ManifestPrefix
%s: Skipping Apply. Updater(LUN:%d,RouterID:%d) has finished.
Invalid Message Length
Processing Error
Overriding LUN to 1 since it was 0 or unspecified
Ace is in boot mode, trying to read mode again after 1000ms\n
Error querying RID: 0x%x\n
Failed to mark asset as fully staged when verifying version: 0x%x\n
MetaData Corrupt
Invalid Payload
UARP.RESTORE.LAYER3.WATCHDOG.EXPIRE
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestData failed with status: %u
UarpRestoreRemoteEndpointAddHandler
com.apple.uarp.restore.ace3
Options
Verbose
UARP Restore: %s: fLayer3RescindStatus is NULL
performNextStage
%@: Continuing after TSS offer.
%s: There is no asset to apply.
%s: UarpRestoreStageFirmwareDataBuffer() returns %u.
Cannot find address\n
Couldn't find RID for service, skipping!\n
Ace in unexpected mode 0x%08x\n
Ace is in ADFU mode, trying to read mode again after 1000ms
Cannot find start of buffer\n
RestoreInternal
uarpMsgRecvDownstreamEndpointUnreachable
Invalid Message
Asset Decompression Failure
Found updatable Ace based on usbc-update-protocol value\n
Address not number type
Finished AC\n
libUSBCUpdate: Fully torn down
Accessory
CoreUARP Restore IM4M: uarpPlatformEndpointOfferAsset: %d 
Error allocating info\n
UARP.LAYER3.OFFER.SUPERBINARY - Not Implemented
%@,%@
IM4M-CoreUARPRestore-%d-%02d-%02d-%02d-%02d-%02d.uarp
Unrecognized
Failed to persist FW version: 0x%x, treating as non-fatal\n
HPM in ADFU in OTA stage2
UARP Restore: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
Ace3 skip same version: %s
-[UARPSoCUpdaterController numberOfAvailableUnits]
streaming
Proceeding with update to %u.%u.%u.%u because Ace is booted from ramdisk\n
Error converting to UARP version: 0x%x\n
Reading of start_of_buffer failed\n
%s: NULL pBlock
-[UARPSoCUpdaterInstance applyStagedFirmware]
BundleDataDict
USBPortController
HPM in ADFU in OTA stage2\n
Expected more data: actual_more_data=0x%X, length=0x%X, (current_index + bytes_to_write) = 0x%X\n
Error getting active version: 0x%x\n
Failed to free FW Image buffer, stageImage status = 0x%x, DestroyImageBuffer status = 0x%x\n
fPayloadData
ECID
%s: NULL pUarpCtx
UarpRestoreLayer3UarpPropertyUpdateQueueHandler
Information Response
Data Request
Not resetting RID %d in mode 0x%x\n
Error staging FW: 0x%x, abandoning asset\n
UARP Restore: %s: UARPRestoreAsset->_fp is NULL
UARP Restore (Asset Solicitation): %s: fPayloadMetaDataTLV not implemented
%s: Personalization data is expected but empty.
Unknown Data Transfer State
fPayloadWriteToAsset
UARP Restore (Asset Solicitation): %s: pEndpoint is NULL
UARP Restore Layer 3: Solicit Status; status <0x%04x>, reason <0x%04x>
generateMeasurements
-[UARPSoCUpdaterController offerPersonalizationDataWithDictionary:]
%s: Don't offer IM4M Asset to Updater(LUN:%d,RouterID:%d); is done
UARP.LAYER2 <%s> Cannot find downstream endpoint
Staging FW in personalization backend
fAssetMetaDataComplete
-[UARPSoCUpdaterInstance offerPersonalizationResponse:]
Invalid Argument
Retimer SPI NOR access failed, value = %u, status = 0x%X\n
Device error RID=0x%d\n
UARP Restore: %s: fLayer3ApplyStatus is NULL
UARP Restore (Asset Solicitation): %s: %u bytes written
HPM mode=0x%X\n
UARP Restore: Failed to remove endpoint, status 0x%08x
UarpRestoreEndpointDataRecvQueueHandler
AppleHPMDeviceHALType3
verify_only set; avoiding unnecessary SFWi calls
Setting payload index\n
Payload Data complete
Waiting for processing notification before closing
Trusted
Invalid Super Binary Header
IONameMatch
%s: Received Invalid tssOptions
%@ Update: %u%%
Yes
Path
Ignoring initialization option to skip flashing same verison based on bootarg\n
Workaround: not putting any bits of the digest list into the image, due to no personalization
UARP Restore: UARP RX: Buffer = %p, Payload Length = %u, Type = 0x%04x, Total Length = %u, ID = %u
%@
Unknown Personalization Option
%02X
fAssetReleased2 called\n
BoardId
Unknown
Bad task result from %c%c%c%c 4CC: 0x%x\n
CPFM
Received %d bytes of IM4M\n
ERROR: failed in fAssetAllHeadersAndMetaDataComplete, status = 0x%x (%s)\n
@%@
UarpRestoreLayer3FirmwareApplyStatusQueueHandler
Asset Processing Notification Ack
WARNING: SFWi failed status=0x%X, task_result=0x%X\n
Bad return value from version register read: 0x%x\n
fAssetProcessingNotificationAck called
UarpRestoreEndpointMsgRecvQueueHandler
usbc,sn201202x,spmi
Workaround: setting digest list length to 0 because we aren't doing personalization\n
Setting payload index
Ticket
%s: Tss Response: %@
%s (%d)
%s: Maybe Offer IM4M Asset to Updater(LUN:%d,RouterID:%d); %@
Asset Transfer Complete
usbc-update-protocol
IOService
AAPL,phandle
UARP Restore: UARP RX: Asset Available Notification; Asset ID %u
Payload Index %u
UarpRestoreAssetSolicitationHandler
%s: Success.
Unknown Information Option
Invalid EndpointID
Success
Asset Rescinded Notification Ack
UARP Restore: %s: Accepted dynamic asset
uarpMsgRecvDownstreamEndpointMessage
Processing Incomplete
USBFirmware
UARP Restore: UARP RX: Asset Processing Notification ACK; Asset ID %u
BoardID
ForceLocalSigning
Invalid Data Request Length
ERROR: Unexpected read length for register 0x2c: 0x%llx\n
boardID=0x%llX\n
Received some payload data\n
UARP Restore: %s: Rx pRestoreAsset was NULL
%@: staging complete signaling waiting callbacks
Endpoint Bulk Information Request
Found no matching device tree nodes
-[Ace3UpdaterInstance uarpRestoreInitOptions]
uarp
%@: options = %@
%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>
Invalid Object
otpBuf:\n
UART HPMs not found, treating as non-fatal
Error allocating accessory
UarpRestoreLayer3TssRequestQueueHandler
UARP Restore: Mismatch in writing to personalized firmware file %s.Expected to write %d bytes, actually wrote %d bytes
Failed to get mode for RID %d: 0x%x\n
ace3
%@: Waiting for TSS offer to complete...
-[UARPSoCUpdaterInstance tssRequestWithOptions:serverURL:assetCtx:siliconCtx:]
%s[%u]
Information Request
libusbupdate-allow-same-version
Non-Fatal error sending tag hint(0x%x) to backend: 0x%x\n
UARP Restore: UARP RX: Asset Processing Notification; Asset ID %u
UARP Restore (Asset Solicitation): %s: fseek failed
Options Passed: %@
Offering FIRM to controller\n
w+
UARP Restore (Asset Solicitation): %s: fAssetMetaDataTLV not implemented
fAssetStore
%@: TSS request signal waiting callbacks
%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Asset In Flight
Address
UARP Restore: %s: Protocol Version Selected %d, was previously %d
DeferredCommit
%@: Waiting for staging to complete...
Unexpected boot flags register length %llu\n
%s: Local Signing is enabled, no personalization data expected.
Unexpected usbc-update-protocol value %d\n
Preparing to flash 0x%x bytes of image to rid %d\n
Cannot find start_of_needle
UARP.LAYER3.TRANSFER.PAUSE.ACK - Not Implemented
%s: error allocating options: No resources
BuildIdentity
MetaData Type Not Found
Begin Manifest Request
%s: NULL pIM4M->payloads
transmitqueue
Downstream Endpoint Unreachable
Offering IM4M to controller\n
Updating to version %u.%u.%u.%u\n
Error allocating accessory\n
CoreUARP Restore IM4M: CoreUARPRestoreBuildPersonalizationResponse: %d 
%s: Skipping Offer Firmware. Updater(LUN:%d,RouterID:%d) has finished.
verify_only set; avoiding unnecessary SFWi calls\n
LocalSigningID
com.apple.AppleAccessoryManager
%@: Continuing after staging.
%s: More TSS Request for Updater(LUN:%d,RouterID:%d)
No Resources
Dynamic Asset Solicitation Ack
RID%u not in restore and getting exclusive access failed, status=0%X\n
validate_same_version: existing = %d.%d.%d.%d, new = %d.%d.%d.%d\n
Offering FIRM to controller
Ace in mode 0x%08x, performing SFW flash\n
False
UARPSoCUpdaterApplyComplete
Same Version Active
memory
Found updatable Ace based on usbc-update-protocol value
HPM in ADFU in OTA Stage 1
Reading of start_of_buffer failed
CoreUARP Restore IM4M: First Pass on TLV <0x%08x>
Dynamic Asset PreProcessing Notification
UARP Restore: %s: fLayer3AssetSolicitationProgress is NULL
fRestoreUARPDynamicAssetOffered
%s: Success. tssOptions:%@, tssServer:%@ 
MetaData Overflow
BDID
chipID=0x%X\n
%1hhx
UARP Restore (Asset Solicitation): %s: pAsset is NULL
CoreUARP Restore IM4M: Post-Layer3: TSS Response is NULL
assert
Asset Rescinded Notification
USBCUpdate: Calling Asset Fully Staged from Processing Notification
libusbcupdate-skip-restore
NONC
Require Personalization = %s\n
fAssetMetaDataTLV
v8@?0
[%s:%s] %s
Error when powering on retimer on RID%u status=0x%X\n
Overriding tag value to 0x%x (was 0x%x) based on metadata hint\n
Stage image\n
Reading bytes failed, nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n
UARP Restore: Could not open personalized firmware file %s
UARPSoCUpdaterLayer4PropertiesComplete
Downstream Endpoint Reachable Ack
USBCUpdate: Calling Asset Fully Staged from Processing Notification\n
usbc,sn201202x,iic
Invalid Asset Type
Invalid Data Response
Cannot find address
Ace is in boot mode, trying to read mode again after 1000ms
Finished DL
%s: %@ Offering Firmware
%s: Failed to receive tssOptions.
%s: Offering Tss Response
DestBundlePath
Buffer Overflow
Failed to set nvram variable %s: 0x%x\n
-restore is %u\n
UARP Restore: Failed to allocate restore asset
Unknown Asset
Staged Firmware Version Equal to Asset
Ace in boot mode: Can't be updated!
SDOM=0x%llX [8b]\n
%s: Unable to locate firmware data.
Asset Not Found
Performing ramdisk, ADFU detected
%2hhx
EPRO
%s: NULL tssOptions
RestoreSystemPartition
Duplicate Accessory
Asset Data Transfer Notification Ack
No Firmware Update Available Ack
Error finding IOKit service: 0x%x\n
Ace is in APP mode, trying to read mode again after 1000ms\n
UARPSoCUpdaterStagingComplete
Warning: Received status 0x%x when reading mode, delaying 1000ms and trying again
Failed to get AHPMLibInterface for RID %d: 0x%x\n
True
UARP Restore: Read error %d, Read %zu bytes
No available units to be updated
%@: Maybe Offer / Stage Firmware
com.apple.uarp.layer3.soc
Apply Staged Assets Request
Asset Available Notification Ack
uarpMsgRecvDownstreamEndpointUnreachableAck
Error allocating info
CoreUARPRestoreAssetTransferStatus
<unknown>
%s.queue
Failure
Ace is in APP mode, trying to read mode again after 1000ms
SDOM
UARP Restore: %s: Asset fully transfered; %c%c%c%c
UARP.LAYER3.TRANSFER.PAUSE - Not Implemented
fPayloadDataComplete
Same Version Staged
Error finding matching device tree nodes: 0x%x\n
Cannot find start_of_needle\n
Failed to create updater instance for LUN %d
Error when reading usbc-update-protocol: 0x%x\n
fAssetReleased2 called
CoreUARPRestoreAssetPersonalizedFirmware
UARP.LAYER3.TRANSFER.RESUME - Not Implemented
-[UARPSoCUpdaterInstance uarpRestoreInitOptions]
%s: UarpRestoreInitializeEndpoint() returns NULL.
Unexpected version register length %llu\n
PreflightRequired
BuildIdentityTags
platform
tag-number
Final params, after accounting for any endianness quirks:
ChipID
Chip ID: %@
PreflightTickets
%s: data = %@
Invalid Data Request Type
Mid Upload
Overriding LUN to 1 since it was 0 or unspecified\n
Bad return value from boot flags register read: 0x%x\n
-[UARPSoCUpdaterController applyStagedFirmware]
Failed to build and Stage personalized FW: 0x%x\n
fPayloadMetaDataComplete
- Version is %u.%u.%u.%u
ESEC
In Use
UART HPM RID%d in VOUT, GAID skipped and APP mode check will be skipped\n
Received the whole IM4M
UARP Restore: %s: Query %d info properties and %d Apple properties
- Data length is %u
%s: More tss request for next round.
Invalid Offset
Cancelled Asset Tag
Ignore Version = %s\n
UARP Restore: EOF %d, Read %zu bytes
Unknown Message Type
uarpTransmitEntryIsValidToSend
Error finding the spi-flash-parent
Found matching tags %s\n
Created updater instance for LUN %d
UARP Restore (Asset Solicitation): %s: No Payload Metadata
UARP Restore: Offered Firmware with outstanding offer
queryInfo
Persistent flash successful
Data Response
UARP Restore: %s: Firmware Asset fully transfered
%@: Detected updater mode %s
uart-hpm-rids
-restore
usbc,version,rid%d
libUSBCUpdate: Fully torn down\n
Cannot find start of buffer
Failed to set FIRM payload index; %u
-[UARPSoCUpdaterController offerFirmwareForUpdater:inputDict:]
Invalid Length
Higher Version Active
CPID=0x%llX [16b]\n
Built and Staged the personalized FW\n
UARP Restore: Failed to accept superbinary; 0x%08x
OTA Stage 2
Unsupported Hardware Revision
Apply Staged Assets Response
UART HPMs reset failed, status=0x%X, treating as non-fatal\n
Received error 0x%x from GAID, silencing\n
Return value from GAID on RID %d: 0x%x\n
Nonce
UarpRestoreLayer3AssetSolicitationStatusQueueHandler
OTA Stage 1
Error finding the atcrt service (found the iic service)
verify_only set! Should not be attempting to flash!
UarpRestoreStageFirmwareDataBufferQueueHandler
UarpRestoreApplyStagedAssetsHandler
Priority Activity
Failed to recv message, status = 0x%x\n
Waiting for processing notification before closing\n
PreflightContext
Limited
%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Out Of Order Message ID
RID0 cannot get exlusive access from retimer, status=0x%X, will assume implicit permission\n
pStatus=%d, secMode=%d, SDOM=0x%X, PREV=0x%X\n
UARP Restore: %s: fLayer3AssetSolicitationStatus is NULL
Unexpected boot source after ADF* update: 0x%x\n
Received the whole IM4M\n
CoreUARPRestoreAssetRescindStatus
DigestListSize
Tethered Preflight
%s: Offer IM4M Asset to Updater(LUN:%d,RouterID:%d)
Error decompressing buffer for payload
UARP Restore: %s: Provided filepath is greater than max filepath length %i
Payload Metadata <0x%08x>
%@: Really Offer / Stage Firmware
%s
-[UARPSoCUpdaterController createUpdaterInstanceFor:helper:options:]
Needs Restart
Couldn't get number value
UARP.LAYER3.APPLY.ASSETS - Not Implemented
%s: error allocating callbacks: No resources
Skipping firmware update due to version number check\n
WARNING: HPM in ADFU in Unknown Mode and force_dfu not set
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetRequestMetaData failed with status: %u
NeRD Preflight
Stage image
UARP Restore: %s: pAsset->_pAsset is NULL
%@ Update: 100%%
product
UARP Restore: %s: uarpPlatformEndpointPrepareSolicitedDynamicAsset() failed; 0x%08x
No
Upload Abandoned
fAssetSetBytesAtOffset2
Is Display & has Preflight Tickets - setting to Stage 1
NeRD Stage1
IODeviceTree:/options
Error finding the spi-flash-parent\n
CPID
fAssetProcessingNotification2
Endpoint Discovery Request
Current firmware version: %u.%u.%u.%u, new version: %u.%u.%u.%u\n
UarpRestoreAssetSolicitation
Buffer Would Overflow
Downstream Endpoint Discovery
%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p
Couldn't find RID for service, skipping!
Finished Patch
UarpRestoreStageFirmwareFilenameQueueHandler
-[UARPSoCUpdaterInstance uarpRestoreLayer4Callbacks]
%s (%s)
Vendor Specific
AppleHPM
Error when relinquishing shared SPI access on RID%u status=0x%X\n
Workaround: not putting any bits of the digest list into the image, due to no personalization\n
Found Board ID 0x%llx\n
UARP Restore: Failed to open file %s
UARP.RESTORE.LAYER3.INFO.RESPONSE <Last Error> - Not Implemented
%s: ERROR adding remote endpoint, status = 0x%08x
CPFM=0x%llX [8b]\n
Digest
BundlePath
Invalid Function Pointer
Built and Staged the personalized FW
UARP Restore: %s: fLayer3FirmwareStageStatus is NULL
UARP Restore (Asset Solicitation): %s: Asset fully staged
CoreUARP Restore IM4M: Building Personalization Response
%s: NULL pIM4M
-[UARPSoCUpdaterInstance receievePersonalizationRequestByOfferFirmwareData:]
Endpoint Component Discovery Request
UARP Restore: Failed to offer superbinary
fPayloadMetaDataTLV
UARP Restore (Asset Solicitation): %s: uarpAssetQueryPayloadInfo failed with status: %u
No Version Agreement
Upload Denied
spi-flash-parent
Ace is in ADFU mode, trying to read mode again after 1000ms\n
UARP.LAYER3.WATCHDOG.CANCEL
com.apple.uarp.layer3.restore
-[UARPSoCUpdaterInstance uarpRestoreQueueName]
%@ Staging Complete
Info
Invalid Data Request Offset
Unsupported
Asset Processing Notification
UARP Restore: %s: fLayer3PersonalizedFirmware is NULL
fRestoreUARPProtocolVersion
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestMetaData failed with status: %u
UARP Restore (Asset Solicitation): %s: pAsset->_fp is NULL
UARP Restore: Could not open manifest file %s
Invalid Data Response Length
Mismatch Personalization Option
RID
UarpRestoreLayer3MsgSendQueueHandler
%s: Failed to init Restore UARP.
IOPropertyMatch
Error: Got unexpected VID 0x%x\n
PREV=0x%llX [8b]\n
Device Error
Dynamic Asset PreProcessing Notification Ack
Endpoint Component Discovery Response
Warning: Frontend expects tag to be %d, but Backend is using tag %d\n
libusbcupdate_log
Payload Data complete\n
Finished Patch\n
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Info - %d )
SkipSameVersion
Active Firmware Version Equal to Asset
No Firmware Update Available
UARP Restore: Failed to offer superbinary, status 0x%08x
uarpPlatformEndpointRecvMessage
Unknown Controller
Invalid Payload Header
Unknown Failure
Offering IM4M to controller
UARP Restore (Asset Solicitation): %s: remove failed
UarpRestoreLayer3ApplePropertyUpdateQueueHandler
%@: Don't Offer / Stage Firmware
uarpMsgRecvDownstreamEndpointReachable
Host Controller
Sync
Downstream Endpoint Discovery Ack
otpBuf:
GR2
%s: Updating is not finish yet for unit with LUN: %d, RouterID: %d
ResponseTags
Asset Invalid Compression
Exceeded Packet Retry
Low Battery
Flashing block %d, CRC = 0x%08x\n
ECID=0x%llX\n
r
uarpPlatformEndpointStreamingRecvBytes() failed; 0x%08x
TicketName
%s: Skipping Apply for Updater(LUN:%d,RouterID:%d)
Address not number type\n
Skipping updatable check due to bootarg
UARP Restore: Failed to tx uarp message to uarp silicon updater;status <0x%08x>, %s
Active Firmware Version Greater than Asset
Error when forcing ATCRT update on RID%u status=0x%X\n
queryTags
Version Discovery Response
Found tag value %d for RID %d\n
Incompatible Protocol Version
HigherVersion
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
Endpoint Bulk Information Response
Trying to find AHPMLibInterface for RID 0x%02x\n
ERROR: Unexpected second read length for register 0x2c: 0x%llx\n
-[UARPSoCUpdaterInstance initUARP]
Data Transfer Paused
AppleARMIICDevice
UART HPMs not found, treating as non-fatal\n
- Tag is %c%c%c%c
UARP Restore: Mismatch in writing to manifest file %s.Expected to write %d bytes, actually wrote %d bytes
Tethered
Duplicate Controller
Asset No Bytes Remaining
Unexpected length of field %s in USB string: 0x%lx bytes\n
CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
FirmwareData
Nothing Staged
protocolaccessory
Downstream Endpoint Message Ack
PREV
CoreUARPRestoreAssetTransferProgress
UARP Restore: Tatsu Server set to %s
UarpRestoreInfoQueriesQueueHandler
-[UARPSoCUpdaterInstance initWithLogicUnitNumber:helper:options:]
Asset Data Paused
libusbcupdate-always-personalize
CPRV
Unexpected RID size: 0x%x\n
UARP.RESTORE.LAYER3.INFO.RESPONSE <Statistics> - Not Implemented
UARP Restore Layer 3: Stage Status; status <0x%04x>, reason <0x%04x>
%s: Applying Staged Assets
Invalid Asset Tag
Dynamic Asset Solicitation
Persistent flash successful\n
Failing message: 0x%02x%02x%02x%02x%02x%02x
Begin Manifest Request\n
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetQueryNumberOfPayloads failed with status: %u
-[Ace3UpdateController createUpdaterInstanceFor:helper:options:]
OTA Preflight
Upload Complete
protocolcontroller
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
Switching to using LUN %d based on hint\n
Found no matching services\n
UARP Restore: %s: pAsset is NULL
UARP Restore (Asset Solicitation): %s: pPayload->_fp is NULL
<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>
success
Mismatch UUID
Asset Id Unknown
BDID=0x%llX\n
nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n
CoreUARPRestoreQueryOutstandingInfoProperties
UARP Restore (Asset Solicitation): %s: fAssetProcessingNotification2 not implemented
%s: Error: Multiple payload needs personalization
rid
WARNING: Unexpected tag for offered Dynamic Asset\n
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Apple - %d )
UARP Restore: %s: uarpPlatformEndpointSolicitDynamicAsset() failed; 0x%08x
UARP Restore: %s: Protocol Version Not Selected; defer info queries
Failed to force retimer at RID%u into DFU, status=0x%X\n
fPayloadReady
Duplicate Message ID
Error finding the atcrt service (found the iic service)\n
UARP.LAYER3.TRANSFER.RESUME.ACK - Not Implemented
Asset Data Transfer Notification
HPM in ADFU, yet boot-nonce found to be all 0s, blocking SFWi attempt\n
Ignoring initialization option to skip flashing same verison based on bootarg
Searching for Board ID 0x%llx\n
SecurityDomain
-[Ace3UpdaterInstance uarpRestoreLayer4Callbacks]
\n
Endpoint Bulk Information Request Ack
IOParentMatch
Error: Got unexpected DID 0x%x\n
DeviceInfo
Better Transport
Controller
%s\n
%s
Ace3UpdateController
Ace3UpdaterInstance
KeyPrefixSearch
SoCUpdaterHelper
UARPSoCUpdaterInstance
UARPSoCUpdaterController
setApplyFlags:
setRouterID:
updaterMode
TI,V_logicUnitNumber
TI,V_stagingStatus
initUARPComplete
namePrefix
numberOfAvailableUnits
logicUnitNumber
setUpdaterMode:
_pAssetContext
countByEnumeratingWithState:objects:count:
firmwareTags
initializeUpdatersWithOptions:
unsignedIntValue
boolValue
bytes
initWithOptions:logFunction:logContext:
updateAppleProperty:siliconCtx:
offerFirmwareDataWithDictionary:
personalizationRequestDict
length
name
offerFirmwareData:
verboseLog:
UTF8String
_personalizationRequests
offerPersonalizationResponse:
printUpdaterMode
_stagingResult
keyWithPrefix:
TI,V_applyFlags
TI,V_stagingStatusReason
_logContext
routerID
skipApplyStage
setLogicUnitNumber:
log
_skipSameVersion
count
setLog:
arrayWithArray:
offerPersonalizationDataWithDictionary:
initWithHelper:options:
log:
stringWithString:
ticketNameTags
_uarpContext
hasPrefix:
ticketName
_nextUpdateProgressReportPercentThreshold
dictionaryWithDictionary:
init
updateStagingProgressWithBytesSent:bytesTotal:
useLocalSigning
applyStagedFirmware
dictionaryWithObjects:forKeys:count:
initWithRouterID:helper:options:
isEqual:
personalizationRequests
Ti,V_updaterMode
initWithLogicUnitNumber:helper:options:
manifestPrefix
setStagingStatusReason:
stringWithFormat:
.cxx_destruct
T@\"NSString\",R,V_restorePartition
_isDone
TB,R,V_isDone
_forceLocalSigning
_logFunction
_name
objectAtIndexedSubscript:
_assetTransferUARPSemaphore
_prefixNeedsLogicalUnitNumber
addObject:
applyFlags
offerFirmwareForUpdater:inputDict:
stagingCompleteWithStatus:reason:
_restorePartition
_tssRequestServerURL
addEntriesFromDictionary:
_applyFlags
_queue
applyAssetComplete
uarpRestoreLayer4Callbacks
updaterLog:
numberWithBool:
_verbose
queryInfo
stagingStatus
uarpRestoreQueueName
TC,V_routerID
initUARPWithFirmware:
receievePersonalizationRequestByOfferFirmwareData:
firmwareTagName
_lastPercentComplete
_log
T@\"NSString\",R
_logicUnitNumber
_suffixNeedsLogicalUnitNumber
logInternal:arguments:
stagingStatusReason
_logicUnitNumberFromDevice
_updaterMode
assetTransferUARPComplete
initWithFormat:arguments:
_applyAssetUARPSemaphore
_endpoint
_initUARPSemaphore
_stagingStatusReason
copy
createUpdaterInstanceFor:helper:options:
objectForKeyedSubscript:
restorePartition
TB,R
_requiresPersonalization
_routerID
T@\"NSDictionary\",R
TB,R,V_skipSameVersion
skipSameVersion
_manifestPrefixName
isDone
setStagingStatus:
stringWithUTF8String:
_updaters
appendString:
initUARPRestoreQueryInfo
isEqualToString:
tssRequestWithOptions:serverURL:assetCtx:siliconCtx:
_ticketLongName
_stagingStatus
_tssRequest
initUARP
uarpRestoreInitOptions
T@\"SoCUpdaterHelper\",&,V_log
^?
v20@0:8C16
I16@0:8
^v16@0:8
r*16@0:8
@24@0:8@16
@\"NSDictionary\"
B16@0:8
B24@0:8@16
C16@0:8
i
C
^{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8
v24@0:8@16
v24@0:8I16I20
i16@0:8
@\"SoCUpdaterHelper\"
v32@0:8@16*24
B
@16@0:8
v48@0:8@16@24^v32^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}40
^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^
I
B32@0:8@16@24
@32@0:8@16@24
@36@0:8I16@20@28
v20@0:8I16
@\"NSString\"
@36@0:8C16@20@28
v16@0:8
v28@0:8I16^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}20
@\"NSObject<OS_dispatch_queue>\"
^v
@40@0:8@16^?24^v32
v20@0:8i16
@\"NSObject<OS_dispatch_semaphore>\"
@\"NSMutableArray\"
```
