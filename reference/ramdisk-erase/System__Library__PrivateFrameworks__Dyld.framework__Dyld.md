# `/System/Library/PrivateFrameworks/Dyld.framework/Dyld`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 668,432 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 39 (Size: 5504)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (19)

- `/System/Library/PrivateFrameworks/Dyld.framework/Dyld (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftCompression.dylib (compatibility version 1.0.0, current version 18.0.0, weak)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftSystem.dylib (compatibility version 1.0.0, current version 5027.0.67)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (27 classes, 3 protocols)

Classes: `_DYAOTImage`, `_DYEnvironment`, `_DYEventHandlerToken`, `_DYImage`, `_DYProcess`, `_DYSegment`, `_DYSharedCache`, `_DYSnapshot`, `_DYSubCache`, `_TtC4Dyld11MachOMapper`, `_TtC4Dyld12MemoryBuffer`, `_TtC4Dyld24MemoryBufferNSDataBridge`, `_TtC4Dyld6Bitmap`, `_TtC4Dyld9MemoryMap`, `_TtCCV4Dyld7Process4Impl19ProcessUpdateRecord`, `_TtCCV4Dyld7Process4Impl21ProcessNotifierRecord`, `_TtCV4Dyld11Environment4Impl`, `_TtCV4Dyld11SharedCache4Impl`, `_TtCV4Dyld18MappedFileLRUCache5Entry`, `_TtCV4Dyld5Image4Impl`, `_TtCV4Dyld7Process4Impl`, `_TtCV4Dyld7Segment4Impl`, `_TtCV4Dyld8AOTImage4Impl`, `_TtCV4Dyld8Snapshot14DecoderContext`, `_TtCV4Dyld8Snapshot4Impl`, `_TtCV4Dyld8SubCache4Impl`, `_TtCVV4Dyld11SharedCache13ProcessRecord4Impl`

Protocols: `NSObject`, `OS_dispatch_source`, `OS_dispatch_source_mach_recv`

## Strings (413)

```
packedCPUType
respondsToSelector:
task
notifierClients
T@\"NSString\",N,R
isMemberOfClass:
unpinMappings
event
T@\"NSDictionary\",N,C
Tq,N,R
count
debugDescription
name
setQueue:
$__lazy_storage_$_sharedCache
$__lazy_storage_$_singleFile
aotImages
self
value
$__lazy_storage_$_filePaths
T@\"NSString\",R,C
initWithContentsOfMappedFile:
queue
timestamp
aotUuid
TQ,R
_queue
buffer
vmsize
zone
pid
aotImageKey
path
setImages:
setSegments:
initWithContentsOfURL:
preferredLoadAddress
$__lazy_storage_$_zerofill
TI,N,R
initWithValue:
performSelector:withObject:withObject:
stringWithUTF8String:
unsafeImageBPList
cacheInfoLoaded
isProxy
code
initWithTask:queue:error:
performSelector:withObject:
withVMLayoutBytes:
zerofillExtension
currentId
initWithLongLong:
memoryBuffer
pinnedMapMemoryBuffer
$__lazy_storage_$_sharedCachePlist
domain
registerChangeNotificationsWithError:handler:
retainCount
userInfo
TQ,N,R
Ti,N,R
UTF8String
initWithCoder:
initWithContentsOfFile:
initWithContentsOfURL:options:error:
mappedPrivate
mappings
$__lazy_storage_$_images
$__lazy_storage_$_sharedCacheSlide
.cxx_destruct
T@\"_DYEnvironment\",N,R
conformsToProtocol:
forceCacheScavenge
getCurrentSnapshotAndReturnError:
pinnedCacheMemoryMap
TB,N,R
$__lazy_storage_$_aotImages
_sharedCacheBitmap
initWithPath:error:
notifierState
rootPath
subCaches
withLocalSymbolData:
$__lazy_storage_$_env
mappers
T#,R
hash
initWithData:
initialImageCount
installname
next
deallocator
filePath
performSelector:
processForCurrentTask
segments
setMetrics:
systemSharedCachesForSystemPath:
info
initWithBase64EncodedData:options:
localSymbolPath
$__lazy_storage_$_bitmap
T@\"OS_dispatch_data\",N,R
dataWithBytesNoCopy:length:freeWhenDone:
initWithData:error:
isEqualToString:
$__lazy_storage_$_localSymbolsFilePath
currentSnapshot
$__lazy_storage_$_localSymbolsPath
_value
initWithBytesNoCopy:length:freeWhenDone:
pageSize
prev
sharedCacheAtlasBuffer
T@\"NSArray\",N,C
$__lazy_storage_$_subCaches
_sharedCachePath
sharedCache
$__lazy_storage_$_sharedCacheRecord
T@\"NSData\",N,R
T@\"NSString\",?,R,C
class
countByEnumeratingWithState:objects:count:
initWithBytes:length:
initWithBytesNoCopy:length:
initWithInternal:
T@\"_DYSharedCache\",N,&
_snapshot
filePaths
files
isKindOfClass:
objectForKeyedSubscript:
retain
state
T@\"NSArray\",N,R
address
T^v,N,R
$__lazy_storage_$_sharedCacheBitmap
T@\"_DYSharedCache\",N,R
block
environment
platform
dataForVMRangeWithAddress:size:
registerForEvent:error:handler:
T@\"OS_dispatch_queue\",N,&
active
aotAddress
autorelease
isEqual:
pinMappings
$__lazy_storage_$_sharedCacheAddress
impl
systemSharedCaches
updateClients
$__lazy_storage_$_segments
initWithBytesNoCopy:length:deallocator:
initWithContentsOfFile:options:error:
snapshotAtlasBuffer
metrics
aotSize
T@\"NSUUID\",N,R
_sharedCache
bytes
data
images
installedSharedCaches
$__lazy_storage_$_destRange
$__lazy_storage_$_memoryMap
setSharedCache:
permissions
range
setSubCaches:
snapshotPreValidated
uuid
TC,N,R
init
x86Address
$__lazy_storage_$_continuous
dealloc
release
$__lazy_storage_$_sourceRange
_sharedCacheUuid
description
getUUIDBytes:
initWithBase64EncodedString:options:
length
pinnedMappingRefCount
pointerSize
superclass
unregisterForEvent:
$__lazy_storage_$_snapshotPlist
$__lazy_storage_$_metrics
intValue
@24@0:8:16
B16@0:8
i16@0:8
@\"NSString\"16@0:8
v24@0:8@16
@36@0:8I16@20^@28
^v16@0:8
I16@0:8
B24@0:8@16
B24@0:8#16
B24@0:8:16
v8@?0
@24@0:8@16
@40@0:8^v16q24@?32
@40@0:8@16Q24^@32
@40@0:8:16@24@32
^{_NSZone=}16@0:8
B24@0:8@\"Protocol\"16
Q16@0:8
B24@0:8@?16
@32@0:8Q16Q24
@32@0:8@16^@24
@32@0:8^@16@?24
#16@0:8
@24@0:8^@16
@32@0:8@16Q24
@32@0:8^v16q24
@36@0:8^v16q24B32
v16@0:8
@16@0:8
@20@0:8I16
@36@0:8I16^@20@?28
@32@0:8:16@24
@20@0:8B16
C16@0:8
Vv16@0:8
q16@0:8
load command #%d LC_VERSION_MIN_* size wrong
load command #%d LC_BUILD_VERSION size wrong
/usr/lib/libsharedcache.dylib
Dyld/Atlas.swift
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/Library/dyld/
init(data:)
AAREncoder.cpp
0 && \"Invalid data blob size\"
bplist00
(null)
perm
dyld_process_snapshot_create_from_data
Invalid image info
Fatal error
load command #%d LC_ATOM_INFO size wrong
load command #%d LC_DYLD_INFO_ONLY size wrong
XATA
segs
Setting up notifications requires a queue
init()
/Library/Developer/CoreSimulator/Profiles/Runtimes
load command #%d LC_FUNCTION_VARIANTS size wrong
flag
Dyld/BPList.swift
/Contents/Resources/RuntimeRoot/System/Library/Caches/com.apple.dyld
load command #%d LC_FUNCTION_STARTS size wrong
AA01
uuid
/System/Library/Caches/com.apple.dyld/
/Library/Developer/CoreSimulator/Caches/dyld/
init(contentsOf:options:)
load command #%d LC_SYMTAB size wrong
ifGrowableEnsureSpaceForAppending
v20@?0@\"_DYImage\"8B16
__dsc_opt_list
foff
Unpinning shared cache mapping that was not pinned
init(contentsOfFile:)
load command #%d LC_FUNCTION_VARIANT_FIXUPS size wrong
hw.optional.arm.FEAT_MTE4
/System/Cryptexes/Incoming/OS/System/Library/dyld/
big endian mach-o file
/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/
init() not supported
init(contentsOf:)
init(coder:) has not been implemented
load command #%d unknown required load command 0x%08X
reserved1 == nil
v24@?0r^v8Q16
threadCount > 0
/private/preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
Dyld/AtlasContext.swift
dyld_shared_cache_
unknown filetype %d
v24@?0r^{load_command=II}8^B16
PATP
TYP1F
init
fsze
/private/preboot/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
dyld_sim_shared_cache_
DATB
proc
init(contentsOfFile:options:)
__TEXT
kern_return_t
time
name
v24@?0r^v8^B16
load command #%d LC_SEGMENT_SPLIT_INFO size wrong
lsl::Vector iterator invalidated: mutation during iteration
stubs
imgs
Decompressed more bytes than allocated space for block
init(base64Encoded:options:)
load command #%d LC_ENCRYPTION_INFO size wrong
load command #%d LC_SEGMENT_64 size does not match number of sections
load command #%d string offset (%u) outside its size (%u)
addr
encodeFile
Allocator.cpp
LegacyAPIShims.mm
load command #%d LC_UUID size wrong
unknown mach-o filetype (%u)
/System/Cryptexes/Rosetta/System/x86Support/System/Library/dyld/
init(bytesNoCopy:length:)
init(bytes:length:)
Unload
gots
ProcessScavenger.cpp
init(bytesNoCopy:length:deallocator:)
!sMemoryManagerInitialized
/System/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/dyld/
/System/DriverKit/System/Library/dyld/
/System/Library/dyld/
Dyld/MemoryBuffer.swift
load command #%d LC_DYLD_EXPORTS_TRIE size wrong
file does not start with MH_MAGIC[_64]: 0x%08X 0x%08X
objc_stubs
Tearing down notifications requires a queue
/System/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
load command #%d LC_DYLD_CHAINED_FIXUPS size wrong
/private/preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
/System/Cryptexes/Rosetta/System/Library/dyld
load commands length (%llu) exceeds length of file (%llu)
load command #%d string extends beyond end of load command
process.plist
Resolved memory map contains unresolved entries
/Library/Developer/CoreSimulator/Caches/dyld
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) is too large, load commands end at %p
TYP1L
plat
/System/Cryptexes/OS/System/Library/dyld/
Dyld.MemoryBufferNSDataBridge
Mappings must be fully resolved
v8@?0
stat
/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
Dyld/PublicInterface.swift
malformed load command (%d of %d) at %p with mh=%p, off end of load commands
allocStart != 0
size
com.apple.dyld.crc32c
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
load command #%d LC_ENCRYPTION_INFO_64 size wrong
load command #%d LC_SEGMENT size does not match number of sections
DATC
reserved2 == 0
CString.cpp
init(bytesNoCopy:length:freeWhenDone:)
LNKP
v32@?0Q8I16I20^B24
padr
TaskSuspender
com.apple.dyld.snapshot
/Library/Developer/CoreSimulator/Volumes/
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) too small
file
/System/Volumes/Preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
Dyld/MemoryMapper.swift
load command #%d LC_MAIN size wrong
DATA
kr == 0
v32@?0r^v8Q16Q24
cput
Dyld/IntrospectionObjC.swift
init(contentsOfMappedFile:)
Notifier (%s):\n\tPath: %s\n\tAddress: 0x%llx\n\tTimestamp: %llu\n
Load
/private/preboot/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
/System/ExclaveKit/System/Library/dyld/
load command #%d LC_DYSYMTAB size wrong
_DYAOTImage
_DYSharedCache
_TtC4Dyld12MemoryBuffer
_TtCCV4Dyld7Process4Impl21ProcessNotifierRecord
_DYSegment
_TtC4Dyld24MemoryBufferNSDataBridge
_TtCV4Dyld8AOTImage4Impl
_TtCV4Dyld11SharedCache4Impl
_TtCV4Dyld8SubCache4Impl
_TtCCV4Dyld7Process4Impl19ProcessUpdateRecord
OS_dispatch_source
_DYEnvironment
_TtC4Dyld11MachOMapper
_TtCV4Dyld7Segment4Impl
_TtCV4Dyld7Process4Impl
_DYProcess
_TtC4Dyld9MemoryMap
_TtCVV4Dyld11SharedCache13ProcessRecord4Impl
_TtCV4Dyld8Snapshot4Impl
_TtCV4Dyld18MappedFileLRUCache5Entry
OS_dispatch_source_mach_recv
_TtC4Dyld13CStringBuffer
_DYSubCache
_DYEventHandlerToken
NSObject
_TtCV4Dyld5Image4Impl
_TtCV4Dyld8Snapshot14DecoderContext
_DYSnapshot
_TtCV4Dyld11Environment4Impl
_TtC4Dyld6Bitmap
_DYImage
```
