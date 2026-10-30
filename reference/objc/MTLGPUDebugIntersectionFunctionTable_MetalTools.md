# `MTLGPUDebugIntersectionFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIntersectionFunctionTable`
- Protocols: `MTLGPUDebugResource`
- 4 instance variables, 21 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _gpuIdentifier;
@"MTLGPUDebugComputePipelineState" _computePipelineState;
@"MTLGPUDebugRenderPipelineState" _renderPipelineState;
Q _stage;
```

## Properties

```
@property (T@"<MTLIntersectionFunctionTable>",&,D,N) baseObject;
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
-[MTLGPUDebugIntersectionFunctionTable dealloc];
-[MTLGPUDebugIntersectionFunctionTable length];
-[MTLGPUDebugIntersectionFunctionTable setFunctions:withRange:];
-[MTLGPUDebugIntersectionFunctionTable handleForOffset:];
-[MTLGPUDebugIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:];
-[MTLGPUDebugIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:computePipelineState:];
-[MTLGPUDebugIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:renderPipelineState:stage:];
-[MTLGPUDebugIntersectionFunctionTable underlyingGPUAddress];
-[MTLGPUDebugIntersectionFunctionTable useWithComputeEncoder:usage:];
-[MTLGPUDebugIntersectionFunctionTable useWithRenderEncoder:usage:stages:];
```
