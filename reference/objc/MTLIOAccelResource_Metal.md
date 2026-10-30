# `MTLIOAccelResource`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLResource`
- Protocols: `MTLResourceSPI`
- 4 instance variables, 23 properties, 40 instance methods, 0 class methods

## Instance variables

```
{_MTLIOAccelResource="vendor"(?="reserved"[4Q])"info"{IOAccelResourceInfo="iosurface"^{__IOSurface}"resourceSize"b56"iosurfaceField"b8"resourceID"I}"sharedAllocationUniqueId"Q"cachedAllocationUniqueId"Q"gpuAddress"Q"device"@"MTLIOAccelDevice<MTLDevice>""label"@"NSString""globalTraceObjectID"Q"labelTraceID"Q"resourceRef"^{__IOAccelResource}"clientSharedRO"^{IOAccelClientSharedRO}"clientSharedRW"^{IOAccelClientSharedRW}"virtualAddress"^v"options"Q"storageMode"Q"cpuCacheMode"Q"responsibleProcess"i"purgeableState"Q"purgeableAllowed"B"sharedAllocationInfo"@"MTLResourceAllocationInfo""cachedAllocationInfo"@"MTLResourceAllocationInfo""heap"@"MTLIOAccelHeap""resource"@"MTLIOAccelResource""offset"Q"length"Q"pinned"B"labelLock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _res;
@"MTLIOAccelResource" next;
@"MTLIOAccelResource" prev;
Q uniqueId;
```

## Properties

```
@property (T^{__IOAccelResource=},R) resourceRef;
@property (T^v,R,N) virtualAddress;
@property (TQ,R,N) gpuAddress;
@property (TI,R,N) resourceID;
@property (TQ,R,N) resourceSize;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (TQ,R) allocatedSize;
@property (TQ,R) protectionOptions;
@property (TQ,R) heapOffset;
@property (TQ,R) allocationID;
@property (TQ,R) gpuHandle;
@property (Ti) responsibleProcess;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLIOAccelResource resourceOptions];
-[MTLIOAccelResource isComplete];
-[MTLIOAccelResource hazardTrackingMode];
-[MTLIOAccelResource copyAnnotations];
-[MTLIOAccelResource setOwnerWithIdentity:];
-[MTLIOAccelResource cpuCacheMode];
-[MTLIOAccelResource storageMode];
-[MTLIOAccelResource unfilteredResourceOptions];
-[MTLIOAccelResource protectionOptions];
-[MTLIOAccelResource device];
-[MTLIOAccelResource label];
-[MTLIOAccelResource setLabel:];
-[MTLIOAccelResource allocatedSize];
-[MTLIOAccelResource dealloc];
-[MTLIOAccelResource gpuAddress];
-[MTLIOAccelResource waitUntilComplete];
-[MTLIOAccelResource gpuHandle];
-[MTLIOAccelResource setPurgeableState:];
-[MTLIOAccelResource heap];
-[MTLIOAccelResource isAliasable];
-[MTLIOAccelResource virtualAddress];
-[MTLIOAccelResource makeAliasable];
-[MTLIOAccelResource isPurgeable];
-[MTLIOAccelResource initWithResource:];
-[MTLIOAccelResource heapOffset];
-[MTLIOAccelResource setResponsibleProcess:];
-[MTLIOAccelResource resourceID];
-[MTLIOAccelResource allocationID];
-[MTLIOAccelResource annotateResource:];
-[MTLIOAccelResource copyAnnotationDictionary:obj_key_name:obj_dict:];
-[MTLIOAccelResource doesAliasAllResources:count:];
-[MTLIOAccelResource doesAliasAnyResources:count:];
-[MTLIOAccelResource doesAliasResource:];
-[MTLIOAccelResource initMemoryless:descriptor:];
-[MTLIOAccelResource initStandinWithDevice:];
-[MTLIOAccelResource initWithDevice:options:args:argsSize:];
-[MTLIOAccelResource resourceRef];
-[MTLIOAccelResource resourceSize];
-[MTLIOAccelResource responsibleProcess];
-[MTLIOAccelResource retainedLabel];
```
