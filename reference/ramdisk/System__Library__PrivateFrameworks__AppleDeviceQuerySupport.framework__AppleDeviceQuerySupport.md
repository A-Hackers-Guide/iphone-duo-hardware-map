# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`

From the upgrade restore ramdisk (141-29011-104.dmg). 260,704 bytes.

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
setBulkInternalMGKeys:getValuesAndError:
visibleStringFromData:
.cxx_destruct
T@\"NSString\",R,V_name
dataWithLength:
errorWithDomain:code:userInfo:
numberWithInteger:
setInternalKey:andOptions:andPreferences:getValueAndError:
initWithName:andCapacity:andCacheType:
aRecursiveMutex
cacheList
getConfigOfKey:withError:
getDylibHandlerWithError:
hasSuffix:
numberWithUnsignedLongLong:
T@\"NSXPCConnection\",&
cacheType
characterAtIndex:
code
T@\"ZhuGeCache\",&,V_keysCacheForCopyValue
accessInstanceVariablesDirectly
T^?,V_logHandler
description
initWithCapacity:
initWithFormat:arguments:
isDataConvertibleToVisibleString:
ZhuGeDescription
cacheDict
initData
initWithServiceName:
setInterruptionHandler:
stringByPaddingToLength:withString:startingAtIndex:
delCacheForKey:
isAtEnd
_cacheType
addObject:
boolValue
getInternalSupportPath
keysCacheForCopyValue
name
getCacheForKey:
allKeys
stringFromData:
initWithBytes:length:encoding:
isXpcConnectionValid
stringByTrimmingCharactersInSet:
substringFromIndex:
UTF8String
_cacheList
appendBytes:length:
appendFormat:
dictionaryWithContentsOfFile:
errorWithZhuGeErrorCode:underlyingError:
stringByLeftTrimmingCharacter:
stringWithUTF8String:
cStringUsingEncoding:
characterSetWithCharactersInString:
isKey:withError:
length
numberWithInt:
arrayWithArray:
_cacheDict
integerFromData:size:truncate:isSigned:needSwap:
integerValue
setCache:forKey:withError:
setCacheList:
setKeysCacheForCopyValue:
setObject:forKeyedSubscript:
T@\"NSNumber\",R,V_capacity
descriptionFromZhuGeErrorCode:
executeCacheRefresh
lastPathComponent
regularExpressionWithPattern:options:error:
setBulkInternalKeys:getValuesAndError:
setInternalMGKey:getValueAndError:
sharedInstance
ccccValue
_capacity
numberWithBool:
numberWithLongLong:
objectForKeyedSubscript:
queryKey:andOptions:andPreferences:withError:
recursiveMutexForCopyValue
setIsXpcConnectionValid:
_name
clearCache
numberWithUnsignedChar:
numberWithUnsignedInt:
numberWithUnsignedLong:
setExportedObject:
setLogHandler:
capacity
getXpcProxyWithError:
macAddressStringFromData:
macAddressStringFromSysconfigDataSixByte:
objectForKey:
setExportedInterface:
stringByRemovingCharactersInString:
numberWithLong:
setMGKey:getValueAndError:
firstMatchInString:options:range:
getObfuscatedKey:withError:
scanHexInt:
setWithObjects:
arrayWithObjects:count:
boolFromData:needNegate:
classList
initWithData:encoding:
setClasses:forSelector:argumentIndex:ofReply:
callStackSymbols
fileExistsAtPath:isDirectory:
mutableBytes
T@\"NSMutableArray\",R,V_cacheList
_logHandler
dataFromHexString:
firstObject
isEqualToString:
_ZhuGeDescriptionWithLayer:
stringByRightTrimmingCharacter:
activate
componentsJoinedByString:
getSharedInstanceByName:withError:
helper
setDylibHandler:
substringToIndex:
count
graphicInfoArrayFromArray:
pathWithComponents:
rangeAtIndex:
setXpcConnection:
T@\"NSMutableDictionary\",R,V_cacheDict
TB
numberWithChar:
dictionaryWithDictionary:
numberWithShort:
userInfo
T#,R,V_cacheType
addEntriesFromDictionary:
dylibHandler
integerFromCInt:size:isSigned:needSwap:
logHandler
registerCacheRefresh:
stringByTrimmingCharactersInString:
armoryClassName
_keysCacheForCopyValue
init
printRemoteLog:withReply:
recursiveMutex
remoteObjectInterface
stringWithFormat:
hexStringFromData:
isEqualToNumber:
processInfo
removeObject:
scannerWithString:
setKey:andOptions:andPreferences:getValueAndError:
getBytes:range:
scanInt:
setInvalidationHandler:
arrayFromShellCommandString:
T^v
containsObject:
setBulkMGKeys:getValuesAndError:
synchronousRemoteObjectProxyWithErrorHandler:
bytes
dictionaryWithObjects:forKeys:count:
intValue
numberWithUnsignedShort:
xpcConnection
objectAtIndex:
setBulkKeys:getValuesAndError:
substringWithRange:
T@\"NSMutableArray\",&
defaultManager
numberWithUnsignedInteger:
processName
removeAllObjects
removeObjectForKey:
setRemoteObjectInterface:
stringByReplacingOccurrencesOfString:withString:
countByEnumeratingWithState:objects:count:
domain
interfaceWithProtocol:
isInternalAssistant
v24@0:8@16
@32@0:8@16^@24
@24@0:8^@16
@48@0:8@16Q24q32B40B44
v24@0:8^?16
#
^v16@0:8
^?
B40@0:8@16@24^@32
@\"NSNumber\"
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
@32@0:8Q16@24
v16@0:8
v48@0:8@16@24@32@?40
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
^{_opaque_pthread_mutex_t=q[56c]}16@0:8
@28@0:8@16B24
@16@0:8
@\"NSMutableArray\"
v24@0:8^v16
@\"ZhuGeCache\"
#16@0:8
@\"NSMutableDictionary\"
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
@20@0:8c16
^?16@0:8
v20@0:8B16
v32@0:8@16@?24
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
B16@0:8
^v24@0:8^@16
@40@0:8Q16Q24B32B36
B24@0:8@16
@40@0:8@16@24#32
@24@0:8@16
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
@\"NSString\"
@24@0:8Q16
cryptex_msm_array_destroy
Quotation \"%c\" is not paired in command \"%@\"!
Issue may be due to the underlying error out of ZhuGe
Please check sysdiagnose for more detail
%@ failed to provide a proxy with error : %@!
%@%@
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
Invalid ZhuGe Error Code!
Failed to get locker instance from armory, error: %@!
/dev/console
FactoryDiskImage
Maybe the method name or signature is incorrect
Entry %@ doesn't contain a valid personalized disk image path
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
OBJC_CLASS_$_ZhuGeArmory
Failed to get configuration for \"%@\" in privilege query!
Bool entitlement value mismatched: expected \"%@\", actual \"%@\"!
ZhuGeSetLogHandler
Failed to get a shared instance for \"%@\"!
Error System Issue
Please check the path of IO entry
Path Not Found
Path Invalid
Please make sure the option is correct
Failed to get entitlements, error: %@!
/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeUtils.m
getZhuGeFDIPathsWithError
Current OS is not defined
SP Data Type Null
Restore
Please check whether the path of XPC service correct and existing
Get failure when calling API of Img4
The entry %@ mounted personalized disk image with type %@
+[ZhuGeInternalSupportAssistant getInternalSupportPath]
Entry %@ doesn't contain personalized image type
ZhuGeCopyPrivilege
In bulk query, the key \"%@\" is repeated, skip: %@
In bulk query, failed to get obfuscated key for \"%@\"!
%@
IODeviceTree:/options
Something might be wrong with Near Field component
Reserved ZhuGeErrorCode %@ shall not be the argument
Failed to get a proxy for \"%@\"!
--> %@ -- %@
%02x
OS Unsupported
\"%@\" is not a ZhuGe native key!
The input data may be unexpected and cannot be processed
JSON String Invalid
Query key: \"%@\" in temporary entrusted way
Failed to get the temporary service proxy for \"%@\"!
queryPathForConfigAndPref
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeCache.m
getCallerString
+[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]
ReleaseType
FDR API Failed
Cannot open certain file
IO Entry Not Found
Memory is not enough
The key could possibly be a MobileGestalt key, not supported at all
Please make sure the key string is correct
Q
isEntitlementExpected
File Open Failed
IO Service Mismatching
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupportAssistant.m
Failed to get FDI paths
%s\n
Initialization Failed
Path Not Absolute
XPC Service Not Exist
Failed to get ZhuGe internal support path for xpc proxy!
Bits will be truncated since real size is %@, while required size is %@
Memory Exhausted
The failure might be expected without specific hardware
SMC Key Size Unexpected
original_key
Option ROM Version
This failure is intentionally, please check the input data length, content etc.
BoraSikPub
\"%@\" is not a ZhuGe key nor a MobileGestalt key!
Failed to get the service proxy for \"%@\"!
%s: 
The string is not a valid ZhuGe key
Options
libZhuGeInternalArmory.dylib
No mobile storage device is detected
Entry %@ doesn't contain a valid device type
Privilege
i
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
Probaby the wrong arguments defined in xml
All possible tries has failed
Entry %@ doesn't contain a correct personalized image type
Option or input value is not in defined range
Begin: bulk query values
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4
w
Please check the data source or code
For key: \"%@\"%@, value: %@, error: %@
ZCV
Option Unsupported
Query original key: %@
hHlMwws2VQHQYigJJ/5rH0A/jBQDSHL7oVazpEgFDfaME
+[ZhuGeSupportAssistant isKey:withError:]
This error code should never be reported
Failed to have shared instance for \"%@\"!
+[ZhuGeSupportAssistant getXpcProxyWithError:]
<%@ %@(%@)>
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/NSArray+ZhuGe.m
XPC Service Entitlement Missing
Failed to cache domain for key \"%@\", error: %@!
Failed to connect \"%@\"!
%s
OS Unknown
The system profiler data type is null
Query key: \"%@\" from internal entrusted MG
Straight way will be picked
/usr/local/ZhuGe/ZhuGeInternalSupport
Stack only has %@ layers, not great than %@
The data indexed by the indexArray is not valid
Unsupported entitlement or the entitlement type
Failed to cache dylib shared instance for key \"%@\"!
Internal XPC connection is already available
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
Data Convert Failed
Please check whether device supports the service
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/ZhuGeLog.m
Please check whether the user has the privilege
DEPRECATED_SOON
UnknownFunc
ERR
graphicsArray pointer is nil!
Failed to get obfuscated key for \"%@\" in privilege query!
In bulk query, failed to get query path for \"%@\"!
ZhuGe Error module itself got some issues
Error Customized
Some internal issues happened when converting data
Unsupported preferred way: \"%@\"!
For key: \"%@\", privilege: %@, error: %@
Error
zhuge_debug
Check error description to understand failure reason
Failed to dlopen ZhuGe internal armory dylib with error: %s!
INF
Failed to link libcryptex.dylib!
Dictionary entitlement missing sub-entitlement %@: expected \"%@\", actual \"%@\"!
Data Convert To Nil
domainForKey
ZhuGe Key Not Supported
Name of queried sysconfig key might be wrong
key pointer is NULL!
%s%s\n
Failed to copy cryptex list, error %d(%s)
The key is not supported by MobileGestalt
key pointer is nil!
internal 
keys pointer is NULL!
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3
%s <%s %s(%ld)> ERR: 
\x91
Get failure when calling API of SecCertificate
Failed to get armory shared instance for \"%@\"!
Get domain for \"%@\" from cache
Array entitlement missing sub-entitlement %@: expected \"%@\", actual \"%@\"!
Call Back Function Not Found
Failed to decode with proper API
Img4 API Failed
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupport.m
is_cacheable
Failed to find class symbol for \"%@\" with error: %s!
WRN
Chipset Model
ZhuGePrintStderr
:
Option of the CLI command is not supported
Key Not Found
Path or name of XPC service might be incorrect
In bulk query, \"%@\" is not a ZhuGe key nor a MobileGestalt key!
Connection to \"%@\" invalidated!
???
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
VBIOS Version
Flexible key doesn't macth its pattern
Get failure when calling API of libFDR
SP Report Crashed
^\\d+\\s+(\\S+)\\s+\\S+\\s+([^+-]\\S+|[+-]\\[.+\\])\\s*.*$
kMobileStorageMountPathKey
Please check whether there is any underlying isse in the decoding API.
v16@?0@\"NSError\"8
kMobileStorageDeviceTypeDiskImage
Flexible ZhuGe Key Invalid
Caller's entitlement value is mismatched with required one
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
Please check whether the path using is correct
ZhuGeBulkCopyPrivileges
In bulk query, failed to cache value for key \"%@\", error: %@!
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeCommon/NSNumber+ZhuGe.m
Underlying service may be not ready
Index %@ of ZhuGeErrorCode table got a wrong code %@
The system profiler report crashed
v24@?0@\"NSDictionary\"8@\"NSError\"16
Full call stacks are: %@
Please check your code to use a correct class
Method Invoke Failed
Please make sure the process is using memory reasonably
In bulk query, get value for key \"%@\" from cache
In %@, aKey pointer is nil!
ZhuGeLog
Added %s to Cryptex paths array
Check error description to find out recvoery suggestion
Path of IO entry might be wrong
Key Duplicated
No SMC service available on this device.
Entrusted way will be picked
Entry %@ is not a dictionary
PropertyList Serialization Failed
Stright way is configured
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2
RegEx doesn't further match layer %@
Unsupport entitlement: expects \"%@\", actually \"%@\"!
Failed to encode with proper API
Check the string in code or input source
\n
Device ID
ROM Revision
Didn't successfully call init related method
In %@, error p-pointer is nil!
cryptex_copy_list_4MSM
May due to an invalid IO Service connection
Value Out Of Range
In bulk query, query key: \"%@\" in %@straight way
ZhuGe-459.40.2
Device type in entry %@ is not disk image
Dylib Not Available
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
RegEx Not Matched
Pattern string can not cover the case
XPC Service denied access due to lacking of entitlement
Please check newly added code that calling ZhuGeError API
Please check latest code that using ZhuGe error API
Please check sysdiagnose for more clue
Near Field API Failed
In bulk query, too many elements in an embedded dictionary, only allows one! The wrong dictionary: %@!
In bulk query, failed to get the values from internal entrusted MG!
CFPreference API return error
Cannot connect to lockdown daemon via a local socket
Length of some object is unexpected
User defaults doesn't support the specific domain
ACTION_QUERY_PATH_STRAIGHT
Failed to create SecTask for self!
/Library/Caches/com.apple.xbs/9E4E8628-8851-4889-8053-4A3473C4A9F3/TemporaryDirectory.SzDH2T/Sources/ZhuGe/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2
Please check sysdiagnose FDR related log
User have no proper access
+[ZhuGeSupportAssistant getDylibHandlerWithError:]
Failed to get Cryptex paths
Unknown class name!
Method Signature Get Failed
The option passed in is not supported
SecCertificate API Failed
Caching value for key: \"%@\"
is_deprecatedSoon
Failed to link mobile storage framework
Operation is not done in certain time
Please make sure the Caller has the correct entitlement
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]
SP Report Creation failed
Failed to get service proxy for \"%@\"!
End: bulk query values
In bulk query, failed to get the service proxy!
/usr/lib/libcryptex.dylib
Please make sure the entitlement is correctly configured
ZhuGe Key Not Native Supported
/System/Library/CoreServices/SystemVersion.plist
The ACE command returns an error
AMFI Get Failed
Failed to get configurations for \"%@\"!
In bulk query, unsupported element in the keys array: %@!
Catch the NULL format pointer from: %s %s(%ld)
Path not exists or the string is not a path
We may need to check with libSMC together
 
