# `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 977,328 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3760)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (126 classes, 8 protocols)

Classes: `ACE`, `ACETaskCommand`, `ACETaskCommandDFUf`, `ACETaskCommandVOUT`, `ATCRTAPHardwareID`, `ATCRTBloodhoundPacketDumper`, `ATCRTCommand`, `ATCRTCommandGAID`, `ATCRTCommandSFWd`, `ATCRTCommandSFWf`, `ATCRTCommandSFWi`, `ATCRTCommandSFWs`, `ATCRTResponse`, `ATCRTResponseSFWd`, `ATCRTResponseSFWf`, `ATCRTResponseSFWi`, `ATCRTResponseSFWs`, `AppleTypeCPacketDumper`, `AppleTypeCRetimerBoardIDFile`, `AppleTypeCRetimerDFU`, `AppleTypeCRetimerDFUChecker`, `AppleTypeCRetimerFifoDumper`, `AppleTypeCRetimerFifoQueue`, `AppleTypeCRetimerHPM`, `AppleTypeCRetimerHardwareID`, `AppleTypeCRetimerIIC`, `AppleTypeCRetimerIICBase`, `AppleTypeCRetimerIICDeviceHandle`, `AppleTypeCRetimerIICFifo`, `AppleTypeCRetimerPanicStatus`, `AppleTypeCRetimerUARPHardwareIDQuerier`, `AppleTypeCRetimerUARPUpdaterController`, `AppleTypeCRetimerUARPUpdaterInstance`, `AppleTypeCRetimerUpdateController`, `AppleTypeCRetimerUpdaterHelper`, `AppleTypeCRetimerUpdaterIIC`, `AppleTypeCRetimerUpdaterInstance`, `B2PAutoHealGetCommand`, `B2PAutoHealGetResponse`, `B2PBudVersionGetCommand`, `B2PBudVersionGetResponse`, `B2PCommand`, `B2PDFUBootCommand`, `B2PDFUValidateCommand`, `B2PDataSessionConnectCommand`, `B2PDataSessionConnectResponse`, `B2PDataSessionDataCommand`, `B2PDataSessionDataResponse`, `B2PDataSessionDiscoveryCommand`, `B2PDataSessionDiscoveryEntry`, `B2PDataSessionDiscoveryResponse`, `B2PEngine`, `B2PFirmwareVersionGetCommand`, `B2PIdentificationCommand`, `B2PIdentificationResponse`, `B2PPingCommand`, `B2PPingResponse`, `B2PProductCategoryGetCommand`, `B2PProductCategoryGetResponse`, `B2PResponse`, `B2PSerialNumberGetResponse`, `B2PTimer`, `FTABFile`, `FTABSubfile`, `HPMForceRetimerDFUModeSetter`, `IECSInterface_GoldRestore2`, `NSArray`, `NSData`, `NSFileHandle`, `NSMutableData`, `NSMutableString`, `NSString`, `ThunderboltInterface`, `ThunderboltPacketDumper`, `UARPAssetTag`, `UARPAssetVersion`, `UARPMetaDataTLV`, `UARPMetaDataTLV16`, `UARPMetaDataTLV32`, `UARPMetaDataTLV64`, `UARPMetaDataTLV8`, `UARPMetaDataTLVData`, `UARPMetaDataTLVString`, `UARPPayloadPersonalizationInfo`, `UARPSuperBinary`, `UARPSuperBinaryPayload`, `UARPTLVHostPersonalizationRequired`, `UARPTLVMeasuredPayload`, `UARPTLVPayloadCompressionAlgorithm`, `UARPTLVPersonalizationBoardID`, `UARPTLVPersonalizationChipEpoch`, `UARPTLVPersonalizationChipID`, `UARPTLVPersonalizationChipRevision`, `UARPTLVPersonalizationECID`, `UARPTLVPersonalizationECIDData`, `UARPTLVPersonalizationEnableMixMatch`, `UARPTLVPersonalizationFTABPayload`, `UARPTLVPersonalizationFTABSubfileDigest`, `UARPTLVPersonalizationFTABSubfileDigestFilename`, `UARPTLVPersonalizationFTABSubfileEPRO`, `UARPTLVPersonalizationFTABSubfileESEC`, `UARPTLVPersonalizationFTABSubfileHashAlgorithm`, `UARPTLVPersonalizationFTABSubfileLongname`, `UARPTLVPersonalizationFTABSubfileTag`, `UARPTLVPersonalizationFTABSubfileTrusted`, `UARPTLVPersonalizationLife`, `UARPTLVPersonalizationLogicalUnitNumber`, `UARPTLVPersonalizationManifestEpoch`, `UARPTLVPersonalizationManifestPrefix`, `UARPTLVPersonalizationManifestSuffix`, `UARPTLVPersonalizationNonce`, `UARPTLVPersonalizationNonceHash`, `UARPTLVPersonalizationPayloadTag`, `UARPTLVPersonalizationPrefixNeedsLogicalUnitNumber`, `UARPTLVPersonalizationProductionMode`, `UARPTLVPersonalizationProvisioning`, `UARPTLVPersonalizationRequired`, `UARPTLVPersonalizationSecurityDomain`, `UARPTLVPersonalizationSecurityMode`, `UARPTLVPersonalizationSoCLiveNonce`, `UARPTLVPersonalizationSuffixNeedsLogicalUnitNumber`, `UARPTLVPersonalizationSuperBinaryAssetID`, `UARPTLVPersonalizationSuperBinaryPayloadIndex`, `UARPTLVPersonalizationTicketNeedsLogicalUnitNumber`, `UARPTLVPersonalizedManifest`, `UARPTLVRequiredPersonalizationOption`

Protocols: `AppleTypeCRetimerDFUDelegate`, `AppleTypeCRetimerDeviceHandle`, `AppleTypeCRetimerIICDelegate`, `AppleTypeCRetimerIICFifoDelegate`, `AppleTypeCRetimerUARPUpdaterInstanceDelegate`, `NSCoding`, `NSCopying`, `NSSecureCoding`

## Strings (2,860)

