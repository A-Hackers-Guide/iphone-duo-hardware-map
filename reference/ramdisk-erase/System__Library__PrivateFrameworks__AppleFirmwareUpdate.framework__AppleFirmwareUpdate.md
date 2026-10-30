# `/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 269,312 bytes.

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
IODeviceTree
FDR Classes
v8@?0
Matching Servive error
Service open error
FW Asset file error
aud-early-boot-critical
%s: Critical earlyBoot entry: imageTag %u
%s: %s\n
SORRY... NO LONGER SUPPORTED\n
com.apple.accessoryfirmwareupdate
Registry entry not found
FW Asset version error
%s: %u
Mmap error
com.apple.appleFirmwareUpdate.delegateQueue
DeviceClassName
IOPropertyMatch
-[AppleFirmwareUpdateController createFWAssetInfoInternal]
LoadFDR error
i
Image Tag
%s: Failed to registered for tag %@
-[AppleFirmwareUpdateController registerForPendingEarlyBootAccessoriesInternal]
%s: Registered for tag %@
1
IOMatching error
-[AppleFirmwareUpdateController getEarlyBootListInternal:]
-[AppleFirmwareUpdateController readCriticalEarlyBootEntries]
%s
Download Not Needed
AppleFirmwareUpdateKext
%s: Pending critical earlyBoot entries %@
LoadingGroup
default
LoadFE error
com.apple.mau.plugin.generickext
FW Asset signature error
IOMatchLaunchServiceID
skip-image-loading
-[AppleFirmwareUpdateController getEarlyBootList:]_block_invoke
q24@?0@8@16
-[AppleFirmwareUpdateController earlyBootAccessoryAttachedInternal:]
IMG4
NONE
FW Asset file size error
OptionsDict
-[AppleFirmwareUpdateController updateFirmwareWithOptionsInternal:]
No Error
FUD
-[AppleFirmwareUpdateController extractFDRDataWithClassKey:error:]
com.apple.mobileaccessoryupdater
FW Asset file open error
Allocation errror
Unknown Error
IOServiceMatched
image-tag
Need FUD Download
CopyAllowUnsealed
com.apple.appleFirmwareUpdate.workQueue
%@/%@
com.apple.AppleFirmwareUpdate
/
Bootstrap Error:%@ code=0x%0lx registryEntryID=%@
Failed to read %{public}@ with error %{public}@ 
IMG4 decode init failed - %@
%s: key (%@) is not valid.
%s: localDict is NULL for key (%@).
%s: Ealyboot List: %@
%s: Error:%@ code=0x%0lx
Firmware directory path: %@
FDR class from registry entry='%@'
FW asset for tag=0x%0x not found
%s:\n registryID=%@\n fwTag=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@\n options=%@ error=%@
download needed property not in registry entry
Failed to read file %{public}@ with error %{public}@
%s
Zero tag value in registry entry
Failed decoding check for %{public}@
IMG4 get tag failed - %@
LoadFDR class='%@' with %u bytes ret=%d
%s: registry entry not found for service=%d
personalizedDataPath: %@
Found FW file for tag=0x%0x - %@ [size=%zu]
No asset files found
Cannot find FDR data for class '%@': %@
LoadFDRDataComplete ret=%d
Invalid FDR class in registry entry
%s:\n registryID=%@\n fwTag=%@ fwDirectory=%@ fwFile=%@\n fwSignType=%@\n fwVersion=%@\n fwSize=%@
AppleFirmwareUpdateController
setFwAssetFile:
_fwAssetDirectory
_fwAssetSignatureType
_iokitNotifyPort
shouldSkipImage4Download
dealloc
copy
isEqualToString:
numberWithUnsignedLongLong:
unsignedLongLongValue
T@\"NSArray\",&,N,V_fdrClasses
T@\"NSNumber\",&,N,V_fwAssetVersion
appendFormat:
count
setDelegate:
unsignedIntegerValue
appendData:
countByEnumeratingWithState:objects:count:
createFWAssetInfoInternal
dataWithContentsOfFile:options:error:
defaultManager
removeAllObjects
sendFDRData:
setObject:forKey:
_pendingCriticalEarlyBootEntriesInternal
enableEarlyBootLoggingMode
fwAssetSignatureType
removeObject:
setFdrClasses:
setObject:forKeyedSubscript:
sortEarlyBootListWithLoadingGroup:
updateFirmwareWithOptions:
T@\"NSNumber\",&,N,V_img4Tag
_delegate
_fdrClasses
_fwAssetSize
compare:
extractFDRDataWithClassKey:error:
findFWAssetFromTag:tag:size:
fwAssetFile
initWithCapacity:
setImg4Tag:
T@\"NSString\",&,N,V_fwAssetSignatureType
componentsSeparatedByString:
copyPathForPersonalizedData:error:
setFwAssetVersion:
earlyBootAccessoryAttachedInternal:
UTF8String
_delegateQueue
bytes
contentsOfDirectoryAtPath:error:
dataUsingEncoding:
numberWithLongLong:
registerForPendingEarlyBootAccessoriesInternal
createFWAssetInfo
earlyBootAccessoryAttached:
containsString:
setFwAssetSize:
_log
_registryEntryID
addObject:
cStringUsingEncoding:
dictionary
_fwAssetVersion
arrayWithArray:
_fwAssetFile
closeFile
fwAssetVersion
getEarlyBootList:
length
dictionaryWithObjects:forKeys:count:
fileHandleForReadingAtPath:
getServiceForRegistryID:
initWithRegistryEntryID:fwAssetDirectory:
registerForPendingEarlyBootAccessories
setFwAssetSignatureType:
updateFirmwareWithOptionsInternal:
T@\"NSString\",&,N,V_fwAssetFile
getEarlyBootListInternal:
readCriticalEarlyBootEntries
sortUsingComparator:
stringWithFormat:
stringByAppendingPathComponent:
_workQueue
getBytes:length:
objectAtIndexedSubscript:
sharedDataAccessor
stringWithCapacity:
T@\"NSNumber\",&,N,V_fwAssetSize
boolValue
fdrClasses
fwAssetSize
getConnectionForRegistryID:
isFWDownloadNeeded:
readDataUpToLength:error:
unsignedIntValue
_img4Tag
errorWithDomain:code:userInfo:
getPendingEarlyBootAccessories
init
initWithFormat:arguments:
numberWithUnsignedInt:
objectForKeyedSubscript:
dictionaryWithCapacity:
img4Tag
.cxx_destruct
v20@0:8I16
@16@0:8
I24@0:8^q16
@36@0:8@16I24^Q28
@32@0:8@16^@24
@\"NSObject<OS_os_log>\"
@\"NSNumber\"
@32@0:8@16@24
v16@0:8
@24@0:8@16
q20@0:8I16
@\"NSMutableArray\"
@\"<AppleFirmwareUpdateControllerDelegate>\"
@\"NSArray\"
v24@0:8@16
B16@0:8
@\"NSObject<OS_dispatch_queue>\"
@\"NSString\"
B24@0:8@16
^{IONotificationPort=}
```