\"%@\" is not a vaild MobileGestalt key!
MobileStorageCopyDevicesWithError
IO Property Not Found
SMC Key Type Wrong
XPC service name may be invalid
Illegal ZhuGe Error Code!
{\n%@%@\n%@}
Query privilege of original key: %@
RegEx doesn't match layer %@
Lockdown Query Failed
Please check if you really want to try this function in current OS or environment
Unexpected SMC Key Size returned
Failed to call SMC APIs, unsupported SMC key etc.
Please make sure the domain is correctly inputted
May due to an invalid IO entry
IO Service Open Failed
The path just doesn't exist or the way to find the path is incorrect.
This special error code is used for ZhuGe configuration analysis
In %@, key \"%@\" got a wrong cache class type \"%@\"!
ZhuGeSupport
One graphic in graphics array is not a dictionary, ignore it.
SP Data Report Invalid
Please check sysconfig key name input
{%d:0x%llx}
ZhuGe received a relative path
Code Max
Straight way was chosen, but entitlement mismatched: expected %@, actual %@!
Device may not support the service
Please contact Near Field team for issue triaging
Please check the name that being querying
Stright way is preferred
+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke
String entitlement value mismatched: expected \"%@\", actual \"%@\"!
ZhuGe is running well
IO Service Get Failed
May due to an invalid IO Service
In bulk query, failed to get armory shared instance for \"%@\"!
Entrusted way is preferred
ZhuGeInternalService.xpc
MGkey pointer is nil!
In %@, aCache pointer is nil!
com.apple.AppleDeviceQueryService
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
Query key: \"%@\" in %@straight way
%s %@
Array entitlement sub-entitlement %@ value mismatched: expected \"%@\", actual \"%@\"!
Please check whether the dylib provided correctly
ZhuGe Key Further Check Needed
In bulk query, failed to get the values from %@entrusted ZhuGe!
q
Unsupported configured way: \"%@\"!
Failed to get ZhuGe armory handler!
Connection to \"%@\" interrupted!
Nothing Wrong
Please check whether there is any underlying isse in the encoding API.
Sysconfig Key Invalid
ZhuGe internal support path is updated to: %@
Failed to get proxy for \"%@\"!
Specific function isn't supported in current OS or environment.
In bulk query, failed to get configurations for \"%@\"!
cryptexIdentifier pointer is nil!
Please file a radar against \"ZhuGe|all\"
Method Invocation Get Failed
SMC Service Failed
Failed to set dylib shared instance cache for key \"%@\", error: %@!
MGQuery
kMobileStorageDeviceTypeKey
Maybe the name for querying is incorrect
Entitlement type mismatched: expected \"%@\", actual \"%@\"!
ZhuGeIsKeyValid
ACTIONS
ZHUGE_NULL
Decode Failed
Please make sure IO Service is valid
Time Out
The key is not a ZhuGe native key
Pointer Null
Unsupported ZhuGe key \"%@\" in privilege query!
ZhuGeCopyValue
Didn't find ZhuGe internal Support Path
com.apple.ZhuGeInternalService
Number entitlement value mismatched: expected \"%@\", actual \"%@\"!
The property list cannot be serialized
Failed to dlopen ZhuGe armory dylib with error: %s!
ACE Command Failed
The dylib does not exists or too old version
User Defaults Domain Not Exists
Entrusted way is configured
+[ZhuGeSupportAssistant getSharedInstanceByName:withError:]
%s ERR: 
keysArray pointer is NULL!
Failed to get obfuscated key for \"%@\"!
armoryInstanceForKey
Please make sure the key being querying correct
Maybe the method itself got some issue
Permission Denied
SMC Key Name Invalid
OBJC_CLASS_$_ZhuGeLockerInternalArmory
v24@?0@8@\"NSError\"16
\x85
Please check whether the key or alias input correct, or implemented.
Begin: bulk query privileges
Please check path of the code calling CFPreference
CLI Option Unsupported
Specific Hardware Needed
Please make sure the correct SE type is input
ZhuGeErrorCode %@ exceed maximum
OBJC_CLASS_$_ZhuGeLockerArmory
Query privilege of key: %@
(DEPRECATED SOON!)
aSIFK
Failed to get domain for \"%@\"!
ZhuGe only supports absolute path, caller needs to convert relative path by itself
Usually this error code shall not be displayed
MobileGestalt Not Supported
Please check whether the call back function name exists in the library
Class Type Wrong
SMC key information indicate a wrong type
Current process is not a XPC service process
Failed to cache value for key \"%@\", error: %@!
OBJC_CLASS_$_ZhuGeInternalArmory
error p-pointer is nil!
Skip retrieving internal support path in restoreOS
/usr/local/lib/libcryptex.dylib
Name of the call back function doesn't exist in library
CFPreference Error
Please make sure the file exists
Type of some object is invalid
Query key: \"%@\" in %@entrusted way
Required size is %@, while usually it should be %@ or %@ or %@ or %@
Entry %@ doesn't contain a valid personalized image type
The system profiler exited
Please make sure locakdown daemon and local sockets work well
Sysctl Failed
 or 
