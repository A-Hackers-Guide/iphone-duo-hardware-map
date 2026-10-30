# `MTLHeapSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLHeap`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R) unfilteredResourceOptions;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R,N) protectionOptions;
@property (TQ,R,N) memoryPoolId;
```

## Instance methods

```
-[MTLHeapSPI memoryPoolId];
-[MTLHeapSPI unfilteredResourceOptions];
-[MTLHeapSPI newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLHeapSPI formattedDescription:];
-[MTLHeapSPI newAccelerationStructureWithSize:resourceIndex:];
-[MTLHeapSPI detachBacking];
-[MTLHeapSPI replaceBackingWithRanges:readOnly:];
-[MTLHeapSPI protectionOptions];
-[MTLHeapSPI gpuAddress];
```
