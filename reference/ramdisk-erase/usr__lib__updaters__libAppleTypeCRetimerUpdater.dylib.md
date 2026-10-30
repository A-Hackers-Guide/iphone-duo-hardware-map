# `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 977,328 bytes.

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
generatePersonalizedSuperBinary
TC,R,V_boardRevision
TQ,R,V_minorVersion
_assetID
setECID:
T@\"<AppleTypeCRetimerIICFifoDelegate>\",W,V_delegate
TC,R,V_isRequired
_b2p
byteString
string
_tbtInterface
setChipID:
valid
_keyManifest
lastPathComponent
lock
_opCode
_releaseVersion
TQ,R
TQ,R,V_pendingMinor
_chipRevision
_manifestData
_type
T@\"NSString\",C,V_payload4cc
getMeasurements
_tlvs
removeSubfileWithTag:
TB,V_fwPanic
_enableDFUMode
_nonce
TI,V_boardID
Ti,R
_asset
_notReadyRouterIDs
enableUART
initHPMInterface
initWithEnabled:forceDFU:
T@\"NSString\",R,V_longname
Ti,R,V_category
_infoID
isEqual:
numberWithUnsignedInt:
T@\"NSObject<OS_dispatch_queue>\",&,V_delegateQueue
TB,R,V_useLocalSigning
code
configReadForRoute:port:space:index:result:
getDataBlock:offset:
initializeDeviceInterfaceForRouterID:
name
path
T@\"NSData\",R,V_sessionData
T@\"NSNumber\",&,V_securityMode
_activeFile
_configBuffer
payloadWith4ccTag:
pollForReceiveData
setPersonalizedMetaData:
setPrefixNeedsLogicalUnitNumber:
personalizationParameters
_idResponse
_persistent
b2pReset:
initFile
initWithOpCode:route:data:
manifestBytesSent:bytesTotal:
setDelegateQueue:
TI,V_maxB2PFrameSize
checkDeferredRouterIDs
drainTransmitQueue
setLongname:
setRoute:
tssOption
writeBytes:length:
_isDone
TC,R,V_suffixNeedsLogicalUnitNumber
decodeIntegerForKey:
dfuValidate
sharedInstance
_productionStatus
decodeObjectOfClass:forKey:
dumpATCConfigRegisterWrite:value:
firmwareBytesTransferred:bytesTotal:
setDigest:
_timerSource
getPayloads
initWithUTF8String:
_protocolVersion
retimerEnterDFU
T@\"NSString\",R,V_filename
_serviceName
_stageSuccess
convertDWordsToData:bytes:
firmwareApplyCompleteWithStatus:flags:
prefixNeedsLogicalUnitNumber
_bytesReceived
_trusted
generation
performUpdateForFTABData:manifestData:apHardwareID:skipSameVersion:debugFlags:
processTLVsForPersonalization
setSecurityMode:
writeBytes:length:handle:
T@\"NSDictionary\",R
TC,R,V_result
dataLength
query
_trustedOverride
TC,R,V_chipRev
Tr*,R,V_dataPointer
generateTatsuMeasurements:
initWithBytes:length:encoding:
magic
_flavorField
_maxB2PFrameSize
filePointer
initWithRouterID:delegate:forcePower:
inputData
setUnitNumber:
TC,R,V_value
_effectiveSecurityMode
configReadMetadata:opCode:
Ti,R,V_protocolMode
_isForceDFUModeEnabled
_payloadLongname
setSuppressed:
setSessionData:
countByEnumeratingWithState:objects:count:
dataTransferUpdateForBytesSent:bytesTotal:sessionID:
initWithRoute:status:sessionID:dataSessionStatus:data:
locatedObjects
objectAtIndex:
pathWithComponents:
unsignedLongLongValue
doCheck
trusted
_longname
_manifestEpoch
initWithTag:data:
lookupThunderboltController
sortUsingComparator:
_writeData
personalizeSuperBinary:signingServer:ssoOnly:
setPersonalizedData:
_personalizedData
appendFlag:field:descStr:
arrayWithArray:
buildVersion
createChipSpecificSuperBinaryDataForStockSuperBinary:manifestData:apHardwareID:debugFlags:
dictionary
TB,R,V_enabled
provisioning
sendCommand:
writeData:
T@\"FTABSubfile\",R,V_manifest
dataSessionStatus
dumpATCMetadataPacketType:metadata:opCode:
queryPanicStatus:
registerWriteForVendorIndex:value:
retimerForcePower
setHashAlgorithm:
_payloadDigest
generatePersonalizedSuperBinaryWithoutRRKO
isEqualToString:
TC,R,V_sessionID
setUarpContext:
findBaseAddress
_useLocalSigning
allocateUpdaterIIC
compressionAlgorithm
hardwareID
initWithRouterID:route:port:space:baudRate:
T@\"NSData\",R
_pendingMinor
appendValue:descFunc:descStr:
getACIOParentData
hasPrefix:
writeSubfileToURL:tag:
TC,R,V_persistent
T@\"NSArray\",&,N,V_locatedObjects
_dfuBaseAddress
Tc,R,V_char1
_queue
initWithOpCode:route:status:data:
dfuBoot
_fileLength
setLife:
updateTransmitFifoSpace
tlvType
_bytesWritten
_notReadyRouterIDsLock
activeFile
dequeueDataOfLength:
stopPollingforReceiveData
iecsAtomicCommand:data:dataLength:retData:retDataLength:flags:timeout:
T@\"NSURL\",R,V_url
sendPingCommand
url
version
convertBytesToDword:length:
initForceDFU
longTagName:
tssOptions
T@\"NSString\",&,V_keyManifest
addSubfileWithTagName:contentsOfURL:
releaseVersion
T@\"NSString\",R,V_serialNumber
Tc,R,V_char4
isGreaterThan:
lowercaseString
TC,R,V_enableMixMatch
stringByAppendingPathComponent:
TC,R,V_securityMode
_char1
initWithBoardID:chipID:portNumber:securityDomain:flavor:
pendingMajor
T^v,V_layer2Context
checkReady
composeTSSRequest:
getRouterIDs
metaDataTableEntry
readData
setFilename:
setUarpChipCallbacks:
T@\"NSNumber\",C,V_digestListSize
shouldSkipSameVersion:
suffixNeedsLogicalUnitNumber
unsignedLongValue
TI,R,V_chipEpoch
dealloc
initWithCoder:
locatedDevices
superbinary:logString:
value
TI,R,V_isRequired
_valid
dictionaryWithDictionary:
initWithOptions:logFunction:logContext:forcingPower:
tlvValue:
unsignedCharValue
setTag:
_b2pTransmitBuffer
componentsSeparatedByString:
initWithURL:delegate:delegateQueue:
securityDomain
TI,R,V_code
_applySuccess
_manifest
dataWithBytes:length:
initWithBloodhoundDumper:
TI,R,V_boardID
_routerID
initWithType:length:value:
expandMetaData:
_hardwareID
securityMode
startPacketDumperWithFileName:
trimmedTlvs
chipID
errorWithDomain:code:userInfo:
setDigestListSize:
setManifest:
_txQueue
initWithBytes:length:
TC,R,V_pendingFile
TQ,R,V_ecid
performUpdateWithDictionaryAggregate:
T@\"<AppleTypeCRetimerUpdaterIICDelegate>\",W,V_delegate
TI,R,V_securityMode
payloadsWithout4ccTag:
setDebugLevel:
compare:
configWriteForRoute:port:space:index:value:
encodeInteger:forKey:
initWithForceDFUMode:allowOnlyIfConnected:
queryInfoAggregate
setSecurityDomain:
stringWithValidatedFormat:validFormatSpecifiers:error:
TB,R,V_allowOnlyIfConnected
.cxx_destruct
TC,V_securityMode
Ti,R,V_status
_compressionAlgorithm
_formatVersion
bverString
generateTatsuMeasurementsPerPayload:
TI,R,V_chipID
_b2pOpCodeInFlight
_ftab
longname
initWithFileName:
objectForKey:
serviceMatchesRouterID:routerID:
state
T@\"NSObject<OS_os_log>\",R
TI,N,V_service
_ecID
_started
_totalLength
bytes
encodeWithCoder:
queryChipInfo:
_logContext
initWithPanicState:assertID:
isRequired
setChipEpoch:
transferFirmware:length:
tssKeyName:unitNumber:
_hashAlgorithm
b2pTimerForNSTimer:
stringByAppendingString:
TS,R,V_opCode
allocateUpdaterDFU
appendData:
_layer2Context
blockCount
delegateQueue
generateHashSHA512
initWithUnsignedInteger:
_bytesSent
_route
TC,R,V_portNumber
_chipRev
setManifestSuffix:
aceInfo
URLByDeletingLastPathComponent
_address
_iicUpdater
getThunderboltControllerForARMIODevice:
T@\"NSNumber\",&,V_chipID
appendData:descStr:
parseFileData
removeObject:
T@\"NSNumber\",C,V_trustedOverride
isValid
dfuModeEnabled
generateSubfileData
initWithHPMService:deviceService:enableDFUMode:
_b2pReset
allocateACE
appendBytes:length:
generateTLV:tlvValue:
opCode
_prefixNeedsUnitNumber
initWithService:isHCPM:
setPayload4cc:
tlvs
T@\"NSNumber\",C,V_demote
char4
T@\"NSData\",&,V_personalizedMetaData
TC,R,V_life
TC,R,V_enable
activeMinor
convertBytesToDwords:length:dWordBuffer:
retimerEnterForceDFU:
stringWithString:
_uarpQueue
tssRequestAsString
_dfuCheckHasRun
T@\"NSData\",R,V_writeData
propertyChanged
arrayWithObjects:count:
majorVersion
processMeasurementsForTSSOptions:unitNumber:asMeasurement:
setIsTrusted:
setLocatedObjects:
demote
initWithOptions:logFunction:logContext:deviceNamePrefix:
logInternal:arguments:
stringWithDescString:
writeRegister:buffer:length:
initWithRoute:status:data:
initWithSessionID:tag:
payloadData
_activeRevision
_boardRevision
digest
dumpATCRegisterWrite:value:
initWithByte0:
initWithContentsOfURL:
initWithData:
performUpdateWithDictionary:
_liveNonce
_minorVersion
TI,R,V_valid
_ace
configReadForIndex:result:
setCompressionAlgorithm:
setEffectiveProductionMode:
setEffectiveSecurityMode:
TQ,V_unitNumber
TS,R,V_activeRevision
_buildVersion
_connection
initWithFormat:arguments:
setIsRequired:
setSecurityEpoch:
tatsuMeasurements:
T@\"NSArray\",R,V_entries
TQ,R,V_majorVersion
_ticketNeedsUnitNumber
convertDwordToData:bytes:
initWithChipID:boardID:securityEpoch:productionStatus:securityMode:securityDomain:ecid:nonce:chipRev:
initWithFourCharacterCode:
setService:
_data
enableMixMatch
initWithDeadlineMS:type:queue:block:
route
writeToURL:error:
pendingRevision
dataWithContentsOfURL:
getTssRequest
_uarpContext
hasResponse
setKeyManifest:
TB,V_demote
setObject:forKeyedSubscript:
versionString
T@\"NSData\",&,V_personalizedData
_isTrusted
getAvailableReceiveDataLength
T@\"NSArray\",R,V_measurements
T@\"NSString\",R,V_name
TS,R,V_chipID
metaDataTable
TS,R,V_assetID
_pendingMajor
TC,R,V_blockCount
initWithRouterID:namePrefix:
T@\"NSData\",R,V_magic
_payloadIndex
_timer
setDelegate:
TS,R,V_version
fileExistsAtPath:isDirectory:
result
sessionData
setAssetID:
_enable
T@\"NSMutableArray\",&,V_trimmedTlvs
_scheduledTimers
_skipSameVersion
_totalBytesRequested
checkForVersionMatch:withBver:
getARMIODeviceRegistryEntryForACIOParentProperty:
TB,R,V_needsHostPersonalization
T@\"NSData\",R,V_nonceHash
configWriteMetadata:opCode:
sleepTimeForCommandResultPollIteration:
success
initWithChar1:char2:char3:char4:
initWithSessionID:status:data:
setDeviceService:
_powerForced
enqueueData:
setTssOptions:
dataWithContentsOfURL:options:error:
fileLength
_baudRate
_block
isDoneAggregate
_apChipRev
_securityEpoch
_tssRequest
initPluginInterfaceForService:
TI,R,V_magic
_tlvValue
data
effectiveSecurityMode
initWithFilePath:delegate:delegateQueue:
tlvFromPropertyListValue:
_chipID
T@\"NSData\",R,V_data
TI,R,V_tag
setFwPanic:
setSessionID:
unitNumber
TC,V_securityDomain
_digestListSize
tlvValue
forceRetimerPower:
shouldResetAfterUpdate
supportsSecureCoding
_state
epro
T@\"NSData\",R,V_digest
setTrimmedTlvs:
char3
payloadLongname
Ti,R,V_state
addObjectsFromArray:
applyFirmware
arrayWithObjects:
queryInfo
_b2pCommandInFlight
digestListSize
pendingMinor
setTrusted:
_handle
T@\"<AppleTypeCRetimerDFUDelegate>\",W,V_delegate
preparePayload:
TC,R,V_securityDomain
date
forceDFU
rid
_prefixNeedsLogicalUnitNumber
array
measurements
performReset
receiveData:
TI,R,V_chipRevision
_activeMinor
dumpResponse:
numberWithUnsignedInteger:
TB,R,V_productionStatus
_resultDescFunc
_serialNumber
initWithHPMService:routerID:deviceService:
stop
timer
_deviceInterface
_measurements
bytesAvailableToRead
nonce
_version
expandTLVs
_b2pContext
_writeQueue
deleteCharactersInRange:
verboseLog:
Ti,R,V_dataSessionStatus
_port
caseInsensitiveCompare:
configWriteForIndex:value:
initWithSessionID:state:
performUpdateDFU
stopTimerType:
dataWithContentsOfFile:
resetWithReason:
sendDataSessionDataCommandForSessionID:status:data:
bytesWritten
generateTatsuMeasurements:relativeURL:
setChipRev:
setTssOption:
_ecidData
initWithOptions:logFunction:logContext:
sendB2PCommand:responseClass:
setComplete
setEsec:
addSubfile:tag:
TS,R,V_esec
_dataSessionStatus
chipRev
_activeMajor
apChipRev
bootNonce
setTLVs:
T@\"NSData\",R,V_metaData
_delegate
_provisioning
TQ,R,V_buildVersion
_b2pSemaphore
_thunderboltController
composeTSSRequest:asMeasurement:
Ti,R,V_infoID
type
protocolVersion
TC,V_productionMode
T@\"NSData\",&,V_nonce
productionStatus
suppressed
_service
_suppressed
dfufTaskRunning
_pollingTimerSource
fwPanic
getBver
expandSuperBinary
fileExistsAtPath:
initIICServiceForRouterID:
keyManifest
printVersions
assetID
TI,R,V_logicalUnitNumber
generateHashSHA384
setLiveNonce:
writeToDestination
_iic
setTicketPrefix:
TQ,R,V_activeMinor
_deviceHandle
numberWithUnsignedShort:
startPollingForReceiveData
TC,V_route
_deviceService
ticketPrefix
_enableMixMatch
attributesOfItemAtPath:error:
dumpATCConfigRegisterRead:value:
receivedResponse:
TC,R,V_securityEpoch
_tssOptions
timeIntervalSinceDate:
T@\"UARPAssetVersion\",R,V_version
TB,R,V_forceDFU
_b2pReceiveBuffer
_portNumber
decodeBytesForKey:returnedLength:
T@\"NSString\",R,V_ticketPrefix
T@\"<AppleTypeCRetimerIICDelegate>\",W,V_delegate
skipDescendants
initializeUpdaterInstancesForcingPower:
performUpdateWithDictionarySingleStep:
dictionaryWithObjects:forKeys:count:
inputCommandWithOpCode:data:
personalizedData
queryTatsuSigningServer:ssoOnly:error:
writeToURL:
TC,R,V_ticketNeedsLogicalUnitNumber
TQ,V_ecID
_fileHandleWriteDestination
_pendingRevision
waitForCurrentRouterOperationToComplete:
_txFifoSpace
bytesSent:bytesTotal:
count
_epro
createUserClient
start
TB,R
updateWithFTAB:
life
tlvWithLength:value:
TC,R,V_provisioning
T@\"NSString\",C,V_payloadLongname
isTrusted
payload4cc
TC,R,V_routerID
queryHardwareID:
_querySemaphore
unlock
decodeCharForKey:key:
doCheckForRouterID:allowsNotReady:
dumpPacketType:data:
forceUpdateMode:
initUARPWithDeviceHandle:captureFileName:
sendManifest
TI,R,V_productionMode
TQ,R,V_ecID
stripHWModelSuffix:
log
_hpmInterface
hashAlgorithm
TI,V_assertID
char1
createPluginInterfaceForService:
payloads
startAppModeUpdateForSuperBinaryData:
TI,R,V_flavor
_bootNonce
_fileData
addObject:
arrayWithCapacity:
encodeObject:forKey:
_uarpChipCallbacks
executeIECSCommand:withData:dataLength:
forceDFUMode
startPacketDumperWithFileName:productID:
initWithString:
appendByte:
dumpATCMetadataRead:opCode:
flavor
generatePersonalizedSuperBinaryInternal:
parseCommand:
payloadIndex
TB,R,V_forceDFUMode
_productionMode
_debugLevel
_deviceNamePrefix
TQ,R,V_totalLength
_tatsuMeasurements
getManifest
setEpro:
TS,R,V_pendingMajor
_subfiles
nonceHash
waitForACEsWithRouterIDs:
boolValue
checkForVersionMatch:
effectiveProductionMode
_fwPanic
pollForB2PResponseForCommand:
TS,R,V_activeMajor
description
sendIdentificationCommand
TC,R,V_route
setNonceHash:
Ti,R,V_type
_life
_sessionID
bytesReceived
T@\"NSData\",C,V_manifest
_digest
receivedCommand:
registerIndexForVendorIndex:
setManifestEpoch:
T@\"UARPAssetTag\",R,V_tag
addSubfileWithTagName:subfileData:
writeData
T@\"NSNumber\",C,V_effectiveSecurityMode
initWithOutput:
serialNumber
T@\"NSData\",R,V_ecID
Tc,R,V_char3
createFileAtPath:contents:attributes:
initWithService:
isDoneSingleStep
_dataLength
_generation
_notification
_unitNumber
appleTypeCRetimerIICFifoTransferError:error:
copy
flavorField
initWithDelegate:socat:
boardID
TS,R,V_trusted
containsAllObjectsIn:
ecID
metaData
T@\"NSNumber\",&,V_ecID
_effectiveProductionMode
_entries
_notificationPort
allowOnlyIfConnected
setBoardID:
setState:
dumpPacket:type:metadata:metadataLength:
T@\"NSData\",C,V_nonce
T@\"NSNumber\",C,V_isTrusted
generateTLV
initWithOpCode:route:status:
logicalUnitNumber
setNonce:
T@\"NSDictionary\",R,V_tssRequest
T@\"NSString\",R,V_manifestSuffix
Ti,R,V_protocolVersion
doesNotRecognizeSelector:
inputCommandResponseWithOpCode:status:data:
totalBytesRequested
getBytes:range:
initWithFormat:
_protocolMode
dumpATCMetadataWrite:opCode:
initWithDeviceHandle:captureFileName:
manifest
availableRouterIDs
fileURLWithPath:isDirectory:relativeToURL:
objectForKeyedSubscript:
pendingVersion
setProvisioning:
T@\"NSNumber\",C,V_effectiveProductionMode
delegate
iecsWaitForIdle:pollInterval:timeout:
initWithFourCharacterCode:byte0:resultDescriptionFunction:
_payloadData
_pendingFile
initWithRouterID:
initWithVersionString:
queryChipIdentification
TS,R,V_boardID
_apHardwareID
_esec
boardRevision
doSet
initForRouterID:
T@\"NSString\",R
_pluginInterface
generateManifestForFTAB:hardwareID:apParameters:
T@\"NSArray\",R
_cfPlugInInterface
absoluteString
fileValidForOffset:length:
_dataWriteDestination
_ticketSuffix
performDfuUpdateForSuperBinary:withManifestData:
_notificationQueue
dumpAccessForRegisterAddress:ioReturn:data:
_dumper
T@\"NSData\",R,V_payloadData
_hpm
_nextUpdateProgressReportPercentThreshold
activeVersion
char2
T@\"NSNumber\",&,V_productionMode
TI,R,V_tlvLength
_space
liveNonce
setLogicalUnitNumber:
setPayloadIndex:
T@\"NSNumber\",&,V_securityDomain
_buffer
T@\"NSNumber\",R
_hpmService
_uarpSemaphore
_verbose
setMaxB2PFrameSize:
_logFunction
_subFileArray
manifestEpoch
performUpdateForSuperBinaryData:manifestData:apHardwareID:skipSameVersion:debugFlags:bver:
retimerEnterDFULegacy
totalLength
TI,R,V_tlvType
_forceDFUMode
initWithBVERString:
minorVersion
nonceString
TQ,R,V_boardID
_tag
_updaterInstances
createFileNameForFirmware:
needsHostPersonalization
_b2pLock
_dataPointer
TI,R,V_dataLength
cancel
securityEpoch
TS,R
TS,R,V_epro
_assertID
_isRequired
copyWithZone:
protocolMode
queryInfoSingleStep
removeItemAtPath:error:
TC,R,V_activeFile
TQ,R,V_bytesReceived
_url
pendingFile
pingChip
setPayloadLongname:
stringByExpandingTildeInPath
tssRequest
createFileHandleForWritingToURL:
generateHashSHA256
startPacketDumperWithBloodhoundDumper:
unsignedIntegerValue
_nextDFUManifestProgressReportPercentThreshold
T@\"NSData\",C,V_payloadDigest
T@\"NSString\",R,V_tag
layer2Context
b2pDataSessionOpenForSessionID:
_aggregateUpdateComplete
hash
infoID
isDone
command
_char3
getDeviceNames
T@\"AppleTypeCRetimerHardwareID\",R
_locatedObjects
TQ,R,V_bytesSent
_payload4cc
appendLittleInt16:
initWithBlockCount:value:
integerValue
routerID
T@\"NSDictionary\",&,V_tssOptions
_demote
Ti,R,V_sessionID
_userClientActive
setProductionMode:
Tq,V_hashAlgorithm
_nonceHash
_sessionData
appleTypeCRetimerIICFifo:receivedData:
dfuImageBytesSent:bytesTotal:
numberWithUnsignedChar:
numberWithUnsignedLong:
requestType
TC,R,V_productionStatus
Ti,V_state
_hpmConnection
_personalizedMetaData
_tlvType
initWithTag:dataPointer:dataLength:
length
personalizedMetaData
T@\"NSData\",R,V_nonce
TC,V_sessionID
TI,V_chipID
activeRevision
configureDataWriteDestination
dumpATCRouterOperationWithOpCode:data:
T@\"NSNumber\",&,V_boardID
subfileWithTag:
sessionID
_b2pQueue
generateFTABForData:manifestData:apHardwareID:debugFlags:
queue
setAssertID:
setBootNonce:
_flavor
_fifo
initWithDeviceHandle:
retimerExitForceDFU
ticketNeedsLogicalUnitNumber
T@\"NSData\",C,V_ecidData
entries
tag
_code
_filename
chipRevision
disableDFUfTaskIfActive
opCodeField
_securityDomain
assertID
bytesSent
receivedData:
sfwfBlockCount:length:
TI,R,V_tssOption
Ti,V_status
appendLittleInt32:
initWithData:metaData:tag:version:
setTicketNeedsLogicalUnitNumber:
transferError:
_metaData
initWithOpCode:
TC,R,V_prefixNeedsLogicalUnitNumber
TC,V_manifestEpoch
appendBool:descStr:
deviceService
iecsReadForAddress:buffer:length:flags:andOutReadLength:
init
_name
numberWithBool:
findCapabilityForRoute:port:space:mask:value:offset:
removeAllObjects
setDemote:
subdataWithRange:
subfiles
T@\"NSData\",&,V_manifest
containsObject:
TC,R,V_liveNonce
_ecid
enable
setChipRevision:
TC,R,V_apChipRev
_filePointer
_updaterIndex
dateByAddingTimeInterval:
initWithMajorVersion:minorVersion:releaseVersion:buildVersion:
queryManifestForFTAB:
TQ,R,V_releaseVersion
_uarpInitialized
addSubfiles:
manifestSuffix
setMaxTransmitAttempts:
setSuffixNeedsLogicalUnitNumber:
maxB2PFrameSize
_tssOption
nextObject
performUpdateIIC
setTrustedOverride:
startPacketDumperWithFileName:productID:dataSessionProtocol:
timerFired:
writeToData
T@\"NSTimer\",R,V_timer
queryHardwareID
_aceInfo
_boardID
_chipEpoch
_magic
iecsWriteForAddress:buffer:length:flags:
T@\"NSString\",R,V_aceInfo
_nextDFUFirmwareProgressReportPercentThreshold
requiresPersonalization
sendDFUImage:length:
TI,R,V_payloadIndex
_b2pLinkLinearBuffer
_trimmedTlvs
performRouterOperationWithOpCode:metadata:dWordBuffer:dWordCount:returnStatus:
T@\"NSArray\",R,V_tlvs
TI,R,V_flavorField
_char4
_securityMode
_tlvLength
_uinitNumber
writeData:error:
TB,R,V_securityMode
TB,V_provisioning
dumpCommand:
TB,V_suppressed
TB,R,V_isDone
_category
removeSubfile:tag:
T@\"NSData\",C,V_sessionData
_payloads
initWithData:encoding:
status
_suffixNeedsLogicalUnitNumber
dumpRegisterOperation:registerNumber:value:
ecid
firmwareStagingCompleteWithStatus:reason:
requiredTSSOptions
setStatus:
trustedOverride
appendFormat:
queryHardwareParameters
setEnableMixMatch:
tlvLength
_forceDFU
configureFileHandleWriteDestinationForURL:
enumeratorAtPath:
TC,R,V_manifestEpoch
_value
filename
initWithData:delegate:delegateQueue:
setPayloadDigest:
Tc,R,V_char2
_b2pResponse
_delegateQueue
_ticketPrefix
doCheckForRouterIDList:allowsNotReady:
longLongValue
persistent
setEcidData:
T@\"NSArray\",R,V_payloads
_blockCount
initUARP
queryRetimerPanicStatus:
startMonitoringForOperationCompletion
TQ,R,V_totalBytesRequested
appendString:
internalFirmwareVersion
_result
initDebugFlags:
_singleStepMode
_suffixNeedsUnitNumber
stringWithUTF8String:
useLocalSigning
activeMajor
chipEpoch
chipInfo
verifyRouterIsNotEnumerated
_debugFlags
esec
ftabWriteData:error:
T@\"NSData\",R,V_bootNonce
TI,R,V_securityDomain
_dfuUpdater
_allowOnlyIfConnected
_logicalUnitNumber
parseResponse:
sendData:
TI,R,V_generation
_char2
getNeedsHostPersonalization
portNumber
Ti,V_debugLevel
TI,R,V_bytesWritten
_ticketNeedsLogicalUnitNumber
initWithDeviceHandle:queueLabelSuffix:
initWithWriteData:
now
_ms
getTlvs
UTF8String
encodeBytes:length:forKey:
unsignedIntValue
_log
codeString
transferDataBuffer:length:sessionID:
TQ,R,V_fileLength
_panicStatus
productionMode
queryComplete
_status
_enabled
ecidData
numberWithUnsignedLongLong:
setEcID:
stringWithFormat:
TS,R,V_hashAlgorithm
_interface
category
defaultManager
unsignedShortValue
_manifestSuffix
_needsHostPersonalization
log:
debugLevel
hasSuffix:
TS,R,V_pendingRevision
destroyUserClient
getDelegateQueue
TC,V_life
dataWithData:
sendDataSessionConnectCommandForSessionID:state:
Tr*,R,V_filePointer
dfuWithFTAB:forcePersonalize:
payloadDigest
registerReadForVendorIndex:result:
sendResponse:
enabled
_notificationSemaphore
fileHandleForWritingToURL:error:
tlvFromKey:value:
service
_skipUpdates
addEntriesFromDictionary:
startTimerType:deadlineMS:
TI,N,V_deviceService
readRegister:buffer:length:
retimerExitDFU
setLayer2Context:
_majorVersion
dataPointer
executeTask:
objectAtIndexedSubscript:
tlvTypeName:
retimerRemoveForcePower
tlvFromType:length:value:
dumpATCRegisterRead:value:
getAddressForDeviceService:
@32@0:8C16i20@24
B28@0:8@16S24
Q
B24@0:8C16B20
@\"NSTimer\"
^?
B48@0:8@16@24@32Q40
B32@0:8I16*20I28
i
B20@0:8I16
@28@0:8Q16B24
B24@0:8^{UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}16
@\"NSObject<OS_os_log>\"16@0:8
@\"<B2PEngineDelegate>\"
@20@0:8S16
@24@0:8^{ATCRTTaskSFWdOutput=I}16
@\"UARPAssetTag\"
@36@0:8@16r^v24I32
@\"NSURL\"
c16@0:8
B48@0:8S16^I20^I28I36^I40
C
^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHe
@44@0:8@16^?24^v32B40
@40@0:8I16i20@24@?32
@?
@32@0:8I16C20^?24
@28@0:8S16@20
B28@0:8I16^I20
@\"ThunderboltInterface\"
@\"NSObject<OS_dispatch_queue>\"
@24@0:8I16C20
I24@0:8@16
B20@0:8B16
q24@0:8@16
I16@0:8
B28@0:8@16B24
I20@0:8I16
^^{IOThunderboltLibInterfaceStruct}
v32@0:8@16@24
@40@0:8@16@24@32
@32@0:8I16I20^v24
@28@0:8S16C20i24
@32@0:8Q16Q24
{?=\"cb\"[208C]\"dbg_stats\"{?=\"response_timeouts\"I\"midpacket_timeouts\"I\"tx_packet_retry_cnt\"I\"max_tx_level\"I\"rx_packet_cnt\"I\"rx_packet_err_cnt\"I\"tx_packet_cnt\"I}\"client_context\"^v}
@28@0:8I16@20
q
@32@0:8@16#24
v20@0:8B16
v36@0:8r*16I24^I28
v44@0:8@16I24^v28Q36
i24@0:8@16
@24@0:8I16B20
i64@0:8I16^v20Q28^v36Q44I52Q56
c
B
i32@0:8C16r^v20I28
@\"AppleTypeCRetimerFifoQueue\"
@32@0:8@16Q24
^v
B32@0:8^B16@24
@24@0:8@\"NSCoder\"16
v20@0:8i16
@24@0:8B16B20
B36@0:8@16B24^@28
B24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16
@28@0:8I16C20I24
v28@0:8B16r*20
v36@0:8I16^?20r*28
B16@0:8
B20@0:8C16
Q16@0:8
S16@0:8
B44@0:8Q16I24I28I32^I36
v32@0:8S16i20@24
@48@0:8@16@24@32Q40
@32@0:8S16C20@24
@\"NSString\"
@\"AppleTypeCRetimerIICDeviceHandle\"
^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}
@48@0:8@16^?24^v32@40
B32@0:8r*16I24C28
@\"ThunderboltPacketDumper\"
@24@0:8^{ATCRTTaskSFWfOutput=I}16
i16@0:8
@\"NSData\"40@0:8@\"FTABFile\"16@\"AppleTypeCRetimerHardwareID\"24@\"NSDictionary\"32
v20@0:8S16
@60@0:8S16S20C24C28C32C36Q40@48C56
i20@0:8B16
B32@0:8r^v16Q24
I
B28@0:8^I16S24
i32@0:8C16^v20I28
v24@0:8I16S20
@\"<AppleTypeCRetimerDeviceHandle>\"
{uarpChipCallbacks=\"fRestoreMsgRecv\"^?\"fRestoreDataRecv\"^?}
@\"AppleTypeCRetimerPanicStatus\"
@24@0:8C16C20
@28@0:8C16@20
B32@0:8@16S24C28
@16@0:8
@\"B2PEngine\"
@24@0:8Q16
v20@0:8C16
@36@0:8Q16@24B32
r*16@0:8
v16@0:8
@\"<AppleTypeCRetimerIICFifoDelegate>\"
^^{AppleHPMLibInterfaceStructV3}
[262144C]
v24@0:8I16I20
@24@0:8^@16
v32@0:8@\"AppleTypeCRetimerIICFifo\"16@\"NSData\"24
@\"AppleTypeCRetimerDFU\"
B24@0:8I16S20
@32@0:8@16@24
@\"NSMutableDictionary\"
C28@0:8r*16I24
B52@0:8@16@24@32B40Q44
i48@0:8C16^v20Q28I36^Q40
@\"B2PIdentificationResponse\"
C16@0:8
@48@0:8@16@24@32@40
@\"NSString\"16@0:8
@28@0:8@16B24
@\"NSLock\"
v32@0:8@\"AppleTypeCRetimerIICFifo\"16@\"NSError\"24
v32@0:8C16I20@24
v20@0:8I16
S
@20@0:8I16
@\"ACE\"
@\"AppleTypeCRetimerIICFifo\"
@\"NSMutableData\"
v32@0:8I16I20r*24
@48@0:8Q16Q24Q32Q40
@24@0:8B16I20
B24@0:8I16I20
v28@0:8I16I20C24
@20@0:8C16
v28@0:8S16I20S24
v24@0:8@\"NSString\"16
@\"<AppleTypeCRetimerIICDelegate>\"
@\"NSFileHandle\"
@\"NSObject<OS_os_log>\"
@\"B2PResponse\"
@\"AppleTypeCRetimerFifoDumper\"
B48@0:8Q16I24I28I32I36^I40
v24@0:8^v16
@24@0:8I16S20
@24@0:8^{_NSZone=}16
q16@0:8
@40@0:8C16Q20I28I32I36
B32@0:8@16@24
v24@0:8q16
@\"NSArray\"
@\"<AppleTypeCRetimerUpdaterIICDelegate>\"
@40@0:8@16^?24^v32
B24@0:8@16
@24@0:8I16I20
B40@0:8Q16I24I28I32I36
@\"<UARPSuperBinaryDelegate>\"
v24@0:8i16I20
@\"FTABSubfile\"
B24@0:8^B16
@\"IECSInterface_GoldRestore2\"
B28@0:8r*16I24
@\"<AppleTypeCRetimerDFUDelegate>\"
B24@0:8I16C20
@\"UARPAssetVersion\"
B32@0:8@16o^@24
@\"<AppleTypeCRetimerUpdaterInstanceDelegate>\"
@32@0:8c16c20c24c28
v24@0:8Q16
B60@0:8@16@24@32B40Q44@52
B40@0:8r^v16Q24@32
@\"AppleTypeCRetimerIIC\"
@\"NSDictionary\"
@\"NSObject<OS_dispatch_semaphore>\"
^^{IOCFPlugInInterfaceStruct}
@\"NSMutableArray\"
B32@0:8Q16@24
^v16@0:8
@\"ATCRTBloodhoundPacketDumper\"
@\"AppleTypeCRetimerHPM\"
i28@0:8I16I20I24
I28@0:8r*16I24
v24@0:8@16
@24@0:8C16i20
@\"NSData\"
@28@0:8I16Q20
[65536C]
v28@0:8S16I20I24
v28@0:8S16@20
@24@0:8@16
v32@0:8@16*24
@28@0:8I16I20B24
@\"AppleTypeCRetimerHardwareID\"
@\"<AppleTypeCRetimerUARPUpdaterInstanceDelegate>\"
@32@0:8Q16^v24
@\"ATCRTAPHardwareID\"
@40@0:8Q16S24C28C32I36
@\"NSObject<OS_dispatch_source>\"
v36@0:8@16Q24B32
v32@0:8@16r*24
i40@0:8C16^v20Q28I36
r*32@0:8@16@24
B24@0:8^I16
@28@0:8^I16I24
@\"FTABFile\"
@\"NSMutableString\"
@32@0:8C16@20B28
v24@0:8^{uarpChipCallbacks=^?^?}16
@40@0:8C16i20C24i28@32
v24@0:8@\"NSCoder\"16
@\"NSNumber\"
^{IONotificationPort=}
r*
@\"AppleTypeCPacketDumper\"
@36@0:8S16C20i24@28
@\"AppleTypeCRetimerUpdaterIIC\"
LZ4
assert
UarpRestoreRemoteEndpointAddHandler
\tNonce: %@\n
\tSecurity Domain: %u\n
com.apple.accessoryupdater.atcrt
\tPort Number: %u\n
sections
Unsupported
Unsupported Asset Tag
\tRID: %@\n
\tActive Version: %@\n
fPayloadMetaDataTLV
Filepath
EventID
Cancelled Asset Tag
Timer,RTKitOS
CoreUARPRestoreAssetTransferProgress
Personalization Matching Data
com.apple.accessoryupdater.ftab
Bad Argument
Yes
UARP Restore: %s: fLayer3ApplyStatus is NULL
RTKitOSFeature
generic error
Payload Signature
Integer
Active Firmware Version Greater than Asset
Version Discovery Request
Enabled
rt13-failure-panic
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestMetaData failed with status: %u
RTP
\tVersion: %s\n
unrecognized
HDS
- Version is %u.%u.%u.%u
\tState: %s
fuse locked
Timer,RTKitOS,%u
Personalization Security Mode
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetRequestMetaData failed with status: %u
Log Serial Number
Payload Metadata <0x%08x>
Wait %u seconds for retimer(s) to reboot.
\tEnable: %s\n
Version BVER File
EventFields
\tValue: 0x%02x
Verify Fail
Failed to parse updated super binary
UARP Restore: %s: Query %d info properties and %d Apple properties
isTrusted
Host Minimum Battery Level
DeploymentList
SocLiveNonce
app
https://mesu.apple.com/assets
Personalized Manifest
Payload Compression ChunkSize
Voice Assist Locale
%s: NULL pUarpCtx
UploaderRetryLimit
-[HPMForceRetimerDFUModeSetter doSet]
DebugFlags
<%@: 0x%02x>
ready
Needs Restart
Personalization Required
diags
Minimum Required Version
Unknown
BT
Plaform specific
...Unable to find parent for IECS service.  err = 0x%X
Version Mismatch
com.apple.%@.apply
Sysconfig Region Code
Invalid Data Request Offset
suffix_length <= max_name_length
dfu
%s: Device panicked %@
%s: DFU complete for %@
%@: Continuing after UARP apply has completed.
UARP.RESTORE.LAYER3.WATCHDOG.EXPIRE
Vendor Specific
%@ has new firmware version: %@ (%@)
UARP Restore (Asset Solicitation): %s: Asset fully staged
Signature Write Error
las_tunableh_write
%s:%d:%s: %s\n
-[AppleTypeCRetimerUARPUpdaterInstance initWithRouterID:delegate:forcePower:]
com.apple.%@.fifo_delegate
CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
\t\tECID: 0x%016llx\n
%@: FIFO transfer error (%@)
Personalization FTAB Payload Security Mode
buddy
silicon
MetaData plist
Endian
Endpoint Bulk Information Request
-[AppleTypeCRetimerDFU b2pDataSessionOpenForSessionID:]
UARP Restore: %s: fLayer3AssetSolicitationStatus is NULL
IM4M
Deferred DFU check failed.
Payload Hash
BTLEServer
Endpoint Bulk Information Response Ack
BundleDataDict
Personalization Enable Mix Match
UARP Restore: UARP RX: Asset Available Notification; Asset ID %u
EventName
%c%c%c%c
%s: Error reading from register %s(0x%x)
TtrSolicitLogs
Sysconfig Manufacturing Part Number
countryList
Write Data
%s: Falling back to DFU mode for %@.
Name
<%@: %u>
fAssetReady
Personalization Payload Digest Filename
Sync
com.apple.%@.hw_id_fifo_delegate
<Type = 0x%08x, Length = 0x%08x>
Duplicate Controller
https://gs.apple.com:443
com.apple.uarp.UARPUpdaterServiceHID.personalizationNeeded
Bytes Written: %u
close
HCPM
UARP Restore: Offered Firmware with outstanding offer
1
Path
parsing
Higher Version Active
-[AppleTypeCRetimerDFU sendPingCommand]
CoreUARP Restore IM4M: Post-Layer3: TSS Response is NULL
TicketName
\t\tChip ID: 0x%02x\n
PreflightTickets
hashAlgorithm
Invalid TLV
SFWd was not run
%@%u
Running DFU check for deferred router IDs.
DFU image
Personalization Matching Data Payload Tags
SupportsHeySiriCompact
Assets
UarpRestoreAssetSolicitation
Failed to locate firmware super binary payload when updating super binary
on
tethered
AirPods case FWUP iAUP server session
FirmwareVersionBuild
ACE Not Found
File Not Found
Failed to allocate device handle for %@ during Updater instance initialization
Boolean AppleTypeCRetimerUARPUpdaterReset(AppleTypeCRetimerUARPUpdaterRef _Nonnull, CFErrorRef * _Nullable)
-[AppleTypeCRetimerDFU transferDataBuffer:length:sessionID:]
Host Personalization Required
Payload Expand Filename
SupplementalAssets
Personalization Matching Data Product Revision Maximum
Minimum watchOS Version
ProductNumber
Failed to query hardware ID for router ID %u
Excluded Hardware Version
tmpfiles
com.apple.Bluetooth.AccessoryCase.pif_daily
\t\tSession ID: %u\n
AppleARMIICDevice
Downstream Endpoint Unreachable
%@:\n\tOp Code: 0x%04x\n\tRoute: %s
Failed to locate RRKO payload in super binary
UARP Restore: Failed to process rx uarp message
Duplicate Message ID
las_tunableh_init_plaintext
%lu.%lu.%lu.%lu
UarpRestoreLayer3TssRequestQueueHandler
AppleARMIODevice
dbgb
Unable to create DFU updater for %@
Personalization FTAB Payload Trusted
Waiting for ACEs with routerIDs: %@. Available ACEs: %@.
test session
char1
Bad Sequence Number
HardwareID
Dynamic Asset PreProcessing Notification Ack
<%@ panicState=%d assertID=%u>
https://basejumper.apple.com/livability/
UnsignedInteger
hidPersonalizationNeeded
Sysconfig Regulatory Model Number
UARP Restore: EOF %d, Read %zu bytes
CoreUARPRestoreAssetRescindStatus
UARP Restore: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
Accessory
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Apple - %d )
_brd
fAssetProcessingNotification2
sysdiagnose_approved
Invalid Update
Failed to access router ID %u in DFU mode. Bytes sent: %lu, bytes received: %lu
fRestoreUARPDynamicAssetOffered
Device Specific Data
/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/Current/Resources
Warning: Unable to locate ticket name: %@
queryInfo
CoreUARPRestoreQueryOutstandingInfoProperties
MCU
Personalization Payload Demotion Production Mode
USB-PD Location
log_version
Invalid Object
Personalization Security Domain
fPayloadDataComplete
%02x
payloadDigest
Payload 4CC
streaming
Performing DFU for %@
ESEC
-[AppleTypeCRetimerUARPUpdaterInstance applyFirmware]
UARP Restore: %s: Provided filepath is greater than max filepath length %i
Apple Inc.
Float
HeySiri Model Role
FieldLength
las_tunableh_fig_get_expression
Timer,ProductionMode,%u
All ACEs are available
\tStatus: %u (%s)\n
%s: fatal error detected at this stage.
Payload Version
Buffer Overflow
Rejected
SuperBinary Firmware Version
FirmwareBundle
FieldType
%s: Update failed for %@
RT13 B2P Queue
fAssetMetaDataTLV
payload4cc
A
IM4M-CoreUARPRestore-%d-%02d-%02d-%02d-%02d-%02d.uarp
\t\tSecurity Domain: %u\n
\tVersion: %u\n
Minimum tvOS Version
Invalid Data Transfer Notification
DFU complete for %@
-[AppleTypeCRetimerDFU readData]
-[AppleTypeCRetimerIICDeviceHandle initIICServiceForRouterID:]
sbd1
Compressed Headers Payload Index
Success
UarpRestoreLayer3MsgSendQueueHandler
HPMForceRetimerDFUModeSetter
SecurityMode
Personalization Logical Unit Number
ACE
CertificateSecurityMode
FirmwareData
expr
0000
Processing Incomplete
Timer,ECID,%u
Using local signing: %s
\tData: %@\n
\tGeneration: 0x%08x\n
Failed to parse FTAB file
Failed to parse updated FTAB data
UARP Restore (Asset Solicitation): %s: pPayload->_fp is NULL
SingleStepMode
hpm
Active Firmware Version Equal to Asset
%lu
Personalization SuperBinary AssetID
effectiveProductionMode
SupportedAccessoriesUARP-Internal.plist
SupportedAccessoriesUARP-InternalFuture.plist
-[FTABFile parseFileData]
%s: Device panicked <%@ panicState=%d assertID=%u>
Voice Assist Role
\t%s: %@\n
-[ACE dfufTaskRunning]
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetSetPayloadIndex failed with status: %u
crashlog
MetaData Corrupt
%s: Starting update for %@
No Memory
/var/db/accessoryupdater/uarp/
rtpf
Personalization Payload Effective Production Mode
Personalization Payload Demotion Security Mode
Mid Upload
Apply Staged Assets Request
ATCRT_REG_FIFO_TX
Failed to locate RRKO data
-[AppleTypeCRetimerUARPUpdaterInstance checkForVersionMatch:withBver:]
Personalization Ticket Needs Logical Unit Number
Urgent Update
Payload Ordered Index
Personalization Payload Longname
B2PHID
FIRM
Personalization Production Mode
Life
%s: NULL pIM4M
ProductName
ServiceBSDNotifications
Downstream Endpoint Reachable
%s: Failed to start UARP update for %@ (%s)
RTKitOS
SupportsAccMode7
las_tunableh_initialized()
-[HPMForceRetimerDFUModeSetter startMonitoringForOperationCompletion]
void triggerSystemPanic(NSString * _Nonnull __strong)
ace
IOReturn 0x%08x
%@: New firmware version %@ (%@)
DeferredCommit
Router ID %u not ready for DFU check.
UARP Restore: UARP RX: Asset Processing Notification ACK; Asset ID %u
Host Inactive To Stage Asset
Host Trigger Battery Level
Unrecognized
UARP.LAYER3.APPLY.ASSETS - Not Implemented
-[AppleTypeCRetimerIIC transferFirmware:length:]
ProductType
HID
address=0x%llx mask=0x%llx writable=0x%llx...\n
ForceLocalSigning
system config
App Start Failed
%@: Waiting for UARP apply to complete...
YES
Failed to set FIRM payload index; %u
\tState: %u (%s)
Asset Id Unknown
-[ThunderboltInterface createPluginInterfaceForService:]
enable
- MetaData length is %u
com.apple.uarp.daemon
UARP Restore: Failed to tx uarp message
ok
Dynamic Asset Solicitation
SecurityDomain
Personalization Suffix Needs Logical Unit Number
stop
<%@ len=%lu>
%s: Unable to query hardware ID in DFU mode for %@.
CoreUARPRestoreAssetApplyStatus
Out Of Order Message ID
SupportsFriendlyName
FirmwareImageFile
bug_type
accessory_pid
-[ThunderboltInterface findCapabilityForRoute:port:space:mask:value:offset:]
BOOL isPanicEnabled(char *)
Personalization Options Required
\tProtocol Version: %s
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetQueryNumberOfPayloads failed with status: %u
bad argument
Minimum macOS Version
Invalid EndpointID
Downstream Endpoint Discovery Ack
UARP Restore (Asset Solicitation): %s: fseek failed
UARP Restore: %s: Protocol Version Selected %d, was previously %d
https://basejumper.apple.com/mesu_staging
BSDNotifications
DecodedCrashLogChildKey
thunderbolt-drom
SHA-512
FirmwareVersionMinor
Analytics Event Name
VoiceAssist
chip_metadata
Device Error
App
Header Not Found
-[AppleTypeCRetimerIICFifo drainTransmitQueue]
Too many queryInfo calls!
com.apple.uarp.BTLEServer.personalizationNeeded
Voice Assist Type
FTAB %@:\n
%s: NULL pBuffer
%s: NULL tssOptions
-[AppleTypeCRetimerIICDeviceHandle writeRegister:buffer:length:]
%@: DFU manifest transfer: %u%%
minorVersion
%@,%@
APInfo
\t\tBoard ID: 0x%04x\n
\tSecurity Domain: %u
com.apple.uarphidd
UARP Restore: %s: uarpPlatformEndpointSolicitDynamicAsset() failed; 0x%08x
VendorName
isPowerSource
UARP Restore: Read error %d, Read %zu bytes
CoreUARP Restore IM4M: First Pass on TLV <0x%08x>
%@\n
com.apple.accessoryupdater.uarp
Personalization Prefix Needs Logical Unit Number
unknown
Flash Section Length
SupportsDeveloperSettings
dynamicassets
Controller
-[AppleTypeCRetimerDFU sendDataSessionConnectCommandForSessionID:state:]
%s: Fatal error, no iic devices found for prefix %@.
Payload MetaData
-[AppleTypeCRetimerUpdaterInstance performUpdateIIC]
UARP Restore: Failed to offer superbinary, status 0x%08x
Digest
com.apple.UARPUpdaterServiceUSBPD
IECSInterface::createUserClient...
UARP Restore: %s: fLayer3PersonalizedFirmware is NULL
bver
RestoreRTKitOS
yboot
no
Personalization FTAB Payload Digest
Host Inactive To Apply Asset
Compose Payload Hash Algorithm
USB-PD Device Class
CmapEvents
Invalid Function Pointer
Skipping update for %@ because the retimer chip is deprecated.
Bluetooth
UarpRestoreEndpointDataRecvQueueHandler
-[AppleTypeCRetimerIICFifo getAvailableReceiveDataLength]
UARP Restore: %s: Asset fully transfered; %c%c%c%c
Did NOT find service(s) matching AppleHPMDevice(index:%d)
com.apple.%@.fifo.%@
Info
All ACEs are now available.
idle
UploaderResponseTimeout
Nothing Staged
UARP Restore Layer 3: Stage Status; status <0x%04x>, reason <0x%04x>
las_tunableh_fig_get_value
\tSession ID: %u (%s)\n
\t\tChip Revision: %u\n
%u
Personalization Matching Data Product Revision Minimum
Upload Abandoned
LocalSigningID
com.apple.notifyd.matching
Personalization SuperBinary Payload Index
status
releasenotes
Bad Command
Voice Assist Certificate
ATCRT Command: %@
Asset Data Paused
Invalid Message
Asset Not Found
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (after to IOCreatePlugInInterfaceForService or at exit)
char2
ACE2 No FET
Nonce
atcrt
USB-C_%s
\tECID: 0x%016llx\n
DeviceInfo
I
Unexpected type for retimer debug flags: %@
UARP Restore: %s: fLayer3FirmwareStageStatus is NULL
ApChipID
Address
SuperBinary Payloads
Dynamic Payload
\tInternal FW Version: %s\n
%@: DFU firmware transfer: %u%%
LZBitmap2
UARP Restore: %s: pAsset is NULL
UARP.LAYER3.TRANSFER.PAUSE - Not Implemented
rkof
BVER
Personalization FTAB Payload Production Mode Host Override
UARP.LAYER3.TRANSFER.RESUME.ACK - Not Implemented
FieldPrivacyRestricted
Staged Firmware Version Equal to Asset
Same Version Active
UarpRestoreStageFirmwareDataBufferQueueHandler
ApBoardID
CoreUARP Restore IM4M: CoreUARPRestoreBuildPersonalizationResponse: %d 
No iic devices found for prefix %@, nothing else to do.
Host Network Delay
Invalid Payload Header
Failed
UarpRestoreApplyStagedAssetsHandler
-[AppleTypeCRetimerDFU sendB2PCommand:responseClass:]
-[AppleTypeCRetimerDFUChecker doCheck]
phyb
https://mesu.apple.com/assets/macos/
IECS command '%c%c%c%c' still outstanding
\tFirmware Version: %02X%01X.%01X%02X.%02X\n
atcrtu
RestoreInternal
\tHardware ID:\n
Unable to create IIC device handle for %@%u
fPayloadWriteToAsset
request
...Unable to create CFPlugInInterface. err = 0x%X
Timer,Nonce,%u
-[AppleTypeCRetimerIICBase queryRetimerPanicStatus:]
\tBoard ID: 0x%08x\n
reserved
AirPods FWUP iAUP client session
Analytics Payload Type
DownstreamAppleModelNumbers
Unknown Data Transfer State
<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u
Information Request
UarpRestoreEndpointMsgRecvQueueHandler
/Library/Caches/com.apple.xbs/1B41C110-6977-45B0-93CC-2DE6B66CB3A1/TemporaryDirectory.WwQFnM/Sources/libAppleSilicon/tunableh/v2/tunableh.c
ATCRT_REG_FIFO_RX
\t\tNonce: %@\n
rkos
AOP
Payload Hash Algorithm
Asset Data Transfer Notification Ack
UARP Restore (Asset Solicitation): %s: fAssetProcessingNotification2 not implemented
Force DFU
Personalization Manifest Prefix
Router ID %u not ready for DFU check after IIC check failed.
response
name
,%lu
locust device
com.apple.system.powermanagement.poweradapter
SOP
Personalization Failure
User Client Access Error
AppleTypeCRetimerUpdaterUtils.m
\t\tTag: %@\n
Invalid Offset
Endpoint Discovery Request
ThunderboltDROM
com.apple.%@.updater
start
Payload Filepath
HeySiri Model Digest
taptoradar
CrashLogKey
Unknown Failure
-[HPMForceRetimerDFUModeSetter propertyChanged]
SecurityEpoch
SoftwareBinaryDsp1
secure boot
system
Minimum iOS Version
Asset Rescinded Notification
\tType: %s\n
\tMagic: 0x%08x\n
Personalization FTAB Payload
SupportsAnalytics
yes
retimer
HeySiri Model Signature
rampPeriod
Did NOT find service matching AppleHPMDevice
%s: NULL pIM4M->payloads
Version match: Failed to query chip Bver for %@
battery
Endpoint Bulk Information Response
DFU failed for %@
FW upgrade was not in IDLE state
\tProtocol Version: %s\n
%@: options = %@
fPayloadReady
SHA-384
-[ACE retimerForcePower]
enabled
HeySiri Model Type
Personalization FTAB Payload Hash Algorithm
\tFlavor Field: %u
CoreUARP Restore IM4M: Building Personalization Response
Timer,SecurityDomain,%u
BuildIdentity
SkipSameVersion
com.apple.AppleAccessoryManager
tmap
Information Response
-[AppleTypeCRetimerDFU sendIdentificationCommand]
<%@: \r
    >
