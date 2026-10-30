# `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`

From the upgrade restore ramdisk (141-29011-104.dmg). 140,000 bytes.

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
+[MSUDataAccessor bootUUIDWithError:]
/
Path symbol resolution failure
Bad type in response to crypto hash method query
kInvalidInput
IODeviceTree:/chosen
boardid
iscpreboot
/usr/local/standalone/firmware/Baseband
MSUDataAccessor
Failed to boot manifest hash
symbol
/FactoryData/System/Library/Caches/com.apple.factorydata
/history_sec
Failed to locate hardware volume
[preboot]/downlevel/current
chipid
BootManifestHash
/Pearl/System/Library/Pearl/ReferenceFrames
/history
Unable to find path for requested personalized data
[iscpreboot]
[preboot]/cryptex1/current/
/private/var/Keychains/apticket.der
/LocalPolicy.cryptex1.img4
/genx_history
[hardware]
v32@?0@\"NSTextCheckingResult\"8Q16^B24
Too many volumes
bootobjectspath
TF31PAB6aO8KAbPyNKSxKA
[
Unknown volume type
Found apticket at %@ but it does not match the boot manifest hash
v8@?0
lp-nsih
v40@?0r^v8{_NSRange=QQ}16^B32
boot-uuid
hwmodel
ECID
sha2-384
/lac
kMSUDAErrorNone
[preboot]/cryptex1/current/rollback
volguuid
%X
could not alloc/init regex
/FactoryData/System/Library/Caches/apticket.der
[preboot]/cryptex1/current/SystemVersion.plist
[cryptex1ticketpath]
cryptex1ticketpath
/usr/standalone/firmware/sep-patches.img4
apticket.%@.im4m
]
/bic_sec
kMSUDAErrorAllocFailure
[sourcepreboot]
%02X
nsih
hardware
[preboot]/cryptex1/current/RestoreVersion.plist
apticket.%@.%@.im4m
Failed to allocate path
Volume not mounted
sha1
boot-manifest-hash
/dramecc
MSUDAError
[%@=%ld] %@
566JrJVMlDfnslGpwUzNlQ
BootManifestHash is not CFData
/srvo
Unknown Error Code
Failed to read boot-uuid in order to locate personalized data root
%llX
cryptex1
/usr/standalone/firmware
com.apple.MSUDataAccessor
x86legacyap
bad regex
0uthiXrHZ212KvcJizKHEw
boot-objects-path
current
/Battery
InDiagnosticsMode
Failed to fetch manifest hash
sourcepreboot
regex
/private/var/hardware
[preboot]/cryptex1/current/os.dmg
[preboot]/cryptex1/current/BuildManifest.plist
preboot
IODeviceTree:/chosen/manifest-properties
\\
[iscpreboot]/SFR/current/apticket.der
Unsupported crypto hash method %@
/System/Library/Caches/apticket.der
/mnt1
Failed to locate preboot volume
IODeviceTree:/chosen/asmb
Failed to get %@ node
Bad type in response to boot manifest hash query
/usr/standalone/firmware/sep-firmware.img4
/private/var/MobileSoftwareUpdate/Hardware/Battery
[%@=%ld]
MSUDASymbolicPathResolverError
(\\\\\\\\)|(\\\\\\[)|(\\\\\\])|(\\[\\w+\\])
/private/var/hardware/FactoryData/System/Library/Caches/Repair
Image4CryptoHashMethod
/AppleInternal/Diags/bin/diag.img4
/bic
Unable to find path for requested persistent data
/private/preboot
hw.target
ecid
Missing volume
could not alloc/init regex:%@
returning resolved path for symbolic path %@: %@
Failed to locate mount point for preboot volume\n
Path is : %@
Failed to find personalized data path for dataType=%d
Failed to find persistent data path for dataType=%d
%@
%s: Failed to read boot-uuid in order to locate personalized data root..bailing\n
Unknown symbol:%@
error %@ ; discarding incomplete unresolved path: %@
Preboot volume is mounted at %@\n
Failed to locate bootManifestHash\n
bad regex:%@
MSUDataAccessor
MSUDataAccessorDiagnostics
MSUDataAccessorSymbolicPathResolver
MSUDataAccessorRestore
appendFormat:
dataWithBytesNoCopy:length:freeWhenDone:
dataWithContentsOfFile:options:error:
enumerateByteRangesUsingBlock:
objectForKeyedSubscript:
specialCaseFDRPathForDiagnostics
UTF8String
appendString:
copyPathForPersistentData:error:
hardwareRootWithError:
sharedDataAccessor
stringWithUTF8String:
buildErrorForRef:code:description:
fileExistsAtPath:isDirectory:
getBytes:length:
init
mountPoint
rangeAtIndex:
symbolicPathResolver
objectAtIndex:
range
resolvedSymbol:error:
stringByAppendingString:
returnDirectoryIfExistsForPath:
copyBootManifestHashWithError:
copyPathForPersonalizedData:error:
getCString:maxLength:encoding:
isEqualToData:
longLongValue
bytes
mutableCopy
resolveFilePathForEntry:error:
specialCaseAPTicketForRamdiskWithError:
dealloc
errorWithDomain:code:userInfo:
fileExistsAtPath:
ioreg:property:error:
overrideSymbol:resolvedPath:
string
allMedia
code
cryptex1TicketType
intValue
isEqualToString:
copyMountPointForVolumeType:error:
dictionaryWithObjects:forKeys:count:
findVolumesWithRole:
removeObjectForKey:
resolve:error:
initWithFormat:
orderedSetWithCapacity:
stringWithCapacity:
stringWithFormat:
stringByAppendingPathComponent:
bootUUIDWithError:
errorNameForCode:
addObject:
count
hardwareModelWithError:
length
substringWithRange:
copy
copyPersistentDataPathsWithError:
getVolumeWithUUID:
regularExpressionWithPattern:options:error:
lowercaseString
_overrides
enumerateMatchesInString:options:range:usingBlock:
mediaUUID
pathWithComponents:
.cxx_destruct
array
countByEnumeratingWithState:objects:count:
personalizedRootWithError:
setObject:forKeyedSubscript:
arrayWithObjects:count:
defaultManager
role
@24@0:8@16
@32@0:8@16^@24
v16@0:8
@16@0:8
Q16@0:8
@28@0:8i16^@20
v32@0:8@16@24
@\"NSMutableDictionary\"
@20@0:8i16
v40@0:8^@16q24@32
@24@0:8q16
@40@0:8@16@24^@32
@24@0:8^@16
@32@0:8r^{path_table_entry=(?=ii)B@@}16^@24
```
