# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 506,320 bytes.

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
getSensorSerialNumber -> err:0x%x\n
getSensorID(%p)\n
getSensorID -> err:0x%x\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
getSensorProvisioningState(%p)\n
getSensorSerialNumber, retry: %d\n
getMesaFDRIdentifier(%p, %p)\n
getMesaFDRIdentifier -> err:0x%x\n
%{public}@
!!! IMPL ERROR !!! RefCount is zero yet _connection is non-null!\n
!!! IMPL ERROR !!! RefCount is non-zero yet _connection is null!\n
getSensorProvisioningState -> err:0x%x, state:%d\n
getSensorSerialNumber(%p, %p)\n
ZhuGeArmory
ZhuGeKeysConfigArmory
ZhuGeModuleArmory
ZhuGeBasebandConnectionArmory
ZhuGeBasebandArmory
ZhuGeMobileEquipmentInfoArmory
ZhuGeBasebandFirmwareUpdateInfoArmory
ZhuGeCacheArmory
forUndefinedKey
ZhuGeBasebandPostponementStatusArmory
ZhuGeBasebandFirmwareSecurityInfoArmory
ZhuGe
ZhuGeSingletonArmory
ZhuGeArmoryHelperArmory
ZhuGeKeysActionArmory
ZhuGeLockerArmory
systemOSSerialNumber
T#,R,V_configClass
ZhuGeToDo:withError:
count
initWithFormat:arguments:
stringByPaddingToLength:withString:startingAtIndex:
T@\"ZhuGeCacheArmory\",&,V_propertiesCache
getPrimarykeyOfKey:withError:
macAddressStringFromData:
meInfoList
propertiesOfKey:withError:
queryNFSecureElementByKey:WithError:
setPropertiesCache:
_flexibleList
hasPrefix:
isEqualToNumber:
stringByReplacingOccurrencesOfString:withString:options:range:
_xpcConnection
escapedPatternForString:
lowercaseStringWithLocale:
queryIOPropertyFromPath:andCriteria:withError:
supportsDynamicSIMConfigurationWithError:
T@\"NSMutableArray\",&,V_dependencyPath
_aliasesMap
arrayWithArray:
_cacheType
boolValue
initWithCapacity:
numberWithUnsignedInteger:
runForKey:andOptions:andPreferences:withError:
_capacity
configClass
dictionaryWithObjectsAndKeys:
domain
numberWithUnsignedInt:
option
setTarget:
setXpcConnection:
_firmwareUpdateInfo
boolFromData:needNegate:
initWithData:encoding:
methodSignatureForSelector:
queryTouchScreenCert:
containsObject:
numberWithChar:
stringByRightTrimmingCharacter:
dataFromHexString:
sortedArrayUsingComparator:
numberWithLong:
environment
getObfuscatedKey:withError:
length
objectAtIndexedSubscript:
querySPUProperty:withError:
dependencyPath
invocationWithMethodSignature:
numberWithUnsignedChar:
queryFDRDeviceAsidMetadataIsVerified:withError:
queryThreadRadioMacAddressForProvisioningWithError:
T@\"NSDictionary\",&,V_firmwareUpdateInfo
.cxx_destruct
getCacheForKey:
_logHandler
getProperty:inPlane:withName:withOption:
queryExternalDisplayBacklightUIDWithError:
querySysctlVariableName:dataType:withError:
queryVinylEUICCCSNbyKey:withError:
T@\"NSDictionary\",R,V_aliasesMap
appendBytes:length:
isEqual:
setCache:forKey:withError:
setMobileEquipInfoList:
setObject:forKeyedSubscript:
characterSetWithCharactersInString:
numberWithUnsignedShort:
removeObject:
stringByTrimmingCharactersInSet:
T^?,V_logHandler
accessInstanceVariablesDirectly
uppercaseString
_keysConfig
capacity
countByEnumeratingWithState:objects:count:
query:withError:
queryComponentAuthChipIDSN:withError:
ZhuGeDescription
T@\"NSDictionary\",&,V_firmwareSecurityInfo
base64EncodedDataWithOptions:
numberOfArguments
rangeOfString:
scanInt:
sortAliasFromUnionizedConfig:withError:
stringWithFormat:
dataWithBytes:length:
queryIOCameraByProperty:withError:
waitUntilBasebandReady:retryInterval:
T@\"NSString\",&
_mobileEquipInfoList
arrayWithCapacity:
isEuiccActiveWithError:
sharedHardwareManager:
userInfo
_option
initWithBytes:length:encoding:
queryDisplayUniqueChipIDWithError:
numberWithBool:
config
getEuiccData:
loadFirmwareUpdateInfo:
T@\"NSDictionary\",R,V_keysConfig
T@\"NSDictionary\",R,V_option
key
getBasebandClass
removeObjectForKey:
replaceBytesInRange:withBytes:
sleepForTimeInterval:
T@\"NSMutableDictionary\",R,V_cacheDict
getReturnValue:
_cacheList
cacheList
isKeyAlias:withError:
T@\"NSArray\",R,V_flexibleList
dataUsingEncoding:
queryBasebandFirmwareSecurityInfo:withError:
setPostponementStatus:
slotId
T@\"CTMobileEquipmentInfoList\",&,V_mobileEquipInfoList
errorWithDomain:code:userInfo:
getKeyAndOptionFromDependency:withError:
numberWithInt:
queryThreadRadioMacAddress64BitWithError:
xpcConnection
numberWithLongLong:
setArgument:atIndex:
arrayWithObjects:count:
hasBaseband
loadPostponementStatus:
propertiesByKey:andSuperKeyRange:withError:
queryAIDTouchScreenCert:idx:withError:
setDependencyPath:
T@\"NSMutableArray\",R,V_cacheList
UTF8String
appendFormat:
getPropertiesOfKey:withError:
getSubkeyOfKey:withError:
isDataConvertibleToVisibleString:
pickFlexibleFromUnionizedConfig:withError:
unsignedIntegerValue
description
eUICCPairingIdentifier
getReportFDRDiagnosticFromOption:withError:
keysConfig
queryMogulIDSN:withError:
setEUICCPairingIdentifier:
_actionClass
getConfigOfKey:withError:
init
initData
initWithName:andCapacity:andCacheType:
rangeAtIndex:
stringValue
valueForUndefinedKey:
allKeys
propertiesCache
firmwareSecurityInfo
getCoreTelephonyClient
_firmwareSecurityInfo
intValue
getBytes:length:
integerFromCInt:size:isSigned:needSwap:
substringWithRange:
verifyDependencyWithError:
isBasebandReady
T@\"NSNumber\",R,V_capacity
hasSuffix:
printRemoteLog:withReply:
queryBMUExpectedBoardIDWithError:
queryCentauriSikPubWithError:
regularExpressionWithPattern:options:error:
uppercaseStringWithLocale:
initWithRawConfig:
serialNumber
sharedInstance
embeddedSecureElementWithError:
T@\"NSString\",R,V_key
code
componentsSeparatedByString:
queryCHUnitSimMuxDualPhysicalStateWithError:
querySysCfgKey:withError:
_config
_helper
queryWLModuleSerialNumberWithError:
visibleStringFromData:
dataWithLength:
query:forceCacheable:withError:
firstMatchInString:options:range:
logHandler
numberWithUnsignedLongLong:
query:ofSlot:isCachable:withError:
queryFactoryShippingSettingTimeWithError:
scanHexInt:
_dependencyPath
errorWithZhuGeErrorCode:underlyingError:
getEuiccPairingIdentifier:
longLongValue
stringWithUTF8String:
_eUICCPairingIdentifier
convertReturnValue:toCase:
currentLocale
getCTServerConnection
graphicInfoArrayFromArray:
numberWithUnsignedLong:
objectForKey:
query:isCachable:withError:
T@\"NSDictionary\",&,V_postponementStatus
mobileEquipInfoList
setFirmwareSecurityInfo:
setSelector:
stringByReplacingOccurrencesOfString:withString:
stringByTrimmingCharactersInString:
substringToIndex:
convertToPostponementKey:
loadFirmwareSecurityInfoBootedOS:
valueForKey:
JSONObjectWithData:options:error:
aRecursiveMutex
_ZhuGeDescriptionWithLayer:
clearCache
convertReturnValue:ByItselfAndError:AndRevalues:
lowercaseString
_propertiesCache
loadFirmwareSecurityInfoRestoreOS:
numberOfRanges
unionizeRawConfig:withError:
_key
cacheType
getConfig
numberFromString:
numberWithInteger:
queryMesaSensorIDSensorSNWithError:
isAtEnd
dictionaryWithObjects:forKeys:count:
flexibleList
stringByLeftTrimmingCharacter:
T#,R,V_actionClass
T@\"NSXPCConnection\",&,V_xpcConnection
checkDependency:withError:
initWithError:
queryKey:andOptions:andPreferences:withError:
removeAllObjects
convertReturnValue:toFormat:
helper
initWithBytes:length:
invoke
updateChangeablePropertiesForKey:andOption:withError:
T@\"NSData\",&,V_eUICCPairingIdentifier
isAppleBaseband
initWithQueue:
loadEUICCPairingIdentifier:
processName
queryIOProperty:fromCriteria:withError:
setKey:
componentsJoinedByString:
firmwareUpdateInfo
name
T@\"NSString\",R,V_name
T@\"ZhuGeArmoryHelperArmory\",R,V_helper
addObject:
cStringUsingEncoding:
numberWithShort:
setFirmwareUpdateInfo:
getBytes:range:
hexStringFromData:
isEqualToString:
queryFDRSealingStatusWithManifestOverride:WithError:
queryMesaProvisionStateWithError:
cacheDict
dictionaryWithDictionary:
getMobileEquipInfoIn:ofSlot:
integerFromData:size:truncate:isSigned:needSwap:
lastPathComponent
initWithLength:
ccccValue
methodReturnLength
processInfo
bytes
setObject:atIndexedSubscript:
actionClass
delCacheForKey:
_name
dictionaryWithContentsOfFile:
stringByRemovingCharactersInString:
synchronousRemoteObjectProxyWithErrorHandler:
T#,R,V_cacheType
allValues
arrayFromShellCommandString:
firstObject
integerValue
queryWLHWIdentifierInfoByProperty:withError:
setLogHandler:
substringFromIndex:
T@\"NSDictionary\",R,V_config
stringFromData:
_cacheDict
_configClass
actForKey:andName:andConfig:andOptions:andPreferences:withError:
descriptionFromZhuGeErrorCode:
macAddressStringFromSysconfigDataSixByte:
objectForKeyedSubscript:
_postponementStatus
characterAtIndex:
mutableBytes
postponementStatus
queryMobileEquipInfo:byKey:withError:
queryScreenSerialNumberByProperty:withError:
unsignedLongLongValue
aliasesMap
arrayWithObject:
getMobileEquipmentInfo:
loadMobileEquipInfoList:
scannerWithString:
@32@0:8@16q24
@\"NSData\"
@28@0:8@16B24
B32@0:8@16^@24
@48@0:8@16{_NSRange=QQ}24^@40
v24@0:8^?16
@24@0:8@16
@\"NSDictionary\"
B40@0:8@16@24^@32
@24@0:8Q16
@\"NSXPCConnection\"
B24@0:8i16i20
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
@\"NSMutableArray\"
@16@0:8
^{__CTServerConnection=}16@0:8
#16@0:8
#
@64@0:8@16@24@32@40@48^@56
@\"ZhuGeCacheArmory\"
@24@0:8^@16
@40@0:8@16@24^@32
v24@0:8@16
@48@0:8@16Q24q32B40B44
^?
@20@0:8c16
B24@0:8@16
B16@0:8
@\"CTMobileEquipmentInfoList\"
@\"NSNumber\"
@32@0:8@16@24
@48@0:8@16@24@32^@40
@32@0:8Q16@24
@32@0:8@16^@24
@44@0:8[512c]16[128c]24^{__CFString=}32I40
B24@0:8^@16
v16@0:8
@\"NSString\"
@\"NSMutableDictionary\"
@\"NSArray\"
q16@0:8
@44@0:8@16q24B32^@36
@40@0:8@16@24#32
@40@0:8Q16Q24B32B36
B40@0:8^@16@24@32
@\"ZhuGeArmoryHelperArmory\"
@32@0:8B16i20^@24
^?16@0:8
@36@0:8@16B24^@28
qcLoMoHuqwN9l2o0uaPaq0FGgheBaItLe5TCoQ5VCxqiw
???
Please check if you really want to try this function in current OS or environment
XPC Service Connect Failed
wlan
EID
Get IDSN from AuthCP: %@
ProvisionedUnknownKey
transportProperties: %@
RLi/BisKjNTSYXoStoELs1FSND6rfSKuGpBJ4E0g8Wfd8
+[NSArray(ZhuGe) arrayFromShellCommandString:]
-[ZhuGeArmory convertReturnValue:toCase:]
Timeout
fail to create plain cert
BackTeleCameraSNUM
FrontCameraRenoModuleSerialNumString
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m
STRING_SIZE_GIB
-[ZhuGeArmoryHelperArmory getPrimarykeyOfKey:withError:]
fullPath
W6G2ZPL+BzsMLGtunPo4q13HKvqm45nmzrVJEV2Uq/x18
Error System Issue
Failed to retrive value for \"%@\" from MobileGestalt!
ProvisionedWithTest
fail to decode ContentInfo
/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c
RegEx Not Matched
bmu-num-supported
AMFDRSealingMapVerifySealing
IOService://AppleTCONControl/coverglass-serial-number
Implementation error: Connection handle to AppleBiometricServices has a refcount of zero and should be null but the handle is non-null!
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
The ACE command returns an error
Failed to read IDSN via AID
Failed to get pinecrest cert from libFDR for key \"%@\"!
Failed to get MobileEquipmentInfo: %@
unionizedConfig pointer is nil!
Caching properties for key: \"%@\"
path
+[ZhuGeKeysActionArmory queryWLHWIdentifierInfoByProperty:withError:]
AkfIj49PscGvuFSmdygUq10dr0OOsjzBlVg1cnpJVQO/M
NUMBER_UINT32
Failed to convert format for key \"%@\"!
Please make sure IO Service is valid
Option Unsupported
Length of sysconfig key %@ is wrong, expecting 4!
IODeviceTree://chosen/mac-address-ethernet0
queryExternalDisplayBacklightUIDWithError:
qXLtae9hyCs7VeXhQLkRM097iiuk2VDpWcN4E56+F84hE
IOS
-->
cannot allocate space for idsn data
queryScreenSerialNumberByProperty:withError:
CopyIdentifier
Get failure when calling API of libFDR
XPC Service Entitlement Missing
Find service class: \"%@\"
+[ZhuGeKeysActionArmory queryVinylEUICCCSNbyKey:withError:]
INF
NUMBER_SIZE_GB
$superkey
The failure might be expected without specific hardware
DataStore
%s%s\n
v8@?0
Failed to get properties for key \"%@\" in TAUREN!
SP Exited
XPC service name may be invalid
+[ZhuGeKeysActionArmory querySysctlVariableName:dataType:withError:]
+[ZhuGeBasebandConnectionArmory getCoreTelephonyClient]
ROM Revision
ACTION_TIMEOUT
May due to an invalid IO entry
Maybe the method itself got some issue
child
systemSESN
ProvisionedWithGID
Encode Failed
ProvisionedLockedWithUID
BackCameraSNUM
w3d+bqLep9C2KRT5Dc/t717IDOHkzNoShIRuhKyVGx19w
UZxSgv2us0ZfhXwIhUX7a0FiCXZhsoLlXmkH6rQVODX9s
Method Invoke Failed
7tlZ0ABSfOYXqMZAXN1431B1h+Br5M7upUxKdr6Xkc5t8
raw-panel-serial-number-2
-[ZhuGeArmory checkDependency:withError:]
Method \"%@\" of key \"%@\" has a non-dictionary retry!
May due to an invalid IO Service
AIDReadIDSN
VgWVrLlQU2UvcGFbcIufd2AwKkT5U+ZXrdjwkciFRKQAE
pmu-follower-serial-number
Error Customized
+[ZhuGeKeysActionArmory queryThreadRadioMacAddress64BitWithError:]
BBUpdaterSetOptions
Lacking subkey of key \"%@\"!
Near Field API Failed
ComponentType
CZbYk6sTjNxVqTYUgxbf+17r9md3DZ5QRHzUHBjtnELao
parentPlane
Failed to query IO property \"ecid\" for TCON!
DERParseSequenceContent failed to decode into validity with der state %@!
auth,mlb
%s\n
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoRestoreOS:]_block_invoke
fail to load BBUpdaterExecCommand from BBUpdater dylib
Searching from fullPath service.
+[ZhuGeKeysActionArmory queryAIDTouchScreenCert:idx:withError:]
\x85
FLEXIBLE_PATTERN
logCallbackForSyslogWithLevelBuffer
FduIrkWaePZT8tDWdxcu00FF+SES2WC9g094cg6x2FEa4
v16@?0@\"NSNumber\"8
In %@, error p-pointer is nil!
Method \"%@\" of key \"%@\" doesn't exist!
Preference of key \"%@\" has a non-number timeout!
Check error description to find out recvoery suggestion
%d
als-front-land-serial-num
xlNWiCzpngNoAeP0QHH+m14YQmhHOMAr8wVl3QH5rfgAU
Failed to resolve dependency \"%@\" for key \"%@\"!
The system profiler exited
nJcmJi6nEp5Ll6CuYyaC+10jXex+M+8W1qy3xdu3e1OMA
-l 0xFFFFFFFF -v 99
Issue may be due to the underlying error out of ZhuGe
Failed to query property for %@, error %@
+[ZhuGeKeysActionArmory queryDisplayUniqueChipIDWithError:]
IOService://AppleProxAbstractHIDEventDriver/SerialNumber
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoRestoreOS:]
didn't retrieve functions from BBUpdater dylib properly
SP Report Crashed
Value Out Of Range
parentClass
RoswellAuthI2CRelayInterface
queryCentauriSikPubWithError:
dependency \"%@\" doesn't contain a valid JSON string!
Failed to match parent class or name of entry \"%@\" for key \"%@\"!
ctx pointer is nil!
integer:1
Error: RefCount reached its maximum value!
Format \"%@\" and class \"%@\" mismatched!
Maybe the name for querying is incorrect
Please check whether the path of XPC service correct and existing
FDR options is %@
AppleH2CamIn
CentauriUpdaterCopySiKPublicKey is not supported!
kVinylEUICCPairingIdentifier
p_obfuscated_key
Path or name of XPC service might be incorrect
No property \"%@\" in entry \"%u\"
fdr-product-type
AppleBiometricSensor
%@
-[ZhuGeBasebandFirmwareUpdateInfoArmory query:isCachable:withError:]
Alias \"%@\" is duplicated in keys of \"%@\" and \"%@\"!
Failed to get length for str2: %@, error: %@
servicePlane
panel-serial-number
querySysCfgKey:withError:
Failed to convert \"%@\" to hex number!
Key \"%@\" defines a empty method for action \"%@\"
%s%d
IO Entry Not Found
key pointer is nil
ACTION_ENTITLEMENT
<%@ %@(%@)>
Please check whether the user has the privilege
MobileGestalt Not Supported
%@%02zX%@
STRING_TRIM_SIZE_UNIT_CHARS
needOverride pointer is nil!
Failed to find a non-fullPath service for key \"%@\"
SMC Key Name Invalid
Img4 API Failed
{\n%@%@\n%@}
xZzLE50x6to8PZQH74StP1BZPsZBi5uXN0EBtMq6N9rAA
Illegal ZhuGe Error Code!
No
Missing basic criteria for key \"%@\"!
parent class and name
nfKey pointer is nil!
property pointer is nil!
IDSN
+[ZhuGeBasebandArmory isBasebandReady]
Key \"%@\" defines a non-array argument for action \"%@\"
Usually this error code shall not be displayed
serviceName
Trying IO service entry \"%@\"
GCTLLrRCKiXGd80/EQDwd080a0NacPCy4eEn6racjYhN8
/dev/console
NUMBER_UINT64
Failed to get value of property \"%@\" due to %@(%@)!
querySPUProperty:withError:
yTyKhgkJ+N+ZMHJDz95Gb0BK1bLAMFxFm3aqAYh69bBo8
com.apple.ZhuGe.ZhuGeBaseband
baseband class should be an integer
-[ZhuGeBasebandPostponementStatusArmory query:isCachable:withError:]
ZHUGE_NULL
ACTION_METHOD
Failed to find a non-fullPath service for path \"%@\"
C
One graphic in graphics array does not contain \"sppci_model\"
Failed to get keys config from raw config, error %@
Failed to get properties of \"%@\" for config!
bmu-num-enabled
all
AppleAuthCPAID
AMFDRSealingMapVerifyAsidMetadataForDevice
NUCsgvu+SXiI5u3u8TzQG0Fv4m3ytDyk6B9u0YYgbIPIY
+[ZhuGeBasebandArmory getBasebandClass]
Memory Exhausted
Checking entry \"%@\", plane \"%@\" for property \"%@\" with direction %@,
Output is too long (%@ > %@) for SPU property \"%@\"!
lEKNOip1IEPHg8L978amc0CNhXOgGSVJSBCKO37yUcv7k
%@:/%@
+[ZhuGeKeysActionArmory queryBMUExpectedBoardIDWithError:]
jcopSESN
+[ZhuGeKeysActionArmory queryBasebandFirmwareSecurityInfo:withError:]
Default component found
Failed to get IO service iterator for \"%@\" due to %@(%@)!
Will invocate for key \"%@\"!
Failed to get properties of \"%@\" for subkey!
Flexible key doesn't macth its pattern
Key Duplicated
No matching services for AuthCP: %s, skip reading from it...
did not find plain cert
SIM_MUX verified: Device is in P+E configuration (expected P+P)
Case \"%@\" and class \"%@\" mismatched!
data:
+[ZhuGeKeysActionArmory queryIOCameraByProperty:withError:]
Unknown SE Type \"%@\"!
uU6Q/yVGRbrIwfV5JhBYH11bVr+w7C8fkcxwcwEsQQxek
V+FPtV8y9rZfentcqCYeL1F22eWzbGyVPgBgIEoydQw4k
Got IO service iterator for \"%@\"!
%s
-[ZhuGeArmory verifyDependencyWithError:]
Flexible key \"%@\" got a nil subkey!
Issue Underlying
no
com.apple.BiometricKit
sppci_model
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
+[ZhuGeKeysActionArmory queryIOProperty:fromCriteria:withError:]
parentName
ACTION_RETRY_NUMBER
Key \"%@\" is not converted, keep original value %@
+[ZhuGeKeysActionArmory getReportFDRDiagnosticFromOption:withError:]
-restore
Failed to get flexible list from keys config, error %@
Please contact Near Field team for issue triaging
\"%@\" is not a valid data criterion
%lu
decodePKCS7TouchScreenCert
printfErr == offset
+[ZhuGeBasebandArmory getProperty:inPlane:withName:withOption:]
Failed to get config for dependency \"%@\"!
MesaSensorIDSensorSN allocation failed
AppleAuthCP
AppleBiometricServices
(null)
aString pointer is nil!
AppleCamera
Failed to get valid data for \"%@\" in bootedOS!
pBZwlrYQ/Yqs7UBWEniBp0BscFwhG7wt++nWg6W28fEPE
hw.product
Failed to create a matching dict for service \"%@\"!
Failed to check dependency for key \"%@\" in path \"%@\"
Searching from non-fullPath services.
Failed to query property %@! after trying all methods
VlPZNgOg1p1oj0IEgDd6F10jh+is1Z1X+RW+DXL/lKQvY
Failed to initialize a module instance!
VRAM Size
com.apple.AppleDeviceQueryService
MGkey pointer is nil!
RETURN_REVALUE_OUTCOME
Sysctl Failed
Yes
Unexpected length of wifi-module-sn: %@, expecting length %d
PRIVILEGE
AppleCBTL1614Device
ACTION_QUERY_PATH_STRAIGHT
als-rear-serial-num
BSD Name
6LFIpJX7gwmw6i+QUugjN16ftZ0ANUfFRD0/FcFGGjdlo
no mobile equipment information of slot%d
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m
Required size is %@, while usually it should be %@ or %@ or %@ or %@
Path Invalid
+[ZhuGeKeysActionArmory queryMesaSensorIDSensorSNWithError:]
IOService://ethernet/local-mac-address
Xacf3g3sv/7PX2J9rFL9z072dgMx0j9mwYTqP80jkZRAA
SerialNumber
Entitlement Unsupported
%s:/%@
wifi-module-sn
Failed to get touch screen cert from ioreg
Successfully read AccessoryCertificate from AppleAuthCP AID service.
EMa2
UnknownFunc
\"%@\" of entry \"%@\" is class %@ while expecting NSNumber
IODeviceTree://chosen/mac-address-bluetooth0
P4vgmVNL1cIFO9Qi+yX9t0AckhWpSpeq5SpH7rTu9tNMA
Device does not support dynamic configuration
EMPTY_ARRAY
Name of queried sysconfig key might be wrong
Lacking of criteria \"fullPath\" service or not!
Failed to read \"%@\" from sysconfig dictionary
BasebandUpdater
+[ZhuGeKeysActionArmory querySPUProperty:withError:]
ID
parent
Failed to get plane entry for key \"%@\"!
parent class
bBUGOKyRf8JC1/kbTQbCp0C7Gf6xGsFgHS8xrmZbHlrJQ
IODeviceTree://chosen/mac-address-wifi0
IODeviceTree
Restore
ZhuGe Error module itself got some issues
Didn't successfully verify fdr data sealing status, error %@!
extra
ofKYA7HqFrx8cnA8dcfB627DgJl7n7nPu7EM0tRG1SEdY
Error: RefCount equal to zero is trying to get decremented!
Get failure when calling API of AppleMobileFileIntegrity
Preference of key \"%@\" has an invalid retry interval: %@!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeKeys/ZhuGeKeysAction.m
direction
ZhuGeToDo:withError:
TeSXZEwq35nFS8donhmyb1Ck5VDKjR5ddJ3qChRQGO+WU
ZhuGeLog
%s %@
STRING_MAC_ADDR_SYSCFG_6BYTE
Key \"%@\" defines a non-string access
Alias of key \"%@\" is not an string!
Got properties after obfuscating \"%@\" for key \"%@\"
+[ZhuGeKeysActionArmory querySysCfgKey:withError:]
Key \"%@\" original value is %@, error is %@
Key \"%@\" revalued value is %@, error is %@
SP Data Report Invalid
name pointer is nil!
sensorID
Query key: \"%@\" without time limitation
%
Read %@, field %@, output %@
+[ZhuGeKeysActionArmory queryFactoryShippingSettingTimeWithError:]
v24@?0@\"NSDictionary\"8@\"NSError\"16
VBIOS Version
Querying the key: %@
Class Type Wrong
Dylib Not Available
Some pointer shall not be NULL
The property list cannot be serialized
The data indexed by the indexArray is not valid
Failed to get FDR data for class \"%@\"!
ARRAY_GRAPHIC_INFO
ZhuGe Key Further Check Needed
ChipNumber
buffer
+[ZhuGeBasebandConnectionArmory getCTServerConnection]
String is invalid, like unpaired quotation, bracket etc.
+[ZhuGeKeysActionArmory queryScreenSerialNumberByProperty:withError:]
Failed to get a connection for AID Bus!
RETURN_FORMAT
Path of IO entry might be wrong
User defaults doesn't support the specific domain
RN8kLj4030Fn1SvU0Woix2BHxZAAMREu2PbvTnt3fTmzw
tritium-mando-uid
Failed to get properties for key \"%@\" itself!
ZhuGe Key Not Supported
Failed to search property \"%@\" for key \"%@\" due to a nil service plane!
readPropertyFromComponentAuthService
Rz0lOIZTohL+Ri3DNSjvf19Isbz5Z2lVYAvTeQYgrxJzw
CFPreference API return error
Sysconfig Key Invalid
FDRDeviceAsidMetadataIsVerified_Options
backglass-serial-number
coverglass-serial-number-2
MahiChipDieID
BackSuperWideCameraModuleSerialNumString
Failed to open IO connection for \"%@\" due to %@(%@)!
dependency pointer is nil!
Key \"%@\" doesn't define the default action
IODeviceTree:/options
NUMBER_SINT64
+[ZhuGeKeysActionArmory queryFDRSealingStatusWithManifestOverride:WithError:]
Failed to weak link libnfrestore.dylib, NfRestoreSEEnumerate isn't available!
+[ZhuGeKeysActionArmory queryThreadRadioMacAddressForProvisioningWithError:]
Failed to get properties of \"%@\" for primary key!
Please make sure the file exists
Reserved ZhuGeErrorCode %@ shall not be the argument
AzRjL78vqZvv+67BDObFP1BuLaSpSTaRpPUKVhQGQp45w
aString length is too long for 2 hex number expression!
getFDRDataByFDRClassWithError
Failed to retrieve Secure Element!
ProvisionedUnpaired
+qluw9N3tQ6lWJQydep/p0Esxk6EuILApUlLaNC16MfYc
Failed to get CT server connection interface!
Failed to get CTServerConnection instance
fail to load BBUpdaterSetOptions from BBUpdater dylib
-[ZhuGeCacheArmory setCache:forKey:withError:]
Unsupported type \"%@\" for criterion \"%@\"
\"%@\" of entry \"%@\" is class %@ while expecting Integer<NSNumber>
BackTeleCameraModuleSerialNumString
kVinylFwUpdateCsn
ACTION_ARGUMENT
Method \"%@\" of key \"%@\" has a non-number timeout
VerifyData
tcon
-
Didn't get properties after obfuscating \"%@\" for key \"%@\"
Specific function isn't supported in current OS or environment.
User Defaults Domain Not Exists
(IO[a-z]+)://(.+)/(.+)
-[ZhuGeArmory actForKey:andName:andConfig:andOptions:andPreferences:withError:]_block_invoke
+[ZhuGeKeysActionArmory queryNFSecureElementByKey:WithError:]_block_invoke
TMac in sysconfig dictionary is with invalid length.
v24@?0@\"NSData\"8@\"NSError\"16
Find service name: \"%@\"
4kQV96buQ1aquc9FF+wrG25mwAi9lpBZByqq6XYGVVB14
pServiceMatchingMethod pointer is NULL!
Failed to get IO properties from entry \"%@\", %s
H70NRtAMRoBV3+QCls5nJ082VJDNyJHgTfyr6AU66Z5gs
Preference of key \"%@\" has a non-number retry interval!
basic
service class and name
error p-pointer is nil!
ALL_ZERO
Alias \"%@\" is duplicated with keys!
Unexpected nil primary key of key \"%@\"!
Time Out
Nm1YmAePxemPeq+uQQ9o521b7ifMduKD62l3Hviu/BoUs
AppleBiometricServices io_service_t failed to be released!
mobileEquipInfoList is reloaded
STRING_UPPERCASE
Failed to get bootstrap main port for key \"%@\"!
w
Pattern string can not cover the case
service class
IOService
Unsupported service matching method!
MGQuery
MSB
Please check the CLI option that input
SMC Service Unsupported
ZhuGeBasebandFirmwareUpdateInfo query:%@ isCachable:%s
BBUpdaterExtremeCreate failed to create an updater
BOOL_POSITIVE
Please file a radar against \"ZhuGe|all\"
defaults
dependency \"%@\" format is wrong!
Current process is not a XPC service process
Please check newly added code that calling ZhuGeError API
Failed to get parent entry of entry \"%@\" for key \"%@\"!
local-mac-address
cannot get error code, result: %s
AppleSmartBatteryPack
7tFI/Pj8fSzpumF8D8YsF2Bv0TS4DIqwHyG+SPrv1BCaU
ATE
Failed to read the display unique identifier!
isComponentAuthChipAuthCPService
IOSERVICE_MARCONI_WIFI
IOSERVICE_WLAN
-[ZhuGeArmoryHelperArmory getPropertiesOfKey:withError:]_block_invoke
Found %@ property \"%@\" for key \"%@\" with non-fullPath
SNRaw
Failed to query Centauri Sik Pub!
STRING_HEX
Dependency of \"%@\" is not ready, error %@
Found 1 property \"%@\" for key \"%@\" with non-fullPath
DERParseSequence failed to decode into TBS Cert with der state %@!
CENGetSiKPublicKey is not supported!
STRING_LOWERCASE
Please make sure the domain is correctly inputted
Failed to run for dependency \"%@\" for key \"%@\"
-[ZhuGeArmoryHelperArmory propertiesByKey:andSuperKeyRange:withError:]
-[ZhuGeArmoryHelperArmory getObfuscatedKey:withError:]
Failed to decode with proper API
ZhuGe received a relative path
Vendor
queryIOProperty:fromCriteria:withError:
multi-touch
Failed to get eUICC firmware info!
BBUpdaterSetOptions failed: %@
returnValue p-pointer is nil!
Value config of revalue \"%@\" is not an array
No SMC service available on this device.
Please make sure the correct SE type is input
AppleH4CamIn
Failed to weak link libVinylNonUpdater.dylib, VinyleUICCPerformOperationWithLogSync isn't available!
Will invocate for dependency \"%@\"!
ALIAS
Name of the call back function doesn't exist in library
SMC Key Size Unexpected
Please make sure the key string is correct
ip2drLzT5EvOXD6cPP5rU2AbR9glnV9CPclFfGGNV5y/A
integer:0
j2z/JVne3XTHRxqKe6Far0DTF7xLJ4qxJY55wPbx7RRKU
Bits will be truncated since real size is %@, while required size is %@
RetryNumber
Flexible ZhuGe Key Invalid
nova-serial-num
EMc2
ZhuGePrintStderr
Unprovisioned
ComponentFunction
Bqxx4pprqbYXTAyEXXvN312TS9ZrRHvd5gfR5+U9g2F74
can not find baseband class
BOOL_NEGATIVE
ACTION_RETRY_INTERVAL
May due to an invalid IO Service connection
Failed to query WLHWIdentifier due to mismatch data type, data read %@
Read WLModuleSerialNumber, output %@
CACHEABLE
err == 0 
key %@ does not exist in postponementStatus
-[CTMobileEquipmentInfo(forUndefinedKey) valueForUndefinedKey:]
Failed to weak link core telephony client framework!
Configuration of key \"%@\" has an invalid retry number: %@!
Operation is not done in certain time
AppleH6CamIn
kUmcdgObIa1Tmrury+vs80E+P7feurT7fjeBoSNzOjBrM
cmd
Key \"%@\" dependency got deadloop
HWIdentifiers
IOService://AppleTCONControl/module-serial-number
AWCSMahiDeviceInfo
ChipID
rpcp
getElucidatedStringLen
/usr/lib/libFDR.dylib
-[ZhuGeArmoryHelperArmory propertiesOfKey:withError:]
Failed to get properties of \"%@\" for itself!
AMFDRSealingMapVerifyAsidMetadataForDevice failed!
ERR
BBUpdaterExecCommand
Failed step1 of matching \"%@\" for key \"%@\"!
string:
Checking in self node for property \"%@\"
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Binaries/ZhuGe_Service/install/Symbols/embattled/embattled_keys.m
0qO8mRy+jZlCdJFm2K3Zl19kvekAelETHsWb+9scmH8hI
hCf3J+I7Gvmj39kb5wuYT1CfwQRQymZQ/Xo+KPRhX4lU8
%08X-
 
