# `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,420,864 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 3776)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/updaters/libAppleTconUARPUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (175 classes, 8 protocols)

Classes: `BanyanUARPTransport`, `BanyanUARPUpdaterDevice`, `BanyanUARPUpdaterLog`, `BanyanUARPUpdaterManager`, `Tcon`, `UARPComponentConfiguration`, `UARPComponentTag`, `UARPComponentVersion`, `UARPDeploymentRules`, `UARPEndpointConfiguration`, `UARPEndpointLayer3`, `UARPEndpointOptions`, `UARPEndpointPacketCapture`, `UARPHashMachine`, `UARPLastError`, `UARPMetaData`, `UARPMetaDataComposeBVERStringFile`, `UARPMetaDataComposeFTABPayload`, `UARPMetaDataComposeMarketingBVERStringFile`, `UARPMetaDataComposeMetaDataHashAlgorithm`, `UARPMetaDataComposePayloadHashAlgorithm`, `UARPMetaDataComposePropertyListPayload`, `UARPMetaDataComposeSimpleBVERStringFile`, `UARPMetaDataComposeVersionStringFile`, `UARPMetaDataCrashAnalyticsAppleModelNumber`, `UARPMetaDataCrashAnalyticsCoreName`, `UARPMetaDataCrashAnalyticsTestMode`, `UARPMetaDataDeviceCompressPayloadChunkSize`, `UARPMetaDataDeviceCompressedHeaders`, `UARPMetaDataDeviceFirmwareVariant`, `UARPMetaDataDeviceFlashSectionLength`, `UARPMetaDataDeviceIgnoreVersion`, `UARPMetaDataDeviceMetaDataHash`, `UARPMetaDataDeviceMetaDataHashAlgorithm`, `UARPMetaDataDeviceMinimumRequiredVersion`, `UARPMetaDataDevicePayloadCertificate`, `UARPMetaDataDevicePayloadExpandFilename`, `UARPMetaDataDevicePayloadHash`, `UARPMetaDataDevicePayloadHashAlgorithm`, `UARPMetaDataDevicePayloadIdentifier`, `UARPMetaDataDevicePayloadIdentifierString`, `UARPMetaDataDevicePayloadOrderedIndex`, `UARPMetaDataDevicePayloadSignature`, `UARPMetaDataDeviceUncompressedPayloadLength`, `UARPMetaDataDeviceUrgentUpdate`, `UARPMetaDataDeviceVendorVersionStringFile`, `UARPMetaDataFdrContext`, `UARPMetaDataFdrData`, `UARPMetaDataFdrDataToSign`, `UARPMetaDataFdrParameterData`, `UARPMetaDataFdrParameterName`, `UARPMetaDataFdrSignature`, `UARPMetaDataHeySiriModelActiveModel`, `UARPMetaDataHeySiriModelCertificate`, `UARPMetaDataHeySiriModelDigest`, `UARPMetaDataHeySiriModelEngineType`, `UARPMetaDataHeySiriModelEngineVersion`, `UARPMetaDataHeySiriModelHash`, `UARPMetaDataHeySiriModelLocale`, `UARPMetaDataHeySiriModelRole`, `UARPMetaDataHeySiriModelSignature`, `UARPMetaDataHeySiriModelType`, `UARPMetaDataHostDeploymentRuleCountry`, `UARPMetaDataHostDeploymentRulePercentage`, `UARPMetaDataHostExcludedHwVersion`, `UARPMetaDataHostMinimumBatteryLevel`, `UARPMetaDataHostMinimumVersion_iOS`, `UARPMetaDataHostMinimumVersion_macOS`, `UARPMetaDataHostMinimumVersion_tvOS`, `UARPMetaDataHostMinimumVersion_visionOS`, `UARPMetaDataHostMinimumVersion_watchOS`, `UARPMetaDataHostPersonalizationRequired`, `UARPMetaDataHostTriggerBatteryLevel`, `UARPMetaDataInformationActiveFirmwareVersion`, `UARPMetaDataInformationAppleModelNumber`, `UARPMetaDataInformationAssetIdentifier`, `UARPMetaDataInformationFriendlyName`, `UARPMetaDataInformationHardwareFusing`, `UARPMetaDataInformationHardwareVersion`, `UARPMetaDataInformationManufacturerName`, `UARPMetaDataInformationModelName`, `UARPMetaDataInformationSerialNumber`, `UARPMetaDataInformationStagedFirmwareVersion`, `UARPMetaDataMappedAnalyticsAppleModelNumber`, `UARPMetaDataMappedAnalyticsEventID`, `UARPMetaDataPayloadCompressionAlgorithm`, `UARPMetaDataPersonalizationAllowFlashWrite`, `UARPMetaDataPersonalizationAllowUnsealedData`, `UARPMetaDataPersonalizationBoardID`, `UARPMetaDataPersonalizationBoardID64`, `UARPMetaDataPersonalizationBootNonce`, `UARPMetaDataPersonalizationCertificateEpoch`, `UARPMetaDataPersonalizationChipEpoch`, `UARPMetaDataPersonalizationChipID`, `UARPMetaDataPersonalizationChipRevision`, `UARPMetaDataPersonalizationDemotionProductionMode`, `UARPMetaDataPersonalizationDemotionSecurityMode`, `UARPMetaDataPersonalizationDigestListSize`, `UARPMetaDataPersonalizationECID`, `UARPMetaDataPersonalizationECIDData`, `UARPMetaDataPersonalizationEnableFutureFWVersion`, `UARPMetaDataPersonalizationEnableMixMatch`, `UARPMetaDataPersonalizationFTABGeneration`, `UARPMetaDataPersonalizationFTABPayload`, `UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride`, `UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride`, `UARPMetaDataPersonalizationFTABSubfileDigest`, `UARPMetaDataPersonalizationFTABSubfileDigestFilename`, `UARPMetaDataPersonalizationFTABSubfileEPRO`, `UARPMetaDataPersonalizationFTABSubfileESEC`, `UARPMetaDataPersonalizationFTABSubfileHashAlgorithm`, `UARPMetaDataPersonalizationFTABSubfileLongname`, `UARPMetaDataPersonalizationFTABSubfileTag`, `UARPMetaDataPersonalizationFTABSubfileTrusted`, `UARPMetaDataPersonalizationFdrRootCaDigest`, `UARPMetaDataPersonalizationLife`, `UARPMetaDataPersonalizationLogicalUnitNumber`, `UARPMetaDataPersonalizationManifestEpoch`, `UARPMetaDataPersonalizationManifestPrefix`, `UARPMetaDataPersonalizationManifestSuffix`, `UARPMetaDataPersonalizationMatchingData`, `UARPMetaDataPersonalizationMatchingDataPayloadTags`, `UARPMetaDataPersonalizationMatchingDataProductRevisionMax`, `UARPMetaDataPersonalizationMatchingDataProductRevisionMin`, `UARPMetaDataPersonalizationMoreRequestsToFollow`, `UARPMetaDataPersonalizationNonFTABPayload`, `UARPMetaDataPersonalizationNonFTABSubfileDigest`, `UARPMetaDataPersonalizationNonFTABSubfileEPRO`, `UARPMetaDataPersonalizationNonFTABSubfileESEC`, `UARPMetaDataPersonalizationNonFTABSubfileHashAlgorithm`, `UARPMetaDataPersonalizationNonFTABSubfileLongname`, `UARPMetaDataPersonalizationNonFTABSubfileTrusted`, `UARPMetaDataPersonalizationNonce`, `UARPMetaDataPersonalizationNonceHash`, `UARPMetaDataPersonalizationNonceSeed`, `UARPMetaDataPersonalizationPayloadTag`, `UARPMetaDataPersonalizationPrefixNeedsLogicalUnitNumber`, `UARPMetaDataPersonalizationProductType`, `UARPMetaDataPersonalizationProductionMode`, `UARPMetaDataPersonalizationProvisioning`, `UARPMetaDataPersonalizationRealHdcpKeyPresent`, `UARPMetaDataPersonalizationRequired`, `UARPMetaDataPersonalizationSecurityDomain`, `UARPMetaDataPersonalizationSecurityMode`, `UARPMetaDataPersonalizationSharedManifest`, `UARPMetaDataPersonalizationSoCLiveNonce`, `UARPMetaDataPersonalizationSuffixNeedsLogicalUnitNumber`, `UARPMetaDataPersonalizationSuperBinaryAssetID`, `UARPMetaDataPersonalizationSuperBinaryPayloadIndex`, `UARPMetaDataPersonalizationTicketNeedsLogicalUnitNumber`, `UARPMetaDataPersonalizationUIDMode`, `UARPMetaDataPersonalizationUseGlobalSigning`, `UARPMetaDataPersonalizedManifest`, `UARPMetaDataRequiredPersonalizationOption`, `UARPMetaDataVoiceAssistActiveModel`, `UARPMetaDataVoiceAssistCertificate`, `UARPMetaDataVoiceAssistDigest`, `UARPMetaDataVoiceAssistEngineVersion`, `UARPMetaDataVoiceAssistHash`, `UARPMetaDataVoiceAssistLocale`, `UARPMetaDataVoiceAssistRole`, `UARPMetaDataVoiceAssistSignature`, `UARPMetaDataVoiceAssistType`, `UARPRTKitFTAB`, `UARPRTKitFTABSubfile`, `UARPStatistics`, `UARPSuperBinaryLayer3`, `UARPSuperBinaryPayloadLayer3`, `UARPTatsuBootNonceLocation`, `UARPTatsuFTABProperties`, `UARPTatsuManifestLocation`, `UARPTatsuManifestProperties`, `UARPTatsuObjectProperties`, `UARPTatsuOptions`, `UARPTatsuTicket`

Protocols: `NSCoding`, `NSCopying`, `NSSecureCoding`, `UARPEndpointLayer3DelegateProtocol`, `UARPEndpointTransportRxProtocol`, `UARPEndpointTransportTxProtocol`, `UARPRestoreDeviceProtocol`, `UARPRestoreUpdaterDeviceProtocol`

## Strings (3,368)

