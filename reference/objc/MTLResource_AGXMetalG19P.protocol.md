# `MTLResource` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLAllocation`
- 0 instance variables, 9 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
```

## Instance methods

```
-[MTLResource resourceOptions];
-[MTLResource hazardTrackingMode];
-[MTLResource setOwnerWithIdentity:];
-[MTLResource cpuCacheMode];
-[MTLResource storageMode];
-[MTLResource device];
-[MTLResource label];
-[MTLResource setLabel:];
-[MTLResource allocatedSize];
-[MTLResource setPurgeableState:];
-[MTLResource heap];
-[MTLResource isAliasable];
-[MTLResource makeAliasable];
-[MTLResource heapOffset];
```
