# `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,420,864 bytes.

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
uarpPlatformEndpointRecvMessage
-[Tcon init]
FirmwareVersion
Property List Payload
Upload Denied  - Better Transport
success
Board ID (64-bit)
Security Domain
Component Tag
Mismatch UUID
Invalid Message Length
com.apple.banyan
<%@: %@>
Manufacturer Name
-[UARPSuperBinaryLayer3 expandPayloadWithHeaderAsURL:payloadIndex:payload4cc:payloadVersion:payloadMetaData:]
bst2
Use Global Signing
chipRevision=%@ \n
Personalization Payload Demotion Security Mode
sysdiagnose
Apple Info Real Hdcp Key Present
RealHdcpKeyPresent
-[UARPSuperBinaryLayer3 expandPropertyListPayload:payloadIndex:]
Asset Available Notification Ack
Endpoint Bulk Information Request
EcidData
Board ID (32-bit)
Apple Info Chip Revision
-[UARPEndpointLayer3 acceptLayer3Asset:]_block_invoke
%s: Tatsu Ticket %@
\xf0\xb1
-[UARPEndpointLayer3 checkPropertyQueryComplete]_block_invoke
Logical Unit Number
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
Data Request
EPRO
Upload Denied  - Same Version Staged
Hardware Specific
Key Name: %@, 4CC: %@, TLV 0x%08x
-[UARPEndpointLayer3 notifyEndpointReachable]
AppleTconUARPUpdater: entering TCON Get Tags.
AppleTconUARPUpdater: Failed to query tags from TCON
Host Personalization Required
Personalization FTAB Payload
Downstream Msg Name
fgvl
Baobab,ProductionMode
Real HDCP Key Present
SocLiveNonce
Apple Info Logical Unit Number
AppleTconUARPUpdater: Reachable Devices.
Asset Id Unknown
Nonce
Upload Abandoned  - Better Transport
SecurityDomain
Deployment Rule Percentage
Apple Info Ap Board ID
Apple Info Personalization Nonce Seed
%s-%@-%@.pcap
Personalization SoC Live Nonce
securityDomain=%@ \n
Needs ESEC
,%lu
-[UARPSuperBinaryPayloadLayer3 generatePayloadHash:measureOffset:measureLength:]
<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>
Active Firmware Version Equal to Asset
-[Tcon onTconIrq]
Personalization Matching Data Product Revision Minimum
device/assets/heysiri
Upload Denied  - Same Asset Tag In Progress
-[UARPSuperBinaryLayer3 addTatsuTicketManifest:ticket:manifestLocation:payload:]
Asset Data Paused
Sending Firmware Data for DFU Stage
Mapped Analytics Apple Model Number
Payload Filepath
Chip Revision
No Version Agreement
Personalization Failure
AppleTconUARPUpdater: TCON Manager is nil, returning.
<%@: Algorithm %u, Actual Offset %u, Compressed Length %u, Uncompressed Length %u>
Personalization Payload Demotion Production Mode
<Type = 0x%08x, Length = 0x%08x>
Apple Info ECID Data
Payload Header\n
Invalid Offset
AppleTconUARPUpdater Error: TCON nil ECID Data
Failed to get personalization info from Asset
Personalization More Requests to Follow
Until Day
Payload Certificate
Asset Corrupt
SHA-256
Compose Payload Hash Algorithm
-[UARPSuperBinaryPayloadLayer3 composePayload]
Asset Transfer Complete
IS
Duplicate Accessory
Personalization FTAB Payload Production Mode
Compose MetaData Hash Algorithm
Upload Abandoned  - Higher Version
Components
tcon-registers
Certificate Epoch
FTAB:\n
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionary:]
AppleTconUARPUpdater: Setting Debug Register Access in TSS Request.
blt2
Life
UNKNOWN
Ticket Construction Failure
Live Nonce
queryPersonalizationInfo
Payload Compression Algorithm
-[BanyanUARPUpdaterDevice layer3EndpointAssetFullyStaged:txFirmwareAsset:]
Property Value
superbinary.uarp
Invalid Object
%s (%s)
Unknown Accessory
Asset No Bytes Remaining
-[Tcon currentOperationalMode]
FirmwareData
Personalization FTAB Payload Production Mode Host Override
Upload Abandoned  - Device Error
Successfully DFU Staged TCON Firmware
queryInfo
Payload Hash Algorithm
Deployment Rules
%@\n
-[Tcon setFusingType:error:]
\tValid: %u\n
Apple Info Requires Personalization
Version Discovery Request
uarpMsgRecvDownstreamEndpointUnreachableAck
Serial Number
Personalization FTAB Payload Digest
ticketLongName=%@ \n
uidMode=%@ \n
Security Mode
SuperBinary Header\n
Apple Info Board ID
AppleTconUARPUpdater: Update Firmware with Dictionary.
realHdcpKeyPresent=%@ \n
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackUnsolicitedDynamicAssetOffered:assetTag:]_block_invoke
Processing Incomplete
Required Personalization Option
Personalization Payload Trusted
superbinaryAsset
Personalization Manifest Suffix
Personalization Payload Tag
Key Name
-[UARPEndpointLayer3 rescindAssets]_block_invoke
AppleTconUARPUpdater: Transport is nil, returning nil.
Trusted
Personalization Payload Hash Algorithm
majorVersion
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetReady:]_block_invoke
Personalization Chip Epoch
Upload Abandoned  - Processing Error
Upload Abandoned  - Personalization Failure
Payload Window Length
device/assets/crash
HeySiri Model Signature
Cancelled - No Network
Staged Firmware Version Greater than Asset
Unable to find Manifest Data as TLV on superbinary
FDR Signature
-[UARPEndpointLayer3 queryOutstandingEndpointIDComponentProperties:]
AppleTconUARPUpdater Error: TCON nil Chip ID
build
Prefix Needs LUN
-[UARPEndpointLayer3 notifyTxDynamicAssetFullyStaged:]
-[UARPSuperBinaryPayloadLayer3 hashPayload]
Corrupt SuperBinary
FTAB Payload
%@-%@-%@
Active Firmware Version
-[UARPSuperBinaryLayer3 setupTemporaryFolder]
Unsupported
Personalization FTAB Payload Security Mode Host Override
Personalization Chip ID
In Use
payload.%lu
Apple Info HW Fusing Type
Apple Info Hardware Specific
char3
-[BanyanUARPUpdaterDevice layer3EndpointPersonalizationNeeded:asset:]
Banyan already fused.
ForceDFU
Personalization Payload Longname
LZBitmap2
Property Name
uarpMsgRecvDownstreamEndpointReachable
HWFusingType
\t\t%@
-[UARPSuperBinaryLayer3 expandPayloadWithHeaderAsData:payloadIndex:payload4cc:payloadVersion:payloadMetaData:]
char2
Personalization Payload
\t
, EPRO %@
AppleTconUARPUpdater: Creating UARPTconDevice.
Apply Staged Assets Response
AppleTconUARPUpdater: entering TCON Create Request.
AppleTconUARPUpdater: Building personalized SuperBinary Asset for TCON.
%s: Tatsu Request for ticket %@
Model Name
-[UARPEndpointLayer3 stageFirmwareSuperBinary:tssServerURL:]_block_invoke
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackApplyStagedAssets]
Error: Input Dictionary is nil \n
-[UARPRTKitFTABSubfile getDataBlock:offset:]
Personalization Nonce
-[UARPEndpointLayer3 notifyLayer2RxFirmwareFullyStaged:]
char1
Invalid Length
-[UARPRTKitFTAB composeFTAB]
Voice Assist Active Model
-[UARPEndpointLayer3 processOutstandingEndpointInfoQueries:infoProperties:]
Version BVER File
SuperBinary Format Version
Needs SHA384
-[UARPSuperBinaryPayloadLayer3 setPayloadURL:]
Downstream Endpoint Message
-[UARPEndpointLayer3 configureEndpointLayer2Tags]
-[UARPEndpointLayer3 sendSyncToPeer]_block_invoke
transmitqueue
SuperBinary: Format Version: %lu, Asset Version %@\n
%@,Ticket
-[UARPEndpointLayer3 notifyRxDynamicAssetFullyStaged:]
Unable to find Bootloader or Bootloader Config on Payloads
Personalization SuperBinary AssetID
0.0.0.0
manifestSuffix=%@ \n
\tNum Subfiles: %d\n
-[UARPEndpointLayer3 notifyEndpointPayloadDataComplete:payload:]
tconUARPManager
Product Type
Payload - 4cc <%@> - Version <%@> - TLVs - %@
Apply Staged Assets Request
Downstream Endpoint Reachable Ack
-[UARPEndpointLayer3 denyAsset:denyReason:]_block_invoke
HeySiri Model Hash
A
pcapfiles
Upload Abandoned  - Unsupported Asset Tag
Attempt AppleConnect
%lu
Mismatch Personalization Option
AppleTconUARPUpdater: PRDocOptions set:\n FuseSDOM: %@,\n FusePROD: %@,\n DebugRegisterAccess: %@,\n ForceDFU: %@,\n LifeCycles: %@,\n SkipPreCalData: %@
Personalization Matching Data Payload Tags
+++++++++++++++++\n
Vendor Specific
AppleTconUARPUpdater: Query Info from TCON Device.
AppleTCONControl
No MetaData
AppleTconUARPUpdater: Cannot Fuse PROD, SDOM is not fused.
PROD
Manifest Location
Needs Trusted
-[UARPEndpointLayer3 selectLayer3Payload:payloadIndex:]_block_invoke
MetaData Overflow
Asset Rescinded Notification
AppleTconUARPUpdater: entering TCON create.
Don't fuse - Banyan in DFU mode.
AppleTconUARPUpdater: In DFU mode - Returning empty dictionary
, 4CC: %@
-[UARPEndpointLayer3 sendMessageUpstream:fromDownstreamID:]_block_invoke
Mismatch Data Offset
ffsc
liveNonce=%@ \n
Upload Abandoned
No Tatsu Measurements
-[UARPEndpointLayer3 noFirmwareAvailable]_block_invoke
Personalization Enable Mix Match
Compressed Headers
Version Simple BVER File
Manifest Destination
+++++++++++++++++++\n
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackActiveFirmwareVersionResponse:]
nonceSeed=%@ \n
%04ld-%02ld-%02ld
Manifest as FTAB Subfile of 4CC: %@
Endpoint Bulk Information Request Ack
Setting Banyan fusing type failed.
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetRescind:]
Personalization SuperBinary Payload Index
Voice Assist Certificate
Invalid Payload Header
AppleTconUARPUpdater: Setting SkipPreCalData Settings: %@
Personalization Matching Data
Subfile: type=%@, length=%lu
SuperBinary MetaData Length : %lu\n
Apple Info Prefix Needs Logical Unit Number
streaming
UARPAssetLayer2CallbacksPayloadMetaDataTLV
<%@: %llu>
Asset Staging Still In Progress
Minimum visionOS Version
Priority Activity
AppleTconUARPUpdater %s: TCON asset staging complete with success
%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@
Downstream Msg Type
-[UARPEndpointLayer3 processOutstandingComponentInfoQueries:infoProperties:]
-[UARPEndpointLayer3 notifyEndpointPayloadMetaDataComplete:payload:]
-[UARPEndpointLayer3 notifyAssetSolicited:]
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryKeyValuePayload]
Dynamic Asset PreProcessing Notification Ack
BuildIdentityTags
manifestPrefix=%@ \n
Measure Offset
Upstream Endpoint UUID
Downstream Msg msgID
Downstream Endpoint Discovery
InfoArray
enableFutureFWVersion=%@ \n
Invalid
Upload Denied  - Device Error
Dynamic Asset Solicitation Ack
Endpoint Discovery Request
-[BanyanUARPUpdaterDevice layer3EndpointAppliedStagedAssets:layer3Flags:]
-[Tcon setRestoreUpdaterDelegate:]_block_invoke
Compose Measured Payloads
PMAP
Personalization Provisioning
Fdr Root Ca Digest
-[UARPEndpointLayer3 personalizeFirmwareSuperBinaryInternal:tssServerURL:]
AppleTconUARPUpdater: Saving PR Doc options.
Version File
Voice Assist Digest
HeySiri Model Engine Version
, Trusted %@
Payload Headers Offset      : %lu\n
-[UARPEndpointLayer3 personalizeFirmwareSuperBinary:tssServerURL:]_block_invoke
In Progress
SecurityMode
Firmware (RX)
ROOT
Msg Type
Apple Info Personalization Manifest Epoch
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadReady:]_block_invoke
HigherVersion
ProductionMode
YES
Personalization Manifest Epoch
Until Month
Property List Digest Path
Upload Denied  - Personalization Failure
-[UARPSuperBinaryLayer3 initWithLayer2Context:assetTag:tmpFolderPath:]
%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>
AppleTconUARPUpdater: Updater Querying Information.
Failed to set TCON into DFU Mode
Personalization Matching Data Product Revision Maximum
Staged Firmware Version
Personalization Security Mode
i
%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>
Same Version Active
AppleTconUARPUpdater: successfully copied firmware.
Upload Denied  - Same Version Active
-[UARPEndpointLayer3 downstreamEndpointUnreachable:downstreamEndpointID:]_block_invoke
>
hardwareSpecific=%@ \n
<%@: %lu until %@>
%s
-[UARPEndpointLayer3 notifyAssetPersonalizationNeeded:]
AppleTconUARPUpdater: Failed to fuse PROD for TCON Device
-[UARPSuperBinaryPayloadLayer3 compressPayload]
Invalid Asset Type
Asset Data Transfer Notification
Format Version              : %lu\n
Upstream Endpoint ID
fvgl
Personalized Manifest
memory
chipEpoch=%@ \n
Cancelled
%lu.%lu.%lu.%lu
Hw Fusing Type
Apple Info Security Domain
Data Response
AppleTconUARPUpdater: Query Tags from Device
StagedFirmwareVersion
FusePROD
device/assets/mappedanalytics
Manifest Epoch
%c%c%c%c
Apple Info Manifest Prefix
Key Name: %@
Payload Data Length     : %lu\n
Information Request
ftpl
device/assets/voiceassist
|
2
blt3
Allow Flash Write
Upload Denied
Invalid Data Transfer Notification
assert
Creating Asset failed
Voice Assist Hash
Personalization Digest List Size
Manifest Suffix
Payload Data Offset     : %lu\n
protocolaccessory
Baobab,Life
Minimum Required Version
nonce=%@ \n
Hardware Fusing
Baobab,DebugRegisterAccess
Uncompressed Payload Length
MetaData Hash
Requires Personalization
-[UARPEndpointLayer3 notifyTxFirmwareFullyStaged:]
Invalid Asset Tag
Voice Assist Engine Version
Personalization FTAB Payload Hash Algorithm
Chip Epoch
-[UARPSuperBinaryPayloadLayer3 composePersonalizedFTAB]
v8@?0
@%@
v32@?0@\"NSString\"8@16^B24
FDR Parameter Name
Percentage Limit
Property List Version Path
-[UARPEndpointLayer3 notifyAssetStagingProgress:bytesTransferred:assetLength:]
Invalid Message
com.apple.uarp.layer3
AppleTconUARPUpdater: Banyan in DFU Mode, taking it out, isDone = False.
Expanding New Asset failed
uarpMsgRecvDownstreamEndpointMessage
Manifest Property
Apple Info Apple Model Number
Unsupported Message Type
HeySiri Model Certificate
AppleTconUARPUpdater: Updater Querying Personalization Information.
-[Tcon dfuInfo:]
Personalization Real Hdcp Key Present
FTAB Boot Nonce
https://gs.apple.com:443
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackModelNameResponse:]
downstream
Compose Measured Payloads (Non-FTAB)
fwrg
AppleTconUARPUpdater: Excluding Calibration Data
-[Tcon getFusingType:error:]
AppleTconUARPUpdater: Building Excluded Payloads
Baobab,TCON
MetaData Hash Algorithm
No Resources
Better Transport
Nothing Staged
Manifest as MetaData of %@
Header Length           : %lu\n
-[UARPSuperBinaryPayloadLayer3 setDataBlockToURL:offset:url:]
AppleTconUARPUpdater: Update Device Firmware with Data
UID Mode
Higher Version Active
Endpoint Discovery Response
endpoint
IS NOT
Downstream Endpoint Reachable
Trying to set TCON into DFU Mode
Options
FTAB Properties
-[UARPEndpointLayer3 handleProtocolVersionSelected:]
AppleTconUARPUpdater: Updater update firmware with Dictionary.
, offset=%lu
Success
Dynamic Asset (RX)
Product Number
-[UARPSuperBinaryLayer3 updateIncomingAssetProperties:]
Apple Info ECID
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadMetaDataComplete:]_block_invoke
Successfully fused
UARP.LAYER2 <%s> Cannot find downstream endpoint
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryTLVs:]
Server Unreachable
-
Ticket LongName
Protocol Version
Unknown Personalization Option
Personalization FTAB Payload Trusted
AppleTconUARPUpdater: Successfully restored TCON.
Manifest Locations
-[UARPEndpointLayer3 directConfiguration]_block_invoke
-[UARPSuperBinaryPayloadLayer3 decompressPayload]
product
Information Response
Device Error
Firmware Variant
Apple Info Ap Production Mode
assets
SuperBinary MetaData
Personalization Tickets
Flash Section Length
-[UARPEndpointLayer3 stopUARPLayer2Internal]
-[UARPEndpointLayer3 notifyRxFirmwareFullyStaged:]
Payload MetaData Length : %lu\n
Upload Abandoned  - MetaData Overflow
Invalid Payload
UARPSuperBinaryProcessMetaData
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
-[Tcon uarpMessageSendToTransport:]
provisioning=%@ \n
Idle
Invalid Data Response Length
Error: Missing Firmware Data from inputOptions\n
AppleTconUARPUpdater %s: TCON Manifest in Superbinary
Measure Length
IOGeneralInterest
Personalization Nonce Hash
FDR Data To Sign
HeySiri Model Locale
Unknown
-[UARPSuperBinaryPayloadLayer3 getDataBlock:offset:]
AppleTconUARPUpdater: No TCON Devices, returning nil.
sysdiagnose_approved
NO
Downstream Endpoint Unreachable
AppleTconUARPUpdater:Security Domain is false, setting Provisioning.
Crash Analytics Test Mode
Payload Compression ChunkSize
Upload Denied  - Cancelled Asset Tag
%c%c
-[UARPSuperBinaryLayer3 expandPayloadHeadersAndMetaData:offset:]
-[UARPEndpointLayer3 craftTatsuRequests:]
Error: TSS Request is nil for TCON \n
AppleTconUARPUpdater: Query Info failed on TCON Device.
BoardId
Until Year
%02x
0x
ECID=%@ \n
,%@
\n
UARPAssetLayer2CallbacksAssetMetaDataTLV
Upload Abandoned  - Update In Progress
-[Tcon dfuStage:]
, FTAB Subfile: %@
packetCapture
AppleTconUARPUpdater: Overwriting Debug Register Access: %@
Incompatible Protocol Version
Endpoint Component Discovery Request
AppleTconUARPUpdater: Finished DFU stage - sleeping.
fbsr
SHA-384
%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@
-[UARPSuperBinaryLayer3 addPayloadWith4cc:payloadVersion:payloadIndex:]
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryPropertyListPayload:]
Downstream Endpoint Message Ack
DebugRegisterAccess
Personalization Payload Effective Production Mode
SuperBinary Firmware Version
%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
Asset Invalid Compression
Personalization Manifest Prefix
Upload Denied  - Priority Activity
Upload Abandoned  - Higher Version Staged
Upload Abandoned  - Cancelled Asset Tag
boardID64=%@ \n
Apple Info Nonce
AppleTconUARPUpdater: Fusing SDOM Banyan Device
Ap Chip ID
Apple Info Ticket Long Name
Accessory
AppleTconUARPUpdater Error: TCON nil Security Mode
fdvc
bfwc
ECID
AppleTconUARPUpdater: Building superbinary data failed with %@
-[UARPSuperBinaryPayloadLayer3 generateHash:ftabSubfile:]
Error decompressing buffer for payload
-[BanyanUARPUpdaterDevice stageFirmwareWithDictionary:error:]
Msg Payload Length
/
AppleTconUARPUpdater: Failed to apply firmware a for TCON Device
Vendor Version String File
Personalization Logical Unit Number
LZBitmapFast2
FTAB %@:\n
Endpoint Bulk Information Response Ack
Getting Banyan fusing type failed.
Deployment Rule Country
-[UARPEndpointLayer3 downstreamEndpointRemove:]_block_invoke
Apple Info Chip Epoch
-[BanyanUARPUpdaterDevice layer3EndpointAssetPersonalizationComplete:asset:status:]
Voice Assist Role
logicalUnitNumber=%@ \n
Manifest as MetaData 
Needs Restart
, SHA-512 as %@
Apple Info Ap Chip ID
Unsupported Hardware Revision
Allow Unsealed Data
Host Minimum Battery Level
Mapped Analytics Event ID
-[UARPSuperBinaryLayer3 getDataBlock:offset:]
HSML
ESEC
Needs SHA512
-[UARPEndpointLayer3(Layer2VendorCallbacks) layer2CallbackHwFusingTypeResponse:]
Downstream Endpoint Discovery Ack
No Firmware Update Available
AppleTconUARPUpdater: Overriding Life Cycles on TSS Request.
chipID=%@ \n
Nonce Seed
Upload Complete (Reboot Required)
Manifest Prefix
Apple Info Enable Mix Match
com.apple.uarp.embedded
Firmware (TX)
Msg Name
-[UARPEndpointLayer3 startUARPLayer2Internal]
-[UARPEndpointLayer3 uarpRouteRecvMessageToDownstreamEndpoint:downstreamEndpointID:]_block_invoke
Host Trigger Battery Level
Needs SHA256
Enable Future FW Version
\tSubfiles: (Offset=0x%08zx) %zu\n
Upload Denied  - Low Battery
Ap Security Mode
-[UARPSuperBinaryLayer3 expandSuperBinaryPropertyList]
-[UARPSuperBinaryPayloadLayer3 initWithPayload4cc:payloadVersion:payloadIndex:baseURL:]
%02ld-%02ld-%02ld
, SHA-256 as %@
uarpMsgRecvDownstreamEndpointUnreachable
Unknown Asset
Upload Denied  - Processing Error
Version Marketing BVER File
-[UARPSuperBinaryPayloadLayer3 setDataBlockToData:offset:payloadData:]
Error: Query Personalization Info Input Dictionary is nil
Upload Abandoned  - Priority Activity
Not Auth Listed
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetPayloadData:offset:asset:]_block_invoke
Asset Data Transfer Notification Ack
fwlc
-[UARPEndpointLayer3 acceptLayer3Payload:]_block_invoke
HeySiri Model Role
Payload Hash
Personalization FTAB Payload Security Mode
Max Payload Length
-[UARPSuperBinaryLayer3 expandSuperBinaryPlist]
UARPEndpointLayer3: %@
Apple Info FTAB Generation
Dynamic Asset Solicitation
AppleTconUARPUpdater: removing Payload: %@
PLST
Payload 4CC
Apple Info Personalization Manifest Suffix
Unknown Failure
protocolcontroller
AppleTconUARPUpdater %s: TCON info queries complete
Asset Identifier
Personalization FTAB Payload Tag
releaseVersion
Asset Length                : %lu\n
%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>
tcon-api
Upload Denied  - Unsupported Asset Tag
FTAB Subfile
AppleTconUARPUpdater: Setting Force DFU to each banyan %@
boardID32=%@ \n
, Static Value %@
Payload Tag             : %c%c%c%c\n
Invalid TLV
Error: Unable to validate Firmware for TCON\n
AppleTconUARPUpdater: Overwriting SkipPreCalData: %@
SuperBinary Payloads
Property List Path
Ap Production Mode
Header Length               : %lu\n
-[UARPSuperBinaryPayloadLayer3 getDataRangeFromURL:]
psf0
-[BanyanUARPUpdaterDevice layer3EndpointReachable:]
Ignore Version
Object Properties
fdrg
, hash=%@
-[UARPRTKitFTAB expandFileTable:]
com.apple.uarp.endpoint.packet.parser
-[UARPEndpointLayer3 notifyDownstreamEndpointUnreachable:]
AppleTconUARPUpdater: Query Tags from TCON Device.
Payload Version
TCON already in DFU Mode
Upload Abandoned  - Same Version Staged
-[UARPSuperBinaryPayloadLayer3 cachePayloadData]
Unknown Data Transfer State
Buffer Would Overflow
Payload Expand Filename
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackSerialNumberResponse:]
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackStagedFirmwareVersionResponse:]
Payload Identifier
Friendly Name
Request Failure
-[UARPEndpointLayer3 uarpMessageRecvFromTransport:]_block_invoke
Apple Info Personalization Life
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackFriendlyNameResponse:]
FDR Data
HeySiri Model Digest
Personalization Payload Effective Security Mode
-[UARPRTKitFTAB getDataBlock:offset:]
-[UARPEndpointLayer3 notifyEndpointRemoteNotResponding]
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetProcessingCompletedAck:]_block_invoke
\xf0\xf0\xf0\xf0a
Personalization FTAB Payload Digest Filename
-[UARPEndpointLayer3 processRespondedEndpointInfoQueries:tlvs:]
-[UARPEndpointLayer3 notifyAssetPersonalizationComplete:status:]
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc31
personalizedPayload.%lu
platform
Invalid Data Request Offset
Error: Firmware Data is corrupt\n
Crash Analytics Apple Model Number
AppleTconUARPUpdater: Fusing PROD Banyan Device
bst0
Percentage Rules
Upload Denied  - Higher Version Staged
HeySiri Model Engine Type
Apple Info Personalization Provisioning
AppleTconUARPUpdater: In DFU mode - Query Personalization DFU Info
\tBoot Nonce: 
-[UARPSuperBinaryLayer3 getDataRangeFromURL:]
BoardID
-[UARPEndpointLayer3 notifyApplyStagedAssets]
Apple Info SoC Live Nonce
Downstream Endpoint Unreachable Ack
AppleTconUARPUpdater: entering TCON Copy Firmware.
-[UARPRTKitFTAB getDataRangeFromURL:]
In Flight
, SHA-384 as %@
Endpoint Component Discovery Response
ChipID
of 4CC: %@
Dynamic Asset (TX)
Apple Info Production Mode
securityMode=%@ \n
<unknown>
Upload Denied  - MetaData Overflow
Invalid Function Pointer
AppleTconUARPUpdater: Overwriting Fusing SDOM: %@
Payload Identifier String
None
%@:\n
Version Discovery Response
Personalization Board ID
Hardware Version
AllAMN.tmap
Out Of Order Message ID
Voice Assist Type
Country
endpointDatabase
Endpoint UUID
IM4M
Unknown Downstream Endpoint
AppleTconUARPUpdater %s: TCON personalization info queries complete
AppleTconUARPUpdater Error: TCON nil HW Fusing Type
Minimum watchOS Version
Unknown Payload
Duplicate Message ID
Same Version Staged
Personalization FTAB Payload Longname
-[UARPRTKitFTABSubfile getDataRangeFromURL:]
Upload Denied  - Higher Version Active
Processing Error
Creating New Asset failed
Excluded Hardware Version
-[UARPSuperBinaryLayer3 expandPropertyListPayloads:]
Downstream Msg Payload Length
<%@: %@ until %@>
AppleTconUARPUpdater: Creating TCON Updater Manager.
Digest
Personalization ECID
Urgent Update
:
AppleTconUARPUpdater:Security Domain is true, removing Provisioning for Tatsu.
Expanding Asset failed
Personalization ECID Data
cachedassets
Attempt Auth Listed
Needs EPRO
bst1
HeySiri Model Type
Ap Board ID
-[UARPSuperBinaryPayloadLayer3 initWithPayloadData:payloadMetaData:payload4cc:payloadVersion:payloadIndex:]
Staged Firmware Version Equal to Asset
Mid Upload
Controller
Crash Analytics Core Name
\tManifest: (Offset=0x%08x) %@\n
PLACEHOLDER
char4
Invalid Super Binary Header
ResponseTags
enableMixMatch=%@ \n
Personalization Board ID (64 bits)
Active Firmware Version Greater than Asset
Cancelled Asset Tag
\tSubfiles:\n
Payload Signature
Upload Abandoned  - Same Asset Tag In Progress
SHA-512
Asset Available Notification
SkipPreCalData
ecidData=%@ \n
Voice Assist Signature
Upload Denied  - Higher Version
-[UARPEndpointLayer3 processRespondedComponentInfoQueries:tlvs:]
Unknown Message Type
Payload MetaData Offset : %lu\n
Personalization Prefix Needs Logical Unit Number
productionMode=%@ \n
Chip ID
AppleTconUARPUpdater %s: TCON asset apply complete with flags:%ld
Minimum macOS Version
Firmware Version
Apple Info Asset Identifer
Payload Version         : %lu.%lu.%lu.%lu\n
com.apple.banyan.uarp
HeySiri Model Active Model
-[UARPEndpointLayer3 notifyPayloadReady:payload:]
Asset In Flight
Exceeded Packet Retry
<%@: %u>
updv
-[UARPEndpointLayer3 notifyEndpointAppliedStagedAssets:]
AppleTconUARPUpdater: Creating Device.
device/assets/logs
UARPLayer3UtilsCleanFileHandleForWriting
Asset Decompression Failure
Low Battery
AppleTconUARPUpdater: Banyan came back from applying, sleeping
Baobab,Ticket
tmapdatabase
ftabSubfile
DownstreamEndpoint Endpoint ID
Invalid Data Request Length
-[UARPSuperBinaryLayer3 prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:]
-[UARPEndpointLayer3 applyStagedAssets]_block_invoke
4CC: %@, Property 0x%08x
Upload Abandoned  - Same Version Active
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackRescindAllAssets]
Duplicate Controller
AppleTconUARPUpdater %s: TCON asset staging complete
Personalization Required
ftabSuffix
Apple Info Personalization Nonce Hash
Invalid Argument
blt1
Crafting Tatsu Request
life=%@ \n
AppleTconUARPUpdater: TCON Asset failed to stage with failure: %@
Upload Abandoned  - Low Battery
Apple Info Chip ID
0x%08x
buildVersion
-[UARPEndpointLayer3 nextLayer3Payload:]_block_invoke
-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:tlvs:]
LifeCycle
Baobab,Provisioning
SuperBinary Version         : %lu.%lu.%lu.%lu\n
-[UARPEndpointLayer3 notifyAssetOffered:]
No Firmware Update Available Ack
AppleTconUARPUpdater Error: TCON nil Board ID
}
Unknown Controller
Asset Processing Notification
AppleTconUARPUpdater: Created UARPTconDevice
Minimum iOS Version
Upload Complete
-[UARPEndpointLayer3 solicitDynamicAsset:assetTag:]_block_invoke
MetaData Corrupt
minorVersion
DownstreamEndpoint Endpoint UUID
AppleTconUARPUpdater: In DFU mode - Query DFU Info (noop)
Asset Not Found
Enable Mix Match
SDOM
\tGeneration: 0x%08x\n
TCON is not staging DFU Firmware
----------------------------\n
-[UARPEndpointLayer3(Layer2AssetCallbacks) assetAllHeadersAndMetaDataComplete:]_block_invoke
compressedPayload.%lu
Invalid Data Request Type
Failed to create Tatsu Request
-[UARPEndpointLayer3 discoverEndpointIDs]_block_invoke
Dynamic Asset PreProcessing Notification
-[Tcon switchOperationalMode:]
<%@:
FDR Context
Personalization Chip Revision
.
-[UARPEndpointLayer3 assetFullyStaged:status:]_block_invoke
-[UARPSuperBinaryPayloadLayer3 personalizedData]
Endpoint Bulk Information Response
-[UARPEndpointLayer3 queryOutstandingEndpointIDProperties:]
AppleTconUARPUpdater: Overwriting Fusing PROD: %@
Days From Compose
Product Group
-[Tcon resetDevice]
++++++++++++++++\n
-[UARPSuperBinaryPayloadLayer3 preparePersonalizedURL]
Upload Abandoned  - Higher Version Active
Not Needed
-[UARPSuperBinaryLayer3 expandSuperBinaryHeader]
Msg Downstream ID
-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]_block_invoke
PersonalizationInfo
Upload Denied  - Update In Progress
<Payload: %@, Version %@> 
Msg msgID
-[UARPEndpointLayer3 notifyEndpointAssetMetaDataComplete:]
FuseSDOM
Payload Long Name
Manifest Properties
Apple Info Ap Security Mode
-[Tcon uarpMessageSendToDevice:]
metrics
com.apple.uarp.endpoint.layer3
ftabGeneration=%@ \n
psf2
performNextStage
Personalization Life
device/assets/personalization
Failure
Endpoint ID
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackManufacturerNameResponse:]
UARP Tatsu Options: { \n
com.apple.uarp.endpoint.layer3.tss
Invalid EndpointID
%lu-%lu-%lu
Asset Processing Notification Ack
tconuarpqueue
suffixNeedsLUN=%@ \n
yyyy-MM-dd
device/assets/analytics
-[UARPEndpointLayer3 notifyEndpointRescindedStagedAssets]
%@
TCON Updater Device: Failed to create Layer2
Ticket Name
Payload Ordered Index
Invalid Data Response
Personalization Payload Digest
Personalization Production Mode
btfw
uarp
FTAB Generation
Country Rules
Boot Nonce Location
Getting Banyan fuse.
Production Mode
-[UARPEndpointLayer3 notifyEndpointPayloadData:payload:offset:payloadData:]
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackSendMessage:length:]_block_invoke
Buffer Overflow
AppleTconUARPUpdater: Failed to stage firmware with Data for TCON Device
AppleTconUARPUpdater: Starting UARP Devices for TCON
Shared Manifest
Apple Info Suffix Needs Logical Unit Number
-[UARPSuperBinaryPayloadLayer3 initWithPayloadURL:payloadTlvs:payload4cc:payloadVersion:payloadIndex:]
-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryData:]
%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p
fwdl
im4m
prefixNeedsLUN=%@ \n
Provisioning
Payload MetaData
Manifest as FTAB Suffix of 4CC: %@
AssetIdentifier
Unknown Information Option
-[UARPRTKitFTAB appendDataBlockToURL:]
Voice Assist Locale
Additional %@:\n
ECID Data
Apple Info Security Mode
-[UARPEndpointLayer3(Layer2VendorCallbacks) layer2CallbackAppleModelNumberResponse:]
MetaData
-[UARPEndpointLayer3 offerDynamicAsset:fourCC:]_block_invoke
com.apple.uarp.packetcapture
AppleTconUARPUpdater: Overwriting Life Cycles: %@
FDR Parameter Data
Personalization Security Domain
-[UARPSuperBinaryLayer3 setupTemporaryFolderForExpand]
-[UARPSuperBinaryLayer3 expandPropertyListTLVs:]
Host Controller
Sync
Baobab,SecurityDomain
Minimum tvOS Version
, ESEC %@
psf1
Object Property: %@
Payload Headers Length      : %lu\n
Asset Rescinded Notification Ack
SuperBinary MetaData Offset : %lu\n
Data Transfer Paused
AppleTconUARPUpdater: Banyan came back setting DFU, sleeping
Personalization Ticket Needs Logical Unit Number
Apple Model Number
-[UARPSuperBinaryLayer3 expandPayloadWithHeader:payloadIndex:]
-[UARPEndpointLayer3 downstreamEndpointAdd:]_block_invoke
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackDiscoveredEndpointIDs:]_block_invoke
uarpTransmitEntryIsValidToSend
, Value %@
-[UARPEndpointLayer3 personalizeFirmwareAssetComplete:]_block_invoke
Unsupported Asset Tag
manifestEpoch=%@ \n
Suffix Needs LUN
-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackHardwareVersionResponse:]
MetaData Type Not Found
AppleTconUARPUpdater: Failed to fuse SDOM for TCON Device
-[BanyanUARPUpdaterDevice craftTatsuRequest:]
NOT IMPLEMENTED YET - Asset Set Data for SuperBinary <%@> for Endpoint <%@>
%s: Take %@ hash of payload %@ at offset %lu with length of %lu 
%s: payload URL is nil for payload index %lu
%s: Failed to set TCON API
%s: cannot close %@, error %@
%s: SuperBinary Header length is too long; Actual Length is %lu, SuperBinary Headers says %lu
NOT IMPLEMENTED YET - Asset Orphan for SuperBinary <%@> for Endpoint <%@>
%s: offset %lu does not equal %lu 
%s: get data block failed for offset %lu, 
%s: Clear interrupt status (%#x)
Asset Personalization, status is %@. UUID of %@
%s: cannot find endpoint for tatsu ticket; %@
%s: uarpPlatformEndpointAssetAbandon() failed; <%u> %s
Payload Index <%lu> Data Complete for SuperBinary <%@> for Endpoint <%@>
%s: Wrote %u bytes (%#x)
%s: removeItemAtPath %@ failed %@ 
%s: expandPropertyListPayloads: failed to process payloads
%s: Removed Personalizing Asset - %@
%s: Failed to create IONotificationPort
%s: NEW UARP delegate overridden
%s: Missing bootloader asset
%s: Bootloader too small for ITCM and DTCM
%s: Failed to instantiate UARPSuperBinaryPayloadLayer3 at index %lu for %@
----------
%s: %lu Outstanding Apple Properties for endpoint configuration %@
%s: uarpPlatformEndpointSendSyncMsg() failed, status is %s
%s: Bootloader is too small %lu
%s: uarpPlatformEndpointDiscoverEndpointIDs() failed with status is %s
Endpoint %@: Downstream Endpoint Unreachable, ID = %u
%s: closeAndReturnError failed %@ 
%s: composing payload failed
%s: Failed to craft tatsu requests, %@
%s: uarpPlatformGetSupportsBulkInfoQueries() failed %s, %@
%s: could not expand FTAB for payload %@, index %lu
%s: SuperBinary payload file is not present; %@
%s: Someone called me and I'm deprecated, with %@
%s: On Banyan IRQ %#llx [%#llx] (%#x)
%s: Unexpected type for bootloader config asset
%s: closeAndReturnError failed with %@
%s: Block Compression Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
%s: seekToOffset:error: failed with %@
%s: Deny Asset
%s: uarpPlatformEndpointBulkInfoResponse() failed, responseStatus is %s
%s: Tatsu Request for ticket %@
%s: could not instantiate UARPSuperBinaryLayer3 for tag %@ on endpoint %@
%s: setting up payload %lu with file %@
%s: Could not archive property list to payload data
%s: Full Temp Folder is %@
%s: processDeploymentRules: failed to process
%s: configuration id is %lu
%s: Maximum write size exceeded %u
%s: Error querying asset tag -> <%u> %s
%s: Wait for %lu Outstanding Info Properties for endpoint component %@ 
%s: Error preparing solicited dynamic asset -> <%u> %s
%s: %lu configurations
%s: Error offering asset to endpoint -> <%u> %s
uarpPlatformEndpointRecvMessage(length=%lu) failed; <%u> %s
Endpoint %@: Solicit Dynamic Asset %@
NOT IMPLEMENTED YET - Asset Rescinded for SuperBinary <%@> for Endpoint <%@>
%s: Missing manifest asset
%s: created file at path  %@ 
%s: invalid payload header size; expected %lu, but got %u
%s: Failed to deompress buffer, status is %s
%s: SuperBinary Payload index %lu, file is missing; FAIL
%s: uarpPlatformEndpointBulkInfoQuery() failed, status is %s
%s: rescind assets
%s: %c%c%c%c has zero outstanding info properties
Payload Index <%lu> MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s: hash of payload %@ ending offset %lu beyond payload  length of %lu
%s: SuperBinary payload 4cc is not a string
%s: UARP restore updater delegate not set
%s: Unexpected bootloader config length %lu
%s: %@
Failed to init local endpoint, status is %s
%s: uarpPlatformConfigureEndpointIDs() failed, status is %s
%s: Error setting payload index to %lu
%s: Tatsu Ticket %@
%s: RX Firmware Asset Fully Staged, status is %lu. Asset Verison is %@. Staged Version is %@. UUID of %@
%s: NEW UARP delegate set
%s: Failed to write ITCM (%#x)
%s: Solicit Dynamic Asset; 4cc = %@, UUID = %@
NOT IMPLEMENTED YET - Asset Pre Processing Notification Ack for SuperBinary <%@> for Endpoint <%@>
%s: Could not create TLV for uncompressedLength
%s: property list is not a dictionary
%s: no previous ftab associated for payload index %lu
%s: Read UARP packet %u (%#x)
%s: Missing bootloader config asset
Failed to remove downstream endpoint id %lu, status is %s
%s: direct endpoint, no need for downstream routing
%s: Failed to write AUTH (%#x)
%s: Invalid Fusing Type
%s: uarpPlatformEndpointBulkInfoResponseAddTLV() failed, status is %s
%s: cannot find component %@ for tatsu ticket; %@
%s: Could not create hash algorithm tlv (%@) for payload %@
%s: not an FTAB payload for payload index %lu
%s: Invalid mode request
%s: cannot read range (offset %lu, length %lu) from %@, error %@
%s: Unexpected header magic (%02x %02x %02x %02x %02x %02x %02x %02x)
%s: hash of subfile %@ is %@
%s: copied %@ to %@
%s: Payload headers has unexpected excess buffer length of %lu
Endpoint Packet Capture at %@
%s: Cleared UARP Packet Ready (%#x)
%s: Unexpected key TLV type %@
%s: File name for asset is %@
Fully Staged for SuperBinary <%@> for Endpoint <%@>
%s: uarpPlatformEndpointAssetFullyStaged() failed; <%u> %s
%s: failed to append chdr data at compressed offset %lu
%s: Can only provide %d bytes from offset %d of ftab %@
%s: Endpoint %@: Endpoint ID = %d, saved %@
Asset TLV %@ for SuperBinary <%@> for Endpoint <%@>
%s: Compression below tolerance update Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
%s: Requested offset (%d) longer than subfile length %d
Watchdog Expired failed, status is %s
Payload Index <%lu> for SuperBinary <%@> for Endpoint <%@>.updated staged firmware version to %@
All Headers And MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s\n
%s: composing personalized ftab failed
%s: writeRegister %#x (%#x)
%s: RX Dynamic Asset Fully Staged (%@), status is %lu. UUID of %@
%s: Can only provide %d bytes from offset %d of asset %@
%s: skip copying %@ to %@; original file does not exist
%s: asset does not need host personalization %@, UUID of %@
%s: Could not generate hash (%@) for payload %@
%s: Compressed with Algorithm: %lu, Offset: %lu, Compressed Length: %lu, Uncompressed Length: %lu
%s: SuperBinary Payload index %lu value is not an NSArray
%s: readRegister %#x (%#x)
%s: outstandingInfoProperties does not contain %@ (%@), ignoring
%s: SuperBinary payload cannot be compressed; %@
%s: cleanFileHandleForWriting failed %@ 
%s: metadata padding is %lu
Offer Dynamic Asset %@. UUID of %@
%s: Unhandled processing status is %lu. UUID of %@; assume corrupt
%s: Can only provide %d bytes from offset %d of subfile %@
%s: Rescind Staged Assets. UUID of %@
%s: SuperBinary payload version is not a string
%s: Failed to write TCON CONFIG (%#x)
%s: Could not create TLV for 0x%04x of length %u for SuperBinary <%@> for Endpoint <%@>
%s: could not instantiate UARPSuperBinaryPayloadLayer3 for asset %@ on endpoint %@
%s: Adding downstream endpoint id 0x%04x
%s: Apply Staged Assets - Nothing Staged
%s: Phase 1: Wrong FTAB Tag Size
%s: expandPropertyListTLVs: failed to process tlv
%s: Notify Endpoint Reachable, Role %s, %@
%s: Could not find %@ to take measurement
uarpMessageAdjustedForEndpointID() failed; <%u> %s
%s: Endpoint %@: Endpoint ID = %d, not saving %@
%s: Asset Ready SuperBinary <%@> for Endpoint <%@>
%s: Failed to create register IOAVDisplayMemory
%s: Failed to modify date to now for file %@; error %@
Failed to init local endpoint
%s: Accept Layer 3 Payload
Asset MetaData Complete for SuperBinary <%@> for Endpoint <%@>
%s: Error querying payload info to %lu
%s: Error calling uarpPlatformEndpointPayloadRequestData: -> <%u> %s
%s: cleanFileHandleForWriting failed with %@
%s: Failed to connect to AppleTCONControl
%s: Error writing reset sequence (%#x)
%s: Failed to get TCON API
%s: Query Bulk Info Property for endpoint configuration: %@ (%@)
%s: hash of payload %@ adjust length to %lu and ending offset %lu 
%s: Unable to retrieve ECID (%#x)
%s: writeData:error: failed with %@
%s: Requested offset (%d) longer than asset length %d
%s: %@, %@ supported
%s: Interrupt status was %#llx
Failed to send message to downstream endpoint id %lu, status is %s
%s: endpoint base has zero outstanding info properties
Endpoint %@: Solicited Dynamic Asset Offered %@
%s: Error querying asset metadata -> <%u> %s
Payload Index <%lu> MetaData Processing Error for SuperBinary <%@> for Endpoint <%@>
%s: could not decompress payload %@, index %lu
%s: Failed to write boot block (%#x)
%s: cannot seek to offset %lu (subfile length %lu) from %@, error %@
%s: protocol version %u, cannot do downstream routing
%s: bootloader length itcm: %u dtcm: %u
%s: createDirectoryAtPath %@ failed %@ 
%s: not enough data to process a TLV's header
%s: _superbinaryURLis nil
%s: Failed to get compressed header
\n
%s: Send message from downstream endpoint id %lu
%s: uarpPlatformEndpointAssetCorrupt() failed; <%u> %s
Endpoint %@: Superbinary Offer %@
%s: Hash payload %@ started at %@.%@ and completed at %@.%@
%s: Requested offset (%d) longer than payload length %d
%s: Could not read payload url into property list
%s: cannot seek to offset %lu (file length %lu) from %@, error %@
%s: Personalize Asset %@. UUID of %@
%s: Error appending payload data to index %lu
%s: Could not create hash tlv (%@) for payload %@
%s: Removing downstream endpoint
%s: Could not find subfile %@ in %@ to take measurement; let tatsu fail this
%s: could not prepare personalized URL for payload index %lu
%s: createFileAtPath failed %@ 
Failed to query info property %u, status is %s
%s: Found Downstream Endpoint matching Downstream ID %lu, %@
%s: Active Firmware Verison is %@. Staged Firmware Version is %@. UUID of %@
Endpoint %@: Downstream Endpoint Reachable, ID = %u, TLVs = %@
Asset Fully Processed, status is %lu. UUID of %@
%s: hash of payload %@ adjust starting offset %lu 
Asset Processing Notification <%@> for SuperBinary <%@> for Endpoint <%@>
%s: No Data Block, no URL failed 
%s: NEED TO HANDLE DECOMPRESSION AS FILE
%s: Someone called me and I'm deprecated
%s: cannot open %@ for reading, error %@
%s: Added Personalizing Asset - %@
%s: writing to personalized URL failed, %@
%s: Can only provide %d bytes from offset %d of payload %@
%s: Outstanding Info Property %@ (%@)for endpoint component %@ 
%s: Responded Bulk Info Property %@ (%@) for endpoint configuration %@
%s: Unable to determine fusing (%#x)
%s: SuperBinary payload filename is not a string
%s: Failed to read boot status (%#x)
%s: TX Firmware Asset Fully Staged, status is %lu. UUID of %@
%s: uarpPlatformEndpointAssetFullyStagedRequiresReboot() failed; <%u> %s
%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)
%s: [pid=%d] %@\n
%s: Unrecognized TLV key %#x
%s: Requested offset (%d) longer than ftab length %d
%s: metadata length is %lu
%s: no firmware available
%s: Responded Bulk Info Property for endpoint configuration: %@ (%@)
%s: Failed to query payload info for index %lu -> <%u> %s
%s: Interrupt mask is %#llx
%s: Cannot add direct endpoint as downstream endpoint
%s: %c%c%c%c has %d outstanding info properties
%s: component %@ outstandingInfoProperties does not contain %@ (%@), ignoring
%s: Failed to find AppleTCONControl
%s: Outstanding Info Property for endpoint configuration: %@ (%@)
%s: Apply staged assets
%s: Error querying payload metadata -> <%u> %s
%s: fileHandleForWritingToURL %@ failed %@ 
%s: SuperBinary contains no plist
%s: uarpPlatformConfigureEndpointTags() failed, status is %s
%s: failed to prepare firmware <%s> to endpoint %@
Payload Index <%lu> Data (offset %lu, length %lu> for SuperBinary <%@> for Endpoint <%@>
Asset MetaData Processing Error for SuperBinary <%@> for Endpoint <%@>
Payload Index <%lu> Ready for SuperBinary <%@> for Endpoint <%@>
%s: RX Dynamic Asset Processing Complete (%@). UUID of %@
%s: Enable Banyan Interrupt (%#x)
%s: starting firmware authentication
%s: not enough data to process a TLV's value
%s: uarpPlatformRemoteEndpointRemove() failed, status is %s
%s: Next Layer 3 Payload
Asset Release for SuperBinary <%@> for Endpoint <%@>
%s: Failed to read Fusing Register
%s: metadata padded length is %lu
%s: Outstanding Preflight Info Property %@ (%@) for endpoint component %@ 
Failed to add downstream endpoint id = %lu, status is %s
Asset Corrupt for SuperBinary <%@> for Endpoint <%@>
%s: payload length is zero, cannot get block
%s: Unexpected type for bootloader asset
%s: processSuperBinaryPropertyList: failed to process
%s: SuperBinary Payload key's value is not an NSArray
%s: could not read superbinary header
%s: buffer %u
%s: Unexpected type for manifest asset
%s: Unexpected manifest length %lu
Payload Index <%lu> TLV for SuperBinary <%@> for Endpoint <%@>
%s: ftabSubfile is nil
%s: Unmask UARP interrupt (%#x)
%s: Error querying asset version -> <%u> %s
%s: ftab is nil
%s: Failed to create IOAVDisplayMemory
%s: Failed to write bootloader length (%#x)
%s: TX Dynamic Asset Fully Staged, status is %lu. UUID of %@
Endpoint %@: Apply Staged Assets Response, ID = %ld
Endpoint %@: Remote Not Responding
Endpoint %@: Unsolicited Dynamic Asset Offered %@
%s: asset length is zero, cannot get block
%s: Timeout boot status %#x expected %#x
%s: Error querying number of payloads -> <%u> %s
%s: Query Info Properties for endpoint component %@ 
%s: Downstream Endpoints %@
%s: Failed to write DTCM (%#x)
Failed to query Apple info property %u, status is %s
Stage Asset %@. UUID of %@
%s: Added Personalized Asset - %@
%s: Asset %@, processing status is %@, asset type is %@
%s: Transfer Asset
%s: unknown 0x%08x
%s: uarpPlatformQueryEndpointComponentDiscovery() %s
NOT IMPLEMENTED YET - Asset Pre Processing Notification for SuperBinary <%@> for Endpoint <%@>
%s: Unable to retrieve BNCH (%#x)
%s: completed firmware authentication %#x boot ROM %#x (%#x)
%s: cannot copy %@ to %@, error %@
%s: processPersonalizationTickets: failed to process
%s: SuperBinary Header length is unexpected %d
%s: expandPayloadWithHeader failed
%s: Asset <%@> for Endpoint <%@>; payload index %lu has unexpected data length of %d
%s: cannot expand payload index %lu
%s: %lu Outstanding Info Properties for endpoint configuration: %@
%s: Could find subfile %@ for %@
%s:  to create directory at %@ (%@)
%s: _data is nil
Failed to add remote endpoint, status is %s
uarpPlatformEndpointRecvMessage() failed; Type = %s, payload length = %lu, msd id = %lu
%s: Endpoint %@, Cancelling staged assets
%s: failed to append block data at compressed offset %lu
%s: Could not create TLV for value 0x%08x, length %u
%s: Endpoint %@, Role %s. Protocol Version Selected (%lu), previously (%lu).
Endpoint %@: Rescinded Assets Response
UARPMetaDataCrashAnalyticsCoreName
UARPMetaDataDeviceCompressedHeaders
UARPMetaDataPersonalizationNonFTABSubfileESEC
UARPMetaDataPersonalizationSecurityDomain
UARPMetaDataPersonalizationFTABSubfileDigestFilename
UARPEndpointTransportTxProtocol
UARPMetaDataPersonalizationFTABSubfileEPRO
UARPMetaDataPersonalizedManifest
UARPMetaDataHostMinimumVersion_visionOS
Layer2EndpointCallbacks
UARPComponentTag
BanyanUARPUpdaterDevice
UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
UARPMetaDataPersonalizationMatchingData
UARPMetaDataInformationAppleModelNumber
UARPMetaDataPersonalizationFTABPayload
UARPMetaDataDeviceUrgentUpdate
UARPMetaDataComposeVersionStringFile
UARPMetaDataPersonalizationEnableFutureFWVersion
UARPMetaDataPersonalizationRequired
UARPMetaDataHeySiriModelSignature
UARPMetaDataPersonalizationAllowUnsealedData
UARPMetaDataPersonalizationNonFTABSubfileHashAlgorithm
UARPMetaDataDeviceIgnoreVersion
UARPMetaDataPersonalizationProductionMode
UARPMetaDataHostTriggerBatteryLevel
UARPMetaDataHostMinimumVersion_macOS
UARPMetaDataHostMinimumVersion_watchOS
UARPMetaDataHostDeploymentRuleCountry
UARPMetaDataInformationStagedFirmwareVersion
UARPMetaDataPersonalizationSuffixNeedsLogicalUnitNumber
UARPMetaDataPersonalizationNonce
UARPTatsuObjectProperties
UARPMetaDataFdrDataToSign
BanyanUARPTransport
UARPMetaDataPersonalizationNonFTABPayload
UARPHashMachine
UARPMetaDataPersonalizationNonFTABSubfileDigest
UARPMetaDataHeySiriModelEngineVersion
UARPMetaDataHostExcludedHwVersion
UARPMetaDataPersonalizationSecurityMode
UARPMetaDataHeySiriModelEngineType
UARPMetaDataPersonalizationMoreRequestsToFollow
UARPMetaDataPersonalizationFTABSubfileESEC
UARPMetaDataPersonalizationFTABGeneration
UARPMetaDataVoiceAssistSignature
UARPTatsuManifestProperties
UARPMetaDataHostMinimumVersion_iOS
UARPMetaDataPersonalizationFTABSubfileLongname
UARPMetaDataRequiredPersonalizationOption
UARPMetaDataPersonalizationSuperBinaryAssetID
UARPEndpointOptions
UARPEndpointConfiguration
UARPEndpointTransportRxProtocol
UARPMetaDataPersonalizationManifestEpoch
UARPMetaDataPersonalizationLogicalUnitNumber
UARPMetaDataComposePayloadHashAlgorithm
UARPMetaDataComposeMetaDataHashAlgorithm
UARPMetaDataComposeSimpleBVERStringFile
UARPMetaDataFdrContext
UARPRestoreUpdaterDeviceProtocol
UARPMetaDataPersonalizationUIDMode
UARPMetaDataPersonalizationFTABSubfileTrusted
UARPMetaDataPersonalizationDemotionProductionMode
UARPEndpointPacketCapture
BanyanUARPUpdaterManager
UARPMetaDataPersonalizationProvisioning
UARPMetaDataPersonalizationSoCLiveNonce
UARPMetaDataDevicePayloadHashAlgorithm
UARPMetaDataComposeFTABPayload
UARPMetaDataInformationHardwareVersion
UARPMetaDataPersonalizationEnableMixMatch
UARPMetaDataDevicePayloadIdentifierString
UARPMetaDataPersonalizationMatchingDataPayloadTags
UARPMetaDataVoiceAssistDigest
UARPMetaDataPersonalizationTicketNeedsLogicalUnitNumber
UARPMetaDataInformationFriendlyName
UARPMetaDataComposeBVERStringFile
UARPMetaDataInformationHardwareFusing
BanyanUARPUpdaterLog
UARPRestoreDeviceProtocol
UARPMetaDataPersonalizationNonFTABSubfileTrusted
UARPMetaDataPersonalizationUseGlobalSigning
UARPMetaDataPersonalizationChipID
UARPMetaDataPersonalizationBootNonce
UARPTatsuBootNonceLocation
UARPSuperBinaryLayer3
UARPMetaDataFdrParameterData
UARPMetaDataPersonalizationManifestPrefix
UARPRTKitFTABSubfile
UARPMetaDataDeviceMetaDataHash
UARPMetaDataDevicePayloadHash
UARPMetaDataHeySiriModelHash
UARPMetaDataDeviceMetaDataHashAlgorithm
UARPMetaDataVoiceAssistLocale
UARPMetaDataFdrData
UARPMetaDataPersonalizationFTABSubfileDigest
UARPTatsuOptions
UARPMetaDataDeviceCompressPayloadChunkSize
UARPMetaDataMappedAnalyticsEventID
UARPMetaDataFdrParameterName
UARPMetaDataPersonalizationNonFTABSubfileEPRO
UARPMetaDataVoiceAssistType
UARPMetaDataHostPersonalizationRequired
UARPMetaDataHeySiriModelActiveModel
UARPMetaDataHostDeploymentRulePercentage
UARPMetaDataDevicePayloadExpandFilename
UARPMetaDataDevicePayloadOrderedIndex
UARPMetaDataInformationAssetIdentifier
UARPTatsuFTABProperties
UARPEndpointLayer3DelegateProtocol
UARPMetaDataPersonalizationLife
UARPMetaDataPersonalizationSharedManifest
UARPMetaDataHeySiriModelType
NSCoding
UARPMetaDataDeviceFlashSectionLength
UARPMetaDataDeviceVendorVersionStringFile
UARPMetaDataPersonalizationChipEpoch
UARPMetaDataPersonalizationBoardID
UARPMetaDataVoiceAssistCertificate
UARPMetaDataPersonalizationNonceHash
UARPMetaDataDeviceFirmwareVariant
UARPTatsuManifestLocation
UARPMetaDataVoiceAssistRole
UARPMetaDataPersonalizationDemotionSecurityMode
UARPMetaDataPersonalizationPayloadTag
UARPMetaDataDevicePayloadCertificate
Layer2AssetCallbacks
UARPMetaDataPersonalizationPrefixNeedsLogicalUnitNumber
UARPMetaDataHeySiriModelCertificate
UARPComponentVersion
UARPMetaDataHostMinimumVersion_tvOS
UARPLastError
Tcon
NSCopying
UARPMetaDataPersonalizationMatchingDataProductRevisionMin
UARPMetaDataPersonalizationAllowFlashWrite
UARPMetaDataPersonalizationFdrRootCaDigest
UARPMetaDataPersonalizationNonceSeed
UARPMetaDataPersonalizationECIDData
UARPMetaDataPersonalizationFTABSubfileTag
NSSecureCoding
UARPMetaData
UARPMetaDataFdrSignature
UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
UARPMetaDataPersonalizationMatchingDataProductRevisionMax
UARPMetaDataDeviceUncompressedPayloadLength
UARPMetaDataHeySiriModelLocale
UARPMetaDataPersonalizationDigestListSize
UARPMetaDataCrashAnalyticsAppleModelNumber
UARPMetaDataCrashAnalyticsTestMode
UARPMetaDataHeySiriModelDigest
UARPMetaDataInformationSerialNumber
UARPMetaDataPersonalizationNonFTABSubfileLongname
UARPMetaDataPayloadCompressionAlgorithm
DeviceBasedPersonalization
UARPEndpointLayer3
UARPMetaDataHostMinimumBatteryLevel
UARPMetaDataComposePropertyListPayload
UARPStatistics
UARPMetaDataVoiceAssistHash
UARPMetaDataInformationModelName
UARPMetaDataVoiceAssistEngineVersion
UARPMetaDataInformationManufacturerName
UARPMetaDataPersonalizationManifestSuffix
UARPMetaDataDevicePayloadSignature
UARPMetaDataPersonalizationSuperBinaryPayloadIndex
UARPMetaDataDevicePayloadIdentifier
Deprecated
UARPMetaDataPersonalizationProductType
Layer2VendorCallbacks
UARPSuperBinaryPayloadLayer3
UARPMetaDataHeySiriModelRole
UARPDeploymentRules
UARPMetaDataPersonalizationBoardID64
UARPTatsuTicket
UARPComponentConfiguration
UARPMetaDataMappedAnalyticsAppleModelNumber
UARPMetaDataPersonalizationChipRevision
UARPMetaDataPersonalizationFTABSubfileHashAlgorithm
UARPMetaDataInformationActiveFirmwareVersion
UARPMetaDataVoiceAssistActiveModel
UARPMetaDataPersonalizationRealHdcpKeyPresent
UARPMetaDataDeviceMinimumRequiredVersion
UARPMetaDataPersonalizationCertificateEpoch
UARPMetaDataPersonalizationECID
UARPRTKitFTAB
UARPMetaDataComposeMarketingBVERStringFile
componentTagWithLength:value:
_banyanManager
initWithChar:
minimumVersionString
updateDelegateFilename
_offset
prepareQueriesForPersonalization:
uarpReadPacket:packetSize:
TQ,V_bytesTransferred
TQ,V_txBufferOverhead
_provisioning
generateHash:
notifyPayloadReady:payload:
payloads
TB,R,V_ftabSuffix
_longname
_nonceSeed
composeFTAB
setObject:forKeyedSubscript:
tlvNameForType:
_useGlobalSigning
untilDate
T@\"NSString\",R,V_serialNumber
_debugDataPackets
_digestKeyName
majorVersion
setCertificateEpoch:
unsignedCharValue
T@\"NSData\",&,V_nonceSeed
_chipID
TI,R,V_tag
resetDevice
urgentUpdate
T@\"NSString\",R,V_firmwareVariant
T@\"NSString\",R,V_vendorVersionString
TB,V_disableRetries
TQ,R,V_totalBytesRequested
dataWithContentsOfURL:
isFTAB
layer2CallbackActiveFirmwareVersionResponse:
layer2CallbackChipRevisionResponse:
T@\"NSUUID\",R,V_uuid
T@\"NSNumber\",C,V_ECID
copyItemAtURL:toURL:error:
exportAsDictionary
irqConnection
manifestDestination
modelLocale
queryOutstandingEndpointIDComponentProperties:
T@\"NSNumber\",C,V_endpointID
initWithLength:
T@\"NSString\",R,V_friendlyName
T@\"NSURL\",R,V_superbinaryURL
TI,R,V_productRevisionMin
_isRequired
addEntriesFromDictionary:
clearMatchingLayer2Context:
T@\"NSData\",R,V_nonceHash
T@\"NSData\",R,V_payloadHash
setWithObjects:
initWithlogFunction:logContext:
_packetQueue
_upgradeOnly
appendCompressedPayloadData:offset:
closeAndReturnError:
T@\"NSData\",C,V_nonce
_layer3Delegate
T@\"NSString\",R,V_ticketPrefix
UTF8String
_certificateEpoch
_pcapDelegate
addDigestForTatsuDictionary:objectProperty:
composePayload
_tssOption
getIrqStatus:
initWithBytes:length:
initWithURL:offset:length:subFileTag:
isDone
metaDataHash
payloadData
selectLayer3Payload:payloadIndex:
T@\"NSData\",R,V_nonceSeed
_banyanManagerQueue
_manufacturerName
_requiresPersonalization
defaultOptions
hashPayload
isGreaterThan:
setManifest:
addECID:componentTag:tatsuTicket:keyName:
configureEndpointLayer2Tags
digestListSize
initWithData:offset:length:subFileTag:
updateFilepath:uuid:
T@\"NSNumber\",C,V_chipEpoch
T@\"NSURL\",R,V_url
TS,R,V_chunkSize
notifyRxDynamicAssetFullyStaged:
stopUARPLayer2
verboseLog:
T@\"NSNumber\",C,V_allowUnsealedData
_manifestProperties
_maxTxPayloadLength
compressionAlgorithm
isEqualToNumber:
setFusingType:error:
stagingInProgress
T@\"NSNumber\",C,V_requiresPersonalization
T@\"UARPComponentVersion\",C,V_firmwareVersion
.cxx_destruct
TB,R
_expansionFolderURL
_payloads
_suffixNeedsLogicalUnitNumber
expandPropertyListPayloads:
T@\"NSString\",R,V_hardwareFusing
_chipEpoch
_osVersion
_percentageLimit
_tatsuRequest
formatVersion
initWithPacketsNoVersionAgreement:packetsMissed:packetsDuplicate:packetsOutOfOrder:
layer2CallbackApBoardIDResponse:
T@\"NSString\",C,V_manifestSuffix
_packetsMissed
assetMetaDataTLV:
assetPreProcessingAck:
layer2CallbackTicketLongNameResponse:
notifyEndpointPayloadData:payload:offset:payloadData:
packetsOutOfOrder
remoteEndpointFullyStagedAsset:processingStatus:
TS,R,V_securityModeHostOverride
_demotionSecurityMode
_friendlyName
_majorVersion
_payloadSignature
ftabSubfile
layer3DownstreamEndpointReachable:downstreamID:tlvs:
longLongValue
banyanTransport
TC,R,V_allowFlashWrite
assetMetaDataProcessingError:asset:
bootNonceAsTLV
layer2CallbackRemoteNotResponding:length:
matchingTLVs:
packetsNoVersionAgreement
processSubfileInfo:
T@\"NSNumber\",C,V_suffixNeedsLUN
T@\"NSData\",R,V_metaData
_fdrData
_ticketPrefix
arrayWithObjects:
needsDigest:algorithm:objp:objectDictionary:
numPreallocatedBuffers
setBoardID64:
_productRevisionMax
_txDynamicAssets
nonceHash
processPMAP:
productNumber
string
irqPort
setPayloadData:
_pauseRemote
_useHostPushModel
initWithBVERString:
T@\"NSNumber\",C,V_enableMixMatch
T@\"NSMutableArray\",C,V_outstandingInfoProperties
TC,R,V_activeModel
TQ,R,V_formatVersion
_numPayloads
objectAtIndexedSubscript:
queryTags:error:
setBootNonceAsTLV:
TQ,V_processingStatus
_context384
_packetsNoVersionAgreement
dataWithData:
layer2CallbackUnsolicitedDynamicAssetOffered:assetTag:
setDisableRetries:
startUARPLayer2:configuration:infoProperties:appleProperties:endpointID:upstreamEndpoint:pcapDelegate:
watchdogCancelOnQueue
TI,R,V_tssOption
_debugPackets
_measureLength
_propertyList
boardID64
doesNotRecognizeSelector:
paddingBlock
_payloadTags
_pendingConfigurations
_tlvName
signature
eventID
now
_needsSHA512
liveNonce
uarpMessageSendToDevice:
T@\"NSString\",R,V_hwVersion
TI,R,V_securityDomain
_retryLimit
_stagedFirmwareVersion
autoApply
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
writeToFileHandle:includedPayloads:allHeaders:allMetaData:error:
fdrData
_manifestLocation
expandPropertyListPayload:payloadIndex:
layer3EndpointPayloadDataComplete:asset:payload:
numberWithUnsignedChar:
T@\"NSString\",R,V_filename
T@\"NSString\",R,V_longname
TI,R,V_chipRevision
_lastApplyStatus
assetVersion
dataToSign
defaultManager
getDataRangeFromURL:
_banyanManagerSemaphore
_ignoreVersion
addSecurityDomain:componentTag:tatsuTicket:keyName:
allowUnsealedData
initWithUnsignedInt:
manifestEpoch
offerDynamicAsset:fourCC:
personalizeFirmwareSuperBinary:tssServerURL:
_needsEPRO
downstreamEndpointUnreachable:downstreamEndpointID:
initWithUUID:transportTxDelegate:layer3Delegate:tmpFolderPath:
layer3DownstreamEndpointReachable:downstreamID:
prepareBulkQueriesForPersonalization:
processRespondedEndpointInfoQueries:tlvs:
removePayloadsWithMatchingTag:
setProductionMode:
_tmpFolderPath
initWithPayloadDictionary:payloadsURL:payloadIndex:
mutableCopy
productRevisionMin
T@\"NSNumber\",R,V_measureOffset
TI,R,V_urgentUpdate
TS,R,V_productionModeHostOverride
_productNumber
_tlvType
layer2CallbackLifeResponse:
needsSHA512
T@\"UARPComponentVersion\",R,V_assetVersion
_digestListSize
T@\"NSNumber\",C,V_useGlobalSigning
TC,R,V_life
_minimumVersionString
composeFTABAsData
initWithLayer2Context:assetTag:tmpFolderPath:
serialNumber
hardwareVersion
TB,V_supportsBulkInfoQueries
addChipID:componentTag:tatsuTicket:keyName:
addECIDData:componentTag:tatsuTicket:keyName:
integerValue
setManufacturerName:
tlvValueWithUInt64:
T@\"NSString\",R,V_manifestSuffix
dealloc
Tq,R,V_personalizationStatus
expandPayloadWithHeaderAsURL:payloadIndex:payload4cc:payloadVersion:payloadMetaData:
layer2CallbackStagedFirmwareVersionResponse:
productType
T@\"NSString\",C,V_manifestPrefix
TB,R,V_metaData
_apProductionMode
modelName
payloadDataAsData
prepareComposeMetaData
processCountryDeploymentRules:
T@\"NSString\",C,V_productGroup
_ecidData
_minorVersion
countByEnumeratingWithState:objects:count:
logRxPacket:
uarpMessageRecvFromTransport:
_endpointQueue
boardID32
dictionaryWithContentsOfURL:error:
engineVersion
logicalUnitNumber
uncompressedLength
T@\"NSString\",R,V_tlvName
TQ,R,V_ecID
fileURLWithPath:
requiresPersonalization
setManifestEpoch:
setProductGroup:
whitespaceAndNewlineCharacterSet
_payloadIdentifier
subdataWithRange:
ticketNeedsLogicalUnitNumber
T@\"NSData\",R,V_composedMetaData
T@\"NSNumber\",C,V_ftabGeneration
T@\"NSNumber\",C,V_securityMode
addTLVs:
addUIDMode:componentTag:tatsuTicket:keyName:
getFusingType:
writeComposedPayloadToFile:error:
assetIdentifier
TS,R,V_assetID
nextLayer3Payload:
payloadVersion
personalizationStatePrepare:endpoint:
setAssetType:
stopUARPLayer2AndWait
tlvValueWithComponentVersion:
T@\"NSData\",C,V_manifest
_appleModelNumber
_layer2AssetCallbacks
appendData:
assetFullyStaged:status:
layer2CallbackLogTxPacket:uarpStatus:
personalizationInProgress
setAssetIdentifier:
T@\"NSNumber\",C,V_realHdcpKeyPresent
_needsESEC
_productRevisionMin
_serialNumber
_useFileSystem
initWithBytes:length:encoding:
initWithUUID:tmpFolderPath:delegate:
notifyDownstreamEndpointUnreachable:
T@\"NSData\",R,V_matchingData
copyWithZone:
hwVersion
processOutstandingEndpointInfoQueries:infoProperties:
unsignedLongLongValue
T@\"NSNumber\",C,V_chipID
url
_hashValue
setBoardID32:
tssRequests
uarpMessageRecvFromDevice:
isEqualToArray:
infoProperty
T@\"NSURL\",R,V_tssServerURL
TB,V_upgradeOnly
TQ,V_maxRxPayloadLength
_debugNotifications
_uarpRole
assetPayloadData:offset:asset:
setMaxTransmitsInFlight:
TS,R,V_modelRole
_enableFutureFWVersion
_infoProperty
addFTABGeneration:payload:componentTag:defaultFTABGeneration:
boolValue
dfuStage:
getDataBlock:offset:
initWithHashAlgorithm:
context
_epro
addRealHdcpKeyPresent:componentTag:tatsuTicket:keyName:
layer2CallbackModelNameResponse:
payloadTags
setLiveNonce:
tssResponse
layer2RemoteCtx
T@\"NSString\",R,V_subFileTag
TI,R,V_actualOffset
TQ,R,V_lastError
Tq,V_assetType
_lastError
assetStagingProgress:bytesTransferred:assetLength:
currentOperationalMode
_hardwareSpecific
addNonce:componentTag:tatsuTicket:keyName:defaultNonce:
downstreamEndpointReachable:downstreamEndpointID:tlvs:
downstreamEndpointRemove:
layer2CallbackDownstreamReleased:
needsTrusted
offerFirmwareAsset:assetUUID:
releaseVersion
_hardwareFusing
_packetsOutOfOrder
productGroup
suffixNeedsLUN
ticketName
ECIDData
TI,R,V_productRevisionMax
_signature
initWithSimpleBVERString:
layer2CallbackManifestEpochResponse:
layer2CallbackSocLiveNonceResponse:
readRegister::
setTxBufferOverhead:
_ticketLongName
TI,R,V_useGlobalSigning
_identifierString
apProductionMode
appendString:
compare:options:range:
identifierString
initWithDict:
initWithString:
T@\"NSData\",R,V_payloadCertificate
protocolVersion
UUID
_bootNonceLocation
_liveNonce
_manifestLocations
layer3EndpointAssetFullyStaged:asset:processingStatus:
T@\"NSString\",R,V_countryCode
T@\"NSString\",R,V_tmpFolderPath
initWithPayloadHash:
layer2CallbackNoFirmwareUpdateAvailable
modelDigest
setRecvCounterpart:
stringWithString:
superbinaryURL
_payloadVersion
TI,R,V_payloadIndex
_banyanDeviceSemaphore
_tlvsMutable
getDfuInfo
objectProperties
onTconIrq
setNonce:
_tssServerURL
addObjectsFromArray:
buildExcludedPayloadTags:
getBytes:length:
subFileLength
supportsSecureCoding
TQ,R,V_payloadIdentifier
_apChipID
_compressedHeaders
payloadWithMatchingIndex:
setECID:
upgradeOnly
writeComposedPayloadURLToFile:error:
T@\"NSString\",R,V_expandFilename
initWithFilePath:assetUUID:tmpFolderPath:
startUARPLayer2Internal
tlvValueWithUInt16:
uarpMessageSendToTransport:
T@\"NSNumber\",C,V_boardID32
fdrRootCaDigest
_logicalUnitNumber
_modelName
initWithMajorVersion:minorVersion:releaseVersion:buildVersion:
layer3EndpointPersonalizationNeeded:asset:
T@\"<UARPEndpointPacketCaptureDelegateProtocol>\",R,W,V_pcapDelegate
_debugDownstream
assetAllHeadersAndMetaDataComplete:
componentsSeparatedByString:
generatePayloadHash:
preparePersonalizedURL
setStagedFirmwareVersion:
_ECID
_measureOffset
_payloadCertificate
addTatsuTicketManifest:
assetPayloadMetaDataComplete:
chipRevision
queue
restoreUpdaterDelegate
composeFTABAsURL:
initWithUTF8String:
layer2CallbackSecurityModeResponse:
securityMode
setApBoardID:
suffixNeedsLogicalUnitNumber
T@\"NSData\",R,V_manifest
_boardID32
layer2CallbackDataTransferPaused
layer2CallbackRealHdcpKeyPresentResponse:
layer2CallbackSuffixNeedsLogicalUnitNumberResponse:
objectForKeyedSubscript:
T@\"NSString\",R,V_algorithm
T@\"NSString\",C,V_assetIdentifier
tag
TI,R,V_chipID
_uncompressedLength
countryRules
layer2CallbackSendMessage:length:
layer2CallbackSolicitedDynamicAssetOffered:asset:
T@\"NSString\",C,V_ticketLongName
T@\"NSString\",R,V_hardwareVersion
TC,R,V_liveNonce
acceptLayer3Payload:
layer2CallbackBulkInfoResponse:componentTag:tlvs:
layer2CallbackNonceResponse:
layer2CallbackRequestTransmitMsgBuffer:
layer3EndpointAssetOffered:asset:
_needsSHA256
_packetsDuplicate
isEqualToString:
notifyAssetSolicited:
numPayloads
payloadCertificate
stageFirmwareWithDictionary:error:
subFileTag
clearIrqStatus:
_fileLength
_uncompressedPayloadURL
numberWithUnsignedInt:
subfileHashAlgorithm
version
TQ,V_protocolVersion
setEndpointType:
setPayloadURL:
subFileOffset
uniquePacketCaptureFilename
dataWithLength:
_untilYear
expandPropertyListTLVs:
fileHandleForReadingFromURL:error:
filename
setRestoreUpdaterDelegate:
tlvLength
T@\"NSString\",R,V_appleModelNumber
TC,R,V_provisioning
_char4
assetPayloadDataComplete:hash:
composedPayloadLength
layer2Ctx
_firmwareAssets
TC,R,V_moreRequestsToFollow
_moreRequestsToFollow
layer2CallbackDownstreamDiscovery
stageFirmwareSuperBinary:tssServerURL:
containsObject:
T^v,V_layer2Context
T@\"NSString\",R,V_productType
stringFromDate:
keyName
_banyanDeviceQueue
_manifestAsSuffix
_ticketNeedsLogicalUnitNumber
decodeArrayOfObjectsOfClass:forKey:
nonceSeed
_modelLocale
_untilMonth
dataFromPlistValue:
fileSize
generatePayloadHash:measureOffset:measureLength:
layer3EndpointPayloadData:asset:payload:offset:payloadData:
processComposeMeasuredPayloads:value:relativeURL:
processingStatus
compressPayload
TI,R,V_eventID
TI,R,V_ftabGeneration
_manifestAfterSubfiles
containsTLV:
numberWithUnsignedShort:
setChipEpoch:
setSupportsBulkInfoQueries:
T@\"NSData\",R,V_dataToSign
subfileWithTag:
TI,R,V_batteryLevel
disableRetries
findComponentConfiguration:endpointConfig:
rangeOfString:
setApChipID:
setApProductionMode:
T@\"NSNumber\",C,V_liveNonce
_payloadDataInternal
_tatsuTickets
coreName
layer2CallbackReturnAssetBuffer:
setProvisioning:
solicitationQueueDepth
watchdogExpire
ECID
TS,R,V_payloadOrderedIndex
_char3
_firmwareVariant
_ftabSubfile
_protocolVersion
assetProcessingCompletedAck:
componentTag
URLByAppendingPathComponent:
expandSuperBinaryPlist
initWithData:subFileTag:
initWithURL:assetUUID:tmpFolderPath:
personalizationCompleted:
unsignedShortValue
_banyanTransport
devicePersonalizationStateCompleted
ftabGeneration
index
personalizeFirmwareAssetComplete:
demotionSecurityMode
expandPayloadDictionaryKeyValuePayload
initWithMarketingBVERString:
setIsHostRole:
containsPayloadWithMatchingTag:
_countryRules
_defaultAppleProperties
addTatsuTicketManifest:ticket:manifestLocation:payload:
assetReady:
encodeObject:forKey:
maxPayloadLength
T@\"NSString\",R,V_identifierString
TQ,R,V_buildVersion
_layer2RemoteEndpoint
_personalizingAssets
acceptOffer:queue:
addSubfileMeasurement:
digest
needsEPRO
T@\"NSDictionary\",C,V_tatsuRequest
_securityModeHostOverride
manifestData
metaData
prepareEndpointBulkQueriesForPersonalization:config:
processOutstandingComponentInfoQueries:infoProperties:
setDataBlockToURL:offset:url:
TB,V_isHostRole
T@\"NSString\",C,V_productNumber
numberWithBool:
T@\"UARPComponentVersion\",R,V_minimumVersion
_logContext
_processingStatus
_url
composedMetaData
_assetType
_endpointType
_log
_payloadURL
_solicitationQueueDepth
chunkSize
initWithOptions:logFunction:logContext:
lastAction
_hardwareVersion
_hwVersion
applyStagedAssets
im4mCraftTatsuTickets:
initWithCoder:
processDeploymentRules:
setFusePROD:
writeRegisters:::
_excludedPayloadTags
bootNonceLocation
data
downstreamEndpointAdd:
im4mBuildKey:keyPrefix:keyPrefixNeedsLUN:keySuffixNeedsLUN:logicalUnitNumber:
layer2CallbackHardwareVersionResponse:
layer3EndpointPayloadMetaDataComplete:asset:payload:
notifyRxFirmwareFullyStaged:
TQ,R,V_percentageLimit
_kInternalQueueKey
assetRescind:
createFileAtPath:contents:attributes:
directConfiguration
encodeWithCoder:
manifestProperties
setPayloadHeader:
tlvName
TS,R,V_ignoreVersion
appleModelNumber
notifyTxFirmwareFullyStaged:
offerAsset:queue:
osVersion
uidMode
_downstreamEndpoints
isRequired
setFdrRootCaDigest:
transfersInProgress
T@\"NSData\",R,V_payloadSignature
_ftabHeader
_maxTransmitsInFlight
_uidMode
setNeedsStaging:
setProcessingStatus:
T@\"NSData\",R,V_fdrData
TC,R,V_allowUnsealedData
TQ,R,V_subFileOffset
_isFTABPayload
_responseTimeout
_superbinaryHeader
assetProcessingCompleted:flagsDescription:asset:
endpointType
T@\"NSData\",C,V_fdrRootCaDigest
TQ,V_solicitationQueueDepth
_fusePROD
addPayloadWith4cc:payloadVersion:payloadIndex:
hardwareFusing
initWithTicketName:componentName:tatsuRequest:
layer2CallbackEcidResponse:
tatsuRequest
TI,R,V_chipEpoch
_subFileTag
initWithAlgorithm:
isEqualToData:
layer2CallbackManufacturerNameResponse:
layer3EndpointRescindedAssets:
manifestSuffix
T@\"NSString\",R
_ecID
_uuid
modelHash
decodeCharForKey:key:
expandPayloadDictionaryTLVs:
noTatsuMeasurements
setFirmwareVersion:
layer2CallbackEcidDataResponse:
TS,R,V_epro
_asset4cc
_componentTag
additionalManifestLocations
layer2CallbackManifestSuffixResponse:
maxRxPayloadLength
T@\"NSNumber\",C,V_apSecurityMode
T@\"UARPComponentTag\",R,V_componentTag
_countryCode
_manifest
layer3EndpointAssetFullyStaged:txFirmwareAsset:
personalizedURL
initWithPayloadDictionary:payloadsURL:payloadIndex:useFilesystem:
initWithUUID:tmpFolderPath:
layer2CallbackLogInfo:logMsg:
payloadsWith4cc:
setComponents:
setManifestAsSuffix:
Ti,V_endpointType
_isHostRole
assetFullyStaged:processingStatus:
assetPayloadMetaDataProcessingError:asset:
char1
layer2CallbackRequestAssetBuffer:
TB,R,V_needsSHA256
TC,R,V_suffixNeedsLogicalUnitNumber
_internalQueue
_nonce
acceptLayer3Asset:
fuse:
getAllBanyanDevices
layer2CallbackRescindedAllAssets
_digest
TQ,V_maxTxPayloadLength
calculateWeeklyDeploymentDay:
description
ecidData
packetsDuplicate
processPercentageDeploymentRules:
setApSecurityMode:
T@\"NSData\",R,V_digest
_char2
_life
_logFunction
assetOrphan:
boardID
T@\"NSString\",R,V_manufacturerName
friendlyName
manifestPrefix
minimumVersion
setLogicalUnitNumber:
transportTxDelegate
uarpRole
percentageLimit
setUpgradeOnly:
TB,R,V_needsEPRO
firstObject
generateMetaDataHash:metaData:
layer2CallbackDataTransferPausedByRemote
layer3DownstreamEndpointUnreachable:downstreamID:
payloadWindowLength
T@\"NSNumber\",R,V_measureLength
TC,R,V_uidMode
assetRelease:
demotionProductionMode
fileURLWithPath:isDirectory:relativeToURL:
dateFromString:
TQ,R,V_numPayloads
URLByDeletingLastPathComponent
_manifestData
layer2CallbackHwFusingTypeResponse:
logInternal:arguments:
outstandingInfoProperties
setCompressedDataBlock:offset:
_bootNonceAsTLV
ftabDescription
_payloadDigest
expandPayloadDictionaryPropertyListPayload:
removeItemAtPath:error:
tmpFolderPath
writeComposedPayloadDataToFile:error:
TI,R,V_logicalUnitNumber
TI,R,V_securityMode
prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:
setFtabGeneration:
setHardwareSpecific:
_isCompressed
bytes
notifyEndpointRescindedStagedAssets
personalizeFirmwareSuperBinaryInternal:tssServerURL:
_expandFilename
TB,R,V_needsSHA384
_inDfuMode
assetLength
characterSetWithCharactersInString:
ftabProperties
layer3EndpointAssetFullyStaged:txDynamicAsset:
setRetryLimit:
currentCalendar
_ftabLength
layer2CallbackLastErrorResponse:
numberWithUnsignedLongLong:
subfileEPRO
T@\"NSData\",C,V_ecidData
_algorithm
cleanFileHandleForWriting:error:
layer3EndpointAssetStagingProgress:asset:bytesTransferred:assetLength:
readDataUpToLength:error:
setDateFormat:
_sharedManifest
TQ,R,V_packetsMissed
_payloadWindowLength
initWithDictionary:
propertyValue
substringWithRange:
responseTimeout
TI,R,V_demotionSecurityMode
_selectedPayloadIndex
_vendorVersionString
enableFutureFWVersion
layer2CallbackStatisticsResponse:
tagString
composeMetaData
TQ,R,V_assetLength
_compressedLength
_outstandingInfoProperties
layer2CallbackUnsolicitedDynamicAssetOffered:
maxTxPayloadLength
TI,R,V_uncompressedPayloadLength
_personalizationStatus
expandFilename
prefixNeedsLogicalUnitNumber
stringFromPlistValue:
tlvsFromKey:value:relativeURL:
processSuperBinaryPropertyList:
TC,R,V_testMode
_manifestPrefix
TB,V_useHostPushModel
_productType
T@\"<UARPEndpointTransportTxProtocol>\",R,W,V_transportTxDelegate
T@\"NSDate\",R,V_untilDate
_banyanDevices
_parameterData
addProvisioining:componentTag:tatsuTicket:keyName:
count
layer2CallbackAppleModelNumberResponse:
outstandingAppleProperties
T@\"NSDictionary\",C,V_tatsuResponse
_apSecurityMode
Ti,R,V_compressionAlgorithm
_lastAction
bytesTransferred
initWithData:assetUUID:tmpFolderPath:
processTatsuTicketManifest:ticket:
setLife:
TC,R,V_realHdcpKeyPresent
_maxPayloadLength
engineType
layer3EndpointApplyStagedAssets:
sharedManifest
_objectProperties
_supportsBulkInfoQueries
components
compressedLength
dictionaryWithDictionary:
inDfuMode
personalizationStatePrepare:
removeObject:
_modelSignature
Tc,R,V_char1
_boardID
_compressedPayloadDataInternal
asset4cc
logTxPacket:
setAllowFlashWrite:
superBinaryWithURL:useFilesystem:tmpFolderPath:
T@\"NSNumber\",C,V_apChipID
T@\"NSString\",R,V_minimumVersionString
TC,R,V_ticketNeedsLogicalUnitNumber
_modelDigest
assetMetaDataComplete:
hash
layer3EndpointAppliedStagedAssets:layer3Flags:
removeTLV:
subfileLongname
_apBoardID
_tlvs
_untilDay
expandPayloadHeadersAndMetaData:offset:
getDataRangeFromData:
ignoreVersion
layer2CallbackAssetSolicitation:
_context256
_needsHostPersonalization
dictionaryWithContentsOfURL:
getFusingType:error:
layer2CallbackDownstreamReachable:tlvs:
layer2CallbackProductionModeResponse:
manifest
measurementsForDevicePersonalization
_minimumVersion
TB,R,V_needsSHA512
TC,R,V_enableFutureFWVersion
TC,R,V_isRequired
_actualOffset
_compressionAlgorithm
determinePayloadHashAlgorithm
enumerateKeysAndObjectsUsingBlock:
composePersonalizedPayload
craftTatsuRequests:
initCommon:
isPropertyListPayload
layer2CallbackWatchdogCancel
longname
notifyAssetPersonalizationComplete:status:
numberFromPlistValue:
TQ,V_responseTimeout
_fdrRootCaDigest
absoluteString
addPayload:
appendBytes:length:
char2
initWithManifestPropertyDictionary:
layer3EndpointRemoteNotResponding:
_components
_defaultInfoProperties
_layer3Ready
epro
layer2CallbackBulkInfoQuery:componentTag:infoProperties:
measureLength
mergePayloadsPMAPs
solicitDynamicAsset:assetTag:
T@\"NSString\",R,V_coreName
T@\"UARPEndpointLayer3\",R,W,V_layer3Endpoint
_dfuTatsuOptions
setOutstandingAppleProperties:
initWithObjectPropertyDictionary:
intValue
layer2CallbackBoardID64Response:
packetTracking:packetDirection:inFunction:
processTatsuTicketManifest:ticket:manifestLocation:
setGeneration:
startUARPLayer2:configuration:infoProperties:appleProperties:endpointID:upstreamEndpoint:
unsignedLongValue
T@\"<UARPEndpointLayer3DelegateProtocol>\",R,W,V_layer3Delegate
_dataToSign
_filepath
componentsSeparatedByCharactersInSet:
expandPayloadWithHeader:payloadIndex:
notifyApplyStagedAssets
personalizeFirmwareAssetComplete:tssResponse:
removeObjectForKey:
_productionMode
TS,R,V_trusted
initWithBanyanManager:restoreDevice:
layer2CallbackChipEpochResponse:
needsHostPersonalization
reofferFirmwareOnSync
setSecurityDomain:
setTatsuRequest:
T@\"NSDictionary\",R,V_superBinaryPlist
assetType
layer2CallbackPrefixNeedsLogicalUnitNumberResponse:
setupPendingInfoQueries
tcon
T@\"NSObject<OS_os_log>\",R,V_log
T@\"NSNumber\",C,V_manifestEpoch
TQ,R,V_packetsOutOfOrder
_ftab
addToVersion:
appendPayloadData:offset:
expandFileTable:
layer2CallbackChipIDResponse:
T@\"NSNumber\",C,V_enableFutureFWVersion
T@\"NSString\",R,V_keyName
apSecurityMode
selectedPayloadIndex
_suffixNeedsLUN
T@\"NSData\",R,V_parameterData
_preflightInfoProperties
appendFormat:
setManifest:asSuffix:
T@\"NSData\",R,V_fdrRootCaDigest
_reofferFirmwareOnSync
_testMode
assetMetaDataTLV:asset:
expandPayloadDictionary:
measureOffset
packetCapture
unsignedIntegerValue
T@\"UARPComponentTag\",R,V_payload4cc
_hashAlgorithm
_tag
_untilDate
component:fromDate:
nonce
notifyEndpointPayloadMetaDataComplete:payload:
objectForKey:
_ftabGeneration
```
