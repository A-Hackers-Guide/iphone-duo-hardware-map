# `/usr/lib/libAHTRestore.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 114,096 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2904)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libAHTRestore.dylib (compatibility version 1.0.0, current version 10110.1.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 0 protocols)

Classes: `AHTLoader`

## Strings (116)

```
dealloc
arrayWithObjects:count:
isEqual:
objectForKeyedSubscript:
_name
appendData:
bootloaderPropertiesForImageTag:
isEqualToString:
stringWithUTF8String:
TI,N,V_connect
initWithCapacity:
overrideNextLoadOptions:error:
errorFromAfuKextResult:error:
loadImage:payloadOnly:options:error:
sortDescriptorWithKey:ascending:comparator:
UTF8String
dataUsingEncoding:
open:
stringByAppendingString:
allDevices
bytes
length
_service
addObject:
numberWithUnsignedInt:
setService:
stringWithFormat:
unsignedIntValue
_connect
description
dictionaryWithObjects:forKeys:count:
loadingGroup
registryPropertiesForService:
withService:
service
close
init
withName:
_imageTag
TI,R,N,V_imageTag
isEqualToNumber:
overrideFDR:fdrClass:fdrSubclass:error:
stringByAppendingFormat:
initWithService:
sortUsingDescriptors:
T@\"NSString\",R,N,V_name
fullDescription
countByEnumeratingWithState:objects:count:
errorWithDomain:code:userInfo:
.cxx_destruct
_loadingGroup
errorFromKernel:error:
stringByPaddingToLength:withString:startingAtIndex:
TI,R,N,V_loadingGroup
connect
TI,N,V_service
setConnect:
code
imageTag
intValue
name
numberWithUnsignedInteger:
v16@0:8
B24@0:8^@16
B48@0:8@16@24@32^@40
v20@0:8I16
I
@16@0:8
B28@0:8i16^@20
B44@0:8@16B24Q28^@36
B32@0:8Q16^@24
I16@0:8
@\"NSString\"
@24@0:8@16
@20@0:8I16
LoadingGroup
%@ (%c%c%c%c)
\n\n%-20s | %-60s | %-20s\n
-
IgnoreFailures
Result
N/A
AHTBootloadLoadImageResult
AIDNextLoadOptions
Time (ms)
AHTBootload%sResult
%-20s | %-60s | %-20s
AHT_PRE_FDR_CHECKPOINT
AHTLoaderName
Image Tag
AHTBootload%sTimeMs
LoadImage
kFWDownloadAsync
ImageTag
\n
AHTBootloadLoadImageEnd
%@/%@
SkipUpdate
image-tag
%s | %s | %s\n
%u
!
DeviceName
Unknown FWDownloadStatus: 0x%08X
AIDFirmwareUpdateService
q24@?0@\"AHTLoader\"8@\"AHTLoader\"16
AppleHIDTransportBootloader
@\"NSString\"16@?0r*8
%@\n
kFWDownloadFailure
NeedsUpdate
Description
LoadFirmware
AppleHIDTransportSupport
LockChip
AHTLoader
```
