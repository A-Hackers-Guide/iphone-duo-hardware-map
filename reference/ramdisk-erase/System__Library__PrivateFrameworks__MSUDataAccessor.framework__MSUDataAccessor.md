# `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 140,000 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 3392)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libpartition2_dynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 0 protocols)

Classes: `MSUDataAccessor`, `MSUDataAccessorDiagnostics`, `MSUDataAccessorRestore`, `MSUDataAccessorSymbolicPathResolver`

## Strings (225)

```
[preboot]/cryptex1/current/os.dmg
%X
v32@?0@\"NSTextCheckingResult\"8Q16^B24
BootManifestHash
MSUDAError
Missing volume
bad regex
\\
lp-nsih
/mnt1
/usr/local/standalone/firmware/Baseband
[cryptex1ticketpath]
/srvo
Image4CryptoHashMethod
/Pearl/System/Library/Pearl/ReferenceFrames
v8@?0
Unknown Error Code
iscpreboot
%llX
TF31PAB6aO8KAbPyNKSxKA
566JrJVMlDfnslGpwUzNlQ
/LocalPolicy.cryptex1.img4
[preboot]/cryptex1/current/rollback
Failed to get %@ node
hardware
/System/Library/Caches/apticket.der
/private/preboot
Failed to boot manifest hash
boot-uuid
Path symbol resolution failure
[
[%@=%ld] %@
[preboot]/cryptex1/current/
volguuid
symbol
Unsupported crypto hash method %@
kMSUDAErrorAllocFailure
MSUDataAccessor
kMSUDAErrorNone
v40@?0r^v8{_NSRange=QQ}16^B32
MSUDASymbolicPathResolverError
0uthiXrHZ212KvcJizKHEw
Unknown volume type
preboot
IODeviceTree:/chosen/manifest-properties
sha1
/usr/standalone/firmware/sep-patches.img4
/bic_sec
[preboot]/cryptex1/current/RestoreVersion.plist
%02X
Bad type in response to boot manifest hash query
/usr/standalone/firmware/sep-firmware.img4
/history
Bad type in response to crypto hash method query
/Battery
/lac
IODeviceTree:/chosen
apticket.%@.im4m
/history_sec
(\\\\\\\\)|(\\\\\\[)|(\\\\\\])|(\\[\\w+\\])
apticket.%@.%@.im4m
com.apple.MSUDataAccessor
BootManifestHash is not CFData
regex
]
[preboot]/cryptex1/current/BuildManifest.plist
hw.target
bootobjectspath
Unable to find path for requested persistent data
[%@=%ld]
[preboot]/cryptex1/current/SystemVersion.plist
/dramecc
kInvalidInput
IODeviceTree:/chosen/asmb
x86legacyap
boardid
[preboot]/downlevel/current
/
Failed to allocate path
hwmodel
/usr/standalone/firmware
/bic
/private/var/MobileSoftwareUpdate/Hardware/Battery
Failed to fetch manifest hash
Failed to locate hardware volume
[sourcepreboot]
current
sha2-384
/genx_history
Failed to locate preboot volume
boot-manifest-hash
/private/var/hardware/FactoryData/System/Library/Caches/Repair
sourcepreboot
/FactoryData/System/Library/Caches/com.apple.factorydata
cryptex1ticketpath
Too many volumes
Volume not mounted
/private/var/Keychains/apticket.der
InDiagnosticsMode
[hardware]
ecid
[iscpreboot]
/private/var/hardware
chipid
ECID
boot-objects-path
Unable to find path for requested personalized data
+[MSUDataAccessor bootUUIDWithError:]
nsih
cryptex1
could not alloc/init regex
Found apticket at %@ but it does not match the boot manifest hash
[iscpreboot]/SFR/current/apticket.der
/AppleInternal/Diags/bin/diag.img4
/FactoryData/System/Library/Caches/apticket.der
Failed to read boot-uuid in order to locate personalized data root
Unknown symbol:%@
bad regex:%@
returning resolved path for symbolic path %@: %@
Failed to locate mount point for preboot volume\n
Preboot volume is mounted at %@\n
Path is : %@
Failed to find personalized data path for dataType=%d
Failed to find persistent data path for dataType=%d
error %@ ; discarding incomplete unresolved path: %@
could not alloc/init regex:%@
Failed to locate bootManifestHash\n
%@
%s: Failed to read boot-uuid in order to locate personalized data root..bailing\n
MSUDataAccessorSymbolicPathResolver
MSUDataAccessorRestore
MSUDataAccessor
MSUDataAccessorDiagnostics
bootUUIDWithError:
dataWithBytesNoCopy:length:freeWhenDone:
mutableCopy
rangeAtIndex:
stringWithCapacity:
stringWithFormat:
dealloc
enumerateByteRangesUsingBlock:
length
role
symbolicPathResolver
stringByAppendingPathComponent:
.cxx_destruct
countByEnumeratingWithState:objects:count:
stringByAppendingString:
_overrides
buildErrorForRef:code:description:
copyBootManifestHashWithError:
errorNameForCode:
personalizedRootWithError:
resolve:error:
copy
copyMountPointForVolumeType:error:
fileExistsAtPath:isDirectory:
getVolumeWithUUID:
isEqualToData:
sharedDataAccessor
specialCaseFDRPathForDiagnostics
initWithFormat:
resolveFilePathForEntry:error:
lowercaseString
addObject:
bytes
dictionaryWithObjects:forKeys:count:
string
UTF8String
copyPathForPersonalizedData:error:
ioreg:property:error:
mountPoint
returnDirectoryIfExistsForPath:
dataWithContentsOfFile:options:error:
findVolumesWithRole:
longLongValue
overrideSymbol:resolvedPath:
range
setObject:forKeyedSubscript:
count
getBytes:length:
objectAtIndex:
pathWithComponents:
defaultManager
enumerateMatchesInString:options:range:usingBlock:
objectForKeyedSubscript:
removeObjectForKey:
appendFormat:
hardwareRootWithError:
mediaUUID
stringWithUTF8String:
getCString:maxLength:encoding:
intValue
isEqualToString:
allMedia
array
arrayWithObjects:count:
copyPathForPersistentData:error:
copyPersistentDataPathsWithError:
appendString:
hardwareModelWithError:
init
cryptex1TicketType
errorWithDomain:code:userInfo:
fileExistsAtPath:
regularExpressionWithPattern:options:error:
resolvedSymbol:error:
code
orderedSetWithCapacity:
specialCaseAPTicketForRamdiskWithError:
substringWithRange:
@20@0:8i16
@16@0:8
v40@0:8^@16q24@32
@24@0:8q16
@40@0:8@16@24^@32
@24@0:8^@16
@32@0:8r^{path_table_entry=(?=ii)B@@}16^@24
@28@0:8i16^@20
@24@0:8@16
Q16@0:8
@32@0:8@16^@24
v16@0:8
v32@0:8@16@24
@\"NSMutableDictionary\"
```
