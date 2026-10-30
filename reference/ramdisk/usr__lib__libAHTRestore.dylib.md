# `/usr/lib/libAHTRestore.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 114,096 bytes.

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
AHTBootload%sResult
LoadImage
LoadFirmware
\n
!
LockChip
AIDFirmwareUpdateService
AHTLoaderName
\n\n%-20s | %-60s | %-20s\n
Unknown FWDownloadStatus: 0x%08X
IgnoreFailures
AppleHIDTransportSupport
NeedsUpdate
image-tag
%@ (%c%c%c%c)
%@/%@
AIDNextLoadOptions
SkipUpdate
q24@?0@\"AHTLoader\"8@\"AHTLoader\"16
N/A
%u
Result
-
@\"NSString\"16@?0r*8
kFWDownloadFailure
kFWDownloadAsync
DeviceName
LoadingGroup
AppleHIDTransportBootloader
AHTBootload%sTimeMs
AHTBootloadLoadImageEnd
AHT_PRE_FDR_CHECKPOINT
Image Tag
Description
Time (ms)
%-20s | %-60s | %-20s
%@\n
AHTBootloadLoadImageResult
ImageTag
%s | %s | %s\n
AHTLoader
initWithService:
isEqual:
description
fullDescription
close
overrideNextLoadOptions:error:
TI,N,V_service
TI,N,V_connect
dealloc
errorFromAfuKextResult:error:
_loadingGroup
isEqualToString:
setConnect:
stringWithUTF8String:
T@\"NSString\",R,N,V_name
TI,R,N,V_imageTag
addObject:
open:
_imageTag
_service
dataUsingEncoding:
withName:
code
isEqualToNumber:
service
_connect
bootloaderPropertiesForImageTag:
numberWithUnsignedInt:
stringByPaddingToLength:withString:startingAtIndex:
.cxx_destruct
bytes
countByEnumeratingWithState:objects:count:
imageTag
length
connect
TI,R,N,V_loadingGroup
initWithCapacity:
overrideFDR:fdrClass:fdrSubclass:error:
unsignedIntValue
name
stringByAppendingFormat:
allDevices
arrayWithObjects:count:
objectForKeyedSubscript:
sortDescriptorWithKey:ascending:comparator:
UTF8String
errorFromKernel:error:
numberWithUnsignedInteger:
sortUsingDescriptors:
stringByAppendingString:
stringWithFormat:
withService:
_name
dictionaryWithObjects:forKeys:count:
init
intValue
loadingGroup
registryPropertiesForService:
appendData:
errorWithDomain:code:userInfo:
loadImage:payloadOnly:options:error:
setService:
@\"NSString\"
@20@0:8I16
B24@0:8^@16
B44@0:8@16B24Q28^@36
v20@0:8I16
I
@16@0:8
@24@0:8@16
B28@0:8i16^@20
v16@0:8
B48@0:8@16@24@32^@40
B32@0:8Q16^@24
I16@0:8
```
