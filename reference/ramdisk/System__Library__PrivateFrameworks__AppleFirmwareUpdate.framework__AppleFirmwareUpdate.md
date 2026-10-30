# `/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate`

From the upgrade restore ramdisk (141-29011-104.dmg). 269,312 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3512)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 0 protocols)

Classes: `AppleFirmwareUpdateController`

## Strings (216)

```
IOPropertyMatch
FW Asset file error
Allocation errror
com.apple.appleFirmwareUpdate.delegateQueue
OptionsDict
-[AppleFirmwareUpdateController updateFirmwareWithOptionsInternal:]
skip-image-loading
LoadFDR error
-[AppleFirmwareUpdateController getEarlyBootListInternal:]
-[AppleFirmwareUpdateController earlyBootAccessoryAttachedInternal:]
IMG4
FW Asset file open error
Registry entry not found
Download Not Needed
i
%s: Failed to registered for tag %@
FW Asset file size error
%s: Pending critical earlyBoot entries %@
%s: Registered for tag %@
%@/%@
-[AppleFirmwareUpdateController createFWAssetInfoInternal]
com.apple.AppleFirmwareUpdate
com.apple.appleFirmwareUpdate.workQueue
q24@?0@8@16
LoadingGroup
Service open error
Mmap error
IOMatching error
NONE
AppleFirmwareUpdateKext
v8@?0
default
FW Asset version error
LoadFE error
IOServiceMatched
CopyAllowUnsealed
%s
%s: %s\n
Matching Servive error
aud-early-boot-critical
No Error
-[AppleFirmwareUpdateController getEarlyBootList:]_block_invoke
DeviceClassName
-[AppleFirmwareUpdateController registerForPendingEarlyBootAccessoriesInternal]
-[AppleFirmwareUpdateController readCriticalEarlyBootEntries]
/
com.apple.mau.plugin.generickext
IOMatchLaunchServiceID
%s: %u
SORRY... NO LONGER SUPPORTED\n
IODeviceTree
FDR Classes
FW Asset signature error
%s: Critical earlyBoot entry: imageTag %u
Need FUD Download
Unknown Error
image-tag
FUD
1
com.apple.mobileaccessoryupdater
-[AppleFirmwareUpdateController extractFDRDataWithClassKey:error:]
com.apple.accessoryfirmwareupdate
Image Tag
LoadFDRDataComplete ret=%d
%s: key (%@) is not valid.
%s: localDict is NULL for key (%@).
%s:\n registryID=%@\n fwTag=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@\n options=%@ error=%@
%s: Ealyboot List: %@
personalizedDataPath: %@
Firmware directory path: %@
%s:\n registryID=%@\n fwTag=%@ fwDirectory=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@
Bootstrap Error:%@ code=0x%0lx registryEntryID=%@
download needed property not in registry entry
No asset files found
%s: registry entry not found for service=%d
Invalid FDR class in registry entry
FDR class from registry entry='%@'
Zero tag value in registry entry
FW asset for tag=0x%0x not found
Failed decoding check for %{public}@
Failed to read file %{public}@ with error %{public}@
IMG4 decode init failed - %@
%s
%s: Error:%@ code=0x%0lx
Found FW file for tag=0x%0x - %@ [size=%zu]
Failed to read %{public}@ with error %{public}@ 
Cannot find FDR data for class '%@': %@
IMG4 get tag failed - %@
LoadFDR class='%@' with %u bytes ret=%d
AppleFirmwareUpdateController
countByEnumeratingWithState:objects:count:
setFdrClasses:
setFwAssetSignatureType:
setImg4Tag:
shouldSkipImage4Download
T@\"NSString\",&,N,V_fwAssetSignatureType
_fwAssetSize
dataWithContentsOfFile:options:error:
dictionaryWithCapacity:
getServiceForRegistryID:
isEqualToString:
stringWithFormat:
updateFirmwareWithOptionsInternal:
containsString:
T@\"NSString\",&,N,V_fwAssetFile
.cxx_destruct
boolValue
numberWithLongLong:
updateFirmwareWithOptions:
T@\"NSNumber\",&,N,V_img4Tag
_fdrClasses
fwAssetFile
initWithFormat:arguments:
_fwAssetFile
initWithRegistryEntryID:fwAssetDirectory:
setObject:forKeyedSubscript:
sortEarlyBootListWithLoadingGroup:
_fwAssetVersion
img4Tag
_iokitNotifyPort
appendFormat:
cStringUsingEncoding:
copyPathForPersonalizedData:error:
dictionary
numberWithUnsignedLongLong:
T@\"NSNumber\",&,N,V_fwAssetVersion
_delegate
earlyBootAccessoryAttachedInternal:
extractFDRDataWithClassKey:error:
fwAssetVersion
getPendingEarlyBootAccessories
initWithCapacity:
readCriticalEarlyBootEntries
_fwAssetDirectory
componentsSeparatedByString:
earlyBootAccessoryAttached:
unsignedLongLongValue
_workQueue
appendData:
bytes
closeFile
fileHandleForReadingAtPath:
fwAssetSignatureType
getBytes:length:
objectAtIndexedSubscript:
UTF8String
dealloc
copy
count
fwAssetSize
sendFDRData:
setDelegate:
sharedDataAccessor
arrayWithArray:
stringByAppendingPathComponent:
createFWAssetInfoInternal
dictionaryWithObjects:forKeys:count:
fdrClasses
getEarlyBootList:
isFWDownloadNeeded:
length
createFWAssetInfo
findFWAssetFromTag:tag:size:
getEarlyBootListInternal:
init
registerForPendingEarlyBootAccessoriesInternal
removeAllObjects
removeObject:
sortUsingComparator:
T@\"NSNumber\",&,N,V_fwAssetSize
_delegateQueue
_pendingCriticalEarlyBootEntriesInternal
compare:
defaultManager
getConnectionForRegistryID:
objectForKeyedSubscript:
stringWithCapacity:
_log
contentsOfDirectoryAtPath:error:
setFwAssetSize:
_fwAssetSignatureType
_registryEntryID
dataUsingEncoding:
enableEarlyBootLoggingMode
errorWithDomain:code:userInfo:
numberWithUnsignedInt:
readDataUpToLength:error:
setFwAssetFile:
addObject:
registerForPendingEarlyBootAccessories
setFwAssetVersion:
setObject:forKey:
unsignedIntValue
unsignedIntegerValue
T@\"NSArray\",&,N,V_fdrClasses
_img4Tag
v24@0:8@16
B24@0:8@16
v20@0:8I16
@24@0:8@16
@36@0:8@16I24^Q28
q20@0:8I16
@32@0:8@16^@24
@\"NSMutableArray\"
@32@0:8@16@24
B16@0:8
@16@0:8
I24@0:8^q16
@\"NSObject<OS_dispatch_queue>\"
@\"NSString\"
@\"NSArray\"
@\"NSObject<OS_os_log>\"
v16@0:8
@\"NSNumber\"
^{IONotificationPort=}
@\"<AppleFirmwareUpdateControllerDelegate>\"
```
