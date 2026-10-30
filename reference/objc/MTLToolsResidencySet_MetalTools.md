# `MTLToolsResidencySet`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLResidencySetSPI`
- 4 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _allocations;
^v _committedAllocations;
@"NSMutableSet" _pendingAdds;
@"NSMutableSet" _pendingRemoves;
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
-[MTLToolsResidencySet commit];
-[MTLToolsResidencySet label];
-[MTLToolsResidencySet allocatedSize];
-[MTLToolsResidencySet dealloc];
-[MTLToolsResidencySet setCurrentGeneration:];
-[MTLToolsResidencySet currentGeneration];
-[MTLToolsResidencySet addAllocation:];
-[MTLToolsResidencySet removeAllocation:];
-[MTLToolsResidencySet allocationCount];
-[MTLToolsResidencySet addAllocations:count:];
-[MTLToolsResidencySet allAllocations];
-[MTLToolsResidencySet containsAllocation:];
-[MTLToolsResidencySet endResidency];
-[MTLToolsResidencySet removeAllAllocations];
-[MTLToolsResidencySet removeAllocations:count:];
-[MTLToolsResidencySet requestResidency];
-[MTLToolsResidencySet initWithBaseObject:parent:];
-[MTLToolsResidencySet allCommittedAllocations];
-[MTLToolsResidencySet countForAllocation:];
-[MTLToolsResidencySet expiredGeneration];
-[MTLToolsResidencySet generationForAllocation:];
-[MTLToolsResidencySet setExpiredGeneration:];
```
