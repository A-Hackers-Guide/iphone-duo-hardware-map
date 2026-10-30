# `/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo`

iOS 27.2 dyld shared cache image. Version `491.0.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 5 classes, 0 protocols, 78 methods, 40 properties

### Class pages

Every class and protocol, with its methods: [`IOAccelMemoryInfo`](../objc/IOAccelMemoryInfo_IOAccelMemoryInfo.md), [`IOAccelMemoryMapInfo`](../objc/IOAccelMemoryMapInfo_IOAccelMemoryInfo.md), [`IOAccelMemoryOpenCLInfo`](../objc/IOAccelMemoryOpenCLInfo_IOAccelMemoryInfo.md), [`IOAccelMemoryOpenGLInfo`](../objc/IOAccelMemoryOpenGLInfo_IOAccelMemoryInfo.md), [`IOAccelMemoryPoolTotals`](../objc/IOAccelMemoryPoolTotals_IOAccelMemoryInfo.md)

### Classes

`IOAccelMemoryInfo`, `IOAccelMemoryMapInfo`, `IOAccelMemoryOpenCLInfo`, `IOAccelMemoryOpenGLInfo`, `IOAccelMemoryPoolTotals`

### Properties

```
@property (TQ,R) memoryPool;
@property (TQ,R) length;
@property (TQ,R) residentLength;
@property (TQ,R) dirtyLength;
@property (TB,R) wired;
@property (TB,R) cachedCopy;
@property (TB,R) cacheDirty;
@property (TB,R) purgeable;
@property (TB,R) orphaned;
@property (T@"NSArray",R) devices;
@property (TI,R) surfaceID;
@property (T@"NSSet",R) processIDs;
@property (T@"NSSet",R) blamedProcesses;
@property (T@"NSArray",R) mappings;
@property (T@"NSArray",R) openglObjects;
@property (T@"NSArray",R) openclObjects;
@property (T@"NSArray",R) formattedDescriptions;
@property (Ti,Vpid) pid;
@property (TQ,Vaddress) address;
@property (Ti,Vpid) pid;
@property (T@"NSString",&,Vcl_context) cl_context;
@property (TQ,Vcl_mem) cl_mem;
@property (T@"NSString",&,VobjectType) objectType;
@property (T@"NSString",&,VobjectDescription) objectDescription;
@property (Ti,Vpid) pid;
@property (T@"NSString",&,Vsharegroup) sharegroup;
@property (TQ,VobjectType) objectType;
@property (Ti,Vname) name;
@property (Ti,VblamedProcess) blamedProcess;
@property (T@"NSString",&,VobjectDescription) objectDescription;
@property (T@"NSString",&,VdebugLabel) debugLabel;
@property (T@"NSString",&,Vdevice_name) device_name;
@property (T@"NSString",&,Vpool) pool;
@property (TQ,VallocatedSize) allocatedSize;
@property (TQ,VresidentSize) residentSize;
@property (TQ,VwiredSize) wiredSize;
@property (TQ,VdirtySize) dirtySize;
@property (TQ,VpurgeableSize) purgeableSize;
@property (TQ,VnonpurgeableSize) nonpurgeableSize;
@property (TQ,VorphanedSize) orphanedSize;
```

## Strings (127)

```
-[IOAccelMemoryInfo memoryPool]
size
CachedCopy
IOAccelMemoryInfoProcessIDKey
)
, on behalf of %@
IOAccelMemory failed to collect data from %@: timeout (typically because the process is dead or sandboxed)
Payload
Error during purge: %@
createMergedEntry
insertPIDsIntoSet
v16@?0@\"NSObject<OS_xpc_object>\"8
+[IOAccelMemoryInfo newKernelAllocationList:]
Removable
-[IOAccelMemoryInfo openclObjects]
 (
+[IOAccelMemoryInfo collectDataWithCompletionQueue:completionBlock:]
produced_bytes != 0
ResponsiblePID
PerLevelDescription
TargetProcess
[devices_array count] == 1
IOAccelSurfaceWidth
IOServiceOpen failed for driver %@, 0x%08x
[value isKindOfClass: expected_type]
Renderbuffer
Type
%s.%d
IOAccelMemoryInfoIOKitDriverKey
IOAccelMemoryInfo.mm
(dirty_size != NULL) == (resident_size != NULL)
pid
Unknown
DirtySize
IOGPU
gpumemd request queue
Descriptions
false
OpenCLContext
IOAccelSurfaceID
+[IOAccelMemoryInfo newKernelAllocationTotals:totalsReturn:errorReturn:]
Resources
-[IOAccelMemoryInfo mappings]
Cached Copy
IOAccelSurfaceBufferIndex
insertEitherValue
IOAccelMemoryInfo: unexpected event received: %s\n
Timeout
new_mem
PID
Wired
%@@%llx%s
+[IOAccelMemoryInfo validateDictionary:]
Orphaned
mergeAllocationList
validateArray
v8@?0
IOAccelSurfacePixelFormat
failed to collect data from PID %@: %s
OpenGLObjects
0
Processes
[pid isKindOfClass: [NSNumber class]]
Failed to purge all vidmem, kr: %d\n
pid_num != 0
-[IOAccelMemoryInfo openglObjects]
Sharegroup
IOGraphicsAccelerator2
[array isKindOfClass: [NSArray class]]
[obj isKindOfClass: expected_type]
Label
[mempool isEqualToString:@\"VidMem\"] || [mempool isEqualToString:@\"SysMem\"]
Size
produced_bytes == required_size
-[IOAccelMemoryInfo length]
Purgeable
[found_values containsObject: obj] == FALSE
IOAccelSurfaceHeight
[process isKindOfClass: [NSDictionary class]]
Mappings
OSObject
vidmem
Dirty Cached Copy
%@, Context %@, %@ 0x%llx
ResidentSize
com.apple.gpumemd.client
Name
IOServiceGetMatchingServices failed, 0x%08x
IOSurfaceID
proc_pid
OpenCLObjects
kernel_allocations != NULL
IOAcceleratorES
Description
B32@?0@8Q16^B24
Unserialization failed for device %@
MemoryPool
VidMem
getDictForPID_block_invoke
IOConnect call failed for device %@: %x
CFGetTypeID(cf_alloc_array) == CFArrayGetTypeID()
 (%@)
(REMOVABLE)
AllocationIdentifiers
Unserialization failed for device %@: %@
sysmem
IOAccelMemoryInfoErrorDomain
Buffer
[observed_pids member: pid] == nil
%@ Sharegroup %@ %@ %d
Devices
Data not collected from driver %@, because it hasn't adopted the IOAcceleratorFamily-2 APIs
mempool
-[IOAccelMemoryInfo processIDs]
test_pid_num
Texture
end_count <= initial_count
mergeAllocationListByIOSurfaceID
Unknown Process.%d
, 
kr == KERN_SUCCESS
SysMem
PageoffRequired
OpenCLMem
[iosid_num isKindOfClass: [NSNumber class]]
pid_num
+[IOAccelMemoryInfo collectDataWithCompletionQueue:completionBlock:]_block_invoke_4
```
