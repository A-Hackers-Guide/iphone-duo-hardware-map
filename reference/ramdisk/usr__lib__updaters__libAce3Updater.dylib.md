# `/usr/lib/updaters/libAce3Updater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 373,424 bytes.

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
Buffer Overflow
Staging FW in personalization backend
Found no matching device tree nodes\n
Couldn't get number value
Unexpected boot source after ADF* update: 0x%x\n
UARP Restore (Asset Solicitation): %s: %u bytes written
Endpoint Bulk Information Request
%02X
Finished Patch
CoreUARPRestoreAssetPersonalizedFirmware
UARP Restore: %s: Accepted dynamic asset
Unknown Controller
UARP Restore (Asset Solicitation): %s: uarpAssetQueryPayloadInfo failed with status: %u
fAssetSetBytesAtOffset2
Invalid Function Pointer
Information Request
Dynamic Asset PreProcessing Notification Ack
UARP Restore: Failed to open file %s
performNextStage
%s: Don't offer IM4M Asset to Updater(LUN:%d,RouterID:%d); is done
No Resources
Invalid Data Response
In Progress
get_mode failed in get pers param status=0x%x\n
Ace in boot mode: Can't be updated!
\n
%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Host Controller
Downstream Endpoint Message Ack
libusbcupdate_log
verify_only set! Should not be attempting to flash!
Finished Patch\n
Error staging FW: 0x%x, abandoning asset\n
%s: UarpRestoreStageFirmwareDataBuffer() returns %u.
Asset Data Paused
Controller
Failed to get AHPMLibInterface for RID %d: 0x%x\n
HPM in ADFU in OTA Stage 1
Received the whole IM4M\n
Found Board ID 0x%llx\n
UARP Restore (Asset Solicitation): %s: fAssetMetaDataTLV not implemented
%s: Failed to init Restore UARP Query Info.
downstream
Error querying RID: 0x%x\n
UARP.LAYER3.TRANSFER.RESUME - Not Implemented
OTA Stage 2
-[UARPSoCUpdaterInstance tssRequestWithOptions:serverURL:assetCtx:siliconCtx:]
%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>
Asset Id Unknown
Unsupported
Unknown Payload
Vendor Specific
fPayloadMetaDataTLV
No Firmware Update Available
Ace never enterred mode 0x%x\n
Device error RID=0x%d\n
Performing ramdisk, ADFU detected
Require Personalization = %s\n
Failed to mark asset as fully staged when verifying version: 0x%x\n
SecurityMode
Failed to create updater instance for LUN %d
Path
uarpMsgRecvDownstreamEndpointReachable
tag-number
fAssetProcessingNotificationAck called
UARP Restore (Asset Solicitation): %s: pAsset->_fp is NULL
SocLiveNonce
%@,%@
generateMeasurements
PreflightTickets
Invalid Argument
Unexpected usbc-update-protocol value %d\n
HPM in ADFU in OTA stage2
UARP Restore: %s: fLayer3FirmwareStageStatus is NULL
Trusted
Apply Staged Assets Response
Found tag value %d for RID %d\n
Preparing to flash 0x%x bytes of image to rid %d\n
Stage image\n
Buffer size = 0! 
UARP Restore Layer 3: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
protocolaccessory
UARP Restore: UARP RX: Buffer = %p, Payload Length = %u, Type = 0x%04x, Total Length = %u, ID = %u
CoreUARPRestoreAssetTransferStatus
%s: Offering Tss Response
%@: options = %@
IOParentMatch
Found no matching services
Offering IM4M to controller
Unexpected version register length %llu\n
OTA Stage 1
%s
Unknown Asset
PREV=0x%llX [8b]\n
Built and Staged the personalized FW\n
UarpRestoreEndpointMsgRecvQueueHandler
UARP Restore: Failed to tx uarp message to uarp silicon updater;status <0x%08x>, %s
%s: There is no asset to apply.
%s: Updating is not finish yet for unit with LUN: %d, RouterID: %d
Unknown Personalization Option
No Version Agreement
UarpRestoreLayer3FirmwareStageStatusQueueHandler
queryTags
-[UARPSoCUpdaterInstance offerPersonalizationResponse:]
Asset Transfer Complete
Mismatch Personalization Option
Unknown Data Transfer State
Invalid Length
platform
fAssetMetaDataComplete
UarpRestoreLayer3MsgSendQueueHandler
MetaData Corrupt
Data Request
UART HPMs not found, treating as non-fatal
Overriding tag value to 0x%x (was 0x%x) based on metadata hint\n
Error creating backend: 0x%x\n
Error converting to UARP version: 0x%x\n
Ace3 skip same version: %s
Info
Upload Abandoned
True
Setting payload index\n
UARP Restore: Failed to allocate restore asset
Invalid Data Transfer Notification
HPM in ADFU, yet boot-nonce found to be all 0s, blocking SFWi attempt\n
apBORD=0x%X, apChip=0x%X\n
Searching for Board ID 0x%llx\n
Setting payload index
UARP Restore: Failed to process rx uarp message
UARP Restore (Asset Solicitation): %s: pAsset is NULL
Device Error
Retimer SPI NOR access failed, value = %u, status = 0x%X\n
Ace is in ADFU mode, trying to read mode again after 1000ms\n
pStatus=%d, secMode=%d, SDOM=0x%X, PREV=0x%X\n
com.apple.uarp.restore.ace3
%s: data = %@
UARPSoCUpdaterFirmwareTssRequest
%s: options = %@
Duplicate Message ID
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
Information Response
HPM in ADFU, yet boot-nonce found to be all 0s, blocking SFWi attempt
UARP Restore (Asset Solicitation): %s: fAssetProcessingNotification2 not implemented
BoardId
SkipSameVersion
Error finding matching device tree nodes: 0x%x\n
IODeviceTree:/options
otpBuf:\n
False
CoreUARPRestoreAssetApplyStatus
com.apple.uarp.layer3.restore
Performing ramdisk, ADFU detected\n
Ignore Version = %s\n
%s: Skipping Apply for Updater(LUN:%d,RouterID:%d)
No
-[UARPSoCUpdaterController numberOfAvailableUnits]
Ace is in boot mode, trying to read mode again after 1000ms\n
%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Unknown Failure
Ignoring initialization option to skip flashing same verison based on bootarg\n
chipID=0x%X\n
uarpPlatformEndpointStreamingRecvBytes() failed; 0x%08x
-[Ace3UpdateController createUpdaterInstanceFor:helper:options:]
-[UARPSoCUpdaterInstance uarpRestoreInitOptions]
Asset Corrupt
UARP Restore: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
Dynamic Asset Solicitation Ack
Failed to free FW Image buffer, stageImage status = 0x%x, DestroyImageBuffer status = 0x%x\n
fAssetStore
UARP Restore: Mismatch in writing to personalized firmware file %s.Expected to write %d bytes, actually wrote %d bytes
-[UARPSoCUpdaterInstance receievePersonalizationRequestByOfferFirmwareData:]
%@: Detected updater mode %s
uarpMsgRecvDownstreamEndpointMessage
Asset Rescinded Notification
Endpoint Bulk Information Response
Found no matching services\n
%s: Skipping Apply. Updater(LUN:%d,RouterID:%d) has finished.
Asset Decompression Failure
Unsupported Message Type
Version Discovery Response
libusbcupdate-update-all-aces
Couldn't find RID for service, skipping!
UART HPM interface is NULL for RID %d\n
Ignoring initialization option to skip flashing same verison based on bootarg
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestData failed with status: %u
Tethered
%s: Maybe Offer IM4M Asset to Updater(LUN:%d,RouterID:%d); %@
Invalid Data Request Type
Active Firmware Version Equal to Asset
QueryInterface returned 0x%08x\n
Workaround: setting digest list length to 0 because we aren't doing personalization\n
Verbose
Invalid Payload Header
Offering FIRM to controller
AppleARMIICDevice
HPM in ADFU in OTA stage2\n
SDOM=0x%llX [8b]\n
CoreUARP Restore IM4M: First Pass on TLV <0x%08x>
BuildIdentityTags
Out Of Order Message ID
Duplicate Accessory
Unknown Downstream Endpoint
Endpoint Discovery Request
uart-hpm-rids
UARP Restore (Asset Solicitation): %s: pEndpoint is NULL
%s: Personalization data is expected but empty.
In Use
Downstream Endpoint Discovery
Finished DL\n
UARP Restore: UARP RX: Asset Available Notification; Asset ID %u
- Tag is %c%c%c%c
BoardID
-restore is %u\n
libusbcupdate-skip-restore
Bad return value from boot flags register read: 0x%x\n
LocalSigningID
GR2
%s: Success.
Unexpected boot flags register length %llu\n
libUSBCUpdate: Fully torn down\n
UARP Restore (Asset Solicitation): %s: Asset fully staged
PreflightRequired
-[UARPSoCUpdaterInstance initWithRouterID:helper:options:]
Address not number type
UarpRestoreAssetSolicitation
Couldn't find RID for service, skipping!\n
ERROR: failed in fAssetAllHeadersAndMetaDataComplete, status = 0x%x (%s)\n
fAssetReady
Digest
Skipping updatable check due to bootarg\n
USBPortController
otpBuf:
ECID=0x%llX\n
SecurityDomain
DeferredCommit
-[UARPSoCUpdaterInstance initWithLogicUnitNumber:helper:options:]
%s: error subclass needs to override this property
%@ Staging Complete
com.apple.uarp.layer3.soc
Processing Error
transmitqueue
%s.%u.payload
UarpRestoreLayer3AssetSolicitationStatusQueueHandler
UarpRestoreInfoQueriesQueueHandler
%@: Continuing after TSS offer.
%@: TSS request signal waiting callbacks
<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>
Overriding LUN to 1 since it was 0 or unspecified\n
libusbcupdate-always-personalize
UARP Restore: UARP RX: Asset Processing Notification; Asset ID %u
Address
Error finding the atcrt service (found the iic service)\n
Skipping firmware update due to version number check\n
verify_only set; avoiding unnecessary SFWi calls
WARNING: HPM in ADFU in Unknown Mode and force_dfu not set
CPID
-[Ace3UpdaterInstance uarpRestoreLayer4Callbacks]
-[UARPSoCUpdaterInstance initUARPWithFirmware:]
HPM in ADFU in OTA Stage 1\n
Return value from GAID on RID %d: 0x%x\n
CPFM
Failed to build and Stage personalized FW: 0x%x\n
Stage image
- Data length is %u
UARP Restore: Mismatch in writing to manifest file %s.Expected to write %d bytes, actually wrote %d bytes
BundlePath
Processing Incomplete
Offering FIRM to controller\n
BDID=0x%llX\n
Reading of start_of_buffer failed\n
UARP Restore: %s: pAsset is NULL
-[UARPSoCUpdaterInstance initUARP]
Higher Version Active
Unexpected RID size: 0x%x\n
Workaround: setting digest list length to 0 because we aren't doing personalization
UARP.LAYER3.TRANSFER.RESUME.ACK - Not Implemented
Exceeded Packet Retry
assert
UARP Restore: Offered Firmware with outstanding offer
queryInfo
%@: Waiting for staging to complete...
Invalid TLV
Error when relinquishing shared SPI access on RID%u status=0x%X\n
Options
%@: Continuing after staging.
memory
Updating to version %u.%u.%u.%u\n
Workaround: not putting any bits of the digest list into the image, due to no personalization\n
CoreUARP Restore IM4M: CoreUARPRestoreBuildPersonalizationResponse: %d 
Forcing retimer at RID%u into DFU due to failure to get exclusive access, status=0x%X\n
DigestListSize
Chip ID: %@
Tethered Preflight
%s: UarpRestoreInitializeEndpoint() returns NULL.
UarpRestoreLayer3ApplePropertyUpdateQueueHandler
TicketName
UARPSoCUpdaterLayer4PropertiesComplete
-[UARPSoCUpdaterController offerFirmwareForUpdater:inputDict:]
Invalid Super Binary Header
-[UARPSoCUpdaterController applyStagedFirmware]
Created updater instance for LUN %d
Invalid Data Request Length
Asset No Bytes Remaining
verify_only set; avoiding unnecessary SFWi calls\n
SDOM
fAssetReleased2 called
%s: NULL pIM4M->payloads
[%s:%s] %s
Failed to set nvram variable %s: 0x%x\n
%1hhx
UARP Restore: Could not open personalized firmware file %s
UarpRestoreStageFirmwareFilenameQueueHandler
Incompatible Protocol Version
Invalid Object
Invalid Payload
Warning: Frontend expects tag to be %d, but Backend is using tag %d\n
Cannot find address
Found no matching device tree nodes
%s: NULL pIM4M
%s: error allocating callbacks: No resources
No MetaData
Error allocating info
Received some payload data
Reading of start_of_buffer failed
UarpRestoreAssetSolicitationHandler
Invalid Asset Tag
-restore
UARP Restore: %s: Firmware Asset fully transfered
UARP Restore Layer 3: Solicit Status; status <0x%04x>, reason <0x%04x>
%s (%d)
<unknown>
UARP Restore: UARP RX: Asset Processing Notification ACK; Asset ID %u
fAssetMetaDataTLV
-[UARPSoCUpdaterInstance applyStagedFirmware]
-[UARPSoCUpdaterInstance uarpRestoreLayer4Callbacks]
BuildIdentity
IOService
Failed to persist FW version: 0x%x, treating as non-fatal\n
Found matching tags %s\n
UARP Restore: Failed to tx uarp message
%s: NULL pUarpCtx
%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>
Staging FW in personalization backend\n
Begin Manifest Request\n
%s: More TSS Request for Updater(LUN:%d,RouterID:%d)
%@ Update: %u%%
BundleDataDict
Invalid Offset
Asset Not Found
Bad return value from version register read: 0x%x\n
Ace in boot mode: Can't be updated!\n
Ace in unexpected mode 0x%08x\n
Ace is in APP mode, trying to read mode again after 1000ms
UARP Restore (Asset Solicitation): %s: No Asset Metadata
%@
%s: error allocating options: No resources
BootedOS
Mismatch UUID
Invalid Message
Asset Invalid Compression
Error when forcing ATCRT update on RID%u status=0x%X\n
UARP Restore (Asset Solicitation): %s: No Payload Metadata
CoreUARP Restore IM4M: Post-Layer3: TSS Response is NULL
-[Ace3UpdaterInstance uarpRestoreInitOptions]
RestoreInternal
%s: Received Invalid tssOptions
uarpPlatformEndpointRecvMessage
UARP.LAYER2 <%s> Cannot find downstream endpoint
Unsupported Hardware Revision
UARP Restore: Tatsu Server set to %s
Sync
Found updatable Ace based on usbc-update-protocol value\n
Non-Fatal error sending tag hint(0x%x) to backend: 0x%x\n
Failed to force retimer at RID%u into DFU, status=0x%X\n
boardID=0x%llX\n
Waiting for processing notification before closing\n
%2hhx
UARP Restore: %s: fLayer3AssetSolicitationProgress is NULL
UpdaterRef
%s: Success. tssOptions:%@, tssServer:%@ 
product
Writing NVRAM variable %s to {0x%02x,0x%02x,0x%02x,0x%02x,0x%02x,0x%02x}\n
UARP Restore (Asset Solicitation): %s: fseek failed
Ticket
%@: Firmware staging failed. Status: 0x%08x (%s), Reason: 0x%08x (%s)
Unknown Accessory
Invalid UART RID 0x%x for SPI RID 0x%x\n
Offering IM4M to controller\n
CoreUARP Restore IM4M: uarpPlatformEndpointOfferAsset: %d 
BDID
CPFM=0x%llX [8b]\n
CPRV
Built and Staged the personalized FW
UARP.LAYER3.TRANSFER.PAUSE.ACK - Not Implemented
NeRD Stage1
UARPSoCUpdaterLayer4UARPPropertyUpdate
HigherVersion
Couldn't get number value\n
HPM mode=0x%X\n
USBFirmware
Finished AC\n
CoreUARPRestoreAssetRescindStatus
UARP.LAYER3.WATCHDOG.CANCEL
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetRequestMetaData failed with status: %u
UarpRestoreApplyStagedAssetsHandler
Payload Data complete
UARP Restore: %s: Provided filepath is greater than max filepath length %i
UARP Restore Layer 3: Stage Status; status <0x%04x>, reason <0x%04x>
UARP Restore: Could not open manifest file %s
Downstream Endpoint Unreachable Ack
Skipping updatable check due to bootarg
UART HPMs reset failed, status=0x%X, treating as non-fatal\n
Asset Processing Notification Ack
UARP Restore: EOF %d, Read %zu bytes
%s: ERROR adding remote endpoint, status = 0x%08x
Failed to set FIRM payload index; %u
%s Update Finished For Unit (LUN:%d,RouterID:%hhu)
Cancelled Asset Tag
ERROR: Unexpected read length for register 0x2c: 0x%llx\n
ESEC
%s: Error: Multiple payload needs personalization
UARPSoCUpdaterStagingComplete
Finished DL
PreflightContext
Unrecognized
%s[%u]
%s: Offer IM4M Asset to Updater(LUN:%d,RouterID:%d)
Priority Activity
Downstream Endpoint Reachable Ack
WARNING: Unexpected tag for offered Dynamic Asset\n
UARP Restore: Failed to offer superbinary
UARP Restore: %s: Protocol Version Selected %d, was previously %d
%s: NULL pBlock
Board ID: %@
-[UARPSoCUpdaterController offerPersonalizationDataWithDictionary:]
Unsupported Asset Tag
Upload Denied
Accessory
UARP Restore: Failed to accept superbinary; 0x%08x
Endpoint Component Discovery Request
Asset Rescinded Notification Ack
Current firmware version: %u.%u.%u.%u, new version: %u.%u.%u.%u\n
PREV
UARP Restore (Asset Solicitation): %s: fPayloadMetaDataTLV not implemented
Unknown
Persistent flash successful\n
UARP Restore: %s: Rx pRestoreAsset was NULL
v8@?0
UARPSoCUpdaterApplyComplete
NONC
Error getting active version: 0x%x\n
IOPropertyMatch
Ace is in boot mode, trying to read mode again after 1000ms
CPID=0x%llX [16b]\n
Mismatch Data Offset
Ace in mode 0x%08x, performing SFW flash\n
usbc,version,rid%d
Received some payload data\n
UARP Restore: %s: fLayer3FirmwareStageProgress is NULL
fRestoreUARPProtocolVersion
fPayloadDataComplete
%s.queue
Staged Firmware Version Greater than Asset
Failing message: 0x%02x%02x%02x%02x%02x%02x
UARP Restore: %s: uarpPlatformEndpointSolicitDynamicAsset() failed; 0x%08x
%s: Local Signing is enabled, no personalization data expected.
%@: Waiting for TSS offer to complete...
Not resetting RID %d in mode 0x%x\n
No Firmware Update Available Ack
Buffer Would Overflow
Same Version Staged
uarpTransmitEntryIsValidToSend
usbc,sn201202x,spmi
ECID
fPayloadMetaDataComplete
Same Version Active
Upload Complete
USBCUpdate: Calling Asset Fully Staged from Processing Notification\n
Flashing block %d, CRC = 0x%08x\n
Skipping firmware update due to version number check
Error allocating info\n
Duplicate Controller
Mid Upload
Reading bytes failed, nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Apple - %d )
UARP Restore: Failed to remove endpoint, status 0x%08x
Is Display & has Preflight Tickets - setting to Stage 1
Active Firmware Version Greater than Asset
USBCUpdate: Calling Asset Fully Staged from Processing Notification
UARP Restore: %s: fLayer3PersonalizedFirmware is NULL
UarpRestoreLayer3TssRequestQueueHandler
%s: Tss Response: %@
Yes
Warning: Received status 0x%x when reading mode, delaying 1000ms and trying again
UARP Restore: Read error %d, Read %zu bytes
validate_same_version: existing = %d.%d.%d.%d, new = %d.%d.%d.%d\n
CoreUARPRestoreAssetTransferProgress
fPayloadData
Payload Metadata <0x%08x>
fRestoreUARPDynamicAssetOffered
fAssetProcessingNotification2
NeRD Preflight
Asset Processing Notification
Switching to using LUN %d based on hint\n
WARNING: HPM in ADFU in Unknown Mode and force_dfu not set\n
Received the whole IM4M
Workaround: not putting any bits of the digest list into the image, due to no personalization
UARP.RESTORE.LAYER3.INFO.RESPONSE <Statistics> - Not Implemented
ChipID
ProductionMode
Error decompressing buffer for payload
WARNING: Unexpected tag for offered Dynamic Asset
@%@
fAssetProcessingNotificationAck called\n
CoreUARP Restore IM4M: Building Personalization Response
No available units to be updated
Data Transfer Paused
IONameMatch
FirmwareData
UARPSoCUpdaterLayer4ApplePropertyUpdate
Trying to find AHPMLibInterface for RID 0x%02x\n
Proceeding with update to %u.%u.%u.%u because Ace is booted from ramdisk\n
UARP Restore: Failed to offer superbinary, status 0x%08x
com.apple.AppleAccessoryManager
uarpMsgRecvDownstreamEndpointUnreachable
Corrupt SuperBinary
UARP Restore (Asset Solicitation): %s: pPayload->_fp is NULL
UARP Restore: %s: Protocol Version Not Selected; defer info queries
Needs Restart
Asset Data Transfer Notification
AAPL,phandle
Received error 0x%x from GAID, silencing\n
Ace is in APP mode, trying to read mode again after 1000ms\n
r
usbc-update-protocol
Error: Got unexpected DID 0x%x\n
OTA Preflight
Invalid Asset Type
Low Battery
libusbupdate-allow-same-version
Failed SFWi on RID %d with 'Flash Busy' error - check SPI flash seating\n
fPayloadReady
success
Success
Data Response
%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p
Found updatable Ace based on usbc-update-protocol value
Payload Data complete\n
UARP Restore: %s: UARPRestoreAsset->_fp is NULL
ace3
DestBundlePath
Error finding the spi-flash-parent\n
MetaData Overflow
Downstream Endpoint Discovery Ack
Downstream Endpoint Reachable
Error finding IOKit service: 0x%x\n
Error finding the spi-flash-parent
Cannot find start_of_needle
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetQueryNumberOfPayloads failed with status: %u
%s: More tss request for next round.
-[UARPSoCUpdaterController createUpdaterInstanceFor:helper:options:]
Invalid Data Response Length
streaming
UARP Restore: %s: fLayer3AssetSolicitationStatus is NULL
UARP.LAYER3.TRANSFER.PAUSE - Not Implemented
EPRO
Invalid EndpointID
Nothing Staged
Error allocating accessory
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetSetPayloadIndex failed with status: %u
%s: NULL pBuffer
Downstream Endpoint Message
%@: _forceLocalSigning = %d
Asset In Flight
UART HPMs not found, treating as non-fatal\n
ERROR: Unexpected second read length for register 0x2c: 0x%llx\n
Persistent flash successful
Final params, after accounting for any endianness quirks:\n
Received %d bytes of IM4M\n
%s: %@ Offering Firmware
UARP.LAYER3.OFFER.SUPERBINARY - Not Implemented
%@ Update: 100%%
Invalid Data Request Offset
Version Discovery Request
Endpoint Bulk Information Request Ack
Overriding LUN to 1 since it was 0 or unspecified
AppleHPMDeviceHALType3
Ace is in ADFU mode, trying to read mode again after 1000ms
fAssetReleased2 called\n
Cannot find start of buffer\n
UARP Restore: %s: uarpPlatformEndpointPrepareSolicitedDynamicAsset() failed; 0x%08x
UarpRestoreLayer3UarpPropertyUpdateQueueHandler
Asset Available Notification
RID%u not in restore and getting exclusive access failed, status=0%X\n
verify_only set! Should not be attempting to flash!\n
Cannot find start of buffer
CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
UARP.LAYER3.APPLY.ASSETS - Not Implemented
Payload Index %u
DeviceInfo
Better Transport
Apply Staged Assets Request
Endpoint Discovery Response
ForceLocalSigning
%s: Failed to receive tssOptions.
Error allocating accessory\n
UARP Restore: %s: fLayer3RescindStatus is NULL
UarpRestoreEndpointDataRecvQueueHandler
Asset Available Notification Ack
Dynamic Asset Solicitation
Failed to get mode for RID %d: 0x%x\n
CoreUARPRestoreQueryOutstandingInfoProperties
%s (%s)
com.apple.uarp.embedded
AppleHPM
%s: NULL tssOptions
-[UARPSoCUpdaterInstance uarpRestoreQueueName]
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
fPayloadWriteToAsset
UARP Restore (Asset Solicitation): %s: remove failed
%s: error subclass needs to override this method
Endpoint Bulk Information Response Ack
Error: Got unexpected VID 0x%x\n
%@: Maybe Offer / Stage Firmware
Error finding the atcrt service (found the iic service)
Waiting for processing notification before closing
%s: Failed to init Restore UARP.
UARP Restore: %s: pAsset->_pAsset is NULL
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestMetaData failed with status: %u
UarpRestoreRemoteEndpointAddHandler
%s: Unable to locate firmware data.
uarpMsgRecvDownstreamEndpointUnreachableAck
Failure
rid
w+
RID0 cannot get exlusive access from retimer, status=0x%X, will assume implicit permission\n
Endpoint Component Discovery Response
Error when powering on retimer on RID%u status=0x%X\n
Expected more data: actual_more_data=0x%X, length=0x%X, (current_index + bytes_to_write) = 0x%X\n
Final params, after accounting for any endianness quirks:
nibbles_in_field=0x%zX, buffer=%p, *buffer=0x%hhX, buffer_size=0x%zX, count=0x%zX, start_of_buf=%s\n
Nonce
Finished init Restore UARP Query Info
RestoreSystemPartition
ManifestPrefix
-[UARPSoCUpdaterController offerFirmwareDataWithDictionary:]
Invalid Message Length
Failed to recv message, status = 0x%x\n
Finished AC
Dynamic Asset PreProcessing Notification
UARP Restore: %s: Query %d info properties and %d Apple properties
- MetaData length is %u
UarpRestoreLayer3FirmwareApplyStatusQueueHandler
Options Passed: %@
Staged Firmware Version Equal to Asset
protocolcontroller
CRPV=0x%llX [16b]\n
UARP Restore: %s: fLayer3ApplyStatus is NULL
RID
- Version is %u.%u.%u.%u
IM4M-CoreUARPRestore-%d-%02d-%02d-%02d-%02d-%02d.uarp
Limited
Error when reading usbc-update-protocol: 0x%x\n
UARP Restore: %s: Asset fully transfered; %c%c%c%c
UARP.RESTORE.LAYER3.INFO.RESPONSE <Last Error> - Not Implemented
%s: Applying Staged Assets
Personalization Failure
Asset Data Transfer Notification Ack
libusbcupdate-prevent-downgrades
Bad task result from %c%c%c%c 4CC: 0x%x\n
uarp
%s: Skipping Offer Firmware. Updater(LUN:%d,RouterID:%d) has finished.
Cannot find address\n
spi-flash-parent
usbc,sn201202x,iic
WARNING: SFWi failed status=0x%X, task_result=0x%X\n
Cannot find start_of_needle\n
UARP.RESTORE.LAYER3.WATCHDOG.EXPIRE
fAssetGetBytesAtOffset2
%@%d
Unknown Message Type
Unknown Information Option
UART HPM RID%d in VOUT, GAID skipped and APP mode check will be skipped\n
Begin Manifest Request
Unexpected length of field %s in USB string: 0x%lx bytes\n
UarpRestoreStageFirmwareDataBufferQueueHandler
%@: Don't Offer / Stage Firmware
%@: Really Offer / Stage Firmware
%@: staging complete signaling waiting callbacks
MetaData Type Not Found
Downstream Endpoint Unreachable
Address not number type\n
libUSBCUpdate: Fully torn down
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Info - %d )
ResponseTags
%s
%s\n
UARPSoCUpdaterInstance
UARPSoCUpdaterController
Ace3UpdateController
Ace3UpdaterInstance
KeyPrefixSearch
SoCUpdaterHelper
stringWithUTF8String:
ticketName
offerFirmwareData:
log
_applyAssetUARPSemaphore
_prefixNeedsLogicalUnitNumber
_stagingResult
_updaters
applyAssetComplete
T@\"NSString\",R,V_restorePartition
setLog:
skipSameVersion
_initUARPSemaphore
_tssRequestServerURL
addObject:
ticketNameTags
_ticketLongName
TI,V_logicUnitNumber
arrayWithArray:
T@\"SoCUpdaterHelper\",&,V_log
_endpoint
firmwareTags
manifestPrefix
restorePartition
TI,V_applyFlags
_log
stagingCompleteWithStatus:reason:
stringWithString:
updaterMode
_applyFlags
log:
routerID
objectAtIndexedSubscript:
offerPersonalizationDataWithDictionary:
receievePersonalizationRequestByOfferFirmwareData:
setRouterID:
verboseLog:
_logicUnitNumberFromDevice
_pAssetContext
addEntriesFromDictionary:
applyStagedFirmware
Ti,V_updaterMode
personalizationRequests
_routerID
queryInfo
uarpRestoreLayer4Callbacks
isEqual:
firmwareTagName
TI,V_stagingStatusReason
useLocalSigning
TB,R,V_isDone
_assetTransferUARPSemaphore
_name
initWithOptions:logFunction:logContext:
_lastPercentComplete
_stagingStatusReason
_updaterMode
count
countByEnumeratingWithState:objects:count:
uarpRestoreQueueName
_restorePartition
hasPrefix:
TB,R
_isDone
TC,V_routerID
initUARPRestoreQueryInfo
UTF8String
_personalizationRequests
_verbose
applyFlags
boolValue
initWithHelper:options:
setStagingStatusReason:
skipApplyStage
isDone
_forceLocalSigning
length
_logContext
createUpdaterInstanceFor:helper:options:
initUARPWithFirmware:
printUpdaterMode
updaterLog:
T@\"NSString\",R
initUARP
keyWithPrefix:
setStagingStatus:
.cxx_destruct
copy
numberOfAvailableUnits
T@\"NSDictionary\",R
personalizationRequestDict
_tssRequest
dictionaryWithDictionary:
isEqualToString:
setApplyFlags:
updateStagingProgressWithBytesSent:bytesTotal:
_nextUpdateProgressReportPercentThreshold
namePrefix
_queue
_stagingStatus
appendString:
logInternal:arguments:
TB,R,V_skipSameVersion
numberWithBool:
_requiresPersonalization
initWithRouterID:helper:options:
tssRequestWithOptions:serverURL:assetCtx:siliconCtx:
objectForKeyedSubscript:
offerFirmwareForUpdater:inputDict:
offerPersonalizationResponse:
_logFunction
_logicUnitNumber
init
initWithFormat:arguments:
initWithLogicUnitNumber:helper:options:
_manifestPrefixName
bytes
stagingStatusReason
unsignedIntValue
_uarpContext
assetTransferUARPComplete
name
setLogicUnitNumber:
stagingStatus
uarpRestoreInitOptions
_skipSameVersion
dictionaryWithObjects:forKeys:count:
initUARPComplete
stringWithFormat:
logicUnitNumber
updateAppleProperty:siliconCtx:
setUpdaterMode:
TI,V_stagingStatus
_suffixNeedsLogicalUnitNumber
initializeUpdatersWithOptions:
offerFirmwareDataWithDictionary:
v32@0:8@16*24
@\"NSMutableArray\"
^v
v20@0:8C16
@\"NSObject<OS_dispatch_queue>\"
@\"NSObject<OS_dispatch_semaphore>\"
I
B32@0:8@16@24
@40@0:8@16^?24^v32
@32@0:8@16@24
@16@0:8
B16@0:8
@36@0:8C16@20@28
^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^
C
@36@0:8I16@20@28
I16@0:8
@24@0:8@16
v24@0:8@16
v28@0:8I16^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}20
v24@0:8I16I20
C16@0:8
v20@0:8i16
B
i
@\"SoCUpdaterHelper\"
^v16@0:8
r*16@0:8
v16@0:8
v48@0:8@16@24^v32^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}40
@\"NSDictionary\"
^{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8
^?
B24@0:8@16
v20@0:8I16
i16@0:8
@\"NSString\"
```
