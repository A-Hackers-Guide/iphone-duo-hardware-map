# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 260,704 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 4264)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (11 classes, 3 protocols)

Classes: `NSArray`, `NSData`, `NSError`, `NSNumber`, `NSString`, `ZhuGeCache`, `ZhuGeInternalSupportAssistant`, `ZhuGeLocker`, `ZhuGeRestoreLog`, `ZhuGeSingleton`, `ZhuGeSupportAssistant`

Protocols: `ZhuGeInternalServiceProtocol`, `ZhuGeRestoreLogProtocol`, `ZhuGeServiceProtocol`

## Strings (750)

```
%{public}@
softlink:r:path:/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
ZhuGeSingleton
ZhuGeInternalServiceProtocol
ZhuGeRestoreLog
ZhuGeCache
ZhuGeRestoreLogProtocol
ZhuGeServiceProtocol
ZhuGeSupportAssistant
ZhuGeInternalSupportAssistant
ZhuGe
ZhuGeLocker
length
_cacheDict
descriptionFromZhuGeErrorCode:
logHandler
macAddressStringFromSysconfigDataSixByte:
setBulkInternalMGKeys:getValuesAndError:
setInterruptionHandler:
setIsXpcConnectionValid:
defaultManager
numberWithUnsignedInteger:
T@\"NSMutableArray\",&
dylibHandler
removeObjectForKey:
scanHexInt:
accessInstanceVariablesDirectly
numberWithBool:
graphicInfoArrayFromArray:
lastPathComponent
setCache:forKey:withError:
setMGKey:getValueAndError:
stringByLeftTrimmingCharacter:
initWithBytes:length:encoding:
substringToIndex:
T@\"NSNumber\",R,V_capacity
T@\"NSString\",R,V_name
_name
addEntriesFromDictionary:
cStringUsingEncoding:
componentsJoinedByString:
dataFromHexString:
helper
arrayWithArray:
integerFromCInt:size:isSigned:needSwap:
numberWithUnsignedShort:
pathWithComponents:
removeAllObjects
setExportedObject:
stringByPaddingToLength:withString:startingAtIndex:
stringWithFormat:
dataWithLength:
rangeAtIndex:
stringByTrimmingCharactersInSet:
stringWithUTF8String:
delCacheForKey:
getCacheForKey:
executeCacheRefresh
getSharedInstanceByName:withError:
recursiveMutex
setRemoteObjectInterface:
visibleStringFromData:
containsObject:
T@\"NSXPCConnection\",&
T@\"NSMutableDictionary\",R,V_cacheDict
_keysCacheForCopyValue
bytes
dictionaryWithObjects:forKeys:count:
firstObject
init
integerValue
isInternalAssistant
numberWithUnsignedChar:
setExportedInterface:
allKeys
setWithObjects:
arrayFromShellCommandString:
classList
initWithData:encoding:
synchronousRemoteObjectProxyWithErrorHandler:
userInfo
T^v
_cacheList
cacheDict
initWithFormat:arguments:
keysCacheForCopyValue
T^?,V_logHandler
dictionaryWithContentsOfFile:
getDylibHandlerWithError:
scannerWithString:
setClasses:forSelector:argumentIndex:ofReply:
setKey:andOptions:andPreferences:getValueAndError:
appendFormat:
integerFromData:size:truncate:isSigned:needSwap:
macAddressStringFromData:
objectAtIndex:
setBulkInternalKeys:getValuesAndError:
setBulkMGKeys:getValuesAndError:
cacheList
characterAtIndex:
fileExistsAtPath:isDirectory:
interfaceWithProtocol:
isEqualToString:
numberWithUnsignedInt:
scanInt:
setInternalMGKey:getValueAndError:
getConfigOfKey:withError:
isEqualToNumber:
sharedInstance
T@\"NSMutableArray\",R,V_cacheList
stringByRightTrimmingCharacter:
aRecursiveMutex
appendBytes:length:
cacheType
count
firstMatchInString:options:range:
isXpcConnectionValid
T@\"ZhuGeCache\",&,V_keysCacheForCopyValue
numberWithChar:
clearCache
code
initData
numberWithLongLong:
numberWithUnsignedLong:
setLogHandler:
UTF8String
stringFromData:
countByEnumeratingWithState:objects:count:
getInternalSupportPath
hasSuffix:
hexStringFromData:
isKey:withError:
mutableBytes
arrayWithObjects:count:
setBulkKeys:getValuesAndError:
setInvalidationHandler:
stringByReplacingOccurrencesOfString:withString:
ZhuGeDescription
numberWithUnsignedLongLong:
setObject:forKeyedSubscript:
stringByRemovingCharactersInString:
stringByTrimmingCharactersInString:
xpcConnection
numberWithLong:
isAtEnd
activate
callStackSymbols
ccccValue
isDataConvertibleToVisibleString:
setXpcConnection:
.cxx_destruct
description
errorWithDomain:code:userInfo:
numberWithInt:
substringFromIndex:
_capacity
_cacheType
addObject:
characterSetWithCharactersInString:
initWithCapacity:
numberWithInteger:
queryKey:andOptions:andPreferences:withError:
armoryClassName
boolFromData:needNegate:
errorWithZhuGeErrorCode:underlyingError:
intValue
removeObject:
numberWithShort:
setInternalKey:andOptions:andPreferences:getValueAndError:
setKeysCacheForCopyValue:
T#,R,V_cacheType
getObfuscatedKey:withError:
objectForKeyedSubscript:
printRemoteLog:withReply:
recursiveMutexForCopyValue
getBytes:range:
_logHandler
initWithServiceName:
name
processInfo
substringWithRange:
boolValue
capacity
dictionaryWithDictionary:
getXpcProxyWithError:
objectForKey:
regularExpressionWithPattern:options:error:
setDylibHandler:
domain
processName
registerCacheRefresh:
remoteObjectInterface
setCacheList:
TB
_ZhuGeDescriptionWithLayer:
initWithName:andCapacity:andCacheType:
^?
v24@0:8@16
B40@0:8@16@24^@32
#16@0:8
@\"NSMutableArray\"
^v24@0:8^@16
@\"ZhuGeCache\"
@24@0:8@16
@\"NSNumber\"
v32@0:8@16@?24
v48@0:8@16@24@32@?40
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
B16@0:8
v20@0:8B16
B24@0:8@16
v24@0:8^?16
@32@0:8Q16@24
@40@0:8@16@24#32
@16@0:8
v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
^{_opaque_pthread_mutex_t=q[56c]}16@0:8
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
v24@0:8^v16
@28@0:8@16B24
@24@0:8Q16
@\"NSString\"
#
@\"NSMutableDictionary\"
@24@0:8^@16
^?16@0:8
v16@0:8
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
@40@0:8Q16Q24B32B36
@20@0:8c16
@32@0:8@16^@24
^v16@0:8
@48@0:8@16Q24q32B40B44
In %@, aCache pointer is nil!
Failed to get proxy for \"%@\"!
Catch the NULL format pointer from: %s %s(%ld)
/dev/console
Issue may be due to the underlying error out of ZhuGe
ZhuGeIsKeyValid
ZhuGe Error module itself got some issues
Query key: \"%@\" in %@entrusted way
ACTION_SEQUENCE
Please check regEx related code in ZhuGe
Underlying service may be not ready
Please check the path of IO entry
Pointer Null
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
Device type in entry %@ is not disk image
The key is not supported by MobileGestalt
Reserved ZhuGeErrorCode %@ shall not be the argument
Initialization Failed
Query privilege of key: %@
Privilege
error p-pointer is nil!
May due to wrong implementation or system problem
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
Failed to find class symbol for \"%@\" with error: %s!
-restore
Method Invocation Get Failed
Length of some object is unexpected
Path not exists or the string is not a path
v16@?0@\"NSError\"8
-- %@
Failed to encode with proper API
aSIFK
Chipset Model
ACE Command Failed
XPC Service Entitlement Missing
libZhuGeInternalArmory.dylib
Error Customized
The dylib does not exists or too old version
IO Service Mismatching
Please make sure the entitlement is correctly configured
-[ZhuGeCache setCache:forKey:withError:]
+[ZhuGeSupportAssistant getSharedInstanceByName:withError:]
Array entitlement sub-entitlement %@ value mismatched: expected \"%@\", actual \"%@\"!
ZhuGe Key Not Supported
Please file a radar against \"ZhuGe|all\"
The option passed in is not supported
Failed to get configuration for \"%@\" in privilege query!
%@
i
Data Convert To Nil
The input data may be unexpected and cannot be processed
In bulk query, failed to get the values from %@entrusted ZhuGe!
Cannot open certain file
Input may be missing subkey(s), or something wrong with flexible pattern definition
Wrong key or the key is not configured
Failed to create IORegistryEntry iterator
JSON String Invalid
Entitlement Unsupported
End: bulk query privileges
Didn't find ZhuGe internal Support Path
<%@ %@(%@)>
ERR
Stack only has %@ layers, not great than %@
Stack got %@ layers, not great than %@
is_deprecatedSoon
Entrusted way is configured
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]
Bits will be truncated since real size is %@, while required size is %@
Failed to link libcryptex.dylib!
Something might be wrong with Near Field component
Get dylib shared instance for \"%@\" from cache
No mobile storage device is detected
The ACE command returns an error
Img4 API Failed
%s <%s %s(%ld)> ERR: 
Please check sysdiagnose FDR related log
Flexible key doesn't macth its pattern
Please make sure the process is using memory reasonably
Current OS is not defined
SMC Key Type Wrong
Please check the CLI option that input
Please make sure the file exists
Lockdown Query Failed
Current process is not a XPC service process
CACHEABLE
/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib
%s%s\n
RegEx doesn't match layer %@
May due to an invalid IO Service
Key of dictionary is redundant
Operation is not done in certain time
Failed to get a proxy for \"%@\"!
ZhuGeInternalService.xpc
MGQuery
String Format Wrong
%@ failed to provide a proxy with error : %@!
The path just doesn't exist or the way to find the path is incorrect.
The system profiler report crashed
Please check sysconfig key name input
Option or input value is not in defined range
SecCertificate API Failed
RegEx doesn't further match layer %@
Caller's entitlement value is mismatched with required one
Failed to get service proxy for \"%@\"!
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupportAssistant.m
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
Failed to link mobile storage framework
PropertyList Serialization Failed
Code Max
OBJC_CLASS_$_ZhuGeLockerArmory
In bulk query, failed to get the values from internal entrusted MG!
\x85
Failed to get a shared instance for \"%@\"!
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m
Internal XPC connection is already available
Entry %@ doesn't contain a correct personalized image type
Please check whether the dylib provided correctly
SP Report Crashed
Please make sure the Caller has the correct entitlement
Illegal ZhuGe Error Code!
OBJC_CLASS_$_ZhuGeLockerInternalArmory
\"%@\" is not a ZhuGe native key!
(null)
Failed to get Cryptex paths
FactoryDiskImage
Please check whether the user has the privilege
Value Out Of Range
Skip retrieving internal support path in restoreOS
cryptexIdentifier pointer is nil!
Dictionary entitlement sub-entitlement %@ value mismatched: expected \"%@\", actual \"%@\"!
The system profiler data type is null
XPC Service Not Exist
This error code should never be reported
Failed to get obfuscated key for \"%@\"!
com.apple.ZhuGeInternalService
Memory Exhausted
 or 
v24@?0@\"NSDictionary\"8@\"NSError\"16
ACTION_QUERY_PATH
Failed to get ZhuGe armory handler!
Checking entry %@
The property list cannot be serialized
ZhuGe internal support path is updated to: %@
WRN
ReleaseType
^\\d+\\s+(\\S+)\\s+\\S+\\s+([^+-]\\S+|[+-]\\[.+\\])\\s*.*$
sppci_model
Check error description to understand failure reason
v24@?0@8@\"NSError\"16
Entrusted way is preferred
MSB
QueryPath_Entrusted
Failed to dlopen ZhuGe internal armory dylib with error: %s!
Added %@ to FDI paths array
User have no proper access
Check the string in code or input source
com.apple.FactoryCryptexSupport
Lockdown Connect Failed
XPC Service Not Available
Index %@ of ZhuGeErrorCode table got a wrong code %@
armoryInstanceForKey
atm_diagnostic_config
Name of the call back function doesn't exist in library
Device may not support the service
Path Not Found
Unexpected SMC Key Size returned
Entitlement Mismatched
Query privilege of original key: %@
In bulk query, failed to get query path for \"%@\"!
In %@, error p-pointer is nil!
ROM Revision
Failed to call SMC APIs, unsupported SMC key etc.
ZhuGeErrorCode %@ exceed maximum
getZhuGeCryptexPathsWithError
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
Device ID
Please check whether the call back function name exists in the library
XPC Service Connect Failed
In bulk query, \"%@\" is not a ZhuGe key nor a MobileGestalt key!
QueryPath_Straight
Path of IO entry might be wrong
Key Duplicated
The failure might be expected without specific hardware
We may need to check with libSMC together
Failed to get configurations for \"%@\"!
Value
IO Property Not Found
keysArray pointer is NULL!
Failed to cache value for key \"%@\", error: %@!
\"%@\" is not a vaild MobileGestalt key!
Call Back Function Not Found
Class Type Wrong
The data indexed by the indexArray is not valid
zhuge_debug
+[ZhuGeSupportAssistant getXpcProxyWithError:]
Option of the CLI command is not supported
In bulk query, failed to get configurations for \"%@\"!
ZhuGe-459.40.2
Retrieving unchanged internal supported path: %@
%s\n
:
Please contact Near Field team for issue triaging
ZhuGeSetLogHandler
key pointer is NULL!
PRIVILEGE
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
User defaults doesn't support the specific domain
MobileGestalt Not Supported
Get failure when calling API of Img4
Failed to cache dylib shared instance for key \"%@\"!
%s: 
[ZhuGe]
graphicsArray pointer is nil!
Please check whether device supports the service
Name of queried sysconfig key might be wrong
%@ 
Quotation \"%c\" is not paired in command \"%@\"!
Cannot connect to lockdown daemon via a local socket
Sysctl Failed
is_cacheable
domainForKey
ZhuGe is running well
Flexible ZhuGe Key Invalid
Please make sure the correct SE type is input
Option ROM Version
Please check whether the key or alias input correct, or implemented.
CLI Option Unsupported
Please make sure IO Service is valid
Object Type Invalid
The system profiler exited
Please make sure the option is correct
w
Failed to open IO Master port
Near Field API Failed
Near Field SE Type Invalid
v8@?0
OBJC_CLASS_$_ZhuGeArmory
Straight way will be picked
+[ZhuGeSupportAssistant isKey:withError:]
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2
Data Convert Failed
Please check whether the path using is correct
SMC Service Unsupported
Failed to get obfuscated key for \"%@\" in privilege query!
+[ZhuGeSupportAssistant getDylibHandlerWithError:]
Failed to have shared instance for \"%@\"!
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke
Array entitlement missing sub-entitlement %@: expected \"%@\", actual \"%@\"!
Error
Please make sure locakdown daemon and local sockets work well
Get failure when calling API of AppleMobileFileIntegrity
INF
FDR API Failed
Path Not Absolute
Sysconfig Key Invalid
Unknown class name!
ZhuGeSupport
IO Entry Not Found
Please make sure the domain is correctly inputted
%s %@
???
ZhuGePrintStderr
String entitlement value mismatched: expected \"%@\", actual \"%@\"!
Usually this error code shall not be displayed
\"%@\" is not a ZhuGe key nor a MobileGestalt key!
In bulk query, failed to get the service proxy!
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeUtils.m
Failed to get domain for \"%@\"!
Entry %@ doesn't contain personalized image type
May due to an invalid IO entry
String is invalid, like unpaired quotation, bracket etc.
ACTION_ENTITLEMENT
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/NSNumber+ZhuGe.m
RegEx Not Matched
Query key: \"%@\" in %@straight way
com.apple.AppleDeviceQueryService
Unsupport entitlement: expects \"%@\", actually \"%@\"!
kMobileStorageDeviceTypeKey
Preferences
Entrusted way will be picked
CFPreference Error
Path Invalid
Maybe the name for querying is incorrect
Project=%@; Caller=%@; %s=0x%llx; %s
QueryPath
+[ZhuGeInternalSupportAssistant getInternalSupportPath]
Required size is %@, while usually it should be %@ or %@ or %@ or %@
LSB
Failed to cache domain for key \"%@\", error: %@!
Entry %@ doesn't contain a valid personalized image type
SMC key information indicate a wrong type
Path or name of XPC service might be incorrect
Failed to get locker instance from armory, error: %@!
ZhuGeBulkCopyValues
Please check your code to use a correct class
In bulk query, for key: \"%@\"%@, value: %@, error: %@
\n
Entry %@ is not a dictionary
In bulk query, failed to cache value for key \"%@\", error: %@!
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4
+[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]
So far so good, keep going
Get failure when calling API of libFDR
No SMC service available on this device.
q
getZhuGeFDIPathsWithError
Straight way was chosen, but entitlement mismatched: expected %@, actual %@!
ZCV
Check error description to find out recvoery suggestion
Type of some object is invalid
All possible tries has failed
ZhuGeCopyValue
ACTION_QUERY_PATH_STRAIGHT
UnknownFunc
Failed to lookup mobile storage devices
Entry %@ doesn't contain a valid device type
Encode Failed
XPC Service denied access due to lacking of entitlement
{\n%@%@\n%@}
Begin: bulk query privileges
keys pointer is NULL!
/usr/local/ZhuGe/ZhuGeInternalSupport
Issue Underlying
ZhuGe received a relative path
In bulk query, query key: \"%@\" in %@straight way
ACTIONS
/usr/local/lib/libcryptex.dylib
MobileStorageCopyDevicesWithError
\x91
This failure is intentionally, please check the input data length, content etc.
ZhuGeLog
Please check sysdiagnose for more clue
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
cryptex_msm_array_destroy
One graphic in graphics array does not contain \"sppci_model\"
Options
ACTION_QUERY_PATH_ENTRUSTED
cryptex_msm_get_string
One graphic in graphics array is not a dictionary, ignore it.
SMC Key Name Invalid
Pattern string can not cover the case
internal 
For key: \"%@\"%@, value: %@, error: %@
Query privilege of key: %@ from MobileGestalt
In bulk query, failed to get obfuscated key for \"%@\"!
In %@, aKey pointer is nil!
Please make sure the way using ZhuGe is correct
Caching value for key: \"%@\"
Query original key: %@
Entitlement type mismatched: expected \"%@\", actual \"%@\"!
Dictionary entitlement missing sub-entitlement %@: expected \"%@\", actual \"%@\"!
Please check sysdiagnose for more detail
Please check newly added code that calling ZhuGeError API
Dylib Not Available
Method Signature Get Failed
Please make sure the key string is correct
LoggingSimulating
In %@, key \"%@\" got a wrong cache class type \"%@\"!
Failed to decode with proper API
Please check whether there is any underlying isse in the encoding API.
Didn't successfully call init related method
ZhuGe Key Not Native Supported
original_key
+[NSArray(ZhuGe) arrayFromShellCommandString:]
Maybe the method name is incorrect
The key is not a ZhuGe native key
Failed to get the service proxy for \"%@\"!
In bulk query, failed to get armory shared instance for \"%@\"!
Connection to \"%@\" interrupted!
key pointer is nil!
File Open Failed
SP Data Type Null
Stright way is preferred
Specific Hardware Needed
Tries All Failed
queryPathForConfigAndPref
Failed to get armory shared instance for \"%@\" in privilege query!
hHlMwws2VQHQYigJJ/5rH0A/jBQDSHL7oVazpEgFDfaME
Full call stacks are: %@
CFPreference API return error
Permission Denied
Added %s to Cryptex paths array
Memory is not enough
Query key: \"%@\" from internal entrusted MG
Some internal issues happened when converting data
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
Failed to create SecTask for self!
Error System Issue
Probaby the wrong arguments defined in xml
Entry %@ doesn't contain a valid personalized disk image path
Object Length Invalid
Some pointer shall not be NULL
Please make sure IO Service connection is valid
The system profiler report failed to be created
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeLog.m
%s ERR: Cannot print serial log!\n
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke
{%d:0x%llx}
 
Please check path of the code calling CFPreference
ZhuGeCopyPrivilege
Query key: \"%@\" from cache
Connection to \"%@\" invalidated!
Failed to get FDI paths
cryptex_copy_list_4MSM
Didn't successfully get data due to lacking of specific hardware
MobileGestalt: %@, error: %@
MGkey pointer is nil!
Method Invoke Failed
Number entitlement value mismatched: expected \"%@\", actual \"%@\"!
The string is not a valid ZhuGe key
Option Unsupported
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeCache.m
Failed to get entitlements, error: %@!
ZHUGE_NULL
getCallerString
%02x
Please check latest code that using ZhuGe error API
%@%@
UnknownFile
Maybe the method itself got some issue
SMC Service Failed
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
Time Out
DEPRECATED_SOON
Q
isEntitlementExpected
kMobileStorageDeviceTypeDiskImage
IO Service Open Failed
ZhuGe Key Further Check Needed
AMFI Get Failed
Unsupported ZhuGe key \"%@\" in privilege query!
PersonalizedImageType
The entry %@ mounted personalized disk image with type %@
IODeviceTree:/options
VBIOS Version
ENTITLEMENT
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3
%s
(DEPRECATED SOON!)
dFK
Please check whether the path of XPC service correct and existing
For key: \"%@\", privilege: %@, error: %@
Failed to get armory shared instance for \"%@\"!
Get domain for \"%@\" from cache
May due to an invalid IO Service connection
SP Report Creation failed
User Defaults Domain Not Exists
Get failure when calling API of SecCertificate
Unsupported preferred way: \"%@\"!
Invalid ZhuGe Error Code!
Begin: bulk query values
In bulk query, the key \"%@\" is repeated, skip: %@
--> %@ -- %@
In bulk query, too many elements in an embedded dictionary, only allows one! The wrong dictionary: %@!
printZhuGeInfoOnce_block_invoke
OBJC_CLASS_$_ZhuGeInternalArmory
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
/System/Library/CoreServices/SystemVersion.plist
Nothing Wrong
IO Service Get Failed
Maybe the method name or signature is incorrect
OS Unsupported
OS Unknown
Didn't find the expected path
Please check if you really want to try this function in current OS or environment
Unsupported SE Type
Stright way is configured
Failed to dlopen ZhuGe armory dylib with error: %s!
Failed to copy cryptex list, error %d(%s)
Please check whether there is any underlying isse in the decoding API.
SP Exited
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/NSArray+ZhuGe.m
SMC Key Size Unexpected
Unsupported entitlement or the entitlement type
This special error code is used for ZhuGe configuration analysis
ZhuGe only supports absolute path, caller needs to convert relative path by itself
%s ERR: 
/usr/lib/libcryptex.dylib
kMobileStorageMountPathKey
com.apple.zhuge
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupport.m
ZhuGeBulkCopyPrivileges
Unsupported configured way: \"%@\"!
XPC connection is already available
Failed to get ZhuGe internal support path for dylib handler!
Restore
VRAM Size
SP Data Report Invalid
Found regEx error: %@
Failed to get query path for \"%@\"!
Bool entitlement value mismatched: expected \"%@\", actual \"%@\"!
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
Please check sysdiagnose lockdown related log
The key could possibly be a MobileGestalt key, not supported at all
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2
Failed to get ZhuGe internal support path for xpc proxy!
Query key: \"%@\" in temporary entrusted way
In bulk query, get value for key \"%@\" from cache
Failed to set dylib shared instance cache for key \"%@\", error: %@!
Specific function isn't supported in current OS or environment.
Please check the name that being querying
BoraSikPub
Failed to get the temporary service proxy for \"%@\"!
Decode Failed
Please check the data source or code
IO Service Close Failed
Key Not Found
XPC service name may be invalid
End: bulk query values
Failed to connect \"%@\"!
Please make sure the key being querying correct
In bulk query, unsupported element in the keys array: %@!
```
