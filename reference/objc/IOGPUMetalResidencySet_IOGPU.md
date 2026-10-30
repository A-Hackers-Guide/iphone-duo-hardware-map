# `IOGPUMetalResidencySet`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLResidencySetSPI`
- 10 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
{IOGPUResourceInfo="iosurface"^{__IOSurface}"resourceSize"b56"iosurfaceField"b8"resourceID"I} _info;
Q _globalTraceObjectID;
Q _labelTraceID;
^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ^v[0Q]} _groupRef;
@"IOGPUMetalDevice<MTLDeviceSPI>" _device;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _evictsImmediately;
Q _currentGeneration;
Q _expiredGeneration;
{IOGPUGenerationalSet<id, IOGPUMTLIdKey, IOGPUMTLObjectHashAllocator>="m_keyTable"^{IOGPUMTLIdKey}"m_generationTable"^Q"m_hopInfo"^I"m_usedInfo"^Q"m_dirtyInfo"^Q"m_dirtyInfoH"^Q"m_hashSize"I"m_hashMask"I"m_usedMask"I"m_dirtyHMask"I"m_hashShift"I"m_count"I"m_dirtyCount"I"m_maxSize"I"m_allocatedSize"Q"m_currentGeneration"Q"m_expiredGeneration"Q"m_init"B} _hashTable;
```

## Properties

```
@property (T@"NSArray",?,R,C) allCommittedAllocations;
@property (TQ,?,N) currentGeneration;
@property (TQ,?,N) expiredGeneration;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (TQ,R) allocatedSize;
@property (T@"NSArray",R,C) allAllocations;
@property (TQ,R) allocationCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[IOGPUMetalResidencySet initWithDevice:descriptor:args:argsSize:];
-[IOGPUMetalResidencySet commit];
-[IOGPUMetalResidencySet device];
-[IOGPUMetalResidencySet allocatedSize];
-[IOGPUMetalResidencySet dealloc];
-[IOGPUMetalResidencySet setCurrentGeneration:];
-[IOGPUMetalResidencySet currentGeneration];
-[IOGPUMetalResidencySet addAllocation:];
-[IOGPUMetalResidencySet removeAllocation:];
-[IOGPUMetalResidencySet allocationCount];
-[IOGPUMetalResidencySet addAllocations:count:];
-[IOGPUMetalResidencySet allAllocations];
-[IOGPUMetalResidencySet containsAllocation:];
-[IOGPUMetalResidencySet endResidency];
-[IOGPUMetalResidencySet removeAllAllocations];
-[IOGPUMetalResidencySet removeAllocations:count:];
-[IOGPUMetalResidencySet requestResidency];
-[IOGPUMetalResidencySet _commitAddedAllocations:count:removedAllocations:count:];
-[IOGPUMetalResidencySet _commitAddedHeaps:count:removedHeaps:count:];
-[IOGPUMetalResidencySet _commitAddedResources:count:removedResources:count:];
-[IOGPUMetalResidencySet allCommittedAllocations];
-[IOGPUMetalResidencySet countForAllocation:];
-[IOGPUMetalResidencySet expiredGeneration];
-[IOGPUMetalResidencySet generationForAllocation:];
-[IOGPUMetalResidencySet setExpiredGeneration:];
```
