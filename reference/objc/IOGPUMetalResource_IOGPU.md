# `IOGPUMetalResource`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLResource`
- Protocols: `MTLResourceSPI`
- 6 instance variables, 24 properties, 44 instance methods, 0 class methods

## Instance variables

```
{_IOGPUMetalResource="vendor"(?="reserved"[4Q])"info"{IOGPUResourceInfo="iosurface"^{__IOSurface}"resourceSize"b56"iosurfaceField"b8"resourceID"I}"sharedAllocationUniqueId"Q"cachedAllocationUniqueId"Q"gpuAddress"Q"device"@"IOGPUMetalDevice<MTLDevice>""label"@"NSString""globalTraceObjectID"Q"labelTraceID"Q"resourceRef"^{__IOGPUResource}"clientSharedRO"^{IOGPUClientSharedRO}"virtualAddress"^v"options"Q"storageMode"Q"cpuCacheMode"Q"responsibleProcess"i"purgeableState"Q"purgeableAllowed"B"heap"@"IOGPUMetalHeap""resource"@"IOGPUMetalResource""offset"Q"length"Q"pinned"B"labelLock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"metadataVirtualAddress"^v} _res;
@"IOGPUMetalResource" next;
@"IOGPUMetalResource" prev;
Q uniqueId;
@"IOGPUMetalResource" weakSelf;
@ attachedResourceInfoTraceEmitter;
```

## Properties

```
@property (T^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ^v[0Q]},R) resourceRef;
@property (T^v,R,N) virtualAddress;
@property (T^v,R,N) metadataVirtualAddress;
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
@property (T@,W,N,VattachedResourceInfoTraceEmitter) attachedResourceInfoTraceEmitter;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
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
-[IOGPUMetalResource resourceOptions];
-[IOGPUMetalResource isComplete];
-[IOGPUMetalResource hazardTrackingMode];
-[IOGPUMetalResource copyAnnotations];
-[IOGPUMetalResource setOwnerWithIdentity:];
-[IOGPUMetalResource cpuCacheMode];
-[IOGPUMetalResource emitResourceInfoTraceEvent];
-[IOGPUMetalResource _setLabel:];
-[IOGPUMetalResource storageMode];
-[IOGPUMetalResource unfilteredResourceOptions];
-[IOGPUMetalResource protectionOptions];
-[IOGPUMetalResource device];
-[IOGPUMetalResource label];
-[IOGPUMetalResource setLabel:];
-[IOGPUMetalResource allocatedSize];
-[IOGPUMetalResource dealloc];
-[IOGPUMetalResource gpuAddress];
-[IOGPUMetalResource waitUntilComplete];
-[IOGPUMetalResource setPurgeableState:];
-[IOGPUMetalResource heap];
-[IOGPUMetalResource isAliasable];
-[IOGPUMetalResource virtualAddress];
-[IOGPUMetalResource makeAliasable];
-[IOGPUMetalResource isPurgeable];
-[IOGPUMetalResource initWithResource:];
-[IOGPUMetalResource heapOffset];
-[IOGPUMetalResource setResponsibleProcess:];
-[IOGPUMetalResource resourceID];
-[IOGPUMetalResource allocationID];
-[IOGPUMetalResource annotateResource:];
-[IOGPUMetalResource copyAnnotationDictionary:obj_key_name:obj_dict:];
-[IOGPUMetalResource doesAliasAllResources:count:];
-[IOGPUMetalResource doesAliasAnyResources:count:];
-[IOGPUMetalResource doesAliasResource:];
-[IOGPUMetalResource initMemoryless:descriptor:];
-[IOGPUMetalResource initStandinWithDevice:];
-[IOGPUMetalResource initWithDevice:options:args:argsSize:];
-[IOGPUMetalResource resourceRef];
-[IOGPUMetalResource resourceSize];
-[IOGPUMetalResource responsibleProcess];
-[IOGPUMetalResource retainedLabel];
-[IOGPUMetalResource attachedResourceInfoTraceEmitter];
-[IOGPUMetalResource metadataVirtualAddress];
-[IOGPUMetalResource setAttachedResourceInfoTraceEmitter:];
```
