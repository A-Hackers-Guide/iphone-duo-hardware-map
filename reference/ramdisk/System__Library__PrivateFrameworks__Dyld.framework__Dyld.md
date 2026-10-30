# `/System/Library/PrivateFrameworks/Dyld.framework/Dyld`

From the upgrade restore ramdisk (141-29011-104.dmg). 668,432 bytes.

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
Dyld/IntrospectionObjC.swift
init(bytesNoCopy:length:)
reserved1 == nil
/System/DriverKit/System/Library/dyld/
init(contentsOf:)
load command #%d LC_FUNCTION_STARTS size wrong
load command #%d LC_DYLD_INFO_ONLY size wrong
load command #%d LC_SEGMENT_64 size does not match number of sections
CString.cpp
init() not supported
AAREncoder.cpp
file
dyld_sim_shared_cache_
kr == 0
init(contentsOfMappedFile:)
load command #%d LC_UUID size wrong
DATA
ifGrowableEnsureSpaceForAppending
v24@?0r^v8Q16
Unload
padr
Dyld/AtlasContext.swift
Fatal error
init(contentsOfFile:options:)
init(coder:) has not been implemented
load command #%d LC_ENCRYPTION_INFO_64 size wrong
unknown filetype %d
v24@?0r^{load_command=II}8^B16
encodeFile
com.apple.dyld.crc32c
/System/Library/Caches/com.apple.dyld/
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) is too large, load commands end at %p
dyld_process_snapshot_create_from_data
reserved2 == 0
v32@?0r^v8Q16Q24
Load
/private/preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
Dyld.MemoryBufferNSDataBridge
load command #%d LC_FUNCTION_VARIANT_FIXUPS size wrong
DATC
/System/Cryptexes/Rosetta/System/x86Support/System/Library/dyld/
Resolved memory map contains unresolved entries
load command #%d LC_MAIN size wrong
unknown mach-o filetype (%u)
v32@?0Q8I16I20^B24
imgs
proc
TaskSuspender
/System/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/dyld/
init(bytesNoCopy:length:freeWhenDone:)
malformed load command (%d of %d) at %p with mh=%p, size (0x%X) too small
XATA
TYP1L
v24@?0r^v8^B16
Dyld/PublicInterface.swift
file does not start with MH_MAGIC[_64]: 0x%08X 0x%08X
TYP1F
v8@?0
stubs
process.plist
/System/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
/System/Library/dyld/
load command #%d LC_DYSYMTAB size wrong
name
com.apple.dyld.snapshot
init(bytesNoCopy:length:deallocator:)
Mappings must be fully resolved
load command #%d LC_SEGMENT size does not match number of sections
Dyld/MemoryBuffer.swift
init(bytes:length:)
/Library/Developer/CoreSimulator/Profiles/Runtimes
dyld_shared_cache_
load commands length (%llu) exceeds length of file (%llu)
/usr/lib/libsharedcache.dylib
segs
/private/preboot/Cryptexes/Incoming/OS/System/Library/Caches/com.apple.dyld/
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/Library/dyld/
Unpinning shared cache mapping that was not pinned
DATB
time
cput
ProcessScavenger.cpp
Invalid image info
/System/Cryptexes/Incoming/OS/System/Library/dyld/
lsl::Vector iterator invalidated: mutation during iteration
kern_return_t
/private/preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
/System/ExclaveKit/System/Library/dyld/
/System/Volumes/Preboot/Cryptexes/Incoming/OS/System/DriverKit/System/Library/dyld/
init(contentsOfFile:)
AA01
plat
size
/Contents/Resources/RuntimeRoot/System/Library/Caches/com.apple.dyld
load command #%d LC_DYLD_CHAINED_FIXUPS size wrong
malformed load command (%d of %d) at %p with mh=%p, off end of load commands
flag
Dyld/MemoryMapper.swift
init(data:)
load command #%d LC_BUILD_VERSION size wrong
load command #%d LC_FUNCTION_VARIANTS size wrong
Allocator.cpp
bplist00
Tearing down notifications requires a queue
Dyld/BPList.swift
/Library/Developer/CoreSimulator/Caches/dyld/
load command #%d LC_ATOM_INFO size wrong
hw.optional.arm.FEAT_MTE4
/Library/Developer/CoreSimulator/Volumes/
v20@?0@\"_DYImage\"8B16
Notifier (%s):\n\tPath: %s\n\tAddress: 0x%llx\n\tTimestamp: %llu\n
(null)
uuid
foff
/System/Volumes/Preboot/Cryptexes/OS/System/DriverKit/System/Library/dyld/
LNKP
objc_stubs
/private/preboot/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
Dyld/Atlas.swift
/System/Cryptexes/OS/System/Library/dyld/
init(contentsOf:options:)
load command #%d string offset (%u) outside its size (%u)
0 && \"Invalid data blob size\"
!sMemoryManagerInitialized
/Library/Developer/CoreSimulator/Caches/dyld
load command #%d LC_ENCRYPTION_INFO size wrong
big endian mach-o file
/System/Cryptexes/Rosetta/System/Library/dyld
Decompressed more bytes than allocated space for block
/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/
load command #%d LC_DYLD_EXPORTS_TRIE size wrong
load command #%d LC_VERSION_MIN_* size wrong
__dsc_opt_list
init
init(base64Encoded:options:)
load command #%d unknown required load command 0x%08X
load command #%d LC_SEGMENT_SPLIT_INFO size wrong
PATP
perm
load command #%d LC_SYMTAB size wrong
gots
Setting up notifications requires a queue
allocStart != 0
LegacyAPIShims.mm
__TEXT
addr
threadCount > 0
/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/
init()
load command #%d string extends beyond end of load command
stat
fsze
_TtC4Dyld11MachOMapper
_TtCV4Dyld11Environment4Impl
_TtCV4Dyld11SharedCache4Impl
_TtCV4Dyld8SubCache4Impl
_TtCCV4Dyld7Process4Impl19ProcessUpdateRecord
_DYEnvironment
_TtCV4Dyld7Segment4Impl
_TtC4Dyld13CStringBuffer
_TtC4Dyld24MemoryBufferNSDataBridge
_TtC4Dyld9MemoryMap
_TtC4Dyld6Bitmap
_DYSegment
_DYSharedCache
_DYEventHandlerToken
OS_dispatch_source_mach_recv
_TtCV4Dyld5Image4Impl
_TtCVV4Dyld11SharedCache13ProcessRecord4Impl
OS_dispatch_source
_DYAOTImage
_DYSnapshot
_DYProcess
NSObject
_TtCV4Dyld8AOTImage4Impl
_TtCV4Dyld8Snapshot14DecoderContext
_TtCV4Dyld18MappedFileLRUCache5Entry
_TtCCV4Dyld7Process4Impl21ProcessNotifierRecord
_DYSubCache
_TtCV4Dyld8Snapshot4Impl
_TtCV4Dyld7Process4Impl
_DYImage
_TtC4Dyld12MemoryBuffer
TC,N,R
pageSize
respondsToSelector:
mappers
T@\"_DYSharedCache\",N,&
Ti,N,R
_queue
_sharedCachePath
installedSharedCaches
memoryBuffer
objectForKeyedSubscript:
T@\"NSUUID\",N,R
_sharedCacheBitmap
mappedPrivate
mappings
queue
segments
setSegments:
$__lazy_storage_$_snapshotPlist
pid
active
class
initWithContentsOfFile:options:error:
initWithContentsOfURL:options:error:
initWithLongLong:
setMetrics:
T^v,N,R
aotSize
isEqual:
permissions
timestamp
$__lazy_storage_$_subCaches
TB,N,R
aotAddress
data
getUUIDBytes:
initWithContentsOfMappedFile:
name
preferredLoadAddress
T@\"OS_dispatch_data\",N,R
TQ,N,R
buffer
event
initWithContentsOfURL:
pinnedCacheMemoryMap
superclass
$__lazy_storage_$_sharedCachePlist
_snapshot
initWithData:
isKindOfClass:
processForCurrentTask
registerChangeNotificationsWithError:handler:
$__lazy_storage_$_sharedCacheAddress
files
initWithContentsOfFile:
$__lazy_storage_$_segments
dataForVMRangeWithAddress:size:
_value
aotImageKey
deallocator
initialImageCount
pinMappings
retainCount
$__lazy_storage_$_destRange
metrics
release
T@\"NSArray\",N,C
$__lazy_storage_$_sharedCache
initWithValue:
intValue
pinnedMappingRefCount
autorelease
initWithBytesNoCopy:length:
pointerSize
setSubCaches:
snapshotAtlasBuffer
unsafeImageBPList
updateClients
uuid
$__lazy_storage_$_bitmap
localSymbolPath
domain
currentSnapshot
$__lazy_storage_$_continuous
conformsToProtocol:
vmsize
x86Address
$__lazy_storage_$_aotImages
$__lazy_storage_$_env
$__lazy_storage_$_sharedCacheBitmap
T@\"_DYEnvironment\",N,R
packedCPUType
unpinMappings
userInfo
debugDescription
path
setImages:
bytes
length
pinnedMapMemoryBuffer
prev
range
$__lazy_storage_$_filePaths
currentId
initWithBytesNoCopy:length:deallocator:
initWithPath:error:
systemSharedCachesForSystemPath:
$__lazy_storage_$_localSymbolsPath
.cxx_destruct
T@\"OS_dispatch_queue\",N,&
Tq,N,R
retain
T@\"NSArray\",N,R
registerForEvent:error:handler:
$__lazy_storage_$_singleFile
T@\"_DYSharedCache\",N,R
isMemberOfClass:
performSelector:withObject:
value
$__lazy_storage_$_images
T@\"NSString\",N,R
block
installname
performSelector:withObject:withObject:
address
aotUuid
hash
initWithCoder:
performSelector:
setQueue:
sharedCacheAtlasBuffer
withVMLayoutBytes:
T@\"NSDictionary\",N,C
getCurrentSnapshotAndReturnError:
withLocalSymbolData:
zone
$__lazy_storage_$_zerofill
T@\"NSString\",?,R,C
UTF8String
images
isEqualToString:
platform
rootPath
state
$__lazy_storage_$_sourceRange
code
environment
info
stringWithUTF8String:
zerofillExtension
TI,N,R
TQ,R
_sharedCache
count
init
systemSharedCaches
$__lazy_storage_$_memoryMap
T#,R
dataWithBytesNoCopy:length:freeWhenDone:
description
filePath
initWithBase64EncodedData:options:
initWithTask:queue:error:
subCaches
forceCacheScavenge
initWithBase64EncodedString:options:
initWithBytesNoCopy:length:freeWhenDone:
initWithData:error:
snapshotPreValidated
self
unregisterForEvent:
dealloc
$__lazy_storage_$_metrics
setSharedCache:
T@\"NSData\",N,R
impl
initWithBytes:length:
initWithInternal:
next
$__lazy_storage_$_localSymbolsFilePath
isProxy
notifierState
task
$__lazy_storage_$_sharedCacheRecord
T@\"NSString\",R,C
_sharedCacheUuid
aotImages
countByEnumeratingWithState:objects:count:
filePaths
sharedCache
cacheInfoLoaded
$__lazy_storage_$_sharedCacheSlide
notifierClients
Q16@0:8
v24@0:8@16
@32@0:8^@16@?24
@36@0:8I16^@20@?28
@40@0:8^v16q24@?32
@40@0:8@16Q24^@32
v16@0:8
@40@0:8:16@24@32
@20@0:8B16
B24@0:8@?16
@24@0:8:16
Vv16@0:8
@36@0:8^v16q24B32
B24@0:8@16
@24@0:8@16
@32@0:8@16^@24
C16@0:8
@24@0:8^@16
^v16@0:8
B24@0:8#16
B24@0:8@\"Protocol\"16
v8@?0
@16@0:8
B16@0:8
@36@0:8I16@20^@28
q16@0:8
@32@0:8@16Q24
#16@0:8
@32@0:8Q16Q24
i16@0:8
I16@0:8
@20@0:8I16
@32@0:8^v16q24
@32@0:8:16@24
B24@0:8:16
^{_NSZone=}16@0:8
@\"NSString\"16@0:8
```