case
InputDictionary
-[FTABFile addSubfileWithTagName:contentsOfURL:]
Personalization Manifest Epoch
MetaData Format Version
SupplementalAssetsModelNumber
Dynamic Asset Solicitation Ack
UarpRestoreAssetSolicitationHandler
CertificateProductionStatus
Personalization Provisioning
Personalization ECID
%s: Failed to start firmware apply for %@ (%s)
%s: IIC Communication Error: Failed to query %@ panic status.\n%@
Personalization FTAB Payload Longname
Apply failed for router ID %u
HeySiri Model Engine Version
SupportsVersions
SupportedAccessoriesUARP.plist
<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u
uarp
Timer,SecurityMode,%u
SupportsVoiceAssist
UarpRestoreStageFirmwareFilenameQueueHandler
Perform update input = %@
https://basejumper.apple.com/assets/
memory
las_tunableh_get_fig() == NULL
ProductionMode
%@: Attempting to query hardware ID via UARP.
Personalization Board ID
SupportsPowerlog
AllowDownloadOnCellular
UI_country_code
Unknown Controller
char4
Tethered Preflight
ACIBT
BluetoothProductVersion
Not Found
UARP Restore Layer 3: Apply Staged Assets; status <0x%04x>, flags <0x%04x>
UarpRestoreLayer3UarpPropertyUpdateQueueHandler
crashlogs
.
Missing Remote
Disable Scan
Personalization Payload Tag
ManifestPrefix
UARP Restore: Failed to allocate restore asset
manifest
im4m
com.apple.system.powersources.source
SectionName
Downstream Endpoint Message Ack
IOPCIDevice
\tPersistent: %s\n
UARP.RESTORE.LAYER3.INFO.RESPONSE <Statistics> - Not Implemented
MetaData Overflow
AppleHPMDevice
thunderbolt
Subfile: type=%@, length=%u
SupportsMappedAnalytics
Mismatch Data Offset
Update complete for %@
-[ACE disableDFUfTaskIfActive]
fAssetSetBytesAtOffset2
,Ticket
Skipping update for %@ because it already has this firmware version.
%@/%@
Timed out or aborted
\tSecurity Mode: %s\n
Personalization Chip Revision
PreflightRequired
effectiveSecurityMode
-[AppleTypeCRetimerDFU receivedCommand:]
LZBitmapFast2
right bud
Value
BluetoothVendorIDSource
pcapfiles
Failure
ApSecurityMode
MLB
tatsuSigningServer
Mismatch UUID
Data Request
Endpoint Bulk Information Request Ack
None
Personalization Board ID (64 bits)
No Resources
Asset Decompression Failure
Better Transport
VendorID
\tProduction Status: %s\n
UARP.LAYER3.WATCHDOG.CANCEL
com.apple.UARPUpdaterServiceHID
analytics_test_mode
las_tunableh_init
name_length <= max_name_length
v8@?0
\t\tSecurity Epoch: %u\n
%@: Firmware staging failed. Status: 0x%08x (%s), Reason: 0x%08x (%s)
<%@: 0x%08x>
<%@: 0x%016llx>
OTA Stage 1
protocolcontroller
%@:\n
%@: Performing DFU
ProductGroup
Invalid Asset Tag
Voice Assist Signature
Case
FirmwareVersionRelease
- Tag is %c%c%c%c
UARP Restore (Asset Solicitation): %s: uarpAssetQueryPayloadInfo failed with status: %u
untethered
Endpoint Discovery Response
rrko
performNextStage
BootedOS
goLiveDate
_dev
\tManifest: %@\n
\t%s: %s (%u)\n
Upload Denied
\tProtocol Mode: %s
Low Battery
Asset Available Notification Ack
Invalid Host
-[ThunderboltInterface configReadForRoute:port:space:index:result:]
w+
Asset Invalid Compression
UARP Restore: Tatsu Server set to %s
Force DFU Mode
Payload - 4cc <%@> - Version <%@> - TLVs - %@
Serial
No Firmware Update Available
Boot
Timer,ChipID,%u
Force DFU mode is %s
Router ID %u placed into DFU mode
digestListSize
Personalization FTAB Payload Digest Filename
AppleHCPM
Disabled
InfoArray
queryTags
aopf
Personalization Digest List Size
Dynamic Asset PreProcessing Notification
UARP Restore Layer 3: Solicit Status; status <0x%04x>, reason <0x%04x>
Failed to locate Bver.
HeySiri Model Engine Type
\tEntry:\n
Unknown Payload
Invalid Super Binary Header
las_tunableh_device_has_chip_number(self)
- Data length is %u
Forcing power on for router ID %u
left bud
Staged Firmware Version Greater than Asset
Allow Only if Connected
-[AppleTypeCRetimerUARPUpdaterInstance performDfuUpdateForSuperBinary:withManifestData:]
Compressed Headers
/System/Library/PrivateFrameworks/CoreUARP.framework
releaseVersion
-[AppleTypeCRetimerDFU writeData:]
@%@
Vendor Version String File
BigEndian
cmap
'%c%c%c%c'
PreflightContext
start ex
supplementalassets
Unknown Accessory
uarp_querier
Host Reconnect After Apply
UARP Restore: Failed to tx uarp message to uarp silicon updater;status <0x%08x>, %s
Candidate retimer firmware version: %@
acib
Power Adapter
\tSubfiles:\n
Failed to generate updated super binary for %@
Compose Measured Payloads (Non-FTAB)
Unsuccessful
%s%u
fAssetStore
com.apple.corespeech.voicetriggerassetchange
FusingOverrideUnfused
Personalities
\tBoot Nonce: 
Asset Transfer Complete
\n
Demote
OTA Preflight
UARP.RESTORE.LAYER3.INFO.RESPONSE <Last Error> - Not Implemented
UID_MODE
usbc-fw-personality
\tActive File: %u\n
HeySiri Model Locale
Log Apple Model Number
-[AppleTypeCRetimerUpdaterInstance initWithRouterID:delegate:forcePower:]
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (prior to IOCreatePlugInInterfaceForService)
Invalid
%s: IIC hardware ID query failed for %@.
-[HPMForceRetimerDFUModeSetter getACIOParentData]
-[AppleTypeCRetimerDFU dfuBoot]
FieldName
%s: ERROR adding remote endpoint, status = 0x%08x
UarpRestoreInfoQueriesQueueHandler
Required Personalization Option
response timeout
IsSimulator
...Unable to create Device Interface. err = 0x%X
Payload Index %u
Unable to locate ACE for router ID %u
/var/db/accessoryupdater/dropbox
MetaData Type Not Found
retimerDFU
DFU manifest
char3
\tCategory: %s\n
BundlePath
disabled
%s.%u.payload
Flash Partition Bitmap
FTAB:\n
Endpoint Component Discovery Response
UARP Restore: %s: Protocol Version Not Selected; defer info queries
RestoreSystemPartition
AutoAppliesStagedFirmware
SupportsInternalSettings
Asset No Bytes Remaining
Boolean AppleTypeCRetimerUpdaterExecCommand(AppleTypeCRetimerUpdaterRef _Nonnull, CFStringRef _Nonnull, CFDictionaryRef _Nullable, CFDictionaryRef * _Nullable, CFErrorRef * _Nullable)
AppleModelNumber
SFWi was not run
BoardId
Warning: Unable to locate manifest for '%@'
NeRD Stage1
not implemented
Asset Processing Notification Ack
True
%s: Error writing to register %s(%x)
Ticket
Personalization Life
Personalization SoC Live Nonce
Payload Long Name
SOP Prime
\tVendor ID: 0x%04x\n
Same Version Staged
Downstream Endpoint Discovery
UARP Restore: Could not open personalized firmware file %s
las_tunableh_module_evaluate
disable
ATCRT_REG_PANIC_STATUS
Timing out waiting for ACEs. Last available: %@
UARP Restore: %s: Firmware Asset fully transfered
UTF8String
platform
I/O Error
Failed to parse super binary.
UARP Restore (Asset Solicitation): %s: remove failed
UARP.LAYER3.TRANSFER.RESUME - Not Implemented
Personalization Payload Trusted
\t%s: %s\n
Asset Data Transfer Notification
isalnum(c)
%@: Continuing after UARP staging has completed.
%s: DFU failed for %@
Payload Compression Algorithm
Payload Digest
logs
Invalid Data Request Type
\tMode: %s\n
Failure code: 0x%08X
USB-C_FW
\tChip ID: 0x%08x\n
\tSecurity Mode: %u\n
-[HPMForceRetimerDFUModeSetter getARMIODeviceRegistryEntryForACIOParentProperty:]
OTA Stage 2
MobileAssetsModelNumber
/AppleInternal/usr/local/misc
UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestData failed with status: %u
UARP.LAYER3.TRANSFER.PAUSE.ACK - Not Implemented
Payload Missing
cmapdatabase
Invalid Asset Type
RID
Did NOT build matching dict
\tStatus: %s\n
-[AppleTypeCRetimerDFU dfuWithFTAB:forcePersonalize:]
Options
\tChip Rev: %u
Compose MetaData Hash Algorithm
I2C
false
%@: UARP hardware ID check succeeded.
Failed to add RRKO data to FTAB
Limited
off
MetaData Hash
No Compressed Headers
accessory_type
core
open
SuperBinary Format Version
Version Discovery Response
UarpRestoreLayer3ApplePropertyUpdateQueueHandler
dev
ProductionStatus
Update failed for router ID %u
No Version Agreement
-[AppleTypeCRetimerUpdaterInstance queryHardwareID]
IOGeneralInterest
%@: Firmware staging complete.
Transport
MagSafe Cable
No MetaData
com.apple.%@.uarp.hw_id
lpda
/usr/standalone/firmware/accessoryupdater/UARP
Unknown Information Option
Failed to create updater instance for router ID %@
UARP Restore: %s: Accepted dynamic asset
host_debug_assert
Router ID %u does not require DFU mode
SoftwareBinaryDsp2
Flash Partition Boot
Unable to query chip Bver for %@
\tSecurity Epoch: %u\n
application-info
buildVersion
%s: IIC hardware ID query failed for %@ (%@).
TSS Request Options for payload %@
r
error
Unknown Message Type
Apply Staged Assets Response
-[ACE executeIECSCommand:withData:dataLength:]
UarpRestoreLayer3FirmwareApplyStatusQueueHandler
input
ap
-[AppleTypeCRetimerIICFifo pollForReceiveData]
%@%d
<%@: %@>
Tethered
USB-PD
\t\t%@
IOThunderboltController
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0
Personalization Chip Epoch
Personalization Nonce Hash
Minimum Battery Level
AirPodsPublicSeed
Asset Processing Notification
Downstream Endpoint Unreachable Ack
RRKO
\tPending Version: %@\n
Verbose
UARP Restore: %s: pAsset->_pAsset is NULL
ManifestEpoch
Asset In Flight
\x81
MetaData Values
UARP Restore: Failed to accept superbinary; 0x%08x
decoderId
Unknown Personalization Option
CoreUARP Restore IM4M: uarpPlatformEndpointOfferAsset: %d 
Property List Payload
fPayloadData
-[AppleTypeCRetimerDFU dfuValidate]
Trusted
ATCRT Response: %@\n\tResult: %s (%u)\n
Invalid Message Length
com.apple.uarp.internal.personalization
UARP Restore (Asset Solicitation): %s: pAsset is NULL
UARP Restore: %s: fLayer3RescindStatus is NULL
-[FTABFile initWithContentsOfURL:]
\xf0!
host_release_assert
Asset Corrupt
GR2
UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Info - %d )
UARP Restore: Failed to open file %s
Invalid Payload
ApProductionMode
TagNumber
Verifying retimer(s) booted version.
HigherVersion
Processing Error
Entering into DFU mode for Router ID %u
Uncompressed Payload Length
DPRO
\tBlock Count: %u\n
\tSerial Number: %@\n
%@
-[AppleTypeCRetimerUARPUpdaterInstance queryHardwareID]
Personalization Manifest Suffix
Unable to locate super binary.
Flash Write Error
UARP Restore: Mismatch in writing to manifest file %s.Expected to write %d bytes, actually wrote %d bytes
Personalization Chip ID
UARP Restore: %s: fLayer3AssetSolicitationProgress is NULL
AirPods FWUP iAUP server session
downstream
!
Personalizing %@
com.apple.%@.uarp
CoreUARPRestoreAssetTransferStatus
protocolaccessory
Unable to create IIC updater for %@
uatcrt
Unable to locate ACE for %@
IIC
\tChip ID: 0x%04x\n
-[AppleTypeCRetimerUARPUpdaterInstance startAppModeUpdateForSuperBinaryData:]
-[AppleTypeCRetimerIIC sendCommand:]
AirPodsDeveloperSeed
Unsupported Message Type
Host Controller
las_tunableh_apply
updater_instance
generateMeasurements
midpacket
Log Friendly Name
USB-C to Lightning
SOP Double Prime
Base64EncodedString
Incompatible HW
-[AppleTypeCRetimerIICFifo updateTransmitFifoSpace]
SupportsLogs
Invalid Data Response
Downstream Endpoint Reachable Ack
sbd2
SuperBinary MetaData
fPayloadMetaDataComplete
Payload Certificate
BuildManifest.plist
No Firmware Update Available Ack
FW open file failed
b2pEngine
UarpRestoreLayer3FirmwareStageStatusQueueHandler
las_tunableh_device_flavor_from_name
-[AppleTypeCRetimerDFU queryManifestForFTAB:]
v16@?0@\"B2PTimer\"8
Trigger Battery Level
Personalization More Requests to Follow
Version File
UUID
Unknown Asset
update
NO
-[HPMForceRetimerDFUModeSetter lookupThunderboltController]
retimer_force_dfu
UARP Restore (Asset Solicitation): %s: No Payload Metadata
Personalization Payload Effective Security Mode
False
Failed to force power for router ID %u (0x%08x)
Unable to locate bver in FTAB.
ChipID
DestBundlePath
-[AppleTypeCRetimerUARPUpdaterInstance printVersions]
UARP Restore (Asset Solicitation): %s: No Asset Metadata
Compose Measured Payloads
USBCLightningDisconnect
Data Response
acio-parent
%@: Update: %u%%
UARP Restore (Asset Solicitation): %s: %u bytes written
UARP Restore: %s: fLayer3FirmwareStageProgress is NULL
LeapBinsDigestsArray
ReofferFirmwareOnSync
Mismatch Personalization Option
Upload Complete
\tAP Chip Rev: %u
-[ThunderboltInterface configWriteForRoute:port:space:index:value:]
,%@
ResponseTags
No
Personalization FTAB Payload Tag
Voice Assist Digest
Corrupt SuperBinary
Enter DFU request failed for router ID %u (0x%08x)
UARP Restore: %s: Rx pRestoreAsset was NULL
<%@: %s (%u ms)>
USB
Bad Source File
Timer%u,Ticket
Failed to force power on for %@ during Updater instance initialization
%@: Waiting for UARP stage to complete...
Personalization FTAB Payload Production Mode
Manifest
Invalid Length
\tID: %s\n
com.apple.uarp.layer3.restore
ATCRT_REG_FIFO_STATUS
UARP Restore: UARP RX: Asset Processing Notification; Asset ID %u
driver 00
Payload Signature (Development)
com.apple.MobileAsset.UARP
\tValid: %u\n
Buffer Would Overflow
-[AppleTypeCRetimerIICDeviceHandle readRegister:buffer:length:]
UARP Restore (Asset Solicitation): %s: pEndpoint is NULL
UARP Restore: Failed to offer superbinary
DFUMode
%s (%s)
q24@?0@8@16
UpdateRequiresPowerAssertion
LittleEndian
Priority Activity
No AC Power
btlePersonalizationNeeded
Provisioning
|
AAPL,phandle
        <%@>\r
