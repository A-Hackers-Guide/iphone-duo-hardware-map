# `/usr/lib/updaters/libSEUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,120,192 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 33 (Size: 4568)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (15)

- `/usr/lib/updaters/libSEUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/NearField.framework/NearField (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libnfrestore.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (8 classes, 2 protocols)

Classes: `APDUUtil`, `AlohaPairingController`, `AlohaPairingVerifier`, `BAADelegateImpl`, `NSData`, `NSMutableData`, `NSString`, `SETransceiveHelper`

Protocols: `BAASupportDelegate`, `NSObject`

## Strings (1,594)

```
CXX
AlohaPairingController
FDR
APDUUtil
BAADelegateImpl
BAASupportDelegate
NSObject
AlohaPairingVerifier
Append
HexString
DER
SETransceiveHelper
UTF8String
_debugRecordPath
debugDescription
enumerateObjectsUsingBlock:
getBlessedUser:keybagUUID:
injectSEPKtoSSE_Debug:
T@\"NSMutableArray\",&,N,V_rapduRecord
dataWithCapacity:
performSelector:
setConnectionProxyDictionary:
setState:
isProxy
boolValue
numberWithUnsignedInt:
asCXXVector
dataWithPropertyList:format:options:error:
getBytes:length:
selectWithAID:
stringWithCXXString:
performSelector:withObject:
setSeid:
TQ,R
fSeController
retainCount
T@\"NSString\",?,R,C
performSelector:withObject:withObject:
dataWithBytes:length:
secureElements
getValue:
numberWithLongLong:
crsSetSharingResult:signature:error:
setDebugRecordPath:
superclass
DERItem
_ecid
asHexString
isMemberOfClass:
.cxx_destruct
T@\"NSMutableArray\",&,N,V_alohaPlistRecord
dataWithCXXVector:
getSigKeyCertificates:certificates:
numberWithUnsignedLong:
copyDeviceType:
TQ,N,V_state
_alohaHostname
T{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}},N,V_fSeController
copySeid:
sharedHardwareManager
stringWithCapacity:
subdataWithRange:
processInfo
sessionWithConfiguration:
setRapduRecord:
appendU32BE:
dictionaryWithObjects:forKeys:count:
fullServerSessionID
manifestQuery
numberWithInt:
transceiveAndRecordCapdu:rapdu:
appendFormat:
appendU8:
count
setUseReverseProxy:
performAlohaVerification
unsignedIntValue
T@\"NSMutableArray\",&,N,V_capduRecord
alohaHostname
statusCode
class
copyA9Parameters:
dataWithData:
getHwSupport
hash
integerValue
T@\"NSData\",&,N,V_seid
copySESignature:hsmChallengeSE:ecid:outError:
array
conformsToProtocol:
getSharingRequestWithSignature:withError:
initWithOptions:seController:
recordApdu:toRecord:
asCXXString
dataWithHexString:
objectAtIndexedSubscript:
createFileAtPath:contents:attributes:
mutableBytes
setAlohaHostname:
setApChipId:
setFullServerSessionID:
useReverseProxy
dataWithContentsOfFile:
performAuthKeySharingWithAppleSSE:sharingRequest:requestSignature:resultSignature:withError:
T@\"NSNumber\",&,N,V_alohaVersion
arrayWithObjects:count:
initWithSEController:
transceiver
alohaVersion
dataUsingEncoding:
invalidate
stringWithCString:encoding:
stringWithFormat:
T@\"NSDictionary\",&,N,V_reverseProxySettings
description
isEqualToNumber:
retain
setAuthRandom:mac:error:
rapduRecord
appendBytes:length:
appendU32LE:
_alohaServerIP
stringByAppendingString:
_rapduRecord
getCXXApduWithCla:ins:p1:p2:payload:
isEqualToString:
setValue:forHTTPHeaderField:
dealloc
_serverSessionID
addObject:
bytes
isInternal
state
_state
beginPair:
getSigKeyExpDate:expirationDate:
objectForKeyedSubscript:
propertyListWithData:options:format:error:
setObject:forKeyedSubscript:
uppercaseString
_reverseProxySettings
appendU16BE:
info
setAlohaPlistRecord:
setTransceiver:
alohaPlistRecord
dataWithBytesNoCopy:length:freeWhenDone:
initWithController:options:
setDelegate:
setSigKey:expirationDate:keyData:certificates:
componentsSeparatedByString:
copyCasdCert:
performAlohaPairing
writeRecord:fileExtension:
URLWithString:
_transceiver
confirmSigKey:status:
countByEnumeratingWithState:objects:count:
getReverseProxySettings:outError:
generateSigKey:keyData:attestation:pubKey:
isKindOfClass:
setFSeController:
TB,N,V_useReverseProxy
copy
requestWithURL:cachePolicy:timeoutInterval:
T@\"NSString\",&,N,V_alohaHostname
base64Encoding
T@\"NSString\",&,N,V_fullServerSessionID
personalisable
T@\"NSString\",&,N,V_debugRecordPath
_alohaVersion
initWithFormat:arguments:
crsGetSharingRequestWithError:
errorWithDomain:code:userInfo:
numberWithUnsignedInteger:
processName
resume
debugRecordPath
_apChipId
_fullServerSessionID
defaultSessionConfiguration
processEndPair:
queryHardwareSupport:
setEcid:
T@\"NSString\",&,N,V_serverSessionID
stringByAppendingPathComponent:
dataTaskWithRequest:completionHandler:
ecid
getAPDUWithCla:ins:p1:p2:payload:
serverSessionID
_restoreEnvironment
capduRecord
reverseProxySettings
setValue:forKey:
writeToFile:options:error:
_alohaPlistRecord
T@\"NSString\",R,C
respondsToSelector:
setServerSessionID:
apChipId
setHTTPMethod:
injectSEPKtoSSE:
seid
setHTTPBody:
_seid
numberWithInteger:
performHTTPRequestWithRequestDict:outError:
appendU64LE:
length
verifyAndRetrieveServerSessionId:
zone
self
release
T#,R
appendData:
defaultManager
isEqual:
_fSeController
getSEPK:andSEID:deleteExisting:error:
prepareLazily
numberWithBool:
stringByAppendingPathExtension:
_options
processApduReqPayload:outError:
dataWithDERItem:
init
setReverseProxySettings:
containsObject:
issueNewCertificate
mutableCopy
submitPairingRecord:
T@\"NSNumber\",&,N,V_apChipId
T@\"SETransceiveHelper\",&,N,V_transceiver
_capduRecord
appendU16LE:
injectSEPKtoSSE_FDR:
setAlohaVersion:
T@\"NSNumber\",&,N,V_ecid
appendU64BE:
dataWithLength:
addObjectsFromArray:
processAuthReqPayload:outError:
_useReverseProxy
autorelease
stringValue
setCapduRecord:
.cxx_construct
v32@0:8@16@24
i44@0:8I16Q20@28@36
i28@0:8I16^@20
i24@0:8I16i20
B24@0:8@\"Protocol\"16
@40@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16r^v32
B24@0:8^@16
v32@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16
@\"NSString\"
i44@0:8I16^@20^@28^@36
v20@0:8I16
v48@0:8{Apdu=^^?{shared_ptr<std::vector<unsigned char>>=^v^{__shared_weak_count}}}16@40
{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16@0:8
@\"NSMutableArray\"
@40@0:8:16@24@32
@32@0:8^v16^v24
@40@0:8r^v16{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}24
v16@0:8
@32@0:8^@16^@24
@24@0:8@16
B24@0:8@16
B24@0:8:16
@24@0:8r^{?=*Q}16
Q
@\"NSString\"16@0:8
i16@0:8
@24@0:8^@16
v20@0:8B16
@\"NSData\"
#16@0:8
@24@0:8:16
Vv16@0:8
^{_NSZone=}16@0:8
r^v
q24@0:8^@16
@\"SETransceiveHelper\"
v20@0:8C16
{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}16@0:8
@\"NSDictionary\"
@40@0:8C16C20C24C28@32
{CApdu=^^?{shared_ptr<std::vector<unsigned char>>=^v^{__shared_weak_count}}^{?}*QQ}40@0:8C16C20C24C28@32
@32@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16
@32@0:8@16^@24
@\"NSNumber\"
{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8
v24@0:8@16
@32@0:8:16@24
@24@0:8r^v16
B40@0:8@16@24^@32
B44@0:8^@16^@24B32^@36
B16@0:8
i32@0:8^I16[16C]24
i44@0:8I16Q20@\"NSData\"28@\"NSArray\"36
v24@0:8Q16
@16@0:8
@56@0:8@16@24@32^@40^@48
v20@0:8S16
{?=*Q}16@0:8
@48@0:8@16@24@32^@40
Q16@0:8
{shared_ptr<SEUpdater::P73BaseSEController>=\"__ptr_\"^{P73BaseSEController}\"__cntrl_\"^{__shared_weak_count}}
i28@0:8I16^Q20
B24@0:8#16
B
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
isEntitledForBAA(): entitled = %u
%s
fSource
DF21
Failed to transceive code = %d
logSink
Successfully deleted terminated PTC\n
Fail to get SEID from the request
Unexpected top level tag 0x%X expected 0x%X\n
-[AlohaPairingController beginPair:]
Setting debugArgs (empty): %s\n
%02x
fRequestDict
Failed to parse DStatusContainerDataItem
singleStep
ProductionUpdatePayloadHash
Performed sharing with SEID %@\n
Failed to get nonce from manifest
Bad length for JCOP1 primary attack log indicator\n
WriteEvent
X-Apple-Aloha-IP
fSeHandle == nullptr
SN300V detected based on manifest query response\n
ConfigureOSUReserves
Skipping MP <%s> because module not on SE\n
Can't get weakly linked NFHM class, nothing to personalize\n
failed to CFDataCreate for manifest data
Wrong SEPK + SEID size %zu\n
SE310S detected based on manifest query response\n
getSEHealthCheckResult
Dumping AC Log\n
BeeConnexions update required: %s\n
Could not get memory info, skipping indices check\n
The csnMap of platform %d is empty. Skip the config item\n
Failed to select ISD
sendApdus
Returning outError:\n
EVENT LOGGING: debugLogPath not present\n
While terminating
DeviceClass
Encountered error when retrieving seDeviceTypeData from %@\n
SEUpdaterExecCommand
keyData
Failed to copy SEID
-- GET DATA AVAILABLE MEMORY -- \n
validate
40D0_Enable_WithFilters_SW_ISO_Type
Wrong type for kRoseTagMeasurementSwBinDsp1
Error encountered when getting OBKG %@\n
Unexpected state encountered %lu\n
{ 
SLAMMigrateNeon_YK300R107
InstallSEAppletTool
SE,RapRTKitOS
DebugLogPath
ErrorMessage
confirmSigKey
 failed for '
Missing kRoseTagDigest in kRoseTagMeasurementSwBinDsp1
expectedBSN
fail to get Data
Warning APDU: %s idx %d replaying %d
AlohaPairingVerified invalidated\n
SN210V (Ceres)
Skipping SE Updater due to enrolled Seshat\n
KUD is set (0x%x), can proceed\n
SLAMDeleteSilverBullet
Davenport Delete
len <= bytes->size()
BeeConnexions package not found (SW=0x%04X)\n
SLAMDeleteXenon
SLAMSlalomMigration_14_5_0
AlohaPairingController deallocating\n
SCRT
SecTaskCopyValueForEntitlement
DEBUG
Fail to Img4EncodeItemEnd
Seshat get data response is 0x%zx bytes, expected 0x%lx or 0x%lx
Copernicus + Sunsprite SLAM
simDetectHIZ
PerformSLAMMigrations
,
CFDataGetLength(seid) <= sizeof(inData->data.seid)
UOS1_ERROR
isFPRequired
SLAMLoadAndInstallReaderSIOPackage
Digest
getDataSize
Fail to add sedh
IM4M_validated
UNK_IM4_STATE
_CFDictionarySetInteger32
}: 
Failed to query Seshat KUD status, pass forceUpdate if you really know what you are doing and want to skip it\n
SEPEffectiveProductionMode
 (OSU Key ID: 0x
Fail to add seph
generateSigKey
Unexpected CPLC data top level tag %llu
Verify options:\n
Select PT: SW1 0x%x SW2 0x%x SW3 0x%x\n
libDERErrorDomain
Wrong type for kRoseTagMeasurementRTKitOS
UOS2_ERROR
Skipping SE update due to missing update path coming from CrystalSU\n
SLAMLoadAndInstallHelium_v1021_ESE18
index>=0 && index<fObjs.size()
Pairing ended without error\n
libNfRestoreErrorDomain
userID
sizeof(CApduHeader_t) >= bytes->size()
size of factoryPostflightState or cometRootKeyId doesn't match
Im4_error
SN300V2 (Eos v2)
Failed to SLAMInstallPTCInstances due to %s, retrying...
PRP timed out %d\n
Passing fdrOptions with ApTicket of length %lu
Failed to parse updateProperties as per UpdatePropertiesItemSpec.
Skip Oasis install: JCOP version low.\n
Bad length for context
Oasis Config ID not matching or missing, needs reconfiguration\n
getSigKeyExpDate
len < bytes->size()
This process may take a long time (~16 min)\n
installSunspriteLogger
Failed to parse CRS get perso state response\n
Delete Oasis
SLAMDESFireMigration_1_0_23
Invalid listKeys output %@\n
Cannot proceed in SC state
injectSEPKtoSSE
CheckAndInstallOasisUnifiedReader
Failed to parse device data, manifest query: %s\n
tmpNum
*outDataSignatureLength is 0
-[SETransceiveHelper copyCasdCert:]
A0000001515350414141504C
kern.bootargs
AMFDRSealingMapCopyLocalData
AlohaVersion
No updater context hint, defaulting to limited environment\n
certSize <= (end - pos)
size >= sizeof(outData->data)
4216_I2CA_FrameLog_Enable_Debug
-[AlohaPairingController invalidate]
Invalid input
activated
40D0_Enable_WithFilters_SW
Failed to add rbdd
IMPORT_REQUIRED
SN300V3 (Eos v3)
SLAMLoadAndInstallSEAppletTool_0_0_2
MIFARE DESFire SLAM
splitDERSeq
 { 
Failed to parse forceDeviceHwVersion debug argument
SERS
Unable to retrieve seDeviceType with error %@\n
payload == &((*bytes)[sizeof(CApduHeader_t)])
Receiving R-APDU %d: %zu\n
Install SunspriteLogger: %s\n
At Configure OSU Reserve
PTC key deleted with error %@\n
SE,BLFWKeysIdentifier
DebugArgs
Proxy Unavailable\n
GetChipId
doRestrictedMode
\n
Fail to create dictionary for request
SLAMDeletePioneer
ApBoardId
Project version%s: %s\n
No RestoreOptions dictionary? Defaulting to limited environment\n
Wrong UpdateTable entries
Failed to parse attack log output\n
Oasis Config ID: %s\n
SLAMSlalomMigration_14_3_0
getDataFromDict
Checking for Bee Connexions and Executable Load File Version Number\n
BeginPair
ServerA9CertSN
%s : 0x%x
outData->data.macSize <= (end - pos)
YES
Fail to create dictionary for request image properties
deletePTCKeysWithNoStoredPK
CF=(
SessionId
InternalBuild
Unknown ChipId: 0x%x for platform category mapping. Macro HELSINKI_HIDE_NEW_HW: %s
dumpDebugInfo
Failed again to SLAMInstallPTCInstances due to %s, terminating.
KeyID %s is not localCA!
Unable to EnableTestSEContext %d
SE in restricted mode\n
Skip LoadAndInstallSEAppletTool by key\n
signInternal
Transceive
4108_DisableInFPM_DisableLogging
size of MQRD doesn't match
Missing element in updateTableEnry
P73 detected based on manifest query response\n
SLAMConfigureOSUReserves
Stinger version 0x%04X is lower than expected 0x%04X\n
Available indices in index table: %u, Total indices in index table: %u, Max indices in JCOP: %u, Total available indices in JCOP: %u\n
retAuthRandom
  request    %@\n
fOutput
No PTA loaded on device, skipping delete operation\n
Could not get Stinger version: SW=0x%X, size=%zu\n
Command
pos
Failed to select seshat with ret: %d and sw: %x\n
Failed to kill all slots with ret: %d and sw: %x\n
doCommand_block_invoke
getMinCSNForTrain
Error encountered when copying SEID %@\n
Encountered error when talking to server %@\n
SN200V detected based on manifest query response\n
SN300V3 detected based on manifest query response\n
DERParseSequence
SIMDetectGPIO_4143
Bad length for secondary attack log indicator\n
err == 0 
) 
dataToSign && dataToSignLength
seDeviceType does not support A9\n
SOCSecurityMode
MGGetBoolAnswer
No update table entry match found.
Pioneer Delete
DevelopmentUpdatePayloadHash
/System/Library/Frameworks/Security.framework/Security
getAlohaVerificationOptions
IM4P_Resent
} 
Details: 
SE Health check result: %s\n
skipAppletCleanup
Skipping cleanup script <%s, %s> because of no erase install\n
getAlohaPairingOptions
  SEID: %@\n
Pairing options:\n
SLAMDeleteSEAppletTool
Failed to run script %s. %s
SE,RapSwBinDsp
Missing SE,ChipID in request dictionary
 with option 
HSMChallengeSE
Failed to add sesa
SERestoreInfoHelpers.hpp
entry.data && entry.length
-[SETransceiveHelper dealloc]
Error encountered when selecting Star SD %@\n
retSharingResult
No Neon Package loaded on device, skipping delete operation\n
Failed to select the ISD
Skip configuring %s with option %s: already configured.\n
Failed to verify the configuration update of 
SetP2
Failed to select CRS 0x%X\n
Successfully deleted Neon Applet YK300R106 with AID: %s\n
PID  INFO %s, version  INFO 0x%04llX\n
While parsing the respons from SLAM state
fstat()
basic_string
  --> wouldDowngrade %d\n
Failed to retrieve SEPK %d 0x%hx\n
********************************************************************************\n
GetAvailableMemory
Resetting due to 0x%hx
Successfully loaded and installed Sunsprite Logger\n
EVENT LOGGING: Unable to recreate full file name with path\n
retAttestation
Assertion: 
Failed to send manifest query
factory_postflight
 overwrite: 0x
, 
Failed to set AR %d 0x%hx\n
'
preflight
Skip DeleteSEAppletTool by key\n
Error encountered when parsing IMG4Blob %d\n
Pairing selected: %d\n
Failure
SEUpdaterErrorDomain
parseArgs
Fail to parse MQR.data
0x
Cannot init sequence for ImageBinary.apdus
Update was going to proceed but bailing out due to forceDeviceHwVersion debug arg; don't want to brick SEs
NfRestoreSETransceive returns %d
Error encountered when forming request body %@\n
wrong sessionID received %@, expected %@\n
Successfully dumped SE NVM to %s\n
All instances found for %s\n
  sePk: %@\n
Failed to query hardware version\n
Failed APDU # %ld during attempt # %d; replaying from scratch\n
Successfully set AR\n
service
Resuming interrupted script 0x%llx
Fail to NfRestoreSETransceive
encodeSequence
Failed to decode top level 7F21 dr %d\n
setEraseInstall
A000000704C0000000000001
Error encountered when getting cert SN %@\n
capdu
%s/%d : %s
map::at:  key not found
4217_I2CB_FrameLog_Enable_Debug
Successfully pushed binary: %s\n
Configuring Stinger for %s environment\n
sendIm4M
Stinger Config ID not matching or missing, needs reconfiguration\n
IndexTableCompaction_415E
/usr/lib/libMobileGestalt.dylib
QueryAppletStatus.cpp
production
Skipping Install Missing Instance <%s> by key\n
Unrecognized command %s
-[AlohaPairingVerifier injectSEPKtoSSE_Debug:]
4107_GuardTimeout_30s
PROD 
setFTAActivationStatus
receiving R-APDU: %zu \n
Success
IsBootedOS
sharingRequestSignature
SSEGetAuthorizationRandom %d
Failed to add seac
Cannot parse property
fDeviceInfo
Failed to configure Stinger\n
Oasis applet not found\n
Unable to split certificates\n
Recover interrupted script 0x%llx before running 0x%llx
!fIsDone
disableAMRetry
PreLoadEligibleApplets
Failed to select CASD\n
Failed to get PRP\n
PTC Load and install SLAM
performFactoryConfiguration
InstallSunspriteLogger
-[AlohaPairingController processAuthReqPayload:outError:]
found SE with ID: %d \n
Start processing command: %s\n
Missing kRoseTagDigest in kRoseTagMeasurementRTKitOS
Executing script <%s, %s>\n
SLAMMigrateCopernicus_2_5_4_LoadAndInstallSunsprite_2_2_6
PairStockholm
fail to register kLibSEUpdaterClass
nonce
[cert isKindOfClass:[NSData class]]
{
SLAMLoadAndInstallLogger_1_0_0
Skipping MP <%s> because we are up to date %d or would downgrade %d \n
Verified result -- %@\n
print
Fail to DERDecodeSeqInit firmwareArray.
FirmwareData
outDataSize >= sizeof(outData->data)
SLAMDeleteDavenport
SLAMMigrateIron_2_0_13
Error when copying a9 params %@\n
[cert length] <= (end - pos)
No matching delivery object found.
Forcing device hardware version %u\n
iPhone
BootedOS
parseStartOptions
Found BeeConnexions Unified with Load File Version: 0x%04X (expected: 0x%04X)\n
SELogObj
ApChipId
open()
 
At MP: %s %s
Iron SLAM
Failed to get JCOP Config Trigger, invalid item type
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Failed to getSEPK : %@
data
Fail to parse MQR: wrong top level tag
Successfully deleted SEAppletTool\n
Helium Load and install SLAM
Error encountered when building apdu resp dictionary: %@\n
plist
Argon Load and install SLAM
scrt
While querying SLAM state
4108_EnableInFPM_EnableLogging
UnknownSEChipType
Aborting due to DO BSN 0x%X <= 0x01AD or device RSN 0x%X < 0x0192\n
No slots are enrolled, can proceed\n
Successfully deleted enablement PTA\n
InstallMissingInstances
SE in restricted mode
Cannot switch to UOS
Could not find a matching script within SEFW
Wrong DeviceInfo
Fail to Img4EncodeItemBegin
Failed to get sharing request\n
%@%@
FactoryPostflight revision: 
SecTaskCreateFromSelf
[keyData length] <= (end - pos)
GetCombined
-[AlohaPairingVerifier getSharingRequestWithSignature:withError:]
-- ----------------------- -- \n
DumpSE
-[AlohaPairingController getReverseProxySettings:outError:]
doStart
Passing fdrOptions %@
MAX
Refusing to V2 pair EOS with CSN 0x%X
ReadResponse
No personalizable SE found\n
| 
Fail to parse MQR
Failed to send Image4 trigger
DeactivateAll for %s ret %d SW 0x%hx\n
PTC Instance %s in LC state 0x%X\n
Can't retrieve Image4 signer; unknown ChipID: 
isHardwareiPhone: MGCopyAnswer returned nullptr for DeviceClass, defaulting to iPhone\n
no controller instance
skipReperso
type return to continue
Failed to query submit pairing record: %s\n
Failed to AMFDRDataPutForRestore : %@
ApSecurityDomain
] 
SLAMLuauMigration_1_2_0_5
Encountered error when decoding top level 0x%llx\n
Error encountered when building begin pair dictionary: %@\n
   OSU Mem Reserves PHEAP %u THEAP %u\n
Stinger is up to date (version: 0x%04X)\n
Error encountered when decoding top level 0x%llx\n
_notifyport
Unexpected length for CPLC data %zu
Invalidating transceiver wrapper\n
mac
com.apple.private.applesse.allow
sizeof(uint32_t) <= (end - pos)
Failed to parse top level %d
Failed to add rtod
%s\n
Krypton SLAM
SLAMMigrateArgon_2_1_4_0B
-[AlohaPairingVerifier performAlohaVerification]
Update is done successfully: %s\n
Error encountered when building auth resp dictionary: %@\n
-[AlohaPairingController performHTTPRequestWithRequestDict:outError:]
userInfo
Legacy (plist) SLAM SEFW path is no longer supported
VERBOSE
AppleSSE Log Starts - System Version %s
a
4216_I2CA_FrameLog_Enable_Default
simDetectWPD
OBKG
setLogLevelFromOptions
<libSEUpdater %p [%p]>{}
EVENT LOGGING: Invalid options parameter\n
Skipping Pre Load <%s> by key\n
While deleting key slot 0x%x\n
SE,ID
EffectiveProductionStatusAp
Binaries: 
SE Health Test Policy: %s\n
Forced FPF with device BSN != firmware BSN
AUTHREQ
SEUpdaterCreate
SEFW: %s: \n
Found action %d\n
Successfully ran trigger %s\n
SE %u personalisable %d\n
Skip configuring %s: SE key not supported\n
ErrorCode
fail to create SEUpdaterObj
level >= 0 && level < _LOG_LEVEL_MAX && \"level is not good\"
4217_I2CB_FrameLog_Enable_Default
Refusing to V2 pair with ChipID 0x%X
SLAMLoadAndInstallLogger_1_0_0_Internal
Wrong type for kRoseTagDigest
Cannot parse DeliveryObject.binaries
Unknown ChipID
PASS
_AddError
Unsupported SE key type
Unexpected SLAM version length %zu
40D0_Enable_WithFilters_SW_ISO
performSEHealthCheck
FPF: forced %d, torn %d, requested %d, required %d, allowed %d\n
handle
Failed to set MFDAll ret: %d\n
Failed to set MFDAll SW: %x\n
SLAMDeleteCopernicusAndSunsprite
Stinger applet not found\n
Oasis applet not found: SW=0x%X\n
PTC key in slot %d to be deleted %d\n
Could not create deleteKeyCommandData\n
Failed to send CommandGetAMState
Cannot found any matched delivery object
SE,Nonce
Additional actions: FTA will be %s, MFD will %sbe performed\n
DERDecodeSequenceContentWithBlock
helsinki
 fsn=0x
Exception! what: %s
DEV 
Wrong length for updateTableEnry
Failed to retrieve the config ID
SLAMMigrateKrypton_3_3_2_0E
While writing command\n
DF30
copyIdentifier
retSharingResultSignature
Failed to transceive %@\n
4108_DisableInFPM_EnableLogging
Successfully set FTA Activation Status to %d\n
At SLAMDeleteCopernicusAndSunsprite
Running trigger %s script 0x%s\n
WriteCommand
mmap()
Starting BeeConnexions update sequence\n
Fail to create data for SEDH in request
Apdu
Cannot parse UpdateTable.
FPF
Bad SW received when copying device type 0x%x\n
Unable to construct obkg data\n
Unable to form plist from data %@\n
Called SEUpdaterDestroy updater %p\n
Failed to decode ret %d tag 0x%llx exoected 0x%llx
Will dump SE to file --> %s\n
Failed to dump rc %d sw 0x%x\n
SCRT is nil\n
A00000015153504341534400
ExceptionLog_40D0
Created updater %p\n
CFNumberGetValue(tmp, kCFNumberSInt32Type, (void *)&chipID)
UniqueDeviceID
retKeyData
Successfully extracted ApTicket from options.\n
sePk
fmt
Fail to get Nonce from the request
crsSetSharingResult
Received incomplete E3 TLV from GetStatusApplications
SLAMDeleteOasis
EVENT LOGGING: Successfully wrote to file %s with events %s:\n
SEPEffectiveSecurityMode
outData->data.attV2AuthKeySize == outDataSize - sizeof(outData->data)
Error
Unexpected tag for perso state\n
%s
Finish processing command: %s and returning %d \n
haltOnCrash
  Instance %s Module %s LC %s\n
Not FW found in option
getStingerVersionAndConfig
Skip pairing due to RestoreOptions not present\n
v8@?0
Failed to parse as per PropertyItemSpec
forceSLAM
Dumping AM Info\n
Oasis version: %s\n
At SLAMInstallPTCInstances
Adding header %@ = %@\n
Are we in booted OS? %d\n
 bsn=0x
At SLAMDeletePTCInstances
0x%2.2x 
updateJCOPConfig
Stinger version: 0x%04X\n
info.tag == (ASN1_PRIVATE | ASN1_PRIMITIVE | 0x23)
SLAMMigrateHaishan_1_2_07
while encoding extensions : %d\n
context && outdata && outlength
Proxy Available\n
Skip DeleteSEAppletTool by SE chip type\n
While reading response for command\n
rd=md0
Bad SW from GET_STATUS: 
isSCAMInProgress
Skipping cleanup script <%s, %s> because module is not in selectable or installed state\n
SLAMMigratePTC
new state --> %d\n
*outDataSignature is nullptr
While performing recovery
Fail to allocate imageProps
requestDict
Pairing protocol version: %s\n
getSigKeyCertificates
VerifyData
Could not create listKeysCommandData\n
SE <<<< %@\n
BoardId
queryInfo
> %s
Unified Reader check/install completed successfully\n
Failed to decode CPLC data top level tag %d
Cannot allocate for dict
SE FW DEV Version
APDUREQ
Mismatched signing keys device %s script %s
  restoreEnvironment: %d\n
[%s] %s: %s
Could not copy device type with error %@\n
Selecting SE with ID: %d \n
Cannot parse ImageBinary.apdus
Failed to select OSU\n
Successfully loaded and installed SEAppletTool\n
SE,IsDev
I2CA_FrameLog_4216
size == sizeof(outData->data) + outData->data.keyDataSize + outData->data.attestationSize + outData->data.pubKeySize
EVENT LOGGING: Could not recreate log events properties from file - Defaulting to empty file\n
SE,ChipID
expirationDate
Fail to Img4EncodeItemCopyBuffer
SLAMMigrateSodium_1_0_12
Shutdown fSeHandle %p\n
Skip configuring %s: JCOP platform not supported\n
Successfully FDR-injected SE Public Key into SSE for SEID %@\n
Fail to Img4EncodeItemBegin: %d
No matching FW found
DeleteEnablementPTA
40C9_GuardTimeout_30s
sendIm4P
SE,FactoryMode
AC Platform Primary %d Platform Secondary %d JCOP1 %d JCOP2 %d\n
Error encountered when transceiving copy SEID \n
SEID
Fail to enumerate
Transmitting C-APDU %d: %zu\n
Failed to send Select ISD
CleanUpTerminatedPTC
Neon Delete
verifyPairing
EVENT LOGGING: Unable to serialize data - %s\n
certificates
SE Hardware Failure!
markForDeleteAll
SLAMLoadAndInstallOasis_1_0_07
Stinger Config ID: %s\n
AppleSSE
-- JCOP Train too low to GET DATA AVAILABLE MEMORY -- \n
info.tag == (ASN1_PRIVATE | ASN1_CONSTRUCTED | 0x3)
 for SEChipType 
 csn=0x
SE in restricted mode; skipping update\n
Failed to query attack log status %d SW: %x\n
b.data && b.length
Cannot init sequence for DeliveryObject.binaries
Hardware still not in a valid state: 
_createDataSignature
Error encountered when transceiving select %@\n
I2CA_GuardTimeout_40C9
CASDCert
AUTHRESP
APDURESP
outData->data.resultSize <= (end - pos)
Dumping platform identifier\n
Skipping Install Missing Instance <%s> by platform\n
Pre Load <%s, %s> executed successfully!\n
Expected tag 0x%llx, got tag 0x%llx\n
ptc_DeleteKey
%s() -> %d
Could not parse memory constraints within SEFW
info.tag == (ASN1_PRIVATE | ASN1_PRIMITIVE | 0x2A)
 }
getOasisVersionAndConfig
Malformed sessionId received %@\n
AlohaV2Pairing-
Got Updater Context %s\n
~P73BaseSEController
NO
Bad length for platform primary attack log indicator\n
Argon Migration SLAM
EffectiveSecurityModeAp
0
transceive
v32@?0@\"NFSecureElement\"8Q16^B24
-[AlohaPairingController verifyAndRetrieveServerSessionId:]
DATA
\tuserID        = %u\n
setSigKey
412A_Default
Fail to parse MQR: cannot decode top level tag
sendManifestQuery
Unexpected length for perso state response\n
Slalom Dev SLAM
Bad SW encountered when getting OBKG 0x%x\n
ParseE3TLVs_block_invoke
Failed to toggle SE power on
DF31
DebugLogPath not present\n
-[AlohaPairingController performAlohaPairing]
Error encountered when performing HTTP request %@, got reply %@, with error %@\n
EVENT LOGGING: Options not present\n
Failed to toggle SE power off
packageOnSE.size() >= versionLocationInPID.second && targetPackageAID.size() >= versionLocationInPID.second && versionLocationInPID.first < versionLocationInPID.second
size == sizeof(outData)
\tentropy hash  = %016llx\n
|
Skipping SE update due to low number of available indices\n
len >= 2
info.tag == (ASN1_PRIVATE | ASN1_CONSTRUCTED | 0x1E)
shouldAbortToAvoidBrick
SLAMDeleteStinger
Installing Stinger applet\n
EVENT LOGGING: Error writing to file - %s\n
-[SETransceiveHelper transceiveAndRecordCapdu:rapdu:]
Missing csn-train mapping for platform: 
Warning: No ApTicket available to pass in fdrOptions
Neon SLAM
-[SETransceiveHelper selectWithAID:]
Bad HTTP Status Code received %ld\n
SOCProductionMode
deactivated
ERR
Unsupported manifest query version: 
Cleaning up unused applets\n
ctx
Unsupported SLAM SEFW version %u.
Bad length for AM status
sharingResult
Starting SE Dump\n
Failed to parse key data %d %@\n
Setting debugArgs (kv): %s=%s\n
Haishan SLAM
Cannot parse UpdateTable entries
[
outDataSize <= sizeof(*outData)
ignoreSecureChannelAM
HWState returns UnSupported, bailing out\n
SE,OsKeysIdentifier
-[SETransceiveHelper crsGetSharingRequestWithError:]
-[SETransceiveHelper setAuthRandom:mac:error:]
PreflightContext
Destroying Update Controller\n
nfcd
Successfully Configured OSU Reserve \n
CFNumberGetValue(tmpNum, kCFNumberSInt32Type, (void*)&tmpValue)
EVENT LOGGING: debugLogPath obtained\n
EXPORT_REQUIRED
Could not get Oasis config ID: SW=0x%X, size=%zu\n
Failed to select CRS with ret %d SW: %x\n
Stinger applet not found: SW=0x%X\n
Package already present, skipping pre load <%s> \n
Fail to add SEID
ChipID
assertSW
attestation
Failed to decode script %d
EffectiveProductionStatusSEP
SE HW type %d multi-OS %d\n
execCommand
%s [%s]: 
_baaSupportClass
shutdown
APC finished with return code %d\n
StockholmPairingProtocolVersion
Internal Restore? %s\n
/var/mobile/Library/Logs/AppleSSE.log
vector
Get Data AUTH.PK %@\n
)
Pre-update SE Health check result: %s\n
Reinstall PTC
Attempt %d state %d is not yet ready, sleeping a bit\n
ECID from endPair %@ _ecid %@
keybagUUID
Failed SW 0x%hX at idx %d
This update would brick the SE due to rdar://problem/90407147
DeleteNeonAppletYK300R106
HSMChallengeSEP
SE,UpdatePayload
FactoryRFTest
Error encountered when processing end pair:%@\n
EndPair
libSEUpdater
setAuthRandom
Unexpected Get Status response for BeeConnexions (size=%zu): %s\n
Unknown chipID in BLOB
CertificateProductionStatus
CertificateSecurityMode
Failed to extract ApTicket from options.\n
deactivateAll
no
sendApduFile
Install signal handlers\n
Apdu.hpp
ignoreFPTear
At SLAMLoadAndInstallLogger
-[AlohaPairingController getReverseProxySettings:outError:]_block_invoke
CFDataGetLength(nonce) <= sizeof(inData.data.nonce)
CFDataGetLength(sePk) <= 4294967295U
Failed to read CPLC data; defaulting to SN210V
Failed to decode manifest
Neon Package AID on device is %s, skipping delete operation\n
Unable to get AM Digest with error code %d\n
I2CB_FrameLog_4217
-[AlohaPairingController(FDR) submitPairingRecord:]
While querying migration state
APTicket
outError && outMeasurementDict
SN100V detected based on manifest query response\n
deviceFPFBSN 0x%x deviceFPREV %d deliveryBSN 0x%x deliveryFPFRev %d amStateOK %d bsnChanged %d revChanged %d ret %d\n
Bad status received when sharing auth key %d or nil for sharing result %d or nil for sharing result signature %d\n
[%3.3ld.%1.1d] [%s] %s: %s
Bad SW from SELECT: 
Failed to parse 'sehv' value
Skipping MP <%s> by key\n
/usr/lib/libAppleSSEExt.dylib
with name %s, pkHash %s, platformCategory %d
INFO
num != nullptr
doPerform
Sodium SLAM
%02X
SESA
!rApdu.isBad() && sizeof(SelectOSUResponse) == rApdu.size()
SN300V2 detected based on manifest query response\n
Existing packageAID %s anyPackageOutOfDate %d wouldDowngrade %d anyModuleMissing %d, migrationTrigger %s
Failed to read response\n
Error encountered when decoding tag 0xDF21\n
40BD_EnableInFPM_EnableLogging
Missing kSETagMeasurementUpdatePayload or wrong type
binaryItem.data && binaryItem.length
While listing keys: %@\n
doAlohaPairing
Downgrade past 0x2A is not allowed
data is either not found or in wrong CFType
Failed to get commnand set-config, unsupported se key
EffectiveSecurityModeSEP
Submitting sePk data to FDR\n
40BD_EnableInFPM_DisableLogging
4217_I2CB_FrameLog_Disable
Failed to send select ISD
At least one slot enrolled & no KUD\n
Dumping OSU\n
POST
SLAM SEFW version 0 is deprecated.
Destroy BaseSEController\n
deleteUnusedApplets
Performing cleanup of old PTC keys\n
Options not present\n
Failed to parse signedSection as per SignedSectionItemSpec
Hardware version %u\n
No personalisable SEs found\n
Error encountered when parsing SCRTBlob %d\n
Dumping manifest query\n
Error encountered when decoding cert SN\n
makeUpdateController
\tsseKey hash   = %016llx\n
seHealthTest
SE >>>> %@\n
Failed recovery with scriptID 0x%llx, error was %s
-[AlohaPairingVerifier injectSEPKtoSSE_FDR:]
Unexpected length for sharing request %u\n
ExecuteCommand
SN450 detected based on manifest query response\n
len <= MAX_APDU_LEN
40D0_Disable
Loop %u of 31\n
v12@?0i8
Failed to write at offset 0x%x\n
outData.deviceVersion > 0
outData->data.authRandomSize <= (end - pos)
Recovering incomplete termination
DERDecodeItem
wrong updateTableEnry with wrong hash size
Debug argument forceDeviceHwVersion empty
Failed to parse DStatusContainerItem
Couldn't get sharedHardwareManager
Size of UpdateTable.entries is zero
rebooting\n
Checking for legacy Muirfield to cleanup\n
Error getting secure element array
-[SETransceiveHelper copyDeviceType:]
Perform configuring %s with option %s successfully\n
Failed to load NFC stack
setDebugOptions
Failed to GET_DATA Seshat 0x%x\n
-[SETransceiveHelper copyA9Parameters:]
Error encountered when transceiving copy SE Signature \n
BAASupport
ExecuteScriptWithResult
Bad length for primary attack log indicator\n
SLAMStingerConfig_qa_5F7E35F9D391B1367F75823E36496533
Checking for legacy Oasis to cleanup\n
Unknown command: 
SEAC
Error encountered when transceiving copyCasdCert\n
bytes && bytes->size() >= sizeof(CApduHeader_t)
SN210V detected based on manifest query response\n
Found forceUpdateLoop: %lu\n
-[SETransceiveHelper crsSetSharingResult:signature:error:]
end
DecodeSequenceContent returned %d
Fail to switch to updaterOS
chipID 0x%X isProd %d expectedBSN 0x%X (has_value %d) deliveryBSN 0x%X isPORUpdate %d\n
SLAMOasisConfig_10270000050000000000000000000000
copyPayload
ECID
Caller did not provide an output dictionary\n
Missing or wrong length tag 0x%llx
Caught exception %s\n
SLAMDeleteNeon
Failed to select %@\n
debugLogPath is unavailable, unable to log APDU and plists\n
Pairing error debug log path: %s\n
Install SEAppletTool: %s\n
Bad length for platform secondary attack log indicator\n
Skipping cleanup script <%s, %s> because hardware is iPhone\n
authRandom
outData
Failed to parse as per DeliveryObjectItemSpec
Failed to parse updatePayload as per UpdatePayloadItemSpec
No update item with index: 
Successfully MFD'ed all applets\n
Sending GET DATA OBKG\n
Deleting enablement PTA %s\n
runFactoryPostflight
SE OS not in idle state
development
Installing Oasis applet\n
SLAMInstallPTCInstances
Bad SW 0x%x received in select %@\n
Bad SW 0x%x received in get sharing request\n
-- GET STATUS APPLICATIONS -- \n
 rsn=0x
No APDU
-[AlohaPairingController performHTTPRequestWithRequestDict:outError:]_block_invoke
input.data && input.length
Error encountered when selecting CASD %@\n
fSeController
PTC SLAM
While selecting CASD\n
Aloha Pairing failed with return code\n
inData
 Device info: 
UnknownSEConfiguration
forceProd
PID on SE %s, version on SE 0x%04llX\n
SE,Ticket
UNDEFINED
tmpData
LoadAndInstallSEAppletTool
@SE,Ticket
Continue update with forceUpdateLoop=%lu \n
Exception during dumpDebugInfo: %s\n
Unexpected tag encountered 0x%llx, expected tag 0x%llx\n
Executing script %s ID 0x%llX
Error from AMFDRSealingMapCopyLocalData: %@
Fail to allocate tmpData
UpdateTable: 
Cannot parse forceUpdate counter: %s. Ignoring...\n
Failed to parse device info?
retMac
Cannot proceed in OSU state
_CFDictionarySetData
Proxy aborted? %d\n
(
I2CB_GuardTimeout_4107
Could not get Stinger config ID: SW=0x%X, size=%zu\n
For Trigger %s missing instance AID %s\n
SLAMSeosMigration_1_2_4
workaroundForPTCExport
Missing mandatory outparam
SN100V (Venus)
version
sharingResultSignature
 \t
getSharingRequestWithSignature
FAILED
No command output, returning NULL\n
getBlessedUser
events
Unsupported firmware version: 
Was expecting XML format but received %lu\n
payload.length <= 4294967295U
fDeliveryObj
operator()
setActivateFTA
outError && outDict
info.content.length == 4
Releasing transceiver wrapper\n
SLAMDeletePTCInstances
yes
Skip pairing due to version %@\n
verifyAlohaPairing
Legacy Oasis was found, removing it\n
@SE2,Ticket
outData->data.resultSignatureSize <= (end - pos)
SE is PROD_EVAL -> Skip SE-SEP pairing verification\n
Failed to send IM4 APDU
IOGeneralInterest
sizeof(CApduHeader_t) + payloadLen == bytes->size()
Perform Factory Postflight requested? %s\n
Bee MID was found, removing it\n
SLAM unavailable for MP <%s> on current platform\n
context
retPubKey
KeyID 0x%X, overwriting with dev %d
Cannot find SE ticket in restore option
doOneAction
Slalom Prod SLAM
%2.2x
Skip update since secure channel context AM is in progress\n
Oasis version mismatch. Current: %s, Expected: %s\n
transceiveInternal
transmitting C-APDU: %zu \n
-[SETransceiveHelper invalidate]
%F %T (%z)
\tnoPasscodeCnt = %u\n
PerformScriptWithResult
While parsing migration state
Skipping cleanup script <%s, %s> by key\n
Fail to add Nonce
Unexpected command received %@\n
description
updateSize
EXPORT_FINISHED
command
-[SETransceiveHelper copySESignature:hsmChallengeSE:ecid:outError:]
getSEInfo
PTA Package AID on device is %s, skipping delete operation\n
Could not get Oasis version: SW=0x%X, size=%zu\n
Cleanup complete\n
retAttV2AuthKey
SE FW PROD Version
Bad transceive with return code %d\n
-[SETransceiveHelper getSEPK:andSEID:deleteExisting:error:]
rapdu
SN300V (Eos)
SSEGetEntangledAuthorizationRandom
StripImg4
MQ: %s\n
While executing APDU %d
415E_Value00
Failed to get expected config data, invalid option: 
endpair payload %@\n
GetInstanceInfo
forceUpdate
Failed to configure Oasis\n
<FAILED TO VASPRINTF>
Querying scrt with UniqueDeviceID: %@\n
RestoreOptions
reboot
Failed to query Seshat KUD
MP <%s, %s> executed successfully!\n
While listing keys
\tauthRand hash = %016llx\n
Cannot parse ImageBinary.
Payload dictionary is wrong %@\n
Response from AMFDRDataPutForRestore %d (%@)\n
libImage4Encode
~P73BaseUpdateController
Fail to create dictionary for new manifest
Failed to configure 
StockholmPairingServerURL
ApEffectiveSecurityMode
\tseid          = 
doCommand
RSN 0x%X BSN 0x%X, skipSLAM %d forceSLAM %d isDowngrade %d\n
SE is PROD_EVAL -> Skip SE-SEP pairing\n
Error.hpp
Bad SW 0x%x received in copy SE Signature\n
Cannot parse ImageBinary.index.
skipSeshatCheck
Skipping cleanup script <%s, %s> because package is not found\n
Failed to get memory info, skipping indices check. Caught exception: %s\n
CFDataGetLength(seid) <= sizeof(inData.data.seid)
\tkeybag hash   = %016llx\n
While selecting ISD
SSESetSEPubKey returned %d\n
Called SSGetAttV2AuthKey with nonce (hsmChallengeSEP) : %@
4216_I2CA_FrameLog_Disable
Forcing local signing\n
Seos SLAM
key
SE,RootKeyIdentifier
Pairing is requested but no server URL is provided\n
not 
IM4P_validated
Calling %s\n
Skip: JCOP version low.\n
Copernicus SLAM
wouldDowngrade
EOSMemoryReserve_412A
-[AlohaPairingController dealloc]
At cleanup script: %s, %s\n
Error encountered when decoding tag 0xFE\n
ApEffectiveProductionMode
SEUpdaterDestroy
UNK_STATE
SE310S (Juno)
Start of LogBuffer\n
Unable to decode top level 0x%llx\n
Command output:\n
forceDeviceHwVersion
Failed to open file %s\n
SLAMLoadAndInstallStinger
Legacy BeeConnexion was found, removing it\n
  requestSig %@\n
outDataSignature && outDataSignatureLength
Failed to get config item 
skipUpdate
Luau SLAM
Fail to DERDecodeSeqNext firmwareArray.
Bad SW encountered when getting cert SN 0x%x\n
RestoreOptions not a dict?
hasSSE()
performAuthKeySharingWithAppleSSE
Successfully debug-injected SE Public Key into SSE for SEID %@\n
-[AlohaPairingVerifier invalidate]
  apTicket.length: %lu\n
header == reinterpret_cast<CApduHeader_t*>(&((*bytes)[0]))
4108_EnableInFPM_DisableLogging
Failed to validate delivery object
SESignature
Failed to add sers
 FPState=0x
BSN: 
Unknown algorithm 
assign
Cannot parse properties entries
Skip LoadAndInstallSEAppletTool by SE chip type\n
Bad status received when getting Auth Key V2 %d or nil for AuthKey %d\n
Recovery script 0x%llx not found, terminating!
< %s
Unexpected returned length for hardware version query %zu != %zu\n
SE2,Ticket
Failed to register for proxy\n
seid
40BD_DisableInFPM_DisableLogging
hasSufficientIndicesForOSU
A000000704C0000000000002
Wrong size for get config response 
dataSize <= sizeof(payloadHeader.seid)
Options
Failed to SELECT Seshat 0x%x?\n
Fail to parse SEFW.
Failed to sign: %d
Failed to get commnand set-config, invalid option: 
Error encountered when retrieving casdCertificate %@\n
Failed to transceive code = %d\n
sharingRequest
415E_Value0C
Skip sending the Update Payload because of IM4 state %s\n
DeactivateAll for %s failed to SELECT CRS %d SW 0x%hx\n
Failed to perform pre-update health check Caught exception %s\n
RestoreInternal
performNextStage
Unsupported chip ID
postflight
SLAMStingerConfig_prod_505C2526532CCF2049A2E3BDB6FD2867
At installation trigger %s script %s\n
Failed to parse SEFirmware.version.
Pairing with reverse proxy: %d\n
Setting loglevel to %d\n
Fail to sendApdus
%s: \n
printManifest
Configuring Oasis applet\n
Error code %d received when setting SE PK in SSE
-[AlohaPairingVerifier performAuthKeySharingWithAppleSSE:sharingRequest:requestSignature:resultSignature:withError:]
getForceUpdateLoop
SLAMLoadAndInstallPTC
-[SETransceiveHelper copySeid:]
Failed to get commnand get-config, unsupported se key
CreateFilesystemPartitions
CreateFilesystemPartitions missing or wrong type
com.apple.private.applesse.baa
Invalid health check policy: 
/usr/standalone/firmware/SLAM/SLAM.sefw
  useDebugSSEInterface: %d\n
Cannot parse UpdateTable.bsn.
MQ: %s: \n
Pushed Manifest successfully\n
At Pre Load: %s %s
%04x: 
failed to Img4EncodeCreateManifest
\tsubcounter    = %llu\n
Bad SW from GET_DATA AVAILABLE MEMORY: 
At SLAMDeleteNeon
Bee Delete
Unexpected SW 0x%hX
SLAM
Failed to select CRS %d 0x%hx\n
Error encountered when geting scrt %@ or scrt absent %d\n
getDeviceHardwareVersion
No factory postflight in the update bundle
Context 0x%X status 0x%X\n
Failed to decode with dr %d\n
cbNfRestoreSEEnumerate
While getting ChipId for platform category
pubKey
copySEID
payload == nullptr
AC Platform Primary %d Platform Secondary %d\n
SLAMMigrateCopernicus_2_5_4
AlohaPairingController invalidating\n
Error when verifying session ID %@\n
UniqueChipID
/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSElib/AppleSSElib.m
bytes
Failed to select ISD %d SW: %x\n
Bad SW 0x%x received\n
Skip configuring %s: JCOP version low (current csn: 0x%04X, min csn: 0x%04X)\n
PlatformBitmap absent for a script with name %s
SN200V (Ceres)
data.data && data.length
Pushed Update Payload successfully\n
isSeshatEnrolledAndNotKUD
At SLAMLoadAndInstallSEAppletTool_0_0_2
DeleteSEAppletTool
Failed to get SEPK+SEID: %@
i24@?0^{?=Q{?=*Q}}8^B16
Skip sending the Manifest because of nonce mismatch\n
LoadAndInstallSunspriteLogger
SLAM unavailable for Pre Load <%s> on current platform\n
Attempting to split a non DER sequence %d\n
Malformed reply dictionary received %@\n
->pls attach debugger\n
Failed to decode APDUs %d
image_no_reset
SunspriteLogger Applet is already installed, skipping load and install\n
SLAMDeleteBee
DERDecodeData
ptc_listKeys
Missing SE,RootKeyIdentifier in request dictionary
Pairing hostname URL: %s\n
End of LogBuffer\n
SecureElement
Unknown legacy platform category %u
SLAMDeleteBeeLegacy
SEUpdaterEventsLog.plist
SE,OSUPubKeyID
Get Attestation V2 Auth Key feature is not supported on this device with status %d\n
outdata && outlength
Failed to retrieve CRS perso state\n
(sizeof(CApduHeader_t)+len)<=MAX_APDU_LEN
Xenon Delete
WARNING
Failed to parse 'seci' value
At SLAMDeleteSEAppletTool
Pairing not enabled\n
/
Ignoring NFC load stack error\n
Unknown personalizable SE %d\n
(end - pos) >= dataSize
40BD_DisableInFPM_EnableLogging
Can't retrieve config ID since JCOP is not active
Got personalisable SE with nil manifestQuery?!
Fail to add chip ID
attV2AuthKey
caught signal %d\n
pos <= end
Failed to set FTA activation with SW: %x\n
Bailing out.\n
SLAMLoadAndInstallArgon_2_1_4_0B
manifest is null or zero manifesetLen
Unknown RootCAId: 
image
updateMeasurementDict
fSeHandle
NULL deviceInfo
Oasis is up to date\n
Bad SW 0x%x received in copy SEID\n
-[AlohaPairingController processEndPair:]
4143_WeakPullDown
ImageBinary.type is out of range.
Dumping Update Table\n
Cleanup script <%s, %s> executed successfully!\n
Submitting sePK to FDR: %d\n
```