First 2,500 of 3,368.
```
AppleTconUARPUpdater: In DFU mode - Query Personalization DFU Info
Version BVER File
Upload Denied  - Higher Version Staged
, 4CC: %@
-[UARPEndpointLayer3 solicitDynamicAsset:assetTag:]_block_invoke
Asset Decompression Failure
Endpoint Bulk Information Request Ack
%@-%@-%@
++++++++++++++++\n
Version Marketing BVER File
Payload MetaData
Voice Assist Type
Msg Type
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetReady:]_block_invoke
platform
IOGeneralInterest
YES
Host Trigger Battery Level
life=%@ \n
Ap Chip ID
Exceeded Packet Retry
Downstream Endpoint Reachable Ack
uarp
InfoArray
Needs SHA512
Key Name: %@
provisioning=%@ \n
%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p
%@
0.0.0.0
Ticket Name
payload.%lu
char3
AppleTconUARPUpdater: Query Info failed on TCON Device.
Personalization Tickets
Minimum visionOS Version
Board ID (64-bit)
-[UARPEndpointLayer3 directConfiguration]_block_invoke
Apple Info Chip Revision
%s (%s)
pcapfiles
blt2
HeySiri Model Role
ticketLongName=%@ \n
Prefix Needs LUN
AppleTconUARPUpdater: Overwriting Debug Register Access: %@
AppleTconUARPUpdater: Created UARPTconDevice
@%@
FirmwareData
Apple Info Asset Identifer
Host Personalization Required
realHdcpKeyPresent=%@ \n
Manifest Location
Needs Trusted
<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>
Voice Assist Signature
Object Properties
Higher Version Active
TCON Updater Device: Failed to create Layer2
enableMixMatch=%@ \n
Manufacturer Name
fwdl
Failed to create Tatsu Request
Personalization Matching Data Product Revision Maximum
Upload Abandoned  - Update In Progress
Payload Headers Length      : %lu\n
Payload - 4cc <%@> - Version <%@> - TLVs - %@
-[BanyanUARPUpdaterDevice layer3EndpointAssetPersonalizationComplete:asset:status:]
Key Name: %@, 4CC: %@, TLV 0x%08x
Personalization FTAB Payload Hash Algorithm
char4
No Resources
Personalization Ticket Needs Logical Unit Number
Percentage Rules
Measure Length
-[UARPSuperBinaryPayloadLayer3 composePayload]
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryPropertyListPayload:]
Staged Firmware Version Equal to Asset
-[UARPRTKitFTABSubfile getDataBlock:offset:]
chipID=%@ \n
Payload 4CC
-[UARPEndpointLayer3 notifyAssetOffered:]
Upload Abandoned  - Same Version Active
Asset Length                : %lu\n
Endpoint Component Discovery Request
FDR Context
AppleTconUARPUpdater: Setting Force DFU to each banyan %@
com.apple.uarp.endpoint.layer3
Required Personalization Option
Fdr Root Ca Digest
Unknown Payload
Invalid TLV
Personalization Enable Mix Match
Deployment Rules
FTAB %@:\n
Hardware Fusing
-[UARPSuperBinaryPayloadLayer3 personalizedData]
com.apple.banyan
Voice Assist Engine Version
Firmware (RX)
-[UARPSuperBinaryLayer3 expandPropertyListTLVs:]
Personalization Nonce
Nothing Staged
+++++++++++++++++++\n
Sync
ecidData=%@ \n
-[UARPEndpointLayer3 stageFirmwareSuperBinary:tssServerURL:]_block_invoke
AppleTconUARPUpdater:Security Domain is true, removing Provisioning for Tatsu.
Deployment Rule Percentage
Personalization Required
releaseVersion
Boot Nonce Location
Downstream Msg Payload Length
-[UARPEndpointLayer3 stopUARPLayer2Internal]
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackHardwareVersionResponse:]
Endpoint ID
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionary:]
Downstream Msg msgID
-[UARPEndpointLayer3 notifyLayer2RxFirmwareFullyStaged:]
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadData:offset:asset:]_block_invoke
Corrupt SuperBinary
Device Error
-[Tcon uarpMessageSendToDevice:]
Baobab,Ticket
FDR Data To Sign
, offset=%lu
securityDomain=%@ \n
\tBoot Nonce: 
-
com.apple.uarp.endpoint.layer3.tss
Invalid Offset
-[UARPSuperBinaryLayer3 setupTemporaryFolderForExpand]
Invalid Data Response
Asset Processing Notification Ack
Dynamic Asset PreProcessing Notification
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackManufacturerNameResponse:]
Duplicate Message ID
Unsupported Asset Tag
AppleTconUARPUpdater %s: TCON Manifest in Superbinary
Ticket Construction Failure
uarpMsgRecvDownstreamEndpointReachable
ffsc
-[UARPSuperBinaryLayer3 expandSuperBinaryPropertyList]
AppleTconUARPUpdater: removing Payload: %@
AppleTconUARPUpdater: Overriding Life Cycles on TSS Request.
AppleTconUARPUpdater: Successfully restored TCON.
UARP Tatsu Options: { \n
FTAB Boot Nonce
-[UARPSuperBinaryPayloadLayer3 generatePayloadHash:measureOffset:measureLength:]
Upstream Endpoint ID
tcon-registers
Personalization Payload Demotion Production Mode
Manifest Property
<Payload: %@, Version %@> 
Country Rules
Crash Analytics Core Name
FTAB Subfile
Getting Banyan fuse.
HeySiri Model Hash
Max Payload Length
SuperBinary MetaData Length : %lu\n
MetaData Corrupt
AppleTconUARPUpdater: Update Firmware with Dictionary.
ChipID
packetCapture
AppleTconUARPUpdater: Fusing SDOM Banyan Device
Apple Info HW Fusing Type
Apple Info ECID
Invalid Payload
Personalization Failure
HeySiri Model Engine Type
SuperBinary Payloads
MetaData
%02x
-[UARPSuperBinaryLayer3 addPayloadWith4cc:payloadVersion:payloadIndex:]
Payload Ordered Index
-[Tcon setFusingType:error:]
0x%08x
-[UARPRTKitFTAB expandFileTable:]
Upload Denied  - Cancelled Asset Tag
minorVersion
-[UARPSuperBinaryLayer3 expandSuperBinaryPlist]
-[UARPEndpointLayer3 discoverEndpointIDs]_block_invoke
ResponseTags
Personalization FTAB Payload Digest Filename
Property List Payload
com.apple.uarp.endpoint.packet.parser
Dynamic Asset PreProcessing Notification Ack
AppleTconUARPUpdater: Updater Querying Information.
Baobab,SecurityDomain
hardwareSpecific=%@ \n
Voice Assist Locale
Property List Version Path
Upload Abandoned  - Processing Error
Unknown Personalization Option
Asset No Bytes Remaining
Banyan already fused.
Expanding Asset failed
Personalization Production Mode
Firmware Version
-[UARPEndpointLayer3 checkPropertyQueryComplete]_block_invoke
Endpoint Bulk Information Response
Vendor Version String File
prefixNeedsLUN=%@ \n
, SHA-512 as %@
Vendor Specific
Minimum iOS Version
fdvc
AppleTconUARPUpdater: entering TCON Copy Firmware.
uidMode=%@ \n
Personalization Nonce Hash
Upload Abandoned  - Device Error
Asset Rescinded Notification
EPRO
productionMode=%@ \n
Until Month
IM4M
%lu
%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>
Needs SHA256
No Version Agreement
-[Tcon switchOperationalMode:]
Personalization FTAB Payload Tag
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryData:]
AppleTconUARPUpdater: No TCON Devices, returning nil.
Baobab,Provisioning
LZBitmap2
tmapdatabase
device/assets/personalization
product
AppleTconUARPUpdater: Banyan came back setting DFU, sleeping
AppleTconUARPUpdater: Finished DFU stage - sleeping.
-[BanyanUARPUpdaterDevice layer3EndpointPersonalizationNeeded:asset:]
Upload Denied  - Device Error
DownstreamEndpoint Endpoint ID
Manifest Properties
<%@: %llu>
-[UARPEndpointLayer3 notifyAssetPersonalizationComplete:status:]
uarpMsgRecvDownstreamEndpointUnreachableAck
Personalization Payload
protocolcontroller
Dynamic Asset Solicitation
%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@
AppleTconUARPUpdater: Query Tags from TCON Device.
psf2
Failed to get personalization info from Asset
-[Tcon setRestoreUpdaterDelegate:]_block_invoke
Upload Denied  - Better Transport
Cancelled - No Network
Property Value
-[UARPEndpointLayer3 notifyAssetPersonalizationNeeded:]
Asset Staging Still In Progress
-[UARPEndpointLayer3 notifyEndpointAssetMetaDataComplete:]
-[UARPEndpointLayer3 handleProtocolVersionSelected:]
Apple Info Manifest Prefix
Endpoint Discovery Response
Life
FDR Signature
FTAB Properties
Apple Info Logical Unit Number
AppleTconUARPUpdater: Reachable Devices.
-[UARPSuperBinaryPayloadLayer3 initWithPayload4cc:payloadVersion:payloadIndex:baseURL:]
In Progress
Error: Query Personalization Info Input Dictionary is nil
Personalization Matching Data Payload Tags
HeySiri Model Signature
Mapped Analytics Event ID
, SHA-256 as %@
\tManifest: (Offset=0x%08x) %@\n
SuperBinary Firmware Version
SHA-256
UARPLayer3UtilsCleanFileHandleForWriting
-[UARPSuperBinaryLayer3 getDataRangeFromURL:]
AppleTconUARPUpdater %s: TCON asset staging complete with success
-[BanyanUARPUpdaterDevice stageFirmwareWithDictionary:error:]
Voice Assist Hash
Product Type
protocolaccessory
AppleTconUARPUpdater: TCON Asset failed to stage with failure: %@
Personalization FTAB Payload Production Mode Host Override
UARPAssetLayer2CallbacksAssetMetaDataTLV
Personalization ECID Data
yyyy-MM-dd
Manifest Destination
-[UARPEndpointLayer3 nextLayer3Payload:]_block_invoke
-[UARPSuperBinaryPayloadLayer3 getDataRangeFromURL:]
FDR Parameter Name
Upload Abandoned  - Low Battery
Downstream Endpoint Reachable
AppleTconUARPUpdater: Fusing PROD Banyan Device
AppleTconUARPUpdater Error: TCON nil Security Mode
HeySiri Model Type
-[UARPSuperBinaryPayloadLayer3 cachePayloadData]
\tSubfiles: (Offset=0x%08zx) %zu\n
Idle
.
Personalization Chip Epoch
manifestSuffix=%@ \n
of 4CC: %@
Unknown Information Option
FusePROD
Payload Certificate
updv
Deployment Rule Country
Personalization Life
ECID
-[UARPEndpointLayer3 processRespondedComponentInfoQueries:tlvs:]
AppleTconUARPUpdater: Cannot Fuse PROD, SDOM is not fused.
AppleTconUARPUpdater: Building Excluded Payloads
com.apple.banyan.uarp
-[UARPEndpointLayer3 notifyAssetSolicited:]
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackDiscoveredEndpointIDs:]_block_invoke
Asset Id Unknown
AppleTconUARPUpdater: entering TCON Get Tags.
Compressed Headers
\xf0\xb1
-[UARPEndpointLayer3 notifyDownstreamEndpointUnreachable:]
Error: Input Dictionary is nil \n
Unable to find Manifest Data as TLV on superbinary
Baobab,Life
FDR Data
device/assets/logs
,%@
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackFriendlyNameResponse:]
AppleTconUARPUpdater: TCON Manager is nil, returning.
Personalization Payload Trusted
-[UARPRTKitFTAB composeFTAB]
%c%c
Product Group
-[UARPEndpointLayer3 notifyEndpointPayloadMetaDataComplete:payload:]
com.apple.uarp.packetcapture
streaming
-[BanyanUARPUpdaterDevice layer3EndpointReachable:]
Until Year
Personalization Digest List Size
Property Name
, ESEC %@
Invalid Argument
fdrg
Manifest Epoch
Components
Apple Info Production Mode
fbsr
AppleTconUARPUpdater: Saving PR Doc options.
Personalization FTAB Payload
SuperBinary MetaData
Minimum tvOS Version
Don't fuse - Banyan in DFU mode.
AppleTconUARPUpdater: successfully copied firmware.
, SHA-384 as %@
-[UARPSuperBinaryLayer3 updateIncomingAssetProperties:]
Priority Activity
AllAMN.tmap
<Type = 0x%08x, Length = 0x%08x>
Data Request
AppleTconUARPUpdater: Setting SkipPreCalData Settings: %@
DebugRegisterAccess
>
Manifest as MetaData 
endpoint
%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>
Invalid Asset Tag
v8@?0
blt1
Trusted
queryInfo
Compose Payload Hash Algorithm
SuperBinary Version         : %lu.%lu.%lu.%lu\n
Apple Info Suffix Needs Logical Unit Number
Invalid Length
AppleTconUARPUpdater: Overwriting Life Cycles: %@
Failed to set TCON into DFU Mode
Apple Info Ap Board ID
Payload MetaData Offset : %lu\n
Unknown Controller
Buffer Overflow
Same Version Active
Until Day
Not Auth Listed
Protocol Version
Msg Payload Length
AppleTconUARPUpdater: Overwriting Fusing PROD: %@
Payload Hash Algorithm
Model Name
MetaData Overflow
queryPersonalizationInfo
Upload Denied  - Update In Progress
Upload Abandoned  - Priority Activity
-[UARPEndpointLayer3 configureEndpointLayer2Tags]
-[UARPEndpointLayer3 denyAsset:denyReason:]_block_invoke
tconUARPManager
AppleTconUARPUpdater: Building superbinary data failed with %@
superbinaryAsset
Manifest Locations
Apple Info ECID Data
TCON already in DFU Mode
-[Tcon dfuStage:]
Host Minimum Battery Level
-[UARPSuperBinaryPayloadLayer3 decompressPayload]
\tSubfiles:\n
Upload Denied  - MetaData Overflow
Key Name
Board ID (32-bit)
Invalid Data Request Offset
Buffer Would Overflow
Serial Number
Compose Measured Payloads
Downstream Endpoint Unreachable
fwrg
TCON is not staging DFU Firmware
Upload Denied  - Low Battery
ftabSubfile
Manifest Prefix
,%lu
Endpoint Bulk Information Request
psf0
Personalization Payload Tag
Needs SHA384
Apple Info Personalization Life
AppleTconUARPUpdater: entering TCON create.
Object Property: %@
Upload Complete (Reboot Required)
-[UARPEndpointLayer3 personalizeFirmwareSuperBinaryInternal:tssServerURL:]
Unknown Asset
ftpl
fwlc
Upload Denied  - Priority Activity
Upload Complete
Duplicate Controller
Processing Incomplete
AppleTconUARPUpdater: Excluding Calibration Data
Personalization Chip ID
Payload Filepath
Endpoint UUID
Creating Asset failed
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryTLVs:]
Controller
SocLiveNonce
Chip Revision
-[UARPEndpointLayer3 acceptLayer3Payload:]_block_invoke
Mismatch UUID
<unknown>
IS
Ap Board ID
Real HDCP Key Present
Unknown Failure
AppleTconUARPUpdater %s: TCON asset staging complete
btfw
Successfully DFU Staged TCON Firmware
Upload Abandoned  - MetaData Overflow
AppleTCONControl
, Value %@
, FTAB Subfile: %@
Country
Property List Path
Invalid
Logical Unit Number
Unsupported Hardware Revision
-[BanyanUARPUpdaterDevice craftTatsuRequest:]
Version Simple BVER File
metrics
Sending Firmware Data for DFU Stage
Personalization Provisioning
Personalization Board ID
Upstream Endpoint UUID
-[UARPEndpointLayer3 noFirmwareAvailable]_block_invoke
-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:tlvs:]
Apple Info Nonce
Endpoint Bulk Information Response Ack
-[Tcon onTconIrq]
nonceSeed=%@ \n
Apply Staged Assets Request
AppleTconUARPUpdater: In DFU mode - Returning empty dictionary
Percentage Limit
Asset Not Found
, EPRO %@
Payload Version         : %lu.%lu.%lu.%lu\n
Unsupported
AppleTconUARPUpdater: Failed to fuse SDOM for TCON Device
<%@: Algorithm %u, Actual Offset %u, Compressed Length %u, Uncompressed Length %u>
AssetIdentifier
Downstream Endpoint Message Ack
Upload Abandoned  - Personalization Failure
UARP.LAYER2 <%s> Cannot find downstream endpoint
Invalid Object
Downstream Endpoint Discovery
-[Tcon currentOperationalMode]
Personalization Payload Effective Production Mode
-[UARPSuperBinaryLayer3 expandPayloadWithHeaderAsData:payloadIndex:payload4cc:payloadVersion:payloadMetaData:]
FTAB Generation
-[UARPEndpointLayer3 notifyApplyStagedAssets]
Invalid Data Response Length
blt3
Personalization Logical Unit Number
assets
Upload Denied
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackApplyStagedAssets]
uarpMsgRecvDownstreamEndpointMessage
success
Ignore Version
Personalization ECID
Hw Fusing Type
Payload Hash
PLACEHOLDER
----------------------------\n
Apple Info Ap Production Mode
Unknown Accessory
bfwc
PersonalizationInfo
Urgent Update
SuperBinary: Format Version: %lu, Asset Version %@\n
Apple Info Apple Model Number
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetAllHeadersAndMetaDataComplete:]_block_invoke
AppleTconUARPUpdater: Failed to stage firmware with Data for TCON Device
UID Mode
Personalization Matching Data Product Revision Minimum
Payload Compression Algorithm
-[UARPSuperBinaryPayloadLayer3 hashPayload]
ForceDFU
MetaData Hash Algorithm
Upload Abandoned  - Same Version Staged
|
-[UARPEndpointLayer3 notifyPayloadReady:payload:]
<%@:
manifestPrefix=%@ \n
Not Needed
Payload Window Length
Digest
MetaData Hash
Security Mode
-[UARPSuperBinaryPayloadLayer3 preparePersonalizedURL]
AppleTconUARPUpdater Error: TCON nil ECID Data
Personalization Manifest Epoch
Upload Denied  - Personalization Failure
-[UARPEndpointLayer3 applyStagedAssets]_block_invoke
transmitqueue
Baobab,DebugRegisterAccess
Personalization Security Domain
\tGeneration: 0x%08x\n
AppleTconUARPUpdater %s: TCON personalization info queries complete
\tNum Subfiles: %d\n
Production Mode
-[UARPEndpointLayer3 notifyRxFirmwareFullyStaged:]
Mismatch Data Offset
AppleTconUARPUpdater: Creating UARPTconDevice.
Personalization Prefix Needs Logical Unit Number
Minimum Required Version
Use Global Signing
HeySiri Model Engine Version
Asset Invalid Compression
Downstream Endpoint Unreachable Ack
AppleTconUARPUpdater: Update Device Firmware with Data
-[UARPEndpointLayer3 rescindAssets]_block_invoke
HeySiri Model Digest
<%@: %@ until %@>
AppleTconUARPUpdater: Query Info from TCON Device.
Setting Banyan fusing type failed.
Chip Epoch
-[UARPEndpointLayer3 queryOutstandingEndpointIDProperties:]
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackStagedFirmwareVersionResponse:]
No MetaData
Invalid EndpointID
Better Transport
performNextStage
Personalization FTAB Payload Longname
Allow Flash Write
Personalization SuperBinary AssetID
Header Length               : %lu\n
HSML
Information Response
HeySiri Model Locale
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetProcessingCompletedAck:]_block_invoke
manifestEpoch=%@ \n
Security Domain
Unknown
Additional %@:\n
Enable Mix Match
Data Transfer Paused
AppleTconUARPUpdater: Banyan in DFU Mode, taking it out, isDone = False.
logicalUnitNumber=%@ \n
Success
Flash Section Length
-[UARPSuperBinaryPayloadLayer3 setPayloadURL:]
Unknown Downstream Endpoint
Successfully fused
Upload Abandoned  - Better Transport
Measure Offset
UARPSuperBinaryProcessMetaData
Duplicate Accessory
Invalid Payload Header
Creating New Asset failed
ProductionMode
LifeCycle
FDR Parameter Data
Personalization Security Mode
AppleTconUARPUpdater: PRDocOptions set:\n FuseSDOM: %@,\n FusePROD: %@,\n DebugRegisterAccess: %@,\n ForceDFU: %@,\n LifeCycles: %@,\n SkipPreCalData: %@
SHA-512
Apple Info Enable Mix Match
Error: TSS Request is nil for TCON \n
Payload Compression ChunkSize
Server Unreachable
Personalization Payload Longname
Upload Denied  - Same Asset Tag In Progress
Manifest as FTAB Suffix of 4CC: %@
AppleTconUARPUpdater: Failed to fuse PROD for TCON Device
Allow Unsealed Data
Dynamic Asset (TX)
-[UARPEndpointLayer3 processOutstandingComponentInfoQueries:infoProperties:]
HigherVersion
BuildIdentityTags
ftabSuffix
Asset Data Transfer Notification
com.apple.uarp.layer3
ECID=%@ \n
Unknown Data Transfer State
\xf0\xf0\xf0\xf0a
ECID Data
assert
-[UARPEndpointLayer3 sendMessageUpstream:fromDownstreamID:]_block_invoke
-[Tcon init]
device/assets/analytics
device/assets/voiceassist
AppleTconUARPUpdater: Failed to query tags from TCON
bst0
BoardID
SecurityDomain
Voice Assist Role
Payload Signature
-[UARPEndpointLayer3 selectLayer3Payload:payloadIndex:]_block_invoke
AppleTconUARPUpdater: Failed to apply firmware a for TCON Device
\n
psf1
Hardware Version
Product Number
-[UARPEndpointLayer3 downstreamEndpointRemove:]_block_invoke
Apple Info Ticket Long Name
liveNonce=%@ \n
-[UARPEndpointLayer3 notifyEndpointPayloadDataComplete:payload:]
Error: Firmware Data is corrupt\n
AppleTconUARPUpdater: Overwriting Fusing SDOM: %@
-[Tcon getFusingType:error:]
Asset Rescinded Notification Ack
%s
\t\t%@
Asset Corrupt
None
Endpoint Component Discovery Response
Personalization FTAB Payload Security Mode Host Override
%@:\n
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackSendMessage:length:]_block_invoke
AppleTconUARPUpdater: Query Tags from Device
SHA-384
-[UARPEndpointLayer3 personalizeFirmwareAssetComplete:]_block_invoke
-[UARPEndpointLayer3 notifyRxDynamicAssetFullyStaged:]
%s-%@-%@.pcap
Personalization FTAB Payload Digest
Upload Denied  - Processing Error
2
Asset Processing Notification
No Firmware Update Available Ack
Error: Missing Firmware Data from inputOptions\n
Personalization FTAB Payload Trusted
boardID32=%@ \n
Days From Compose
Personalized Manifest
Firmware Variant
Chip ID
SuperBinary Header\n
https://gs.apple.com:443
Upload Abandoned
-[UARPSuperBinaryLayer3 expandPropertyListPayloads:]
UARPEndpointLayer3: %@
IS NOT
-[UARPEndpointLayer3 notifyEndpointPayloadData:payload:offset:payloadData:]
Personalization Payload Digest
Subfile: type=%@, length=%lu
, hash=%@
Apple Info Board ID
Unknown Message Type
device/assets/heysiri
-[UARPEndpointLayer3 notifyEndpointRemoteNotResponding]
PROD
-[UARPSuperBinaryPayloadLayer3 initWithPayloadURL:payloadTlvs:payload4cc:payloadVersion:payloadIndex:]
MetaData Type Not Found
tcon-api
<%@: %u>
Personalization FTAB Payload Security Mode
Personalization Board ID (64 bits)
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadReady:]_block_invoke
Low Battery
downstream
ESEC
Personalization SuperBinary Payload Index
<%@: %lu until %@>
Personalization Payload Demotion Security Mode
Minimum watchOS Version
-[UARPEndpointLayer3 downstreamEndpointUnreachable:downstreamEndpointID:]_block_invoke
-[UARPEndpointLayer3 craftTatsuRequests:]
Payload Header\n
boardID64=%@ \n
Voice Assist Certificate
, Trusted %@
uarpPlatformEndpointRecvMessage
char1
-[UARPRTKitFTAB getDataBlock:offset:]
Minimum macOS Version
Apple Info Ap Chip ID
Apple Model Number
Requires Personalization
Apple Info Hardware Specific
Staged Firmware Version
Mapped Analytics Apple Model Number
-[UARPRTKitFTABSubfile getDataRangeFromURL:]
Manifest as MetaData of %@
AppleTconUARPUpdater: Updater update firmware with Dictionary.
AppleTconUARPUpdater Error: TCON nil HW Fusing Type
-[UARPEndpointLayer3 processOutstandingEndpointInfoQueries:infoProperties:]
Same Version Staged
-[Tcon resetDevice]
-[UARPRTKitFTAB getDataRangeFromURL:]
SuperBinary Format Version
+++++++++++++++++\n
-[UARPEndpointLayer3 downstreamEndpointAdd:]_block_invoke
Crash Analytics Apple Model Number
Invalid Data Request Type
Header Length           : %lu\n
%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Asset Transfer Complete
AppleTconUARPUpdater: Creating Device.
FTAB:\n
-[UARPEndpointLayer3 offerDynamicAsset:fourCC:]_block_invoke
Staged Firmware Version Greater than Asset
Version Discovery Request
Dynamic Asset (RX)
-[UARPEndpointLayer3 uarpRouteRecvMessageToDownstreamEndpoint:downstreamEndpointID:]_block_invoke
Apple Info Requires Personalization
AppleTconUARPUpdater: entering TCON Create Request.
tconuarpqueue
Personalization Matching Data
-[UARPSuperBinaryPayloadLayer3 initWithPayloadData:payloadMetaData:payload4cc:payloadVersion:payloadIndex:]
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
Crash Analytics Test Mode
Request Failure
-[UARPSuperBinaryLayer3 getDataBlock:offset:]
Cancelled Asset Tag
-[Tcon dfuInfo:]
ROOT
Needs EPRO
Apple Info Security Domain
Payload Tag             : %c%c%c%c\n
FuseSDOM
\t
Compose MetaData Hash Algorithm
Upload Abandoned  - Same Asset Tag In Progress
%c%c%c%c
Error: Unable to validate Firmware for TCON\n
Upload Abandoned  - Higher Version Active
Downstream Msg Name
DownstreamEndpoint Endpoint UUID
-[UARPSuperBinaryPayloadLayer3 composePersonalizedFTAB]
Asset Available Notification
Expanding New Asset failed
PMAP
bst1
sysdiagnose
superbinary.uarp
-[UARPEndpointLayer3 notifyTxDynamicAssetFullyStaged:]
-[UARPSuperBinaryLayer3 expandPayloadWithHeader:payloadIndex:]
Nonce
Baobab,ProductionMode
Personalization More Requests to Follow
:
BoardId
Payload Data Offset     : %lu\n
Mid Upload
Accessory
%s: Tatsu Ticket %@
StagedFirmwareVersion
<%@: %@>
4CC: %@, Property 0x%08x
Msg Name
UARPAssetLayer2CallbacksPayloadMetaDataTLV
Ap Security Mode
-[UARPEndpointLayer3 startUARPLayer2Internal]
uarpMsgRecvDownstreamEndpointUnreachable
Invalid Message
Property List Digest Path
-[UARPEndpointLayer3 acceptLayer3Asset:]_block_invoke
-[UARPEndpointLayer3 uarpMessageRecvFromTransport:]_block_invoke
Apple Info Personalization Nonce Seed
Payload Data Length     : %lu\n
Apply Staged Assets Response
device/assets/crash
Ap Production Mode
Processing Error
SDOM
NO
Personalization Real Hdcp Key Present
device/assets/mappedanalytics
AppleTconUARPUpdater: Creating TCON Updater Manager.
Payload Identifier
Personalization Manifest Suffix
Suffix Needs LUN
-[UARPSuperBinaryLayer3 expandPayloadWithHeaderAsURL:payloadIndex:payload4cc:payloadVersion:payloadMetaData:]
Apple Info Security Mode
Apple Info Prefix Needs Logical Unit Number
Endpoint Discovery Request
AppleTconUARPUpdater:Security Domain is false, setting Provisioning.
Msg Downstream ID
-[UARPEndpointLayer3 notifyAssetStagingProgress:bytesTransferred:assetLength:]
-[UARPSuperBinaryPayloadLayer3 setDataBlockToData:offset:payloadData:]
Invalid Data Request Length
enableFutureFWVersion=%@ \n
Personalization FTAB Payload Production Mode
-[UARPEndpointLayer3 notifyEndpointAppliedStagedAssets:]
Invalid Function Pointer
Excluded Hardware Version
buildVersion
Payload Headers Offset      : %lu\n
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetRescind:]
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
Asset Available Notification Ack
Personalization SoC Live Nonce
Hardware Specific
Error decompressing buffer for payload
AppleTconUARPUpdater: Updater Querying Personalization Information.
fvgl
Manifest Suffix
-[UARPSuperBinaryLayer3 setupTemporaryFolder]
fgvl
HeySiri Model Certificate
Attempt AppleConnect
-[UARPEndpointLayer3(Layer2VendorCallbacks) layer2CallbackHwFusingTypeResponse:]
endpointDatabase
Apple Info Chip ID
Apple Info Personalization Manifest Epoch
compressedPayload.%lu
Payload Identifier String
Upload Abandoned  - Higher Version
Ticket LongName
Personalization Payload Hash Algorithm
-[UARPEndpointLayer3 sendSyncToPeer]_block_invoke
Out Of Order Message ID
Dynamic Asset Solicitation Ack
UNKNOWN
-[UARPSuperBinaryLayer3 expandPropertyListPayload:payloadIndex:]
Unable to find Bootloader or Bootloader Config on Payloads
nonce=%@ \n
Apple Info FTAB Generation
Unsupported Message Type
-[BanyanUARPUpdaterDevice layer3EndpointAppliedStagedAssets:layer3Flags:]
SkipPreCalData
Version File
suffixNeedsLUN=%@ \n
Payload Expand Filename
Payload Long Name
In Use
%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@
AppleTconUARPUpdater: Building personalized SuperBinary Asset for TCON.
Manifest as FTAB Subfile of 4CC: %@
-[UARPSuperBinaryLayer3 addTatsuTicketManifest:ticket:manifestLocation:payload:]
im4m
SuperBinary MetaData Offset : %lu\n
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryKeyValuePayload]
}
-[UARPEndpointLayer3 notifyEndpointRescindedStagedAssets]
AppleTconUARPUpdater: In DFU mode - Query DFU Info (noop)
EcidData
Failure
Apple Info Real Hdcp Key Present
Asset In Flight
Data Response
Apple Info Personalization Manifest Suffix
Active Firmware Version Equal to Asset
chipRevision=%@ \n
A
Personalization Payload Effective Security Mode
-[BanyanUARPUpdaterDevice layer3EndpointAssetFullyStaged:txFirmwareAsset:]
Firmware (TX)
uarpTransmitEntryIsValidToSend
Nonce Seed
ftabGeneration=%@ \n
cachedassets
Upload Denied  - Same Version Staged
, Static Value %@
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackModelNameResponse:]
LZBitmapFast2
In Flight
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackSerialNumberResponse:]
Active Firmware Version Greater than Asset
chipEpoch=%@ \n
build
Apple Info Personalization Nonce Hash
Mismatch Personalization Option
Information Request
Upload Abandoned  - Cancelled Asset Tag
Apple Info Chip Epoch
Trying to set TCON into DFU Mode
PLST
Format Version              : %lu\n
-[UARPEndpointLayer3 processRespondedEndpointInfoQueries:tlvs:]
FirmwareVersion
Upload Denied  - Higher Version Active
%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Asset Data Paused
Asset Data Transfer Notification Ack
HWFusingType
Asset Identifier
Compose Measured Payloads (Non-FTAB)
Attempt Auth Listed
AppleTconUARPUpdater Error: TCON nil Chip ID
SecurityMode
Personalization Chip Revision
%04ld-%02ld-%02ld
%@\n
-[UARPSuperBinaryLayer3 prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:]
Apple Info Ap Security Mode
AppleTconUARPUpdater: Transport is nil, returning nil.
AppleTconUARPUpdater: Banyan came back from applying, sleeping
sysdiagnose_approved
Downstream Endpoint Message
com.apple.uarp.embedded
Upload Denied  - Same Version Active
-[UARPSuperBinaryPayloadLayer3 generateHash:ftabSubfile:]
Options
securityMode=%@ \n
-[UARPEndpointLayer3 assetFullyStaged:status:]_block_invoke
HeySiri Model Active Model
Payload Version
-[UARPSuperBinaryLayer3 initWithLayer2Context:assetTag:tmpFolderPath:]
Downstream Endpoint Discovery Ack
AppleTconUARPUpdater: Starting UARP Devices for TCON
bst2
\tValid: %u\n
majorVersion
Live Nonce
-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]_block_invoke
Invalid Asset Type
Getting Banyan fusing type failed.
Crafting Tatsu Request
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackUnsolicitedDynamicAssetOffered:assetTag:]_block_invoke
-[UARPEndpointLayer3(Layer2VendorCallbacks) layer2CallbackAppleModelNumberResponse:]
-[UARPSuperBinaryPayloadLayer3 compressPayload]
Active Firmware Version
No Tatsu Measurements
Downstream Msg Type
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc31
-[UARPSuperBinaryPayloadLayer3 getDataBlock:offset:]
No Firmware Update Available
AppleTconUARPUpdater Error: TCON nil Board ID
AppleTconUARPUpdater %s: TCON asset apply complete with flags:%ld
-[Tcon uarpMessageSendToTransport:]
Incompatible Protocol Version
Upload Denied  - Unsupported Asset Tag
Cancelled
Host Controller
Certificate Epoch
Personalization Manifest Prefix
-[UARPSuperBinaryLayer3 expandSuperBinaryHeader]
%s: Tatsu Request for ticket %@
Component Tag
-[UARPSuperBinaryLayer3 expandPayloadHeadersAndMetaData:offset:]
-[UARPEndpointLayer3 notifyEndpointReachable]
AppleTconUARPUpdater %s: TCON info queries complete
Uncompressed Payload Length
Friendly Name
-[UARPRTKitFTAB appendDataBlockToURL:]
%@,Ticket
-[UARPEndpointLayer3 queryOutstandingEndpointIDComponentProperties:]
Invalid Message Length
Enable Future FW Version
Voice Assist Active Model
0x
Apple Info Personalization Provisioning
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackRescindAllAssets]
AppleTconUARPUpdater: Setting Debug Register Access in TSS Request.
Voice Assist Digest
Invalid Super Binary Header
Upload Denied  - Higher Version
%lu.%lu.%lu.%lu
i
-[UARPEndpointLayer3 personalizeFirmwareSuperBinary:tssServerURL:]_block_invoke
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackActiveFirmwareVersionResponse:]
/
AppleTconUARPUpdater: Overwriting SkipPreCalData: %@
FTAB Payload
Upload Abandoned  - Unsupported Asset Tag
Needs Restart
Provisioning
Apple Info SoC Live Nonce
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadMetaDataComplete:]_block_invoke
char2
RealHdcpKeyPresent
Baobab,TCON
v32@?0@\"NSString\"8@16^B24
Needs ESEC
-[UARPEndpointLayer3 notifyTxFirmwareFullyStaged:]
Payload MetaData Length : %lu\n
-[UARPSuperBinaryPayloadLayer3 setDataBlockToURL:offset:url:]
Invalid Data Transfer Notification
Msg msgID
memory
Version Discovery Response
Shared Manifest
%lu-%lu-%lu
Upload Abandoned  - Higher Version Staged
%02ld-%02ld-%02ld
personalizedPayload.%lu
%s: completed firmware authentication %#x boot ROM %#x (%#x)
%s: Added Personalizing Asset - %@
Endpoint %@: Solicited Dynamic Asset Offered %@
Asset MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s: offset %lu does not equal %lu 
%s: expandPayloadWithHeader failed
%s: On Banyan IRQ %#llx [%#llx] (%#x)
%s: Requested offset (%d) longer than ftab length %d
%s: createFileAtPath failed %@ 
%s: created file at path  %@ 
%s: SuperBinary Payload index %lu value is not an NSArray
%s: Outstanding Info Property %@ (%@)for endpoint component %@ 
%s: uarpPlatformEndpointDiscoverEndpointIDs() failed with status is %s
%s: Tatsu Request for ticket %@
%s: Apply Staged Assets - Nothing Staged
Endpoint %@: Solicit Dynamic Asset %@
%s: SuperBinary payload file is not present; %@
%s: composing personalized ftab failed
%s: payload URL is nil for payload index %lu
%s: Interrupt status was %#llx
%s: Failed to write DTCM (%#x)
%s: Endpoint %@, Role %s. Protocol Version Selected (%lu), previously (%lu).
%s: could not instantiate UARPSuperBinaryLayer3 for tag %@ on endpoint %@
%s: Could not create TLV for uncompressedLength
%s: SuperBinary payload version is not a string
%s: Unmask UARP interrupt (%#x)
%s: Added Personalized Asset - %@
%s: uarpPlatformEndpointBulkInfoResponseAddTLV() failed, status is %s
uarpPlatformEndpointRecvMessage(length=%lu) failed; <%u> %s
%s: Endpoint %@, Cancelling staged assets
%s: Rescind Staged Assets. UUID of %@
%s: Someone called me and I'm deprecated, with %@
%s: Failed to connect to AppleTCONControl
%s: seekToOffset:error: failed with %@
%s: _data is nil
%s: SuperBinary payload 4cc is not a string
%s: Responded Bulk Info Property for endpoint configuration: %@ (%@)
%s: uarpPlatformEndpointAssetFullyStaged() failed; <%u> %s
Endpoint Packet Capture at %@
%s: Failed to write bootloader length (%#x)
Failed to add remote endpoint, status is %s
Stage Asset %@. UUID of %@
%s: get data block failed for offset %lu, 
%s: cannot read range (offset %lu, length %lu) from %@, error %@
----------
%s: uarpPlatformConfigureEndpointIDs() failed, status is %s
%s: uarpPlatformEndpointBulkInfoQuery() failed, status is %s
%s: Endpoint %@: Endpoint ID = %d, not saving %@
%s: Could not create hash tlv (%@) for payload %@
%s: bootloader length itcm: %u dtcm: %u
%s: starting firmware authentication
%s: createDirectoryAtPath %@ failed %@ 
%s: composing payload failed
%s: SuperBinary contains no plist
%s: Outstanding Preflight Info Property %@ (%@) for endpoint component %@ 
Asset Processing Notification <%@> for SuperBinary <%@> for Endpoint <%@>
%s: Someone called me and I'm deprecated
%s: fileHandleForWritingToURL %@ failed %@ 
%s: uarpPlatformEndpointBulkInfoResponse() failed, responseStatus is %s
%s: Requested offset (%d) longer than subfile length %d
%s: removeItemAtPath %@ failed %@ 
%s: Send message from downstream endpoint id %lu
%s: Query Info Properties for endpoint component %@ 
%s: Error querying asset version -> <%u> %s
%s: invalid payload header size; expected %lu, but got %u
%s: direct endpoint, no need for downstream routing
%s: Query Bulk Info Property for endpoint configuration: %@ (%@)
uarpMessageAdjustedForEndpointID() failed; <%u> %s
Payload Index <%lu> MetaData Processing Error for SuperBinary <%@> for Endpoint <%@>
All Headers And MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s: writeRegister %#x (%#x)
%s: Bootloader too small for ITCM and DTCM
%s: Notify Endpoint Reachable, Role %s, %@
%s: uarpPlatformEndpointAssetAbandon() failed; <%u> %s
%s: Could not create hash algorithm tlv (%@) for payload %@
%s: Could find subfile %@ for %@
%s: failed to append block data at compressed offset %lu
%s: SuperBinary payload filename is not a string
Failed to query Apple info property %u, status is %s
%s: Accept Layer 3 Payload
Fully Staged for SuperBinary <%@> for Endpoint <%@>
%s: protocol version %u, cannot do downstream routing
Asset TLV %@ for SuperBinary <%@> for Endpoint <%@>
NOT IMPLEMENTED YET - Asset Pre Processing Notification for SuperBinary <%@> for Endpoint <%@>
%s: Failed to create register IOAVDisplayMemory
%s: copied %@ to %@
%s: not enough data to process a TLV's value
%s: Full Temp Folder is %@
%s: cannot find endpoint for tatsu ticket; %@
%s: RX Dynamic Asset Processing Complete (%@). UUID of %@
%s: metadata length is %lu
%s: Adding downstream endpoint id 0x%04x
Asset MetaData Processing Error for SuperBinary <%@> for Endpoint <%@>
%s: _superbinaryURLis nil
Failed to init local endpoint
%s: asset does not need host personalization %@, UUID of %@
Endpoint %@: Apply Staged Assets Response, ID = %ld
%s: Could not generate hash (%@) for payload %@
%s: Error querying number of payloads -> <%u> %s
%s: Unhandled processing status is %lu. UUID of %@; assume corrupt
%s: ftabSubfile is nil
%s: Failed to deompress buffer, status is %s
%s: NEW UARP delegate set
%s: Missing bootloader asset
%s: Block Compression Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
%s: Unexpected type for manifest asset
%s: Unable to retrieve BNCH (%#x)
%s: Missing bootloader config asset
%s: Unexpected type for bootloader config asset
%s: Failed to write boot block (%#x)
%s: processPersonalizationTickets: failed to process
%s: configuration id is %lu
%s: %c%c%c%c has zero outstanding info properties
%s: Unable to determine fusing (%#x)
%s: Can only provide %d bytes from offset %d of subfile %@
%s: Can only provide %d bytes from offset %d of ftab %@
Failed to init local endpoint, status is %s
%s: uarpPlatformEndpointAssetCorrupt() failed; <%u> %s
%s: Active Firmware Verison is %@. Staged Firmware Version is %@. UUID of %@
%s: SuperBinary payload cannot be compressed; %@
%s: closeAndReturnError failed %@ 
%s: Apply staged assets
uarpPlatformEndpointRecvMessage() failed; Type = %s, payload length = %lu, msd id = %lu
NOT IMPLEMENTED YET - Asset Rescinded for SuperBinary <%@> for Endpoint <%@>
%s: Invalid Fusing Type
%s: writeData:error: failed with %@
Failed to add downstream endpoint id = %lu, status is %s
%s: %c%c%c%c has %d outstanding info properties
%s: %@, %@ supported
%s: hash of payload %@ adjust length to %lu and ending offset %lu 
%s: Unexpected key TLV type %@
%s: Unexpected manifest length %lu
%s: Failed to modify date to now for file %@; error %@
%s: SuperBinary Header length is unexpected %d
%s: Personalize Asset %@. UUID of %@
%s: Error querying payload metadata -> <%u> %s
%s: Failed to craft tatsu requests, %@
%s: Error calling uarpPlatformEndpointPayloadRequestData: -> <%u> %s
%s: Unable to retrieve ECID (%#x)
%s: Failed to read boot status (%#x)
%s: Phase 1: Wrong FTAB Tag Size
%s: File name for asset is %@
Offer Dynamic Asset %@. UUID of %@
Failed to send message to downstream endpoint id %lu, status is %s
Endpoint %@: Downstream Endpoint Reachable, ID = %u, TLVs = %@
Payload Index <%lu> MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s: cannot open %@ for reading, error %@
%s: metadata padded length is %lu
%s: uarpPlatformEndpointSendSyncMsg() failed, status is %s
%s: failed to prepare firmware <%s> to endpoint %@
NOT IMPLEMENTED YET - Asset Orphan for SuperBinary <%@> for Endpoint <%@>
%s: could not expand FTAB for payload %@, index %lu
%s: not enough data to process a TLV's header
%s: Requested offset (%d) longer than asset length %d
%s: cannot copy %@ to %@, error %@
%s: SuperBinary Payload index %lu, file is missing; FAIL
%s: endpoint base has zero outstanding info properties
Payload Index <%lu> Data Complete for SuperBinary <%@> for Endpoint <%@>
Asset Fully Processed, status is %lu. UUID of %@
%s: SuperBinary Header length is too long; Actual Length is %lu, SuperBinary Headers says %lu
%s: Unrecognized TLV key %#x
%s: Asset %@, processing status is %@, asset type is %@
%s: Found Downstream Endpoint matching Downstream ID %lu, %@
Endpoint %@: Superbinary Offer %@
Payload Index <%lu> Ready for SuperBinary <%@> for Endpoint <%@>
%s: failed to append chdr data at compressed offset %lu
%s: NEW UARP delegate overridden
%s: asset length is zero, cannot get block
%s: Error querying asset metadata -> <%u> %s
%s: Error querying payload info to %lu
Payload Index <%lu> Data (offset %lu, length %lu> for SuperBinary <%@> for Endpoint <%@>
%s: Enable Banyan Interrupt (%#x)
%s:  to create directory at %@ (%@)
%s: cannot find component %@ for tatsu ticket; %@
Payload Index <%lu> TLV for SuperBinary <%@> for Endpoint <%@>
%s: Failed to write ITCM (%#x)
%s: %@
%s: Could not find subfile %@ in %@ to take measurement; let tatsu fail this
%s: TX Firmware Asset Fully Staged, status is %lu. UUID of %@
Endpoint %@: Rescinded Assets Response
%s: uarpPlatformQueryEndpointComponentDiscovery() %s
%s: Failed to read Fusing Register
Watchdog Expired failed, status is %s
%s: Compression below tolerance update Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)
%s: expandPropertyListTLVs: failed to process tlv
%s: %lu Outstanding Info Properties for endpoint configuration: %@
%s: Next Layer 3 Payload
%s: Error preparing solicited dynamic asset -> <%u> %s
%s: Tatsu Ticket %@
%s: TX Dynamic Asset Fully Staged, status is %lu. UUID of %@
%s: RX Dynamic Asset Fully Staged (%@), status is %lu. UUID of %@
%s: uarpPlatformGetSupportsBulkInfoQueries() failed %s, %@
%s: Failed to create IONotificationPort
%s: %lu configurations
%s: Error offering asset to endpoint -> <%u> %s
%s: not an FTAB payload for payload index %lu
%s: Missing manifest asset
%s: Can only provide %d bytes from offset %d of asset %@
%s: Error setting payload index to %lu
Endpoint %@: Remote Not Responding
%s: Failed to query payload info for index %lu -> <%u> %s
%s: Wrote %u bytes (%#x)
%s: Maximum write size exceeded %u
%s: Error querying asset tag -> <%u> %s
%s: processSuperBinaryPropertyList: failed to process
%s: cannot expand payload index %lu
%s: cleanFileHandleForWriting failed %@ 
%s: Requested offset (%d) longer than payload length %d
%s: Asset Ready SuperBinary <%@> for Endpoint <%@>
%s: hash of payload %@ ending offset %lu beyond payload  length of %lu
%s: no previous ftab associated for payload index %lu
%s: Unexpected header magic (%02x %02x %02x %02x %02x %02x %02x %02x)
%s: metadata padding is %lu
%s: Outstanding Info Property for endpoint configuration: %@ (%@)
%s: Removed Personalizing Asset - %@
%s: rescind assets
%s: Endpoint %@: Endpoint ID = %d, saved %@
Asset Release for SuperBinary <%@> for Endpoint <%@>
%s: could not decompress payload %@, index %lu
%s: Compressed with Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
\n
%s: no firmware available
Failed to remove downstream endpoint id %lu, status is %s
%s: expandPropertyListPayloads: failed to process payloads
Failed to query info property %u, status is %s
Asset Personalization, status is %@. UUID of %@
%s: Could not find %@ to take measurement
%s: uarpPlatformEndpointAssetFullyStagedRequiresReboot() failed; <%u> %s
%s: writing to personalized URL failed, %@
%s: hash of payload %@ adjust starting offset %lu 
%s: ftab is nil
%s: Interrupt mask is %#llx
%s: UARP restore updater delegate not set
%s: Read UARP packet %u (%#x)
%s: Unexpected type for bootloader asset
%s: SuperBinary Payload key's value is not an NSArray
%s: Solicit Dynamic Asset; 4cc = %@, UUID = %@
%s: Asset <%@> for Endpoint <%@>; payload index %lu has unexpected data length of %d
%s: could not prepare personalized URL for payload index %lu
%s: closeAndReturnError failed with %@
%s: Could not create TLV for value 0x%08x, length %u
%s: Transfer Asset
%s: Cannot add direct endpoint as downstream endpoint
%s: payload length is zero, cannot get block
%s: cannot close %@, error %@
%s: hash of subfile %@ is %@
%s: Failed to instantiate UARPSuperBinaryPayloadLayer3 at index %lu for %@
%s: processDeploymentRules: failed to process
%s: could not read superbinary header
%s: cannot seek to offset %lu (file length %lu) from %@, error %@
%s: Invalid mode request
%s: Payload headers has unexpected excess buffer length of %lu
%s: Deny Asset
NOT IMPLEMENTED YET - Asset Set Data for SuperBinary <%@> for Endpoint <%@>
%s: Failed to get compressed header
%s: Failed to write AUTH (%#x)
%s: Downstream Endpoints %@
%s: unknown 0x%08x
Endpoint %@: Unsolicited Dynamic Asset Offered %@
%s: [pid=%d] %@\n
Payload Index <%lu> for SuperBinary <%@> for Endpoint <%@>.updated staged firmware version to %@
%s: Take %@ hash of payload %@ at offset %lu with length of %lu 
%s: Could not archive property list to payload data
%s: Failed to find AppleTCONControl
%s: Unexpected bootloader config length %lu
%s: Failed to get TCON API
%s: skip copying %@ to %@; original file does not exist
%s: Wait for %lu Outstanding Info Properties for endpoint component %@ 
%s: Removing downstream endpoint
%s: Error writing reset sequence (%#x)
Asset Corrupt for SuperBinary <%@> for Endpoint <%@>
%s: cleanFileHandleForWriting failed with %@
%s: Can only provide %d bytes from offset %d of payload %@
%s: No Data Block, no URL failed 
%s: property list is not a dictionary
NOT IMPLEMENTED YET - Asset Pre Processing Notification Ack for SuperBinary <%@> for Endpoint <%@>
%s: Could not read payload url into property list
%s: Clear interrupt status (%#x)
%s: uarpPlatformConfigureEndpointTags() failed, status is %s
%s\n
%s: Cleared UARP Packet Ready (%#x)
%s: readRegister %#x (%#x)
%s: RX Firmware Asset Fully Staged, status is %lu. Asset Verison is %@. Staged Version is %@. UUID of %@
%s: Error appending payload data to index %lu
%s: NEED TO HANDLE DECOMPRESSION AS FILE
%s: component %@ outstandingInfoProperties does not contain %@ (%@), ignoring
Endpoint %@: Downstream Endpoint Unreachable, ID = %u
%s: could not instantiate UARPSuperBinaryPayloadLayer3 for asset %@ on endpoint %@
%s: Failed to create IOAVDisplayMemory
%s: Timeout boot status %#x expected %#x
%s: Failed to set TCON API
%s: uarpPlatformRemoteEndpointRemove() failed, status is %s
%s: %lu Outstanding Apple Properties for endpoint configuration %@
%s: Responded Bulk Info Property %@ (%@) for endpoint configuration %@
%s: setting up payload %lu with file %@
%s: buffer %u
%s: Bootloader is too small %lu
%s: Could not create TLV for 0x%04x of length %u for SuperBinary <%@> for Endpoint <%@>
%s: cannot seek to offset %lu (subfile length %lu) from %@, error %@
%s: outstandingInfoProperties does not contain %@ (%@), ignoring
%s: Hash payload %@ started at %@.%@ and completed at %@.%@
%s: Failed to write TCON CONFIG (%#x)
UARPStatistics
UARPRestoreDeviceProtocol
UARPMetaDataPersonalizationManifestEpoch
UARPMetaDataPersonalizationFTABSubfileTrusted
UARPMetaDataPersonalizationFTABGeneration
UARPMetaDataVoiceAssistLocale
UARPTatsuObjectProperties
UARPMetaDataPersonalizationUseGlobalSigning
UARPMetaDataHostPersonalizationRequired
UARPMetaDataPayloadCompressionAlgorithm
UARPMetaDataPersonalizationDigestListSize
UARPMetaData
UARPMetaDataPersonalizationNonFTABPayload
UARPMetaDataPersonalizationPrefixNeedsLogicalUnitNumber
UARPMetaDataVoiceAssistHash
UARPMetaDataVoiceAssistRole
UARPMetaDataPersonalizationNonFTABSubfileESEC
UARPTatsuOptions
UARPMetaDataPersonalizationFTABSubfileTag
UARPMetaDataComposeBVERStringFile
BanyanUARPUpdaterDevice
UARPMetaDataFdrParameterData
UARPMetaDataPersonalizationProductType
UARPMetaDataHeySiriModelSignature
NSCopying
UARPSuperBinaryLayer3
Layer2VendorCallbacks
Layer2AssetCallbacks
UARPMetaDataPersonalizationNonFTABSubfileTrusted
UARPMetaDataPersonalizationAllowFlashWrite
UARPMetaDataHostMinimumBatteryLevel
UARPMetaDataPersonalizationFTABPayload
UARPMetaDataComposeSimpleBVERStringFile
UARPMetaDataPersonalizationPayloadTag
UARPMetaDataPersonalizationManifestSuffix
UARPMetaDataPersonalizationProvisioning
UARPMetaDataPersonalizationMatchingDataProductRevisionMax
UARPMetaDataPersonalizationNonFTABSubfileLongname
UARPTatsuBootNonceLocation
UARPRTKitFTABSubfile
UARPMetaDataPersonalizationSecurityDomain
UARPMetaDataPersonalizationECID
UARPMetaDataPersonalizationNonce
UARPMetaDataPersonalizationSharedManifest
UARPMetaDataVoiceAssistSignature
UARPMetaDataDeviceCompressPayloadChunkSize
UARPEndpointLayer3
UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
UARPMetaDataPersonalizationTicketNeedsLogicalUnitNumber
UARPMetaDataComposeMetaDataHashAlgorithm
UARPRTKitFTAB
BanyanUARPUpdaterLog
Tcon
UARPMetaDataComposeFTABPayload
UARPMetaDataDeviceCompressedHeaders
UARPMetaDataDevicePayloadHash
UARPEndpointOptions
UARPMetaDataFdrDataToSign
UARPMetaDataFdrData
UARPMetaDataDevicePayloadHashAlgorithm
UARPMetaDataPersonalizationSuperBinaryPayloadIndex
UARPMetaDataHostTriggerBatteryLevel
UARPMetaDataHostExcludedHwVersion
UARPMetaDataPersonalizedManifest
UARPMetaDataPersonalizationDemotionSecurityMode
UARPMetaDataPersonalizationFTABSubfileLongname
UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
UARPMetaDataPersonalizationFTABSubfileEPRO
UARPComponentVersion
UARPMetaDataPersonalizationBoardID64
UARPMetaDataHostDeploymentRuleCountry
UARPSuperBinaryPayloadLayer3
UARPMetaDataCrashAnalyticsAppleModelNumber
BanyanUARPUpdaterManager
UARPMetaDataHeySiriModelRole
UARPMetaDataVoiceAssistEngineVersion
UARPComponentTag
UARPMetaDataDeviceVendorVersionStringFile
UARPMetaDataInformationFriendlyName
UARPMetaDataPersonalizationDemotionProductionMode
UARPMetaDataPersonalizationMoreRequestsToFollow
UARPMetaDataPersonalizationChipID
UARPMetaDataPersonalizationBootNonce
UARPMetaDataHeySiriModelActiveModel
UARPMetaDataHostMinimumVersion_visionOS
UARPMetaDataDevicePayloadOrderedIndex
UARPEndpointPacketCapture
UARPMetaDataPersonalizationChipEpoch
UARPMetaDataComposePayloadHashAlgorithm
NSSecureCoding
NSCoding
UARPMetaDataHostMinimumVersion_tvOS
UARPMetaDataPersonalizationEnableMixMatch
UARPMetaDataCrashAnalyticsTestMode
UARPMetaDataDevicePayloadIdentifierString
UARPMetaDataPersonalizationNonFTABSubfileHashAlgorithm
UARPMetaDataDeviceMetaDataHash
UARPMetaDataHeySiriModelEngineType
UARPEndpointConfiguration
UARPMetaDataDeviceUncompressedPayloadLength
UARPMetaDataPersonalizationSecurityMode
UARPMetaDataHeySiriModelCertificate
UARPMetaDataDevicePayloadSignature
UARPMetaDataInformationHardwareFusing
UARPMetaDataMappedAnalyticsEventID
UARPEndpointLayer3DelegateProtocol
UARPMetaDataPersonalizationFTABSubfileHashAlgorithm
UARPMetaDataPersonalizationCertificateEpoch
UARPMetaDataVoiceAssistDigest
UARPMetaDataVoiceAssistType
UARPMetaDataHeySiriModelEngineVersion
UARPMetaDataPersonalizationLife
Deprecated
UARPMetaDataComposeMarketingBVERStringFile
UARPMetaDataPersonalizationMatchingDataProductRevisionMin
UARPMetaDataComposeVersionStringFile
UARPMetaDataMappedAnalyticsAppleModelNumber
UARPMetaDataInformationActiveFirmwareVersion
UARPMetaDataPersonalizationRequired
BanyanUARPTransport
UARPMetaDataFdrContext
UARPMetaDataPersonalizationMatchingDataPayloadTags
UARPMetaDataPersonalizationFdrRootCaDigest
UARPTatsuTicket
UARPMetaDataDeviceFirmwareVariant
UARPMetaDataHostMinimumVersion_watchOS
UARPEndpointTransportTxProtocol
UARPMetaDataCrashAnalyticsCoreName
UARPMetaDataInformationAppleModelNumber
UARPMetaDataComposePropertyListPayload
UARPMetaDataPersonalizationRealHdcpKeyPresent
UARPMetaDataDevicePayloadIdentifier
UARPMetaDataPersonalizationProductionMode
UARPMetaDataHeySiriModelLocale
UARPMetaDataVoiceAssistCertificate
UARPMetaDataDeviceMinimumRequiredVersion
UARPTatsuFTABProperties
UARPMetaDataHeySiriModelHash
UARPMetaDataInformationManufacturerName
UARPMetaDataPersonalizationNonFTABSubfileEPRO
UARPMetaDataPersonalizationSuffixNeedsLogicalUnitNumber
UARPMetaDataPersonalizationFTABSubfileESEC
UARPMetaDataDeviceUrgentUpdate
UARPMetaDataPersonalizationEnableFutureFWVersion
UARPMetaDataHostDeploymentRulePercentage
UARPMetaDataVoiceAssistActiveModel
DeviceBasedPersonalization
UARPMetaDataPersonalizationUIDMode
UARPHashMachine
UARPMetaDataPersonalizationFTABSubfileDigest
UARPMetaDataHeySiriModelType
UARPMetaDataHostMinimumVersion_macOS
UARPMetaDataDeviceFlashSectionLength
Layer2EndpointCallbacks
UARPMetaDataInformationSerialNumber
UARPMetaDataPersonalizationNonFTABSubfileDigest
UARPTatsuManifestProperties
UARPEndpointTransportRxProtocol
UARPMetaDataHostMinimumVersion_iOS
UARPMetaDataFdrParameterName
UARPMetaDataPersonalizationAllowUnsealedData
UARPMetaDataPersonalizationManifestPrefix
UARPMetaDataInformationModelName
UARPDeploymentRules
UARPLastError
UARPComponentConfiguration
UARPMetaDataPersonalizationNonceSeed
UARPMetaDataInformationAssetIdentifier
UARPMetaDataPersonalizationSuperBinaryAssetID
UARPMetaDataDevicePayloadExpandFilename
UARPTatsuManifestLocation
UARPMetaDataFdrSignature
UARPMetaDataHeySiriModelDigest
UARPMetaDataPersonalizationMatchingData
UARPMetaDataPersonalizationECIDData
UARPMetaDataPersonalizationNonceHash
UARPRestoreUpdaterDeviceProtocol
UARPMetaDataPersonalizationSoCLiveNonce
UARPMetaDataRequiredPersonalizationOption
UARPMetaDataPersonalizationLogicalUnitNumber
UARPMetaDataDeviceIgnoreVersion
UARPMetaDataPersonalizationFTABSubfileDigestFilename
UARPMetaDataPersonalizationBoardID
UARPMetaDataDevicePayloadCertificate
UARPMetaDataInformationStagedFirmwareVersion
UARPMetaDataPersonalizationChipRevision
UARPMetaDataDeviceMetaDataHashAlgorithm
UARPMetaDataInformationHardwareVersion
uidMode
_banyanManager
_downstreamEndpoints
_paddingBlock
asset4cc
boardID64
layer2CallbackManifestEpochResponse:
uarpMessageSendToDevice:
T@\"NSData\",R,V_payloadCertificate
_allowUnsealedData
_compressedPayloadDataInternal
_signature
personalizationStatePrepare:endpoint:
updateFirmwareWithDictionary:
T@\"NSString\",R,V_tagString
_logContext
_manifestLocation
addSecurityDomain:componentTag:tatsuTicket:keyName:
appendBytes:length:
arrayWithObjects:
generatePayloadHash:measureOffset:measureLength:
numberWithUnsignedChar:
_urgentUpdate
apBoardID
chipID
expandSuperBinaryPlist
tcon_reg
updateDelegateFilename
addNonce:componentTag:tatsuTicket:keyName:defaultNonce:
modelCertificate
notifyEndpointAppliedStagedAssets:
processPMAP:
T@\"NSString\",R,V_modelHash
TC,R,V_allowFlashWrite
TI,R,V_urgentUpdate
_payloadIdentifier
setRecvCounterpart:
TB,R,V_needsTrusted
_layer2Context
modelDigest
needsSHA384
tatsuRequest
T@\"NSData\",C,V_nonceSeed
T@\"NSData\",R,V_metaData
clearIrqStatus:
layer2VendorCtx
_supportsBulkInfoQueries
addUIDMode:componentTag:tatsuTicket:keyName:
appendCompressedPayloadData:offset:
initWithPayloadURL:payloadTlvs:payload4cc:payloadVersion:payloadIndex:
T@\"NSData\",R,V_nonceHash
T@\"NSNumber\",&,V_ftabGeneration
TI,R,V_tag
_bootNonce
_compressedHeaders
_inDfuMode
_needsSHA384
_solicitationQueueDepth
_productionMode
initWithFormat:
_ticketLongName
_pendingConfigurations
actualOffset
expandFilename
layer2CallbackAssetSolicitation:
layer2CallbackDownstreamReachable:tlvs:
fdrData
numberWithLong:
_manifestAsSuffix
logRxPacket:
metaData
sendSyncToPeer
setLogicalUnitNumber:
tag
T@\"UARPComponentVersion\",R,V_version
TQ,R,V_numPayloads
TS,R,V_productionModeHostOverride
_layer2VendorExtension
_propertyList
productionMode
tlvsFromKey:value:relativeURL:
composeToData:
isEqualToString:
queryOutstandingEndpointIDComponentProperties:
subfileESEC
T@\"NSString\",C,V_manifestPrefix
T@\"NSString\",R,V_osVersion
_filename
longLongValue
tlvNameForAppleProperty:
T@\"NSNumber\",C,V_liveNonce
TQ,R,V_ecID
_excludedPayloadTags
acceptLayer3Payload:
assetPayloadData:offset:asset:
needsDigest:algorithm:objp:objectDictionary:
setAttributes:ofItemAtPath:error:
setIsHostRole:
T@\"NSNumber\",C,V_apSecurityMode
_banyanManagerQueue
_demotionSecurityMode
_lastAction
composedMetaData
getDfuInfo
isDone
setDataBlock:offset:
T@\"<UARPEndpointTransportTxProtocol>\",R,W,V_transportTxDelegate
T@\"NSString\",R,V_digestKeyName
layer2CallbackDataTransferPausedByRemote
layer2CallbackLogicalUnitNumberResponse:
layer2CallbackManifestPrefixResponse:
modelLocale
outstandingInfoProperties
setupDefaultPropertyQueries
T@\"NSData\",C,V_manifest
Tc,R,V_char4
_bootNonceLocation
_packetsMissed
_txDynamicAssets
activeModel
now
_objectProperties
_useFileSystem
expandSuperBinaryHeader
numberWithUnsignedLongLong:
queryInfo:
unsignedIntegerValue
T@\"NSString\",R,V_manifestSuffix
data
expandPayloadDictionaryKeyValuePayload
inDfuMode
layer3EndpointAssetPersonalizationComplete:asset:status:
manifestLocation
_life
_measureOffset
_selectedPayloadIndex
acceptOffer:queue:
tssServerURL
_hardwareFusing
_boardID64
_layer2WatchdogTimer
_subFileLength
_tagString
appendString:
queryAppleProperty:
whitespaceAndNewlineCharacterSet
T@\"NSURL\",R,V_url
chunkSize
initWithPayloadHash:
readReversedRegisters:::
tssRequests
T@\"NSString\",R,V_firmwareVariant
Tc,R,V_char2
addTatsuTicketManifest:ticket:manifestLocation:payload:
moreRequestsToFollow
setAssetType:
setBootNonce:
writeToFileHandle:includedPayloads:allHeaders:allMetaData:error:
containsString:
T@\"NSString\",C,V_manifestSuffix
TC,R,V_testMode
TB,V_ignoreVersion
_defaultAppleProperties
componentTagWithLength:value:
formatVersion
initWithTicketDictionary:
T@\"<UARPEndpointPacketCaptureDelegateProtocol>\",R,W,V_pcapDelegate
_chipID
generateHash:ftabSubfile:
metaDataHash
modelHash
setECID:
ticketNeedsLogicalUnitNumber
T@\"NSData\",R,V_parameterData
_ticketNeedsLogicalUnitNumber
addEntriesFromDictionary:
assetProcessingCompletedAck:
composeFTABAsData
decodeArrayOfObjectsOfClass:forKey:
dictionaryWithDictionary:
downstreamEndpointReachable:downstreamEndpointID:tlvs:
T@\"UARPTatsuManifestLocation\",R,V_manifestLocation
applyStagedAssets
initWithLayer2Context:tmpFolderPath:
personalizationStatePrepare:
preparePersonalizedURL
setEndpointID:
sharedManifest
eventID
_minorVersion
_tatsuRequest
caseInsensitiveCompare:
layer2CallbackSuperBinaryOffered:
personalizeFirmwareAsset:assetUUID:tssServerURL:
T@\"NSString\",R,V_expandFilename
TQ,R,V_packetsOutOfOrder
_maxTxPayloadLength
initWithDaysFromNow:
T@\"NSData\",R,V_payloadSignature
TB,R,V_metaData
T@\"UARPTatsuManifestDestination\",R,V_manifestDestination
TI,R,V_ftabGeneration
_ftabHeader
_provisioning
copyItemAtURL:toURL:error:
layer2CallbackDiscoveredEndpointID:components:
TC,R,V_ticketNeedsLogicalUnitNumber
TQ,V_solicitationQueueDepth
_needsSHA256
arrayWithObject:
layer2CallbackAppleModelNumberResponse:
nextLayer3Payload:
notifyPayloadReady:payload:
processPercentageDeploymentRules:
initWithlogFunction:logContext:
TQ,R,V_assetLength
_componentTag
_maxRxPayloadLength
_requiresPersonalization
_superbinaryHeader
assetProcessingCompleted:flagsDescription:asset:
digestListSize
_assetVersion
getAllBanyanDevices
notifyRxDynamicAssetFullyStaged:
setManifest:asSuffix:
setTatsuResponse:
assetRescinded:
numberWithBool:
TQ,R,V_packetsNoVersionAgreement
UUID
characterSetWithCharactersInString:
setNeedsStaging:
layer2CallbackEcidDataResponse:
_bytesTransferred
_useGlobalSigning
addFTABGeneration:payload:componentTag:defaultFTABGeneration:
securityDomain
setApProductionMode:
_moreRequestsToFollow
bytesTransferred
readDataUpToLength:error:
T@\"NSData\",R,V_digest
_flashSectionLength
_productionModeHostOverride
getFusingType:
superbinaryURL
tlvs
T@\"NSNumber\",C,V_securityMode
TQ,R,V_boardID
_firmwareVersion
initWithHashAlgorithm:
startUARPLayer2:configuration:infoProperties:appleProperties:endpointID:upstreamEndpoint:
T@\"NSString\",C,V_friendlyName
_char2
_ftabSuffix
hwVersion
tssResponse
T@\"UARPEndpointLayer3\",R,W,V_layer3Endpoint
T@\"NSData\",R,V_manifestData
T@\"NSString\",R,V_ticketPrefix
TB,V_fuseSDOM
_uarpCallbacks
layer2CallbackSecurityDomainResponse:
layer2CallbackWatchdogSet:
setMaxTxPayloadLength:
T@\"NSObject<OS_os_log>\",R,V_log
TI,R,V_useGlobalSigning
_hwFusingType
manifestProperties
nonce
payloadWindowLength
setPaddingBlock:
T@\"NSString\",R,V_minimumVersionString
copyWithZone:
initWithDict:
matchingData
packetTracking:packetDirection:inFunction:
pcapDelegate
rescindAssets
T@\"NSString\",C,V_productGroup
T@\"NSString\",R,V_friendlyName
_pcapDelegate
_reofferFirmwareOnSync
addRealHdcpKeyPresent:componentTag:tatsuTicket:keyName:
dfuInfo:
initWithRulesDictionary:
layer2CallbackDataTransferResumedByRemote
tlvType
TC,R,V_moreRequestsToFollow
TQ,V_txBufferOverhead
offerDynamicAsset:fourCC:
setRestoreUpdaterDelegate:
writeData:error:
_modelType
_needsStaging
_outstandingInfoProperties
_payloadHash
epro
expandPropertyListTLVs:
filename
_digest
_superbinaryURL
T@\"NSString\",R,V_countryCode
checkPropertyQueryComplete
compare:
notifyAssetOffered:
payloadLength
securityModeHostOverride
_manifestData
_maxTransmitsInFlight
_packetQueue
fusePROD
getIrqStatus:
initWithLastAction:lastError:
layer2CallbackHwFusingTypeResponse:
layer2CallbackManifestSuffixResponse:
T@\"NSDictionary\",C,V_tatsuRequest
assetIdentifier
TS,R,V_endpointID
_modelDigest
calculateDeploymentPercent:
layer2CallbackRequestBuffer:
layer2CallbackTicketLongNameResponse:
setAllowUnsealedData:
_compressedHash
T@\"UARPComponentTag\",R,V_tag
_packetsOutOfOrder
configureEndpointLayer2Tags
engineVersion
layer2CallbackNonceResponse:
seekToOffset:error:
setProvisioning:
Tq,R,V_personalizationStatus
_activeModel
notifyDownstreamEndpointUnreachable:
paddingBlock
setOutstandingInfoProperties:
tagString
totalBytesRequested
uarpMessageRecvFromTransport:
T@\"NSString\",R,V_hwVersion
T@\"UARPComponentVersion\",R,V_firmwareVersion
_eventID
_hardwareSpecific
_tmpFolderPath
bootNonceLocation
initWithPropertyList:payloadsURL:
objectProperties
T@\"NSNumber\",C,V_productionMode
TQ,R,V_lastError
_banyanTransport
_ticketName
addObject:
layer2CallbackSocLiveNonceResponse:
metaDataTable
TB,V_reofferFirmwareOnSync
_data
_fdrData
_tatsuMeasurements
fileURLWithPath:
layer2CallbackApSecurityModeResponse:
payloadHash
processRespondedEndpointInfoQueries:tlvs:
dataWithBytes:length:
initWithUUID:transportTxDelegate:layer3Delegate:tmpFolderPath:
layer3EndpointAppliedStagedAssets:layer3Flags:
ticketLongName
T@\"NSNumber\",C,V_allowUnsealedData
TS,R,V_assetID
measureOffset
updateIncomingAssetProperties:
T@\"NSNumber\",C,V_suffixNeedsLUN
T@\"NSString\",R,V_algorithm
T@\"UARPComponentVersion\",R,V_assetVersion
TB,V_disableRetries
_banyanDevices
layer3DownstreamEndpointUnreachable:downstreamID:
removeObjectAtIndex:
setBoardID32:
T@\"NSString\",R,V_keyName
_completedAssets
composeToDataExcludingTags:error:
initWithPayload4cc:payloadVersion:payloadIndex:baseURL:
stopUARPLayer2Internal
stringFromPlistValue:
subfileTag
supportsSecureCoding
T@\"NSString\",C,V_manufacturerName
personalizedURL
_chipEpoch
_countryCode
_numPreallocatedBuffers
setDisableRetries:
_sharedManifest
T@\"UARPComponentVersion\",C,V_stagedFirmwareVersion
TS,R,V_uncompressedLength
_tatsuTickets
bootNonce
dataWithContentsOfURL:
expandPayloadDictionaryData:
initWithUUID:tmpFolderPath:
T@\"NSData\",R,V_bootNonce
T@\"UARPComponentVersion\",R,V_engineVersion
_logicalUnitNumber
_productRevisionMin
_untilDay
layer2CallbackBulkInfoQuery:componentTag:infoProperties:
pathWithComponents:
payloadWithMatchingIndex:
TC,R,V_liveNonce
TI,R,V_securityDomain
_layer2PayloadHeader
demotionSecurityMode
devicePersonalizationStateCompleted
notifyAssetPersonalizationNeeded:
personalizationStarted:
processDeploymentRules:
_productGroup
countByEnumeratingWithState:objects:count:
initWithCoder:
layer2CallbackRequestTransmitMsgBuffer:
matchingTLVs:
removeTLV:
setBootNonceAsTLV:
setCertificateEpoch:
_char1
firstObject
ignoreVersion
processTatsuTicketManifest:ticket:
setComponents:
setManufacturerName:
tlvValue
responseTimeout
T@\"NSUUID\",R,V_uuid
_algorithm
initWithLength:value:
setEndpointType:
setTatsuRequest:
tlvValueWithUInt8:
_layer3Endpoint
T@\"UARPEndpointPacketCapture\",R,V_packetCapture
_enableMixMatch
_packetsNoVersionAgreement
assetSetData:offset:asset:
notifyAssetPersonalizationComplete:status:
setProcessingStatus:
writeComposedPayloadDataToFile:error:
T@\"NSData\",C,V_hardwareSpecific
TC,R,V_sharedManifest
TI,R,V_boardID
TI,R,V_eventID
TI,R,V_securityMode
TQ,R,V_lastAction
_fdrRootCaDigest
composePayload
T@\"UARPComponentVersion\",R,V_minimumVersion
_verbose
addSecurityMode:componentTag:tatsuTicket:keyName:
exportAsDictionary
layer2CallbackLogError:logMsg:
mergePayloadsPMAPs
notifyEndpointRescindedStagedAssets
superBinaryPlist
_manifestPrefix
_isCompressed
fileSize
getManifest
prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:
savePrDocOptions:
TB,R,V_needsHostPersonalization
_payloadOrderedIndex
archivedDataWithRootObject:requiringSecureCoding:error:
noFirmwareAvailable
setHardwareVersion:
ticketName
layer2RemoteCtx
TB,R,V_needsEPRO
TQ,V_maxTransmitsInFlight
addDigestForTatsuDictionary:objectProperty:
layer2CallbackDownstreamReleased:
initWithUnsignedInt:
uarpRouteRecvMessageToDownstreamEndpoint:downstreamEndpointID:
uniquePacketCaptureFilename
updateHash:
T@\"NSString\",C,V_modelName
ECIDData
TQ,R,V_packetsDuplicate
_forceDFU
getDataRangeFromURL:
layer3EndpointAssetFullyStaged:txFirmwareAsset:
personalizedData
T@\"NSString\",R,V_manufacturerName
T@\"NSString\",R,V_subFileTag
dataWithLength:
TB,V_supportsBulkInfoQueries
TC,R,V_allowUnsealedData
irqConnection
setChipEpoch:
TB,V_useHostPushModel
TI,R,V_actualOffset
dataWithData:
initWithPayloadData:payloadMetaData:payload4cc:payloadVersion:payloadIndex:
apSecurityMode
assetRelease:
assetType
digest
disableRetries
initWithLayer2Context:assetTag:tmpFolderPath:
solicitationQueueDepth
T@\"NSString\",R,V_hardwareVersion
_assetLength
fuse:
hashValue
layer3EndpointProtocolVersionSelected:
mutableBytes
_asset
_majorVersion
containsTLV:
devicePersonalizationStateStarted
retryLimit
T@\"NSNumber\",C,V_allowFlashWrite
TC,R,V_enableMixMatch
_assetType
_tlvName
defaultOptions
nonceHash
notifyEndpointPayloadData:payload:offset:payloadData:
Tc,R,V_char3
_boardID32
_trusted
closeAndReturnError:
ftabProperties
hashPayload
logString:
manifestDestination
TB,R,V_isDone
_batteryLevel
_compressionAlgorithm
_layer2RemoteEndpoint
_metaDataHash
createFileAtPath:contents:attributes:
setBoardID64:
setDataBlockToData:offset:payloadData:
T@\"NSNumber\",C,V_prefixNeedsLUN
componentVersionWithLength:value:
needsStaging
serialNumber
setModelName:
transportTxDelegate
untilDate
assetStagingProgress:bytesTransferred:assetLength:
countryRules
expandPayloadWithHeaderAsData:payloadIndex:payload4cc:payloadVersion:payloadMetaData:
layer2CallbackApBoardIDResponse:
payloadSignature
stopUARPLayer2AndWait
addTLV:
TQ,V_maxRxPayloadLength
_defaultInfoProperties
processComposeMeasuredPayloads:value:relativeURL:
setResponseTimeout:
uarpRole
T@\"NSNumber\",C,V_manifestEpoch
toUpper
UUIDString
_context256
_needsESEC
queryInfo
setManifestSuffix:
tssOption
allowFlashWrite
subfileLongname
TB,V_needsStaging
TI,R,V_infoProperty
_engineVersion
_keyManifest
assetReady:
composePersonalizedFTAB
_digestKeyName
_filepath
_modelHash
_useHostPushModel
expandPayloadHeadersAndMetaData:offset:
index
initWithBytes:length:
layer3EndpointPersonalizationNeeded:asset:
T@\"NSData\",R,V_ecID
TS,R,V_securityModeHostOverride
_minimumVersionString
_nonceHash
assetVersion
layer3EndpointAssetOffered:asset:
payloadData
queue
T@\"NSData\",R,V_metaDataHash
setUpgradeOnly:
Tq,V_assetType
_suffixNeedsLogicalUnitNumber
assetLength
countryCode
decodeCharForKey:key:
enableMixMatch
T@\"NSString\",R,V_context
decodeObjectOfClass:forKey:
ftabSubfile
layer2CallbackLogFault:logMsg:
txBufferOverhead
_composedMetaData
T@\"UARPComponentVersion\",C,V_firmwareVersion
T@\"NSData\",R,V_nonce
_minimumVersion
TI,R,V_productRevisionMin
_tssServerURL
clearMatchingLayer2Context:
manufacturerName
preflightInfoProperties
version
_prefixNeedsLUN
T@\"NSNumber\",C,V_logicalUnitNumber
TI,R,V_certificateEpoch
notifyApplyStagedAssets
releaseVersion
setDateFormat:
setUseHostPushModel:
T@\"NSURL\",R,V_superbinaryURL
productNumber
T@\"NSString\",R,V_parameterName
containsPayloadWithMatchingTag:
TQ,V_maxTxPayloadLength
composedPayloadLength
layer3EndpointApplyStagedAssets:
notifyAssetSolicited:
notifyEndpointAssetMetaDataComplete:
tatsuTickets
T@\"NSString\",R,V_assetIdentifier
TQ,R,V_subFileLength
_hardwareVersion
_untilYear
needsESEC
setLiveNonce:
setSecurityMode:
uarpReadPacketSize:
T@\"NSString\",C,V_productNumber
T@\"UARPTatsuBootNonceLocation\",R,V_bootNonceLocation
_measureLength
minimumVersionString
parameterData
dataFromPlistValue:
generatePayloadHash:
nonceSeed
payloadOrderedIndex
URLByAppendingPathComponent:
_manifestProperties
_payloads
setRequiresPersonalization:
_fuseSDOM
dateByAddingTimeInterval:
majorVersion
maxRxPayloadLength
prefixNeedsLogicalUnitNumber
prepareQueriesForPersonalization:
setApBoardID:
versionString
T@\"NSData\",R,V_composedMetaData
T@\"NSData\",C,V_ecidData
T@\"NSData\",R,V_manifest
T@\"NSData\",R,V_modelDigest
TQ,R,V_majorVersion
_coreName
digestKeyName
initWithChar1:char2:char3:char4:
T@\"NSURL\",R,V_personalizedURL
TQ,V_responseTimeout
_lastApplyStatus
_uncompressedPayloadURL
layer2CallbackDownstreamReachable:
layer2CallbackHardwareSpecificResponse:
packetsNoVersionAgreement
realHdcpKeyPresent
T@\"UARPComponentVersion\",R,V_payloadVersion
ftabDescription
TB,R,V_ftabSubfile
_payload4cc
boardID32
dfuStage:
firstLayer3Payload:
needsTrusted
T@\"NSData\",R,V_fdrRootCaDigest
_appleModelNumber
_ftabSubfile
initWithPropertyList:payloadsURL:noMissingPayloads:
layer2CallbackRemoteNotResponding:length:
layer2CallbackStatisticsResponse:
setAssetIdentifier:
setFusePROD:
lastApplyStatus
requiredPersonalizationOptions:
TS,R,V_trusted
_formatVersion
layer2CallbackLogDebug:logMsg:
maxTransmitsInFlight
offerFirmwareAsset:assetUUID:
removeAllObjects
T@\"NSDate\",R,V_untilDate
T@\"NSNumber\",C,V_payloadWindowLength
_compressedPayloadURL
_modelCertificate
init
layer2CallbackProvisioningResponse:
payloadCertificate
prefixNeedsLUN
boardID
tlvName
log:
processingStatus
setFusingType:error:
setUidMode:
subFileOffset
tlvValueWithUInt64:
T@\"NSString\",R
TS,R,V_protocolVersion
_firmwareVariant
_nonce
componentsSeparatedByCharactersInSet:
personalizeFirmwareAssetComplete:tssResponse:
selectedPayloadIndex
setFirmwareVersion:
_banyanManagerSemaphore
_rxDynamicAssets
description
stagedFirmwareVersion
stagingInProgress
writeToURL:excludeTags:error:
engineType
im4mBuildTicketPrefixForPayload:ticketNeedsLUN:logicalUnitNumber:
initWithComponentName:ftabSubfile:metaData:
numberWithUnsignedInteger:
setLife:
uncompressedPayloadLength
_ecID
conformsToProtocol:
manifestData
tlvValueWithString:
updateFilepath:uuid:
writeComposedPayloadToFile:error:
T@\"NSNumber\",C,V_chipID
Ti,V_endpointType
im4mCraftTatsuTickets:
initWithPayloadDictionary:payloadsURL:payloadIndex:
logicalUnitNumber
modelName
outstandingAppleProperties
tlvValueWithComponentVersion:
writeRegister::
_liveNonce
dictionaryWithContentsOfURL:
getFusingType:error:
removeObject:
writeRegisters:::
_ecidData
assetPayloadMetaDataComplete:
craftTatsuRequest:
findComponentConfiguration:endpointConfig:
layer3EndpointAssetSolicited:assetTag:
personalizationCompleted:
setProductGroup:
TI,R,V_flashSectionLength
downstreamEndpointAdd:
length
personalizationStatus
selectLayer3Payload:payloadIndex:
T@\"NSNumber\",C,V_securityDomain
T@\"NSNumber\",C,V_realHdcpKeyPresent
_needsDevicePersonalization
expandPayloadWithHeader:payloadIndex:
initWithData:assetUUID:tmpFolderPath:
reofferFirmwareOnSync
_actualOffset
addPayload:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
initWithData:offset:length:subFileTag:
lastAction
payloadIndex
stringWithString:
updateSubfileOffset:
T@\"NSNumber\",C,V_ftabGeneration
_bootNonceAsTLV
TS,R,V_lastApplyStatus
_chunkSize
_engineType
_personalizationQueue
_tlvLength
initWithBVERString:
setProductType:
TQ,R,V_releaseVersion
_asset4cc
appendDataBlockToURL:
encodeWithCoder:
payload4cc
trusted
TC,R,V_provisioning
TQ,V_processingStatus
assetFullyStaged:status:
upstreamEndpoint
stringFromDate:
addToVersion:
notifyEndpointReachable
parameterName
setGeneration:
subfileEPRO
unsignedCharValue
_identifierString
_manifestEpoch
initWithURL:offset:length:subFileTag:
measurementsForDevicePersonalizationNonFTAB
Tc,R,V_char1
count
layer2CallbackLogTxPacket:uarpStatus:
layer2CallbackSendMessage:length:
payloadVersion
setSerialNumber:
_ftabGeneration
T@\"NSString\",R,V_ticketName
initWithFTABPropertyDictionary:
initCommon:
initWithMetaDataHash:
numberWithUnsignedShort:
_nonceSeed
_txBufferOverhead
ftabSuffix
personalizationStateStarted
personalizeFirmwareSuperBinary:tssServerURL:
_payloadVersion
firmwareVariant
T@\"NSString\",R,V_modelLocale
TC,R,V_manifestEpoch
TC,R,V_uidMode
assetPayloadMetaDataTLV:asset:
compressedLength
layer3EndpointAssetStagingProgress:asset:bytesTransferred:assetLength:
irqService
isPropertyListPayload
layer2CallbackSecurityModeResponse:
payloadDataAsData
provisioning
setFtabGeneration:
stopUARPLayer2
keyName
initWithFilePath:assetUUID:tmpFolderPath:
logTxPacket:
setMaxPayloadLength:
setObject:forKeyedSubscript:
setUseGlobalSigning:
setupTemporaryFolder
uarpMessageSendToTransport:
TB,V_autoApply
prepareComposeMetaData
subFileLength
useHostPushModel
TI,R,V_productRevisionMax
TQ,R,V_subFileOffset
_isHostRole
expandSuperBinaryMetaData:offset:
isEqualToNumber:
layer2CallbackRealHdcpKeyPresentResponse:
layer3EndpointPayloadDataComplete:asset:payload:
_packetCapture
assetPayloadDataComplete:hash:
unsignedLongLongValue
_offset
TQ,R,V_buildVersion
lastError
layer2CallbackSolicitedDynamicAssetOffered:asset:
osVersion
T@\"NSNumber\",C,V_provisioning
_disableRetries
T@\"NSData\",C,V_fdrRootCaDigest
_certificateEpoch
_parameterName
_payloadsURL
appendData:
initWithSubfileTag:
T@\"NSData\",R,V_payloadHash
T@\"NSNumber\",C,V_uidMode
T@\"UARPComponentTag\",C,V_componentTag
TI,R,V_isRequired
TI,R,V_tlvLength
numberWithLength:value:
assetID
TQ,R,V_payloadIdentifier
Tq,R,V_hashAlgorithm
_chipRevision
assetMetaDataTLV:
componentsSeparatedByString:
findMatchingAsset:
setPrefixNeedsLUN:
T@\"NSData\",R,V_dataToSign
.cxx_destruct
TI,R,V_chipEpoch
_compressedLength
_preflightInfoProperties
_tag
addSoCLiveNonce:componentTag:tatsuTicket:keyName:
layer2CallbackModelNameResponse:
log
TC,R,V_prefixNeedsLogicalUnitNumber
_matchingData
flashSectionLength
layer2CallbackReturnBuffer:
needsSHA512
packetCapture
securityMode
_enableFutureFWVersion
_realHdcpKeyPresent
acceptLayer3Asset:
array
layer2CallbackDataTransferPaused
layer2CallbackUnsolicitedDynamicAssetOffered:
layer3EndpointRemoteNotResponding:
manifestEpoch
T@\"NSNumber\",C,V_chipRevision
TQ,V_payloadWindowLength
_index
_propertyListVersion
attributesOfItemAtPath:error:
coreName
solicitDynamicAsset:assetTag:
T@\"NSString\",C,V_hwFusingType
TQ,R,V_totalBytesRequested
_isRequired
_manifest
algorithm
demotionProductionMode
objectAtIndexedSubscript:
prepareBulkQueriesForPersonalization:
isValid
T@\"NSNumber\",C,V_certificateEpoch
_buildVersion
_pausedLocal
_payloadDataInternal
_personalizedData
appendFormat:
discoverEndpointIDs
composeMetaData
_tlvType
layer2CallbackDownstreamRecvMessage:uarpMsg:
layer2CallbackLifeResponse:
layer2CallbackProtocolVersionSelected:
layer2CallbackStagedFirmwareVersionResponse:
objectForKey:
packetsMissed
setNumberStyle:
TB,V_upgradeOnly
TI,R,V_demotionProductionMode
enumerateKeysAndObjectsUsingBlock:
friendlyName
hostDefaultOptions
productGroup
productionModeHostOverride
T@\"NSArray\",C,V_components
_epro
fileURLWithPath:isDirectory:relativeToURL:
initWithUTF8String:
_manifestSuffix
dfuStage:error:
T@\"NSNumber\",C,V_boardID32
TI,R,V_demotionSecurityMode
_productRevisionMax
layer2CallbackSuffixNeedsLogicalUnitNumberResponse:
manifestSuffix
notifyEndpointPayloadDataComplete:payload:
TC,R,V_isPropertyList
assetAllHeadersAndMetaDataComplete:
isFTAB
layer2CallbackDataTransferResumed
payloadTags
personalizeFirmwareSuperBinaryInternal:tssServerURL:
stringWithContentsOfURL:encoding:error:
tlvFromType:length:value:
T@\"NSNumber\",C,V_apBoardID
queryPersonalizationTags:error:
_apChipID
_internalQueue
initWithProjectSourceVersion:projectBuildVersion:
layer3EndpointAssetMetaDataComplete:asset:
removeItemAtPath:error:
removeObjectForKey:
_char3
layer3EndpointPayloadReady:asset:payload:
setCompressedDataBlock:offset:
stageFirmwareSuperBinary:tssServerURL:
T@\"NSNumber\",C,V_boardID64
T@\"NSString\",R,V_hardwareFusing
T@\"NSMutableArray\",C,V_outstandingAppleProperties
T@\"NSNumber\",C,V_life
TB,R,V_needsSHA256
TI,R,V_batteryLevel
_layer2AssetCallbacks
_logFunction
startUARPDevice
```
