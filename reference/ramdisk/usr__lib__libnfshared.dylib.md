# `/usr/lib/libnfshared.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 469,312 bytes.

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
07
ftp://anonymous:anonymous@
Unknown
vasMode
%s:%i Unsupported length 0x%X
%s
hammerfest-spmi
08
%s:%i Underflow
-[NFPowerAssertion releasePowerAssertion:logFaultOnOverRelease:]
RF
totalFelicaTransitTransaction
blockedBySessionType
_NFProductHasNFCRadio
com.apple.nfcd.exceptions.seRestrictedModeExitEvent
09
hasAccessExpressTransactionEnable
%s:%i Invalid extended response length : %{public}@
com.apple.nfcd.lpm.factorytest
NDEF: %@
Legacy ISO15693 filter List=%@
hash1
pop:
1e
vasPasses
CallbackUUID
%s:%i \"%s\" errno=%d Failed to open %s
ndefAvailability
com.apple.nfcd.session.cardmigration
WDG_SWP
context
https://
uaCorporateEndpointCount
%s:%i Dispatch queue has been destroyed !
+[NFNdefRecordInternal _decodeTextRecord:]
urn:epc:raw:
%s:%i Unregistering Power notifications
FDPresentmentIntentSuppressionHolder
sessionConfig
statusCode
%s:%i Invalid payload length; dropping message
%@%@
-[NFTLV valueAsUnsignedLongLong]
Middleware
-[NFPowerObserver _powerNotificationMessage:argument:]
Generic 3B
felicaSystemCodes
%s:%i Failed to query build
faultType
%@ { %@ }
PreventUserIdleSystemSleep
totalSuccessfulCardIngestion
totalCHFieldNotification
unknown
%@\n
U
totalAPNReceived
totalCardSession
com.apple.developer.nfc.readersession.iso15693.tag-identifiers
%s:%i Invalidating XPC connection
SwpProcessSp
noUUID
totalFailureWithMissingTransactionEndEvent
alishaEndpointCount
com.apple.nfcd.session.se
%s:%d
SwpProcessWaitObject
hwCount
NSArray
com.apple.nfcd.resetTimingEvent
com.apple.nfcd.deviceExceptionStatistic
ftps://
com.apple.nearfield
22
CoreNFC
F
selectedAID
com.apple.nfcd.hce
tagType5ReadSuccessCount
loadStackErrorCount
tel:
dav://
sips:
delayConnectionHandoverRestart
%s:%i Incorrect length field
-[NFPowerObserver unregisterForEvents]
com.apple.stockholm.preferenceschanged
%s:%i Error : Hash is not of expected type
1c
1d
%02x
+[NFNdefRecordInternal decodeFromRecord:]
Prevent Connection Handover
%s:%i released assertion: counter: %lu id: %{public}@
com.apple.stockholm.NCILog
nfs://
23
NFAssertionTime
+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]
com.apple.greentea
Accessory
_NFTagSession
totalAccessTransaction
Payload
records
NSDictionary
GeneralSignposts
totalCEEnabledWithNoFieldDetected
totalFailureWithTransactionEndEventErrors
totalProhibitTimerErrors
controllerType
%s:%i %s doesn't exist
v32@?0@\"NSString\"8@16^B24
05
totalSuccessfulVAS
radioIsEnabled
totalIdentifiersUnknowntoSE
kextCallDuration
MiFare Classic
urn:epc:tag:
%s:%i Unexpected length did you mean to use extended length ?
totalDynamicRFParametersUpdate
totalDynamicPackages
%@-%@ { Tech=%@ Type=%@ ID=%@ PMm=%@ %@%@}
-[NSData(HexString) NF_asHexString]
spStatus
hash6
16
Secondary
totalExpressFelicaTransaction
_TLVCreateWithBytes
TagManufacturerCode
NDEF
%s:%i Invalid AID entry: %{public}@
_NFPlatformGetSupportedLPMFlags
com.apple.nfcd.exceptions.expressSetupFailures
initialScanText
ConfigType
_NFReaderSession
SystemCode
%s:%i Error fetching teamID: %{public}@
%s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@
stockholm
pllUnlockDuringPMICPowerCycle
holders
totalHighTemperatureNotifCount
totalDuration
com.apple.developer.nfc.paymentreader.development
com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes
com.apple.nfcd.session.ecommerce
readerModeTransceiveErrorCount
%@[%@]
%s:%i System never went to sleep ! Ignoring will power on message.
nfcDeviceModeStateChangeCount
(
VAS
com.apple.UIKit.vends-view-services
com.apple.nfcd.session.selogging
%s:%i Expected length is too large.
%s:%i Require definite encoding, but got zero tag and len
Logging
com.apple.developer.nfc.readersession.iso7816.select-identifiers.trusted
ISO7816 Set=%@
PACEPoll: %@
state
com.apple.nfcd.exceptions.middlewareExceptionEvent
18
file://
NFDataCreateWithFile
successfulTapCount
Darwin Internal
com.apple.nfcd.exceptions.txLdoErrors
%s:%i Invalid payload encoding; dropping message
http://www.
com.apple.internal.nfc.use.unfiltered.applets
notNDEFFormatedTagCount
eventType
id
17
urn:epc:
+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]_block_invoke
+[NFTLV _parseTLVs:end:simple:definite:]
r
ISO15693
sn450WithLoadSwitch
RfProcessSp
Field detect presentment intent suppression
%@ for PID %d (%lf)
%@ %02x = %@
_NFSecureTransactionServicesHandoverHybridSession
_NFSecureTransactionServicesHandoverSession
totalCoreNFCConnectionDuration
%s:%i Unable to find scratch firmware hash : %s
nfcWithRadio
com.apple.nfcd.exceptions.hciTransactionExceptionEvent
_NFInternalConfigurationSession
totalPurpleTrustKeys
%s:%i Identifier string exceeds the maximum length, %{public}@
longitude
_NFPlatformSupportsSecureTimersInOff
YES
3
queueWait
assertionType
com.apple.internal.nfc.allow.backgrounded.session
currentBatteryLevel
hash4
NFCoreNFCPollConfig.m
com.apple.nfcd.exceptions.tsmConnectivityExceptionEvent
TagReader
historicalBytes
]
%s:%i InterruptedHandler: ConnectionID=%lu
bundleID
KernelProcessState
WDG_RF
%s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@
nci.primary.stream
com.apple.seld.tsmmanager
%s:%i Clearing XPC Connection
horizontalAccuracy
nil != self
nfccFWVersion
restrictedModeCount
com.apple.nfcd.exceptions.appletProvisioningFailures
VASReader
com.apple.nfcd.generalTransactionStatistic
MiFare DESFire
atqa
platformIdentifier
rfFrameInterface
[Hex dump: offset=%04X] '
com.apple.nfcd.dailyBackgroundTagReadingEvent
0123456789abcdefABCDEF*
com.apple.nfcd.session.trust
hasCardEmulationStarted
+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]_block_invoke
totalNoUrlTagsRead
sak
eSEInRestrictedMode
nfcd
%@ { records %@ }
allSystemCodes
com.apple.nfcd.mininv.write
errorStatus
news:
Presentment intent suppression
inRestoreOS
UID
sessionEndTime
@\"NSDictionary\"8@?0
dev
hasAttackLogs
IsVirtualDevice
R12
%s:%i 0 record type length; unable to decode
initialUIText
totalCHConnections
i
disableCompletionNotification
AccessoryRF
%s:%i %s: %s
sfgi
*
Application Identifier: %@
+[NFHashes validateNFCCHashes:reference:expectedVersion:hashResults:]
+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]
%s:%i [NFTLV TLVWithTag:children:] failed!
%s:%i Underflow: tag=0x%x len=%u
com.apple.nfcd.assertionSupressDefaultAppPresentment
nfcDeviceModeDefault
IsUIBuild
10
%s:%i Minimum length requirement not met
%s:%i Unexpected customer application version %s, expected %s
breadcrump
contactless
mailto:
0a
pollDuration
_NFContactlessSession
-[NFXPCServiceClient getConnectionAndID:]_block_invoke
validHash
Darwin
%s:%i Could not create the Publisher!!!
deactivateAllApps
http://
totalAuthECommerce
totalPeerPaymentRequestFailure
totalPlasticCardModeEnable
'%@' : %@
, %@
A
%s:%i opened assertion: counter: %lu id: %{public}@
ecp
totalBurnoutTimerCounter
%s:%i \"%s\" errno=%d Failed to read data %ld/%ld
)
1
v32@?0@8@16^B24
Q
totalFieldDetectLaunches
%@-%@ { Tech=%@ Type=%@ ID=%@ silentType=%d SAK=%@ ATQA=%@ sfgi=0x%X %@ %@}
application-identifier
-[NFXPCServiceClient invalidateConnection]
cardValidationStatus
%s:%i Unexpected protected firmware version %s, expected %s
HWModelStr
%s:%i Radio %s.
%@ { MB=%d ME=%d CF=%d SR=%d IL=%d TNF=%d Type Length=%d Type=%@ ID=%@ Payload Length=%d Payload=%@ }
%s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu
NFTimer: not started
skipMifareClassify
falseDetectionCount
pollingOption
%s:%i Failed find IOKit service
%s:%i Have not received initial barrier; not sending %@
%s:%i [Tag 0x12] Unexpected data length: 0x%X
%s:%i Failed to register for PM notifications
fd
hasFelicaExpressTransactionEnable
NFCReaderUsageDescription
%s:%i Unable to find info hash : %s
%s:%i %{public}@ not in allow list
sessionDuration
NFDataAppendBytes
I
-[NFAccessoryTagI2CBridge(NTAG5Boost) _readFromBridgeType0:fragmentationSupport:]
AccessoryMiddleware
false
com.apple.nfcd.deviceExceptionStatisticDim
readerModeDisconnectErrorCount
totalCEEnable
com.apple.nfcd.hwmanager
tagType4ReadSuccessCount
com.apple.nfcd.lpcdStatistic
altitude
AIDAllowList
%s:%i No TLV detected
NFSharedLogTransport
com.apple.nfcd.radio.powertoggle
h63QSdBCiT/z0WU6rdQv6Q
NFPlatformHasLoadSwitchWorkaround
PM assertion create failure
PM assertion release failure
C
RestoreOSBuild
com.apple.nfcd.exceptions.crsAuthInitExceptionEvent
commandResult
%s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple
-[NFAccessoryTagI2CBridge(NTAG5Boost) _bridgeType0ReadMultipleSRAMPagesWithBuffer:]
AssertLevel
aids
com.apple.nfcd.cardIngestionSessionStateChangeEvent
-[NFXPCEventPublisher initWithStreamName:queue:]
systemOS
15
Untagged internal use
totalReaderSession
-[NFXPCServiceClient resetConnectionWithId:]
sessionStartTime
hash2
WDG_Host
seRemovedEvt0Count
totalNotBackgroundTagsRead
serviceType
\t
%s:%i Resume connectionID=%lu
com.apple.stockholm
RfProcessState
exceptionData
01
, startOnLocUpdate=1
NFPowerAssertion
%s:%i System never went to sleep ! Ignoring will not sleep message.
queryTypeFSystemCodes
hasExpressTransactionStarted
com.apple.nfc.accessory.signpost
PID
totalMWExceptions
AssertName
NFLogGetLogger
_NFUnifiedAccessSession
totalDoubleClickLaunches
Felica
com.apple.internal.nfc.ignore.appstate
tagType3ReadSuccessCount
sessionConfigOverride
com.apple.nfcd.exceptions.vasTransactionExceptionEvent
https://www.
sessionType
com.apple.nfc.seld
_NFSecureElementLoggingSession
_NFBuiltinSession
bootStopDetected
nfccModel
SwpProcessPc
checkAIDAllowList
%s:%i all assertions: %{public}@
%s:%i Failed to alloc %ld
Generic B
ndefMessageSize
-[NFServiceWhitelistChecker _copyValueOfEntitlement:secTask:]
+[NFHashes _checkHash:againstReference:expectedVersion:matchingVersion:]_block_invoke
RfProcessWaitObject
type
hasOverCurrentErrors
seid
imap:
tcpobex://
NDEFReader
sftp://
NFLogSetLogger
*%@
[
%s:%i Failed to connect to NFCD
reportId
commandType
%s:%i More than one TLV detected
com.apple.nfc.rf
LR
03
12
PMm
%@ %02x = %@ \"%@\"
chipID
Generic 3A
com.apple.nfcd.session.reader.internal.update.polling.profile
%s:%i Invalid reference format
Msp
Nfc
_NFCredentialSession
totalLPEMCounter
com.apple.nfcd.session.hardwareRegisters
HostProcessState
hfLr
%s:%i prefixBytes is of invalid length=%ld
06
-[NFCoreNFCPollConfig initPollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:]
true
failForwardRestoreAttemptFailureCount
currentProvisionedCards
-[NSDictionary(NFExtension) NF_objectForKey:expectedClass:]
NFBuildVersion_block_invoke
transactionUUID
smb://
0c
venLowDuration
ReleaseType
UnknownBuild
02
sip:
NFAssertionType
com.apple.nfc.signpost
%s:%i InvalidationHandler: ConnectionID=%lu
%s:%i Unable to find scratch lifecycle hash : %s
description
20
radioChangeCount
totalNotNdefTagsRead
sleepDuration
MiFare Plus
historicalBytes=%@ 
NFPlatformHasBootMeasurements
Psp
parityErrorCount
ValidateAPDUWithAIDAllowList
%s:%i Unrecognized tag: 0x%X
category < NFLogCategoryMax
identifier
%s:%i Unexpected application version %s, expected %s
-[NFXPCEventPublisher handleEventWithAction:token:descriptor:]
WDG_MBox
firstOctet
0b
1b
%s:%i Failed with 0x%x
_NFFieldDetectSession
NDnoY3adyyskgiIQBNtlyQ
IsSimulator
_NFPlatformGetEdtNFCCModel
overCurrentErrorCount
0e
0f
NFTagInternal.m
Generic A
WDG_Sys_Ticks
mwCount
com.apple.nfcd.exceptions.seFailures
furyLoadStackErrorCount
DescriptionForInternalAssertion
tech
MiFare UL
%@-%@ { Tech=%@ Type=%@ ID=%@, NDEF=%d, capacity=%lu, messageSize=%lu }
telnet://
tftp:
1a
@`
A`
-[NFPowerObserver allowSleep]
totalIdentifiersReceived
supportsPACE
%s:%i Unexpected error from XPC event publisher for stream %{public}@: %s
nfcDeviceAngle
urn:
19
passIdentifier
tagType2ReadSuccessCount
latitude
R3
osID
_NFLoyaltyAndPaymentSession
%@*
com.apple.developer.nfc.readersession.formats
city
status
Overflow
-[NFServiceWhitelistChecker _initCardSessionEntitlementsWithSecTask:]
com.apple.nfcd.assertion.dontreset
{%@=%@, %@=%@}
CH
lpm
+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]_block_invoke
typeFSystemCode
hasGenericAExpressEnable
-[NFXPCServiceClient resetConnection]
com.apple.stockholm.analytics
Unexpected Result
hardwareType
assertionDebug
%s:%i [Tag 0x%X] Unexpected data length: 0x%X
_NFCardMigrationPaymentSession
-[NFResponseAPDU decodeUnderlyingAppletError:]
+[NSData(HexString) NF_dataWithHexString:]
_NFPeerPaymentSession
ndefContainerSize
N
BootMeasurements
absent
readerModeConnectErrorCount
%s:%i Invalid URI; dropping message
Assertion-PowerUp-%d-%lf
totalPurpleTrustDatabaseCorruption
-[NFCALogger removeRestrictedMode]
hasAlternateRFSettings
com.apple.nfcd.powerassertion
_NFContactlessPaymentSession
%s:%i \"%s\" errno=%d Failed to realloc to %zu bytes
-[NFXPCEventPublisher sendXpcNotificationEventWithDictionary:]
R1
method
totalTransientDeactiveTimeout
timestampDay
DEV
com.apple.nfcd.exceptions.hardwareFault
13
%s:%i Invalid payload character; dropping message
%s:%i Failed to get entitlements: %{public}@
VAS: %@
TAG: %@
HostProcessSp
%s:%i Source is not hex encoded bytes
urn:epc:id:
T
NFAssertionPID
PaymentTagReader
_NFSecureElementReaderSession
totalCoreNFCSessionBurnout
iso7816SelectIdentifiers
v28@?0I8Q12@\"NSObject<OS_xpc_object>\"20
irdaobex://
-[NFAccessoryTagI2CBridge(NTAG5Boost) _writeToBridgeType0:fragmentationSupport:]
NFSharedDumpTransport
settleDuration
PresentmentIntentSuppressionHolder
CardSession: %@
+[NFMSEIParser parseResponseAPDU:]
+[NFTLV TLVWithData:]
%s:%i %{public}@ does not hold assertion
totalReaderSessionBurnout
%s:%i String is of invalid length=%ld with 0x prefix
%s:%i %{public}@ Expected %{public}@, got %{public}@
middlewareExceptionCount
DeviceClassNumber
KernelProcessSp
ftp://
PassKit foreground presentment intent
com.apple.nfcd.generalTransactionStatisticDim
totalFelicaEMoneyTransaction
totalPeerPaymentRequest
WDG_Kernel
aid
urn:nfc:
NFCIP
PACE=Y
com.apple.developer.nfc.hce
com.apple.nfcd.assertion.tagreading
com.apple.nfcd.assertion.handover
%s:%i Unable to find protected lifecycle hash : %s
NFTimer: popTimeInSeconds: %f
Generic 4A
%s:%i String is of invalid length=%ld
sessionStatus
%s:%i Unable to find customer application hash : %s
Invalid Parameter
totalRestrictModeEntered
%s:%i Invalid character found, skipping
Legacy wallet force as default presentment
TagSerialNumber
initialSelectBeforeRun
-[NFPowerObserver registerForEvents]
_NFSingleUserSession
totalOtherErrors
%s:%i Disabled
Root queue has been destroyed
country
hash0
%s:%i Unable to find application hash : %s
com.apple.nfc.middleware
%s:%i Returned %x
endTime
BurnoutTimerDisable
teamID
se-lpem-enabled
21
uiMode
startTime
MiFare
AppleHammerfestSPMI
stockholm-spmi
com.apple.stockholm.logging.key
Iso15693
SystemCode=%@
%s:%i Unexpected version %s, expected %s
PC
com.apple.nfcd.exceptions.crsAuthExceptionEvent
rtsp://
btspp://
btl2cap://
%s:%i [Tag 0x11] Unexpected data length: 0x%X
lpcd
+[NFNdefRecordInternal _decodeTextRecordText:]
com.apple.nfc
developmentPresentments
BuildVersion
com.apple.nfcd.exceptions.ReaderModeExceptionEvent
_NFECommercePaymentSession
resetMode
com.apple.nfcd.session.credential.manager
%s:%i Restricted mode for eSE is NOT set!
%s:%i XPC event publisher for stream %@ with action = %d
11
_NFTrustSession
%s:%i Unable to find protected firmware hash : %s
pllUnlock
%s:%i Invalid language code length; dropping message
00
ISO15693Reader
totalCEEnabledWithMissingTransactionEndEvent
totalSuccesfulBackgroundTagsRead
:
hash3
+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]
%s:%i Unexpected %u len on tag 0
%s:%i System not ready.  Abort
SystemCodeList=%@ 
com.apple.ManagedConfiguration.profileListChanged
WDG_LowPower
tagType
com.apple.nfcd.exceptions.contactlessErrors
ftp://ftp.
totalCoreNFCSession
com.apple.nfcd.generalDeviceStatistic
com.apple.nfcd.exceptions.mobileSoftwareUpdateExceptionEvent
mode=%lu, type=%@%@%@%@
%s:%i Value too large: %{public}@
configuredTime
com.apple.nfcd.seshat
CFBundleIdentifier
Method
mobile
, delayCHRestart=1
v32@?0@8Q16^B24
%s:%i Tag value overflows
currentNFCDefault
%s:%i Cannot create SecTaskRef with XPC Connection: %{public}@
%s:%i Connection ID doesn't match (%lu vs %lu), may have already refreshed. Ignoring
R2
swStatus
btgoep://
!
com.apple.nfc.middleware.signpost
TSM.Scripts
totalVASSignup
com.apple.nfcd.setupEndpointFailureEvent
com.apple.nfcd.exceptions.seRestrictedModeEnteredEvent
includeAPDUDuration
+[NFCommandAPDU appendExpectedLength:usingExtendedLength:toAPDU:]
[Hex dump: length=%lu bytes] (%s:%i %s)
, 
%s:%i Memory allocation request failed.
%s:%i ConnectionID does not match active (%lu), may have already been cleared
duration
%@ %02x : %@
nci.secondary.stream
com.apple.stockholm.powerobserver
/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
spmiErrorCount
NFSharedLog.c
hasError
com.apple.nfcd.sessionMetrics
dailyDeviceUUID
uuidUpdateDate
NFCRadio
HostProcessPc
com.apple.nfcd.exceptions.seRemovedEvent
+[NFNdefRecordInternal _decodeTextRecordLanguage:]
AssertType
uaHomeEndpointCount
nfc
RfProcessPc
com.apple.nfcd.exceptions.atlFailures
14
1f
2
B
com.apple.nfcd.session.reader.internal
AssertionProgramCounter
XPsr
04
com.apple.nfc.i2cbridge
, devTestMode=1
TSM
totalVASActivation
-[NFServiceWhitelistChecker _initCoreNFCEntitlements:secTask:]
v8@?0
Line
%s:%i Validated %lu hashes
%s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@
nci.primary.dump
totalGenericAExpressTransaction
PollingProfileUpdate: %d
R0
%@
%s:%i Failed to get power assertion - system already going to sleep
_NFLPEMConfigSession
com.apple.nfcd.session.peerpayment
startTimestamp
payload
0d
totalCoreNFCPollingDuration
silentType
TAG
%s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s
%s:%i Unable to create event dictionary; dropping event
+[NFCommandAPDU buildAPDUHeaderWithClass:instruction:p1:p2:len:useExtendedLength:]
totalPurpleTrustKeyDeletionFailed
aliroEndpointCount
com.apple.nfcd.singleUser
%s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring
c
AppleStockholmSPMI
HostProcessWaitObject
com.apple.nfcd.exceptions.hardwareExceptionEvent
No description provided
Power Up
%s:%i Underflow: tag=0x%x
%s:%i System already sent a will sleep message ! Ignoring will sleep.
_NFHCESession
pace
failForwardState
com.apple.nfcd.plasticCardEnableEvent
technology
endTimestamp
KernelProcessPc
reason
_NFSecureElementAndHostCardEmulationSession
PACE
%s:%i Identifier string does not meet the minimum required length, %{public}@
CardSessionAIDPrefixList: %@
-[NFXPCEventPublisher initWithStreamName:queue:]_block_invoke_2
errorCode
totalVASTransactionException
No Reset
AssertionOnBehalfOfPID
-[NFPowerAssertion holdPowerAssertion:onBehalfOf:behaviourWhenSleepStarted:]
_NFSeshatSession
totalSuccessfulCardIngestionWithSessionToken
present
nci.secondary.dump
totalLowTemperatureNotifCount
totalCardProvisioned
-[NFXPCServiceClient getConnectionAndID:]
%s:%i Missing hash !
%s:%i XPC event publisher for stream %@ received initial barrier
Primary
com.apple.nfcd.session.lpemConfig
tagType1ReadSuccessCount
hash5
Invalid State
\"
???
-[NSString(HexString) NF_isPrefixOfHexEncodedEqualToBytes:length:]
_NFCardSession
%s:%i NULL error: tag=0x%x len=%u
Generic 4B
-[NFXPCEventPublisher sendXpcNotificationEvent:]_block_invoke
SwpProcessState
middlewareVersion
urn:epc:pat:
-[NFServiceWhitelistChecker sessionTimeLimit]
Y
_NFRootQueueFinalizer
v32@?0@\"NSString\"8@\"NSData\"16^B24
+[NFNdefRecordInternal _decodeURIRecord:]
-[NFTLV valueAsUnsignedShort]
v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24
_NFSecureElementManagerSession
totalPurpleTrustSigningOperations
AppData
-[NFServiceWhitelistChecker initWithConnection:coreNFCConnection:]
v12@?0i8
KernelProcessWaitObject
-[NFTLV valueAsUnsignedLong]
totalTransactionEndEvent
NFDataPrintAsHexString
-[NFTagInternal _setSupportsPACE:]
-[NFServiceWhitelistChecker _isAIDStringValid:]
com.apple.nfcd.session.fieldOperations
0123456789ABCDEF
com.apple.nfcd.exceptions.osResetEvent
exitReason
%{public}s:%i Failed to alloc %ld
%{public}s:%i [Tag 0x%X] Unexpected data length: 0x%X
%{public}s:%i Unexpected %u len on tag 0
transceiveToI2c_select
%{public}s:%i Disabled
%{public}s:%i Failed find IOKit service
%{public}s:%i Require definite encoding, but got zero tag and len
%{public}s:%i \"%s\" errno=%d Failed to open %s
%{public}s:%i all assertions: %{public}@
%{public}@ does not hold assertion
%{public}s:%i Failed to register for PM notifications
%{public}s:%i Restricted mode for eSE is NOT set!
%{public}s:%i Failed to query build
%{public}s:%i %s doesn't exist
%{public}s:%i Expected length is too large.
transceiveToI2c_read
%{public}s:%i released assertion: counter: %lu id: %{public}@
system will power on
%{public}s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring
%{public}s:%i Failed to connect to NFCD
%{public}s:%i Unable to find info hash : %s
%{public}s:%i Unable to find scratch lifecycle hash : %s
Critical error : this device should have NFC !!! cache = %d, MG = %d, EDT = %d
%{public}s:%i Radio %s.
%{public}s:%i Source is not hex encoded bytes
%{public}s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu
%{public}s:%i System never went to sleep ! Ignoring will not sleep message.
%{public}s:%i Have not received initial barrier; not sending %@
%{public}s:%i System already sent a will sleep message ! Ignoring will sleep.
%{public}s:%i Dispatch queue has been destroyed !
%{public}s:%i prefixBytes is of invalid length=%ld
%{public}s:%i %{public}@ not in allow list
%{public}s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@
error
%{public}s:%i ConnectionID does not match active (%lu), may have already been cleared
%{public}s:%i Clearing XPC Connection
%{public}s:%i Value too large: %{public}@
%{public}s:%i Underflow: tag=0x%x
%{public}s:%i Invalid AID entry: %{public}@
%{public}s:%i Validated %lu hashes
%{public}s:%i Failed to get power assertion - system already going to sleep
%{public}s:%i Unable to create event dictionary; dropping event
%{public}s:%i Memory allocation request failed.
%{public}s:%i NULL error: tag=0x%x len=%u
%{public}s:%i \"%s\" errno=%d Failed to realloc to %zu bytes
%{public}s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s
transceiveToI2c_read1SRAMPage
%{public}s:%i Unregistering Power notifications
%{public}s:%i %{public}@ Expected %{public}@, got %{public}@
%{public}s:%i Error fetching teamID: %{public}@
totalLen=%{public,signpost.description:attribute}lu
%{public}s:%i Missing hash !
%{public}s:%i Unexpected error from XPC event publisher for stream %{public}@: %s
%{public}s:%i XPC event publisher for stream %@ received initial barrier
%{public}s:%i Identifier string does not meet the minimum required length, %{public}@
transceiveToI2c_pollForSystemReady
%{public}s %{public,stockholm:NCI}.*P
%{public}s:%i Unable to find application hash : %s
%{public}s:%i [Tag 0x11] Unexpected data length: 0x%X
%{public}s:%i No TLV detected
%{public}s:%i More than one TLV detected
beforeWrite=%{public,signpost.description:attribute}d
XPC service client invalidated
%{public}s:%i Unexpected application version %s, expected %s
%{public}s:%i Unexpected length did you mean to use extended length ?
%{public}s:%i Unrecognized tag: 0x%X
%{public}s:%i Tag value overflows
%{public}s:%i Failed with 0x%x
%{public}s:%i Minimum length requirement not met
%{public}s:%i InvalidationHandler: ConnectionID=%lu
%{public}s:%i Resume connectionID=%lu
%{public}s:%i Connection ID doesn't match (%lu vs %lu), may have already refreshed. Ignoring
%{public}s:%i Error : Hash is not of expected type
%{public}s:%i Invalid URI; dropping message
ReadConfigError
transceiveToI2c_pollForWriteComplete
%{public}s:%i Could not create the Publisher!!!
%{public}s:%i %{public}@ does not hold assertion
%{public}s:%i Invalid extended response length : %{public}@
%{public}s:%i Unable to find scratch firmware hash : %s
%{public}s:%i Unexpected version %s, expected %s
%{public}s:%i Unable to find protected firmware hash : %s
%{public}s:%i Invalid language code length; dropping message
%{public}s:%i Unexpected customer application version %s, expected %s
timeout=%{public,signpost.description:attribute}d
%{public}s:%i System never went to sleep ! Ignoring will power on message.
%{public}s:%i Unexpected protected firmware version %s, expected %s
%{public}s:%i Invalid character found, skipping
%{public}s:%i 0 record type length; unable to decode
system will not sleep
%{public}s:%i Underflow: tag=0x%x len=%u
XPC service client interrupted
%{public}s:%i Unable to find customer application hash : %s
%{public}s:%i [NFTLV TLVWithTag:children:] failed!
Error 0x%02X : %{public}s
%{public}s:%i String is of invalid length=%ld
%{public}s:%i Invalidating XPC connection
%{public}s:%i Invalid payload character; dropping message
%{public}s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple
%{public}s:%i Invalid reference format
%{public}s:%i Unable to find protected lifecycle hash : %s
%{public}s:%i XPC event publisher for stream %@ with action = %d
%{public}s:%i Unsupported length 0x%X
systemReady=%{public,signpost.description:attribute}d
%{public}s:%i %s: %s
%{public}s:%i [Tag 0x12] Unexpected data length: 0x%X
%{public}s:%i Cannot create SecTaskRef with XPC Connection: %{public}@
%{public}s:%i InterruptedHandler: ConnectionID=%lu
%{public}s:%i Invalid payload length; dropping message
system will sleep
%{public}s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@
%{public}s:%i Invalid payload encoding; dropping message
%{public}s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@
isLastPage=%{public,signpost.description:attribute}d
transceiveToI2c_write
%{public}s:%i String is of invalid length=%ld with 0x prefix
%{public}s:%i Failed to get entitlements: %{public}@
%{public}s:%i Underflow
[Hex dump: offset=%04X] %{public,stockholm:dataDump}.*P
%{public}s:%i Identifier string exceeds the maximum length, %{public}@
%{public}s:%i Incorrect length field
transceiveToI2c_write1SRAMPage
%{public}s:%i System not ready.  Abort
systemNotReady
%{public}s:%i opened assertion: counter: %lu id: %{public}@
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
%{public}s:%i \"%s\" errno=%d Failed to read data %ld/%ld
%{public}s:%i Returned %x
NFCardSessionConfig
NFResponseAPDU
NFLocation
NFCALogger
NSSecureCoding
NSObject
NFNdefRecordInternal
NFNdefRecord
NSCopying
NFTLV
NFTagA
NFHashes
NFVASPassConfig
NFMSEIParser
NFAccessoryTag
NFXPCConnectionUserInfoDictionary
NFPaymentTagReaderDeveloperPresentmentReport
NFAssertionInternal
NFAssertionInternalWrapper
NFCommandAPDU
NFCTKPollConfig
NFAssertionCALogger
NFPaymentTagReaderDeveloperPresentmentSessionData
NFExceptionsCALogger
HexString
NFWhitelistChecker
NFAccessoryTagI2CBridge
NFReaderSessionPollConfig
NFTagB
NFTagF
NFExtension
NFServiceWhitelistChecker
NFReaderModeCardIngestionCALogger
NFRunScriptParametersInternal
NFNdefMessage
NFReaderSessionConfig
NFPowerAssertion
NFTimer
NFPowerObserver
NFGeneralStatisticsCALogger
NFUserInfo
NFXPCEventPublisher
Comparison
NFTagInternal
NFTag
NFPreferenceObserver
Numeric
NFXPCServiceClient
NFLPCDStatisticsCALogger
NFCoreNFCPollConfig
NSCoding
NFNdefMessageInternal
NFNSCheckedDecoder
NTAG5Boost
_tag
countByEnumeratingWithState:objects:count:
postMiddlewareExceptionEvent:mwVersion:errorType:errorCode:breadcrumb:description:
startTimestamp
T@\"NSArray\",&,N,V_AIDAllowList
T@\"<NFAccessoryTagDelegate>\",W,N,V_delegate
_callback
_ndefMessageSize
_setupInitValuesForDeviceExceptionStatistic
nfcPaymentTagReaderDeveloperMode
technology
isSelectCommand
NF_clientName
ndefAvailability
toSystemOS
TB,N,V_selected
T@\"NSString\",R,V_country
_bridgeType0CreateAccessoryHeaderWithBuffer:pageLength:isLastPage:
_sessionConfig
applicationIdentifier
localDeviceCAParameters
radioToggle
TB,N,V_pace
_dontResetAssertion
setShortRecord:
date
selectTag
TB,N,V_fieldDetect
getAppInfoDictionary
pollConfigWithTechnology:
valueAsHexString
pollIDCardConfigWithTechnology:
_setSak:
_sleepMessageArgument
hasSuffix:
initSleepTimerWithCallback:queue:
publisher
characterIsMember:
isEqualToNumber:
streamName
T@\"NSString\",R,N,V_city
_delegates
initWithBytes:length:encoding:
restrictedMode
sessionTypeString:
_startTimestamp
numberWithUnsignedLong:
setSeid:
bgTagReadingAssertion
initWithLatitude:longitude:altitude:horizontalAccuracy:city:state:country:
atqa
scanCharactersFromSet:intoString:
updateGeneralDeviceStatistic:
T@\"NSString\",&,N,V_applicationIdentifier
TS,R,N,V_status
_radioToggle
valueAsString
TQ,N,V_type
_useUnfilteredApplets
NF_hasPrefix:
getCALoggerUserDefaults
objectsForKeys:notFoundMarker:
pace
seLoggingSessionAccess
setCallback:
pid
_teamIdentifier
_bridgeType0ReadMultipleSRAMPagesWithBuffer:
setDelegate:
NF_callbackUUID
TQ,N,V_pollingOption
_bucketizeOverCurrentCount:
_enableDebug
setIso7816SelectIdentifiers:
_initISO7816PermissibleAIDListWithSecTask:infoPlist:
postAnalyticsSetupEndpoints:totalUnknowntoSE:
T@\"NSString\",R,V_city
TC,R,N
_boolValueOfEntitlement:secTask:
decodeIntegerForKey:
initWithCallback:queue:
numberWithDouble:
initWithLength:
developmentPresentments
setDisableCompletionNotification:
historicalBytes
TQ,R,V_endTimestamp
addDeviceModeDimensionsToDictionary:
nfcCardSessionAccess
setStartOnLocationUpdate:
_publisher
characterAtIndex:
componentsSeparatedByString:
scannerWithString:
setReceivedInitialBarrier:
updateDailyTagStatistic:
weakObjectsHashTable
_seSessionAccess
postAnalyticsMobileSoftwareUpdateExceptionEvent:
teamID
T@\"NSNumber\",R,N
_country
decodeBoolForKey:
decodeUnderlyingAppletError:
sessionTypeForClass:
setRemoteObjectInterface:
teamIdentifier
zone
asData
remainingTime
state
updateAnalyticsGeneralTransactionStatistics:
IDm
asDictionary
count
encodeInt64:forKey:
messageEnd
p2
transactionCounter
_deactivateAllApps
init
initWithDictionary:
country
T@\"NSData\",R,C,N
_iso7816SelectIdentifiers
_setUID:
class
integerForKey:
TB,R,N,V_nfcHardwareRegistersAccess
_applicationIdentifier
_type0ReadConfigRange:data:
assertionTime
compare:options:range:
holdPowerAssertion:behaviourWhenSleepStarted:
pollConfigWithAppletIdentifiers:
pollingProfileUpdate
T@\"NSString\",R,N,V_state
_chAssertion
cardMigrationAccess
stringWithUTF8String:
_value
city
initWithObjectsAndKeys:
initWithType:
numberWithUnsignedLongLong:
T@\"NFTimer\",&,N,V_releaseTimer
nfcTagReaderPACEPollingAllow
postSessionMetricsEvent:sessionDurationMs:queueWaitMs:blockedBySessionType:hasError:
seid
TQ,R,N,V_uiMode
_singleUserAccess
setApplicationIdentifier:
timeIntervalSince1970
typeNameFormat
TB,R,N,V_bgTagReadingAssertion
_bridgeType0WritePollForSystemReadyWithTimeout:beforeWrite:outError:
_developmentPresentments
_vasMode
setType:
TB,N
_disableCompletionNotification
processIdentifier
setAIDAllowList:
sharedPowerAssertion
NF_clearFDPresentmentIntentSuppressionHolder
transceive:response:maxTimeout:
initWithData:encoding:
initWithReportId:timestampDay:bundleID:teamID:developmentPresentments:
setIdentifier:
TB,R,N,V_eCommerceAccess
_data
data
removeRestrictedMode
validateNFCCHashes:reference:expectedVersion:hashResults:
T@\"NSArray\",R,V_developmentPresentments
TB,R,N,V_nfcPaymentTagReaderDeveloperMode
allowBackgroundedSession
_deviceModeDefault
_isAIDStringValid:
appendExpectedLength:usingExtendedLength:toAPDU:
enumerateObjectsUsingBlock:
isEqualToDate:
isEqualToString:
roundToSignificantDigit:forValue:
_skipMifareClassify
postAnalyticsCRSDeAuthWithStatus:
setLpcd:
valueAsUnsignedLongLong
Td,R,V_altitude
_cardModeAccess
Tq,R,N,V_type
_seshatAccess
TQ,N,V_sessionConfig
TB,R,N,V_lpemConfigSessionAccess
_initialScanText
numberWithUnsignedChar:
T@\"NSString\",&,N,V_streamName
TI,R,N
decodeObjectOfClasses:forKey:
T@\"NSArray\",&,N,V_felicaSystemCodes
numberWithBool:
TB,N,V_startOnLocationUpdate
_atqa
decodeIntForKey:
lpmFactoryTest
trustedISO7816AidList
_internalAccess
T@\"NSData\",&,N
_supportsPACE
performSelector:withObject:
_setQueue:
_worseCaseSizeAsData
decodeInt32ForKey:
releasePowerAssertion:
_sak
removeAllObjects
simpleTLVsWithData:
start:
timeIntervalSinceDate:
validateISO15693TagAccessWithManufacturerCode:serialNumber:
isSecureMessaging
ndefMessageSize
_p1
_setSilentType:
T@\"NSString\",R,V_state
decodeFromRecord:
setRestrictedMode:
shortRecord
_type0ReadSRAM:numOfBlocks:data:
addObject:
_setSystemCode:
T@\"NSString\",R,N,V_country
_setHistoricalBytes:
dumpState
encodeBool:forKey:
tagF
TLVWithTag:value:
allSystemCodes
childrenWithTag:
localizedCaseInsensitiveContainsString:
setEnableDebug:
setFieldDetect:
callback
setStreamName:
_arrayValueOfEntitlement:secTask:
dictionaryWithObjects:forKeys:count:
isGetVasDataCommand
numberWithUnsignedInt:
postAnalyticsExpressSetupFailureEvent:context:error:
_reportId
_resetDailyTagStatisticToDefaults
_queue
value
_allSystemCodes
_uiMode
TLVsWithData:
_miniNVWriteAccess
decodeDoubleForKey:
isSelectByDFNameCommand
pollingOption
includeAPDUDuration
setTransactionCounter:
_resetGeneralDeviceStatisticToDefaults
boolForKey:
validateISO15693TagAccessWithManufacturerCode:
unregisterForEvents
_deviceAngleDegrees
_setSystemCodes:
_idm
_tagID
_validate
initWithUTF8String:
mutableBytes
simpleTLVsWithTag:fromData:
TB,R,N,V_remoteAdminAccess
Td,R,N,V_latitude
_iso15693TagAccessFilters
auditToken
powerObserverSystemHasPoweredOn:
NF_setCallbackUUID:
_setIDm:
isEqualToData:
postCASERestrictedModeExited:exitReason:
singleUserAccess
subdataWithRange:
_seLoggingSessionAccess
pollConfigWithTypeFSystemCode:
postAnalyticsContactlessErrorsEvent:status:error:
postGeneralDeviceStatistics
releasePowerAssertion:logFaultOnOverRelease:
setSessionConfig:
TB,R,N,V_ignoreAppStateMonitor
TC,N
_assertionTime
altitude
postAnalyticsGeneralTransactionStatistics
postAnalyticsSERestrictedModeEntered:
initialScanText
updateDeviceExceptionStatistic:
_AIDAllowList
_checkHash:againstReference:expectedVersion:matchingVersion:
_vasPasses
children
isMemberOfClass:
_assertion
postAnalyticsATLFailureEvent:aid:error:
resetCALoadStackExceptionCount
TB,R,N
_powerAssertTransaction
_writeToBridgeType0:fragmentationSupport:
_lpmFactoryTest
T@\"NSArray\",R,N
_firstOctet
holdPowerAssertion:onBehalfOf:behaviourWhenSleepStarted:
nfcNDEFReaderAccess
T@\"NSString\",R,C,N,V_passIdentifier
NF_numberForKey:
_exportedInterface
_stringValueOfEntitlement:secTask:
asMutableData
hceAccess
_teamID
_appData
_stringFromArray:
initWithService:remoteObjectInterface:exportedInterface:exportedObject:
postDailyTagStatistics
sessionID
setTypeFSystemCode:
bytes
setQueue:
T@\"NSData\",R,N
_children
_popTimeInSeconds
mutableCopy
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
TB,R,N,V_purpleTrustAccess
_type0ReadConfigReg:data:
_status
TLVsWithData:requireDefiniteEncoding:
TQ,R
_felicaSystemCodes
_workQueue
unsignedLongValue
dataFromRecord:
T@\"NSData\",&,N,V_tagUUID
_setAppData:
initWithConnection:coreNFCConnection:
performSelector:
TB,R,N,V_seSessionAccess
_bgTagReadingAssertion
_incrementMiddlewareExceptionCountWithReset:
_parseTLVs:end:simple:definite:
initWithStartTimestamp:endTimestamp:latitude:longitude:altitude:horizontalAccuracy:city:state:country:successfulTapCount:
initWithStreamName:queue:
setPollDuration:
surfSessionAccess
getHardwareTypeForCA:
AppData
characterSetWithCharactersInString:
initWithMachServiceName:options:
passConfigWithMode:passIdentifier:
releaseTimer
_ndefReaderAccess
coder:decodeArrayOfClass:forKey:
numberWithInteger:
TI,N,V_technology
_getSystemCodeListString
tagA
UTF8String
_xpcConnection
getDurationFrom:
chunked
TQ,R,V_successfulTapCount
_checkAIDAllowList
initWithBytes:length:
setPublisher:
_p2
generateUUID
postAnalyticsOsResetEvent:osID:hardwareType:
startTimer:
latitude
.cxx_destruct
TB,N,V_disableCompletionNotification
TLVSsWithBytes:length:requireDefiniteEncoding:
_delegate
_surfSessionAccess
Ti,N,V_transactionCounter
_pace
_setSupportsPACE:
appendString:
checkAIDAllowList
getTimestamp
TLVWithTag:unsignedShort:
_pollingOption
_successfulTapCount
delegate
standardUserDefaults
T@\"NSString\",R,N,V_clientName
addEntriesFromDictionary:
setTokens:
_releaseTimer
_tagUUID
modifyObjectForKey:handler:
recordsFromBytes:length:
numberWithInt:
pollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:
supportsPACE
nfcVASReaderAccess
timestampDay
NF_urlForKey:
performSelector:withObject:withObject:
postAnalyticsLPCDStatistic:
TB,R,N,V_radioToggle
_bridgeType0WriteOneSRAMPage:fragmentationSupport:isLastPage:
description
initWithNFTagForUIDOnly:
valueAsUnsignedLong
_lengthExpected
_pollingProfileUpdate
purpleTrustAccess
NF_stringForKey:
T@\"NSData\",&,N,V_ecp
_selectTagType0
_sfgi
decodeObjectOfClass:forKey:
parseRecordUsingScanner:header:type:identifier:payload:
setWithObjects:
_ndefContainerSize
_queryTypeFSystemCodes
encodeObject:forKey:
_endTimestamp
_initCoreNFCEntitlements:secTask:
_pollDuration
lastObject
objectAtIndex:
reportId
encodeInt32:forKey:
fileURLWithPath:isDirectory:
removeObject:
_tokens
T@\"NSArray\",&,N,V_iso7816SelectIdentifiers
tagUUID
_setNDEFContainerSize:
initWithSuiteName:
userInfo
records
TB,N,V_queryTypeFSystemCodes
_type0WriteSRAM:data:
isKindOfClass:
pupi
TI,N,V_pollDuration
assertionType
status
_setTechnology:
externalReaderAccessAllow
hash
initWithDelegate:
vasMode
boolValue
silentType
Tq,R,N,V_vasMode
handlePreferencesOrProfileChanged
typeFSystemCode
_ignoreAppStateMonitor
encodeWithCoder:
setDeactivateAllApps:
TB,R,N,V_useUnfilteredApplets
NF_serviceType
_readerInternalAccess
encodeInt:forKey:
TB,R
_eCommerceAccess
_longitude
_lpemConfigSessionAccess
length
getBytes:range:
resetConnection
getUUIDBytes:
resetConnectionWithId:
T@\"NSObject<OS_xpc_event_publisher>\",&,N,V_publisher
_nfcCardSessionAccess
_setSelectedAID:
getBatteryPercent
initWithData:uniformLengthCheck:
_idLengthPresent
_records
initWithDomain:code:userInfo:
initialUIText
parseResponseAPDU:
NF_fdPresentmentIntentSuppressionHolder
T@\"NSDate\",R,V_assertionTime
TLVWithData:
_willSleep
identifier
NF_clearCallbackUUID
T@\"NSString\",R,C,N
_clientCount
_setupInitValuesForGeneralTransactionStatistics
dontResetAssertion
horizontalAccuracy
isDevTestMode
selectedAID
seSessionAccess
_pendingSendEvents
arrayWithCapacity:
T@\"NSMutableSet\",&,N,V_tokens
T@\"NSArray\",R,C,N
_monotonic
_identifier
_sessionType
sessionConfig
_nfcTagReaderPACEPollingAllow
postAnalyticsHardwareFault:errorStatus:parityErrorCount:
NF_objectForKey:expectedClass:
delayConnectionHandoverRestart
appendBytes:length:
Td,R,N,V_altitude
_serviceWhitelist
array
bucketDeviceAngle:
postAnalyticsVASTransactionException:withSWStatus:
_streamName
instruction
messageBegin
initWithType:delegate:
isSilent
payloadLength
_passIdentifier
T@\"NSMutableArray\",&,N,V_pendingSendEvents
TLVWithTag:unsignedChar:
initWithServiceWhitelist:clientName:
postAnalyticsReaderModeExceptionForType:tagType:rfFrameInterface:withErrorCode:
T@\"<NFTagA>\",R,N
isProxy
T@\"NSString\",&,N,V_initialUIText
_assertionType
encodeInteger:forKey:
substringFromIndex:
numberWithUnsignedShort:
removeLastObject
setPace:
tagB
T@\"NSArray\",R,C,N,V_vasPasses
TB,N,V_enableDebug
_setNDEFAvailability:
_trustedISO7816AidList
bundleIdentifier
_iso15693ReaderAccess
_decodeTextRecord:
_latitude
enableDebug
Td,R,N
_nfcHardwareRegistersAccess
initWithService:remoteObjectInterface:exportedInterface:exportedObject:xpcDispatchQueue:
Td,R,N,V_longitude
_clientName
_powerNotificationPort
_type0WriteConfigReg:data:
_remoteAdminAccess
allowSleep
valueAsUnsignedShort
ecp
_pmm
setChunked:
NF_presentmentIntentSuppressionHolder
Td,R,N,V_horizontalAccuracy
appendFormat:
postAnalyticsHciTransactionException:eventType:commandResult:status:
TB,N,V_isDevTestMode
_technology
didInterrupt:connectionID:
internalAccess
postHardwareExceptionEventWithAssertionCounter:hardwareType:firmwareVersion:wdogDump:hwFltDump:wdgTickInfo:assertionData:
_initTagSpecifier:maximumFilterStringLength:
appendData:
decodeInt64ForKey:
postDeviceExceptionStatisticsDim
readFromBridge:fragmentationSupport:response:
retain
scanHexInt:
_createAccessDictionaryFromICCode:serialNumber:maximumFilterStringLength:
addObjectsFromArray:
pendingSendEvents
_nfcCardSessionAIDPrefixList
deactivateAllApps
remoteAdminAccess
_clientProcessIdentifier
pollDuration
TB,R,N,V_seLoggingSessionAccess
TLVWithTag:unsignedLongValue:
_historicalBytes
buildAPDUHeaderWithClass:instruction:p1:p2:len:useExtendedLength:
isEqualToNFTag:
SystemCode
TB,R,N,V_readerInternalAccess
getConnectionAndID:
stringByTrimmingCharactersInSet:
substringWithRange:
Ti,R,V_pid
conformsToProtocol:
unsignedIntValue
useUnfilteredApplets
T@\"NSString\",&,N,V_seid
eCommerceAccess
TB,R,N,V_cardMigrationAccess
_fieldDetect
unsignedLongLongValue
cardModeAccess
TB,N,V_includeAPDUDuration
_appletIdentifiers
_intToData:
isSendCertificateCommand
chAssertion
payloadBytes
recordsWithTNF:type:identifier:payload:chunkSize:outError:
setExportedInterface:
TB,N,V_receivedInitialBarrier
TB,R,N,V_miniNVWriteAccess
postCAEventFor:eventInput:
TQ,R,V_assertionType
code
dataWithBytes:length:
processInfo
setAssertion:
setPayload:
vasPasses
NF_whitelistChecker
_typeFSystemCode
applicationDataCoding
ndefContainerSize
_powerNotificationNotifier
setSkipMifareClassify:
T@\"NSString\",R,N
_src
NF_arrayForKey:
Td,R,V_latitude
TB,R,N,V_dontResetAssertion
_initialUIText
doubleValue
initWithCoder:
setInvalidationHandler:
TB,R,N,V_pollingProfileUpdate
copy
registerForEvents
NF_setPresentmentIntentSuppressionHolder
bundleID
didInvalidate:
queryTypeFSystemCodes
setIsDevTestMode:
initWithFormat:
_stringFromISO15693AccessFilterList
TB,N,V_checkAIDAllowList
TLVWithTag:fromData:
_initISO15693TagSpecifier:
assertion
setInitialUIText:
PMm
_ndefAvailability
_setAtqa:
_xpcConnectionID
UUIDString
assertionHolders
lpcd
stopTimer
T@\"NSData\",R,N,V_data
_type0GetSystemInfo:
supportsSecureCoding
initWithData:
retainCount
tokens
updateDeviceAngle:modeDefault:
uppercaseString
_lpcd
_payload
_seid
removeDelegate:
_horizontalAccuracy
dataFromNDEFMessage:
numberWithUnsignedInteger:
seshatAccess
setCheckAIDAllowList:
_cardMigrationAccess
_city
removeObjectForKey:
NF_dataWithHexString:
_powerNotificationMessage:argument:
_setIdLengthPresent:
response
sessionTimeLimit
setValue:forKey:
sfgt
TB,N,V_initialSelectBeforeRun
T@?,C,V_callback
clientName
substringToIndex:
T@\"NSString\",R,V_bundleID
_readerPurposeString
sfgi
TB,R,N,V_delayConnectionHandoverRestart
Td,R,V_longitude
_assertionHolders
_decodeTextRecordLanguage:
decode
intValue
self
setTagUUID:
_setType:
setAppletIdentifiers:
setObject:forKeyedSubscript:
superclass
_transactionCounter
responseWithData:
TB,R,N,V_chAssertion
decodeFromNDEFMessage:
TB,R,N,V_internalAccess
TB,R,V_willSleep
TQ,R,N
queue
sendXpcNotificationEventWithDictionary:
setObject:forKey:
T@\"NSOrderedSet\",R,&,N
tag
T@\"NFAssertionInternal\",&,N,V_assertion
TB,R,N,V_lpmFactoryTest
_nfcPaymentTagReaderDeveloperMode
initWithCapacity:
nfcCardSessionAIDPrefixList
postPlasticCardEnableStatus:aid:
nfcTagReaderAccess
readerPurposeString
stringForKey:
TB,N,V_toSystemOS
initWithNDEFRecord:
readerInternalAccess
addRecord:
dictionary
setTechnology:
startOnLocationUpdate
T@\"<NFTagF>\",R,N
getMiddlewareExceptionCount
NF_userInfo
TQ,R,V_startTimestamp
_decodeURIRecord:
_setSFGI:
caseInsensitiveCompare:
setIncludeAPDUDuration:
now
_state
validateNFCCHashes:reference:expectedVersion:
T@\"NSString\",R,C,N,V_initialScanText
TQ,R,N,V_sessionType
felicaSystemCodes
setQueryTypeFSystemCodes:
T@\"NSOrderedSet\",R,N
generateDailyUUIDForCA
_startOnLocationUpdate
tagID
UID
postAnalyticsDefaultAppSupression:prepOnly:
setFelicaSystemCodes:
_exportedObject
lpemConfigSessionAccess
_powerNotificationConnection
initWithConnection:
TB,R,N,V_seCredentialManagerAccess
setHeader:
setInterruptionHandler:
setPendingSendEvents:
isEqual:
sessionType
NF_toUint64:
TB,N,V_lpcd
_copyValueOfEntitlement:secTask:
_delayConnectionHandoverRestart
_setIdentifier:
TB,R,N,V_cardModeAccess
TB,R,N,V_nfcTagReaderPACEPollingAllow
TB,R,N,V_singleUserAccess
_includeAPDUDuration
postAnalyticsTSMConnectivityException:
setPollingOption:
TB,R,N,V_surfSessionAccess
_class
_initCardSessionEntitlementsWithSecTask:
nfcHardwareRegistersAccess
applicationData
appletIdentifiers
initWithAppletIdentifiers:
invalidateConnection
sendXpcNotificationEvent:
TB,N,V_skipMifareClassify
_allowBackgroundedSession
_initialSelectBeforeRun
initWithNDEFMessage:
processName
TQ,R,V_timestampDay
hasPrefix:
objectAtIndexedSubscript:
NF_dataForKey:
coder:decodeDictOfClass:forKey:
isEqualToArray:
TB,R,N,V_allowBackgroundedSession
type
_purpleTrustAccess
_remoteObjectInterface
_selected
configWithInitialUIText:
sendXpcNotificationEventWithString:
whitespaceAndNewlineCharacterSet
T@\"NSNumber\",&,N,V_typeFSystemCode
sak
T@\"<NFTagB>\",R,N
UUID
allocWithZone:
ignoreAppStateMonitor
initWithArray:
NF_clearPresentmentIntentSuppressionHolder
addRecordArray:
T@\"NSString\",R,C
debugDescription
resume
startTimer:leeway:
AIDAllowList
T@\"NFServiceWhitelistChecker\",R,N,V_serviceWhitelist
member:
T@\"NSUUID\",R,V_reportId
clss
endTimestamp
uiMode
NF_isPrefixOfHexEncodedEqualToBytes:length:
setEcp:
_isDevTestMode
objectForKeyedSubscript:
seCredentialManagerAccess
_instruction
_readFromBridgeType0:fragmentationSupport:
_xpcQueue
childWithTag:
invalidate
isURIRecord
setMessageBegin:
serviceWhitelist
_setNDEFMessageSize:
encodeDouble:forKey:
objectForKey:
setToSystemOS:
unsignedIntegerValue
_dataLock
_silentType
initWithHeader:type:identifier:payload:
initWithObjects:
p1
pollConfigWithOption:sessionConfig:
postAnalyticsCRSAuthInitEventWithStatus:
addDelegate:
disableCompletionNotification
initialSelectBeforeRun
iso7816SelectIdentifiers
setInitialSelectBeforeRun:
T@\"NSString\",R,V_teamID
payload
T@\"NSString\",R,&,N,V_readerPurposeString
receivedInitialBarrier
NF_setFDPresentmentIntentSuppressionHolder
sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:startOnLocationUpdate:isDevTestMode:
TB,N,V_deactivateAllApps
isGetMoreVasDataCommand
postAnalyticsCRSAuthWithStatus:withMethod:
postAnalyticsReaderModeCardIngestionSession:prepOnly:
selected
validateISO15693TagAcesssWithUID:
longitude
T@\"NSString\",?,R,C
initWithString:
Td,R,V_horizontalAccuracy
Tr*,R,N
_receivedInitialBarrier
coder:decodeArrayOfArrayOfClass:forKey:
postAnalyticsSERemovedEvent:hasExpressTransactionStarted:hasCardEmulationStarted:hardwareType:
setExportedObject:
release
sharedCALogger
stop
NF_asHexString
T@\"NSArray\",&,N,V_appletIdentifiers
postAnalyticsSEFailureEvent:context:error:
handleEventWithAction:token:descriptor:
jsonDictionary
respondsToSelector:
stringWithFormat:
_bridgeType0WritePollForCompletionWithTimeout:
_ecp
integerValue
writeToBridge:fragmentationSupport:response:
TB,R,N,V_seshatAccess
TLVWithTag:children:
_payloadRange
_type
miniNVWriteAccess
_customDescription
_decodeTextRecordText:
initWithUUIDString:
postAnalyticsAppletProvisioningFailureEvent:responseCode:
getCAUniversityCode:universityCodes:
nfcISO15693ReaderAccess
setMessageEnd:
_altitude
_pid
_setPMm:
_vasReaderAccess
_toSystemOS
autorelease
copyWithZone:
enumerateKeysAndObjectsUsingBlock:
initWithNFTag:
lengthExpected
setReleaseTimer:
TB,R,N,V_hceAccess
_serviceName
header
setTypeNameFormat:
URLByDeletingLastPathComponent
_timestampDay
passIdentifier
setString:
T#,R
_tagReaderAccess
_uid
skipMifareClassify
willSleep
NF_dictionaryForKey:
NF_isZeroed
_hceAccess
fieldDetect
powerObserverSystemWillSleep:
dealloc
_bundleID
postAnalyticsCRSAuthECommerceWithParameters:
postAnalyticsSERestrictedModeExited:exitReason:
setSelected:
successfulTapCount
T@\"NSString\",R,N,V_teamIdentifier
_seCredentialManagerAccess
@32@0:8@?16@24
B24@0:8@\"<NFTag>\"16
I32@0:8Q16@24
B16@0:8
v48@0:8I16I20I24I28Q32@40
#16@0:8
I
@32@0:8C16C20^@24
@\"<NFTagF>\"16@0:8
v36@0:8I16Q20@28
v20@0:8S16
v20@0:8I16
v28@0:8B16@20
S
@16@0:8
v24@0:8@16
@48@0:8Q16Q24@32@40
@32@0:8Q16Q24
v24@0:8I16I20
@24@0:8@\"NSCoder\"16
i
@32@0:8q16@24
v32@0:8I16I20B24I28
B56@0:8^{_NFDataScanner=^{_NFData}Q^v}16*24^@32^@40^@48
@60@0:8C16@20@28@36Q44^I52
{_NSRange=\"location\"Q\"length\"Q}
B28@0:8@16I24
@\"NFServiceWhitelistChecker\"
@24@0:8^Q16
B48@0:8@16@24@32@40
v48@0:8@16@24@32@40
B36@0:8d16B24^@28
v28@0:8@16B24
^{IONotificationPort=}
@?
B32@0:8@16^{__SecTask=}24
@\"NSHashTable\"
@24@0:8@\"NSData\"16
v24@0:8@\"NSData\"16
@\"NSData\"
B24@0:8:16
@\"NSString\"16@0:8
@60@0:8Q16Q24@32@40B48B52B56
@28@0:8I16@20
v24@0:8@\"NSCoder\"16
v52@0:8Q16Q24Q32Q40B48
v32@0:8@16Q24
v20@0:8B16
v28@0:8I16I20I24
r*16@0:8
@\"NSObject<OS_os_transaction>\"
Q
d16@0:8
v28@0:8I16^v20
@32@0:8@16^{__SecTask=}24
v16@0:8
B20@0:8B16
v32@0:8I16B20B24I28
@24@0:8:16
C
@32@0:8@16@24
@40@0:8@16@24@32
^{_NSZone=}16@0:8
v20@0:8i16
@24@0:8I16C20
S24@0:8^@16
@24@0:8@\"<NFTag>\"16
AB
v24@0:8I16S20
B32@0:8r*16Q24
@\"NSDate\"
@\"<NFTagB>\"16@0:8
@32@0:8@16#24
@72@0:8d16d24d32d40@48@56@64
v32@0:8@16^I24
B
@\"NSObject<OS_xpc_event_publisher>\"
@44@0:8C16@20@28@36
@32@0:8:16@24
@\"NSMutableDictionary\"
@\"NSString\"
@\"NFAssertionInternal\"
@36@0:8@16B24^@28
@24@0:8I16I20
^v
v32@0:8^{__SecTask=}16@24
@28@0:8@16B24
@?16@0:8
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@\"NSArray\"16@0:8
I24@0:8@16
@24@0:8I16S20
S16@0:8
@32@0:8@16B24B28
v32@0:8d16d24
@\"NSXPCInterface\"
@24@0:8@\"<NFNdefRecord>\"16
@32@0:8r*16Q24
@36@0:8r^v16Q24B32
@28@0:8^@16B24
^v32@0:8@16^{__SecTask=}24
v32@0:8@16@24
I24@0:8Q16
@\"NSArray\"
@\"NSMutableArray\"
B24@0:8@\"Protocol\"16
@\"NSData\"16@0:8
v28@0:8q16B24
Q32@0:8Q16Q24
v24@0:8S16S20
@24@0:8^@16
B24@0:8#16
@
@96@0:8Q16Q24d32d40d48d56@64@72@80Q88
I20@0:8I16
B24@0:8@16
v32@0:8S16S20@24
v20@0:8C16
@40@0:8r^*16r*24B32B36
@28@0:8C16@20
@56@0:8@16Q24@32@40@48
Q16@0:8
@24@0:8@16
@20@0:8I16
@24@0:8d16
v24@0:8d16
d
v32@0:8@16@?24
v32@0:8@16^{__SecTask=}24
@40@0:8:16@24@32
@48@0:8@16@24@32@40
q24@0:8q16
@24@0:8Q16
v36@0:8@16Q24B32
B32@0:8@16i24I28
v24@0:8@?16
v24@0:8^{__SecTask=}16
v60@0:8I16I20I24^I28^I36^I44@52
v24@0:8@\"NSArray\"16
q
@40@0:8{_NSRange=QQ}16^@32
@56@0:8@16@24@32@40@48
v24@0:8Q16
v36@0:8S16@20@28
@24@0:8@\"<NFNdefMessage>\"16
@24@0:8^{_NSZone=}16
@28@0:8C16^@20
@\"<NFPowerObserverDelegate>\"
@40@0:8@16@24Q32
@\"NSMutableOrderedSet\"
@\"NSObject<OS_dispatch_queue>\"
@32@0:8S16B20@24
@\"<NFTagA>\"16@0:8
Q24@0:8^@16
I16@0:8
@40@0:8C16C20C24C28I32B36
@\"<NFAccessoryTagDelegate>\"
@\"NSMutableSet\"
@28@0:8r^v16I24
v24@0:8@\"<NFNdefRecord>\"16
@\"NFTimer\"
@40@0:8@16#24@32
@\"NSNumber\"
@\"NSXPCConnection\"
@\"NSUUID\"
Ai
i16@0:8
q16@0:8
@\"NSObject<OS_dispatch_source>\"
Q24@0:8#16
v24@0:8S16I20
Vv16@0:8
C16@0:8
```
