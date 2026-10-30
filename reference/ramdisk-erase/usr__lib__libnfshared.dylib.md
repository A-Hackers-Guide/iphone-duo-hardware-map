# `/usr/lib/libnfshared.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 469,312 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 4504)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/usr/lib/libnfshared.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (41 classes, 10 protocols)

Classes: `NFAccessoryTag`, `NFAccessoryTagI2CBridge`, `NFAssertionCALogger`, `NFAssertionInternal`, `NFAssertionInternalWrapper`, `NFCALogger`, `NFCTKPollConfig`, `NFCardSessionConfig`, `NFCommandAPDU`, `NFCoreNFCPollConfig`, `NFExceptionsCALogger`, `NFGeneralStatisticsCALogger`, `NFHashes`, `NFLPCDStatisticsCALogger`, `NFLocation`, `NFMSEIParser`, `NFNSCheckedDecoder`, `NFNdefMessageInternal`, `NFNdefRecordInternal`, `NFPaymentTagReaderDeveloperPresentmentReport`, `NFPaymentTagReaderDeveloperPresentmentSessionData`, `NFPowerAssertion`, `NFPowerObserver`, `NFPreferenceObserver`, `NFReaderModeCardIngestionCALogger`, `NFReaderSessionConfig`, `NFReaderSessionPollConfig`, `NFResponseAPDU`, `NFRunScriptParametersInternal`, `NFServiceWhitelistChecker`, `NFTLV`, `NFTagInternal`, `NFTimer`, `NFVASPassConfig`, `NFXPCConnectionUserInfoDictionary`, `NFXPCEventPublisher`, `NFXPCServiceClient`, `NSData`, `NSDictionary`, `NSString`, `NSXPCConnection`

Protocols: `NFNdefMessage`, `NFNdefRecord`, `NFTag`, `NFTagA`, `NFTagB`, `NFTagF`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

## Strings (2,130)

