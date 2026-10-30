# `MTLGPUDebugVisibleFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsVisibleFunctionTable`
- Protocols: `MTLGPUDebugResource`
- 2 instance variables, 21 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _gpuIdentifier;
Q _stage;
```

## Properties

```
@property (T@"<MTLVisibleFunctionTable>",&,D,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugVisibleFunctionTable setBuffers:offsets:withRange:];
-[MTLGPUDebugVisibleFunctionTable setBuffer:offset:atIndex:];
-[MTLGPUDebugVisibleFunctionTable dealloc];
-[MTLGPUDebugVisibleFunctionTable gpuAddress];
-[MTLGPUDebugVisibleFunctionTable length];
-[MTLGPUDebugVisibleFunctionTable handleForOffset:];
-[MTLGPUDebugVisibleFunctionTable initWithVisibleFunctionTable:descriptor:computePipeline:];
-[MTLGPUDebugVisibleFunctionTable initWithVisibleFunctionTable:descriptor:device:];
-[MTLGPUDebugVisibleFunctionTable initWithVisibleFunctionTable:descriptor:renderPipeline:stage:];
-[MTLGPUDebugVisibleFunctionTable underlyingGPUAddress];
-[MTLGPUDebugVisibleFunctionTable useWithComputeEncoder:usage:];
-[MTLGPUDebugVisibleFunctionTable useWithRenderEncoder:usage:stages:];
```
