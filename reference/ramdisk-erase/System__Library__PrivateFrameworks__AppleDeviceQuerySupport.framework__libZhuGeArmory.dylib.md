# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 506,320 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 39 (Size: 5248)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (19)

- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/NearField.framework/NearField (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libnfrestore.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/usr/lib/libVinylNonUpdater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/updaters/libCentauriUpdater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/Centauri.framework/Centauri (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (20 classes, 0 protocols)

Classes: `CTMobileEquipmentInfo`, `NSArray`, `NSData`, `NSError`, `NSNumber`, `NSString`, `ZhuGeArmory`, `ZhuGeArmoryHelperArmory`, `ZhuGeBasebandArmory`, `ZhuGeBasebandConnectionArmory`, `ZhuGeBasebandFirmwareSecurityInfoArmory`, `ZhuGeBasebandFirmwareUpdateInfoArmory`, `ZhuGeBasebandPostponementStatusArmory`, `ZhuGeCacheArmory`, `ZhuGeKeysActionArmory`, `ZhuGeKeysConfigArmory`, `ZhuGeLockerArmory`, `ZhuGeMobileEquipmentInfoArmory`, `ZhuGeModuleArmory`, `ZhuGeSingletonArmory`

## Strings (1,678)

```
T@\"NSDictionary\",&,V_firmwareUpdateInfo
initWithError:
replaceBytesInRange:withBytes:
stringByReplacingOccurrencesOfString:withString:
_config
arrayWithArray:
_cacheType
appendBytes:length:
keysConfig
setDependencyPath:
sortedArrayUsingComparator:
_configClass
JSONObjectWithData:options:error:
numberWithLong:
errorWithZhuGeErrorCode:underlyingError:
invoke
length
_keysConfig
arrayWithObjects:count:
embeddedSecureElementWithError:
T@\"NSData\",&,V_eUICCPairingIdentifier
firstMatchInString:options:range:
firstObject
processName
substringFromIndex:
getSubkeyOfKey:withError:
description
numberWithShort:
T@\"NSDictionary\",&,V_firmwareSecurityInfo
dataFromHexString:
environment
initWithQueue:
queryFDRSealingStatusWithManifestOverride:WithError:
querySPUProperty:withError:
stringByTrimmingCharactersInString:
hasSuffix:
loadMobileEquipInfoList:
methodSignatureForSelector:
T@\"ZhuGeArmoryHelperArmory\",R,V_helper
_xpcConnection
isEqualToNumber:
isEqualToString:
substringWithRange:
helper
updateChangeablePropertiesForKey:andOption:withError:
T@\"ZhuGeCacheArmory\",&,V_propertiesCache
dataWithLength:
UTF8String
config
integerFromCInt:size:isSigned:needSwap:
numberWithLongLong:
numberWithUnsignedShort:
T@\"NSString\",R,V_name
getCoreTelephonyClient
macAddressStringFromSysconfigDataSixByte:
slotId
verifyDependencyWithError:
_aliasesMap
actForKey:andName:andConfig:andOptions:andPreferences:withError:
countByEnumeratingWithState:objects:count:
integerFromData:size:truncate:isSigned:needSwap:
serialNumber
queryBasebandFirmwareSecurityInfo:withError:
querySysCfgKey:withError:
initWithLength:
getCTServerConnection
actionClass
numberOfRanges
numberWithUnsignedChar:
propertiesByKey:andSuperKeyRange:withError:
queryCHUnitSimMuxDualPhysicalStateWithError:
queryMobileEquipInfo:byKey:withError:
queryThreadRadioMacAddressForProvisioningWithError:
rangeAtIndex:
T@\"NSDictionary\",R,V_option
query:forceCacheable:withError:
_eUICCPairingIdentifier
_firmwareUpdateInfo
numberFromString:
postponementStatus
accessInstanceVariablesDirectly
T@\"NSXPCConnection\",&,V_xpcConnection
lowercaseStringWithLocale:
queryNFSecureElementByKey:WithError:
numberWithBool:
uppercaseString
isEqual:
sharedInstance
_name
convertReturnValue:toFormat:
setLogHandler:
T@\"NSMutableArray\",R,V_cacheList
queryThreadRadioMacAddress64BitWithError:
queryWLHWIdentifierInfoByProperty:withError:
userInfo
cStringUsingEncoding:
dictionaryWithDictionary:
visibleStringFromData:
aRecursiveMutex
getBytes:range:
T@\"NSString\",R,V_key
numberOfArguments
pickFlexibleFromUnionizedConfig:withError:
queryVinylEUICCCSNbyKey:withError:
dataUsingEncoding:
getPropertiesOfKey:withError:
numberWithUnsignedLongLong:
scanInt:
stringWithUTF8String:
unsignedIntegerValue
isAppleBaseband
count
initWithBytes:length:
queryFactoryShippingSettingTimeWithError:
stringByRightTrimmingCharacter:
_mobileEquipInfoList
dependencyPath
numberWithUnsignedInteger:
queryKey:andOptions:andPreferences:withError:
regularExpressionWithPattern:options:error:
_helper
hasBaseband
lastPathComponent
logHandler
.cxx_destruct
cacheDict
clearCache
integerValue
stringByReplacingOccurrencesOfString:withString:options:range:
stringValue
setKey:
ZhuGeToDo:withError:
convertReturnValue:toCase:
getKeyAndOptionFromDependency:withError:
getProperty:inPlane:withName:withOption:
graphicInfoArrayFromArray:
hexStringFromData:
methodReturnLength
T#,R,V_cacheType
configClass
numberWithInteger:
queryIOPropertyFromPath:andCriteria:withError:
setPropertiesCache:
lowercaseString
appendFormat:
escapedPatternForString:
getConfig
getEuiccData:
getMobileEquipmentInfo:
invocationWithMethodSignature:
query:isCachable:withError:
_flexibleList
descriptionFromZhuGeErrorCode:
dictionaryWithContentsOfFile:
removeAllObjects
removeObject:
stringWithFormat:
T@\"NSString\",&
_ZhuGeDescriptionWithLayer:
loadPostponementStatus:
queryExternalDisplayBacklightUIDWithError:
valueForUndefinedKey:
firmwareUpdateInfo
isEuiccActiveWithError:
arrayWithCapacity:
numberWithChar:
T#,R,V_actionClass
_actionClass
option
queryWLModuleSerialNumberWithError:
sortAliasFromUnionizedConfig:withError:
arrayFromShellCommandString:
bytes
code
T@\"NSNumber\",R,V_capacity
key
dataWithBytes:length:
initWithFormat:arguments:
loadFirmwareUpdateInfo:
dictionaryWithObjects:forKeys:count:
errorWithDomain:code:userInfo:
getEuiccPairingIdentifier:
hasPrefix:
intValue
queryAIDTouchScreenCert:idx:withError:
queryIOCameraByProperty:withError:
stringByTrimmingCharactersInSet:
_option
T@\"NSArray\",R,V_flexibleList
cacheList
checkDependency:withError:
convertReturnValue:ByItselfAndError:AndRevalues:
getPrimarykeyOfKey:withError:
queryMogulIDSN:withError:
T#,R,V_configClass
boolFromData:needNegate:
flexibleList
initWithName:andCapacity:andCacheType:
queryIOProperty:fromCriteria:withError:
supportsDynamicSIMConfigurationWithError:
waitUntilBasebandReady:retryInterval:
numberWithInt:
scannerWithString:
unsignedLongLongValue
_propertiesCache
getConfigOfKey:withError:
mutableBytes
_cacheList
getBytes:length:
initWithData:encoding:
longLongValue
componentsJoinedByString:
currentLocale
dictionaryWithObjectsAndKeys:
loadFirmwareSecurityInfoRestoreOS:
queryTouchScreenCert:
T@\"NSDictionary\",R,V_keysConfig
aliasesMap
boolValue
getReportFDRDiagnosticFromOption:withError:
initData
isKeyAlias:withError:
setFirmwareSecurityInfo:
setObject:forKeyedSubscript:
containsObject:
isBasebandReady
_key
setEUICCPairingIdentifier:
sharedHardwareManager:
uppercaseStringWithLocale:
ccccValue
characterAtIndex:
characterSetWithCharactersInString:
queryMesaSensorIDSensorSNWithError:
setFirmwareUpdateInfo:
stringByPaddingToLength:withString:startingAtIndex:
propertiesCache
isAtEnd
objectForKeyedSubscript:
query:withError:
queryDisplayUniqueChipIDWithError:
setArgument:atIndex:
setObject:atIndexedSubscript:
setPostponementStatus:
stringFromData:
_cacheDict
allValues
processInfo
queryBMUExpectedBoardIDWithError:
stringByRemovingCharactersInString:
delCacheForKey:
_logHandler
meInfoList
name
querySysctlVariableName:dataType:withError:
sleepForTimeInterval:
synchronousRemoteObjectProxyWithErrorHandler:
getCacheForKey:
getBasebandClass
loadFirmwareSecurityInfoBootedOS:
T@\"NSMutableArray\",&,V_dependencyPath
T@\"NSMutableDictionary\",R,V_cacheDict
T^?,V_logHandler
init
initWithBytes:length:encoding:
mobileEquipInfoList
queryComponentAuthChipIDSN:withError:
scanHexInt:
T@\"CTMobileEquipmentInfoList\",&,V_mobileEquipInfoList
T@\"NSDictionary\",R,V_config
numberWithUnsignedInt:
removeObjectForKey:
_dependencyPath
initWithCapacity:
initWithRawConfig:
T@\"NSDictionary\",R,V_aliasesMap
getMobileEquipInfoIn:ofSlot:
ZhuGeDescription
isDataConvertibleToVisibleString:
objectForKey:
setXpcConnection:
substringToIndex:
systemOSSerialNumber
firmwareSecurityInfo
loadEUICCPairingIdentifier:
arrayWithObject:
base64EncodedDataWithOptions:
getObfuscatedKey:withError:
queryFDRDeviceAsidMetadataIsVerified:withError:
runForKey:andOptions:andPreferences:withError:
xpcConnection
allKeys
_firmwareSecurityInfo
convertToPostponementKey:
eUICCPairingIdentifier
query:ofSlot:isCachable:withError:
queryCentauriSikPubWithError:
setCache:forKey:withError:
setMobileEquipInfoList:
T@\"NSDictionary\",&,V_postponementStatus
capacity
numberWithUnsignedLong:
valueForKey:
getReturnValue:
componentsSeparatedByString:
macAddressStringFromData:
rangeOfString:
setTarget:
_capacity
cacheType
objectAtIndexedSubscript:
printRemoteLog:withReply:
queryScreenSerialNumberByProperty:withError:
domain
_postponementStatus
stringByLeftTrimmingCharacter:
addObject:
propertiesOfKey:withError:
queryMesaProvisionStateWithError:
setSelector:
unionizeRawConfig:withError:
@32@0:8Q16@24
@\"NSData\"
@20@0:8c16
@24@0:8^@16
v24@0:8@16
B40@0:8@16@24^@32
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
@\"NSMutableDictionary\"
@40@0:8Q16Q24B32B36
@48@0:8@16Q24q32B40B44
B40@0:8^@16@24@32
^{__CTServerConnection=}16@0:8
B24@0:8i16i20
@\"NSNumber\"
@\"ZhuGeArmoryHelperArmory\"
@48@0:8@16{_NSRange=QQ}24^@40
@\"ZhuGeCacheArmory\"
@\"NSXPCConnection\"
@32@0:8@16^@24
v16@0:8
@\"NSString\"
@64@0:8@16@24@32@40@48^@56
@\"NSArray\"
B24@0:8@16
@\"NSMutableArray\"
B16@0:8
q16@0:8
@44@0:8[512c]16[128c]24^{__CFString=}32I40
@36@0:8@16B24^@28
@32@0:8@16q24
@\"CTMobileEquipmentInfoList\"
@\"NSDictionary\"
@16@0:8
@44@0:8@16q24B32^@36
@40@0:8@16@24#32
#
@48@0:8@16@24@32^@40
@32@0:8B16i20^@24
^?16@0:8
v24@0:8^?16
B32@0:8@16^@24
@24@0:8Q16
^?
@40@0:8@16@24^@32
B24@0:8^@16
@24@0:8@16
#16@0:8
@28@0:8@16B24
@32@0:8@16@24
ChipID
orjkMiWWInwIkY/Z7N3hr221P46zXZD9kH3CzhdxkV34s
Failed to get TMac from sysconfig dictionary!
ECID
IODeviceTree://chosen/development-cert
Failed to get eUICC firmware info!
VBIOS Version
Please make sure IO Service is valid
Method Invocation Get Failed
IODeviceTree://chosen/effective-security-mode-sep
AMFDRSealingMapCopyLocalDataForClass
pBZwlrYQ/Yqs7UBWEniBp0BscFwhG7wt++nWg6W28fEPE
*bufferSize
%08X-
Device does not support dynamic configuration
-[ZhuGeArmory updateChangeablePropertiesForKey:andOption:withError:]
property pointer is nil!
Failed to query WLHWIdentifier due to mismatch data type, data read %@
Successfully read IDSN from AppleAuthCP I2C service.
z/7S0WfcGLDiM3juoXAPk16+dabQmWIXU2/xn5nLqcsyI
IODeviceTree://product/panel-serial-number
BackCameraModuleSerialNumString
caseType is invalid!
Caching properties for key: \"%@\"
Failed to get properties of \"%@\" for primary key!
ReportFDRDiagnostic_Options
touch screen cert has %ld bytes after decoding
cmd
error p-pointer is nil!
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoBootedOS:]
revalues pointer is nil!
IONameMatch
AppleAuthCP
transportProperties: %@
AppleSmartBatteryPack
wCREDfKF3ElH/GhqMIJjn15CQ72E5I5V/bN+n/bBR4MNU
baseband class should be an integer
/usr/lib/libFDR.dylib
%llu
-[ZhuGeArmoryHelperArmory sortAliasFromUnionizedConfig:withError:]
service class and name
+[ZhuGeKeysActionArmory queryCentauriSikPubWithError:]
isComponentAuthChipAuthCPService
BackSuperWideCameraModuleSerialNumString
Dependency \"%@\" defines a non-array dependency
ACTION_SEQUENCE
Failed to convert case for key \"%@\"!
SP Report Crashed
+[ZhuGeKeysActionArmory queryTouchScreenCert:]
Failed to convert \"%@\" to hex number!
Memory Exhausted
Please contact Near Field team for issue triaging
The key could possibly be a MobileGestalt key, not supported at all
+[ZhuGeKeysActionArmory queryMesaProvisionStateWithError:]
MissingMSRk
IOService://ethernet/local-mac-address
WMc2
Failed to encode with proper API
Lacking subkey of key \"%@\"!
Key Duplicated
Already found %@, skip this
EMa2
Failed to get CT server connection interface!
6Gxpv/uzw0b4QcHxsgcfH0AuNp2A/PFANYZxtAYKfBbnw
queryMesaSensorIDSensorSNWithError:
Key \"%@\" defines a non-array argument for action \"%@\"
Arguments were set for key \"%@\": (%@)
ZhuGe is running well
Please check your code to use a correct class
data:tcon
MesaSensorIDSensorSN allocation failed
tRn/qRwm394es24o13orf0CTTM60oo8/DS2Dx26ehaqHw
getReportFDRDiagnosticFromOption:withError:
nil
RetryNumber
OS Unsupported
Failed to find IO entry for \"%@\"!
Missing basic criteria for key \"%@\"!
\"%@\" of entry \"%@\" is class %@ while expecting Integer<NSNumber>
AccessoryCertificate
STRING_HEX
ProvisionedLockedUnknownKey
flags
ZhuGeToDo:withError:
0
SMC Service Unsupported
string:
%@ length %@ is too long
Library-MesaFactory
Key \"%@\" is defined action sequence with non-array
No property \"%@\" in entry \"%u\"
Failed to find a non-fullPath service for key \"%@\"
Failed to query BMUExpectedBoardIDData. isBMU2 = %d
Exiting aHWManagerReady callback
graphicsArray pointer is nil!
Failed to update config for key \"%@\"!
Invalid basic criteria type for key \"%@\"!
jcopSESN
/YHNnwv/KBMBEzyR3td5118gYU9eWHwdKy6bKcb1vddZU
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
Query key: \"%@\" within %@ms
+[ZhuGeKeysActionArmory queryAIDTouchScreenCert:idx:withError:]
Img4DecodeInit failed to decode fdrData with der state %@!
lEKNOip1IEPHg8L978amc0CNhXOgGSVJSBCKO37yUcv7k
(null)
firmwareSecurityInfo can not be nil
-[ZhuGeArmory convertReturnValue:ByItselfAndError:AndRevalues:]
data:
IOService://wlan/local-mac-address
:
YTrd2LofkEtmiM4cXwiLc082s6U/st5pPHdDS8MT8UAsc
FrontCameraRenoModuleSerialNumString
Cannot find IO service entry from path \"%@\" for key \"%@\"!
Successfully read IDSN from AppleAuthCP AID service.
X0kI6yR4hRNgedMr+8P2z15g6ljy/AS4p+MmcSrWDUI/I
-[ZhuGeBasebandFirmwareUpdateInfoArmory loadEUICCPairingIdentifier:]
Unsupported service matching method!
-[ZhuGeArmory runForKey:andOptions:andPreferences:withError:]
AppleH3CamIn
Unsupported AID mogul type
querySPUProperty:withError:
ACTION_TIMEOUT
Will invocate for key \"%@\"!
Key \"%@\" isn't supported in %@!
IO Service Close Failed
Please make sure IO Service connection is valid
Path Not Absolute
RegEx Not Matched
AppleH16CamIn
Failed to get CoreTelephonyClient instance
-[ZhuGeBasebandFirmwareUpdateInfoArmory query:isCachable:withError:]
\"%@\" is not a vaild MobileGestalt key!
Method Signature Get Failed
Failed to match the service name \"%@\"!
did not find the config of key %@
StripImg4
logCallbackForSyslogWithContextBuffer
-[ZhuGeArmoryHelperArmory initWithRawConfig:]
SP Report Creation failed
fullPath
IODeviceTree:/product
AWCSMahiDeviceInfo
-[ZhuGeBasebandPostponementStatusArmory query:isCachable:withError:]
ARRAY_GRAPHIC_INFO
Failed to read the display unique identifier!
tritium-mando-uid
DSp557sXEG12LTRMsGdoP0DnK4Tq6SBvsLPV6rag2VVVQ
BBUpdaterExecCommand
unknown
path pointer is nil!
String Format Wrong
Time Out
ComponentIndex
queryIOProperty:fromCriteria:withError:
FduIrkWaePZT8tDWdxcu00FF+SES2WC9g094cg6x2FEa4
Failed to get invocation method \"%@\" for key \"%@\"
-[ZhuGeArmoryHelperArmory isKeyAlias:withError:]
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
querying %@/%@ returned %s and %@
queryBMUExpectedBoardIDWithError:
[ZhuGe]
-[ZhuGeArmory convertReturnValue:toFormat:]
IO Entry Not Found
Local
Failed to get IO properties from service entry %@! %s!
parent check failed
Entering aHWManagerReady callback
BBUpdaterExtremeCreate
ZhuGe_Action_Retry_Serial_Queue
Initialization Failed
Get failure when calling API of AppleMobileFileIntegrity
Invalid extra criteria type for key \"%@\"!
product
RID
Didn't find EID from response of eUICC operation!
IODeviceTree://options/boot-args
VlPZNgOg1p1oj0IEgDd6F10jh+is1Z1X+RW+DXL/lKQvY
err == 0 
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m
Failed to cache string for \"%@\"!
Method \"%@\" of key \"%@\" has a non-number retry interval
Failed to create IORegistryEntry iterator
LBJfwOEzExRxzlAnSuI7eg
W6G2ZPL+BzsMLGtunPo4q13HKvqm45nmzrVJEV2Uq/x18
%s: 
IODeviceTree
returnValue p-pointer is nil!
gPOK
Please check the path of IO entry
MobileGestalt Not Supported
als-front-land-serial-num
K0trEdL9AkfNZmKGN1K/S0DuAHqkSCTPqZspPP0bapRbA
no mobile equipment information of slot%d
Issue Underlying
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
No firmwareSecurityInfo found
RetryInterval
Cannot open certain file
The failure might be expected without specific hardware
Searching from fullPath service.
CACHEABLE
logCallbackForSyslogWithLevelBuffer
VutVHB8Wg9nACkP4UQgs31CxyuH0G43a9ffxeavEwVXJs
RETURN_REVALUE_ERROR
Failed to get length of flexible key \"%@\"!
+[ZhuGeKeysActionArmory getReportFDRDiagnosticFromOption:withError:]
service class or name
wlan
IOService://AppleTCONControl/coverglass-serial-number
DataStore
root
IOSERVICE_MARCONI_WIFI
Failed to weak link core telephony client framework!
BBUpdaterSetOptions
/usr/local/lib/libFDR.dylib
parent class or name
+[ZhuGeKeysActionArmory queryWLModuleSerialNumberWithError:]
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
%s
Revalue \"%@\" criteria are matched
ZhuGe received a relative path
criteria pointer is nil!
IOPortTransportAIDBus
8ybq4N66oFkNzgwX0r/uh12j3Yul3nPiPplgdku4vHwGw
+[ZhuGeBasebandConnectionArmory getCoreTelephonyClient]
Flexible key \"%@\" got a nil subkey!
-[ZhuGeArmory checkDependency:withError:]
m
+[ZhuGeKeysActionArmory queryMesaSensorIDSensorSNWithError:]
In %@, error p-pointer is nil!
\"%@\" of entry \"%@\" is class %@ while expecting NSData
Failed to get pinecrest cert from libFDR for key \"%@\"!
queryVinylEUICCCSNbyKey:withError:
UnknownFunc
Please check newly added code that calling ZhuGeError API
Illegal ZhuGe Error Code!
Read %@, field %@, output %@
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m
Catch the NULL format pointer from: %s %s(%ld)
v8@?0
w3d+bqLep9C2KRT5Dc/t717IDOHkzNoShIRuhKyVGx19w
{%d:0x%llx}
mobileEquipInfoList is reloaded
Something might be wrong with Near Field component
The system profiler data type is null
Matching regEx failed for IO path \"%@\"!
Cannot find IO entry from path \"%@\"!
BackCameraSNUM
_connectHandleRefCount > 0
Failed to get a valid IO service iterator for \"%@\"!
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
Lockdown Query Failed
%@:/%@
TMac
Failed to read IDSN via AID
Unknown
DERParseSequence failed to decode into TBS Cert with der state %@!
f3JPDMLbeFqGZ6JKp/Cxc10Junmx7Bkr3WAFSj7+tHdh4
h+cEHH8im90i0QmeMjdFa15fpOD6vCrZthyvGqlk72MUM
ctx pointer is nil!
%s ERR: 
firmwareUpdateInfo is reloaded
Got IO connection for \"%@\" with type \"%@\".
NIL
-
-[ZhuGeArmoryHelperArmory getConfigOfKey:withError:]
mogulAce3
6rUXDHIWCVKLhA5uFbxB41Aw9LlmCMGCvEkW0TG6dPwe0
K0+xnwAxaxD8HiKQ4gDJd1DOtVl5HGVtbPZ1C+nR24SJ8
nJcmJi6nEp5Ll6CuYyaC+10jXex+M+8W1qy3xdu3e1OMA
v24@?0@\"NSDictionary\"8@\"NSError\"16
Failed to get io service iterator by \"%@\" for key \"%@\"!
s
queryIOPropertyFromPath:andCriteria:withError:
BackTeleCameraSNUM
TGiWzHMwhvg0m4uhHqJED0BUxYG4igeW4GbuHTy/DAXPw
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m
In %@, aKey pointer is nil!
ACTION_RETRY
The property list cannot be serialized
AMFI Get Failed
\"%@\" is not a valid integer
psim-present
o8SKs/wlQuqD2Q2nnHk9z1CpnG8Hc9hmFwcjNYdYxeWRo
Path Not Found
SMC Service Failed
Entry \"%@\" failed check at %@/%@
success read idsnData, first byte: %x
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Binaries/ZhuGe_Service/install/Symbols/embattled/embattled_keys.m
class
ZHUGE_NULL
fail to load BBUpdaterSetOptions from BBUpdater dylib
Alias of key \"%@\" is not an array
Reserved ZhuGeErrorCode %@ shall not be the argument
%s:/%@
XPC_SERVICE_NAME
NUMBER_SINT32
Original key \"%@\" is already obfuscated
Name of the call back function doesn't exist in library
Entitlement Unsupported
CentauriUpdaterCopySiKPublicKey is not supported!
mZfUC7qo4pURNhyMHZ62RQ
SIM_MUX verified: Device is in P+E configuration (expected P+P)
LSB
-[ZhuGeArmoryHelperArmory propertiesOfKey:withError:]
nfKey pointer is nil!
-[ZhuGeArmory actForKey:andName:andConfig:andOptions:andPreferences:withError:]_block_invoke
CZbYk6sTjNxVqTYUgxbf+17r9md3DZ5QRHzUHBjtnELao
key length is %@, but super key range is {%@, %@}!
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
Failed to get bootstrap main port for key \"%@\"!
name pointer is nil!
Failed to retrive value for \"%@\" from MobileGestalt!
AIDReadIDSN
Some pointer shall not be NULL
parent
multi-touch
tcon
didn't retrieve functions from BBUpdater dylib properly
-[ZhuGeArmory convertReturnValue:toCase:]
-[ZhuGeArmory getKeyAndOptionFromDependency:withError:]
dependency \"%@\" doesn't contain a valid JSON string!
Failed to cache properties for key \"%@\"!
AppleCamera
SecAbsoluteTimeFromDateContentWithError failed, error = %@
HRr/DU1S07L/YFiEw2YzX18zHSFPcobEs4ZEajjWPCx64
Booted OS: loading firmware security info via CoreTelephony
Method \"%@\" of key \"%@\" doesn't return anything!
Probaby the wrong arguments defined in xml
CFDictionaryCreateMutable failed!
defaults
ACTION_QUERY_PATH_STRAIGHT
MahiChipDieID
qjRH5QM3m6nH/auYOa6eC0D5vPWulgi0+VLCngICk+c2w
Failed to get postponementStatus: %d:%d(%s)
Restore
aString length is too long for 2 hex number expression!
parent no check
hCf3J+I7Gvmj39kb5wuYT1CfwQRQymZQ/Xo+KPRhX4lU8
J9wpYRxZXBUk1WO0ni6v917+rriuGS/GSQobZkVtVCsTM
SensorID
Key \"%@\" isn't supported in restoreos!
STRING_UUID_WITHOUT_DASH
STRING_SIZE_GIB
STRING_LOWERCASE
Key \"%@\" doesn't define the default action
-[ZhuGeArmoryHelperArmory unionizeRawConfig:withError:]
AppleH13CamIn
Failed to query IO property \"ecid\" for TCON!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeIO.m
 
Config \"%@\" for key \"%@\" is not a dictionary
Please check whether there is any underlying isse in the encoding API.
???
AppleBiometricServices
systemSESN
gB61Se7lVm1BUkLqacQ980B55i3Rbb9ngrzF3NEAPgXFM
JSON String Invalid
serviceName
Rz0lOIZTohL+Ri3DNSjvf19Isbz5Z2lVYAvTeQYgrxJzw
postponement status %@
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoRestoreOS:]_block_invoke
Encode Failed
May due to an invalid IO Service
%@%02zX%@
bmu2-board-id
+[ZhuGeKeysActionArmory queryComponentAuthChipIDSN:withError:]
NUMBER_TRIM_SIZE_UNIT_CHARS
Error: RefCount reached its maximum value!
Unexpected nil config of key \"%@\"!
CFPreference API return error
Path not exists or the string is not a path
queryExternalDisplayBacklightUIDWithError:
i
Failed to check dependency for key \"%@\" in path \"%@\"
Method \"%@\" of key \"%@\" has a non-number timeout
printfErr == offset
SIM_MUX verified: Device is in P+P configuration
Failed to get length for str1: %@, error: %@
Failed to retrieve Secure Element!
VgWVrLlQU2UvcGFbcIufd2AwKkT5U+ZXrdjwkciFRKQAE
com.apple.BiometricKit
CopyIdentifier
Trying IO service entry \"%@\"
khQ6/64HBXiF12L+ikQM+18cKR8mllprzF7FjID+1xKWg
%@ms timeout for method \"%@\" of key \"%@\"!
YsAbn1q6x+q9+Xdb5GZbm23p1YMig5ka1M7Dfnng81vWM
CTMobileEquipmentInfo does not have property %@
aObfuscatedString pointer is nil!
Will invocate for dependency \"%@\"!
DebugArgs
Creating regEx failed for checking flexible key \"%@\"!
This special error code is used for ZhuGe configuration analysis
\"%@\" of entry \"%@\" is class %@ while expecting NSNumber
k2L0muVU/NTtMtzysnNs210RDcjTSFUOp9M9EJEp0hvNs
Failed to get response from eUICC operation! Error code: %@
Configuration of key \"%@\" has an invalid retry number: %@!
Key \"%@\" may need further check
IOService
Key \"%@\" is repeated in %@!
Cannot connect to lockdown daemon via a local socket
ACTION_ENTITLEMENT
RearCameraAuthICChipID
Failed to query WLHWIdentifier for property %@, no matching key found in %s
sQlgU/hLxqme+OsLfVFJ822oV5I22G2S9IwE7gSKOJvAE
5naLQAP8rbYbM+dDqBTdG12FDdDJA2iGVuiKxLbZmjOVg
raw-panel-serial-number
IODeviceTree:/chosen
Preference of key \"%@\" has an invalid retry interval: %@!
Failed to get properties for key \"%@\" in MERMAID!
Failed to get flexible list from keys config, error %@
Path Invalid
Please check regEx related code in ZhuGe
Code Max
Failed to match parent class of entry \"%@\" for key \"%@\"!
AMFDRLogSetHandler
Invalid full path to search property \"%@\" for key \"%@\"!
Query wifi-module-sn fail, type %@, data %@
RoswellAuthI2CRelayInterface
Get the component index number is : %@
queryBasebandFirmwareSecurityInfo:withError:
queryMogulIDSN:withError:
ZhuGeArmory
MGkey pointer is nil!
RETURN_REVALUE_OUTCOME
EMPTY_ARRAY
Key \"%@\" is not converted, keep original value %@
Please check whether the key or alias input correct, or implemented.
Mogul is not ready via AID, result: %s
key %@ does not exist in firmwareUpdateInfo
-restore
key pointer is nil!
serviceClass
9aOxr1//Y8XlITR3p5/CT1Amyb/Z9TI/b88Mi/ETgB8oM
/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c
Failed to query isEuiccActive: %@
ZERO_NUMBER
Failed to get properties of \"%@\" for itself!
path
Please make sure the option is correct
(IO[a-z]+)://(.+)/(.+)
+qluw9N3tQ6lWJQydep/p0Esxk6EuILApUlLaNC16MfYc
Failed to get CTServerConnection instance
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m
Failed to act for key \"%@\"!
Please check path of the code calling CFPreference
Unexpected SMC Key Size returned
+[ZhuGeKeysActionArmory querySPUProperty:withError:]
Failed to get MobileEquipmentInfo: %@
needOverride pointer is nil!
Cannot find service class: \"%@\", %s
parent class and name
AppleH1CamIn
+[ZhuGeKeysActionArmory queryThreadRadioMacAddress64BitWithError:]
+[ZhuGeBasebandConnectionArmory getCTServerConnection]
GPXrJXV9cmnYFY6vDzNBd0BJ83EQQN8iNp2FlUkSsaSA4
_connectHandleRefCount < 4294967295U
Failed to get aliases map from keys config, error %@
Get failure when calling API of SecCertificate
%02x
propertyValue
SYSCFG
+[ZhuGeKeysActionArmory queryFDRSealingStatusWithManifestOverride:WithError:]
Parent entry is \"%@\", class is \"%@\", name is \"%@\"
kVinylEUICCPairingIdentifier
NUMBER_SINT64
ACTION_METHOD
Near Field API Failed
Type of some object is invalid
UZxSgv2us0ZfhXwIhUX7a0FiCXZhsoLlXmkH6rQVODX9s
string
Option ROM Version
Key \"%@\" doesn't define actions
Failed to open IO Master port
Please make sure the Caller has the correct entitlement
Unsupported type \"%@\" for criterion \"%@\"
readPropertyFromComponentAuthService
uU6Q/yVGRbrIwfV5JhBYH11bVr+w7C8fkcxwcwEsQQxek
bufferSize
Key \"%@\" doesn't define argument for action \"%@\"
Initialize config for ZhuGeArmoryHelper instance \"%@\"
\"%@\" of entry \"%@\" is class %@ while expecting BOOL<NSNumber>
integer:0
wasRetained
com.apple.ZhuGe.ZhuGeBaseband
ReleaseType
=
RETURN_REVALUE_VALUE
STRING_UPPERCASE
ACTION_ARGUMENT
CFPreference Error
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
-[ZhuGeBasebandPostponementStatusArmory loadPostponementStatus:]
postponementStatus is reloaded
The path just doesn't exist or the way to find the path is incorrect.
FDR options is %@
AppleOLYHAL
Failed to query wifi-module-sn from ioreg path %@!
Failed to get touch screen cert from ioreg
IODeviceTree://chosen/mac-address-ethernet0
Checking entry \"%@\", plane \"%@\" for property \"%@\" with direction %@,
AppleH2CamIn
querySysCfgKey:withError:
EMac
queryFDRSealingStatusWithManifestOverride:WithError:
5eXj+hsAOI+a21+Lu3eMC13BVB7Ac992kT1Vd8WoCUiOE
One graphic in graphics array is not a dictionary, ignore it.
Key \"%@\" defines a empty method for action \"%@\"
wifi-module-sn
Did not find config of key %@
sppci_model
atm_diagnostic_config
Flexible key \"%@\" only has %@ subkeys while requring %@ subkeys!
Key Not Found
Failed to get parent entry of entry \"%@\" for key \"%@\"!
Failed step2 to get parent name of entry \"%@\" for key \"%@\"!
AppleH6CamIn
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeArmory.m
Call Back Function Not Found
SP Data Report Invalid
dependency pointer is nil!
-->
Failed to match parent name of entry \"%@\" for key \"%@\"!
YwMa8PyxriC0h96yJPyvz110EsCWKO7txsHYVZNN7KEps
Failed to match parent class or name of entry \"%@\" for key \"%@\"!
AzRjL78vqZvv+67BDObFP1BuLaSpSTaRpPUKVhQGQp45w
pServiceMatchingMethod pointer is NULL!
Failed to update properties for key \"%@\", error %@!
-[ZhuGeArmoryHelperArmory getPropertiesOfKey:withError:]
The input data may be unexpected and cannot be processed
AMFDRCreateWithOptions failed!
P
Q7oU1FM7t+//vn8mEzH061EmoC99VGc8umtJUlLoEuOPY
%s%d
Please check the CLI option that input
Please make sure the correct SE type is input
Please check sysdiagnose for more detail
{\n%@%@\n%@}
backglass-compass-serial-number
CertificationPublicKey
Key \"%@\" dependency got deadloop
Method \"%@\" of key \"%@\" doesn't exist!
Key \"%@\" does not match any definition!
Please check latest code that using ZhuGe error API
Failed to search property \"%@\" for key \"%@\"!
SNRaw
+[ZhuGeKeysActionArmory queryFactoryShippingSettingTimeWithError:]
%s <%s %s(%ld)> ERR: 
Config of revalue \"%@\" is not a dictionary
Outcome config of revalue \"%@\" is unsupported!
{
Failed to get properties of \"%@\" for subkey!
ID
DRHpQ4yYNpFi5QjmIq+Y810Pw1l7FsGmAoX3s4cTiJYmY
v16@?0@\"NSNumber\"8
Failed to resolve dependency \"%@\" for key \"%@\"!
ACTION_DEFAULT
Decode Failed
XPC service name may be invalid
Failed to get io service iterator from \"%@\" for key \"%@\"!
Unknown sensor state received!
queryCentauriSikPubWithError:
Case \"%@\" and class \"%@\" mismatched!
Some internal issues happened when converting data
Permission Denied
Cannot look up \"%@\". System errno=%d errstr=%s
Failed to query Centauri Sik Pub!
jf+movONCK+lGgv8Y7TQ812yC7fbxm9/zB8+a8Uxem6c8
YonkersIR1UID
-[ZhuGeMobileEquipmentInfoArmory loadMobileEquipInfoList:]
In %@, aCache pointer is nil!
rawConfig pointer is nil!
BackSuperWideCameraSNUM
p/WRH+Et8QKgGhS/ov82N219tUCy3Wu9eyWTS5gvqBY1A
WCzva5VLvofdVaqMS6Ap917z9HXFlBToosgmEDJBalieM
buffer
Method \"%@\" of key \"%@\" has a non-dictionary retry!
p_config
Please check whether the path using is correct
MesaSensorIDSensorSNBufferSize %zu, should be %d
8jvikGIcqTbQS4FdgY3t6160TElV+a3nnrgv6KQmmRbsc
+[NSArray(ZhuGe) arrayFromShellCommandString:]
-[ZhuGeArmoryHelperArmory getPropertiesOfKey:withError:]_block_invoke
Invalid ZhuGe Error Code!
Integer \"%@\" of entry \"%@\" is %@ while expecting %@
readAccessoryCertificateAuthCP
Device ID
Name of queried sysconfig key might be wrong
Failed to match the service class \"%@\"!
ProvisionedLockedWithUID
Output is too long (%@ > %@) for SPU property \"%@\"!
propertyValueRef
BBUpdaterExtremeCreate failed to create an updater
Sysctl Failed
option is not a dictionary
Failed to decode AccessoryCertificate
sensorID
, 
XPC Service Not Exist
ZhuGeErrorCode %@ exceed maximum
option is nil
Failed to query \"%@\"!
UpdateBaseband
ZSWBgzP2yLseFXKsNKKMC0D7VhPb8UXsL1ynXSrA9r3MI
getFDRDataByFDRClassWithError
Please check whether the user has the privilege
Tries All Failed
The key is not supported by MobileGestalt
6Q2HUd0W2HvvW1uXtIrXh0BgG9/ymV6FwuWvCVnjBLnag
fail to load BBUpdaterExecCommand from BBUpdater dylib
NUMBER_SIZE_GIB
Error System Issue
SMC Key Size Unexpected
+[ZhuGeKeysActionArmory queryThreadRadioMacAddressForProvisioningWithError:]
read IDSN failed, errorcode: %x
YK1jvTHgjdt2Od1g1cGNg1EzY5VLX6jKTt3wQupFvEbI8
Key \"%@\" defines a non-string method for action \"%@\"
Dylib Not Available
Failed to get IO properties from service entry %@! %s, a potential issue!
queryIOCameraByProperty:withError:
number:
CENGetSiKPublicKey is not supported!
%s %@
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
-[ZhuGeArmoryHelperArmory pickFlexibleFromUnionizedConfig:withError:]
AMFDRSealingMapVerifyAsidMetadataForDevice failed!
direction
Found 1 property \"%@\" for key \"%@\" with non-fullPath
IOObjectRelease(service) == 0 
ALIAS
Please check sysdiagnose lockdown related log
servicePlane
Failed to get valid data for \"%@\" in restoreOS!
failed to get errorcode response: %x
Nothing Wrong
The string is not a valid ZhuGe key
Current OS is not defined
EID
a cert
eiBoDNfdjGI+4DTEZmHZB18Dyio2oSnjU9BjtR0BFWARY
STRING_TRIM_SIZE_UNIT_CHARS
Failed to get properties for key \"%@\" in TAUREN!
Get failure when calling API of libFDR
queryMesaProvisionStateWithError:
H70NRtAMRoBV3+QCls5nJ082VJDNyJHgTfyr6AU66Z5gs
qcLoMoHuqwN9l2o0uaPaq0FGgheBaItLe5TCoQ5VCxqiw
Implementation error: Connection handle to AppleBiometricServices has a refcount of zero and should be null but the handle is non-null!
Error: Connection to AppleBiometricServices could not be initialized!
%s://%@/%@
Failed to weak link near field framework!
Q
Preference of key \"%@\" has a non-number timeout!
Preference of key \"%@\" has an invalid retry number: %@!
%
Alias \"%@\" is duplicated with keys!
SP Exited
Sysconfig Key Invalid
Unsupported entitlement or the entitlement type
-[CTMobileEquipmentInfo(forUndefinedKey) valueForUndefinedKey:]
-[ZhuGeArmoryHelperArmory getSubkeyOfKey:withError:]
bool:
NSString \"%@\" of entry \"%@\" is %@ while expecting %@
Failed to weak link libnfrestore.dylib, NfRestoreSEEnumerate isn't available!
Unknown Mogul Type
failed to get read memory response
Properties of key \"%@\" is: %@
%x
r8L1DAtjrZMjuEhYjJB6J0DmQfsy8VWuW95w7j+wYUmfI
IOSERVICE_WLAN
can not find baseband class
FrontCameraModuleSerialNumString
Input may be missing subkey(s), or something wrong with flexible pattern definition
The system profiler exited
readIDSNAuthCP
UnknownFile
%s ERR: Restore log connection error: %@
Timeout
The data indexed by the indexArray is not valid
mogulTopModuleSecondary
One graphic in graphics array does not contain \"sppci_model\"
File Open Failed
Get failure when calling API of Img4
parent class
AppleARMSPIDevice
SUPPORT_RESTOREOS
Failed to convert format for key \"%@\"!
FLEXIBLE_PATTERN
EMc2
-[ZhuGeBasebandFirmwareSecurityInfoArmory query:forceCacheable:withError:]
Got IO service iterator for \"%@\"!
Please check the name that being querying
+[ZhuGeBasebandArmory queryCHUnitSimMuxDualPhysicalStateWithError:]
Key of dictionary is redundant
SealingManifestOverride
Checking in self node for property \"%@\"
Vendor
TMac in sysconfig dictionary is with invalid length.
fail to load BBUpdaterExtremeCreate from BBUpdater dylib
Lockdown Connect Failed
true
ChipNumber
Stepping
Duplicated dependency \"%@\" for key \"%@\"
PRIVILEGE
Data Convert To Nil
May due to an invalid IO Service connection
Nm1YmAePxemPeq+uQQ9o521b7ifMduKD62l3Hviu/BoUs
bBUGOKyRf8JC1/kbTQbCp0C7Gf6xGsFgHS8xrmZbHlrJQ
Chipset Model
-[ZhuGeArmory actForKey:andName:andConfig:andOptions:andPreferences:withError:]
The dylib does not exists or too old version
Creating regEx failed for IO query!
Unexpected length of wifi-module-sn: %@, expecting length %d
w
\"%@\" is not a valid data criterion
+[ZhuGeKeysActionArmory queryIOCameraByProperty:withError:]
IOService://AppleProxAbstractHIDEventDriver/SerialNumber
EMa3
String is invalid, like unpaired quotation, bracket etc.
Failed to query property %@! after trying all methods
ModuleVersion
Unknown SE Type \"%@\"!
System Secure Element Serial Number
RLi/BisKjNTSYXoStoELs1FSND6rfSKuGpBJ4E0g8Wfd8
-[ZhuGeCacheArmory setCache:forKey:withError:]
Maybe the method name is incorrect
Maybe the name for querying is incorrect
Failed to match parent class and name of entry \"%@\" for key \"%@\"!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeBaseband.m
RETURN_REVALUES
No property \"%@\" in entry \"%@\"
fillmore
IDSN
PropertyList Serialization Failed
Searching from non-fullPath services.
device_type
ProvisionedUnpaired
IOService://IOMedia/Size
Failed to run for dependency \"%@\" for key \"%@\"
parentName
Read WLModuleSerialNumber, output %@
+[ZhuGeKeysActionArmory queryVinylEUICCCSNbyKey:withError:]
Pattern string can not cover the case
Entitlement Mismatched
Failed to read \"%@\" from sysconfig dictionary
JCOP Secure Element Serial Number
XJmjmvrLmAug+1qdKaBX910Aji9wPl4nTnUhrN8zNbZpw
Required size is %@, while usually it should be %@ or %@ or %@ or %@
SMC key information indicate a wrong type
FDR options is not a dictionary \"%@\"!
SysCfgDict
No property: %@
V+FPtV8y9rZfentcqCYeL1F22eWzbGyVPgBgIEoydQw4k
IODeviceTree:/baseband
dependency \"%@\" format is wrong!
XPC Service Entitlement Missing
+[ZhuGeKeysActionArmory queryDisplayUniqueChipIDWithError:]
Argument type \"%@\" is incorrect for IOServiceMatching!
Key \"%@\" defines a non-string access
ZhuGe Key Not Native Supported
This error code should never be reported
+[ZhuGeKeysActionArmory querySysCfgKey:withError:]
ProvisionedWithGID
queryNFSecureElementByKey:WithError:
yTyKhgkJ+N+ZMHJDz95Gb0BK1bLAMFxFm3aqAYh69bBo8
Wrong key or the key is not configured
PFSN
cannot get error code, result: %s
WMac
logCallBackForVinylEUICCWithLevelFormat
mogul,a1222
Failed to get properties of \"%@\" for alias!
Img4 API Failed
Get the flag number is : %@
raw-panel-serial-number-2
IOService://sdio/local-mac-address
Configuration of key \"%@\" has an invalid retry interval: %@!
Revalued key \"%@\" to nil intentionally!
Specific function isn't supported in current OS or environment.
%s\n
ACTION_RETRY_INTERVAL
Failed to get valid data for \"%@\" in bootedOS!
Failed to get MesaProvisioningState, returned error 0x%08x
queryScreenSerialNumberByProperty:withError:
VRAM Size
\x85
CopyAllowUnsealed
Please make sure the file exists
Pointer Null
extra
/System/Library/CoreServices/SystemVersion.plist
aObfuscatedString length is incorrect!
Didn't successfully call init related method
panel-serial-number
DERParseSequence failed to decode cert chain with der state %@!
integer:1
WRN
did not find plain cert
nova-serial-num
*bufferSize > 2*(sizeof(sensorID)+serialSize)
Failed to query supportsDynamicSIMConfiguration: %@
Failed to get fwSecurityInfo: %d:%d(%s)
Failed to get properties for key \"%@\" itself!
-[ZhuGeArmoryHelperArmory getObfuscatedKey:withError:]
+[ZhuGeKeysActionArmory queryNFSecureElementByKey:WithError:]_block_invoke
ofKYA7HqFrx8cnA8dcfB627DgJl7n7nPu7EM0tRG1SEdY
I32sGclpgl5VujQRJxyhKQ
Object Length Invalid
ZhuGe only supports absolute path, caller needs to convert relative path by itself
BasebandUpdater
fail to strip root sequence
hj0kXUT8dWr2Uy8kgsYzv1E2Gvl0NncSrj0ngVjgeDLVU
Please check sysdiagnose for more clue
Failed to get MesaSensorIDSensorSN, returned error 0x%08x
can not find property %@ under %s
unionizedConfig pointer is nil!
Trying to get IO iterator with condition of \"%@\"
M
seList pointer is nil!
com.apple.zhuge
Near Field SE Type Invalid
Argument type \"%@\" is incorrect for IOBSDNameMatching!
IO Service Mismatching
Didn't find the expected path
yes
bmu-num-enabled
tcon-api
als-md-mlb-serial-num
/YYygAofPDbhrwToVsXdeA
XPC Service Connect Failed
touch screen cert has %ld bytes, returned without decoding
pcrt
ip2drLzT5EvOXD6cPP5rU2AbR9glnV9CPclFfGGNV5y/A
Ny83MdAFmn0Klc53MPhcJ121gbiy5Y4e1NHpKdaQ3+hrg
queryDisplayUniqueChipIDWithError:
4QXj82hRhZ6/k74y2qWao0BROSL65x+Bvew1MAHwp6RZw
Querying the key: %@
Failed to get tcon API!
Failed to open IO connection for \"%@\" due to %@(%@)!
-[ZhuGeArmoryHelperArmory getPrimarykeyOfKey:withError:]
All possible tries has failed
mogulLAS
RETURN_REVALUE_DEFAULT
BackTeleCameraModuleSerialNumString
/usr/lib/libBBUpdaterDynamic.dylib
Flexible key \"%@\" is missing subkey(s)!
bg-magnetometer-serial-number
P4vgmVNL1cIFO9Qi+yX9t0AckhWpSpeq5SpH7rTu9tNMA
%@%@
Implementation error: Connection handle to AppleBiometricServices has a non-zero refcount and should be non-null but the handle is null!
fail to dlopen BBUpdater dylib with error: %s!
getIOConnection
p_subkey
ZhuGe Error module itself got some issues
Current process is not a XPC service process
IODeviceTree://chosen/mac-address-bluetooth0
STRING
Preference of key \"%@\" has a non-number retry interval!
ZhuGe Key Not Supported
service plane
%lu
coverglass-serial-number-2
IOSERVICE_ETHERNET
YonkersIR1ChipID
^(?:$superkey)(.+)$
Vinyl error code: %@
MMac
IOService://marconi-wifi/local-mac-address
als-md-sensor-flex-serial-num
centauri
AMFDRSealingMapVerifySealing
pmu-follower-serial-number
Error config of revalue \"%@\" is not an array
-[ZhuGeArmory verifyDependencyWithError:]
Preference of key \"%@\" has a non-number retry number!
auth,display
fail to decode content
Key \"%@\" defines a non-array dependency
May due to wrong implementation or system problem
OS Unknown
Caller's entitlement value is mismatched with required one
Failed to get registry properties
Value config of revalue \"%@\" is not an array
Check error description to understand failure reason
Querying %@ of Secure Element.
Failed to get sysconfig dictionary!
ERR
Index %@ of ZhuGeErrorCode table got a wrong code %@
DERParseSequenceContent failed to decode into validity with der state %@!
-[ZhuGeModuleArmory initWithError:]
bmu-num-supported
CLI Option Unsupported
ACTION_QUERY_PATH
%s ERR: Cannot print serial log!\n
\"%@\" doesn't exist in entry \"%@\"
v16@?0@\"NFHardwareManager\"8
Length of sysconfig key %@ is wrong, expecting 4!
xlNWiCzpngNoAeP0QHH+m14YQmhHOMAr8wVl3QH5rfgAU
ZhuGe is runing on an unknown OS!
Please make sure the domain is correctly inputted
No matching services for AuthCP: %s, skip reading from it...
Bqxx4pprqbYXTAyEXXvN312TS9ZrRHvd5gfR5+U9g2F74
ROM Revision
parent name
local-mac-address
Unprovisioned
Successfully read AccessoryCertificate from AppleAuthCP AID service.
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoRestoreOS:]
EMPTY_STRING
$subkey
Please check whether device supports the service
no
Failed to find a non-fullPath service for path \"%@\"
The ACE command returns an error
Please check if you really want to try this function in current OS or environment
ProvisionedWithUID
AMFDRDiagnosticGenerateReport
getConfigDict_block_invoke
+[ZhuGeBasebandArmory getBasebandClass]
Failed to open a valid IO connection for \"%@\"!
Check the string in code or input source
als-tb-sensor-flex-serial-num
Failed to get FDR data for class \"%@\"!
p_is_alias
Failed to obfuacate super key of \"%@\" in range<%zu, %zu>!
Path of IO entry might be wrong
Platform
mogulTopModule
ComponentFunction
qXLtae9hyCs7VeXhQLkRM097iiuk2VDpWcN4E56+F84hE
p_primarykey
Unexpected nil primary key of key \"%@\"!
Failed to read AccessoryCertificate of mogul based top module
MFTFDybYdMEa3t7lEekmZ0DVntZfm8FTx8hVssqp6sQ80
%s ERR: Failed to get a restore log proxy!
aString pointer is nil!
Didn't get properties after obfuscating \"%@\" for key \"%@\"
User defaults doesn't support the specific domain
Didn't successfully verify fdr data sealing status, error %@!
Yes
child
cannot allocate space for idsn data
null or empty pkcs7 cert content
ENTITLEMENT
Option of the CLI command is not supported
AMFDRDiagnosticGenerateReport failed!
%@:/
+[ZhuGeKeysActionArmory queryBMUExpectedBoardIDWithError:]
DERDecodeItem failed to decode validity notBefore time with der state %@!
pNbNAqd6QFlv6xayKmTAf14Qa69vrR7VZDaFl+WwyDULY
_connectHandle != ((io_object_t) 0)
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m
service pointer is nil!
Failed to create a matching dict for service \"%@\"!
Dependency of \"%@\" is not ready, error %@
Please check sysdiagnose FDR related log
Device may not support the service
FDRDeviceAsidMetadataIsVerified_Options
Error: RefCount equal to zero is trying to get decremented!
Failed to link libFDR dylib!
Issue may be due to the underlying error out of ZhuGe
Please check whether there is any underlying isse in the decoding API.
XPC Service denied access due to lacking of entitlement
ModuleName
No data for property %@, field %@
IOService://AppleHPMDevice/UUID
NUCsgvu+SXiI5u3u8TzQG0Fv4m3ytDyk6B9u0YYgbIPIY
Argument type \"%@\" is incorrect for IOServiceNameMatching!
Failed to decode with proper API
%02X
printfErr == 2
BBUpdaterExecCommand(CopyIdentifier) failed: %@
The system profiler report failed to be created
+[ZhuGeKeysActionArmory queryIOProperty:fromCriteria:withError:]
+[ZhuGeKeysActionArmory queryNFSecureElementByKey:WithError:]
FSRsyiOWdf4OCG6zvks590DxmrR3/XoDhE85oTuP1f480
IOS
Failed to get config for dependency \"%@\"!
Key \"%@\" revalued value is %@, error is %@
Cannot create CF property for property \"%@\"!
C
AkfIj49PscGvuFSmdygUq10dr0OOsjzBlVg1cnpJVQO/M
sg1SrHyuq7Uu15zGYwGGz1CjjOASEqn31w0kiAkOfUKt0
RETURN
Failed to get properties of \"%@\" for config!
Method Invoke Failed
ecid
+[ZhuGeKeysActionArmory queryBasebandFirmwareSecurityInfo:withError:]
Unknown mogul type
AppleBiometricSensor
NUMBER_UINT32
Lacking of criteria \"fullPath\" service or not!
No
NSData \"%@\" of entry \"%@\" is %@ while expecting %@
logCallbackForSyslogCDPWithLevelBuffer
Default component found
6LFIpJX7gwmw6i+QUugjN16ftZ0ANUfFRD0/FcFGGjdlo
AppleBiometricServices io_service_t failed to be released!
+[ZhuGeBasebandArmory isBasebandReady]
MGQuery
Get IDSN from AuthCP: %@
ProvisionedWithTest
firmwareSecurityInfo is reloaded: %@
Failed to get properties for key \"%@\" in overall range!
User have no proper access
AppleAuthCPAID
Unsupported SPU property \"%@\"!
-[ZhuGeArmoryHelperArmory propertiesByKey:andSuperKeyRange:withError:]
Please check whether the dylib provided correctly
Please check sysconfig key name input
Failed to get IO properties from entry \"%@\", %s
AMFDRCreateWithOptions
fail to decode ContentInfo
zhuge_debug
Class Type Wrong
Please make sure the key being querying correct
Cannot find service name: \"%@\", %s
Failed to get a connection for AID Bus!
invalid decoded plain cert: [%p:%zu]
SerialNumber
$option
Flexible ZhuGe Key Invalid
The system profiler report crashed
Find service class: \"%@\"
decodePKCS7TouchScreenCert
Usually this error code shall not be displayed
+[ZhuGeKeysActionArmory ZhuGeToDo:withError:]
Failed to get ScreenSerialNumber
0qO8mRy+jZlCdJFm2K3Zl19kvekAelETHsWb+9scmH8hI
STRING_MAC_ADDR_SYSCFG_6BYTE
Key \"%@\" original value is %@, error is %@
Didn't successfully get data due to lacking of specific hardware
+[ZhuGeKeysActionArmory queryFDRDeviceAsidMetadataIsVerified:withError:]
+[ZhuGeKeysActionArmory queryWLHWIdentifierInfoByProperty:withError:]
getObfuscatedString
ALL_ZERO
STRING_SIZE_GB
q24@?0@\"NSString\"8@\"NSString\"16
service name
Failed to query property for %@, error %@
kVinylFwUpdateCsn
com.apple.AppleDeviceQueryService
AppleCBTL1614Device
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
%s%s\n
+[ZhuGeBasebandArmory getProperty:inPlane:withName:withOption:]
Quotation \"%c\" is not paired in command \"%@\"!
NUMBER_SIZE_GB
RETURN_FORMAT
Failed to call SMC APIs, unsupported SMC key etc.
service class
IOService://AppleTCONControl/module-serial-number
+u7dB6GE+RzxUTEJzzjGS16kN811vk8Oia1lGFoLWCZdE
IO Service Open Failed
Uninitialized
MSB
Alias of key \"%@\" is not an string!
Please check whether the call back function name exists in the library
Please make sure the way using ZhuGe is correct
SP Data Type Null
Underlying service may be not ready
AppleH4CamIn
ZhuGeLog
tmpString length is incorrect!
getElucidatedStringLen
returnValue pointer is nil!
Get data <%@> of property: %@
BMac
After %@ ms, retry %@/%@ times for method \"%@\" of key \"%@\"
SecCertificate API Failed
HWIdentifiers
queryFactoryShippingSettingTimeWithError:
\n
Failed to initialize a module instance!
-[ZhuGeBasebandFirmwareUpdateInfoArmory loadFirmwareUpdateInfo:]
ACTION_RETRY_NUMBER
Please make sure the entitlement is correctly configured
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
parentClass
HNRRSHuuTAZ59tHGR4NbA1Fisf/bq+UFvYjF0qeAbGFSo
4kQV96buQ1aquc9FF+wrG25mwAi9lpBZByqq6XYGVVB14
RESTOREOS
VerifyData
fail to create plain cert
RearCameraAuthICUID
RETURN_CASE
Check error description to find out recvoery suggestion
We may need to check with libSMC together
number
key pointer is nil
rpcp
string length should not be zero!
Failed to get keys config from raw config, error %@
Please make sure the process is using memory reasonably
all
BSD Name
TeSXZEwq35nFS8donhmyb1Ck5VDKjR5ddJ3qChRQGO+WU
INF
kCTPostponementStatus
IODeviceTree:/options
Failed to get plane entry for key \"%@\"!
IOSERVICE_SDIO
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeModule/ZhuGeModule.m
The size of %@(less than %d) isn't correct: %@!
nhuNuIQn8s2Vrcmy9g8PD1B6i3c7ZmQEK1utNTKO2vHUo
Key \"%@\" contains non-string alias
Flexible key doesn't macth its pattern
Please make sure the key string is correct
Checking dependency \"%@\"
Query key: \"%@\" without time limitation
Found %@ property \"%@\" for key \"%@\" with non-fullPath
+[ZhuGeKeysActionArmory queryScreenSerialNumberByProperty:withError:]
ComponentType
/dev/console
FDR API Failed
BOOL \"%@\" of entry \"%@\" is %@ while expecting %@
+[ZhuGeKeysActionArmory querySysctlVariableName:dataType:withError:]
err != (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x1)
Failed to get length for str2: %@, error: %@
Please file a radar against \"ZhuGe|all\"
Path or name of XPC service might be incorrect
Failed to search property \"%@\" for key \"%@\" due to a nil service plane!
Bits will be truncated since real size is %@, while required size is %@
Current process priviledge is not allowed by Key \"%@\"
Failed to initialize an instance for ZhuGeArmoryHelper!
Serial
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeArmoryHelper.m
Got properties after obfuscating \"%@\" for key \"%@\"
XPC Service Not Available
Please check whether the path of XPC service correct and existing
Failed to weak link libVinylNonUpdater.dylib, VinyleUICCPerformOperationWithLogSync isn't available!
v24@?0@\"NSData\"8@\"NSError\"16
key %@ does not exist in firmwareSecurityInfo
BOOL_POSITIVE
Please check the data source or code
hw.product
7tFI/Pj8fSzpumF8D8YsF2Bv0TS4DIqwHyG+SPrv1BCaU
Restore OS: loading firmware security info via BBUpdater
NUMBER_UINT64
BOOL_NEGATIVE
Hit cached properties for real key: \"%@\"
No SMC service available on this device.
esdm-fuses
NULL
Failed to get a connection for pressure!
+[ZhuGeKeysActionArmory queryExternalDisplayBacklightUIDWithError:]
baseband class: %@
eUICCPairingIdentifier is reloaded
Length of some object is unexpected
bmu-board-id
ProvisionedUnknownKey
<%@ %@(%@)>
-[ZhuGeMobileEquipmentInfoArmory query:ofSlot:isCachable:withError:]
UNKNOWN_OS
format is invalid!
Format \"%@\" and class \"%@\" mismatched!
Method \"%@\" of key \"%@\" has a non-number retry number
Object Type Invalid
failed to read IDSN data via AID, result: %s
GCTLLrRCKiXGd80/EQDwd080a0NacPCy4eEn6racjYhN8
Unexpected nil isAlias of key \"%@\"!
basic
service
Iay9Sr+EgQjh8wCawoxNP10KX4+UsX2CXjihZPv1EcZPk
Key \"%@\" doesn't define method for action \"%@\"
Maybe the method itself got some issue
Unsupported SE Type
Failed step1 of matching \"%@\" for key \"%@\"!
auth,mlb
SEs5TXAVh1zo4q7nzd6BI0A/2poOxsJ4U7WDQ9fbQe1vw
RN8kLj4030Fn1SvU0Woix2BHxZAAMREu2PbvTnt3fTmzw
Failed to verify for key \"%@\" in dependency \"%@\"
Please make sure locakdown daemon and local sockets work well
AppleH9CamIn
AppleAuthCPRelay
fail to decode SignedData
User Defaults Domain Not Exists
Xacf3g3sv/7PX2J9rFL9z072dgMx0j9mwYTqP80jkZRAA
ZhuGePrintStderr
key %@ does not exist in postponementStatus
Key \"%@\" defines a non-array user privilege
Key \"%@\" is defined action sequence with no action item
size == sizeof(state)
format pointer is nil!
STRING_VISIBLE
^(.+)(?:$superkey)$
IO Service Get Failed
Value Out Of Range
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeKeys/ZhuGeKeysAction.m
disk0
Failed to get eUICCPairingIdentifier!
AppleDeviceQueryService
May due to an invalid IO entry
Option or input value is not in defined range
Find service name: \"%@\"
Failed to get IO service iterator for \"%@\" due to %@(%@)!
ACTIONS
Data Convert Failed
SMC Key Name Invalid
%d
Atl1ygbcnX05i/r/gHKSk120MRi9vBhvi9JojCVetjyLc
IODeviceTree://chosen/effective-production-status-sep
 KkMmGgTtBb
DEPENDENCY
Alias \"%@\" is duplicated in keys of \"%@\" and \"%@\"!
Failed step1 to get parent class of entry \"%@\" for key \"%@\"!
integer:
isMogulService
BBUpdaterSetOptions failed: %@
Argument type \"%@\" is incorrect for IORegistryEntryIDMatching!
EMPTY_DICTIONARY
-[ZhuGeArmory queryKey:andOptions:andPreferences:withError:]
$superkey
p_obfuscated_key
Maybe the method name or signature is incorrect
Operation is not done in certain time
This failure is intentionally, please check the input data length, content etc.
ZhuGe Key Further Check Needed
+[ZhuGeKeysActionArmory queryIOPropertyFromPath:andCriteria:withError:]
-l 0xFFFFFFFF -v 99
ZhuGeBasebandFirmwareUpdateInfo query:%@ isCachable:%s
pressure
fdr-product-type
YonkersIR2ChipID
%@
Error Customized
ACE Command Failed
SMC Key Type Wrong
V
logCallbackForSyslogWithContextLevelFormat
BMc2
fail to create an option CFDictionary for BBUpdater
Wasn't successful to find a matched revalue pattern!
The key is not a ZhuGe native key
backglass-serial-number
v16@?0@\"NSError\"8
STRING_MAC_ADDR
AppleH10CamIn
Failed to find AuthCP service: %s, skip reading from it...
NSNumber \"%@\" of entry \"%@\" is %@ while expecting %@
als-rear-serial-num
IO Property Not Found
Memory is not enough
Initialize keys config!
xsY3cS4aDX96XNwVKUi7L08r7F8ncE7jhvsPDL61Eg9LM
can not find entry at %s
So far so good, keep going
Option Unsupported
listSecureElementsCallback
YonkersIR2UID
baseband
FDRClass pointer is nil!
Outcome config of revalue \"%@\" is invalid!
Found property \"%@\" for key \"%@\" with fullPath
ZhuGeBasebandFirmwareSecurityInfo query:%@ forceCacheable:%s
als-front-port-serial-num
xZzLE50x6to8PZQH74StP1BZPsZBi5uXN0EBtMq6N9rAA
In %@, key \"%@\" got a wrong cache class type \"%@\"!
The option passed in is not supported
parentPlane
AMFDRSealingMapVerifyAsidMetadataForDevice
GW8jawjUZ/zcAuUmHkGbN27chdKx5AN/e8KCGpcUqktYg
7tlZ0ABSfOYXqMZAXN1431B1h+Br5M7upUxKdr6Xkc5t8
j2z/JVne3XTHRxqKe6Far0DTF7xLJ4qxJY55wPbx7RRKU
querySysctlVariableName:dataType:withError:
gOS
Specific Hardware Needed
ATE
kUmcdgObIa1Tmrury+vs80E+P7feurT7fjeBoSNzOjBrM
xg7hMKYgB3nm1AjjFLxRx0DEJEH2VRVTITfkK7F6q1llI
IOService://AppleARMSPIDevice/chipid
IODeviceTree://chosen/mac-address-wifi0
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
caseType pointer is nil!
Failed to load libFDR.dylib!
Searching property \"%@\" for key \"%@\" with criteria %@
Failed to get value of property \"%@\" due to %@(%@)!
function: %@, targetFunction: %@, type: %@, targetType: %@
%{public}@
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
!!! IMPL ERROR !!! RefCount is non-zero yet _connection is null!\n
getSensorProvisioningState(%p)\n
getSensorProvisioningState -> err:0x%x, state:%d\n
getSensorSerialNumber(%p, %p)\n
getSensorSerialNumber -> err:0x%x\n
getSensorID(%p)\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n
!!! IMPL ERROR !!! RefCount is zero yet _connection is non-null!\n
getSensorSerialNumber, retry: %d\n
getSensorID -> err:0x%x\n
getMesaFDRIdentifier(%p, %p)\n
getMesaFDRIdentifier -> err:0x%x\n
ZhuGeModuleArmory
ZhuGeBasebandConnectionArmory
forUndefinedKey
ZhuGeArmory
ZhuGeMobileEquipmentInfoArmory
ZhuGeBasebandFirmwareUpdateInfoArmory
ZhuGeCacheArmory
ZhuGeBasebandArmory
ZhuGeBasebandPostponementStatusArmory
ZhuGeArmoryHelperArmory
ZhuGeLockerArmory
ZhuGeBasebandFirmwareSecurityInfoArmory
ZhuGe
ZhuGeKeysActionArmory
ZhuGeSingletonArmory
ZhuGeKeysConfigArmory
```
