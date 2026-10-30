# `MTLResidencySet` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (TQ,R) allocatedSize;
@property (T@"NSArray",R,C) allAllocations;
@property (TQ,R) allocationCount;
```

## Instance methods

```
-[MTLResidencySet commit];
-[MTLResidencySet device];
-[MTLResidencySet label];
-[MTLResidencySet allocatedSize];
-[MTLResidencySet addAllocation:];
-[MTLResidencySet removeAllocation:];
-[MTLResidencySet allocationCount];
-[MTLResidencySet addAllocations:count:];
-[MTLResidencySet allAllocations];
-[MTLResidencySet containsAllocation:];
-[MTLResidencySet endResidency];
-[MTLResidencySet removeAllAllocations];
-[MTLResidencySet removeAllocations:count:];
-[MTLResidencySet requestResidency];
```