ACTION_QUERY_PATH_ENTRUSTED
-[ZhuGeCache setCache:forKey:withError:]
Lockdown Connect Failed
Unsupported SE Type
Query key: \"%@\" from cache
VRAM Size
Please make sure IO Service connection is valid
SMC Service Unsupported
CACHEABLE
[ZhuGe]
Issue Underlying
Failed to open IO Master port
Tries All Failed
Get failure when calling API of AppleMobileFileIntegrity
MobileGestalt: %@, error: %@
Value
ACTION_SEQUENCE
PersonalizedImageType
+[NSArray(ZhuGe) arrayFromShellCommandString:]
String is invalid, like unpaired quotation, bracket etc.
Maybe the method name is incorrect
Object Type Invalid
ZhuGeBulkCopyValues
ACTION_QUERY_PATH
Retrieving unchanged internal supported path: %@
printZhuGeInfoOnce_block_invoke
-restore
%@ 
cryptex_msm_get_string
Near Field SE Type Invalid
Some pointer shall not be NULL
Found regEx error: %@
Query privilege of key: %@ from MobileGestalt
PRIVILEGE
LoggingSimulating
UnknownFile
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
Checking entry %@
Didn't successfully get data due to lacking of specific hardware
Project=%@; Caller=%@; %s=0x%llx; %s
ACTION_ENTITLEMENT
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke
%s ERR: Cannot print serial log!\n
Failed to lookup mobile storage devices
Please check the CLI option that input
Input may be missing subkey(s), or something wrong with flexible pattern definition
Failed to create IORegistryEntry iterator
Key of dictionary is redundant
atm_diagnostic_config
QueryPath_Entrusted
LSB
One graphic in graphics array does not contain \"sppci_model\"
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
Dictionary entitlement sub-entitlement %@ value mismatched: expected \"%@\", actual \"%@\"!
End: bulk query privileges
SP Exited
ENTITLEMENT
-- %@
Encode Failed
XPC Service Connect Failed
Failed to get armory shared instance for \"%@\" in privilege query!
com.apple.zhuge
Wrong key or the key is not configured
Please check regEx related code in ZhuGe
The system profiler report failed to be created
XPC Service Not Available
Get dylib shared instance for \"%@\" from cache
Added %@ to FDI paths array
Failed to get query path for \"%@\"!
QueryPath_Straight
Failed to get ZhuGe internal support path for dylib handler!
IO Service Close Failed
Please check sysdiagnose lockdown related log
Entitlement Mismatched
v8@?0
Preferences
Stack got %@ layers, not great than %@
QueryPath
getZhuGeCryptexPathsWithError
sppci_model
Didn't find the expected path
(null)
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
In bulk query, for key: \"%@\"%@, value: %@, error: %@
dFK
XPC connection is already available
May due to wrong implementation or system problem
Please make sure the way using ZhuGe is correct
String Format Wrong
Entitlement Unsupported
com.apple.FactoryCryptexSupport
So far so good, keep going
Object Length Invalid
MSB
%{public}@
softlink:r:path:/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
ZhuGeCache
ZhuGeServiceProtocol
ZhuGeSupportAssistant
ZhuGeSingleton
ZhuGeRestoreLog
ZhuGeRestoreLogProtocol
ZhuGeInternalServiceProtocol
ZhuGeInternalSupportAssistant
ZhuGe
ZhuGeLocker
```