revalues pointer is nil!
Key \"%@\" doesn't define argument for action \"%@\"
Failed to get length of flexible key \"%@\"!
Successfully read IDSN from AppleAuthCP I2C service.
IODeviceTree://options/boot-args
err != (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x1)
5naLQAP8rbYbM+dDqBTdG12FDdDJA2iGVuiKxLbZmjOVg
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
key %@ does not exist in firmwareUpdateInfo
aObfuscatedString pointer is nil!
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
+[ZhuGeKeysActionArmory queryExternalDisplayBacklightUIDWithError:]
readAccessoryCertificateAuthCP
J9wpYRxZXBUk1WO0ni6v917+rriuGS/GSQobZkVtVCsTM
-[ZhuGeMobileEquipmentInfoArmory loadMobileEquipInfoList:]
ACTION_SEQUENCE
Key \"%@\" is repeated in %@!
Key \"%@\" does not match any definition!
Call Back Function Not Found
PropertyList Serialization Failed
:
parent name
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
Failed to query \"%@\"!
I32sGclpgl5VujQRJxyhKQ
Library-MesaFactory
_connectHandleRefCount < 4294967295U
YwMa8PyxriC0h96yJPyvz110EsCWKO7txsHYVZNN7KEps
Argument type \"%@\" is incorrect for IOServiceMatching!
criteria pointer is nil!
did not find the config of key %@
IOObjectRelease(service) == 0 
In %@, aKey pointer is nil!
Failed to cache properties for key \"%@\"!
Input may be missing subkey(s), or something wrong with flexible pattern definition
CTMobileEquipmentInfo does not have property %@
AppleH13CamIn
tRn/qRwm394es24o13orf0CTTM60oo8/DS2Dx26ehaqHw
raw-panel-serial-number
printfErr == 2
key length is %@, but super key range is {%@, %@}!
product
Platform
V
STRING
ACTION_DEFAULT
Atl1ygbcnX05i/r/gHKSk120MRi9vBhvi9JojCVetjyLc
%s ERR: 
fail to load BBUpdaterExtremeCreate from BBUpdater dylib
No firmwareSecurityInfo found
NIL
Key \"%@\" contains non-string alias
readIDSNAuthCP
The string is not a valid ZhuGe key
May due to wrong implementation or system problem
ZhuGe only supports absolute path, caller needs to convert relative path by itself
The option passed in is not supported
SealingManifestOverride
+[ZhuGeKeysActionArmory queryFDRDeviceAsidMetadataIsVerified:withError:]
ecid
Failed to decode AccessoryCertificate
NUMBER_SINT32
Flexible key \"%@\" is missing subkey(s)!
Failed to get length for str1: %@, error: %@
4QXj82hRhZ6/k74y2qWao0BROSL65x+Bvew1MAHwp6RZw
AppleH3CamIn
%s://%@/%@
queryMogulIDSN:withError:
ECID
bufferSize
-[ZhuGeBasebandPostponementStatusArmory loadPostponementStatus:]
STRING_UUID_WITHOUT_DASH
Failed to query WLHWIdentifier for property %@, no matching key found in %s
Query wifi-module-sn fail, type %@, data %@
SecAbsoluteTimeFromDateContentWithError failed, error = %@
GW8jawjUZ/zcAuUmHkGbN27chdKx5AN/e8KCGpcUqktYg
IOService://IOMedia/Size
getReportFDRDiagnosticFromOption:withError:
, 
After %@ ms, retry %@/%@ times for method \"%@\" of key \"%@\"
Key of dictionary is redundant
YTrd2LofkEtmiM4cXwiLc082s6U/st5pPHdDS8MT8UAsc
LSB
RETURN_REVALUES
ModuleVersion
8ybq4N66oFkNzgwX0r/uh12j3Yul3nPiPplgdku4vHwGw
queryFactoryShippingSettingTimeWithError:
pNbNAqd6QFlv6xayKmTAf14Qa69vrR7VZDaFl+WwyDULY
m
AccessoryCertificate
ComponentIndex
failed to get errorcode response: %x
SYSCFG
Failed to load libFDR.dylib!
yes
ACTION_QUERY_PATH
X0kI6yR4hRNgedMr+8P2z15g6ljy/AS4p+MmcSrWDUI/I
atm_diagnostic_config
ZERO_NUMBER
Failed to initialize an instance for ZhuGeArmoryHelper!
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
Failed to match parent name of entry \"%@\" for key \"%@\"!
firmwareSecurityInfo is reloaded: %@
Error config of revalue \"%@\" is not an array
Failed to verify for key \"%@\" in dependency \"%@\"
Path Not Absolute
Please check regEx related code in ZhuGe
orjkMiWWInwIkY/Z7N3hr221P46zXZD9kH3CzhdxkV34s
WRN
EMPTY_DICTIONARY
IODeviceTree://product/panel-serial-number
Did not find config of key %@
queryMesaProvisionStateWithError:
service pointer is nil!
ACE Command Failed
Caller's entitlement value is mismatched with required one
AppleH1CamIn
failed to get read memory response
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m
DEPENDENCY
Failed to get io service iterator by \"%@\" for key \"%@\"!
Q7oU1FM7t+//vn8mEzH061EmoC99VGc8umtJUlLoEuOPY
%02x
unknown
Dependency \"%@\" defines a non-array dependency
failed to read IDSN data via AID, result: %s
6rUXDHIWCVKLhA5uFbxB41Aw9LlmCMGCvEkW0TG6dPwe0
DRHpQ4yYNpFi5QjmIq+Y810Pw1l7FsGmAoX3s4cTiJYmY
path pointer is nil!
-[ZhuGeArmory getKeyAndOptionFromDependency:withError:]
ZhuGe is running well
Index %@ of ZhuGeErrorCode table got a wrong code %@
IOService://AppleHPMDevice/UUID
fail to create an option CFDictionary for BBUpdater
Current OS is not defined
Near Field SE Type Invalid
Failed to get IO properties from service entry %@! %s!
RearCameraAuthICChipID
5eXj+hsAOI+a21+Lu3eMC13BVB7Ac992kT1Vd8WoCUiOE
Failed to get eUICCPairingIdentifier!
%@ms timeout for method \"%@\" of key \"%@\"!
Parent entry is \"%@\", class is \"%@\", name is \"%@\"
mogulTopModuleSecondary
backglass-compass-serial-number
Error: Connection to AppleBiometricServices could not be initialized!
Properties of key \"%@\" is: %@
Failed to get IO properties from service entry %@! %s, a potential issue!
+[ZhuGeKeysActionArmory ZhuGeToDo:withError:]
Failed to get MesaSensorIDSensorSN, returned error 0x%08x
als-md-mlb-serial-num
-[ZhuGeBasebandFirmwareUpdateInfoArmory loadEUICCPairingIdentifier:]
The input data may be unexpected and cannot be processed
RETURN_REVALUE_DEFAULT
WCzva5VLvofdVaqMS6Ap917z9HXFlBToosgmEDJBalieM
YK1jvTHgjdt2Od1g1cGNg1EzY5VLX6jKTt3wQupFvEbI8
IOService://AppleARMSPIDevice/chipid
*bufferSize
STRING_VISIBLE
Checking dependency \"%@\"
SecCertificate API Failed
service name
IOService://wlan/local-mac-address
%s <%s %s(%ld)> ERR: 
Matching regEx failed for IO path \"%@\"!
One graphic in graphics array is not a dictionary, ignore it.
Please check whether the path using is correct
We may need to check with libSMC together
The system profiler report failed to be created
AMFDRCreateWithOptions failed!
mogulTopModule
queryIOCameraByProperty:withError:
o8SKs/wlQuqD2Q2nnHk9z1CpnG8Hc9hmFwcjNYdYxeWRo
\n
CopyAllowUnsealed
TMac
IODeviceTree://chosen/development-cert
IOService://sdio/local-mac-address
Wasn't successful to find a matched revalue pattern!
Key \"%@\" doesn't define actions
This error code should never be reported
IODeviceTree://chosen/effective-production-status-sep
Failed to obfuacate super key of \"%@\" in range<%zu, %zu>!
Get the flag number is : %@
gB61Se7lVm1BUkLqacQ980B55i3Rbb9ngrzF3NEAPgXFM
Get failure when calling API of Img4
size == sizeof(state)
-[ZhuGeArmoryHelperArmory getSubkeyOfKey:withError:]
Maybe the method name is incorrect
PFSN
disk0
-[ZhuGeArmoryHelperArmory getPropertiesOfKey:withError:]
Key Not Found
Failed to find IO entry for \"%@\"!
data:tcon
\"%@\" is not a vaild MobileGestalt key!
EMPTY_STRING
Key \"%@\" may need further check
SMC Service Failed
Failed to search property \"%@\" for key \"%@\"!
Vinyl error code: %@
Unknown Mogul Type
Iay9Sr+EgQjh8wCawoxNP10KX4+UsX2CXjihZPv1EcZPk
-[ZhuGeArmory convertReturnValue:toFormat:]
Unexpected nil config of key \"%@\"!
logCallbackForSyslogCDPWithLevelBuffer
+u7dB6GE+RzxUTEJzzjGS16kN811vk8Oia1lGFoLWCZdE
IOService://marconi-wifi/local-mac-address
zhuge_debug
Please check whether there is any underlying isse in the encoding API.
AMFDRLogSetHandler
Catch the NULL format pointer from: %s %s(%ld)
BBUpdaterExtremeCreate
Data Convert To Nil
Already found %@, skip this
postponement status %@
Failed to cache string for \"%@\"!
Key \"%@\" is defined action sequence with non-array
-[ZhuGeArmoryHelperArmory initWithRawConfig:]
Data Convert Failed
Failed to read AccessoryCertificate of mogul based top module
VutVHB8Wg9nACkP4UQgs31CxyuH0G43a9ffxeavEwVXJs
GPXrJXV9cmnYFY6vDzNBd0BJ83EQQN8iNp2FlUkSsaSA4
Please check whether device supports the service
AppleAuthCPRelay
+[ZhuGeKeysActionArmory queryCentauriSikPubWithError:]
queryDisplayUniqueChipIDWithError:
q24@?0@\"NSString\"8@\"NSString\"16
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
Please check your code to use a correct class
Specific Hardware Needed
Didn't successfully get data due to lacking of specific hardware
number
Uninitialized
Mogul is not ready via AID, result: %s
6Q2HUd0W2HvvW1uXtIrXh0BgG9/ymV6FwuWvCVnjBLnag
khQ6/64HBXiF12L+ikQM+18cKR8mllprzF7FjID+1xKWg
EMa3
xsY3cS4aDX96XNwVKUi7L08r7F8ncE7jhvsPDL61Eg9LM
ZhuGeArmory
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeBaseband.m
Failed to get properties of \"%@\" for alias!
Please check whether the dylib provided correctly
UnknownFile
Method \"%@\" of key \"%@\" has a non-number retry interval
CLI Option Unsupported
Unsupported entitlement or the entitlement type
-[ZhuGeArmory actForKey:andName:andConfig:andOptions:andPreferences:withError:]
Alias of key \"%@\" is not an array
Get data <%@> of property: %@
BMac
%s: 
The system profiler data type is null
AMFDRDiagnosticGenerateReport failed!
HRr/DU1S07L/YFiEw2YzX18zHSFPcobEs4ZEajjWPCx64
postponementStatus is reloaded
Key \"%@\" doesn't define method for action \"%@\"
Failed to create IORegistryEntry iterator
Cannot look up \"%@\". System errno=%d errstr=%s
MMac
firmwareSecurityInfo can not be nil
ZhuGe_Action_Retry_Serial_Queue
Check error description to understand failure reason
CFDictionaryCreateMutable failed!
IOPortTransportAIDBus
root
[ZhuGe]
Argument type \"%@\" is incorrect for IOBSDNameMatching!
Key \"%@\" defines a non-array dependency
Key \"%@\" defines a non-string method for action \"%@\"
p_config
%@:/
Failed to get TMac from sysconfig dictionary!
MFTFDybYdMEa3t7lEekmZ0DVntZfm8FTx8hVssqp6sQ80
All possible tries has failed
Please check sysdiagnose for more detail
AMFDRDiagnosticGenerateReport
queryBasebandFirmwareSecurityInfo:withError:
/usr/lib/libBBUpdaterDynamic.dylib
The path just doesn't exist or the way to find the path is incorrect.
MissingMSRk
RearCameraAuthICUID
CFPreference Error
YonkersIR1UID
Please check path of the code calling CFPreference
ZhuGeBasebandFirmwareSecurityInfo query:%@ forceCacheable:%s
pcrt
Failed to encode with proper API
Failed to call SMC APIs, unsupported SMC key etc.
service
8jvikGIcqTbQS4FdgY3t6160TElV+a3nnrgv6KQmmRbsc
Ny83MdAFmn0Klc53MPhcJ121gbiy5Y4e1NHpKdaQ3+hrg
getObfuscatedString
Code Max
Querying %@ of Secure Element.
DERParseSequence failed to decode cert chain with der state %@!
6Gxpv/uzw0b4QcHxsgcfH0AuNp2A/PFANYZxtAYKfBbnw
Q
-[ZhuGeArmoryHelperArmory getConfigOfKey:withError:]
touch screen cert has %ld bytes after decoding
Key \"%@\" isn't supported in restoreos!
Duplicated dependency \"%@\" for key \"%@\"
Key \"%@\" isn't supported in %@!
Failed to get aliases map from keys config, error %@
OS Unknown
Please make sure the way using ZhuGe is correct
null or empty pkcs7 cert content
%@%@
Failed to get postponementStatus: %d:%d(%s)
Maybe the method name or signature is incorrect
XPC Service Not Available
getIOConnection
Failed to get properties for key \"%@\" in MERMAID!
Cannot create CF property for property \"%@\"!
Failed to get io service iterator from \"%@\" for key \"%@\"!
Get the component index number is : %@
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeArmoryHelper.m
logCallBackForVinylEUICCWithLevelFormat
YonkersIR2ChipID
Arguments were set for key \"%@\": (%@)
Failed to act for key \"%@\"!
Failed to open IO Master port
Probaby the wrong arguments defined in xml
Lockdown Query Failed
Permission Denied
NSString \"%@\" of entry \"%@\" is %@ while expecting %@
Failed to query wifi-module-sn from ioreg path %@!
can not find entry at %s
SUPPORT_RESTOREOS
RETURN_REVALUE_VALUE
BackSuperWideCameraSNUM
kCTPostponementStatus
com.apple.zhuge
Invalid ZhuGe Error Code!
option is not a dictionary
logCallbackForSyslogWithContextBuffer
+[ZhuGeBasebandArmory queryCHUnitSimMuxDualPhysicalStateWithError:]
-[ZhuGeBasebandFirmwareSecurityInfoArmory query:forceCacheable:withError:]
-[ZhuGeArmory runForKey:andOptions:andPreferences:withError:]
-[ZhuGeArmoryHelperArmory unionizeRawConfig:withError:]
Found property \"%@\" for key \"%@\" with fullPath
invalid decoded plain cert: [%p:%zu]
esdm-fuses
*bufferSize > 2*(sizeof(sensorID)+serialSize)
Please check whether the call back function name exists in the library
bool:
querying %@/%@ returned %s and %@
-[ZhuGeArmoryHelperArmory sortAliasFromUnionizedConfig:withError:]
IO Property Not Found
Something might be wrong with Near Field component
+[ZhuGeKeysActionArmory queryIOPropertyFromPath:andCriteria:withError:]
+[ZhuGeKeysActionArmory queryComponentAuthChipIDSN:withError:]
logCallbackForSyslogWithContextLevelFormat
JCOP Secure Element Serial Number
-[ZhuGeArmory convertReturnValue:ByItselfAndError:AndRevalues:]
Method \"%@\" of key \"%@\" doesn't return anything!
AppleOLYHAL
IODeviceTree:/product
^(.+)(?:$superkey)$
NULL
0
STRING_SIZE_GB
-[ZhuGeArmoryHelperArmory pickFlexibleFromUnionizedConfig:withError:]
Creating regEx failed for checking flexible key \"%@\"!
device_type
Failed to get sysconfig dictionary!
getConfigDict_block_invoke
HNRRSHuuTAZ59tHGR4NbA1Fisf/bq+UFvYjF0qeAbGFSo
fail to dlopen BBUpdater dylib with error: %s!
ACTIONS
Nothing Wrong
Please check whether the key or alias input correct, or implemented.
Please check whether there is any underlying isse in the decoding API.
AppleARMSPIDevice
seList pointer is nil!
jf+movONCK+lGgv8Y7TQ812yC7fbxm9/zB8+a8Uxem6c8
-[ZhuGeBasebandFirmwareSecurityInfoArmory loadFirmwareSecurityInfoBootedOS:]
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeIO.m
ZhuGeErrorCode %@ exceed maximum
Cannot find IO service entry from path \"%@\" for key \"%@\"!
queryBMUExpectedBoardIDWithError:
K0+xnwAxaxD8HiKQ4gDJd1DOtVl5HGVtbPZ1C+nR24SJ8
K0trEdL9AkfNZmKGN1K/S0DuAHqkSCTPqZspPP0bapRbA
YonkersIR1ChipID
IO Service Mismatching
SMC key information indicate a wrong type
IONameMatch
bg-magnetometer-serial-number
propertyValue
Failed to link libFDR dylib!
NUMBER_SIZE_GIB
Query key: \"%@\" within %@ms
Path Not Found
SP Report Creation failed
success read idsnData, first byte: %x
Check the string in code or input source
ReportFDRDiagnostic_Options
Local
Failed step1 to get parent class of entry \"%@\" for key \"%@\"!
%llu
Failed to get fwSecurityInfo: %d:%d(%s)
Failed to update config for key \"%@\"!
-[ZhuGeArmory queryKey:andOptions:andPreferences:withError:]
-[ZhuGeArmoryHelperArmory isKeyAlias:withError:]
+[ZhuGeKeysActionArmory queryTouchScreenCert:]
Failed to get tcon API!
YsAbn1q6x+q9+Xdb5GZbm23p1YMig5ka1M7Dfnng81vWM
firmwareUpdateInfo is reloaded
AppleDeviceQueryService
Outcome config of revalue \"%@\" is invalid!
This failure is intentionally, please check the input data length, content etc.
Creating regEx failed for IO query!
No property \"%@\" in entry \"%@\"
psim-present
+[ZhuGeKeysActionArmory queryWLModuleSerialNumberWithError:]
Option ROM Version
Failed to get a valid IO service iterator for \"%@\"!
Got IO connection for \"%@\" with type \"%@\".
tmpString length is incorrect!
gPOK
The system profiler report crashed
+[ZhuGeKeysActionArmory queryMesaProvisionStateWithError:]
AMFDRCreateWithOptions
RETURN_CASE
AppleH16CamIn
s
Didn't find EID from response of eUICC operation!
xg7hMKYgB3nm1AjjFLxRx0DEJEH2VRVTITfkK7F6q1llI
XPC Service Not Exist
ZhuGe Key Not Native Supported
Unsupported SPU property \"%@\"!
als-md-sensor-flex-serial-num
SIM_MUX verified: Device is in P+P configuration
Please check the data source or code
Failed to match the service name \"%@\"!
NSNumber \"%@\" of entry \"%@\" is %@ while expecting %@
P
Quotation \"%c\" is not paired in command \"%@\"!
AMFDRSealingMapCopyLocalDataForClass
Method Invocation Get Failed
OS Unsupported
als-tb-sensor-flex-serial-num
Wrong key or the key is not configured
Stepping
DebugArgs
tcon-api
Failed to get CoreTelephonyClient instance
Object Type Invalid
Entitlement Mismatched
eiBoDNfdjGI+4DTEZmHZB18Dyio2oSnjU9BjtR0BFWARY
wCREDfKF3ElH/GhqMIJjn15CQ72E5I5V/bN+n/bBR4MNU
returnValue pointer is nil!
Original key \"%@\" is already obfuscated
Please make sure the entitlement is correctly configured
Cannot find service name: \"%@\", %s
queryNFSecureElementByKey:WithError:
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeArmory.m
Configuration of key \"%@\" has an invalid retry interval: %@!
Some internal issues happened when converting data
serviceClass
parent no check
StripImg4
RESTOREOS
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
BOOL \"%@\" of entry \"%@\" is %@ while expecting %@
Entering aHWManagerReady callback
Serial
Outcome config of revalue \"%@\" is unsupported!
Failed to get response from eUICC operation! Error code: %@
Failed to get registry properties
Chipset Model
p_subkey
Tries All Failed
Successfully read IDSN from AppleAuthCP AID service.
/YYygAofPDbhrwToVsXdeA
%02X
JSON String Invalid
Type of some object is invalid
Please check the name that being querying
parent class or name
a cert
fail to strip root sequence
p/WRH+Et8QKgGhS/ov82N219tUCy3Wu9eyWTS5gvqBY1A
FDR API Failed
number:
centauri
graphicsArray pointer is nil!
Please make sure IO Service connection is valid
Unexpected SMC Key Size returned
parent check failed
+[ZhuGeKeysActionArmory queryNFSecureElementByKey:WithError:]
=
Please make sure locakdown daemon and local sockets work well
Failed to query supportsDynamicSIMConfiguration: %@
Booted OS: loading firmware security info via CoreTelephony
service plane
UpdateBaseband
Failed to get MesaProvisioningState, returned error 0x%08x
Initialize keys config!
key %@ does not exist in firmwareSecurityInfo
caseType is invalid!
Unknown mogul type
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
Please make sure the Caller has the correct entitlement
\"%@\" of entry \"%@\" is class %@ while expecting NSData
FSRsyiOWdf4OCG6zvks590DxmrR3/XoDhE85oTuP1f480
Please check sysdiagnose FDR related log
File Open Failed
Underlying service may be not ready
v16@?0@\"NFHardwareManager\"8
wasRetained
-[ZhuGeModuleArmory initWithError:]
RETURN
true
sg1SrHyuq7Uu15zGYwGGz1CjjOASEqn31w0kiAkOfUKt0
hj0kXUT8dWr2Uy8kgsYzv1E2Gvl0NncSrj0ngVjgeDLVU
TGiWzHMwhvg0m4uhHqJED0BUxYG4igeW4GbuHTy/DAXPw
YonkersIR2UID
Get failure when calling API of SecCertificate
RID
qjRH5QM3m6nH/auYOa6eC0D5vPWulgi0+VLCngICk+c2w
{%d:0x%llx}
/System/Library/CoreServices/SystemVersion.plist
The dylib does not exists or too old version
AMFI Get Failed
Failed step2 to get parent name of entry \"%@\" for key \"%@\"!
function: %@, targetFunction: %@, type: %@, targetType: %@
queryFDRSealingStatusWithManifestOverride:WithError:
DSp557sXEG12LTRMsGdoP0DnK4Tq6SBvsLPV6rag2VVVQ
propertyValueRef
UNKNOWN_OS
FDRClass pointer is nil!
Cannot connect to lockdown daemon via a local socket
IOSERVICE_SDIO
RETURN_REVALUE_ERROR
Please make sure the option is correct
Failed to get ScreenSerialNumber
querySysctlVariableName:dataType:withError:
can not find property %@ under %s
Please check sysdiagnose lockdown related log
sQlgU/hLxqme+OsLfVFJ822oV5I22G2S9IwE7gSKOJvAE
/usr/local/lib/libFDR.dylib
STRING_MAC_ADDR
Decode Failed
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
Unsupported SE Type
ProvisionedLockedUnknownKey
DERDecodeItem failed to decode validity notBefore time with der state %@!
No data for property %@, field %@
Failed to query isEuiccActive: %@
$option
RetryInterval
Key \"%@\" is defined action sequence with no action item
Failed to update properties for key \"%@\", error %@!
Object Length Invalid
System Secure Element Serial Number
integer:
\"%@\" is not a valid integer
v16@?0@\"NSError\"8
%s ERR: Restore log connection error: %@
class
{
So far so good, keep going
Failed to query BMUExpectedBoardIDData. isBMU2 = %d
touch screen cert has %ld bytes, returned without decoding
Unknown sensor state received!
Unexpected nil isAlias of key \"%@\"!
Please check sysdiagnose for more clue
String Format Wrong
The key is not a ZhuGe native key
\"%@\" of entry \"%@\" is class %@ while expecting BOOL<NSNumber>
NSData \"%@\" of entry \"%@\" is %@ while expecting %@
IODeviceTree://chosen/effective-security-mode-sep
string length should not be zero!
Revalued key \"%@\" to nil intentionally!
Invalid basic criteria type for key \"%@\"!
listSecureElementsCallback
SensorID
BBUpdaterExecCommand(CopyIdentifier) failed: %@
Failed to open a valid IO connection for \"%@\"!
IO Service Close Failed
Integer \"%@\" of entry \"%@\" is %@ while expecting %@
flags
Method Signature Get Failed
ModuleName
Img4DecodeInit failed to decode fdrData with der state %@!
string
eUICCPairingIdentifier is reloaded
SP Data Type Null
service class or name
ProvisionedWithUID
queryIOPropertyFromPath:andCriteria:withError:
als-front-port-serial-num
IOSERVICE_ETHERNET
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m
caseType pointer is nil!
User have no proper access
The size of %@(less than %d) isn't correct: %@!
isMogulService
z/7S0WfcGLDiM3juoXAPk16+dabQmWIXU2/xn5nLqcsyI
nhuNuIQn8s2Vrcmy9g8PD1B6i3c7ZmQEK1utNTKO2vHUo
In %@, aCache pointer is nil!
In %@, key \"%@\" got a wrong cache class type \"%@\"!
nil
Didn't successfully call init related method
Searching property \"%@\" for key \"%@\" with criteria %@
ZSWBgzP2yLseFXKsNKKMC0D7VhPb8UXsL1ynXSrA9r3MI
9aOxr1//Y8XlITR3p5/CT1Amyb/Z9TI/b88Mi/ETgB8oM
%s ERR: Cannot print serial log!\n
key pointer is nil!
IO Service Get Failed
SMC Key Type Wrong
Invalid full path to search property \"%@\" for key \"%@\"!
Unsupported AID mogul type
fail to decode content
r8L1DAtjrZMjuEhYjJB6J0DmQfsy8VWuW95w7j+wYUmfI
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m
ENTITLEMENT
Please check the path of IO entry
Option or input value is not in defined range
AppleH9CamIn
WMc2
Failed to get invocation method \"%@\" for key \"%@\"
Failed to get a connection for pressure!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeArmory/ZhuGeModule/ZhuGeModule.m
 KkMmGgTtBb
Failed to convert case for key \"%@\"!
/YHNnwv/KBMBEzyR3td5118gYU9eWHwdKy6bKcb1vddZU
Config of revalue \"%@\" is not a dictionary
Failed to get valid data for \"%@\" in restoreOS!
mogul,a1222
read IDSN failed, errorcode: %x
fail to decode SignedData
queryVinylEUICCCSNbyKey:withError:
FrontCameraModuleSerialNumString
BackCameraModuleSerialNumString
Initialize config for ZhuGeArmoryHelper instance \"%@\"
Please check sysconfig key name input
Invalid extra criteria type for key \"%@\"!
Memory is not enough
Didn't find the expected path
Failed to weak link near field framework!
EMac
WMac
_connectHandleRefCount > 0
NUMBER_TRIM_SIZE_UNIT_CHARS
Flexible key \"%@\" only has %@ subkeys while requring %@ subkeys!
IODeviceTree:/chosen
baseband class: %@
Argument type \"%@\" is incorrect for IOServiceNameMatching!
Pointer Null
fillmore
mogulLAS
No property: %@
queryMesaSensorIDSensorSNWithError:
%s ERR: Failed to get a restore log proxy!
i
AppleH10CamIn
pressure
-[ZhuGeMobileEquipmentInfoArmory query:ofSlot:isCachable:withError:]
Revalue \"%@\" criteria are matched
$subkey
Please make sure the key being querying correct
Length of some object is unexpected
FDR options is not a dictionary \"%@\"!
Failed to find AuthCP service: %s, skip reading from it...
gOS
format pointer is nil!
Key \"%@\" defines a non-array user privilege
Cannot open certain file
SysCfgDict
Device ID
XPC_SERVICE_NAME
Device may not support the service
mogulAce3
Failed to get properties for key \"%@\" in overall range!
IO Service Open Failed
Failed to match the service class \"%@\"!
M
LBJfwOEzExRxzlAnSuI7eg
IODeviceTree:/baseband
p_primarykey
rawConfig pointer is nil!
Hit cached properties for real key: \"%@\"
Option of the CLI command is not supported
XPC Service denied access due to lacking of entitlement
Please check latest code that using ZhuGe error API
f3JPDMLbeFqGZ6JKp/Cxc10Junmx7Bkr3WAFSj7+tHdh4
-[ZhuGeBasebandFirmwareUpdateInfoArmory loadFirmwareUpdateInfo:]
ReleaseType
%x
Preference of key \"%@\" has a non-number retry number!
^(?:$superkey)(.+)$
This special error code is used for ZhuGe configuration analysis
CertificationPublicKey
Restore OS: loading firmware security info via BBUpdater
Argument type \"%@\" is incorrect for IORegistryEntryIDMatching!
aObfuscatedString length is incorrect!
-[ZhuGeArmory updateChangeablePropertiesForKey:andOption:withError:]
option is nil
\"%@\" doesn't exist in entry \"%@\"
bmu2-board-id
k2L0muVU/NTtMtzysnNs210RDcjTSFUOp9M9EJEp0hvNs
baseband
Path not exists or the string is not a path
Cannot find service class: \"%@\", %s
Exiting aHWManagerReady callback
SEs5TXAVh1zo4q7nzd6BI0A/2poOxsJ4U7WDQ9fbQe1vw
h+cEHH8im90i0QmeMjdFa15fpOD6vCrZthyvGqlk72MUM
_connectHandle != ((io_object_t) 0)
format is invalid!
Current process priviledge is not allowed by Key \"%@\"
Config \"%@\" for key \"%@\" is not a dictionary
Please make sure the process is using memory reasonably
Unknown
%@ length %@ is too long
mZfUC7qo4pURNhyMHZ62RQ
BMc2
Preference of key \"%@\" has an invalid retry number: %@!
Lockdown Connect Failed
bmu-board-id
auth,display
Method \"%@\" of key \"%@\" has a non-number retry number
p_is_alias
Initialization Failed
ACTION_RETRY
ZhuGe is runing on an unknown OS!
Cannot find IO entry from path \"%@\"!
Failed to match parent class of entry \"%@\" for key \"%@\"!
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
The key could possibly be a MobileGestalt key, not supported at all
The key is not supported by MobileGestalt
Trying to get IO iterator with condition of \"%@\"
MesaSensorIDSensorSNBufferSize %zu, should be %d
XJmjmvrLmAug+1qdKaBX910Aji9wPl4nTnUhrN8zNbZpw
Implementation error: Connection handle to AppleBiometricServices has a non-zero refcount and should be non-null but the handle is null!
Failed to match parent class and name of entry \"%@\" for key \"%@\"!
Entry \"%@\" failed check at %@/%@
```