First 2,500 of 2,860.
```
@\"<UARPSuperBinaryDelegate>\"
^{IONotificationPort=}
@\"NSURL\"
@24@0:8C16C20
@\"<AppleTypeCRetimerIICFifoDelegate>\"
B20@0:8I16
B40@0:8Q16I24I28I32I36
B48@0:8Q16I24I28I32I36^I40
B24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16
@\"NSString\"16@0:8
B60@0:8@16@24@32B40Q44@52
@24@0:8@\"NSCoder\"16
@24@0:8@16
q
B24@0:8^B16
@\"AppleTypeCRetimerIIC\"
i48@0:8C16^v20Q28I36^Q40
@40@0:8@16^?24^v32
c16@0:8
c
B24@0:8I16I20
@\"NSString\"
B32@0:8Q16@24
@28@0:8I16I20B24
@\"ATCRTBloodhoundPacketDumper\"
v32@0:8@\"AppleTypeCRetimerIICFifo\"16@\"NSData\"24
@44@0:8@16^?24^v32B40
v32@0:8I16I20r*24
@32@0:8Q16Q24
v44@0:8@16I24^v28Q36
[65536C]
@40@0:8I16i20@24@?32
@\"AppleTypeCPacketDumper\"
@\"NSFileHandle\"
q24@0:8@16
B32@0:8I16*20I28
v28@0:8I16I20C24
i16@0:8
i
v36@0:8@16Q24B32
@\"<B2PEngineDelegate>\"
v32@0:8@\"AppleTypeCRetimerIICFifo\"16@\"NSError\"24
i64@0:8I16^v20Q28^v36Q44I52Q56
@\"NSDictionary\"
B20@0:8C16
v20@0:8i16
S
@20@0:8I16
v32@0:8S16i20@24
@32@0:8c16c20c24c28
r*32@0:8@16@24
Q16@0:8
@24@0:8I16C20
B44@0:8Q16I24I28I32^I36
^^{IOCFPlugInInterfaceStruct}
B24@0:8^{UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}16
{?=\"cb\"[208C]\"dbg_stats\"{?=\"response_timeouts\"I\"midpacket_timeouts\"I\"tx_packet_retry_cnt\"I\"max_tx_level\"I\"rx_packet_cnt\"I\"rx_packet_err_cnt\"I\"tx_packet_cnt\"I}\"client_context\"^v}
@32@0:8I16C20^?24
@28@0:8S16C20i24
v20@0:8B16
@\"NSObject<OS_dispatch_semaphore>\"
C
@24@0:8B16B20
@48@0:8@16@24@32Q40
v24@0:8^{uarpChipCallbacks=^?^?}16
@40@0:8C16i20C24i28@32
@24@0:8^{_NSZone=}16
I
@24@0:8C16i20
B24@0:8I16C20
v28@0:8S16I20I24
B24@0:8C16B20
@36@0:8@16r^v24I32
v24@0:8@\"NSCoder\"16
v28@0:8B16r*20
v20@0:8I16
B36@0:8@16B24^@28
v24@0:8I16I20
@28@0:8I16C20I24
i20@0:8B16
i28@0:8I16I20I24
@\"<AppleTypeCRetimerUARPUpdaterInstanceDelegate>\"
@\"AppleTypeCRetimerPanicStatus\"
@24@0:8^{ATCRTTaskSFWdOutput=I}16
C28@0:8r*16I24
@\"<AppleTypeCRetimerIICDelegate>\"
@\"NSMutableData\"
@48@0:8Q16Q24Q32Q40
@32@0:8@16@24
^^{AppleHPMLibInterfaceStructV3}
@28@0:8I16@20
^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}
B20@0:8B16
B48@0:8@16@24@32Q40
@40@0:8Q16S24C28C32I36
q16@0:8
@\"AppleTypeCRetimerUpdaterIIC\"
B28@0:8I16^I20
@\"B2PIdentificationResponse\"
@\"NSData\"
@\"ThunderboltPacketDumper\"
@\"AppleTypeCRetimerFifoDumper\"
@\"FTABSubfile\"
v24@0:8I16S20
@\"AppleTypeCRetimerHardwareID\"
@\"AppleTypeCRetimerDFU\"
@24@0:8I16B20
@24@0:8B16I20
B16@0:8
B48@0:8S16^I20^I28I36^I40
v36@0:8r*16I24^I28
v32@0:8C16I20@24
v24@0:8@\"NSString\"16
@28@0:8I16Q20
@\"UARPAssetVersion\"
@\"NSNumber\"
^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHe
v28@0:8S16@20
@\"AppleTypeCRetimerIICFifo\"
v20@0:8S16
I28@0:8r*16I24
@32@0:8C16i20@24
@24@0:8Q16
@\"FTABFile\"
@24@0:8^{ATCRTTaskSFWfOutput=I}16
@\"NSArray\"
@\"<AppleTypeCRetimerUpdaterIICDelegate>\"
i40@0:8C16^v20Q28I36
B28@0:8r*16I24
@\"B2PEngine\"
i32@0:8C16r^v20I28
@\"NSData\"40@0:8@\"FTABFile\"16@\"AppleTypeCRetimerHardwareID\"24@\"NSDictionary\"32
^?
B32@0:8@16o^@24
@\"<AppleTypeCRetimerUpdaterInstanceDelegate>\"
@\"<AppleTypeCRetimerDFUDelegate>\"
@32@0:8@16Q24
@\"NSObject<OS_os_log>\"16@0:8
@32@0:8Q16^v24
v24@0:8q16
v32@0:8@16r*24
B52@0:8@16@24@32B40Q44
@\"NSMutableString\"
@\"AppleTypeCRetimerHPM\"
S16@0:8
i32@0:8C16^v20I28
@\"NSMutableDictionary\"
@\"UARPAssetTag\"
I24@0:8@16
@28@0:8C16@20
@48@0:8@16^?24^v32@40
@60@0:8S16S20C24C28C32C36Q40@48C56
@32@0:8@16#24
B28@0:8@16S24
@36@0:8Q16@24B32
@?
@32@0:8S16C20@24
@\"IECSInterface_GoldRestore2\"
@28@0:8^I16I24
v24@0:8Q16
@24@0:8I16S20
@24@0:8I16I20
@\"NSObject<OS_os_log>\"
@\"NSObject<OS_dispatch_queue>\"
@\"NSObject<OS_dispatch_source>\"
@40@0:8@16@24@32
v32@0:8@16*24
i24@0:8@16
v28@0:8S16I20S24
B24@0:8I16S20
Q
^v16@0:8
@28@0:8S16@20
v24@0:8i16I20
@\"NSLock\"
@\"<AppleTypeCRetimerDeviceHandle>\"
@32@0:8C16@20B28
@40@0:8C16Q20I28I32I36
B32@0:8r*16I24C28
C16@0:8
v20@0:8C16
^v
@\"ACE\"
@\"ATCRTAPHardwareID\"
r*
@\"B2PResponse\"
v32@0:8@16@24
r*16@0:8
@\"AppleTypeCRetimerIICDeviceHandle\"
@32@0:8I16I20^v24
B32@0:8r^v16Q24
B40@0:8r^v16Q24@32
v36@0:8I16^?20r*28
I16@0:8
B28@0:8^I16S24
B24@0:8@16
v16@0:8
^^{IOThunderboltLibInterfaceStruct}
@28@0:8Q16B24
v24@0:8^v16
@28@0:8@16B24
@16@0:8
I20@0:8I16
v24@0:8@16
@20@0:8C16
[262144C]
B32@0:8@16@24
{uarpChipCallbacks=\"fRestoreMsgRecv\"^?\"fRestoreDataRecv\"^?}
@\"NSTimer\"
B
@\"ThunderboltInterface\"
@\"AppleTypeCRetimerFifoQueue\"
@48@0:8@16@24@32@40
@24@0:8^@16
B32@0:8^B16@24
@20@0:8S16
@36@0:8S16C20i24@28
B32@0:8@16S24C28
B24@0:8^I16
B28@0:8@16B24
@\"NSMutableArray\"
%s: Update failed for %@
\tSecurity Domain: %u\n
%@: Waiting for UARP stage to complete...
com.apple.%@.uarp
com.apple.AppleAccessoryManager
AutoAppliesStagedFirmware
FirmwareBundle
Downstream Endpoint Unreachable Ack
BoardId
b2pEngine
\tActive Version: %@\n
performNextStage
FirmwareVersionBuild
atcrtu
TagNumber
Failed to add RRKO data to FTAB
%@: Continuing after UARP apply has completed.
<%@: %u>
com.apple.notifyd.matching
Vendor Version String File
Version BVER File
BuildIdentity
@Timer%u,Ticket
%s: Failed to start UARP update for %@ (%s)
%@: Firmware apply failed. Status: 0x%08x (%s), Flags 0x%08x (%s)
Unknown
logs
Property List Payload
Unknown Controller
com.apple.uarphidd
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetRequestMetaData failed with status: %u
AirPods case FWUP iAUP server session
Invalid Message Length
Unsupported Asset Tag
...Unable to find parent for IECS service.  err = 0x%X
Unsuccessful
com.apple.uarp.layer3.restore
CertificateProductionStatus
Log Friendly Name
AlternativeAppleModelNumbers
Needs Restart
Dynamic Asset PreProcessing Notification
Endpoint Discovery Request
%s: NULL pIM4M
-[AppleTypeCRetimerIICFifo drainTransmitQueue]
Host Personalization not required for payload %@
v16@?0@\"B2PTimer\"8
/usr/standalone/firmware/accessoryupdater/UARP
Unknown Asset
-[AppleTypeCRetimerUpdaterInstance performUpdateIIC]
Unrecognized error 0x%x
-[HPMForceRetimerDFUModeSetter getACIOParentData]
RestoreSystemPartition
\tBlock Count: %u\n
%@: Firmware staging failed. Status: 0x%08x (%s), Reason: 0x%08x (%s)
Unexpected type for retimer debug flags: %@
lpda
Verify Fail
Personalization Ticket Needs Logical Unit Number
Forcing power on for router ID %u
aopf
Asset In Flight
UARP Restore: Failed to allocate restore asset
UARP.LAYER3.OFFER.SUPERBINARY - Not Implemented
LZ4
CrashLogKey
cmapdatabase
Boot
<%@: 0x%08x>
UARP Restore: %s: Firmware Asset fully transfered
tethered
BigEndian
retimerDFU
UARP Restore: %s: UARPRestoreAsset->_fp is NULL
UARP.LAYER3.TRANSFER.PAUSE.ACK - Not Implemented
request
fRestoreUARPDynamicAssetOffered
bver
SupportsVoiceAssist
Staged Firmware Version Greater than Asset
Host Controller
LocalSigningID
close
Endian
DecodedCrashLogChildKey
%s: IIC Communication Error: Failed to query %@ panic status.\n%@
ATCRT %u: %@
crashlog
UARP Restore: %s: uarpPlatformEndpointPrepareSolicitedDynamicAsset() failed; 0x%08x
SOP
SupportsMappedAnalytics
UARP.LAYER3.TRANSFER.PAUSE - Not Implemented
crsh
Invalid TLV
Out Of Order Message ID
-[ACE executeIECSCommand:withData:dataLength:]
Timeout
SocLiveNonce
BundleDataDict
queryTags
UpdaterRef
Unrecognized
UARP Restore: UARP RX: Asset Available Notification; Asset ID %u
%02x
Bytes Written: %u
v8@?0
ChipRev
%@: Continuing after UARP staging has completed.
UARP.RESTORE.LAYER3.WATCHDOG.EXPIRE
core
log_version
FW open file failed
ACE
No
Warning: Unable to locate ticket name: %@
/var/db/accessoryupdater/uarp/
application-info
%s: NULL pBuffer
\tCategory: %s\n
User Client Access Error
%s: NULL tssOptions
SHA-384
UARP Restore: Offered Firmware with outstanding offer
las_tunableh_fig_get_value
\t\tSecurity Domain: %u\n
fAssetGetBytesAtOffset2
hpm
driver 00
SHA-512
Payload Missing
SOP Prime
ProductNumber
status
\tSubfiles:\n
DFU complete for %@
BVER
Unknown Personalization Option
Unknown Information Option
MetaData Overflow
uarpPlatformEndpointStreamingRecvBytes() failed; 0x%08x
UARP.LAYER3.TRANSFER.RESUME.ACK - Not Implemented
Voice Assist Role
Failed to parse FTAB file
UarpRestoreEndpointMsgRecvQueueHandler
AAPL,phandle
-[ThunderboltInterface configReadForRoute:port:space:index:result:]
Failed to query AP hardware information
phyb
%lu.%lu.%lu.%lu
false
ForceLocalSigning
NeRD Preflight
power
acio-parent
Payload Signature (Development)
MagSafe Cable
las_tunableh_device_has_chip_number(self)
\tProtocol Mode: %s
digestListSize
Voice Assist Signature
B2PHID
-[ACE retimerForcePower]
ApBoardID
Timer%u,Ticket
LeapBinsDigestsArray
-[AppleTypeCRetimerUpdaterInstance printVersions]
BoardID
hidPersonalizationNeeded
CoreUARPRestoreQueryOutstandingInfoProperties
Serial
Unsupported
Buffer Overflow
Timer,RTKitOS,%u
%@: Firmware apply complete
\tPort Number: %u\n
Personalization FTAB Payload Longname
Personalization Manifest Suffix
\tActive File: %u\n
/System/Library/PrivateFrameworks/CoreUARP.framework
fAssetProcessingNotification2
CoreUARPRestoreAssetTransferStatus
USB-C to Lightning
UnsignedInteger
False
UARP Restore: Failed to process rx uarp message
com.apple.%@.updater
diags
VendorName
-[FTABFile parseFileData]
\t\t%@
USB-C_%s
\t\tNonce: %@\n
%s: Falling back to DFU mode for %@.
unknown
Downstream Endpoint Reachable
Invalid Host
Invalid Data Transfer Notification
rrko
RTP
Personalization Matching Data Product Revision Maximum
Upload Denied
UARP Restore (Asset Solicitation): %s: %u bytes written
FusingOverrideUnfused
TtrSolicitLogs
com.apple.MobileAsset.UARP
Asset Data Paused
Mismatch Personalization Option
Digest
%@: New firmware version %@ (%@)
Running DFU check for deferred router IDs.
AirPodsPublicSeed
Asset Transfer Complete
%s: IIC hardware ID query failed for %@ (%@).
\t\tECID: 0x%016llx\n
Personalization Payload Tag
\tPending Version: %@\n
UARP Restore (Asset Solicitation): %s: uarpAssetQueryPayloadInfo failed with status: %u
Minimum iOS Version
<%@: %s (%u ms)>
deploymentLimit
-[AppleTypeCRetimerIICFifo getAvailableReceiveDataLength]
Personalized Manifest
UARP Restore: %s: Query %d info properties and %d Apple properties
Invalid Data Request Length
streaming
UARP Restore (Asset Solicitation): %s: No Asset Metadata
\tSecurity Epoch: %u\n
\n
Version match: Failed to query chip Bver for %@
Warning: Unable to locate manifest for '%@'
        <%@>\r
UARP Restore: UARP RX: Buffer = %p, Payload Length = %u, Type = 0x%04x, Total Length = %u, ID = %u
enable
host_release_assert
UARP Restore (Asset Solicitation): %s: fAssetProcessingNotification2 not implemented
-[AppleTypeCRetimerDFU sendDataSessionConnectCommandForSessionID:state:]
-[AppleTypeCRetimerIICFifo pollForReceiveData]
%@%d
%s: Failed to start firmware apply for %@ (%s)
Invalid Payload Header
q24@?0@8@16
Options
\tFlavor: %u
    >
\tPending File: %u\n
Compose MetaData Hash Algorithm
/AppleInternal/usr/local/misc
UarpRestoreStageFirmwareFilenameQueueHandler
Timer,RestoreRTKitOS,%u
Payload 4CC
las_tunableh_write
Failed to force power on for %@ during Updater instance initialization
tatsuSigningServer
char4
%s: NULL pBlock
Bluetooth
HDS
DeferredCommit
fPayloadMetaDataComplete
uatcrt
%s: Unable to query hardware ID in DFU mode for %@.
char3
Using local signing: %s
com.apple.system.powermanagement.poweradapter
FieldName
com.apple.%@.uarp.hw_id
SFWi was not run
\t\tSecurity Epoch: %u\n
Host Minimum Battery Level
PersonalizationNotification
Asset Processing Notification Ack
Asset Rescinded Notification Ack
I/O Error
las_tunableh_apply
enabled
-[AppleTypeCRetimerIICFifo updateTransmitFifoSpace]
CoreUARP Restore IM4M: uarpPlatformEndpointOfferAsset: %d 
Required Personalization Option
Personalization Payload Hash Algorithm
<unknown>
Failed to locate RRKO payload in super binary
BootedOS
com.apple.uarppersonalization
analytics_test_mode
Invalid
DigestListSize
USB
atcrt
MetaData Format Version
USB-C_FW
char2
SecurityEpoch
UARP Restore: %s: fLayer3RescindStatus is NULL
/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/Current/Resources
Missing Remote
1
\tState: %u (%s)
disabled
Version Discovery Response
DestBundlePath
GR2
UARP Restore: UARP RX: Asset Processing Notification; Asset ID %u
CoreUARPRestoreAssetTransferProgress
UARP Restore: %s: fLayer3AssetSolicitationProgress is NULL
Minimum tvOS Version
SupportsFriendlyName
MobileAssetsModelNumber
SecurityMode
Personalization Nonce Hash
taptoradar
_dev
Invalid Message
Buffer Would Overflow
Did NOT build matching dict(index:%d)
ACE2 No FET
ProductionStatus
Personalization Security Mode
rkof
b2p
Asset Processing Notification
FW upgrade was not in IDLE state
\tSecurity Mode: %u\n
Yes
Personalization Manifest Prefix
Ignore Version
UpdateRequiresPowerAssertion
UTF8String
com.apple.accessoryupdater.hpm
generic error
manifest
Personalization Payload Longname
Asset Id Unknown
Downstream Endpoint Discovery
Endpoint Bulk Information Response Ack
\tHardware ID:\n
Device Specific Data
Voice Assist Hash
Information Response
las_tunableh_read
CoreUARP Restore IM4M: Building Personalization Response
fAssetSetBytesAtOffset2
Value
\tSerial Number: %@\n
MetaData Type Not Found
Duplicate Controller
Staged Firmware Version Equal to Asset
Failed to set FIRM payload index; %u
Timer,SecurityDomain,%u
ATCRT_REG_PANIC_STATUS
UARP Restore (Asset Solicitation): %s: remove failed
UI_country_code
Asset Decompression Failure
Personalization Failure
Unable to locate super binary.
midpacket
ModelName
FirmwareVersionMajor
-[AppleTypeCRetimerUpdaterInstance initWithRouterID:delegate:forcePower:]
thunderbolt-drom
EPRO
RestoreInternal
%@: Waiting for UARP apply to complete...
com.apple.uarppersonalization.btleserver
rtpf
SoftwareBinaryDsp1
%@:\n\tOp Code: 0x%04x\n\tRoute: %s\n\tStatus: %s
fPayloadReady
Personalization Payload Digest
Compressed Headers Payload Index
%@\n
DebugFlags
%s.%u.payload
Asset Available Notification
com.apple.uarp.daemon
Payload Signature
BTLEServer
-[AppleTypeCRetimerDFU sendIdentificationCommand]
Personalization Payload Effective Production Mode
Downstream Endpoint Reachable Ack
las_tunableh_get_fig() == NULL
\t\tBoard ID: 0x%04x\n
CoreUARPRestoreAssetRescindStatus
Failed to locate Bver.
idle
InputDictionary
Unsupported Message Type
%s: NULL pIM4M->payloads
las_tunableh_device_get_chip_number
No Firmware Update Available
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (after to IOCreatePlugInInterfaceForService or at exit)
Timer,ECID,%u
start
response timeout
BuildManifest.plist
\tValue: 0x%02x
Flash Partition Boot
com.apple.uarp.embedded
...Unable to create CFPlugInInterface. err = 0x%X
Waiting for ACEs with routerIDs: %@. Available ACEs: %@.
Plaform specific
FTAB:\n
%s (%s)
Payload Metadata <0x%08x>
\t\tChip Revision: %u\n
Failed to parse super binary.
-[AppleTypeCRetimerUARPUpdaterInstance applyFirmware]
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Apple - %d )
Subfile: type=%@, length=%u
ProductID
FirmwareData
Failed to query hardware ID for router ID %u
Log Apple Model Number
SuperBinary Format Version
Invalid Data Request Offset
\tFirmware Version: %02X%01X.%01X%02X.%02X\n
Demote
TicketName
APInfo
%@: Firmware staging complete.
IM4M
fuse locked
Personalization FTAB Payload Security Mode Host Override
com.apple.uarppersonalizationd
Upload Complete
UarpRestoreLayer3FirmwareApplyStatusQueueHandler
%s: Device panicked %@
SecurityDomain
com.apple.uarp.internal.personalization
no
fAssetReady
Analytics Event Name
decoderId
@%@
-[HPMForceRetimerDFUModeSetter lookupThunderboltController]
rt13-failure-panic
UARP Restore (Asset Solicitation): %s: Asset fully staged
fRestoreUARPProtocolVersion
rampPeriod
Sync
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestMetaData failed with status: %u
UARP.LAYER3.TRANSFER.RESUME - Not Implemented
\tData: %@\n
effectiveSecurityMode
MetaData Values
Version Mismatch
RRKO
stop
True
Failed to locate firmware super binary payload when updating super binary
com.apple.uarp.UARPUpdaterServiceHID.personalizationNeeded
supplementalassets
UID_MODE
uuid
\t\tTag: %@\n
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
-[AppleTypeCRetimerDFU b2pDataSessionOpenForSessionID:]
All ACEs are now available.
product
Information Request
SupportedAccessoriesUARP-Internal.plist
Did NOT find service(s) matching AppleHPMDevice(index:%d)
Timer,Nonce,%u
UARP Restore (Asset Solicitation): %s: fAssetMetaDataTLV not implemented
UARP Restore Layer 3: Solicit Status; status <0x%04x>, reason <0x%04x>
\tProduction Status: %u\n
-[AppleTypeCRetimerUARPUpdaterInstance initWithRouterID:delegate:forcePower:]
ATCRT %u: info = %@
DFU image
buildVersion
Unknown Downstream Endpoint
Nothing Staged
-[AppleTypeCRetimerDFU dfuBoot]
-[HPMForceRetimerDFUModeSetter propertyChanged]
DFU manifest
Host Trigger Battery Level
EventFields
UARP Restore: %s: uarpPlatformEndpointSolicitDynamicAsset() failed; 0x%08x
In Use
Cancelled Asset Tag
CoreUARP Restore IM4M: Post-Layer3: TSS Response is NULL
SkipSameVersion
Personalization Provisioning
Payload Digest
AirPodsDeveloperSeed
Device Error
com.apple.%@.hw_id_fifo_delegate
RT13 B2P Queue
Personalization Suffix Needs Logical Unit Number
MCU
HeySiri Model Signature
Dynamic Payload
countryList
Performing DFU for %@
Bad Command
\tEnable: %s\n
RestoreRTKitOS
Invalid Data Response
Not Found
-[ThunderboltInterface configWriteForRoute:port:space:index:value:]
%@: Update: %u%%
Router ID %u not ready for DFU check after IIC check failed.
Invalid Object
Asset No Bytes Remaining
%s: Starting update for %@
%s: IIC hardware ID query failed for %@.
ace
Wait %u seconds for retimer(s) to reboot.
com.apple.uarp.personalization-needed.dispatchqueue
Minimum Battery Level
No Compressed Headers
Voice Assist Digest
Version File
DFUMode
Unknown Data Transfer State
dev
%@: FIFO transfer error (%@)
\t%s: %s\n
Asset Invalid Compression
Invalid Update
\tProtocol Version: %s\n
com.apple.%@.fifo_delegate
Failed to create updater instance for router ID %@
app
ready
https://basejumper.apple.com/livability/
Unknown Failure
Better Transport
Timer,BoardID,%u
fAssetStore
sbd1
FTAB %@:\n
assert
\tRID: %@\n
App
-[AppleTypeCRetimerDFU receivedCommand:]
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetQueryNumberOfPayloads failed with status: %u
payloadDigest
Payload Compression ChunkSize
DeploymentList
EventName
ATCRT Command: %@
Write Data
\x81
AppleARMIODevice
Low Battery
UARP Restore: Failed to remove endpoint, status 0x%08x
Failed to locate RRKO data
UARP Restore (Asset Solicitation): %s: fPayloadMetaDataTLV not implemented
\tChip Rev: %u
SupportedAccessoriesUARP-InternalFuture.plist
Did NOT build matching dict
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (prior to IOCreatePlugInInterfaceForService)
Tethered
-[AppleTypeCRetimerDFUChecker doCheck]
payloadLongname
\tInfo ID: %s
Payload - 4cc <%@> - Version <%@> - TLVs - %@
OTA Stage 1
Flash Section Length
chip_metadata
\tAP Chip Rev: %u
BT
SupportedAccessoriesUARP.plist
Provisioning
fAssetMetaDataTLV
start ex
Compressed Headers
Payload MetaData
Invalid Function Pointer
Data Transfer Paused
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
Failed to parse updated super binary
Personalization Required
Personalization FTAB Payload Production Mode Host Override
Mismatch Data Offset
Active Firmware Version Greater than Asset
Unable to query chip Bver for %@
\tType: %s\n
\tFlavor Field: %u
%@: UARP hardware ID check succeeded.
com.apple.corespeech.voicetriggerassetchange
parsing
void triggerSystemPanic(NSString * _Nonnull __strong)
Dynamic Asset Solicitation
usbc-fw-personality
UploaderRetryLimit
FirmwareImageFile
HeySiri Model Type
Personalization Board ID (64 bits)
SupportsAccMode7
Success
...Unable to create Device Interface. err = 0x%X
UARP Restore: Could not open manifest file %s
IOPCIDevice
UARP Restore: Failed to accept superbinary; 0x%08x
dfu
Skip same version: %s
Power Adapter
Entering into DFU mode for Router ID %u
left bud
DecodedCrashLogKey
panicState=%@ assertID=%u
Info
Unsupported Hardware Revision
CertificateSecurityMode
Voice Assist Type
Invalid Super Binary Header
-[AppleTypeCRetimerUpdaterInstance queryHardwareID]
IECSInterface::createUserClient...
TSS Request Options for payload %@
w+
HeySiri Model Locale
IP
ACE2
ATCRT_REG_FIFO_RX
Too many queryInfo calls!
Personalization Chip Revision
<%@: 0x%016llx>
Sysconfig Region Code
UUID
reserved
bad argument
Host Inactive To Apply Asset
Header Not Found
USB-PD Location
Invalid EndpointID
\tMode: %s\n
char1
YES
Personalizing %@
Personalization FTAB Payload Production Mode
\tProtocol Version: %s
Incompatible Protocol Version
Boolean AppleTypeCRetimerUARPUpdaterReset(AppleTypeCRetimerUARPUpdaterRef _Nonnull, CFErrorRef * _Nullable)
-[FTABFile addSubfileWithTagName:contentsOfURL:]
OTA Stage 2
success
Personalization Payload Demotion Production Mode
Unable to locate bver in FTAB.
dbgb
AppleTypeCRetimerUpdaterUtils.m
UARP.LAYER3.WATCHDOG.CANCEL
not implemented
com.apple.%@.fifo.%@
-[AppleTypeCRetimerUARPUpdaterInstance checkForVersionMatch:withBver:]
none
right bud
VoiceAssist
ManifestEpoch
%s: DFU failed for %@
las_tunableh_init_plaintext
test session
%lu
Unable to create DFU updater for %@
Invalid Length
%@: Attempting to query hardware ID via UARP.
locust device
Transport
Vendor Specific
UARP Restore: %s: fLayer3FirmwareStageProgress is NULL
goLiveDate
\t\tChip ID: 0x%02x\n
Personalization Board ID
Payload Ordered Index
Payload Version
USB-PD
Case
UARP Restore: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
Voice Assist Locale
Compose Payload Hash Algorithm
tmapdatabase
.
Invalid Argument
Duplicate Message ID
Invalid Data Request Type
ECID
<%@: %@>
fPayloadWriteToAsset
UARP Restore: %s: pAsset is NULL
UARP Restore: %s: Accepted dynamic asset
Personalization FTAB Payload Digest
dynamicassets
Data Request
RTKitOS
|
Data Response
Asset Data Transfer Notification
File Not Found
UarpRestoreApplyStagedAssetsHandler
case
Personalization Payload Digest Filename
Failure
-[AppleTypeCRetimerUpdaterIIC updateWithFTAB:]
AppleHCPM
ACE Not Found
\tVersion: %u\n
HCPM
UarpRestoreLayer3FirmwareStageStatusQueueHandler
\tProduction Status: %s\n
Trigger Battery Level
Same Version Staged
Downstream Endpoint Message
las_tunableh_init
\tSecurity Mode: %s\n
\tECID: 0x%016llx\n
No iic devices found for prefix %@, nothing else to do.
-[AppleTypeCRetimerDFU writeData:]
\tNonce: %@\n
acib
releaseVersion
Failed
Bad Sequence Number
Rejected
ATCRT Response: %@\n\tResult: %s (%u)\n
secure boot
Minimum watchOS Version
uarp_querier
UarpRestoreLayer3ApplePropertyUpdateQueueHandler
UarpRestoreStageFirmwareDataBufferQueueHandler
-[AppleTypeCRetimerDFU sendPingCommand]
\tBoard ID: 0x%04x\n
-[AppleTypeCRetimerUARPUpdaterInstance printVersions]
<%@: 0x%02x>
Deferred DFU check failed.
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0
UARP Restore: Failed to tx uarp message
UARP Restore: Failed to tx uarp message to uarp silicon updater;status <0x%08x>, %s
%s: Error reading from register %s(%x)
Personalization FTAB Payload Trusted
Base64EncodedString
UarpRestoreLayer3MsgSendQueueHandler
-[AppleTypeCRetimerIICDeviceHandle readRegister:buffer:length:]
UARP.LAYER3.APPLY.ASSETS - Not Implemented
basic
AllowDownloadOnCellular
Mid Upload
-[AppleTypeCRetimerIICDeviceHandle writeRegister:buffer:length:]
%s: Error reading from register %s(0x%x)
Payload Compression Algorithm
UARP Restore (Asset Solicitation): %s: pAsset is NULL
\tBoot Nonce: 
<%@ panicState=%d assertID=%u>
LZBitmap2
bug_type
Asset Corrupt
UarpRestoreEndpointDataRecvQueueHandler
UarpRestoreRemoteEndpointAddHandler
address=0x%llx mask=0x%llx writable=0x%llx...\n
uarp
\tSession ID: %u (%s)\n
UARP Restore (Asset Solicitation): %s: pAsset->_fp is NULL
%c%c%c%c
Flash Write Error
UarpRestoreLayer3UarpPropertyUpdateQueueHandler
%u
MLB
SOP Double Prime
ProductType
Signature Write Error
- Version is %u.%u.%u.%u
IM4M-CoreUARPRestore-%d-%02d-%02d-%02d-%02d-%02d.uarp
Timing out waiting for ACEs. Last available: %@
CoreUARPRestoreAssetApplyStatus
system
\t%s: %s (%u)\n
IECS command '%c%c%c%c' still outstanding
UarpRestoreLayer3AssetSolicitationStatusQueueHandler
-[HPMForceRetimerDFUModeSetter getARMIODeviceRegistryEntryForACIOParentProperty:]
ManifestPrefix
CoreUARPRestoreAssetPersonalizedFirmware
SoftwareBinaryDsp2
Invalid Payload
Skipping update for %@ because the retimer chip is deprecated.
las_tunableh_initialized()
Ticket
response
Payload Description
com.apple.accessoryupdater.ftab
\tEntry:\n
sysdiagnose_approved
memory
retimer
Personalization Manifest Epoch
Personalization SuperBinary AssetID
UARP Restore: %s: Provided filepath is greater than max filepath length %i
UARP Restore: Failed to open file %s
suffix_length <= max_name_length
-[HPMForceRetimerDFUModeSetter doSet]
Assets
input
Invalid Asset Type
Apple Inc.
Asset Available Notification Ack
Downstream Endpoint Discovery Ack
Endpoint Component Discovery Response
%@: Performing DFU
expr
%@: DFU manifest transfer: %u%%
Personalization FTAB Payload Hash Algorithm
FirmwareVersionRelease
No Version Agreement
Asset Data Transfer Notification Ack
%s:%d:%s: %s\n
UARP Restore: %s: Protocol Version Selected %d, was previously %d
Accessory
Downstream Endpoint Message Ack
\tID: %s\n
ApChipID
name_length <= max_name_length
,Ticket
-[AppleTypeCRetimerIICDeviceHandle initIICServiceForRouterID:]
Unable to locate ACE for %@
Personalization Life
%s: Fatal error, no iic devices found for prefix %@.
UARP Restore: Failed to offer superbinary
Priority Activity
In Progress
\xf0!
Perform update input = %@
SupportsHeySiriCompact
las_tunableh_device_flavor_from_name
isalnum(c)
hashAlgorithm
Uncompressed Payload Length
DownstreamAppleModelNumbers
UarpRestoreInfoQueriesQueueHandler
ApSecurityMode
SupportsDeveloperSettings
FIRM
-[AppleTypeCRetimerIIC sendCommand:]
BSDNotifications
UARP Restore: Could not open personalized firmware file %s
btlePersonalizationNeeded
payload4cc
ProductionMode
Tethered Preflight
yes
ACIBT
\tState: %s
Personalization Logical Unit Number
com.apple.system.powersources.percent
crashlogs
ap
ok
Corrupt SuperBinary
Unable to create IIC updater for %@
IOReturn 0x%08x
Warning: Unable to locate manifest: %@
\tPersistent: %s\n
'%c%c%c%c'
las_tunableh
Personalization Payload Demotion Security Mode
Personalization FTAB Payload Digest Filename
Compose Measured Payloads
%@/%@
Upload Abandoned
UARP Restore: %s: Protocol Version Not Selected; defer info queries
%@.plist
HeySiri Model Role
ProductName
cmap
com.apple.system.powersources.source
All ACEs are available
DeviceInfo
com.apple.accessoryupdater.atcrt
Unable to convert '%@' retimer debug flags string to a 64 bit number
Version Discovery Request
\tBoard ID: 0x%08x\n
Path
Enter DFU request failed for router ID %u (0x%08x)
pcapfiles
Apply Staged Assets Response
\tChip ID: 0x%08x\n
UARP Restore (Asset Solicitation): %s: pEndpoint is NULL
UARP Restore: UARP RX: Asset Processing Notification ACK; Asset ID %u
UARP.RESTORE.LAYER3.INFO.RESPONSE <Statistics> - Not Implemented
Excluded Hardware Version
isPowerSource
majorVersion
Failed to allocate device handle for %@ during Updater instance initialization
Personalization Chip Epoch
Personalization FTAB Payload Tag
fPayloadMetaDataTLV
Mapped Analytics Event ID
isTrusted
Personalization Digest List Size
protocolaccessory
Not supported message received
NO
- Data length is %u
<Type = 0x%08x, Length = 0x%08x>
HeySiri Model Hash
Voice Assist Engine Version
UARP Restore Layer 3: Stage Status; status <0x%04x>, reason <0x%04x>
CoreUARP Restore IM4M: First Pass on TLV <0x%08x>
\tBoard ID: 0x%016llx\n
r
Endpoint Bulk Information Response
Timed out or aborted
%@,%@
Minimum macOS Version
UARP Restore: Read error %d, Read %zu bytes
buddy
accessory_pid
Personalization SuperBinary Payload Index
HPMForceRetimerDFUModeSetter
%s: Failed to query new firmware version for %@
Urgent Update
FieldLength
ESEC
%s%u
%@: DFU firmware transfer: %u%%
fPayloadDataComplete
AirPods FWUP iAUP server session
Personalization Payload Trusted
Compose Measured Payloads (Non-FTAB)
FieldPrivacyRestricted
ThunderboltDROM
Payload Certificate
Sysconfig Manufacturing Part Number
https://mesu.apple.com/assets
SupportsInternalSettings
SupportsVersions
\t%s: %@\n
UarpRestoreAssetSolicitationHandler
Active Firmware Version Equal to Asset
%@ has new firmware version: %@ (%@)
Disabled
Personalization Production Mode
com.apple.uarp.BTLEServer.personalizationNeeded
Unable to locate ACE for router ID %u
-[AppleTypeCRetimerIIC transferFirmware:length:]
rkos
Personalities
SupportsAnalytics
ReofferFirmwareOnSync
No Resources
%@
CoreUARP Restore IM4M: CoreUARPRestoreBuildPersonalizationResponse: %d 
\t\tProduction Status: %u\n
HeySiri Model Engine Type
Invalid Data Response Length
Processing Incomplete
Host Personalization Required
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetSetPayloadIndex failed with status: %u
LittleEndian
accessory_type
\t\tSession ID: %u\n
No Firmware Update Available Ack
Timer,RTKitOS
\tVendor ID: 0x%04x\n
Personalization Prefix Needs Logical Unit Number
busy
too large
Voice Assist Certificate
BluetoothVendorIDSource
UpdaterName
-[AppleTypeCRetimerDFU dfuValidate]
Created updater instance for router ID %@
\tBoard Revision: %u\n
Personalization Enable Mix Match
Personalization Nonce
NeRD Stage1
CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
Apply failed for router ID %u
AppleARMIICDevice
Update complete for %@
BuildIdentityTags
\tMagic: 0x%08x\n
com.apple.UARPUpdaterServiceUSBPD
Mismatch UUID
Endpoint Component Discovery Request
Failed to parse updated FTAB data
HeySiri Model Engine Version
FieldType
Bad Source File
UARP Restore: Mismatch in writing to manifest file %s.Expected to write %d bytes, actually wrote %d bytes
-[AppleTypeCRetimerDFU queryManifestForFTAB:]
\tChip ID: 0x%04x\n
Payload Index %u
ResponseTags
-[AppleTypeCRetimerIICBase queryRetimerPanicStatus:]
\tSecurity Domain: %u
Verbose
OTA Preflight
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Info - %d )
effectiveProductionMode
Personalization Matching Data Product Revision Minimum
Float
downstream
Micro Comms Error
BundlePath
Payload Expand Filename
SectionName
https://gs.apple.com:443
PreflightContext
UARP.RESTORE.LAYER3.INFO.RESPONSE <Last Error> - Not Implemented
platform
UARP Restore Layer 3: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
,%@
queryInfo
Log Serial Number
Invalid Asset Tag
Asset Rescinded Notification
%@%u
Failed to force power for router ID %u (0x%08x)
UARP Restore: %s: Asset fully transfered; %c%c%c%c
Payload Long Name
Personalization Options Required
SupplementalAssetsModelNumber
-[ThunderboltInterface findCapabilityForRoute:port:space:mask:value:offset:]
Failed to access router ID %u in DFU mode. Bytes sent: %lu, bytes received: %lu
UARP Restore: %s: fLayer3PersonalizedFirmware is NULL
Filepath
-[AppleTypeCRetimerUARPUpdaterInstance queryHardwareID]
Personalization FTAB Payload Security Mode
Payload Filepath
0000
com.apple.Bluetooth.AccessoryCase.pif_daily
update
Timer,ProductionMode,%u
battery
Boolean AppleTypeCRetimerUpdaterExecCommand(AppleTypeCRetimerUpdaterRef _Nonnull, CFStringRef _Nonnull, CFDictionaryRef _Nullable, CFDictionaryRef * _Nullable, CFErrorRef * _Nullable)
Dynamic Asset PreProcessing Notification Ack
RID
-[AppleTypeCRetimerDFU dfuWithFTAB:forcePersonalize:]
im4m
IsSimulator
%@:\n
Force DFU
disable
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestData failed with status: %u
Personalization Matching Data
FirmwareVersionMinor
Duplicate Accessory
-[ACE retimerEnterDFULegacy]
generateMeasurements
untethered
SuperBinary Payloads
Manifest
Endpoint Bulk Information Request
%s: Device panicked <%@ panicState=%d assertID=%u>
%s: ERROR adding remote endpoint, status = 0x%08x
ApProductionMode
UARP Restore: %s: fLayer3FirmwareStageStatus is NULL
Exceeded Packet Retry
BOOL isPanicEnabled(char *)
UARP Restore (Asset Solicitation): %s: pPayload->_fp is NULL
las_tunableh_fig_get_mask
thunderbolt
Host Network Delay
SupportsLogs
Disable Scan
Personalization ECID
UARP Restore: %s: fLayer3ApplyStatus is NULL
AppleModelNumber
IIC
BluetoothProductVersion
Same Version Active
Failure code: 0x%08X
ATCRT_REG_FIFO_TX
Allow Only if Connected
SingleStepMode
Router ID %u not ready for DFU check.
Dynamic Asset Solicitation Ack
A
UarpRestoreLayer3TssRequestQueueHandler
!las_tunableh_initialized()
UARP Restore: EOF %d, Read %zu bytes
Failed to initialize UARP endpoint for %@
PreflightTickets
Router ID %u does not require DFU mode
Verifying retimer(s) booted version.
open
MetaData Hash
Force DFU Mode
UARP Restore (Asset Solicitation): %s: fseek failed
sbd2
off
Personalization Payload Effective Security Mode
minorVersion
ACE Task: %@
InfoArray
\tVersion: %s\n
SuperBinary Firmware Version
Controller
UarpRestoreAssetSolicitation
fPayloadData
Personalization More Requests to Follow
App Start Failed
ChipID
Personalization Security Domain
Force DFU mode is %s
on
com.apple.UARPUpdaterServiceHID
writing
Higher Version Active
Nonce
LZBitmapFast2
UploaderResponseTimeout
DFU failed for %@
Update failed for router ID %u
AOP
USB-PD Device Class
SFWd was not run
I2C
%s: NULL pUarpCtx
/Library/Caches/com.apple.xbs/1B41C110-6977-45B0-93CC-2DE6B66CB3A1/TemporaryDirectory.WwQFnM/Sources/libAppleSilicon/tunableh/v2/tunableh.c
-[HPMForceRetimerDFUModeSetter startMonitoringForOperationCompletion]
%u.%llu.%u
error
system config
sections
CmapEvents
-[ACE disableDFUfTaskIfActive]
AppleHPMDevice
Erase Option
,%lu
- Tag is %c%c%c%c
-[AppleTypeCRetimerUARPUpdaterInstance performDfuUpdateForSuperBinary:withManifestData:]
_brd
host_debug_assert
las_tunableh_fig_get_expression
Unable to create IIC device handle for %@%u
Unknown Payload
protocolcontroller
%s: Error writing to register %s(%x)
\t\tSecurity Mode: %u\n
Personalization FTAB Payload
UARP Restore: %s: fLayer3AssetSolicitationStatus is NULL
UARP Restore: %s: Rx pRestoreAsset was NULL
\tGeneration: 0x%08x\n
No Memory
-[AppleTypeCRetimerDFU transferDataBuffer:length:sessionID:]
yboot
Payload Hash Algorithm
USBCLightningDisconnect
I
<%@: \r
\tManifest: %@\n
Endpoint Bulk Information Request Ack
-[AppleTypeCRetimerDFU sendB2PCommand:responseClass:]
/var/db/accessoryupdater/dropbox
Events
transmitqueue
IOService
-[AppleTypeCRetimerUARPUpdaterInstance startAppModeUpdateForSuperBinaryData:]
Name
MetaData plist
UARP Restore: Tatsu Server set to %s
com.apple.accessoryupdater.uarp
Candidate retimer firmware version: %@
Payload Hash
Unknown Message Type
MetaData Corrupt
Unable to create DFU updater for router ID %u
UARP Restore (Asset Solicitation): %s: No Payload Metadata
Updater instance forcing power on for %@
%s: DFU complete for %@
Personalization Chip ID
ServiceBSDNotifications
Asset Not Found
-[ThunderboltInterface createPluginInterfaceForService:]
PhyBlueTooth
https://mesu.apple.com/assets/macos/
EventID
HigherVersion
Timer,ChipID,%u
retimer_force_dfu
SHA-256
Integer
\tValid: %u\n
No MetaData
Endpoint Discovery Response
Bad Argument
None
VendorID
SupplementalAssets
firmware
<%@ len=%lu>
Downstream Endpoint Unreachable
-[ACE dfufTaskRunning]
las_tunableh_module_evaluate
HeySiri Model Certificate
-[FTABFile initWithContentsOfURL:]
ACE Info:\n
UARP Restore: Failed to offer superbinary, status 0x%08x
\tInternal FW Version: %s\n
PreflightRequired
unrecognized
HeySiri Model Digest
Invalid Offset
Timer,SecurityMode,%u
-[AppleTypeCRetimerDFU readData]
Skipping update for %@ because it already has this firmware version.
\tStatus: %u (%s)\n
com.apple.%@.apply
SupportsPowerlog
sysdiagnose
Failed to generate updated super binary for %@
fAssetMetaDataComplete
Minimum Required Version
MetaData Hash Algorithm
UARP Restore: Mismatch in writing to personalized firmware file %s.Expected to write %d bytes, actually wrote %d bytes
\tStatus: %s\n
Personalization SoC Live Nonce
%s: fatal error detected at this stage.
Life
%@:\n\tOp Code: 0x%04x\n\tRoute: %s
Incompatible HW
Limited
UARP Restore: %s: pAsset->_pAsset is NULL
silicon
ProductGroup
tmap
Sysconfig Regulatory Model Number
name
Did NOT find service matching AppleHPMDevice
Personalization Matching Data Payload Tags
SuperBinary MetaData
https://basejumper.apple.com/assets/
https://basejumper.apple.com/mesu_staging
Unknown Accessory
Apply Staged Assets Request
IOThunderboltController
HID
tmpfiles
Personalization ECID Data
Analytics Payload Type
Processing Error
IOGeneralInterest
- MetaData length is %u
Trusted
\tDevice ID: 0x%04x\n
updater_instance
Router ID %u placed into DFU mode
host
AirPods FWUP iAUP client session
%@: options = %@
Host Reconnect After Apply
DPRO
RTKitOSFeature
Flash Partition Bitmap
releasenotes
!
No AC Power
Enabled
Address
Host Inactive To Stage Asset
ATCRT_REG_FIFO_STATUS
HardwareID
%s: read operation failed
Failed to write '%@' header
Router Op: Timed out waiting for prvious router operation processing to complete
Router Op: Failed to read data register %u
Unable to continue with DFU, router is already enumerated.
%s: write operation returned %u
%@: Detected FIFO RX underrun
%s: Unable to locate %@
%s: %@ [RID %u]
Failed to receive response to %@
B2P has been reset
Failed to force update mode %s (0x%08x) [RID=%u]
%s: Error parsing file offset list (offset=%u, length=%lu)
%s: Unable to open connection to %@ (0x%08x)
Found rid %d on PCI device
Task %@ failed to execute: 0x%02x (%s) [RID %u]
Router Op: Timed out waiting for router operation 0x%04x to complete
%s: Failed to locate ARM device
%s: Unable to open file at %@ (%@)
Failed to query task result status for %@ (%@) [RID %u]
%s: Waiting for %s request to complete
Failed to open file handle for writing to '%@'
%s: No response received for ID command
%s: Detected that ACE is in DFU mode. [RID %u]
Failed to force power %s (0x%08x) [RID=%u]
Failed to enable UART
Failed to locate device address (0x%08x)
%s: Data write for %@ failed (0x%08x).
HPM interface not supported for service.
%s\n
Router Op: Failed to write metadata
%s: DFU validation failed
%s: Failed to look up ARM devices (0x%08x)
%s: Code write for %@ failed (0x%08x).
%@: Detected FIFO TX overrun
%s: Update failed
%s: Failed to receive data response
%s: read operation returned %u
%@: Failed to read FIFO error register (0x%08x)
%s: Subfile offset error (offset=%u, length=%u)
%@: Failed to initialize UARP endpoint for querying the hardware ID
%s: Read more bytes than asked! (%u > %u)
Failed to locate plugin interface (0x%08x)
%s: Read %u bytes, expected %u
Command response with op code 0x%04x is not supported
HPM v3 interface supported.
%s: File tag parse error (%02x %02x %02x %02x)
Unable to delete file at %@
Failed to locate retimer for router ID %u
%s: No response received for ping command
Expired temp file %@ 
%s: %@
%s: Failed to force ACE out of DFU mode [RID %u]
Router Op: Failed to start operation
%s: write operation failed
%s: Command in flight!
File path is a directory, skipping it and it's descendants %@
%s: Failed to register for interest (0x%08x)
%s: Timed out waiting for %s operation to complete.
Force update mode %s [RID=%u]
Router Op: Router operation 0x%04x was not supported
%s: Failed to locate _thunderboltController
%s: %s is %s
%s: %@ Command failed\n%@
%s: Unexpected header magic (%02x %02x %02x %02x %02x %02x %02x %02x)
Failed to locate Thunderbolt interface for router ID %u
%s: Failed to locate ACIO parent data
%s: Read result 0x%08x
Failed to query vendor specific base regiser
%s: Task %@, unexpected command response %@
%s: Manifest parameters are invalid
%s: Unable to locate rkos image
%s: Force power failed (0x%08x) [RID %u]
%s: Write result 0x%08x, length = %u
Unable to open file for writing at %@ (%@)
%@ task failed to execute [RID %u]
%@: HW ID Querier FIFO transfer error (%@)
%s: Failed to generate manifest.
%s: Receiving commands not supported
%s: Force retimer DFU mode failed (0x%08x)
Failed to trigger system panic: %d
%s: Task %@ timed out
%s: Failed to read output for %@ (0x%08x)
Failed to write '%@'
Updating to version: %@
Failed to locate valid address property.
%s: Local transfer count did not match chip transfer count (local=%u, chip=%u)
%s: Unable to locate rrko image
%s: No response received for data session connect command (session=%s, state=%s)
Checking age of temp file %@
%s: %s operation completed successfully
Unable to parse command response for op code 0x%04x
Unable to locate subfile with tag '%@'
%s: DFUf check failed [RID %u]
Router Op: Failed to write to data register %u
Failed to write manifest
%s: DFU boot failed
%s: Parsing command output not supported for %@
%s: HPM iterator lookup failed (0x%08x)
%@
%@: Failed to start query (%s)
%s: Wrote more bytes than asked! (%u > %u)
Unable to create file at %@
Failed to read ROUTER_CS_VCS_17
%s: Failed to send %@
%s: Set complete.
%s: Task %@ unrecognized
Force power %s [RID=%u]
%s: command request failed (%@) [RID %u]
%s: Failed to open %s data session
Found rid %d on ARMIO device
Failed to query HPM interface (0x%08x)
Router Op: Failed to read metadata
Failed to read ROUTER_CS_3
HPM v3 interface not supported.
%s: File too short
Failed to write FTAB header
%s: ACE DFU mode has been disabled. [RID %u]
%s: Failed to query ACE mode [RID %u]
DFUing verson: %@
Failed to find vendor specific capability
%s: failed (0x%08x)
%s: No work to do for %s request
%s: Command response read for %@ failed on iteration %u (0x%08x)
%s: Force DFU failed [RID %u]
%s
Router Op: Dword buffer too large (%u)
UARPTLVPersonalizationSecurityDomain
UARPTLVPersonalizationChipRevision
UARPTLVPersonalizationManifestPrefix
B2PFirmwareVersionGetCommand
UARPTLVPersonalizationBoardID
UARPTLVPersonalizationFTABSubfileTag
B2PDataSessionConnectResponse
AppleTypeCRetimerIICDeviceHandle
UARPTLVMeasuredPayload
B2PAutoHealGetCommand
B2PCommand
B2PDataSessionDataCommand
ContainsUtils
AppleTypeCRetimerIIC
FTABFile
AppleTypeCRetimerPanicStatus
ThunderboltPacketDumper
UARPTLVPersonalizationFTABSubfileEPRO
UARPTLVPersonalizationFTABSubfileHashAlgorithm
B2PDFUValidateCommand
ATCRTCommandSFWd
ATCRTCommandSFWs
ATCRTCommandGaid
AppleTypeCRetimerDeviceHandle
B2PAutoHealGetResponse
B2PDataSessionConnectCommand
B2PDataSessionDiscoveryResponse
AppleTypeCRetimerFifoQueue
B2PPingResponse
AppleTypeCRetimerUpdateController
UARPTLVHostPersonalizationRequired
UARPTLVPersonalizationFTABSubfileESEC
UARPTLVPersonalizationTicketNeedsLogicalUnitNumber
UARPTLVPersonalizationManifestSuffix
UARPAssetTag
UARPTLVPersonalizationLogicalUnitNumber
HardwareIDUtils
UARPTLVPayloadCompressionAlgorithm
ATCRTResponseSFWf
B2PBudVersionGetCommand
UARPMetaDataTLVString
AppleTypeCPacketDumper
UARPTLVPersonalizationSuperBinaryAssetID
ATCRTResponse
ThunderboltInterface
UARPTLVPersonalizationFTABSubfileDigestFilename
ATCRTCommandSFWi
B2PBudVersionGetResponse
NSCoding
Utils
B2PIdentificationCommand
AppleTypeCRetimerDFU
UARPTLVPersonalizationEnableMixMatch
AppleTypeCRetimerDFUChecker
B2PProductCategoryGetCommand
ATCRTCommand
RTKit
UARPTLVPersonalizationProvisioning
Bver
NSCopying
UARPTLVPersonalizationChipEpoch
UARPTLVRequiredPersonalizationOption
AppleTypeCRetimerUpdaterHelper
AppleTypeCRetimerUARPUpdaterController
ACETaskCommandDFUf
UARPTLVPersonalizationSuffixNeedsLogicalUnitNumber
AppleTypeCRetimerHardwareID
B2PIdentificationResponse
ATCRTResponseSFWs
ACE
AppleTypeCRetimerIICFifoDelegate
UARPTLVPersonalizationFTABSubfileLongname
UARPTLVPersonalizationNonce
UARPTLVPersonalizationRequired
UARPTLVPersonalizationManifestEpoch
FTABSubfile
AppleTypeCRetimerUpdaterIIC
ACETaskCommand
UARPTLVPersonalizationProductionMode
UARPTLVPersonalizationECID
B2PDataSessionDataResponse
AppleTypeCRetimerIICDelegate
AppleTypeCRetimerUARPUpdaterInstance
UARPTLVPersonalizationSoCLiveNonce
B2PDFUBootCommand
UARPSuperBinaryPayload
UARPTLVPersonalizationFTABSubfileTrusted
FTABWrite
ATCRTResponseSFWd
B2PPingCommand
AppleTypeCRetimerUARPHardwareIDQuerier
IECSInterface_GoldRestore2
AppleTypeCRetimerIICFifo
UARPSuperBinary
UARPMetaDataTLVData
AppleTypeCRetimerUpdaterInstance
ACETaskCommandVOUT
AppleTypeCRetimerDFUDelegate
AppleTypeCRetimerHPM
ATCRTCommandSFWf
B2PEngine
B2PProductCategoryGetResponse
UARPTLVPersonalizedManifest
NSSecureCoding
B2PDataSessionDiscoveryEntry
ATCRTAPHardwareID
UARPTLVPersonalizationECIDData
B2PTimer
AppleTypeCRetimerFifoDumper
UARPTLVPersonalizationChipID
UARPTLVPersonalizationLife
UARPTLVPersonalizationPayloadTag
UARPMetaDataTLV16
ATCRTCommandGAID
PrintUtils
UARPAssetVersion
UARPMetaDataTLV64
UARPMetaDataTLV8
UARPTLVPersonalizationSuperBinaryPayloadIndex
UARPTLVPersonalizationNonceHash
AppleTypeCRetimerUARPUpdaterInstanceDelegate
ATCRTResponseSFWi
B2PResponse
UARPMetaDataTLV32
UARPTLVPersonalizationPrefixNeedsLogicalUnitNumber
UARPTLVPersonalizationFTABPayload
UARPPayloadPersonalizationInfo
UARPMetaDataTLV
B2PDataSessionDiscoveryCommand
AppleTypeCRetimerBoardIDFile
AppleTypeCRetimerIICBase
HPMForceRetimerDFUModeSetter
UARPTLVPersonalizationSecurityMode
UARPTLVPersonalizationFTABSubfileDigest
B2PSerialNumberGetResponse
ATCRTBloodhoundPacketDumper
_activeRevision
Ti,R,V_dataSessionStatus
_b2pLinkLinearBuffer
_category
effectiveProductionMode
initWithRoute:status:sessionID:dataSessionStatus:data:
initWithService:
queryChipIdentification
T@\"UARPAssetVersion\",R,V_version
T@\"NSData\",R,V_bootNonce
payloadIndex
TC,V_route
TI,R,V_chipID
_securityEpoch
bootNonce
setBootNonce:
_log
_suppressed
chipInfo
fileValidForOffset:length:
payloadDigest
performUpdateWithDictionarySingleStep:
TB,V_demote
TI,R,V_securityDomain
dumpATCConfigRegisterRead:value:
setManifest:
writeRegister:buffer:length:
_b2pCommandInFlight
_filename
byteString
isValid
_ticketPrefix
minorVersion
stringByAppendingPathComponent:
_b2pOpCodeInFlight
_protocolVersion
b2pReset:
initWithChipID:boardID:securityEpoch:productionStatus:securityMode:securityDomain:ecid:nonce:chipRev:
_dfuBaseAddress
forceDFU
initFile
receivedData:
setECID:
setTssOption:
tssOption
writeData
rid
_scheduledTimers
ecidData
arrayWithObjects:count:
setLongname:
_formatVersion
_uinitNumber
stopPollingforReceiveData
timeIntervalSinceDate:
_securityDomain
TS,R,V_opCode
performRouterOperationWithOpCode:metadata:dWordBuffer:dWordCount:returnStatus:
setSecurityEpoch:
TB,R,V_needsHostPersonalization
TB,V_fwPanic
_locatedObjects
tlvs
TC,R,V_boardRevision
_fwPanic
_manifest
getDataBlock:offset:
initWithRouterID:delegate:forcePower:
writeToURL:
_notReadyRouterIDs
opCodeField
stringWithFormat:
_dumper
.cxx_destruct
decodeObjectOfClass:forKey:
digestListSize
initWithDeviceHandle:
setPersonalizedData:
setSessionID:
_ticketSuffix
convertDwordToData:bytes:
logInternal:arguments:
numberWithUnsignedShort:
T@\"NSString\",R,V_longname
dealloc
initWithFormat:
_uarpQueue
createFileNameForFirmware:
requiresPersonalization
_metaData
tssOptions
TB,R,V_forceDFUMode
tlvLength
errorWithDomain:code:userInfo:
expandSuperBinary
generatePersonalizedSuperBinaryWithoutRRKO
length
queryInfoSingleStep
startTimerType:deadlineMS:
TB,R,V_enabled
_hpmInterface
encodeObject:forKey:
initWithDeviceHandle:queueLabelSuffix:
isTrusted
securityMode
tlvTypeName:
TC,R,V_apChipRev
TC,R,V_result
_fileHandleWriteDestination
_isRequired
_payloads
_stageSuccess
queryInfo
sleepTimeForCommandResultPollIteration:
T@\"NSData\",R,V_ecID
TQ,R,V_bytesSent
hasResponse
_asset
init
initPluginInterfaceForService:
manifestBytesSent:bytesTotal:
route
TB,R
tag
Tq,V_hashAlgorithm
_logFunction
_pollingTimerSource
doCheckForRouterIDList:allowsNotReady:
getACIOParentData
pendingRevision
_tlvType
convertBytesToDword:length:
dfuWithFTAB:forcePersonalize:
epro
initWithChar1:char2:char3:char4:
retimerForcePower
T@\"NSData\",R,V_writeData
TQ,R,V_totalLength
_char1
destroyUserClient
removeSubfile:tag:
sharedInstance
preparePayload:
T@\"NSData\",C,V_ecidData
_applySuccess
_deviceHandle
addSubfileWithTagName:contentsOfURL:
bytes
_url
pingChip
_dataPointer
payloadWith4ccTag:
_manifestSuffix
TS,R,V_version
appendByte:
initializeUpdaterInstancesForcingPower:
numberWithUnsignedInt:
pathWithComponents:
sendDataSessionConnectCommandForSessionID:state:
updateTransmitFifoSpace
dfufTaskRunning
dataPointer
waitForCurrentRouterOperationToComplete:
_singleStepMode
TI,V_chipID
_nextDFUFirmwareProgressReportPercentThreshold
createFileAtPath:contents:attributes:
sendManifest
setEffectiveProductionMode:
TI,V_assertID
arrayWithObjects:
needsHostPersonalization
unitNumber
T@\"<AppleTypeCRetimerDFUDelegate>\",W,V_delegate
TI,R,V_chipEpoch
writeToDestination
command
_b2pReset
_useLocalSigning
dfuModeEnabled
doesNotRecognizeSelector:
startMonitoringForOperationCompletion
_digestListSize
TC,R,V_portNumber
TQ,R,V_boardID
_liveNonce
life
tatsuMeasurements:
TS,R,V_activeMajor
parseResponse:
status
forceUpdateMode:
lowercaseString
T@\"NSData\",C,V_sessionData
getPayloads
printVersions
setLogicalUnitNumber:
T@\"NSObject<OS_dispatch_queue>\",&,V_delegateQueue
T@\"NSData\",R,V_digest
T@\"NSNumber\",&,V_chipID
T@\"NSTimer\",R,V_timer
Tr*,R,V_filePointer
_b2pQueue
checkForVersionMatch:withBver:
inputCommandWithOpCode:data:
_status
_esec
queryManifestForFTAB:
TB,R,V_allowOnlyIfConnected
_uarpChipCallbacks
addObject:
initWithURL:delegate:delegateQueue:
timer
_tssOption
TS,R,V_epro
Ti,V_state
_layer2Context
enableMixMatch
logicalUnitNumber
stringWithString:
Ti,R,V_category
TC,R,V_prefixNeedsLogicalUnitNumber
_flavor
checkReady
generateTLV
pollForReceiveData
updateWithFTAB:
fileExistsAtPath:
retimerRemoveForcePower
TC,R,V_routerID
T@\"NSData\",C,V_nonce
_protocolMode
category
encodeInteger:forKey:
_boardID
_notificationPort
_txFifoSpace
TC,R,V_ticketNeedsLogicalUnitNumber
tlvWithLength:value:
_demote
T@\"NSNumber\",R
TC,V_securityDomain
_nextDFUManifestProgressReportPercentThreshold
initWithData:metaData:tag:version:
registerWriteForVendorIndex:value:
metaData
setPayloadIndex:
TQ,R,V_fileLength
shouldResetAfterUpdate
_interface
firmwareStagingCompleteWithStatus:reason:
initWithBVERString:
initWithData:encoding:
parseCommand:
unsignedCharValue
_enable
dumpATCRouterOperationWithOpCode:data:
name
T@\"NSData\",&,V_manifest
T@\"NSData\",R,V_magic
TI,R,V_dataLength
_pendingRevision
_tlvLength
_trimmedTlvs
generateFTABForData:manifestData:apHardwareID:debugFlags:
personalizeSuperBinary:signingServer:ssoOnly:
_enableMixMatch
state
T@\"NSString\",R,V_ticketPrefix
_fileLength
longTagName:
setUarpChipCallbacks:
_infoID
TC,V_sessionID
_uarpContext
tssRequestAsString
cancel
createUserClient
filename
initWithFilePath:delegate:delegateQueue:
_buffer
startPacketDumperWithFileName:productID:
verifyRouterIsNotEnumerated
performUpdateIIC
setMaxB2PFrameSize:
T@\"NSString\",C,V_payloadLongname
T@\"<AppleTypeCRetimerUpdaterIICDelegate>\",W,V_delegate
_forceDFUMode
boardRevision
payloadsWithout4ccTag:
setComplete
T@\"NSData\",R
T@\"NSMutableArray\",&,V_trimmedTlvs
initWithRouterID:route:port:space:baudRate:
initWithTag:data:
payloadData
pendingMajor
setManifestEpoch:
T@\"NSNumber\",&,V_productionMode
_apChipRev
date
flavor
iecsAtomicCommand:data:dataLength:retData:retDataLength:flags:timeout:
setAssetID:
setNonce:
_assertID
_assetID
transferDataBuffer:length:sessionID:
initWithWriteData:
setPayloadDigest:
firmwareBytesTransferred:bytesTotal:
nonceString
queryComplete
queryHardwareID:
setTicketNeedsLogicalUnitNumber:
startPollingForReceiveData
suppressed
unsignedLongLongValue
_aceInfo
_epro
copy
setRoute:
writeData:error:
personalizedMetaData
setChipEpoch:
TC,R,V_securityMode
_chipEpoch
_timerSource
setFilename:
setPayload4cc:
TB,V_suppressed
pendingFile
setPersonalizedMetaData:
manifestSuffix
numberWithUnsignedChar:
processTLVsForPersonalization
useLocalSigning
TS,R
initWithFourCharacterCode:byte0:resultDescriptionFunction:
sessionID
setPrefixNeedsLogicalUnitNumber:
_chipID
UTF8String
_logicalUnitNumber
T@\"NSString\",&,V_keyManifest
_blockCount
_idResponse
configWriteForRoute:port:space:index:value:
_releaseVersion
TI,R,V_securityMode
configWriteForIndex:value:
initializeDeviceInterfaceForRouterID:
personalizationParameters
TS,R,V_trusted
_buildVersion
_iicUpdater
_trustedOverride
b2pTimerForNSTimer:
code
payload4cc
Ti,R,V_infoID
_hpmConnection
encodeBytes:length:forKey:
initWithContentsOfURL:
TI,V_maxB2PFrameSize
addSubfileWithTagName:subfileData:
executeTask:
keyManifest
measurements
TC,R,V_blockCount
TI,R,V_chipRevision
TI,R,V_isRequired
_compressionAlgorithm
_dataWriteDestination
_deviceService
appleTypeCRetimerIICFifo:receivedData:
hashAlgorithm
iecsWriteForAddress:buffer:length:flags:
T@\"<AppleTypeCRetimerIICDelegate>\",W,V_delegate
activeMajor
initWithDeadlineMS:type:queue:block:
initWithBloodhoundDumper:
initWithMajorVersion:minorVersion:releaseVersion:buildVersion:
removeObject:
stringWithValidatedFormat:validFormatSpecifiers:error:
TS,R,V_pendingMajor
_skipSameVersion
TI,R,V_productionMode
expandTLVs
versionString
writeSubfileToURL:tag:
_tbtInterface
createPluginInterfaceForService:
fileLength
initWithRoute:status:data:
tlvValue:
_isForceDFUModeEnabled
chipRevision
drainTransmitQueue
setEnableMixMatch:
protocolVersion
_serviceName
_value
setChipRevision:
T@\"NSString\",R
_service
dumpPacket:type:metadata:metadataLength:
fileHandleForWritingToURL:error:
initWithVersionString:
Ti,V_debugLevel
TI,R,V_tssOption
initWithType:length:value:
TI,R,V_generation
_tag
numberWithBool:
TC,V_manifestEpoch
appendLittleInt16:
ecID
_activeFile
appendBytes:length:
description
isDoneSingleStep
queryInfoAggregate
setEcidData:
setUarpContext:
Ti,R,V_sessionID
bytesAvailableToRead
dumpCommand:
T@\"NSData\",R,V_nonceHash
Ti,R,V_status
_enabled
requestType
sfwfBlockCount:length:
_pendingMinor
initWithSessionID:tag:
log:
nonce
objectForKey:
setService:
superbinary:logString:
dumpResponse:
isEqualToString:
string
_forceDFU
chipEpoch
count
getARMIODeviceRegistryEntryForACIOParentProperty:
setMaxTransmitAttempts:
log
TC,R,V_value
getDelegateQueue
TQ,R,V_majorVersion
readData
serialNumber
setCompressionAlgorithm:
T@\"NSNumber\",&,V_securityDomain
_trusted
composeTSSRequest:
iecsWaitForIdle:pollInterval:timeout:
metaDataTableEntry
registerIndexForVendorIndex:
initIICServiceForRouterID:
objectForKeyedSubscript:
TQ,V_unitNumber
_route
T@\"NSData\",R,V_metaData
TI,R,V_magic
_logContext
dumpAccessForRegisterAddress:ioReturn:data:
initWithService:isHCPM:
unsignedIntValue
enabled
TB,R,V_isDone
Ti,R,V_type
_aggregateUpdateComplete
_allowOnlyIfConnected
_bytesWritten
generateHashSHA512
nextObject
T@\"NSNumber\",C,V_demote
_payloadIndex
tlvFromKey:value:
writeToData
T@\"NSNumber\",C,V_effectiveProductionMode
Tc,R,V_char4
initForceDFU
initWithString:
TC,R,V_activeFile
_ftab
char1
forceDFUMode
T@\"NSNumber\",C,V_isTrusted
T@\"NSString\",R,V_filename
TC,R,V_suffixNeedsLogicalUnitNumber
_pluginInterface
_started
_configBuffer
getThunderboltControllerForARMIODevice:
stripHWModelSuffix:
_bytesReceived
_dfuUpdater
_uarpSemaphore
path
TI,N,V_deviceService
_isTrusted
initWithDelegate:socat:
initWithForceDFUMode:allowOnlyIfConnected:
receivedResponse:
setEffectiveSecurityMode:
startPacketDumperWithFileName:productID:dataSessionProtocol:
_result
containsObject:
TC,R,V_enable
_generation
_routerID
addObjectsFromArray:
dataWithContentsOfURL:options:error:
_entries
blockCount
convertBytesToDwords:length:dWordBuffer:
dataWithData:
initWithRouterID:namePrefix:
setEcID:
bverString
getDeviceNames
opCode
retimerEnterForceDFU:
transferError:
_ace
_writeQueue
initWithHPMService:deviceService:enableDFUMode:
T@\"NSDictionary\",&,V_tssOptions
locatedDevices
removeItemAtPath:error:
_hashAlgorithm
defaultManager
initWithBytes:length:
payloadLongname
dfuValidate
isGreaterThan:
removeSubfileWithTag:
setAssertID:
T@\"NSData\",&,V_personalizedData
getBver
TI,R,V_logicalUnitNumber
_b2pLock
suffixNeedsLogicalUnitNumber
activeFile
char4
initWithByte0:
TI,R,V_tlvLength
deleteCharactersInRange:
registerReadForVendorIndex:result:
startAppModeUpdateForSuperBinaryData:
T@\"NSNumber\",C,V_digestListSize
T@\"NSNumber\",C,V_trustedOverride
TI,R,V_tlvType
_iic
hasPrefix:
retimerEnterDFULegacy
setSuffixNeedsLogicalUnitNumber:
_hardwareID
findCapabilityForRoute:port:space:mask:value:offset:
initWithEnabled:forceDFU:
performUpdateDFU
unsignedIntegerValue
activeRevision
performUpdateForFTABData:manifestData:apHardwareID:skipSameVersion:debugFlags:
sendResponse:
TB,R,V_productionStatus
Ti,R
_boardRevision
_nonceHash
initWithTag:dataPointer:dataLength:
TC,R,V_manifestEpoch
checkDeferredRouterIDs
T@\"NSData\",C,V_payloadDigest
now
Tc,R,V_char2
_bytesSent
assertID
queryRetimerPanicStatus:
_b2pSemaphore
_magic
_writeData
doSet
flavorField
personalizedData
TS,R,V_assetID
_char4
_life
_tlvValue
isDone
version
_prefixNeedsUnitNumber
_valid
setChipRev:
setTrustedOverride:
setKeyManifest:
T@\"NSString\",R,V_name
_port
caseInsensitiveCompare:
generateTLV:tlvValue:
_sessionID
initWithBytes:length:encoding:
initWithHPMService:routerID:deviceService:
T@\"NSData\",R,V_data
T@\"NSData\",R,V_payloadData
TC,R,V_securityDomain
T^v,V_layer2Context
processMeasurementsForTSSOptions:unitNumber:asMeasurement:
timerFired:
setTrimmedTlvs:
_tssOptions
compressionAlgorithm
initUARPWithDeviceHandle:captureFileName:
inputData
TQ,R,V_activeMinor
TQ,R,V_bytesReceived
TS,R,V_hashAlgorithm
TS,R,V_pendingRevision
_ecidData
longname
portNumber
result
T@\"NSNumber\",&,V_ecID
TI,R,V_valid
Tr*,R,V_dataPointer
_persistent
arrayWithCapacity:
copyWithZone:
createFileHandleForWritingToURL:
fileExistsAtPath:isDirectory:
_data
firmwareApplyCompleteWithStatus:flags:
objectAtIndex:
tlvValue
_baudRate
_prefixNeedsLogicalUnitNumber
_updaterIndex
addEntriesFromDictionary:
lastPathComponent
liveNonce
releaseVersion
TQ,R
_type
dataTransferUpdateForBytesSent:bytesTotal:sessionID:
queryHardwareID
TS,R,V_boardID
_code
boolValue
initWithSessionID:status:data:
protocolMode
stringByExpandingTildeInPath
writeBytes:length:handle:
T@\"NSString\",R,V_aceInfo
TQ,V_ecID
URLByDeletingLastPathComponent
generateHashSHA384
setUnitNumber:
writeToURL:error:
b2pDataSessionOpenForSessionID:
maxB2PFrameSize
_txQueue
numberWithUnsignedLong:
setHashAlgorithm:
stopTimerType:
expandMetaData:
T@\"NSArray\",R,V_measurements
doCheck
_unitNumber
allocateUpdaterDFU
configureFileHandleWriteDestinationForURL:
hardwareID
initWithOpCode:route:status:
T@\"UARPAssetTag\",R,V_tag
persistent
TI,R,V_flavorField
_sessionData
appendData:
containsAllObjectsIn:
queryChipInfo:
unlock
_deviceNamePrefix
_pendingMajor
_queue
subdataWithRange:
Ti,R,V_protocolMode
setObject:forKeyedSubscript:
Ti,R,V_state
_b2p
_personalizedData
_serialNumber
bytesSent:bytesTotal:
hash
configureDataWriteDestination
digest
unsignedShortValue
propertyChanged
_char2
configReadForIndex:result:
inputCommandResponseWithOpCode:status:data:
prefixNeedsLogicalUnitNumber
_notification
ecid
T@\"NSArray\",&,N,V_locatedObjects
TI,R,V_flavor
queryPanicStatus:
trimmedTlvs
TC,R,V_life
T@\"NSArray\",R,V_tlvs
_ecID
_enableDFUMode
_suffixNeedsLogicalUnitNumber
allocateACE
configReadForRoute:port:space:index:result:
_querySemaphore
_address
_payloadLongname
pendingMinor
receivedCommand:
securityDomain
setManifestSuffix:
_notificationSemaphore
lookupThunderboltController
pendingVersion
removeAllObjects
stringWithDescString:
T@\"NSData\",R,V_sessionData
_productionMode
_measurements
appendString:
configReadMetadata:opCode:
dataWithContentsOfURL:
sendIdentificationCommand
T@\"NSNumber\",&,V_boardID
_notReadyRouterIDsLock
_payloadData
absoluteString
_block
convertDWordsToData:bytes:
generateTatsuMeasurements:relativeURL:
url
initWithOptions:logFunction:logContext:deviceNamePrefix:
performUpdateForSuperBinaryData:manifestData:apHardwareID:skipSameVersion:debugFlags:bver:
setTag:
T@\"FTABSubfile\",R,V_manifest
T@\"NSArray\",R
Ti,V_status
_b2pResponse
_uarpInitialized
_userClientActive
appendData:descStr:
TC,R,V_liveNonce
dateByAddingTimeInterval:
generateTatsuMeasurementsPerPayload:
getAvailableReceiveDataLength
setLiveNonce:
totalBytesRequested
verboseLog:
T@\"NSString\",C,V_payload4cc
T@\"NSNumber\",C,V_effectiveSecurityMode
Ti,R,V_protocolVersion
_connection
checkForVersionMatch:
```