host
Downstream Endpoint Message
UpdaterRef
fAssetMetaDataComplete
PhyBlueTooth
power
Ignore Version
firmware
crsh
DecodedCrashLogKey
panicState=%@ assertID=%u
Personalization ECID Data
uarpPlatformEndpointStreamingRecvBytes() failed; 0x%08x
SHA-256
Asset Rescinded Notification Ack
UarpRestoreLayer3AssetSolicitationStatusQueueHandler
\tBoard ID: 0x%04x\n
Exceeded Packet Retry
Updater instance forcing power on for %@
uuid
-[ACE retimerEnterDFULegacy]
ACE Info:\n
ACE2
Unrecognized error 0x%x
com.apple.uarppersonalization.btleserver
Personalization Payload Digest
-[AppleTypeCRetimerUpdaterInstance printVersions]
\tDevice ID: 0x%04x\n
Unable to convert '%@' retimer debug flags string to a 64 bit number
deploymentLimit
UARP Restore: Could not open manifest file %s
las_tunableh_device_get_chip_number
Host Personalization not required for payload %@
Warning: Unable to locate manifest: %@
UARP Restore: UARP RX: Buffer = %p, Payload Length = %u, Type = 0x%04x, Total Length = %u, ID = %u
sysdiagnose
<unknown>
\tBoard ID: 0x%016llx\n
MetaData Hash Algorithm
com.apple.system.powersources.percent
ProductID
Endpoint Component Discovery Request
\t\tSecurity Mode: %u\n
Created updater instance for router ID %@
```
