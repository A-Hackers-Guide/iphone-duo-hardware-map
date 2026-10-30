# `MTLDebugResidencySet`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResidencySet`
- 1 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _accessStatus;
```

## Instance methods

```
-[MTLDebugResidencySet commit];
-[MTLDebugResidencySet allocatedSize];
-[MTLDebugResidencySet setCurrentGeneration:];
-[MTLDebugResidencySet currentGeneration];
-[MTLDebugResidencySet addAllocation:];
-[MTLDebugResidencySet removeAllocation:];
-[MTLDebugResidencySet allocationCount];
-[MTLDebugResidencySet addAllocations:count:];
-[MTLDebugResidencySet allAllocations];
-[MTLDebugResidencySet containsAllocation:];
-[MTLDebugResidencySet endResidency];
-[MTLDebugResidencySet removeAllAllocations];
-[MTLDebugResidencySet removeAllocations:count:];
-[MTLDebugResidencySet requestResidency];
-[MTLDebugResidencySet validateResource:];
-[MTLDebugResidencySet allCommittedAllocations];
-[MTLDebugResidencySet expiredGeneration];
-[MTLDebugResidencySet generationForAllocation:];
-[MTLDebugResidencySet setExpiredGeneration:];
-[MTLDebugResidencySet clearWriteBit];
-[MTLDebugResidencySet initWithResidencySet:device:];
-[MTLDebugResidencySet setWriteBit];
-[MTLDebugResidencySet validateAllocation:];
-[MTLDebugResidencySet validateHeap:];
```