```
%{public}s:%i Unexpected protected firmware version %s, expected %s
%{public}s:%i Invalid payload encoding; dropping message
transceiveToI2c_select
[Hex dump: offset=%04X] %{public,stockholm:dataDump}.*P
%{public}s:%i Memory allocation request failed.
%{public}s:%i InvalidationHandler: ConnectionID=%lu
%{public}s:%i %{public}@ not in allow list
%{public}s:%i Error : Hash is not of expected type
%{public}s:%i Invalid reference format
%{public}s:%i %{public}@ does not hold assertion
transceiveToI2c_write
%{public}s:%i Invalid AID entry: %{public}@
%{public}s:%i More than one TLV detected
%{public}s:%i Invalid payload character; dropping message
error
%{public}s:%i Unexpected customer application version %s, expected %s
%{public}s:%i ConnectionID does not match active (%lu), may have already been cleared
%{public}s:%i InterruptedHandler: ConnectionID=%lu
%{public}s:%i XPC event publisher for stream %@ received initial barrier
%{public}s:%i [Tag 0x12] Unexpected data length: 0x%X
%{public}s:%i Failed to get entitlements: %{public}@
%{public}s:%i Cannot create SecTaskRef with XPC Connection: %{public}@
%{public}s:%i Identifier string exceeds the maximum length, %{public}@
%{public}s:%i Unable to create event dictionary; dropping event
%{public}s:%i Underflow
systemReady=%{public,signpost.description:attribute}d
%{public}s:%i released assertion: counter: %lu id: %{public}@
XPC service client interrupted
%{public}s:%i Invalidating XPC connection
transceiveToI2c_pollForWriteComplete
%{public}s:%i System never went to sleep ! Ignoring will not sleep message.
%{public}s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@
%{public}s:%i Identifier string does not meet the minimum required length, %{public}@
%{public}s:%i Unable to find protected lifecycle hash : %s
%{public}s:%i Invalid language code length; dropping message
%{public}s:%i Unexpected version %s, expected %s
%{public}s:%i Validated %lu hashes
%{public}s:%i Underflow: tag=0x%x
%{public}s:%i Clearing XPC Connection
Critical error : this device should have NFC !!! cache = %d, MG = %d, EDT = %d
%{public}s:%i Radio %s.
%{public}s:%i Value too large: %{public}@
%{public}s:%i Tag value overflows
%{public}s:%i Failed to register for PM notifications
%{public}s:%i %s doesn't exist
%{public}s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@
transceiveToI2c_read
%{public}s:%i Unregistering Power notifications
%{public}s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring
%{public}s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu
system will sleep
XPC service client invalidated
%{public}s:%i Unable to find scratch lifecycle hash : %s
%{public}s:%i Unable to find protected firmware hash : %s
%{public}s:%i Could not create the Publisher!!!
%{public}s:%i Disabled
%{public}s:%i No TLV detected
beforeWrite=%{public,signpost.description:attribute}d
isLastPage=%{public,signpost.description:attribute}d
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
system will not sleep
%{public}s:%i Invalid extended response length : %{public}@
%{public}s:%i Have not received initial barrier; not sending %@
%{public}s:%i [Tag 0x%X] Unexpected data length: 0x%X
%{public}s:%i Unrecognized tag: 0x%X
%{public}s:%i all assertions: %{public}@
%{public}s:%i \"%s\" errno=%d Failed to open %s
%{public}s:%i String is of invalid length=%ld with 0x prefix
%{public}s:%i Error fetching teamID: %{public}@
%{public}s:%i Missing hash !
%{public}s:%i Unable to find customer application hash : %s
%{public}s:%i Unexpected %u len on tag 0
%{public}@ does not hold assertion
%{public}s:%i Underflow: tag=0x%x len=%u
%{public}s:%i String is of invalid length=%ld
%{public}s:%i Failed to connect to NFCD
%{public}s:%i prefixBytes is of invalid length=%ld
%{public}s:%i Invalid payload length; dropping message
%{public}s:%i Incorrect length field
%{public}s:%i System already sent a will sleep message ! Ignoring will sleep.
%{public}s:%i Unable to find scratch firmware hash : %s
%{public}s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s
%{public}s:%i Invalid character found, skipping
%{public}s:%i System not ready.  Abort
%{public}s:%i %s: %s
%{public}s:%i Resume connectionID=%lu
%{public}s:%i XPC event publisher for stream %@ with action = %d
%{public}s:%i Restricted mode for eSE is NOT set!
transceiveToI2c_write1SRAMPage
%{public}s:%i Dispatch queue has been destroyed !
%{public}s:%i Unable to find info hash : %s
%{public}s:%i Unexpected application version %s, expected %s
%{public}s:%i Unexpected error from XPC event publisher for stream %{public}@: %s
%{public}s:%i Minimum length requirement not met
%{public}s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple
timeout=%{public,signpost.description:attribute}d
%{public}s:%i Unable to find application hash : %s
ReadConfigError
systemNotReady
Error 0x%02X : %{public}s
system will power on
%{public}s:%i NULL error: tag=0x%x len=%u
%{public}s:%i 0 record type length; unable to decode
%{public}s:%i Unsupported length 0x%X
%{public}s:%i Expected length is too large.
%{public}s:%i Failed to get power assertion - system already going to sleep
%{public}s:%i opened assertion: counter: %lu id: %{public}@
%{public}s:%i System never went to sleep ! Ignoring will power on message.
%{public}s:%i \"%s\" errno=%d Failed to read data %ld/%ld
%{public}s:%i \"%s\" errno=%d Failed to realloc to %zu bytes
%{public}s:%i Source is not hex encoded bytes
%{public}s:%i [Tag 0x11] Unexpected data length: 0x%X
transceiveToI2c_read1SRAMPage
%{public}s:%i Failed with 0x%x
%{public}s:%i Unexpected length did you mean to use extended length ?
%{public}s:%i Require definite encoding, but got zero tag and len
%{public}s:%i Failed to query build
transceiveToI2c_pollForSystemReady
%{public}s %{public,stockholm:NCI}.*P
%{public}s:%i Invalid URI; dropping message
%{public}s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@
%{public}s:%i [NFTLV TLVWithTag:children:] failed!
%{public}s:%i Returned %x
%{public}s:%i Failed to alloc %ld
%{public}s:%i %{public}@ Expected %{public}@, got %{public}@
%{public}s:%i Failed find IOKit service
totalLen=%{public,signpost.description:attribute}lu
%{public}s:%i Connection ID doesn't match (%lu vs %lu), may have already refreshed. Ignoring
NFXPCConnectionUserInfoDictionary
NFReaderModeCardIngestionCALogger
NFCALogger
NSCopying
NFAccessoryTag
NFUserInfo
NFPreferenceObserver
NFServiceWhitelistChecker
NFXPCEventPublisher
HexString
NFPowerObserver
NFResponseAPDU
NFTagInternal
NFLocation
NFPaymentTagReaderDeveloperPresentmentSessionData
NFNdefMessage
NSObject
NFAssertionInternalWrapper
NFMSEIParser
NFAssertionCALogger
NFPaymentTagReaderDeveloperPresentmentReport
NFHashes
NFVASPassConfig
NFCommandAPDU
NFReaderSessionConfig
NFNSCheckedDecoder
NFTLV
NFPowerAssertion
NFCTKPollConfig
NFRunScriptParametersInternal
NFNdefRecord
NFAssertionInternal
Comparison
NFGeneralStatisticsCALogger
NFTag
NFXPCServiceClient
NFLPCDStatisticsCALogger
NFCoreNFCPollConfig
NSCoding
NFAccessoryTagI2CBridge
NFTimer
NFCardSessionConfig
NFReaderSessionPollConfig
NFTagA
NFWhitelistChecker
NFExceptionsCALogger
NSSecureCoding
NFNdefMessageInternal
NFNdefRecordInternal
NTAG5Boost
NFTagB
Numeric
NFExtension
NFTagF
valueAsUnsignedLongLong
assertionTime
encodeDouble:forKey:
sessionID
TQ,R,N,V_sessionType
_nfcCardSessionAccess
_serviceName
_typeFSystemCode
teamID
type
_applicationIdentifier
stringForKey:
messageEnd
hasSuffix:
postAnalyticsGeneralTransactionStatistics
T@\"NSData\",R,N,V_data
_class
trustedISO7816AidList
NF_arrayForKey:
clss
isDevTestMode
setInitialSelectBeforeRun:
validateISO15693TagAccessWithManufacturerCode:serialNumber:
_country
_hceAccess
buildAPDUHeaderWithClass:instruction:p1:p2:len:useExtendedLength:
setMessageEnd:
supportsPACE
tagA
initWithLength:
setSkipMifareClassify:
setObject:forKeyedSubscript:
TB,N,V_skipMifareClassify
_initISO15693TagSpecifier:
_queryTypeFSystemCodes
_stringValueOfEntitlement:secTask:
sfgi
simpleTLVsWithTag:fromData:
T@\"NSArray\",R,N
NF_dataWithHexString:
_historicalBytes
_includeAPDUDuration
date
nfcISO15693ReaderAccess
TLVWithTag:unsignedShort:
bundleIdentifier
compare:options:range:
componentsSeparatedByString:
initWithNFTagForUIDOnly:
processName
_allowBackgroundedSession
initWithUTF8String:
performSelector:withObject:
applicationData
_eCommerceAccess
cardModeAccess
hceAccess
initWithStartTimestamp:endTimestamp:latitude:longitude:altitude:horizontalAccuracy:city:state:country:successfulTapCount:
unsignedLongValue
_tokens
TB,R,N,V_nfcHardwareRegistersAccess
appendString:
T#,R
T@\"NSString\",R,C,N
Td,R,N
URLByDeletingLastPathComponent
_boolValueOfEntitlement:secTask:
_customDescription
characterSetWithCharactersInString:
p1
sessionConfig
TI,N,V_technology
_decodeTextRecordText:
_setNDEFContainerSize:
hash
initialUIText
isEqualToDate:
timeIntervalSince1970
_getSystemCodeListString
localDeviceCAParameters
parseResponseAPDU:
initialScanText
_lpemConfigSessionAccess
getMiddlewareExceptionCount
objectsForKeys:notFoundMarker:
T@\"NSString\",&,N,V_applicationIdentifier
encodeInt64:forKey:
objectAtIndexedSubscript:
dealloc
UUIDString
_idm
appendFormat:
TB,R,N,V_ignoreAppStateMonitor
T@\"<NFAccessoryTagDelegate>\",W,N,V_delegate
AppData
processIdentifier
numberWithBool:
performSelector:
pupi
resetCALoadStackExceptionCount
_pollingOption
_sfgi
asMutableData
_radioToggle
handlePreferencesOrProfileChanged
setChunked:
T@\"NSData\",&,N,V_ecp
_lpcd
eCommerceAccess
_isAIDStringValid:
decodeDoubleForKey:
T@\"NSString\",R,V_country
_xpcConnection
numberWithUnsignedShort:
seid
isEqualToArray:
TB,R,N,V_internalAccess
_arrayValueOfEntitlement:secTask:
_ecp
addDeviceModeDimensionsToDictionary:
setCheckAIDAllowList:
setStreamName:
unsignedLongLongValue
NF_numberForKey:
initWithFormat:
TB,N,V_toSystemOS
_worseCaseSizeAsData
objectForKeyedSubscript:
selectedAID
sessionTypeForClass:
_remoteObjectInterface
_vasMode
unsignedIntValue
NF_isPrefixOfHexEncodedEqualToBytes:length:
_setAtqa:
clientName
_initialScanText
allowSleep
pollConfigWithTypeFSystemCode:
tokens
vasPasses
NF_fdPresentmentIntentSuppressionHolder
_iso7816SelectIdentifiers
_sak
holdPowerAssertion:behaviourWhenSleepStarted:
TB,N,V_initialSelectBeforeRun
scanHexInt:
_silentType
dictionaryWithObjects:forKeys:count:
initWithBytes:length:encoding:
initWithData:encoding:
internalAccess
T@\"NSString\",R,C,N,V_initialScanText
UID
NF_whitelistChecker
Td,R,V_longitude
pollConfigWithTechnology:
_copyValueOfEntitlement:secTask:
parseRecordUsingScanner:header:type:identifier:payload:
_setSupportsPACE:
dataWithBytes:length:
getAppInfoDictionary
T@\"NSMutableSet\",&,N,V_tokens
T@\"NSString\",R,&,N,V_readerPurposeString
TB,R,V_willSleep
_writeToBridgeType0:fragmentationSupport:
lastObject
sessionType
setShortRecord:
TB,R,N,V_bgTagReadingAssertion
TB,R,N,V_surfSessionAccess
_setNDEFMessageSize:
encodeInt32:forKey:
initWithDelegate:
header
setQueue:
isSelectCommand
_setIdLengthPresent:
validateISO15693TagAcesssWithUID:
decodeIntForKey:
externalReaderAccessAllow
latitude
seshatAccess
T@\"NSData\",R,N
disableCompletionNotification
handleEventWithAction:token:descriptor:
NF_clientName
TB,N,V_pace
_nfcTagReaderPACEPollingAllow
conformsToProtocol:
encodeInt:forKey:
_type0WriteSRAM:data:
dumpState
powerObserverSystemWillSleep:
setAIDAllowList:
setAppletIdentifiers:
toSystemOS
TB,R,N,V_purpleTrustAccess
_internalAccess
releasePowerAssertion:
TB,R,N,V_remoteAdminAccess
T@\"NSOrderedSet\",R,&,N
initWithStreamName:queue:
setIso7816SelectIdentifiers:
startTimer:
valueAsHexString
_setupInitValuesForDeviceExceptionStatistic
nfcVASReaderAccess
setTagUUID:
_bridgeType0CreateAccessoryHeaderWithBuffer:pageLength:isLastPage:
_reportId
initWithArray:
subdataWithRange:
_startTimestamp
bgTagReadingAssertion
isEqual:
valueAsUnsignedLong
sak
TB,R,N,V_lpmFactoryTest
_bundleID
_singleUserAccess
applicationIdentifier
initWithService:remoteObjectInterface:exportedInterface:exportedObject:xpcDispatchQueue:
postAnalyticsVASTransactionException:withSWStatus:
seLoggingSessionAccess
allowBackgroundedSession
initWithService:remoteObjectInterface:exportedInterface:exportedObject:
numberWithUnsignedInt:
setReleaseTimer:
setExportedInterface:
tagF
timestampDay
TQ,R,V_successfulTapCount
Td,R,N,V_longitude
restrictedMode
T@\"NSNumber\",&,N,V_typeFSystemCode
TLVsWithData:requireDefiniteEncoding:
decode
postAnalyticsHardwareFault:errorStatus:parityErrorCount:
setDeactivateAllApps:
TB,R
TB,R,N
_miniNVWriteAccess
_payloadRange
bytes
initWithData:uniformLengthCheck:
lpemConfigSessionAccess
payloadBytes
_selectTagType0
T@\"NSString\",R,C,N,V_passIdentifier
_setSystemCodes:
decodeFromRecord:
transceive:response:maxTimeout:
isURIRecord
publisher
purpleTrustAccess
setToSystemOS:
skipMifareClassify
SystemCode
T@\"NSString\",&,N,V_initialUIText
TB,N,V_disableCompletionNotification
TB,N,V_enableDebug
bucketDeviceAngle:
initWithConnection:
T@\"NSString\",R,V_city
substringWithRange:
_bridgeType0WriteOneSRAMPage:fragmentationSupport:isLastPage:
_checkAIDAllowList
NF_clearPresentmentIntentSuppressionHolder
NF_dataForKey:
applicationDataCoding
class
postAnalyticsHciTransactionException:eventType:commandResult:status:
setFelicaSystemCodes:
tagID
userInfo
_clientName
pollConfigWithAppletIdentifiers:
NF_asHexString
_assertionTime
_status
TQ,R
roundToSignificantDigit:forValue:
setInitialUIText:
_decodeTextRecord:
dontResetAssertion
receivedInitialBarrier
setInterruptionHandler:
numberWithDouble:
postAnalyticsAppletProvisioningFailureEvent:responseCode:
T@\"NSObject<OS_xpc_event_publisher>\",&,N,V_publisher
coder:decodeArrayOfClass:forKey:
objectAtIndex:
uiMode
_assertionHolders
childWithTag:
uppercaseString
_bridgeType0ReadMultipleSRAMPagesWithBuffer:
messageBegin
setDelegate:
T@\"<NFTagB>\",R,N
postPlasticCardEnableStatus:aid:
valueAsString
asDictionary
copyWithZone:
ndefMessageSize
_clientProcessIdentifier
initWithNDEFMessage:
localizedCaseInsensitiveContainsString:
postAnalyticsDefaultAppSupression:prepOnly:
initWithType:
setTypeFSystemCode:
sharedCALogger
T@\"NSString\",&,N,V_streamName
_passIdentifier
T@\"<NFTagA>\",R,N
TB,R,N,V_delayConnectionHandoverRestart
_initCardSessionEntitlementsWithSecTask:
T@\"NSString\",R,N,V_clientName
_purpleTrustAccess
hasPrefix:
setSeid:
TB,R,N,V_useUnfilteredApplets
encodeInteger:forKey:
streamName
postCAEventFor:eventInput:
setInvalidationHandler:
_surfSessionAccess
_tag
appendExpectedLength:usingExtendedLength:toAPDU:
postAnalyticsContactlessErrorsEvent:status:error:
_deviceAngleDegrees
ndefContainerSize
queryTypeFSystemCodes
addObjectsFromArray:
AIDAllowList
_assertionType
includeAPDUDuration
getBytes:range:
_releaseTimer
_serviceWhitelist
_sessionConfig
_type
enumerateObjectsUsingBlock:
isMemberOfClass:
sendXpcNotificationEventWithString:
NF_serviceType
initWithLatitude:longitude:altitude:horizontalAccuracy:city:state:country:
retainCount
transactionCounter
TC,N
_seSessionAccess
seCredentialManagerAccess
sendXpcNotificationEventWithDictionary:
setHeader:
assertionType
description
dictionary
queue
setPendingSendEvents:
_setSystemCode:
_p1
_intToData:
dataFromNDEFMessage:
stringByTrimmingCharactersInSet:
pollIDCardConfigWithTechnology:
_dataLock
_setQueue:
removeLastObject
scanCharactersFromSet:intoString:
TS,R,N,V_status
_appData
_longitude
_teamIdentifier
TB,N,V_queryTypeFSystemCodes
updateDailyTagStatistic:
_seid
passConfigWithMode:passIdentifier:
copy
isEqualToString:
_children
_trustedISO7816AidList
altitude
decodeInt32ForKey:
getDurationFrom:
holdPowerAssertion:onBehalfOf:behaviourWhenSleepStarted:
isGetVasDataCommand
response
Ti,R,V_pid
generateDailyUUIDForCA
identifier
postSessionMetricsEvent:sessionDurationMs:queueWaitMs:blockedBySessionType:hasError:
validateNFCCHashes:reference:expectedVersion:
_streamName
decodeIntegerForKey:
initWithObjectsAndKeys:
postAnalyticsTSMConnectivityException:
T@\"NSMutableArray\",&,N,V_pendingSendEvents
T@\"NSString\",R,C
_initialUIText
setIsDevTestMode:
updateDeviceAngle:modeDefault:
TB,R,N,V_readerInternalAccess
_incrementMiddlewareExceptionCountWithReset:
_cardModeAccess
setValue:forKey:
lpcd
numberWithUnsignedLongLong:
pendingSendEvents
sendXpcNotificationEvent:
simpleTLVsWithData:
valueAsUnsignedShort
_powerNotificationNotifier
_workQueue
NF_callbackUUID
TLVWithTag:fromData:
_bucketizeOverCurrentCount:
enumerateKeysAndObjectsUsingBlock:
postAnalyticsReaderModeCardIngestionSession:prepOnly:
setPayload:
initWithAppletIdentifiers:
reportId
IDm
T@\"NFAssertionInternal\",&,N,V_assertion
tagUUID
_pollDuration
T@\"NSArray\",R,C,N
TQ,R,N,V_uiMode
Tr*,R,N
postAnalyticsReaderModeExceptionForType:tagType:rfFrameInterface:withErrorCode:
sessionTypeString:
TB,R,N,V_seLoggingSessionAccess
initWithCallback:queue:
isSecureMessaging
T@\"NSArray\",&,N,V_felicaSystemCodes
vasMode
_identifier
payloadLength
pollingProfileUpdate
setIncludeAPDUDuration:
setFieldDetect:
TB,N,V_deactivateAllApps
_idLengthPresent
_tagID
initWithConnection:coreNFCConnection:
NF_setFDPresentmentIntentSuppressionHolder
TLVSsWithBytes:length:requireDefiniteEncoding:
boolForKey:
nfcHardwareRegistersAccess
T@?,C,V_callback
children
setReceivedInitialBarrier:
setStartOnLocationUpdate:
PMm
country
T@\"NSString\",R,N,V_city
getCAUniversityCode:universityCodes:
postAnalyticsLPCDStatistic:
_transactionCounter
T@\"NSData\",R,C,N
_teamID
T@\"NSArray\",&,N,V_AIDAllowList
TQ,N,V_pollingOption
_initCoreNFCEntitlements:secTask:
postAnalyticsATLFailureEvent:aid:error:
releaseTimer
.cxx_destruct
TB,R,N,V_eCommerceAccess
_AIDAllowList
invalidateConnection
stringWithFormat:
whitespaceAndNewlineCharacterSet
TC,R,N
unregisterForEvents
TB,R,N,V_hceAccess
_atqa
unsignedIntegerValue
TB,R,N,V_singleUserAccess
_initTagSpecifier:maximumFilterStringLength:
getConnectionAndID:
readFromBridge:fragmentationSupport:response:
_firstOctet
_popTimeInSeconds
horizontalAccuracy
postAnalyticsExpressSetupFailureEvent:context:error:
T@\"NSString\",R,N
TB,R,N,V_seshatAccess
_createAccessDictionaryFromICCode:serialNumber:maximumFilterStringLength:
initWithNDEFRecord:
_lengthExpected
_bgTagReadingAssertion
_setSFGI:
successfulTapCount
supportsSecureCoding
_assertion
_monotonic
isKindOfClass:
length
T@\"NSString\",R,N,V_state
characterAtIndex:
pollDuration
postAnalyticsOsResetEvent:osID:hardwareType:
TI,R,N
_clientCount
characterIsMember:
useUnfilteredApplets
postDailyTagStatistics
historicalBytes
initWithString:
_successfulTapCount
isSendCertificateCommand
longitude
lpmFactoryTest
delegate
remoteAdminAccess
removeRestrictedMode
setPollingOption:
start:
typeFSystemCode
_timestampDay
state
addRecordArray:
TB,R,N,V_dontResetAssertion
_latitude
_records
_sessionType
removeObject:
substringToIndex:
_lpmFactoryTest
_p2
NF_setPresentmentIntentSuppressionHolder
TB,R,N,V_seSessionAccess
_isDevTestMode
initSleepTimerWithCallback:queue:
TI,N,V_pollDuration
_nfcCardSessionAIDPrefixList
postAnalyticsSERestrictedModeExited:exitReason:
removeObjectForKey:
resume
self
autorelease
coder:decodeArrayOfArrayOfClass:forKey:
deactivateAllApps
decodeObjectOfClass:forKey:
nfcNDEFReaderAccess
postDeviceExceptionStatisticsDim
startTimestamp
ecp
_setSak:
_decodeTextRecordLanguage:
_seshatAccess
getHardwareTypeForCA:
getUUIDBytes:
setWithObjects:
_bridgeType0WritePollForSystemReadyWithTimeout:beforeWrite:outError:
encodeObject:forKey:
initWithData:
postHardwareExceptionEventWithAssertionCounter:hardwareType:firmwareVersion:wdogDump:hwFltDump:wdgTickInfo:assertionData:
_setTechnology:
NF_hasPrefix:
city
pollConfigWithOption:sessionConfig:
_resetDailyTagStatisticToDefaults
_seCredentialManagerAccess
_technology
NF_clearFDPresentmentIntentSuppressionHolder
TB,N,V_selected
Td,R,V_horizontalAccuracy
UTF8String
ignoreAppStateMonitor
postAnalyticsSetupEndpoints:totalUnknowntoSE:
removeDelegate:
_bridgeType0WritePollForCompletionWithTimeout:
_readFromBridgeType0:fragmentationSupport:
miniNVWriteAccess
setRemoteObjectInterface:
TB,R,N,V_lpemConfigSessionAccess
initWithUUIDString:
postAnalyticsCRSAuthWithStatus:withMethod:
sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:startOnLocationUpdate:isDevTestMode:
TB,R,N,V_cardMigrationAccess
initWithDictionary:
T@\"NSArray\",R,C,N,V_vasPasses
TB,N,V_lpcd
_xpcQueue
atqa
responseWithData:
T@\"NSData\",&,N,V_tagUUID
_setupInitValuesForGeneralTransactionStatistics
decodeInt64ForKey:
_selected
_tagReaderAccess
_type0ReadConfigReg:data:
pace
scannerWithString:
addObject:
encodeBool:forKey:
NF_clearCallbackUUID
_type0ReadConfigRange:data:
addDelegate:
teamIdentifier
chunked
T@\"NSArray\",R,V_developmentPresentments
callback
ndefAvailability
childrenWithTag:
decodeBoolForKey:
didInvalidate:
readerPurposeString
T@\"NSString\",?,R,C
TQ,R,V_timestampDay
_toSystemOS
configWithInitialUIText:
selectTag
mutableBytes
TLVsWithData:
_setSelectedAID:
_state
boolValue
generateUUID
nfcCardSessionAIDPrefixList
recordsWithTNF:type:identifier:payload:chunkSize:outError:
respondsToSelector:
_setIdentifier:
Td,R,N,V_latitude
jsonDictionary
singleUserAccess
addEntriesFromDictionary:
arrayWithCapacity:
encodeWithCoder:
setApplicationIdentifier:
Td,R,N,V_horizontalAccuracy
_setAppData:
_src
debugDescription
status
_data
_horizontalAccuracy
_setIDm:
assertion
delayConnectionHandoverRestart
lengthExpected
recordsFromBytes:length:
integerValue
NF_urlForKey:
TLVWithTag:children:
_endTimestamp
releasePowerAssertion:logFaultOnOverRelease:
superclass
T@\"NSString\",R,V_bundleID
getCALoggerUserDefaults
initWithCapacity:
startTimer:leeway:
_cardMigrationAccess
setExportedObject:
_setNDEFAvailability:
timeIntervalSinceDate:
T@\"NSArray\",&,N,V_iso7816SelectIdentifiers
TQ,R,N
_supportsPACE
array
isSilent
standardUserDefaults
TQ,R,V_endTimestamp
_deviceModeDefault
selected
weakObjectsHashTable
tag
TB,N,V_startOnLocationUpdate
instruction
isEqualToNFTag:
TB,R,N,V_allowBackgroundedSession
_nfcHardwareRegistersAccess
asData
cardMigrationAccess
isGetMoreVasDataCommand
setTechnology:
records
member:
_startOnLocationUpdate
T@\"NSNumber\",R,N
_decodeURIRecord:
caseInsensitiveCompare:
data
stop
coder:decodeDictOfClass:forKey:
TLVWithData:
_iso15693ReaderAccess
_skipMifareClassify
objectForKey:
resetConnection
_powerAssertTransaction
TB,R,N,V_pollingProfileUpdate
setEcp:
_deactivateAllApps
Td,R,V_altitude
_appletIdentifiers
setTypeNameFormat:
T@\"NSString\",R,V_teamID
_dontResetAssertion
initialSelectBeforeRun
UUID
_nfcPaymentTagReaderDeveloperMode
postAnalyticsCRSAuthECommerceWithParameters:
T@\"NSString\",R,N,V_teamIdentifier
TB,R,N,V_cardModeAccess
_ndefAvailability
_powerNotificationPort
shortRecord
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
NF_userInfo
_ndefMessageSize
initWithBytes:length:
dataFromRecord:
TB,R,N,V_chAssertion
_receivedInitialBarrier
numberWithInteger:
setAssertion:
TB,N
_remoteAdminAccess
T@\"NSDate\",R,V_assertionTime
_initISO7816PermissibleAIDListWithSecTask:infoPlist:
bundleID
_parseTLVs:end:simple:definite:
_uiMode
TB,R,N,V_nfcPaymentTagReaderDeveloperMode
TB,R,N,V_seCredentialManagerAccess
_setType:
setObject:forKey:
_enableDebug
_useUnfilteredApplets
setType:
validateISO15693TagAccessWithManufacturerCode:
_validate
_setSilentType:
TLVWithTag:value:
addRecord:
powerObserverSystemHasPoweredOn:
TB,N,V_checkAIDAllowList
_payload
_readerPurposeString
appendData:
initWithCoder:
silentType
T@\"NSString\",R,N,V_country
_delegate
iso7816SelectIdentifiers
T@\"NFServiceWhitelistChecker\",R,N,V_serviceWhitelist
TQ,R,V_assertionType
_pmm
nfcTagReaderAccess
postAnalyticsSEFailureEvent:context:error:
TB,R,N,V_nfcTagReaderPACEPollingAllow
numberWithUnsignedChar:
TB,N,V_fieldDetect
TB,R,N,V_radioToggle
nfcCardSessionAccess
numberWithUnsignedInteger:
NF_toUint64:
postCASERestrictedModeExited:exitReason:
postMiddlewareExceptionEvent:mwVersion:errorType:errorCode:breadcrumb:description:
setString:
willSleep
_instruction
TLVWithTag:unsignedChar:
performSelector:withObject:withObject:
resetConnectionWithId:
isProxy
_stringFromISO15693AccessFilterList
postAnalyticsMobileSoftwareUpdateExceptionEvent:
remainingTime
setMessageBegin:
setSessionConfig:
stopTimer
setEnableDebug:
_powerNotificationMessage:argument:
_type0GetSystemInfo:
code
initWithNFTag:
NF_stringForKey:
TQ,N,V_sessionConfig
_fieldDetect
_iso15693TagAccessFilters
_pendingSendEvents
chAssertion
serviceWhitelist
seSessionAccess
_seLoggingSessionAccess
initWithServiceWhitelist:clientName:
invalidate
nfcTagReaderPACEPollingAllow
Ti,N,V_transactionCounter
_disableCompletionNotification
initWithDomain:code:userInfo:
initWithMachServiceName:options:
postAnalyticsCRSDeAuthWithStatus:
_vasReaderAccess
readerInternalAccess
_setHistoricalBytes:
setDisableCompletionNotification:
setIdentifier:
_queue
felicaSystemCodes
Td,R,N,V_altitude
_developmentPresentments
_powerNotificationConnection
isEqualToNumber:
setQueryTypeFSystemCodes:
_callback
_readerInternalAccess
_setPMm:
_type0WriteConfigReg:data:
setLpcd:
stringWithUTF8String:
T@\"NSArray\",&,N,V_appletIdentifiers
_willSleep
initWithObjects:
intValue
p2
sessionTimeLimit
setPollDuration:
getTimestamp
integerForKey:
nfcPaymentTagReaderDeveloperMode
validateNFCCHashes:reference:expectedVersion:hashResults:
_city
_pace
pollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:
_vasPasses
setCallback:
updateAnalyticsGeneralTransactionStatistics:
TQ,N,V_type
decodeFromNDEFMessage:
NF_dictionaryForKey:
T@\"NSOrderedSet\",R,N
pollingOption
setRestrictedMode:
sharedPowerAssertion
didInterrupt:connectionID:
T@\"NSData\",&,N
initWithHeader:type:identifier:payload:
startOnLocationUpdate
Tq,R,N,V_vasMode
_initialSelectBeforeRun
initWithReportId:timestampDay:bundleID:teamID:developmentPresentments:
numberWithInt:
allSystemCodes
init
updateGeneralDeviceStatistic:
updateDeviceExceptionStatistic:
allocWithZone:
assertionHolders
TB,N,V_receivedInitialBarrier
_pid
appendBytes:length:
_allSystemCodes
postAnalyticsSERestrictedModeEntered:
substringFromIndex:
getBatteryPercent
TB,R,N,V_miniNVWriteAccess
_felicaSystemCodes
decodeObjectOfClasses:forKey:
sfgt
NF_setCallbackUUID:
doubleValue
value
T@\"NSString\",&,N,V_seid
isEqualToData:
mutableCopy
_altitude
_resetGeneralDeviceStatisticToDefaults
_type0ReadSRAM:numOfBlocks:data:
initWithType:delegate:
isSelectByDFNameCommand
_sleepMessageArgument
countByEnumeratingWithState:objects:count:
decodeUnderlyingAppletError:
endTimestamp
removeAllObjects
_chAssertion
appletIdentifiers
setPace:
technology
_delayConnectionHandoverRestart
T@\"NFTimer\",&,N,V_releaseTimer
TB,N,V_isDevTestMode
_checkHash:againstReference:expectedVersion:matchingVersion:
_stringFromArray:
_uid
radioToggle
zone
_ignoreAppStateMonitor
_xpcConnectionID
postAnalyticsSERemovedEvent:hasExpressTransactionStarted:hasCardEmulationStarted:hardwareType:
setPublisher:
setTransactionCounter:
_delegates
_publisher
_tagUUID
_value
initWithSuiteName:
retain
setSelected:
release
_pollingProfileUpdate
postGeneralDeviceStatistics
Tq,R,N,V_type
_setUID:
enableDebug
setTokens:
writeToBridge:fragmentationSupport:response:
T@\"NSString\",R,V_state
_exportedInterface
developmentPresentments
registerForEvents
T@\"<NFTagF>\",R,N
pid
checkAIDAllowList
numberWithUnsignedLong:
NF_isZeroed
tagB
NF_presentmentIntentSuppressionHolder
count
fieldDetect
postAnalyticsCRSAuthInitEventWithStatus:
T@\"NSUUID\",R,V_reportId
modifyObjectForKey:handler:
surfSessionAccess
NF_objectForKey:expectedClass:
Td,R,V_latitude
TLVWithTag:unsignedLongValue:
TQ,R,V_startTimestamp
_ndefReaderAccess
fileURLWithPath:isDirectory:
passIdentifier
processInfo
now
payload
TB,N,V_includeAPDUDuration
auditToken
_exportedObject
_ndefContainerSize
typeNameFormat
v24@0:8@16
v48@0:8@16@24@32@40
@\"NSString\"16@0:8
q16@0:8
@28@0:8C16@20
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@\"NSObject<OS_dispatch_queue>\"
v24@0:8S16I20
@\"NSArray\"16@0:8
@32@0:8C16C20^@24
d
B32@0:8@16^{__SecTask=}24
@\"NSUUID\"
@32@0:8@16@24
@32@0:8:16@24
@\"NSDate\"
@\"<NFTagA>\"16@0:8
@72@0:8d16d24d32d40@48@56@64
v36@0:8I16Q20@28
@20@0:8I16
S16@0:8
@\"<NFTagF>\"16@0:8
v32@0:8@16@24
@\"NSMutableSet\"
@24@0:8@\"NSCoder\"16
@28@0:8r^v16I24
B36@0:8d16B24^@28
@\"NSXPCConnection\"
@96@0:8Q16Q24d32d40d48d56@64@72@80Q88
Q
v24@0:8I16I20
v20@0:8i16
@32@0:8S16B20@24
@32@0:8@16B24B28
d16@0:8
v28@0:8I16^v20
@\"<NFPowerObserverDelegate>\"
v20@0:8B16
@32@0:8r*16Q24
{_NSRange=\"location\"Q\"length\"Q}
@32@0:8@?16@24
S
AB
v24@0:8@\"<NFNdefRecord>\"16
@60@0:8Q16Q24@32@40B48B52B56
v32@0:8d16d24
@\"NSMutableOrderedSet\"
@24@0:8^Q16
@\"NSHashTable\"
v24@0:8@\"NSCoder\"16
@\"NSData\"16@0:8
v24@0:8@\"NSData\"16
@\"NSNumber\"
v32@0:8@16Q24
v60@0:8I16I20I24^I28^I36^I44@52
@60@0:8C16@20@28@36Q44^I52
r*16@0:8
I
^{IONotificationPort=}
v32@0:8@16^{__SecTask=}24
@\"NSXPCInterface\"
B20@0:8B16
@44@0:8C16@20@28@36
@\"NFAssertionInternal\"
@24@0:8I16I20
@24@0:8^@16
@?
I24@0:8Q16
@40@0:8C16C20C24C28I32B36
Q24@0:8^@16
v32@0:8@16@?24
I16@0:8
v20@0:8I16
B16@0:8
v28@0:8I16I20I24
@24@0:8@\"NSData\"16
@\"NSData\"
@\"<NFTagB>\"16@0:8
v32@0:8^{__SecTask=}16@24
@\"NSMutableArray\"
q24@0:8q16
B
@\"NSString\"
B24@0:8#16
@28@0:8@16B24
v24@0:8d16
I32@0:8Q16@24
@48@0:8@16@24@32@40
B24@0:8:16
@24@0:8@\"<NFNdefMessage>\"16
i
@\"NSObject<OS_dispatch_source>\"
Q24@0:8#16
v24@0:8@?16
v28@0:8q16B24
v32@0:8I16B20B24I28
v24@0:8@\"NSArray\"16
@\"NFTimer\"
@32@0:8q16@24
q
@24@0:8d16
Q32@0:8Q16Q24
v32@0:8@16^I24
v32@0:8I16I20B24I28
@24@0:8^{_NSZone=}16
@24@0:8I16S20
@?16@0:8
v28@0:8B16@20
S24@0:8^@16
@
B48@0:8@16@24@32@40
B24@0:8@16
@40@0:8:16@24@32
i16@0:8
@36@0:8r^v16Q24B32
@28@0:8C16^@20
Q16@0:8
Ai
#16@0:8
I24@0:8@16
@24@0:8I16C20
@40@0:8{_NSRange=QQ}16^@32
B28@0:8@16I24
@32@0:8@16^{__SecTask=}24
@16@0:8
@24@0:8:16
v24@0:8Q16
v20@0:8C16
@24@0:8@\"<NFTag>\"16
B24@0:8@\"<NFTag>\"16
^v32@0:8@16^{__SecTask=}24
@56@0:8@16@24@32@40@48
v20@0:8S16
v28@0:8@16B24
@40@0:8@16@24Q32
@24@0:8@\"<NFNdefRecord>\"16
@36@0:8@16B24^@28
@40@0:8@16#24@32
v36@0:8@16Q24B32
v16@0:8
@24@0:8@16
@\"NSObject<OS_xpc_event_publisher>\"
v24@0:8S16S20
B32@0:8r*16Q24
C16@0:8
C
@28@0:8^@16B24
@48@0:8Q16Q24@32@40
v32@0:8S16S20@24
@\"NSMutableDictionary\"
@\"NFServiceWhitelistChecker\"
@\"NSArray\"
v36@0:8S16@20@28
B32@0:8@16i24I28
@32@0:8@16#24
v24@0:8^{__SecTask=}16
v24@0:8I16S20
Vv16@0:8
B24@0:8@\"Protocol\"16
B56@0:8^{_NFDataScanner=^{_NFData}Q^v}16*24^@32^@40^@48
@24@0:8Q16
@\"<NFAccessoryTagDelegate>\"
@28@0:8I16@20
^v
^{_NSZone=}16@0:8
@40@0:8r^*16r*24B32B36
v52@0:8Q16Q24Q32Q40B48
@56@0:8@16Q24@32@40@48
v48@0:8I16I20I24I28Q32@40
I20@0:8I16
@40@0:8@16@24@32
@32@0:8Q16Q24
@\"NSObject<OS_os_transaction>\"
totalCEEnabledWithMissingTransactionEndEvent
totalCoreNFCSessionBurnout
%s:%i Memory allocation request failed.
com.apple.UIKit.vends-view-services
nfc
Darwin
1
com.apple.nfcd.exceptions.hardwareExceptionEvent
com.apple.nfcd.exceptions.atlFailures
NSArray
PreventUserIdleSystemSleep
%s:%i %s: %s
Line
Method
BuildVersion
hasExpressTransactionStarted
com.apple.nfcd.exceptions.seRemovedEvent
readerModeTransceiveErrorCount
Presentment intent suppression
NFLogSetLogger
Invalid State
stockholm
HostProcessPc
I
%@ { MB=%d ME=%d CF=%d SR=%d IL=%d TNF=%d Type Length=%d Type=%@ ID=%@ Payload Length=%d Payload=%@ }
AssertName
com.apple.stockholm.powerobserver
totalExpressFelicaTransaction
dev
PM assertion release failure
supportsPACE
%s:%i ConnectionID does not match active (%lu), may have already been cleared
-[NFXPCServiceClient resetConnectionWithId:]
mwCount
context
com.apple.nfcd.exceptions.seFailures
06
urn:epc:pat:
_NFSecureElementReaderSession
com.apple.nfcd.generalTransactionStatistic
configuredTime
NFPlatformHasBootMeasurements
-[NFXPCEventPublisher sendXpcNotificationEvent:]_block_invoke
16
Untagged internal use
FDPresentmentIntentSuppressionHolder
NFCIP
NFCReaderUsageDescription
%s:%i Error fetching teamID: %{public}@
LR
nfccFWVersion
NFAssertionPID
%s:%i [Tag 0x%X] Unexpected data length: 0x%X
fd
inRestoreOS
r
com.apple.nfcd.session.trust
SwpProcessWaitObject
exitReason
news:
_NFCardMigrationPaymentSession
_NFPeerPaymentSession
CFBundleIdentifier
Legacy ISO15693 filter List=%@
latitude
-[NFCALogger removeRestrictedMode]
RfProcessWaitObject
https://www.
15
tcpobex://
T
com.apple.nfc.i2cbridge
com.apple.greentea
uuidUpdateDate
true
hardwareType
03
com.apple.nfcd.powerassertion
resetMode
kextCallDuration
com.apple.nfcd.mininv.write
_NFPlatformGetEdtNFCCModel
+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]
timestampDay
/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
%s:%i Unexpected version %s, expected %s
felicaSystemCodes
%s:%i Failed to query build
v28@?0I8Q12@\"NSObject<OS_xpc_object>\"20
+[NFCommandAPDU buildAPDUHeaderWithClass:instruction:p1:p2:len:useExtendedLength:]
Middleware
%s:%i System already sent a will sleep message ! Ignoring will sleep.
totalCHConnections
-[NFTLV valueAsUnsignedLongLong]
NFSharedDumpTransport
_NFCredentialSession
totalCHFieldNotification
totalDynamicPackages
radioIsEnabled
Generic 4B
AppData
hash3
RfProcessState
09
PACE=Y
%@-%@ { Tech=%@ Type=%@ ID=%@, NDEF=%d, capacity=%lu, messageSize=%lu }
com.apple.nfcd.session.credential.manager
CardSession: %@
AppleStockholmSPMI
R2
com.apple.nfcd.exceptions.vasTransactionExceptionEvent
U
%@ %02x = %@
+[NFTLV _parseTLVs:end:simple:definite:]
%s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu
category < NFLogCategoryMax
hash5
-[NFCoreNFCPollConfig initPollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:]
ftp://
_NFSecureTransactionServicesHandoverSession
totalPeerPaymentRequestFailure
serviceType
0123456789abcdefABCDEF*
-[NFServiceWhitelistChecker initWithConnection:coreNFCConnection:]
http://
ftps://
%s:%i Minimum length requirement not met
skipMifareClassify
noUUID
Prevent Connection Handover
uiMode
%s:%i [Tag 0x12] Unexpected data length: 0x%X
-[NFAccessoryTagI2CBridge(NTAG5Boost) _bridgeType0ReadMultipleSRAMPagesWithBuffer:]
lpcd
aids
com.apple.developer.nfc.readersession.iso7816.select-identifiers.trusted
validHash
%02x
+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]_block_invoke
_NFFieldDetectSession
totalReaderSession
checkAIDAllowList
05
com.apple.nfc.rf
NFTimer: popTimeInSeconds: %f
_NFInternalConfigurationSession
currentNFCDefault
totalDoubleClickLaunches
Generic 3B
IsSimulator
errorStatus
%s:%i Tag value overflows
selectedAID
-[NFServiceWhitelistChecker _initCoreNFCEntitlements:secTask:]
sessionStartTime
country
startTimestamp
%s:%i Unexpected error from XPC event publisher for stream %{public}@: %s
-[NFTLV valueAsUnsignedShort]
%s:%i Require definite encoding, but got zero tag and len
totalTransactionEndEvent
-[NSDictionary(NFExtension) NF_objectForKey:expectedClass:]
-[NFXPCServiceClient resetConnection]
falseDetectionCount
v8@?0
telnet://
%s:%i Disabled
exceptionData
description
02
urn:
ConfigType
totalSuccessfulVAS
hasError
com.apple.nfcd.lpm.factorytest
com.apple.stockholm
SwpProcessSp
com.apple.nfcd.exceptions.middlewareExceptionEvent
_NFLoyaltyAndPaymentSession
totalDynamicRFParametersUpdate
%s:%i Cannot create SecTaskRef with XPC Connection: %{public}@
com.apple.seld.tsmmanager
com.apple.nfcd.hce
KernelProcessPc
HostProcessWaitObject
17
%@%@
VAS
transactionUUID
totalMWExceptions
-[NFAccessoryTagI2CBridge(NTAG5Boost) _writeToBridgeType0:fragmentationSupport:]
totalFailureWithMissingTransactionEndEvent
tagType3ReadSuccessCount
city
teamID
developmentPresentments
iso7816SelectIdentifiers
R1
initialSelectBeforeRun
08
Unknown
!
%s:%i released assertion: counter: %lu id: %{public}@
totalLowTemperatureNotifCount
nfcDeviceModeDefault
id
0e
totalPeerPaymentRequest
chipID
Darwin Internal
com.apple.nfcd.exceptions.osResetEvent
04
_NFCardSession
_NFUnifiedAccessSession
totalFelicaTransitTransaction
totalIdentifiersUnknowntoSE
com.apple.developer.nfc.readersession.iso15693.tag-identifiers
%s:%i Unable to find customer application hash : %s
middlewareVersion
rfFrameInterface
0b
totalSuccessfulCardIngestionWithSessionToken
Generic A
]
{%@=%@, %@=%@}
com.apple.nearfield
Assertion-PowerUp-%d-%lf
CardSessionAIDPrefixList: %@
hasCardEmulationStarted
commandType
%@\n
Power Up
Field detect presentment intent suppression
Iso15693
com.apple.internal.nfc.ignore.appstate
%s:%i %s doesn't exist
WDG_LowPower
%s:%i Value too large: %{public}@
totalFailureWithTransactionEndEventErrors
sessionDuration
+[NFHashes _checkHash:againstReference:expectedVersion:matchingVersion:]_block_invoke
RfProcessSp
totalCardSession
allSystemCodes
longitude
%s:%i Error : Hash is not of expected type
-[NSString(HexString) NF_isPrefixOfHexEncodedEqualToBytes:length:]
https://
21
+[NFNdefRecordInternal decodeFromRecord:]
pollDuration
totalFieldDetectLaunches
endTime
ReleaseType
%s:%i XPC event publisher for stream %@ with action = %d
Psp
statusCode
10
hasAccessExpressTransactionEnable
%@-%@ { Tech=%@ Type=%@ ID=%@ silentType=%d SAK=%@ ATQA=%@ sfgi=0x%X %@ %@}
com.apple.stockholm.preferenceschanged
MiFare DESFire
com.apple.developer.nfc.hce
0123456789ABCDEF
eSEInRestrictedMode
???
seRemovedEvt0Count
+[NFNdefRecordInternal _decodeURIRecord:]
radioChangeCount
bootStopDetected
Generic 4A
mailto:
%s:%i Incorrect length field
hasAttackLogs
-[NFServiceWhitelistChecker _isAIDStringValid:]
%s:%i Invalidating XPC connection
+[NFNdefRecordInternal _decodeTextRecordText:]
tftp:
%@
[Hex dump: offset=%04X] '
%@-%@ { Tech=%@ Type=%@ ID=%@ PMm=%@ %@%@}
)
hash4
YES
method
00
btspp://
NFAssertionTime
tagType1ReadSuccessCount
horizontalAccuracy
btl2cap://
uaCorporateEndpointCount
11
%@ for PID %d (%lf)
TagReader
nci.secondary.dump
_NFContactlessSession
totalLPEMCounter
totalNotNdefTagsRead
ISO15693
BootMeasurements
ValidateAPDUWithAIDAllowList
nci.primary.dump
%s:%i Unregistering Power notifications
-[NSData(HexString) NF_asHexString]
%@*
%s:%i Invalid AID entry: %{public}@
com.apple.nfcd.hwmanager
h63QSdBCiT/z0WU6rdQv6Q
dav://
1b
%s:%i System not ready.  Abort
-[NFAccessoryTagI2CBridge(NTAG5Boost) _readFromBridgeType0:fragmentationSupport:]
Primary
totalPurpleTrustSigningOperations
NFDataPrintAsHexString
%s:%i Have not received initial barrier; not sending %@
smb://
NFSharedLogTransport
GeneralSignposts
nci.secondary.stream
com.apple.nfcd.generalDeviceStatistic
%s:%i Invalid extended response length : %{public}@
atqa
DeviceClassNumber
osID
%s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@
%s:%i String is of invalid length=%ld with 0x prefix
PACE
-[NFServiceWhitelistChecker sessionTimeLimit]
PACEPoll: %@
%s:%i Dispatch queue has been destroyed !
%s
_NFHCESession
totalHighTemperatureNotifCount
startTime
ndefAvailability
middlewareExceptionCount
hash1
hwCount
spmiErrorCount
DescriptionForInternalAssertion
com.apple.nfcd.session.selogging
ISO7816 Set=%@
bundleID
RestoreOSBuild
failForwardRestoreAttemptFailureCount
hasOverCurrentErrors
http://www.
+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]
%s:%i Returned %x
queueWait
com.apple.nfcd.session.peerpayment
%s:%i Unexpected application version %s, expected %s
PassKit foreground presentment intent
NDEFReader
+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]_block_invoke
totalCEEnable
MiFare Plus
[
notNDEFFormatedTagCount
-[NFPowerObserver allowSleep]
totalVASSignup
stockholm-spmi
KernelProcessState
records
TSM.Scripts
totalGenericAExpressTransaction
false
%s:%i Connection ID doesn't match (%lu vs %lu), may have already refreshed. Ignoring
ISO15693Reader
%s:%i Failed to get power assertion - system already going to sleep
Nfc
AccessoryRF
%s:%i Failed to register for PM notifications
totalNoUrlTagsRead
@\"NSDictionary\"8@?0
nfcWithRadio
Msp
com.apple.nfcd.exceptions.contactlessErrors
v32@?0@\"NSString\"8@16^B24
%s:%i Invalid language code length; dropping message
uaHomeEndpointCount
alishaEndpointCount
KernelProcessSp
totalVASTransactionException
faultType
pllUnlockDuringPMICPowerCycle
%s:%i %{public}@ not in allow list
01
%s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple
settleDuration
R0
22
totalCoreNFCSession
PID
\t
com.apple.nfcd.session.se
com.apple.nfcd.session.hardwareRegisters
BurnoutTimerDisable
NFCoreNFCPollConfig.m
SwpProcessPc
file://
sessionType
+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]_block_invoke
AccessoryMiddleware
tech
totalReaderSessionBurnout
Payload
%s:%i [NFTLV TLVWithTag:children:] failed!
%s:%i Failed with 0x%x
historicalBytes=%@ 
com.apple.nfcd.assertion.tagreading
%s:%i Clearing XPC Connection
%s:%i Unable to find protected firmware hash : %s
1c
, %@
%s:%i InterruptedHandler: ConnectionID=%lu
tagType5ReadSuccessCount
AppleHammerfestSPMI
1a
A
, startOnLocUpdate=1
AssertType
hasGenericAExpressEnable
com.apple.developer.nfc.paymentreader.development
com.apple.nfcd.session.reader.internal
RfProcessPc
+[NFNdefRecordInternal _decodeTextRecord:]
19
irdaobex://
Logging
%s:%i System never went to sleep ! Ignoring will power on message.
ecp
totalFelicaEMoneyTransaction
totalCoreNFCPollingDuration
sleepDuration
application-identifier
%s:%i InvalidationHandler: ConnectionID=%lu
%s:%i Invalid payload encoding; dropping message
queryTypeFSystemCodes
_NFSecureElementLoggingSession
_NFTrustSession
TAG: %@
spStatus
endTimestamp
+[NFHashes validateNFCCHashes:reference:expectedVersion:hashResults:]
com.apple.nfc.seld
, 
-[NFServiceWhitelistChecker _initCardSessionEntitlementsWithSecTask:]
PollingProfileUpdate: %d
_NFProductHasNFCRadio
+[NFTLV TLVWithData:]
nci.primary.stream
totalPurpleTrustKeys
MiFare Classic
_NFPlatformGetSupportedLPMFlags
%s:%i XPC event publisher for stream %@ received initial barrier
eventType
urn:epc:raw:
Q
%s:%i \"%s\" errno=%d Failed to read data %ld/%ld
state
%s:%i Unable to find application hash : %s
07
PaymentTagReader
A`
_NFTagSession
_NFECommercePaymentSession
com.apple.nfcd.assertionSupressDefaultAppPresentment
VAS: %@
NFAssertionType
com.apple.stockholm.logging.key
totalPlasticCardModeEnable
hasFelicaExpressTransactionEnable
cardValidationStatus
com.apple.nfcd.exceptions.crsAuthExceptionEvent
1d
No Reset
totalAuthECommerce
Y
-[NFXPCServiceClient getConnectionAndID:]
NDnoY3adyyskgiIQBNtlyQ
-[NFXPCEventPublisher initWithStreamName:queue:]
com.apple.nfcd.exceptions.seRestrictedModeEnteredEvent
pop:
-[NFResponseAPDU decodeUnderlyingAppletError:]
ndefContainerSize
tagType2ReadSuccessCount
nfcDeviceAngle
%s:%i Restricted mode for eSE is NOT set!
%s:%i Unable to create event dictionary; dropping event
WDG_Kernel
Legacy wallet force as default presentment
initialScanText
%s:%i Identifier string does not meet the minimum required length, %{public}@
duration
\"
NFCRadio
XPsr
pllUnlock
TSM
PresentmentIntentSuppressionHolder
se-lpem-enabled
ftp://ftp.
totalBurnoutTimerCounter
controllerType
hammerfest-spmi
AssertionProgramCounter
com.apple.nfcd.exceptions.tsmConnectivityExceptionEvent
com.apple.nfcd.deviceExceptionStatisticDim
rtsp://
urn:nfc:
%s:%i More than one TLV detected
com.apple.nfcd.resetTimingEvent
hash2
R3
VASReader
totalPurpleTrustDatabaseCorruption
-[NFServiceWhitelistChecker _copyValueOfEntitlement:secTask:]
com.apple.internal.nfc.allow.backgrounded.session
NDEF: %@
Root queue has been destroyed
restrictedModeCount
com.apple.nfcd.exceptions.hardwareFault
%s:%d
%s:%i Missing hash !
readerModeConnectErrorCount
holders
Accessory
unknown
venLowDuration
com.apple.nfcd.session.fieldOperations
hash0
totalDuration
F
technology
ndefMessageSize
com.apple.nfcd.session.reader.internal.update.polling.profile
sessionStatus
v32@?0@8Q16^B24
AssertionOnBehalfOfPID
com.apple.nfc
_NFBuiltinSession
failForwardState
identifier
%s:%i String is of invalid length=%ld
nfccModel
R12
breadcrump
com.apple.nfcd.exceptions.txLdoErrors
%s:%i Unsupported length 0x%X
+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]
v32@?0@8@16^B24
SystemCodeList=%@ 
12
%s:%i Expected length is too large.
_NFContactlessPaymentSession
%s:%i Resume connectionID=%lu
SwpProcessState
KernelProcessWaitObject
com.apple.nfcd.exceptions.hciTransactionExceptionEvent
deactivateAllApps
com.apple.nfc.signpost
com.apple.nfcd.sessionMetrics
-[NFXPCEventPublisher initWithStreamName:queue:]_block_invoke_2
disableCompletionNotification
mode=%lu, type=%@%@%@%@
[Hex dump: length=%lu bytes] (%s:%i %s)
_NFSecureTransactionServicesHandoverHybridSession
%s:%i Failed to alloc %ld
SystemCode
TagSerialNumber
com.apple.nfcd.exceptions.mobileSoftwareUpdateExceptionEvent
%s:%i No TLV detected
%s:%i Underflow
_TLVCreateWithBytes
%s:%i NULL error: tag=0x%x len=%u
NDEF
com.apple.nfcd.session.cardmigration
i
Unexpected Result
%s:%i Could not create the Publisher!!!
PC
systemOS
%s:%i System never went to sleep ! Ignoring will not sleep message.
totalIdentifiersReceived
com.apple.nfcd.exceptions.ReaderModeExceptionEvent
0a
%s:%i Underflow: tag=0x%x
totalNotBackgroundTagsRead
TagManufacturerCode
%s:%i Unable to find info hash : %s
NFLogGetLogger
totalPurpleTrustKeyDeletionFailed
CallbackUUID
NFDataAppendBytes
*%@
CH
WDG_RF
reason
RF
_NFSecureElementAndHostCardEmulationSession
HostProcessSp
parityErrorCount
%@ { %@ }
platformIdentifier
13
%s:%i Invalid URI; dropping message
%@ %02x = %@ \"%@\"
com.apple.nfcd.assertion.dontreset
com.apple.stockholm.analytics
sessionConfig
WDG_Sys_Ticks
imap:
com.apple.ManagedConfiguration.profileListChanged
TAG
NFBuildVersion_block_invoke
_NFPlatformSupportsSecureTimersInOff
%s:%i Radio %s.
totalRestrictModeEntered
com.apple.nfcd.exceptions.expressSetupFailures
%s:%i Invalid payload length; dropping message
'%@' : %@
NFDataCreateWithFile
:
present
14
%s:%i Unexpected %u len on tag 0
-[NFPowerObserver _powerNotificationMessage:argument:]
totalProhibitTimerErrors
*
sessionConfigOverride
WDG_SWP
nfs://
urn:epc:
_NFReaderSession
%s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring
_NFRootQueueFinalizer
mobile
+[NFCommandAPDU appendExpectedLength:usingExtendedLength:toAPDU:]
MiFare
sak
com.apple.internal.nfc.use.unfiltered.applets
dailyDeviceUUID
NFPlatformHasLoadSwitchWorkaround
errorCode
passIdentifier
@`
Application Identifier: %@
-[NFXPCEventPublisher sendXpcNotificationEventWithDictionary:]
%s:%i [Tag 0x11] Unexpected data length: 0x%X
_NFLPEMConfigSession
totalOtherErrors
assertionType
com.apple.nfcd.singleUser
successfulTapCount
%s:%i Validated %lu hashes
HWModelStr
firstOctet
-[NFPowerAssertion holdPowerAssertion:onBehalfOf:behaviourWhenSleepStarted:]
com.apple.nfcd.session.ecommerce
%s:%i Unable to find scratch lifecycle hash : %s
%s:%i Unexpected protected firmware version %s, expected %s
hasAlternateRFSettings
%@ { records %@ }
delayConnectionHandoverRestart
%s:%i Unrecognized tag: 0x%X
%@[%@]
-[NFXPCServiceClient getConnectionAndID:]_block_invoke
sip:
com.apple.nfc.accessory.signpost
totalCEEnabledWithNoFieldDetected
v32@?0@\"NSString\"8@\"NSData\"16^B24
furyLoadStackErrorCount
payload
-[NFTLV valueAsUnsignedLong]
totalTransientDeactiveTimeout
totalVASActivation
com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes
com.apple.nfcd.radio.powertoggle
%s:%i Unable to find scratch firmware hash : %s
%s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s
tagType
includeAPDUDuration
vasMode
Generic B
historicalBytes
type
aid
tel:
NFPowerAssertion
com.apple.stockholm.NCILog
NFTagInternal.m
urn:epc:tag:
2
-[NFPowerAssertion releasePowerAssertion:logFaultOnOverRelease:]
com.apple.nfc.middleware
-[NFPowerObserver registerForEvents]
%s:%i Unexpected customer application version %s, expected %s
HostProcessState
v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24
_NFSingleUserSession
Generic 3A
overCurrentErrorCount
%s:%i 0 record type length; unable to decode
%s:%i opened assertion: counter: %lu id: %{public}@
com.apple.nfcd.generalTransactionStatisticDim
com.apple.nfcd.lpcdStatistic
pollingOption
swStatus
No description provided
AIDAllowList
23
, delayCHRestart=1
blockedBySessionType
com.apple.developer.nfc.readersession.formats
IsUIBuild
IsVirtualDevice
WDG_MBox
com.apple.nfcd.exceptions.appletProvisioningFailures
btgoep://
CoreNFC
typeFSystemCode
totalAccessTransaction
loadStackErrorCount
%s:%i all assertions: %{public}@
currentBatteryLevel
%s:%i Invalid reference format
hash6
_NFSeshatSession
%s:%i \"%s\" errno=%d Failed to realloc to %zu bytes
%s:%i Source is not hex encoded bytes
ftp://anonymous:anonymous@
18
%s:%i Invalid payload character; dropping message
-[NFPowerObserver unregisterForEvents]
totalCoreNFCConnectionDuration
totalCardProvisioned
%s:%i \"%s\" errno=%d Failed to open %s
%s:%i Failed find IOKit service
1e
, devTestMode=1
%s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@
initialUIText
com.apple.nfcd.plasticCardEnableEvent
com.apple.nfcd.seshat
C
-[NFXPCEventPublisher handleEventWithAction:token:descriptor:]
WDG_Host
contactless
3
nfcDeviceModeStateChangeCount
N
com.apple.nfcd.cardIngestionSessionStateChangeEvent
status
urn:epc:id:
1f
totalAPNReceived
%s:%i Identifier string exceeds the maximum length, %{public}@
sessionEndTime
tagType4ReadSuccessCount
absent
hfLr
com.apple.nfcd.deviceExceptionStatistic
PM assertion create failure
%s:%i %{public}@ does not hold assertion
Secondary
%s:%i Failed to get entitlements: %{public}@
nil != self
readerModeDisconnectErrorCount
seid
+[NFMSEIParser parseResponseAPDU:]
silentType
DEV
com.apple.nfcd.exceptions.seRestrictedModeExitEvent
NSDictionary
pace
aliroEndpointCount
UID
com.apple.nfcd.assertion.handover
nfcd
AssertLevel
PMm
%s:%i %{public}@ Expected %{public}@, got %{public}@
lpm
assertionDebug
%s:%i prefixBytes is of invalid length=%ld
%s:%i Invalid character found, skipping
0c
NFTimer: not started
_NFSecureElementManagerSession
com.apple.nfcd.setupEndpointFailureEvent
sn450WithLoadSwitch
+[NFNdefRecordInternal _decodeTextRecordLanguage:]
B
sfgi
(
+[NSData(HexString) NF_dataWithHexString:]
-[NFXPCServiceClient invalidateConnection]
c
UnknownBuild
%s:%i Unexpected length did you mean to use extended length ?
%@ %02x : %@
totalSuccessfulCardIngestion
currentProvisionedCards
-[NFTagInternal _setSupportsPACE:]
%s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@
altitude
%s:%i Unable to find protected lifecycle hash : %s
sftp://
sips:
NFSharedLog.c
%s:%i Underflow: tag=0x%x len=%u
Felica
SystemCode=%@
%s:%i Failed to connect to NFCD
com.apple.nfc.middleware.signpost
MiFare UL
com.apple.nfcd.session.lpemConfig
reportId
Invalid Parameter
com.apple.nfcd.exceptions.crsAuthInitExceptionEvent
0f
20
com.apple.nfcd.dailyBackgroundTagReadingEvent
totalSuccesfulBackgroundTagsRead
Overflow
v12@?0i8
commandResult
0d
vasPasses
```
